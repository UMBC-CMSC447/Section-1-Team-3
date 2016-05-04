# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'avatar'
        db.create_table(u'polls_avatar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(default='/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'polls', ['avatar'])


    def backwards(self, orm):
        # Deleting model 'avatar'
        db.delete_table(u'polls_avatar')


    models = {
        u'polls.avatar': {
            'Meta': {'object_name': 'avatar'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'/no-img.jpg'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'polls.property': {
            'Approval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Image': ('django.db.models.fields.files.ImageField', [], {'default': "'/no-img.jpg'", 'max_length': '100'}),
            'Lat': ('django.db.models.fields.FloatField', [], {'default': '38.388656', 'null': 'True'}),
            'Location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Long': ('django.db.models.fields.FloatField', [], {'default': '-75.063863', 'null': 'True'}),
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