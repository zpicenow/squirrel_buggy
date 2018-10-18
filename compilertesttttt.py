import copy


# 输入输入序列w 和预测分析表M ,非终结符的集合N ，终结符的集合T 开始进行预测分析
def prediction_analyze(w, M, N, T):
    mat = "步骤{:<15}\t栈内容 {:<20}\t当前输入 {:<30}\t动作{:<30}\t描述 {:<20}"
    print(mat.format(" ", " ", " ", " ", " ", ))
    Stack = list()  # 创建符号栈
    Stack.append('#')  # 压入结束表示符#
    Stack.append(N[0])  # 压入开始符，即非终结符的集合N的第一个元素
    top = len(Stack) - 1  # top用于记录栈顶的下标，即最后一个元素下标
    ip = 0  # 用于记录输入序列w中的终结符的下标，从首部开始
    step = 1  # 记录步骤
    # 当栈非空
    while Stack:
        content = ''.join(Stack)  # 将栈内容转为字符串
        inputchar = ''.join(w[ip:])
        action = ""
        des = ""
        a = w[ip]  # a用于获取到当前输入符号
        x = Stack[top]  # x用于获取栈顶的元素
        if x in T:  # 如果栈顶元素为终结符，判断是否匹配
            if x == a:  # 如果匹配到终结符
                if Stack[-1] == '#' and a == '#':
                    mat = "{:<20}\t {:<25}\t {:<30}\t {:<40}\t{:<20}"
                    print(mat.format(step, content, inputchar, " ", "正确结束"))

                    break
                action = "pop(" + x + "), next(ip)"
                des = "匹配" + x
                Stack.pop()  # 弹出栈顶元素
                top -= 1
                ip += 1  # 指向w的下一个字符
            else:
                print("出错！栈顶终结符不匹配。")
                return False
        else:  # 如果栈顶元素为非终结符，查表展开产生式
            xIndex = N.index(x)  # 获取x在N中的下标，方便查表
            if a in M[xIndex]:  # 如果M[X,a]不为空
                result = copy.deepcopy(M[xIndex][a])  # 得到产生式的右侧（格式为list）
                action = "pop(" + x + "), push(" + ''.join(result) + ")"
                des = "按" + x + "->" + ''.join(result) + "展开"

                Stack.pop()  # 弹出栈顶元素
                top -= 1
                if result[0] == 'n':  # 如果为n，无需push
                    action = "pop(" + x + ")       "
                else:
                    # 将展开结果取反序压入栈中
                    result.reverse()
                    for j in range(0, len(result)):
                        Stack.append(result[j])
                        top += 1

            else:
                print("出错！产生式不匹配。")
                return False

        # 输出本次执行情况
        mat = "{:<20}\t {:<25}\t {:<30}\t {:<30}\t{:<20}"
        print(mat.format(step, content, inputchar, action, des))
        step += 1  # 步骤数加1 继续循环


if __name__ == '__main__':
    print("---------即将开始收集数据，请按提示操作---------' ")

    print("请输入文法G的非终结符的集合N , 输入格式为List , 如['L' , 'E' , 'rE' , 'T' , 'rT' , 'F'] ")
    N = eval(input(":"))
    # # #print( N)
    print("请输入文法G的终结符的集合T , 输入格式为List , 如['id' , 'num' , '+' , '-' , '* ', '/ ', 'mod' , '(' , ')' , '; ', '#'] ")
    T = eval(input(":"))
    # # print(T) #预测表： [{'id' : ['E', ';' , 'L'] ,       'num' : ['E', ';' , 'L'],      '(' : ['E', ';' , 'L'],
    # '#' : ['n']} ,{'id' : ['T', 'rE'] ,       'num' : ['T', 'rE'] ,     '(' : ['T', 'rE'] } ,{'+' : ['+' , 'T' ,
    # 'rE'] ,      '-' : ['-' , 'T' ,  'rE'] ,       ')' : ['n'] ,       ';' : ['n'] } ,{'id' : ['F' , 'rT'] ,
    # 'num' : ['F' , 'rT'] ,       '(' : ['F' , 'rT'] } ,{'+' : ['n'] ,      '-' : ['n'] ,     '*' : ['*' , 'F',
    # 'rT'] ,     '/' : ['/' , 'F', 'rT'] ,     'mod' : ['mod' , 'F', 'rT'] ,       ')' : ['n'] ,       ';' : ['n']}
    # ,{'id' : ['id'] ,      'num' : ['num'] ,       '(' : ['(', 'E' , ')'] }  ]
    print("请输入文法G的预测表M , 输入格式如{'id' : ['id'] ,      'num' : ['num'] ,       '(' : ['(', 'E' , ')'] }  ] ")
    # "[{'id' : ['E', ';' , 'L'] ,       'num' : ['E', ';' , 'L'],      '(' : ['E', ';' , 'L'],     '#' : ['n']} ,
    # \n " "{'id' : ['T', 'rE'] ,       'num' : ['T', 'rE'] ,     '(' : ['T', 'rE'] } ,  \n " "{'+' : ['+' , 'T' ,
    # 'rE'] ,      '-' : ['-' , 'T' ,  'rE'] ,       ')' : ['n'] ,       ';' : ['n'] } ,  \n " "{'id' : ['F' ,
    # 'rT'] ,      'num' : ['F' , 'rT'] ,       '(' : ['F' , 'rT'] } ,   \n" "{'+' : ['n'] ,      '-' : ['n'] ,
    # '*' : ['*' , 'F', 'rT'] ,     '/' : ['/' , 'F', 'rT'] ,     'mod' : ['mod' , 'F', 'rT'] ,       ')' : ['n'] ,
    #      ';' : ['n']} ,   \n" "{'id' : ['id'] ,      'num' : ['num'] ,       '(' : ['(', 'E' , ')'] }  ] ")
    M = eval(input(":"))

    # #print(M) print("---------收集数据完成，请按提示操作---------' ") N =['L' , 'E' , 'rE' , 'T' , 'rT' , 'F'] T = ['id' ,
    # 'num' , '+' , '-' , '*', '/ ', 'mod' , '(' , ')' , ';', '#'] M = [{'id' : ['E', ';' , 'L'] ,
    # 'num' : ['E', ';' , 'L'],      '(' : ['E', ';' , 'L'],     '#' : ['n']} , {'id' : ['T', 'rE'] ,
    # 'num' : ['T', 'rE'] ,     '(' : ['T', 'rE'] } , {'+' : ['+' , 'T' ,  'rE'] ,      '-' : ['-' , 'T' ,  'rE'] ,
    #      ')' : ['n'] ,       ';' : ['n'] } , {'id' : ['F' , 'rT'] ,      'num' : ['F' , 'rT'] ,       '(' : ['F' ,
    # 'rT'] } , {'+' : ['n'] ,      '-' : ['n'] ,     '*' : ['*' , 'F', 'rT'] ,     '/' : ['/' , 'F', 'rT'] ,
    # 'mod' : ['mod' , 'F', 'rT'] ,       ')' : ['n'] ,       ';' : ['n']} , {'id' : ['id'] ,      'num' : ['num'] ,
    #       '(' : ['(', 'E' , ')'] }  ]
    while True:
        w = eval(input('请输入要分析的序列w（以#号结束）：'))
        # w = ['id' , '+' , 'id' , '*' , 'id' , ';' , '#']
        print(
            "----------------------------------------------------分析过程----------------------------------------------------")
        prediction_analyze(w, M, N, T)  # 开始进行预测分析
        print(
            "----------------------------------------------------分析结束----------------------------------------------------")
        break
