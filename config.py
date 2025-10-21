#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zamanlayıcı Konfigürasyon Dosyası
Uygulama ayarları ve sabitler
"""

import os
from utils import FileManager

class Config:
    """Uygulama konfigürasyon sınıfı"""
    
    def __init__(self):
        self.app_name = "Zamanlayıcı"
        self.version = "1.0.0"
        self.author = "Zamanlayıcı Ekibi"
        
        # Varsayılan ayarlar
        self.default_settings = {
            'sound_enabled': 'True',
            'sound_volume': '0.5',
            'default_timer_minutes': '5',
            'theme': 'default',
            'language': 'tr',
            'auto_save': 'True',
            'notification_enabled': 'True'
        }
        
        # Ayarları yükle
        self.settings = self.load_settings()
    
    def load_settings(self):
        """Ayarları dosyadan yükle"""
        settings = FileManager.load_settings()
        
        # Varsayılan ayarları eksik olanlarla tamamla
        for key, default_value in self.default_settings.items():
            if key not in settings:
                settings[key] = default_value
        
        return settings
    
    def save_settings(self):
        """Ayarları dosyaya kaydet"""
        FileManager.save_settings(self.settings)
    
    def get(self, key, default=None):
        """Ayar değerini al"""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """Ayar değerini ayarla"""
        self.settings[key] = str(value)
        self.save_settings()
    
    def get_bool(self, key, default=False):
        """Boolean ayar değerini al"""
        value = self.get(key, str(default))
        return value.lower() in ('true', '1', 'yes', 'on')
    
    def get_int(self, key, default=0):
        """Integer ayar değerini al"""
        try:
            return int(self.get(key, str(default)))
        except ValueError:
            return default
    
    def get_float(self, key, default=0.0):
        """Float ayar değerini al"""
        try:
            return float(self.get(key, str(default)))
        except ValueError:
            return default
    
    # Özellik erişimcileri
    @property
    def sound_enabled(self):
        return self.get_bool('sound_enabled', True)
    
    @sound_enabled.setter
    def sound_enabled(self, value):
        self.set('sound_enabled', value)
    
    @property
    def sound_volume(self):
        return self.get_float('sound_volume', 0.5)
    
    @sound_volume.setter
    def sound_volume(self, value):
        self.set('sound_volume', max(0.0, min(1.0, value)))
    
    @property
    def default_timer_minutes(self):
        return self.get_int('default_timer_minutes', 5)
    
    @default_timer_minutes.setter
    def default_timer_minutes(self, value):
        self.set('default_timer_minutes', max(1, value))
    
    @property
    def theme(self):
        return self.get('theme', 'default')
    
    @theme.setter
    def theme(self, value):
        self.set('theme', value)
    
    @property
    def language(self):
        return self.get('language', 'tr')
    
    @language.setter
    def language(self, value):
        self.set('language', value)
    
    @property
    def auto_save(self):
        return self.get_bool('auto_save', True)
    
    @auto_save.setter
    def auto_save(self, value):
        self.set('auto_save', value)
    
    @property
    def notification_enabled(self):
        return self.get_bool('notification_enabled', True)
    
    @notification_enabled.setter
    def notification_enabled(self, value):
        self.set('notification_enabled', value)

# Uygulama sabitleri
class Constants:
    """Uygulama sabitleri"""
    
    # Zaman sabitleri
    MIN_TIMER_MINUTES = 1
    MAX_TIMER_MINUTES = 1440  # 24 saat
    DEFAULT_TIMER_MINUTES = 5
    
    # UI sabitleri
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300
    MIN_WINDOW_WIDTH = 300
    MIN_WINDOW_HEIGHT = 200
    
    # Ses sabitleri
    DEFAULT_VOLUME = 0.5
    MIN_VOLUME = 0.0
    MAX_VOLUME = 1.0
    
    # Dosya sabitleri
    SETTINGS_FILE = "settings.txt"
    LOG_FILE = "zamanlayici.log"
    
    # Renkler (hex)
    PRIMARY_COLOR = "#2E86AB"
    SECONDARY_COLOR = "#A23B72"
    SUCCESS_COLOR = "#28A745"
    WARNING_COLOR = "#FFC107"
    ERROR_COLOR = "#DC3545"
    
    # Fontlar
    DEFAULT_FONT = ("Arial", 10)
    TITLE_FONT = ("Arial", 16, "bold")
    LARGE_FONT = ("Arial", 24, "bold")

# Dil desteği
class Language:
    """Dil desteği sınıfı"""
    
    TURKISH = {
        'app_title': 'Zamanlayıcı',
        'start': 'Başlat',
        'stop': 'Durdur',
        'reset': 'Sıfırla',
        'time_label': 'Süre (dakika):',
        'time_finished': 'Süre doldu!',
        'error_invalid_time': 'Lütfen geçerli bir süre girin!',
        'error_numeric_value': 'Lütfen sayısal bir değer girin!',
        'settings': 'Ayarlar',
        'sound': 'Ses',
        'volume': 'Ses Seviyesi',
        'theme': 'Tema',
        'language': 'Dil'
    }
    
    ENGLISH = {
        'app_title': 'Timer',
        'start': 'Start',
        'stop': 'Stop',
        'reset': 'Reset',
        'time_label': 'Duration (minutes):',
        'time_finished': 'Time\'s up!',
        'error_invalid_time': 'Please enter a valid duration!',
        'error_numeric_value': 'Please enter a numeric value!',
        'settings': 'Settings',
        'sound': 'Sound',
        'volume': 'Volume',
        'theme': 'Theme',
        'language': 'Language'
    }
    
    @classmethod
    def get_text(cls, key, language='tr'):
        """Dil metnini al"""
        if language == 'en':
            return cls.ENGLISH.get(key, key)
        else:
            return cls.TURKISH.get(key, key)
