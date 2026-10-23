set -e
rm -rf ./db/dev_data
rm -rf ./db/dev_redis
DATABASE_LOCATION="./db/dev_data" REDIS_LOCATION="./db/dev_redis" docker compose up secondbrain-server-db secondbrain-server-redis
rm -rf ./db/dev_data
rm -rf ./db/dev_redis