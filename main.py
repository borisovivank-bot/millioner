print ("привет, приветствую вас на игре 'Победи миллион'!")
questions = [
    "Кто открыл электричество?",
    "Кто был первым президентом Америки"
]
print(questions[1])

answers = [
    ["Бенджамин Франклин", "Томас Эдисон", "Никола Тесла", "Альберт Эйнштейн"],
    ["Дональд Трамп", "Джордж Вашингтон", "Пейтон Рэндольф", "Джефферсон Дэвис"]
]

right_answers = [
    "1",
    "2"
    ]
for print(questions[1])i in range(1, len(answers)+1):
    print(f"{i}. {answers[i-1]}")


user_answer = input("ведите ответ:")
if  user_answer==right_answers:
    print("Верно!")

