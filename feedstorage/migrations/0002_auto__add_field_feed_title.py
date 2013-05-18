# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feed.title'
        db.add_column(u'feedstorage_feed', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Feed.title'
        db.delete_column(u'feedstorage_feed', 'title')


    models = {
        u'feedstorage.entry': {
            'Meta': {'unique_together': "(('feed', 'uid_hash'),)", 'object_name': 'Entry'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedstorage.Feed']"}),
            'fetch_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedstorage.FetchStatus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid_hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'xml': ('django.db.models.fields.TextField', [], {})
        },
        u'feedstorage.feed': {
            'Meta': {'object_name': 'Feed'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'})
        },
        u'feedstorage.fetchstatus': {
            'Meta': {'unique_together': "(('feed', 'timestamp_start'),)", 'object_name': 'FetchStatus'},
            'error_msg': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedstorage.Feed']"}),
            'http_status_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb_entries': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nb_new_entries': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size_bytes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'timestamp_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'timestamp_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        u'feedstorage.subscription': {
            'Meta': {'unique_together': "(('feed', 'callback'),)", 'object_name': 'Subscription'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'callback': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'dispatch_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'edit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedstorage.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['feedstorage']