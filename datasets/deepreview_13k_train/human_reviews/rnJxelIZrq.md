# Beyond Mere Token Analysis: A Hypergraph Metric Space Framework for Defending Against Socially Engineered LLM Attacks

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Recent jailbreak attempts on Large Language Models (LLMs) have shifted from algorithm-focused to human-like social engineering attacks, with persuasion-based techniques emerging as a particularly effective subset. These attacks evolve rapidly, demonstrate high creativity, and boast superior attack success rates. To combat such threats, we propose a promising approach to enhancing LLM safety by leveraging the underlying geometry of input prompt token embeddings using hypergraphs. This approach allows us to model the differences in information flow between benign and malicious LLM prompts.

In our approach, each LLM prompt is represented as a metric hypergraph, forming a compact metric space. We then construct a higher-order metric space over these compact metric hypergraphs using the Gromov-Hausdorff distance as a generalized metric. Within this space of metric hypergraph spaces, our safety filter learns to classify between harmful and benign prompts. Our study presents theoretical guarantees on the classifier's generalization error for novel and unseen LLM input prompts. Extensive empirical evaluations demonstrate that our method significantly outperforms both existing state-of-the-art generic defense mechanisms and naive baselines. Notably, our approach also achieves comparable performance to specialized defenses against algorithm-focused attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
LLMs are susceptible to socially engineered jailbreak attacks, which remains underexplored by traditional defense methods. This paper proposed a new defense method specifically designed against socially engineered jailbreaks, based on a hypergraph approach. This method captures both sequential and semantic relationships among tokens to understand underlying intent, constructs hypergraphs from each prompt, and trains an SVM classifier as a prompt filter to detect jailbreak prompts. They theoretically provided the upper bounds of the generalization error of the proposed filter. The experiments demonstrated the effectiveness of the proposed defense against socially engineered jailbreaks on Llama-3.1 and GPT-4.

### Strengths
1.	This paper brings a novel perspective by introducing a hypergraph-based method for representing and analyzing LLM prompts. 
2.	Addressing socially engineered jailbreak attacks contributes to a crucial yet underexplored area in LLM security.
3.	The overall writing is well-structured, and the theoretical proofs provide strong justification for the method’s design.

### Weaknesses
1. The paper omits several advanced LLM defenses (e.g., SmoothLLM mentioned in Related Works) from the baseline comparisons, which limits the strength of the results. Including these methods would provide a clearer understanding of the proposed approach’s relative effectiveness. Specifically, the lack of comparison with defenses that use adversarial training or input transformation techniques leaves a gap in demonstrating the robustness of the proposed method against a wider range of defense strategies. The absence of these comparisons makes it difficult to assess whether the hypergraph approach offers a significant advantage over more established defense techniques.
2. There is ambiguity regarding the application of GCG and AutoDAN (both white-box attacks) on GPT-4, which is a black-box model. It is unclear how the authors applied a white-box attack to a black-box model. Clarifying or adapting the experimental setup here would strengthen the credibility of the results. The description of how gradient information is accessed for GCG and how the internal structures of GPT-4 are used for AutoDAN needs to be made explicit. Without this clarity, the validity of the experimental results is questionable.
3. The proposed method is complex, involving modified Gromov-Hausdorff distances and hypergraph structures, which likely increases time complexity. While the time complexity of each component is theoretically analyzed and inference efficiency is addressed in Appendix B, a discussion of the computational costs associated with training would be beneficial. The paper should provide a breakdown of the training time for each component of the method, such as hypergraph construction, distance calculations, and classifier training. This would allow for a better understanding of the practical feasibility of the approach.

### Questions
Please refer to weaknesses.

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
5

### Summary
This paper proposes a novel defense against jailbreak attacks. The defense is based on hypergraphs and a Gromov-Hausdorff metric to build a classifier and distinguish harmful prompts.

### Strengths
The perspective of this work is novel and interesting. A detailed and solid theoretical analysis is provided. Experiments on different kinds of attacks are conducted to illustrate the effectiveness of the proposed method.

### Weaknesses
1. The motivation of the proposed method is very unclear. There is a gap between jailbroken prompts and the hypergraph-based method. The authors only provide a simple intuition of adopting hypergraph to distinguish jailbroken prompts, but there is no clear evidence why hypergraph is useful, including either empirical or theoretical analysis or existing literatures.

2. Sections 3 and 4 are used to introduce notations, how to construct hypergraphs, and how to build a classifier using metrics between hypergraphs. However, there is no explanation of how these constructions are related to defending against jailbreak attacks. The authors simply state their notations, construction, and theorem on generalization error bounds on the SVM built on the metric, but there is no practical implication of these contents such as how the hypergraph and distance constructed in this way can show the difference between benign prompts and jailbroken prompts, etc. This theoretical analysis should clearly state how the defending effectiveness is guaranteed. 

3. The details of conducting baselines is unclear. For example, how to apply white-box attacks like GCG and AutoDAN to API-only model GPT-4 is unclear. Besides, the number of tested models is not sufficient.

