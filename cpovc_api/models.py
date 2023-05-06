from django.db import models

class ListGeneral(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_description = models.CharField(max_length=255)

    def __str__(self):
        return self.item_description

class RegOrgUnit(models.Model):
    org_unit_id = models.AutoField(primary_key=True)
    org_unit_name = models.CharField(max_length=255)
    parent_org_unit_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.org_unit_name

class ListGeo(models.Model):
    geo_id = models.AutoField(primary_key=True)
    geo_name = models.CharField(max_length=255)
    parent_geo_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.geo_name
