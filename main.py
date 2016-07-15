from git import Repo
from time import gmtime, strftime
import sys

if len(sys.argv) < 2:
    print "Use: python main.py <repos_path>"
    sys.exit(1)
repo_path = sys.argv[1]
repo = Repo(repo_path)
tags = []
for tag in repo.tags:
    commit = tag.commit
    obj = {
        "tag": tag,
        "author": commit.author,
        "date": strftime("%Y-%m-%d", gmtime(commit.committed_date)),
        "message": commit.message
    }
    tags.append(obj)

changelog = """
# Change Log
All notable changes to this project will be documented in this file.
This project adheres to to [Semantic Versioning](http://semver.org/).

"""
tags.reverse()
for tag in tags:
    entry = "## [{version}] - {date}\n{message}\n".format(
        version=str(tag["tag"]),
        date=tag["date"],
        message=tag["message"])
    changelog += entry

print changelog
