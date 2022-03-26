import time
import schedule
from src.covid_19_worker.BS_worker.statistic.world import world_statistic_creator
from src.covid_19_worker.BS_worker.statistic.russia import russia_statistic_creator
import emoji
from src.covid_19_worker.JSON_worker.question import questions_creator
from src.covid_19_worker.JSON_worker.fact import facts_creator
from src.covid_19_worker.JSON_worker.text import text_creator


# Данный скрипт собирает всю самую нужную информацию о COVID-19:

# Метод отправки статистики по миру и России:
def show_statistic(message, telebot, bot):
    buff_russia = "Россия " + emoji.emojize("🇷🇺")
    buff_world = "Мир " + emoji.emojize("🌎")
    buff_message = emoji.emojize(
        "📊") + " Выберите статистику нужного региона:"

    keyboard_statistic = telebot.types.InlineKeyboardMarkup()
    button_russia = telebot.types.InlineKeyboardButton(text=buff_russia,
                                                       callback_data="russia",
                                                       parse_mode="Markdown")
    button_world = telebot.types.InlineKeyboardButton(text=buff_world,
                                                      callback_data="world",
                                                      parse_mode="Markdown")

    keyboard_statistic.add(button_russia, button_world)
    bot.send_message(message.from_user.id, buff_message,
                     reply_markup=keyboard_statistic)


# Метод отправки новостей:
def show_news(message, telebot, bot):
    buff_google = "1️⃣ rbk.com"
    buff_interfax = "2️⃣ interfax.ru"
    buff_yandex = "3️⃣ yandex.ru"
    buff_message = emoji.emojize(
        "📑") + " Выберите сайт, новости которого хотите посмотреть:"

    keyboard_statistic = telebot.types.InlineKeyboardMarkup()
    button_google = telebot.types.InlineKeyboardButton(text=buff_google,
                                                       callback_data="rbk",
                                                       parse_mode="Markdown")
    keyboard_statistic.add(button_google)
    button_interfax = telebot.types.InlineKeyboardButton(text=buff_interfax,
                                                         callback_data="interfax",
                                                         parse_mode="Markdown")
    keyboard_statistic.add(button_interfax)
    button_yandex = telebot.types.InlineKeyboardButton(text=buff_yandex,
                                                       callback_data="yandex",
                                                       parse_mode="Markdown")
    keyboard_statistic.add(button_yandex)
    bot.send_message(message.from_user.id, buff_message,
                     reply_markup=keyboard_statistic)


# Метод отправки симптомов covid_19_worker:
def show_symptoms(message, bot):
    TEXT_SYMPTOMS = text_creator.get_text("symptoms")
    bot.send_message(message.from_user.id, TEXT_SYMPTOMS,
                     parse_mode="Markdown")


# Метод отправки профилактики covid_19_worker:
def show_prevention(message, bot):
    TEXT_PREVENTION = text_creator.get_text("prevention")
    bot.send_message(message.from_user.id, TEXT_PREVENTION,
                     parse_mode="Markdown")


# Метод вывода всех доступных вопросов:
def show_questions(message, telebot, bot):
    TEXT_QUESTIONS = questions_creator.questions_print()
    bot.send_message(message.from_user.id, TEXT_QUESTIONS,
                     parse_mode="Markdown")
    show_answers(message, telebot, bot)


# Метод вывода кнопок для получения ответа на определенный вопрос:
def show_answers(message, telebot, bot):
    buff_message = emoji.emojize(
        ":keyboard:") + " Для того, чтобы получить ответ на вопрос нажмите на нужную кнопку."
    keyboard_answers = telebot.types.InlineKeyboardMarkup()

    numbers = [1, 2, 3, 4, 5]
    for j in range(5):
        buff_button_one = telebot.types.InlineKeyboardButton(str(numbers[0]),
                                                             callback_data=str(
                                                                 numbers[0]),
                                                             parse_mode="Markdown")
        buff_button_two = telebot.types.InlineKeyboardButton(str(numbers[1]),
                                                             callback_data=str(
                                                                 numbers[1]),
                                                             parse_mode="Markdown")
        buff_button_three = telebot.types.InlineKeyboardButton(str(numbers[2]),
                                                               callback_data=str(
                                                                   numbers[2]),
                                                               parse_mode="Markdown")
        buff_button_four = telebot.types.InlineKeyboardButton(str(numbers[3]),
                                                              callback_data=str(
                                                                  numbers[3]),
                                                              parse_mode="Markdown")
        buff_button_five = telebot.types.InlineKeyboardButton(str(numbers[4]),
                                                              callback_data=str(
                                                                  numbers[4]),
                                                              parse_mode="Markdown")
        keyboard_answers.row(buff_button_one, buff_button_two,
                             buff_button_three, buff_button_four,
                             buff_button_five)

        for i in range(5):
            numbers[i] += 5

    bot.send_message(message.from_user.id, buff_message,
                     reply_markup=keyboard_answers)


# Метод вывода одного интересного факта:
def show_fact(message, bot):
    TEXT_FACT = facts_creator.facts_print()
    bot.send_message(message.from_user.id, TEXT_FACT, parse_mode="Markdown")


def show_bot_tasks(message, bot):
    TEXT_TASKS = text_creator.get_text("tasks")
    bot.send_message(message.from_user.id, TEXT_TASKS, parse_mode="Markdown")



