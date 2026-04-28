# FCVL: Fourier Cross-View Learning for Generalizable 3D Object Detection in Bird’s Eye View

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 5, 5, 6, 3

## Abstract
Improving the generalization of Birds' Eye View (BEV) detection models is essential for safe driving in real world. In this paper, we consider a realistic yet more challenging scenario, which aims to improve the generalization with single source data for training, as collecting multiple source data is time-consuming and labor intensive in autonomous driving. To achieve this, we rethink the task from a frequency perspective and exploit the cross-view consistency between adjacent perspectives. We propose the Fourier Cross-View Learning (FCVL) framework including Fourier Hierarchical Augmentation (FHiAug), an augmentation strategy in frequency domain to boost domain diversity and Fourier Cross-View Semantic Consistency Loss to facilitate the model to learn more domain-invariant features. Furthermore, we provide theoretical guarantees via augmentation graph theory. To the best of our knowledge, this is the first study to explore generalizable 3D Object Detection in BEV with single source data, and extensive experiments on various testing domains have demonstrated that our approach achieves the best performance on various test domains with single source data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FCVL (Fourier Cross-View Learning), a framework to improve the generalization capability of Bird's Eye View (BEV) 3D object detection models when trained on single-source data.

### Strengths
1. While most previous work focuses on multi-domain generalization, this paper tackles the more challenging and practical problem of single-domain generalization. This is especially relevant for autonomous driving where collecting multi-domain data is expensive and time-consuming. 
2. The paper provides a formal analysis using augmentation graph theory, connecting practical augmentations to theoretical guarantees. The theoretical analysis provides insights into why the method works.

### Weaknesses
1. Fourier transformations are computationally intensive and scale quadratically with image dimensions. Lack of analysis of how the method scales with increasing image resolution or number of cameras. 
2. Limited discussion of computational overhead and training time, which is critical for practical implementation.  How does the computational complexity of FCVL compare to baseline methods, particularly during training and inference? e.g. total training time comparison with baselines, additional memory requirements and computations for frequency domain operations. 
3. In table.1, it seems FCVL didn't show superior performance on the normal validation set.
4. Missing references:
- HotBEV: Hardware-oriented transformer-based multi-view 3D detector for BEV perception
- Bevformer v2: Adapting modern image backbones to bird's-eye-view recognition via perspective supervision
- Clip-bevformer: Enhancing multi-view image-based bev detector with ground truth flow
- Ocbev: Object-centric bev transformer for multi-view 3d object detection
- BEVNeXt: Reviving Dense BEV Frameworks for 3D Object Detection

### Questions
1. What is the rationale behind the specific choices of frequency domain transformations? Were other alternatives considered?
2. Does the method maintain its effectiveness when dealing with rapid environmental changes (e.g., entering/exiting tunnels)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of improving the generalization of BEV detection models for autonomous driving. The authors introduce a novel framework called Fourier Cross-View Learning, which includes two key components:
1. Fourier Hierarchical Augmentation, an augmentation strategy that operates in the frequency domain to enhance domain diversity.
2. Fourier Cross-View Semantic Consistency Loss, which helps the model learn domain-invariant features.

### Strengths
1. The paper introduces the Fourier Cross-View Learning framework, featuring Fourier Hierarchical Augmentation to enhance domain diversity without additional complexity.
2. The paper proposes fourier cross-view semantic consistency loss to improving generalization in real-world scenarios.

### Weaknesses
1. Since the primary augmentation occurs on 2D images, it can be difficult to differentiate it from standard 2D augmentation techniques. A more detailed explanation of these methods might enhance clarity for readers less familiar with them. Specifically, the paper lacks a rigorous comparison to existing 2D augmentation methods in the context of BEV detection. It's unclear how the proposed Fourier-based augmentations offer a significant advantage over, for example, applying random rotations, scaling, or color jittering directly to the input images before BEV transformation. The paper should provide a more detailed analysis of the frequency domain manipulations and how they translate to meaningful variations in the BEV space.
2. Because the evaluation is solely conducted on the nuScenes-C dataset, there is a risk that the models may be trained to excel in this specific context, potentially neglecting more challenging real-world scenarios. Testing exclusively on one dataset limits the robustness of the findings and reduces the overall credibility of the conclusions. The paper needs to demonstrate the effectiveness of the proposed method on a wider variety of datasets with different environmental conditions, sensor configurations, and geographical locations. This is crucial to ensure the generalizability of the approach to unseen scenarios.

