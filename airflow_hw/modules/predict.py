# <YOUR_IMPORTS>

import json
import os
import sys

import dill
import pandas as pd

from datetime import datetime

# Путь к папке, которую нужно проверить
folder_path = r"~\data\models\\"
tests_path = r"~\data\test\\"
# predict_path = r"C:\Users\DIAS\Desktop\DS_lessons\ds-intro\33\airflow_hw\\"
path = os.path.expanduser(r'~\Desktop\DS_lessons\ds-intro\33\airflow_hw')
# Добавим путь к коду проекта в переменную окружения, чтобы он был доступен python-процессу
os.environ['PROJECT_PATH'] = path
# Добавим путь к коду проекта в $PATH, чтобы импортировать функции
sys.path.insert(0, path)

# Список файлов в папке
file_list = os.listdir(folder_path)
tests_list = os.listdir(tests_path)

MODEL_FILE = file_list[0]


def predict(MODEL_FILE, tests_list):
    # <YOUR_CODE>
    fold = folder_path + MODEL_FILE
    with open(fold, 'rb') as model:
        model = dill.load(model)

    predicts = []
    for test in tests_list:
        path = tests_path + test
        with open(path, 'r') as f:
            data = json.load(f)

        df = pd.DataFrame.from_dict(data, orient='index').T

        y = model.predict(df)
        predicts.append((data['id'], y[0]))

    return pd.DataFrame(predicts, columns=['car_id', 'prep']).to_csv(
        fr'{predict_path}\data\predictions\preds_{datetime.now().strftime("%Y%m%d%H%M")}.csv')


if __name__ == '__main__':
    predict(MODEL_FILE, tests_list)
