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

all_clip_models = [{name:"RN50::openai",checked=True},
{name:"RN50::yfcc15m",checked=False},
{name:"RN50::cc12m",checked=False},
{name:"RN50-quickgelu::openai",checked=False},
{name:"RN50-quickgelu::yfcc15m",checked=False},
{name:"RN50-quickgelu::cc12m",checked=False},
{name:"RN101::openai",checked=False},        
{name:"RN101::yfcc15m",checked=False},       
{name:"RN101-quickgelu::openai",checked=False},          
{name:"RN101-quickgelu::yfcc15m",checked=False},         
{name:"RN50x4::openai",checked=False},        
{name:"RN50x16::openai",checked=False},       
{name:"RN50x64::openai",checked=False},       
{name:"ViT-B-32::openai",checked=True},      
{name:"ViT-B-32::laion2b_e16",checked=False}, 
{name:"ViT-B-32::laion400m_e31",checked=False},
{name:"ViT-B-32::laion400m_e32",checked=False},
{name:"ViT-B-32-quickgelu::openai",checked=False},
{name:"ViT-B-32-quickgelu::laion400m_e31",checked=False},
{name:"ViT-B-32-quickgelu::laion400m_e32",checked=False},
{name:"ViT-B-16::openai",checked=True},      
{name:"ViT-B-16::laion400m_e31",checked=False},          
{name:"ViT-B-16::laion400m_e32",checked=False},           
{name:"ViT-B-16-plus-240::laion400m_e31",checked=False},  
{name:"ViT-B-16-plus-240::laion400m_e32",checked=False},  
{name:"ViT-L-14::openai",checked=False},      
{name:"ViT-L-14-336::openai",checked=False}]
default_clip_models = ['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']


class DefaultSettings(FlaskForm):
    # description = TextAreaField('Course Description',
    #                             validators=[InputRequired(),
    #                                         Length(max=200)])
    batch_name = StringField('batch_name')
    batch_size = IntegerField('batch_size')
    clamp_grad = BooleanField('clamp_grad', default='checked')
    clamp_max = DecimalField('clamp_max')
    clip_denoised = BooleanField('clip_denoised')
    clip_guidance_scale = IntegerField('clip_guidance_scale')
    clip_models = SelectMultipleField('clip_models',
                       choices=all_clip_models,
                       default=default_clip_models)
    cut_ic_pow = DecimalField('cut_ic_pow')
    cut_icgray_p = StringField('cut_icgray_p')
    cut_innercut = StringField('cut_innercut')
    cut_overview = StringField('cut_overview')
    cutn_batches = IntegerField('cutn_batches')
    diffusion_model = StringField('diffusion_model')
    diffusion_sampling_mode = StringField('diffusion_sampling_mode')
    display_rate = IntegerField('display_rate')
    eta = DecimalField('eta')
    gif_fps = IntegerField('gif_fps')
    gif_size_ratio = DecimalField('gif_size_ratio')
    image_output = BooleanField('image_output', default='checked')
    init_scale = IntegerField('init_scale')
    n_batches = IntegerField('n_batches')
    name_docarray = StringField('name_docarray')
    on_misspelled_token = StringField('on_misspelled_token')
    perlin_init = BooleanField('perlin_init')
    perlin_mode = StringField('perlin_mode')
    rand_mag = DecimalField('rand_mag')
    randomize_class = BooleanField('randomize_class', default='checked')
    range_scale = IntegerField('range_scale')
    sat_scale = IntegerField('sat_scale')
    save_rate = IntegerField('save_rate')
    seed = StringField('seed')

    seed = StringField('seed')
    skip_steps = IntegerField('skip_steps')
    steps = IntegerField('steps')
    text_prompt = StringField('text_prompt')
    transformation_percent = DecimalField('transformation_percent')
    truncate_overlength_prompt = BooleanField('truncate_overlength_prompt')
    tv_s = DecimalField('tv_s')
    use_horizontal_symmetry = BooleanField('use_horizontal_symmetry')
    use_secondary_model = BooleanField('use_secondary_model',default='checked')
    use_vertical_symmetry = BooleanField('use_vertical_symmetry')
    visualize_cuts = BooleanField('visualize_cuts')
    width = IntegerField('width')
    height = IntegerField('height')

@app.route('/',methods=['GET'])
def index():
    session['batch_name'] ="DiscoTest"
    session['batch_size'] =1
    session['clamp_grad'] =True
    session['clamp_max'] =0.25
    session['clip_denoised'] =False
    session['clip_guidance_scale'] =14000
    session['clip_models'] =['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']
    session['clip_models_schedules'] =None 
    session['cut_ic_pow'] =1.0 
    session['cut_icgray_p'] ='[0.2]*400+[0]*600'
    session['cut_innercut'] ='[4]*400+[12]*600'
    session['cut_overview'] ='[12]*400+[4]*600'
    session['cut_schedules_group'] =None
    session['cutn_batches'] =4
    session['diffusion_model'] ='512x512_diffusion_uncond_finetune_008100'
    session['diffusion_model_config'] =None
    session['diffusion_sampling_mode'] ='ddim'
    session['display_rate'] =1
    session['eta'] =0.8 
    session['gif_fps'] =20
    session['gif_size_ratio'] =0.5
    session['image_output'] =True
    session['init_image'] =None
    session['init_scale'] =1000
    session['n_batches'] =4
    session['name_docarray'] ='discoart-0df4d0c8654811ed8b84c4bde571e200'
    session['on_misspelled_token'] ='ignore'
    session['perlin_init'] =False
    session['perlin_mode'] ='mixed'
    session['rand_mag'] =0.05
    session['randomize_class'] =True
    session['range_scale'] =150
    session['sat_scale'] =0
    session['save_rate'] =20
    session['seed'] =-1
    session['skip_event'] =None
    session['skip_steps'] =0
    session['steps'] =900
    session['stop_event'] =None
    session['text_clip_on_cpu'] =None
    session['text_prompt'] = ['A beautiful painting of a singular lighthouse, shining its light across a tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on artstation.', 'yellow color scheme']
    session['transformation_percent'] =[0.09]
    session['truncate_overlength_prompt'] =False
    session['tv_s'] =0
    session['use_horizontal_symmetry'] =False
    session['use_secondary_model'] =True
    session['use_vertical_symmetry'] =False
    session['visualize_cuts'] =False
    session['width_height'] =[1280, 768]
    print("session",session['tv_s'])
    return render_template('index.html', form = DefaultSettings())


@app.route('/startRender', methods=['POST'])
def startRender():
    for key in session:
        print(key)
        print(session[key])
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