from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        return Response({
            'per_page': self.page_size,
            'page': self.page.number,
            'total': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'data': data
        })
