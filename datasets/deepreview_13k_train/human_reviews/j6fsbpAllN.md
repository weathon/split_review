# Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Low-Rank Adaptation (LoRA) has emerged as a popular technique for fine-tuning large language models (LLMs) to various domains due to its modular design and widespread availability on platforms like Huggingface. This modularity has sparked interest in combining multiple LoRAs to enhance LLM capabilities. However, existing methods for LoRA composition primarily focus on task-specific adaptations that require additional training, and current model merging techniques often fail to fully leverage LoRA's modular nature, leading to parameter interference and performance degradation. In this paper, we investigate the feasibility of disassembling and reassembling multiple LoRAs at a finer granularity, analogous to assembling LEGO blocks. We introduce the concept of Minimal Semantic Units (MSUs), where the parameters corresponding to each rank in LoRA function as independent units. These MSUs demonstrate permutation invariance and concatenation-summation equivalence properties, enabling flexible combinations to create new LoRAs. Building on these insights, we propose the LoRA-LEGO framework. This framework conducts rank-wise parameter clustering by grouping MSUs from different LoRAs into $k$ clusters. The centroid of each cluster serves as a representative MSU, enabling the assembly of a merged LoRA with an adjusted rank of $k$. Additionally, we apply a dual reweighting strategy to optimize the scale of the merged LoRA. Experiments across various benchmarks demonstrate that our method outperforms existing approaches in LoRA merging.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the LoRA-LEGO framework, which combines multiple LoRAs for multi-task and mixed-task scenarios. It uses clustering to group MSUs from different LoRAs into k clusters before constructing a merged LoRA based on the cluster centroids. Parameter reweighting is then performed to scale the centroid with respect to the average cluster norm. Experiments are conducted against 4 baselines (weighted average, ensemble, task arithmetic and ties merging) for multi-task and mixed-task scenarios, showing improved average performance.

### Strengths
After reading the authors' rebuttals, my concerns have been adequately addressed.

### Weaknesses
1. The paper is generally well written with good illustrations. However, I found the approach not particularly novel. It relies on a straightforward k-means clustering method for grouping and subsequently aggregating cluster parameters.

2. The approach is not particularly strong, and this simplicity may limit the framework’s performance which is reflected in the empirical results. While the average performance across tasks improves, it does not apply to all tasks. For example, performance remains poor for WNLI, an out of domain task for multi-task learning.

3. The baselines involving LoRA composition methods are basic and are not established methods in existing literature. It lacks citations that would align them with related work. This weakens the comparative analysis and raises questions about the validity of the selected baselines.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed the LoRA-LEGO framework for combining Low-Rank Adaptation (LoRA) modules in large language models (LLMs). LoRA-LEGO introduces Minimal Semantic Units (MSUs), independent components within LoRA, enabling flexible merging through clustering and rank adjustment. This modular approach allows task-specific LoRAs to be disassembled and reassembled, tackling parameter misalignment and knowledge conflicts seen in traditional merging methods. The dual reweighting strategy optimizes the scale of the combined LoRA, resulting in a more efficient and flexible system that performs well across both in-domain and out-of-domain tasks.

### Strengths
* Modularity and Flexibility: The MSU-based modular approach enhances flexibility in merging LoRAs, allowing for custom rank adjustments.

* Efficient Scaling: Dual reweighting improves output scale management, maintaining model performance across tasks.

### Weaknesses
 * Performance may degrade when merging LoRAs designed for highly divergent tasks.

* Merging effectiveness can be highly sensitive to hyperparameter settings.

### Questions
1. How does LoRA-LEGO address performance degradation when merging LoRAs for tasks with significant divergence?

2. Why does performance improve for MRPC and RTE tasks in Table 1 following permutation merging?

3. How can the optimal number of clusters $k$ in equation (2) be determined?

4. Why does the weight averaging method in Table 3 achieve identical performance to the task-specific LoRA (upper bound) for the MRPC task?

### Soundness
4

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
2

### Summary
The paper presents an innovative framework called LoRA-LEGO, which enhances the merging of LoRA for large language models. The approach leverages the modularity of LoRAs by introducing Minimal Semantic Units (MSUs) and employs rank-wise clustering to optimize parameter efficiency and performance. The framework aims to overcome limitations in existing methods by reducing parameter interference and maintaining task-specific knowledge.

### Strengths
- The concept of treating LoRA parameters as LEGO blocks, specifically through MSUs, is creative and offers a fresh perspective on modularity in model adaptation.
- The paper provides solid theoretical foundations, including permutation invariance and concatenation-summation equivalence, which support the proposed method.
- Extensive experiments demonstrate the framework's effectiveness across multiple benchmarks, outperforming existing methods.

### Weaknesses
 - The MSU is not related to some semantics that can be understood by humans, it would be better if we could see some analysis.
- Although the proposed method outperforms existing approaches, a more detailed comparison with a wider range of baseline methods could strengthen the claims.
- It does not report the overhead (e.g., in inference and training time, memory) that may introduced by this approach.

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the concept of Minimal Semantic Unit (MSU) for disassembling and reassembling multiple LoRAs at a finer granularity. MSUs have permutation invariance and concatenation summation equivalence properties and thus enable flexible combinations for create new LoRAs. Evaluation results show the MSU-based approach achieves a good performance.

### Strengths
+ MSU is an interesting concept with permutation invariance and concatenation summation equivalence properties.

### Weaknesses
 - While MSU is an interesting concept, it is unclear why the finer granularity merging of LoRAs is the right approach for combing multiple LoRAs to enhance LLM capabilities: the clustering and the use of the centroid of each cluster essentially impact the performance of the merged LoRA. Specifically, the method of clustering LoRA parameters into MSUs and then using the centroid of each cluster for merging raises concerns about information loss and potential distortion of the original LoRA's learned representations. The process of averaging parameters within a cluster, especially if the cluster contains parameters with diverse functions, could lead to a merged representation that does not accurately reflect the nuances of the individual LoRAs. Furthermore, the reliance on a centroid might discard valuable information present in the variance of the parameters within each cluster.
- The evaluation used only 7 LoRAs. It is unclear how the proposed approach may work with more LoRAs. The limited number of LoRAs used in the evaluation raises questions about the scalability and robustness of the proposed approach. Merging a larger number of LoRAs could exacerbate the issues of parameter interference and knowledge conflict, potentially leading to a significant drop in performance. It is crucial to assess how the method performs with a more substantial number of LoRAs, as real-world applications may involve combining tens or even hundreds of LoRAs.

### Questions
How can the finer-grained merging of LoRAs preserve the performance of the merged LoRA, particularly in comparison with the approach of selecting individual LoRAs? How many LoRAs can be supported by the MSU-based approach, and what performance it can achieve with more (e.g., tens of) LoRAs?

### Soundness
2

### Presentation
2

### Contribution
2
