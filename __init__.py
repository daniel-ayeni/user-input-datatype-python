# This code was written because python doesn't give the correct data-type when you try to check the datatypes of values
# inputted by users

# import regular expressions
import re

# collect value from user
value = input('Enter your value: ')

# Create pattern to crosscheck and be used to determine what datatype was inputted.
# Unlike some other programming languages, Python does not have double datatype.
# Pattern for identifying a float datatype
# float datatypes are series of numbers and a single period inbetween
pattern_float = re.compile('[0-9]+.[0-9]')
# Pattern for identifying a list datatype
# list datatypes are identified majorly with their bracket type which is []
pattern_list = re.compile('[\[]+[A-Za-z0-9\'\"]')
# Pattern for identifying a tuple datatype
# tuple datatypes are identified majorly with their bracket type or parentheses which is ()
pattern_tuple = re.compile('[\(]+[A-Za-z0-9]')
# Pattern for identifying a complex datatype
# Complex number represented by complex class. Specified as (real part) + (imaginary part)j
pattern_complex = re.compile('[0-9]+\+[0-9]+[j]')
# Pattern for identifying an unknown datatypes.
# Unknown datatypes are datatypes that combine string with int or vice-versa.
pattern_unknown = re.compile('[A-Za-z]+[0-9]')
# Unknown datatypes can also include any of this below.
pattern_unknown_2 = re.compile('[\!,\@\,,\#,\$,\^,\&,\(,\),\{,\},\<,\>,\.,\`,\~,\;,\:,\",\',\?,\\,\|,\/,\=,\_,\*,\-,\+,\%]')
# Pattern for identifying set datatype
pattern_set = re.compile('[\{]+[A-Za-z0-9\'\"]')
# Pattern for identifying dictionary datatype
pattern_dict = re.compile('[\{]+[A-Za-z0-9\'\"]+[\:]+[A-Za-z0-9\'\"]')

# Check if pattern matches any of the above
# Matching for float datatype
float_type = pattern_float.match(value)
# Matching for list datatype
list_type = pattern_list.match(value)
# Matching for tuple datatype
tuple_type = pattern_tuple.match(value)
# Python Interpreter reads line by line. pattern_dict & pattern_set are almost the same. It is advisable for set_type
# to be read last
# Matching for dictionary datatype
dict_type = pattern_dict.match(value)
# Matching for set datatype
set_type = pattern_set.match(value)
# Matching for complex datatype
complex_type = pattern_complex.match(value)
# Matching for unknown datatypes
unknown_type = pattern_unknown.match(value)
unknown_type_2 = pattern_unknown_2.match(value)

# using if statements, we cross-check which of the pattern was correctly matched and display an output if any
# We started with complex_type because data is automatically matched with float_type even with 'j' suffix
if complex_type is not None:
    print(value, 'is a complex data type')
elif float_type is not None:
    print(value, 'is a float data type')
elif list_type is not None:
    print(value, 'is a list data type')
elif tuple_type is not None:
    print(value, 'is a tuple data type')
elif dict_type is not None:
    print(value, 'is a dictionary data type')
elif set_type is not None:
    print(value, 'is a set data type')
elif unknown_type is not None or unknown_type_2 is not None:
    print(value, 'is Unknown')
# If non-matched, the else block runs
else:
    # Use try statement to catch any ValueError. This happens if the user inputs values that do not match the above and
    # is not an integer. That is, it's a String.
    try:
        # We could also use regular expression for int, but we decided to go with this instead.
        # The value from the user is converted to integer and then divided by it-integer-self. using modulus,
        # we check for remainders.
        # If the value inputted by user is anything but an integer, a ValueError will be raised while trying to convert
        # it to integer. Else, the result will be zero.
        if int(value) % int(value) == 0:
            # Could not print directly from inside this if statement. So, I used pass
            pass
        print(value + ' is an int data type')
    # If we get a ValueError, the except block will run.
    except ValueError:
        # Python is an interpreter, read line by line. After a ValueError is generated, we check if the text from the
        # user matches 'True' or 'False'. If it does, it is regarded as boolean data type
        if value == 'True' or value == 'False':
            print(value, 'is a bool data type')
        # The proper way to check the datatype of values is cross-checked to confirm if it's a string
        elif type(value) == str:
            print(value, 'is a string data type')
        # If none of the above is correct or matches, The else statement runs.
        # This block will most likely not run at all because we have created a regular expression to catch unknown
        # datatypes
        else:
            print('unknown')