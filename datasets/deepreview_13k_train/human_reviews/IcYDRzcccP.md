# Optimizing 4D Gaussians for Dynamic Scene Video from Single Landscape Images

- Decision: Accept
- Scores: 3, 6, 8, 6

## Abstract
To achieve realistic immersion in landscape images, fluids such as water and clouds need to move within the image while revealing new scenes from various camera perspectives. Recently, a field called dynamic scene video has emerged, which combines single image animation with 3D photography. These methods use pseudo 3D space, implicitly represented with Layered Depth Images (LDIs). LDIs separate a single image into depth-based layers, which enables elements like water and clouds to move within the image while revealing new scenes from different camera perspectives. However, as landscapes typically consist of continuous elements, including fluids, the representation of a 3D space  separates a landscape image into discrete layers, and it can lead to diminished depth perception and potential distortions depending on camera movement. Furthermore, due to its implicit modeling of 3D space, the output may be limited to videos in the 2D domain, potentially reducing their versatility. In this paper, we propose representing a complete 3D space for dynamic scene video by modeling explicit representations, specifically 4D Gaussians, from a single image. The framework is focused on optimizing 3D Gaussians by generating multi-view images from a single image and creating 3D motion to optimize 4D Gaussians. The most important part of proposed framework is consistent 3D motion estimation, which estimates common motion among multi-view images to bring the motion in 3D space closer to actual motions. As far as we know, this is the first attempt that considers animation while representing a complete 3D space from a single landscape image. Our model demonstrates the ability to provide realistic immersion in various landscape images through diverse experiments and metrics. Extensive experimental results are https://anonymous.4open.science/r/ICLR_3D_MOM-7B9E/README.md.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a framework to form the 4D Gaussians representation for dynamic video generated from the single landscape image. To be more specific, the author builds the point cloud based on the single depth estimation. By reprojecting it to the multi view images, the static 3D Gaussians can be optimized. Then, the author proposed consistent 3D motions estimation module to lift the predicted 2D motions into the 3D space and further achieve the consistent motion in the 3D space with further optimization. Finally, the motion and 3D guassian can be used to optimize the 4D Gaussians as the final representation. The experiment conducted on the dataset from Animating Pictures with Eulerian Motion Fields demonstrating that the results surpasses several baseline methods.

### Strengths
1. The experiment shows the performance surpass the baselines on the public dataset.
2. The paper tries to solve the multi view consistency issue in the 3D generation by leveraging minimizing the reprojection error for the motion prediction. It is a good to attempt for this common challenging issue in this field.

### Weaknesses
1. The Sec. 3.1 for 3D Gaussians generation seems to just follow the previous work, Luciddreamer. Please correct me there is any additional novel effort for this part.
2. Reprojecting the point cloud from the single view image to different views always leads to the holes, distortion and some other artifacts. A common idea to incorporate the generative model to fulfill the missing information. But it seems the author does not include anything related to this point. Please include more discussion if it is not necessary.
3. Minimizing the reprojection error for the predicted motions seems to be feasible in Sec. 3.2, However, this optimization is still based on the 2D information and can hardly achieve the 3D consistency. For example, in Structure from Motions, such method is always used refine the estimated camera poses and the position for the point clouds. But it does not consider the inter relationship between each 3D positions, so I am not sure that the 3D consistency can be achieved with this method.  
4. Please provide more implementation details of the 3D Motion Optimization Module. It seems to be vague now.
5. The Sec. 3.3 for 4D Gaussians generation seems to just follow the previous work. Please correct me there is any additional novel effort for this part.
6. The experimental results will be more solid and comprehensive if more dataset and baselines can be included. For example, the author mentions that simply using animation based method cannot achieve satisfying results, so similar baselines can be included.
7. The paper presentation can be more compact if the part of just following the previous work can be shortened while emphasizing the novel part.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method based on 4DGS to represent landscape 4D scenes from a single landscape image. It adapts Gaussian Splatting techniques for content with fluidity in the landscape images from the following aspects: 
-  3DGS methods require sparse points as initiations, while this paper uses existing depth prediction models to lift 2D pixels.     
- This paper proposes a module named 3D Motion Optimization to generate 3D animations with off-the-shelf 2D motion methods.
It also conducts experiments over multiple datasets to show quantitative and qualitative comparisons over existing methods.

