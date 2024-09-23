#This program will take a text file with prompts, pass it into the phi3 language model, and store the output into another text file
#If the user does not have the phi3 model already installed, the program automatically installs it

#CS 325 Project 1 - Created by Joseph Cisler


import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import linecache as lc

# Load the model and tokenizer from HF
model_name = "microsoft/Phi-3-mini-128k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

#Create the new text file and overwrite the file if it is already there
open('answers.txt', 'w')

#Opens the file with the prompts and allows it to be read
with open('Prompts.txt', 'r') as textFile:

    #Retrieves the first line in the prompts text file
    inputText = textFile.readline()

    #Loops until there are no more lines in the prompt file
    while inputText:



        # Tokenize the text
        inputs = tokenizer(inputText, return_tensors="pt")

        # Generate outputs using the model
        output = model.generate(**inputs, max_length=100)

        # Decode the output into regular text
        output_text = tokenizer.decode(output[0], skip_special_tokens=True)

        #Appends the answers text file and adds the new output
        with open('answers.txt', 'a') as output:
            output.write(output_text)
            output.write("\n")


        inputText = textFile.readline()

    textFile.close()