from flask import Flask
from flask_restful import Api
from resources.emp import Profile,Clubdelete,Clubnames,Displaypostevents,Login,Adminlog,Requesttoclub,Clubmembers,Addclub,Forgotpassword,Allclubdetails,Changepassword,Addclubmembers
from flask_jwt_extended import JWTManager

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY']='coscskillup'
api=Api(app)
jwt=JWTManager(app)
api.add_resource(Addclub,'/addclub')
api.add_resource(Profile,'/profile')
api.add_resource(Clubdelete,'/del')
api.add_resource(Clubnames,'/clubnames')
api.add_resource(Login,'/login')
api.add_resource(Allclubdetails,'/allclub')
api.add_resource(Addclubmembers,'/addclubmembers')
api.add_resource(Changepassword,'/changepassword')
api.add_resource(Forgotpassword,'/forgotpassword')
api.add_resource(Clubmembers,'/clubmembers')
api.add_resource(Requesttoclub,'/requesttoclub')
api.add_resource(Adminlog,'/adminlog')
api.add_resource(Displaypostevents,'/displaypostevents')

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401



if __name__=='__main__':
    app.run()