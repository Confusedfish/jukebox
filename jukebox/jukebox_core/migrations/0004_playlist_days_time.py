# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DefaultPlaylist.Days'
        db.add_column('jukebox_core_DefaultPlaylist', 'Days', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.add_column('jukebox_core_DefaultPlaylist', 'StartTime', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.add_column('jukebox_core_DefaultPlaylist', 'EndTime', self.gf('django.db.models.fields.IntegerField')(null=True))
        db.add_column('jukebox_core_DefaultPlaylist', 'Editing', self.gf('django.db.models.fields.BooleanField')(null=False))

    def backwards(self, orm):
        # Removing field 'DefaultPlaylist.Days'
        db.delete_column('jukebox_core_DefaultPlaylist', 'Days')
        db.delete_column('jukebox_core_DefaultPlaylist', 'StartTime')
        db.delete_column('jukebox_core_DefaultPlaylist', 'EndTime')
        db.delete_column('jukebox_core_DefaultPlaylist', 'Editing')

    models = {
        'jukebox_core.DefaultPlaylist': {
            'Meta': {'ordering': "['Name']", 'object_name': 'DefaultPlaylist'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
			'Days': ('django.db.models.fields.IntegerField', [], {}),
			'StartTime': ('django.db.models.fields.IntegerField', [], {}),
			'EndTime': ('django.db.models.fields.IntegerField', [], {}),
			'Editing': ('django.db.models.fields.BooleanField', [], {})
        },
        'jukebox_core.DefaultPlaylistFavourite': {
            'Created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-Created']", 'unique_together': "(('Song', 'User'),)", 'object_name': 'DefaultPlaylistFavourite'},
            'Song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jukebox_core.Song']"}),
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jukebox_core.DefaultPlaylist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jukebox_core.album': {
            'Meta': {'ordering': "['Title']", 'object_name': 'Album'},
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jukebox_core.artist': {
            'Meta': {'ordering': "['Name']", 'object_name': 'Artist'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jukebox_core.genre': {
            'Meta': {'ordering': "['Name']", 'object_name': 'Genre'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
		'jukebox_core.song': {
            'Album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jukebox_core.Album']", 'null': 'True'}),
            'Artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jukebox_core.Artist']"}),
            'Filename': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jukebox_core.Genre']", 'null': 'True'}),
            'Length': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'ordering': "['Title', 'Artist', 'Album']", 'object_name': 'Song'},
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }

    }

    complete_apps = ['jukebox_core']