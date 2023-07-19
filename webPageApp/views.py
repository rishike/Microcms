from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from webPageApp.models import Device

from webPageApp.forms import LeadCaptureForm

from webPageApp.forms import WalkInForm
from webPageApp.models import WalkIn

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def device_list(request):
    devices = Device.objects.all()

    paginator = Paginator(devices, 12)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    lead_form = LeadCaptureForm()

    return render(request, 'webPage\device_list.html', {'page_obj': page_obj, 'form' : lead_form})


def lead_capture(request):
    if request.method == 'POST':
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            devices = Device.objects.filter(city=city)

            # Paginate the devices
            paginator = Paginator(devices, 12)  # Display 12 devices per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'device_list.html', {'page_obj': page_obj})
    else:
        form = LeadCaptureForm()

    return render(request, 'lead_capture.html', {'form': form})


def device_detail(request, device_id):
    device = Device.objects.get(id=device_id)

    if request.method == 'POST':
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            # Process the form data and save the lead to the database
            # You can access the form data using form.cleaned_data
            # Example: lead = Lead.objects.create(**form.cleaned_data)
            return redirect('thank_you')  # Redirect to a thank you page after successful submission
    else:
        form = LeadCaptureForm()

    return render(request, 'device_detail.html', {'device': device, 'form': form})

def send_visitor_email(walk_in):
    subject = 'Walk-in Confirmation'
    html_message = render_to_string('email/visitor_email.html', {'walk_in': walk_in})
    plain_message = strip_tags(html_message)
    from_email = 'your-email@example.com'
    to_email = walk_in.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

def send_vendor_email(walk_in):
    subject = 'New Walk-in Notification'
    html_message = render_to_string('email/vendor_email.html', {'walk_in': walk_in})
    plain_message = strip_tags(html_message)
    from_email = 'your-email@example.com'
    to_email = walk_in.vendor.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

def walk_in(request):
    if request.method == 'POST':
        form = WalkInForm(request.POST)
        if form.is_valid():
            # Create a new walk-in record with a token number
            walk_in = form.save(commit=False)
            walk_in.token_number = WalkIn.objects.count() + 1
            walk_in.save()
 
            # Send email notifications
            send_visitor_email(walk_in)
            send_vendor_email(walk_in)
            
            return redirect('thank_you')  # Redirect to a thank you page after successful submission
    else:
        form = WalkInForm()

    return render(request, 'walk_in.html', {'form': form})


