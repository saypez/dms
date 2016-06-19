from django.shortcuts import render
def conv(request):
	return render(request, 'dms/convert.html')
