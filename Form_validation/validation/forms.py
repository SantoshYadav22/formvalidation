from django import forms

#create your forms here

class FormClass(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Email=forms.EmailField()
    Place=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100)
    ReEnterPassword=forms.CharField(max_length=100)

    def clean(self) :
        cleaned_data=super().clean()
        valpwd=cleaned_data['Password']
        valpwd2=cleaned_data['ReEnterPassword']
        

        if valpwd != valpwd2:
            print('password error')
            raise forms.ValidationError('password not match')

            # else:
            #     print('password match')
            #     wrong='right password'
            #     return render (request,'base.html',{'nm':name,'wrg':wrong})    

    