from flask import Flask, redirect, render_template, request, flash, session
import datetime
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

queue = []; #first in first out

dataObject = {
    "batch_name":"DiscoTest",
    "batch_size":1,
    "clamp_grad":True,
    "clamp_max":0.25,
    "clip_denoised":False,
    "clip_guidance_scale":14000,
    "clip_models":['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai'],
    "clip_models_schedules":None ,
    "cut_ic_pow":1.0 ,
    "cut_icgray_p":'[0.2]*400+[0]*600',
    "cut_innercut":'[4]*400+[12]*600',
    "cut_overview":'[12]*400+[4]*600',
    "cut_schedules_group":None,
    "cutn_batches":4,
    "diffusion_model":'512x512_diffusion_uncond_finetune_008100',
    "diffusion_model_config":None,
    "diffusion_sampling_mode":'ddim',
    "display_rate":1,
    "eta":0.8 ,
    "gif_fps":20,
    "gif_size_ratio":0.5,
    "image_output":True,
    "init_image":None,
    "init_scale":1000,
    "n_batches":4,
    "name_docarray":'discoart-0df4d0c8654811ed8b84c4bde571e200',
    "on_misspelled_token":'ignore',
    "perlin_init":False,
    "perlin_mode":'mixed',
    "rand_mag":0.05,
    "randomize_class":True,
    "range_scale":150,
    "sat_scale":0,
    "save_rate":20,
    "seed":-1,
    "skip_event":None,
    "skip_steps":0,
    "steps":900,
    "stop_event":None,
    "text_clip_on_cpu":None,
    "text_prompt":['A beautiful painting of a singular lighthouse, shining its light across a tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on artstation.', 'yellow color scheme']  ,
    "transformation_percent":[0.09],
    "truncate_overlength_prompt":False,
    "tv_s":0,
    "use_horizontal_symmetry":False,
    "use_secondary_model":True,
    "use_vertical_symmetry":False,
    "visualize_cuts":False,
    "width_height":[1280, 768]   
}


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
    return render_template('index.html')


@app.route('/startRender', methods=['POST'])
def startRender():
    for key in session:
        print(key)
    return render_template('rendering.html')

    
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