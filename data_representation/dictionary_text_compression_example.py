# Based upon a question from the 2019 Oxford Computing Challenge - https://challenge.tcsocc.uk/index.php?action=user_question&grq_id=932
words = ["a","about","alice","an","and","another","anything","as","at","be","beautiful","been","brought","by","called","came","come","did","do","done","door","down","eyes","face","feet","felt","first","fish","footman","for","four","frighten","frog","garden","get","go","had","have","herself","high","him","his","house","how","i","in","inches","into","is","it","judging","knuckles","large","like","little","livery","lives","long","looking","loudly","minute","near","never","next","nine","not","of","only","open","opened","or","out","place","quite","rapped","right","round","running","said","she","should","since","size","so","stood","strange","suddenly","that","the","them","their","there","thing","this","thought","till","to","two","upon","venture","was","when","with","whoever","why","will","wits","wonder","wood","would"]

encoded_string = "49 100 83 57 81 79 36 11 6 61 88 75 82 87 49 25 73 85 8 26 88 63 92 48 96 34 47 87 10 33 43 48 87 96 9 19 44 107 7 79 78 93 79 15 86 98 3 68 72 102 0 54 42 45 49 1 30 24 39 103 56 91 94 2 49 105 62 18 96 16 98 89 93 82 104 44 80 31 89 71 66 90 106 79 17 65 99 96 35 61 88 42 95 79 36 12 38 21 96 64 46 39 29 0 60 70 97 79 84 58 8 88 42 101 86 0 28 45 55 15 77 71 66 88 108 50 13 41 23 67 79 109 37 14 40 0 27 4 74 59 8 88 20 102 41 51 49 100 69 13 5 28 45 55 102 0 76 23 4 52 22 53 0 32"

word_numbers = encoded_string.split(" ")
word_numbers = map(int, word_numbers)

output = ""

for wn in word_numbers:

    output += words[wn] + " "

print(output)