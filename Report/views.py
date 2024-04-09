from django.shortcuts import render, redirect
from .models import report
from .forms import ReportForm


def createReport(request):
    """the function creat a new report according to the request of the user and save it in the database"""
    if request.method == 'POST':
        form = ReportForm(request.POST)  # creat a form for the report
        if form.is_valid():
            new_report = form.save(commit=False)
            new_report.save()  # saving the new report in the database
            return redirect('Report:all_reports')  # refers to the page of all reports
    return render(request, 'Report/createReport.html', {'form': ReportForm()})


def all_reports(request):
    """the function presents all reports in the order of their arrival"""
    reports = report.objects.order_by('-date')
    return render(request, 'Report/all_reports.html', {'reports': reports})


def deleteReport(request, report_id):
    """the function delete a report according to the request of the user (volunteer only) and delete it
     from the database """
    Report = report.objects.get(pk=report_id)
    Report.delete()  # delete the report from the database
    return redirect('Report:all_reports')  # refers to the page of all reports
