# TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
The Mixture of Experts (MoE) architecture has emerged as a promising solution for reducing computational overhead by selectively activating subsets of model parameters. The effectiveness of MoE models is primarily dependent on their routing mechanisms, with the widely adopted Top-K routing scheme used to activate experts. However, the Top-K scheme has notable limitations, including unnecessary activations and underutilization of existing experts. In this work,  rather than modifying the routing mechanism as in previous studies, we propose Ternary Choice MoE (TC-MoE), a novel approach that expands the expert space by multiplying each expert with the ternary set {-1, 0, 1}. This expansion allows for more efficient and effective expert activations without incurring significant computational cost. Additionally, given the unique characteristics of the expanded expert space, we introduce a new load balancing loss and reward loss to ensure workload balance and achieve a flexible trade-off between effectiveness and efficiency. Extensive experiments demonstrate that TC-MoE achieves an average improvement of more than 1.1% over the traditional approaches, while reducing the average number of activated experts by up to 9%. These results confirm that TC-MoE effectively address the inefficiencies of classical routing schemes, offering a more efficient and scalable solution for MoE-based large language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an interesting study about Mixture of Experts (MoE). Instead of selecting the top-K experts in the architecture of MoE to be active in prediction, the paper extends the weights of experts to be projected to {−1, 0, 1}, which allows negative contributions from certain experts. To incorporate this idea, it is necessary to enable the router to learn more complex routing strategies during the training process. New loss functions are thus designed. Evaluation was conducted on a decoder-only transformer model, primarily based on the LLaMA architecture. The model consists of 32 transformer layers, each including both an attention layer and an MoE layer. And each MoE layer consists of 8 FFN experts. The evaluation tasks are mainly text-based, such as language understanding and commonsense reasoning. The results demonstrate that the proposed model outperforms mostly the other baselines.

### Strengths
S1: The paper is easy to follow. The motivation is clear. The overall design is reasonable. 
S2: The evaluation is comprehensive, from the overall performance comparison with baselines on downstream tasks, ablation study to analysis of active experts over layers, over steps and so on.

### Weaknesses
W1: In the proposed architecture, will the requirement on memory doubled, or even more? Although no extra computational cost may be introduced.
W2: The results show that most of the time, only 2 experts (or on average 1.8 experts) are selected for being active. Is this small number of active experts limiting the performance improvement regarding the introduction of negative contribution? By checking Table 1 and 2, we can see that the proposed model is not always outperforming baselines with a notable improvement.

### Questions
Please see the W1 and W2.

---- After the rebuttal
I have read the response and additional results from authors. W1 and W2 are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose an alternative routing scheme to the widely-used Top-K approach in Mixture of Experts (MoE) models. Their method expands the expert space by introducing a multiplicative set {−1,0,1}, allowing each expert E to activate as E\*1, E\*(−1), or E\*0. Here, E\*0 corresponds to a no-operation choice, effectively reducing the number of active experts to save computational resources. This addition permits the model to activate fewer than K experts when beneficial, lowering computation costs.
To optimize the routing, they adapt the load balancing loss to treat each expert Ei equivalently, regardless of whether it is activated with +1 or −1. Additionally, they introduce a loss term that rewards the model for selecting E\*0, controlled by a hyperparameter that balances efficiency and accuracy. This approach allows the model to expand the effective expert space without adding significant parameter costs. Their results show improvement over three other competitors (Top-K, Random drop, Top-P) in both accuracy and computational savings.

### Strengths
- The authors introduce a novel routing scheme that minimizes overhead while achieving comparable or improved accuracy and reduced computational cost.
- The paper is well-written, with a clear, logical flow and excellent presentation.
- The evaluation is thorough, tested across multiple datasets, strengthening the results.
- Additional analyses, such as the impact of unnecessary activations, activated ratio of different expert types, Load Balance, and the ablation study, are relevant and well-executed, adding depth to the study.
- The authors made a commendable effort in providing detailed information for reproducibility, including specific model configurations, dataset details, and experimental setups.

### Weaknesses
 - Some figures are not fully self-explanatory; they lack clear takeaways, requiring readers to refer back to the text for important details to understand them.
- The improvements in accuracy appear marginal and may not be statistically significant (although it does seem to be better in terms of computation needed).
- Despite reporting the accuracy correctly on some test benchmarks, some of the results presented in the figures (Figs. 3, 4, 5, 6 and 7) are based on training loss or analyses conducted solely on the training dataset. For a more robust evaluation, results should ideally be shown on a validation or test set to confirm generalization.

### Questions
- With a variety of datasets used, why were some of the most standard benchmarks, such as MMLU or SuperGLUE, left out?
- Could the authors provide more justification for choosing (K = 2) in their Top-K approach? It appears they reference Zoph et al. (2022), but additional context would clarify this choice.
- Some benchmarks categorize tasks by difficulty. Would it be possible to show if the model's accuracy improvements correlate with task difficulty?
- Why did the authors limit quantization levels to ({-1, 0, 1})? Exploring additional quantization levels might provide further insights.
- Given the new term introduced in the loss function, is the loss comparison with other baselines still fair and directly comparable?

