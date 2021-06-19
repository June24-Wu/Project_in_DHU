import pandas as pd

def read_data():
    data = pd.read_excel('est3.xls')
    test = data[data['Task'] <= 100].sort_values('Task')
    train = data[data['Task'] > 100].sort_values('Task')
    return train , test

def caculate_task_var(train = None):
    mode_list = []
    for i in train['Task'].drop_duplicates():
        task = train[train['Task'] == i]
        mode_list.append([i, task['Score'].mode()[0]])
    mode_list = pd.DataFrame(mode_list, columns=['Task', 'Mode'])
    result = pd.merge(left=train, right=mode_list, how='left',
                      left_on='Task', right_on='Task')
    result['Var'] = abs(result['Score'] - result['Mode']) / 5
    return result
def get_accuracy(result = None):
    print('Start get accuracy(Time consuming)')
    acc = {}
    # initialize the accuracy
    for i in train['Worker'].drop_duplicates():
        acc[i] = 0.5
    acc_list = []
    for row in result.iterrows():
        worker = int(row[1][0])
        if row[1][-1] == 0:
            acc[worker] = acc[worker] + 0.5 * (1 - acc[worker])
        else:
            acc[worker] = acc[worker] - abs(acc[worker] * row[1][-1])
    for key in acc.keys():
        acc_list.append([key, acc[key]])
    acc_list = pd.DataFrame(acc_list, columns=['Worker', 'Accuracy'])
    print('Got Accuracy')
    return acc_list

def testing(acc_list = None , test = None):
    test_df = pd.merge(left=test, right=acc_list, how='left',
                       left_on='Worker', right_on='Worker')
    truth_list = []
    for task in test_df['Task'].drop_duplicates():
        df = test_df[test_df['Task'] == task]
        df = df.sort_values('Accuracy', ascending=False)
        numerator, denominator = 0, 0
        for i in df.iloc[0:8].iterrows():
            numerator += i[1][2] * i[1][3]
            denominator += i[1][3]
        truth = numerator / denominator
        truth_list.append([task, truth])
    truth_list = pd.DataFrame(truth_list, columns=['Task', 'Truth'])
    return truth_list



if __name__ == "__main__":
    train , test = read_data()
    result = caculate_task_var(train=train)
    acc_list = get_accuracy(result=result)
    truth_list = testing(acc_list=acc_list,test=test)

    # Save
    truth_list.to_csv('Truth.csv')
    acc_list.to_csv('Accuracy.csv')
    print('Finished!!!!')

