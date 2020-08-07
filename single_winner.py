# COMP 202 A3
# Name: Ye Yuan
# Student ID: 260921269

from a3_helpers import *


def count_plurality(ballots):
    '''
    (list) -> dict
    return a dictionary which contains the candidates as keys and the number
    of votes as value.
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL','NDP'])
    {'LIBERAL': 3, 'NDP': 2}
    >>> count_plurality([])
    {}
    '''
    #create a new dictionary to store the value
    plurality={}
    #iterate all the elements in ballots
    for element in ballots:
        #if the element already in the dictionary, plus one to its value
        if element in plurality:
            plurality[element]+=1
        #if the element not in the dictionary, assign one to its value
        if element not in plurality:
            plurality[element]=1
    #return the result dictionary
    return plurality
    

def count_approval(ballots):
    '''
    (list) -> dict
    input a nested list as the ballots, and count the votes won by
    each candidate
    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval([['LIBERAL'], ['NDP'], ['GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 1, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval([])
    {}
    '''
    #revise the nested list to a normal list
    revised_ballots=flatten_lists(ballots)
    #use the created function to count the votes
    result=count_plurality(revised_ballots)
    #return the result
    return result

def count_rated(ballots):
    '''
    (dict) -> dict
    input a nested list include several dictionary, add all of them together
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}])
    {'LIBERAL': 5, 'NDP': 2}
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}, \
    {'NDP':4, 'GREEN':5}, {'LIBERAL': 5, 'NDP':2}])
    {'LIBERAL': 10, 'NDP': 12, 'GREEN': 10}
    '''
    #create a new dictionary to store the value
    my_dic={}
    #add each dictionary in the ballots to the created new dictionary
    for dic in ballots:
        my_dic=add_dicts(my_dic, dic)
    #return the result dictionary
    return my_dic

def count_first_choices(ballots):
    '''
    (list) -> dict
    input a nested list as the ballots, count all of the first candidate
    in each ballots. If the candidates don't win any first place votes,
    count its votes as zero.
    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']])
    {'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    >>> count_first_choices([['NDP', 'LIBERAL'], ['NDP', 'NDP'], \
    ['NDP', 'NDP']])
    {'NDP': 3, 'LIBERAL': 0}
    >>> count_first_choices([])
    {}
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> count_first_choices([g]*5 + [n]*3)
    {'GREEN1': 5, 'NDP1': 3, 'GREEN2': 0, 'GREEN3': 0, 'NDP2': 0, 'NDP3': 0, 'BLOC1': 0}
    '''
    #create a new dictionary to store the value
    first_choices={}
    #iterate all the first element in the list
    for lists in ballots:
        if len(lists)!=0:
            #check if the first element is in the created new dictionary
            if lists[0] in first_choices:
                #plus one to its value
                first_choices[lists[0]]+=1
            #assign one to its value 
            if lists[0] not in first_choices:
                first_choices[lists[0]]=1
    #change the nested list to normal list
    revised_ballots=flatten_lists(ballots)
    #add the candidate which is not the first choice
    for element in revised_ballots:
        #assign zero to its value
        if element not in first_choices:
            first_choices[element]=0
    #return the result dictionary
    return first_choices

if __name__ == '__main__':
    doctest.testmod()
