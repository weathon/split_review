# Ensembles of Low-Rank Expert Adapters

- Decision: Accept
- Scores: 5, 6, 6, 6, 6

## Abstract
The training and fine-tuning of large language models (LLMs) often involve diverse textual data from multiple sources, which poses challenges due to conflicting gradient directions, hindering optimization and specialization.  These challenges can undermine model generalization across tasks, resulting in reduced downstream performance.  Recent research suggests that fine-tuning LLMs on carefully selected, task-specific subsets of data can match or even surpass the performance of using the entire dataset.  Building on these insights, we propose the Ensembles of Low-Rank Expert Adapters (ELREA) framework to improve the model's capability to handle diverse tasks.  ELREA clusters the training instructions based on their gradient directions, representing different areas of expertise and thereby reducing conflicts during optimization.  Expert adapters are then trained on these clusters, utilizing the low-rank adaptation (LoRA) technique to ensure training efficiency and model scalability.  During inference, ELREA combines predictions from the most relevant expert adapters based on the input data's gradient similarity to the training clusters, ensuring optimal adapter selection for each task.  Experiments show that our method outperforms baseline LoRA adapters trained on the full dataset and other ensemble approaches with similar training and inference complexity across a range of domain-specific tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Ensembles of Low-Rank Expert Adapters (ELREA), a framework that combines efficient adaptation techniques to resolve conflicting gradients in LLM fine-tuning. By leveraging gradient clustering, the study creates expert adapters for diverse tasks, independent of specific data features. Results indicate that ELREA outperforms baseline LoRA adapters and other expert and self-consistency methods across various applications.

### Strengths
1.  The presentation is well.
2.  The method section of the paper is clearly articulated, especially Figure 1, which is a clear and self-explanatory flowchart. 
3.  Major differences of MoE and Deep Ensembles are highlighted (P.4). Assumptions (P.5) and limitations (P.10) are clearly stated.
4.  Included detailed appendices to further explain the datasets, experiment setups so the main body is not bulky.

### Weaknesses
Missing Paper Structure. The section “Related Work” should be better put in the Appendix.

Limit of Novelty. This paper proposes combine two points together creatively. However, the method for data selection and partitioning (Section 3.2) directly depends on [1]. Moreover, the per-cluster fine-tuning actually has little to do with LoRA; for instance, we could also use full-parameter or soft-prompt tuning for each cluster. Therefore, the motivation for exclusive “LoRA” is not adequate, which needs further illustration.

Lack of comparison with other “LoRA” baselines. It would be more complete if some mixture-of-lora-expert methods[2,3] are included to compare appropriately. 

Some writing typos that will not affect the rating scores:

* A few minor grammatical mistakes are found (e.g. P.4: which is the most adapted for LM fine-tuning; P.6: we the weights do not need to sum to 1).

* Undefined symbols: x_{t} in (1) on P.2; d_{model} on line 2 of P.3; cos’ in (9) on P.6 [they are interpretable but the authors should state clearly].

* Conflicting symbol: sigma^bar_c on the line above (8) and in (8) have different formulae on P.5.

* Figure 1: The paragraph following the section heading “3 Method” (P.4) said “The pipeline, shown in Figure 1, consists of three main steps” but the “steps” are not clearly shown in Figure 1. Simply speaking, the 4 phrases in Figure 1 do not match the 3 steps.

* The reference item “Improving language understanding by generative pre- training” (Radford et al.) on P.15 seems to be incomplete. A possible URL: https://cdn.openai.com/research-covers/language- unsupervised/language_understanding_paper.pdf

### Questions
Please see the weakness section.

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
2

### Summary
This paper proposes a novel two-stage fine-tuning method for large language models, named ELREA. In the first stage, ELREA trains a general adapter on the entire fine-tuning dataset. In the second stage, it clusters the training data into multiple groups and trains a specialized adapter for each group. During inference, ELREA dynamically selects the most suitable adapter based on the gradient similarity between the input data and the training clusters. Experimental results confirm the effectiveness of ELREA.

### Strengths
1. The paper is well-written and easy to understand.
2. The combination of LoRA with gradient-based clustering for expert adapters to address the conflicting gradient issue is interesting.
3. The framework’s design is well-structured, and the authors provide extensive experimental validation to demonstrate the efficacy of ELREA.

