# LEAP: Liberate Sparse-View 3D Modeling from Camera Poses

- Decision: Accept
- Avg Score: 5.20
- Scores: 6, 6, 5, 1, 8

## Abstract
Are camera poses necessary for multi-view 3D modeling?
Existing approaches predominantly assume access to accurate camera poses. While this assumption might hold for dense views, accurately estimating camera poses for sparse views is often elusive.
Our analysis reveals that noisy estimated poses lead to degraded performance for existing sparse-view 3D modeling methods.
To address this issue, we present \modelname{}, a novel \textit{pose-free} approach, therefore challenging the prevailing notion that camera poses are indispensable.
\modelname{} discards pose-based operations and learns geometric knowledge from data. \modelname{} is equipped with a neural volume, which is shared across scenes and is parameterized to encode geometry and texture priors. For each incoming scene, we update the neural volume by aggregating 2D image features in a feature-similarity-driven manner. The updated neural volume is decoded into the radiance field, enabling novel view synthesis from any viewpoint.
On both object-centric and scene-level datasets, we show that \modelname{} significantly outperforms prior methods when they employ predicted poses from state-of-the-art pose estimators.
Notably, \modelname{} performs on par with prior approaches that use ground-truth poses while running $400\times$ faster than PixelNeRF.
We show \modelname{} generalizes to novel object categories and scenes, and learns knowledge closely resembles epipolar geometry.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed LEAP, a pose-free approach for 3D modeling from a set of unposed sparse-view images. By appropriately setting the 3D coordinate and aggregating 2D image features, LEAP demonstrates satisfying novel view synthesis quality.

### Strengths
++ As a pose-free approach, LEAP discards pose-based operations and learns geometric knowledge from data. 

++ LEAP is equipped with a neural volume, which is shared across scenes and is parameterized to encode geometry
and texture priors. For each incoming scene, it updated the neural volume by aggregating 2D image features in a feature-similarity-driven manner. The updated neural volume is decoded into the radiance field, enabling novel view synthesis from any viewpoint.

++ The experimental evaluations and ablation studies are extensive.

### Weaknesses
-- Novel view synthesis is defined as rendering the images as specific camera pose and time (for dynamic scenes). When the camera poses are not avaliable or not estimated as this paper, how to deal with NVS with given camera poses, i.e., how to align the given camera poses with the training set images.

-- Essentially, the method incoorporated the feature correspondences into the overall optimization, it is thus interesting to make comparisons with estimated correspondences from optical flow where the dense matching is learned.

-- It is worth to compare related work such as Unposed NERF to verify the effectiveness of the proposed method.

### Questions
Please refer to my questions as listed in the above Weaknesses section.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a pose-free method for novel view synthesis in sparse-view settings. Unlike previous methods that estimate/optimise camera poses, the proposed approach uses a novel transformer-based 2D-3D mapping method to aggregate 2D image features in 3D space. After training in large-scale data with ground-truth poses, the method is able to generalize to new scenes without the pose input. It shows that the proposed method outperforms previous approaches that use estimated camera poses in both object-level and scene-level datasets.

### Strengths
1. The idea is novel. Unlike previous methods that try to predict or estimate camera poses in sparse views, the proposed method completely did not use camera pose to build the 3D volume representation.

2. The paper is well-written. It is easy to read and understand the motivation, background, problem, and high-level ideas to address the challenge.

3. The proposed multi-view encoder and the 2d-3d information mapping layers are novel, and efficacy has been demonstrated in the ablation study.

4. The experimental results are evaluated in both object-level and scene-level datasets, and it shows that the proposed method outperforms previous methods when they use estimated camera poses.

### Weaknesses
1. Unlike the traditional pose-based projection, the proposed 2D-3D mapping layers are a weighted fusion of 2D features. The mapping may be more robust than pose-based projection when the pose is inaccurate but it limits in accuracy. Consequently, the reconstruction and rendering are often blurred, as shown in Figure 6. The weighted fusion approach, while robust to pose errors, inherently smooths out high-frequency details, leading to the observed blurriness. This is a fundamental limitation of the method, as it trades off accuracy for robustness. The authors should discuss the theoretical limits of this approach in terms of achievable reconstruction fidelity.

2. Sparse-view reconstruction is an ill-posed problem because the input images contain incomplete scene information. Although the proposed method is better than previous approaches, the performance is still very limited. In this scenario, most of the existing methods can refine the results by using more input images. However, the proposed method only aggregates information and runs forward pass at the inference time. Is it possible to do refinement when more input images are given? The lack of iterative refinement is a significant drawback, as it prevents the method from leveraging additional information to improve the reconstruction quality. The authors should explore techniques to incorporate iterative refinement into their framework, possibly by using the initial reconstruction as a prior for subsequent refinement steps.

