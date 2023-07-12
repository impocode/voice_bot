from dataclasses import dataclass


@dataclass
class callback_text:
    menu = "Меню"
    back = "Назад"
    delete_account = "Удалить аккаунт"
    save_voice_button = "💾"
    delete_voice_button = "❌"


ct = callback_text


@dataclass
class callback_data_prefix:
    save_voice = "sv_"
    delete_voice = "dl_"
    show_categories = "show_categories"
    show_subcategory = "sh_sc_"
    show_voice = "sh_v_"
    show_popular = "popular"
    show_my_voices = "my_voices"


cdp = callback_data_prefix


@dataclass
class message_text:
    start = (
        "Привет! Меня зовут VosayBot и я стану твоим незаменимым помошником в общении.\n\n"
        "Группа новостей бота: @vosaynews\n"
        "Помощь: /help\n"
        "Помощь(расширенная): /help_advanced\n"
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
    popular_not_found = "Hic sunt dracones!"
    delete_account_step_one = (
        "Ваш аккаунт и все сохранённые сообщения будут удалены! Вы уверены, что хотите продолжить?"
    )
    delete_account_step_two = (
        "Ваш аккаунт и все сохранённые сообщения удалены! Можете очистить и удалить чат с ботом.\n\n"
        "*Предупреждение*: При попытке использовать бота в любом из режимов аккаунт будет создан автоматически.\n\n"
        "Надеюсь мы еще увидимся!😇"
    )
    donate = (
        "Спасибо, что ты используешь VosayBot! Поддержать разработчика можно следующими способами:\n"
        "Monero: `47bDCeAvB2nh3aAcmBXetD2uYSCDZTgru8kZEVLT5XJgX2eHhuJafYpVHNYkoms112Mbpnv6NsYARJXTbEzjSVsvG1m6aja`"
    )
    help = (
        "Список доступных команд:\n"
        "/start - Запуск бота\n"
        "/voices - Показать voice-паки\n"
        "/popular - Популярные voice-стикеры\n"
        "/my_voices - Список сохранённых голосовых\n"
        "/delete_account - Удаление аккаунта\n"
        "/help_advanced - Помощь(расширенная)\n"
        "/donate - Помочь в разработке\n\n"
        "Возможности inline режима:\n"
        "my - Список сохранённых голосовых"
    )
    help_advanced = (
        "*Сохранение и удаление голосовых сообщений:*\n\n"
        f"{ct.save_voice_button} - кнопка сохранения. Сохраняет голосове сообщение в базу пользователя, после нажатия меняется на кнопку {ct.delete_voice_button}.\n"
        f"{ct.delete_voice_button} - кнопка удаления. Удаляет голосове сообщение из базы пользователя, после нажатия меняется на кнопку {ct.save_voice_button}.\n\n"
        "*Управление голосовыми сообщениями:*\n\n"
        "Сохранённые сообщения можно легко просматривать/удалять вызвав команду: `my_voices`.\n"
        "Также сохранённые сообщения можно легко просматривать и отправлять в `inline` режиме написав в любом чате: `@vosaybot my`."
    )


mt = message_text

__all__ = ["ct", "cdp", "mt"]
