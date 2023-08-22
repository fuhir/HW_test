import unittest

from accounting import command_l_list, command_a_add, command_d_delete


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def test_command_l_list(self):
        etalon = ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"',
                  'insurance "10006" "Аристарх Павлов"']
        result = command_l_list(self.documents)
        self.assertEqual(etalon, result)

    def test_command_a_add(self):
        doc_number = '555444'
        doc_type = 'drive_license'
        name_in_doc = 'Вася Пупкин'
        shell_number = '3'
        etalon = 'Добавление выполнено успешно'
        result = command_a_add(self.documents, self.directories, doc_number, doc_type, name_in_doc, shell_number)
        self.assertEqual(etalon, result)

    def test_command_d_delete(self):
        doc_number = '10006'
        etalon = 'Удаление выполнено успешно.'
        result = command_d_delete(self.documents, self.directories, doc_number)
        self.assertEqual(etalon, result)

if __name__ == "__main__":
    unittest.main()