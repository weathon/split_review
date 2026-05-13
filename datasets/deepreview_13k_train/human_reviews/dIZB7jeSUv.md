# CamI2V: Camera-Controlled Image-to-Video Diffusion Model

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Recent advancements have integrated camera pose as a user-friendly and physics-informed condition in video diffusion models, enabling precise camera control. In this paper, we identify one of the key challenges as effectively modeling noisy cross-frame interactions to enhance geometry consistency and camera controllability. We innovatively associate the quality of a condition with its ability to reduce uncertainty and interpret noisy cross-frame features as a form of noisy condition. Recognizing that noisy conditions provide deterministic information while also introducing randomness and potential misguidance due to added noise, we propose applying epipolar attention to only aggregate features along corresponding epipolar lines, thereby accessing an optimal amount of noisy conditions. Additionally, we address scenarios where epipolar lines disappear, commonly caused by rapid camera movements, dynamic objects, or occlusions, ensuring robust performance in diverse environments.
Furthermore, we develop a more robust and reproducible evaluation pipeline to address the inaccuracies and instabilities of existing camera control metrics. Our method achieves a 25.64\% improvement in camera controllability on the RealEstate10K dataset without compromising dynamics or generation quality and demonstrates strong generalization to out-of-domain images. Training and inference require only 24GB and 12GB of memory, respectively, for 16-frame sequences at 256×256 resolution. We will release all checkpoints, along with training and evaluation code. Dynamic videos are best viewed at  \url{https://zgctroy.io/CamI2V}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper extends an existing I2V method (DynamiCrafter) to accept additional camera viewpoint control. The input cameras are parameterized as Plücker rays, serving as a position encoding. The authors additionally inset learnable Epipolar attention layers before temporal attn, which explicitly model cross-view geometry to further enhance the adherence to the input camera.

### Strengths
The paper is well written with a few nicely created figures, e.g., Fig. 1 and Fig. 2. The ideas of (1) clean vs. noisy condition & (2) register tokens are neat (but they are also related to the weakness and questions below). Despite tuned with static/rigid scene dataset -- RealEstate10k, from the few generated videos in the supplementary, the motion dynamic of foreground is not lost too much. The discussion in L457-479 is good and clearly supports the design choices. For fair comparison, the authors spend effort reproducing the recipes of baselines (MotionCtrl and CameraCtrl) in their framework (instead of applying the released ckpt out of the box) such that they all stand on a common ground.

### Weaknesses
 * Contribution is clearly articulated in L.135-139 but not verified in the experiment: using Plücker embedding and/or epipolar attention has become a norm in the 3D generation literature, e.g. [1]. Applying one of them, if not both, in the video generation field has also been done, e.g., CameraCtrl, CamCo etc. Therefore, the biggest technical contribution I see in this work, to my knowledge, is applying the idea of register tokens to account for occlusion, zero epipolar scenarios, etc. Despite simple, I find this idea neat, but I don't see any experiments ablating this key idea to analyze the effect. A contribution/novelty has be verified by the experiments. If this concern can be addressed, I am happy to raise the rating.

* Method description is a bit insufficient. I need to read Sec. 5.3 to realize Plücker rays are also used as global positional encoding similar to CameraCtrl. This is also part of the final method so it has to be described in Section 3.  The lack of clarity in Section 3 regarding the dual use of Plücker embeddings, both as a positional encoding and within the epipolar attention mechanism, makes it difficult to fully grasp the method's architecture and novelty. Specifically, the method description should explicitly state that the Plücker embedding serves as a global positional encoding, similar to CameraCtrl, and also as an input to the epipolar attention layers. This dual role is crucial for understanding the method's design and should be clearly presented in the main method section, not buried in the experimental details.

### Questions
1. The concept of clean vs. noisy conditions is also neat. The authors even make a figure to illustrate it (Fig. 1), but the knowledge of clean vs. noisy conditions seems not fully exploited in the method? For example, Fig. 1 points out that text and RT are clean conditions, but I don't see this new insight leads to new architectural designs? Adding camera information through Plücker embedding and epipolar attention is a natural choice due to the nature of multi-view geometry, not because it is a clean condition. I wonder if making such separation is really necessary in the exposition.  (This is more of a question for presentation, not technical details.) 

2. More generated video results. All video examples in the supplementary material show only zooming-out camera motion, which, in my experience, is the easiest one to be learnt by the network. Please provide other examples, such as panning left/right, moving up/down, etc.

### Soundness
3

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
The paper proposes a new method to inject camera pose conditions for controlled video generation using a diffusion model. The method uses Plücker coordinates to represent the camera rays and introduces epi-polar mask attention for cross-view attention, which is more efficient than the full 3D attention counterpart. The proposed method is evaluated on the RealEstate10K dataset and achieves state-of-the-art performance.

### Strengths
+ The epi-polar mask attention layer proposed in the paper helps to enhance the camera control ability for video diffusion models. Also, it is plug-and-play – we don't need to retrain other modules of the original pretrained VDM.

+ It is an interesting idea to include the register token to handle cases where the epipolar constraint on correspondences fails, although more discussion and evaluation on it are needed (see the weakness section).

+ The paper addresses the inaccuracy in the SfM for robust evaluation metrics. Specifically, GLOMAP, a more state-of-the-art dense SfM pipeline, is used to validate the camera pose consistency.

### Weaknesses
 + Discussion and experiment missing for a key statement in the paper: While the paper states (in L112) that register tokens are included to handle rapid camera movements, occlusions, and dynamic objects, this contribution (also the key difference from CamCo) is not discussed in more detail. For example, how does this additional token help to deal with the non-epipolar constrained correspondences? Can the image-level register token handle pixel-level dense correspondences across frames (like moving arms of people)? In addition, the register token is not ablated, so it’s unclear if it actually helps for dynamic scene generation. Furthermore, since this is the key difference from CamCo, more discussion and evaluation could help to distinguish this submission from CamCo.

+ Some parts of the presentation are confusing: While the discussion in Fig. 1 and Sec. 1 on different types of conditions based on how much uncertainty the condition can reduce is interesting, how is that related to the epipolar condition? Does the epipolar condition reduce more uncertainty, hence making it a good condition? How does this view of condition serve as a principle to introduce the epipolar condition in the paper? More clarification is needed.

+ For the quantitative results, cross-view consistency is missing, although it has been highlighted in the qualitative subsection (Fig. 7). Is there any reason why it is ignored in the tables as a metric? Cross-frame consistency can be another useful metric to show how the epipolar attention helps, in addition to camera controllability.

+ In Fig. 5, the multi-resolution epipolar mask is shown but not discussed in the text. What is the motivation for using a multi-resolution epipolar mask? Specifically, how do different resolutions of the epipolar mask affect the attention mechanism and the final video generation quality? Does applying the epipolar constraint at multiple resolutions offer any advantage over applying it at a single resolution, and if so, what is the trade-off?

### Questions
Please refer to the weakness section above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces CAMI2V, a camera controlled I2V model that integrates several camera-based components, such as epipolar attention and plucker embeddings, image conditions and text prompts.

### Strengths
The paper is easy to follow, figures are intuitive and look good. 

Experiments shows the model outperforms all available state-of-the-art works.

### Weaknesses
Novelty of the paper: The contribution of this paper highly resembles CamCo, which is released in June (3.5 months prior to the submission deadline). Both methods use plucker embedding, epipolar lines, and are aimed for image-2-video model. The paper mentioned that CamCo does not supports video trajectories with non-overlapping frames, and the introduction of register token alleviate this problem. Yet this can be  considered as a relatively minor improvement, and is not well supported by experiments. While CamCo does not release its code for reproduction, an ablation study on the token (comparing to other trivial techniques, such as averaging all K/V together), might be helpful to show its effectiveness. Aside from CamCo, CVD (Kuang et.al. 2024) also applies the epipolar attention in its cross-view modules, and CameraCtrl/CVD both use plucker embedding. All these methods challenge the novelty of this work. 

While many of the components proposed by the paper are originated from other prior works, the paper spent a huge portion of space to explain these components, overcomplicating the model itself. For example, in Figure 1/2 the authors try to analyze the differences between image/text conditions and noisy latents and show the importance of the epipolar attention, and later provides very detailed calculation on how to compute the attention maps. These contents are somehow redundant since they are already been proposed in prior works. 

The author also claims the improvement of the evaluation protocol as one of the major contributions, yet the changes are rather trivial. It only replaces COLMAP with GLOMAP, and fixing the GT camera parameters to the registration. 

All of the examples shown in the paper are in relatively small camera changes, which does not support the claims that CAMI2V can handle large camera movements with non-overlapped area. One of the example in Ours_I2V_on_unseen_image_3.gif also shows strong inconsistency across frames (5’th one from the left)

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper retrofits the text-guided video diffusion model with a camera control module, enhancing the camera trajectory controllability and 3D consistency for image animation. 

By representing a pinhole camera model as a bundle of ray-level 3D embeddings through Pl&uuml;cker coordinates, the denoising process is conditioned on camera poses in a _clean_ and expressive manner. To facilitate multi-view 3D reasoning and efficiency, the epipolar attention mechanism is developed, which only aggregates cross-view information within a limited region along the epipolar line. 

The authors test the method on RealEstate10K and out-of-domain datasets using an improved evaluation pipeline, and demonstrate its superiority over other alternatives.

### Strengths
- The idea of introducing epipolar geometry to the temporal attention is straightforward and well-motivated, which allows the model to explicitly reason about the 3D world.
- It is interesting and technically sound to configure register tokens for degenerate cases where no corresponding epipolar lines are detected.
- Experiments on RealEstate10K and in the wild have shown that the proposed method improves the camera motion controllability and stability.

### Weaknesses
 - One major concern is that the proposed method is somewhat lack of novelty. The epipolar attention mechanism is not new [1], while the Plücker embedding is adopted from [2].  There are some impressive innovations, e.g. the concept of _clean/noised conditions_ and the register tokens, but related exposition and analysis could be more thorough. Please see Q1-5 in the question section for details.
- In the conclusion, the authors announce that their method _significantly_ improves the controllability and stability (Line 534-535), which may be an overstatement. In Tab.1, the advantage of CamI2V (the proposed method) over CameraCtrl is kind of minor, and in Tab.2, the introduction of the epipolar attention quantitatively appears to bring in only limited improvement. It would be nice to include additional (qualitative) results that demonstrate the effectiveness of each contribution. Also see Q6.
- One contribution that the authors adapt GLOMAP for more robust evaluation pipeline raises another concern. It is not convincing that GLOMAP can effectively address limitations such as low resolution and dynamic scenarios. More details and experimental comparisons would be helpful to demonstrate the merits of the proposed evaluation protocol.

### Questions
1. Elaboration on the insight of the _clean/noised conditions_. The Pl&uuml;cker embeddings and the proposed epiplolar attention are regarded as clean conditions, but no further clarification is given. It would be preferable to include some mathematical analysis on how clean conditions can reduce uncertainty more effectively than noisy conditions, as the current perspective seems just intuitive and empirical rather than theoretically supported.
2. I appreciate the idea of reserving register tokens for special cases, but the authors fail to demonstrate its effectiveness through essential ablation studies. 
3. In the epipolar attention part, a hard mask strategy is employed, which filters out pixels far from epipolar lines, while [1] proposes the epipolar weight matrix (a form of soft masks). It would be interesting to draw a comparison between them. The hard mask strategy might be computationally more efficient, so for example, more specific details about the computational complexity or running time would be beneficial.
4. The epipolar geometry is based on the assumption that observations are all static. Wouldn't the proposed epipolar attention incur degradation in cases involving dynamic objects?
5. The multiple guidance scale is not only similar to [2] but also lacks explanation and experimental support. The authors should reconsider whether to count it as one contribution (Line 133-134).
6. Limited qualitative results. Camera trajectories used in supplementary materials are similar and relatively simple. Diverse camera trajectories for evaluating are in great need. 

- The authors may have to check the citation in Line 208-209: we follow _(Tseng et al., 2023)_ to represent cameras as ray bundles. 
- In the top middle of Fig. 4, what do the "Project" module and its learnable weights refer to? 
- Please check the format of notations. Make sure they are consistent throughout the paper. For example, the latent code should be in bold: $\mathbf{z}_t$.

[1] Hung-Yu Tseng, et al. "Consistent View Synthesis with Pose-Guided Diffusion Models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). 2023.

[2] Jinbo Xing, et al. "DynamiCrafter: Animating Open-domain Images with Video Diffusion Priors." Proceedings of the 18th European Conference on Computer Vision (ECCV). 2024

### Soundness
3

### Presentation
3

### Contribution
2
