# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PrivacyLevel'
        db.create_table(u'privacy_privacylevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=31)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], blank=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'privacy', ['PrivacyLevel'])

        # Adding model 'RCLPrivacySetting'
        db.create_table(u'privacy_rclprivacysetting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
            ('photos_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
            ('residents_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='residents_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
            ('calendar_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='calendar_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
            ('projects_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
            ('experiences_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exoeriences_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
            ('donations_privacy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donations_settings_applied', null=True, to=orm['privacy.PrivacyLevel'])),
        ))
        db.send_create_signal(u'privacy', ['RCLPrivacySetting'])


    def backwards(self, orm):
        # Deleting model 'PrivacyLevel'
        db.delete_table(u'privacy_privacylevel')

        # Deleting model 'RCLPrivacySetting'
        db.delete_table(u'privacy_rclprivacysetting')


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
        u'privacy.privacylevel': {
            'Meta': {'object_name': 'PrivacyLevel'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        },
        u'privacy.rclprivacysetting': {
            'Meta': {'object_name': 'RCLPrivacySetting'},
            'calendar_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'calendar_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"}),
            'donations_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donations_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"}),
            'experiences_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exoeriences_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"}),
            'photos_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"}),
            'projects_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"}),
            'residents_privacy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'residents_settings_applied'", 'null': 'True', 'to': u"orm['privacy.PrivacyLevel']"})
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

    complete_apps = ['privacy']