# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'property.Owner'
        db.add_column(u'polls_property', 'Owner',
                      self.gf('django.db.models.fields.CharField')(default='Matthew', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'property.Owner'
        db.delete_column(u'polls_property', 'Owner')


    models = {
        u'polls.property': {
            'Location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'property'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Price': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['polls']