3. Does the proposed method work well with different frame numbers during inference time? As the proposed 2d-3d mapping needs aggregating information from all frames, does it consume huge memory in dense views (e.g., more than 100 frames)? The computational cost and memory consumption of aggregating information from a large number of frames is a major concern. The authors should provide a detailed analysis of the method's scalability with respect to the number of input views, including memory usage and runtime performance. This is especially important for practical applications where the number of input views may vary significantly.

### Questions
See weakness.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new methodology designed to transition Nerf from a pose-based optimization framework to a pose-independent reconstruction paradigm. Within the fusion phase, the network generates a feature volume, with the initial view serving as the canonical reference point, subsequently integrating further perspectives by means of feature matching between the 3D volume and 2D image feature similarity. This design ensures that the entire process remains agnostic to pose, obviating the necessity for explicit pose optimization.

The paper conducts an exhaustive series of experiments to substantiate the robustness and efficacy of the proposed methodology, employing both object-centric and scene-centric datasets. The findings conclusively demonstrate that the proposed approach yields results on par with previous works that rely on ground-truth poses, while exhibiting superior generalizability in comparison to its predecessors.

### Strengths
Originality:
The reviewer did not identify a comparable concept within the existing literature, suggesting that the idea presented in this paper is novel and distinctive. Furthermore, the concept exhibits significant potential for broader applications across various use cases, further underscoring its relevance and practical utility.

Clarity:
The problem statement, literature review, and a portion of the methods and experimental details are clear to me.

Quality and significance:
The paper exhibits a well-structured organization that facilitates ease of comprehension. The experimental design effectively showcases the efficacy of the proposed methodology.

### Weaknesses
1. Clarity in the exposition of the method's approach to generating predicted images during the optimization process would be beneficial.
2. It would be advantageous if the paper delved deeper into the reasons behind its enhanced speed and the trade-offs involved in achieving such acceleration.
3. The proposed methodology presents certain limitations, particularly concerning relative poses. A more detailed exploration of how the network achieves accurate scale predictions without pose information would be insightful.

### Questions
The paper is not well written:
1. Concerning the proposed methodology, the process of generating predictions remains unclear. Specifically, after enhancing the 3D neural volume, how is the establishment of a 2D to 3D association executed for rendering the input view during optimization? Regrettably, this paper does not provide a satisfactory response to this inquiry.

2. A noticeable absence of local consistency, which is essential for ensuring a robust 3D to 2D association, prompts the question of how the proposed approach manages challenges such as occlusion and variations in lighting conditions. Clarity regarding the method's strategy for addressing these issues would be greatly appreciated.

3. The impact of an increasing number of input views on the method's prediction accuracy compared to baseline methods remains unaddressed. It is crucial to understand whether the accuracy is expected to decrease or improve with a greater quantity of input views. The author's insights on this matter would be valuable.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Summary**: The paper proposes a 3D modelling method that predicts a NeRF volume from sparse input views without requiring camera poses at inference time. 

**Method**: The main contribution is proposing an attention-based structure and a feature volume to associates image features across all views and between 2D and 3D. Essentially the method is similar to PixelNeRF and IBRNet, but does not need camera poses at inference time. 

**Evaluation**: The evaluation is comprehensive and convincing. It would be better to add some cross-dataset evaluation.

### Strengths
1. The paper is well written and easy to follow.
2. Code is provided in supplementary.
3. The proposed method is novel. The proposed method alleviates the need of camera poses while being simple and effective, by applying attention across image features from all source views and attention between a feature volume and source views.
4. The evaluation is convincing. The paper shows clear improvement comparing with previous methods and offers extensive analysis and discussions.

### Weaknesses
While the experiment is convincing, it appears to me that all experiments are trained and evaluated on train/test splits of same datasets. It would be interesting to see cross dataset performance and a comparison between other method, i.e. training on dataset A and evaluating on dataset B.

A minor issue: missing a reference to *Sajjadi, Mehdi SM, Aravindh Mahendran, Thomas Kipf, Etienne Pot, Daniel Duckworth, Mario Lučić, and Klaus Greff. "RUST: Latent Neural Scene Representations from Unposed Imagery." In CVPR 2023*.

