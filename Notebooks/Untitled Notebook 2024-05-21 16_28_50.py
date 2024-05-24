# Databricks notebook source
# MAGIC %sql
# MAGIC declare or replace variable Description default '';
# MAGIC set var Description=' Consult for laparoscopic gastric bypass.'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM identifier('john_snow_labs_medical_transcription.medical_transcription.medical_transcription_samples')
# MAGIC WHERE Description = Description

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE STREAMING TABLE app_usage_cleaned_2 AS
# MAGIC SELECT * FROM STREAM(LIVE.app_usage)
