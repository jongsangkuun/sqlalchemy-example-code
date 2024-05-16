from sqlalchemy.orm import sessionmaker
import utils.config
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from typing import Type, Dict, List, Optional, Union
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database:
    def __init__(self, config_type: str):
        if config_type is not None:
            config_reader = utils.config.IniReader().get_section_data("database")
        else:
            config_reader = utils.config.IniReader().get_section_data(config_type)

        db_url = URL.create(
            drivername="postgresql",
            username=config_reader["user"],
            password=config_reader["passwd"],
            host=config_reader["host"],
            database=config_reader["name"],
            port=config_reader["port"],
        )

        self.engine = create_engine(db_url)

        self.connection = self.engine.connect()

        self.Session = sessionmaker(bind=self.engine)

    def search_one(
        self, table: Type[DeclarativeMeta], **kwargs
    ) -> Optional[DeclarativeMeta]:

        session = self.Session()

        try:
            return session.query(table).filter_by(**kwargs).first()
        finally:
            session.close()

    def search_many(
        self, table: Type[DeclarativeMeta], limit: int = None, **kwargs
    ) -> list[Dict]:

        session = self.Session()

        try:
            query = session.query(table).filter_by(**kwargs)
            if limit is not None:
                query = query.limit(limit)
            results = query.all()
            return [to_dict(result) for result in results]

        finally:
            session.close()

    def insert_one(self, data: Dict, table: Type[DeclarativeMeta]):
        # data parameter should be a database model instance
        # table parameter is the table (model class) where you want to insert the data
        # Create a new session
        session = self.Session()

        try:
            # Create an instance of the
            # 'table' class with the provided 'data'
            record = table(**data)

            # Add the record to the session
            session.add(record)

            # Commit the session to the database
            session.commit()

            print("Data inserted successfully")
        except Exception as e:
            # If there was an exception, roll back the changes
            session.rollback()
            print("Failed to insert data")
            print(e)
        finally:
            # Ensure the session is closed
            session.close()

    def insert_many(self, data: List[Dict], table: Type[DeclarativeMeta]):
        session = self.Session()

        try:
            # Create a list of 'table' instances
            records = [table(**item) for item in data]

            # Add all the records to the session
            session.add_all(records)

            # Commit the session to the database
            session.commit()

            print("Data inserted successfully")
        except Exception as e:
            # If there was an error, roll back the session
            session.rollback()

            print("Failed to insert data")
            print(e)
        finally:
            # Ensure the session is closed
            session.close()

    def update_records(
        self,
        table: Type[DeclarativeMeta],
        update_data: Dict,
        filter_by: Union[Dict, List[Dict]],
    ):
        session = self.Session()

        try:
            filter_by_list = filter_by if isinstance(filter_by, list) else [filter_by]

            for filter_by in filter_by_list:
                # Get the records
                records = session.query(table).filter_by(**filter_by)

                # If no records found for a filter, print and continue to next filter
                if records.count() == 0:
                    print(f"No record found to update for filter {filter_by}")
                    continue

                # Update each record found
                for record in records:
                    for key, value in update_data.items():
                        setattr(record, key, value)

            # Commit the changes
            session.commit()

            print("Data updated successfully")
        except Exception as e:
            # If there was an exception, rollback the changes
            session.rollback()
            print("Failed to update data")
            print(e)
        finally:
            # Always ensure the session is closed
            session.close()

    def delete_records(
        self, table: Type[DeclarativeMeta], filter_by: Union[Dict, List[Dict]]
    ):
        session = self.Session()

        try:
            filter_by_list = filter_by if isinstance(filter_by, list) else [filter_by]

            for _filter in filter_by_list:
                records = session.query(table).filter_by(**_filter).all()

                if not records:
                    print(f"No record found to delete for filter {_filter}")
                    continue

                for record in records:
                    session.delete(record)

            session.commit()

            print("Data deleted successfully")
        except Exception as e:
            session.rollback()
            print("Failed to delete data")
            print(e)
        finally:
            session.close()


def to_dict(model_instance):
    return {
        c.name: getattr(model_instance, c.name)
        for c in model_instance.__table__.columns
    }
