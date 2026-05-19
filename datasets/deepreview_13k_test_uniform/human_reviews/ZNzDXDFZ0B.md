# PanoDiffusion: 360-degree Panorama Outpainting via Diffusion

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Generating complete 360\textdegree{} panoramas from narrow field of view images is ongoing research as omnidirectional RGB data is not readily available. 
Existing GAN-based approaches face some barriers to achieving higher quality output, and have poor generalization performance over different mask types. In this paper, we present our 360\textdegree{} indoor RGB-D panorama outpainting model using latent diffusion models (LDM), called \mname. 
We introduce a new bi-modal latent diffusion structure that utilizes both RGB and depth panoramic data during training, which works surprisingly well to outpaint \emph{depth-free} RGB images during inference. 
We further propose a novel technique of introducing progressive camera rotations during each diffusion denoising step, which leads to substantial improvement in achieving panorama wraparound consistency. 
Results show that our \mname not only significantly outperforms state-of-the-art methods on RGB-D panorama outpainting by producing diverse well-structured results for different types of masks, but can also synthesize high-quality depth panoramas to provide realistic 3D indoor models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new diffusion based method to tackle panorama image generation task. The proposed method utilizes the latent diffusion models to outpaint the area that is not originally taken by the camera. Relying on the powerful generation capability of diffusion models, the proposed method proposes to progressively apply camera rotations during the image generation process in order to enhance the generalizability. Extensive experiments show that the proposed method is able to outperforms the baseline methods significantly.

### Strengths
1. This paper is generally well written with strong motivation and well-organized writing. It clearly demonstrates the problem of  current pano generation and implies the proposed method is tackling the problems stated. 
2. The proposed method significantly outperforms the baseline methods on the selected benchmarks.

### Weaknesses
1. During the training stage, does the random angle rotation only apply to horizontal direction?
2. Depth map actually provides rich information indicating the scales of the objects in the images. In order to test the generalization capability, can you provide more results of running the proposed method on other datasets?
3. This paper claims the camera rotations as one of the contributions, please provide an ablation study on how the camera rotation actually works effectively.

### Questions
The authors are suggested to address the concerns raised in the weaknesses section during the rebuttal period.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a way to outpaint a near field-of-view image (i.e. a normal image from a normal camera) to a panorama, which they represent as a equirectangular projected image. They use latent diffusion models to do so. Their latent model is trained on RGB-D panoramic data, but works on just RGB inputs. 

One problem with outpainting panoramic images is that the left and right side of the equirectangular project image need to map to each other. The authors introduce a novel technique to do this. It works by rotating the image by 90 degrees in each denoising step in the diffusion model.

The authors compare to a variety of other techniques and show that their method is better than competing methods.

### Strengths
The paper is well-written and the results seem pretty good. The author’s idea to rotate the image 90 degrees in each denoising step seems very novel. 

There are lots of comparisons to many other methods and the proposed method is better based on a variety of techniques. 

I appreciate that the authors include the code as supplementary material!

### Weaknesses
It is somewhat hard to evaluate the generated panoramic images based on looking at images or fixed rotations. I would be interested in seeing the panoramic images of both the proposed method and competing method in a viewer like threejs. See https://threejs.org/examples/webgl_panorama_equirectangular.html

### Questions
There are many ways to represent 360 degree panorama images. The authors should clarify that using the equirectangular projection is a choice they are making.

Do the authors only rotate the camera in the horizontal direction? Or are vertical rotations allowed as well?

During inference, did the authors try 180 degree shifts instead of 90 degree shifts? Or some other rotation?

What’s the difference between Fig. 2 and Fig. 3? They seem like they are both figures about how training and inference are done, but they seem to be different. Specifically, Fig. 2b does not add noise and does not reference the circular shift, while Fig. 3b does. Is Fig. 2b incorrect?

In the supplemental video, do the shown 3D Scenes at 00:12 use the generated depth maps?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a latent diffusion model (LDM) for indoor RGB panaroma inpainting and depth map generation. During training stage, the input to the bi-modal LDM structure are RGB images and corresponding depth maps, which improve the performance of panaroma inpainting. At each stage of the denoising process in the diffusion model, the proposed alignment mechanism enhances the wraparound consistency of the results. The results indicate that the proposed PanoDiffusion excels not only by achieving a substantial performance advantage over state-of-the-art techniques in RGB-D panorama outpainting, yielding diverse and well-structured results for various mask types, but also by demonstrating the capability to generate high-quality depth panoramas.

### Strengths
- During inference process, there is no need to input the depth map as a guidance, only training process requires depth maps as input. It is significantly different from the previous approaches.
- This paper proposed a noval approach that involves gradually introducing camera rotations at each stage of the diffusion denoising process, resulting in a notable enhancement in achieving seamless panorama wraparound consistency.
- With the clear description of each module and step, this approach ensures that the framework is not only effective but also easily comprehensible and straightforward to follow.

### Weaknesses
- There is not many noval changes to the LDM framework. The authors only add a pretrained depth map encoder as a guidance.
- There are only one visual result (Figure 6) in the paper, which is not convincing. The authors should add more visual results for comparison in the supplementary materials.

### Questions
- How about the training and inference time compared to other frameworks? Since LDM requires a step-by-setp mechanism to generate the final results, the efficiency may be a problem.
- There are only 4 types of maskes. Each type of mask covers different portion of the whole panaroma. I recommand the authors to add a chart that describes the performance changing along the percentage of the mask. According to my understanding, with the increase of the percentage of the mask, the performance will drop.
- The mask are all continuous presented in this paper, I am curious when there are several separate masks in one panaroma, what will the performance become?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a diffusion model for panoramic image generation. A two-stage RGB-D PanoDiffusion model is proposed for indoor RGB-D panorama outpainting. The model taks depth information as input and processed through a bi-modal LDM structure. As the results shown, the use of depth information enhances the generation of RGB panoramas, and the alignment mechanism ensures wraparound consistency in the results. The method can be used to generate RGB-D panoramas at 512×1024 resolution.

### Strengths
The RGB-D fusion and combination mechanism is brought to the field of panoramic image generation via using the latent diffusion models. A RGB-D panoramic outpainting model is proposed to perform indoor 360-degree image generation. 

A bi-modal latent diffusion structure is proposed to combine RGB and depth information during training the diffusion model for panoramic image generation. 

A camera-rotation method is proposed to perform a stronger data augmentation. The two-end method can be used to crop a 90-degree equivalent area and stitch to the opposite sides to perform additional data augmentation to improve the wraparound consistency.

### Weaknesses
As compared to the previous methods, the depth information is additionally added to train the diffusion model. Even though the depth information is not needed for inference. 

The proposed RGB-D framework is constructed by using two parallel LDM to reconstruct the depth and RGB images separately. This structure might result in a larger and more complex model architecture than using a shared or depth-conditional LDM.  

An additional module is needed to refine and upscale the low-resolution image output to a high-resolution image. However, a pre-trained super-resolution GAN model is needed to perform such a refinement.

### Questions
Apart from the visualization results, how about the evaluation results of using concatenation or cross-attention in the so-called depth-conditional diffusion model? 

How is the cross-attention operation used in the depth-conditional method? Whether the authors try other advanced multimodal fusion methods to better combine the features from RGB and depth? 

It would be better to ablate the camera-rotation data augmentation method. 

In the depth panoramic synthesis, how about the comparison to some RGB-based depth estimation methods? For example, in the case of using fully masked input. 

How about the runtime or complexity analysis of the proposed method, since the parallel LDM are used for RGB and depth separately.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
