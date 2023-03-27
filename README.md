# Cimple_compiler
A Cimple compiler is a program that translates source code written in the Cimple programming language into executable code that can be run on a computer. 
Cimple is a simplified language that is designed to be easy to learn and use, with a small number of features that are suitable for teaching programming fundamentals.

A typical Cimple compiler consists of several stages:
Lexical analysis: 
The source code is broken down into a stream of tokens, each representing a basic unit of the language such as a keyword, identifier, or operator.

Syntax analysis: 
The tokens are analyzed to determine whether they conform to the rules of the language's grammar, and a tree-like structure called an abstract syntax tree (AST) is constructed to represent the program's structure.

Semantic analysis:
The AST is checked to ensure that it makes sense according to the rules of the language, such as type checking and scoping rules.

Code generation:
The AST is transformed into a lower-level representation, such as assembly code or machine code, that can be executed by the computer.

A Cimple compiler can be implemented in many different programming languages, including Python. To create a Cimple compiler in Python, one can use a parser generator such as ANTLR or PLY to generate the parser for the language, and then write code to perform the remaining stages of the compilation process.

In my own implementation of a Cimple compiler in Python, I used PLY to generate the parser, and then wrote Python code to handle the remaining stages of compilation. 
The compiler supports a subset of the Cimple language, including basic arithmetic operations, conditional statements, and loops. The generated code is in the form of Python bytecode, which can be executed by the Python interpreter.

Overall, the Cimple compiler I created in Python demonstrates the process of translating high-level source code into executable code, and provides a useful tool for teaching and learning programming fundamentals.
