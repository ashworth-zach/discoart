from flask import Flask, redirect, render_template, request, flash, session
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, DecimalField,SelectMultipleField)
from wtforms.validators import InputRequired, Length
import datetime
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

queue = []; #first in first out

default_clip_models = ['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']


defaults = {}
defaults['batch_name'] ="DiscoTest"
defaults['batch_size'] =1
defaults['clamp_grad'] =True
defaults['clamp_max'] =0.25
defaults['clip_denoised'] =False
defaults['clip_guidance_scale'] =14000
defaults['clip_models'] =['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']
defaults['clip_models_schedules'] =None 
defaults['cut_ic_pow'] =1.0 
defaults['cut_icgray_p'] ='[0.2]*400+[0]*600'
defaults['cut_innercut'] ='[4]*400+[12]*600'
defaults['cut_overview'] ='[12]*400+[4]*600'
defaults['cut_schedules_group'] =None
defaults['cutn_batches'] =4
defaults['diffusion_model'] ='512x512_diffusion_uncond_finetune_008100'
defaults['diffusion_model_config'] =None
defaults['diffusion_sampling_mode'] ='ddim'
defaults['display_rate'] =1
defaults['eta'] =0.8 
defaults['gif_fps'] =20
defaults['gif_size_ratio'] =0.5
defaults['image_output'] =True
defaults['init_image'] =None
defaults['init_scale'] =1000
defaults['n_batches'] =4
defaults['name_docarray'] ='discoart-0df4d0c8654811ed8b84c4bde571e200'
defaults['on_misspelled_token'] ='ignore'
defaults['perlin_init'] =False
defaults['perlin_mode'] ='mixed'
defaults['rand_mag'] =0.05
defaults['randomize_class'] =True
defaults['range_scale'] =150
defaults['sat_scale'] =0
defaults['save_rate'] =20
defaults['seed'] =-1
defaults['skip_event'] =None
defaults['skip_steps'] =0
defaults['steps'] =900
defaults['stop_event'] =None
defaults['text_clip_on_cpu'] =None
defaults['text_prompt'] = ['A beautiful painting of a singular lighthouse, shining its light across a tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on artstation.', 'yellow color scheme']
defaults['transformation_percent'] =[0.09]
defaults['truncate_overlength_prompt'] =False
defaults['tv_s'] =0
defaults['use_horizontal_symmetry'] =False
defaults['use_secondary_model'] =True
defaults['use_vertical_symmetry'] =False
defaults['visualize_cuts'] =False
defaults['width_height'] =[1280, 768]


