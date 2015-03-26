import cStringIO

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File

import requests

from models import Article


class StringIO(object):

    def __init__(self, *args, **kwargs):
        self.s = cStringIO.StringIO(*args)
        self.name = kwargs.get("name", '')

    @property
    def size(self):
        current = self.tell()
        self.seek(0, os.SEEK_END)
        value = self.tell()
        self.seek(current)
        return value

    def __getattr__(self, key):
        return getattr(self.s, key)

    def __iter__(self):
        for line in self.readlines():
            yield line

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


def index(request):
    return HttpResponse("Hello World!")


def fetch_pdf(request):
    page_url = request.GET.get("url")
    title, filename, pdf_url = get_acs_stuff(page_url)
    print title, filename, pdf_url
    f = download_file(filename, pdf_url)
    article = Article(title=title, filename=filename)
    article.pdf = File(f)
    article.save()
    return HttpResponse("Fetched!")


def get_acs_stuff(url):
    r = requests.get(url)
    text = r.text
    start = text.index("<title>")
    end = text.index("</title>")
    title = text[start+7:end].strip() + ".pdf"
    return title, '_'.join(url.split('/')[-2:]), url.replace("full", "pdf")


def download_file(filename, url):
    r = requests.get(url, stream=True)
    f = StringIO(name=filename)
    for chunk in r.iter_content(chunk_size=1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
            f.flush()
    return f