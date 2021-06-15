db_name=quiz_db
set_up_file=set_up.py
populating_file=populate.sql
py=python
app=server.py
rds=sqlite3


all: run

run:
	@clear
	@$(py) $(app)

clean:
	@echo "Cleaning"
	@rm -f $(db_name)
	@echo "Done!"

setup: clean
	@echo "Setting up database and tables"
	@$(py) $(set_up_file)
	@echo "Done!!"

test: setup
	@echo "Running unittest"
	@$(py) -m unittest discover test
	@echo "Done!!!"
	@echo "run make, or make run to execute the application."

populate: setup
	@echo "Populate database tables with some pre-defined data to work with."
	@$(rds) $(db_name) < $(populating_file)
	@echo "Done!!!"