class DefaultSettings(FlaskForm):
    # description = TextAreaField('Course Description',
    #                             validators=[InputRequired(),
    #                                         Length(max=200)])
    batch_name = StringField('batch_name', default=defaults['batch_name'])
    batch_size = IntegerField('batch_size', default=defaults['batch_size'])
    clamp_grad = BooleanField('clamp_grad', default='checked')
    clamp_max = DecimalField('clamp_max', default=defaults['clamp_max'])
    clip_denoised = BooleanField('clip_denoised', default=defaults['clip_denoised'])
    clip_guidance_scale = IntegerField('clip_guidance_scale', default=defaults['clip_guidance_scale'])

    clip_model0 = BooleanField("clip_model0", default='checked') #RN50::openai 
    clip_model1 = BooleanField("clip_model1") #RN50::yfcc15m
    clip_model2 = BooleanField("clip_model2") #RN50::cc12m
    clip_model3 = BooleanField("clip_model3") #RN50-quickgelu::openai
    clip_model4 = BooleanField("clip_model4") #RN50-quickgelu::yfcc15m
    clip_model5 = BooleanField("clip_model5") #RN50-quickgelu::cc12m
    clip_model6 = BooleanField("clip_model6") #RN101::openai
    clip_model7 = BooleanField("clip_model7") #RN101::yfcc15m   
    clip_model8 = BooleanField("clip_model8") #RN101-quickgelu::openai      
    clip_model9 = BooleanField("clip_model9") #RN101-quickgelu::yfcc15m      
    clip_model10 = BooleanField("clip_model10") #RN50x4::openai      
    clip_model11 = BooleanField("clip_model11") #RN50x16::openai     
    clip_model12 = BooleanField("clip_model12") #RN50x64::openai     
    clip_model13 = BooleanField("clip_model13", default='checked') #ViT-B-32::openai    
    clip_model14 = BooleanField("clip_model14") #ViT-B-32::laion2b_e16
    clip_model15 = BooleanField("clip_model15") #ViT-B-32::laion400m_e31
    clip_model16 = BooleanField("clip_model16") #ViT-B-32::laion400m_e32
    clip_model17 = BooleanField("clip_model17") #ViT-B-32-quickgelu::openai
    clip_model18 = BooleanField("clip_model18") #ViT-B-32-quickgelu::laion400m_e31
    clip_model19 = BooleanField("clip_model19") #ViT-B-32-quickgelu::laion400m_e32
    clip_model20 = BooleanField("clip_model20", default='checked') #ViT-B-16::openai    
    clip_model21 = BooleanField("clip_model21") #ViT-B-16::laion400m_e31        
    clip_model22 = BooleanField("clip_model22") #ViT-B-16::laion400m_e32        
    clip_model23 = BooleanField("clip_model23") #ViT-B-16-plus-240::laion400m_e31
    clip_model24 = BooleanField("clip_model24") #ViT-B-16-plus-240::laion400m_e32
    clip_model25 = BooleanField("clip_model25") #ViT-L-14::openai    
    clip_model26 = BooleanField("clip_model26") #ViT-L-14-336::opena
    cut_ic_pow = DecimalField('cut_ic_pow', default=defaults['cut_ic_pow'])
    cut_icgray_p = StringField('cut_icgray_p', default=defaults['cut_icgray_p'])
    cut_innercut = StringField('cut_innercut', default=defaults['cut_innercut'])
    cut_overview = StringField('cut_overview', default=defaults['cut_overview'])
    cutn_batches = IntegerField('cutn_batches', default=defaults['cutn_batches'])
    diffusion_model = StringField('diffusion_model', default=defaults['diffusion_model'])
    diffusion_sampling_mode = StringField('diffusion_sampling_mode', default=defaults['diffusion_sampling_mode'])
    display_rate = IntegerField('display_rate', default=defaults['display_rate'])
    eta = DecimalField('eta', default=defaults['eta'])
    gif_fps = IntegerField('gif_fps', default=defaults['gif_fps'])
    gif_size_ratio = DecimalField('gif_size_ratio', default=defaults['gif_size_ratio'])
    image_output = BooleanField('image_output', default='checked')
    init_scale = IntegerField('init_scale', default=defaults['init_scale'])
    n_batches = IntegerField('n_batches', default=defaults['n_batches'])
    name_docarray = StringField('name_docarray', default=defaults['name_docarray'])
    on_misspelled_token = StringField('on_misspelled_token', default=defaults['on_misspelled_token'])
    perlin_init = BooleanField('perlin_init', default=defaults['perlin_init'])
    perlin_mode = StringField('perlin_mode', default=defaults['perlin_mode'])
    rand_mag = DecimalField('rand_mag', default=defaults['rand_mag'])
    randomize_class = BooleanField('randomize_class', default='checked')
    range_scale = IntegerField('range_scale', default=defaults['range_scale'])
    sat_scale = IntegerField('sat_scale', default=defaults['sat_scale'])
    save_rate = IntegerField('save_rate', default=defaults['save_rate'])
    seed = StringField('seed', default=defaults['seed'])
    skip_steps = IntegerField('skip_steps', default=defaults['skip_steps'])
    steps = IntegerField('steps', default=defaults['steps'])
    text_prompt = TextAreaField('text_prompt', default=defaults['text_prompt'])
    transformation_percent = DecimalField('transformation_percent', default=defaults['transformation_percent'])
    truncate_overlength_prompt = BooleanField('truncate_overlength_prompt', default=defaults['truncate_overlength_prompt'])
    tv_s = DecimalField('tv_s', default=defaults['tv_s'])
    use_horizontal_symmetry = BooleanField('use_horizontal_symmetry', default=defaults['use_horizontal_symmetry'])
    use_secondary_model = BooleanField('use_secondary_model',default='checked')
    use_vertical_symmetry = BooleanField('use_vertical_symmetry', default=defaults['use_vertical_symmetry'])
    visualize_cuts = BooleanField('visualize_cuts', default=defaults['visualize_cuts'])
    width = IntegerField('width', default=1280)
    height = IntegerField('height', default=768)

