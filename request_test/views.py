from django.shortcuts import render


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


