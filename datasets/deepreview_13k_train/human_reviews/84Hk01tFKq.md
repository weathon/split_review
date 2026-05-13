# HyperFields: Towards Zero-Shot Generation of NeRFs from Text

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
We introduce HyperFields, a method for generating text-conditioned Neural Radiance Fields (NeRFs) with a single forward pass and (optionally) some fine-tuning. Key to our approach are: (i) a dynamic hypernetwork, which learns a smooth mapping from text token embeddings to the space of NeRFs; (ii) NeRF distillation training, which distills scenes encoded in individual NeRFs into one dynamic hypernetwork. These techniques enable a single network to fit over a hundred unique scenes. We further demonstrate that HyperFields learns a more general map between text and NeRFs, and consequently is capable of predicting novel in-distribution and out-of-distribution scenes --- either zero-shot or with a few finetuning steps. Finetuning HyperFields benefits from accelerated convergence thanks to the learned general map, and is capable of synthesizing novel scenes 5 to 10 times faster than existing neural optimization-based methods. Our ablation experiments show that both the dynamic architecture and NeRF distillation are critical to the expressivity of HyperFields.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a framework for achieving zero-shot NeRF generation from texts. This is accomplished through the training of a dynamic hypernetwork using hundreds of pre-trained NeRFs to acquire the mapping from text token embeddings to NeRF weights. Extensive experiments demonstrate the capability of the proposed method to predict in-distribution scenes in a zero-shot manner and out-distribution scenes with a few steps of fine-tuning.

### Strengths
1. This paper is clearly written and easy to follow.

2. The proposed pipeline intuitively makes sense and it is interesting to see the disentanglement of different attributes learned by the proposed hypernetwork.

### Weaknesses
1. My primary concern is the technical contributions of this work in comparison to the referenced ATT3D study. Specifically, while this paper clarifies the connections with ATT3D, it remains unclear what novel techniques or insights are newly introduced by this work. A more compelling justification is highly desirable. For instance, what specific limitations of ATT3D does the proposed method address? Does the proposed method offer any advantages in terms of computational efficiency, generalizability, or scalability compared to ATT3D?

2. Furthermore, there is a lack of benchmarking against ATT3D and the reported results indicate that ATT3D may achieve much better visualization effects. This discrepancy arises because the proposed method appears to only disentangle objects with simple attributes like colors, while ATT3D's reported visualizations can manipulate higher-level attributes and behaviors, such as "chimpanzee holding a cup." The authors are highly expected to conduct a benchmarking comparison with ATT3D using the same text prompt. The comparison should include quantitative metrics, such as FID or Inception Score, to provide a more objective assessment of the generated NeRF quality. Additionally, a qualitative comparison of the generated images from both methods would be beneficial.

3. Although intriguing, it remains unclear why the hypernetwork can successfully learn the disentanglement of various attributes. This may be attributed to the limited scope of text prompts and attributes during training. The authors are expected to provide more insights on this matter. For example, what is the distribution of attributes in the training data? How does the hypernetwork architecture contribute to the disentanglement? An ablation study investigating the impact of different hypernetwork components on disentanglement would be valuable.

### Questions
My questions are included in the weakness section. I am willing to adjust my scores if my concerns are properly addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel generalizable text-to-3D framework to generate a 3D representation with neural radiance field (NeRF) given text inputs. The text inputs are processed by a pretrained BERT network to get powerful embeddings to condition the NeRF generation process. The dynamic hypernetwork is the key innovation of the design to make it succeed to generalize across different 3D shapes over various text conditions. Then a distillation loss is employed to train the NeRF image rendering process given 3D coordinates and synthesized 2D images from DreamFusion. This work will facilitate significant progress of 3D AIGC and inspire future explorations on generalizable 3D generation.

### Strengths
(1) The motivation of this work is clear and the technical impact of this work are significant. Limited by the intrinsic mapping relationship between 3D coordinate and color field of NeRF, current work struggles to achieve generalizable 3D shapes with various conditional input with a unified framework. This work proposes a hypernetwork architecture, which is justified as the key innovation to learn a generalized text-to-3D mapping across different inputs.
(2) Authors conduct extensive experiments on both in-distribution and out-of-distribution samples during testing, and results look consistently appealing.
(3) Benefit from the use of InstantNGP, the generation is much faster than the baseline DreamFusion, which is crucial for some real-time applications such as real-time rendering and editing.
(4) Authors have committed that they will release all the code and pretrained models, which will facilitate better reproduction and follow-up for the community.