@app.route('/',methods=['GET'])
def index():
    print("session",session['tv_s'])
    return render_template('index.html', form = DefaultSettings(), defaults=defaults)


@app.route('/AddRender', methods=['POST'])
def startRender():
    print(request.form)
    newObject = []
    for key in request.form:
        if(request.form[key]=='y'):
            newObject.append((key,True))
        else:
            newObject.append((key,request.form[key]))

        print(key)
        print(request.form[key])
    for key in newObject:
        print(key)
        print(newObject[key])
    return render_template('rendering.html',form=DefaultSettings())

    
if __name__ == "__main__":
    app.run(debug=True)




# // |                    DEFAULT | SETTINGS 
# // |                 batch_name │ None                                                                               │
# // │                 batch_size │ 1                                                                                  │
# // │                 clamp_grad │ True                                                                               │
# // │                  clamp_max │ 0.05                                                                               │
# // │              clip_denoised │ False                                                                              │
# // │        clip_guidance_scale │ 5000                                                                               │
# // │                clip_models │ ['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']                           │
# // │      clip_models_schedules │ None                                                                               │
# // │                 cut_ic_pow │ 1.0                                                                                │
# // │               cut_icgray_p │ [0.2]*400+[0]*600                                                                  │
# // │               cut_innercut │ [4]*400+[12]*600                                                                   │
# // │               cut_overview │ [12]*400+[4]*600                                                                   │
# // │        cut_schedules_group │ None                                                                               │
# // │               cutn_batches │ 4                                                                                  │
# // │            diffusion_model │ 512x512_diffusion_uncond_finetune_008100                                           │
# // │     diffusion_model_config │ None                                                                               │
# // │    diffusion_sampling_mode │ ddim                                                                               │
# // │               display_rate │ 1                                                                                  │
# // │                        eta │ 0.8                                                                                │
# // │                    gif_fps │ 20                                                                                 │
# // │             gif_size_ratio │ 0.5                                                                                │
# // │               image_output │ True                                                                               │
# // │                 init_image │ None                                                                               │
# // │                 init_scale │ 1000                                                                               │
# // │                  n_batches │ 4                                                                                  │
# // │             name_docarray* │ discoart-0df4d0c8654811ed8b84c4bde571e200                                          │
# // │        on_misspelled_token │ ignore                                                                             │
# // │                perlin_init │ False                                                                              │
# // │                perlin_mode │ mixed                                                                              │
# // │                   rand_mag │ 0.05                                                                               │
# // │            randomize_class │ True                                                                               │
# // │                range_scale │ 150                                                                                │
# // │                  sat_scale │ 0                                                                                  │
# // │                  save_rate │ 20                                                                                 │
# // │                      seed* │ 4088028464                                                                         │
# // │                 skip_event │ None                                                                               │
# // │                 skip_steps │ 0                                                                                  │
# // │                      steps │ 250                                                                                │
# // │                 stop_event │ None                                                                               │
# // │           text_clip_on_cpu │ False                                                                              │
# // │               text_prompts │ ['A beautiful painting of a singular lighthouse, shining its light across a        │
# // │                            │ tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on          │
# // │                            │ artstation.', 'yellow color scheme']                                               │
# // │     transformation_percent │ [0.09]                                                                             │
# // │ truncate_overlength_prompt │ False                                                                              │
# // │                   tv_scale │ 0                                                                                   │
# // │    use_horizontal_symmetry │ False                                                                              │
# // │        use_secondary_model │ True                                                                               │
# // │      use_vertical_symmetry │ False                                                                              │
# // │             visualize_cuts │ False                                                                              │
# // │               width_height │ [1280, 768]    

