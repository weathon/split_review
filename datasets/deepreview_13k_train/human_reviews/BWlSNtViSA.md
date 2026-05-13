# Coupling Fairness and Pruning in a Single Run: a Bi-level Optimization Perspective

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Deep neural networks have demonstrated remarkable performance in various tasks.
With a growing need for sparse deep learning, model compression techniques, especially pruning, have gained significant attention.
However, conventional pruning techniques can inadvertently exacerbate algorithmic bias, resulting in unequal predictions.
To address this, we define a fair pruning task where a sparse model is derived subject to fairness requirements.
In particular, we propose a framework to jointly optimize the pruning mask and weight update processes with fairness constraints.
This framework is engineered to compress models that maintain performance while ensuring fairness in a single execution.
To this end, we formulate the fair pruning problem as a novel constrained bi-level optimization task and derive efficient and effective solving strategies.
We design experiments spanning various datasets and settings to validate our proposed method.
Our empirical analysis contrasts our framework with several mainstream pruning strategies, emphasizing our method's superiority in maintaining model fairness, performance, and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this paper investigate the algorithmic bias issue in neural network pruning. A joint optimization framework is proposed. It is called Bi-level Fair Pruning (BiFP) based on bi-level optimization to ensure fairness in both the weights and the mask. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper studies a novel and interesting problem. Addressing demographic disparity challenges has received much attention in the recent works on deep learning. However, most works on pruning do not address this issue.
2. The proposed method is reasonable. 
3. This paper is organized well.

### Weaknesses
1. The experiment suffers from samll scale. Only small models (ResNet10 and Mobilenetv2) are used as an uncompressed model. The used datasets (CelebA and LFW) are also small. The lack of experiments on larger models such as ResNet50 or transformer-based models, and larger datasets like ImageNet, limits the generalizability of the findings. It is unclear if the proposed method would scale effectively to more complex architectures and datasets.

2. Althogh the propsed method is reasonable, it seems trivial. Eq 5 defines the joint optimization framework. It simply combines two constrains. This paper is short of novel techniques. The formulation in Equation 5, while combining fairness and pruning objectives, appears to be a straightforward linear combination of existing loss functions. The paper lacks a deeper exploration of the theoretical properties of this combined objective, such as convergence guarantees or the impact of different weighting strategies between the two objectives.

### Questions
None

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the problem of exacerbating biases in neural networks upon pruning. In particular, the authors propose a bi-level optimization based unstructured pruning algorithm to mitigate the biases. The core idea is to optimize for the pruning mask and weights in an alterating fashion to jointly minimize the classification loss and fairness metric. 

The approach proposed demonstrates better accuracy-fairness tradeoff with respect to pruning methods that do not optimize for fairness at different sparsity levels.

### Strengths
S1. The problem is important and has been gaining some traction in the recent years.

S2. Overall the paper is well written - especially the preliminaries.

### Weaknesses
W1. The idea of using bi-level optimization is not new to pruning. [a] uses it in a very similar fashion to that in the paper. While [a] is cited in the manuscript, it is not explicitly called out that they also use a very similar bi-level optimization framework - which looks misleading. The core issue is that the paper does not sufficiently differentiate its approach from [a] in terms of the optimization framework itself. The authors need to clearly articulate the novel aspects of their bi-level formulation beyond simply incorporating a fairness metric, as the high-level optimization structure is very similar.

W2. Definition 2 (Compressed Model Performance Degradation) and Definition 3 (Performance Degradation Fariness) seems unnecessary, since the authors essentially use only the fairness perfromance metric (definition 1) in practice when pruning the model. The paper would benefit from a more focused presentation that directly relates the definitions to the experimental setup. The current definitions appear disconnected from the actual evaluation process.

W3. Experiments are limited across dimensions such as datasets, models. More datasets (including larger ones) should be included such as in [b]. Larger models such as ResNets should also be included in the study. The empirical evaluation needs to be more comprehensive to demonstrate the robustness and generalizability of the proposed method. The current experiments are insufficient to validate the method's effectiveness across diverse scenarios.

W4. Stronger baselines need to be used. At the moment, none of the baselines used optimize for fairness. However, there are other works such as [b] that optimize for fairness and should be used as a baseline to show the benefit of bi-level optimization over existing pruning approaches. The lack of comparison against fairness-aware pruning methods makes it difficult to assess the true contribution of the proposed approach. The paper needs to demonstrate that the bi-level optimization provides a tangible benefit over existing fairness-aware pruning techniques.

