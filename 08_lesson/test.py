class Test:
    def test(self):
        return "бяка"

    def test2(self):
        print(self.test())


player = Test()
player.test2()