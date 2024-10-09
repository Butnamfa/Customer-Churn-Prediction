from django import forms

class PredictionForm(forms.Form):
    age = forms.FloatField(
        label='Age',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    gender = forms.ChoiceField(
       label='Gender',
       choices=[('', 'เลือกเพศ'), (0, 'ชาย'), (1, 'หญิง')],  # เพิ่มตัวเลือกที่ไม่มีค่าเริ่มต้น
       widget=forms.Select(attrs={'class': 'form-control'}),
       required=True  # บังคับให้เลือก
)

    tenure = forms.FloatField(
        label='Tenure',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    usage_frequency = forms.FloatField(
        label='Usage Frequency',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    support_calls = forms.FloatField(
        label='Support Calls',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    payment_delay = forms.FloatField(
        label='Payment Delay',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    subscription_type = forms.ChoiceField(
        label='Subscription Type',
        choices=[('', 'ประเภทสมาชิก'), (0, 'Basic'), (1, 'Standard'), (2, 'Premium')],  # เพิ่มตัวเลือกที่ไม่มีค่าเริ่มต้น
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True  # บังคับให้เลือก
    )
    contract_length = forms.ChoiceField(
        label='Contract Length',
        choices=[('', 'ระยะเวลาของสัญญา'), (0, 'Monthly'), (1, 'Quarterly'), (2, 'Annual')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    total_spend = forms.FloatField(
        label='Total Spend',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    last_interaction = forms.FloatField(
        label='Last Interaction',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
