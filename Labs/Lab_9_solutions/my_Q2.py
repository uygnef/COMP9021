from array_stack import *
s = input('input expression:')
List = []
reading_number = False
for c in s:
    if c.isdigit():
        if reading_number:
            number = number*10+int(c)
        else:
            reading_number = True
            number = int(c)
    else:
        if reading_number:
            List.append(number)
            reading_number = False
        if c in '+-*/()[]{}':
            List.append(c)
        elif c != ' ':
            raise ValueError

if reading_number:
    List.append(number)
    reading_number = False

stack = ArrayStack()

for token in List:
    if token in list('+-*/([{') or isinstance(token,int):
       stack.push(token)
    else:
        try:
            first_element = stack.pop()
            operator = stack.pop()
            second_element = stack.pop()
            group_symbol = stack.pop()
            if token == ')' and group_symbol != '(' or \
               token == '}' and group_symbol != '{' or \
               token == ']' and group_symbol != '[':
                raise   Exception
        except:
            print('Incorrect expression')
        if operator == '+':
            stack.push(first_element + second_element)
        elif operator == '-':
            stack.push(second_element - first_element)
        elif operator == '*':
            stack.push(first_element * second_element)
        elif operator == '/' and first_element:
            stack.push(second_element / first_element)
        else:
            raise ValueError('can not divided by 0')


if stack.is_empty():
    print('wrong')
    raise ValueError
print('The result is:',stack.pop())
if not stack.is_empty():
    raise ValueError('wrong')
