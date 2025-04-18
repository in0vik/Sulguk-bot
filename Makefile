.PHONY: setup run test deploy-gcloud clean

setup:
	pip install -r requirements.txt

run:
	python main.py

test:
	python test_sulguk.py

deploy-gcloud:
	gcloud builds submit --tag gcr.io/$$(gcloud config get-value project)/tg-html-bot
	gcloud run deploy tg-html-bot \
		--image gcr.io/$$(gcloud config get-value project)/tg-html-bot \
		--platform managed \
		--allow-unauthenticated

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete 