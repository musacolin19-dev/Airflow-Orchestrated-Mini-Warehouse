# Airflow-Orchestrated Mini Warehouse

A batch ELT example with an actual Apache Airflow DAG for extracting staged CSV orders, loading a SQLite warehouse, and building a daily revenue mart. All tasks are independently executable, making local tests possible without an Airflow installation. Add Airflow to run scheduled DAGs; the local driver proves the transformations work.

## Quick start

```bash
python warehouse.py
python -m unittest discover -s tests -v
# optional: install Apache Airflow separately, then place dags/orders_dag.py in its DAG folder
```

## Architecture and scope

SQL warehouse uses SQLite for a no-account demo; production Airflow deployment and managed warehouse integration are separate exercises.

**Portfolio note:** Original educational starter code, not a production deployment. Use only synthetic/public datasets, document your own extensions, and test integrations before claiming production experience.
