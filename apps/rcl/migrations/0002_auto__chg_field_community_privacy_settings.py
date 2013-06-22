# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Community.privacy_settings'
        db.alter_column(u'rcl_community', 'privacy_settings_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['privacy.RCLPrivacySetting'], unique=True, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Community.privacy_settings'
        raise RuntimeError("Cannot reverse this migration. 'Community.privacy_settings' and its values cannot be restored.")

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
            'privacy_settings': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['privacy.RCLPrivacySetting']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'url_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '127'})
        },
        u'rcl.communityexperience': {
            'Meta': {'object_name': 'CommunityExperience'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'community': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_experiences'", 'to': u"orm['rcl.Community']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'community_experiences'", 'to': u"orm['users.User']"})
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