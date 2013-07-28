from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inverseIndex = {}

    for (docid, line) in enumerate(strlist):
        for word in line.split():
            if word in inverseIndex:
                inverseIndex[word].add(docid)
            else:
                inverseIndex[word] = { docid }

    return inverseIndex

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    docIds = set()
    for q in query:
        if q in inverseIndex:
            docIds = docIds | inverseIndex[q]
    return docIds

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    docIds = set()
    for q in query:
        if q in inverseIndex:
            if not docIds:
                docIds = inverseIndex[q]
            else:
                docIds = docIds & inverseIndex[q]
    return docIds


def main():
    print(movie_review("foo"))
    print(list2dict([1,2,3], [4,5,6]))
    print(listrange2dict([1,2,3,4,5,6]))
    inv = makeInverseIndex(list(open('stories_big.txt')))
    # print(inv)
    orS = orSearch(inv, ["declared", "layperson"])
    print(orS)
    andS = andSearch(inv, ["declared", "layperson"])
    print(andS)

if __name__ == "__main__":
    main()
