from diagrams import Diagram, Edge
from diagrams.aws.network import ELB
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

with Diagram("monolithic_architecture", show=False):
    user = User("User")
    lb = ELB("Load Balancer")
    monolith = Server("Monolithic App")
    db = PostgreSQL("Database")

    user >> lb >> monolith
    monolith >> db
