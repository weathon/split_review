# Reduce, Reuse, and Recycle: Navigating Test-Time Adaptation with OOD-Contaminated Streams

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Test-Time Adaptation (TTA) aims to quickly adapt a pre-trained Deep Neural Network (DNN) to shifted test data from unseen distributions. Early TTA works only targeted simple and restrictive test scenarios that did not align with the philosophy of TTA that emphasizes practicality. Subsequent research efforts have thus been geared towards exploring more realistic test scenarios. In the same spirit, this work investigates for the first time TTA with data streams contaminated with out-of-distribution (OOD) data. Surprisingly, we observe the existence of benign OOD data that can improve TTA performance. We provide meaningful insights into the causes of benign OOD-contamination by analyzing the feature space of the pre-trained DNN. Inspired by these empirical findings, we propose R3, a novel TTA algorithm that specifically targets OOD-contaminated streams. Our experimental results verify that R3 improves competitive baselines by up to nearly 3%p on OOD-contaminated streams created with CIFAR-10-C and ImageNet-C.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies an interesting test-time adaptation (TTA) problem, namely TTA with OOD-Contaminated Streams, in which the data stream faces not only sample distribution shifts but also the presence of novel classes. The authors find the existence of benign OOD contamination and conduct experiments to analyze the underlying reasons. Based on the analysis, the authors further propose a R3 (Reduce, Reuse and Recycle) method. Experiments demonstrate the promise of R3. Frankly speaking, I was one of the reviewers when this work was submitted to NeurIPS. For the ICLR version, most of my concerns have been addressed and I only have the following questions and suggestions.

### Strengths
The studied problem of TTA with OOD-Contaminated data stream is practical and novel.

Analyses regarding benign OOD-contamination are interesting and contribute new insights.

Experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
According to Figure 4, the performance gain is mainly attributed to the "Filter" component, whereas the performance gains from the other components ("Cont" and "Unif") are a bit marginal.

- Why is there a difference in accuracy between "separate" and "mixed" for "Test (no adapt)" in Tables 1-3? Please include corresponding implementation details in the main paper. Moreover, I highly suggest the authors mix all 15 corrupted datasets rather than sampling a part of the test samples from each corrupted dataset, as the former one is more challenging to demonstrate the effectiveness of the proposed R3 method.

- Could the authors provide information on the number of OOD samples (with novel classes) that are filtered out by your method? This would help further validate the claim of "Benign OOD contamination."

- Will the proposed method still be effective under small batch sizes, e.g., 1, 2, 4? It would be better to provide these results even though it does not perform well enough.

- It would enhance comprehension if clear definitions of "shifted InD" and "OOD" were provided in the introduction. Additionally, it may be more appropriate to utilize alternative terms to describe "shifted InD" and "OOD," as "OOD" inherently encompasses "shifted InD" for the sake of general understanding.

- Many references have been published. Pls carefully check this and cite the corresponding published version.

- It would be better to clearly point out that in Tables 1-3 the clean stream accuracy is measured by Tent. Additionally, in Tables 1-3, the performance gain of Clean Stream (Tent) over “Test (no adapt)” is lower than other TTA papers. I guess this is because the authors use ResNet-50-BN from timm. Here I suggest the authors could also provide comparisons based on ResNet50BN from torchvision and include the results in the Appendix.

### Questions
- Why is there a difference in accuracy between "separate" and "mixed" for "Test (no adapt)" in Tables 1-3? Please include corresponding implementation details in the main paper. Moreover, I highly suggest the authors mix all 15 corrupted datasets rather than sampling a part of the test samples from each corrupted dataset, as the former one is more challenging to demonstrate the effectiveness of the proposed R3 method.

- Could the authors provide information on the number of OOD samples (with novel classes) that are filtered out by your method? This would help further validate the claim of "Benign OOD contamination."

- Will the proposed method still be effective under small batch sizes, e.g., 1, 2, 4? It would be better to provide these results even though it does not perform well enough.

- It would enhance comprehension if clear definitions of "shifted InD" and "OOD" were provided in the introduction. Additionally, it may be more appropriate to utilize alternative terms to describe "shifted InD" and "OOD," as "OOD" inherently encompasses "shifted InD" for the sake of general understanding.

- Many references have been published. Pls carefully check this and cite the corresponding published version.

- It would be better to clearly point out that in Tables 1-3 the clean stream accuracy is measured by Tent. Additionally, in Tables 1-3, the performance gain of Clean Stream (Tent) over “Test (no adapt)” is lower than other TTA papers. I guess this is because the authors use ResNet-50-BN from timm. Here I suggest the authors could also provide comparisons based on ResNet50BN from torchvision and include the results in the Appendix.

——Post Rebuttal——

