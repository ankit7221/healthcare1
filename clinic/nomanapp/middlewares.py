from django.utils.deprecation import MiddlewareMixin

class ClearAdminSessionCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/admin/') and 'admin_session' in request.session:
            response.delete_cookie('admin_session')
        return response
