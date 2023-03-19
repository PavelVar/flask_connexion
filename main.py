import connexion
from flask import app


def init_app():
    app = connexion.App(__name__, specification_dir='./')

    app.add_api('swagger.yml')

    # def startup():
    #     start_logging()
    #     get_or_create_engine()
    #
    # def shutdown():
    #     await dispose_engine()
    #
    return app


if __name__ == '__main__':
    app = init_app()
    app.run(debug=True)
