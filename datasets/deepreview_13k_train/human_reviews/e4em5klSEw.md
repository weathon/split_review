# CLIP-MoE: Towards Building Mixture of Experts for CLIP with Diversified Multiplet Upcycling

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
In recent years, Contrastive Language-Image Pre-training (CLIP) has become a cornerstone in multimodal intelligence. 
However, recent studies have identified that the information loss in the encoding process of CLIP is substantial.
Such deficiency significantly limits the ability of a single CLIP model to handle images rich in visual detail.
In this work, we propose a simple yet effective model-agnostic strategy, \textbf{Diversified Multiplet Upcycling (DMU)} for CLIP. 
It integrates multiple CLIP models that capture diversified, complementary information into a Mixture of Experts (MoE) architecture.
Inspired by the recently proposed Multistage Contrastive Learning (MCL), which constructs multiple CLIP models that share the same structure while capturing different complementary information, Diversified Multiplet Upcycling efficiently fine-tunes a series of CLIP models from a dense pre-trained CLIP checkpoint to capture different feature distributions, sharing parameters except for the Feed-Forward Network (FFN). These models are then transformed into a \textbf{CLIP-MoE} with a larger model capacity but minimal computational overhead. 
Extensive experiments demonstrate the significant performance of CLIP-MoE across various zero-shot retrieval, zero-shot image classification tasks, and downstream Multimodal Large Language Model (MLLM) benchmarks by serving as a vision encoder. Furthermore, Diversified Multiplet Upcycling enables the conversion of any dense CLIP model into CLIP-MoEs, which can seamlessly replace CLIP in a plug-and-play manner without requiring further adaptation in downstream frameworks.
Through Diversified Multiplet Upcycling, we aim to provide valuable insights for future research on developing more efficient and effective multimodal learning systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a novel method, Diversified Multiplet Upcycling (DMU), for constructing Mixture of Experts (MoE) on CLIP models. The study showcases the effectiveness of DMU by presenting results on zero-shot image retrieval benchmarks, zero-shot image classification benchmarks, and MLLM understanding benchmarks by integrating it as the vision encoder in Llava-1.5. The findings demonstrate that DMU is indeed effective in enhancing the performance of CLIP models.

### Strengths
The experiments conducted in this study cover a wide range of tasks including zero-shot retrieval, classification, and MLLM understanding. By comparing against the original OpenAI CLIP large model, LongCLIP, and Llava-1.5, the results demonstrate superior performance of the proposed method. Additionally, this work shows that the Diversified Multiplet Upcycling (DMU) is more efficient compared to simply upcycling the FFN to a MoE.

### Weaknesses
1. The zero-shot image classification results should be more diverse. Only including ImageNet, ImageNet-O, ImageNet-V2, CIFAR-10, and CIFAR-100 is not sufficient. Please refer to the CLIP benchmark [1]. I believe that including ImageNet, ImageNetV2, ImageNet-A, ImageNet-R, ImageNet-Sketch, and ObjectNet datasets is essential for a more comprehensive evaluation.

2. I'm interested in the performance on the MM-Vet benchmark.

### Questions
please see weaknesses

### Soundness
3

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
3

### Summary
This work applies the recent popular concept of Mixture of Experts (MoE) in LLMs to CLIP. Specifically, it first uses Multistage Contrastive Learning (MCL) to lightly train various diversified FFNs. Then, these FFNs are used as experts in a CLIP-MoE, and the router is fine-tuned to obtain the final model. The work achieves impressive results in zero-shot image-text retrieval and zero-shot image classification tasks.

### Strengths
1. This work claims to be the first attempt to apply MoE to a CLIP-style model. I also believe it is an early attempt at incorporating MoE into contrastive learning.
2. The authors propose a novel method for initializing multiple experts in MoE, using MCL to first train and obtain diverse yet meaningful experts.
3. The proposed method is efficient, as it does not require retraining from scratch.
4. The paper is well-written, allowing me to quickly understand the authors’ key ideas.

### Weaknesses
1. The motivation behind this work—that CLIP often encodes inputs in a very coarse-grained manner—is neither novel nor particularly compelling. Additionally, the paper lacks an in-depth analysis of why this issue arises and does not clearly explain how the proposed method addresses it. The introduction could benefit from further refinement, as it currently seems to have chosen a weak motivation simply to justify applying MoE to CLIP.

2. The rationale for using Multistage Contrastive Learning (MCL) is not fully convincing. The paper suggests that clustering can simulate grouping raw data by attributes, such as color or shape. However, as clustering is conducted entirely within CLIP’s feature space, this outcome is not necessarily assured. The authors could strengthen their argument by visualizing each expert’s focus on distinct details, using methods such as t-SNE. Additionally, the routing analysis and case study presented in the experiments are too general to effectively illustrate MCL’s advantages. Beside, a more targeted comparison that highlights each expert's independent downstream task performance would provide clearer insights into the effectiveness of MCL.

3. The zero-shot tasks for CLIP lack sufficient comparisons to other state-of-the-art methods. This work mainly compares against Long-CLIP, which was primarily designed for sequence extension rather than enhancing CLIP’s zero-shot performance in downstream tasks.

4. The design of the ablation study is somewhat unclear. The sole comparison (w/o S1, S2) introduces too many variables, such as the number of experts, whether the experts were fine-tuned, and whether fine-tuning occurred on the original dataset or the clustered data (assuming clustering aims to mine hard negatives). The authors should design more distinct ablation studies to clearly demonstrate the contribution of each component.

