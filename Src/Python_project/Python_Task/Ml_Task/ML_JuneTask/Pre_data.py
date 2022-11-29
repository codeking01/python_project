# author: code_king
# time: 2022/11/24 22:37 
# file: Pre_data.py
"""
还是5%异常来处理
前面阶段的输入和输出是否都是下一个阶段的输入’和‘前面阶段的输入是下一个阶段的输入’两种方式都尝试一下
"""
import os

import joblib
import pandas as pd
from numpy import unique
import numpy as np

from ML_JuneTask.DimensionalityReduction import DataDelete
from ML_JuneTask.NewPreDeal_Tools import Del_deletion_data, Deal_sorted_Ydata, get_final_useablecols, all_ydata, \
    delAndGetCols, get_merge_tabledata, deal_verify_ydata, get_former_Ydata, convert_to_num

# 这个pandas处理数据效果不太好 建议用numpy
thedata = pd.read_excel(io=r'data_original.xlsx', sheet_name='8000D数据标准化-建模用')
Preddata = pd.read_excel(io=r'data_original.xlsx', sheet_name='8000D数据标准化-预测用')
# 用来查看数据结果的excel对象
from openpyxl import load_workbook

filename = 'data_original.xlsx'
data = load_workbook(f'{filename}')
sheetnames = data.sheetnames
# create_sheet
if len(sheetnames) < 3:
    sheetnames.append('预测结果')
    data.create_sheet(sheetnames[2], len(sheetnames))
    # 赋值sheet
    # sheet=data[sheetnames[0]]
    # content=data.copy_worksheet(sheet)
    data.save(f'{filename}')
# 预测结果的excel表
table = data[sheetnames[2]]
sheetnames = data.sheetnames
table = data[sheetnames[2]]

# 获取数据表对象(建模和与预测的数据)
thedata = np.array(thedata)
Preddata = np.array(Preddata)


# 写入excel文件
def write_to_excel(start_index, table, current_column, content):
    # 标签
    for i in range(len(content)):
        table.cell(start_index, current_column).value = content[i]
        start_index += 1


def save_model(model, model_name, X_train, X_test, y_train, y_test):
    """
    :param model: 需要训练的模型
    :param X_train:
    :param X_test:
    :param y_train:
    :param y_test:
    :return:
    """
    if not os.path.exists(f"models/{model_name}"):
        os.makedirs(name=f"models/{model_name}", exist_ok=True)
    acc_dic = {}
    for i in range(11):
        model.fit(X_train, y_train.astype(float))
        # 训练集准确率
        model_train_acc = accuracy_score(y_train.astype(float), model.predict(X_train))
        # print('Rfc_train_acc准确率：', model_train_acc)
        # model_pred = Rfc.predict(X_test)
        # model_acc = accuracy_score(y_test.astype(float), model_pred)
        acc_dic.update({f"model[{i}]": model_train_acc})
        # 模型保存
        joblib.dump(model, f'models/{model_name}/model[{i}].pkl')
    for i in range(11, 101):
        # temp_keys 是键的按照值从小到打排序的列表 [model[1],model[5],...]
        temp_keys = sorted(acc_dic, reverse=True)
        model.fit(X_train, y_train.astype(float))
        # 训练集准确率
        model_train_acc = accuracy_score(y_train.astype(float), model.predict(X_train))
        # print('Rfc_train_acc准确率：', model_train_acc)
        # model_pred = Rfc.predict(X_test)
        # model_acc = accuracy_score(y_test.astype(float), model_pred)
        # 替换一个最小的模型
        for key_item_index in range(0, len(temp_keys)):
            if key_item_index != len(temp_keys) - 1:
                if acc_dic[f"{temp_keys[key_item_index]}"] < model_train_acc < acc_dic[
                    f"{temp_keys[key_item_index + 1]}"]:
                    acc_dic.update({f"{temp_keys[key_item_index]}": model_train_acc})
                    joblib.dump(model, f'models/{model_name}/{temp_keys[key_item_index]}.pkl')
            elif acc_dic[f"{temp_keys[key_item_index]}"] < model_train_acc:
                acc_dic.update({f"{temp_keys[key_item_index]}": model_train_acc})
                joblib.dump(model, f'models/{model_name}/{temp_keys[key_item_index]}.pkl')

    # model1 = joblib.load(filename="filename.pkl")


