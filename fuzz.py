import os
import random
import ast
from datetime import datetime
import time
import sys
import lint_engine
import py_parser
import main

def random_string(length=10):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

def random_filepath():
    return os.path.join(random_string(), random_string() + '.py')

def fuzz_getDataLoadCount():
    filepath = random_filepath()
    try:
        lint_engine.getDataLoadCount(filepath)
        print(f"Fuzzed getDataLoadCount with: {filepath}")
    except Exception as e:
        print(f"Error during fuzzing getDataLoadCount: {e}")

def fuzz_getModelLoadCounta():
    filepath = random_filepath()
    try:
        lint_engine.getModelLoadCounta(filepath)
        print(f"Fuzzed getModelLoadCounta with: {filepath}")
    except Exception as e:
        print(f"Error during fuzzing getModelLoadCounta: {e}")

def fuzz_getFunctionDefinitions():
    try:
        tree = ast.parse(f"class Test:\n    def {random_string()}(self): pass")
        py_parser.getFunctionDefinitions(tree)
        print("Fuzzed getFunctionDefinitions with a random AST tree")
    except Exception as e:
        print(f"Error during fuzzing getFunctionDefinitions: {e}")

def fuzz_getPythonAtrributeFuncs():
    try:
        tree = ast.parse(f"obj.{random_string()}()")
        py_parser.getPythonAtrributeFuncs(tree)
        print("Fuzzed getPythonAtrributeFuncs with a random AST tree")
    except Exception as e:
        print(f"Error during fuzzing getPythonAtrributeFuncs: {e}")

def fuzz_giveTimeStamp():
    try:
        timestamp = main.giveTimeStamp()
        print(f"Fuzzed giveTimeStamp: Returned {timestamp}")
    except Exception as e:
        print(f"Error during fuzzing giveTimeStamp: {e}")

if __name__ == "__main__":
    print("Starting fuzzing...")
    for _ in range(20):
        fuzz_getDataLoadCount()
        fuzz_getModelLoadCounta()
        fuzz_getFunctionDefinitions()
        fuzz_getPythonAtrributeFuncs()
        fuzz_giveTimeStamp()
    print("Fuzzing complete.")
