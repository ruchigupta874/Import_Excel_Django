from django.shortcuts import render
from django.urls import reverse_lazy
from .models import employee
from .forms import employeeForm,allupdate
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import HttpResponse
from django import forms
import openpyxl

class EmployeeListView(ListView):
    model = employee
    paginate_by = 10
    context_object_name = 'employee'
    template_name = 'employee_list.html'
    queryset = employee.objects.all()

class EmployeeCreateView(CreateView):
    model = employee
    fields = '__all__'
    template_name = 'employee_create.html'

class EmployeeUpdateView(UpdateView):
    model = employee
    fields = '__all__'
    template_name = 'employee_create.html'

class EmployeeDeleteView(DeleteView):
    model = employee
    template_name = 'delete.html'
    success_url = reverse_lazy('emp_list')

def filter(request):
    global result
    result = ''
    form = employeeForm()
    if request.method == 'POST':
        form = employeeForm(request.POST)

        if form.is_valid():
            Name=form.cleaned_data['name']
            Company = form.cleaned_data['company']
            Salary = form.cleaned_data['salary']

            if Name and Company and Salary:
                result = employee.objects.filter(name=Name, company=Company, salary=Salary)
            elif not Name and not Company and not Salary:
                print("Expects atleast one field to filter!")

            elif not Name and not Company:
                result = employee.objects.filter(salary=Salary)

            elif not Name and not Salary:
                result = employee.objects.filter(company=Company)

            elif not Company and not Salary:
                result = employee.objects.filter(name=Name)

            elif not Name:
                result = employee.objects.filter(company=Company, salary=Salary)

            elif not Salary:
                result = employee.objects.filter(name=Name, company=Company)

            elif not Company:
                result = employee.objects.filter(name=Name, salary=Salary)
            else:
                print("Sorry we didn't understand your query!")

    args = {'insert_me': form,'display': result}
    return render(request, 'filter_page.html', args)

def update(request):
    global column_to_update
    global new_value
    output=''
    global result
    column_to_update=''
    new_value=''
    form = allupdate()
    if request.method == 'POST':
        form = allupdate(request.POST)
        if form.is_valid():
            column_to_update = form.cleaned_data['column_to_update']
            new_value=form.cleaned_data['new_value']
        if result:
            for i in (result.values_list('id', flat=True)):
                employee.objects.filter(pk=i).update(**{column_to_update: new_value})
                output='Record Updated successfully !'
        else:
            output='No Records selected for update !'
        print('done successfully')
    args = {'insert_me': form ,'display':result,'text':output}
    return render(request, 'update_page.html', args)


def updated_record(request):
    global result
    global column_to_update
    global new_value
    after_update=''
    if column_to_update and new_value:
        after_update=employee.objects.filter(**{column_to_update: new_value})
        print(after_update)
    else:
        print('nothing selected')
    args={'updated_record':after_update}
    return render(request,'updated.html',args)

class UploadFileForm(forms.Form):
    file = forms.FileField()

def import_sheet(request):
    output=''
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=employee,
                mapdict=['name', 'company','salary'])
            #return HttpResponse("OK")
            output='FILE IMPORTED TO DB SUCCESSFULLY'
    else:
        form = UploadFileForm()
    args={'form': form,'result':output}
    return render(request,'import_excel.html',args)
