#Практическое задание по теме "Переменные."

#кол-во выполненных домашних заданий
homeworks_completed = 12

#кол-во часов, затраченных на выполнение домашних заданий
hours_spent_on_homeworks = 1.5

#название курса
name_of_course = "Python"

#время, затраченное на одно задание,
time_for_one_homework = hours_spent_on_homeworks / homeworks_completed

print(f"Курс: {name_of_course}\n"
      f"Выполнено заданий: {homeworks_completed} заданий\n"
      f"Затраченно часов: {hours_spent_on_homeworks} часа\n"
      f"Среднее время, затраченное на одно задание: {time_for_one_homework} часа "
      f"({time_for_one_homework * 60} минут)")