class StaticVariable:
    val = 0
    def __init__(self, v):
        StaticVariable.val = v



if __name__ == '__main__':
    StaticVariable1 = StaticVariable(1)
    StaticVariable2 = StaticVariable(2)
    StaticVariable3 = StaticVariable(3)
    StaticVariable4 = StaticVariable(4)
    print(StaticVariable1.val)
    print(StaticVariable2.val)
    print(StaticVariable3.val)
    print(StaticVariable4.val)
    print(StaticVariable.val)