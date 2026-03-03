from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="seasons")
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["series", "number"]
        unique_together = ["series", "number"]

    def __str__(self):
        return f"{self.series.title} - Season {self.number}"


class Episode(models.Model):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="episodes"
    )
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.DurationField(blank=True, null=True)
    script = models.TextField(blank=True, help_text="Full episode script")
    script_status = models.CharField(
        max_length=50,
        choices=[
            ("draft", "Draft"),
            ("review", "Under Review"),
            ("approved", "Approved"),
            ("final", "Final"),
        ],
        default="draft",
        blank=True,
    )
    script_author = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["season", "number"]
        unique_together = ["season", "number"]

    def __str__(self):
        return f"S{self.season.number:02d}E{self.number:02d} - {self.title}"


class Sequence(models.Model):
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="sequences"
    )
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["episode", "number"]
        unique_together = ["episode", "number"]

    def __str__(self):
        return f"{self.episode} - Sequence {self.number}"


class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    series = models.ManyToManyField(Series, related_name="characters", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class WardrobeItem(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name="wardrobe_items"
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["character", "name"]

    def __str__(self):
        return f"{self.character.name} - {self.name}"


class Shot(models.Model):
    sequence = models.ForeignKey(
        Sequence, on_delete=models.CASCADE, related_name="shots"
    )
    number = models.PositiveIntegerField()
    script = models.TextField(blank=True, help_text="Script/dialogue for this shot")
    characters = models.ManyToManyField(
        Character, through="ShotCharacter", related_name="shots"
    )
    background = models.CharField(
        max_length=500, blank=True, help_text="Background description"
    )
    camera_angle = models.CharField(
        max_length=500, blank=True, help_text="Camera angle description"
    )
    camera_movement = models.CharField(
        max_length=500, blank=True, help_text="Camera movement description"
    )
    duration = models.DurationField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["sequence", "number"]
        unique_together = ["sequence", "number"]

    def __str__(self):
        return f"{self.sequence} - Shot {self.number}"


class ShotCharacter(models.Model):
    shot = models.ForeignKey(Shot, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    wardrobe = models.ForeignKey(
        WardrobeItem, on_delete=models.SET_NULL, blank=True, null=True
    )
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ["shot", "character"]

    def __str__(self):
        wardrobe_str = f" ({self.wardrobe.name})" if self.wardrobe else ""
        return f"{self.shot} - {self.character.name}{wardrobe_str}"
