from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from .forms import TextFileForm
from .utils import mix_words_letters, is_txt_file


def home(request: WSGIRequest) -> HttpResponse:
    form = TextFileForm
    context = {"form": form}
    if request.method == "POST":
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            if is_txt_file:
                for chunk in file.chunks():
                    text_before = chunk.decode()
                    text_after: str = mix_words_letters(chunk.decode().split())
                context = {"text_after": text_after, "text_before": text_before}
                return render(request, "result.html", context)
            else:
                return HttpResponse(f"Wrong format, file should have .txt format")
    return render(request, "file_upload_form.html", context)