Overall, I feel that the paper is still incomplete and is not yet ready for publishing. Moreover, I observe limited novelty in this work due to lack of difference from [a]'s pruning objective (Equation 1). Instead of the regulariser, the authors have replaced it with equation 8 of the manuscript which is directly bought in from [c].

### Questions
1. As stated above equation 8, $u(.)$ is a surrogate function for the indicator function. What is your choice of $u(.)$?
2. As stated in section 4.3.2 $m$ is taken to be continuous. It is not clear how the mask is selected when pruning the network. Do you select the sparsity level at the start of the pruning procedure and try to identify appropriate indices in the mask that should be made 0. Or do you gradually increase the sparsity level. Also, what if the mask value becomes, say -2.5. What would you do in that case?


Minor comments:

- In Definition 3 and beyond, $\mathbb{F(f_c, \mathcal{D}; \mathbb{R})}$ should be  $\mathbb{F(f, f_c, \mathcal{D}; \mathbb{R})}$
- In equation 5, what are you minimizing with respect to in the upper optimization problem?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission presents Bi-level Fair Pruning (BiFP), a new approach to neural network pruning that ensures fairness (with another convex relaxation to efficient training). BiFP optimizes the pruning mask and network weights simultaneously under fairness constraints.  The experimental results on two benchmark datasets show some interesting performances.

### Strengths
- The submission is in good shape, and the writing clearly conveys the novelty and contribution. 

- The problem setting (i.e., neural network pruning with fairness constraints) is novel to the best of my knowledge. 

- The proposed bi-level pruning is sound and reasonable, and experimental results show some interesting findings.

### Weaknesses
 - My main concern is the random initiation of the mask. It is not clear what kind of randomization is used in the experiment, and whether different randomization strategies will lead to different performances. Specifically, the paper lacks details on the distribution from which the random values are sampled (e.g., uniform, normal, or a more specialized distribution), and how this distribution's parameters are set. The impact of different initialization scales or variances on the final performance and fairness metrics is also not explored. This makes it difficult to assess the robustness of the proposed method.

- The paper presents a bi-level pruning method (i.e., optimizing one variable while fixing another one). How do you guarantee the convergence theoretically. Again, since the mask is randomly initialized, will different randomization lead to different convergences? Noted that different randomization could also impact the objective function (leading to different landscapes), thus, both theoretical and experimental studies regarding the issue of convergence should be conducted. The paper does not provide any theoretical analysis of the convergence properties of the proposed bi-level optimization. It is unclear whether the alternating optimization scheme is guaranteed to converge to a stationary point, and if so, under what conditions. The lack of theoretical guarantees raises concerns about the reliability of the method, especially when different random initializations might lead to different convergence behaviors and potentially suboptimal solutions. Furthermore, the paper does not discuss the potential for oscillations or divergence during the alternating optimization process.

- Based on the results in Fig. 3 and 4, the improvement seems to be very marginal. It is not clear to me whether the improvement is significant. The reported improvements in accuracy and fairness metrics appear to be quite small, particularly when considering the complexity of the proposed method. The paper does not provide a rigorous statistical analysis to demonstrate that these improvements are statistically significant, and it is unclear whether the observed differences are due to the proposed method or simply random variations. The lack of statistical significance testing makes it difficult to assess the practical value of the proposed approach.

- The adopted datasets and models for evaluation seem to be toy to me, perhaps more realistic dataset (e.g., healthcare) and more advanced model should be evaluated. The datasets used in the experiments (LFW and CelebA) are relatively small and may not be representative of real-world scenarios. The models used are also relatively simple, and it is unclear whether the proposed method would scale to more complex architectures. The lack of evaluation on more challenging datasets and models limits the generalizability of the findings.

- The motivation of using conves relaxation in 4.3 is not clear to me. Based on the submission, it seems the advantage of using convex relaxation is to let the fairness constraint convex and differentiable, but noted that our deep neural network is non-convex in nature (e.g., ReLU, maxpooling, etc.), the argument above is not convincing to me. While convex relaxation can simplify optimization, the paper does not adequately justify why this approach is necessary or beneficial in the context of a non-convex neural network. The paper should discuss the limitations of using convex relaxation and explore alternative approaches that might be more suitable for non-convex optimization.

### Questions
Please see above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
