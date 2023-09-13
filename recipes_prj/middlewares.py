from recipes_prj.core.auth_helper.auth_error import error_403


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 403:
            return error_403(request)
        return response

    return middleware
