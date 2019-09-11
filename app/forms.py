from django import forms
from .models import Post
from django.utils import timezone


# class CreateForm(forms.ModelForm):
#     """実況の新規作成用のフォーム"""
#     class Meta:
#         model = Post
#         fields = ('title', 'start_time', 'episode', 'comment')
#         widgets = {
#             'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
#         # 以下が動かなかったのでModelFormは不採用にしました。
#         # input_formats = {
#         #     'start_time': ['%Y/%m/%d %H:%i']
#         # }

class CreateForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=140,
        help_text='Twitterハッシュタグの仕様上、？や！などの記号は使えません。Vtuberなどのアーカイブの場合、「配信タイトル_名前」を推奨します。'
    )
    start_time = forms.DateTimeField(
        label='開始時刻',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    episode = forms.IntegerField(
        label='話数',
        help_text='劇場作品やYouTube動画のときはとりあえず０話にしておいてください。空欄不可なので。（後々対応します）'
    )
    comment = forms.CharField(
        label='コメント',
        widget=forms.Textarea(attrs={"max_length": 140}),
        max_length=140,
        help_text='「未視聴なのでネタバレNG」「一緒に考察しましょう」「１５周目」「〇〇への愛を語りましょう」など書いておくといいかもしれません。'
                  'あと、見るプラットフォーム（Netflix, Prime Videoなど）を書いてあげると優しいかもです。'
    )

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     symbol = ['!', '"', '#', '$', '%', '&', '(', ')', '-', '=', '~', '^', '¥', '|', '@', '`', '[', ']', '{', '}',
    #     '?', '/']
    #     if all((s in title) for s in symbol):
    #         raise forms.ValidationError(
    #             '記号は含めないでください'
    #         )
    #     return title
