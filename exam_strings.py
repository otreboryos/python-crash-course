#The is_palindrome function checks if a string is a palindrome.
#A palindrome is a string that can be equally read from left to right or
#right to left, omitting blank spaces, and ignoring capitalization.
#Examples of palindromes are words like kayak and radar, and phrases
#like "Never Odd or Even". Fill in the blanks in this function to return True
#if the passed string is a palindrome, False if not.


def is_palindrome(input_string):
    n_string = ""
    r_string = ""
    new_string = ""
    reverse_string = ""

    long=int(len(input_string))

    n_string = input_string.lower().split()

    for long in reversed(range(long)):
        r_string += input_string[long].lower()

    r_string = r_string.split()

    for word in n_string:
        new_string += word

    for word in r_string:
        reverse_string += word

    if new_string == reverse_string:
        return True
    else: return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


#If we have a string variable named Weather = "Rainfall", which of the
#following will print the substring or all characters before the "f"?

Weather = "Rainfall"

print(Weather[:4])
print(Weather[4:])
print(Weather[1:4])
#print(Weather[:"f"])




#Fill in the gaps in the nametag function so that it uses the format
#method to return first_name and the first initial of last_name followed
#by a period. For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."




#Using the format method, fill in the gaps in the convert_distance function
#so that it returns the phrase "X miles equals Y km", with Y having only 1
#decimal place. For example, convert_distance(12) should return
#"12 miles equals 19.2 km".



def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km




# The replace_ending function replaces the old string in a sentence with
# the new string, but only if the sentence ends with the old string.
# If there is more than one occurrence of the old string in the sentence,
# only the one at the end is replaced, not all of them. For example,
# replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
# The string comparison is case-sensitive,
# so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence
#sentence="It's raining cats and cats"
#old="cats"
#new="dogs"

    if sentence.endswith(old):
        new_sentence = sentence.rpartition(old)
        return new_sentence[0]+new
    else: return sentence
        # Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the
		# end with the new string
		#i = ___
#print(new_sentence)
#print(new_sentence[0]+new)
		#return new_sentence

	# Return the original sentence if there is no match
	#return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
