from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoanForm
import joblib

# Load the model from the savedModels directory
model=joblib.load('./savedModels/loan_voting_classifier_model1.pkl')

def predict(request):
    result = None
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Process form data
            person_age = form.cleaned_data['person_age']
            person_gender = form.cleaned_data['person_gender']
            person_education = form.cleaned_data['person_education']
            person_income = form.cleaned_data['person_income']
            person_emp_exp = form.cleaned_data['person_emp_exp']
            person_home_ownership = form.cleaned_data['person_home_ownership']
            loan_amnt = form.cleaned_data['loan_amnt']
            loan_intent = form.cleaned_data['loan_intent']
            loan_int_rate = form.cleaned_data['loan_int_rate']
            loan_percent_income = form.cleaned_data['loan_percent_income']
            cb_person_cred_hist_length = form.cleaned_data['cb_person_cred_hist_length']
            credit_score = form.cleaned_data['credit_score']
            previous_loan_defaults_on_file = form.cleaned_data['previous_loan_defaults_on_file']
            
            # Prepare input data for the model (convert to appropriate features)
            input_data = [[person_age, person_gender, person_education, person_income, person_emp_exp, 
                           person_home_ownership, loan_amnt, loan_intent, loan_int_rate, loan_percent_income, 
                           cb_person_cred_hist_length, credit_score, previous_loan_defaults_on_file]]
            
            # Predict loan approval status
            result = model.predict(input_data)[0]
            
    else:
        form = LoanForm()
    
    return render(request, 'loan_application.html', {'form': form, 'result': result})

def data_analysis(request):
    return render(request, 'data-analysis.html')

def about_project(request):
    return render(request, 'about_project.html')
