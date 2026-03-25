Unfortunately stretch is not in a displayable condition at the moment as its my current main personal project and undergoing a major shift in design.

I will however provide a description, and some examples of its code.


Stretch is my dream project, ever since I started learning to code, I though wouldn't it be cool to make my own programming language? That must be incredibly difficult right? I won't be able to do that until I'm an extremely advanced programmer.
All of these assumptions are wrong!

Making a very simple programming language simply by parsing text and executing commands based on it is very simple; this is called an interpreted language.

This is a good way to start creating your language, and python is a very good language to write your first interpreter in, as it provides multiple tools and libraries you can install and use to start designing your interpreter.

Eventually if your language gets complex enough you might want to make it faster.
You could try compiling it, but unless you know machine code or assembly, compiling it will seem impossible.
A good middle ground is to move to designing a byte code format.
This is actually very similar to how python itself works.
If you have a basic understanding of binary + bytes it isnt too complex to create a bytecode.
Then you can compile your language to your own bytecode and interpret your bytecode instead of raw text instead! this is much faster, and will help you practice the concepts you will need to eventually compile your language (if that is your goal; interpreted languages are perfectly valid too!).

The main takeaway is that you don't have to build something to completion in one step. Even with beginner knowledge you can start something small and take it all the way to the top.


Here are some examples of stretch code!

a comment, simple
'''
# comment, this is a comment!
'''

numbers
'''
# notice semicolons seperate each statement
# so this is 3 statements
0; 3; 5 8;
'''

strings
'''
"hello";
"world";
'''

variables
'''
# setting a variable
# using alphabetic identifier
.x: "a value";

# using numeric identifier
\0: "another value";


# getting a variable
.x;
\0;
'''

stacks and groups
'''
# when you create a stack, it is evaluated just like a statement
.mystack: [0 1 .x .x: 9]; # [0, 1, 9]

# a group is evaluated just like a stack, but becomes rigid after constructed
.mygroup: (9 3 5 2);

'''


using keywords
'''
print -> "hello" "world!"; # takes "hello" and "world!" as arguments

print["hello"] "world!"; # only takes "hello" as an argument
'''


init_statements
'''
# init statements get evaluated before the rest of the code, so this is perfectly valid
# especially useful when combined with goto (a keyword) to go to a stored line value
print -> .x;

# marked with $
$.x: 9;
'''


blocks
'''

.code: {
    $\0: 9;

    .x: "hello";

};

print -> .code\0; # 9

print -> .code.x; # error, the block has not been entered yet so .x is not defined
'''


running a block
'''
# block which doesnt take arguments
.code: {
    print -> 0 1 3;
};


# enter keyword
enter[.code]; # 0 1 3
enter -> .code; # 0 1 3

# empty call
.code() # 0 1 3


# block which takes arguments
.code: {
    print -> \1;

};

# group
.code(0, 1, 2); # prints 0
# if you call a block with a group,
# the group is seperated into numbered arguments stored at \0 \1 \2...

# stack
.code[3, 4, 5]; # prints [3, 4, 5]
# if you call a block with a stack, the stack becomes the first
# argument of the block
'''


named parameters
'''
.code {
    $.__params__: ("arg1", "arg2", "0") 
    print -> .arg2 .arg1 \0
};

# if you add a group of names to your block, named __params__
# the parameters inside become the name of given arguments

.code(6, 7, 8) # 7, 6, 8

'''

