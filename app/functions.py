import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

def handle_uploaded_file(f):  
    with open('static/app/datasets/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def topsis(weights, impacts, file):  
    with open('static/app/datasets/'+file, "r") as f:
        dataset = pd.read_csv(f)

    data = dataset.iloc[:, 1:]
    column_names = list(dataset.columns)
    column_names.extend(['Topsis Score', 'Rank'])
    row_names = dataset.iloc[:, 0].values

    arr = np.array(data)

    squared_arr = arr**2
    col_sums = np.sqrt(np.sum(squared_arr, axis=0))
    arr = arr / col_sums

    w = np.fromstring(weights, dtype=float, sep=",")
    arr = arr * w
 
    imp = np.array(impacts.split(','))
    ideal_best = []
    ideal_worst = []
    for col in range(arr.shape[1]):
        if imp[col] == '+':
            ideal_best.append(np.amax(arr[:, col]))
            ideal_worst.append(np.amin(arr[:, col]))
        else:
            ideal_best.append(np.amin(arr[:, col]))
            ideal_worst.append(np.amax(arr[:, col]))

    difference = arr - ideal_best
    squared_difference = difference**2
    sum_of_squared_difference = np.sum(squared_difference, axis=1)
    best_euclidean_distance = np.sqrt(sum_of_squared_difference)
    best_euclidean_distance = best_euclidean_distance.reshape(-1, 1)
    best_euclidean_distance

    difference = arr - ideal_worst
    squared_difference = difference**2
    sum_of_squared_difference = np.sum(squared_difference, axis=1)
    worst_euclidean_distance = np.sqrt(sum_of_squared_difference)
    worst_euclidean_distance = worst_euclidean_distance.reshape(-1, 1)
    worst_euclidean_distance

    p = worst_euclidean_distance / (best_euclidean_distance + worst_euclidean_distance)
    result = np.concatenate((data, p), axis=1)

    score = result[:, -1]
    sort_indices = np.argsort(score)
    ranks = np.empty(len(score))
    ranks[sort_indices] = np.arange(1, len(sort_indices) + 1)
    ranks = len(ranks) - ranks + 1
    result = np.concatenate((result, ranks.reshape(-1, 1)), axis=1)

    result = np.concatenate((row_names.reshape(-1, 1), result), axis=1)
    final_dataframe = pd.DataFrame(result, columns=column_names)
    final_dataframe['Rank'] = final_dataframe['Rank'].astype(int)

    final_dataframe.to_csv(r'static/app/datasets/output.csv', index=False)

def send_email(email):
    mail = EmailMessage(
        'Topsis Results', 'Hey there! Please find your TOPSIS results in the attachments', 'settings.EMAIL_HOST_USER', [email],
    )
    mail.attach_file('static/app/datasets/output.csv')
    mail.send()
    
