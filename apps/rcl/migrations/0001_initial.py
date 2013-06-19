# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Community'
        db.create_table(u'rcl_community', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('max_capacity', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('current_residents_amount', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('needs_people', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url_name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=127)),
            ('datetime_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'rcl', ['Community'])


    def backwards(self, orm):
        # Deleting model 'Community'
        db.delete_table(u'rcl_community')


    models = {
        u'rcl.community': {
            'Meta': {'object_name': 'Community'},
            'current_residents_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'datetime_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'max_capacity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'needs_people': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '127'})
        }
    }

    complete_apps = ['rcl']