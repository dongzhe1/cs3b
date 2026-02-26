#################################################
# CS03B - Winter 2026
# Assignment 3 - Question 3
# Student Name: Zhe Dong
# SID: 20703849
#################################################


def decode(s):
    stack = []
    freq = 0
    temp_str = ""

    for i in range(0, len(s)):
        if s[i].isdigit():
            freq = freq * 10 + int(s[i])
        elif s[i] == '[':
            if len(temp_str) > 0:
                stack.append(temp_str)
                temp_str = ""
            if freq > 0:
                stack.append(freq)
                freq = 0
        elif s[i].isalpha():
            temp_str += s[i]
        elif s[i] == ']':
            if temp_str == "":
                temp_str = stack[-1]
                stack.pop()

            while len(stack) > 0 and isinstance(stack[-1], str):
                temp_str = stack.pop() + temp_str

            temp_str = temp_str * stack[-1]
            stack.pop()
            while len(stack) > 0 and isinstance(stack[-1], str):
                temp_str = stack[-1] + temp_str
                stack.pop()

            stack.append(temp_str)
            temp_str = ""

    return ''.join(stack) + temp_str

def run():
    decode("3[a2[c]b]")
    inputs = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "abc3[cd]xyz"]
    for s in inputs:
        print(f"Input: {s}")
        print(f"Output: {decode(s)}")


if __name__ == "__main__":
    run()