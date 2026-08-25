class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        keypad_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        disgits_list = []


        def letter(index , n ) :
            if index >=  len(digits) :
                disgits_list.append(n)
                return 

            current_digit = digits[index]
            possible_letters = keypad_dict[current_digit]
                
            for char in possible_letters:

                letter(index+1,n+char)


        letter(0, "")

        return disgits_list
