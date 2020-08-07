# COMP 202 A3
# Name:Ye Yuan
# Student ID:260921269

from instant_run_off import *

################################################################################

def irv_to_stv_ballot(ballots, num_winners):
    '''
    (list,int) -> list
    input a list and a number, return a new list which numbers them from 0
    to the input number minus one.
    >>> irv_to_stv_ballot([['NDP', 'CPC'], ['GREEN']], 3)
    [['NDP0', 'NDP1', 'NDP2', 'CPC0', 'CPC1', 'CPC2'], ['GREEN0', 'GREEN1', 'GREEN2']]
    '''
    #create a new list
    result=[]
    #iterate every list in ballots
    for lists in ballots:
        #create a temporary list to store the value
        temp=[]
        #iterate all candidates in a list
        for candidate in lists:
            #iterate all numbers from zero to input number
            for i in range(num_winners):
                #add it to the temporary list
                temp.append(candidate+str(i))
        #add the temporary list to the result list
        result.append(temp)
    #return the final result
    return result
        

################################################################################


def eliminate_n_ballots_for(ballots, to_eliminate, n):
    '''(lst, str) -> lst
    Remove n of the ballots in ballots where the first choice is for the candidate to_eliminate.

    Provided to students. Do not edit.

    >>> ballots = [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 2)
    [['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3', 'GREEN1'], 5)
    [['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> b = [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    >>> eliminate_n_ballots_for(b, ['GREEN1'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    '''
    quota = n
    new_ballots = []
    elims = 0
    for i,b in enumerate(ballots):
        if (elims >= quota) or  (len(b) > 0 and b[0] not in to_eliminate):
            new_ballots.append(b)
        else:
            elims += 1
    return new_ballots



def stv_vote_results(ballots, num_winners):
    '''(lst of list, int) -> dict

    From the ballots, elect num_winners many candidates using Single-Transferable Vote
    with Droop Quota. Return how many votes each candidate has at the end of all transfers.
    
    Provided to students. Do not edit.

    >>> random.seed(1) # make the random tie-break consistent
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 2, 'NDP3': 0}
    >>> random.seed(0)
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 0, 'NDP3': 0}
    >>> green = ['GREEN', 'NDP', 'BLOC', 'LIBERAL', 'CPC']
    >>> ndp = ['NDP', 'GREEN', 'BLOC', 'LIBERAL', 'CPC']
    >>> liberal = ['LIBERAL', 'CPC', 'GREEN', 'NDP', 'BLOC']
    >>> cpc = ['CPC', 'NDP', 'LIBERAL', 'BLOC', 'GREEN']
    >>> bloc = ['BLOC', 'NDP', 'GREEN', 'CPC', 'LIBERAL']
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 2))
    {'BLOC': 32, 'CPC': 34, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 34}
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 3))
    {'BLOC': 26, 'CPC': 26, 'GREEN': 0, 'LIBERAL': 22, 'NDP': 26}
    >>> g = ['GREEN', 'NDP', 'BLOC']
    >>> n = ['NDP', 'GREEN', 'BLOC']
    '''
    quota = votes_needed_to_win(ballots, num_winners)

    to_eliminate = []
    result = {}
    final_result = {}

    for i in range(num_winners):
        # start off with quasi-IRV
        result = count_first_choices(ballots)
        
        while (not has_votes_needed(result, quota)) and len(result) > 0:
            to_eliminate.append( last_place(result) ) 
            ballots = eliminate_candidate(ballots, to_eliminate)
            result = count_first_choices(ballots)

        # but now with the winner, reallocate ballots above quota and keep going
        winner = get_winner(result)
        if winner:
            final_result[winner] = quota # winner only needs quota many votes
            ballots = eliminate_n_ballots_for(ballots, final_result.keys(), quota)
            ballots = eliminate_candidate(ballots, final_result.keys())
            result = count_first_choices(ballots)

    # remember the candidates we eliminated, their count should be 0
    for candidate in to_eliminate:
        final_result[candidate] = 0
    final_result.update(result)
    return final_result


################################################################################


def count_stv(ballots, num_winners):
    '''
    (dict) -> dict
    count the result evaluated by the above function, for example, bot Green0
    and Green1 will be counted as Green.
    >>> random.seed(1) # make the random tie-break consistent
    >>> g = ['GREEN', 'NDP', 'BLOC']
    >>> n = ['NDP', 'GREEN', 'BLOC']
    >>> pr_dict(count_stv([g]*5 + [n]*3, 4))
    {'BLOC': 0, 'GREEN': 3, 'NDP': 1}
    '''
    #create a new empty list
    result={}
    #get all candidates' name
    all_candidate=get_all_candidates(ballots)
    #initialize the created result dict with zero to each candidate
    for candidate in all_candidate:
        result[candidate]=0
    #transfer the input ballots to stv form
    ballots=irv_to_stv_ballot(ballots, num_winners)
    #calculate the quota
    quota = votes_needed_to_win(ballots, num_winners)
    #calculate the stv result
    stv_result=stv_vote_results(ballots, num_winners)
    #iterate the candidate in stv result, find the value equal to quota
    for key in stv_result:
        if stv_result[key]==quota:
            result[key[:len(key)-1]]+=1
    #return the final result
    return result


################################################################################


def count_SL(results, num_winners):
    '''
    (list) -> dict
    input a result of plurality, and find the result of Sainte-Lagu ̈e Method
    >>> count_SL([['A']*100000,['B']*80000,['C']*30000,['D']*20000], 8)
    {'A': 3, 'B': 3, 'C': 1, 'D': 1}
    '''
    #transfer the nested list to normal list
    results=flatten_lists(results)
    #calculate the plurality results
    results=count_plurality(results)
    #create a new empty dict
    quotient_result={}
    #initialize the created dict with the inital value of plurality results
    for party in results:
        quotient_result[party]=results[party]
    #created a new empty dict
    party_seat={}
    #initialize the party seat dict with zero
    for party in results:
        party_seat[party]=0
    #create a new variable to count how many seats have been allocated
    seats_allocated=0
    #iterate the loop to find the winner of each round until find enough seats
    while(seats_allocated<num_winners):
        winner=get_winner(quotient_result)
        party_seat[winner]+=1
        quotient=results[winner]/((2*party_seat[winner])+1)
        quotient_result[winner]=quotient
        seats_allocated+=1
    #return the final result
    return party_seat

################################################################################


if __name__ == '__main__':
    doctest.testmod()
