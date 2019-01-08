"""Configurations Module for the Questioner REST API."""

class Config():
    """Base Configurations Class."""
    DEBUG = False

class DevelopmentConfig(Config):
    """Development Configurations Class."""
    DEBUG = True

