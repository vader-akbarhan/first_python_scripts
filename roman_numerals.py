# Work in progress

def get_roman_value(value):
    pass


def get_decimal_value(value):
    pass


class Number:
    def __init__(self, value):
        if type(value) is str:
            self._roman_value = value
            self._decimal_value = get_decimal_value(value)
        elif type(value) is int:
            self._decimal_value = value
            self._roman_value = get_roman_value(value)
        else:
            raise Exception("Unsupported value for Number()")


    @property
    def roman_value(self):
        return self._roman_value

    @roman_value.setter
    def roman_value(self, value):
        self._roman_value = value
        self._decimal_value = get_decimal_value(value)

    @roman_value.deleter
    def roman_value(self):
        del self._roman_value
        del self._decimal_value


    @property
    def decimal_value(self):
        return self._decimal_value

    @decimal_value.setter
    def decimal_value(self, value):
        self._decimal_value = value
        self._roman_value = get_roman_value(value)

    @decimal_value.deleter
    def decimal_value(self):
        del self._decimal_value
        del self._roman_value


if __name__ == "__main__":
    first_number = Number("VIII")
    second_number = Number(10)

    assert first_number.decimal_value == 8
    assert first_number.roman_value == "VIII"
    
    assert second_number.decimal_value == 10
    assert second_number.roman_value == "X"


    first_number.decimal_value = 26
    assert first_number.decimal_value == 26    
    assert first_number.roman_value == "XXVI"

    second_number.roman_value = "XLII"    
    assert second_number.decimal_value == 42
    assert second_number.roman_value == "XLII"


    print("Everything works fine.")
