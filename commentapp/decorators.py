from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_comment = Comment.objects.get(pk=kwargs['pk'])
        if target_comment.writer == request.user:
            # 그대로 넣어줌. 우리가 실행하고자 하는 게 get이나 post이기 때문에
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
