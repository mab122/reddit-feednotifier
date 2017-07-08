#/bin/bash
# Very simple and stupid refreshing script.
while true; do
echo Refreshing
# Example subreddits. URLs are assumed to be safe
python main.py https://www.reddit.com/r/teslamotors/new/.rss
python main.py https://www.reddit.com/r/spacex/new/.rss
sleep 300 # 5 minutes * 60 seconds
done
