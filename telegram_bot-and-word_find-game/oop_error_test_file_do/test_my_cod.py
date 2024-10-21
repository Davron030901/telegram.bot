# import unittest
# from name import get_full_name
#
# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('alijon','valiyev',"")
#         self.assertEqual(formatted_name, 'Alijon  Valiyev')
# if __name__ == '__main__':
#     unittest.main()
#
# import unittest
# from name import get_full_name
#
# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('alijon','valiyev')
#         self.assertEqual(formatted_name, 'Alijon Valiyev') #Aynan teng ==
#     def test_toliq_ism_otasi(self):
#         name = get_full_name('hasan','husanov','olimovich')
#         self.assertEqual(name,'Hasan Olimovich Husanov')
#
# if __name__ == '__main__':
#     unittest.main()


# import unittest
# from circle import getArea, getPerimeter
#
#
# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertAlmostEqual(getArea(10), 314.159,3)#3 xonagacha aynnan tengligi
#         self.assertAlmostEqual(getArea(3), 28.27431)
#
#     def test_perimeter(self):
#         self.assertAlmostEqual(getPerimeter(10), 62.8318)
#         self.assertAlmostEqual(getPerimeter(4), 25.13272)
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest
from tubSonmi import tubSonmi


class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))

    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))


if __name__ == '__main__':
    unittest.main()