# H2O-SDF: Two-phase Learning for 3D Indoor Reconstruction using Object Surface Fields

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Advanced techniques using Neural Radiance Fields (NeRF), Signed Distance Fields (SDF), and Occupancy Fields have recently emerged as solutions for 3D indoor scene reconstruction. We introduce a novel two-phase learning approach, $\text{H}_2\text{O-SDF}$,  that discriminates between object and non-object regions within indoor environments. This method achieves a nuanced balance, carefully preserving the geometric integrity of room layouts while also capturing intricate surface details of specific objects. A cornerstone of our two-phase learning framework is the introduction of the Object Surface Field (OSF), a novel concept designed to mitigate the persistent vanishing gradient problem that has previously hindered the capture of high-frequency details in other methods. Our proposed approach is validated through several experiments that include ablation studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a two-phase framework (H2O-SDF) for 3D indoor scene reconstruction. In particular, the proposed method adopts a two-stage method, which consists of one-stage reconstruction for the scene layout followed by a second-stage reconstruction of the objects using NERF. The key contribution is to introduce the concept of the object surface field. The 2D and 3D object surface losses are introduced to estimate the SDF for fine object surface details. The experiments are conducted on ScanNet and show superior results compared with existing methods.

### Strengths
+ The method reconstruct the layout and the object separately and achieves very good reconstruction on the details of the objects.
+ The introduced OSF captures the occupancy of the surface of the 3D object.
+ The introduced two losses let the SDF captured more surface details.

### Weaknesses
-	2D object surface loss. Could it be explained as the loss between the rendered object masks and the ground truth masks? It would be great to make it clear that the proposed method actually requires object annotations. The current description leaves ambiguity regarding the source of the 2D object masks and whether the method relies on pre-existing object instance segmentations or if it generates them internally. The paper should explicitly state if object instance annotations are required during training or if a pre-trained model is used to generate pseudo-ground truth masks.
-	It would be great to explain OSF with more details. Based on the description in the paper, it is quite similar to the absolute gradient field of the occupancy values. In particular, Eq. 3 actually enforces the OSF to have large values on the object defined by the 3D points.  In addition, 3D points provide strong prior on the details of the shapes. It would be great to provide the ablations study of using the point cloud with MVS images or not. The explanation of OSF is not sufficiently detailed, and its relationship to the SDF gradient is unclear. The paper needs to clarify how OSF differs from a simple gradient field and why it is a more effective representation for capturing object surface details. Furthermore, the impact of the 3D point cloud derived from MVS images needs to be isolated to understand the true contribution of OSF.
-	Experiments on ablations studies. It is not clear to the reviewer what model A, B, C are. It would be great to provide detailed explanations about those models. The current ablation study lacks clarity regarding the specific configurations of models A, B, and C. The paper should provide a detailed description of each model, including the specific components and training procedures, to enable a proper understanding of the ablation study.
-	For the second stage, it would be great to ablate whether all the losses have contributed to the final results. The proposed method adopts more accurate point cloud obtained from MVS images compared with monocular depth estimated from a single image. Those factors should be ablated to demonstrate the performance benefits from OSF and the sampling strategy not from the prior data. It is crucial to demonstrate the individual contributions of each loss function in the second stage. The paper should also ablate the influence of the MVS point cloud to isolate the performance gains due to the proposed OSF and sampling strategy from the benefits of more accurate geometric priors.

### Questions
- It would be great to elaborate more on the insight of OSF and also compared with existing density functions parameterised with the SDF values. 
- The ablations studies are missing. Please demonstrate all the losses introduced in stage two all contributes to the improvement of the reconstruction. In addition the proposed method leverages the point cloud obtained from MVS. It would be great to show how these priors can influence the final performance.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes a two-phase learning approach named H2O-SDF that combines both holistic surface learning and object surface learning, for 3D reconstruction in indoor environments. 

The main contributions are: 1) a two-phase learning framework that balances between the reconstruction of global room geometry and local object details. 2) Introduction of Object Surface Field (OSF), a new concept designed to address the vanishing gradient problem suffered by SDF, which hinders the reconstruction of high-frequency details. The authors also introduce an OSF-guided sampling strategy to prioritize object surfaces in the sampling process.

