# 基础类型
Base_Type = ["int", "char", "float", "double"]
# 特殊符号
Special_Symbol = ["(", ")", "[", "]", "*", "const", "volatile", ","]
Compara_Array = Base_Type + Special_Symbol

Input_String = ""
Input_Array = []
Array_Point = 0
# 数据结构堆栈
Stack_Array = []
Stack_Point = 0
# 专门用于处理参数的堆栈
Function_Parameter_Stack_Array = []


# 读取变量的声明，并将其分解为后续程序可执行的列表结构
def declaration_analysis(string):
    global Input_String
    global Input_Array
    compara_succeess_flag = 0
    Input_String = str(string)

    # 去除内部空格" "
    Input_String = Input_String.strip(" ")

    if Input_String == "":
        return

    # 分割声明中的各种符号
    for i in Compara_Array:
        # 如果匹配成功，则删除匹配中的字符串并且加入数组中
        if Input_String.startswith(i):
            # 加入数组
            Input_Array.append(i)
            # 删除匹配字符串
            Input_String = Input_String.lstrip(i)
            # 表示匹配成功
            compara_succeess_flag = 1
            break

    # 匹配不成功,表明为未知变量
    if compara_succeess_flag == 0:
        true_item = len(Input_String)
        for i in Compara_Array:
            item = Input_String.find(i)
            if item >= 0:
                true_item = min(true_item, item)

        Input_Array.append(Input_String[:true_item])
        Input_String = Input_String.lstrip(Input_String[:true_item])

    # 递归调用
    declaration_analysis(Input_String)

    return


def find_the_right_parenthesis(item):
    global Input_Array
    paranthesis_number = 1
    point = item + 1
    while True:
        if Input_Array[point] == "(":
            paranthesis_number += 1
        elif Input_Array[point] == ")":
            paranthesis_number -= 1
            if paranthesis_number == 0:
                break

        point += 1

    return point


def value_right_dealing():
    # TODO 需要改为临时变量，并且这些数据有参数传递尽量，方便进行迭代
    global Array_Point
    global Stack_Array
    global Stack_Point
    # 将输入列表导入数据到stack并且停止在第一个未知数据
    for Array_Point in range(len(Input_Array)):
        Stack_Array.append(Input_Array[Array_Point])

        if Input_Array[Array_Point] in Compara_Array:
            pass
        else:
            print("Find the unknown value:", Input_Array[Array_Point])
            Stack_Point = Array_Point
            break

    # while True:
    if Input_Array[Array_Point + 1] == "(":
        print("The next value is: '('")
        right_parenthesis = find_the_right_parenthesis(Array_Point + 1)
        print("The left and right parenthesis position:%d, %d" % (Array_Point + 1, right_parenthesis))
        temp = Input_Array[(Array_Point + 2):right_parenthesis]
        print(temp)
    elif Input_Array[Array_Point + 1] == "[":
        if Input_Array[Array_Point + 2] != "]":
            print("该变量是一个长度为:", Input_Array[Array_Point + 2], "的数组")
            Array_Point += 3
        else:
            print("该变量是一个长度未知的数组")
            Array_Point += 2
    else:
        pass


if __name__ == "__main__":
    # declaration_analysis("const char *(* c[10])(int **p, char * (*fp)(void b))")
    declaration_analysis("const char * (func(char* time, void *p))")
    print(Input_Array)
    value_right_dealing()
    while True:
        pass