### Questions
Could you provide additional evaluation results using different datasets? Relying solely on the nuScenes-C dataset increases the risk of overfitting through parameter tuning.

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
This paper aims to address the challenge of Single Domain Generalization in BEV-based multi-camera 3D object detection and proposes a Fourier Cross-View Learning (FCVL) framework. This framework consists of a non-parametric Fourier Hierarchical Augmentation (FHiAug) at both image and feature levels to enhance data diversity and a Fourier Cross-View Semantic Consistency Loss to facilitate model to learn more domain-invariant features from adjacent perspectives. Additionally, they provide theoretical guarantees through augmentation graph theory.

### Strengths
1. This paper is clearly structured and written-well. Proper formulization makes the processes of the method easy to understand.
2. This paper focuses on an interesting issue, namely that Single Domain Generalization in BEV-based multi-camera 3D object detection.
3. The paper offers extensive experiments and rigorous theoretical guarantees.

### Weaknesses
1. The Fourier Cross-View Semantic Consistency Loss constructs positive and negative samples by splitting adjacent perspectives into halves. However, this approach has a limitation: each segment contains not only foreground objects but also complex background interference, which requires further analysis.
2. This paper focuses on addressing the domain generalization problem but currently only provides numerical experiments to demonstrate the method's effectiveness. It is recommended to supplement the analysis with commonly used feature distribution visualizations in the field to provide a more intuitive demonstration of the proposed method's efficacy.

### Questions
1. Please refer to the Paper Weaknesses mentioned above.
2. How is the number of positive and negative samples set in the Fourier Cross-View Semantic Consistency Loss?
3. Most of the current experiments are based on relatively older detectors. Is there still a significant performance improvement when applied to the latest SOTA BEV-based detectors?

### Soundness
2

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
The paper introduced a interesting problem, that is 3D object detection models trained on a single source domain can be generalized to others. The authors proposed FCVL (Fourier Cross-View Learning), a framework to improve the generalization of Bird's Eye View (BEV) 3D object detection models when trained on a single source domain. The key contributions include:

- A Fourier Hierarchical Augmentation (FHiAug) strategy that works at both image and feature levels to increase domain diversity without requiring additional modules.
- A Fourier Cross-View Semantic Consistency Loss that leverages natural multi-view inputs to learn domain-invariant features.
- Theoretical guarantees for the effectiveness of FHiAug using augmentation graph theory.
- Extensive experimental validation showing superior performance compared to existing domain generalization methods across various test domains.

### Strengths
The proposed method seems novel. They innovatively use of Fourier domain for both augmentation and cross-view consistency with non-parametric approach that doesn't require additional training modules. Meanwhile, The authors provided solid theoretical guarantees through augmentation graph theory and clear mathematical formulation and proofs for the proposed methods. Extensive experiments across multiple frameworks (BEVFormer, BEVDepth, BEVDet) are conducted.

### Weaknesses
 - The proposed method has seveal hyperparameters to tune, in the paper, the authors did not specifically point it out how to make it work. If the authors could elaborate how to set up these hyperparameters and how do they affect the final performance, it will be better.
- The authors could discuss more on the failure cases or limitations
- The experimental results are preseneted mainly on synthetic corruptions (nuScenes-C), how about others datasets in the self-driving field? It will be beneficial to see more diverse real-world testing scenarios

### Questions
Please refer to weaknesses part for the questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies how to boost the generalization of monocular 3D object detectors, like BEVFormer, when only a single domain of data is available. To this end, this paper develops techniques to boost the model domain generalization via augmentation in the frequency domain. A theoretical analysis based on the augmentation graph theory is provided. Extensive experiments on the nuScenes benchmark are conducted to verify the effectiveness of the proposed techniques.

### Strengths
1. The pipeline figure is well designed.
2. In experiments, this work compares its own method with many other counterparts.

### Weaknesses
1. The studied problem, improving model domain generalization with only a single domain of data, is not very meaningful. First, driving data is not so expensive to collect that only a single domain of data can be collected. For companies, diverse domains of data are absolutely available. I cannot think out a scenario that only a single domain of data can be used in practical applications.
2. The presentation needs significant improvement. For example, the story flow of Intro is not fluent.
3. The technique contributions, data augmentations in the frequency domain, are not very interesting. This is a somewhat straightforward idea. there are many attempts that design operations in the frequency domain, although maybe not in 3D object detection. However, these frequency-domain based methods are not really widely adopted after many years of research, and this work does not present a significant difference from them.
4. The theoretical analysis seems not to add valuable information to this paper. Do not use mathematical formulations just because want to add mathematical formulations. This will make the paper more difficult to understand.

### Questions
See the weakness. The authors can remind me if I overlook or misunderstand something important.

### Soundness
2

### Presentation
2

### Contribution
2
