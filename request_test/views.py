from django.shortcuts import render
from .models import UploadedFile


def get_request_info(request):
    context = {
        'method': request.method,
        'get_data': request.GET,
        'post_data': request.POST,
        'user': request.user,
        'is_logged_in': request.user.is_authenticated,
        'session_value': request.session.get('demo', '없음'),
        'user_agent': request.META.get('HTTP_USER_AGENT', '알 수 없음'),
        'client_ip': request.META.get('REMOTE_ADDR', '알 수 없음'),
        'path': request.path,
        'full_url': request.build_absolute_uri()
    }
    
    request.session['demo'] = '임시 세션입니다'

    return render(request=request, template_name='request_test/request_info.html', context=context)


def upload_file(request):
    upload_file_url = None
    title = None
    success = False

    print(request.FILES)

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES.get('file')
        title = request.POST.get('title')
        uploaded = UploadedFile(title=title, file=file)
        uploaded.save()
        upload_file_url = uploaded.file.url
        success = True
    
    return render(request, 'request_test/upload_file.html', {
        'upload_file_url': upload_file_url,
        'title': title,
        'success': success
    })