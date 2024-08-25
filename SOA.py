from diagrams import Diagram
from diagrams.aws.network import ELB
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Kafka

with Diagram("soa_architecture", show=False):
    user = User("User")
    lb = ELB("Load Balancer")
    esb = Kafka("ESB")

    trip_service = Server("Trip Service")
    user_service = Server("User Service")
    payment_service = Server("Payment Service")
    db = PostgreSQL("Database")

    user >> lb >> esb
    esb >> trip_service
    esb >> user_service
    esb >> payment_service

    trip_service >> db
    user_service >> db
    payment_service >> db
