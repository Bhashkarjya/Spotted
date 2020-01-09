from django.shortcuts import render

### Landing
def base(request):
    return render(request, 'Animal/base.html', )

def campaign(request):
    return render(request, 'Animal/campaign.html')

def donate(request):
    return render(request, 'Animal/donate.html')

def volunteer(request):
    return render(request, 'Animal/volunteer.html')



def News_Events(request):
    return render(request, 'Animal/News_Events.html')

def about(request):
    return render(request, 'Animal/about.html')

def thanku(request):
    return render(request, 'Animal/thanku.html')
