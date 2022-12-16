from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if (f.filename == ''):
            return redirect('/', code=302)
        if not f.filename.endswith('.h5'):
            return redirect('/', code=302)
        filename = secure_filename(f.filename)
        f.save('tmp/' + filename)
        v1 = tf.Variable(5, name='v1')
        v2 = tf.Variable(6, name='v2')
        saver = tf.compat.v1.train.Saver([v1, v2])
#        model = keras.Model.load_model('tmp/' + filename)
        model = load_model('tmp/' + filename)
        sess = keras.backend.get_session()
        saver.save(sess, 'tmp/' + filename + '.ckpt')
        return "Okay - " + filename
    else:
        return redirect('/', code=302)
app.run()