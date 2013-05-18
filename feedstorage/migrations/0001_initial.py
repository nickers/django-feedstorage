# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'feedstorage_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200, db_index=True)),
            ('etag', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'feedstorage', ['Feed'])

        # Adding model 'FetchStatus'
        db.create_table(u'feedstorage_fetchstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedstorage.Feed'])),
            ('http_status_code', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('size_bytes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('timestamp_start', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('timestamp_end', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('nb_entries', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('nb_new_entries', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('error_msg', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'feedstorage', ['FetchStatus'])

        # Adding unique constraint on 'FetchStatus', fields ['feed', 'timestamp_start']
        db.create_unique(u'feedstorage_fetchstatus', ['feed_id', 'timestamp_start'])

        # Adding model 'Entry'
        db.create_table(u'feedstorage_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedstorage.Feed'])),
            ('fetch_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedstorage.FetchStatus'])),
            ('xml', self.gf('django.db.models.fields.TextField')()),
            ('uid_hash', self.gf('django.db.models.fields.CharField')(max_length=32, db_index=True)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('edit_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'feedstorage', ['Entry'])

        # Adding unique constraint on 'Entry', fields ['feed', 'uid_hash']
        db.create_unique(u'feedstorage_entry', ['feed_id', 'uid_hash'])

        # Adding model 'Subscription'
        db.create_table(u'feedstorage_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedstorage.Feed'])),
            ('callback', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('dispatch_uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('edit_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'feedstorage', ['Subscription'])

        # Adding unique constraint on 'Subscription', fields ['feed', 'callback']
        db.create_unique(u'feedstorage_subscription', ['feed_id', 'callback'])


    def backwards(self, orm):
        # Removing unique constraint on 'Subscription', fields ['feed', 'callback']
        db.delete_unique(u'feedstorage_subscription', ['feed_id', 'callback'])

        # Removing unique constraint on 'Entry', fields ['feed', 'uid_hash']
        db.delete_unique(u'feedstorage_entry', ['feed_id', 'uid_hash'])

        # Removing unique constraint on 'FetchStatus', fields ['feed', 'timestamp_start']
        db.delete_unique(u'feedstorage_fetchstatus', ['feed_id', 'timestamp_start'])

        # Deleting model 'Feed'
        db.delete_table(u'feedstorage_feed')

        # Deleting model 'FetchStatus'
        db.delete_table(u'feedstorage_fetchstatus')

        # Deleting model 'Entry'
        db.delete_table(u'feedstorage_entry')

        # Deleting model 'Subscription'
        db.delete_table(u'feedstorage_subscription')


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