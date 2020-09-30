from django import forms

#[(i, str(i)) for i in range(x, y)] создаёт список с кортежами вроде этого [(x, 'x'), (x+1, 'x+1'), ... (y-2, 'y-2'), (y-1, 'y-1')]
#CHOICES = [(i, str(i)) for i in range(1, 31)]


class AddCartF(forms.Form):
    count = forms.IntegerField()