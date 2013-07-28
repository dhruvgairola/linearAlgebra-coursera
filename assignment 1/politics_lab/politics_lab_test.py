import sys
import politics_lab

def main():
    full_dict = politics_lab.create_voting_dict()
    voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
    print(politics_lab.policy_compare('Fox-Epstein','Ravella', voting_dict))
    vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
    print(politics_lab.most_similar('Klein', vd))
    print(politics_lab.least_similar('Klein', vd))
    print(politics_lab.most_similar('Chafee', full_dict))
    print(politics_lab.least_similar('Santorum', full_dict))
    vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
    print(politics_lab.find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd))

    voting_data = list(open("voting_record_dump109.txt"))

    democrat_list = []

    most_avg = 0.0
    most_average_Democrat = ''

    for vote_entry in voting_data:
        v = vote_entry.split()
        if v[1] == 'D':
            democrat_list.append(v[0])

    for key, val in full_dict.items():
        avg = politics_lab.find_average_similarity(key, set(democrat_list), full_dict)
        if most_avg < avg:
            most_avg = avg
            most_average_Democrat = key

    print(most_average_Democrat)

    voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
    print(politics_lab.find_average_record({'Fox-Epstein','Ravella'}, voting_dict))
    print(politics_lab.find_average_record(democrat_list, full_dict))

    voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
    print(politics_lab.bitter_rivals(voting_dict))

if __name__ == "__main__":
    main()