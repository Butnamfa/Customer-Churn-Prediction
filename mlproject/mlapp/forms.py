from django import forms

class PredictionForm(forms.Form):
    age = forms.FloatField(
        label='Age',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    gender = forms.ChoiceField(
        label='Gender',
        choices=[(0, 'ชาย'), (1, 'หญิง')],  # บังคับให้ผู้ใช้เลือก ชาย (0) หรือ หญิง (1)
        widget=forms.Select(attrs={'class': 'form-control'})
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
        choices=[(0, 'Basic'), (1, 'Standard'), (2, 'Premium')],  # บังคับให้เลือก Subscription Type
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    contract_length = forms.ChoiceField(
        label='Contract Length',
        choices=[(0, 'Monthly'), (1, 'Quarterly'), (2, 'Annual')],  # บังคับให้เลือก Contract Length
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    total_spend = forms.FloatField(
        label='Total Spend',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    last_interaction = forms.FloatField(
        label='Last Interaction',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