Since I am not very familiar with the latest work in the field of LLM fine-tuning, I may not be in the best position to assess the novelty of this paper. This paper is interesting for me. I am inclined to accept and respect the opinions of other reviewers.

### Weaknesses
1. As discussed by the authors in the limitations section, the computational and memory overhead of ELREA is substantial.
2. The paper lacks an in-depth discussion on the robustness of the clusters and the impact of the clustering algorithm (BIRCH) on performance. Since clustering is central to ELREA, variations in cluster formation could significantly affect adapter performance.

### Questions
Why is the base adapter still used during the inference phase? Since the cluster adapters are derived from the base adapter, they should already contain the necessary information from it. Could the authors’ inclusion of the base adapter at inference suggest that the cluster adapters may have forgotten some useful information from other clusters during training?

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
4

### Summary
The authors presented a framework aimed at enhancing the fine-tuning of large language models (LLMs) by addressing challenges related to conflicting gradient directions. By clustering training instructions according to their gradient features and independently training expert adapters on these clusters using the Low-Rank Adaptation (LoRA) technique, the authors proposed a method to improve training efficiency and model scalability. The framework dynamically selected the most relevant adapters during inference to optimize performance, which was demonstrated through experiments to outperform baseline methods and other ensemble approaches across various domain-specific tasks.

### Strengths
1.	The authors explained the challenges of fine-tuning large models from the perspective of gradient conflicts, which is a novel approach. They then propose clustering training samples based on their gradients and training them separately using LoRA. By integrating multiple LoRA adapters, they enhance the performance of LoRA fine-tuning.

2.	The authors’ writing structure is well-organized and the text is clear and easy to understand. Additionally, the research methodology is rigorous, with detailed experiments conducted.

### Weaknesses
1.	The authors did not discuss the complexity of the method. Compared to the vanilla LoRA, this approach introduces a clustering process and the training of multiple LoRAs, which inevitably increases the complexity of training. Additionally, computing different LoRA weight combinations for each sample could also lead to a decline in inference performance. Although the author's method does indeed improve accuracy, whether it is practical in real-world scenarios requires further discussion.

2.	The authors’ experimental comparisons are not sufficiently comprehensive. Currently, there are many methods dedicated to enhancing LoRA's performance on multitasking, such as MixLoRA[1], MultiLoRA[2], and MOELoRA[3]. However, the MOE methods compared by the author appear to be just modified versions of their own approach, which might be more suitable for inclusion in an ablation study. If the authors could compare their method with these more advanced techniques, it would further demonstrate the effectiveness of the proposed method.

3.	The authors use the random clustering approach for training, and the performance is only slightly worse than the gradient-based clustering method. This suggests that the gradient-based approach may not be essential, which contradicts the overall motivation of the method.

### Questions
1.	Could you have provided more details on the computational overhead associated with the ELREA framework?

2.	You use 5,000 samples for clustering, which is a relatively small portion of the entire training set. If the sample changes, could this lead to different clustering results and significantly alter the final training outcomes? In other words, does this clustering method possess stability?

3.	For the experiments where the performance gains from gradient-based clustering are far less significant than those from LoRA ensembling, can you provide a reasonable explanation? If clustering is not used, and each LoRA is trained using different random seeds and then ensembled, could this also achieve good performance?

### Soundness
3

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
The paper explores the issue of gradient conflict during multi-source data training. It addresses this problem by clustering gradients and training LoRA for each cluster, followed by ensembling to avoid the conflicts. Subsequent experiments on multiple datasets validate the effectiveness of the proposed method.

### Strengths
Using gradient features for clustering provides a more direct solution to the gradient conflict issue compared to clustering based on sentence embeddings, resulting in improved performance.

### Weaknesses
1. The paper does not sufficiently justify the choice of ensembling over a mixture of experts (MoE) approach. It mentions that ensembling performs better in value prediction and uncertainty estimation; however, this may not hold true for NLP tasks. In fact, MoE can optimize routing at a finer granularity, which may yield better performance compared to ensembling. This should be discussed in the paper. Additionally, a comparison should be made during the second stage of training cluster-specific LoRA, where a router could be trained alongside (with similar computational overhead) instead of using ELREA's weights for routing.
2. The paper needs to address the algorithm's time complexity. The overall process is lengthy and involves additional gradient calculations, leading to higher computational costs compared to other methods. Discussing these costs is essential for the practical application of the proposed method.

