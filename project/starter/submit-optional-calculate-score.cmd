docker exec -it spark-streaming_spark-worker-1_1 /opt/bitnami/spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0 /home/workspace/project/starter/sparkpyoptionalriskcalculation.py | tee ../../spark/logs/optional-score.log 