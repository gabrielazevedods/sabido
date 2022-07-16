from django.test import TestCase
from curso.models import Curso


class CursoTestCase(TestCase):
    


    def setUp(self):
        Curso.objects.create(
        nome = "sistemas de informação",
        instituicao = "ufrn"
        )

    def test_retorno_str(self):
        p1 = Curso.objects.get(nome="sistemas de informação")
        self.assertEquals(p1.__str__(), "sistemas de informação")