### Questions
See weakness section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper describes LEAP, a method for novel view synthesis from 5 or fewer images. Unlike other novel view synthesis methods, LEAP does not require camera poses to be provided at test time. However, LEAP still requires camera poses at training time.
​
LEAP generates novel views using a sequence of image- and voxel-based attention layers. Given a set of input views, it arbitrarily designates one view as the canonical view. It uses this view to define a world coordinate space in which novel views can be queried. After having picked the canonical view, LEAP encodes the context views, alternating between self-attention among all views and cross-attention between queries from the non-canonical views and keys/values from the canonical view. It then lifts the resulting image features to 3D via cross-attention between learned (shared across scenes) query tokens in a 3D voxel grid and key/value tokens from the images. Finally, it maps the voxel grid's features to a density and renderable feature at each location, uses NeRF-style volumetric rendering to composite these features, and finally converts the rendered features to an RGB image using a 2D convolutional network.
​
LEAP is trained using a mean-squared error loss on RGB values, an image-based perceptual loss, and a mask loss (if masks are available). It is important to note that although the rendering process itself does not require camera poses, the training process does, since the views that are rendered to compute these losses are queried using known poses.
​

### Strengths
​* LEAP is among the first methods that perform novel view synthesis without known poses at test time. While SRT also performs novel view synthesis without known poses at test time, LEAP has better results on object-level scenes and guarantees consistency between viewpoints by using an explicit 3D representation.
* The authors provide video results that convincingly show LEAP working qualitatively on a large number of objects.
* LEAP outperforms the provided baselines on object-level scenes.
* The description of the method is clear and easy to follow. Additionally, the authors provide concise code for the LEAP model that is helpful for understanding the details.

### Weaknesses
 * The authors claim that they significantly outperform prior methods on scene-scale datasets. However, LEAP only presents a comparison on the small DTU dataset. This comparison is somewhat flawed, since it prevents the authors from benchmarking against SRT, which is focused on scene-scale novel view synthesis. It would be much more convincing to see results on MultiShapeNet, which is a publicly available scene-scale dataset that SRT is trained and compared on. Showing more scene-scale results seems particularly important because LEAP's use of a 3D voxel grid with fixed extents seems likely to limit its usefulness on scene-scale datasets. It is also worth noting that the scenes in the DTU dataset have small camera baselines, meaning that classical pose estimation would produce near-perfect estimated poses on DTU. Using a wide-baseline dataset for scene-scale comparison (where pose estimation is more likely to fail) would be more convincing.
* Figure 8 appears to be flawed and somewhat misleading. The experiment setup, as I understand it, is that the authors feed a synthetic scene consisting of a single dot projected onto five images into a trained LEAP network. The authors show that the neural volume's density is highest along the ray that corresponds to the dot's location in the canonical view. This is good evidence that the network has "understood" the meaning of the canonical view and has learned to map pixels to rays within the volume. However, the authors claim that the network then "leverages the multi-view information to resolve the depth ambiguity of the ray." However, estimating pose given images of a single dot is impossible, since the scene's appearance is invariant to rotation around the dot. Since pose and correspondence are both needed to correctly place a 3D point, this means that in this case, the network cannot actually be doing what the authors claim. It seems much more likely that because the training dataset consisted of objects/surfaces that were all at roughly the same depth, the network is simply placing the dot near the mean of those depths.
* The authors should explicitly clarify both in the intro and the methods section that their method requires camera poses at training time. Currently, the first sentence of section 3 might suggest that their method doesn't require poses at training time either.
* The authors cannot both claim that their method is the first to introduce the pose-free paradigm (first paragraph, page 4) while also stating that the SRT already introduced the same paradigm (which it very much did). The authors should soften that claim to saying that they merely implement a new way of solving this pose-free problem, rather than introducing it.



### Questions
* Was the SRT used for comparison trained for long enough? In particular, how many training steps were used for the SRT? The SRT results shown here are significantly blurrier than those shown in the SRT paper.
* Is rendering features and decoding them with a CNN to produce the final image necessary? I would be curious to see an ablation regarding this design choice.
* Does LEAP show any robustness to noisy views at training time?
* How does the cross-attention layer (equation 1) compare with simply concatenating learnable vectors for canonical vs. non-canonical views to the transformer tokens when using self-attention (equation 2)?
* Can a trained LEAP network be fine-tuned to estimate pose? It would be very interesting to see if a pose estimation network/head could be trained on top of LEAP image features from just before the 3D lifting step. The RUST paper contains a similar experiment.

Please also address the weaknesses in the "weaknesses" section.


______

I thank the authors for addressing my questions. I have updated my score accordingly, and recommend acceptance of the paper!

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
