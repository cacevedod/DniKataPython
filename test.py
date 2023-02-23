import unittest
from main import Dni

class TestDni(unittest.TestCase):
    dni = Dni()

    def test_dni11111111A_Fail(self):
        resp = self.dni.construir("11111111A")
        self.assertEqual(resp, False)
    
    def test_longiudEsMenor9Fail(self):
        resp = self.dni.construir("1111")
        self.assertEqual(resp, False)

    def test_longiudEs10EntoncesFail(self):
        resp = self.dni.construir("1111111111")
        self.assertEqual(resp, False)

    def test_dni11111111P_OK(self):
        resp = self.dni.construir("11111111P")
        self.assertEqual(resp, True)

    def test_dni11112222N_OK(self):
        resp = self.dni.construir("11112222N")
        self.assertEqual(resp, True)

    def test_dni99999999A_OK(self):
        resp = self.dni.construir("99999999A")
        self.assertEqual(resp, True)

    def test_dni99999999R_Fail(self):
        resp = self.dni.construir("99999999R")
        self.assertEqual(resp, False)

if __name__ == '__main__':
    unittest.main()