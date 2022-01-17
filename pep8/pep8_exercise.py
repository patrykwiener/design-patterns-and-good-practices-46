from typing import List

CONST = 'Ala ma kota'


def count_message_letters(message):
    count = 0
    for _ in message:
        count += 1
    return count


def modify_message_to_list(message: str) -> List[str]:
    return [letter + ' - ' + message for letter in message]


class SampleClass:
    some_const = 0

    def __init__(self):
        self.array = []

    def sample_method(self, item):
        return self.array.append(item)
