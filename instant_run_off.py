# COMP 202 A3
# Name:Ye Yuan
# ID:260921269

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    (list,int) -> int
    input a list of ballots and the number of winners, return the votes
    needed to win
    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4},\
    {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    '''
    #get the number of total votes in the ballots
    number_of_votes=len(ballots)
    #calculate the number of the votes needed to win
    votes_to_win=int((number_of_votes/(num_winners+1))+1)
    #return the number of the votes
    return votes_to_win
    

def has_votes_needed(result, votes_needed):
    '''
    (dict,int) -> boolean
    input a votes result dictionary and the number of votes needed to win
    return if the winner in the result has more votes than votes needed to win
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    '''
    #if the input result is empty, return False
    if len(result)==0:
        return False
    #find who has the highest votes in the dictionary
    winner_name=get_winner(result)
    #check his or her votes
    votes=result[winner_name]
    #return whether the votes he or she got is higher than the votes needed
    return votes>=votes_needed

################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    (list,list) -> list
    input a list with ballots and a list with elements to be eliminated
    return a new list after the elimination
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
    ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    '''
    #create a new list to store the value
    result=[]
    #iterate every ballot in the list
    for lists in ballots:
        #create a new temporary list to store the value
        temp=[]
        #iterate the candidates in each ballot
        for candidates in lists:
            #if the candidate's name is not in the eliminate list
            if(candidates not in to_eliminate):
                #add it to the temporary list
                temp.append(candidates)
        #add the temporary list to the result list
        result.append(temp)
    #return the result list
    return result
            

################################################################################
def count_irv(ballots):
    '''
    (list) -> dict
    >>> count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], \
    ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'],['BLOC', 'CPC'], \
    ['LIBERAL', 'GREEN'], ['NDP']])
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    '''
    #initialize the condition as False
    condition= False
    #calculate the votes needed to win 
    votes_needed=votes_needed_to_win(ballots, 1)
    #find the irv result
    result=count_first_choices(ballots)
    #iterate the calculation unitl find the candidate who has the majority
    while(not condition):
        vote=count_first_choices(ballots)
        last=last_place(vote)
        ballots=eliminate_candidate(ballots, last)
        condition=has_votes_needed(vote, votes_needed)
    #store the value after calculation, and assign zero to other canidates
    for key in result:
        if key in vote:
            result[key]=vote[key]
        else:
            result[key]=0
    #sort the result dictionary as increasing order
    final={}
    keys=[]
    for key in result:
        keys.append(key)
    keys.sort()
    #store in the final result
    for key in keys:
        final[key]=result[key]
    #return the final result
    return final
################################################################################

if __name__ == '__main__':
    doctest.testmod()
