import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os
import cv2
import pickle

def load_data(path_root):
    datasets = []
    labels = []
    for idx, child in enumerate(os.listdir(path_root)):
        path_child = os.path.join(path_root, child)
        for dir_ in os.listdir(path_child):
            img_path = os.path.join(path_child, dir_)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (15, 15))
            datasets.append(img.flatten())
            labels.append(idx)
    return datasets, labels

def split_data(datasets, labels, test_size=0.8, random_state=32, shuffle=False):
    X_train, X_test, y_train, y_test = train_test_split(datasets, labels, test_size=test_size, random_state=random_state, shuffle=shuffle)
    return X_train, X_test, y_train, y_test

def train(X_train, y_train, model):
    model.fit(X_train, y_train)

def test(X_test, y_test, model):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='binary')
    recall = recall_score(y_test, y_pred, average='binary')
    f1 = f1_score(y_test, y_pred, average='binary')
    return accuracy, precision, recall, f1

if __name__ == "__main__":
    datasets, labels = load_data(path_root='clf-data')
    X_train, X_test, y_train, y_test = split_data(datasets, labels, shuffle=True, random_state=100, test_size=0.2)
    model = SVC()
    train(X_train, y_train, model)

    accuracy, precision, recall, f1 = test(X_test, y_test, model)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")

    with open('model/model.p', 'wb') as f:
        pickle.dump(model, f)
