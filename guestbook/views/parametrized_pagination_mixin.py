class ParametrizedPaginationMixin():
    """Allows customizing paginate_by by checking for optional GET request
    parameter: ?paginate_by
    """

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return paginate_by
