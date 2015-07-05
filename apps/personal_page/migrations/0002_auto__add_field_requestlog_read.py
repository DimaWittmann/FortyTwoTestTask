# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RequestLog.read'
        db.add_column('personal_page_requestlog', 'read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RequestLog.read'
        db.delete_column('personal_page_requestlog', 'read')


    models = {
        'personal_page.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'personal_page.requestlog': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'RequestLog'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'encoding': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True'}),
            'get': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.TextField', [], {'max_length': '10', 'null': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        }
    }

    complete_apps = ['personal_page']