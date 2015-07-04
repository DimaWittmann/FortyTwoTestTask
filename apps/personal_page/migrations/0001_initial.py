# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('personal_page_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(default='')),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('personal_page', ['Person'])

        # Adding model 'RequestLog'
        db.create_table('personal_page_requestlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True)),
            ('get', self.gf('django.db.models.fields.TextField')(null=True)),
            ('post', self.gf('django.db.models.fields.TextField')(null=True)),
            ('path', self.gf('django.db.models.fields.CharField')(null=True, max_length=255)),
            ('method', self.gf('django.db.models.fields.TextField')(null=True, max_length=10)),
            ('encoding', self.gf('django.db.models.fields.TextField')(null=True, max_length=255)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('personal_page', ['RequestLog'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('personal_page_person')

        # Deleting model 'RequestLog'
        db.delete_table('personal_page_requestlog')


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
            'encoding': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '255'}),
            'get': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255'}),
            'post': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['personal_page']