I thank the authors for their response. However, most of my concerns are still being unaddressed now. The authors did no revisions regarding the Mixed Setting, ShiftID and OOD definition, Results under Small Batch Sizes, Citation Formats, etc. I shall lower my score as I think the current version is still below the high bar of ICLR.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on TTA with data streams contaminated with out-of-distribution (OOD) data. The authors analysis the reasons for of benign OOD-contamination. And they propose a R3 (Reduce, Reuse, and Recycle) TTA algorithm tailored to OOD-contaminated streams.

### Strengths
1.	The authors propose metrics of energy and similarity to identify harmful OOD instances.
2.	The authors propose a sample mixup method to alleviate the noisy learning signal from test labels.
3.	The proposed method achieves promising performance in the experimental results.

### Weaknesses
1.	I am still unclear about the distinction between “shifted InD data” and OOD data. While the authors introduce “shifted InD data” as corrupted in the input space but sharing the label space, the practical difference from standard OOD data in the context of TTA remains vague. The introduction of this concept at the end of page 1 without a clear, motivating example makes it difficult to grasp its significance and how it differs from typical domain shift scenarios. A more detailed explanation with concrete examples of how this “shifted InD data” is generated and why it requires a different treatment than standard OOD data is necessary.
2.	The concept of “benign OOD-contamination” needs further clarification. While the authors suggest it refers to OOD data helpful for TTA, the mechanism by which certain OOD samples become beneficial is not well-explained. Specifically, what characteristics of these OOD samples make them useful for adaptation, and how can we reliably identify them? Are they simply low-entropy samples, or is there a more nuanced relationship with the target domain that needs to be explored?
3.	In Section 4.1, the “Reduce” part, the advantages over EATA are not sufficiently justified. The authors claim that R3 is more effective, but a deeper analysis of why the combination of energy and similarity metrics outperforms EATA's filtering is missing. A comparison of the decision boundaries or the types of samples filtered by each method would be more insightful. Furthermore, while energy is used, the question of whether entropy could be used instead is not sufficiently addressed. A discussion of the theoretical and practical differences between energy and entropy in this context is needed.
4.	The handling of irrelevant OOD data, which does not share the label space, is not clearly explained. The authors mention that R3 remains blind to the distinction during adaptation, but how this impacts the learning process and the final model performance is not discussed. Does this blind adaptation lead to any negative transfer, and if so, how is it mitigated? A more in-depth analysis of the effects of irrelevant OOD data on the proposed method is required.
5.	The computational cost of the pipeline is a significant concern. While the authors acknowledge the latency increase compared to TENT, they do not provide a detailed analysis of the computational overhead. A comparison of the inference time and resource consumption with other SOTA methods is necessary to assess the practical applicability of the proposed method. Without this, it is difficult to determine if the performance gains justify the added computational burden.

### Questions
Some key concepts are not described clearly in the current manuscript. And some motivation behind current technique solutions remains unclear. If the authors can address my concerns, I would raise my scoring.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of TTA with OOD-contaminated data streams. They empirically reveal that the existence of benign OOD data can improve the adaptation performance on shifted ID data. Then, they introduce a stage-wise approach, term R3, to aid in the domain transfer process. Experimental results show that R3 improves baseline methods on OOD-contaminated streams created with CIFAR-10-C and ImageNet-C.

### Strengths
- The paper is well organized and with clear clarification.

- Based on the experiment results, this paper provides some findings or analyses.

### Weaknesses
 - My main concern is the motivation. Using external OOD data during training has empirically proved to be effective in OOD detection/generalization. However, in this manuscript, the authors appear to replicate these observed phenomena without introducing novel insights or furnishing theoretical guarantees specific to test-time adaptation. This redundancy raises questions about the contribution and originality of the work, necessitating a more comprehensive justification to substantiate the research's value. Moreover, the term 'benign' in the manuscript is vaguely defined, leading to potential confusion about what constitutes 'harmful' or 'malignant' in this context. Clarification from the authors would enhance the paper's clarity.

- The use of t-SNE visualization for validating assumptions on benign OOD data in the manuscript is notably heuristic and may not be entirely reliable. This situation gives the impression that the authors are attempting to validate one intuitive hypothesis using another intuitive tool, which significantly weakens the theoretical foundation of the paper.  For example, t-SNE is known to be sensitive to parameter settings and may not preserve global structure, making it an unreliable tool for drawing strong conclusions about the data manifold.

