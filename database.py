# import sqlalchemy
# print(sqlalchemy.__version__)
from sqlalchemy import create_engine ,text
import pymysql
import os

db_connection_string = os.environ['DB_CONNECTION_STRING'].strip('"')

engine = create_engine(db_connection_string,connect_args={
  "ssl": {
   "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result =conn.execute(text("select * from jobs"))
    jobs = []
    jobs = [dict(row._mapping) for row in result.all()]
  return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :id").bindparams(id=id)
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      row = rows[0]
      return dict(row._mapping)