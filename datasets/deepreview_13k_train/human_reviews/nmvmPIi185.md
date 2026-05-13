# Neural Causal Graph for Interpretable and Intervenable Classification

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Advancements in neural networks have significantly enhanced the performance of classification models, achieving remarkable accuracy across diverse datasets. However, these models often lack transparency and do not support interactive reasoning with human users, which are essential attributes for applications that require trust and user engagement. To overcome these limitations, we introduce an innovative framework, Neural Causal Graph (NCG), that integrates causal inference with neural networks to enable interpretable and intervenable reasoning. We then propose an intervention training method to model the intervention probability of the prediction, which can serve as a contextual prompt to facilitate the fine-grained reasoning and human-AI interaction ability of NCG. Our experiments reveal that the proposed framework significantly enhances the performance of classical classification baselines. Furthermore, NCG achieves nearly 95% top-1 accuracy on the ImageNet dataset by employing a test-time intervention method. This capability not only supports sophisticated post-hoc interpretation but also enables dynamic human-AI interactions, significantly improving the model's transparency and applicability in real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper combines the causal inference frameworks of structural causal models and potential outcomes models, using neural network implementations, to provide better transparency and interactive reasoning capabilities in classification settings. Estimation of causal effects (ATEs) to build the underlying graph is is done using propensity score matching and doubly robust learning. Compared to naive utilization of neural networks for classification, this approach gives a more inherently interpretable model for classification by explicitly modeling underlying causal relationships. The authors demonstrate their method on the ImageNet and Bird datasets and show improved performance as well as improved interpretability and human intervene-ability (via test-time intervention experiment) over certain neural network baseline models. They argue it is the explicit modeling and tweaking of underlying causal structure that gives accuracy improvements, with some ablations as evidence.

### Strengths
Very clear intro and stated contributions. Work is original and well-motivated. Results feel complete and experiments are convincing (e.g. with ablations showing the importance of both Intervention Training and Learnable Scaled Weight). As a reader, most of my immediate/obvious questions are answered in the paper and/or the Appendix.

Strong conceptual figures; I am familiar with traditional causal inference frameworks and appreciated the concise and relevant presentation here. Tables and graphs are appropriately used; the one on ablations is especially clear. The Appendix provides clear pseudocode and more concrete examples and visualizations of the authors’ method and experiments – relevant info to better understand the model and application concretely.

Represents a solid and clear contribution and advance for a conference paper work. Above acceptance threshold.

### Weaknesses
I have no major issues with this paper.

Small typo: 310/311 intervention is spelled wrong.

More of a leading question: is the prior work complete? It's a relatively small section of the Intro, and I wonder if there are previous attempts to integrate causal inference frameworks in NNs (maybe not in interpretability specifically) that are important to acknowledge and relevant to cite. I.e. previous work on modeling causality with GNNs? Your paper does not obviously acknowledge that causal reasoning on graphs implemented as NNs is an established concept. You say "Unlike conventional methods that rely on correlation-based learning, NCG constructs a causal graph..." but GNNs attempting to model causality aren't mentioned.

### Questions
Is there anything systematic that you can comment on or hypothesize about in Section 4.2 about DRL doing better on Bird vs. PSM doing better on ImageNet performance in Table 2?

You are space constrained, but since the intervention training method is an important contribution, I wonder if it could get a little more space in the main text.

Regarding your explanation of the accuracy drop for DRL+CLIP w/o intervention training: are you saying that the method reaches a point (high number of nodes) after which it can’t learn the underlying structure (w/o intervention training) and therefore reason appropriately (“get the right answer”)? Are there metrics other than accuracy that could demonstrate the difference in underlying reasoning (even just at the point on the graph, ~1300 nodes for CLIP+DRL, between the two graphs) and make your claim stronger?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new interpretable and intervenable neural network. The main idea of the proposed models is to incorporate a causal graph among latent concepts and target labels into a neural network. To train such a model, the authors propose calculating the causal effects between concepts and labels by propensity score matching and doubly robust learning. Its prediction of each concept or label is modeled by the linear combination of the estimated causal effects of the parent concepts in a causal graph, as well as the output of the encoder in a pre-training network. The authors also propose an intervention training technique that generates counterfactual samples by intervening in selected training samples according to the causal graph. Experimental results demonstrated that the proposed method attained higher accuracy than the existing baselines, including the concept bottleneck model.

### Strengths
- S1. The authors proposed a new concept bottleneck model by incorporating a causal graph that represents causal relationships between latent concepts and target labels. I think it is interesting and useful to generate concepts corresponding to the labels and their causal directions using WordNet. 
- S2. The proposed method slightly improved the accuracy and F1 score on the Bird and ImageNet datasets compared to the baselines.

### Weaknesses
 - W1. It was difficult for me to understand the whole picture of the proposed method. Maybe this is because this paper is structured to describe the proposed method in a bottom-up manner. I believe describing the proposed method in a top-down manner, that is, first giving an abstracted model of the proposed model and then describing its formulation of each detail, may help readers understand the proposed method. In addition, while the authors introduce several unique techniques (e.g., causal effect calculation, concept reasoning, and intervention training), it was unclear to me what purpose these techniques are introduced for and what observation or motivation they are based on. If my understanding is correct, the proposed method can be regarded as an extension of the concept bottleneck models incorporating causal relationships between labels and concepts. I think this paper may be improved by organizing it following the original paper on the concept bottleneck models [Koh et al. 2020]. 
