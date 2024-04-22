deploy-default:
	gcloud app deploy app.yaml --no-cache --promote --version=default1

deploy-queue:
	gcloud app deploy queue.yaml