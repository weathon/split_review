# Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
For Mixture-of-Experts~(MoE) models, an unbalanced expert load will lead to routing collapse or increased computational overhead. 
Existing methods commonly employ an auxiliary loss to encourage load balance, but a large auxiliary loss will introduce non-negligible interference gradients into training and thus impair the model performance. 
In order to control load balance while not producing undesired gradients during training, we propose \textbf{\ours{}}, featured by an auxiliary-loss-free load balancing strategy. 
To be specific, before the top-K routing decision, \ours{} will first apply an expert-wise bias to the routing scores of each expert.
By dynamically updating the bias of each expert according to its recent load, \ours{} can consistently maintain a balanced distribution of expert load.
In addition, since \ours{} does not produce any interference gradients, it also elevates the upper bound of model performance gained from MoE training.
We validate the performance of \ours{} on MoE models with up to 3B parameters trained on up to 200B tokens.
Experimental results show that \ours{} achieves both better performance and better load balance compared with traditional auxiliary-loss-controlled load balancing strategies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose an alternative loss-free method for load balancing of experts during MoE training. Load imbalance is a critical issue in MoE training as it can lead to expert collapse or increased utilization of some experts over the others. The proposed method achieves load balancing by dynamically applying expert-wise biases on routing scores according to their recent load, avoiding interfering gradients. The added bias is designed to only affect the top-k selection without changing the routing weights for combining the selected experts.

The loss-free load balancing approach is applied to DeepSeekMoE models with sizes 1B and 3B. The authors report perplexity on the validation set vs Maximal Violation scores.

### Strengths
- The paper is well-written and the method is clearly explained
- Good visualizations
- Simple approach that should be very easy to test and cheaper to compute than the conventionally used load-balancing loss

### Weaknesses
 - I am concerned over the validity of the claims. The empirical evaluations are very limited constrained to two DeepSeekMoE models and perplexity differences among the models and the baselines are at the level of 0.05 difference. Is this difference in perplexity significant?

- The evaluation is limited to language modelling and perplexity values. It would be better to see the actual effect of the loss-free load balancing on other downstream tasks such as MMLU or GLUE.

- The proposed Max Violation (MaxVio) score subtracts the mean load from the maximum load an expert receives, which highlights the worst-case scenario of load imbalance. Since MaxVio focuses on the maximum load, it can be highly sensitive to outliers. A single batch with unusually high token routing to one expert can disproportionately affect the MaxVio calculation, making it appear as though there is a significant imbalance even if most batches are well-balanced.

- To make the comparison fair, it would be useful to also see the load balancing (loss) values (without back propagating) and see how the loss-free variant behaves on that score as the training continues (e.g., a plot of load balancing loss over training steps for both methods).

### Questions
The load-balancing loss brings the advantage of load balancing to the inference stage by directly affecting the routing weights? How does the proposed method behave during inference.

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
The paper introduces Loss-Free Balancing, a new load balancing strategy for MoEs that avoids auxiliary loss, which traditionally introduces interference gradients and hampers model performance. The motivation stems from the need to balance expert loads in MoE models to prevent routing collapse and computational overhead, issues that current auxiliary-loss methods attempt to address but with performance trade-offs. The major research question is whether a balancing strategy can maintain expert load distribution without harming model performance. The proposed method adjusts each expert's routing score using a dynamically updated bias based on recent loads, promoting balanced expert utilization without adding interference gradients. Experiments on 1B and 3B parameter MoE models trained on abundant datasets show that Loss-Free Balancing achieves better load balance and improved validation perplexity compared to traditional methods, making it a promising approach for scaling large language models while preserving efficiency and performance.

### Strengths
This paper has the following strengths:

1. The proposed Loss-Free Balancing method eliminates the need for auxiliary loss, which traditionally adds undesirable interference gradients. This results in a cleaner training signal focused solely on the primary language modeling objective, potentially enhancing overall model performance.

2. By dynamically adjusting biases for each expert based on recent load data, the method ensures a balanced expert load without compromising model efficiency.

3. The strategy is compatible with expert parallelism, a key feature for training extremely large MoE models across multiple devices. This makes it highly suitable for scaling up model sizes while maintaining efficient load balancing.

