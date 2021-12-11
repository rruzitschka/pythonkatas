
#Part 2 of closest to zero kata : https://www.sammancoaching.org/kata_descriptions/closest_to_zero.html
# I tried to work in real TDD mode: creat test -fail -refactor until pass

#Given a list of strings, find the one closest to “zero”.
# A word is close to “zero” if it contains the same letters.
# If more than one word contains the same letters, choose the shortest one.
# If more than one is the same length, choose the one with the letters in the most similar order.
# If there is still a tie, choose the one that appeared first in the original list.
#test list
# check if a single word is close to zero
# return the length of a word (no need to test, built in)
# return a score how close a word is to zero: if letters are in the perfect order, score is 4
# return a list of words close to zero

def check_close(test_word, ref_word):
     close=True
     for i in range(len(ref_word)):
         if test_word.find(ref_word[i])== -1:
             close = False

     return close

def check_position (word, ref_word):
    pos = []
    for i in range (len(ref_word)):
        pos.append(word.find(ref_word[i]))

    return pos

# this function returns a score for th order of the characters, if they are ordered like the reference word, the score is 0
# more ordered means a smaller order score
def order_score(pos):
    score=0;
    for i in range(len(pos)-1):
        if pos[i]>pos[i+1]:
            score += 1

    return score


def compare_order(word1, word2, ref_word):
# get the order_score for the two words:
# 1) get the positions for word1 and word 2
# 2) get the order scores for the positions
# 3) return true if the order_score of word 1 is smaller
    pos1 = check_position(word1, ref_word)
    pos2 = check_position(word2, ref_word)

    if order_score(pos1) < order_score(pos2):
        return True
    if order_score(pos1) > order_score(pos2):
        return False
    if order_score(pos1) == order_score(pos2):
        return "TIE"


def closest(word_list, ref_word):
    close_word_list = []
    for i in range (len(word_list)):
        if check_close(word_list[i], ref_word):         #is the word close at all? then add it to the list of close words
          close_word_list.append(word_list[i])
    if len(close_word_list) == 0:
        return "No close word found"    # not a single word is close!
# do we have more than one word?
    if len(close_word_list) == 1:  # we have found a single close word
        return close_word_list[0]

# we haver mor than one, no find out the shortest
    close_word_list_min_length = [] #this could be list if multiple words have the same min length
    min_length = len(close_word_list[0]) # fetch the lenght of the first close word a s starting point
    for i in range(len(close_word_list)):
        if len(close_word_list[i])<min_length:
            min_length = len(close_word_list[i])

    #now we have the minimum length, lets collect all the words of that length

    for i in range (len(close_word_list)):
        if len(close_word_list[i]) == min_length:
            close_word_list_min_length.append(close_word_list[i]) # put the word on the list

    # do we have only one word on the list? send it back!
    if len(close_word_list_min_length) == 1:
        return close_word_list_min_length[0]

    close_word_list = close_word_list_min_length #reduce the close_word_list, we have eliminated already some words
# we have more than one close word of the same length, now let's select by order. First find out the minimum order
    close_word_list_min_order = [] #this could be list if multiple words have the same min order
    min_order_score = order_score(check_position(close_word_list[0], ref_word)) # fetch the order score of the first left word
    for i in range(len(close_word_list)):
        word_order_score = order_score(check_position(close_word_list[i], ref_word))
        if word_order_score<min_order_score:
            min_order_score = word_order_score

    #now we have the minimum order score, lets collect all the words of that order score

    for i in range (len(close_word_list)):
        word_order_score = order_score(check_position(close_word_list[i], ref_word))
        if word_order_score == min_order_score:
            close_word_list_min_order.append(close_word_list[i]) # put the word on the list

    # do we have only one word on the list? send it back!
    if len(close_word_list_min_order) == 1:
        return close_word_list_min_order[0]

    #we still have multiple words in the list with the same order, now the position in th original word list decides
    min_index = word_list.index(close_word_list_min_order[0]) #start with the index of the forst word still available
    for i in range (len(close_word_list_min_order)):
        word_index = word_list.index(close_word_list_min_order[i])
        if word_index < min_index:
            min_index = word_index
    # now we have found the word with the minimum index number of the initial list and we are done.
    return word_list[min_index]
