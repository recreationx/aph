from redbaron import RedBaron, nodes
import openai
import argparse

parser = argparse.ArgumentParser(description='Generate docstrings for functions in a file.')
parser.add_argument('filename', help='The file to generate docstrings for.')
parser.add_argument('output', help='The filename to output the modified file to.')
parser.add_argument('api_key', help='The OpenAI API key to use.')
args = parser.parse_args()

class GPTFactory:
    def __init__(self, api_token):
        openai.api_key = api_token
        
    def process_function_name(self, function_name):
        """Attempt to generate a docstring for the given function name."""
        a = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Write a docstring for the function {function_name}",
            max_tokens=32
        )
        return a.choices[0].text.strip()
        

    
class CodeModifier:
    def __init__(self, filename, factory):
        """Initializes the class with the filename of the source code"""
        self.filename = filename
        self.factory = factory
    
    def initialize_tree(self):
        """Initializes the RedBaron tree with the source code from the file"""
        with open(self.filename, 'r') as source_code:
            self.tree = RedBaron(source_code.read())

    def output_tree(self):
        """Outputs the modified tree to the file"""
        with open(args.output, 'w') as source_code:
            source_code.write(self.tree.dumps())
    
    def replace_docstrings(self):
        """Replaces the docstrings in the source code with a auto-generated docstring"""
        for node in self.tree:
            # Checks if node is a function definition
            if isinstance(node, nodes.DefNode):
                # Checks if function definition starts with a string node
                if isinstance(node.value[0], nodes.StringNode):
                    # Is this an intended docstring? Yes, if it starts with triple quotes
                    if node.value[0].value.startswith('"""'):
                        docstring = node.value[0].value.strip('"""')
                        # Replace docstring with auto-generated docstring
                        node.value[0].value = '"""' + self.factory.process_function_name(node.name) + '"""'

factory = GPTFactory(args.api_key)
code = CodeModifier(args.filename, factory)
code.initialize_tree()
code.replace_docstrings()
code.output_tree()