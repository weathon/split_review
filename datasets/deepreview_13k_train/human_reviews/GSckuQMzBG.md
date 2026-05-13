# Scaled Inverse Graphics: Efficiently Learning Large Sets of 3D Scenes

- Decision: Reject
- Scores: 1, 1, 5, 5, 3

## Abstract
While the field of inverse graphics has been witnessing continuous growth, techniques devised thus far predominantly focus on learning individual scene representations.
In contrast, learning large sets of scenes has been a considerable bottleneck in NeRF developments, as repeatedly applying inverse graphics on a sequence of scenes, though essential for various applications, remains largely prohibitive in terms of resource costs.
We introduce a framework termed ``\emph{scaled} inverse graphics'', aimed at efficiently learning large sets of scene representations, and propose a novel method to this end.
It operates in two stages: (i) training a compression model on a subset of scenes, then (ii) training NeRF models on the resulting smaller representations, thereby reducing the optimization space per new scene.
In practice, we compact the representation of scenes by learning NeRFs in a latent space to reduce the image resolution, and sharing information across scenes to reduce NeRF representation complexity.
We experimentally show that our method presents both the lowest training time and memory footprint in scaled inverse graphics compared to other methods applied independently on each scene.
Our codebase is publicly available as open-source.
Our project page can be found at \url{https://scaled-ig.io}\ .

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces Scaled Inverse Graphics, a framework aimed at efficient large-scale 3D scene learning. The framework leverage a Micro-Macro decomposition and a two-stage training process, reducing memory use and training time. Using Tri-Planes in a latent-space auto-encoder, it achieves efficient scene representations by first learning shared features on a subset of scenes and then applying these to train remaining scenes. Experiments on ShapeNet Cars and Basel Faces validate the method’s resource efficiency and rendering quality.

### Strengths
1. The framework presents a unique decomposed scene representation, with Micro and Macro components, facilitating shared feature learning across a large dataset. This approach is novel in the context of NeRF-based methods, where scene-specific and globally shared information is seldom jointly optimized (in an explicit way).
2. The paper is well-written and well-organized. The methodology is detailed.

### Weaknesses
The major weakness of this paper is very limited experiments and analysis on the performance of the proposed method.
1. The experiments are limited to single-category datasets (e.g., cars and faces), where scene variations are relatively uniform. This narrow scope restricts its applicability for more diverse datasets with higher inter-sample variation. Without more experiments, it is impossible to fully assess the method. Demonstrating this method's capability to handle more complex, multi-category datasets would strengthen its generalizability claims. For instance, the method's performance on datasets with varying object types, textures, and lighting conditions is unknown. The current experiments do not sufficiently demonstrate the robustness of the approach.
2. The experiments are limited to object-level datasets, where the scene "scale" is relatively small. The method's ability to handle larger, more complex scenes with greater depth and spatial variation is not evaluated. This raises questions about its scalability and applicability to real-world scenarios.
3. The method is not competitive when compare to recent advances on feed-forward reconstruction pipelines (LRM-variants, multi-view 3D Gen), while the training and inference settings are similar. The latter works are more efficient and do not rely on slow volumetric rendering while handle sparse settings well. The paper does not provide a clear justification for not comparing against these more efficient methods, which are becoming increasingly popular in the field.
4. The experiments lack relevant baselines (only compared to Tri-Planes), including recent advanced NeRF-variants, 3DGS-variants, Feed-forward nerf variants (MVSNeRF), and LRM-variants and 3D generative models with image condition. The absence of these comparisons makes it difficult to assess the true contribution of the proposed method and its performance relative to the state-of-the-art.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper considers the task of distilling knowledge from a large set of 3D scenes to improve resource use at inference time. Specifically, the paper proposes to learn a tri-plane representation using an auto-encoder. The latent tri-plane is further decomposed into a global tri-plane shared across all scenes in a category and a scene-specific tri-plane. The paper’s baseline is a scene-specific tri-plane, and experiments are conducted on ShapeNet Cars and Basel Faces. The paper demonstrates that after the distillation phase, their method is significantly faster and requires fewer parameters than per-scene tri-plane while achieving similar performance.

### Strengths
* The paper is easy to read and understand. The methodology is clear and well-explained
* The explicit decomposition of shared global embeddings and scene-specific embeddings in a concatenated Tri-Plane space is interesting.

### Weaknesses
 * Lack of compelling baselines. Although the paper presents a latent NeRF, there are no latent NeRF baselines. The paper is only compared to a per-scene Tri-NeRF. Some relevant NeRF-centric papers that learn a shared representation that is then used to quickly adapt to new scenes include [1] and [2]. Arguably, any single-view or multi-view feedforward method trained using analysis-by-synthesis rendering losses (MVSplat, Pixelsplat, Splatter Image, CAT3D, SparseFusion, SRT, UP-SRT, RUST, etc) is also trained on a large set of 3D scenes and then adapted quickly to an inference scene. These would still fit into the proposed task setting and would likely be several orders of magnitude faster than the proposed method (miliseconds vs 2 min). Finally, since the method still uses 144 input views for shapenet cars and 45 for faces, any recent fast scene-specific method would perform better than Tri-Planes and be faster (a few seconds for 3DGS and InstantNGP). Yet, even with the distillation, the proposed method is not much better than the Tri-Planes baseline, performing slightly worse in LPIPS for shapenet cars.
* Weak motivation. The primary problem of reducing resource costs at inference time seems to be better solved using existing fast (3DGS, INGP) and low memory (NeRFLight) NeRFs or even distillation into smaller NeRFs (Plenoctrees). These solutions would be orders of magnitudes faster (few seconds vs 31 hours + 2.2min/scene) and lower memory (10-30MB vs 360 MB). The notable challenge described in the introduction is that “the creation of NeRF datasets, which serve as a prerequisite for training… is prohibitive, as creating large-scale datasets of implicit scene representations entails significant computational costs” [L55-58]. This problem does not seem to be addressed by this paper since it still requires constructing a large dataset for pre-training Stage 1.
* Memory costs are misleading. The paper claims that decomposing global and scene-specific parameters reduces memory footprint because it reduces trainable features by F/F_mic [L214-215]. However, this doesn’t make sense because the global features must still be stored in memory in order to decode the scene. There doesn’t seem to be any memory savings from the core technical contribution of the paper.

### Questions
What does it mean for IG-AE to be the “only available approach to build NeRF-compatible 3D-aware latent spaces” [L120-121]?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper attempts to scale neural representations of scenes, focusing on Tri-planes. Their idea is to learn a global tri-plane that is queried for all new scenes (macro), as well as per-scene tri-planes. When volume-rendering a tri-plane representation, both the macro and scene-specific micro representations are rendered, and features from both are concatenated along the feature dimension. The Macro planes are actually a collection of triplanes, and the final features from the macro planes are a weighted average. The paper shows that the overall amortized cost of the macro-micro plane approach is less than the cost of training a new independent tri-plane representation that does not benefit from having seen other scenes.

### Strengths
*I think this is a useful paper that brings scalability to tri-planes. Having the macro-micro decomposition is clearly more efficient than learning one tri-plane per scene. 
*Method is clearly explained

### Weaknesses
 *The classic tri-plane representation (EG3D) involves a single neural network generating the tri-planes from a latent code that are then rendered. Did the authors explore a single network to generate the tri-planes per scene and comparing that cost with the macro-micro approach? I believe at a minimum the authors should perform an ablation by training a single EG3D on their dataset (perhaps with varying feature dimensionality to match the macro-micro feature space).

*Line 134-138: why does the data need to be divided into two disjoint subsets?

### Questions
Line 134-138: why does the data need to be divided into two disjoint subsets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed to address the problem of nerf training for a large set of scenes. In particular, they propose to learn the Micro-macro Tri-planes, where the Macro Tri-planes capture the shared features for the scene and Micro Tri-planes captures the features for each scene. The Nerf is trained on a subset of scenes first and then fine-tuned on remaining scenes. The proposed framework is evaluated on Cars dataset from ShapeNet and front-facing Basel-Face dataset which shows similar rendering performance but reduced computational time and memory cost.

### Strengths
The proposed training strategy highly reduced the computational time and memory for nerf training using decouple Tri-plane representations- Macro and Micro Tri-planes, for large set of 3D scenes.

### Weaknesses
- Scene VS Object. The method claimed efficient learning for a large set of 3D scene but the evaluations are done only on objects. No extra experimental results are listed in the supplementary material.
- Clarification about micro and macro decomposition of Tri-Planes. The current experiments cannot explain whether the Macro Tri-planes capture the global feature. Actually, it is not clear what this global feature means. It would be great to render the image or 3D model based using learned Macro Tri-planes only. The lack of ablation studies on the Macro Tri-plane representation makes it difficult to assess its contribution to the overall performance.
- Validate the influence on the performance by the ratio of the number of scenes used for training in the first stage and the second stage. The paper lacks a systematic analysis of how the split between the initial training set and the fine-tuning set affects the final rendering quality and convergence speed. This is a critical aspect for understanding the method's robustness and practical applicability.

- Some details are not clearly presented in the paper.

1) “S describes N scenes drawn from a common distribution.” (line 134-135) It would be great that this definition to be more specific. Are those scenes required to be from the same category or the scene type, such as living room, or kitchen?
2) Line135-136, the definition of x_{i,j} and p_{i,j} are unclear. I would assume x_{i,j} represents the image rendered at ith view where the camera pose is defined as p_{i,j}. The current definitions are not clear at all.
3) Line 230-231: Please clarify the encoded ground truth image and latent image. Do you mean the latents of the ground truth image and latent image?

