import re

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

phone_regex = RegexValidator(
    regex=r'^996\d{9}$',
    message=_("Phone number must be entered in the format: "
            "'996*******'. Up to 15 digits allowed.")
)

acc_number_regex=RegexValidator(
    regex=r'\d{16}',
    message=_('Account number up to 16 digits allowed')
)

inn_regex=RegexValidator(
    regex=r'^(1|2){1}\d{13}$',
    message=_('Pass valid Inn number')
)

def clean_phone(phone):
    return '+' + re.sub(r"\D", "", str(phone))