- The proposed method simply concatenates three stages without offering additional insights, particularly concerning the so-called `benign OOD data'. The authors need to delve deeper and elucidate how these stages interact and contribute to handling benign OOD data. Specifically, the paper lacks a clear explanation of how the dual filtering mechanism in R3 is designed to specifically preserve data that is beneficial for adaptation, and how the mixup and contrastive learning components are tailored to leverage the presence of benign OOD data, rather than just being generic regularization techniques.

- The experimental results indicate that the proposed method only achieves marginal improvements, which raises further doubts about whether the motivation of the paper has been accurately conveyed and validated. The authors need to address this issue by providing a more thorough analysis of the results and discussing potential reasons for the limited improvement, ensuring that the paper's objectives and contributions are clearly and convincingly presented. For example, the paper does not explore the sensitivity of the method to the amount of OOD data present in the stream or the specific types of OOD data used, which could provide valuable insights into the method's robustness and applicability.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to tackle test-time adaptation in an open-world setting where data from unseen classes (OOD data) and seen classes (InD data) are mixed up in the test data stream under the same distribution shift. Based on empirical observation, this paper claims that the existence of OOD data can benefit the adaptation of the pre-trained model on shifted InD data. A TTA algorithm is further proposed with OOD data filtering and recycling, similarity-based data mixup, and contrastive learning with class-wise prototypes. Experimental results on CIFAR-10-C and ImageNet-C are illustrated. No theory is provided.

### Strengths
1. This paper considers test-time adaption in the open world, which is interesting and realistic.

2. This paper tackles the OOD-contaminated distribution-shifted data streams by rigorously filtering out OOD data and then learning the shifted InD and OOD data with different training objectives.

3. Experimental results on CIFAR-10-C and ImageNet-C show that the proposed algorithm outperforms the baselines under single and mixed corruption scenarios.

### Weaknesses
1. The claim of "benign OOD contamination" is not strong enough:
   - Experimental settings are lacking to show a fair comparison between test streams with and without OOD contamination. Specifically, the paper does not isolate the effect of OOD data by comparing performance on a shifted InD test set with and without the addition of OOD samples, while controlling for the total number of samples used for adaptation. It is crucial to demonstrate that the performance gain is not simply due to a larger number of samples being used for adaptation when OOD data is present. The current experiments do not provide a clear picture of how much the OOD data helps or hinders the adaptation process.
   - The total number of data samples is not mentioned in the comparison. If test streams with OOD data have more data than those without OOD data, there is not enough evidence to show that the improvements come from auxiliary signals provided by OOD data rather than the increase of shifted data samples. The paper needs to explicitly state the number of InD and OOD samples used in each experiment to allow for a proper analysis.
   - Only batch norm adaptation is discussed and analyzed. While batch norm adaptation is common in TTA, the paper should acknowledge and discuss the potential impact of adapting other parameters, such as the classifier weights or feature extractor, and how this might interact with the presence of OOD data.

2. The discussion about benign and harmful OOD data is not sufficient.
   - According to which measure can we distinguish benign OOD data and harmful OOD data? The paper needs to define a clear and quantifiable measure or metric to differentiate between benign and harmful OOD data, instead of relying on post-adaptation performance. Without a clear definition, it is hard to evaluate the effectiveness of the proposed filtering mechanism. For example, are OOD samples with high cosine similarity to InD samples always benign? What is the threshold for considering an OOD sample benign based on cosine similarity?
   - Does the advancement of R3 come from the removal of OOD data or the preservation of benign OOD data? The main experiment results show that R3 only outperforms the clean stream baseline under a few OOD-contaminated scenarios. Does it mean that benign OOD data is also removed during the filtering process? This highlights a lack of clarity on the mechanism by which R3 improves performance. It is unclear if the performance gains come from removing harmful OOD data or from effectively utilizing the benign OOD data, or both. A more detailed ablation study is needed to isolate the contribution of each component.

3. The reason for using cosine similarity is not clearly stated. Using cosine similarity alone as the filtering scheme is also recommended in the ablation study. While cosine similarity is a common metric, the paper needs to provide a more thorough justification for why it is suitable for filtering OOD data in this specific context. What are the limitations of relying solely on cosine similarity? Are there other similarity metrics that could be more effective?

4. Why perform the filtering process on mixed shifted InD data? It is not clear why the filtering process is applied to a mixture of shifted InD and OOD data. Why not filter the OOD data first, and then perform adaptation on the shifted InD data? The paper should provide a clear rationale for this design choice.

5. Discussions regarding the effect of batch size and the ratio of InD to OOD data on the performance of R3 are also recommended. The paper should include a more detailed analysis of the impact of batch size and the ratio of InD to OOD data on the performance of the proposed method. This is critical for understanding the robustness and practical applicability of the method.

6. Although it outperforms baselines in the mixed corruption scenario, R3 still fails to improve the pre-trained model on CIFAR-10-C+SVHN/DTD/DTD+SVHN and ImageNet-C with OOD data. This suggests that the proposed method is not universally effective, and its limitations need to be further explored. The paper should analyze the specific conditions under which R3 fails to improve performance and identify the potential causes for these failures.

### Questions
Please [Weaknesses]

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
