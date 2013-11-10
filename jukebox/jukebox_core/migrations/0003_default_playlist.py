# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
		# Adding model 'DefaultPlaylist'
        db.create_table('jukebox_core_DefaultPlaylist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('jukebox_core', ['DefaultPlaylist'])

        # Adding model 'DefaultPlaylistFavourate'
        db.create_table('jukebox_core_DefaultPlaylistFavourite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jukebox_core.Song'])),
            ('DefaultPlaylist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jukebox_core.DefaultPlaylist'])),
            ('Created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('jukebox_core', ['DefaultPlaylistFavourite'])

        # Adding unique constraint on 'DefaultPlaylistFavourite', fields ['Song', 'DefaultPlaylist']
        db.create_unique('jukebox_core_DefaultPlaylistFavourite', ['Song_id', 'DefaultPlaylist_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'DefaultPlaylistFavourite', fields ['Song', 'DefaultPlaylist']
        db.delete_unique('jukebox_core_DefaultPlaylistFavourite', ['Song_id', 'DefaultPlaylist_id'])

        # Deleting model 'DefaultPlaylist'
        db.delete_table('jukebox_core_DefaultPlaylist')

        # Deleting model 'DefaultPlaylistFavourite'
        db.delete_table('jukebox_core_DefaultPlaylistFavourite')

    models = {
        'jukebox_core.DefaultPlaylist': {
            'Meta': {'ordering': "['Name']", 'object_name': 'DefaultPlaylist'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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