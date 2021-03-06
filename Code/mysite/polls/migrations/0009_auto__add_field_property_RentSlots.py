# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'property.RentSlots'
        db.add_column(u'polls_property', 'RentSlots',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'property.RentSlots'
        db.delete_column(u'polls_property', 'RentSlots')


    models = {
        u'polls.property': {
            'Approval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Image': ('django.db.models.fields.files.ImageField', [], {'default': "'/no-img.jpg'", 'max_length': '100'}),
            'Location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'property'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Price': ('django.db.models.fields.FloatField', [], {}),
            'Rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Rent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'RentSlots': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['polls']