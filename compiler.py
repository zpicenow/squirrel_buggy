import pandas as pd

# 带同步记号的预测分析表
data = {'id': ['E→TE\'', '', 'T→FT\'', '', 'F→id'],
        '+': ['', 'E\'→+TE\'', 't', 'T\'→ε', 't'],
        '*': ['', '', '', 'T\'→*FT\'', 't'],
        '(': ['E→TE\'', '', 'T→FT\'', '', 'F→(E)'],
        ')': ['t', 'E\'→ε', 't', 'T\'→ε', 't'],
        '#': ['t', 'E\'→ε', 't', 'T\'→ε', 't']}
frame = pd.DataFrame(data, index=['E', 'E\'', 'T', 'T\'', 'F'])
stk = "#E"  # 用字符串模拟栈
ahead = ""  # 当前正待处理的输入记号
sub = ""  # 当前待处理记号被处理后的输入


def nextToken():  # 获取下一个词法记号
    global sub
    if sub[0:2] == "id":
        sub = sub[2:]
        return "id"
    else:
        s = sub[0:1]
        sub = sub[1:]
        return s


def empty():  # 栈是否为空
    if len(stk) == 0:
        return True
    return False


def top():  # 获取栈顶元素
    global stk
    if stk[-1:] == '\'' or stk[-1:] == 'd':
        return stk[-2:]
    else:
        return stk[-1:]


def pop():  # 弹出栈顶元素
    global stk
    if stk[-1:] == '\'' or stk[-1:] == 'd':
        stk = stk[:-2]
    else:
        stk = stk[:-1]


def push(s):  # 产生式→右边的逆序入栈
    global stk
    while s[-1:] != '→':
        if s[-1:] == '\'' or s[-1:] == 'd':
            stk += s[-2:]
            s = s[0:-2]
        else:
            stk += s[-1:]
            s = s[0:-1]


def handle(top, head):  # 预测分析程序
    global ahead
    if top == head:
        if head != '#':  # 不用输出 匹配 #
            print('匹配', head)
        ahead = nextToken()
        pop()
    else:
        s = frame[head][top]  # 从预测分析表中获取产生式
        if s == '':  # 出错，跳过当前记号
            ahead = nextToken()
        elif s == 't':  # 出错，在该非终结符的同步记号集合中，无需跳过任何记号，该终结符被弹出
            pop()
        else:
            print(s)
            pop()
            if s[-1:] != 'ε':  # 对于产生空串的产生式，只需弹栈，不需入栈
                push(s)


if __name__ == '__main__':
    print('____________________________')
    sub = input()
    print('____________________________')
    sub += '#'
    ahead = nextToken()
    while not empty():  # 当栈不为空时
        t = top()  # 获取栈顶元素
        handle(t, ahead)  # 调用预测分析程序
    print('____________________________')
