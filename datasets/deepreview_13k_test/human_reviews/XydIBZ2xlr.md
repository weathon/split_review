# Boost 3D Reconstruction using Diffusion-based Intrinsic Estimation

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we present DM-Calib, a diffusion-based approach for estimating pinhole camera intrinsic parameters from a single input image. Monocular camera calibration is essential for many 3D vision tasks. However, most existing methods depend on handcrafted assumptions or are constrained by limited training data, resulting in poor generalization across diverse real-world images. Recent advancements in stable diffusion models, trained on massive data, have shown the ability to generate high-quality images with varied characteristics. Emerging evidence indicates that these models implicitly capture the relationship between camera focal length and image content. Building on this insight, we explore how to leverage the powerful priors of diffusion models for monocular pinhole camera calibration. Specifically, we introduce a new image-based representation, termed Camera Image, which losslessly encodes the numerical camera intrinsics and integrates seamlessly with the diffusion framework. Using this representation, we reformulate the problem of estimating camera intrinsics as the generation of a dense Camera Image conditioned on an input image. By fine-tuning a stable diffusion model to generate a Camera Image from a single RGB input, we can extract camera intrinsics via a RANSAC operation. We further demonstrate that our monocular calibration method enhances performance across various 3D tasks, including zero-shot metric depth estimation, 3D metrology, pose estimation and sparse-view reconstruction. Extensive experiments on multiple public datasets show that our approach significantly outperforms baselines and provides broad benefits to 3D vision tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces DM-Calib, a diffusion-based model for monocular camera calibration that leverages stable diffusion models trained on diverse data to estimate camera intrinsics from a single image. By integrating an image-based representation called the Camera Image, the method enables the extraction of camera parameters via a generative process with RANSAC for postprocessing. Demonstrated across various 3D vision tasks, DM-Calib outperforms existing methods, offering significant improvements in generalization and accuracy in camera calibration from monocular setups.

### Strengths
1. Compared to previous work that uses diffusion model for intrinsic prediction, this paper proposes a new spatial-aware representation for intrinsics, which is called Camera Image. The main motivation here is, to best leverage the power of pretrained diffusion model, the camera information should be incorporated as an image that fits the domain of the diffusion models. Therefore, this paper proposes to incorporate fx, fy, cx, and xy as the first two dimension, and uses the gray scale image as the third dimension. This design makes sense and seems to generally work well. 

2. This paper did extensive experiments over different tasks and datasets, which effectively proves the ability of the proposed method.

### Weaknesses
1. The main concern comes from the Sparse-view 3D Reconstruction & Pose Estimation experiment. It seems, the authors claim that the proposed monocular view method can achieve better intrinsic estimation than mutli view method dust3r. Such a conclusion looks quite weird to the reviewer, especially given the fact that, although monocular depth estimation has achieved great success in the recent two years with the support of diffusion models, its accuracy is still not as good as those multi-view methods. The task of monocular metric depth estimation is very related to monocular intrinsic estimation, so the reviewer would expect there should not be such a huge difference. If so, does the result of "Sparse-view 3D Reconstruction & Pose Estimation experiment" imply that the intrinsic parameters estimated by dust3r are far away from accurate, or is there any specific setting? The authors mentioned that "Detailed experimental settings are provided in the appendix" in L480 but the reviewer did not find it. 



2. The reviewer agrees that it is best to consider all of fx, fy, cx, and cy. However, looking at the datasets used for training, it seems most of them strictly have a principal point lying at the image center, e.g., all the self-driving datasets, almost all the synthetic datasets, and all the SfM-annotated (i.e., COLMAP) datasets. Furthermore, if I remember it correctly, most of these datasets have fx=fy. This leads to a question that, what is exactly learned by the model? Or in other words, if using a representation, just [fx, fy, gray] (with fx and fy normalized), will the performance be worse, or even better? It would be beneficial if the authors can provide more examples and analysis to prove that the parameters such as cx cy are not ignored by the model.

### Questions
The reviewer recognizes the extensive engineering effort evident in this paper and the promising performance of the implemented system. However, the underlying principle needs a further proof and a more thorough discussion of the sparse reconstruction experiments is needed. The primary concern is the Sparse-View 3D Reconstruction & Pose Estimation experiment, where the results appear unreasonable to the reviewer. Further clarification and justification of these outcomes are necessary.

### Soundness
3

### Presentation
3

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
In this work, authors propose DM-Calib, a monocular camera calibration method by fine-tuning a stable-diffusion model. The main contribution of the work is the image-representation of a pin-hole intrinsic matrix called "Camera Image." This representation allows authors to fine-tune a text-to-image stable-diffusion model as an image-to-camera-image diffusion model. From the generated camera image, authors estimate intrinsic using RANSAC. Authors show their superior camera calibration accuracy compared to non-diffusion and diffusion-based methods.

Authors show multiple applications of their camera calibration method: Specifically, they train Metric-depth estimation that uses a camera image + RGB image to predict one diffusion-step metric depth using a diffusion UNet. Authors also propose applications to sparse view 3D reconstruction, pose estimation, and 3D metrology, and show superior/comparable results to the SOTA methods in this field.

### Strengths
The proposed "Camera Image" shows easy integration with current diffusion-based generative models. Authors also show that intrinsics obtained using this method generalize in a zero-shot manner on multiple real-world indoor and outdoor datasets. This intrinsic representation, which closely resembles an RGB image, opens doors for other 3D reconstruction and calibration methods to be able to use large diffusion model priors. 

