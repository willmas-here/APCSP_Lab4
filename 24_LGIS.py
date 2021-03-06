## Problem 24 - LGIS (Longest Increasing Subsequence)
## Willma
## 1/5/2021

## http://rosalind.info/problems/lgis/

import resources
import copy

def LGIS(n, permutation):
    '''
    Input: length of permutation, permutation of pi \n
    Output: longest increasing subsequence, longest decreasing subsequence
    '''
    
    n = len(permutation)

    # LIS
    traces = [None] * n
    for i in reversed(range(0, n)):
        if i == n-1:
            traces[i] = [permutation[i]]
            continue
        
        longest_possibile_trace = 0
        longest_possibile_trace_length = 0
        # compare with all
        for j in range(i+1, n):
            if permutation[i] < permutation[j]:    #check if <= or <
                if len(traces[j]) > longest_possibile_trace_length:
                    longest_possibile_trace = j
                    longest_possibile_trace_length = len(traces[j])
        
        if longest_possibile_trace == 0:
            traces[i] = [permutation[i]]
            continue

        # print(i, longest_possibile_trace)
        traces[i] = copy.copy(traces[longest_possibile_trace])
        traces[i].insert(0, permutation[i])
    
    lis = []
    for trace in traces:
        if len(trace) > len(lis):
            lis = trace

    # LDS
    traces = [None] * n
    for i in range(0, n):
        if i == 0:
            traces[i] = [permutation[i]]
            continue
        
        longest_possibile_trace = 0
        longest_possibile_trace_length = 0
        # compare with all
        for j in range(0, i):
            if permutation[i] < permutation[j]:    #check if <= or <
                if len(traces[j]) > longest_possibile_trace_length:
                    longest_possibile_trace = j
                    longest_possibile_trace_length = len(traces[j])
        if longest_possibile_trace == 0:
            traces[i] = [permutation[i]]
            continue

        traces[i] = copy.copy(traces[longest_possibile_trace])
        traces[i].append(permutation[i])

    lds = []
    for trace in traces:
        if len(trace) > len(lds):
            lds = trace
    
    output_path = 'outputs/lgis.txt'
    output_list = [resources.list_to_str(i) for i in [lis, lds]]
    resources.write_file(output_path, output_list)



if __name__ == "__main__":
    file_path = 'datasets/rosalind_lgis.txt'
    n, permutation = resources.read_file(file_path).strip('\n').split('\n')
    permutation = permutation.split()
    permutation = [int(i) for i in permutation]
    LGIS(n, permutation)
    

# old code
def old():
    # increasing
    increasing_possibilities = [permutation[0]]
    for num in permutation:
        for possibility in copy.copy(increasing_possibilities):
            # append num to possibility and check if it works
            # if it does, create a new possiblity with that list
            possible = True
            temp = list(copy.copy(possibility))
            temp.append(num)
            for i in range(len(temp) - 1):
                if temp[i] > temp[i+1]:
                    possible = False
                    break
            
            if possible:
                previous_possibilities = copy.copy(increasing_possibilities)
                increasing_possibilities.append(temp)

                # if there is another possibility of same length with lower/higher last number, remove higher possibility
                for possibility in previous_possibilities:
                    possibility = list(possibility)
                    print(possibility,temp)

                    if len(possibility) != len(temp):
                        continue
                    
                    temp1 = list(possibility).pop()
                    temp2 = temp.pop()

                    if temp1 == temp2:
                        if int(possibility[len(possibility) - 1]) > int(temp[len(temp) - 1]):
                            increasing_possibilities.remove(possibility)
                        else:
                            increasing_possibilities.remove(temp)
                            
        
        for possibility in increasing_possibilities:
            if len(possibility) != 1:
                continue
            
            if int(possibility[0]) > int(num):
                increasing_possibilities.remove(possibility)
                increasing_possibilities.append([num])
        
        print(increasing_possibilities)
    
    # find longest possibility
    increasing_longest = []
    increasing_length = 0
    for possibility in increasing_possibilities:
        if len(possibility) > increasing_length:
            increasing_longest = possibility
            increasing_length = len(possibility)
    
    # decreasing
    decreasing_possibilities = []
    for num in permutation:
        for possibility in copy.copy(decreasing_possibilities):
            # append num to possibility and check if it works
            # if it does, create a new possiblity with that list
            possible = True
            temp = copy.copy(possibility)
            temp.append(num)
            for i in range(len(temp) - 1):
                if temp[i] < temp[i+1]:
                    possible = False
                    break
            
            if possible:
                decreasing_possibilities.append(temp)
        
        decreasing_possibilities.append([num])
    
    # find longest possibility
    decreasing_longest = []
    decreasing_length = 0
    for possibility in decreasing_possibilities:
        if len(possibility) > decreasing_length:
            decreasing_longest = possibility
            decreasing_length = len(possibility)
    
    increasing_str = resources.list_to_str(increasing_longest)
    decreasing_str = resources.list_to_str(decreasing_longest)

    output_path = 'outputs/lgis.txt'
    resources.write_file(output_path, [increasing_str, decreasing_str])