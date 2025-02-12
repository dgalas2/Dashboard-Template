from dashboard.dashboard import getDashboardApp
from singlestoredb.apps import run_dashboard_app
import asyncio
'''
Main File to run your dashboard apps
'''
async def main():
	print('This is main')
	dashboard = getDashboardApp()
	await run_dashboard_app(dashboard)

if __name__ == "__main__":
	asyncio.run(main())