def get_pred_data(model_name, X_verify_data):
    """
    :param model_name: 模型名字
    :return: pred_data
    """
    # 预测数据
    all_models = os.listdir(f"models/{model_name}")
    model_pred_list = []
    for i in all_models:
        cursor_model = joblib.load(filename=f"models/{model_name}/{i}")
        model_pred_list.append(cursor_model.predict(X_verify_data))
    model_pred_list = np.array(model_pred_list)
    temp_pred_list = []
    # 循环遍历列
    for pred_list_index in range(0, model_pred_list.shape[1]):
        # 预测结果统一,那个数多就等于哪个
        zero_count = np.where(model_pred_list[:, pred_list_index] == 0)[0].shape[0]
        negative_count = np.where(model_pred_list[:, pred_list_index] == -1)[0].shape[0]
        positive_count = np.where(model_pred_list[:, pred_list_index] == 1)[0].shape[0]
        final_dic = {}
        final_dic.update({"0": zero_count})
        final_dic.update({"-1": negative_count})
        final_dic.update({"1": positive_count})
        # 排序，第一个数预测的最多
        final_result = -1
        if final_dic[f"{final_result}"] < final_dic["0"]:
            final_result = 0
        if final_dic[f"{final_result}"] < final_dic["1"]:
            final_result = 1
        temp_pred_list.append(final_result)
    pred_data = np.array(temp_pred_list)
    return pred_data


def get_train_test_acc(model, X_train, y_train, X_test, y_test):
    """
    :param model:
    :param X_train:
    :param y_train:
    :param X_test:
    :param y_test:
    :return: model_train_acc, model_acc
    """
    model_train_acc = accuracy_score(y_train.astype(float), model.predict(X_train))
    model_pred = model.predict(X_test)
    model_acc = accuracy_score(y_test.astype(float), model_pred)
    return model_train_acc, model_acc


