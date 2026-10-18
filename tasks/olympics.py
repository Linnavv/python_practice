"""
Программа определяет, попал ли результат участника
в тройку лучших результатов олимпиады.
"""

def check_winners(scores, studentscore):
    """
    Проверяет, входит ли результат участника
    в тройку лучших результатов.

    scores — список результатов всех участников.
    studentscore — результат проверяемого участника.
    """
    sorted_scores = sorted(scores, reverse=True)
    top_three = sorted_scores[:3]

    if studentscore in top_three:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

scores = [20, 48, 52, 38, 36, 13, 7, 41]

check_winners(scores, 48)
check_winners(scores, 20)
