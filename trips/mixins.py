<<<<<<< HEAD
class DeleteTripMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
=======
class DeleteTripMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
>>>>>>> 791d9a3a509562de833ab44c5096fe3f04af9371
