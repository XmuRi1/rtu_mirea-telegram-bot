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
    "⁉️") + "* Часто задаваемые вопросы* " + " - \"/questions\" ." "\n" + emoji.emojize(
    ":bookmark_tabs:") + "* Интересный факт* " + " - \"/fact\" ." "\n" + emoji.emojize(
    ":technologist:") + "* Связаться с разработчиками* " + " - \"/develop\" ." "\n" + " " + "\n" + emoji.emojize(
    ":fire:") + " Выберите нужную задачу!"

# Текст с симптомами COVID-19:
TEXT_SYMPTOMS = emoji.emojize(
    "🤕") + " Симптомы COVID-19." + "\n" + " " + "\n" + "*Часто наблюдаемые симптомы: *" + "\n" + " • повышение температуры;" \
                + "\n" + " • кашель;" + "\n" + " • утомляемость;" + "\n" + " • потеря обоняния и вкусовых ощущений." + "\n" \
                + " " + "\n" + "*У некоторых инфицированных могут также наблюдаться:*" + "\n" + " • боль в горле;" + "\n" \
                + " • головная боль;" + "\n" + " • различные другие болевые ощущения;" + "\n" + " • диарея;" + "\n" \
                + " • сыпь на коже или изменение цвета кожи на пальцах рук или ног;" + "\n" + " • покраснение или раздражение глаз." + "\n" \
                + " " + "\n" + "*Симптомы тяжелой формы заболевания:*" + "\n" + " • затрудненное дыхание или одышка;" + "\n" \
                + " • нарушение речи или двигательных функций или спутанность сознания;" + "\n" + " • боль в грудной клетке;" + "\n" + " " + "\n" \
                + "Если у вас наблюдаются симптомы тяжелой формы заболевания, незамедлительно обратитесь за медицинской помощью. " \
                + "Прежде чем посещать клинику или больницу, позвоните и предупредите о своем визите." + "\n" + " " + "\n" \
                + "Людям, у которых наблюдаются умеренно выраженные симптомы и нет других заболеваний, " \
                + "рекомендуется симптоматическое лечение в домашних условиях." + "\n" + " " + "\n" \
                + "В среднем проходит 5–6 дней между моментом инфицирования и появлением симптомов, " \
                + "однако в некоторых случаях данный период может занимать до 14 дней." + "\n" + " " + "\n" \
                + "*Эта информация предоставлена исключительно для справки. Обратитесь к врачу за консультацией.*"

# Текст с профилактикой COVID-19:
TEXT_PREVENTION = emoji.emojize(
    "😷") + " Профилактика COVID-19. " + "\n" + " " + "\n" \
                  + "Чтобы защитить себя и окружающих, пользуйтесь проверенной информацией о болезни и " \
                  + "принимайте необходимые меры профилактики. Следуйте рекомендациям местных органов здравоохранения." \
                  + "\n" + " " + "\n" + "*Чтобы предупредить распространение COVID-19:*" + "\n" \
                  + " • Держитесь на безопасном расстоянии от людей (не менее 1 метра), даже если они не кажутся заболевшими." + "\n" \
                  + " • Носите маску в общественных местах, особенно в закрытых помещениях и там, где соблюдать безопасную дистанцию невозможно." + "\n" \
                  + " • При кашле или чихании прикрывайте рот и нос локтевым сгибом или платком." + "\n" \
                  + " • Сделайте прививку, когда подойдет ваша очередь. Следуйте местным рекомендациям по вакцинации." + "\n" + " " + "\n" \
                  + "Если у вас повысится температура, появится кашель и одышка, обратитесь за медицинской помощью. " \
                  + "Чем раньше вы это сделаете, тем быстрее вас направят к нужному врачу." + "\n" + " " + "\n" \
                  + "Надев маску, вы поможете предотвратить передачу вируса от себя другим людям. " \
                  + "Одних только масок для защиты от вируса, вызывающего COVID-19, недостаточно. " \
                  + "Также следует соблюдать безопасную дистанцию и правила гигиены рук." + "\n" + " " + "\n" \
                  + "*Эта информация предоставлена исключительно для справки. Обратитесь к врачу за консультацией.*"

# Текст со связью с разработчиками COVID-19:
TEXT_DEVELOP = emoji.emojize(
    ":technologist:") + " Разработчики бота \"COVID-19\". " + "\n" + " " + "\n" \
               + "При возникновении каких-либо вопросов и предложений - свяжитесь с разработчиками данного бота: " \
               + "\n" + " " + "\n" \
               + " • [Александр Чекунков](https://t.me/cdr_chknkv)" + "\n" \
               + " • [Яков Цинкерман](https://t.me/XmuRi1)" + "\n" + " " + "\n" + "Спасибо Вам за то, " \
               + "что заинтересовались нашей работой! Надеемся данный бот помог Вам. Следите за своим здоровьем!"

# Текст с сообщением о ошибке:
TEXT_ERROR_MESSAGE = emoji.emojize("❗") + "Ошибка! Бот не видит такой команды!"
