from django import forms
import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

class TestForm(forms.Form):
    file = forms.FileField(label="File Name", widget=forms.ClearableFileInput(attrs={'class': 'form-control'})) 
    weights = forms.CharField(label="Weights", widget=forms.TextInput(attrs={'placeholder': 'Weights', 'class': 'form-control'}))
    impacts = forms.CharField(label="Impacts", widget=forms.TextInput(attrs={'placeholder': 'Impacts', 'class': 'form-control'}))
    email = forms.EmailField(label="Email Id", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))

    def clean_file(self):
        file = self.cleaned_data.get("file")
        filename = file.name
        df = pd.read_csv('static/app/datasets/' + filename)
        self.column_length = df.shape[1] 
        if self.column_length <= 3:
            raise forms.ValidationError("Provide a dataset with more than 3 columns")
        for i in range(1, df.shape[1]):
            if(not is_numeric_dtype(df.iloc[:, i])):
                raise forms.ValidationError("The dataset should contain numeric values from 2nd to the last column")
        return file

    def clean_weights(self):
        weights = self.cleaned_data.get("weights")
        wts = weights.split(',')
        if len(wts) != self.column_length - 1:
            raise forms.ValidationError("{} weights must be provided".format(self.column_length - 1))
        if wts[0] == '' or wts[-1] == '':
            raise forms.ValidationError("Provide comma separated numeric values")
        try:
            for value in wts:
                value = float(value)
        except ValueError:
            raise forms.ValidationError("Weights should be numeric")
        return weights

    def clean_impacts(self):
        impacts = self.cleaned_data.get("impacts")
        imp = np.array(impacts.split(','))
        if len(imp) != self.column_length - 1:
            raise forms.ValidationError("{} impacts must be provided".format(self.column_length - 1))
        index = 0
        for c in impacts:
            if (index % 2 == 0 and c not in '+-') or (index % 2 != 0 and c not in ',') or (impacts[-1] in ','):
                raise forms.ValidationError("Invalid format for impacts. Provide comma-separated '+' or '-' values")
            index += 1
        return impacts
       

