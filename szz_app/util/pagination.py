from rest_framework.pagination import PageNumberPagination


class BasicPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'size'
    max_page_size = 10
