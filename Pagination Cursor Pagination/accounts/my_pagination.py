from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):

    page_size = 3
    ordering = 'name'

    # override default limit
    # default_limit = 5
    #
    cursor_query_param = 'mylimit'
    #
    # offset_query_param = 'myoffset'
    #
    # max_limit = 4


