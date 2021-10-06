from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.inmemory import Redis
from diagrams.programming.flowchart import Action, Delay

b = Edge(color = "darkblue")
g = Edge(color = "darkgreen")
p = Edge(color = "purple")

with Diagram("Evaluate Human Balance with Spark", direction="TB") as di:
    with Cluster("Streaming Application"):
        spark = Spark("Spark Streaming")
    with Cluster("Databases"):
        redis = Redis("Redis Database")
    with Cluster("Business Application"):
        business_app = Action("App")
    with Cluster("Kafka Topics"):
        gear_position = Delay("gear-position")
        vehicle_status = Delay("vehicle-status")
        vehicle_checkin = Delay("vehicle-checkin")
        redis_data = Delay("redis-data")
        checkin_status = Delay("checkin-status")
        bus_app_topics = [gear_position, vehicle_checkin, vehicle_status]

    business_app >>p>> redis >>p>> redis_data >>p>> spark
    spark>>g>>checkin_status>>g>>business_app
    business_app >>f>> bus_app_topics >>f>> spark
