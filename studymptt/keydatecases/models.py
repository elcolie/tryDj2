from django.db import models


class ICD10(models.Model):
    primary_key_number = models.CharField(max_length=10, primary_key=True)
    star_key_number = models.CharField(max_length=10, blank=True, null=True)
    additional_key_number = models.CharField(max_length=10, blank=True, null=True)
    preferred_short_description = models.CharField(max_length=128, )

    def __str__(self):
        return f'{self.primary_key_number} {self.star_key_number}'


class CaseICD10Connection(models.Model):
    case = models.ForeignKey('KeyDateCase', related_name='connections', related_query_name='key_date_cases', on_delete=models.CASCADE)
    icd_10 = models.ForeignKey('ICD10', related_name='connections', related_query_name='icd_10s', on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    certainty = models.CharField(max_length=1, default='G', )


class KeyDateCase(models.Model):
    name = models.CharField(max_length=20)
    diagnose_all_icd_10 = models.ManyToManyField(ICD10, related_name='icd10s', related_query_name='icd10s',
                                                 through=CaseICD10Connection)

