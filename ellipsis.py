#
# ellipsis.py (c) 2024 Rene Oudeweg
#
# ellipsis numbers calculator
#

from antlr4 import *
import readline
from fractions import Fraction
from dist.SimpleArithmeticLexer import SimpleArithmeticLexer
from dist.SimpleArithmeticParser import SimpleArithmeticParser
from termcolor import colored

MAXRANGE = 20


def multiply_with_carry(num1, num2):   
    # Determine the sign of the numbers
    sign1 = 1 if num1[0] != '-' else -1
    sign2 = 1 if num2[0] != '-' else -1
    if sign1 == -1:
        num1 = num1[1:]
    if sign2 == -1:
        num2 = num2[1:]

    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        carry = 0
        for j in range(len(num2) - 1, -1, -1):
            temp = result[i + j + 1] + int(num1[i]) * int(num2[j]) + carry
            result[i + j + 1] = temp % 10
            carry = temp // 10
        #debug(f"DEBUG: {result}")
        if carry != 0:
            result[i] += carry

    if len(result)>=MAXRANGE:
        result = result[1:]
    # Remove leading zeros
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    # Add the sign back to the result
    result[0] *= sign1 * sign2
    return ''.join(map(str, result))


def divide_with_remainder(dividend, divisor):
    # Determine the sign of the numbers
    sign_dividend = 1 if dividend[0] != '-' else -1
    sign_divisor = 1 if divisor[0] != '-' else -1

    if sign_dividend== -1:
        dividend = dividend[1:]
    if sign_divisor == -1:
        divisor = divisor[1:]
    dividend = list(map(int, str(dividend)))
    divisor = int(divisor)
    # Initialize variables
    quotient = []
    remainder = 0
    # Perform long division
    for digit in dividend:
        current_value = digit + remainder * 10
        current_quotient = current_value // divisor
        remainder = current_value % divisor
        quotient.append(current_quotient)
    quotient = quotient[next((i for i, x in enumerate(quotient) if x != 0), len(quotient)):] or [0]
    return ''.join(map(str, quotient)), remainder

def subtract(minuend_str, subtrahend_str):
    result = []
    sign = 1  # 1 for positive, -1 for negative

    # Determine sign based on the values of minuend and subtrahend
    if int(minuend_str) < int(subtrahend_str):
        minuend_str, subtrahend_str = subtrahend_str, minuend_str
        sign = -1

    borrow = 0
    length = max(len(minuend_str), len(subtrahend_str))
    minuend_str = minuend_str.zfill(length)
    subtrahend_str = subtrahend_str.zfill(length)
    for min_digit, sub_digit in zip(minuend_str[::-1], subtrahend_str[::-1]):
        min_value = int(min_digit)
        sub_value = int(sub_digit)

        diff = min_value - sub_value - borrow

        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0

        result.append(str(diff))

    # Reverse the result and apply the sign
    result_str = ''.join(result[::-1])
    return str(sign * int(result_str))


def subtract_with_borrow_bug(num1, num2):
    result = []
    borrow = 0

    # Determine the sign of the numbers
    sign1 = 1 if num1[0] != '-' else -1
    sign2 = 1 if num2[0] != '-' else -1
    if sign1 == -1:
        num1 = num1[1:]
    if sign2 == -1:
        num2 = num2[1:]

    # Make the lengths of num1 and num2 equal by adding leading zeros
    length = max(len(num1), len(num2))
    num1 = num1.zfill(length)
    num2 = num2.zfill(length)
    for i in range(length - 1, -1, -1):
        digit_diff = sign1 * int(num1[i]) - sign2 * int(num2[i]) - borrow
        if digit_diff < 0:
            result.insert(0, 10 + digit_diff)
            borrow = 1
        else:
            result.insert(0, digit_diff)
            borrow = 0
    # Remove leading zeros
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    # Add the sign back to the result
    result[0] *= sign1
    return ''.join(map(str, result))

