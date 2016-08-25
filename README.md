# AWS lambda(python) via apex

# pip & deploy
1. Export package list at functions/<hogehoge>/ dir
`pip freeze > requirement.txt`

2. apex hook call `pip --install -r requirement.txt` when `apex deploy`

# local execution
`mayn.py < ../../events/test.json`
