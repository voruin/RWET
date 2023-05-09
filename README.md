# RWET
For the final assignment, I tried to write source code poems.

The functions implemented so far are: 

1. Randomly generate a short source code poem using words from the corpus of *gutenberg-poetry-v001.ndjson.gz*. 

2. Based on the words in the user input prompts, first find a similar sentence in the corpus (poems about love from 20th Centuray) and use them as the  prompt of a fine-tuned GPT2 model to generate a paragraph. The intention is to use all the nouns and verbs in the paragraph in the final source code poem, but I am not sure how to write logics for each word in the tracery model when the length of the array of nouns and verbs is not fixed. So for now it is still randomly choosing 1-2 nouns as variables and 1 verb as function name (which may appear) to also write a short source code poem.
