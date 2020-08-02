from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import URLs
import urllib
import hashlib
import datetime
import pytz
from urllib.parse import urljoin, urlparse
import re


def validate_url(url):
    url = url or 'invalid'
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    is_valid = re.match(regex, url) is not None
    return is_valid

def home(request):
	return render(request, 'url_shortner/index.html')

def expiry_check(expiry,url):
	utc=pytz.UTC
	current = utc.localize(datetime.datetime.now()) 
	if expiry is not None:
		if expiry < current:
			URLs.objects.filter(targetURL=url).delete()

def get_short_path(short_url):
    parts = urlparse(short_url)
    short_path = parts.path.lstrip('/')
    scheme = parts.scheme.lstrip('/')
    base_url = parts.netloc.lstrip('/')
    return short_path, scheme, base_url

def shortner(request):
	if request.method == 'POST':
		if request.POST["url"] or request.POST["url"] != '':
			if validate_url(request.POST["url"]):
				longurl = request.POST["url"]
				scheme = get_short_path(longurl)[1]
				base_url = get_short_path(longurl)[2]
				created = datetime.datetime.now()
				if request.POST["expiry_time"] or request.POST["expiry_time"]!='':
					expiry_time = created + datetime.timedelta(minutes = int(request.POST["expiry_time"]))
				else:
					expiry_time = ''
				private_token = request.POST["private_token"]
				short_code = request.POST["short_code"]
				try:
					check = URLs.objects.get(targetURL = longurl)
					shortURL = check.shortURL
					expiry = check.expiry_time
					if expiry!= '':
						expiry_check(expiry,longurl)
						check = URLs.objects.get(targetURL = longurl)
					click_info = check.click_info
				except URLs.DoesNotExist:
					click_info = 1
					if short_code == '':
						shortURL = get_short_path(longurl)[0]
						hashObject = hashlib.md5(shortURL.encode('utf-8'))
						shortURL = hashObject.hexdigest()

					else:
						shortURL = short_code
						try:
							check = URLs.objects.get(shortURL = shortURL)
							return render(request, 'url_shortner/index.html',{
								'error_message':"Custom Code is already taken",
							})
						except:
							pass
					if expiry_time == '':
						entry = URLs(shortURL = shortURL, targetURL=longurl, created = created, private_token = private_token, click_info = 1)
					else: 
						entry = URLs(shortURL = shortURL, targetURL=longurl, created = created, expiry_time = expiry_time, private_token = private_token, click_info = 1)
					entry.save()
				return render(request, 'url_shortner/index.html',{
						'shortURL':'{0}://{1}/{2}'.format(scheme, base_url, shortURL),
						'click_info': click_info
					})
			else:
				return render(request, 'url_shortner/index.html',{
					'error_message':"Invalid Url",
				})
		else:
			return render(request, 'url_shortner/index.html',{
					'error_message':"Please enter the URL",
				})
	else:
		return render(request, 'url_shortner/index.html')
def retrieve(request):
	if request.method == 'POST':
		inputURL = request.POST["url"]
		if validate_url(inputURL):
			private_token = request.POST["private_token"]
			shortURL = get_short_path(inputURL)[0]
			try:
				target = URLs.objects.get(shortURL = shortURL)
				targetURL = target.targetURL
				try:
					privateToken = target.private_token
				except:
					privateToken = ''
				
				if privateToken == private_token:
					try:
						target.click_info = int(float(target.click_info))  + 1
					except:
						target.click_info = 1
					target.save()
					return render(request, 'url_shortner/output.html',{
								'URL':targetURL,
							})
				else:
					return render(request, 'url_shortner/output.html',{
								'error_message':"Private Token is wrong",
							})
			except:
				return render(request, 'url_shortner/output.html',{
					'error_message':"URL Not Present",
				})
		else:
			return render(request, 'url_shortner/output.html',{
				'error_message':"Invalid Url",
			})
	else:
		return render(request, 'url_shortner/output.html')