#################################################
# CS03B - Winter 2026
# Assignment 2 - Question 3
# Student Name: Zhe Dong
# SID: 20703849
#################################################


def reverse_words_in_sentence(sentence):
    return " ".join([word[::-1] for word in sentence.split(" ")])


def run():
    input_str = "Let's take LeetCode contest"
    print(f"Input: \"{input_str}\"")
    print(f"Output: \"{reverse_words_in_sentence(input_str)}\"")


if __name__ == "__main__":
    run()