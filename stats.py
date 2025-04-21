def counterfunc(contents):
    return len(contents.split())

def character_counter(contents):
    count_dict = {}
    contents = contents.lower()
    for i in contents:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def final_list(count_dict):
    list_of_dicts = []
    for i, n in count_dict.items():
        list_of_dicts.append({i:n})
    list_of_dicts.sort(reverse=True, key=lambda i: list(i.values())[0])
    return list_of_dicts