4. Unlike the Expert Choice (EC) method, which risks future token leakage, Loss-Free Balancing maintains causal constraints in language modeling, thus preserving the integrity of model generalization.

### Weaknesses
This paper has the following weaknesses:

1. I am at first astonished by the short reference list of this paper, as the authors only cited 10 papers. Clearly, this paper did a very bad job on surveying the related work, including the various auxilliary-loss-based balancing methods, the major improvement of MoEs, the current MoE-based LLMs. Normally, I would list a few of the works for your reference, but the authors missed too many so I do not know where to start. I would strongly suggest the authors to check other MoE-LLM papers to improve the related work part.

2. The authors seemed to enlarge the figures in this paper in order to make the paper length reach 9 pages, which result in a disproportionate paper layout, and the figures look abrupt. 

3. The architecture design of the MoE-based LLMs are versatile. This paper only demonstrates its effectiveness on a small DeepSeek MoE model, while leaving other MoE models unvisited, such as Mistral, QWen, LLaMA-MoE, OpenMoE.

4. The improvement in performance seem trivial, which challenges the motivation of this study: why do we need a loss-free balancing at all.

### Questions
Please see my questions in Weakness column.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a Logg-free balancing strategy to solve the mixture of expert models' unbalanced expert load problem. The advantage of the approach is that it does not produce any interference gradients.
this paper proved that Loss-Free Balancing achieves better performance and better load balance compared with traditional auxiliary-loss-controlled load balancing strategies

### Strengths
This is an interesting research problem and the author aims to develop an efficient solution approach

### Weaknesses
1. The motivation and underlying intuition for the proposed approach could be clarified further to enhance understanding.
2. Additional experiments are recommended to demonstrate the robustness of this approach when applied across varying numbers of expert mixtures. A scalable analysis would also be beneficial.
3. The approach would be strengthened with theoretical justification to substantiate its effectiveness.

### Questions
1. On Page 4, in Formula 3, the selection and initialization process for b_i remains unclear. It would be helpful to clarify whether b_i  is influenced by K or independent of it. Additionally, in the adjustment process—where each bias b_i is iteratively modified based on the load of the corresponding expert—it is unclear by what amount b_i  should be increased or decreased and according to which theoretical basis this adjustment is made.
2. On Page 8, it is stated that 'the load balance of our Loss-Free Balancing consistently improves as the computation batch size increases.' Is there an upper bound to this improvement? 
3. Is there a specific reason for selecting 9 MoE layers for testing?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to replace the standard auxiliary load-balancing loss in mixture of experts (MoE) models with a new load balancing strategy that does not involve additional losses. This is to ensure tokens are being routed evenly to each expert without introducing gradients that do not directly contribute to achieving the language model objective. The authors also introduce a metric to quantify the degree of load balance in a MoE model.

### Strengths
1. There is some originality in viewing the problem of load balancing from the perspective of interfering gradients. 

2. The problem and solution proposed are simple and easy to understand.

### Weaknesses
1. It is unclear if or how the gradients due to the auxiliary load balancing loss results in the model not achieving its training objective. 

2. It is unconvincing that there is a future token leakage when using expert choice. The explanation was brief and relied on Fig. 6 which does not explain how there is a break in the causal constraint of the language modeling. While some empirical evidence is reported, the evidence assumes that "an abnormal loss drop" must be due to a future token leakage. 

3. The experimental results are severely lacking. Only one model is used, DeepSeekMoE, instead of the more commonly used Mixtral or traditional Switch transformer. The improvements are marginal even if there is a significant improvement in load balancing (according to their proposed metric). 

Minor: in the definition for MaxVio, the $\max_i$ is included in the numerator of fraction which does not make sense as the index i is also involved in $\bar{Load_i}$

### Questions
1. Theoretically, can it be shown that an auxiliary loss produces interference gradients that impact model performance?

2. Please clarify further how expert choice leads to future token leakage. 

3. Can this method be applied to a more diverse range of MoE models and for computer vision as well. The improvement over the baseline seems marginal. I have doubts about the impact of the method in improving performance.

### Soundness
1

### Presentation
2

### Contribution
1
