# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Community.internet_focalizer'
        db.add_column(u'rcl_community', 'internet_focalizer',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='internet_focalizers', null=True, to=orm['users.User']),
                      keep_default=False)

        # Adding field 'Community.observer'
        db.add_column(u'rcl_community', 'observer',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='observers', null=True, to=orm['users.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Community.internet_focalizer'
        db.delete_column(u'rcl_community', 'internet_focalizer_id')

        # Deleting field 'Community.observer'
        db.delete_column(u'rcl_community', 'observer_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rcl.community': {
            'Meta': {'object_name': 'Community'},
            'current_residents_amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'datetime_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_focalizer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'internet_focalizers'", 'null': 'True', 'to': u"orm['users.User']"}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'max_capacity': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'needs_people': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'observer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'observers'", 'null': 'True', 'to': u"orm['users.User']"}),
            'url_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '127'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['rcl']