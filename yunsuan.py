import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

while True:

    op1 = input('请输入第一个运算数（必须是数字）：')
    if not is_number(op1):
        print('抱歉，您第一个运算数输入错误')
        sys.exit(1)

    op = input('请输入运算符（必须是+，-，*，/，^）：')
    if not ((op == '+') or (op == '-') or (op == '*') or (op == '/') or (op == '^')):
       print('抱歉，您运算符输入错误')
       sys.exit(1)
    op2 = input('请输入第二个运算数（必须是数字）：')
    if not is_number(op2):
        print('抱歉，您第二个运算数输入错误')
        sys.exit(1)

    #op1 = float(op1)
    #op2 = float(op2)


    if (op == '+'):
        #print(op1 + '+' + op2 + '=' + str(float(op1) + float(op2)))
        print(op1 + '+' + op2 + '=' + '%.3f' % (float(op1) + float(op2)))
    elif (op == '-'):
        #print(op1 + '-' + op2 + '=' + str(float(op1) - float(op2)))
        print(op1 + '-' + op2 + '=' + '%.3f' % (float(op1) - float(op2)))
    elif (op == '*'):
        #print(op1 + '*' + op2 + '=' + str(float(op1) * float(op2)))
        print(op1 + '*' + op2 + '=' + '%.3f' % (float(op1) * float(op2)))
    elif (op == '/' ):
        if (op2 == 0):
            print('抱歉，您输入错误(除数不能为0)')
            sys.exit(1)
        else:
            #print(op1 + '/' + op2 + '=' + str(float(op1) / float(op2)))
            print(op1 + '/' + op2 + '=' + '%.3f' % (float(op1) / float(op2)))
    elif (op == '^'):
        #print(op1 + '^' + op2 + '=' + str(float(op1) ** float(op2)))
        print(op1 + '^' + op2 + '=' + '%.3f' % (float(op1) ** float(op2)))

        
        


