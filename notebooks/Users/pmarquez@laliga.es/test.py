# Databricks notebook source
# MAGIC %sh
# MAGIC pip list

# COMMAND ----------

account_name = "ll1preunedlsdatalake"
tenant_id= "b4773745-cf27-4bf6-a0d2-75b1a79a457c"
adls, ala = datalake.authenticate_user(tenant_id, account_name)
