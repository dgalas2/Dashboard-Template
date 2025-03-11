from s2_dashboard_template.dashboard.dashboard import getDashboardApp
import asyncio
import os
from s2_dashboard_template.db import database
from singlestoredb.apps import run_dashboard_app

# if you do not want to use different db for different env, just set env = "",
# OR do not set variable ENV in .env file
from dotenv import load_dotenv
load_dotenv(".env")
env = os.environ.get('ENV')
connection_url = database.getConnectionString(env)

# only one DB connection string can exist in OS at one time. TODO: change it such that we can use multiple, thus being able to run multiple projects together on local
os.environ["SINGLESTOREDB_URL"] = connection_url
os.environ["DATABASE_URL"] = connection_url


# db = database.DB(connection_url)	

# add all setup code that will be used by the app in this function as this will be called on the platform
async def run_app():
	dashboard = getDashboardApp()
	await run_dashboard_app(dashboard)


# only add code that is required for local. It will not be run on platform
def main():
	
	print('This is main')
	
	asyncio.run(run_app())

if __name__ == "__main__":
	main()
