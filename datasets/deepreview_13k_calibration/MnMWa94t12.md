# DyST: Towards Dynamic Neural Scene Representations on Real-World Videos

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Visual understanding of the world goes beyond the semantics and flat structure of individual images.
    In this work, we aim to capture both the 3D structure and dynamics of real-world scenes from monocular real-world videos. 
    Our Dynamic Scene Transformer (DyST) model leverages recent work in neural scene representation to learn a latent decomposition of monocular real-world videos into scene content, per-view scene dynamics, and camera pose.
    This separation is achieved through a novel co-training scheme on monocular videos and our new synthetic dataset DySO.
    DyST learns tangible latent representations for dynamic scenes that enable view generation with separate control over the camera and the content of the scene.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The goal of this paper is to estimate motion and object pose and shape from monocular videos using a latent neural representation. 
Two modules are trained for camera parameter and object position and shape estimations. Then, these modules are then used as input to a third decoder module to generate novel views. To ensure the specialization of the modules, the authors proposed a training procedure where the data is organized to enforce which information is learned by each module. Evaluations are conducted on a newly created dataset which was used to train the model and qualitative results are presented with motion extraction, novel view generation, video manipulations where novel camera motions or object movements are generated.

### Strengths
Compared to the state of the art, this work investigates the more difficult setting of estimating moving objects and moving cameras only from a few motions pictures and a monocular camera. Moreover, they remove the assumptions of training one model for each scene. 

The separation of 3D structure estimation and camera motion is an interesting property of the model. The training tricks illustrated by Eq. 5 and Eq. 6 provide an practical way of enforcing this while still retaining the benefit of end to end training.

Although the videos are simple and are still far from the complexity of most real world data,it is still a good compromise as a next step toward more mature systems. Experiments shown in Fig.3 to assess the specialization of the different modules are convincing, it is also supported by the qualitative results shown in the videos in the supplementary material on video manipulation and image synthesis.

Experiments seems reproducible, given code and training parameters, and available datasets will be provided.

### Weaknesses
The amplitude of the motion would probably limits the accuracy of the method. In Fig.7 the motion is tiny, and this is not evaluated by the authors. Although the encoder and decoder architectures are rather small for the "simple" cases covered by the paper, I have concerns on the scalability of this method to more real cases and more complex motions. The limited motion in the training data may lead to poor generalization when faced with larger displacements or rotations. The model's ability to handle occlusions and self-occlusions, which are common in real-world scenarios, is also unclear. The reliance on relatively simple scenes and motions during training raises questions about its robustness in more complex environments with cluttered backgrounds, varying lighting conditions, and more intricate object interactions. Furthermore, the paper does not discuss the computational cost associated with training and inference, which could be a limiting factor for practical applications, especially if the model needs to be scaled to handle more complex scenes and motions.

### Questions
Is the latent dynamic space somehow interpretable, and is it possible to generate one instance based on the object position in space, or does the latent space always be inferred from an existing image contained in the processed sequence ? 
In the later case, this means the approach cannot be used to recreate dynamics that do not exist yet in the data ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The authors propose Dynamic Scene Transformer (DyST) which makes a model infer the target view’s control latents (camera pose, scene dynamics) with a pair of corresponding views (different camera pose and scene dynamics from target view).
- Moreover, the authors propose a synthetic dataset, Dynamic Shapenet Objects (DySO), which consists of 5 scene dynamics and 5 camera views for each dynamic scene video to train the DyST.
- By showing qualitative and quantitative results of the experiments on changing control latents, the authors validate that the DyST learns latent decomposition of the space into scene content.

### Strengths
- The authors co-train synthetic and real-world datasets to transfer the dynamics and camera control potential of synthetic scenes to natural monocular video and the results shown in Fig. 5 indicate that the model has learned to encode dynamics independently of the camera pose.
- Since there is no architectural difference between camera pose and scene dynamics, the authors propose to enforce separation through a novel latent control swap training scheme, and the results in Fig. 3 demonstrate their method with a high improvement in PSNR scores.

### Weaknesses
 - [Generalization in different types of motions] Additional experiments are needed to see if the proposed DyST model can generalize to camera poses and scene dynamics that were not seen during training. so, it would be better to provide qualitative results on how the controlled view looks like when horizontal shifts are input after training without horizontal shifts. (DySO’s camera motions consist of 4 horizontal shifts, panning, zooming motions, and random camera points)
- [Cluttered background] Since the backgrounds of the DySO dataset in Fig. 2 and 3 are clean, the authors need to experiment to see if DyST can robustly control the view even when using videos with cluttered backgrounds. In addition, it would be better to have a distance analysis for unclean scenes to see how distinctly it separates camera pose and scene dynamics like the experiment in Figure 5.
- [Quantitative comparison] As the authors mentioned in Sec. 5 Conclusion, unlike NeRF's output, the output of the proposed method has a quality gap, such as objects disappearing or blurring. Therefore, quantitative comparison results such as PSNR and LPIPS between NeRF and DyST are needed.
- [Multiple objects] Also, as mentioned by the authors in the same section, the authors did not provide results for multiple object scenes. It would be helpful to see the results of latent distance analysis in Figure 5, PSNR, and LPIPS in Figure3 for multiple object scenes.

### Questions
- The latent control swap training scheme needs 3 input views. It would be helpful why 3 input views are needed and how the performance changes with less or more than 3 input views.
- It would be better if the authors discuss why it needs the contrastiveness metric and what the authors are trying to show with the swap in Table 1.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Dynamic Scene Transformer that learns latent neural scene representations from monocular dynamic video without any pose information. Different from previous works, this paper mainly focuses on modeling the latent space for dynamic scenes. To achieve this, the authors utilized  a Camera Estimator and a Dynamics Estimator to produce the low-dimensional controllable latents for camera pose and scene dynamics. To separate dynamics from camera pose effectively, the author further design a swap training scheme and establish a multi-view, multi-dynamics dataset synthetic dataset.

### Strengths
1. This paper is well-motivated. The primary goal of this paper is the separation of scene dynamics and camera pose, while most of existing works only cover the static scenes.
2. The authors proposes a novel training scheme that disentangles the camera pose from two views under the same camera while containing a moving object, and disentangles the scene dynamic from two views with still objects while under two different cameras. To fulfill this training strategy, the authors also establish a new synthetic data with multi-view, multi-dynamics data.

### Weaknesses
1. The method is quite similar to RUST[1]. The encoder, decoder and camera estimator are almost the same as the ones proposed in RUST. 
2. Inference procedure. From the method architecture, the target view is required to obtain the camera latents and dynamic latents. In this case,  I wonder if the specific novel view image is needed as the input to generate the novel view?  
3. Control the latent code. In Fig7, the authors show the results of controlling camera latent and dynamic latent. The authors could explain how to control the latent code.
4. Some quantitative results on real data should be provided.

### Questions
Reproducibility Statement should be put in the appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
