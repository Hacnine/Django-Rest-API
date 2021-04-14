from rest_framework.pagination import LimitOffsetPagination


class MyPagination(LimitOffsetPagination):
    # Default Limit use 'pass'
    # pass

    # override default limit
    default_limit = 5

    limit_query_param = 'mylimit'

    offset_query_param = 'myoffset'

    max_limit = 4


