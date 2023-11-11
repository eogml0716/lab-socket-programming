from flask import Flask, json
from flask_restful import Resource, Api
import os
import subprocess  # subprocess 모듈 추가

buildBranch = 'master'
buildPath = '/home/eogml1755/lab-socket-programming/'

# buildCommand 대신 subprocess.run을 사용
def git_pull():
    os.chdir(buildPath)  # 작업 디렉토리 변경
    subprocess.run(['git', 'stash'])  # git stash 실행
    subprocess.run(['git', 'pull', 'origin', buildBranch])  # git pull 실행

app = Flask(__name__)
api = Api(app)

class SetDeploy(Resource):
    def post(self):
        git_pull()
        return {'status': 'success'}

api.add_resource(SetDeploy, '/deploy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# from flask import Flask, json
# from flask_restful import Resource, Api
#
# import os
#
# buildBranch = 'master'
# buildPath = '/home/ubuntu/lab-socket-programming/'
#
# buildCommand = 'cd ' + buildPath + ' && git stash && git pull origin ' + buildPath
#
# app = Flask(__name__)
# api = Api(app)
#
# class setDeploy(Resource):
#     def post(self):
#         os.system(buildCommand)
#         return {'status' : 'success'}
#
# api.add_resource(setDeploy, '/deploy')
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
