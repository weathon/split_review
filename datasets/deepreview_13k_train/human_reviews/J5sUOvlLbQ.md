# LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Large pre-trained models exhibit impressive zero-shot performance across diverse tasks, but fine-tuning often leads to catastrophic forgetting, where improvements on a target domain degrade generalization on other tasks. To address this challenge, we introduce LiNeS, Layer-increasing Network Scaling, a post-training editing technique designed to preserve pre-trained generalization while enhancing fine-tuned task performance. LiNeS scales parameter updates linearly based on their layer depth within the network, maintaining shallow layers close to their pre-trained values to preserve general features while allowing deeper layers to retain task-specific representations.
We further extend this approach to multi-task model merging scenarios, where layer-wise scaling of merged parameters reduces negative task interference. LiNeS demonstrates significant improvements in both single-task and multi-task settings across various benchmarks in vision and natural language processing. 
It mitigates forgetting, enhances out-of-distribution generalization, integrates seamlessly with existing multi-task model merging baselines improving their performance across benchmarks and model sizes, and can boost generalization when merging LLM policies aligned with different rewards via RLHF. Importantly, our method is simple to implement and complementary to many existing techniques. %

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a post-training editing technique, LiNeS, designed to address catastrophic forgetting and facilitate model merging after fine-tuning. LiNeS scales parameter updates linearly with the depth of layers within the network. The technique has shown significant improvements across various domains, including OOD generalization, single-task and multi-task model merging, demonstrating its effectiveness.

### Strengths
1. The paper is easy-to-follow.

2. The topic is essential yet the idea is moderate. Both regularized fine-tuning and model merging are important techniques for the community and the paper addresses two formulations simultaneously.

3. A new method that seems well-motivated and performs well on a lot of benchmarks.

### Weaknesses
1. I like the fact that the authors simply scale the task vectors. But I was not clear why directly edits the difference between the fine-tuned and pre-trained checkpoint via a linearly scaling coefficient ($α+β\frac{l-1}{L-1}$). Also, compare to existing methods, like `Ties-Merging` and `Consensus Merging`, what are the core strengths of this work? More efficient or simpler?

2. The point above also points to the limitation of the current framework, which is a lack of formal theory. It works very well experimentally, but some aspects are not very clear. Providing concrete theoretical analyses or proofs for linearly layer-wise scaling would be better.

3. There are numerous typos and bad grammar throughout the paper. The authors should do a very careful proofreading and fix all the errors.

4. Minor comments:
- Some of the content in the appendix can be put into the body to ensure that the body is a full 10 pages.
- It must be noted that the consistency in verb tense is not maintained throughout the document. For example, the second paragraph in the Introduction section.
- line 112 "task=specific"
-  Two identical sentences appear from line 223 to line 226.

### Questions
1. The basic assumption of this work is that the degradation of performance on control tasks is largely due to these distortions in the shallow layers. However, it lacks of formal theory.

2. From Fig. 2 and Fig. 7, fine-tuned models have obtained high performance for both target task and control tasks in some cases. Can catastrophic forgettinh happen when the result is high?  Please discuss or analyze these specific cases where fine-tuning seems to improve performance on both target and control tasks.

3. The result of "Model 2" in Fig. 10 is different from the other 69 curves, what is the reason?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces LiNeS, a post-training editing technique designed to enhance the generalization ability of fine-tuned models. LiNeS applies a layer-wise linear scaling function to modulate parameter updates, reducing them more in shallow layers than in deep layers. The method is evaluated across several settings to demonstrate its effectiveness.

### Strengths
- The paper is well-motivated and easy to follow.
- The experimental results seem impressive.

### Weaknesses
 - The validation set has a large influence on the OOD performance of the selected models [1]. I suggest the authors discuss the construction of the validation set and whether the same empirical trend can be observed with different validation sets, as suggested by [1]. Specifically, it is unclear how the validation set is constructed and if it is representative of the OOD test set. The paper should clarify if the validation set is sampled from the same distribution as the training data or if it is a separate dataset. Furthermore, it would be beneficial to explore the impact of different validation set sizes and compositions on the final OOD performance.
- The evaluation is limited to the transformer architecture. Including other model architectures, such as ResNet-based CLIP models, would validate whether the benefits of layer-wise scaling extend beyond transformer architecture. It is important to assess whether the observed improvements are specific to the transformer architecture or if they generalize to other architectures. The paper should include experiments on diverse architectures, such as CNNs and hybrid models, to provide a more comprehensive evaluation of the proposed method. This would also help to understand the limitations of the method and identify potential areas for improvement.
- There is a lack of sensitivity analysis for the hyper-parameter $\alpha$ and $\beta$ across different evaluation settings. The paper should include a detailed sensitivity analysis to understand how the performance of the method varies with different values of $\alpha$ and $\beta$. It is important to identify the optimal range of these hyper-parameters and to understand the trade-offs involved in choosing different values. The analysis should also explore the interaction between $\alpha$ and $\beta$ and how they affect the performance of the method. Furthermore, it is unclear if the optimal values of these hyper-parameters are consistent across different tasks and datasets.
- Typos should be checked. For example,
    - enchancing → enhancing (Line 23)
    - bcenchmarks → benchmarks (Line 24)
    - task=specific → task-specific (Line 112)
    - Figure 4 → Table 4

### Questions
- What could be an explanation for why the benefit of LiNeS appear to be smaller for deeper models (e.g. ViT-L/14 in Table 2) and models with smaller patch sizes (e.g. ViT-B/16 in Table 5)?

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
3

### Summary
This paper presents a novel post-training editing technique called LiNeS, designed to address the problem of catastrophic forgetting in large pre-trained models during fine-tuning. Catastrophic forgetting refers to the phenomenon where a model loses its generalization ability on other tasks when fine-tuned for a specific task. LiNeS balances the trade-off between retaining the generalization capability of the pre-trained model and enhancing performance on specific tasks through hierarchical scaling of parameter updates.

### Strengths
- The LiNeS method introduces a novel post-training editing technique that prevents catastrophic forgetting through hierarchical scaling of parameter updates.
- Extensive experiments validate the effectiveness of LiNeS across various scenarios, including single-task fine-tuning, multi-task model merging, and improved out-of-distribution (OOD) generalization.
- The LiNeS method is applicable not only to visual tasks but also to natural language processing tasks, demonstrating its cross-domain versatility.
- LiNeS can be integrated with existing multi-task model merging baselines.

### Weaknesses
 - The article does not discuss the performance of LiNeS in long-term maintenance and updating of models, particularly when faced with evolving data distributions.
- There is a lack of experimental results for LLM tasks.
- Comparisons with the performance of other fine-tuning methods (such as LoRA) are missing.

### Questions
- Are there additional experimental results for LLMs, including different models, datasets, and tasks?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a post-training technique designed to mitigate catastrophic forgetting; more specifically preserving pre-trained generalization while enhancing fine-tuned task performance. This is done by reducing the magnitude of parameter updates for the shallow-layers compared to the deeper-layers. The method boils down to a layer-wise linear interpolation between the fine-tuned and the pretrained model.

### Strengths
1) Overall the idea of the paper is pretty simple and should be easily reproducible. Further, the paper is clearly structured and mostly well-written.
2) The paper thoroughly evaluates the proposed method across multiple tasks. 
3) The results clearly demonstrates strong trade-off performance on both target and control tasks.

### Weaknesses
1) Theoretical analysis have not been provided to support the proposed idea. 
2) Some results lack details. For example, Table 1 what is the selected target and control tasks? Were all other combinations tried out? Not enough baselines have been added. Comparing to pretraining and fine-tuning performances is not enough.
3) How does learning the scaling factors perform compared to linearly scaling the parameter updates? Moreover, does the learned parameters have a consistent increasing trend from shallow-to-deep layers?

### Questions
1) Why a shallow layer must be updated less compared to a deeper layer? Theoretical analysis should be provided to why shallow layers need to be updated less than deeper layers and how does this method affects the model's representation space?
2) Clarify exactly which tasks were used as target and control in your results, and to explain their task selection criteria. Add more baselines that aims at protecting both generalization and the fine-tuning to a downstream task. This would clarify the performance improvements?
3) Conduct an ablation study comparing the linear scaling approach to a learned scaling approach, and analyze the resulting patterns in the learned scaling factors. 
4) How does the proposed method differ from applying different learning rates per layer (low LR for shallow layers and higher LR for deep layers) during fine-tuning? Include a comparison between the proposed post-training method and the layer-wise learning rate scheduling during fine-tuning. This would help clarify the unique benefits of the proposed approach.
5) Provide an experiment to compare your proposed approach to freezing different shallow layers and updating the deeper layers using fine-tuning. This includes, but not limited to, freezing the feature extractor and finetuning the classifier.

### Soundness
3

### Presentation
3

### Contribution
2
