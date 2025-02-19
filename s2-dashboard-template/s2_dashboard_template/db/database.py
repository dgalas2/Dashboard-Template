import singlestoredb as s2
import os
from dotenv import load_dotenv
from s2_dashboard_template.db import singleton
load_dotenv()

def getEnvName(env):
	if env=="" or env==None:
		return ""
	else:
		return env + "_"

def getConnectionString(env):
	connection_url = f'singlestoredb://{os.environ.get(getEnvName(env)+"DB_USER_NAME")}:{os.environ.get(getEnvName(env)+"DB_PASSWORD")}@{os.environ.get(getEnvName(env)+"DML_HOST")}:{os.environ.get(getEnvName(env)+"DML_PORT")}/{os.environ.get(getEnvName(env)+"DATABSE_NAME")}'
	return connection_url

class DB(metaclass=singleton.Singleton):
	def __init__(self,conn_url):
		self.conn = s2.connect(conn_url)
		self.cursor = self.conn.cursor()
	
	def getValues(self):
		self.cursor.execute('SELECT * FROM book')
		return self.cursor.fetchall()
