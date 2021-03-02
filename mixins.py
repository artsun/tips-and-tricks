class BurstMixin(object):
    limits = {}  # need to be overridden
    burst_key = None  # need to be overridden

    # defaults
    burst_codes = [201, 202]
    limits_to_secs = {'minute': 60, 'hour': 3600, 'day': 3600 * 24}
    error_code = 200

    def get_burst_key(self, request, period):
        user_part = get_client_ip(request)
        view_part = self.burst_key or 'mixin'
        return '{}:{}:{}'.format(view_part, user_part, period)

    def check_burst(self, request):
        is_exceeded = []
        for period, limit in self.limits.items():
            key = self.get_burst_key(request, period)
            attempt_cnt = cache.get(key)
            if attempt_cnt and int(attempt_cnt) > int(limit):
                is_exceeded.append(period)
        return is_exceeded

    def increment_counters(self, request):
        for period, limit in self.limits.items():
            key = self.get_burst_key(request, period)
            if cache.get(key):
                cache.incr(key)
            else:
                timeout = self.limits_to_secs.get(period, None)
                cache.set(key, 1, timeout)

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'post':
            is_exceeded = self.check_burst(request)
            if is_exceeded:
                errors = {'__all__': [u'Превышено количество отправок.']}
                return JsonResponse({'status': 'ERR', 'errors': errors}, status=self.error_code)

        response = super(BurstMixin, self).dispatch(request, *args, **kwargs)

        if request.method.lower() == 'post' and response.status_code in self.burst_codes:
            self.increment_counters(request)
        return response


class PaginatorMixin(object):
    objs: Paginator
    pages_left: list
    pages_right: list

    def paginate(self, obj_collection, pages, page):
        paginator = Paginator(obj_collection, pages)
        self.objs = paginator.get_page(page)
        self.pages_left = list(reversed(list(paginator)[int(page)-1::-1][:5]))
        self.pages_right = list(paginator)[int(page)::1][:5]
