install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

brain-calc:
	poetry run brain-calc

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

prompt:
	poetry add prompt

make lint:
	poetry run flake8 brain_games