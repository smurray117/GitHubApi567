import requests
import json
import sys

def getRepos(user):
    repos = requests.get("https://api.github.com/users/%s/repos" % user)
    listRepos = list(map(lambda repo: repo['name'], repos.json()))
    return listRepos

def getCommits(user, repo):
    commits = requests.get("https://api.github.com/repos/%s/%s/commits" % (user, repo))
    numCommits = len(commits.json())
    return numCommits

def displayRepo(user, repo):
    return "Repo: %s Number of commits: %s" % (repo, getCommits(user, repo))

def main():
    repos = getRepos(sys.argv[1])
    for repo in repos:
        print(displayRepo(sys.argv[1], repo))
    

if __name__ == "__main__":
    main()
