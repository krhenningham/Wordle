from wordle_result import LetterAnalysis

def analyze(word, target):
    '''Core function used to analyze both the guessed word and the target word.
     checks each letter in both words to see if they match up or not. returns the results in a dictionary'''
    result = {}


    for i, character in enumerate(word):
        if character == target[i]:
            result[i] = LetterAnalysis.EXACT_MATCH
        elif character in target:
            result[i] = LetterAnalysis.PARTIAL_MATCH
        else:
            result[i] = LetterAnalysis.NO_MATCH

    return result