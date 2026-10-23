set -e

# python ./api/build_init_sql.py > ./db/init.sql

# Get the value of __version__ from secondbrain_server.__init__
version=$(grep -oE '__version__ *= *"[^"]+"' ./api/secondbrain_server/__init__.py | awk -F'"' '{print $2}')
echo "Version: $version"
echo "# Synced from backend ${version}" > ../client/secondbrain/core/blob.py
cat ./api/secondbrain_server/models/blob.py >> ../client/secondbrain/core/blob.py