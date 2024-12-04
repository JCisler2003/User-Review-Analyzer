#This program will take a text file with prompts, pass it into the phi3 language model, and store the output into another text file
#If the user does not have the phi3.5 model already installed, the program automatically installs it

#CS 325 Project 1 - Created by Joseph Cisler


import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import linecache as lc
import matplotlib.pyplot as plt

class LanguageModel:
    def __init__ (self, fileName, outputFile):
            self.reviewFile = fileName
            self.outputFile = outputFile
            self.posCount = 0
            self.negCount = 0
            self.neutCount = 0

    def runModel(self):


        # Load the model and tokenizer from HF
        model_name = "microsoft/Phi-3.5-mini-instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = AutoModelForCausalLM.from_pretrained(model_name).to(device)


        #Create the new text file and overwrite the file if it is already there
        open(self.outputFile, 'w')

        #Opens the file with the prompts and allows it to be read
        with open(self.reviewFile, 'r', encoding = 'UTF-8', errors = 'ignore') as textFile:

            #Retrieves the first line in the prompts text file
            startPrompt = 'Please tell me whether each following comment is Positive, neutral, or negative. One word answers only. Ignore irrelevant phrases like "Read more" and "The media could not be loaded. Do not give any other comments."'
            inputText = textFile.readline()
            inputText = inputText.strip()
            full_prompt = f"{startPrompt} {inputText}"


            #Loops until there are no more lines in the prompt file
            while inputText: 



                # Tokenize the text
                inputs = tokenizer(full_prompt, return_tensors="pt").to(device)

                # Generate outputs using the model
                output = model.generate(**inputs, max_new_tokens= 50)

                # Decode the output into regular text
                output_text = tokenizer.decode(output[0], skip_special_tokens=True, errors = 'ignore')

                #Appends the answers text file and adds the new output
                with open(self.outputFile, 'a', encoding = 'UTF-8', errors = 'ignore') as output:
                    output.write(output_text)

                    #Since phi 3.5 loved to add extra comments after the initial comments, the following code is used to find the answer to the review.
                    #Because Phi 3.5 always said the answer within the first four lines, the following code checks each line to see where the review is located.
                    
                    #Checks to see which line has output in them
                    lines = output_text.splitlines()
                    firstLine = lines[1] if len(lines) > 1 else None
                    secondLine = lines[2] if len(lines) > 2 else None
                    thirdLine = lines[3] if len(lines) > 3 else None
                    fourthLine = lines[4] if len(lines) > 4 else None

                    #Initialize reviewFound. Will turn true when an acceptable response is found.
                    reviewFound = False

                    #Checks if the second output line has the review
                    if firstLine:
                        if(firstLine.split()[-1] in ['Positive', 'Negative', 'Neutral','positive', 'negative', 'neutral'] and reviewFound == False):
                    
                            if(firstLine.split()[-1] in ['Positive','positive']):
                                self.posCount += 1

                            elif(firstLine.split()[-1] in ['Negative', 'negative']):
                                self.negCount += 1

                            else:
                                self.neutCount += 1
                        
                            reviewFound = True
                    
                     #Checks if the third output line has the review

                    if secondLine:
                        if(secondLine.split()[-1] in ['Positive', 'Negative', 'Neutral','positive', 'negative', 'neutral'] and reviewFound == False):

                            if(secondLine.split()[-1] in ['Positive','positive']):
                                self.posCount += 1

                            elif(secondLine.split()[-1] in ['Negative', 'negative']):
                                self.negCount += 1

                            else:
                                self.neutCount += 1


                            reviewFound = True
                    
                     #Checks if the fourth output line has the review
                    if thirdLine:
                        if(thirdLine.split()[-1] in ['Positive', 'Negative', 'Neutral','positive', 'negative', 'neutral'] and reviewFound == False):

                            if(thirdLine.split()[-1] in ['Positive','positive']):
                                self.posCount += 1

                            elif(thirdLine.split()[-1] in ['Negative', 'negative']):
                                self.negCount += 1

                            else:
                                self.neutCount += 1

                            reviewFound = True

                     #Checks if the fifth output line has the review
                    if fourthLine:
                        if(fourthLine.split()[-1] in ['Positive', 'Negative', 'Neutral', 'positive', 'negative', 'neutral'] and reviewFound == False):
    
                            if(fourthLine.split()[-1] in ['Positive','positive']):
                                self.posCount += 1

                            elif(fourthLine.split()[-1] in ['Negative', 'negative']):
                                self.negCount += 1

                            else:
                                self.neutCount += 1
                            
                            reviewFound = True



                inputText = textFile.readline()
                inputText = inputText.strip()
                full_prompt = f"{startPrompt} {inputText}"

            textFile.close()

#Pytest kept running this part, so I needed to add this if statement
if __name__ == "__main__":
    file4090 = LanguageModel('4090.txt', '4090comments.txt')
    file4090.runModel()

    file4080 = LanguageModel('4080.txt', '4080comments.txt')
    file4080.runModel()

    file4070 = LanguageModel('4070.txt', '4070comments.txt')
    file4070.runModel()

    file4060 = LanguageModel('4060.txt', '4060comments.txt')
    file4060.runModel()



    #Sets data points with names and values
    devices = ['4090', '4080', '4070', '4060']
    positive = [file4090.posCount, file4080.posCount, file4070.posCount, file4060.posCount]
    negative = [file4090.negCount, file4080.negCount, file4070.negCount, file4060.negCount]
    neutral = [file4090.neutCount, file4080.neutCount, file4070.neutCount, file4060.neutCount]

    # Define bar width and position
    bar_width = 0.25
    x = range(len(devices))

    # Plot bars for each type
    plt.bar([pos - bar_width for pos in x], positive, bar_width, label='Positive', color='green')
    plt.bar(x, neutral, bar_width, label='Neutral', color='blue')
    plt.bar([pos + bar_width for pos in x], negative, bar_width, label='Negative', color='red')

    # Add labels and title
    plt.xlabel('Devices', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.title('Card Reviews', fontsize=14)
    plt.xticks(ticks=x, labels=devices)
    plt.legend()

    plt.tight_layout()

    # Save the graph to a file
    plt.savefig('CardReviews.png', dpi=300)