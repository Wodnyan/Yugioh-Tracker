import os
from src import create_app

if __name__ == '__main__':
  app = create_app()
  # run app
  app.run(port=os.getenv('PORT'))
