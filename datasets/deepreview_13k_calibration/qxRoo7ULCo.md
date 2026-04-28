# 4K4DGen: Panoramic 4D Generation at 4K Resolution

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
The blooming of virtual reality and augmented reality (VR/AR) technologies has driven an increasing demand for the creation of high-quality, immersive, and dynamic environments. However, existing generative techniques either focus solely on dynamic objects or perform outpainting from a single perspective image, failing to meet the requirements of VR/AR applications that need free-viewpoint, 360$^{\circ}$ virtual views where users can move in all directions. In this work, we tackle the challenging task of elevating a single panorama to an immersive 4D experience. For the first time, we demonstrate the capability to generate omnidirectional dynamic scenes with 360$^{\circ}$ views at 4K (4096 $\times$ 2048) resolution, thereby providing an immersive user experience. Our method introduces a pipeline that facilitates natural scene animations and optimizes a set of dynamic Gaussians using efficient splatting techniques for real-time exploration. To overcome the lack of scene-scale annotated 4D data and models, especially in panoramic formats, we propose a novel \textbf{Panoramic Denoiser} that adapts generic 2D diffusion priors to animate consistently in 360$^{\circ}$ images, transforming them into panoramic videos with dynamic scenes at targeted regions. Subsequently, we propose \textbf{Dynamic Panoramic Lifting} to elevate the panoramic video into a 4D immersive environment while preserving spatial and temporal consistency. By transferring prior knowledge from 2D models in the perspective domain to the panoramic domain and the 4D lifting with spatial appearance and geometry regularization, we achieve high-quality Panorama-to-4D generation at a resolution of 4K for the first time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method by which a static pano image is animated to produce a video pano, then subsequently lifted to 3D using 3DGS.  The authors claim the following contributions:
* 4K4DGen, a method for lifting a static pano to dynamic 3DGS
* A panoramic denoiser which generates consistent animated perspective views 
* A dynamic panoramic lifting which transforms the video pano to dynamic 3DGS

### Strengths
* compelling use case
* qualitative results look good
* quantitative metrics show improvements over baselines
* well written

### Weaknesses
 * The animations each have small spatial extent.  I didn't see an example that illustrated that you could have many of these overlapping perspective animations and for a large scale animation to emerge.  e.g., It would be much more impressive if the authors could show the car in the desert where the car drives around the center of project.

* Some of the generated videos have significant artifacts.  For example, the fireworks in the third row of the supplemental has fireworks that don't move and speckled artifacts that are static. The static regions appear to be areas where the motion mask was not applied, and the speckled artifacts suggest a failure of the denoising process in these regions.

* The motion isn't always globally consistent.  For example, I'm not sure the clouds in row 7 of the supplemental make sense. The cloud motion appears to be inconsistent with the overall scene and exhibits unnatural distortions, possibly due to the limitations of applying a perspective-based animation model to an equirectangular projection.

* I think overall, the idea of applying this existing model to perspective patches is neat, but I'd be concerned this work would be quickly superseded by one where the diffusion model was fine-tuned on 360 videos. The current approach relies on a perspective-based model, which may not be optimal for generating coherent panoramic animations, and a model trained directly on 360 video data could potentially produce more globally consistent and higher-quality results.

* The lifting phase doesn't seem sufficiently evaluated.  It would have been nice to have something to inspect in the supplemental. The evaluation lacks a direct assessment of the 3D geometry, relying instead on rendered views, which may not fully capture the accuracy of the 3D reconstruction.

### Questions
* Have the authors considered using a more recent depth model than MiDaS?  It's pretty old at this point.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel framework to generate 4K4G panoramic video rendered from 3D Gaussian representation. The key technical insights is to use pre-trained 2D perspective camera to denoise the panorama by first rendering it into perspective image patch and then fusing it back into the sphere space. Once a panoramic video is created, a lifting process built on single image depth prediction method is to turn each frame into 3D Gaussian representation so that we can navigate inside the panorama. Both quantitative and qualitative experiments verified the effectiveness of each technical components and overall the framework achieves impressive video generation results.

