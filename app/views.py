from django.shortcuts import render,render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from .forms import Paragraph
from . import getSummary


def landing_view(request):
	result = []
	form = Paragraph(request.POST or None)
	if form.is_valid():
		text = form.cleaned_data.get('Text')
		result = getSummary.main(text)
	context = {
		"form" : form,
		"result" : result,
	}
	return render(request, "landing.html", context)