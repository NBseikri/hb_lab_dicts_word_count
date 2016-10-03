test_dict = {}
# line_list = []

# for line in new_file:
#     line = line.rstrip()
#     line_list = line.split()
#     for word in line_list:
#         test_dict[word] = test_dict.get(word, 0) +1
#         print word, test_dict[word]

# # funct_1(file_path)
#     # open and clean

def clean_file(path):
    new_file = open('test.txt')
    for line in new_file:
        line = line.rstrip()
        line_list = line.split()


print clean_file('test.txt')

# funct_2(list_of words)
    # makes dictionary
def mk_dict(line_list):
    clean_file('test.txt')
    # print path
    for word in line_list:
        test_dict[word] = test_dict.get(word, 0) +1
    return test_dict


print mk_dict('line_list')
# mk_dict('test.txt')
    #     if word in test_dict:
    #         test_dict[word] += 1
    #     else:
    #         test_dict[word] = 1
    # return test_dict
    
# prints out dict
# def print_dict(test_dict):
#     return word, test_dict[word]

# print clean_file('test.txt')
# print mk_dict()
# print print_dict('test_dict')