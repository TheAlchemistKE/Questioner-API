"""Configurations Module for the Questioner REST API."""

class Config():
    """Base Configurations Class."""
    DEBUG = False

class DevelopmentConfig(Config):
    """Development Phase Configurations Class."""
    DEBUG = True

class TestingConfig(Config):
    """Testing Phase Configurations Clas"""
    DEBUG = True
    TESTING = True