### Strengths
1. This paper tackle an important issue in the field of 3D indoor scene reconstruction — the difficulty of preserving the overall geometry while capturing intricate object details. It introduces a two-phase learning approach, which has not been explored before. 
2. The OSF concept is new and shows promising results in handling the inherent vanishing gradient issue in the learning process.
3. It is an interesting idea to use normal uncertainty as a guidance to re-weight normal and color loss, to adaptively moderate normal and color losses in both low-texture and texture-rich regions.
4. The submission appears to be well-organized with its ideas clearly articulated.
5. Experimental evaluations, together with ablation studies, confirm the effectiveness of H2O-SDF. The results show that the proposed solution outperforms existing state-of-the-art methods.

### Weaknesses
1. The explanation and exposition of some key, novel concepts, such as OSF, L2D_OSF, L3D_OSF, could be more thorough. There is insufficient mathematical detail on the OSF guided sampling strategy (although there is graphical illustration in the appendix A2, the explanation seems to be mostly a repetition of the main body). Strengths of the proposed formulation could be better appreciated by providing more detailed explanations and mathematical insights. Specifically, the paper lacks a rigorous definition of how the Object Surface Field (OSF) is mathematically formulated, and how it relates to the standard Signed Distance Function (SDF). The description of L2D_OSF and L3D_OSF also needs more clarity, particularly regarding how these are derived from the OSF and how they contribute to the overall objective function. The OSF-guided sampling strategy is presented conceptually, but the lack of a precise mathematical formulation makes it difficult to fully understand its effectiveness and potential limitations. For instance, how exactly is the sampling probability distribution derived from the OSF, and what are the implications of this distribution on the convergence and accuracy of the model? 

2. Running time: The paper does not provide specific details about the computational complexity or running time of the approach, for both training and inference.  It only states that all experiments were conducted on a single NVIDIA RTX 3090Ti GPU.

3. Comparison with more diverse data (this is more of a suggestion): While the paper compares favorably to state-of-the-art methods on the ScanNet dataset, it would strengthen the paper to include a broader range of data under different conditions, such as different indoor layout complexities, object variations etc.

### Questions
1. It would be interesting to find out to what extent this method relies on pre-trained models and priors, which might limit its application in environments where such models are not easily available.

2. Running time/computational complexity of the proposed method. Please refer to point 2 under Weaknesses.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a neural 3D indoor reconstruction framework to reconstruct 3D mesh of indoor scenes with a volume rendering framework. The key motivation of this paper is to decouple the learning of the layout and object with two stages. In the first stage, the layout of the scene is trained with an uncertainty-aware rendering loss function on both color and normal prediction. In the second stage, a new term named Object surface field (OSF) is introduced to measure the object occupancy of a 3D point, and authors demonstrate how SDF will facilitate SDF with the presented mutual induction. Extensive experiments on ScanNet have showcased the effectiveness of the proposed framework over different state-of-the-art (SOTA) methods.

### Strengths
(1) The motivation to decouple the learning of layout and object into two stage is straightforward and clear. The layout contains planar areas and the objects may have more high-frequency signals, thus may have different pace of convergence.

(2) The introduction of OSF is novel, and how the OSF can be transformed back to SDF and assist its representation is technically sound.

(3) Experiments on ScanNet have shown the advantages of proposed components of the method.

### Weaknesses
 (1) The major concern for me is that of the technical impact of this work is limited by introducing a normal estimation network [1] which is also trained on ScanNet, to provide pseudo groundtruth normal and uncertainty during training. This cannot ensure fairness among baseline comparison and highly constraints the generalizability of the proposed method onto different benchmarks. A fair setting would be replace this network with another model or method which is pretrained on other datasets, or alternatively, test this method onto other indoor datasets such as 7-Scenes. This will significantly improve the fairness and technical impact of this work.

