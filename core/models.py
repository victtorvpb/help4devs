# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_extensions.db.models import TimeStampedModel
from django.db import models



class JobName(TimeStampedModel):
    job_name = models.CharField(max_length=250, blank=False, null=False,  verbose_name="Seu cargo anterior")
  

class Dev(TimeStampedModel):
    name = models.CharField(max_length=250, blank=False, null=False, verbose_name="Seu nome")
    job = models.CharField(max_length=250, blank=False, null=False, default="Dev", verbose_name="Seu cargo anterior")
    place = models.CharField(max_length=200, blank=False, null=False, verbose_name="Localidade que você se encontra")
    email = models.EmailField(blank=False, null=False, verbose_name="Seu e-mail")
    github = models.URLField(blank=True, null=True, verbose_name="Seu Github, se tiver")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Seu Linkedin, se tiver")
    job_name = models.ForeignKey(JobName, on_delete=models.PROTECT, related_name='person_jobs')

    @property
    def short_linkedin_url(self):
        if self.linkedin is None:
            return ""
        return str(self.linkedin).split('/in/')[1]

    @property
    def short_github_url(self):
        if self.github is None:
            return ""
        return str(self.github).split('.com/')[1]