### Strengths
1. Application to a new domain

This paper builds a solution to the problem of modeling landscape 4D scenes. 

2. Adpation of 3DGS / 4DGS

This paper adapts 3DGS from the initializations and 4D GS with motion prior.   

3. Comparison to existing methods 

The method shows better results compared to the existing methods.

### Weaknesses
1) The problem of generating Gaussians from landscape images with fluid content is useful but seems a bit too specific/narrow. If this paper can handle general 4D content, it would have a very large impact.
2) Lack of theoretical innovation for ICLR. To address the task of fluid motion, this paper uses constant speed and direction. As 3DGS is a particle-like model, the theoretical contribution should be greater if this paper can present or show different physical-based models for fluids.
3) Presentaiton of figures. Figure 2’s motion content is hard to see. Too many small arrows and small squares hurt the quality of the figure.

### Questions
1) What is the max temporal length the proposed method can achieve with good quality?
It has potential value if this paper can handle a long temporal range (with generated content). 

2) Can authors provide more technical insights? 
This paper builds upon a lot of exciting techs (depth prediction model, 2D motion models). I would like to know if the authors selected these methods by experiments or random or with insights. If this paper can improve this part, it can benefit future work in this field.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel approach to optimize 4D Gaussian Splatting representations using single landscape images. By leveraging Eulerian motion fields, it effectively generates animations of dynamic scenes like waterfalls, beaches, and rivers. The authors also present the 3D-MOM method, which addresses frame inconsistency to ensure smooth animations. Experimental results demonstrate the method’s state-of-the-art quality.

### Strengths
1. The authors propose a novel method to animate 3D scenes with the flow-based method. It is quite novel and can fit the landscape generation properly.

2. The results seem pretty good in certain demos and demonstrate the SOTA quality. 

3. 3D-MOM method is a good balance  when merging different 2D motion in multi-view images.

### Weaknesses
1. **Section 3.1 Citation:** It seems that a citation for 4D Gaussian Splatting (Wu et al., CVPR 2024) is missing in Section 3.1.

2. **Comparison with VividDream:** I recommend that the authors include discussions or comparisons with VividDream (Lee et al., ArXiv 2024). Using a single image for initialization may not be robust enough, so it would be beneficial to expand the method to accommodate larger 3D scenes. Consider the motivations of viewcrafter/VividDream4D, as merely supporting "zoom in" functionality is insufficient. It’s essential to address additional capabilities like "turn left/right" or "zoom out/up/down."

3. **Multiview Generation and Novel Content:** Since only one image is used as input, the authors suggest that warping techniques can generate multiview images, but this approach may lack **novel content** and leave many empty regions. How do the authors handle these issues? If not resolved, I recommend using viewcrafter to enhance quality. Additionally, how are rendering paths chosen? Please provide more details.

### Questions
**Animating Pictures with Eulerian Motion Fields:** This technique primarily supports fluid motion, such as water and smoke. How does it handle other types of motion, like wind or more complex movements? I am curious about the potential future improvements of this method. Could it be adapted for human or animated motions in the future?

 **Handling $M_0$:** How is $M_0$ obtained? Is SAM or another method used?

Overall, I think the demo and the presentation of the paper are good. My main consideration lies in weakness 2,3,4.

Besides, I just think working on landscape images is quite small (not quite confident).  if the authors can demonstrate this pipeline could be applied in 4D scene generation, I would like to highly recommend accepting this paper.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel framework for generating realistic 4D dynamic videos from a single landscape image. The approach uses a three-stage optimization process: first, it optimizes 3D Gaussians by generating multi-view images from the input; second, it estimates consistent 3D motion across views using the 3D Motion Optimization Module (3D-MOM); and third, it optimizes 4D Gaussians by applying the estimated motion to model changes in position, rotation, and scaling over time. This technique outperforms existing methods, such as 3D Cinemagraphy and Make-It-4D, by producing better qualitative results with reduced artifacts. The use of Gaussian Splatting contributes to improved PSNR and sharper video effects, as demonstrated in the supplementary videos.

