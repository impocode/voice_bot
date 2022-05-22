from urllib.parse import quote

from sqlalchemy import func, select
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.utils import (
    MAX_PAGES,
    MAX_VOICES,
    build_page_buttons,
    check_user,
    ct,
    delete_previous_messages,
    mt
)
from models import user_model, user_voice_model, voice_model
from settings import database, settings


@check_user
@delete_previous_messages
def show_my_voices(update: Update, context: CallbackContext) -> None:
    if update.callback_query and update.callback_query.data.startswith("my_voices"):
        current_page = int(update.callback_query.data.replace("my_voices_", ""))
    elif update.callback_query and update.callback_query.data.startswith("d_m"):
        current_page = int(update.callback_query.data[3])
    else:
        current_page = 1

    user_uuid_subq = (
        user_model.select()
        .with_only_columns(user_model.c.uuid)
        .where(user_model.c.telegram_id == update.effective_user.id)
        .scalar_subquery()
    )
    count_voices = database.execute(
        select(func.count("*"))
        .select_from(voice_model)
        .join(user_voice_model, voice_model.c.uuid == user_voice_model.c.voice_uuid, isouter=True)
        .where(user_voice_model.c.user_uuid == user_uuid_subq)
    ).scalar()
    voices_query = (
        voice_model.select()
        .with_only_columns(
            voice_model.c.uuid, voice_model.c.path, voice_model.c.title, voice_model.c.performer
        )
        .join(user_voice_model, voice_model.c.uuid == user_voice_model.c.voice_uuid, isouter=True)
        .where(user_voice_model.c.user_uuid == user_uuid_subq)
        .order_by(voice_model.c.created_at)
        .offset((MAX_PAGES * current_page) - MAX_PAGES)
        .limit(MAX_VOICES)
    )

    page_buttons = build_page_buttons(
        current_page=current_page,
        count_voices=count_voices,
        category="my",
        subcategory="voices",
    )

    if voices := database.execute(voices_query).all():
        voices_message_id, delete_voices_buttons = [], []
        for index, voice in enumerate(voices, start=1):
            delete_voices_buttons.append(
                InlineKeyboardButton(
                    ct.delete_voice_button, callback_data=f"d_m{current_page}_{voice['uuid']}"
                )
            )
            if index == len(voices):
                reply_markup = InlineKeyboardMarkup(
                    [
                        page_buttons,
                        delete_voices_buttons,
                        [InlineKeyboardButton(ct.menu, callback_data="show_menu")],
                    ],
                )
            else:
                reply_markup = None

            if update.message:
                res = update.message.reply_voice(
                    f"{settings.voice_url}/{settings.telegram_token}/assets/{quote(voice['path'])}",
                    reply_markup=reply_markup,
                    quote=False,
                )
            else:
                res = update.callback_query.message.reply_voice(
                    f"{settings.voice_url}/{settings.telegram_token}/assets/{quote(voice['path'])}",
                    reply_markup=reply_markup,
                    quote=False,
                )
            voices_message_id.append(res.message_id)

        context.user_data["voices_message_id"] = voices_message_id
    else:
        if update.message:
            update.message.reply_text(mt.my_voices_not_found)
        else:
            if current_page > 1:
                update.callback_query.data = f"my_voices_{current_page - 1}"
                show_my_voices(update=update, context=context)
            else:
                update.callback_query.message.reply_text(mt.my_voices_not_found)


__all__ = ["show_my_voices"]