### Questions
1. Since the training of adapters consists of two stages (base LoRA and cluster LoRA training), my understanding is that the base LoRA's role is to learn general knowledge and assist in subsequent gradient estimation, while the cluster LoRA fine-tunes the model further. Could a higher-rank base LoRA be used, while training lower-rank LoRA for different clusters, to achieve faster adaptation?
2. Regarding clustering by gradients, what patterns exist within the data in each cluster? Are the tasks within each cluster more similar to each other?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Ensembles of Low-Rank Expert Adapters (ELREA), an ensemble-style LoRA MoE model to improve task adaptability and mitigate optimization conflicts in LLM fine-tuning. ELREA tackles gradient conflicts from diverse data sources by grouping tasks with similar gradient directions, creating specialized experts for each group. During inference, ELREA dynamically assigns weights to these experts based on gradient similarity with the input task instruction, selecting the most relevant experts for each task. Compared to traditional deep ensembles and standard MoE models, ELREA strikes a balance between performance and computational efficiency. Experimental results validate ELREA’s effectiveness.

### Strengths
- The paper is well-written and easy to follow.
- The model introduces a novel approach by designing experts based on gradient directions, rather than relying on an explicitly learned gating function, which is innovative in MoE design.
- The experiments demonstrate the model’s competitive performance across diverse tasks.

### Weaknesses
Overall, as the authors acknowledge in the limitations, the main weakness lies in efficiency and computational cost:

- In the inference stage, ELREA requires combining predictions from all expert adapters and the base adapter, resulting in inference costs that increase linearly with the number of experts, which can restrict practical applications. This is particularly problematic when deploying to resource-constrained environments or when low-latency is critical. The computational overhead of combining all expert predictions at each inference step significantly limits the scalability of the model.
- During inference, the model needs to first compute and store gradients for different task instructions. This pre-computation step adds latency and memory overhead, making real-time or interactive applications challenging. The need to store gradients for each task instruction also increases memory requirements, especially when dealing with a large number of tasks.
- Additionally, clustering gradients during training introduces extra computational overhead. The clustering process, while necessary for creating specialized experts, adds to the overall training time and resource consumption. The computational cost of clustering needs to be carefully considered, especially when scaling to larger datasets or more complex tasks.
- Although ELREA shows stronger performance compared to baselines like "MoE Routing", this advantage is somewhat diminished by its high inference costs. The performance gains achieved by ELREA must be weighed against the substantial increase in computational costs, especially during inference.

The baseline implementations could be more complete:

- The current implementation of "MoE Routing" bypasses training the MoE gate and instead directly uses weights similar to ELREA’s ensemble approach. However, training the MoE gate separately at each layer would make the baseline comparison more robust. This simplification of the MoE gate in the baseline could lead to an unfair comparison, as the full potential of MoE routing is not explored.

The marginal benefit of ELREA diminishes as the backbone model scales while the inference cost significantly increases. Additionally, there is limited comparison with a 9B model in the experimental results.

### Questions
1. Could ELREA maintain most of its performance by the ensemble of sparse experts, like the top-4 or top-1 experts in addition to the base adapter, to reduce inference costs?

2. Regarding the completeness of baselines, there could be an additional version of "MoE Routing" similar to those implemented in MoLE [1] or LLaVA-MoLE [2]. Further comparisons with other LoRA MoE methods like LoraHub [3] will make the baseline comparisons more robust.

3. Is the clustering process a time-intensive part of the training process?

[1] Wu, Xun, Shaohan Huang, and Furu Wei. "Mixture of LoRA Experts." The Twelfth International Conference on Learning Representations, 2024, https://openreview.net/forum?id=uWvKBCYh4S.

[2] Chen, Shaoxiang, Zequn Jie, and Lin Ma. "Llava-mole: Sparse mixture of lora experts for mitigating data conflicts in instruction finetuning mllms." *arXiv preprint arXiv:2401.16160* (2024).

[3] Huang, Chengsong, et al. "Lorahub: Efficient cross-task generalization via dynamic lora composition." *arXiv preprint arXiv:2307.13269* (2023).

### Soundness
2

### Presentation
3

### Contribution
2
