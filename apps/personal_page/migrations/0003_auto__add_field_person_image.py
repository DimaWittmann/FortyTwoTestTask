# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.image'
        db.add_column('personal_page_person', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='images/no-img.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.image'
        db.delete_column('personal_page_person', 'image')


    models = {
        'personal_page.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'images/no-img.jpg'", 'max_length': '100'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'personal_page.requestlog': {
            'Meta': {'object_name': 'RequestLog', 'ordering': "('-timestamp',)"},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'encoding': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '255'}),
            'get': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255'}),
            'post': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['personal_page']