### Strengths
1. As far as I know, this is the first paper to generate high-resolution 4D panorama videos, which may have many applications in VR. 

2. The proposed method is technically solid and easy to follow. The consistent panoramic animation part is similar to prior works that use 2D diffusion model to generate panorama but the paper replaces 2D diffusion models with 2D video diffusion model. The dynamic panoramic lifting part is also reasonable. 

3. While evaluating generative models is always a difficult problem and there is no prior works solving this problem, this paper still manages to build a set of benchmarks and a reasonable baseline to show the effectiveness of the proposed framework, which should be appreciated. 

5. The paper is well-written and easy to follow.

### Weaknesses
I am not an expert in using diffusion models for video generation and I haven't followed recent progress in that direction. The consistent panoramic animation part looks solid and reasonable to me. I only have some minor questions that are not necessarily the weakness of the paper. 

1. Eq. (3): While this equation is similar to how we generated static panorama using diffusion models for 2D perspective image, I wonder whether that will cause different Gaussian noise distribution at the overlap regions. Since we are essentially average the Gaussian noise from two denoised latent code, will that cause the variance of the noise at the overlap region to be smaller compared to non-overlapping area? Will that cause artifacts in image generation?

2. My second question is how significant the dynamic panoramic lifting can help us render 3D video. Given that all the examples shown in the paper have very large-scale scene and the perturbation $\alpha$ is very small in training, I would guess whether we lift the panorama into 3D or not may not make a big difference and approximating the whole 3D structure with a sphere may give us similar results. I assume the comparison is shown in Figure 6(c) but it is very difficult for me to see the difference. 

3. Also I wonder why don't we choose recent dynamic Gaussian works to model the video. I assume that is a more systematic way to handle this problem and may give us more temporal consistent view synthesis results.

### Questions
My major question is on the necessities of the dynamic panoramic lifting and whether that actually improves the quality when we move the camera and look around. In the submitted video, we can see a little bit camera movements but I wonder if that can be mimiced but simply textured the panorama to a large enough sphere. Also when handling the dynamic scene, why not consider all the dynamic Gaussian papers and instead use static Gaussian with a temporal constraints? If we use dynamic Gaussian representation, will that cause any differences?

### Soundness
3

### Presentation
3

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
The paper proposes an end-to-end solution for generating realistic 4D panoramic videos from static panoramas at 4K resolution for the first time. The paper uses pretrained image to video models to convert the static 2D panoramas to videos and then dynamically (with spatio-temporal alignment) lift them to 3D space resulting in the 4D content. 
The paper demonstrates the appropriateness of using a spherical latent space for the task and how the panoramic denoiser utilizes that. The lifting uses a geometry alignment model (pre-trained depth estimator) and optimize DreamScene360's objective with an additional temporal loss. 

The framework achieves high fidelity generations, both, visually and quantitatively. The user-study also aligns well with the results.

### Strengths
1. Novelty: This is the first paper that allows seamless (spatio-temporally aligned) 4K resolution generation of 4D content.
2. The spherical latent space operation alleviates a lot of visual artifacts and this paper is evidence that it is suitable for Panoramic generation tasks.
3. The model components, intuition and math is well grounded.
4. The fidelity of results is promising. Quantitative metrics suggest the same. (The resulting panorama videos provided on the supplementary page are extremely visually pleasing!)

