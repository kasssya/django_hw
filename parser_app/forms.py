from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("BOOK", "BOOK"),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self) -> object:
        if self.data["media_type"] == "BOOK":
            book_parser = parser.parser_func()
            for i in book_parser:
                models.Books.objects.create(**i)
