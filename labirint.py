from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
questions_list = []

questions_list.append(Question("Бродяги, нищие, уголовные элементы и другие асоциальные личности – как назвать их одним словом?", "Люмпены", "Истеблишмент", "Маргиналы", "Бомонд"))
questions_list.append(Question('Как называлось дружеское общество петербургской молодежи в 1819-1820 годах, в числе членов которого были декабристы Глинка, Толстой и Каверин?', "Зеленая лампа", "Справедливость", "Союз спасения", "Могучая кучка"))
questions_list.append(Question('Какое слово написано правильно?',"Аккордеон", "Котарсис", "Дименция", "Лобировать"))
questions_list.append(Question('Все персонажи из этого списка – из одного произведения, кроме одного.', "Клотильда де Марель", "Эпонина", "Гаврош", "Жавер"))
questions_list.append(Question('Взрослые никогда ничего не понимают сами, а для детей очень утомительно без конца им все объяснять и растолковывать” – откуда цитата?', "Маленький принц", "Королевство кривых зеркал", "Питер пэн", "Алиса в стране чудес"))
questions_list.append(Question('В какой стране находится город Лиссабон?', "Португалия", "Венгрия", "Исландия", "Италия"))
questions_list.append(Question('Что значит “Veni, vidi, vici”?', 'Пришел, увидел, победил', 'Свобода, равенство, братство', 'Первый, второй, третий', 'Люблю, любим и буду любить'))
questions_list.append(Question('Как написать это заковыристое слово правильно?', 'Скрупулёзный', 'Скурпуллёзный', 'Скруппулёзный', 'Скурпулёзный'))
questions_list.append(Question('Кто произнес знаменитую речь под названием «У меня есть мечта»?', 'Мартин Лютер Кинг', 'Франклин Рузвельт', 'Стив Джобс', 'Уинстон Черчилль'))
questions_list.append(Question('В каком из этих фильмов не играла Вивьен Ли?', '“Забавная мордашка”', '“Трамвай "Желание”', '“Леди Гамильтон”', '“Мост Ватерлоо”'))


window = QWidget()
window.setWindowTitle('Carrot')
bth_OK = QPushButton('Ответить')


lb_Question=QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
rbth_1 = QRadioButton('Энцы')
rbth_2 = QRadioButton('Смурфы')
rbth_3 = QRadioButton('Чулымцы')
rbth_4 = QRadioButton('Алеуты')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()


layout_ans2.addWidget(rbth_1)
layout_ans2.addWidget(rbth_2)
layout_ans3.addWidget(rbth_3)
layout_ans3.addWidget(rbth_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(bth_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbth_1)
RadioGroup.addButton(rbth_2)
RadioGroup.addButton(rbth_3)
RadioGroup.addButton(rbth_4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    bth_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    bth_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbth_1.setChecked(False)
    rbth_2.setChecked(False)
    rbth_3.setChecked(False)
    rbth_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == bth_OK.text():
        show_result()
    else:
        show_question()

answers = [rbth_1, rbth_2, rbth_3, rbth_4 ]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов', window.score)
        print('Рейтинг', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг', (window.score/window.total*100), '%')

def next_question():
    '''window.cur_question = window.cur_question + 1'''
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    '''if cur_question >= len(questions_list):
       window.cur_question = 0'''
    ask(q)
    
def click_OK():
    if bth_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
'''
q=Question('Как звали попугая из мультика "Кеша?"', 'Кеша', 'Кот', 'Dog', 'Артем')'''
'''bth_OK.clicked.connect(check_answer)'''
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = -1
bth_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()

window.show()

app.exec()