4. Time complexity analysis is missing.

### Questions
See weakness

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
2

### Summary
The paper introduces a novel defense mechanism against social engineering attacks on large language models (LLMs). It models prompts as hypergraphs, capturing token interactions, and uses a Gromov-Hausdorff metric space to classify prompts as benign or malicious. Key contributions of this paper include hypergraph-based prompt modeling to detect complex manipulative patterns and theoretical guarantees for detecting new attacks. The proposed method outperforms existing defenses against socially engineered attacks. This approach provides a mathematically robust and effective method for improving LLM security.

### Strengths
1.	The paper proposes a method for defending against social engineering attacks using hypergraph structures and Gromov-Hausdorff metric spaces, which represents a novel defensive approach. 
2.	The method is not only applicable to social engineering attacks but also performs well against other types of attacks.

### Weaknesses
1.	Regarding defense methods, the authors should also compare GradSafe, which has been shown in the related work leveraging gradient information to detect jailbreak prompts.
2.	The authors do a great job in demonstrating the effectiveness of the proposed defense. However, as mentioned in the related work, previous methods are memory-intensive and infeasible for practical use. I would expect the authors also conduct a cost analysis on different defenses as well.
3.	More jailbreak datasets should be considered.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies defenses against prompt-based socially engineered attacks on LLMs.  Particularly, the paper introduces a robust prompt filter based on hypergraph metric geometry—each LLM prompt is represented as a metric hypergraph, forming a compact metric space, and the higher-order metric space over these compact metric hypergraphs can be leveraged to model the differences in information flow between benign and malicious LLM prompts.  The paper also derives upper bounds on the generalization error of the proposed prompt filter.  Finally the effectiveness of the proposed filter is demonstrated through experiments on two datasets.

### Strengths
+ the paper is well-written and well-organized

+ the proposed robust prompt filter is novel, well-motivated,  and justified

+ theoretical analysis on the error bound of the robust prompt filter

### Weaknesses
 - more clarifications on the algorithms and experimental results are needed  

- more baselines are needed for comparison

- The paper tests that GNN and HGNN baselines do not perform well to distinguish malicious prompts. More explanations and insights are needed as to why (H)GNNs do not perform well, especially if the clique-expansion graph of a given hypergraph is well constructed. The paper should elaborate on the specific limitations of (H)GNNs in this context, considering their capacity to model complex relationships. 

- The proposed kernel SVM is used to deal with varying size variable dimensional metric hypergraphs. It is unclear how the kernel SVM handles the variable dimensionality of the hypergraphs. It would be beneficial to explore alternative approaches, such as mapping the metric hypergraphs into a latent space before training a classifier, or training a kernel SVM directly on prompt embeddings, like an average of token embeddings. The paper should justify why the proposed approach is superior to these alternatives. 

- There exists many (spatial-temporal) GNN works that can capture temporal, spatial, and higher-order information of the graph. It is unclear why these were not considered as baselines, given their potential to capture the sequential nature of prompts and the complex relationships between tokens. 

- It would be better to add some details of the baseline Mutation-based  and Detection-based defenses. This makes readers better understand the advantage of the proposed robust prompt filter.  

- Any explanation why the proposed robust filter is also robust to algorithmic attack types? Can you also show example failure cases for Hypergraph? 

- How to set w and s in the sliding-window for forward edge construction and r in the ball for forward edge construction in practice? What's the impact of these factors? Is there any (positive/negative) correlation between the classification accuracy and the prompt length?

### Questions
Is Section 3.2 from previous work or proposed by the authors? I would like to know which part is novel and which is inspired by existing work. 

The paper tests that GNN and HGNN baselines do not perform well to distinguish malicious prompts. Can you provide more explanations and insights why (H)GNNs do not perform well, if the clique-expansion graph of a given hypergraph is well constructed. 
On the other hand, I am thinking about two other baselines: 

- 1. How about first performing clustering on the hyperpgraphs and then apply (H)GNN? 

- 2. The proposed kernel SVM is used to deal with varying size variable dimensional metric hypergraphs? What if we first map the metric hypergraphs into a latent space and then train a (SVM) classifier, or simply training a kernel SVM using the (malicious and benign) prompt embedding, which can be, e.g., an average of the tokens’ embeddings?  

- 3. There exists many (spatial-temporal) GNN works that can capture temporal, spatial, and higher-order information of the graph. Able to also compare with them?

It would be better to add some details of the baseline Mutation-based  and Detection-based defenses. This makes readers better understand the advantage of the proposed robust prompt filter.  

Any explanation why the proposed robust filter is also robust to algorithmic attack types? Can you also show example failure cases for Hypergraph? 

How to set w and s in the sliding-window for forward edge construction and r in the ball for forward edge construction in practice? Whats the impact of these factors? Is there any (positive/negative) correlation between the classification accuracy and the prompt length?

### Soundness
3

### Presentation
3

### Contribution
3
