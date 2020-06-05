from flask import Flask, request, url_for, render_template
from flask_pymongo import PyMongo

app =Flask(__name__)
app.config['MONGO_URI'] ='mongodb+srv://upload_img:upload_img@cluster0-yru0g.mongodb.net/img_collection?retryWrites=true&w=majority'
mongo = PyMongo(app)
#set FLASK_ENV = development
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username' : request.form.get('username'), 'profile_image_name':profile_image.filename})
    return 'Done!!!!!!!!'

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)
img_data = {}
@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.users.find_one_or_404({'username': username})
    # print("user is", user)
    # user_data = [item for item,v in user.items()]
    # print('user',user_data)
    # for u in user_data:
    #     img =list(mongo.db.users.find({'username':u}))
    # print('img is',img)
    # img_data = {item['profile_image_name'] for item in img}
    # print("Total images are",img_data)
    for i in range(4):
        return f'''
                <h1>{username}</h1>
                
                <img  src="{url_for('file', filename = user['profile_image_name'])}" width="300" height="200">

            '''
    
    #return render_template('images.html',user = user,username=username)

if __name__ == '__main__':
    app.run(debug=True)
