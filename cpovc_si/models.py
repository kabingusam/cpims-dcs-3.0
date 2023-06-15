from django.db import models
import uuid
from django.utils import timezone

from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_forms.models import OVCCaseRecord
from cpovc_auth.models import AppUser

# Create your models here.

from django.db import models

class SIMain(models.Model):
    care_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False)
    case = models.ForeignKey(OVCCaseRecord, on_delete=models.CASCADE)
    case_number = models.CharField(max_length=12, blank=True)
    care_type = models.CharField(max_length=5, null=True, blank=True)
    care_sub_type = models.CharField(max_length=5, null=True, blank=True)
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    school_level = models.CharField(max_length=4, null=True)
    immunization_status = models.CharField(max_length=4, null=True)
    org_unit = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    case_status = models.BooleanField(null=True, default=None)
    case_stage = models.IntegerField(default=0)
    case_date = models.DateField()
    created_by = models.ForeignKey(
        AppUser, blank=True, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_modified = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    def _get_cases(self):
        _cases = SIMain.objects.all().count()
        if self.case_number:
            return _cases
        else:
            return _cases + 1

    def save(self, *args, **kwargs):
        # This is to save the Unique code.
        if self.pk is None and not self.case_number:
            self.case_number = self.case_number
        elif self.pk and not self.case_number:
            case_num = self._get_cases()
            self.case_number = case_num

        # Call the original save method
        super(SIMain, self).save(*args, **kwargs)

    class Meta:
        db_table = 'ovc_si_main'
        verbose_name = 'Statutory Institution'
        verbose_name_plural = 'Statutory Institutions'

    def __unicode__(self):
        """To be returned by admin actions."""
        return '%s - %s' % (str(self.case_number), str(self.case))

class Person(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField()
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    sub_location = models.CharField(max_length=50, blank=True, null=True)
    village = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname', 'first_name']

    def __str__(self):
        return f"{self.surname}, {self.first_name} {self.other_names}"
