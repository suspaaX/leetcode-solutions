licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
Output =  "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.


# licensePlate = "1s3 456"
# words = ["looks","pest","stew","show"]
# Output= "pest"


def shortestCompletingWord(licensePlate,words) :
    pass


(shortestCompletingWord(licensePlate,words))