- W2. This paper claims that the proposed method is interpretable. However, I could not find any discussion or evidence demonstrating the interpretability of the proposed method. 
- W3. I found some confusing notational errors. For example, while $n$ represents the total number of labels in Line 153, it denotes the total number of nodes in a causal graph in Line 268. Also, in Equation (5), $n$ appears to represent the total number of training samples. Furthermore, while $C$ is defined as a binary variable in Line 203, it denotes the set of concept variables in Line 275. In addition, I think $w_{ij}$ in Equation (6) is correctly $A_{ij}$. Since such notational errors prevent readers from understanding the proposed method, I believe the mathematical part of this paper should be corrected entirely.

### Questions
- Q1. Concerning W1, is my understanding of the proposed method correct?
- Q2. Concerning W2, from what perspective do the authors claim that the proposed model is interpretable?
- Q3. What was the purpose of the experiments in Section 4.5? If the test samples were intervened and their concepts and labels were perturbed according to a causal graph, it seems natural that the accuracy of the proposed method increased and that of CBM decreased since the former was trained with the causal graph and the latter did not. Can this experiment be considered fair?

### Soundness
2

### Presentation
1

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
The paper proposes a classification framework that integrates causal inference within neural networks to enhance interpretability and facilitate human-guided interventions. Experiments are conducted to see how performance compares against baselines such as concept-bottleneck models, then the effect of causal weights, ablation studies, and test time intervention capability.

Overall, the results seem to show that the performance is promising and test time intervention feasible.

### Strengths
* Integrating causal reasoning into deep neural networks is a nice feature of the paper, and not something (to the best of my knowledge) which as been explored before convincingly.
* The method appears quite general, using WordNet should generalize to most domains.
* Test time intervention should be useful in a HCI context, in more complex decision making which is higher stakes.

### Weaknesses
 * First and foremost I found the paper pretty difficult to grasp exactly what had been done, a lot of it is heavily formalized without any intuitive explanations to facility easy reading, this is really going to limit who can read and build upon the work. Those who work in causal reasoning are mostly used to SCMs and it is pretty hard to understand the core differences this presents to that framework, I would really suggest re-writing the paper drastically. For example, Figure 1 is not even reference until page 4, but it's on page 2, this all makes the paper hard to follow.
* The reliance on WordNet, while smart, limits the method a lot because not all concepts/relations will be in this dataset. The method's reliance on a pre-existing structured knowledge base like WordNet means that it is inherently limited to domains where such resources are available. This is a significant constraint, as many real-world problems lack the comprehensive concept coverage that WordNet provides. Furthermore, the method does not address how to handle concepts or relations that are not present in WordNet, which is a common issue when dealing with specialized or emerging domains. The authors need to acknowledge that this reliance on WordNet is a significant limitation that restricts the general applicability of their approach.
* The test time intervention relies on using labels, but what if the human involved doesn't know the labels? The accuracy won't be as good as you are reporting. The test-time intervention assumes that the human expert has knowledge of the prior concept labels, which is a strong assumption. In many real-world scenarios, the human expert may not know the correct labels or may have uncertainty about them. This limitation is not addressed in the paper, and it is unclear how the method would perform under such conditions. The authors need to discuss the robustness of their method to noisy or uncertain interventions and provide a clear explanation of how their method can be used in situations where the human expert does not have perfect knowledge of the labels.

### Questions
* Why did the regular classifiers in Table 2 perform worse than your method? This doesn't make sense to me as you are incorporating more constraints, did the causal reasoning actually result in better results?
* Did you add multi-lables for each datapoint by using WordNet? If so, then all images of e.g. Bird1 have all the same concept labels in every example you train on? Isn't that just making the classification problem more convoluted? Surely each image of Bird1 should have varying concept labels to truly benefit the training process and your method? Otherwise it's just the same classification problem, just with more more labels.
* Can you make explicit how you think test time intervention could be used in application?
* Can you run your method NCG without the causal structure to understand how much benefit is attributed to the causal graph itself?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce Neural Causal Graph, a framework that builds a DAG over concepts from a neural network to improve performance. The DAG yields small but significant classification accuracy improvements on ImageNet and the CUB Birds dataset. The method and results seem compelling, but the writing of the paper is unclear.

### Strengths
- The paper studies an interesting problem of inducing a causal graph over a classification task
- The paper's results show significant improvements in classification accuracy on 2 datasets
- The introduced methodology seems to be generally useful, especially for sharing information between many classes

### Weaknesses
 - The paper's writing is unclear, especially in the methods section.
- The paper overclaims about interpretability, e.g. "This capability not only supports sophisticated post-hoc interpretation but also enables dynamic human-AI interactions" -- it is unclear that the method yields interpretable concepts or arranges them in a manner that allows humans to understand them. More experiments (ideally with real human users) would help to show this
  - On a related note, the "intervention training method" (Secs 3.2.5 and 4.5) are especially unclear. Why would one expect to be able to intervene on a concept in a CBM baseline and maintain accuracy?

### Questions
- I assume the "Bird Dataset" is [CUB-200](https://www.vision.caltech.edu/datasets/cub_200_2011/)? The authors should make this clear in the paper
- Can the authors explain their test-time intervention training and results more clearly?

### Soundness
3

### Presentation
2

### Contribution
3
