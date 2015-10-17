from django.db import models


class Genres(models.Model):
    class Meta:
        verbose_name_plural = 'Genres'

    genre_id = models.IntegerField(null=True, blank=True)
    genre_parent_id = models.IntegerField(null=True, blank=True)
    genre_title = models.CharField(max_length=255, null=True, blank=True)
    genre_handle = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.genre_title


class Artists(models.Model):
    class Meta:
        verbose_name_plural = 'Artists'

    artist_id = models.IntegerField(null=True, blank=True)
    artist_handle = models.CharField(max_length=255, null=True, blank=True)
    artist_url = models.CharField(max_length=255, null=True, blank=True)
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    artist_bio = models.TextField(null=True, blank=True)
    artist_members = models.TextField(max_length=255, null=True, blank=True)
    artist_website = models.CharField(max_length=255, null=True, blank=True)
    artist_wikipedia_page = models.CharField(max_length=255, null=True, blank=True)
    artist_donation_url = models.CharField(max_length=255, null=True, blank=True)
    artist_contact = models.EmailField(max_length=255, null=True, blank=True)
    artist_active_year_begin = models.IntegerField(null=True, blank=True)
    artist_active_year_end = models.IntegerField(null=True, blank=True)
    artist_related_projects = models.TextField(max_length=255, null=True, blank=True)
    artist_associated_labels = models.CharField(max_length=255, null=True, blank=True)
    artist_comments = models.CharField(max_length=255, null=True, blank=True)
    artist_favorites = models.CharField(max_length=255, null=True, blank=True)
    artist_date_created = models.CharField(max_length=255, null=True, blank=True)
    artist_flattr_name = models.CharField(max_length=255, null=True, blank=True)
    artist_paypal_name = models.CharField(max_length=255, null=True, blank=True)
    artist_latitude = models.FloatField(null=True, blank=True)
    artist_longitude = models.FloatField(null=True, blank=True)
    artist_image_file = models.CharField(max_length=255, null=True, blank=True)
    artist_location = models.TextField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.artist_name


# class ArtistImage(models.Model):
#     artist = models.ForeignKey("main.Artists", null=True, blank=True)
#     image = models.ImageField(upload_to="artist_images")


class Albums(models.Model):
    class Meta:
        verbose_name_plural = 'Albums'
        
    album_id = models.IntegerField(null=True, blank=True)
    album_title = models.CharField(max_length=255, null=True, blank=True)
    album_handle = models.CharField(max_length=255, null=True, blank=True)
    album_url = models.CharField(max_length=255, null=True, blank=True)
    album_type = models.CharField(max_length=255, null=True, blank=True)
    album_artist_name = models.ForeignKey('main.Artists', null=True)
    album_producer = models.CharField(max_length=255, null=True, blank=True)
    album_engineer = models.CharField(max_length=255, null=True, blank=True)
    album_information = models.TextField(null=True, blank=True)
    album_date_released = models.CharField(max_length=255, null=True, blank=True)
    album_comments = models.IntegerField(null=True, blank=True)
    album_favorites = models.IntegerField(null=True, blank=True)
    album_tracks = models.IntegerField(null=True, blank=True)
    album_listens = models.IntegerField(null=True, blank=True)
    album_date_created = models.CharField(max_length=255, null=True, blank=True)
    album_image_file = models.ImageField(upload_to="album_images", null=True)

    def __unicode__(self):
        return self.album_title

class Tracks(models.Model):
    class Meta:
        verbose_name_plural = 'Tracks'

    track_id = models.IntegerField(null=True, blank=True)
    track_title = models.CharField(max_length=255, null=True, blank=True)
    track_url = models.CharField(max_length=255, null=True, blank=True)
    track_image_file = models.ImageField(upload_to="track_images", null=True)
    album = models.ForeignKey('main.Albums', null=True)
    license_title = models.CharField(max_length=255, null=True, blank=True)
    license_url = models.CharField(max_length=255, null=True, blank=True)
    track_language_code = models.CharField(max_length=255, null=True, blank=True)
    track_duration = models.CharField(max_length=255, null=True, blank=True)
    track_number = models.IntegerField(null=True, blank=True)
    track_disc_number = models.IntegerField(null=True, blank=True)
    track_explicit = models.CharField(max_length=255, null=True, blank=True)
    track_explicit_notes = models.CharField(max_length=255, null=True, blank=True)
    track_copyright_c = models.CharField(max_length=255, null=True, blank=True)
    track_copyright_p = models.CharField(max_length=255, null=True, blank=True)
    track_composer = models.CharField(max_length=255, null=True, blank=True)
    track_lyricist = models.CharField(max_length=255, null=True, blank=True)
    track_publisher = models.CharField(max_length=255, null=True, blank=True)
    track_instrumental = models.IntegerField(null=True, blank=True)
    track_information = models.CharField(max_length=255, null=True, blank=True)
    track_date_recorded = models.CharField(max_length=255, null=True, blank=True)
    track_comments = models.CharField(max_length=255, null=True, blank=True)
    track_favorites = models.IntegerField(null=True, blank=True)
    track_listens = models.IntegerField(null=True, blank=True)
    track_interest = models.IntegerField(null=True, blank=True)
    track_bit_rate = models.IntegerField(null=True, blank=True)
    track_date_created = models.CharField(max_length=255, null=True, blank=True)
    track_file = models.CharField(max_length=255, null=True, blank=True)
    license_image_file = models.ImageField(upload_to="license_images", null=True)
    licencse_image_file_large = models.ImageField(upload_to="license_images_large", null=True)

    def __unicode__(self):
        return self.album_title
