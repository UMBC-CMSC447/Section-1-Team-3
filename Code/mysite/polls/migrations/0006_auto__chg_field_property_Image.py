# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'property.Image'
        db.alter_column(u'polls_property', 'Image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'property.Image'
        db.alter_column(u'polls_property', 'Image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'polls.property': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Image': ('django.db.models.fields.files.ImageField', [], {'default': "'/no-img.jpg'", 'max_length': '100'}),
            'Location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'property'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Price': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['polls']