if __name__ == '__main__':
    # 将表的内容 7个数据表 挨个处理
    # 获取源建模的X数据 传入的对象是获取的excel对象
    FormerTwo_data, FormerThree_data, FormerFour_data, FormerFive_data, FormerSix_data = get_merge_tabledata(
        excel_data=thedata)
    # 获取预测的X数据
    Verify_TABLE_TWO, Verify_TABLE_THREE, Verify_TABLE_FOUR, Verify_TABLE_FIVE, Verify_TABLE_SIX = get_merge_tabledata(
        excel_data=Preddata)
    all_former_data = [FormerTwo_data, FormerThree_data, FormerFour_data, FormerFive_data, FormerSix_data]
    all_verify_data = [Verify_TABLE_TWO, Verify_TABLE_THREE, Verify_TABLE_FOUR, Verify_TABLE_FIVE, Verify_TABLE_SIX]
    # 依次遍历
    iter_length = len(all_former_data)
    for i in range(iter_length):
        # 统一关键字
        the_Former_data, the_Verify_TABLE_data = convert_to_num(all_former_data[i], all_verify_data[i])
        # 删除缺失值过多的列，并保存del_cols
        # tempFormerTwo_data = delAndGetCols(FormerTwo_data)
        base_Xdata, del_cols = delAndGetCols(the_Former_data)
        # 用del_cols删除验证集X不需要的列
        Verify_Xdata = np.delete(the_Verify_TABLE_data, del_cols, axis=1)
        # 降维处理,这个地方只从训练集判断相关性，然后统一降维
        use_able_x_cols = DataDelete(base_Xdata, 0.80)
        base_Xdata = base_Xdata[:, use_able_x_cols]
        Verify_Xdata = Verify_Xdata[:, use_able_x_cols]
        # base_Xdata,del_cols
        # %%
        # 获取源建模的数据Y_data
        Original_TableTwoYdata, Original_TableThreeYdata, Original_TableFiveYdata, Original_TableSixYdata, Original_TableSevenYdata = get_former_Ydata(
            thedata)
        # 获取预测数据的Y_data
        Predict_TableTwoYdata, Predict_TableThreeYdata, Predict_TableFiveYdata, Predict_TableSixYdata, Predict_TableSevenYdata = get_former_Ydata(
            Preddata)
        all_original_Ydata = [Original_TableTwoYdata, Original_TableThreeYdata, Original_TableFiveYdata,
                              Original_TableSixYdata, Original_TableSevenYdata]
        all_predict_Ydata = [Predict_TableTwoYdata, Predict_TableThreeYdata, Predict_TableFiveYdata,
                             Predict_TableSixYdata, Predict_TableSevenYdata]
        # %%
        # 将Y取出来，然后取出缺失值过多的列
        # 获取可用的列
        Original_TableYdata, Predict_TableYdata = all_original_Ydata[i], all_predict_Ydata[i]
        final_cols = get_final_useablecols(Original_TableYdata, Predict_TableYdata)
        # final_cols
        # %%
        # 获取可以用的Y_data
        Original_YdataList, Pred_YdataList = all_ydata(final_cols, Original_TableYdata, Predict_TableYdata)

        # %%
        # 挨个遍历，取出有用的Y_data
        # 传入起始的坐标 24,67,108,145,179
        # 传入起始的坐标新表 22,31,50,71,88
        colum_list = [22, 31, 50, 71, 88]
        the_column = colum_list[i]
        start = 0
        for index in final_cols:
            # 建模的Y_data
            Modeling_Y_data = Original_YdataList[start]
            # 预测的Y_data
            Pred_Y_data = Pred_YdataList[start]
            start += 1
            # 处理建模的X_data,Y_data
            temp_OriginalXdata = np.column_stack((base_Xdata, Modeling_Y_data))
            # 删除缺失的行
            temp_OriginalXdata = Del_deletion_data(temp_OriginalXdata, 0)
            X_data = temp_OriginalXdata[:, :-1]
            Y_data = temp_OriginalXdata[:, -1]
            # 处理验证的X_data,Y_data
            # 合并数据
            temp_verifydata = np.column_stack((Verify_Xdata, Pred_Y_data))
            # 删除缺失的行
            temp_verifydata = Del_deletion_data(temp_verifydata, 0)
            # 获取预测数据的X_data，Y_data
            X_verify_data = temp_verifydata[:, :-1]
            Y_verify_data = temp_verifydata[:, -1]
            print(list(set(np.where(np.isnan(temp_OriginalXdata.astype(float)) == True)[0].tolist())),
                  list(set(np.where(np.isnan(temp_verifydata.astype(float)) == True)[0].tolist())))
            # 将建模Y_data分类(-1,0,1)，并且取出边界值
            Y_data, Y_data_boundsMin, Y_data_boundsMax = Deal_sorted_Ydata(Y_data)
            # 获取预测数据的Y_data Verify_Ydata = Pred_Y_data
            Verify_Ydata = deal_verify_ydata(Y_verify_data, Y_data_boundsMin, Y_data_boundsMax)
            # 查看是否替换成功
            print([unique(Y_data), Y_data_boundsMin, Y_data_boundsMax], np.unique(Verify_Ydata))
            # 切分训练数据和测试数据
            from sklearn.model_selection import train_test_split

            ## 30%测试数据，70%训练数据，stratify=y表示训练数据和测试数据具有相同的类别比例 修改为0.4
            X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.4, random_state=4,
                                                                stratify=Y_data)
            from sklearn.metrics import accuracy_score
            # 开始训练模型
            from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

            # 获取模型  随机森林
            Rfc = RandomForestClassifier()
            model_name = "Rfc"
            save_model(Rfc, model_name, X_train, X_test, y_train, y_test)
            # 随便取一个作为训练集的结果
            current_model = joblib.load(filename=f"models/{model_name}/model[0].pkl")
            Rfc_train_acc, Rfc_acc=get_train_test_acc(current_model, X_train, y_train, X_test, y_test)
            # Rfc.fit(X_train, y_train.astype(float))
            # # 训练集准确率
            # Rfc_train_acc = accuracy_score(y_train.astype(float), Rfc.predict(X_train))
            # print('Rfc_train_acc准确率：', Rfc_train_acc)
            # Rfc_pred = Rfc.predict(X_test)
            # Rfc_acc = accuracy_score(y_test.astype(float), Rfc_pred)
            # # 测试集准确率
            # print('Rfc_acc准确率:', Rfc_acc)

            # 梯度提升树
            Gbc = GradientBoostingClassifier()
            model_name = "Gbc"
            save_model(Gbc, model_name, X_train, X_test, y_train, y_test)
            current_model = joblib.load(filename=f"models/{model_name}/model[0].pkl")
            Gbc_train_acc, Gbc_acc = get_train_test_acc(current_model, X_train, y_train, X_test, y_test)
            # Gbc.fit(X_train, y_train.astype(float))
            # # 训练集准确率
            # Gbc_train_acc = accuracy_score(y_train.astype(float), Gbc.predict(X_train))
            # print('Gbc_train_acc准确率：', Gbc_train_acc)
            # # 测试集准确率
            # Gbc_pred = Gbc.predict(X_test)
            # Gbc_acc = accuracy_score(y_test.astype(float), Gbc_pred)
            # print('Gbc_acc准确率:', Gbc_acc)

            # 使用SVM模型
            from sklearn.svm import SVC

            Svc = SVC()
            model_name = "Svc"
            save_model(Svc, model_name, X_train, X_test, y_train, y_test)
            current_model = joblib.load(filename=f"models/{model_name}/model[0].pkl")
            Svc_train_acc, Svc_acc = get_train_test_acc(current_model, X_train, y_train, X_test, y_test)
            # Svc.fit(X_train, y_train.astype(float))
            # # 训练集准确率
            # Svc_train_acc = accuracy_score(y_train.astype(float), Svc.predict(X_train))
            # print('Svc_train_acc准确率：', Svc_train_acc)
            # # 测试集准确率
            # Svc_pred = Svc.predict(X_test)
            # Svc_acc = accuracy_score(y_test.astype(float), Svc_pred)
            # print('SVC准确率：', Svc_acc)

            # 使用DNN模型
            from sklearn.neural_network import MLPClassifier

            Dnn = MLPClassifier()
            model_name = "Dnn"
            save_model(Dnn, model_name, X_train, X_test, y_train, y_test)
            current_model = joblib.load(filename=f"models/{model_name}/model[0].pkl")
            Dnn_train_acc, Dnn_acc = get_train_test_acc(current_model, X_train, y_train, X_test, y_test)
            # Dnn.fit(X_train, y_train.astype(float))
            # # 训练集准确率
            # Dnn_train_acc = accuracy_score(y_train.astype(float), Dnn.predict(X_train))
            # print('Dnn_train_acc准确率：', Dnn_train_acc)
            # # 测试集准确率
            # Dnn_pred = Dnn.predict(X_test)
            # Dnn_acc = accuracy_score(y_test.astype(float), Dnn_pred)
            # print('DNN准确率：', Dnn_acc)

            # 使用卷积神经网络模型
            from sklearn.neural_network import MLPClassifier

            CNN = MLPClassifier()
            model_name = "CNN"
            save_model(CNN, model_name, X_train, X_test, y_train, y_test)
            current_model = joblib.load(filename=f"models/{model_name}/model[0].pkl")
            CNN_train_acc, CNN_acc = get_train_test_acc(current_model, X_train, y_train, X_test, y_test)

            # CNN.fit(X_train, y_train.astype(float))
            # # 训练集准确率
            # CNN_train_acc = accuracy_score(y_train.astype(float), CNN.predict(X_train))
            # print('CNN_train_acc准确率：', CNN_train_acc)
            # # 测试集准确率
            # CNN_pred = CNN.predict(X_test)
            # CNN_acc = accuracy_score(y_test.astype(float), CNN_pred)
            # print('CNN准确率：', CNN_acc)

            Rfc_pred = get_pred_data("Rfc", X_verify_data)
            Gbc_pred = get_pred_data("Gbc", X_verify_data)
            Svc_pred = get_pred_data("Svc", X_verify_data)
            Dnn_pred = get_pred_data("Dnn", X_verify_data)
            CNN_pred = get_pred_data("CNN", X_verify_data)

            # Gbc_pred = Gbc.predict(X_verify_data)
            # Svc_pred = Svc.predict(X_verify_data)
            # Dnn_pred = Dnn.predict(X_verify_data)
            # CNN_pred = CNN.predict(X_verify_data)
            # 计算准确率
            verify_y1 = accuracy_score(Y_verify_data.astype(float), Rfc_pred)
            verify_y2 = accuracy_score(Y_verify_data.astype(float), Gbc_pred)
            verify_y3 = accuracy_score(Y_verify_data.astype(float), Svc_pred)
            verify_y6 = accuracy_score(Y_verify_data.astype(float), Dnn_pred)
            verify_y7 = accuracy_score(Y_verify_data.astype(float), CNN_pred)

            # 计算准确率
            print('验证集Rfc_acc准确率:', verify_y1)
            print('验证集Gbc_acc准确率:', verify_y2)
            print('验证集SVC准确率：', verify_y3)
            print('验证集DNN准确率：', verify_y6)
            print('验证集CNN准确率：', verify_y7)

            #  标签 都加20
            write_to_excel(start_index=5, table=table, current_column=1,
                           content=["训练集", "训练集", "训练集", "训练集", "训练集"])
            # 将训练集写入到excel中
            write_to_excel(start_index=5, table=table, current_column=the_column + index,
                           content=[Rfc_train_acc, Gbc_train_acc, Svc_train_acc, Dnn_train_acc, CNN_train_acc])
            # table.cell(5, the_column + index).value = Rfc_train_acc
            # table.cell(6, the_column + index).value = Gbc_train_acc
            # table.cell(7, the_column + index).value = Svc_train_acc
            # table.cell(8, the_column + index).value = Dnn_train_acc
            # table.cell(9, the_column + index).value = CNN_train_acc

            # 将测试集写入到excel中
            write_to_excel(start_index=11, table=table, current_column=1,
                           content=["测试集", "测试集", "测试集", "测试集", "测试集"])
            write_to_excel(start_index=11, table=table, current_column=the_column + index,
                           content=[Rfc_acc, Gbc_acc, Svc_acc, Dnn_acc, CNN_acc])
            # table.cell(11, the_column + index).value = Rfc_acc
            # table.cell(12, the_column + index).value = Gbc_acc
            # table.cell(13, the_column + index).value = Svc_acc
            # table.cell(14, the_column + index).value = Dnn_acc
            # table.cell(15, the_column + index).value = CNN_acc

            # 将预测数据写入到excel中
            write_to_excel(start_index=17, table=table, current_column=1,
                           content=["验证集", "验证集", "验证集", "验证集", "验证集"])
            write_to_excel(start_index=17, table=table, current_column=the_column + index,
                           content=[verify_y1, verify_y2, verify_y3, verify_y6, verify_y7])
            # table.cell(17, the_column + index).value = verify_y1
            # table.cell(18, the_column + index).value = verify_y2
            # table.cell(19, the_column + index).value = verify_y3
            # table.cell(20, the_column + index).value = verify_y6
            # table.cell(21, the_column + index).value = verify_y7

            # 保存excel文件
            data.save(filename)
    print("运行结束！")
