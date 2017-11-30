"""
Preprocess Data
"""



def initial_preprocess(file_name):
    
    row_list = []

    with open(file_name, 'r') as train:
        for line in train:
            vals = [x for x in line.split('\t') if x != '_' and x != '_\n']
            if (len(vals) > 1):
                #print vals
                row_list.append(vals)
                #print vals

    print len(row_list)
    return row_list


def tagging_preprocess(train_list):
    with open('tagging_train.txt', 'w') as f:
        for row in train_list:
            f.write(row[1] + '\t' + row[2] + '-' + row[3] + '\n')

def tagging_preprocess_dev(dev_list):
    with open('tagging_dev.txt', 'w') as f:
        for row in dev_list:
            f.write(row[1] + '\t' + row[2] + '-' + row[3] + '\n')

    

def main():
    #train_list = initial_preprocess('en-universal-train.conll')
    dev_list = initial_preprocess('en-universal-dev.conll')

    #tagging_preprocess(train_list)
    tagging_preprocess_dev(dev_list)




if __name__ == "__main__":
    main()
