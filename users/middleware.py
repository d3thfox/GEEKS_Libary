from django.utils.deprecation import MiddlewareMixin
from  django.http import HttpResponseBadRequest

class ExperienceClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 1:
                return HttpResponseBadRequest('Ваш опыт слишком мал,вы не подходите')
            elif 1 <= experience <= 3:
                request.club = '1000$'
            elif 4 <= experience <= 7:
                request.club = '2000$'
            elif 8 <= experience <= 10:
                request.club = '5000$'
            else:
                return HttpResponseBadRequest('У нас не хватит денег')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Опыт не определен')