### Soundness
3

### Presentation
4

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
This paper identifies the limitation of the commonly-used TopK routing scheme of MoEs:  unnecessary activations and underutilization of existing experts. The authors propose a solution by expanding expert space via a ternary set. Experimental results showcase the effectiveness of the method.

### Strengths
- The paper is easy to follow and clearly structured.

- The authors propose a novel method for improving MoE, which does not act on the router but takes a different approach to expand expert space. 

- The experiments are extensive and the ablation study effectively shows the necessity of having both zero experts and negative experts.

### Weaknesses
 - Only the LLaMA architecture is tested, and only Top2 routing is performed. It is questionable if the results can generalize to other base architectures and TopK (k=1, 4, etc.) routing.

### Questions
- I am having some difficulty understanding how the reward loss functions as you intend. Based on equation (12), minimizing the reward loss seems to result in assigning gating values close to zero for the $E_0$ experts?

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
5

### Summary
This paper proposes a scheme for improving MoE models by using the idea of ternary quantization over the experts. The core idea of this paper is based on their observation that the Top-k scheme underutilizes experts and does not have a way of dynamically selecting the number of experts for a particular token. Their scheme proposes to expand the number of experts available by converting the existing experts three types of experts : null, same, negative. In order to deal with the new challenges this scheme brings about, they design a new load balancing and reward loss. The load balancing loss simply extends the standard loss by accounting for the fact that the expert and the negation of that expert are really the same expert and thus on the same device and so their total workload needs to be balanced. Through experiments, they observe this scheme outperforms standard MoE models by about 1% in flop matched settings on downstream tasks.

### Strengths
In my opinion, the main strength of this paper is the simplicity of the proposed MoE augmentation scheme. Their observation regarding
the negative contribution of some experts is interesting though it is contrary to the idea that dense training / inference is better [1].
Their baseline comparisons are correct although I believe comparing simply with Top-k = 2 would be enough and the compute could have been allocated better elsewhere i.e training larger models. While there is limited explanation for why the ternary quantization works, they have good empirical observations. If the schemes load balancing is better than the top-k load balancing loss, then this approach is indeed worth scaling up in my opinion.

[1] - Pan, Bowen, et al. "Dense Training, Sparse Inference: Rethinking Training of Mixture-of-Experts Language Models." arXiv preprint arXiv:2404.05567 (2024).

### Weaknesses
The performance improvement is quite marginal and since the evaluation is done a relatively small models, we do not know if this technique will scale to larger models. I also did not find any theoretical / intuitive justification for why null experts or negative experts should help. In the questions subsection, I have included one potential reason but it would be interesting to know the intuition the authors had for developing this scheme.
The evaluation is done on limited benchmarks and the impact on realistically sized models is unknown.  A model with 2.3B total parameters has approximately only 700M activated parameters with a Top-k=2 routing scheme. Did the results hold on any smaller models trained or models trained on a more higher quality pretraining dataset like FineWeb? Can the authors evaluate on MMLU as well?. I would have also liked to see the reduction in FLOPS compared to the standard baseline and how their scheme is impacted by fine-grained experts. My intuition is that it would be less effective since their is more capacity within the base MoE to learn different types of experts and thus the need for negated or null experts might be less.

Typos and grammar errors
Line 105 - of classical routing scheme

### Questions
Why did the authors not release their code? How can I verify their results in this paper?
In Fig 2B I can see that there is no null expert for Expert 3. This is different from what the text says that the total expert count = 3 x base_num experts. Is this just an illustration error?

Is this paper suggesting that a dense forward pass is worse than a sparse forward pass? Personally, I have performed several experiments with varying the number of K over standard dense MoE models during training and always found performance to monotonically increase with the number of activated experts. It would be beneficial to be able to add some experiments where the authors can show activation how the performance on a benchmark task(s) is impacted by increasing top-k by 1 over some useful range. 

How are the results in Fig 1a computed? Are these results on benchmark scores evaluated for a particular setting of K? A more detailed caption would be helpful for future readers.

How is the computation for the total number of experts done? It says on Line 210 it is $2N + K$ but if each expert is expanded to three experts, isn't that simply $3N$? Please clarify this.


Do the authors find any connection with null experts to attention sinks [1]? It would be interesting to have a discussion of that as I believe something similar to the idea of attention sinks is happening where instead of randomly routing to a useless expert (in the case of fixed top-k) the model can dynamically choose the number of experts needed for each token. 

[1] - Xiao, G., et al. "Efficient Streaming Language Models with Attention Sinks, 2023." URL http://arxiv. org/abs/2309 17453.

### Soundness
3

### Presentation
3

### Contribution
3
