

.PHONY: test-run-backend
test-run-backend:
	rm -rf ./environment/frontend_server/storage/simulation-test
	./run_backend.sh base_the_ville_isabella_maria_klaus simulation-test
