import sqlite3 as sql


def createTableIfNotExist():
    sqlConnection = sql.connect(r"SQLiteDB\\corpus.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS corpus (
                            id integer primary key autoincrement,
                            progLangName text not null,
                            description text not null
                        );
                    """)


# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())

def insertRecipeData(progLangName, description):
    con = sql.connect("SQLiteDB\\corpus.db")
    cur = con.cursor()
    cur.execute("INSERT INTO corpus (progLangName, description) VALUES (?,?)",
                (progLangName, description))
    con.commit()
    con.close()


def retrieveCorpusData():
    con = sql.connect("SQLiteDB\\corpus.db")
    cur = con.cursor()
    cur.execute("SELECT progLangName, description FROM corpus")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveCorpusDataWithItemName(progLangName):
    con = sql.connect("SQLiteDB\\corpus.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM corpus WHERE progLangName='{progLangName}'")
    recipe = cur.fetchall()
    con.close()
    return recipe

createTableIfNotExist()
# CPP
cppData = """
C++ is a statically typed, compiled, general-purpose, case-sensitive, free-form programming language that supports procedural, object-oriented, and generic programming.
C++ is regarded as a middle-level language, as it comprises a combination of both high-level and low-level language features.
C++ was developed by Bjarne Stroustrup starting in 1979 at Bell Labs in Murray Hill, New Jersey, as an enhancement to the C language and originally named C with Classes but later it was renamed C++ in 1983.
C++ is a superset of C, and that virtually any legal C program is a legal C++ program.
Note â A programming language is said to use static typing when type checking is performed during compile-time as opposed to run-time.C++ fully supports object-oriented programming, including the four pillars of object-oriented development â
Standard C++ consists of three important parts â The core language giving all the building blocks including variables, data types and literals, etc.
The C++ Standard Library giving a rich set of functions manipulating files, strings, etc.
The Standard Template Library (STL) giving a rich set of methods manipulating data structures, etc.
The ANSI standard is an attempt to ensure that C++ is portable; that code you write for Microsoft's compiler will compile without errors, using a compiler on a Mac, UNIX, a Windows box, or an Alpha.
The ANSI standard has been stable for a while, and all the major C++ compiler manufacturers support the ANSI standard.The most important thing while learning C++ is to focus on concepts.
The purpose of learning a programming language is to become a better programmer; that is, to become more effective at designing and implementing new systems and at maintaining old ones.
C++ supports a variety of programming styles. You can write in the style of Fortran, C, Smalltalk, etc., in any language. Each style can achieve its aims effectively while maintaining runtime and space efficiency.
C++ is used by hundreds of thousands of programmers in essentially every application domain.C++ is being highly used to write device drivers and other software that rely on direct manipulation of hardware under realtime constraints.
C++ is widely used for teaching and research because it is clean enough for successful teaching of basic concepts.
Anyone who has used either an Apple Macintosh or a PC running Windows has indirectly used C++ because the primary user interfaces of these systems are written in C++.
If you are still willing to set up your environment for C++, you need to have ranlib, dlltool, and several other GNU tools from the Windows command line.
When we consider a C++ program, it can be defined as a collection of objects that communicate via invoking each other's methods. Let us now briefly look into what a class, object, methods, and instant variables mean.
Object â Objects have states and behaviors. Example: A dog has states - color, name, breed as well as behaviors - wagging, barking, eating. 
An object is an instance of a class.Class â A class can be defined as a template/blueprint that describes the behaviors/states that object of its type support.
Methods â A method is basically a behavior. A class can contain many methods. It is in methods where the logics are written, data is manipulated and all the actions are executed.
Instance Variables â Each object has its unique set of instance variables. An object's state is created by the values assigned to these instance variables.
Let us look at a simple code that would print the words Hello World.
Let us look at the various parts of the above program â
The C++ language defines several headers, which contain information that is either necessary or useful to your program. For this program, the header<iostream> is needed.
The line using namespace std; tells the compiler to use the std namespace. Namespaces are a relatively recent addition to C++.
The next line '// main() is where program execution begins.' is a single-line comment available in C++. Single-line comments begin with // and stop at the end of the line.
The line int main() is the main function where program execution begins.
The next line cout << "Hello World"; causes the message "Hello World" to be displayed on the screen.
The next line return 0; terminates main( )function and causes it to return the value 0 to the calling process.
Let's look at how to save the file, compile and run the program. Please follow the steps given below âOpen a text editor and add the code as above.
Save the file as: hello.cpp
Open a command prompt and go to the directory where you saved the file.
Type 'g++ hello.cpp' and press enter to compile your code. If there are no errors in your code the command prompt will take you to the next line and would generate a.out executable file.
Now, type 'a.out' to run your program.
You will be able to see ' Hello World ' printed on the window.Make sure that g++ is in your path and that you are running it in the directory containing file hello.cpp.
You can compile C/C++ programs using makefile. For more details, you can check our'Makefile Tutorial'.
In C++, the semicolon is a statement terminator. That is, each individual statement must be ended with a semicolon. It indicates the end of one logical entity.
For example, following are three different statements â A block is a set of logically connected statements that are surrounded by opening and closing braces. For example â
C++ does not recognize the end of the line as a terminator. For this reason, it does not matter where you put a statement in a line. For example â is the same as
A C++ identifier is a name used to identify a variable, function, class, module, or any other user-defined item. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores, 
and digits (0 to 9).C++ does not allow punctuation characters such as @, $, and % within identifiers. C++ is a case-sensitive programming language. Thus, Manpower and manpower are two different identifiers in C++.
Here are some examples of acceptable identifiers â
The following list shows the reserved words in C++. These reserved words may not be used as constant or variable or any other identifier names.
A few characters have an alternative representation, called a trigraph sequence. A trigraph is a three-character sequence that represents a single character and the sequence always starts with two question marks.
Trigraphs are expanded anywhere they appear, including within string literals and character literals, in comments, and in preprocessor directives.
Following are most frequently used trigraph sequences â All the compilers do not support trigraphs and they are not advised to be used because of their confusing nature.
A line containing only whitespace, possibly with a comment, is known as a blank line, and C++ compiler totally ignores it.
Whitespace is the term used in C++ to describe blanks, tabs, newline characters and comments. Whitespace separates one part of a statement from another and enables the compiler to identify where one element in a statement, such as int, ends and the next element begins.
In the above statement there must be at least one whitespace character (usually a space) between int and age for the compiler to be able to distinguish them.
In the above statement 2, no whitespace characters are necessary between fruit and =, or between = and apples, although you are free to include some if you wish for readability purpose.
Program comments are explanatory statements that you can include in the C++ code. These comments help anyone reading the source code. All programming languages allow for some form of comments.
C++ supports single-line and multi-line comments. All characters available inside any comment are ignored by C++ compiler.
C++ comments start with /* and end with */. For example â
A comment can also start with //, extending to the end of the line. For example â
When the above code is compiled, it will ignore // prints Hello World and final executable will produce the following result â
Within a /* and */ comment, // characters have no special meaning. Within a // comment, /* and */ have no special meaning. Thus, you can "nest" one kind of comment within the other kind. For example â
While writing program in any language, you need to use various variables to store various information. Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some 
space in memory.You may like to store information of various data types like character, wide character, integer, floating point, double floating point, boolean etc. Based on the data type of a variable, the operating system allocates memory and decides 
what can be stored in the reserved memory.C++ offers the programmer a rich assortment of built-in as well as user defined data types. Following table lists down seven basic C++ data types â Several of the basic types can be modified using one or more of these type 
modifiers â The following table shows the variable type, how much memory it takes to store the value in memory, and what is maximum and minimum value which can be stored in such type of variables.
The size of variables might be different from those shown in the above table, depending on the compiler and the computer you are using.
Following is the example, which will produce correct size of various data types on your computer.
This example uses endl, which inserts a new-line character after every line and << operator is being used to pass multiple values out to the screen. We are also using sizeof() operator to get size of various data types.
When the above code is compiled and executed, it produces the following result which can vary from machine to machine â
You can create a new name for an existing type using typedef. 
Following is the simple syntax to define a new type using typedef âFor example, the following tells the compiler that feet is another name for int â
Now, the following declaration is perfectly legal and creates an integer variable called distance â
An enumerated type declares an optional type name and a set of zero or more identifiers that can be used as values of the type. Each enumerator is a constant whose type is the enumeration.
Creating an enumeration requires the use of the keyword enum. The general form of an enumeration type is â
Here, the enum-name is the enumeration's type name. The list of names is comma separated.
For example, the following code defines an enumeration of colors called colors and the variable c of type color. Finally, c is assigned the value "blue".
By default, the value of the first name is 0, the second name has the value 1, and the third has the value 2, and so on. But you can give a name, a specific value by adding an initializer. For example, in the following enumeration, green will have the value 5.
Here, blue will have a value of 6 because each name will be one greater than the one that precedes it.A variable provides us with named storage that our programs can manipulate. 
Each variable in C++ has a specific type, which determines the size and layout of the variable's memory; the range of values that can be stored within that memory; and the set of operations that can be applied to the variable.
The name of a variable can be composed of letters, digits, and the underscore character. It must begin with either a letter or an underscore. Upper and lowercase letters are distinct because C++ is case-sensitive â There are following basic types of variable in C++ as explained in last 
chapter â bool Stores either value true or false.
char Typically a single octet (one byte). This is an integer type.
int The most natural size of integer for the machine.
float A single-precision floating point value.
double
A double-precision floating point value.
void
Represents the absence of type.
wchar_t
A wide character type.
C++ also allows to define various other types of variables, which we will cover in subsequent chapters like Enumeration, Pointer, Array, Reference, Data structures, and Classes.
Following section will cover how to define, declare and use various types of variables.
A variable definition tells the compiler where and how much storage to create for the variable. A variable definition specifies a data type, and contains a list of one or more variables of that type as follows â
Here, type must be a valid C++ data type including char, w_char, int, float, double, bool or any user-defined object, etc., and variable_list may consist of one or more identifier names separated by commas. Some valid declarations are shown here â
The line int i, j, k; both declares and defines the variables i, j and k; which instructs the compiler to create variables named i, j and k of type int.
Variables can be initialized (assigned an initial value) in their declaration. The initializer consists of an equal sign followed by a constant expression as follows â
Some examples are â
For definition without an initializer: variables with static storage duration are implicitly initialized with NULL (all bytes have the value 0); the initial value of all other variables is undefined.
A variable declaration provides assurance to the compiler that there is one variable existing with the given type and name so that compiler proceed for further compilation without needing complete detail about the variable. A 
variable declaration has its meaning at the time of compilation only, compiler needs actual variable definition at the time of linking of the program.
A variable declaration is useful when you are using multiple files and you define your variable in one of the files which will be available at the time of linking of the program. You will use extern keyword to declare a variable 
at any place. Though you can declare a variable multiple times in your C++ program, but it can be defined only once in a file, a function or a block of code.
Try the following example where a variable has been declared at the top, but it has been defined inside the main function â
When the above code is compiled and executed, it produces the following result â Same concept applies on function declaration where you provide a function name at the time of its declaration and its actual definition can be given anywhere else. For example â
There are two kinds of expressions in C++ â lvalue â Expressions that refer to a memory location is called "lvalue" expression. An lvalue may appear as either the left-hand or right-hand side of an assignment.
rvalue â The term rvalue refers to a data value that is stored at some address in memory. An rvalue is an expression that cannot have a value assigned to it which means an rvalue may appear on the right- but not left-hand side of an assignment.
Variables are lvalues and so may appear on the left-hand side of an assignment. Numeric literals are rvalues and so may not be assigned and can not appear on the left-hand side. Following is a valid statement â
But the following is not a valid statement and would generate compile-time error â
A scope is a region of the program and broadly speaking there are three places, where variables can be declared â
Inside a function or a block which is called local variables,In the definition of function parameters which is called formal parameters.
Outside of all functions which is called global variables.
We will learn what is a function and it's parameter in subsequent chapters. 
Here let us explain what are local and global variables.
Variables that are declared inside a function or block are local variables. 
They can be used only by statements that are inside that function or block of code. Local variables are not known to functions outside their own. Following is the example using local variables â
Global variables are defined outside of all the functions, usually on top of the program. The global variables will hold their value throughout the life-time of your program.
A global variable can be accessed by any function. That is, a global variable is available for use throughout your entire program after its declaration. 
Following is the example using global and local variables âA program can have same name for local and global variables but value of 
local variable inside a function will take preference. For example â
When the above code is compiled and executed, it produces the following 
result â
When a local variable is defined, it is not initialized by the system, you must initialize it yourself. Global variables are initialized automatically by the system when you define them as follows â
It is a good programming practice to initialize variables properly, otherwise sometimes program would produce unexpected result.
Constants refer to fixed values that the program may not alter and they are called literals.
Constants can be of any of the basic data types and can be divided into Integer Numerals, Floating-Point Numerals, Characters, Strings and Boolean Values.
Again, constants are treated just like regular variables except that their values cannot be modified after their definition.
An integer literal can be a decimal, octal, or hexadecimal constant. A prefix specifies the base or radix: 0x or 0X for hexadecimal, 0 for octal, and nothing for decimal.
An integer literal can also have a suffix that is a combination of U and L, for unsigned and long, respectively. The suffix can be uppercase or lowercase and can be in any order.
Here are some examples of integer literals â
Following are other examples of various types of Integer literals â
A floating-point literal has an integer part, a decimal point, a fractional part, and an exponent part. You can represent floating point literals either in decimal form or exponential form.
While representing using decimal form, you must include the decimal point, the exponent, or both and while representing using exponential form, you must include the integer part, the fractional part, or both. The signed exponent is 
introduced by e or E.Here are some examples of floating-point literals â There are two Boolean literals and they are part of standard C++ keywords â
A value of true representing true.
A value of false representing false.
You should not consider the value of true equal to 1 and value of false equal to 0.
Character literals are enclosed in single quotes. If the literal begins with L (uppercase only), it is a wide character literal (e.g., L'x') and should be stored in wchar_t type of variable . Otherwise, it is a narrow character 
literal (e.g., 'x') and can be stored in a simple variable of char type.
A character literal can be a plain character (e.g., 'x'), an escape sequence (e.g., '\t'), or a universal character (e.g., '\u02C0').
There are certain characters in C++ when they are preceded by a backslash they will have special meaning and they are used to represent like newline (\n) 
or tab (\t). Here, you have a list of some of such escape sequence codes â Following is the example to show a few escape sequence characters â
When the above code is compiled and executed, it produces the following result â
String literals are enclosed in double quotes. A string contains characters that are similar to character literals: plain characters, escape sequences, and universal characters.
You can break a long line into multiple lines using string literals and separate them using whitespaces.
Here are some examples of string literals. All the three forms are identical strings.
There are two simple ways in C++ to define constants â
Using #define preprocessor.
Using const keyword.
Following is the form to use #define preprocessor to define a constant â
Following example explains it in detail â
When the above code is compiled and executed, it produces the following result â
You can use const prefix to declare constants with a specific type as follows â
Following example explains it in detail â
When the above code is compiled and executed, it produces the following result â
Note that it is a good programming practice to define constants in CAPITALS.
C++ allows the char, int, and double data types to have modifiers preceding them. A modifier is used to alter the meaning of the base type so that it more precisely fits the needs of various situations.
The data type modifiers are listed here â The modifiers signed, unsigned, long, and short can be applied to integer base types. In addition, signed and unsigned can be applied to char, and long can be applied to double.
The modifiers signed and unsigned can also be used as prefix tolong or short modifiers. For example, unsigned long int.
C++ allows a shorthand notation for declaring unsigned, short, or long integers. You can simply use the word unsigned, short, orlong, without int. It automatically implies int. For example, the following two statements both declare unsigned integer variables.
To understand the difference between the way signed and unsigned integer modifiers are interpreted by C++, you should run the following short program â
When this program is run, following is the output â The above result is because the bit pattern that represents 50,000 as a short unsigned integer is interpreted as -15,536 by a short.
The type qualifiers provide additional information about the variables they precede.
const
Objects of type const cannot be changed by your program during execution.
volatile
The modifier volatile tells the compiler that a variable's value may be changed in ways not explicitly specified by the program.
restrict
A pointer qualified by restrict is initially the only means by which the object it points to can be accessed. Only C99 adds a new type qualifier called restrict.
A storage class defines the scope (visibility) and life-time of variables and/or functions within a C++ Program. These specifiers precede the type that they modify. There are following storage classes, which can be used in a C++ 
Program
The auto storage class is the default storage class for all local variables.
The example above defines two variables with the same storage class, auto can only be used within functions, i.e., local variables.
The register storage class is used to define local variables that should be stored in a register instead of RAM. This means that the variable has a maximum size equal to the register size (usually one word) and can't have the 
unary '&' operator applied to it (as it does not have a memory location).
The register should only be used for variables that require quick access such as counters. It should also be noted that defining 'register' does not mean that 
the variable will be stored in a register. It means that it MIGHT be stored in a register depending on hardware and implementation restrictions.
The static storage class instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating 
and destroying it each time it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.
The static modifier may also be applied to global variables. When this is done, it causes that variable's scope to be restricted to the file in which it is declared.
In C++, when static is used on a class data member, it causes only one copy of that member to be shared by all objects of its class.
When the above code is compiled and executed, it produces the following result â
The extern storage class is used to give a reference of a global variable that is visible to ALL the program files. When you use 'extern' the variable cannot be initialized as all it does is point the variable name at a storage location that has been previously defined.
When you have multiple files and you define a global variable or function, which will be used in other files also, then extern will be used in another file to give reference of defined variable or function. Just for understanding extern is used to declare a global variable or function in another file.
The extern modifier is most commonly used when there are two or more files sharing the same global variables or functions as explained below.Here, extern keyword is being used to declare count in another file. 
Now compile these two files as follows â
This will produce write executable program, try to execute write and check the result as follows â
The mutable specifier applies only to class objects, which are discussed later in this tutorial. It allows a member of an object to override const member function. That is, a mutable member can be modified by a const member function.
An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations. C++ is rich in built-in operators and provide the following types of operators â
This chapter will examine the arithmetic, relational, logical, bitwise, assignment and other operators one by one.
There are following arithmetic operators supported by C++ language â
Assume variable A holds 10 and variable B holds 20, then â
Show Examples
There are following relational operators supported by C++ languageAssume variable A holds 10 and variable B holds 20, then â
Show Examples
There are following logical operators supported by C++ language.
Assume variable A holds 1 and variable B holds 0, then â
Show Examples
Bitwise operator works on bits and perform bit-by-bit operation. The truth tables for &, |, and ^ are as follows â
Assume if A = 60; and B = 13; now in binary format they will be as follows â
A = 0011 1100
B = 0000 1101
-----------------
A&B = 0000 1100
A|B = 0011 1101
A^B = 0011 0001
~A  = 1100 0011
The Bitwise operators supported by C++ language are listed in the following table. Assume variable A holds 60 and variable B holds 13, then â
Show Examples
There are following assignment operators supported by C++ language â
Show Examples
The following table lists some other operators that C++ supports.
sizeof
sizeof operator returns the size of a variable. For example, 
sizeof(a), where âaâ is integer, and will return 4.
Condition ? X : Y
Conditional operator (?). If Condition is true then it returns value 
of X otherwise returns value of Y.
,
Comma operator causes a sequence of operations to be performed. The value of the entire comma expression is the value of the last expression of the comma-separated list.
. (dot) and -> (arrow)
Member operators are used to reference individual members of classes, structures, and unions.
Cast
Casting operators convert one data type to another. For example, 
int(2.2000) would return 2.
&
Pointer operator & returns the address of a variable. For example 
&a; will give actual address of the variable.
*
Pointer operator * is pointer to a variable. For example *var; will pointer to a variable var.
Operator precedence determines the grouping of terms in an expression. This affects how an expression is evaluated. Certain operators have higher precedence than others; for example, the multiplication operator has higher precedence than 
the addition operator â
For example x = 7 + 3 * 2; here, x is assigned 13, not 20 because operator * has higher precedence than +, so it first gets multiplied with 3*2 and then adds into 7.
Here, operators with the highest precedence appear at the top of the table, those with the lowest appear at the bottom. Within an expression, higher precedence operators will be evaluated first.
Show Examples
There may be a situation, when you need to execute a block of code several number of times. In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on.
Programming languages provide various control structures that allow for more complicated execution paths.
A loop statement allows us to execute a statement or group of statements multiple times and following is the general from of a loop statement in most of the programming languages â
C++ programming 
language provides the following type of loops to handle looping requirements.Repeats a statement or group of statements while a given condition is true. It tests the condition before executing the loop body.
Execute a sequence of statements multiple times and abbreviates the code that manages the loop variable.
Like a âwhileâ statement, except that it tests the condition at the end of the loop body.
You can use one or more loop inside any another âwhileâ, âforâ or âdo..whileâ loop.
Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
C++ supports the following control statements.
Terminates the loop or switch statement and transfers execution to the statement immediately following the loop or switch.
Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
Transfers control to the labeled statement. Though it is not advised to use goto statement in your program.
A loop becomes infinite loop if a condition never becomes false. The for loop is traditionally used for this purpose. Since none of the three expressions that form the âforâ loop are required, you can make an endless loop by leaving 
the conditional expression empty.
When the conditional expression is absent, it is assumed to be true. You may have an initialization and increment expression, but C++ programmers more commonly use the âfor (;;)â construct to signify an infinite loop.
NOTE â You can terminate an infinite loop by pressing Ctrl + C keys.
Decision making structures require that the programmer specify one or more conditions to be evaluated or tested by the program, along with a statement or statements to be executed if the condition is determined to be true, and optionally, other statements to be executed if the condition is determined to be false.
Following is the general form of a typical decision making structure found in 
most of the programming languages â
C++ 
programming language provides following types of decision making statements.
An âifâ statement consists of a boolean expression followed by one or more statements.
An âifâ statement can be followed by an optional âelseâ statement, which executes when the boolean expression is false.
A âswitchâ statement allows a variable to be tested for equality against a list of values.
You can use one âifâ or âelse ifâ statement inside another âifâ or âelse ifâ statement(s).
You can use one âswitchâ statement inside another âswitchâ statement(s).
We have covered
conditional operator â? :â in previous chapter which can be used to replace
if...else statements. It has the following general form â
Exp1, Exp2, and Exp3 are expressions. Notice the use and placement of the colon.
The value of a â?â expression is determined like this: Exp1 is evaluated. If it is true, then Exp2 is evaluated and becomes the value of the entire â?â 
expression. If Exp1 is false, then Exp3 is evaluated and its value becomes the value of the expression.
A function is a group of statements that together perform a task. Every C++ program has at least one function, which is main(), and all the most trivial programs can define additional functions.
You can divide up your code into separate functions. How you divide up your code among different functions is up to you, but logically the division usually is such that each function performs a specific task.
A function declaration tells the compiler about a function's name, return type, and parameters. A function definition provides the actual body of the function.
The C++ standard library provides numerous built-in functions that your program can call. For example, function strcat() to concatenate two strings, function memcpy() to copy one memory location to another location and many more functions.
A function is known with various names like a method or a sub-routine or a procedure etc.
The general form of a C++ function definition is as follows â
A C++ function definition consists of a function header and a function body. 
Here are all the parts of a function â
Return Type â A function may return a value. The return_type is the data type of the value the function returns. Some functions perform the desired operations without returning a value. In this case, the return_type is the keyword void.
Function Name â This is the actual name of the function. The function name and the parameter list together constitute the function signature.
Parameters â A parameter is like a placeholder. When a function is invoked, you pass a value to the parameter. This value is referred to as actual parameter or argument. The parameter list refers to the type, order, 
and number of the parameters of a function. Parameters are optional; that is, a function may contain no parameters.
Function Body â The function body contains a collection of statements that define what the function does.
Following is the source code for a function called max(). This function takes two parameters num1 and num2 and return the biggest of both â
A function declaration tells the compiler about a function name and how to call the function. The actual body of the function can be defined separately.
A function declaration has the following parts â
For the above defined function max(), following is the function declaration â
Parameter names are not important in function declaration only their type is required, so following is also valid declaration â
Function declaration is required when you define a function in one source file and you call that function in another file. In such case, you should declare the function at the top of the file calling the function.
While creating a C++ function, you give a definition of what the function has to do. To use a function, you will have to call or invoke that function.
When a program calls a function, program control is transferred to the called function. A called function performs defined task and when itâs return statement is executed or when its function-ending closing brace is reached, it returns 
program control back to the main program.
To call a function, you simply need to pass the required parameters along with function name, and if function returns a value, then you can store returned value. For example â
I kept max() function along with main() function and compiled the source code. While running final executable, it would produce the following result â
If a function is to use arguments, it must declare variables that accept the values of the arguments. These variables are called the formal parameters of the function.
The formal parameters behave like other local variables inside the function and are created upon entry into the function and destroyed upon exit.While calling a function, there are two ways that arguments can be passed to a function â
This method copies the actual value of an argument into the formal parameter of the function. In this case, changes made to the parameter inside the function have no effect on the argument.
This method copies the address of an argument into the formal parameter. Inside the function, the address is used to access the actual argument used in the call. This means that changes made to the parameter affect the argument.
This method copies the reference of an argument into the formal parameter. Inside the function, the reference is used to access the actual argument used in the call. This means that changes made to the parameter affect the argument.
By default, C++ uses call by value to pass arguments. In general, this means that code within a function cannot alter the arguments used to call the function and above mentioned example while calling max() function used the same method.
When you define a function, you can specify a default value for each of the last parameters. This value will be used if the corresponding argument is left blank when calling to the function.
This is done by using the assignment operator and assigning values for the arguments in the function definition. If a value for that parameter is not passed when the function is called, the default given value is used, but if a 
value is specified, this default value is ignored and the passed value is used instead. Consider the following example â
When the above code is compiled and executed, it produces the following result â
Normally, when we work with Numbers, we use primitive data types such as int, short, long, float and double, etc. The number data types, their possible values and number ranges have been explained while discussing C++ Data Types.You have already defined numbers in various examples given in previous 
chapters. Here is another consolidated example to define various types of numbers in C++ â
When the above code is compiled and executed, it produces the following result â
In addition to the various functions you can create, C++ also includes some useful functions you can use. These functions are available in standard C and C++ libraries and called built-in functions. These are functions that can 
be included in your program and then use.C++ has a rich set of mathematical operations, which can be performed on various numbers. Following table lists down some useful built-in mathematical functions available in C++.
To utilize these functions you need to include the math header file 
<cmath>.
double cos(double);
This function takes an angle (as a double) and returns the cosine.
double sin(double);
This function takes an angle (as a double) and returns the sine.
double tan(double);
This function takes an angle (as a double) and returns the tangent.
double log(double);
This function takes a number and returns the natural log of that number.
double pow(double, double);
The first is a number you wish to raise and the second is the power you wish to raise it t
double hypot(double, double);
If you pass this function the length of two sides of a right triangle, it will return you the length of the hypotenuse.
double sqrt(double);
You pass this function a number and it gives you the square root.
int abs(int);
This function returns the absolute value of an integer that is passed to it.
double fabs(double);
This function returns the absolute value of any decimal number passed to it.
double floor(double);
Finds the integer which is less than or equal to the argument passed to it.
Following is a simple example to show few of the mathematical operations â
When the above code is compiled and executed, it produces the following 
result â
There are many cases where you will wish to generate a random number. There are actually two functions you will need to know about random number generation. 
The first is rand(), this function will only return a pseudo random number. The way to fix this is to first call the srand() function.
Following is a simple example to generate few random numbers. This example makes use of time() function to get the number of seconds on your system time, to randomly seed the rand() function â
When the above code is compiled and executed, it produces the following 
result â
C++ provides a data structure, the array, which stores a fixed-size sequential collection of elements of the same type. An array is used to store a collection of data, but it is often more useful to think of an array as a 
collection of variables of the same type.
Instead of declaring individual variables, such as number0, number1, ..., and number99, you declare one array variable such as numbers and use numbers[0], numbers[1], and ..., numbers[99] to represent individual variables. A specific 
element in an array is accessed by an index.All arrays consist of contiguous memory locations. The lowest address corresponds to the first element and the highest address to the last element.To declare an array in C++, the programmer specifies the type of the elements 
and the number of elements required by an array as follows â
This is called a single-dimension array. The arraySize must be an integer constant greater than zero and type can be any valid C++ data type. For example, to declare a 10-element array called balance of type double, 
use this statement â
You can initialize C++ array elements either one by one or using a single statement as follows â
The number of values between braces { } can not be larger than the number of elements that we declare for the array between square brackets [ ]. Following is an example to assign a single element of the array â
If you omit the size of the array, an array just big enough to hold the initialization is created. Therefore, if you write â
You will create exactly the same array as you did in the previous example.The above statement assigns element number 5th in the array a 
value of 50.0. Array with 4th index will be 5th, i.e., last element because all arrays have 0 as the index of their first element which is also called base index. Following is the pictorial representaion of the same 
array we discussed above â An element is accessed by indexing the array name. This is done by placing the index of the element within square brackets after the name of the array. For 
example â
The above statement will take 10th element from the array and assign the value to salary variable. Following is an example, which will use all the above-mentioned three concepts viz. declaration, assignment and accessing arrays â
This program makes use of setw() function to format the output. When the above code is compiled and executed, it produces the following result â
Arrays are important to C++ and should need lots of more detail. There are following few important concepts, which should be clear to a C++ programmer â
C++ supports multidimensional arrays. The simplest form of the multidimensional array is the two-dimensional array.
You can generate a pointer to the first element of an array by simply specifying the array name, without any index.
You can pass to the function a pointer to an array by specifying the array's name without an index.
C++ allows a function to return an array.
C++ provides following two types of string representations â
The C-style character string originated within the C language and continues to be supported within C++. This string is actually a one-dimensional array of characters which is terminated by a null character '\0'. Thus a 
null-terminated string contains the characters that comprise the string followed by a null.
The following declaration and initialization create a string consisting of the word "Hello". To hold the null character at the end of the array, the size of the character array containing the string is one more than the number of 
characters in the word "Hello."
If you follow the rule of array initialization, then you can write the above statement as follows â
Following is the memory presentation of above defined string in C/C++ â
Actually, you do not place the null character at the end of a string constant. 
The C++ compiler automatically places the '\0' at the end of the string when it initializes the array. Let us try to print above-mentioned string â
When the above code is compiled and executed, it produces the following 
result â
C++ supports a wide range of functions that manipulate null-terminated 
strings â
strcpy(s1, s2);
Copies string s2 into string s1.
strcat(s1, s2);
Concatenates string s2 onto the end of string s1.
strlen(s1);
Returns the length of string s1.
strcmp(s1, s2);
Returns 0 if s1 and s2 are the same; less than 0 if s1<s2; greater than 0 if s1>s2.
strchr(s1, ch);
Returns a pointer to the first occurrence of character ch in string s1.
strstr(s1, s2);
Returns a pointer to the first occurrence of string s2 in string s1.
Following example makes use of few of the above-mentioned functions â
When the above code is compiled and executed, it produces result something as 
follows â
The standard C++ library provides a string class type that supports all the operations mentioned above, additionally much more functionality. Let us check the following example â
When the above code is compiled and executed, it produces result something as 
follows â
C++ pointers are easy and fun to learn. Some C++ tasks are performed more easily with pointers, and other C++ tasks, such as dynamic memory allocation, cannot be performed without them.
As you know every variable is a memory location and every memory location has its address defined which can be accessed using ampersand (&) operator which denotes an address in memory. Consider the following which will print the 
address of the variables defined â
When the above code is compiled and executed, it produces the following 
result â
A pointer is a variable whose value is the address of another variable. Like any variable or constant, you must declare a pointer before you can work with it. The general form of a pointer variable declaration is â
Here, type is the pointer's base type; it must be a valid C++ type and var-name is the name of the pointer variable. The asterisk you used to 
declare a pointer is the same asterisk that you use for multiplication. However, in this statement the asterisk is being used to designate a variable as a pointer. Following are the valid pointer declaration â
The actual data type of the value of all pointers, whether integer, float, character, or otherwise, is the same, a long hexadecimal number that represents a memory address. The only difference between pointers of different data types 
is the data type of the variable or constant that the pointer points to.There are few important operations, which we will do with the pointers very frequently. (a) We define a pointer variable. (b) Assign the address of a variable to a pointer. (c) Finally access the value at the 
address available in the pointer variable. This is done by using unary operator * that returns the value of the variable located at the address specified by its operand. Following example makes use of these operations â
When the above code is compiled and executed, it produces result something as 
follows â
Pointers have many but easy concepts and they are very important to C++ programming. There are following few important pointer concepts which should be clear to a C++ programmer â
C++ supports null pointer, which is a constant with a value of zero defined in several standard libraries.
There are four arithmetic operators that can be used on pointers: ++, --, +, -
There is a close relationship between pointers and arrays.
You can define arrays to hold a number of pointers.
C++ allows you to have pointer on a pointer and so on.
Passing an argument by reference or by address both enable the passed argument to be changed in the calling function by the called function.
C++ allows a function to return a pointer to local variable, static variable and dynamically allocated memory as well.
A reference variable is an alias, that is, another name for an already existing variable. Once a reference is initialized with a variable, either the variable name or the reference name may be used to refer to the variable.
References are often confused with pointers but three major differences between references and pointers are â
You cannot have NULL references. You must always be able to assume that a reference is connected to a legitimate piece of storage.
Once a reference is initialized to an object, it cannot be changed to refer to another object. Pointers can be pointed to another object at any time.
A reference must be initialized when it is created. Pointers can be initialized at any time.
Think of a variable name as a label attached to the variable's location in memory. You can then think of a reference as a second label attached to that memory location. Therefore, you can access the contents of the variable through 
either the original variable name or the reference. For example, suppose we have the following example â
We can declare reference variables for i as follows.
Read the & in these declarations as reference. Thus, read the first declaration as "r is an integer reference initialized to i" and read the second declaration as "s is a double reference initialized to d.". Following example 
makes use of references on int and double â When the above code is compiled together and executed, it produces the following result â
References are usually used for function argument lists and function return values. So following are two important subjects related to C++ references which should be clear to a C++ programmer â
C++ supports passing references as function parameter more safely than parameters.
You can return reference from a C++ function like any other data type.
The C++ standard library does not provide a proper date type. C++ inherits the structs and functions for date and time manipulation from C. To access date and time related functions and structures, you would need to include <ctime> 
header file in your C++ program.
There are four time-related types: clock_t, time_t, size_t, and tm. 
The types - clock_t, size_t and time_t are capable of representing the system time and date as some sort of integer.
The structure type tm holds the date and time in the form of a C structure having the following elements â
Following are the important functions, which we use while working with date 
and time in C or C++. All these functions are part of standard C and C++ library and you can check their detail using reference to C++ standard library given below.
time_t time(time_t *time);
This returns the current calendar time of the system in number of seconds elapsed since January 1, 1970. If the system has no time, .1 is returned.
char *ctime(const time_t *time);
This returns a pointer to a string of the form day month year hours:minutes:seconds year\n\0.
struct tm *localtime(const time_t *time);
This returns a pointer to the tm structure representing local time.
clock_t clock(void);
This returns a value that approximates the amount of time the calling program has been running. A value of .1 is returned if the time is not available.
char * asctime ( const struct tm * time );
This returns a pointer to a string that contains the information stored in the structure pointed to by time converted into the form: day month date hours:minutes:seconds year\n\0
struct tm *gmtime(const time_t *time);
This returns a pointer to the time in the form of a tm structure. The time is represented in Coordinated Universal Time (UTC), which is essentially Greenwich Mean Time (GMT).
time_t mktime(struct tm *time);
This returns the calendar-time equivalent of the time found in the structure pointed to by time.
double difftime ( time_t time2, time_t time1 );
This function calculates the difference in seconds between time1 and time2.
size_t strftime();
This function can be used to format date and time in a specific format.
Suppose you want to retrieve the current system date and time, either as a local time or as a Coordinated Universal Time (UTC). Following is the example to achieve the same â
When the above code is compiled and executed, it produces the following 
result â
The tm structure is very important while working with date and time in either C or C++. This structure holds the date and time in the form of a C structure as mentioned above. Most of the time related functions makes use of tm structure. Following is an example which makes use of various date and time 
related functions and tm structure â
While using structure in this chapter, I'm making an assumption that you have basic understanding on C structure and how to access structure members using 
arrow -> operator.
When the above code is compiled and executed, it produces the following 
result â
The C++ standard libraries provide an extensive set of input/output capabilities which we will see in subsequent chapters. This chapter will discuss very basic and most common I/O operations required for C++ programming.
C++ I/O occurs in streams, which are sequences of bytes. If bytes flow from a device like a keyboard, a disk drive, or a network connection etc. to main memory, this is called input operation and if bytes flow from main memory 
to a device like a display screen, a printer, a disk drive, or a network connection, etc., this is called output operation.
There are following header files important to C++ programs â
<iostream>
This file defines the cin, cout, cerr and clog objects, which correspond to the standard input stream, the standard output stream, the un-buffered standard error stream and the buffered standard error stream, respectively.
<iomanip>
This file declares services useful for performing formatted I/O with so-called parameterized stream manipulators, such as setw and setprecision.
<fstream>
This file declares services for user-controlled file processing. We will discuss about it in detail in File and Stream related chapter.
The predefined object cout is an instance of ostream class. The cout object is said to be "connected to" the standard output device, which usually is the display screen. The cout is used in conjunction with the stream insertion operator, which is written as << which are two less than signs 
as shown in the following example.When the above code is compiled and executed, it produces the following 
result â
The C++ compiler also determines the data type of variable to be output and selects the appropriate stream insertion operator to display the value. The << operator is overloaded to output data items of built-in types integer, float, 
double, strings and pointer values.
The insertion operator << may be used more than once in a single statement as shown above and endl is used to add a new-line at the end of the line.
The predefined object cin is an instance of istream class. The cin object is said to be attached to the standard input device, which usually is the keyboard. The cin is used in conjunction with the stream extraction operator, which is written as >> which are two greater than signs as shown in the following example.
When the above code is compiled and executed, it will prompt you to enter a name. You enter a value and then hit enter to see the following result â
The C++ compiler also determines the data type of the entered value and selects the appropriate stream extraction operator to extract the value and store it in the given variables.
The stream extraction operator >> may be used more than once in a single statement. To request more than one datum you can use the following â
This will be equivalent to the following two statements â
The predefined object cerr is an instance of ostream class. The cerr object is said to be attached to the standard error device, which is also a display screen but the object cerr is un-buffered and each stream insertion to cerr causes its output to appear immediately.
The cerr is also used in conjunction with the stream insertion operator as shown in the following example.
When the above code is compiled and executed, it produces the following 
result â
The predefined object clog is an instance of ostream class. The clog object is said to be attached to the standard error device, which is also a display screen but the object clog is buffered. This means that each 
insertion to clog could cause its output to be held in a buffer until the buffer is filled or until the buffer is flushed.
The clog is also used in conjunction with the stream insertion operator as shown in the following example.When the above code is compiled and executed, it produces the following 
result â
You would not be able to see any difference in cout, cerr and clog with these small examples, but while writing and executing big programs the difference becomes obvious. So it is good practice to display error messages using cerr 
stream and while displaying other log messages then clog should be used.
C/C++ arrays allow you to define variables that combine several data items of the same kind, but structure is another user defined data type which allows you to combine data items of different kinds.
Structures are used to represent a record, suppose you want to keep track of your books in a library. You might want to track the following attributes about each book â
To define a structure, you must use the struct statement. The struct statement defines a new data type, with more than one member, for your program. 
The format of the struct statement is this âThe structure tag is optional and each member definition is a normal variable definition, such as int i; or float f; or any other valid variable definition. At the end of the structure's definition, before the final 
semicolon, you can specify one or more structure variables but it is optional. 
Here is the way you would declare the Book structure â
To access any member of a structure, we use the member access operator (.). The member access operator is coded as a period between the structure variable name and the structure member that we wish to access. You would use struct 
keyword to define variables of structure type. Following is the example to explain usage of structure â
When the above code is compiled and executed, it produces the following 
result â
You can pass a structure as a function argument in very similar way as you pass any other variable or pointer. You would access structure variables in the similar way as you have accessed in the above example â
When the above code is compiled and executed, it produces the following 
result â
You can define pointers to structures in very similar way as you define 
pointer to any other variable as follows â
Now, you can store the address of a structure variable in the above defined pointer variable. To find the address of a structure variable, place the & operator before the structure's name as follows â
To access the members of a structure using a pointer to that structure, you must use the -> operator as follows â
Let us re-write above example using structure pointer, hope this will be easy for you to understand the concept â
When the above code is compiled and executed, it produces the following result â
There is an easier way to define structs or you could "alias" types you create. For example â
Now, you can use Books directly to define variables of Books type without using struct keyword. Following is the example â
You can use typedef keyword for non-structs as well as follows â
x, y and z are all pointers to long ints.
The main purpose of C++ programming is to add object orientation to the C programming language and classes are the central feature of C++ that supports object-oriented programming and are often called user-defined types.
A class is used to specify the form of an object and it combines data 
representation and methods for manipulating that data into one neat package. The data and functions within a class are called members of the class.
When you define a class, you define a blueprint for a data type. This doesn't actually define any data, but it does define what the class name means, that is, what an object of the class will consist of and what operations can be performed 
on such an object.A class definition starts with the keyword class followed by the class name; and the class body, enclosed by a pair of curly braces. A class definition must be followed either by a semicolon or a list of declarations. For example, 
we defined the Box data type using the keyword class as follows â
The keyword public determines the access attributes of the members of the class that follows it. A public member can be accessed from outside the class anywhere within the scope of the class object. You can also specify the 
members of a class as private or protected which we will discuss in a sub-section.
A class provides the blueprints for objects, so basically an object is created from a class. We declare objects of a class with exactly the same sort of declaration that we declare variables of basic types. Following statements 
declare two objects of class Box â
Both of the objects Box1 and Box2 will have their own copy of data members.
The public data members of objects of a class can be accessed using the direct member access operator (.). Let us try the following example to make the things clear â
When the above code is compiled and executed, it produces the following 
result â
It is important to note that private and protected members can not be accessed directly using direct member access operator (.). We will learn how private and protected members can be accessed.
So far, you have got very basic idea about C++ Classes and Objects. There are further interesting concepts related to C++ Classes and Objects which we will discuss in various sub-sections listed below â
A member function of a class is a function that has its definition or its prototype within the class definition like any other variable.
A class member can be defined as public, private or protected. By default members would be assumed as private.
A class constructor is a special function in a class that is called when a new object of the class is created. A destructor is also a special function which is called when created object is deleted.
The copy constructor is a constructor which creates an object by initializing it with an object of the same class, which has been created previously.
A friend function is permitted full access to private and protected members of a class.
With an inline function, the compiler tries to expand the code in the body of the function in place of a call to the function.
Every object has a special pointer this which points to the object itself.
A pointer to a class is done exactly the same way a pointer to a structure is. In fact a class is really just a structure with functions in it.
Both data members and function members of a class can be declared as static.
One of the most important concepts in object-oriented programming is that of inheritance. Inheritance allows us to define a class in terms of another class, 
which makes it easier to create and maintain an application. This also provides an opportunity to reuse the code functionality and fast implementation time.
When creating a class, instead of writing completely new data members and member functions, the programmer can designate that the new class should inherit the members of an existing class. This existing class is called the base 
class, and the new class is referred to as the derived class.The idea of inheritance implements the is a relationship. For example, mammal IS-A animal, dog IS-A mammal hence dog IS-A animal as well and so on.
A class can be derived from more than one classes, which means it can inherit data and functions from multiple base classes. To define a derived class, we use a class derivation list to specify the base class(es). A class derivation list 
names one or more base classes and has the form â Where access-specifier is one of public, protected, or private, and base-class is the name of a previously defined class. If the access-specifier is not used, then it is private by default.
Consider a base class Shape and its derived class Rectangle as 
follows â
When the above code is compiled and executed, it produces the following 
result â
A derived class can access all the non-private members of its base class. 
Thus base-class members that should not be accessible to the member functions of derived classes should be declared private in the base class.
We can summarize the different access types according to - who can access them in the following way â
A derived class inherits all base class methods with the following exceptions 
â
When deriving a class from a base class, the base class may be inherited through public, protected or private inheritance. The type of inheritance is specified by the access-specifier as explained above.
We hardly use protected or private inheritance, but public inheritance is commonly used. While using different type of inheritance, 
following rules are applied â
Public Inheritance â When deriving a class from a public base class, public members of the base class become public members of the derived class and protected members of the base class become protected members of the derived class. A base class's 
private members are never accessible directly from a derived class, but can be accessed through calls to the public and protected members of the base class.
Protected Inheritance â When deriving from a protected base class, public and protected members of the base class become protected members of the derived class.
Private Inheritance â When deriving from a private base class, public and protected members of the base class become private members of the derived class.
A C++ class can inherit members from more than one class and here is the extended syntax â
Where access is one of public, protected, or private and would be given for every base class and they will be separated by comma as shown above. Let us try the following example â
When the above code is compiled and executed, it produces the following 
result â
C++ allows you to specify more than one definition for a function name or an operator in the same scope, which is called function overloading and operator overloading respectively.
An overloaded declaration is a declaration that is declared with the same name as a previously declared declaration in the same scope, except that both declarations have different arguments and obviously different definition (implementation).
When you call an overloaded function or operator, the compiler determines the most appropriate definition to use, by comparing the argument types you have used to call the function or operator with the parameter types 
specified in the definitions. The process of selecting the most appropriate overloaded function or operator is called overload resolution.
You can have multiple definitions for the same function name in the same scope. The definition of the function must differ from each other by the types and/or the number of arguments in the argument list. You cannot overload 
function declarations that differ only by return type.Following is the example where same function print() is being used to print different data types â
When the above code is compiled and executed, it produces the following result â
You can redefine or overload most of the built-in operators available in C++. 
Thus, a programmer can use operators with user-defined types as well.
Overloaded operators are functions with special names: the keyword "operator" followed by the symbol for the operator being defined. Like any other function, an overloaded operator has a return type and a parameter list.
declares the addition operator that can be used to add two Box objects and returns final Box object. Most overloaded operators may be defined as ordinary non-member functions or as class member functions. In case we define 
above function as non-member function of a class then we would have to pass two arguments for each operand as follows â
Following is the example to show the concept of operator over loading using a member function. Here an object is passed as an argument whose properties will 
be accessed using this object, the object which will call this operator can be accessed using this operator as explained below â
When the above code is compiled and executed, it produces the following result â
Following is the list of operators which can be overloaded â
Following is the list of operators, which can not be overloaded â
Here are various operator overloading examples to help you in understanding the concept.
The word polymorphism means having many forms. Typically, polymorphism occurs when there is a hierarchy of classes and they are related by inheritance.
C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.
Consider the following example where a base class has been derived by other 
two classes â
When the above code is compiled and executed, it produces the following 
result â
The reason for the incorrect output is that the call of the function area() is being set once by the compiler as the version defined in the base class. This is called static resolution of the function call, or static linkage - the function call is fixed before the program is executed. This is also 
sometimes called early binding because the area() function is set during the compilation of the program.
But now, let's make a slight modification in our program and precede the declaration of area() in the Shape class with the keyword virtual so that it looks like this â
After this slight modification, when the previous example code is compiled and executed, it produces the following result â
This time, the compiler looks at the contents of the pointer instead of it's type. Hence, since addresses of objects of tri and rec classes are stored in *shape the respective area() function is called.
As you can see, each of the child classes has a separate implementation for the function area(). This is how polymorphism is generally used. You have different classes with a function of the same name, and even the same 
parameters, but with different implementations.A virtual function is a function in a base class that is declared using the keyword virtual. Defining in a base class a virtual function, 
with another version in a derived class, signals to the compiler that we don't want static linkage for this function.
What we do want is the selection of the function to be called at any given point in the program to be based on the kind of object for which it is called. 
This sort of operation is referred to as dynamic linkage, or late binding.
It is possible that you want to include a virtual function in a base class so that it may be redefined in a derived class to suit the objects of that class, 
but that there is no meaningful definition you could give for the function in the base class.
We can change the virtual function area() in the base class to the following 
â
The = 0 tells the compiler that the function has no body and above virtual function will be called pure virtual function.
Data abstraction refers to providing only essential information to the outside world and hiding their background details, i.e., to represent the needed information in program without presenting the details.
Data abstraction is a programming (and design) technique that relies on the separation of interface and implementation.
Let's take one real life example of a TV, which you can turn on and off, 
change the channel, adjust the volume, and add external components such as speakers, VCRs, and DVD players, BUT you do not know its internal details, that is, you do not know how it receives signals over the air or through a cable, how 
it translates them, and finally displays them on the screen.
Thus, we can say a television clearly separates its internal implementation from its external interface and you can play with its interfaces like the power button, channel changer, and volume control without having zero knowledge of its 
internals.
In C++, classes provides great level of data abstraction. They provide sufficient public methods to the outside world to play with the functionality of the object and to manipulate object data, i.e., state without actually knowing 
how class has been implemented internally.
For example, your program can make a call to the sort() function without knowing what algorithm the function actually uses to sort the given values. In fact, the underlying implementation of the sorting functionality 
could change between releases of the library, and as long as the interface stays the same, your function call will still work.
In C++, we use classes to define our own abstract data types (ADT). 
You can use the cout object of class ostream to stream data to standard output like this â
Here, you don't need to understand how cout displays the text on the user's screen. You need to only know the public interface and the underlying implementation of âcoutâ is free to change.
In C++, we use access labels to define the abstract interface to the class. A 
class may contain zero or more access labels â
Members defined with a public label are accessible to all parts of the program. The data-abstraction view of a type is defined by its public members.
Members defined with a private label are not accessible to code that uses the class. The private sections hide the implementation from code that uses the type.
There are no restrictions on how often an access label may appear. Each access label specifies the access level of the succeeding member definitions. The specified access level remains in effect until the next access label is encountered or the closing right brace of the class body is seen.
Data abstraction provides two important advantages â
Class internals are protected from inadvertent user-level errors, which might corrupt the state of the object.
The class implementation may evolve over time in response to changing requirements or bug reports without requiring change in user-level code.
By defining data members only in the private section of the class, the class author is free to make changes in the data. If the implementation changes, only the class code needs to be examined to see what affect the change may have. If 
data is public, then any function that directly access the data members of the old representation might be broken.
Any C++ program where you implement a class with public and private members is an example of data abstraction. Consider the following example â
When the above code is compiled and executed, it produces the following 
result â
Above class adds numbers together, and returns the sum. The public members -
addNum and getTotal are the interfaces to the outside world and a user needs to know them to use the class. The private member total is something that the user doesn't need to know about, but is needed for the class to operate properly.
Abstraction separates code into interface and implementation. So while designing your component, you must keep interface independent of the implementation so that if you change underlying implementation then interface would remain intact.
In this case whatever programs are using these interfaces, they would not be impacted and would just need a recompilation with the latest implementation.
All C++ programs are composed of the following two fundamental elements â
Program statements (code) â This is the part of a program that performs actions and they are called functions.
Program data â The data is the information of the program which gets affected by the program functions.
Encapsulation is an Object Oriented Programming concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse. Data encapsulation led to the important OOP concept of data hiding.
Data encapsulation is a mechanism of bundling the data, and the functions that use them and data abstraction is a mechanism of exposing only the interfaces and hiding the implementation details from the user.
C++ supports the properties of encapsulation and data hiding through the creation of user-defined types, called classes. We already have studied that a class can contain private, protected and public members. By 
default, all items defined in a class are private. For example â
The variables length, breadth, and height are private. This means that they can be accessed only by other members of the Box class, and not by any other part of your program. This is one way encapsulation is achieved.
To make parts of a class public (i.e., accessible to other parts of your program), you must declare them after the public keyword. All variables or functions defined after the public specifier are accessible by all 
other functions in your program.
Making one class a friend of another exposes the implementation details and reduces encapsulation. The ideal is to keep as many of the details of each class hidden from all other classes as possible.
Any C++ program where you implement a class with public and private members is an example of data encapsulation and data abstraction. Consider the following 
example â
When the above code is compiled and executed, it produces the following result â
Above class adds numbers together, and returns the sum. The public members addNum and getTotal are the interfaces to the outside world and a user needs to know them to use the class. The private member total is 
something that is hidden from the outside world, but is needed for the class to operate properly.
Most of us have learnt to make class members private by default unless we really need to expose them. That's just good encapsulation.
This is applied most frequently to data members, but it applies equally to all members, including virtual functions.
An interface describes the behavior or capabilities of a C++ class without committing to a particular implementation of that class.
The C++ interfaces are implemented using abstract classes and these abstract classes should not be confused with data abstraction which is a concept of keeping implementation details separate from associated data.
A class is made abstract by declaring at least one of its functions as pure virtual function. A pure virtual function is specified by placing "= 0" in its declaration as follows â
The purpose of an abstract class (often referred to as an ABC) is to provide an appropriate base class from which other classes can inherit. Abstract classes cannot be used to instantiate objects and serves only as an interface. 
Attempting to instantiate an object of an abstract class causes a compilation error.
Thus, if a subclass of an ABC needs to be instantiated, it has to implement each of the virtual functions, which means that it supports the interface declared by the ABC. Failure to override a pure virtual function in a derived 
class, then attempting to instantiate objects of that class, is a compilation error.
Classes that can be used to instantiate objects are called concrete classes.
Consider the following example where parent class provides an interface to the base class to implement a function called getArea() â
When the above code is compiled and executed, it produces the following
result â
You can see how an abstract class defined an interface in terms of getArea() and two other classes implemented same function but with different algorithm to calculate the area specific to the shape.
An object-oriented system might use an abstract base class to provide a common and standardized interface appropriate for all the external applications. 
Then, through inheritance from that abstract base class, derived classes are formed that operate similarly.
The capabilities (i.e., the public functions) offered by the external applications are provided as pure virtual functions in the abstract base class. 
The implementations of these pure virtual functions are provided in the derived classes that correspond to the specific types of the application.
This architecture also allows new applications to be added to a system easily, even after the system has been defined.
So far, we have been using the iostream standard library, which provides cin and cout methods for reading from standard input and writing to standard output respectively.
This tutorial will teach you how to read and write from a file. This requires another standard C++ library called fstream, which defines three new data 
types â
ofstream
This data type represents the output file stream and is used to create files and to write information to files.
ifstream
This data type represents the input file stream and is used to read information from files.
fstream
This data type represents the file stream generally, and has the capabilities of both ofstream and ifstream which means it can create files, write information to files, and read information from files.
To perform file processing in C++, header files <iostream> and <fstream> must be included in your C++ source file.
A file must be opened before you can read from it or write to it. Either ofstream or fstream object may be used to open a file for writing. 
And ifstream object is used to open a file for reading purpose only.
Following is the standard syntax for open() function, which is a member of fstream, ifstream, and ofstream objects.
Here, the first argument specifies the name and location of the file to be opened and the second argument of the open() member function defines the mode in which the file should be opened.
ios::app
Append mode. All output to that file to be appended to the end.
ios::ate
Open a file for output and move the read/write control to the end of the file.
ios::in
Open a file for reading.
ios::out
Open a file for writing.
ios::trunc
If the file already exists, its contents will be truncated before opening the file.
You can combine two or more of these values by ORing them together. 
For example if you want to open a file in write mode and want to truncate it in 
case that already exists, following will be the syntax â
Similar way, you can open a file for reading and writing purpose as follows â
When a C++ program terminates it automatically flushes all the streams, release all the allocated memory and close all the opened files. But it is always a good practice that a programmer should close all the opened files before program termination.
Following is the standard syntax for close() function, which is a member of 
fstream, ifstream, and ofstream objects.
While doing C++ programming, you write information to a file from your program using the stream insertion operator (<<) just as you use that operator to output information to the screen. The only difference is that you use an 
ofstream or fstream object instead of the cout object.
You read information from a file into your program using the stream extraction operator (>>) just as you use that operator to input information from the keyboard. The only difference is that you use an ifstream or fstream object instead of the cin object.
Following is the C++ program which opens a file in reading and writing mode. 
After writing information entered by the user to a file named afile.dat, the program reads information from the file and outputs it onto the screen â
When the above code is compiled and executed, it produces the following sample input and output â
Above examples make use of additional functions from cin object, like getline() function to read the line from outside and ignore() function to ignore the extra characters left by previous read statement.
Both istream and ostream provide member functions for repositioning the file-position pointer. These member functions are seekg ("seek get") for istream and seekp ("seek put") for ostream.
The argument to seekg and seekp normally is a long integer. A second argument can be specified to indicate the seek direction. The seek direction can be ios::beg (the default) for positioning relative to the beginning of a 
stream, ios::cur for positioning relative to the current position in a stream or ios::end for positioning relative to the end of a stream.
The file-position pointer is an integer value that specifies the location in the file as a number of bytes from the file's starting location. Some examples of positioning the "get" file-position pointer are â
An exception is a problem that arises during the execution of a program. A C++ exception is a response to an exceptional circumstance that arises while a program is running, such as an attempt to divide by zero.
Exceptions provide a way to transfer control from one part of a program to another. C++ exception handling is built upon three keywords: try, catch, and throw.
throw â A program throws an exception when a problem shows up. This is done using a throw keyword.
catch â A program catches an exception with an exception handler at the place in a program where you want to handle the problem. The catch keyword indicates the catching of an exception.
try â A try block identifies a block of code for which particular exceptions will be activated. It's followed by one or more catch blocks.
Assuming a block will raise an exception, a method catches an exception using a combination of the try and catch keywords. A try/catch block is placed around the code that might generate an exception. Code within a try/catch 
block is referred to as protected code, and the syntax for using try/catch as follows â
You can list down multiple catch statements to catch different type of exceptions in case your try block raises more than one exception in different situations.
Exceptions can be thrown anywhere within a code block using throw statement. The operand of the throw statement determines a type for the exception and can be any expression and the type of the result of the expression determines the type of exception thrown.
Following is an example of throwing an exception when dividing by zero condition occurs â
The catch block following the try block catches any exception. 
You can specify what type of exception you want to catch and this is determined by the exception declaration that appears in parentheses following the keyword catch.
Above code will catch an exception of ExceptionName type. If you want to specify that a catch block should handle any type of exception that is thrown in a try block, you must put an ellipsis, ..., between the parentheses enclosing 
the exception declaration as follows âThe following is an example, which throws a division by zero exception and we 
catch it in catch block.Because we are raising an exception of type const char*, so while catching this exception, we have to use const char* in catch block. If we compile and run above code, this would produce the following result â
C++ provides a list of standard exceptions defined in <exception> 
which we can use in our programs. These are arranged in a parent-child class hierarchy shown below â
Here is the small description of each exception mentioned in the above hierarchy â
std::exception
An exception and parent class of all the standard C++ exceptions.
std::bad_alloc
This can be thrown by new.
std::bad_cast
This can be thrown by dynamic_cast.
std::bad_exception
This is useful device to handle unexpected exceptions in a C++ program.
std::bad_typeid
This can be thrown by typeid.
std::logic_error
An exception that theoretically can be detected by reading the code.
std::domain_error
This is an exception thrown when a mathematically invalid domain is used.
std::invalid_argument
This is thrown due to invalid arguments.
std::length_error
This is thrown when a too big std::string is created.
std::out_of_range
This can be thrown by the 'at' method, for example a std::vector and 
std::bitset<>::operator[]().
std::runtime_error
An exception that theoretically cannot be detected by reading the code.
std::overflow_error
This is thrown if a mathematical overflow occurs.
std::range_error
This is occurred when you try to store a value which is out of range.
std::underflow_error
This is thrown if a mathematical underflow occurs.
You can define your own exceptions by inheriting and overriding exception class functionality. Following is the example, which shows how you can use 
std::exception class to implement your own exception in standard way â
This would produce the following result â
Here, what() is a public method provided by exception class and it has been overridden by all the child exception classes. This returns the cause of an exception.
A good understanding of how dynamic memory really works in C++ is essential to becoming a good C++ programmer. Memory in your C++ program is divided into two parts â
The stack â All variables declared inside the function will take up memory from the stack.
The heap â This is unused memory of the program and can be used to allocate the memory dynamically when program runs.
Many times, you are not aware in advance how much memory you will need to store particular information in a defined variable and the size of required memory can be determined at run time.
You can allocate memory at run time within the heap for the variable of a given type using a special operator in C++ which returns the address of the space allocated. This operator is called new operator.
If you are not in need of dynamically allocated memory anymore, you can use delete operator, which de-allocates memory that was previously allocated by new operator.
There is following generic syntax to use new operator to allocate memory dynamically for any data-type.
Here, data-type could be any built-in data type including an array or any user defined data types include class or structure. Let us start with built-in data types. For example we can define a pointer to type double and then 
request that the memory be allocated at execution time. We can do this using the new operator with the following statements â
The memory may not have been allocated successfully, if the free store had been used up. So it is good practice to check if new operator is returning NULL pointer and take appropriate action as below â
The malloc() function from C, still exists in C++, but it is recommended to avoid using malloc() function. The main advantage of new over malloc() is that new doesn't just allocate memory, it constructs objects which 
is prime purpose of C++.At any point, when you feel a variable that has been dynamically allocated is not anymore required, you can free up the memory that it occupies in the free store with the âdeleteâ operator as follows â
Let us put above concepts and form the following example to show how ânewâ and âdeleteâ work â
If we compile and run above code, this would produce the following result â
Consider you want to allocate memory for an array of characters, i.e., string of 20 characters. Using the same syntax what we have used above we can allocate memory dynamically as shown below.
To remove the array that we have just created the statement would look like this â
Following the similar generic syntax of new operator, you can allocate for a multi-dimensional array as follows â
However, the syntax to release the memory for multi-dimensional array will still remain same as above â
Objects are no different from simple data types. For example, consider the following code where we are going to use an array of objects to clarify the concept â
If you were to allocate an array of four Box objects, the Simple constructor would be called four times and similarly while deleting these objects, destructor will also be called same number of times.
If we compile and run above code, this would produce the following result â
Consider a situation, when we have two persons with the same name, Zara, in 
the same class. Whenever we need to differentiate them definitely we would have to use some additional information along with their name, like either the area, if they live in different area or their motherâs or fatherâs name, etc.
Same situation can arise in your C++ applications. For example, you might be writing some code that has a function called xyz() and there is another library available which is also having same function xyz(). Now the compiler has no way 
of knowing which version of xyz() function you are referring to within your code.
A namespace is designed to overcome this difficulty and is used as additional information to differentiate similar functions, classes, variables etc. with the same name available in different libraries. Using namespace, you 
can define the context in which names are defined. In essence, a namespace defines a scope.
A namespace definition begins with the keyword namespace followed by the namespace name as follows â
To call the namespace-enabled version of either function or variable, prepend 
(::) the namespace name as follows â
Let us see how namespace scope the entities including variable and functions 
â
If we compile and run above code, this would produce the following result â
You can also avoid prepending of namespaces with the using namespace directive. This directive tells the compiler that the subsequent code is making use of names in the specified namespace. The namespace is thus implied for the 
following code â
If we compile and run above code, this would produce the following result â
The âusingâ directive can also be used to refer to a particular item within a namespace. For example, if the only part of the std namespace that you intend to use is cout, you can refer to it as follows â
Subsequent code can refer to cout without prepending the namespace, but other items in the std namespace will still need to be explicit as follows â
If we compile and run above code, this would produce the following result â
Names introduced in a using directive obey normal scope rules. The name is visible from the point of the using directive to the end of the scope in which the directive is found. Entities with the same name defined in an outer scope are hidden.
A namespace can be defined in several parts and so a namespace is made up of the sum of its separately defined parts. The separate parts of a namespace can be spread over multiple files.
So, if one part of the namespace requires a name defined in another file, that name must still be declared. Writing a following namespace definition either defines a new namespace or adds new elements to an existing one â
Namespaces can be nested where you can define one namespace inside another 
name space as follows â
You can access members of nested namespace by using resolution operators as follows â
In the above statements if you are using namespace_name1, then it will make elements of namespace_name2 available in the scope as follows â
If we compile and run above code, this would produce the following result â
Templates are the foundation of generic programming, which involves writing 
code in a way that is independent of any particular type.
A template is a blueprint or formula for creating a generic class or a function. The library containers like iterators and algorithms are examples of generic programming and have been developed using template concept.
There is a single definition of each container, such as vector, but we can define many different kinds of vectors for example, vector <int> orvector <string>.
You can use templates to define functions as well as classes, let us see how they work â
The general form of a template function definition is shown here â
Here, type is a placeholder name for a data type used by the function. This name can be used within the function definition.
The following is the example of a function template that returns the maximum of two values â
If we compile and run above code, this would produce the following result â
Just as we can define function templates, we can also define class templates. The general form of a generic class declaration is shown here â
Here, type is the placeholder type name, which will be specified when a class is instantiated. You can define more than one generic data type by using a comma-separated list.
Following is the example to define class Stack<> and implement generic methods to push and pop the elements from the stack â
If we compile and run above code, this would produce the following result â
The preprocessors are the directives, which give instructions to the compiler to preprocess the information before actual compilation starts.
All preprocessor directives begin with #, and only white-space characters may appear before a preprocessor directive on a line. Preprocessor directives are not C++ statements, so they do not end in a semicolon (;).
You already have seen a #include directive in all the examples. This macro is used to include a header file into the source file.
There are number of preprocessor directives supported by C++ like #include, #define, #if, #else, #line, etc. Let us see important directives â
The #define preprocessor directive creates symbolic constants. The symbolic constant is called a macro and the general form of the directive is â
When this line appears in a file, all subsequent occurrences of macro in that file will be replaced by replacement-text before the program is compiled. For 
example â
Now, let us do the preprocessing of this code to see the result assuming we have the source code file. So let us compile it with -E option and redirect the result to test.p. Now, if you check test.p, it will have lots of information and 
at the bottom, you will find the value replaced as follows â
You can use #define to define a macro which will take argument as follows â
If we compile and run above code, this would produce the following result â
There are several directives, which can be used to compile selective portions of your program's source code. This process is called conditional compilation.
The conditional preprocessor construct is much like the âifâ selection structure. Consider the following preprocessor code â
You can compile a program for debugging purpose. You can also turn on or off the debugging using a single macro as follows â
This causes the cerr statement to be compiled in the program if the symbolic constant DEBUG has been defined before directive #ifdef DEBUG. You can use #if 0 statment to comment out a portion of the program as follows â
Let us try the following example â
If we compile and run above code, this would produce the following result â
The # and ## preprocessor operators are available in C++ and ANSI/ISO C. The # operator causes a replacement-text token to be converted to a string surrounded by quotes.
Consider the following macro definition â
If we compile and run above code, this would produce the following result â
Let us see how it worked. It is simple to understand that the C++ preprocessor turns the line â
Above line will be turned into the following line â
The ## operator is used to concatenate two tokens. Here is an example â
When CONCAT appears in the program, its arguments are concatenated and used to replace the macro. For example, CONCAT(HELLO, C++) is replaced by "HELLO C++" in the program as follows.
If we compile and run above code, this would produce the following result â
Let us see how it worked. It is simple to understand that the C++ preprocessor transforms â
Above line will be transformed into the following line â
C++ provides a number of predefined macros mentioned below â
__LINE__
This contains the current line number of the program when it is being compiled.
__FILE__
This contains the current file name of the program when it is being compiled.
__DATE__
This contains a string of the form month/day/year that is the date of the translation of the source file into object code.
__TIME__
This contains a string of the form hour:minute:second that is the time at which the program was compiled.
Let us see an example for all the above macros â
If we compile and run above code, this would produce the following result â
Signals are the interrupts delivered to a process by the operating system which can terminate a program prematurely. You can generate interrupts by pressing Ctrl+C on a UNIX, LINUX, Mac OS X or Windows system.
There are signals which can not be caught by the program but there is a following list of signals which you can catch in your program and can take appropriate actions based on the signal. These signals are defined in C++ header file <csignal>.
SIGABRT
Abnormal termination of the program, such as a call to abort.
SIGFPE
An erroneous arithmetic operation, such as a divide by zero or an operation resulting in overflow.
SIGILL
Detection of an illegal instruction.
SIGINT
Receipt of an interactive attention signal.
SIGSEGV
An invalid access to storage.
SIGTERM
A termination request sent to the program.
C++ signal-handling library provides function signal to trap unexpected events. Following is the syntax of the signal() function â
Keeping it simple, this function receives two arguments: first argument as an integer which represents signal number and second argument as a pointer to the signal-handling function.
Let us write a simple C++ program where we will catch SIGINT signal using signal() function. Whatever signal you want to catch in your program, you must register that signal using signal function and associate it with a signal 
handler. Examine the following example â
When the above code is compiled and executed, it produces the following 
result â
Now, press Ctrl+c to interrupt the program and you will see that your program will catch the signal and would come out by printing something as follows â
You can generate signals by function raise(), which takes an integer signal number as an argument and has the following syntax.
Here, sig is the signal number to send any of the signals: SIGINT, SIGABRT, SIGFPE, SIGILL, SIGSEGV, SIGTERM, SIGHUP. Following is the example 
where we raise a signal internally using raise() function as follows â
When the above code is compiled and executed, it produces the following result and would come out automatically â
Multithreading is a specialized form of multitasking and a multitasking is the feature that allows your computer to run two or more programs concurrently. 
In general, there are two types of multitasking: process-based and thread-based.
Process-based multitasking handles the concurrent execution of programs. Thread-based multitasking deals with the concurrent execution of pieces of the same program.
A multithreaded program contains two or more parts that can run concurrently. Each part of such a program is called a thread, and each thread defines a separate path of execution.
C++ does not contain any built-in support for multithreaded applications. Instead, it relies entirely upon the operating system to provide this feature.
This tutorial assumes that you are working on Linux OS and we are going to write multi-threaded C++ program using POSIX. POSIX Threads, or Pthreads provides API which are available on many Unix-like POSIX systems such as 
FreeBSD, NetBSD, GNU/Linux, Mac OS X and Solaris.
The following routine is used to create a POSIX thread â
Here, pthread_create creates a new thread and makes it executable. 
This routine can be called any number of times from anywhere within your code. 
Here is the description of the parameters â
thread
An opaque, unique identifier for the new thread returned by the subroutine.
attr
An opaque attribute object that may be used to set thread attributes. You can specify a thread attributes object, or NULL for the default values.
start_routine
The C++ routine that the thread will execute once it is created.
arg
A single argument that may be passed to start_routine. It must be passed by reference as a pointer cast of type void. NULL may be used if no argument is to be passed.
The maximum number of threads that may be created by a process is implementation dependent. Once created, threads are peers, and may create other threads. There is no implied hierarchy or dependency between threads.
There is following routine which we use to terminate a POSIX thread â
Here pthread_exit is used to explicitly exit a thread. Typically, the pthread_exit() routine is called after a thread has completed its work and is no longer required to exist.
If main() finishes before the threads it has created, and exits with 
pthread_exit(), the other threads will continue to execute. Otherwise, they will be automatically terminated when main() finishes.
Example
This simple example code creates 5 threads with the pthread_create() routine. 
Each thread prints a "Hello World!" message, and then terminates with a call to pthread_exit().
Compile the following program using -lpthread library as follows â
Now, execute your program which gives the following output â
This example shows how to pass multiple arguments via a structure. You can pass any data type in a thread callback because it points to void as explained in the following example â
When the above code is compiled and executed, it produces the following result â
There are following two routines which we can use to join or detach threads â
The pthread_join() subroutine blocks the calling thread until the specified threadid thread terminates. When a thread is created, one of its attributes defines whether it is joinable or detached. Only threads that are created as 
joinable can be joined. If a thread is created as detached, it can never be joined.
This example demonstrates how to wait for thread completions by using the Pthread join routine.
When the above code is compiled and executed, it produces the following result â
The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged between the web server and a custom script.
The CGI specs are currently maintained by the NCSA and NCSA defines CGI is as follows â
The Common Gateway Interface, or CGI, is a standard for external gateway programs to interface with information servers such as HTTP servers.
The current version is CGI/1.1 and CGI/1.2 is under progress.
To understand the concept of CGI, let's see what happens when we click a hyperlink to browse a particular web page or URL.
Your browser contacts the HTTP web server and demand for the URL ie. filename.
Web Server will parse the URL and will look for the filename. If it finds requested file then web server sends that file back to the browser otherwise sends an error message indicating that you have requested a wrong file.Web browser takes response from web server and displays either the 
received file or error message based on the received response.
However, it is possible to set up the HTTP server in such a way that whenever a file in a certain directory is requested, that file is not sent back; instead it is executed as a program, and produced output from the program is sent back 
to your browser to display.
The Common Gateway Interface (CGI) is a standard protocol for enabling applications (called CGI programs or CGI scripts) to interact with Web servers and with clients. These CGI programs can be a written in Python, PERL, Shell, C or C++ etc.
The following simple program shows a simple architecture of CGI â
Before you proceed with CGI Programming, make sure that your Web Server supports CGI and it is configured to handle CGI Programs. All the CGI Programs to be executed by the HTTP server are kept in a pre-configured directory. This directory is called CGI directory and by convention it is named as /var/www/cgi-bin. By convention CGI files will have extension as .cgi, 
though they are C++ executable.
By default, Apache Web Server is configured to run CGI programs in /var/www/cgi-bin. If you want to specify any other directory to run your CGI scripts, you can modify the following section in the httpd.conf file â
Here, I assume that you have Web Server up and running successfully and you are able to run any other CGI program like Perl or Shell etc.
Consider the following C++ Program content â
Compile above code and name the executable as cplusplus.cgi. This file is being kept in /var/www/cgi-bin directory and it has following content. Before running your CGI program make sure you have change mode of file using chmod 
755 cplusplus.cgi UNIX command to make file executable.The above C++ program is a simple program which is writing its output on STDOUT file i.e. screen. There is one important and extra feature available which is first line printing Content-type:text/html\r\n\r\n. This line is 
sent back to the browser and specify the content type to be displayed on the browser screen. Now you must have understood the basic concept of CGI and you can write many complicated CGI programs using Python. A C++ CGI program can 
interact with any other external system, such as RDBMS, to exchange information.The line Content-type:text/html\r\n\r\n is a part of HTTP header, which is sent to the browser to understand the content. All the HTTP header will 
be in the following form âThere are few other important HTTP headers, which you will use frequently in your CGI Programming.
Content-type:
A MIME string defining the format of the file being returned. Example is Content-type:text/html.
Expires: Date
The date the information becomes invalid. This should be used by the browser to decide when a page needs to be refreshed. A valid date string should be in the format 01 Jan 1998 12:00:00 GMT.
Location: URL
The URL that should be returned instead of the URL requested. You can use this filed to redirect a request to any file.
Last-modified: Date
The date of last modification of the resource.
Content-length: N
The length, in bytes, of the data being returned. The browser uses this value to report the estimated download time for a file.
Set-Cookie: String
Set the cookie passed through the string.
All the CGI program will have access to the following environment variables. 
These variables play an important role while writing any CGI program.
CONTENT_TYPE
The data type of the content, used when the client is sending attached content to the server. For example file upload etc.
CONTENT_LENGTH
The length of the query information that is available only for POST requests.
HTTP_COOKIE
Returns the set cookies in the form of key & value pair.
HTTP_USER_AGENT
The User-Agent request-header field contains information about the user agent originating the request. It is a name of the web browser.
PATH_INFO
The path for the CGI script.
QUERY_STRING
The URL-encoded information that is sent with GET method request.
REMOTE_ADDR
The IP address of the remote host making the request. This can be useful for logging or for authentication purpose.
REMOTE_HOST
The fully qualified name of the host making the request. If this information is not available then REMOTE_ADDR can be used to get IR address.
REQUEST_METHOD
The method used to make the request. The most common methods are GET and POST.
SCRIPT_FILENAME
The full path to the CGI script.
SCRIPT_NAME
The name of the CGI script.
SERVER_NAME
The server's hostname or IP Address.
SERVER_SOFTWARE
The name and version of the software the server is running.
Here is small CGI program to list out all the CGI variables.
For real examples, you would need to do many operations by your CGI program. 
There is a CGI library written for C++ program which you can download fromftp://ftp.gnu.org/gnu/cgicc/ and follow the steps to install the library â
You can check related documentation available atâC++ CGI Lib Documentation.
You must have come across many situations when you need to pass some information from your browser to web server and ultimately to your CGI Program. 
Most frequently browser uses two methods to pass this information to web server. 
These methods are GET Method and POST Method.
The GET method sends the encoded user information appended to the page request. The page and the encoded information are separated by the ? character as follows â
The GET method is the default method to pass information from browser to web server and it produces a long string that appears in your browser's 
Location:box. Never use the GET method if you have password or other sensitive information to pass to the server. The GET method has size limitation and you can pass upto 1024 characters in a request string.
When using GET method, information is passed using QUERY_STRING http header and will be accessible in your CGI Program through QUERY_STRING environment variable.
You can pass information by simply concatenating key and value pairs alongwith any URL or you can use HTML <FORM> tags to pass information using GET method.
Here is a simple URL which will pass two values to hello_get.py program using GET method.
Below is a program to generate cpp_get.cgi CGI program to handle input given by web browser. We are going to use C++ CGI library which makes it very easy to access passed information â
Now, compile the above program as follows â
Generate cpp_get.cgi and put it in your CGI directory and try to access usingfollowing link â
This would generate following result â
Here is a simple example which passes two values using HTML FORM and submit button. We are going to use same CGI script cpp_get.cgi to handle this input.
Here is the actual output of the above form. You enter First and Last Name and then click submit button to see the result.
A generally more reliable method of passing information to a CGI program is the POST method. This packages the information in exactly the same way as GET methods, but instead of sending it as a text string after a ? in the URL it 
sends it as a separate message. This message comes into the CGI script in the form of the standard input.
The same cpp_get.cgi program will handle POST method as well. Let us take same example as above, which passes two values using HTML FORM and submit button but this time with POST method as follows â
Here is the actual output of the above form. You enter First and Last Name and then click submit button to see the result.
Checkboxes are used when more than one option is required to be selected.
Here is example HTML code for a form with two checkboxes â
The result of this code is the following form â
Below is C++ program, which will generate cpp_checkbox.cgi script to handle input given by web browser through checkbox button.
Radio Buttons are used when only one option is required to be selected.
Here is example HTML code for a form with two radio button â
The result of this code is the following form â
Below is C++ program, which will generate cpp_radiobutton.cgi script to handle input given by web browser through radio buttons.TEXTAREA element is used when multiline text has to be passed to the CGI 
Program.
Here is example HTML code for a form with a TEXTAREA box â
The result of this code is the following form â
Below is C++ program, which will generate cpp_textarea.cgi script to handle input given by web browser through text area.
Drop down Box is used when we have many options available but only one or two will be selected.
Here is example HTML code for a form with one drop down box â
The result of this code is the following form â
Below is C++ program, which will generate cpp_dropdown.cgi script to handle input given by web browser through drop down box.
HTTP protocol is a stateless protocol. But for a commercial website it is required to maintain session information among different pages. For example one user registration ends after completing many pages. But how to maintain user's 
session information across all the web pages.
In many situations, using cookies is the most efficient method of remembering and tracking preferences, purchases, commissions, and other information required for better visitor experience or site statistics.
Your server sends some data to the visitor's browser in the form of a cookie. The browser may accept the cookie. If it does, it is stored as a plain text record on the visitor's hard drive. Now, when the visitor arrives at another 
page on your site, the cookie is available for retrieval. Once retrieved, your 
server knows/remembers what was stored.
Cookies are a plain text data record of 5 variable-length fields â
Expires â This shows date the cookie will expire. If this is blank, the cookie will expire when the visitor quits the browser.
Domain â This shows domain name of your site.
Path â This shows path to the directory or web page that set the cookie. This may be blank if you want to retrieve the cookie from any directory or page.
Secure â If this field contains the word "secure" then the cookie may only be retrieved with a secure server. If this field is blank, no such restriction exists.
Name = Value â Cookies are set and retrieved in the form of key and value pairs.
It is very easy to send cookies to browser. These cookies will be sent along with HTTP Header before the Content-type filed. Assuming you want to set UserID 
and Password as cookies. So cookies setting will be done as follows From this example, you must have understood how to set cookies. We use 
Set-Cookie HTTP header to set cookies.
Here, it is optional to set cookies attributes like Expires, Domain, and 
Path. It is notable that cookies are set before sending magic line "Content-type:text/html\r\n\r\n.
Compile above program to produce setcookies.cgi, and try to set cookies using 
following link. It will set four cookies at your computer â/cgi-bin/setcookies.cgi
It is easy to retrieve all the set cookies. Cookies are stored in CGI environment variable HTTP_COOKIE and they will have following form.
Here is an example of how to retrieve cookies.
Now, compile above program to produce getcookies.cgi, and try to get a list of all the cookies available at your computer â/cgi-bin/getcookies.cgi
This will produce a list of all the four cookies set in previous section and all other cookies set in your computer â
To upload a file the HTML form must have the enctype attribute set to multipart/form-data. The input tag with the file type will create a "Browse" button.
The result of this code is the following form â
File:
Note â Above example has been disabled intentionally to stop people 
uploading files on our server. But you can try above code with your server.
Here is the script cpp_uploadfile.cpp to handle file upload â
The above example is for writing content at cout stream but you can 
open your file stream and save the content of uploaded file in a file at desired location.
"""
insertRecipeData("CPP", cppData.replace("\n", " "))
# CSS
dsData= """
The term DSA stands for Data Structures and Algorithms. As the name itself suggests, it is a combination of two separate yet interrelated topics – Data Structure and Algorithms.
Introduction to Data Structures and Algorithms (DSA)
Topics
A data structure is defined as a particular way of storing and organizing data in our devices to use the data efficiently and effectively. The main idea behind using data structures is to minimize the time and space complexities. An efficient data structure takes minimum memory space and requires minimum time to execute the data.
Algorithm is defined as a process or set of well-defined instructions that are typically used to solve a particular group of problems or perform a specific type of calculation. To explain in simpler terms, it is a set of operations performed in a step-by-step manner to execute a task.
The first and foremost thing is dividing the total procedure into little pieces which need to be done sequentially.
The complete process to learn DSA from scratch can be broken into 4 parts:
Here comes one of the interesting and important topics. The primary motive to use DSA is to solve a problem effectively and efficiently. How can you decide if a program written by you is efficient or not? This is measured by complexities. Complexity is of two types:
Both of the above complexities are measured with respect to the input parameters. But here arises a problem. The time required for executing a code depends on several factors, such as: 
So how can we determine which one is efficient? The answer is the use of asymptotic notation. 
Asymptotic notation is a mathematical tool that calculates the required time in terms of input size and does not require the execution of the code. 
It neglects the system-dependent constants and is related to only the number of modular operations being performed in the whole program. The following 3 asymptotic notations are mostly used to represent the time complexity of algorithms:
Rate of Growth of Algorithms.The most used notation in the analysis of a code is the Big O Notation which gives an upper bound of the running time of the code (or the amount of memory used in terms of input size).
To learn about complexity analysis in detail, you can refer to our complete set of articles on the Analysis of Algorithms.
Here comes the most crucial and the most awaited stage of the roadmap for learning data structure and algorithm – the stage where you start learning about DSA. The topic of DSA consists of two parts: 
Though they are two different things, they are highly interrelated, and it is very important to follow the right track to learn them most efficiently. If you are confused about which one to learn first, we recommend you to go through our detailed analysis on the topic: What should I learn first- Data Structures or Algorithms?
Here we have followed the flow of learning a data structure and then the most related and important algorithms used by that data structure.
The most basic yet important data structure is the array. It is a linear data structure. An array is a collection of homogeneous data types where the elements are allocated contiguous memory. Because of the contiguous allocation of memory, any element of an array can be accessed in constant time. Each array element has a corresponding index number. 
Array Data Structure
To learn more about arrays, refer to the article “Introduction to Arrays“.
Here are some topics about array which you must learn:
Related posts:A string is also a type of array. It can be interpreted as an array of characters. But it has some special characteristics like the last character of a string is a null character to denote the end of the string. Also, there are some unique operations, like concatenation which concatenates two strings into one.
String Data Structure
Here we are providing you with some must-know concepts of string:
Related posts:As the above data structures, the linked list is also a linear data structure. But Linked List is different from Array in its configuration. It is not allocated to contiguous memory locations. Instead, each node of the linked list is allocated to some random memory space and the previous node maintains a pointer that points to this node. So no direct memory access of any node is possible and it is also dynamic i.e., the size of the linked list can be adjusted at any time. To learn more about linked lists refer to the article “Introduction to Linked List“.
Linked List Data Structure
The topics which you must want to cover are:
Related posts:A matrix represents a collection of numbers arranged in an order of rows and columns. It is necessary to enclose the elements of a matrix in parentheses or brackets.
For example:A matrix with 9 elements is shown below.This Matrix [M] has 3 rows and 3 columns. Each element of matrix [M] can be referred to by its row and column number. For example, a23 = 6.
Related posts:Now you should move to some more complex data structures, such as Stack and Queue. 
Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).
Stack Data Structure
The reason why Stack is considered a complex data structure is that it uses other data structures for implementation, such as Arrays, Linked lists, etc. based on the characteristics and features of Stack data structure.
Related posts:Another data structure that is similar to Stack, yet different in its characteristics, is Queue.
A Queue is a linear structure which follows First In First Out (FIFO) approach in its individual operations.
Queue Data Structure A queue can be of different types like 
Related posts:A Heap is a special Tree-based Data Structure in which the tree is a complete binary tree.
Types of heaps:Generally, heaps are of two types.
Max-Heap: In this heap, the value of the root node must be the greatest among all its child nodes and the same thing must be done for its left and right sub-tree also.
Min-Heap: In this heap, the value of the root node must be the smallest among all its child nodes and the same thing must be done for its left ans right sub-tree also.
Types of Heap Data Structure
Related posts:Hashing refers to the process of generating a fixed-size output from an input of variable size using the mathematical formulas known as hash functions. This technique determines an index or location for the storage of an item in a data structure.
What is Hashing
Related posts:After having the basics covered about the linear data structure, now it is time to take a step forward to learn about the non-linear data structures. The first non-linear data structure you should learn is the tree. 
Tree data structure is similar to a tree we see in nature but it is upside down. It also has a root and leaves. The root is the first node of the tree and the leaves are the ones at the bottom-most level. The special characteristic of a tree is that there is only one path to go from any of its nodes to any other node.
Tree Data Structure Based on the maximum number of children of a node of the tree it can be – 
Based on the configuration of nodes there are also several classifications. Some of them are:
Related posts:Another important non-linear data structure is the graph. It is similar to the Tree data structure, with the difference that there is no particular root or leaf node, and it can be traversed in any order.
A Graph is a non-linear data structure consisting of a finite set of vertices(or nodes) and a set of edges that connect a pair of nodes. 
Graph Data Structure
Each edge shows a connection between a pair of nodes. This data structure helps solve many real-life problems. Based on the orientation of the edges and the nodes there are various types of graphs. 
Here are some must to know concepts of graphs:
Related posts:Once you have cleared the concepts of Data Structures, now its time to start your journey through the Algorithms. Based on the type of nature and usage, the Algorithms are grouped together into several categories, as shown below:
Now we have learned about some linear data structures and is time to learn about some basic and most used algorithms which are hugely used in these types of data structures. One such algorithm is the searching algorithm. 
Searching algorithms are used to find a specific element in an array, string, linked list, or some other data structure. 
The most common searching algorithms are: Besides these, there are other searching algorithms also like 
Here is one other most used algorithm. Often we need to arrange or sort data as per a specific condition. The sorting algorithm is the one that is used in these cases. Based on conditions we can sort a set of homogeneous data in order like sorting an array in increasing or decreasing order. 
Sorting Algorithm is used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure.
An example to show Sorting There are a lot of different types of sorting algorithms. Some widely used algorithms are:
There are several other sorting algorithms also and they are beneficial in different cases. You can learn about them and more in our dedicated article on Sorting algorithms.
This is one interesting and important algorithm to be learned in your path of programming. As the name suggests, it breaks the problem into parts, then solves each part and after that again merges the solved subtasks to get the actual problem solved. 
Divide and Conquer is an algorithmic paradigm. A typical Divide and Conquer algorithm solves a problem using following three steps.
This is the primary technique mentioned in the two sorting algorithms Merge Sort and Quick Sort which are mentioned earlier. To learn more about the technique, the cases where it is used, and its implementation and solve some interesting problems, please refer to the dedicated article Divide and Conquer Algorithm.
As the name suggests, this algorithm builds up the solution one piece at a time and chooses the next piece which gives the most obvious and immediate benefit i.e., which is the most optimal choice at that moment. So the problems where choosing locally optimal also leads to the global solutions are best fit for Greedy.
For example, consider the Fractional Knapsack Problem. The local optimal strategy is to choose the item that has maximum value vs weight ratio. This strategy also leads to a globally optimal solution because we are allowed to take fractions of an item.
Fractional Knapsack Problem Here is how you can get started with the Greedy algorithm with the help of relevant sub-topics:
Recursion is one of the most important algorithms which uses the concept of code reusability and repeated usage of the same piece of code. 
Recursion The point which makes Recursion one of the most used algorithms is that it forms the base for many other algorithms such as:
In Recursion, you can follow the below articles/links to get the most out of it: 
As mentioned earlier, the Backtracking algorithm is derived from the Recursion algorithm, with the option to revert if a recursive solution fails, i.e. in case a solution fails, the program traces back to the moment where it failed and builds on another solution. So basically it tries out all the possible solutions and finds the correct one.
Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time 
Some important and most common problems of backtracking algorithms, that you must solve before moving ahead, are:
Another crucial algorithm is dynamic programming. Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for the same inputs, we can optimize it using Dynamic Programming. 
The main concept of the Dynamic Programming algorithm is to use the previously calculated result to avoid repeated calculations of the same subtask which helps in reducing the time complexity. 
Dynamic Programming
To learn more about dynamic programming and practice some interesting problems related to it, refer to the following articles:
The Pattern Searching algorithms are sometimes also referred to as String Searching Algorithms and are considered as a part of the String algorithms. These algorithms are useful in the case of searching a string within another string.
These algorithms are designed to solve Mathematical and Number Theory problems. They requires in-depth knowledge of different mathematical subjects like
These algorithms are designed to solve Geometric Problems. They requires in-depth knowledge of different mathematical subjects like:LinesTriangleRectangleSquareCircle3D ObjectsQuadilateralPolygon & Convex HullFor Example: Comparing Slopes of two lines, Finding Equation of a plane etc.11. Bitwise AlgorithmsThe Bitwise Algorithms is used to perform operations at the bit-level or to manipulate bits in different ways. The bitwise operations are found to be much faster and are sometimes used to improve the efficiency of a program.For example: To check if a number is even or odd. This can be easily done by using Bitwise-AND(&) operator. If the last bit of the operator is set than it is ODD otherwise it is EVEN. Therefore, if num & 1 not equals to zero than num is ODD otherwise it is EVEN.12. Randomized AlgorithmsAn algorithm that uses random numbers to decide what to do next anywhere in its logic is called Randomized Algorithm. For example, in Randomized Quick Sort, we use a random number to pick the next pivot (or we randomly shuffle the array). Typically, this randomness is used to reduce time complexity or space complexity in other standard algorithms.13. Branch and Bound AlgorithmBranch and bound is an algorithm design paradigm which is generally used for solving combinatorial optimization problems. These problems are typically exponential in terms of time complexity and may require exploring all possible permutations in worst case. The Branch and Bound Algorithm technique solves these problems relatively quickly.4. Practice Problems on Data Structures and Algorithms (DSA)For practicing problems on individual data structures and algorithms, you can use the following links: Practice problems on ArraysPractice problems on StringsPractice problems on Linked ListsPractice problems on Searching algorithmPractice problems on Sorting algorithmPractice problems on Divide And Conquer algorithmPractice problems on StackPractice problems on QueuePractice problems on TreePractice problems on GraphPractice problems on Greedy algorithmPractice problems on Recursion algorithmPractice problems on Backtracking algorithmPractice problems on Dynamic Programming algorithmApart from these, there are many other practice problems that you can refer based on their respective difficulties:School-levelBasic levelEasy levelMedium levelHard levelYou can also try to solve the most asked interview questions based on the list curated by us at: Must-Do Coding Questions for CompaniesTop 50 Array Coding Problems for InterviewsTop 50 String Coding Problems for InterviewsTop 50 Tree Coding Problems for InterviewsTop 50 Dynamic Programming Coding Problems for InterviewsYou can also try our curated lists of problems from below articles:SDE SHEET – A Complete Guide for SDE PreparationDSA Sheet by Love BabbarIf you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.Please write comments if you find anything incorrect, or you want to share more information about the topic discussed aboveMy Personal Notes
arrow_drop_upSave
For Example: Comparing Slopes of two lines, Finding Equation of a plane etc.
The Bitwise Algorithms is used to perform operations at the bit-level or to manipulate bits in different ways. The bitwise operations are found to be much faster and are sometimes used to improve the efficiency of a program.
For example: To check if a number is even or odd. This can be easily done by using Bitwise-AND(&) operator. If the last bit of the operator is set than it is ODD otherwise it is EVEN. Therefore, if num & 1 not equals to zero than num is ODD otherwise it is EVEN.
An algorithm that uses random numbers to decide what to do next anywhere in its logic is called Randomized Algorithm. For example, in Randomized Quick Sort, we use a random number to pick the next pivot (or we randomly shuffle the array). Typically, this randomness is used to reduce time complexity or space complexity in other standard algorithms.
Branch and bound is an algorithm design paradigm which is generally used for solving combinatorial optimization problems. These problems are typically exponential in terms of time complexity and may require exploring all possible permutations in worst case. The Branch and Bound Algorithm technique solves these problems relatively quickly.
"""
insertRecipeData("DataStructures", dsData.replace("\n", " "))
# DS
cssData = """
Today, we will look at the five most fundamental CSS concepts that every designer should know.
Whether you are aware or not, every composition is a hierarchy of some sort. Mentally acknowledging this hierarchy and then implementing it in your design helps structure information for the user — and keep your design tight and consistent.
Hierarchies consist of parents and children. Just like family trees, children can be parents to more children, and most parents are children themselves. In other words, you have ancestors: parents, grandparents, grand-grandparents, etc., and you have descendants: children, grandchildren, etcetera.
Think of your design as a collection of ancestors and descendants, with at the very top the design’s root: the canvas. If an ancestor moves, its descendants move too. If an ancestor changes dimensions, its children redistribute or resize too.
Every object in your design wants to have a defined personal space — or margin. Margin is the space an object wants to keep between itself and other objects, just like people prefer to keep a certain distance from other people in a crowded place.
Objects can have different margins for each of their sides. For example, a square may prefer to keep 100 pixels of space to its left but only 50 pixels of space to its top. A general rule of thumb is that objects with the same parent (siblings) all share the same set of margins. This helps a design look organized.
Changing an objects’ margin changes the distance between that object and other objects.
Closely related to margins, but fundamentally different is padding. Padding can be seen as fur: it’s an integral part of the object, not space around it. Just like margins, padding can have different values for top, left, right, and bottom.
Padding only comes into play when an object has children (or when an object has a predefined width or height, but let’s not complicate things). If a parent object has 20 pixels of padding and contains one child that is 100 pixels wide and 50 pixels high, the parent object will be 140 pixels wide and 90 pixels high because the fur is added to the dimensions of the parent.
Consistent use of padding helps to stabilize a design. If your design contains multiple types of containers (parents with children), even if they serve different purposes, it’s often best to use the same padding on each of those containers.
A container filled with children will grow as padding increases:
Containers can — and often do — have both padding and margins. The padding grows the actual dimensions of the container, the margin then defines the space between the container and other objects:
The distribution of objects in a static design is hardly an issue. But, user interfaces are seldom static. Instead of thinking about objects having a fixed position within their parent, it’s useful to think of their positions being governed by a certain logic. Flexboxes describe this logic.
The first thing to consider is how objects are going to be stacked within their parent. Generally, there are two options: you either stack them sideways (top to bottom or bottom to top) or vertically (left to right, or right to left).
In CSS, this is called the flex-direction property and accepted values are row | row-reverse | column | colum-reverse
Imagine you want to stack your objects from left to right, but the objects are either variable in height, or their parent is much taller than the children. In this case, you have to decide how to align them vertically, for which you will normally choose one of three options: start,center or end.The exact outcome of this value depends greatly on the direction you’ve chosen.
In CSS, this behavior is governed by the align-items property, and accepted values are flex-start | flex-end | center | stretch | baseline | first baseline | last baseline | start | end | self-start | self-end + ... safe | unsafe.
Justification is very similar to alignment. However, where alignment concerns the position on the cross axis, justification governs the object position on the main axis. Put more simply: when using a left-to-right (horizontal) stack, alignment determines where your children go on the vertical axis, and justification concerns the horizontal distribution.
Here, too, we have the three usual suspects: start, center, and end.
Fortunately, there’s more to justification. This is where the logic of flexboxes really starts to shine.
It’s tempting to forego margins when you use flexboxes completely. However, when using flexboxes, margins of child objects are still taken into account. For example, in a left-to-right situation where the children are justified to the start of the flexbox, if the children have margins, there will be space between the children:
Lastly, there is the notion of absolute values versus relative values. In a design, an object can be 200 pixels wide, or 500, or 1171. But once this object is part of the actual user interface, how will it behave? Will it stretch? If yes, how wide may it be, at most? And when the viewport narrows, will the object get squished? How far will you allow it to be squished?
"""
insertRecipeData("CSS", cssData.replace("\n", " "))
# HTML
htmlData = """
HTML stands for Hypertext Markup Language, and it is the most widely used language to write Web Pages.
Hypertext refers to the way in which Web pages (HTML documents) are linked together. Thus, the link available on a webpage is called Hypertext.
As its name suggests, HTML is a Markup Language which means you use HTML to simply "mark-up" a text document with tags that tell a Web browser how to structure it to display.
Originally, HTML was developed with the intent of defining the structure of documents like headings, paragraphs, lists, and so forth to facilitate the sharing of scientific information between researchers.
Now, HTML is being widely used to format web pages with the help of different tags available in HTML language.
In its simplest form, following is an example of an HTML document −
As told earlier, HTML is a markup language and makes use of various tags to format the content. These tags are enclosed within angle braces <Tag Name>. Except few tags, most of the tags have their corresponding closing tags. For example, <html> has its closing tag </html> and <body> tag has its closing tag </body> tag etc.
Above example of HTML document uses the following tags −
This tag defines the document type and HTML version.
This tag encloses the complete HTML document and mainly comprises of document header which is represented by <head>...</head> and document body which is represented by <body>...</body> tags.
This tag represents the document's header which can keep other HTML tags like <title>, <link> etc.
The <title> tag is used inside the <head> tag to mention the document title.
This tag represents the document's body which keeps other HTML tags like <h1>, <div>, <p> etc.
This tag represents the heading.
This tag represents a paragraph.
To learn HTML, you will need to study various tags and understand how they behave, while formatting a textual document. Learning HTML is simple as users have to learn the usage of different tags in order to format the text or images to make a beautiful webpage.
World Wide Web Consortium (W3C) recommends to use lowercase tags starting from HTML 4.
A typical HTML document will have the following structure −
We will study all the header and body tags in subsequent chapters, but for now let's see what is document declaration tag.
The <!DOCTYPE> declaration tag is used by the web browser to understand the version of the HTML used in the document. Current version of HTML is 5 and it makes use of the following declaration −
There are many other declaration types which can be used in HTML document depending on what version of HTML is being used. We will see more details on this while discussing <!DOCTYPE...> tag along with other HTML tags.
Any document starts with a heading. You can use different sizes for your headings. HTML also has six levels of headings, which use the elements <h1>, <h2>, <h3>, <h4>, <h5>, and <h6>. While displaying any heading, browser adds one line before and one line after that heading.
This will produce the following result −
The <p> tag offers a way to structure your text into different paragraphs. Each paragraph of text should go in between an opening <p> and a closing </p> tag as shown below in the example −
This will produce the following result −
Whenever you use the <br /> element, anything following it starts from the next line. This tag is an example of an empty element, where you do not need opening and closing tags, as there is nothing to go in between them.
The <br /> tag has a space between the characters br and the forward slash. If you omit this space, older browsers will have trouble rendering the line break, while if you miss the forward slash character and just use <br> it is not valid in XHTML.
This will produce the following result −
You can use <center> tag to put any content in the center of the page or any table cell.
This will produce following result −
Horizontal lines are used to visually break-up sections of a document. The <hr> tag creates a line from the current position in the document to the right margin and breaks the line accordingly.
For example, you may want to give a line between two paragraphs as in the given example below −
This will produce the following result −
Again <hr /> tag is an example of the empty element, where you do not need opening and closing tags, as there is nothing to go in between them.
The <hr /> element has a space between the characters hr and the forward slash. If you omit this space, older browsers will have trouble rendering the horizontal line, while if you miss the forward slash character and just use <hr> it is not valid in XHTML
Sometimes, you want your text to follow the exact format of how it is written in the HTML document. In these cases, you can use the preformatted tag <pre>.
Any text between the opening <pre> tag and the closing </pre> tag will preserve the formatting of the source document.
This will produce the following result −
Try using the same code without keeping it inside <pre>...</pre> tags
Suppose you want to use the phrase "12 Angry Men." Here, you would not want a browser to split the "12, Angry" and "Men" across two lines −
In cases, where you do not want the client browser to break text, you should use a nonbreaking space entity &nbsp; instead of a normal space. For example, when coding the "12 Angry Men" in a paragraph, you should use something similar to the following code −
This will produce the following result −
An HTML element is defined by a starting tag. If the element contains other content, it ends with a closing tag, where the element name is preceded by a forward slash as shown below with few tags −
So here <p>....</p> is an HTML element, <h1>...</h1> is another HTML element. There are some HTML elements which don't need to be closed, such as <img.../>, <hr /> and <br /> elements. These are known as void elements.
HTML documents consists of a tree of these elements and they specify how HTML documents should be built, and what kind of content should be placed in what part of an HTML document.
An HTML element is defined by a starting tag. If the element contains other content, it ends with a closing tag.
For example, <p> is starting tag of a paragraph and </p> is closing tag of the same paragraph but <p>This is paragraph</p> is a paragraph element.
It is very much allowed to keep one HTML element inside another HTML element −
This will display the following result −
We have seen few HTML tags and their usage like heading tags <h1>, <h2>, paragraph tag <p> and other tags. We used them so far in their simplest form, but most of the HTML tags can also have attributes, which are extra bits of information.
An attribute is used to define the characteristics of an HTML element and is placed inside the element's opening tag. All attributes are made up of two parts − a name and a value
The name is the property you want to set. For example, the paragraph <p> element in the example carries an attribute whose name is align, which you can use to indicate the alignment of paragraph on the page.
The value is what you want the value of the property to be set and always put within quotations. The below example shows three possible values of align attribute:  left, center and right.
Attribute names and attribute values are case-insensitive. However, the World Wide Web Consortium (W3C) recommends lowercase attributes/attribute values in their HTML 4 recommendation.
This will display the following result −
The four core attributes that can be used on the majority of HTML elements (although not all) are −
The id attribute of an HTML tag can be used to uniquely identify any element within an HTML page. There are two primary reasons that you might want to use an id attribute on an element −
If an element carries an id attribute as a unique identifier, it is possible to identify just that element and its content.
If you have two elements of the same name within a Web page (or style sheet), you can use the id attribute to distinguish between elements that have the same name.
We will discuss style sheet in separate tutorial. For now, let's use the id attribute to distinguish between two paragraph elements as shown below.
Example
The title attribute gives a suggested title for the element. They syntax for the title attribute is similar as explained for id attribute −
The behavior of this attribute will depend upon the element that carries it, although it is often displayed as a tooltip when cursor comes over the element or while the element is loading.
Example
This will produce the following result −
Now try to bring your cursor over "Titled Heading Tag Example" and you will see that whatever title you used in your code is coming out as a tooltip of the cursor.
The class attribute is used to associate an element with a style sheet, and specifies the class of element. You will learn more about the use of the class attribute when you will learn Cascading Style Sheet (CSS). So for now you can avoid it.
The value of the attribute may also be a space-separated list of class names. For example −
The style attribute allows you to specify Cascading Style Sheet (CSS) rules within the element.
This will produce the following result −
At this point of time, we are not learning CSS, so just let's proceed without bothering much about CSS. Here, you need to understand what are HTML attributes and how they can be used while formatting content.
There are three internationalization attributes, which are available for most (although not all) XHTML elements.
The dir attribute allows you to indicate to the browser about the direction in which the text should flow. The dir attribute can take one of two values, as you can see in the table that follows −
Example
This will produce the following result −
When dir attribute is used within the <html> tag, it determines how text will be presented within the entire document. When used within another tag, it controls the text's direction for just the content of that tag.
The lang attribute allows you to indicate the main language used in a document, but this attribute was kept in HTML only for backwards compatibility with earlier versions of HTML. This attribute has been replaced by the xml:lang attribute in new XHTML documents.
The values of the lang attribute are ISO-639 standard two-character language codes. Check HTML Language Codes: ISO 639 for a complete list of language codes.
Example
This will produce the following result −
The xml:lang attribute is the XHTML replacement for the lang attribute. The value of the xml:lang attribute should be an ISO-639 country code as mentioned in previous section.
Here's a table of some other attributes that are readily usable with many of the HTML tags.
We will see related examples as we will proceed to study other HTML tags. For a complete list of HTML Tags and related attributes please check reference to HTML Tags List.
If you use a word processor, you must be familiar with the ability to make text bold, italicized, or underlined; these are just three of the ten options available to indicate how text can appear in HTML and XHTML.
Anything that appears within <b>...</b> element, is displayed in bold as shown below −
This will produce the following result −
Anything that appears within <i>...</i> element is displayed in italicized as shown below −
This will produce the following result −
Anything that appears within <u>...</u> element, is displayed with underline as shown below −
This will produce the following result −
Anything that appears within <strike>...</strike> element is displayed with strikethrough, which is a thin line through the text as shown below −
This will produce the following result −
The content of a <tt>...</tt> element is written in monospaced font. Most of the fonts are known as variable-width fonts because different letters are of different widths (for example, the letter 'm' is wider than the letter 'i'). In a monospaced font, however, each letter has the same width.
This will produce the following result −
The content of a <sup>...</sup> element is written in superscript; the font size used is the same size as the characters surrounding it but is displayed half a character's height above the other characters.
This will produce the following result −
The content of a <sub>...</sub> element is written in subscript; the font size used is the same as the characters surrounding it, but is displayed half a character's height beneath the other characters.
This will produce the following result −
Anything that appears within <ins>...</ins> element is displayed as inserted text.
This will produce the following result −
Anything that appears within <del>...</del> element, is displayed as deleted text.
This will produce the following result −
The content of the <big>...</big> element is displayed one font size larger than the rest of the text surrounding it as shown below −
This will produce the following result −
The content of the <small>...</small> element is displayed one font size smaller than the rest of the text surrounding it as shown below −
This will produce the following result −
The <div> and <span> elements allow you to group together several elements to create sections or subsections of a page.
For example, you might want to put all of the footnotes on a page within a <div> element to indicate that all of the elements within that <div> element relate to the footnotes. You might then attach a style to this <div> element so that they appear using a special set of style rules.
This will produce the following result −
The <span> element, on the other hand, can be used to group inline elements only. So, if you have a part of a sentence or paragraph which you want to group together, you could use the <span> element as follows.
This will produce the following result −
These tags are commonly used with CSS to allow you to attach a style to a section of a page.
The phrase tags have been desicolgned for specific purposes, though they are displayed in a similar way as other basic tags like <b>, <i>, <pre>, and <tt>, you have seen in previous chapter. This chapter will take you through all the important phrase tags, so let's start seeing them one by one.
Anything that appears within <em>...</em> element is displayed as emphasized text.
This will produce the following result −
Anything that appears with-in <mark>...</mark> element, is displayed as marked with yellow ink.
This will produce the following result −
Anything that appears within <strong>...</strong> element is displayed as important text.
This will produce the following result −
You can abbreviate a text by putting it inside opening <abbr> and closing </abbr> tags. If present, the title attribute must contain this full description and nothing else.
This will produce the following result −
The <acronym> element allows you to indicate that the text between <acronym> and </acronym> tags is an acronym.
At present, the major browsers do not change the appearance of the content of the <acronym> element.
This will produce the following result −
The <bdo>...</bdo> element stands for Bi-Directional Override and it is used to override the current text direction.
This will produce the following result −
The <dfn>...</dfn> element (or HTML Definition Element) allows you to specify that you are introducing a special term. It's usage is similar to italic words in the midst of a paragraph.
Typically, you would use the <dfn> element the first time you introduce a key term. Most recent browsers render the content of a <dfn> element in an italic font.
This will produce the following result −
When you want to quote a passage from another source, you should put it in between <blockquote>...</blockquote> tags.
Text inside a <blockquote> element is usually indented from the left and right edges of the surrounding text, and sometimes uses an italicized font.
This will produce the following result −
The <q>...</q> element is used when you want to add a double quote within a sentence.
This will produce the following result −
If you are quoting a text, you can indicate the source placing it between an opening <cite> tag and closing </cite> tag
As you would expect in a print publication, the content of the <cite> element is rendered in italicized text by default.
This will produce the following result −
Any programming code to appear on a Web page should be placed inside <code>...</code> tags. Usually the content of the <code> element is presented in a monospaced font, just like the code in most programming books.
This will produce the following result −
When you are talking about computers, if you want to tell a reader to enter some text, you can use the <kbd>...</kbd> element to indicate what should be typed in, as in this example.
This will produce the following result −
This element is usually used in conjunction with the <pre> and <code> elements to indicate that the content of that element is a variable.
This will produce the following result −
The <samp>...</samp> element indicates sample output from a program, and script etc. Again, it is mainly used when documenting programming or coding concepts.
This will produce the following result −
The <address>...</address> element is used to contain any address.
This will produce the following result −
HTML lets you specify metadata - additional important information about a document in a variety of ways. The META elements can be used to include name/value pairs describing properties of the HTML document, such as author, expiry date, a list of keywords, document author etc.
The <meta> tag is used to provide such additional information. This tag is an empty element and so does not have a closing tag but it carries information within its attributes.
You can include one or more meta tags in your document based on what information you want to keep in your document but in general, meta tags do not impact physical appearance of the document so from appearance point of view, it does not matter if you include them or not.
You can add metadata to your web pages by placing <meta> tags inside the header of the document which is represented by <head> and </head> tags. A meta tag can have following attributes in addition to core attributes −
Name
Name for the property. Can be anything. Examples include, keywords, description, author, revised, generator etc.
content
Specifies the property's value.
scheme
Specifies a scheme to interpret the property's value (as declared in the content attribute).
http-equiv
Used for http response message headers. For example, http-equiv can be used to refresh the page or to set a cookie. Values include content-type, expires, refresh and set-cookie.
You can use <meta> tag to specify important keywords related to the document and later these keywords are used by the search engines while indexing your webpage for searching purpose.
Following is an example, where we are adding HTML, Meta Tags, Metadata as important keywords about the document.
This will produce the following result −
You can use <meta> tag to give a short description about the document. This again can be used by various search engines while indexing your webpage for searching purpose.
You can use <meta> tag to give information about when last time the document was updated. This information can be used by various web browsers while refreshing your webpage.
A <meta> tag can be used to specify a duration after which your web page will keep refreshing automatically.
If you want your page keep refreshing after every 5 seconds then use the following syntax.
You can use <meta> tag to redirect your page to any other webpage. You can also specify a duration if you want to redirect the page after a certain number of seconds.
Following is an example of redirecting current page to another page after 5 seconds. If you want to redirect page immediately then do not specify content attribute.
Cookies are data, stored in small text files on your computer and it is exchanged between web browser and web server to keep track of various information based on your web application need.
You can use <meta> tag to store cookies on client side and later this information can be used by the Web Server to track a site visitor.
Following is an example of redirecting current page to another page after 5 seconds. If you want to redirect page immediately then do not specify content attribute.
If you do not include the expiration date and time, the cookie is considered a session cookie and will be deleted when the user exits the browser.
Note − You can check PHP and Cookies tutorial for a complete detail on Cookies.
You can set an author name in a web page using meta tag. See an example below −
You can use <meta> tag to specify character set used within the webpage.
By default, Web servers and Web browsers use ISO-8859-1 (Latin1) encoding to process Web pages. Following is an example to set UTF-8 encoding −
To serve the static page with traditional Chinese characters, the webpage must contain a <meta> tag to set Big5 encoding −
Comment is a piece of code which is ignored by any web browser. It is a good practice to add comments into your HTML code, especially in complex documents, to indicate sections of a document, and any other notes to anyone looking at the code. Comments help you and others understand your code and increases code readability.
HTML comments are placed in between <!-- ... --> tags. So, any content placed with-in <!-- ... --> tags will be treated as comment and will be completely ignored by the browser.
This will produce the following result without displaying the content given as a part of comments −
Comments do not nest which means a comment cannot be put inside another comment. Second the double-dash sequence "--" may not appear inside a comment except as part of the closing --> tag. You must also make sure that there are no spaces in the start-of comment string.
Here, the given comment is a valid comment and will be wiped off by the browser.
This will produce the following result −
But, following line is not a valid comment and will be displayed by the browser. This is because there is a space between the left angle bracket and the exclamation mark.
This will produce the following result −
So far we have seen single line comments, but HTML supports multi-line comments as well.
You can comment multiple lines by the special beginning tag <!-- and ending tag --> placed before the first line and end of the last line as shown in the given example below.
This will produce the following result −
Conditional comments only work in Internet Explorer (IE) on Windows but they are ignored by other browsers. They are supported from Explorer 5 onwards, and you can use them to give conditional instructions to different versions of IE.
You will come across a situation where you will need to apply a different style sheet based on different versions of Internet Explorer, in such situation conditional comments will be helpful.
There are few browsers that support <comment> tag to comment a part of HTML code.
Note − The <comment> tag deprecated in HTML5. Do not use this element.
If you are using IE, then it will produce following result −
But if you are not using IE, then it will produce following result −
Though you will learn JavaScript with HTML, in a separate tutorial, but here you must make a note that if you are using Java Script or VB Script in your HTML code then it is recommended to put that script code inside proper HTML comments so that old browsers can work properly.
This will produce the following result −
Though you will learn using style sheets with HTML in a separate tutorial, but here you must make a note that if you are using Cascading Style Sheet (CSS) in your HTML code then it is recommended to put that style sheet code inside proper HTML comments so that old browsers can work properly.
This will produce the following result −
Images are very important to beautify as well as to depict many complex concepts in simple way on your web page. This tutorial will take you through simple steps to use images in your web pages.
You can insert any image in your web page by using <img> tag. Following is the simple syntax to use this tag.
The <img> tag is an empty tag, which means that, it can contain only list of attributes and it has no closing tag.
To try following example, let's keep our HTML file test.htm and image file test.png in the same directory −
This will produce the following result −
You can use PNG, JPEG or GIF image file based on your comfort but make sure you specify correct image file name in src attribute. Image name is always case sensitive.
The alt attribute is a mandatory attribute which specifies an alternate text for an image, if the image cannot be displayed.
Usually we keep all the images in a separate directory. So let's keep HTML file test.htm in our home directory and create a subdirectory images inside the home directory where we will keep our image test.png.
Assuming our image location is "image/test.png", try the following example −
This will produce the following result −
You can set image width and height based on your requirement using width and height attributes. You can specify width and height of the image in terms of either pixels or percentage of its actual size.
This will produce the following result −
By default, image will have a border around it, you can specify border thickness in terms of pixels using border attribute. A thickness of 0 means, no border around the picture.
This will produce the following result −
By default, image will align at the left side of the page, but you can use align attribute to set it in the center or right.
This will produce the following result −
For Free Web Graphics including patterns you can look into Free Web Graphics
The HTML tables allow web authors to arrange data like text, images, links, other tables, etc. into rows and columns of cells.
The HTML tables are created using the <table> tag in which the <tr> tag is used to create table rows and <td> tag is used to create data cells. The elements under <td> are regular and left aligned by default
This will produce the following result −
Here, the border is an attribute of <table> tag and it is used to put a border across all the cells. If you do not need a border, then you can use border = "0".
Table heading can be defined using <th> tag. This tag will be put to replace <td> tag, which is used to represent actual data cell. Normally you will put your top row as table heading as shown below, otherwise you can use <th> element in any row. Headings, which are defined in <th> tag are centered and bold by default.
This will produce the following result −
There are two attributes called cellpadding and cellspacing which you will use to adjust the white space in your table cells. The cellspacing attribute defines space between table cells, while cellpadding represents the distance between cell borders and the content within a cell.
This will produce the following result −
You will use colspan attribute if you want to merge two or more columns into a single column. Similar way you will use rowspan if you want to merge two or more rows.
This will produce the following result −
You can set table background using one of the following two ways −
bgcolor attribute − You can set background color for whole table or just for one cell.
background attribute − You can set background image for whole table or just for one cell.
You can also set border color also using bordercolor attribute.
Note − The bgcolor, background, and bordercolor attributes deprecated in HTML5. Do not use these attributes.
This will produce the following result −
Here is an example of using background attribute. Here we will use an image available in /images directory.
This will produce the following result. Here background image did not apply to table's header.
You can set a table width and height using width and height attributes. You can specify table width or height in terms of pixels or in terms of percentage of available screen area.
This will produce the following result −
The caption tag will serve as a title or explanation for the table and it shows up at the top of the table. This tag is deprecated in newer version of HTML/XHTML.
This will produce the following result −
Tables can be divided into three portions − a header, a body, and a foot. The head and foot are rather similar to headers and footers in a word-processed document that remain the same for every page, while the body is the main content holder of the table.
The three elements for separating the head, body, and foot of a table are −
<thead> − to create a separate table header.
<tbody> − to indicate the main body of the table.
<tfoot> − to create a separate table footer.
A table may contain several <tbody> elements to indicate different pages or groups of data. But it is notable that <thead> and <tfoot> tags should appear before <tbody>
This will produce the following result −
You can use one table inside another table. Not only tables you can use almost all the tags inside table data tag <td>.
Following is the example of using another table and other tags inside a table cell.
This will produce the following result −
HTML offers web authors three ways for specifying lists of information. All lists must contain one or more list elements. Lists may contain −
<ul> − An unordered list. This will list items using plain bullets.
<ol> − An ordered list. This will use different schemes of numbers to list your items.
<dl> − A definition list. This arranges your items in the same way as they are arranged in a dictionary.
An unordered list is a collection of related items that have no special order or sequence. This list is created by using HTML <ul> tag. Each item in the list is marked with a bullet.
This will produce the following result −
You can use type attribute for <ul> tag to specify the type of bullet you like. By default, it is a disc. Following are the possible options −
Following is an example where we used <ul type = "square">
This will produce the following result −
Following is an example where we used <ul type = "disc"> −
This will produce the following result −
Following is an example where we used <ul type = "circle"> −
This will produce the following result −
If you are required to put your items in a numbered list instead of bulleted, then HTML ordered list will be used. This list is created by using <ol> tag. The numbering starts at one and is incremented by one for each successive ordered list element tagged with <li>.
This will produce the following result −
You can use type attribute for <ol> tag to specify the type of numbering you like. By default, it is a number. Following are the possible options −
Following is an example where we used <ol type = "1">
This will produce the following result −
Following is an example where we used <ol type = "I">
This will produce the following result −
Following is an example where we used <ol type = "i">
This will produce the following result −
Following is an example where we used <ol type = "A" >
This will produce the following result −
Following is an example where we used <ol type = "a">
This will produce the following result −
You can use start attribute for <ol> tag to specify the starting point of numbering you need. Following are the possible options −
Following is an example where we used <ol type = "i" start = "4" >
This will produce the following result −
HTML and XHTML supports a list style which is called definition lists where entries are listed like in a dictionary or encyclopedia. The definition list is the ideal way to present a glossary, list of terms, or other name/value list.
Definition List makes use of following three tags.
This will produce the following result −
A webpage can contain various links that take you directly to other pages and even specific parts of a given page. These links are known as hyperlinks.
Hyperlinks allow visitors to navigate between Web sites by clicking on words, phrases, and images. Thus you can create hyperlinks using text or images available on a webpage.
Note − I recommend you to go through a short tutorial on Understanding URL
A link is specified using HTML tag <a>. This tag is called anchor tag and anything between the opening <a> tag and the closing </a> tag becomes part of the link and a user can click that part to reach to the linked document. Following is the simple syntax to use <a> tag.
Let's try following example which links http://www.tutorialspoint.com at your page −
This will produce the following result, where you can click on the link generated to reach to the home page of Tutorials Point (in this example).
We have used target attribute in our previous example. This attribute is used to specify the location where linked document is opened. Following are the possible options −
_blank
Opens the linked document in a new window or tab.
_self
Opens the linked document in the same frame.
_parent
Opens the linked document in the parent frame.
_top
Opens the linked document in the full body of the window.
targetframe
Opens the linked document in a named targetframe.
Try following example to understand basic difference in few options given for target attribute.
This will produce the following result, where you can click on different links to understand the difference between various options given for target attribute.
When you link HTML documents related to the same website, it is not required to give a complete URL for every link. You can get rid of it if you use <base> tag in your HTML document header. This tag is used to give a base path for all the links. So your browser will concatenate given relative path to this base path and will make a complete URL.
Following example makes use of <base> tag to specify base URL and later we can use relative path to all the links instead of giving complete URL for every link.
This will produce the following result, where you can click on the link generated HTML Tutorial to reach to the HTML tutorial.
Now given URL <a href = "/html/index.htm" is being considered as <ahref = "http://www.tutorialspoint.com/html/index.htm"
You can create a link to a particular section of a given webpage by using name attribute. This is a two-step process.
Note − The name attribute deprecated in HTML5. Do not use this attribute. Use id and title attribute instead.
First create a link to the place where you want to reach with-in a webpage and name it using <a...> tag as follows −
Second step is to create a hyperlink to link the document and place where you want to reach −
This will produce following link, where you can click on the link generated Go to the Top to reach to the top of the HTML Text Link tutorial.
You can set colors of your links, active links and visited links using link, alink and vlink attributes of <body> tag.
Save the following in test.htm and open it in any web browser to see how link, alink and vlink attributes work.
This will produce the following result. Just check color of the link before clicking on it, next check its color when you activate it and when the link has been visited.
You can create text link to make your PDF, or DOC or ZIP files downloadable. This is very simple; you just need to give complete URL of the downloadable file as follows −
This will produce following link and will be used to download a file.
Sometimes it is desired that you want to give an option where a user will click a link and it will pop up a "File Download" box to the user instead of displaying actual content. This is very easy and can be achieved using an HTTP header in your HTTP response.
For example, if you want make a Filename file downloadable from a given link then its syntax will be as follows.
Note − For more detail on PERL CGI programs, go through tutorial PERL and CGI.
We have seen how to create hypertext link using text and we also learnt how to use images in our webpages. Now, we will learn how to use images to create hyperlinks.
It's simple to use an image as hyperlink. We just need to use an image inside hyperlink at the place of text as shown below −
This will produce the following result, where you can click on the images to reach to the home page of Tutorials Point.
This was the simplest way of creating hyperlinks using images. Next we will see how we can create Mouse-Sensitive Image Links.
The HTML and XHTML standards provides a feature that lets you embed many different links inside a single image. You can create different links on the single image based on different coordinates available on the image. Once different links are attached to different coordinates, we can click different parts of the image to open target documents. Such mouse-sensitive images are known as image maps.
There are two ways to create image maps −
Server-side image maps − This is enabled by the ismap attribute of the <img> tag and requires access to a server and related image-map processing applications.
Client-side image maps − This is created with the usemap attribute of the <img> tag, along with corresponding <map> and <area> tags.
Here you simply put your image inside a hyper link and use ismap attribute which makes it special image and when the user clicks some place within the image, the browser passes the coordinates of the mouse pointer along with the URL specified in the <a> tag to the web server. The server uses the mouse-pointer coordinates to determine which document to deliver back to the browser.
When ismap is used, the href attribute of the containing <a> tag must contain the URL of a server application like a cgi or PHP script etc. to process the incoming request based on the passed coordinates.
The coordinates of the mouse position are screen pixels counted from the upper-left corner of the image, beginning with (0,0). The coordinates, preceded by a question mark, are added to the end of the URL.
For example, if a user clicks 20 pixels over and 30 pixels down from the upper-left corner of the following image −
Which has been generated by the following code snippet −
Then the browser sends the following search parameters to the web server which can be processed by ismap.cgi script or map file and you can link whatever documents you like to these coordinates −
This way you can assign different links to different coordinates of the image and when those coordinates are clicked, you can open corresponding linked document. To learn more about ismap attribute, you can check How to use Image ismap?
Note − You will learn CGI programming when you will study Perl programming. You can write your script to process these passed coordinates using PHP or any other script as well. For now, let's concentrate on learning HTML and later you can revisit this section.
Client side image maps are enabled by the usemap attribute of the <img /> tag and defined by special <map> and <area> extension tags.
The image that is going to form the map is inserted into the page using the <img /> tag as a normal image, except it carries an extra attribute called usemap. The value of the usemap attribute is the value which will be used in a <map> tag to link map and image tags. The <map> along with <area> tags define all the image coordinates and corresponding links.
The <area> tag inside the map tag, specifies the shape and the coordinates to define the boundaries of each clickable hotspot available on the image. Here's an example from the image map −
This will produce the following result −
The actual value of coords is totally dependent on the shape in question. Here is a summary, to be followed by detailed examples −
rect = x1 , y1 , x2 , y2
x1 and y1 are the coordinates of the upper left corner of the rectangle; x2 and y2 are the coordinates of the lower right corner.
circle = xc , yc , radius
xc and yc are the coordinates of the center of the circle, and radius is the circle's radius. A circle centered at 200,50 with a radius of 25 would have the attribute coords = "200,50,25"
poly = x1 , y1 , x2 , y2 , x3 , y3 , ... xn , yn
The various x-y pairs define vertices (points) of the polygon, with a "line" being drawn from one point to the next point. A diamond-shaped polygon with its top point at 20,20 and 40 pixels across at its widest points would have the attribute coords = "20,20,40,40,20,60,0,40".
All coordinates are relative to the upper-left corner of the image (0,0). Each shape has a related URL. You can use any image software to know the coordinates of different positions.
It is not difficult to put an HTML email link on your webpage but it can cause unnecessary spamming problem for your email account. There are people, who can run programs to harvest these types of emails and later use them for spamming in various ways.
You can have another option to facilitate people to send you emails. One option could be to use HTML forms to collect user data and then use PHP or CGI script to send an email.
A simple example, check our Contact Us Form. We take user feedback using this form and then we are using one CGI program which is collecting this information and sending us email to the one given email ID.
Note − You will learn about HTML Forms in HTML Forms and you will learn about CGI in our another tutorial Perl CGI Programming.
HTML <a> tag provides you option to specify an email address to send an email. While using <a> tag as an email tag, you will use mailto: email address along with href attribute. Following is the syntax of using mailto instead of using http.
This code will generate the following link which you can use to send email.
Now, if a user clicks this link, it launches one Email Client (like Lotus Notes, Outlook Express etc. ) installed on your user's computer. There is another risk to use this option to send email because if user do not have email client installed on their computer then it would not be possible to send email.
You can specify a default email subject and email body along with your email address. Following is the example to use default subject and body.
This code will generate the following link which you can use to send email.
HTML frames are used to divide your browser window into multiple sections where each section can load a separate HTML document. A collection of frames in the browser window is known as a frameset. The window is divided into frames in a similar way the tables are organized: into rows and columns.
There are few drawbacks with using frames, so it's never recommended to use frames in your webpages −
Some smaller devices cannot cope with frames often because their screen is not big enough to be divided up.
Sometimes your page will be displayed differently on different computers due to different screen resolution.
The browser's back button might not work as the user hopes.
There are still few browsers that do not support frame technology.
To use frames on a page we use <frameset> tag instead of <body> tag. The <frameset> tag defines, how to divide the window into frames. The rows attribute of <frameset> tag defines horizontal frames and cols attribute defines vertical frames. Each frame is indicated by <frame> tag and it defines which HTML document shall open into the frame.
Note − The <frame> tag deprecated in HTML5. Do not use this element.
Following is the example to create three horizontal frames −
This will produce the following result −
Let's put the above example as follows, here we replaced rows attribute by cols and changed their width. This will create all the three frames vertically −
This will produce the following result −
Following are important attributes of the <frameset> tag −
cols
Specifies how many columns are contained in the frameset and the size of each column. You can specify the width of each column in one of the four ways −
Absolute values in pixels. For example, to create three vertical frames, use cols = "100, 500, 100".
A percentage of the browser window. For example, to create three vertical frames, use cols = "10%, 80%, 10%".
Using a wildcard symbol. For example, to create three vertical frames, use cols = "10%, *, 10%". In this case wildcard takes remainder of the window.
As relative widths of the browser window. For example, to create three vertical frames, use cols = "3*, 2*, 1*". This is an alternative to percentages. You can use relative widths of the browser window. Here the window is divided into sixths: the first column takes up half of the window, the second takes one third, and the third takes one sixth.
rows
This attribute works just like the cols attribute and takes the same values, but it is used to specify the rows in the frameset. For example, to create two horizontal frames, use rows = "10%, 90%". You can specify the height of each row in the same way as explained above for columns.
border
This attribute specifies the width of the border of each frame in pixels. For example, border = "5". A value of zero means no border.
frameborder
This attribute specifies whether a three-dimensional border should be displayed between frames. This attribute takes value either 1 (yes) or 0 (no). For example frameborder = "0" specifies no border.
framespacing
This attribute specifies the amount of space between frames in a frameset. This can take any integer value. For example framespacing = "10" means there should be 10 pixels spacing between each frames.
Following are the important attributes of <frame> tag −
src
This attribute is used to give the file name that should be loaded in the frame. Its value can be any URL. For example, src = "/html/top_frame.htm" will load an HTML file available in html directory.
name
This attribute allows you to give a name to a frame. It is used to indicate which frame a document should be loaded into. This is especially important when you want to create links in one frame that load pages into an another frame, in which case the second frame needs a name to identify itself as the target of the link.
frameborder
This attribute specifies whether or not the borders of that frame are shown; it overrides the value given in the frameborder attribute on the <frameset> tag if one is given, and this can take values either 1 (yes) or 0 (no).
marginwidth
This attribute allows you to specify the width of the space between the left and right of the frame's borders and the frame's content. The value is given in pixels. For example marginwidth = "10".
marginheight
This attribute allows you to specify the height of the space between the top and bottom of the frame's borders and its contents. The value is given in pixels. For example marginheight = "10".
noresize
By default, you can resize any frame by clicking and dragging on the borders of a frame. The noresize attribute prevents a user from being able to resize the frame. For example noresize = "noresize".
scrolling
This attribute controls the appearance of the scrollbars that appear on the frame. This takes values either "yes", "no" or "auto". For example scrolling = "no" means it should not have scroll bars.
longdesc
This attribute allows you to provide a link to another page containing a long description of the contents of the frame. For example longdesc = "framedescription.htm"
If a user is using any old browser or any browser, which does not support frames then <noframes> element should be displayed to the user.
So you must place a <body> element inside the <noframes> element because the <frameset> element is supposed to replace the <body> element, but if a browser does not understand <frameset> element then it should understand what is inside the <body> element which is contained in a <noframes> element.
You can put some nice message for your user having old browsers. For example, Sorry!! your browser does not support frames. as shown in the above example.
One of the most popular uses of frames is to place navigation bars in one frame and then load main pages into a separate frame.
Let's see following example where a test.htm file has following code −
Here, we have created two columns to fill with two frames. The first frame is 200 pixels wide and will contain the navigation menu bar implemented by menu.htm file. The second column fills in remaining space and will contain the main part of the page and it is implemented by main.htm file. For all the three links available in menu bar, we have mentioned target frame as main_page, so whenever you click any of the links in menu bar, available link will open in main page.
Following is the content of menu.htm file
Following is the content of main.htm file −
When we load test.htm file, it produces following result −
Now you can try to click links available in the left panel and see the result. The targetattribute can also take one of the following values −
_self
Loads the page into the current frame.
_blank
Loads a page into a new browser window. Opening a new window.
_parent
Loads the page into the parent window, which in the case of a single frameset is the main browser window.
_top
Loads the page into the browser window, replacing any current frames.
targetframe
Loads the page into a named targetframe.
You can define an inline frame with HTML tag <iframe>. The <iframe> tag is not somehow related to <frameset> tag, instead, it can appear anywhere in your document. The <iframe> tag defines a rectangular region within the document in which the browser can display a separate document, including scrollbars and borders. An inline frame is used to embed another document within the current HTML document.
The src attribute is used to specify the URL of the document that occupies the inline frame.
Following is the example to show how to use the <iframe> −
This will produce the following result −
Most of the attributes of the <iframe> tag, including name, class, frameborder, id, longdesc, marginheight, marginwidth, name, scrolling, style, and title behave exactly like the corresponding attributes for the <frame> tag.
Note − The frameborder, marginwidth, longdesc, scrolling, marginheight attributes deprecated in HTML5. Do not use these attributes.
src
This attribute is used to give the file name that should be loaded in the frame. Its value can be any URL. For example, src = "/html/top_frame.htm" will load an HTML file available in html directory.
name
This attribute allows you to give a name to a frame. It is used to indicate which frame a document should be loaded into. This is especially important when you want to create links in one frame that load pages into an another frame, in which case the second frame needs a name to identify itself as the target of the link.
frameborder
This attribute specifies whether or not the borders of that frame are shown; it overrides the value given in the frameborder attribute on the <frameset> tag if one is given, and this can take values either 1 (yes) or 0 (no).
marginwidth
This attribute allows you to specify the width of the space between the left and right of the frame's borders and the frame's content. The value is given in pixels. For example marginwidth = "10".
marginheight
This attribute allows you to specify the height of the space between the top and bottom of the frame's borders and its contents. The value is given in pixels. For example marginheight = "10".
height
This attribute specifies the height of <iframe>.
scrolling
This attribute controls the appearance of the scrollbars that appear on the frame. This takes values either "yes", "no" or "auto". For example scrolling = "no" means it should not have scroll bars.
longdesc
This attribute allows you to provide a link to another page containing a long description of the contents of the frame. For example longdesc = "framedescription.htm"
width
This attribute specifies the width of <iframe>.
All the HTML elements can be categorized into two categories (a) Block Level Elements (b)Inline Elements.
Block elements appear on the screen as if they have a line break before and after them. For example, the <p>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <ul>, <ol>, <dl>, <pre>, <hr />, <blockquote>, and <address> elements are all block level elements. They all start on their own new line, and anything that follows them appears on its own new line.
Inline elements, on the other hand, can appear within sentences and do not have to appear on a new line of their own. The <b>, <i>, <u>, <em>, <strong>, <sup>, <sub>, <big>, <small>, <li>, <ins>, <del>, <code>, <cite>, <dfn>, <kbd>, and <var> elements are all inline elements.
There are two important tags which we use very frequently to group various other HTML tags (i) <div> tag and (ii) <span> tag
This is the very important block level tag which plays a big role in grouping various other HTML tags and applying CSS on group of elements. Even now <div> tag can be used to create webpage layout where we define different parts (Left, Right, Top etc.) of the page using <div> tag. This tag does not provide any visual change on the block but this has more meaning when it is used with CSS.
Following is a simple example of <div> tag. We will learn Cascading Style Sheet (CSS) in a separate chapter but we used it here to show the usage of <div> tag −
This will produce the following result −
The HTML <span> is an inline element and it can be used to group inline-elements in an HTML document. This tag also does not provide any visual change on the block but has more meaning when it is used with CSS.
The difference between the <span> tag and the <div> tag is that the <span> tag is used with inline elements whereas the <div> tag is used with block-level elements.
Following is a simple example of <span> tag. We will learn Cascading Style Sheet (CSS) in a separate chapter but we used it here to show the usage of <span> tag −
This will produce the following result −
By default, your webpage background is white in color. You may not like it, but no worries. HTML provides you following two good ways to decorate your webpage background.
Now let's see both the approaches one by one using appropriate examples.
The bgcolor attribute is used to control the background of an HTML element, specifically page body and table backgrounds.
Note − The bgcolor attribute deprecated in HTML5. Do not use this attribute.
Following is the syntax to use bgcolor attribute with any HTML tag.
This color_value can be given in any of the following formats −
Here are the examples to set background of an HTML tag −
This will produce the following result −
The background attribute can also be used to control the background of an HTML element, specifically page body and table backgrounds. You can specify an image to set background of your HTML page or table.
Note − The background attribute deprecated in HTML5. Do not use this attribute.
Following is the syntax to use background attribute with any HTML tag.
Note − The background attribute is deprecated and it is recommended to use Style Sheet for background setting.
The most frequently used image formats are JPEG, GIF and PNG images.
Here are the examples to set background images of a table.
This will produce the following result −
You might have seen many pattern or transparent backgrounds on various websites. This simply can be achieved by using patterned image or transparent image in the background.
It is suggested that while creating patterns or transparent GIF or PNG images, use the smallest dimensions possible even as small as 1x1 to avoid slow loading.
Here are the examples to set background pattern of a table −
This will produce the following result −
Colors are very important to give a good look and feel to your website. You can specify colors on page level using <body> tag or you can set colors for individual tags using bgcolor attribute.
The <body> tag has following attributes which can be used to set different colors −
bgcolor − sets a color for the background of the page.
text − sets a color for the body text.
alink − sets a color for active links or selected links.
link − sets a color for linked text.
vlink − sets a color for visited links − that is, for linked text that you have already clicked on.
There are following three different methods to set colors in your web page −
Color names − You can specify color names directly like green, blue or red.
Hex codes − A six-digit code representing the amount of red, green, and blue that makes up the color.
Color decimal or percentage values − This value is specified using the rgb( ) property.
Now we will see these coloring schemes one by one.
You can specify direct a color name to set text or background color. W3C has listed 16 basic color names that will validate with an HTML validator but there are over 200 different color names supported by major browsers.
Note − Check a complete list of HTML Color Name.
Here is the list of W3C Standard 16 Colors names and it is recommended to use them.
Here are the examples to set background of an HTML tag by color name −
A hexadecimal is a 6 digit representation of a color. The first two digits(RR) represent a red value, the next two are a green value(GG), and the last are the blue value(BB).
A hexadecimal value can be taken from any graphics software like Adobe Photoshop, Paintshop Pro or MS Paint.
Each hexadecimal code will be preceded by a pound or hash sign #. Following is a list of few colors using hexadecimal notation.
Here are the examples to set background of an HTML tag by color code in hexadecimal −
This color value is specified using the rgb( ) property. This property takes three values, one each for red, green, and blue. The value can be an integer between 0 and 255 or a percentage.
Note −  All the browsers does not support rgb() property of color so it is recommended not to use it.
Following is a list to show few colors using RGB values.
Here are the examples to set background of an HTML tag by color code using rgb() values −
Here is the list of 216 colors which are supposed to be safest and computer independent colors. These colors very from hexa code 000000 to FFFFFF and they will be supported by all the computers having 256 color palette.
Fonts play a very important role in making a website more user friendly and increasing content readability. Font face and color depends entirely on the computer and browser that is being used to view your page but you can use HTML <font> tag to add style, size, and color to the text on your website. You can use a <basefont> tag to set all of your text to the same size, face, and color.
The font tag is having three attributes called size, color, and face to customize your fonts. To change any of the font attributes at any time within your webpage, simply use the <font> tag. The text that follows will remain changed until you close with the </font> tag. You can change one or all of the font attributes within one <font> tag.
Note −The font and basefont tags are deprecated and it is supposed to be removed in a future version of HTML. So they should not be used rather, it's suggested to use CSS styles to manipulate your fonts. But still for learning purpose, this chapter will explain font and basefont tags in detail.
You can set content font size using size attribute. The range of accepted values is from 1(smallest) to 7(largest). The default size of a font is 3.
This will produce the following result −
You can specify how many sizes larger or how many sizes smaller than the preset font size should be. You can specify it like <font size = "+n"> or <font size = "−n">
This will produce the following result −
You can set font face using face attribute but be aware that if the user viewing the page doesn't have the font installed, they will not be able to see it. Instead user will see the default font face applicable to the user's computer.
This will produce the following result −
A visitor will only be able to see your font if they have that font installed on their computer. So, it is possible to specify two or more font face alternatives by listing the font face names, separated by a comma.
When your page is loaded, their browser will display the first font face available. If none of the given fonts are installed, then it will display the default font face Times New Roman.
Note − Check a complete list of HTML Standard Fonts.
You can set any font color you like using color attribute. You can specify the color that you want by either the color name or hexadecimal code for that color.
Note − You can check a complete list of HTML Color Name with Codes.
This will produce the following result −
The <basefont> element is supposed to set a default font size, color, and typeface for any parts of the document that are not otherwise contained within a <font> tag. You can use the <font> elements to override the <basefont> settings.
The <basefont> tag also takes color, size and face attributes and it will support relative font setting by giving size a value of +1 for a size larger or −2 for two sizes smaller.
This will produce the following result −
HTML Forms are required, when you want to collect some data from the site visitor. For example, during user registration you would like to collect information such as name, email address, credit card, etc.
A form will take input from the site visitor and then will post it to a back-end application such as CGI, ASP Script or PHP script etc. The back-end application will perform required processing on the passed data based on defined business logic inside the application.
There are various form elements available like text fields, textarea fields, drop-down menus, radio buttons, checkboxes, etc.
The HTML <form> tag is used to create an HTML form and it has following syntax −
Apart from common attributes, following is a list of the most frequently used form attributes −
action
Backend script ready to process your passed data.
method
Method to be used to upload data. The most frequently used are GET and POST methods.
target
Specify the target window or frame where the result of the script will be displayed. It takes values like _blank, _self, _parent etc.
enctype
You can use the enctype attribute to specify how the browser encodes the data before it sends it to the server. Possible values are −
application/x-www-form-urlencoded − This is the standard method most forms use in simple scenarios.
mutlipart/form-data − This is used when you want to upload binary data in the form of files like image, word file etc.
Note − You can refer to Perl & CGI for a detail on how form data upload works.
There are different types of form controls that you can use to collect data using HTML form −
There are three types of text input used on forms −
Single-line text input controls − This control is used for items that require only one line of user input, such as search boxes or names. They are created using HTML <input> tag.
Password input controls − This is also a single-line text input but it masks the character as soon as a user enters it. They are also created using HTMl <input> tag.
Multi-line text input controls − This is used when the user is required to give details that may be longer than a single sentence. Multi-line input controls are created using HTML <textarea> tag.
This control is used for items that require only one line of user input, such as search boxes or names. They are created using HTML <input> tag.
Here is a basic example of a single-line text input used to take first name and last name −
This will produce the following result −
Following is the list of attributes for <input> tag for creating text field.
type
Indicates the type of input control and for text input control it will be set to text.
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
value
This can be used to provide an initial value inside the control.
size
Allows to specify the width of the text-input control in terms of characters.
maxlength
Allows to specify the maximum number of characters a user can enter into the text box.
This is also a single-line text input but it masks the character as soon as a user enters it. They are also created using HTML <input>tag but type attribute is set to password.
Here is a basic example of a single-line password input used to take user password −
This will produce the following result −
Following is the list of attributes for <input> tag for creating password field.
type
Indicates the type of input control and for password input control it will be set to password.
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
value
This can be used to provide an initial value inside the control.
size
Allows to specify the width of the text-input control in terms of characters.
maxlength
Allows to specify the maximum number of characters a user can enter into the text box.
This is used when the user is required to give details that may be longer than a single sentence. Multi-line input controls are created using HTML <textarea> tag.
Here is a basic example of a multi-line text input used to take item description −
This will produce the following result −
Following is the list of attributes for <textarea> tag.
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
rows
Indicates the number of rows of text area box.
cols
Indicates the number of columns of text area box
Checkboxes are used when more than one option is required to be selected. They are also created using HTML <input> tag but type attribute is set to checkbox..
Here is an example HTML code for a form with two checkboxes −
This will produce the following result −
Following is the list of attributes for <checkbox> tag.
type
Indicates the type of input control and for checkbox input control it will be set to checkbox..
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
value
The value that will be used if the checkbox is selected.
checked
Set to checked if you want to select it by default.
Radio buttons are used when out of many options, just one option is required to be selected. They are also created using HTML <input> tag but type attribute is set to radio.
Here is example HTML code for a form with two radio buttons −
This will produce the following result −
Following is the list of attributes for radio button.
type
Indicates the type of input control and for checkbox input control it will be set to radio.
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
value
The value that will be used if the radio box is selected.
checked
Set to checked if you want to select it by default.
A select box, also called drop down box which provides option to list down various options in the form of drop down list, from where a user can select one or more options.
Here is example HTML code for a form with one drop down box
This will produce the following result −
Following is the list of important attributes of <select> tag −
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
size
This can be used to present a scrolling list box.
multiple
If set to "multiple" then allows a user to select multiple items from the menu.
Following is the list of important attributes of <option> tag −
value
The value that will be used if an option in the select box box is selected.
selected
Specifies that this option should be the initially selected value when the page loads.
label
An alternative way of labeling options
If you want to allow a user to upload a file to your web site, you will need to use a file upload box, also known as a file select box. This is also created using the <input> element but type attribute is set to file.
Here is example HTML code for a form with one file upload box −
This will produce the following result −
Following is the list of important attributes of file upload box −
name
Used to give a name to the control which is sent to the server to be recognized and get the value.
accept
Specifies the types of files that the server accepts.
There are various ways in HTML to create clickable buttons. You can also create a clickable button using <input>tag by setting its type attribute to button. The type attribute can take the following values −
submit
This creates a button that automatically submits a form.
reset
This creates a button that automatically resets form controls to their initial values.
button
This creates a button that is used to trigger a client-side script when the user clicks that button.
image
This creates a clickable button but we can use an image as background of the button.
Here is example HTML code for a form with three types of buttons −
This will produce the following result −
Hidden form controls are used to hide data inside the page which later on can be pushed to the server. This control hides inside the code and does not appear on the actual page. For example, following hidden form is being used to keep current page number. When a user will click next page then the value of hidden control will be sent to the web server and there it will decide which page will be displayed next based on the passed current page.
Here is example HTML code to show the usage of hidden control −
This will produce the following result −
Sometimes you need to add music or video into your web page. The easiest way to add video or sound to your web site is to include the special HTML tag called <embed>. This tag causes the browser itself to include controls for the multimedia automatically provided browser supports <embed> tag and given media type.
You can also include a <noembed> tag for the browsers which don't recognize the <embed> tag. You could, for example, use <embed> to display a movie of your choice, and <noembed> to display a single JPG image if browser does not support <embed> tag.
Here is a simple example to play an embedded midi file −
Following is the list of important attributes which can be used with <embed> tag.
Note −The align and autostart attributes deprecated in HTML5. Do not use these attributes.
align
Determines how to align the object. It can be set to either center, left or right.
autostart
This boolean attribute indicates if the media should start automatically. You can set it either true or false.
loop
Specifies if the sound should be played continuously (set loop to true), a certain number of times (a positive value) or not at all (false)
playcount
Specifies the number of times to play the sound. This is alternate option for loop if you are usiong IE.
hidden
Specifies if the multimedia object should be shown on the page. A false value means no and true values means yes.
width
Width of the object in pixels
height
Height of the object in pixels
name
A name used to reference the object.
src
URL of the object to be embedded.
volume
Controls volume of the sound. Can be from 0 (off) to 100 (full volume).
You can use various media types like Flash movies (.swf), AVI's (.avi), and MOV's (.mov) file types inside embed tag.
.swf files − are the file types created by Macromedia's Flash program.
.wmv files − are Microsoft's Window's Media Video file types.
.mov files − are Apple's Quick Time Movie format.
.mpeg files − are movie files created by the Moving Pictures Expert Group.
This will produce the following result −
You can use HTML <bgsound> tag to play a soundtrack in the background of your webpage. This tag is supported by Internet Explorer only and most of the other browsers ignore this tag. It downloads and plays an audio file when the host document is first downloaded by the user and displayed. The background sound file also will replay whenever the user refreshes the browser.
Note − The bgsound tag is deprecated and it is supposed to be removed in a future version of HTML. So they should not be used rather, it's suggested to use HTML5 tag audio for adding sound. But still for learning purpose, this chapter will explain bgsound tag in detail.
This tag is having only two attributes loop and src. Both these attributes have same meaning as explained above.
Here is a simple example to play a small midi file −
This will produce the blank screen. This tag does not display any component and remains hidden.
Internet Explorer can also handle only three different sound format files − wav, the native format for PCs; au, the native format for most Unix workstations; and MIDI, a universal music-encoding scheme.
HTML 4 introduces the <object> element, which offers an all-purpose solution to generic object inclusion. The <object> element allows HTML authors to specify everything required by an object for its presentation by a user agent.
Here are a few examples −
You can embed an HTML document in an HTML document itself as follows −
Here alt attribute will come into picture if browser does not support object tag.
You can embed a PDF document in an HTML document as follows −
You can specify some parameters related to the document with the <param> tag. Here is an example to embed a wav file −
You can add a flash document as follows −
You can add a java applet into HTML document as follows −
The classid attribute identifies which version of Java Plug-in to use. You can use the optional codebase attribute to specify if and how to download the JRE.
An HTML marquee is a scrolling piece of text displayed either horizontally across or vertically down your webpage depending on the settings. This is created by using HTML <marquees> tag.
Note − The <marquee> tag deprecated in HTML5. Do not use this element, instead you can use JavaScript and CSS to create such effects.
A simple syntax to use HTML <marquee> tag is as follows −
Following is the list of important attributes which can be used with <marquee> tag.
width
This specifies the width of the marquee. This can be a value like 10 or 20% etc.
height
This specifies the height of the marquee. This can be a value like 10 or 20% etc.
direction
This specifies the direction in which marquee should scroll. This can be a value like up, down, left or right.
behavior
This specifies the type of scrolling of the marquee. This can have a value like scroll, slide and alternate.
scrolldelay
This specifies how long to delay between each jump. This will have a value like 10 etc.
scrollamount
This specifies the speed of marquee text. This can have a value like 10 etc.
loop
This specifies how many times to loop. The default value is INFINITE, which means that the marquee loops endlessly.
bgcolor
This specifies background color in terms of color name or color hex value.
hspace
This specifies horizontal space around the marquee. This can be a value like 10 or 20% etc.
vspace
This specifies vertical space around the marquee. This can be a value like 10 or 20% etc.
Below are few examples to demonstrate the usage of marquee tag.
This will produce the following result −
This will produce the following result −
This will produce the following result −
This will produce the following result −
We have learnt that a typical HTML document will have following structure −
This chapter will give a little more detail about header part which is represented by HTML <head> tag. The <head> tag is a container of various important tags like <title>, <meta>, <link>, <base>, <style>, <script>, and <noscript> tags.
The HTML <title> tag is used for specifying the title of the HTML document. Following is an example to give a title to an HTML document −
This will produce the following result −
The HTML <meta> tag is used to provide metadata about the HTML document which includes information about page expiry, page author, list of keywords, page description etc.
Following are few of the important usages of <meta> tag inside an HTML document −
This will produce the following result −
The HTML <base> tag is used for specifying the base URL for all relative URLs in a page, which means all the other URLs will be concatenated into base URL while locating for the given item.
For example, all the given pages and images will be searched after prefixing the given URLs with base URL http://www.tutorialspoint.com/ directory −
This will produce the following result −
But if you change base URL to something else, for example, if base URL is http://www.tutorialspoint.com/home then image and other given links will become like http://www.tutorialspoint.com/home/images/logo.png and http://www.tutorialspoint.com/html/index.htm
The HTML <link> tag is used to specify relationships between the current document and external resource. Following is an example to link an external style sheet file available in css sub-directory within web root −
This will produce the following result −
The HTML <style> tag is used to specify style sheet for the current HTML document. Following is an example to define few style sheet rules inside <style> tag −
This will produce the following result −
Note − To learn about how Cascading Style Sheet works, kindly check a separate tutorial available at css
The HTML <script> tag is used to include either external script file or to define internal script for the HTML document. Following is an example where we are using JavaScript to define a simple JavaScript function −
This will produce the following result, where you can try to click on the given button −
Note − To learn about how JavaScript works, kindly check a separate tutorial available at javascript
Cascading Style Sheets (CSS) describe how documents are presented on screens, in print, or perhaps how they are pronounced. W3C has actively promoted the use of style sheets on the Web since the consortium was founded in 1994.
Cascading Style Sheets (CSS) provide easy and effective alternatives to specify various attributes for the HTML tags. Using CSS, you can specify a number of style properties for a given HTML element. Each property has a name and a value, separated by a colon (:). Each property declaration is separated by a semi-colon (;).
First let's consider an example of HTML document which makes use of <font> tag and associated attributes to specify text color and font size −
Note − The font tag deprecated and it is supposed to be removed in a future version of HTML. So they should not be used rather, it's suggested to use CSS styles to manipulate your fonts. But still for learning purpose, this chapter will work with an example using the font tag.
We can re-write above example with the help of Style Sheet as follows −
This will produce the following result −
You can use CSS in three ways in your HTML document −
External Style Sheet − Define style sheet rules in a separate .css file and then include that file in your HTML document using HTML <link> tag.
Internal Style Sheet − Define style sheet rules in header section of the HTML document using <style> tag.
Inline Style Sheet − Define style sheet rules directly along-with the HTML elements using style attribute.
Let's see all the three cases one by one with the help of suitable examples.
If you need to use your style sheet to various pages, then its always recommended to define a common style sheet in a separate file. A cascading style sheet file will have extension as .css and it will be included in HTML files using <link> tag.
Consider we define a style sheet file style.css which has following rules −
Here we defined three CSS rules which will be applicable to three different classes defined for the HTML tags. I suggest you should not bother about how these rules are being defined because you will learn them while studying CSS. Now let's make use of the above external CSS file in our following HTML document −
This will produce the following result −
If you want to apply Style Sheet rules to a single document only, then you can include those rules in header section of the HTML document using <style> tag.
Rules defined in internal style sheet overrides the rules defined in an external CSS file.
Let's re-write above example once again, but here we will write style sheet rules in the same HTML document using <style> tag −
This will produce the following result −
You can apply style sheet rules directly to any HTML element using style attribute of the relevant tag. This should be done only when you are interested to make a particular change in any HTML element only.
Rules defined inline with the element overrides the rules defined in an external CSS file as well as the rules defined in <style> element.
Let's re-write above example once again, but here we will write style sheet rules along with the HTML elements using style attribute of those elements.
This will produce the following result −
A script is a small piece of program that can add interactivity to your website. For example, a script could generate a pop-up alert box message, or provide a dropdown menu. This script could be written using JavaScript or VBScript.
You can write various small functions, called event handlers using any of the scripting language and then you can trigger those functions using HTML attributes.
Now-a-days, only JavaScript and associated frameworks are being used by most of the web developers, VBScript is not even supported by various major browsers.
You can keep JavaScript code in a separate file and then include it wherever it's needed, or you can define functionality inside HTML document itself. Let's see both the cases one by one with suitable examples.
If you are going to define a functionality which will be used in various HTML documents then it's better to keep that functionality in a separate JavaScript file and then include that file in your HTML documents. A JavaScript file will have extension as .js and it will be included in HTML files using <script> tag.
Consider we define a small function using JavaScript in script.js which has following code −
Now let's make use of the above external JavaScript file in our following HTML document −
This will produce the following result, where you can try to click on the given button −
You can write your script code directly into your HTML document. Usually we keep script code in header of the document using <script> tag, otherwise there is no restriction and you can put your source code anywhere in the document but inside <script> tag.
This will produce the following result, where you can try to click on the given button −
Event handlers are nothing but simply defined functions which can be called against any mouse or keyboard event. You can define your business logic inside your event handler which can vary from a single to 1000s of line code.
Following example explains how to write an event handler. Let's write one simple function EventHandler() in the header of the document. We will call this function when any user brings mouse over a paragraph.
Now This will produce the following result. Bring your mouse over this line and see the result −
Although most (if not all) browsers these days support JavaScript, but still some older browsers don't. If a browser doesn't support JavaScript, instead of running your script, it would display the code to the user. To prevent this, you can simply place HTML comments around the script as shown below.
You can also provide alternative info to the users whose browsers don't support scripts and for those users who have disabled script option their browsers. You can do this using the <noscript> tag.
There may be a situation when you will include multiple script files and ultimately using multiple <script> tags. You can specify a default scripting language for all your script tags. This saves you from specifying the language every time you use a script tag within the page. Below is the example −
Note that you can still override the default by specifying a language within the script tag.
A webpage layout is very important to give better look to your website. It takes considerable time to design a website's layout with great look and feel.
Now-a-days, all modern websites are using CSS and JavaScript based framework to come up with responsive and dynamic websites but you can create a good layout using simple HTML tables or division tags in combination with other formatting tags. This chapter will give you few examples on how to create a simple but working layout for your webpage using pure HTML and its attributes.
The simplest and most popular way of creating layouts is using HTML <table> tag. These tables are arranged in columns and rows, so you can utilize these rows and columns in whatever way you like.
For example, the following HTML layout example is achieved using a table with 3 rows and 2 columns but the header and footer column spans both columns using the colspan attribute −
This will produce the following result −
You can design your webpage to put your web content in multiple pages. You can keep your content in middle column and you can use left column to use menu and right column can be used to put advertisement or some other stuff. This layout will be very similar to what we have at our website tutorialspoint.com.
Here is an example to create three column layout −
This will produce the following result −
The <div> element is a block level element used for grouping HTML elements. While the <div> tag is a block-level element, the HTML <span> element is used for grouping elements at an inline level.
Although we can achieve pretty nice layouts with HTML tables, but tables weren't really designed as a layout tool. Tables are more suited to presenting tabular data.
Note − This example makes use of Cascading Style Sheet (CSS), so before understanding this example you need to have a better understanding on how CSS works.
Here we will try to achieve same result using <div> tag along with CSS, whatever you have achieved using <table> tag in previous example.
This will produce the following result −
You can create better layout using DIV, SPAN along with CSS.
"""
insertRecipeData("HTML", htmlData.replace("\n", " "))
# Python
pythonData = """
Python is a simple, general purpose, high level, and object-oriented programming language.
Python is an interpreted scripting language also. Guido Van Rossum is known as the founder of Python programming.
Our Python tutorial includes all topics of Python Programming such as installation, control statements, Strings, Lists, Tuples, Dictionary, Modules, Exceptions, Date and Time, File I/O, Programs, etc. There are also given Python interview questions to help you better understand Python Programming.
Python is a general purpose, dynamic, high-level, and interpreted programming language. It supports Object Oriented programming approach to develop applications. It is simple and easy to learn and provides lots of high-level data structures.
Python is easy to learn yet powerful and versatile scripting language, which makes it attractive for Application Development.
Python's syntax and dynamic typing with its interpreted nature make it an ideal language for scripting and rapid application development.
Python supports multiple programming pattern, including object-oriented, imperative, and functional or procedural programming styles.
Python is not intended to work in a particular area, such as web programming. That is why it is known as multipurpose programming language because it can be used with web, enterprise, 3D CAD, etc.
We don't need to use data types to declare variable because it is dynamically typed so we can write a=10 to assign an integer value in an integer variable.
Python makes the development and debugging fast because there is no compilation step included in Python development, and edit-test-debug cycle is very fast.
In most of the programming languages, whenever a new version releases, it supports the features and syntax of the existing version of the language, therefore, it is easier for the projects to switch in the newer version. However, in the case of Python, the two versions Python 2 and Python 3 are very much different from each other.
A list of differences between Python 2 and Python 3 are given below:
Unlike the other programming languages, Python provides the facility to execute the code using few lines. For example - Suppose we want to print the "Hello World" program in Java; it will take three lines to print it.
On the other hand, we can do this using one statement in Python.Both programs will print the same result, but it takes only one statement without using a semicolon or curly braces in Python.
There is no use of curly braces or semicolon in Python programming language. It is English-like language. But Python uses the indentation to define a block of code. Indentation is nothing but adding whitespace before the statement when it is needed. For example -
In the above example, the statements that are same level to right belong to the function. Generally, we can use four whitespaces to define indentation.
Python was invented by Guido van Rossum in 1991 at CWI in Netherland. The idea of Python programming language has taken from the ABC programming language or we can say that ABC is a predecessor of Python language.
There is also a fact behind the choosing name Python. Guido van Rossum was a fan of the popular BBC comedy show of that time, "Monty Python's Flying Circus". So he decided to pick the name Python for his newly created programming language.
Python has the vast community across the world and releases its version within the short period.
Python provides many useful features to the programmer. These features make it most popular and widely used language. We have listed below few-essential feature of Python.
Python is a general-purpose, popular programming language and it is used in almost every technical field. The various areas of Python use are given below.
Python has wide range of libraries and frameworks widely used in various fields such as machine learning, artificial intelligence, web applications, etc. We define some popular frameworks and libraries of Python as follows.
The print() function displays the given object to the standard output device (screen) or to the text stream file.
Unlike the other programming languages, Python print() function is most unique and versatile function.The syntax of print() function is given below.Let's explain its parameters one by one.Let's understand the following example.
Output:As we can see in the above output, the multiple objects can be printed in the single print() statement. We just need to use comma (,) to separate with each other.
Output:In the first print() statement, we use the sep and end arguments. The given object is printed just after the sep values. The value of end parameter printed at the last of given object. As we can see that, the second print() function printed the result after the three black lines.
Python provides the input() function which is used to take input from the user. Let's understand the following example.
Example -
Output:By default, the input() function takes the string input but what if we want to take other data types as an input.
If we want to take input as an integer number, we need to typecast the input() function into an integer.
For example -
Example -
Output:We can take any type of values using input() function.
Operators are the symbols which perform various operations on Python objects. Python operators are the most essential to work with the Python data types. In addition, Python also provides identify membership and bitwise operators. We will learn all these operators with the suitable example in following tutorial.
Conditional statements help us to execute a particular block for a particular condition. In this tutorial, we will learn how to use the conditional expression to execute a different block of statements. Python provides if and else keywords to set up logical conditions. The elif keyword is also used as conditional statement.
Sometimes we may need to alter the flow of the program. The execution of a specific code may need to be repeated several numbers of times. For this purpose, the programming languages provide various types of loops capable of repeating some specific code several times. Consider the following tutorial to understand the statements in detail.
Data structures are referred which can hold some data together or we say that they are used to store the data in organized way. Python provides built-in data structures such as list, tuple, dictionary, and set. We can perform complex tasks using data structures.
Python list holds the ordered collection of items. We can store a sequence of items in a list. Python list is mutable which means it can be modified after its creation. The items of lists are enclosed within the square bracket [] and separated by the comma. Let's see the example of list.
If we try to print the type of L1, L2, and L3 using type() function then it will come out to be a list.
Output:To learn more about list, visit the following tutorial.
Python Tuple is used to store the sequence of immutable Python objects. The tuple is similar to lists since the value of the items stored in the list can be changed, whereas the tuple is immutable, and the value of the items stored in the tuple cannot be changed.
Tuple can be defined as follows
Example -
Output:If we try to add new to the tuple, it will throw an error.
Example -
Output:The above program throws an error because tuples are immutable type. To learn more about tuple, visit the Python Tuples.
Python string is a sequence of characters. It is a collection of the characters surrounded by single quotes, double quotes, or triple quotes. It can also define as collection of the Unicode characters. We can create a string as follows.
Example -
Output:Python doesn't support the character data-type. A single character written as 'p' is treated as a string of length 1.
Stings are also immutable. We can't change after it is declared. To learn more about the string, visit the following tutorial.
Python Dictionary is a most efficient data structure and used to store the large amount of data. It stores the data in the key-value pair format. Each value is stored corresponding to its key.
Keys must be a unique and value can be any type such as integer, list, tuple, etc.
It is a mutable type; we can reassign after its creation. Below is the example of creating dictionary in Python.
Example -
Output:The empty curly braces {} are used to create empty dictionary. To learn more, visit the complete tutorial of the dictionary.
A Python set is a collection of unordered elements. Each element in set must be unique and immutable. Sets are mutable which means we can modify anytime throughout the program. Let's understand the example of creating set in Python.
Example -
Output:To get the more information about sets, visit the following resources.
This section of Python tutorial defines some important tools related to functional programming such as lambda and recursive functions. These functions are very efficient in accomplishing the complex tasks. We define a few important functions, such as reduce, map, and filter. Python provides the functools module that includes various functional programming tools. Visit the following tutorial to learn more about functional programming.
Files are used to store data in a computer disk. In this tutorial, we explain the built-in file object of Python. We can open a file using Python script and perform various operations such as writing, reading, and appending. There are various ways of opening a file. We are explained with the relevant example. We will also learn to perform read/write operations on binary files.
Python modules are the program files that contain a Python code or functions. There are two types of module in the Python - User-define modules and built-in modules. A module that the user defines, or we can say that our Python code saved with .py extension, is treated as a user-define module.
Built-in modules are predefined modules of Python. To use the functionality of the modules, we need to import them into our current working program.
An exception can be defined as an unusual condition in a program resulting in the interruption in the flow of the program.
Whenever an exception occurs, the program stops the execution, and thus the further code is not executed. Therefore, an exception is the run-time errors that are unable to handle to Python script. An exception is a Python object that represents an error.
A csv stands for "comma separated values", which is defined as a simple file format that uses specific structuring to arrange tabular data. It stores tabular data such as spreadsheet or database in plain text and has a common format for data interchange. A csv file opens into the excel sheet, and the rows and columns data define the standard format. Visit the following tutorial to learn the CSV module in detail.
We can send or read a mail using the Python script. Python's standard library modules are useful for handling various protocols such as PoP3 and IMAP. We will learn how to send a mail with the popular email service SMTP from a Python script.
Python magic method is defined as the special method which adds "magic" to a class. It starts and ends with double underscores, for example, _init_ or _str_.
The built-in classes define many magic methods. The dir() function can be used to see the number of magic methods inherited by a class. It has two prefixes and suffix underscores in the method name.
Everything in Python is treated as an object including integer values, floats, functions, classes, and none. Apart from that, Python supports all oriented concepts. Below is the brief introduction of oops concepts of Python.
To read the oops concept in detail, visit the following resources.Python includes many advance and useful concepts that help the programmer to solve the complex tasks. These concepts are given below.
An iterator is simply an object that can be iterated upon. It returns one object at a time. It can be implemented using the two special methods, __iter__() and __next__().
To learn more about the iterators visit our Python Iterators tutorial.The Generators are an easiest way of creating Iterators. To learn more about, visit our Python Generators tutorial.
These are used to modify the behavior of the function. Decorators provide the flexibility to wrap another function to expand the working of wrapped function, without permanently modifying it.
"""
insertRecipeData("PYTHON", pythonData.replace("\n", " "))
print(retrieveCorpusData())
print(retrieveCorpusDataWithItemName("PYTHON"))
