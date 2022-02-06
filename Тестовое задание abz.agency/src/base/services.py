from django.core.exceptions import ValidationError


def validate_fio(fio_obj: str) -> bool:
    """Валидация ФИО"""
    if len(fio_obj.split()) != 3:
        raise ValidationError("ФИО введено некоректно.")
