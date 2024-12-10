# apps/emails/models.py
from django.core.mail import EmailMessage
from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django_extensions.db.models import TimeStampedModel

import logging
logger = logging.getLogger(__name__)

class Email(TimeStampedModel):
    template_name = 'mail_base.html'

    to = models.EmailField(
        verbose_name='To',
    )
    subject = models.CharField(
        verbose_name='Subject',
        max_length=200,
    )
    content = models.TextField(
        verbose_name='Content',
    )
    compiled_template = models.TextField(
        verbose_name='compiled_template',
        blank=True,
    )
    bcc = models.TextField(
        verbose_name='bcc',
        blank=True,
    )
    is_sent = models.BooleanField(
        verbose_name='is_sent',
        default=False,
    )

    def save(self, **kwargs):
        if not self.compiled_template:
            request = kwargs.pop('request', None)
            context = {
                'title': self.subject,
                'description': self.content,
                'introduction': 'This is an email from the backend',
            }
            body = render_to_string(
                template_name=self.template_name,
                context=context,
                request=request
            )
            self.compiled_template = body
        super().save(**kwargs)

    def send(self):
        try:
            message = EmailMessage(
                subject=self.subject,
                body=mark_safe(self.compiled_template),
                to=[self.to],
                bcc=self.bcc.split(',') if self.bcc else []
            )
            message.content_subtype = "html"
            message.send()
            self.is_sent = True
            self.save()
            logger.info(f"Email sent to {self.to}")
        except Exception as e:
            logger.error(f"Failed to send email to {self.to}: {e}")

    def __str__(self):
        return self.subject