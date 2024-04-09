from django.shortcuts import render, redirect,  get_object_or_404
from .models import hostReq
from .forms import HostForm
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt
from .filters import host_filter
from django.http import HttpResponseForbidden


from django.contrib.auth.decorators import login_required, permission_required
from .decorators import user_is_host
from django.core.exceptions import PermissionDenied



@login_required
def create_host(request):
    # Print out the names of all the groups the user belongs to
    print([group.name for group in request.user.groups.all()])

    # Check if the user is part of the 'מארח' group or is a superuser
    if not request.user.groups.filter(name='מארח').exists() and not request.user.is_superuser:
        raise PermissionDenied  # or redirect to a different page

    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            host = form.save(commit=False)
            host.user = request.user
            host.save()
            return redirect('host:all_hosts')
    else:
        form = HostForm()
    return render(request, 'host/create_host.html', {'form': form})


def all_hosts(request):
    hosts = hostReq.objects.order_by('-date')
    my_host_filter = host_filter(request.GET, queryset=hosts)
    hosts = my_host_filter.qs
    return render(request, 'host/all_hosts.html', {'hosts': hosts, 'host_filter': my_host_filter})

def delete_host(request, host_id):
    host = get_object_or_404(hostReq, pk=host_id)
    if request.user != host.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    host.delete()
    return redirect('host:all_hosts')

def edit_host(request, host_id):
    host = get_object_or_404(hostReq, pk=host_id)
    if request.user != host.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = HostForm(request.POST, request.FILES, instance=host)
        if form.is_valid():
            form.save()
            return redirect('host:all_hosts')
    else:
        form = HostForm(instance=host)
    return render(request, 'host/create_host.html', {'form': form})

def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='donations/excel')
    response['Content-Disposition'] = 'attachment; filename=hosts' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('hosts')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True

    ws.write(0, 0, 'Hosts report of the "SafeHaven" association:', font_style)  # the title of the file

    columns = ['Name', 'Is Occupied']  # the columns in the table
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = hostReq.objects.all().values_list('fullname', 'is_occupied')

    font_style = xlwt.XFStyle()

    hosts = hostReq.objects.all()
    total_hosts = hosts.count()
    free_hosts = hosts.filter(is_occupied=False).count()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    ws.write(total_hosts + 3, 0, 'Total Hosts:', font_style)
    ws.write(total_hosts + 3, 1, str(total_hosts), font_style)  # print the total amount
    ws.write(total_hosts + 4, 0, 'Free Hosts:', font_style)
    ws.write(total_hosts + 4, 1, str(free_hosts), font_style)  # print the total amount

    wb.save(response)  # save the file

    return response

def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('Tahoma', 'Tahoma.ttf'))
    textob.setFont("Tahoma", 14)  # set the font of the text

    hosts = hostReq.objects.all()  # designate the model
    lines = []  # creat a new list for the objects

    total_hosts = hosts.count()
    free_hosts = hosts.filter(is_occupied=False).count()

    def is_hebrew(s):
        return all('\u0590' <= c <= '\u05EA' or c == ' ' for c in s)

    # print all data we need
    for host in hosts:
        name = host.fullname
        if is_hebrew(name):
            name = name[::-1]
        lines.append('Host name: ' + name)
        lines.append('Is Occupied: ' + str(host.is_occupied))
        lines.append('    ')
        lines.append('----------------------------------')
        lines.append('    ')

    lines.append('Total Hosts:' + str(total_hosts))
    lines.append('Free Hosts:' + str(free_hosts))

    textob.textLine("Hosts report of the 'SafeHaven' association:")  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='hosts.pdf')


