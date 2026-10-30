"""Лабораторная работа №4. Выбор вида кофе для гостя."""


RULES = (
    ({"milk": "no", "volume": "small"}, "Эспрессо"),
    ({"milk": "no", "volume": "large"}, "Американо"),
    ({"milk": "yes", "foam": "much"}, "Капучино"),
    ({"milk": "yes", "foam": "little"}, "Латте"),
)


def ask_choice(question, options):
    """Получить один из предложенных ответов пользователя."""
    print(question)
    for number, (label, value) in enumerate(options, start=1):
        print(f"{number}. {label}")

    while True:
        answer = input("Ваш выбор: ").strip()
        for number, (label, value) in enumerate(options, start=1):
            if answer == str(number):
                return value
        print("Введите номер одного из предложенных вариантов.")


def infer(facts):
    """Перебрать правила ЕСЛИ–ТО и вернуть подходящую рекомендацию."""
    for conditions, recommendation in RULES:
        if all(facts.get(key) == value for key, value in conditions.items()):
            return recommendation
    return None


def main():
    print("Экспертная система: выбор вида кофе для гостя")
    facts = {
        "milk": ask_choice(
            "Хотите кофе с молоком?",
            (("Да", "yes"), ("Нет", "no")),
        )
    }

    if facts["milk"] == "no":
        facts["volume"] = ask_choice(
            "Какой объём чёрного кофе предпочитаете?",
            (("Маленький", "small"), ("Большой", "large")),
        )
    else:
        facts["foam"] = ask_choice(
            "Сколько молочной пены предпочитаете?",
            (("Много", "much"), ("Мало", "little")),
        )

    recommendation = infer(facts)
    if recommendation is None:
        print("Для введённых фактов подходящее правило не найдено.")
    else:
        print(f"Рекомендация: {recommendation}.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nДиалог завершён.")
