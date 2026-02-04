from django.shortcuts import render

# Create your views here.
def scan_page(request):
    return render(request, 'scan.html')


def physical_scanner(request):
    """
    এই ফাংশনটি ফিজিক্যাল স্ক্যানার (Netum M10) এর জন্য 
    আলাদা একটি HTML পেজ রেন্ডার করবে।
    """
    return render(request, 'physical_scanner.html')