# PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Model pruning is an effective approach for compressing Large Language Models (LLMs) and improving inference efficiency. However, this process often leads to significant degradation of model capabilities. While post-training techniques such as instruction tuning are commonly employed to recover model performance, existing methods often overlook the uneven deterioration of model capabilities and incur high computational costs due to extensive recovery training. Moreover, some instruction data irrelevant to model capability recovery may introduce negative effects. To address these challenges, we propose the **P**ost-training d**A**ta **S**election method for **E**fficient pruned large language model **R**ecovery (**PASER**). PASER aims to identify instructions where model capabilities are most severely compromised within a certain recovery data budget. Our approach first applies manifold learning and spectral clustering to group recovery data in the semantic space, revealing capability-specific instruction sets. We then adaptively allocate the data budget to different clusters based on the degrees of model capability degradation. In each cluster, we prioritize data samples where model performance has declined dramatically. To mitigate potential negative transfer, we also detect and filter out conflicting or irrelevant recovery data. Extensive experiments demonstrate that PASER significantly outperforms conventional baselines, effectively recovering the general capabilities of pruned LLMs while utilizing merely 4\%-20\% of the original post-training data and substantially reducing training computational overhead.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
PASER is a new method for efficiently recovering the performance of pruned Large Language Models (LLMs) by carefully selecting the most relevant training data. This three-step process begins by grouping instructions based on the LLM capabilities they target using SentenceBERT embeddings and NMF-based spectral clustering. Then, a Capability Degradation Score (CDS) is calculated for each group to identify the areas where model performance has suffered the most from pruning. The data budget is allocated accordingly, prioritizing these most affected clusters. Within each cluster, data samples with the highest Individual Efficiency Score (IES) are chosen to balance recovery benefits with computational costs. Lastly, a Concept Consistency Graph (CCG) is created to model relationships between concepts and prevent the selection of conflicting or irrelevant samples, mitigating negative transfer during training. Extensive experiments demonstrate that PASER effectively recovers pruned LLMs to near-unpruned performance levels using only part of the original data.

### Strengths
PASER addresses the uneven impact of pruning on different LLM capabilities by using a clustering technique to group instructions based on the capabilities they target. Instead of blindly using all available data or randomly selecting a subset, PASER allocates its data budget proportionally to the Capability Degradation Score (CDS) of each cluster. The use of a Concept Consistency Graph (CCG) helps identify and reject samples that might introduce conflicting or irrelevant information.

### Weaknesses
The quality of the initial pruning likely influences the effectiveness of PASER's recovery process. A poorly pruned model might present challenges that even a targeted recovery approach like PASER cannot fully overcome. 
Additionally, the novelty is not entirely there as this work fails to position itself in the expensive literature similar to this approach.

There are several works on dataset selection, in particular, instruction dataset selection:

[1] Hamish Ivison, Yizhong Wang, Valentina Pyatkin, Nathan Lambert, Matthew E. Peters, Pradeep
Dasigi, Joel Jang, David Wadden, Noah A. Smith, Iz Beltagy, and Hanna Hajishirzi. Camels in
a changing climate: Enhancing lm adaptation with tulu 2.

[2] Wei Liu, Weihao Zeng, Keqing He, Yong Jiang, and Junxian He. What makes good data for
alignment? a comprehensive study of automatic data selection in instruction tuning. 

[3] Peiqi Wang, Yikang Shen, Zhen Guo, Matthew Stallone, Yoon Kim, Polina Golland, and Rameswar
Panda. Diversity measurement and subset selection for instruction tuning datasets. 

[4] Simon Yu, Liangyu Chen, Sara Ahmadian, Marzieh Fadaee. Diversify and Conquer: Diversity-Centric Data Selection with Iterative Refinement.

[5] Yizhong Wang, Hamish Ivison, Pradeep Dasigi, Jack Hessel, Tushar Khot, Khyathi Chandu, David
Wadden, Kelsey MacMillan, Noah A Smith, Iz Beltagy, et al. How far can camels go? exploring
the state of instruction tuning on open resources.

[6] Mengzhou Xia, Sadhika Malladi, Suchin Gururangan, Sanjeev Arora, and Danqi Chen. Less: Selecting
influential data for targeted instruction tuning,

### Questions
- The paper mentions that instruction tuning data is preferred for LLM recovery due to its efficiency and ability to maintain general-purpose abilities. However, are there any limitations to using instruction-tuning data for this purpose? For instance, could there be scenarios where pre-training corpora or fine-tuning datasets might be more suitable for recovering specific capabilities heavily affected by pruning?

- The paper briefly mentions knowledge distillation as an alternative to supervised learning for recovery training. What are the potential benefits and drawbacks of using knowledge distillation compared to standard fine-tuning? How does PASER's performance differ when using knowledge distillation versus supervised learning? Could combining both approaches lead to further improvements?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel post-training selection method PASER to improve the recovery of pruned large language models. Specifically, this method first utilizes manifold learning and spectral clustering to cluster recovery data, and then allocate the data budget based on the degrees of model capability degradation. Experimental results show the effectiveness of PASER in pruned LLM recovery.

### Strengths
1. The paper is well-organized and easy to read with clear explanations of the technical details.
2. The proposed method PARSER includes semantic structural recovery instruction clustering and capability degradation-aware recovery instructions selection is simple yet effective. Experimental results across seven common sense reasoning datasets show some improvements compared with the full fine-tuning method.
3. The author conducts experiments on various types and scales of LLMs, resulting in a relatively comprehensive set of experimental results.

