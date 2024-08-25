from diagrams import Diagram
from diagrams.aws.network import ELB
from diagrams.onprem.client import User
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.queue import Rabbitmq
from diagrams.aws.compute import Lambda

with Diagram("msa_architecture", show=False):
    user = User("User")
    lb = ELB("Load Balancer")

    trip_service = Lambda("Trip Service")
    user_service = Lambda("User Service")
    payment_service = Lambda("Payment Service")

    trip_db = PostgreSQL("Trip DB")
    user_db = PostgreSQL("User DB")
    payment_db = PostgreSQL("Payment DB")

    broker = Rabbitmq("Message Broker")

    user >> lb >> trip_service
    user >> lb >> user_service
    user >> lb >> payment_service

    trip_service >> broker >> trip_db
    user_service >> broker >> user_db
    payment_service >> broker >> payment_db

