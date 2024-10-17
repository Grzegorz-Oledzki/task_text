from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from task.forms import TextFileForm
from task.services.letters_shuffler import is_txt_file, mix_words_letters


def home(request: WSGIRequest) -> HttpResponse:
    form = TextFileForm
    context = {"form": form}
    if request.method == "POST":
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            if is_txt_file(file):
                for chunk in file.chunks():
                    try:
                        text_before = chunk.decode()
                    except UnicodeDecodeError:
                        return HttpResponse(
                            f"Unable to decode this file, try with normal text"
                        )
                    text_after: str = mix_words_letters(text_before.split())
                context = {"text_after": text_after, "text_before": text_before}
                return render(request, "result.html", context)
            else:
                return HttpResponse(f"Wrong format, file should have .txt format")
    return render(request, "file_upload_form.html", context)
