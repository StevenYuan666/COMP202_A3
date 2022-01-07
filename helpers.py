# COMP 202 A3 Part 1
# Name:Ye Yuan
# Student ID:260921269

import doctest
import random

def flatten_lists(nested):
    '''
    (list) -> list
    input a nested list and return a new list which
    replaces any lists inside the nested list with their values.
    >>> flatten_lists([[0], [1, 2], 3])
    [0, 1, 2, 3]
    >>> flatten_lists([[0, 1, 2, 3, 4], [1], [3]])
    [0, 1, 2, 3, 4, 1, 3]
    '''
    #create a new empty list to store the value
    my_list=[]
    #iterate every lists inside the nested list
    for lists in nested:
        #check if the 'lists' is a list or not
        if(type(lists)==list):
            #add every element inside the list to the created empty list
            for element in lists:
                my_list.append(element)
        #add the single value otherwise
        else:
            my_list.append(lists)
    #return the result list
    return my_list

def flatten_dict(d):
    '''
    (dict) -> list
    input a dictionary with all values are integers, and return a list
    the keys of the dictionary, repeated v many times, where v is the
    value associated with the key in the dictionary.
    >>> flatten_dict({'LIBERAL': 5, 'NDP':2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    >>> flatten_dict({'NBA': 3, 'NFL':6})
    ['NBA', 'NBA', 'NBA', 'NFL', 'NFL', 'NFL', 'NFL', 'NFL', 'NFL']
    '''
    #check if all values in the dictionary is non-negative
    for key in d:
        if(d[key]<0):
            return False
    #create an empty list to store the value
    my_list=[]
    #for every key in the dictionary
    for key in d:
        #repeat adding the key to the created empty list for d[key] times
        for i in range(d[key]):
            my_list.append(key)
    #return the result list
    return my_list

def add_dicts(d1, d2):
    '''
    (dict) -> dict
    add two dictionaries, if keys occur in both the two dictionaries,
    add their values.
    >>> add_dicts({'a':5, 'b':2, 'd':-1}, {'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    >>> add_dicts({'a':7, 'b':1, 'c':5}, {'a':5, 'b':2, 'd':-1})
    {'a': 12, 'b': 3, 'c': 5, 'd': -1}
    '''
    #create a new empty dictionary to store the value
    my_dict={}
    #iterate the items in d1
    for keys in d1:
        #check if there is same key in d2 and add their values
        if(keys in d2):
            my_dict[keys]=d1[keys]+d2[keys]
        #otherwise only add the value in d1
        else:
            my_dict[keys]=d1[keys]
    #iterate the items in d2
    for keys in d2:
        #check if there is any key not in d1; add them to the result dictionary
        if(keys not in my_dict):
            my_dict[keys]=d2[keys]
    # return the result dictionary
    return my_dict

def get_all_candidates(ballots):
    '''
    (list) -> list
    input a list (a list of strings, a list of lists,
    or a list of dictionaries. Or a mix of all three.)
    return a new list which contains all unique strings
    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, \
    {'NDP':2, 'LIBERAL':4}, ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates([{'NBA':13, 'NFL':666},\
    ['666' ,'777'], 'GREEN', 'NDP'])
    ['NBA', 'NFL', '666', '777', 'GREEN', 'NDP']
    '''
    #create a new empty list to store the values
    my_list=[]
    #iterate every elements in the input list
    for elements in ballots:
        #check if the element is a list or not
        if(type(elements) != str):
            #iterate everything in the elements
            for members in elements:
                #check if the members is in my_list or not
                if members not in my_list:
                    my_list.append(members)
        #if elements is a string
        else:
            #check if the string is in my_list or not 
            if elements not in my_list:
                my_list.append(elements)
    #return the result list
    return my_list
                


###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''
    input a dictionary with last four functions' formats.
    evaluate the function on the dictionary’s values.
    return the key of the dictionary corresponding to that value.
    break ties randomly.
    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4} 
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    >>> another_result= {'LIBERAL':2, 'NDP':6, 'CPC':6, 'GREEN':4}
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    >>> result={'GREEN1': 5, 'NDP1': 3, 'GREEN2': 0, 'GREEN3': 0, 'NDP2': 0, 'NDP3': 0, 'BLOC1': 0}
    >>> get_candidate_by_place(result, max)
    'GREEN1'
    '''
    #create a new empty list
    value_list=[]
    #store all the values in the input dict to the created list
    for key in result:
        value_list.append(result[key])
    #find the value evaluated by the input function
    important_value=func(value_list)
    #create a new empty list
    key_list=[]
    #store all the keys in the input dict which has the same value as the
    #evaluation of the input function
    for key in result:
        if(result[key]==important_value):
            key_list.append(key)
    #randomly choose a key from the key_list and return it
    return random.choice(key_list)

def get_winner(result):
    '''
    input a dictionary with same format as above
    return the key with the greatest value.
    If there are ties, break them randomly.
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> random.seed(1)
    >>> get_winner({'NDP': 2, 'GREEN': 2, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> random.seed(0)
    >>> get_winner({'NDP': 2, 'GREEN': 2, 'LIBERAL': 0, 'BLOC': 2})
    'GREEN'
    '''
    #if the input result is empty, there is no winner
    if len(result)==0:
        return None
    #use the created function to get the greatest value
    return get_candidate_by_place(result, max)

def last_place(result, seed = None):
    '''
    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4} 
    >>> random.seed(0)
    >>> last_place(result)
    'GREEN'
    >>> random.seed(1)
    >>> last_place(result)
    'LIBERAL'
    >>> another_result = {'LIBERAL':4, 'NDP':1, 'CPC':3, 'GREEN':2}
    >>> last_place(another_result)
    'NDP'
    '''
    #if the input result is empty, there is no last place candidate
    if len(result)==0:
        return None
    #use the created function to get the smallest value
    return get_candidate_by_place(result, min)

###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
