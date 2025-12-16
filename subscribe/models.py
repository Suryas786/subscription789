from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Subscription(models.Model):

    PLAN_CHOICES = (
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="subscription"
    )

    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES
    )

    start_date = models.DateTimeField(
        default=timezone.now
    )

    end_date = models.DateTimeField()

    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        """
        Automatically calculate subscription end date
        based on selected plan
        """
        if not self.end_date:
            if self.plan == "weekly":
                self.end_date = self.start_date + timedelta(days=7)
            elif self.plan == "monthly":
                self.end_date = self.start_date + timedelta(days=30)
            elif self.plan == "yearly":
                self.end_date = self.start_date + timedelta(days=365)

        super().save(*args, **kwargs)

    def days_left(self):
        """
        Returns remaining days of subscription
        """
        remaining = self.end_date - timezone.now()
        return max(remaining.days, 0)

    def __str__(self):
        return f"{self.user.username} - {self.plan}"