### Weaknesses
1. Cluster and then selection paradigm has been used in various data selection methods such as MoDS, and CaR, but the novelty is limited. And the selected data are limited to embedding models and clustering methods.
2. The author conducts extensive experiments, but these are limited to the common sense reasoning task. How does this method perform in other scenarios, such as code or mathematical reasoning tasks?  In these scenarios, where the probability of most tokens for a sample is high, how can the capability degradation score compare the scores between samples of different lengths balanced?

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

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
PASER proposes a method to recover pruned large language models (LLMs) while maintaining computational efficiency. The challenge in model pruning is performance degradation due to data irrelevance and computational costs. PASER employs manifold learning and spectral clustering to group data by specific capabilities, allocating recovery data budgets based on degradation severity in each cluster. This approach ensures balanced capability recovery, reduces computation, and mitigates negative transfer by filtering irrelevant data.

### Strengths
1.	PASER introduces a targeted post-training data selection approach, addressing the issue of uneven capability degradation in pruned models. This is a notable advancement over existing methods, which often lack specificity in data selection for capability recovery.
2.	The proposed method leverages spectral clustering and diffusion kernel methods for data grouping, and introduces a concept consistency graph to minimize negative transfer, highlighting innovative use of these techniques.
3.	Extensive experiments demonstrate PASER's effectiveness across different pruning methods and datasets. This validates the method’s applicability and robustness across a variety of scenarios, contributing to its reliability.

### Weaknesses
1.	While PASER is computationally efficient relative to prior approaches, the process of clustering and capability degradation-aware sampling might still pose a bottleneck for large-scale datasets or real-time applications. Specifically, the spectral clustering step, which involves eigenvalue decomposition of the affinity matrix, can become computationally expensive with a large number of data points. Furthermore, the iterative process of calculating capability degradation and subsequent data sampling adds to the computational overhead, potentially limiting its scalability for very large instruction datasets or real-time model recovery scenarios.
2.	While PASER attempts to filter out irrelevant or conflicting data using the Concept Consistency Graph (CCG), the approach for ensuring consistency could still allow for some degree of negative transfer if conflicting concepts are not comprehensively identified. The CCG relies on co-occurrence patterns, which may not fully capture nuanced semantic relationships or contextual dependencies. For instance, concepts that appear together frequently might still be semantically contradictory in specific contexts, leading to the inclusion of conflicting data during the recovery process. The paper should discuss the limitations of co-occurrence based concept relationships and their impact on model recovery.
3.	Dependence on Capability-Specific Clustering: The effectiveness of PASER hinges on the quality of the clustering step to segregate instructions by capability degradation. Errors in clustering or the inability to accurately map instructions to the affected capabilities could lead to uneven recovery, especially in complex or high-dimensional semantic spaces. The use of spectral clustering, while effective, is sensitive to the choice of parameters and the initial data representation. If the initial representation does not accurately reflect the underlying semantic structure, the clustering may group instructions incorrectly, leading to suboptimal data selection and recovery.

### Questions
1.	While PASER is computationally efficient relative to prior approaches, the process of clustering and capability degradation-aware sampling might still pose a bottleneck for large-scale datasets or real-time applications.
2.	While PASER attempts to filter out irrelevant or conflicting data using the Concept Consistency Graph (CCG), the approach for ensuring consistency could still allow for some degree of negative transfer if conflicting concepts are not comprehensively identified. It might be beneficial for the authors to discuss scenarios where CCG may not fully capture semantic conflicts and the resulting effects on model recovery.
3.	Dependence on Capability-Specific Clustering: The effectiveness of PASER hinges on the quality of the clustering step to segregate instructions by capability degradation. Errors in clustering or the inability to accurately map instructions to the affected capabilities could lead to uneven recovery, especially in complex or high-dimensional semantic spaces. Exploring alternative clustering or dimensionality reduction methods could strengthen the paper’s reliability.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
PASER is a new method to efficiently recover pruned large language models' abilities. It groups training data by capability, allocates resources based on where the model's performance dropped most, and removes unhelpful data. In tests on various models and pruning methods, PASER outperformed other approaches, restoring model performance using only 4-20% of the original training data and significantly reducing training time. While showing promise across different models and datasets,

### Strengths
the PASER framework is thoughtful and comprehensive, including semantic-structural, recovery instruction clustering, capability degradation-aware adaptive recovery instruction selection and negative transfer mitigation.

### Weaknesses
1. model recovery should be focused on the pre-training data, not instruction data since that's what the model has seen the most in training. The claim in line 45, that "instruction tuning data has emerged as a more preferred choice due to its superior efficiency in capability recovery", would need more citations and arguments to stand. 

2. Even if, for efficiency reasons, the authors choose to use instruction data for their experiments, they need to experiment and prove that each component in the PASER framework, the semantic-structural, recovery instruction clustering, capability degradation-aware adaptive recovery instruction selection and negative transfer mitigation, are contributing in some ways. And the authors need to tell us how each component improves. Those just need ablation studies but now not in the main paper.

3 in Appendix C, the authors state that logit distillation is better than label distillation when using a full dataset. this kind of contradicts the statement in the main paper, in line 407, that "the full version of data contains some irrelevant or conflicting information for capability recovery, resulting in the negative transfer during the training phase." If you find that logit distillation +  full dataset is comparable, or even better than label distillation +PASER selected dataset, you really have to sell hard here.

### Questions
I would be happy to revisit my score if weakness 2, the ablation studies for each component is fullfilled.

### Soundness
2

### Presentation
2

### Contribution
2