def add_with_carry(num1, num2):
    result = []
    carry = 0
    # Determine the sign of the numbers
    sign1 = 1 if num1[0] != '-' else -1
    sign2 = 1 if num2[0] != '-' else -1
    if sign1 == -1:
        num1 = num1[1:]
    if sign2 == -1:
        num2 = num2[1:]

    # Make the lengths of num1 and num2 equal by adding leading zeros
    length = max(len(num1), len(num2))
    num1 = num1.zfill(length)
    num2 = num2.zfill(length)
    for i in range(length - 1, -1, -1):
        digit_sum = sign1 * int(num1[i]) + sign2 * int(num2[i]) + carry
        if digit_sum < 0:
            result.insert(0, 10 + digit_sum)
            carry = -1
        else:
            result.insert(0, digit_sum)
            carry = digit_sum // 10
    # Handle carry for the leftmost digit
    if carry < 0:
        result.insert(0, carry)
    # Remove leading zeros
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    # Add the sign back to the result
    result[0] *= sign1
    return ''.join(map(str, result))

def are_all_digits_same(input_str):
    # Check if all characters in the string are digits
    if not input_str.isdigit():
        return False
    # Check if all digits are the same
    return all(char == input_str[0] for char in input_str)

class ArithmeticVisitor(ParseTreeVisitor):

    def visitStart(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3:  # expr '+' term
            left = self.visit(ctx.expr())
            right = self.visit(ctx.term())
            if ctx.getChild(1).symbol.text == '++':
                if ctx.term().factor().NINT()!=None:
                    return str(int(left) + int(right)) 
                return add_with_carry(left,right)           
            if ctx.getChild(1).symbol.text == '--':
                if ctx.term().factor().NINT()!=None:
                    return str(int(left) - int(right)) 
                return subtract(left,right)           
            
        return self.visit(ctx.term())

    def visitTerm(self, ctx):
        if ctx.getChildCount() == 3:  # term '*' factor
            left = self.visit(ctx.term())        
            right = self.visit(ctx.factor())
            if ctx.getChild(1).symbol.text == '*':
                if ctx.term().factor().NINT()!=None:
                    return str(int(left) * int(right)) 
                return multiply_with_carry(left,right)
            if ctx.getChild(1).symbol.text == '/':
                if ctx.term().factor().NINT()!=None:
                    return str(int(left) / int(right)) 
                return divide_with_remainder(left,right)
        if ctx.getChildCount() == 2:  
            left = self.visit(ctx.term())        
            return left
        else:  # factor
            return self.visit(ctx.factor())

    def visitFactor(self, ctx):
        global MAXRANGE
        if ctx.getChildCount() == 1:  # INT
            if ctx.INT() != None:
                return ctx.INT().getText()
            if ctx.NINT() != None:
                return ctx.NINT().getText()
            if ctx.EINT() != None:
                sn = ''
                #if ctx.EINT().getText()[4:5]=='9':
                #    if are_all_digits_same(ctx.EINT().getText()[4:]):
                #        sn = '-1'
                #        return sn
                for x in range(0,MAXRANGE-len(ctx.EINT().getText()[4:])):
                    sn += ctx.EINT().getText()[3]
                sn += ctx.EINT().getText()[4:]
                #frac = parse_recurring_10adic_number(ctx.EINT().getText())
                return sn
            if ctx.EPINT() != None:
                sn = ''
                eplen = len(ctx.EPINT().getText())-3
                x = int(MAXRANGE / eplen)
                for x in range(0, x):
                    sn += ctx.EPINT().getText()[3:]
                return sn
        else:  # '(' expr ')'
            return self.visit(ctx.expr())

def read_input():
    # Read input from the user
    user_input = input(colored("Ellipsis calc>: ", 'red'))
    return user_input

def add_to_history(command):
    readline.add_history(command)

def get_previous_history():
    try:
        return readline.get_history_item(readline.get_current_history_length() - 1)
    except IndexError:
        return ""

def get_next_history():
    try:
        return readline.get_history_item(readline.get_current_history_length() + 1)
    except IndexError:
        return ""
    
def parse_recurring_10adic_number(number_str):
    # Split the input into the part before and after the ellipsis
    parts = number_str.split("...")
    # If there is a part after the ellipsis, treat it as the recurring part
    if len(parts) == 2:
        before_ellipsis, recurring_part = parts
    else:
        # If no ellipsis, consider the entire string as the part before
        before_ellipsis, recurring_part = parts[0], ""
    # Parse the part before the ellipsis
    if len(before_ellipsis):
        value = int(before_ellipsis)
    else:
        value = 0

    # If there is a recurring part, calculate the corresponding fraction
    if recurring_part:
        recurring_length = len(recurring_part)
        denominator = 10 ** len(before_ellipsis) * (10 ** recurring_length - 1)
        numerator = int(recurring_part) + value * (10 ** recurring_length - 1)
        return Fraction(numerator, denominator)
    
    return value

# Example usage:
#ten_adic_number_str = "...123456"
#ten_adic_number_value = parse_recurring_10adic_number(ten_adic_number_str)
#print(f"The 10-adic number represented by '{ten_adic_number_str}' is: {ten_adic_number_value}")

def printhelp():
     print("\n\nellipsis.py 0.1 (c) 2024 Rene Oudeweg \n\nExamples:\n" 
           " 1 ++ 2\n ...111 ++ ...222\n ...999 -- 3\n ~~~123 * 8\n ~~~999 / 3" 
           f"\n\n Commands: help, conv, intrange (current: {MAXRANGE}), quit\n"
           "NOTE: ellipsis numbers are not p-adic numbers (10-adic/p-adic number do not lay on the real number line).\n")

def main():
    global MAXRANGE
    try:
        while (True):
            history_file = ".prompt_history"  # File to store command history
            try:
                readline.read_history_file(history_file)
            except FileNotFoundError:
                pass
            readline.set_history_length(100)  # Set the maximum number of items stored in history
            ssum = ""
            while True:
                s = read_input()
                if s.lower() == 'quit':
                    raise("Exit")
                if s.lower() == 'help':
                    printhelp()
                    continue
                if s.lower() == "conv":
                    s = input(colored("Enter 10-Adic number>: ",'green'))
                    ten_adic_number_value = parse_recurring_10adic_number(s)
                    r = ten_adic_number_value.numerator / ten_adic_number_value.denominator
                    print(f"The 10-adic number represented by '{s}' is: {ten_adic_number_value} {r}")
                    continue
                if s.lower() == "intrange":
                    print(f"current int range = {MAXRANGE}")
                    s = input(colored("Enter integer size range>: ", 'green'))
                    MAXRANGE = int(s)
                    continue
                if s == '\x1b[A':  # Cursor Up
                    ssum = get_previous_history()
                    print("\033[K", end="")  # ANSI escape code to clear the line
                    print(ssum, end="")
                elif s == '\x1b[B':  # Cursor Down
                    ssum = get_next_history()
                    print("\033[K", end="")  # ANSI escape code to clear the line
                    print(ssum, end="")
                else:
                    ssum = s
                    add_to_history(ssum)
                # Process the user input
                input_stream = InputStream(ssum)
                
                try:
                    lexer = SimpleArithmeticLexer(input_stream)
                    stream = CommonTokenStream(lexer)
                    parser = SimpleArithmeticParser(stream)
                    tree = parser.start()
                    visitor = ArithmeticVisitor()
                    result = visitor.visit(tree)
                    if isinstance(result, tuple) == False:
                        print(colored("Ellipsis calc>: ", 'red')+ result)
                        add_to_history(result)
                    else:
                        print(colored("Ellipsis calc>:", 'red') + f"{result}")
                except:
                    pass

                
                
                readline.write_history_file(history_file)            
    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    main()
