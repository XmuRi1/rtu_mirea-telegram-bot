import emoji

# Данный скрипт хранит в себе переменные со всеми строками, которые используются для работы бота.

# Текст с "приветственным сообщением":
START_MESSAGE = emoji.emojize(":handshake:") + " Добрый день! " + "\n" + emoji.emojize(
    "🦠") + " Данный бот расскажет Вам всю самую нужную информацию о COVID-19. " + "\n" + emoji.emojize(
    ":package:") + " В случае возникновения вопросов или предложений - свяжитесь с разработчиками. " + "\n" + emoji.emojize(
    ":woman_health_worker:") + " Не болейте!"

# Текст для вывода задач:
TEXT_BUTTON_TASKS = "Посмотреть доступные задачи " + emoji.emojize(":card_index_dividers:")

# Текст с доступными задачами:
TEXT_TASKS = emoji.emojize(
    ":card_index_dividers:") + " Доступные задачи на данный момент: " + "\n" + " " + "\n" + emoji.emojize(
    ":bar_chart:") + "* Посмотреть статистику*" + " - \"/stat\" ." + "\n" + emoji.emojize(
    "🤕") + "* Симптомы*" + " - \"/symptoms\" ." + "\n" + emoji.emojize(
    "😷") + "* Профилактика*" + " - \"/prevention\" ." "\n" + emoji.emojize(
    "⁉") + "* Часто задаваемые вопросы* " + " - \"/questions\" ." "\n" + emoji.emojize(
    ":technologist:") + "* Связаться с разработчиками* " + " - \"/develop\" ." "\n" + " " + "\n" + emoji.emojize(
    ":fire:") + " Выберите нужную задачу!"

# Текст с сообщением о ошибке:
TEXT_ERROR_MESSAGE = emoji.emojize("❗") + "Ошибка! Бот не видит такой команды!"
