# SaRA: High-Efficient Diffusion Model Fine-tuning with Progressive Sparse Low-Rank Adaptation

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 5, 8, 6, 6

## Abstract
In recent years, the development of diffusion models has led to significant progress in image, video, and 3D generation tasks, with pre-trained models like the Stable Diffusion series playing a crucial role.
However, a key challenge remains in downstream task applications: how to effectively and efficiently adapt pre-trained diffusion models to new tasks.
Inspired by model pruning which lightens large pre-trained models by removing unimportant parameters, we propose a novel model fine-tuning method to make full use of these ineffective parameters and enable the pre-trained model with new task-specified capabilities.
In this work, we first investigate the importance of parameters in pre-trained diffusion models (Stable Diffusion 1.5, 2.0, and 3.0), and discover that the smallest 10\% to 20\% of parameters by absolute values do not contribute to the generation process due to training instabilities rather than inherent model properties.
Based on this observation, we propose a fine-tuning method termed SaRA that re-utilizes these temporatily ineffective parameters, equating to optimizing a sparse weight matrix to learn the task-specific knowledge.
To mitigate potential overfitting, we propose a nuclear-norm-based low-rank sparse training scheme for efficient fine-tuning.
Furthermore, we design a new progressive parameter adjustment strategy to make full use of the re-trained / finetuned parameters.
Finally, we propose a novel unstructural backpropagation strategy, which significantly reduces memory costs during fine-tuning and further enhances the selective PEFT field.
Our method enhances the generative capabilities of pre-trained models in downstream applications and outperforms traditional fine-tuning methods like LoRA in maintaining model's generalization ability. We validate our approach through fine-tuning experiments on SD 1.5, SD 2.0, and SD 3.0, demonstrating significant improvements.
Additionally, we compare our method against previous fine-tuning approaches in various downstream tasks, including domain transfer, customization, image editing, and 3D generation, proving its effectiveness and generalization performance.
SaRA also offers a practical advantage that requires only \textit{a single line of code modification} for efficient implementation and is seamlessly compatible with existing methods.
Source code is available at \url{https://sjtuplayer.io/projects/SaRA}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach for fine-tuning pre-trained diffusion models called SaRA for visual content generation. The method builds on a key insight: parameters with the smallest absolute values in diffusion models contribute minimally to generation due to training instabilities, allowing for their selective reuse. SaRA enhances these low-impact parameters by applying a sparse weight matrix that learns task-specific knowledge while retaining the model’s generalization abilities. To avoid overfitting, the authors introduce a nuclear-norm-based low-rank training scheme. Additionally, SaRA includes a progressive parameter adjustment strategy and an unstructured backpropagation approach to efficiently manage memory use during fine-tuning.


Note: the supplementary materials contain the author's username and IP address (Supplementary Material/code/.idea/deployment.xml)

### Strengths
1. The method visualizations (Figures 1 and 4) provide a step-by-step comparison of the proposed approach with previous techniques that helps the reader to easily understand the nuances of SaRA.
2. The authors show that the method could be applied to different diffusion models denoisers architectures U-Net (SD1.5 and 2.0) and Diffusion Transformer (SD3.0).
3. The design of the method allows a plug-and-play experience for the users that is highly beneficial for practical adoption.
4. The authors demonstrate the capabilities of the proposed approach on various widely-used by the open source community datasets.

### Weaknesses
1. The authors introduce a novel Visual-Linguistic Harmony Index (VLHI) metric; however, it's described only in the appendix.
2. No comparison with the recent SOTA PEFT techniques (e.g., DoRA [Liu et al. 2024] that is available for different models on mentioned in the paper CIVITAI).
3. No ablation on scaling the trained SaRA weights for the inference (as the lora_scale parameter controls the influence of LoRA weights) or mentioning it in the limitations.
4. The authors say that for the FID computation they sampled 5K images from the source and generated data; however, BarbieCore dataset has only 315 images which is definitely not enough for the proper FID evaluation. The details about the sizes of the used datasets should be in the paper.
5.  CLIP L/14 used by authors is trained to provide overall image captions and could miss the details. The visual language models-based evaluations used in T2I-CompBench++[Huang et al. 2023] could be more accurate.
6. The authors skip the most popular Stable Diffusion XL 1.0 version, whereas they include 2.0.
7. Typographical mistakes such as:
*) Table 1: wrong column 2&3 names
*) Figure 1: addictive-> additive

