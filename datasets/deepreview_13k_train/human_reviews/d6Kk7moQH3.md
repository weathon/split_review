# Image registration is a geometric deep learning task

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Data-driven deformable image registration methods predominantly rely on operations that process grid-like inputs.
However, applying deformable transformations to an image results in a warped space that deviates from a rigid grid structure.
Consequently, data-driven approaches with sequential deformations have to apply grid resampling operations between each deformation step. 
While artifacts caused by resampling are negligible in high-resolution images, the resampling of sparse, high-dimensional feature grids introduces errors that affect the deformation modeling process.
Taking inspiration from Lagrangian reference frames of deformation fields, our work introduces a novel paradigm for data-driven deformable image registration that utilizes geometric deep-learning principles to model deformations without grid requirements.
Specifically, we model image features as a set of nodes that freely move in Euclidean space, update their coordinates under graph operations, and dynamically readjust their local neighborhoods.
We employ this formulation to construct a multi-resolution deformable registration model, where deformation layers iteratively refine the overall transformation at each resolution without intermediate resampling operations on the feature grids.
We investigate our method's ability to fully deformably capture large deformations across a number of medical imaging registration tasks. 
In particular, we apply our approach (GeoReg) to the registration of inter-subject brain MR images and inhale-exhale lung CT images, showing on par performance with the current state-of-the-art methods. 
We believe our contribution open up avenues of research to reduce the black-box nature of current learned registration paradigms by explicitly modeling the transformation within the architecture.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposed to approach deformable image registration by using graph neural networks. The authors claimed that using geometric deep learning method would let registration task get rid of grid constraints. Experiments showed that the proposed approach achieved state-of-the-art performance on brain MRI and lung CT datasets.

### Strengths
1. The presentation is clear and easy to follow.
2. The motivation of formulating image deformation registration as a graph learning problem sounds interesting. 
3. Experiments explored large deformation setups on synthetic data as well as lung CT.

