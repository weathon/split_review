# Exploring the Causal Mechanisms: Towards Robust and Explainable Algorithm Selection

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Abstract.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work introduces causality to explore underlying mechanisms in algorithm selection problem. Based on Pearl’s causal framework, it proposes a structural equation model (SEM) based on a causal DAG among problem features and algorithm features. Neural network-based method is proposed to fit the model, through minimizing a mixture of reconstruction, sparsity, acyclicity and 	selection loss. As both demonstrated in texts and experiments, this method is featured by its robustness under distribution shift and explainability towards understanding the mechanism between problem and algorithm features, and it outperforms other methods in most instances especially when constructing dense causal graphs.

### Strengths
* This paper proposes a novel way to treat the algorithm selection problem from causal perspective, and awares us of the bias caused by distribution shift in algorithm selection. It also builds an adequate causal framework to treat the problem under Pearl’s causal framework.

* Experiment results endorse the superior performance of this method in terms of accuracy, robustness, etc. comparing with previous methods in algorithm selection.

### Weaknesses
Some parts of the paper are hard to catch up. e.g.

* **Causal Learning Structure** In section 2.2, the paper considers incorporating graph information of DAG through designing the first layer of NN as an adjacency matrix. It is argued that it leads to a consistent model. However, there seems to be no theory or references to prove the consistency.

* **Loss function** The loss function is designed to be a weighted sum of four different losses. As these four losses measure completely different aspects, it is suggested to discuss on the weight so as to make them comparable. Besides, if the graph is pre-specified, then what is the use of sparsity and acyclic losses? If it is to be discovered, there should be an illustration on how to construct the DAG to ensure there is only directed flow from problem features to algorithm features.

* **Do-calculus** The notation of do-calculus in section 3.2 needs to be clarified. e.g. in $do(\textbf{PF}=\textbf{PF}+\delta_{\textbf{PF}})$, it should be clarified which PF stands for variable and which stands for specific values.

Overall, the paper is well-motivated by incorporating causal frameworks and methods (Do-calculus, SEM, Causal learning) to deal with algorithm selection. However, it seems more efforts ought to be spent on fulfilling details of this method and explaining its rationality.

### Questions
The questions are sufficiently described in the weaknesses section.

### Soundness
2

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
4

### Summary
This paper investigate the problem of selecting optimal algorithm for particular problem instance. Originally, the algorithm feature is predicted based on the problem feature. The correlation-based machine learning methods can be applied to solve this. However, this kind of methods are vulnerable to data bias and distribution shift. To address these issues and improve the transparency, this paper introduce causal structure learning to explore the underlying mechansim of algorithm selection. The experimental results show that the proposed CausalAS method achieve robustness to distribution shift, and provide explainability through causal graph and counterfactual explanation.

### Strengths
The proposed method achieve robustness to distribution shift, which is an important quality to the application of methods. Empirical results show the effectiveness of CausalAS in different scenarios of distribution shift. The improvement margin is significant. Based on the intermediate product (i.e. causal graph), the CausalAS method provides two kinds of explanations, which is critical to the transparency of the method. The above two properties together contribute the trustworthy application of the method.

### Weaknesses
1.I think the novelty of the proposed method is limited. The proposed method is similar to that in [1]. The design of loss function and the given assumptions are similar to the counterpart in [1]. And the problem formulation seems to be directly transformed from recommendation (i.e. problem corresponds to user, algorithm corresponds to item). And the authors did not give citation to this important reference. 


[1] Yue He, Zimu Wang, Peng Cui, Hao Zou, Yafeng Zhang, Qiang Cui, Yong Jiang. CausPref: Causal Preference Learning for Out-of-Distribution Recommendation.

### Questions
1. The authors claim to find the optimal algorithm. However, the candidate algorithms are only divided into selected (S=1) and not selected (S=0). I want to know whether there is only one selected algorithm. If not, which one is the optimal?

2. In the section of "Demonstration of Explainability", only the feature index is demonstrated in Figure 4. The semantic meaning of them is not known. It limits the explainability of the shown demonstration.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new method towards robust and explainable algorithmic selection by using of causality. However, both of the clarity and novelty is lack.

### Strengths
1. Robust and explainable algorithm selection is important and of interest.
2. Incorporating causality into this area is apealing.

### Weaknesses
1. Main issue 1. Clarity. The overall presentation is poor, as authors cannot highlight their contribution and distinguish their work from existing one. For example, counterfactual explanation is well-motivated, and their causal versions are also very popular in previous work. However, authors claim that "we measure the minimal intervention from the perspectives of explanation complexity and explanation strength,", which is wield, as the framework of minimial intervention for CE has already been established in NeurIPS 2021. 
 - (a) What is the physical meaning of AF and PF? Can you provide more detailed clarification? 
-  (b) What is the core task of this paper? 
-  (c) A more clear version of paper is required. Definition of algorithmic selection, the objective of the task, with surrounding definitions and running examples.

2. Lack of novelty. 
- (a) Why the causality is required? I am not convinced by your illustration. Is it introduced for just dealing with distributional shift? If so, please provide formal characterization on shift. If not, please justify this point in detail.
- (b) Searching DAG in continuous spaces is always a popular approach, and the counterfactual explanation is well-studied. Please justify your contribution. 

3. Minor issues.
 You cannot define conditional distribution as P(AF | PF), as PF it self serves as random vectors. Please use more strict and formal illustration in theoretical analysis.

### Questions
See Weakness.

### Soundness
2

### Presentation
1

### Contribution
1