# dataObject = {
#     "batch_name":"DiscoTest",
#     "batch_size":1,
#     "clamp_grad":True,
#     "clamp_max":0.25,
#     "clip_denoised":False,
#     "clip_guidance_scale":14000,
#     "clip_models":['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai'],
#     "clip_models_schedules":None ,
#     "cut_ic_pow":1.0 ,
#     "cut_icgray_p":'[0.2]*400+[0]*600',
#     "cut_innercut":'[4]*400+[12]*600',
#     "cut_overview":'[12]*400+[4]*600',
#     "cut_schedules_group":None,
#     "cutn_batches":4,
#     "diffusion_model":'512x512_diffusion_uncond_finetune_008100',
#     "diffusion_model_config":None,
#     "diffusion_sampling_mode":'ddim',
#     "display_rate":1,
#     "eta":0.8 ,
#     "gif_fps":20,
#     "gif_size_ratio":0.5,
#     "image_output":True,
#     "init_image":None,
#     "init_scale":1000,
#     "n_batches":4,
#     "name_docarray":'discoart-0df4d0c8654811ed8b84c4bde571e200',
#     "on_misspelled_token":'ignore',
#     "perlin_init":False,
#     "perlin_mode":'mixed',
#     "rand_mag":0.05,
#     "randomize_class":True,
#     "range_scale":150,
#     "sat_scale":0,
#     "save_rate":20,
#     "seed":-1,
#     "skip_event":None,
#     "skip_steps":0,
#     "steps":900,
#     "stop_event":None,
#     "text_clip_on_cpu":None,
#     "text_prompt":['A beautiful painting of a singular lighthouse, shining its light across a tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on artstation.', 'yellow color scheme']  ,
#     "transformation_percent":[0.09],
#     "truncate_overlength_prompt":False,
#     "tv_s":0,
#     "use_horizontal_symmetry":False,
#     "use_secondary_model":True,
#     "use_vertical_symmetry":False,
#     "visualize_cuts":False,
#     "width_height":[1280, 768]   
# }

# "RN50::openai",
# "RN50::yfcc15m",
# "RN50::cc12m",
# "RN50-quickgelu::openai",
# "RN50-quickgelu::yfcc15m",
# "RN50-quickgelu::cc12m"",
# "RN101::openai"",        
# "RN101::yfcc15m"",       
# "RN101-quickgelu::openai"          
# "RN101-quickgelu::yfcc15m"         
# "RN50x4::openai",        
# "RN50x16::openai",       
# "RN50x64::openai",       
# "ViT-B-32::openai",      
# "ViT-B-32::laion2b_e16", 
# "ViT-B-32::laion400m_e31",
# "ViT-B-32::laion400m_e32",
# "ViT-B-32-quickgelu::openai",
# "ViT-B-32-quickgelu::laion400m_e31",
# "ViT-B-32-quickgelu::laion400m_e32",
# "ViT-B-16::openai",      
# "ViT-B-16::laion400m_e31",          
# "ViT-B-16::laion400m_e32",           
# "ViT-B-16-plus-240::laion400m_e31",  
# "ViT-B-16-plus-240::laion400m_e32",  
# "ViT-L-14::openai",      
# "ViT-L-14-336::openai"

