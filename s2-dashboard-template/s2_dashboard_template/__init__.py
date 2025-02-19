from s2_dashboard_template.dashboard.dashboard import getDashboardApp
import asyncio
import os
from s2_dashboard_template.db import database
from singlestoredb.apps import run_dashboard_app

# if you do not want to use different db for different env, just set env = "",
# OR do not set variable ENV in .env file
from dotenv import load_dotenv
load_dotenv()
env = os.environ.get('ENV')
connection_url = database.getConnectionString(env)

# only one DB connection string can exist in OS at one time. TODO: change it such that we can use multiple, thus being able to run multiple projects together on local
os.environ["SINGLESTOREDB_URL"] = connection_url
os.environ["DATABASE_URL"] = connection_url


# db = database.DB(connection_url)	

def main():
	
	print('This is main')
	dashboard = getDashboardApp()
	asyncio.run(run_dashboard_app(dashboard))

if __name__ == "__main__":
	main()
