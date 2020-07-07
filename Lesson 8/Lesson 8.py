from random import randint, sample
from termcolor import colored


class Card:
    def __init__(self, card_type):
        self.card_type = card_type
        self.values = {}  # для хранения чисел карточки и их позиции внутри карточки
        self.values_in_card = []  # заполненная карточка
        self.fill_card()

    def __str__(self):
        card_name = 'Ваша карточка' if self.card_type == 'human' else 'Карточка компьютера'
        header_length = 46
        length1 = (header_length - len(card_name)) // 2
        length2 = (header_length - len(card_name)) % 2
        card_str = '-' * length1 + card_name + '-' * (length1 + length2) + '\n|'
        card_str += '|\n|'.join(['|'.join(
            [' ' + (colored("%2d" % el, 'green') if self.values.get(el)[2] else "%2d" % el) + ' ' if el != 0 else '    '
             for el in row]) for row in
            self.values_in_card]) + '|\n'
        card_str += '-' * header_length
        return card_str

    def fill_card(self):
        values = sample(range(1, 91), 15)
        for i in range(0, 3):
            i_values = values[i * 5:(i + 1) * 5]
            i_values.sort()
            for ind, el in enumerate(sample(range(0, 6), 4)):
                i_values.insert(el + ind, 0)
            # Сделал словарь {номер_бочёнка: (ряд, позиция, бочёнок_вышел)}.
            # Такая структура не пригодилась, можно было сделать проще, но переделывать не захотел.
            self.values.update({pos: [i, i_values.index(pos), False] for pos in i_values if pos != 0})
            self.values_in_card.append(i_values)

    def save_keg_and_return_kegover(self, keg):
        if self.values.get(keg) != None:
            self.values.get(keg)[2] = True
        return len([el for el in self.values.values() if not el[2]]) == 0


class Player:
    def __init__(self, player_type):
        self.player_type = player_type
        self.card = Card(player_type)


class LotoGame:
    def __init__(self, player_human, player_computer):
        self.player_human = player_human
        self.player_computer = player_computer
        self.dropped_kegs = []

    def start(self):
        for ind, el in enumerate(sample(range(1, 91), 90)):
            print()
            print(
                f'Новый бочонок {str(el)}, осталось {89 - ind} (вышли следующие: {", ".join(str(i) for i in self.dropped_kegs)})')
            print(player_human.card)
            print(player_computer.card)

            player_answer = input('Зачеркнуть цифру? (y/n) ')
            if player_answer == 'y' and self.player_human.card.values.get(el) == None:
                print(f'Бочонок {str(el)} отсутствует в Вашей карточке. Вы програли.')
                break
            elif player_answer == 'n' and self.player_human.card.values.get(el) != None:
                print(f'Бочонок {str(el)} был в Вашей карточке. Вы програли.')
                break
            elif player_answer != 'y' and player_answer != 'n':
                print(f'Введён некорректный ответ "{player_answer}". Вы програли.')
                break

            self.dropped_kegs.append(el)

            player_kegs_over = self.player_human.card.save_keg_and_return_kegover(el)
            computer_kegs_over = self.player_computer.card.save_keg_and_return_kegover(el)
            if player_kegs_over and computer_kegs_over:
                print()
                print('Вы и компьютер одновременно закончили игру')
                break
            elif player_kegs_over:
                print()
                print('Вы первым закончили игру. Вы победили!')
                break
            elif computer_kegs_over:
                print()
                print('Компьютер первым закончил игру. Вы проиграли.')
                break


# Не пойму, как сделать перечёркнутый текст
# def strike(text):
#     # return ''.join([u'\u0336{}'.format(c) for c in text])
#     return '\u0336'.join(text) + '\u0336'
#
# print(strike('this should do the trick'))


player_human = Player('human')
player_computer = Player('computer')

game = LotoGame(player_human, player_computer)
game.start()
