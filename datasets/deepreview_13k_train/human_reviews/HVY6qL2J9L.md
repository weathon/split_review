# BraiNav: Incorporating Human Brain Activity to Enhance Robustness in Embodied Visual Navigation

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Recent research shows that standard navigation agents significantly underperform and even fail in the presence of various visual corruptions. Unlike embodied agents, the human brain's visual system can robustly perceive the environment and extract the necessary information to complete the visual tasks. In this paper, we propose a two-phase Brain-Machine integration Navigation method called BraiNav, which incorporates neural representations derived from human brain activity to enhance robustness against visual corruptions. In the first phase, a brain encoder, built upon a recently advanced self-supervised pretrained model, is trained on a large-scale human brain activity dataset and then frozen for downstream visual navigation. In the second phase, neural representations harboring high-level cognitive information from the human brain are constructed based on the pretrained frozen brain encoder. Additionally, we propose a multimodal fusion method based on cross-attention to obtain more consistent brain-visual joint representations, which are then used to learn the navigation policy. Sufficient experiments demonstrate that the proposed method exhibits higher robustness against various visual corruptions compared to standard navigation agent and multiple computer vision-enhanced agents. Our study pioneers the incorporation of human brain activity into embodied AI, aiming to catalyze further cross-disciplinary collaboration with computational neuroscience.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on the task of embodied visual navigation. Specifically, it proposes a two-phase Brain-Machine integration Navigation method called BraiNav, which incorporates neural representations derived from human brain activity to enhance robustness against visual corruptions. Additionally, it presents a multimodal fusion method based on cross-attention to obtain more consist brain-visual joint representations. Experiments on several benchmarks demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper is well-written and easy to understand.
2. The motivation of this paper is interesting and solid.
3. Extensive experiments are conducted to show the superiority of the proposed method to other competitors.

### Weaknesses
1. The technical novelty of this proposed method is limited. Designs for both brain encoder and visual-target module are borrowed from previous literature. The key idea for the multimodal fusion module is cross-attention for multi-modal information interaction, which is a common operation in the current era of multi-modal tasks. The difference may lie in features used to produce Q/K/V or the location of skip connections, due to different tasks or inputs/outputs
2. With additional information, the performance improvement of the proposed method is not very significant in Tab. 2. For sixteen metrics across different settings, BraiNav achieves better results for only half of the metrics.
3. One interesting baseline could be added and discussed: a) use the autoencoder or generative model to purify the observed images (via self-supervised training strategy), b) adopt a similar architecture to BraNavi to fuse features from purified images and original images (as well as the target location) for action prediction. 
4. Typos: a) ‘stimulu’ in L 140, b) ‘hemispheres’ in L210

### Questions
Please refer to the Weaknesses for details.

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
5

### Summary
This paper introduces a new method BraiNav, incorporates human brain data to improve the robustness of embodied visual agents when navigating through visually corrupted environments (e.g., blur, noise). BraiNav has two-phases. The first one is the brain encoder trained on the NSD fMRI dataset. The second phase takes neural encoder representations and combines them with visual-target information through a cross-attention-based fusion module. This enables the agent to navigate under different visual conditions. Experiments demonstrate that BraiNav performance is competitive on standard and vision-enhanced agents across various corruptions.

### Strengths
1. The major strength of the study is an innovative use of integrating brain data into a downstream task. I haven’t seen it does this way for visual navigation tasks.
2. The paper in general is well motivated.
3. Robustness is an important problem to solve and using brain data seems like a promising avenue for research. 
4. There is also the potential for broader applications of this strategy even beyond navigation.

### Weaknesses
1. While the use of human brain data is novel, the study doesn’t convincingly demonstrate why brain-derived features offer an advantage over purely data-driven or learned representations in the navigation task. What is it about the fMRI data that seems to work? Why choose one (or 2 subjects) from the 8 available in the dataset? It is unclear whether the improvement is real or due to some added complexity and/or representational power from the model.
2. The paper significantly lacks in a thorough analysis of how brain-derived neural representations contribute to performance on the task. The authors need to justify using the brain data better and the current text is vague about this.
3. Lack of “control” representations. The fMRI encoder is derived from DINOv2. One possibility is that it is the DINO representations that are actually driving the performance gains in the model. But this has not really been evaluated.
4. Alternative models are from an older study. The models are compared against the previous models from Chattopadhyay et al., 2021. Since then several other models have been proposed to improve model robustness.

