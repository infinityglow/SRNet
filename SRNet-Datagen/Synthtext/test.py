with open("./thai_5w_thrid_parity_predict_names.csv", 'r') as f:
    for line in f.readlines()[1:]:
        print(line.strip('\n').split(',')[-1])
