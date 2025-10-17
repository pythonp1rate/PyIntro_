Cheat sheet for git handling of forks:

If you have a repo locally, that's a clone of a forked repo,
, run the below four commands to fetch changes from the 
original repo, merge them into your local main branch, and push them to your forked repo.

git fetch upstream
git checkout main
git merge upstream/main
git push origin main