### Weaknesses
1. Why are Efficient4D and 4DGen not used as baselines that potentially fail on Panoramas as there is no spatial-temporal alignment mechanism there? It would make the paper much stronger. Specifically, a discussion of how the inward-facing camera setup of these methods makes them unsuitable for panoramic generation would be beneficial. Furthermore, a more in-depth analysis of the domain gap between object-centric generation (as in Efficient4D and 4DGen) and scene-level panoramic generation would strengthen the argument for the proposed method's novelty.
2. It would have been nice to see comparisons for the 4D lifting phase to see how the proposed is better than existing methods like: OmniNeRF. This way the speed of the proposed method can also be highlighted as a strength of the paper. A quantitative comparison of the geometric fidelity achieved by the proposed method versus OmniNeRF, perhaps using metrics like Chamfer distance or point cloud alignment error, would be valuable. Additionally, a discussion of the computational bottlenecks in OmniNeRF that make it less suitable for high-resolution panoramic lifting would be insightful.
3. More visual results in the main text would be nice.

### Questions
My main concern is the lack of baselines in the paper but the problem statement, conceptualization and results are very convincing hence the accept rating.

Question(s):
Q1. What is the processing times per generation on the A100 used? I would also be interested in knowing how memory intensive it is.
Q2. If more baselines are added (see weaknesses), I would be willing to upgrade my recommendation score to 8.

Suggestion(s):
* L295: Fix typo: biuld -> build
* The space is low but can the authors somehow manage to split the Evaluation paragraph starting on L407? (split at the each underlined term)

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper first proposes a method, 4D4KGen, which can generate immersive 360-degree, 4K panoramic 4D videos from a single 4K static panoramic image. The method first uses the pre-trained perspective video generative model AnimateAnything to create a panoramic video through a project-and-fuse scheme with a spherical latent space. Next, the pretrained monocular depth estimator MiDaS is used to create a panoramic depth map with a spherical representation. Finally, the 4D animated panoramic videos are rendered using reconstructed 3DGS. Qualitative results show that the proposed method can effectively generate immersive 360-degree 4D panoramic videos.

### Strengths
(1) The paper first proposes animatable 360-degree 4K panoramic images. 

(2) To create 360-degree panorama with fixed-size pretrained video generation and depth estimation models, the authors carefully design the projection function. 

(3) The qualtative results shows that great spatial and temporal consistency.

### Weaknesses
(1) I understand that there is no metric to evaluate 360-degree panoramic images, but there is insufficient basis for measuring FID and KID between the generated frames and the corresponding perspective images projected from the static panoramas. In particular, these metrics may be meaningless when the reference set is small, and in this paper, only 16 panoramic videos were generated. Proposing and measuring such less meaningful metrics, especially when this paper aims to serve as a baseline for future 4D 360-degree panorama video generation, does not seem beneficial for subsequent research. Additionally, if we want to assess the fidelity of the generated video, we could measure FVD [1] and KVD [1]. Therefore, I recommend removing FID and KID.

(2) I don't know how long the proposed method takes, but generating only 16 videos seems too few. To demonstrate that the proposed method works generally on many 4K 360-degree panoramic images, it would be better to generate more videos (at least 30 or more) to measure quantitative results.

(3) In Sec. 4.3 Ablation Studies, a straightforward approach would be to apply animators directly to the entire panorama as the direct baseline, measured by the Q-Align metrics (IQ, IA, and VQ) and also through a user study. If 2D animators cause out-of-memory issues, we can simply upsample each frame of the videos using a super-resolution (upsampling) model such as StableSR [2].

(4) In Fig. 6, Ablation of the Lifting Phase, I find it difficult to visually discern the difference between the proposed temporal regularization and Spatial-Temporal Geometry Alignment (STA). The authors should have included a video of this in the supplementary materials or shown a more definitive difference in the figure.

(5) Since the paper's topic is closely related to panoramic image generation, the following papers [3, 4, 5] should be mentioned in the related work section.

(6) Please double-check the citations (bibtex) to confirm which papers were accepted by specific conferences. Too many papers published in conferences are listed as arXiv.

### Questions
(1) How much time and GPU memory are required to generate a single 4K video?

### Soundness
3

### Presentation
2

### Contribution
3
