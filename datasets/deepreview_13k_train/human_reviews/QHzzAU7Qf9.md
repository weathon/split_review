# Soft Merging of Experts with Adaptive Routing

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Neural networks that learn to route their inputs through different ``expert'' subnetworks provide a form of modularity that standard dense models lack.
Despite their possible benefits, modular models with learned routing often underperform their parameter-matched dense counterparts as well as models that use non-learned heuristic routing strategies.
In this paper, we hypothesize that these shortcomings stem from the gradient estimation techniques used to train modular models that use non-differentiable discrete routing decisions.
To address this issue, we introduce \textbf{S}oft \textbf{M}erging of \textbf{E}xperts with \textbf{A}daptive \textbf{R}outing (SMEAR), which avoids discrete routing by using a single ``merged'' expert constructed via a weighted average of all of the experts' parameters.
By routing activations through a single merged expert, SMEAR does not incur a significant increase in computational costs and enables standard gradient-based training.
We empirically validate that models using SMEAR outperform models that route based on metadata or learn routing through gradient estimation.
Furthermore, we provide qualitative analysis demonstrating that the experts learned via SMEAR exhibit a significant amount of specialization.
All of the code used in our experiments is publicly available

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a novel method for routing experts in Mixture of Experts (MoE) models. Compared to methods that seek discrete routing policies and require gradient estimators (REINFORCE, Gumbel-Softmax), the authors propose an adaptive technique which is fully differentiable. Motivated by work on _merging models_,  SMEAR is presented, which computes a weighted average of expert parameters within each MoE block; thus enabling a fully differentiable routing policy. Authors validate on GLUE and DomainNet. They show that the method outperforms other discrete MoE models at equivalent inference rates.

### Strengths
1. This is very well written paper, clear it its aims, hypotheses, presented method and results. The manuscript offers an extensive analysis of the literature and corresponding baseline methods (gradient estimators, routing policies (top-k, d-select k etc.), heuristic routing, modular models) in addition to related work.

2. Merging expert parameters in MoE networks is under-explored and a straightforward *yet* elegant solution for adaptive routing of experts. The results are convincing although the improvement in accuracy does seem marginal at best (1% over REINFORCE Fig 2a, 2-3% TopK etc.)

3. The paper is a nice and interesting addition to the modular/MoE literature and presents interesting new research direction as pointed by the authors and beyond.

### Weaknesses
1. One weakness of the manuscript is the lack of a detail explanation on the central hypothesis of the work. The authors claim:

_"As we will later show in section 4, the gradient estimation techniques used to train models with discrete routing often fail to produce performant routing strategies."_

This is shown throughout quantitative results but as a reader, I was expecting a substantial theoretical explanation as to why discrete routing methods may fail related to how gradients may be routed, instabilities etc. Additionally, Figure 3 offers qualitative explanation of the learned policy through SMEAR. How does this relate to Top-K, DSelect-K etc. Are the policies that much different?

2. Many MoE methods often seen instabilities in training - mode collapse i.e. an expert being chosen much more, non-optimal solutions etc. The presented method is a weighted average of parameters. How does such a method regularise against particularly known failure modes of MoEs which often require explicit regularisation such as through load, importance, entropy, or Mutual Information?

### Questions
1. How would you go about encouraging exploration across experts in SMEAR to help determine which expert weighting is most beneficial per token/image etc.? In a discrete scenario, one might look at dropout and/or jitter noise on incoming representations? Did the authors try something similar to investigate performance?

2. The computational cost of the averaging works _"as long as there is a modest number of expert"_. In papers such as Switch Transformer, they use 128 experts compared to the 16 used in Scaling experiments. Would this method work in this context?

3. Can you foresee any pitfalls from where weight averaging might not be beneficial? What are the main limitations of the method?

4. How much specialisation do you learn as get one gets deeper into the network? Can you control this and would it get better results if you learned? There is a lot of learned sparsity in Figure3a but is this necessarily good? It could be a limitation that not enough exploration occurs through the proposed learning scheme.