### Strengths
+ Reasonable Pipeline: 

The choice of Gaussian splatting offers better depth approximation compared to Layered Depth Images (LDI), leading to fewer artifacts in novel view synthesis.

+ Natural 3D Motion Consistency: 

The use of 3D consistent motions derived from 2D motion guidance results in more natural and coherent dynamics in the generated videos.

+ Improved Performance: 

The method demonstrates superior PSNR and visually appealing results compared to the approaches by Shen et al. and Li et al.

### Weaknesses
It has several limitations, where my main concerns are the implementation details and its evaluations.

+ Gaussian Splatting Optimization:

In sec. 3.1, the explanation for both (a) camera settings and (b) multi-view optimization is unclear. Monocular depth estimation typically outputs normalized depth or disparity, which loses the depth scale. Additionally, a single image usually lacks intrinsic or extrinsic camera parameters. How were these parameters obtained? Specifically, what is the focal length used, and how is the principal point determined? Are these parameters estimated or assumed? Furthermore, the lack of absolute scale from monocular depth estimation means that the 3D point cloud is only defined up to a scale factor. How does this impact the subsequent motion estimation and 4D Gaussian training?

In Eq. 3, what serves as the ground truth (GT) for multiview loss? A single image cannot provide multiple views for supervision unless additional views are available. However, the paper claims to only use a single image as input. How is Eq. 3 implemented in this case? If novel views are generated by manipulating camera parameters, wouldn't the resulting 3D reconstruction simply replicate the input mono-depth, lacking true 3D understanding? This seems like a chicken-and-egg problem.

+ Motion Estimation:

In sec. 3.2, there is some ambiguity regarding the motion estimation process. Are you using 2D optical flow? While projecting 3D motion into a 2D image would result in 2D optical flow, which offers rich motion data, the implementation is unclear. How is the 2D optical flow computed, and what is the specific model used? How are occlusions handled in the 2D motion estimation, and how does this impact the 3D motion consistency?

For various views, such as in Fig. 1, it seems semantic masks (e.g., for water or fluid) are used. First, how do you get these masks? Second, if you render a novel view with most black regions and it to the motion estimation model, how do you get a reasonable motion estimation result? The paper lacks details on this critical point. What happens when the mask is inaccurate or incomplete?

+ 4D Gaussian Training Process:

In sec. 3.3, the training process for 4D Gaussians is confusing. In pipeline 1 and 2, the method seems to already estimate 3D Gaussians and their motions. This suggests that you could simply deform the Gaussians to generate a video. However, training 4D Gaussians requires a video, but the input is a single 2D image.

Line 343 mentions using a video generation model to produce a pseudo-video (is this using OpenSORA?), which is then used to create a 4D Gaussian with initialized motions and 3D points, supervised by the input image and generated video. Is this correct? What specific video generation model is used, and how does its performance affect the final 4D Gaussian quality? How are the initial 3D Gaussian parameters and motions transferred to the 4D Gaussian representation?

+ Heavy Reliance on Pretrained Models:

If I understand correctly, the method seems to rely heavily on pretrained models. Specifically, it seems to (a) use video generation models to create a video, (b) apply depth and motion models to estimate initial depth and motion, and (c) lift these into 4D for dynamic novel view synthesis (NVS). This implies the core technique is lifting generated 4D content from 2D guidance, which could limit the novelty of the approach. The paper does not clearly articulate the novel contributions beyond the integration of existing models.

+ Applicability to Specific Motions:

The method appears limited to handling fluid motions, such as water. The paper does not discuss the limitations of the Eulerian flow model and its applicability to other types of motion. How does the method perform with more complex motions, such as rigid body movements or articulated objects?

+ Evaluation Metrics:

PSNR may not be a meaningful metric for evaluating motion generation. A user study could provide more insightful feedback. Nevertheless, I acknowledge that the method shows better performance than the baselines, as demonstrated

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2