5. Minor typo: in line 488, "Table 2" should refer to "Figure 2."

### Questions
1. In the MCL process, is each FFN initialized from the previous stage’s FFN or from the pre-trained CLIP FFN?

2.  Why does upcycling appear less effective than direct fine-tuning in Table 1, yet w/o S1 S2 in Table 4, it outperforms both methods significantly, such as on Flickr I2T?

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
4

### Summary
The paper presents a novel model-agnostic fine-tuning strategy called Diversified Multiplet Upcycling (DMU) for enhancing the CLIP framework. This approach utilizes the sparsely activated Mixture of Experts (MoE) architecture to extend model capacity without the need for training from scratch, instead leveraging pre-trained dense checkpoints. DMU fine-tunes a base dense CLIP model to create multiple multiplet experts through Multistage Contrastive Learning (MCL), which encodes diverse information via clustering. These multiplet models share all parameters except for the feed-forward network (FFN) layers, resulting in specialized FFN experts that capture different input aspects.

### Strengths
1. It introduces a new perspective on fine-tuning CLIP with Multistage Contrastive Learning (MCL) and validates this method through proper experiments. 

2. The results show improvements across various downstream tasks, indicating its potential effectiveness in practical applications, supported by coherent writing and a relative reasonable experimental setup.

### Weaknesses
1. A substantive assessment of the weaknesses of the paper. Focus on constructive and actionable insights on how the work could improve towards its stated goals. Be specific, avoid generic remarks. For example, if you believe the contribution lacks novelty, provide references and an explanation as evidence; if you believe experiments are insufficient, explain why and exactly what is missing, etc.

2. Firstly, there is a mislabeling in the paper. In Section 5.5, Table 1 presents the results of the text-to-image retrieval experiment on the COCO dataset. The CLIP-MoE model trained on the Recap-DC dataset achieved an @10 value of 79.4, which is lower than the Upcycling's 79.9. However, the value of 79.4 is erroneously bolded, which may lead to confusion. It is recommended that this be corrected to avoid misinterpretation of the results.

3. Secondly, it might be beneficial to include an analysis of the number of experts utilized in the method. Currently, the CLIP-MoE employs 4 experts to balance performance and computational cost. However, conducting experiments to demonstrate how varying the number of experts—either increasing or decreasing—affects both performance and computational efficiency could provide more compelling evidence for the chosen configuration.

4. Thirdly, while Multistage Contrastive Learning is described in the paper as enabling experts to learn different aspects of features—such as color, texture, and shape—this explanation seems to lack supporting experimental results. To strengthen this claim, it would be beneficial to provide concrete evidence, such as demonstrating that models trained at different stages exhibit distinct capabilities on datasets characterized by these specific features. Alternatively, offering a more nuanced explanation of the effectiveness of Multistage Contrastive Learning would help clarify its role and prevent potential misunderstandings.

5. Lastly, I think the explanation in the ablation study section to be unclear. This section mentions training a CLIP-MoE model with two experts, while Table 4 compares a fully trained CLIP-MoE with a model that has not undergone the first and second stages of MCL training. First, is the latter the CLIP-MoE model with two experts mentioned in the paper? Additionally, based on my understanding, since the fully trained CLIP-MoE in the paper includes 4 experts, it should undergo 4 stages of MCL training. The results related to the CLIP-MoE in Table 4 are also obtained after 4 stages of MCL training. Why is a model that has not gone through the first and second stages of training used for comparison?

### Questions
Please see the weakness section.

### Soundness
2

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
This paper proposed a novel Diversified Multiplet Upcycling for CLIP. Using relatively low computational cost, it trained a CLIP model with a Mixture of Experts (MoE) structure through Multistage Contrastive Learning, enabling the model to capture more fine-grained image information. The designed CLIP-MoE performs well in zero-shot retrieval, zero-shot image classification, and MLLM downstream tasks.

### Strengths
1. Achieved a Mixture of Experts (MoE) architecture for CLIP and proposed the Diversified Multiplet Upcycling method for CLIP.
2. Attained strong results with relatively low computational cost.
3. The paper provides extensive experimental results, evaluating CLIP-MoE’s performance in zero-shot retrieval, zero-shot image classification, and MLLM downstream tasks.

### Weaknesses
See Questions

### Questions
1. The paper claims that compared to the standard CLIP which often encodes inputs in a very coarse-grained manner, CLIP-MoE is able to encode richer information. I am curious about CLIP-MoE's performance in fine-grained image classification tasks, such as on the Stanford Cars, FGVC-Aircraft, Flowers102 and so on.

2. From the experimental results on LLaVA-1.5, replacing the CLIP in the LLaVA model with CLIP-MoE does not significantly improve performance across the five benchmarks; in fact, there are even some cases of performance decline. Additionally, the test results of the MLLM on benchmarks like MME and POPE fluctuate considerably. Are there other benchmark results, or perhaps reasoning cases for MLLM, that can further demonstrate CLIP-MoE’s ability to encode richer information in MLLM?

3. Why did you choose 4 experts? Is there a particular reason for this choice, and is there any observed relationship between the number of experts and CLIP-MoE’s performance?

I may reconsider my score based on your response to these issues.

### Soundness
3

### Presentation
3

### Contribution
3