### Questions
see the weaknesses section

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
4

### Summary
To leverage the unimportant parameters concept in model pruning, this paper proposes a model fine-tuning method for diffusion model by reusing these ineffective parameters. The authors find that such ineffective parameters with small absolute values are random and dynamically change over finetuning. Based on this observation, they further design some efficient strategies for tuning these parameters.

### Strengths
1. This paper verifies that the ineffective parameter concept also applies for diffusion model, i.e., the parameters with small absolute values are not important for the generation. 
2. This paper adopts a series of strategies for the efficient tuning of these ineffective parameters.
3. The effectiveness of this method is verified on the stable diffusion series. It demonstrates better performance over the baselines.

### Weaknesses
1. The main limitation is that this paper poorly extends the concept in static model to the finetuning area, which is a dynamic model. Specifically, the ineffective concept works in model pruning, which is a given fixed model. The ineffective parameters in such static model can be discarded or reused. However, in this paper, the model parameters dynamically change during finetuning, and unimportant parameters also change. Thus, a right way to extend such unimportant parameters is to study their dynamics over change, instead of simple reuse.  Simple reuse may have several issues, for example, smaller optimal parameter search space in the finetuning case.

2. Another concern may lie in how to merge multi tasks’ parameters, and their merging performance. The multi-task parameter merging is a good property of LORA. It is encouraged to explain and verify this.

### Questions
How to understand the better performance after setting some parameters to 0 in Section 3.1? This is actually interesting and may be useful for understanding the behavior of diffusion model.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a new method for fine-tuning diffusion models by training only low-value parameters making them effective on a new task. Additionally, a nuclear norm is used to prevent overfitting, and efficient selective backpropagation and progressive parameter adjustment reduce the memory and time requirements during training. The results show SaRA is on par or better than other fine-tuning methods in terms of FID, CLIP score, and qualitative assessment.

### Strengths
1. The paper is very well written and easy to follow. It has a good flow of information. Every claim is carefully explained and proven by experiments or analysis.
2. The novelty of the method is good. The idea of fine-tuning only ineffective parameters was explored before but combined with nuclear norm regularization, novel approach to backpropagation of a sparse matrices, and adaptive fine-tuning, creates a valuable addition to the field.
3. The experiments are extensive, both comparisons and ablation study.
4. Qualitative results suggest an improvement over other methods.
5. Quantitative results show the model behaves better or similar to other methods. I can see it becoming one of the methods of choice depending on one's needs.

### Weaknesses
1. Minor - as mentioned in Strengths 5., the results are not showing overall superiority over other methods.

### Questions
1. The authors should consider splitting Figures 2 b) and 5 into more subplots. In my opinion, they are too cluttered and it takes too much time to read them.
2. In Table 1, the use of "optimal" and "sub-optimal" is not correct, e.g. optimal FID is 0. "Best" and "second best" or something similar should be used.
3. Could the authors provide more qualitative results for the same prompts (Appendix C) with different seeds to see the diversity of the samples?
4. It would be good to include some of the visual results in the main text.
5. Can authors elaborate on how CLIP score is related to overfitting?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a PEFT method for diffusion models, which progressively trains selectively chosen parameters with small, inefficient values. To prevent memory waste, it avoids storing the gradient of all parameters and instead stores only the chosen parameters in separate nodes, which are then replaced after training.

### Strengths
- Unlike methods like LoRA that require additional parameters, this approach selects parameters within the existing model for fine-tuning, minimizing additional memory usage.
- Existing selective PEFT methods continuously update masks, which requires storing gradients for all parameters, making them inefficient. In contrast, this paper’s method progressively trains only the fixed parameters at each stage, storing only certain gradients, making it more memory-efficient.
- The paper conducts extensive comparison experiments with various versions of Stable Diffusion (SD) and different sizes of fine-tuning parameters.