### Weaknesses
1. The methodology soundness is somewhat questionable. The authors have not mentioned how their proposed model would ensure the graph well-posedness when learning the deformations. Directly representing images in 3D grids to graph nodes could potentially mis-construct the folding/surface structures. Specifically, the paper lacks a clear explanation of how the graph structure inherently prevents issues like self-intersections or volume inversions, which are common challenges in deformable registration. The use of a graph structure, while novel, needs more justification regarding its ability to maintain the topological integrity of the deforming image.
2. To represent registration as graph learning, the authors should compare and discuss the relations between their method and the large body of *point cloud* [1] and *surface* [2] registrations. The current discussion does not adequately address how the proposed method differs from existing graph-based registration techniques, particularly those used in point cloud and surface registration. The paper should clarify whether the graph edges are fixed or dynamically updated during the deformation process, and how this choice impacts the registration accuracy and robustness. A more thorough analysis of the differences and similarities with existing graph-based registration methods is needed to properly contextualize the contribution.
3. The comparisons are not sufficient/convincing and not up-to-date given the fast development of medical image registration field.
(1) Traditional physics-based models for diffeomorphic image registration, e.g., LDDMMs;
(2) Recent learning-based deformable registration models, e.g., SynthMorph, GradICON. For more models, authors could refer to Learn2Reg MICCAI2024 challenge (https://learn2reg.grand-challenge.org/). The experimental section lacks a comprehensive comparison with established methods, including both traditional diffeomorphic approaches like LDDMM [3] and recent deep learning-based methods such as SynthMorph [4] and GradICON [5]. The absence of these comparisons makes it difficult to assess the true performance and novelty of the proposed method. The authors should also consider including more recent state-of-the-art methods from the Learn2Reg challenge to provide a more robust evaluation.

### Questions
My main questions are in the lack of discussion on related work and missing experimental comparisons. Please refer to weakness.

### Soundness
2

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
This paper presents a novel framework for deformable medical image registration that introduces a geometric deep learning-based approach, allowing the model to tackle large deformations and substantial geometric shifts. The key innovation lies in leveraging a Lagrangian framework, where deformations are applied without relying on grid constraints, which is a fresh approach in medical imaging registration. The model’s design also incorporates a multi-resolution framework, which progressively refines transformations from coarse to fine, reducing the need for intermediate resampling and preserving feature integrity. Experiments conducted on synthetic datasets demonstrate the model’s ability to outperform traditional grid-based methods, such as VoxelMorph, especially in handling large and complex deformations.

### Strengths
* Novelty in Approach: The use of a Lagrangian framework in the field of medical image registration is an innovative contribution. It allows transformations without grid dependency, addressing common limitations in traditional models.
* Ability to Handle Large Deformations: The model demonstrates strong performance in capturing large-scale geometric deformations, which many existing methods struggle with.
* Multi-Resolution Deformation Design: The progressive, coarse-to-fine deformation approach effectively reduces computational load at higher resolutions and ensures finer layers need only minimal adjustments, improving efficiency and accuracy.
* Strong Experimental Performance: The model achieves high accuracy in synthetic deformation tasks, showing its robustness in large-deformation registration scenarios, and reports low folding ratios, indicating better spatial regularity.

### Weaknesses
 * Generalizability to Multi-Modal and Realistic Datasets: While the model performs well on synthetic datasets, it is unclear how it might adapt to multi-modal scenarios (e.g., T1-to-T2 MRI registration). There are limited details on how it can capture realistic anatomical variability beyond synthetic deformations. Expanding evaluation to multi-modal datasets with real-world challenges would strengthen the paper. Specifically, the paper lacks a discussion on how the Lagrangian framework handles varying image intensities and contrasts inherent in multi-modal data. The feature extraction process might be sensitive to these variations, and the paper does not address this potential limitation.
* Ambiguity in Experimental Design: In Table 1, the experimental setup lacks clarity. For instance, the distinction between the “Ours (feat. warp)” variant and the primary model (GeoReg) is not fully explained, leaving readers uncertain about the differences in architecture or training procedures between them. The description of the feature warping process is insufficient, and it is unclear how this baseline differs from a standard Eulerian approach. A more detailed explanation of the implementation differences, including the specific warping algorithm used, is necessary.
* Sensitivity to Deformation Degree: The effect of deformation degree, such as the impact of the Brownian deformation parameter, on model performance is not well discussed. It would be helpful to understand how the model behaves under varying levels of deformation severity, as this might impact generalizability in diverse clinical cases. The paper should include a more detailed analysis of how the model's performance degrades with increasing deformation magnitudes and how the multi-resolution approach mitigates these effects. A quantitative analysis of the model's robustness to different deformation parameters is needed.

### Questions
1. How does the model handle multi-modal registration beyond synthetic deformation? For example, would any special modifications be needed for realistic T1-to-T2 datasets?
1. Could you clarify the distinction between “Ours (feat. warp)” and the main GeoReg model in Table 1? How does the architecture or feature handling differ?
1. Does the degree of deformation in synthetic data (e.g., Brownian noise) influence model performance? Specifically, are there limits on the deformation magnitude where the model starts to fail?
1. Are there any practical limitations, such as longer training times or increased memory requirements, due to the Lagrangian framework compared to grid-based methods like VoxelMorph?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new deep learning-based multi-resolution image registration approach for medical data that deviates from the classical grid-like structure needs/approaches by incorporating principles for geometric learning. More specifically, it is proposed to use the Lagrangian reference frame (instead of an Eulerian one) and to model image features as nodes in an adjustable graph instead of on a static grid. It is claimed that this reduces resampling operations by moving into a continuous space for all computations. The proposed method is evaluated on synthetic brain deformations and additionally on three publicly available image registration benchmark datasets (2 brain, 1 lung). The experiments show that the proposed method achieves comparable or better results than the other learning-based registration methods used as baselines.

### Strengths
- I really appreciate the overall framing of the paper that challenges the common paradigms used in DL-based image registration and I believe that in the context of DL, this approach is novel and the paper is also easy to follow.  
- Having a new method available that is less parameter intense is nice (although the memory footprint is concerning).
- Baselines include (some) relevant SOTA approaches and the chosen datasets cover two very common registration tasks. 
- I like the framing (and use) of attention as a data-driven interpolation scheme and its integration into the framework.

### Weaknesses
 - In general, I believe that the overall method is novel, but I am not sure that the chosen application scenarios actually showcase any tangible advantages. In my mind, such a Lagrangian frame-based setup makes most sense in a scenario where the input data is sparsely and irregularly sampled. However, this is not the case in the applications tackled in this paper. I would have expected to see something that either only involves shapes or point clouds to be registered or some artificial scenarios where only data at certain patches or key points is available (e.g., to mimic intra-interventional registration problem arising in radiation therapy). Given the presented applications, I fail to see the claimed benefits of the presented methods. However, in the area of such explicitly spare problems prior work on geometric deep learning already exists (e.g., Hansen et al.) as acknowledged by the authors, which then challenges a bit the novelty of this work.

- Additional problems that I see with the conducted experiments are that half of them operate on somewhat simple synthetic deformations and for the real-world scenarios (brain and lung registration) I miss any statistical tests that really back up the claimed improvements over the chosen baselines. While the baselines cover some of the SOTA approaches in DL-based image registration, it would have been nice to see additional specific, relevant baselines for the datasets chosen (e.g., LapIRNv2, which won last year's Learn2Reg challenge on the NLST data with a TRE of less than 1.5 mm). I am also missing traditional approaches such as ANTs as baselines as right now only a FFD/B-spline-based method is included.

- I also find the number of foldings in the real-world results rather high and concerning. Unfortunately this is not really discussed in the paper (or I have not been able to find it) and I would be interested in learning the reasons for this. Is this a result of the mostly implicit regularization employed here that is not strong enough? While I acknowledge that the authors are not explicitly focusing on presenting a diffeomorphic registration framework, this aspect warrants further investigation and improvements and/or a discussion on how this could be achieved. The lack of explicit diffeomorphic constraints is a significant limitation, especially given that such constraints are commonly employed in medical image registration to ensure physically plausible transformations.

- The presented method appears to be quite memory hungry, but the paper never makes this explicit. I would have expected to see some numbers here instead of the rather abstract discussion in Sec. 3.2.. Right now, it is not really possible to assess this crucial aspect of the paper.

### Questions
- Why do the authors think that the chosen application scenarios are actually helpful in showcasing the potential benefits of their method?
- Why were other potentially more competitive baselines not included in the comparison?
- How do the authors interpret the foldings in the real-work applications?
- What is the exact memory footprint of the method in comparison to the baselines for the chosen applications?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method, GeoReg, that uses geometric deep-learning principles to model deformations without grid requirement, avoiding the need for interpolation in the feature space. Inspired by Lagrangian reference frames of the deformation field, the image features are tracked individually along the trajectory rather than observing the deformation at specific locations, and their coordinates are updated under graph operations. To overcome the local minima, the multi-resolution strategy is applied.

### Strengths
The first introduction of geometric deep learning and the Lagrangian reference into the learning-based method make the paper a novel and significant algorithm contribution. 

The paper is generally easy to understand. Some descriptions that need to be clarified are listed later. 

The experiments demonstrate the superior performance of the proposed method in the cases with rotation, scaling, and translation deformation.

### Weaknesses
1. The paper tries to demonstrate the proposed model’s ability to recover large deformations. Certainly, the model has superior performance in handling rotation, scaling, and translation deformation separately. In practice, the large deformation in medical images should be the combination of the three transformations, which fails to be demonstrated in the experiment. Moreover, the organs are not a rigid body, thus the deformation might not be uniform even in the same organ. For instance, the scaling of the lung at one end might be different from the other end. The experiments should include a combination of these transformations to better reflect real-world scenarios, and also include non-rigid deformations within the same organ to demonstrate the model's robustness.
2. The benchmarks used in the paper are not refined for the image registration with large deformation. The model that is specifically designed for large deformation such as LapIRN (Mok & Chung, 2020) which is mentioned in the paper, FourierNet (Jia et al, 2023), and more need to be compared to assess the performance of the proposed model on large deformation registration. The current benchmarks do not adequately demonstrate the model's performance against state-of-the-art methods specifically designed for large deformations, which is a critical aspect for the claims made in the paper.
3. The experiments are all based on datasets with only one main organ (brain & lung), which might lack the deformation discontinuities of sliding organs (one type of large deformation, see Papiez et al., 2014). The datasets with multiple organs Abdomen CT-CT dataset (also available in learn2reg) might be needed to examine the proposed model's performance on various large deformations. The lack of experiments on datasets with multiple organs and sliding deformations limits the generalizability of the findings and the applicability of the proposed method to more complex anatomical scenarios.

Minor problems
1. Table 2: In row 3, typo of the model name (VoxelMorph?)
2. Table 2: In the middle column (Brain CamCAN T1T2), should the bold font be put on the second to the last row (2.95+/-1.16) rather than the final row (2.98+/-0.89)

### Questions
Several suggestions that might make the paper more solid:
1. It would be better to add some models that specifically designed for large deformations
2. The first experiment could add the tests on the combination of transformations.
3. Add experiment on additional dataset with multiple organs which could contain slippery deformation.

### Soundness
2

### Presentation
2

### Contribution
3