### Questions
Overall, the idea is interesting. However, some claims are not supported by the experiments in the paper.
1) insufficient experiments. Will it be good to train the model for the real scene dataset such as ScanNet? We knew that for typical scenes, there are a large number of combination of object to form a scene. It is not clear how this method would perform for scenes. The current experiments didn't fully demonstrate this.

 2) Please also demonstrate what is actually learned by the Macro tri-plane. It would be interesting to show rendered images or geometries.

3) Please provide the relationship of the performance related to the split of scenes for training.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper deals with the concurrent reconstruction of multiple objects. It bases it works on Triplanes and strikes a balance among training cost and quality.

### Strengths
1. Originality. The proposed two-stage training pipeline and micro-macro tri-planes decomposition serves as a novel technique for the concurrent reconstruction of large sets of object

### Weaknesses
1. As a submission to ICLR25, it seems unreasonable to only compare quality with NeRF-based methods.  The recent 3DGS has shown significant improvement in training cost and gained a series of improvements. It's beneficial to compare the proposed method with recent FlashGS or gsplat.
2. The comparison with Triplanes seems to be unfair as well. The proposed method indeed increases the model capacity. For an apple-to-apple comparison, the capacity of Triplanes should be better aligned.
3. The ablation is insufficient. What quantitative benefit will be brought by second-stage training over direct training on all scenes? How will the result be influenced if I change the ratio of data assigned to two stages? What about adding more stages?

### Questions
1. The writing and organization of the Introduction require improvement. Why is this problem critical? What are typical and critical application scenarios of the problem?
2. The comparison and ablation experiment should be refined, as detailed in Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
