from dataclasses import dataclass


@dataclass
class message_text:
    start = (
        "Привет! Меня зовут VosayBot и я стану твоим незаменимым помошником в общении.\n\n"
        "Группа новостей бота: @vosaynews\n"
        "Команда помошник: /help\n"
        "Помочь в разработке: /donate\n\n"
        "Жми /voices и начинай погружение в мир voice-стикеров!"
    )
    bots_are_not_allowed = "Ботам вход запрещен!"
    select_category = "Выберите категорию!"
    voices_not_found = (
        "К сожалению, для данной категории нет голосовых сообщений. "
        "Используйте команду /start для выхода в меню или обратитесь в поддержку!"
    )
    my_voices_not_found = (
        "Вы не сохранили ни одного голосового сообщения! "
        "Используйте команду /start, чтобы просмотреть все доступные голосовые."
    )
    delete_account_step_one = (
        "Ваш аккаунт и все сохранённые сообщения будут удалены! Вы уверены, что хотите продолжить?"
    )
    delete_account_step_two = (
        "Ваш аккаунт и все сохранённые сообщения удалены! Можете очистить и удалить чат с ботом.\n\n"
        "*Предупреждение*: При попытке использовать бота в любом из режимов аккаунт будет создан автоматически.\n\n"
        "Надеюсь мы еще увидимся!😇"
    )
    help = (
        "Список доступных команд:\n"
        "/start - Запуск бота\n"
        "/voices - Показать voice-паки\n"
        "/my_voices - Список сохранённых голосовых\n"
        "/delete_account - Удаление аккаунта\n"
        "/donate - Помочь в разработке\n\n"
        "Возможности inline режима:\n"
        "my - Список сохранённых голосовых"
    )
    donate = (
        "Спасибо, что ты используешь VosayBot! Поддержать разработчика можно следующими способами:\n"
        "Monero: `47bDCeAvB2nh3aAcmBXetD2uYSCDZTgru8kZEVLT5XJgX2eHhuJafYpVHNYkoms112Mbpnv6NsYARJXTbEzjSVsvG1m6aja`"
    )


@dataclass
class callback_text:
    menu = "Меню"
    back = "Назад"
    delete_account = "Удалить аккаунт"
    save_voice_button = "💾"
    delete_voice_button = "❌"


@dataclass
class callback_data_prefix:
    save_voice = "sv_"
    delete_voice = "dl_"
    show_categories = "show_categories"
    show_subcategory = "sh_sc_"
    show_voice = "sh_v_"
    show_my_voices = "my_voices"


mt = message_text
ct = callback_text
cdp = callback_data_prefix

__all__ = ["mt", "ct", "cdp"]