### Questions
1. Why do the authors train the model on only one subject when the NSD dataset includes 8 subjects? Although the authors claim that the appendix includes data from other subjects, it actually reports data from only one additional subject (subject 2). Training on all 8 subjects and reporting the median performance would provide a more comprehensive evaluation and reduce the risk of overfitting or subject-specific biases.
2. Relatedly, are there specific images or brain regions that contribute most to the model's performance? Identifying the images (or brain regions) particularly influential could tell us how the model uses specific neural patterns for prediction. 
3. The performance ceiling of the model’s encoder needs to be established. Currently, it’s unclear how effective the fMRI encoder truly is, making it difficult to assess the upper limits of its predictive capability. 
4. It is also unclear whether the reported data stems from specific characteristics of the NSD fMRI data or the choice of model (e.g., DINO). Have the authors tested other datasets, such as BOLD5000v2 or THINGS fMRI, to determine if the performance is consistent across different types of brain data? Have the authors tested other backbones and not DINOV2? This inspection is crucial for understanding whether the results reflect properties of the brain data itself or simply the use of high-quality, clean feature representations. Testing on multiple datasets would help disentangle these factors and clarify the model’s generalizability.
5. The authors should include more contemporary models known for their performance on robustness tasks, such as those optimized for invariance to transformations, noise, or domain shifts. Models like CLIP (Contrastive Language-Image Pretraining) or models trained with augmentation strategies for robustness (e.g., adversarial training or contrastive learning with diverse augmentations) may capture more stable, generalized neural representations. 
6. It is currently unclear whether the paper aims to simply demonstrate the feasibility of using brain data for navigation tasks or to support a central claim that incorporating human brain data is essential for improving these tasks. Clarifying this intent is important, as it influences how the results should be interpreted—either as a proof of concept or as evidence for the unique value of brain data. If the latter, stronger arguments and comparative analyses would be needed to establish

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors suggest integrating brain-inspired visual representations into navigation policy networks, motivated by the exceptional robustness of human vision. This integration is accomplished by training a DINOv2 model to predict fMRI responses using a large-scale fMRI dataset. The predicted fMRI responses are then combined with features extracted by navigation networks. The authors demonstrate that these brain-like visual representations can improve the navigation model's robustness when encountering unexpected visual corruptions. They also detail their engineering efforts in designing architectures that effectively leverage fMRI responses. This work makes a novel and valuable contribution to both embodied AI and visual neuroscience.

### Strengths
1. The contribution of incorporating "brain-like" representations in visual navigation is novel and insightful for both neuroscience and computer vision fields. Several previous works [1-4] incorporate brain-like representations or human-like strategies to enhance classification performance and robustness but they only consider classification tasks which are not embodied. Embodiment aspect is never considered in the previous works which makes this work distinct from others.

2. The paper has well-designed and concrete experiments including comparing with the existing non-neuroscience-inspired methods and ablation studies across multiple configurations of the proposed method.


Reference

[1] Learning From Brains How to Regularize Machines (NeurIPS 2019)

[2] Simulating a Primary Visual Cortex at the Front of CNNs Improves Robustness to Image Perturbations (NeurIPS 2020)

[3] Harmonizing the object recognition strategies of deep neural networks with humans(NeurIPS 2022)

[4] Training on Foveated Images Improves Robustness to Adversarial Attacks (NeurIPS 2023)

### Weaknesses
1. The author did not compare with the previous works that incorporate the alignment of neural responses to the models. This may limit the contribution of this work as we will not know what are the best methods to encourage networks to have brain-like representations.
2. The improvement trends are inconsistent. For some corruption types, such as "Camera Crack" and "Low FOV," the method shows no improvement over the baseline.
3. There is no intuition or visulisation explaining why the proposed method works or does not work with certain types of visual corruption.
4. The authors should provide more related works on solving visual corruption in point-goal navigation tasks.

### Questions
I review this paper for the second time so I understand the details. The manuscript has been improved from the last submission so there is no further questions from me.

### Soundness
3

### Presentation
3

### Contribution
3
