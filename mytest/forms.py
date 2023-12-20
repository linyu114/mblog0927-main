from django import forms
#表單
class ContactForm(forms.Form): #繼承forms的Form
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')#輸入
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)#下拉式選單 OR 多選一
    user_school = forms.BooleanField(label='是否在學', required=False)#核取方塊
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)
