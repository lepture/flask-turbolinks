.PHONY: clean-pyc clean-build docs

lint:
	@flake8

test:
	@nosetests -s

coverage:
	@rm -f .coverage
	@nosetests --with-coverage --cover-package=flask_turbolinks --cover-html

clean: clean-build clean-pyc clean-docs


clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info


clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-docs:
	@rm -fr  docs/_build

docs:
	@$(MAKE) -C docs html

js:
	@curl https://raw.github.com/rails/turbolinks/master/lib/assets/javascripts/turbolinks.js.coffee -o vendor/turbolinks.js.coffee
	@coffee -b -c -p vendor/turbolinks.js.coffee > index.js
	@sed -i .bak 's/this\.Turbolinks/module.exports/' index.js