### Weaknesses
(1) The paper lacks a thorough quantitative comparison with the baseline method, DreamFusion. While the qualitative results are visually impressive, the absence of metrics such as CLIP retrieval scores or a comprehensive user study diminishes the overall impact. Specifically, providing CLIP retrieval scores on a diverse set of generated 3D models would offer a more objective measure of the model's ability to accurately capture the semantic meaning of the input text prompts. Moreover, a user study involving human evaluation of the generated 3D models' quality, realism, and relevance to the input text would provide valuable insights into the perceived performance of the proposed method compared to DreamFusion.
(2) The paper would benefit from a more detailed ablation study investigating the impact of training across multiple shapes followed by fine-tuning on a single shape. While the authors mention the benefits of this approach, a direct comparison with a baseline model trained from scratch on the same single shape would further solidify the claim. This comparison should involve training both models for an equivalent number of iterations and evaluating their performance on a held-out set of text prompts specific to the target shape. Metrics such as geometric accuracy, texture fidelity, and rendering quality should be used to quantify the differences between the two approaches. This would help demonstrate the advantage of pre-training on a diverse dataset to learn a more robust and generalizable mapping between text and 3D representations.

### Questions
I may consider further improve my rating if my concerns (listed in the weaknessed part) are well addressed.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a fast way to achieve text-to-3D generation. The key idea is to design a hyper-network that predicts weights that process the spatial latent code of NeRF. The technical contribution is that the hyper-network not only looks at the text input, but also the activations of the MLP to be predicted. Experiment results are shown with only combination of color and shape instead of a full prompt (possibly due to limited computational resources). Qualitative results with very limited examples show that the technique is able to improve text-to-3D speed and achieve certain generalizability toward new concepts.

### Strengths
- The hyper-network is fast since it’s free of optimization. Such feedforward approach can have computational advantages as the training cost can potentially be amortized 
- The experiment shows that the model can compose concepts in certain fashion. This helps illustrate the benefit that such model can amortize training compute to be used for many inference uses.

### Weaknesses
 - Current methods is trained from scratch, which might be computationally expensive. 
- The key architecture of this paper is a hyper-network that predicts the weights for the MLP. 
- A main concern regarding the result is very limited. Most of the results are shown in simple objects and compositions. 
- An other small concern is regarding the need to create a small dataset of NeRF scenes. Each NeRF can takes minutes, and this prevents it to scale to larger datasets.
- If the model weight depends on where we sample the activations, then the generated weights can have high variance. I’m a bit concerned that this means different ways to sample the points can lead to different weights, and thus leading to different performance.

### Questions
- “SDS loss exhibits high variances” - is there any experimental/reference evidence that support it?
- Quality: Figure 4, why is the image looks washed out? Is it because of artifacts from normalization?
- I wonder if the main difference between ATT3D and this paper is whether the hyper-network takes activations?
- Why do we choose three captions during training? Why can’t we spread away these captions throughout different batches?
- Maybe I’ve missed it, but how do we choose different a_i’s?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents "HyperFields", an approach designed to achieve zero-shot generation of Neural Radiance Fields (NeRFs) from textual prompts. By utilizing a dynamic hypernetwork, HyperFields is able to establish a mapping from text token embeddings, specifically derived from BERT, to the domain of NeRF parameters. The paper introduces NeRF distillation training, where individual NeRF-encoded scenes are distilled into a singular dynamic hypernetwork. The main goal of HyperFields is to efficiently generate scenes that the model has seen during its training (in-distribution), and to quickly fine-tune itself for unseen (out-of-distribution) prompts, if necessary.

### Strengths
(+) The paper addresses an important gap in zero-shot generation using NeRFs.

(+) The presentation of the method is clear, with a well-structured explanation of the hypernetwork and NeRF distillation.

(+) The paper introduces a fresh perspective on text-to-NeRF synthesis, leveraging hypernetworks, which is a less explored territory in this context.

### Weaknesses
(-) **Limited experimental results**: The experimental results presented in the paper, particularly in Figure 4 and Figure 5, are quite limited. The in-distribution generalization showcased in Figure 4 uses only 9 basic shapes, and the generalization is restricted to simple uniform color translations. Figure 5, too, is restricted to basic geometry and appearance.

(-) **Low quality of results**: The results presented, especially the simple geometric shapes and uniform color distributions, seem to be of low standard. There is a noticeable disparity in quality when compared to state-of-the-art techniques. Moreover, the ablation study in Figure 6 only provides a single example, which weakens the overall argument.

(-) **Lack of comparative discussion**: It's important to note that recent studies, such as HyperDiffusion (ICCV 2023) and Shap-E (arXiv), have also explored the use of hyperparameters in 3D object generation, resulting in promising results. However, there is a lack of comparative discussion with these methods, which is crucial in positioning HyperFields in the current research landscape. Furthermore, the absence of comparison with ATT3D, a recent method that also tackles text-to-3D generation, is a significant oversight, especially considering its promising results and relevance to the proposed approach.

### Questions
- In Section 4.2 (referencing Figure 5), the paper mentions, "...with no optimization, when provided with the out-of-distribution prompt. The model chooses the semantic nearest neighbor from its training data as the initial guess for out-of-distribution prompts..."; However, it is not clear how the model is capable of retrieving the nearest-neighbor. Could the authors provide more information on the intrinsic capabilities of the model that enable this nearest-neighbor retrieval?
- How does HyperFields handle highly creative textual prompts?
- How does the NeRF distillation process handle the potential loss of scene details? 
- It is important to have a discussion regarding the limitations of the proposed approach.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