[extra]
Formatting - not a question. but a comment on legibility. Section 4.1. needs to be broken up into paragraphs.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on shortcomings of models with discrete routing among experts that can lead them to underperform heuristic non-learned routing. The authors hypothesize that issues with conditional computation stem from issues with gradient estimation, which is a technique utilized to provide approximate gradients for models involving discrete adaptive routing. The authors introduce SMERA for training modular models by computing a weighted average of the parameters of the individual experts.

### Strengths
1. Underperformance of models that use conditional computation is an important topic.
2. This paper provides some empirical analyses to verify the effectiveness of the proposed method.

### Weaknesses
1. The implementation details of the proposed method, SMERA, are not sufficiently clear. For example, the paper does not specify the routing function  $R(\cdot)$. Is it a learned function, and if so, what is its architecture? Is it a simple heuristic? Providing more details on the routing mechanism is crucial for understanding the core of the proposed method. Furthermore, the paper lacks a clear definition of the objective function used during the training process. Is it a standard cross-entropy loss, or are there any modifications or additional terms specific to the SMERA framework? Clarifying the objective function would help readers understand how the model is optimized and how the different components interact during training.

2. This paper lacks sufficient novelty, particularly in relation to the $\pi$-Tuning method described in [1]. While both methods aim to improve the performance of modular models, the paper does not adequately distinguish SMERA from $\pi$-Tuning. For instance, both methods appear to involve a form of interpolation or weighted averaging of expert parameters. The paper should elaborate on the specific differences in how SMERA and $\pi$-Tuning achieve this interpolation. Is there a difference in the way the weights are learned or applied? Are there differences in the underlying assumptions about the relationship between experts and tasks? Highlighting these distinctions is essential to establish the unique contribution of SMERA.

### Questions
1. What routing function $R(\cdot)$ do you use? 
2. What is the specific form of the objective function in the training process?
3. Can you explain what are the differences and advantages of the proposed method, compared to the $\pi$-Tuning method proposed in [1] (Section 2.2 and Section 3.5)?
   
[1] Wu, Chengyue, et al. "$\pi$-Tuning: Transferring Multimodal Foundation Models with Optimal Multi-task Interpolation." International Conference on Machine Learning. 2023.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a simple method to avoid discrete routings in mixture-of-expert models by merging weights of experts during training and inference. Experiments over GLUE and DomainNet with T5-base and ResNet models demonstrate that the proposed approach is computationally efficient and achieves better performance than other MoE methods.

### Strengths
- The proposed method is simple, efficient, and achieves better performance than learned routing in presented experiments
- The choice of baselines are extensive, ranging from ensemble methods, learned routings, and pre-defined routings.
- I appreciate analysis of learned routing by the proposed method.

### Weaknesses
 - The main weakness is the small scale of the data and models studied in the paper. I believe the challenge of reducing computational cost with mixture-of-expert models is more relevant to larger models. The authors however only presented results on ResNet and T5-base (with only 200M parameters). Experiment results with larger models are appreciated.

- If experiments with larger models are not feasible, I hope authors can discuss potential limitations of the study under those larger-scale scenarios. Do you expect the findings in Figure 2 change in larger scale setups?

- The author's hypothesis about the shortcomings of learned routings in existing works that "stem from the gradient estimation techniques used to train modular models that use non-differentiable discrete routing decisions" is not supported with evidence other than the performance of final models in Figure 2. If you visualize the learned routing of these baselines (as in Figure 3), will you notice flaws in these learned routing? Do they yield degenerated routing, or routing that is uniform across all the experts?

### Questions
Following listed items in weakness, I hope authors can address:
- What do you expect the performance looks like in larger-scale models?
- How does the routing learned by reported baselines look like?

Finally, the appendix and full text does not have to be in separate pdfs.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
