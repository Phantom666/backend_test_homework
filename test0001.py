class Hello:
    x: str  # Если здесь не указывать тип переменной,
    # аннотация для x не отобразится в словаре __annotations__,
    # однако анализатор возьмёт аннотацию из __init__ и корректно отработает

    def __init__(self, x: str = "Привет") -> None:
        self.x = x


# Вывод на экран словаря __annotations__ из области видимости класса Hello
print(Hello.__annotations__)
