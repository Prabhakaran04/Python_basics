from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "The Boys":
            raise ValidationError("This book can't be added")
        return value

    def validate_quantity(self, value):
        if value > 200:
            raise ValidationError("Quantity more than 200 are not accepeted")
        return value
