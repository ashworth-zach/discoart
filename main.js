var express = require('express');
var app = express();
const session = require('express-session');
const flash = require('express-flash');
const { exec } = require('child_process');

var AddToQueue = exec('disco.sh',
        (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
        });

var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({
    extended: true
}));

var path = require('path');

app.use(flash());
app.use(express.static(path.join(__dirname, './static')));

app.set('views', path.join(__dirname, './views'));

app.set('view engine', 'ejs');
app.set('trust proxy', 1) // trust first proxy
app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true,
    cookie: {
        maxAge: 60000
    }
}))

app.get('/', function (req, res) {
    res.render("index");
})

app.get('/demo', function (req, res) {
    res.render("test");
})
app.listen(8000, function () {
    console.log("listening on port 8000");
})


// |                    DEFAULT | SETTINGS 
// |                 batch_name │ None                                                                               │
// │                 batch_size │ 1                                                                                  │
// │                 clamp_grad │ True                                                                               │
// │                  clamp_max │ 0.05                                                                               │
// │              clip_denoised │ False                                                                              │
// │        clip_guidance_scale │ 5000                                                                               │
// │                clip_models │ ['ViT-B-32::openai', 'ViT-B-16::openai', 'RN50::openai']                           │
// │      clip_models_schedules │ None                                                                               │
// │                 cut_ic_pow │ 1.0                                                                                │
// │               cut_icgray_p │ [0.2]*400+[0]*600                                                                  │
// │               cut_innercut │ [4]*400+[12]*600                                                                   │
// │               cut_overview │ [12]*400+[4]*600                                                                   │
// │        cut_schedules_group │ None                                                                               │
// │               cutn_batches │ 4                                                                                  │
// │            diffusion_model │ 512x512_diffusion_uncond_finetune_008100                                           │
// │     diffusion_model_config │ None                                                                               │
// │    diffusion_sampling_mode │ ddim                                                                               │
// │               display_rate │ 1                                                                                  │
// │                        eta │ 0.8                                                                                │
// │                    gif_fps │ 20                                                                                 │
// │             gif_size_ratio │ 0.5                                                                                │
// │               image_output │ True                                                                               │
// │                 init_image │ None                                                                               │
// │                 init_scale │ 1000                                                                               │
// │                  n_batches │ 4                                                                                  │
// │             name_docarray* │ discoart-0df4d0c8654811ed8b84c4bde571e200                                          │
// │        on_misspelled_token │ ignore                                                                             │
// │                perlin_init │ False                                                                              │
// │                perlin_mode │ mixed                                                                              │
// │                   rand_mag │ 0.05                                                                               │
// │            randomize_class │ True                                                                               │
// │                range_scale │ 150                                                                                │
// │                  sat_scale │ 0                                                                                  │
// │                  save_rate │ 20                                                                                 │
// │                      seed* │ 4088028464                                                                         │
// │                 skip_event │ None                                                                               │
// │                 skip_steps │ 0                                                                                  │
// │                      steps │ 250                                                                                │
// │                 stop_event │ None                                                                               │
// │           text_clip_on_cpu │ False                                                                              │
// │               text_prompts │ ['A beautiful painting of a singular lighthouse, shining its light across a        │
// │                            │ tumultuous sea of blood by greg rutkowski and thomas kinkade, Trending on          │
// │                            │ artstation.', 'yellow color scheme']                                               │
// │     transformation_percent │ [0.09]                                                                             │
// │ truncate_overlength_prompt │ False                                                                              │
// │                   tv_scale │ 0                                                                                   │
// │    use_horizontal_symmetry │ False                                                                              │
// │        use_secondary_model │ True                                                                               │
// │      use_vertical_symmetry │ False                                                                              │
// │             visualize_cuts │ False                                                                              │
// │               width_height │ [1280, 768]    











//dont use this shit
// function main(){
//     console.log("main.ks")
//     let promptNumber = 0; //is really 1
//     $( "#add-prompt-button" ).click(function() {
//         promptNumber++;
//         $(".prompt-container").append(`<div class="prompt-row prompt-row-${promptNumber}"></div>`);
//         $(`.prompt-row-${promptNumber}`).append(`<input type="text" placeholder="Prompt..." class="prompt-input ${promptNumber}-prompt">`)
//         $(`.prompt-row-${promptNumber}`).append(`<input type="text" placeholder="Weight" class="prompt-weight-input ${promptNumber}-prompt-weight">`)
//         $(`.prompt-row-${promptNumber}`).append(`<button class="removebutton remove-${promptNumber}-prompt">delete</button>`)
//     });
// }

// function deletePromptNode(index){
//     let runner = index+1;
//     $(`.prompt-row-${promptNumber}`).append(`<input type="text" placeholder="Prompt..." class="prompt-input ${promptNumber}-prompt">`)

// }


// // Anonymous "self-invoking" function
// (function() {
//     var startingTime = new Date().getTime();
//     // Load the script
//     var script = document.createElement("SCRIPT");
//     script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
//     script.type = 'text/javascript';
//     document.getElementsByTagName("head")[0].appendChild(script);

//     // Poll for jQuery to come into existance
//     var checkReady = function(callback) {
//         if (window.jQuery) {
//             callback(jQuery);
//         }
//         else {
//             window.setTimeout(function() { checkReady(callback); }, 20);
//         }
//     };

//     // Start polling...
//     checkReady(function($) {
//         $(function() {
//             var endingTime = new Date().getTime();
//             var tookTime = endingTime - startingTime;

//             console.log("jquery loaded after "+tookTime+"ms");
//             main();

//         });
//     });
// })();