(2) In the supplementary material, authors present that they apply the OSF-based Filtering during reconstruction. I am curious about where does the major improvement of OSF comes from, either the proposed osf loss or the filtering. Authors are expected to conduct ablation study about this to make the contribution more convincing.

(3) Minor: The presentation can be further improved, and there exists noticeable typos in the submission such as Table 2.

### Questions
I appreciate the motivation of the design of this paper, however the use of a model seen on the same dataset limits the value of the proposed method. I would consider to improve my rating if my concerns listed in the weaknesses part can be well addressed.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes follow-up method to the SDF-based NeRF-like methods for indoor reconstruction, with a focus to improve geometry on objects in the second phase of optimization. The main novelty is the introduction of the auxiliary representation of Object Surface Field (OSF), which is activated on object surfaces. OSF can learned with 2D supervision of instance segmentation, as well as a loss in 3D which jointly constrain the SDF field and OSF field, bringing about zeros of SDF around object surfaces, leading to improved reconstruction on detailed high-frequency object parts. The method is evaluated against baseline SDF-based NeRF-like methods, on scenes including ScanNet and Replica.

### Strengths
[1] The proposal of using instance segmentation as additional input to the pipeline, as well as designing effective supervision signals with input segmentation. 

Despite it is not new to use additional signals to the task (e.g. monocular normal and depth supervision for 2D-3D consistency, sparse points to supervise local SDF values, and using semantics and planar assumptions improve geometry of layouts), the paper is one of the first to demonstrate the usage of instance segmentation to improve fine geometry. More importantly, the paper does so in a non-trivial way, by introducing OSF to explicitly evolve object surfaces using a 2D loss between the input segmentation and OSF as well as a 3D loss between OSF and SDF.

[2] Illustration of the relationship of OSF and SDF (and the gradients), and the use of the OSF to drive SDF.

The paper provides informative illustration in Fig. 4 and related text on the relationship of OSF and SDF and how does the optimization of OSF loss drive SDF towards zero point around surfaces. The illustration using examples and 1D figures is clear and supports the motivation of the design of OSF.

[3] Extensive evaluation of the proposed method against baseline methods, and on more than one datasets.

### Weaknesses
[1] Clarification on OSF. Despite the good illustration of OSF as mentioned above, extra clarification is urgently needed to explain the motivation of the mathematical form of the 3D OSF loss (Equ. 2), and details in Fig. 4.

Specifically, despite Fig. 4 explains how the gradients of the 3 loss drives SDF to form a zero points around surfaces, and paper does not provide intuitive explanation on (a) why the various terms of the loss in Equ. 2 are designed as they are, (b) how \gamma controls the steepness of the function, how it matters and how $\gamma$ is picked (better with illustrations similar to Fig. 4). Additionally, it is not clear that, between Fig. 4 (a) and (c), why different d(x) lead to identical $\sigma_\gamma(x)$. Without clarifying the issues it is difficult to understand why OSF and the losses are designed the way they are, despite being proven effective.

[2] Demonstration of applying the proposed OSF and losses general SDF-like NeRF-based methods. The proposed OSF and losses should theoretically be applicable to all of the baselines methods as simple drop-in, but somehow the paper decides to compare against its own vanilla baseline. Is it possible to apply to other existing methods to better showcase the general nature of the proposed method, and how effective will it be?

[3] Limited scenes to evaluate. The main evaluation is done on ScanNet, with limited qualitative results on Replica. However ScanNet is known to have image quality issues. Why is the method not evaluated and compared on alternative datasets including Replica, Tanks & Temples, etc, as is done in other papers like MonoSDF? Without the additional evaluation, it is difficult to decide the generalization of the method across various indoor scenes.

[4] Additional comparison. One less important thing to add is, potential comparison with I^2-SDF. Despite I^2-SDF is based on additional geometry supervision signals, the goal is aligned with the proposed method, and it showcases similar improvement in fine detailed objects. It would be beneficial to add comparison to I^2-SDF to inspire the discussion on optimal strategy to improve reconstruction of high frequency signals in indoor geometry.

### Questions
Please see the Weakness section for questions to address.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
