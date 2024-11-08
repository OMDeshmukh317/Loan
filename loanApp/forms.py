from django import forms

class LoanForm(forms.Form):
    person_age = forms.IntegerField(label='Age', required=True)
    person_gender = forms.ChoiceField(label='Gender', choices=[(1, 'Male'), (0, 'Female')], required=True)
    person_education = forms.ChoiceField(
        label='Education Level',
        choices=[(1, 'Bachelor'), (0, 'Associate'), (3, 'High School'), (4, 'Master'), (2, 'Doctorate')],
        required=True
    )
    person_income = forms.DecimalField(label='Annual Income', max_digits=12, decimal_places=2, required=True)
    person_emp_exp = forms.IntegerField(label='Employment Experience (Years)', required=True)
    person_home_ownership = forms.ChoiceField(
        label='Home Ownership',
        choices=[(3, 'Rent'), (0, 'Mortgage'), (2, 'Own'), (1, 'Other')],
        required=True
    )
    loan_amnt = forms.DecimalField(label='Loan Amount', max_digits=10, decimal_places=2, required=True)
    loan_intent = forms.ChoiceField(
        label='Loan Intent',
        choices=[(1, 'Education'), (3, 'Medical'), (5, 'Venture'), (4, 'Personal'), 
                 (0, 'Debt Consolidation'), (2, 'Home Improvement')],
        required=True
    )
    loan_int_rate = forms.DecimalField(label='Interest Rate', max_digits=5, decimal_places=2, required=True)
    loan_percent_income = forms.DecimalField(label='Loan Percent of Income', max_digits=5, decimal_places=2, required=True)
    cb_person_cred_hist_length = forms.DecimalField(label='Credit History Length (Years)', max_digits=5, decimal_places=2, required=True)
    credit_score = forms.IntegerField(label='Credit Score', required=True)
    previous_loan_defaults_on_file = forms.ChoiceField(
        label='Previous Loan Defaults',
        choices=[(1, 'Yes'), (0, 'No')],
        required=True
    )