### Weaknesses
 - Although the paper differentiates itself from selective fine-tuning, I think this method still appears to be a form of selective fine-tuning. The memory efficiency improvement seems to stem from implementing a separate node for gradient storage and selectively fine-tuning only those nodes, rather than from an inherent algorithmic difference.
- Selecting parameters based on a specific threshold seems not a new concept. For example, the related work PaFi is described that it also trains based on absolute values.
- The reasoning behind inefficient parameters becoming efficient during training due to the randomness of the training process is unclear. Since the initial weights are set randomly, many values are likely to change through training. There is no strong basis to assume a correlation with the initial values. Even parameters with initially small values are expected to converge toward the average distribution, making Figure 3 somewhat self-evident.
- Although selecting a mask based on a threshold is computationally efficient, this method is relatively naive compared to other SFT methods that dynamically choose parameters during fine-tuning, which may lead to lower performance. Although it was compared with LT-SFT, there is a lack of comparison with other SFT methods.
- In the table, it is unclear if this method offers a significant performance improvement. While the FID scores are mostly favorable, the CLIP scores appear to be higher for LoRA. Additionally, the L_rank removal in the ablation study does not lead to a significant performance change.

### Questions
- Would similar results be achievable if other SFT methods stored the selected parameters in leaf nodes and updated them as implemented here?
- Could you provide more explanation regarding the impact of training process randomness on initially inefficient parameters becoming efficient?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents SaRA, a method for fine-tuning pre-trained diffusion models that introduces progressive Sparse low-Rank Adaptation (SaRA) to enhance efficiency and reduce memory costs in adapting diffusion models to new tasks. The proposed method leverages parameters with low absolute values, presumed to have limited initial impact on the model’s performance, making them suitable for fine-tuning. SaRA combines sparse parameter updates with a nuclear norm-based low-rank constraint to mitigate overfitting. It also introduces a progressive parameter adjustment and unstructured backpropagation strategy, aimed at further memory efficiency. Extensive experiments demonstrate SaRA's superiority over traditional fine-tuning methods on image generation and customization tasks.

### Strengths
The paper clearly explains the intuition in parameter efficiency by proposing the use of low absolute value parameters for adaptive updates, effectively avoiding overfitting through a nuclear norm constraint.  The progressive parameter adjustment strategy positively contributes to the stability and convergence of model performance, while the unstructured backpropagation method effectively reduces memory costs, making SaRA a practical solution in resource-constrained environments. Additionally, the extensive experiments cover various tasks, such as image generation and customization, thoroughly validating the advantages of the SaRA method in balancing the preservation of model priors and the learning of task-specific knowledge.

### Weaknesses
My main concern centers on the assumption underlying this approach—that parameters with the smallest absolute values are inherently ineffective. This seems more empirical than rigorously substantiated. While small absolute values can indeed correlate with lower impact in certain contexts, particularly in pruning, their effectiveness actually depends on the model architecture and specific task. Small value parameters may exert less direct influence on the output, but they are not intrinsically ineffective; their impact can vary depending on training dynamics, model structure, and optimization objectives.

Some minor weaknesses include:
* The generalizability of the 'adapting small-value parameters' strategy across different architectures is crucial to ensure broader applicability. This paper only investigates the phenomenon of the pre-trained Stable diffusion models. In this sense, I'm worrying about whether it can be applied across different network architectures or frameworks.
* In the caption of Figure 3, weight distributions are claimed to be Gaussian without further clarification, which seems empirical rather than solid.
* The choice of threshold for selecting low-absolute-value parameters could be better justified. If this choice is sensitive, it could limit SaRA's robustness and generalizability across different diffusion models and tasks. An ablation study on this threshold choice would strengthen the claims.
* While the experiments show SaRA's success, the paper could benefit from an analysis of its limitations. For instance, discussing cases where SaRA may not perform as well, such as tasks requiring extensive re-training of high-impact parameters, would improve the comprehensiveness of the evaluation.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2