Authors also show that they can train a single-step diffusion method that generates metric depth from input RGB + intrinsic camera image representation. This simple metric depth achieves comparable performance to specialized metric-depth estimation methods such as Metric3D, and also achieves comparable results to affine-invariant depth estimation methods.

### Weaknesses
While the proposed Camera Image representation for intrinsics is promising, authors did not discuss how to incorporate distortion into this image. Is the calibration limited to the Pinhole model? I would ask authors to clearly state in the abstract that this method can recover pinhole intrinsics from the image, without distortion parameters.

For the metric-depth estimation method, authors propose a single-step diffusion model. I see that it uses a single-step pass for diffusion, which essentially is just a forward pass to the UNet of Stable-diffusion. Is this a diffusion-based method? If yes, I would be happy if authors cite relevant sources.

One thing that is a bit unclear from the paper is that, does the metric-depth estimation model use "GT" camera-image, or a camera-image predicted from the diffusion model? If it uses "GT" camera-image, then the method is not comparable to other metric-depth estimation methods, many of which predict the method without intrinsics. I would request authors to explicitly mention in the paper if the camera-image used in metric depth estimation is GT or predicted one.

While I appreciate the many applications of Camera Intrinsic, describing so many applications is taking the focus away from the main theme of the paper, which is monocular camera calibration. I would propose authors to make the paper focused on camera calibration, such that readers can understand the main contribution of the paper easily. Some of the applications (Metrology, Pose estimation) can go in the appendix.

### Questions
- Is the input to the metric depth estimation module a "real" camera image? If yes, how can this method be compared to other methods?

- Why are the most recent approaches such as "GeoCalib" [1] excluded from comparison? I would be very interested in comparing this method against more "geometry"-inspired methods GeoCalib [1], that has also shown impressive results across many datasets.

References:

[1] Veicht, Alexander, et al. "GeoCalib: Learning Single-image Calibration with Geometric Optimization." arXiv preprint arXiv:2409.06704 (2024).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper repurposes Stable Diffusion (SD) for intrinsic and metric depth prediction. It proposes an image representation termed "Camera Image," which is a 3-channel image: the first two channels are related with ray directions, and the third channel is the grayscale image. The fine-tuned SD 2.1 can predict the corresponding Camera Image from the input image. Then, the intrinsics can be solved by RANSAC. The paper also showcases applications in metric depth estimation and sparse-view reconstruction (based on Dust3r). Experiments are conducted on various datasets. It outperforms baselines on camera calibration and achieves comparable results on depth estimation.

### Strengths
1. The proposed diffusion-based method for intrinsics prediction is simple but effective. It outperforms a recent SOTA baseline DiffCalib.

2. Compared to DiffCalib, the paper uses the grayscale image as the third channel, which makes it closer to the pretrained prior (Table 6). This makes training easier.

3. The paper conducts a good ablation study and many experiments on metric depth prediction and 3D reconstruction.

### Weaknesses
1. The overall idea is very similar to DiffCalib, which was released earlier this year. DiffCalib also fine-tunes Stable Diffusion 2.1 to estimate both the incident map for intrinsics and the depth map.

2. If the VAE is fine-tuned or simply rescaled to match the distribution before the diffusion model training, will the gray image still be necessary?

3. The diffusion model is stochastic. The standard deviation in the experiments should also be reported.

### Questions
L228: Explaining the ray vector r at its first appearance would benefit novice readers.

Typos:

L292: deonise → denoise

L293: encoder → encode

### Soundness
3

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
This paper presents DM-Calib, a diffusion-based approach that utilizes a unique Camera Image representation to estimate monocular camera intrinsics. The authors leverage a pre-trained stable diffusion model, adapting it to predict camera parameters from single images. The proposed method is evaluated on a range of datasets (KITTI, NuScenes, etc.) and is intended to support 3D vision tasks such as depth estimation, 3D reconstruction, and pose estimation.

### Strengths
1. The idea of embedding camera parameters as a “Camera Image” and feeding it into a diffusion model is innovative. I think this approach is a step forward in making monocular camera calibration feasible in single-image scenarios.  

2 . The paper’s evaluations span multiple vision tasks, indicating an attempt to generalize across applications. Evaluating on KITTI, NuScenes, and other datasets gives a broad base for understanding DM-Calib’s performance.

### Weaknesses
From my point of view, the weakness mainly comes from the experiments part:  

(1) I noticed that the baseline comparisons are missing some key controls. For example, it would be essential to include a version of DM-Calib with ablated components (e.g., without Camera Image or grayscale encoding) to clearly understand each component's contribution. The current results leave questions about the true utility of the Camera Image itself and whether it alone brings significant performance gains.     

(2)  In Table 3, I noticed that while DM-Calib reports a slightly lower error than one baseline, the gains are minimal and within the standard deviation range. The small margin makes it hard to justify DM-Calib's superiority, and without significance testing, these small gains may not be meaningful. 

(3) The ablation study provided in Table 4 is sparse and does not explain how each component of DM-Calib contributes to the final accuracy. I think that a more thorough examination of components, such as the role of grayscale encoding, is necessary. In particular, removing grayscale information and testing only the Camera Image format would have strengthened the argument.

### Questions
(1) Could the authors provide a more detailed breakdown of how much the Camera Image impacts the results independently from the rest of the model? Given its centrality, I would expect this to be a core component of the results.

### Soundness
2

### Presentation
3

### Contribution
2
