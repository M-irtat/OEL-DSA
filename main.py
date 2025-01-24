#OPEN-ENDED LAB DSA:

#Objective:
#Given a string s which consists of lowercase or uppercase letters, return the length of the longest Palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome.

#QUESTION NO.1:
#INPUT: s="abccccdd"
#OUTPUT: 7
#EXPLANATION: One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import Counter


def longestPalindrome(s):
    char_count = Counter(s)
    palindrome_length = 0

    for count in char_count.values():
        palindrome_length += (count // 2) * 2
        if palindrome_length % 2 == 0 and count % 2 == 1:
            palindrome_length += 1

    return palindrome_length


s = "abcccdd"
result = longestPalindrome(s)
print(f"Input: s = '{s}'")
print(f"Output: {result}")

#QUESTION NO.1:
#INPUT: s="a"
#OUTPUT: 1
#EXPLANATION: The longest palindrome that can be built is "a", whose length is 1.


from collections import Counter


def longestPalindrome(s):
    char_count = Counter(s)
    palindrome_length = 0

    for count in char_count.values():
        palindrome_length += (count // 2) * 2
        if palindrome_length % 2 == 0 and count % 2 == 1:
            palindrome_length += 1

    return palindrome_length


s = "a"
result = longestPalindrome(s)
print(f"Input: s = '{s}'")
print(f"Output: {result}")

