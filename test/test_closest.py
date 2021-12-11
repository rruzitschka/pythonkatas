from src.closest import *
#requirements for the 'closest' kata

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
ref_word = "zero"
test_word_close ="azbecrdo"
test_word_close2 = "zaebrcod"
test_word_close_mixed_order ="aebzcrdo"
test_word_not_close = "ztuztuzwre"
test_word_ordererd_less = "orderz"

def test_check_close():
    #this checks if all of the characters of the reference words are cotained in the test_word
    assert (check_close(test_word_close, ref_word) == True)

def test_check_not_close():
    assert (check_close(test_word_not_close, ref_word) == False)

def test_check_position_ok():
    #check_postion returns the positions of the reference words characters in the test_word
    assert (check_position (test_word_close, ref_word) == [1,3,5,7])

def test_check_position_ref_word():
    assert (check_position(ref_word, ref_word) == [0,1,2,3])

def test_check_postion_orderd_less():
    assert(check_position(test_word_ordererd_less, ref_word) == [5,3,1,0])

def test_order_score():
    #if the order of the characteres of the ref_word is maintained, the score is 0
    #if the order is reversed,the score is len(ref_word)

    positions1=[1,3,5,7]
    positions2=[5,3,1,0]
    positions3=[5,3,1,2]
    assert(order_score(positions1) == 0 )
    assert(order_score(positions2) == 3)
    assert(order_score(positions3) == 2)



def test_compare_order():
    #if the first argument is orderd more then the second argument than the fucntion gives True
    #ref_word is the reference word that is used to determine closeness
    assert (compare_order(test_word_close, test_word_ordererd_less, ref_word) == True)

def tesst_compare_order_tie():
    #if both words have the same order_score the returned value is "TIE"
    assert (compare_order(test_word_close, ref_word, ref_word) == "TIE")

#this is the test now for the overall kata requirenent

# test if there is no close word

def test_closest_no_close_word():
    test_word_list = ["sdfsdf", "zer", "ertuhj", "jklökrdmr"]
    assert (closest(test_word_list, ref_word) == "No close word found")


def test_closest_single_close_word():
    test_word_list = ["sdfsdf", "zer", "ertuhj", "jklökrdmr", test_word_close]
    assert (closest(test_word_list, ref_word) == test_word_close)

def test_closest_multiple_close_words_different_length():
    test_word_list = ["sdfsdf", "zer", "ertuhj", "jklökrdmr", test_word_close, "zkjhkjkhehkhrkjhhuuo"]
    assert (closest(test_word_list, ref_word) == test_word_close)


def test_closest_multiple_close_words_same_length():
    #if there are multiple close words with the same length, the order decides
    test_word_list = ["sdfsdf", "zer", "ertuhj", "jklökrdmr", test_word_close, "zkjhkjkhehkhrkjhhuuo", test_word_close_mixed_order]
    assert (closest(test_word_list, ref_word) == test_word_close)

def test_closest_multiple_close_words_same_order():
    #now we even have multiple close words with the same order! So the position in the initial word list decides.
    test_word_list = ["sdfsdf", test_word_close2, "zer", "ertuhj", "jklökrdmr", test_word_close, "zkjhkjkhehkhrkjhhuuo", test_word_close_mixed_order]
    assert (closest(test_word_list, ref_word) == test_word_close2)

def test_closest():
    test_word_list = ["sdfsdf",test_word_close2, "zer", "ertuhj", "jklökrdmr", test_word_close, "zkjhkjkhehkhrkjhhuuo",
                      test_word_close_mixed_order]
    assert (closest(test_word_list, ref_word) == test_word_close2)


