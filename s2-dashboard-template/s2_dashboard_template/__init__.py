from dashboard.dashboard import getDashboardApp
from singlestoredb.apps import run_dashboard_app
import asyncio

'''
Using dotenv package to access variables in .env file
'''
from dotenv import load_dotenv
load_dotenv()
'''
Main File to run your dashboard apps
All enviornment variables can be accessed using os.getenv('VARIABLE_NAME')
'''
async def main():
	print('This is main')
	dashboard = getDashboardApp()
	await run_dashboard_app(dashboard)

if __name__ == "__main__":
	asyncio.run(main())