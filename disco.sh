
# just a small note
# i think I wasted my time making this
# I wont be using it
# i think i can just directly call the python script from within main.js when the user adds the item to the queue



while getopts batch_name:batch_size:clamp_grad:clamp_max:clip_denoised:clip_guidance_scale:clip_models:clip_models_schedules:cut_ic_pow:cut_icgray_p:cut_innercut:cut_overview:cut_schedules_group:cutn_batches:diffusion_model:diffusion_model_config:diffusion_sampling_mode:display_rate:eta:gif_fps:gif_size_ratio:image_output:init_image:init_scale:n_batches:name_docarray:on_misspelled_token:perlin_init:perlin_mode:rand_mag:randomize_class:range_scale:sat_scale:save_rate:seed:skip_event:skip_steps:steps:stop_event:text_clip_on_cpu:text_prompt:transformation_percent:truncate_overlength_prompt:tv_s:use_horizontal_symmetry:use_secondary_model:use_vertical_symmetry:visualize_cuts:width_height flag
do
    case "${flag}" in
        batch_name) batch_name=${OPTARG};;
        batch_size) batch_size=${OPTARG};;
        clamp_grad) clamp_grad=${OPTARG};;
        clamp_max) clamp_max=${OPTARG};;
        clip_denoised) clip_denoised=${OPTARG};;
        clip_guidance_scale) clip_guidance_scale=${OPTARG};;
        clip_models) clip_models=${OPTARG};;
        clip_models_schedules) clip_models_schedules=${OPTARG};;
        cut_ic_pow) cut_ic_pow=${OPTARG};;
        cut_icgray_p) cut_icgray_p=${OPTARG};;
        cut_innercut) cut_innercut=${OPTARG};;
        cut_overview) cut_overview=${OPTARG};;
        cut_schedules_group) cut_schedules_group=${OPTARG};;
        cutn_batches) cutn_batches=${OPTARG};;
        diffusion_model) diffusion_model=${OPTARG};;
        diffusion_model_config) diffusion_model_config=${OPTARG};;
        diffusion_sampling_mode) diffusion_sampling_mode=${OPTARG};;
        display_rate) display_rate=${OPTARG};;
        eta) eta=${OPTARG};;
        gif_fps) gif_fps=${OPTARG};;
        gif_size_ratio) gif_size_ratio=${OPTARG};;
        image_output) image_output=${OPTARG};;
        init_image) init_image=${OPTARG};;
        init_scale) init_scale=${OPTARG};;
        n_batches) n_batches=${OPTARG};;
        name_docarray) name_docarray=${OPTARG};;
        on_misspelled_token) on_misspelled_token=${OPTARG};;
        perlin_init) perlin_init=${OPTARG};;
        perlin_mode) perlin_mode=${OPTARG};;
        rand_mag) rand_mag=${OPTARG};;
        randomize_class) randomize_class=${OPTARG};;
        range_scale) range_scale=${OPTARG};;
        sat_scale) sat_scale=${OPTARG};;
        save_rate) save_rate=${OPTARG};;
        seed) seed=${OPTARG};;
        skip_event) skip_event=${OPTARG};;
        skip_steps) skip_steps=${OPTARG};;
        steps) steps=${OPTARG};;
        stop_event) stop_event=${OPTARG};;
        text_clip_on_cpu) text_clip_on_cpu=${OPTARG};;
        text_prompt) text_prompt=${OPTARG};;
        transformation_percent) transformation_percent=${OPTARG};;
        truncate_overlength_prompt) truncate_overlength_prompt=${OPTARG};;
        tv_s) tv_s=${OPTARG};;
        use_horizontal_symmetry) use_horizontal_symmetry=${OPTARG};;
        use_secondary_model) use_secondary_model=${OPTARG};;
        use_vertical_symmetry) use_vertical_symmetry=${OPTARG};;
        visualize_cuts) visualize_cuts=${OPTARG};;
        width_height) width_height=${OPTARG};;
    esac
done
echo "batch_name: $batch_name";
echo "steps: $steps";
echo "eta: $eta";
#sh disco.sh -batch_name 'DiscoParty__00001' -steps 250 -eta 0.7



#                   DEFAULT | SETTINGS 
#                batch_name │ None                                                                           
#                batch_size │ 1                                                                              
#                clamp_grad │ True                                                                           
#                 clamp_max │ 0.05                                                                           
#             clip_denoised │ False                                                                          
#       clip_guidance_scale │ 5000                                                                           
#               clip_models │ ['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']                       
#     clip_models_schedules │ None                                                                           
#                cut_ic_pow │ 1.0                                                                            
#              cut_icgray_p │ [0.2]*400+[0]*600                                                              
#              cut_innercut │ [4]*400+[12]*600                                                               
#              cut_overview │ [12]*400+[4]*600                                                               
#       cut_schedules_group │ None                                                                           
#              cutn_batches │ 4                                                                              
#           diffusion_model │ 512x512_diffusion_uncond_finetune_008100                                       
#    diffusion_model_config │ None                                                                           
#   diffusion_sampling_mode │ ddim                                                                           
#              display_rate │ 1                                                                              
#                       eta │ 0.8                                                                            
#                   gif_fps │ 20                                                                             
#            gif_size_ratio │ 0.5                                                                            
#              image_output │ True                                                                           
#                init_image │ None                                                                           
#                init_scale │ 1000                                                                           
#                 n_batches │ 4                                                                              
#            name_docarray* │ discoart-0df4d0c8654811ed8b84c4bde571e200                                      
#       on_misspelled_token │ ignore                                                                         
#               perlin_init │ False                                                                          
#               perlin_mode │ mixed                                                                          
#                  rand_mag │ 0.05                                                                           
#           randomize_class │ True                                                                           
#               range_scale │ 150                                                                            
#                 sat_scale │ 0                                                                              
#                 save_rate │ 20                                                                             
#                     seed* │ 4088028464                                                                     
#                skip_event │ None                                                                           
#                skip_steps │ 0                                                                              
#                     steps │ 250                                                                            
#                stop_event │ None                                                                           
#          text_clip_on_cpu │ False                                                                          
#              text_prompts │ ['A beautiful painting of a singular lighthouse, shining its light across a    
#                           │ tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on      
#                           │ artstation.', 'yellow color scheme']                                           
#    transformation_percent │ [0.09]                                                                         
# truncate_overlength_prompt │ False                                                                          
#                  tv_scale │ 0                                                                              
#   use_horizontal_symmetry │ False                                                                          
#       use_secondary_model │ True                                                                           
#     use_vertical_symmetry │ False                                                                          
#            visualize_cuts │ False                                                                          
#              width_height │ [1280, 768]    