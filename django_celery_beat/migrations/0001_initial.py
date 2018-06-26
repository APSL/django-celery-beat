# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IntervalSchedule'
        db.create_table(u'django_celery_beat_intervalschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('every', self.gf('django.db.models.fields.IntegerField')()),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=24)),
        ))
        db.send_create_signal(u'django_celery_beat', ['IntervalSchedule'])

        # Adding model 'CrontabSchedule'
        db.create_table(u'django_celery_beat_crontabschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('minute', self.gf('django.db.models.fields.CharField')(default=u'*', max_length=240)),
            ('hour', self.gf('django.db.models.fields.CharField')(default=u'*', max_length=96)),
            ('day_of_week', self.gf('django.db.models.fields.CharField')(default=u'*', max_length=64)),
            ('day_of_month', self.gf('django.db.models.fields.CharField')(default=u'*', max_length=124)),
            ('month_of_year', self.gf('django.db.models.fields.CharField')(default=u'*', max_length=64)),
            ('timezone', self.gf('timezone_field.fields.TimeZoneField')(default=u'UTC')),
        ))
        db.send_create_signal(u'django_celery_beat', ['CrontabSchedule'])

        # Adding model 'PeriodicTasks'
        db.create_table(u'django_celery_beat_periodictasks', (
            ('ident', self.gf('django.db.models.fields.SmallIntegerField')(default=1, unique=True, primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'django_celery_beat', ['PeriodicTasks'])

        # Adding model 'PeriodicTask'
        db.create_table(u'django_celery_beat_periodictask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('interval', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_celery_beat.IntervalSchedule'], null=True, blank=True)),
            ('crontab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_celery_beat.CrontabSchedule'], null=True, blank=True)),
            ('args', self.gf('django.db.models.fields.TextField')(default=u'[]', blank=True)),
            ('kwargs', self.gf('django.db.models.fields.TextField')(default=u'{}', blank=True)),
            ('queue', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('exchange', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('routing_key', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('expires', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('one_off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_run_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('total_run_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'django_celery_beat', ['PeriodicTask'])


    def backwards(self, orm):
        # Deleting model 'IntervalSchedule'
        db.delete_table(u'django_celery_beat_intervalschedule')

        # Deleting model 'CrontabSchedule'
        db.delete_table(u'django_celery_beat_crontabschedule')

        # Deleting model 'PeriodicTasks'
        db.delete_table(u'django_celery_beat_periodictasks')

        # Deleting model 'PeriodicTask'
        db.delete_table(u'django_celery_beat_periodictask')


    models = {
        u'django_celery_beat.crontabschedule': {
            'Meta': {'ordering': "[u'month_of_year', u'day_of_month', u'day_of_week', u'hour', u'minute', u'timezone']", 'object_name': 'CrontabSchedule'},
            'day_of_month': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '124'}),
            'day_of_week': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'hour': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '96'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '240'}),
            'month_of_year': ('django.db.models.fields.CharField', [], {'default': "u'*'", 'max_length': '64'}),
            'timezone': ('timezone_field.fields.TimeZoneField', [], {'default': "u'UTC'"})
        },
        u'django_celery_beat.intervalschedule': {
            'Meta': {'ordering': "[u'period', u'every']", 'object_name': 'IntervalSchedule'},
            'every': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        u'django_celery_beat.periodictask': {
            'Meta': {'object_name': 'PeriodicTask'},
            'args': ('django.db.models.fields.TextField', [], {'default': "u'[]'", 'blank': 'True'}),
            'crontab': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_celery_beat.CrontabSchedule']", 'null': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'exchange': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_celery_beat.IntervalSchedule']", 'null': 'True', 'blank': 'True'}),
            'kwargs': ('django.db.models.fields.TextField', [], {'default': "u'{}'", 'blank': 'True'}),
            'last_run_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'one_off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'queue': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'routing_key': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_run_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'django_celery_beat.periodictasks': {
            'Meta': {'object_name': 'PeriodicTasks'},
            'ident': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'unique': 'True', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['django_celery_beat']