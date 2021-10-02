from StagePytest.calculator import Calcuator


class TestCs:
    def test_cs(self):
        pass


class TestCalculator:
    def setup_class(self):
        self.cal = Calcuator()

    def setup(self):
        print("=" * 50)

    def test_add(self):
        result = self.cal.add(5, 4)
        print(result)
        assert result == 9

    def test_sub(self):
        result = self.cal.sub(10, 5)
        print(result)
        assert result == 5

    def test_div(self):
        result = self.cal.div(10, 5)
        print(result)
        assert result == 2

    def test_mul(self):
        result = self.cal.mul(2, 5)
        print(result)
        assert result == 10
