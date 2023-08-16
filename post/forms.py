from django import forms
from post.models import Post


# class TestForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs["class"] = "form-control"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["picture", "caption", "status", ]
        # exclude = ["user", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"