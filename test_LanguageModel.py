import pytest
from LanguageModel import LanguageModel

#This is a helper function to test the matplotlib. This sets up the graph

def plot_graph(devices, positive, neutral, negative, output_file="CardReviewsTest.png"):
    import matplotlib.pyplot as plt

    
    bar_width = 0.25
    x = range(len(devices))

    
    plt.bar([pos - bar_width for pos in x], positive, bar_width, label="Positive", color="green")
    plt.bar(x, neutral, bar_width, label="Neutral", color="blue")
    plt.bar([pos + bar_width for pos in x], negative, bar_width, label="Negative", color="red")

    
    plt.xlabel("Devices", fontsize=12)
    plt.ylabel("Number of Reviews", fontsize=12)
    plt.title("Card Reviews", fontsize=14)
    plt.xticks(ticks=x, labels=devices)
    plt.legend()

    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()

#This test tests that when a languagemodel object is called, it is made properly

def testInitialization():
    lm = LanguageModel("input.txt", "output.txt")
    assert lm.reviewFile == "input.txt"
    assert lm.outputFile == "output.txt"
    assert lm.posCount == 0
    assert lm.negCount == 0
    assert lm.neutCount == 0

#Given a review that should be neutral, this test makes sure that the model notices

def testNeutral(tmp_path):
    input_file = tmp_path / "input2.txt"
    input_file.write_text("The product is okay, not great but not bad.")
    output_file = tmp_path / "output2.txt"

    lm = LanguageModel(input_file, output_file)
    lm.runModel()

    assert lm.posCount == 0
    assert lm.negCount == 0
    assert lm.neutCount == 1


    ##Given a review that should be positive, this test makes sure that the model notices
    

def testPositive(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("This is a great product!")
    output_file = tmp_path / "output.txt"

    lm = LanguageModel(input_file, output_file)
    lm.runModel()
    assert lm.posCount == 1
    assert lm.negCount == 0
    assert lm.neutCount == 0


#This test makes sure that a graph gets created.
def testGraphGeneration():
    import os
    devices = ["4090", "4080", "4070", "4060"]
    positive = [10, 20, 15, 5]
    negative = [5, 10, 20, 25]
    neutral = [15, 10, 15, 20]

    plot_graph(devices, positive, negative, neutral)
    assert os.path.exists("CardReviewsTest.png")



