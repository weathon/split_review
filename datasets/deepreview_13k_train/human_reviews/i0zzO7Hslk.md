# Parameter and Memory Efficient Pretraining via Low-rank Riemannian Optimization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Pretraining large language models often requires significant computational resources and memory due to their vast parameter amount. An effective approach to enhance parameter efficiency in both training and inference is to parameterize each full-size weight as the product of two trainable low-rank factors. While low-rank fine-tuning has achieved great success, low-rank pretraining remains challenging as it requires learning extensive knowledge from scratch under the restrictive low-rank parameterization. During standard low-rank pretraining, separately optimizing the low-rank factors introduces redundant information from the full gradient, which hinders the learning process. To achieve efficient yet effective low-rank pretraining, we propose a **Lo**w-rank **R**iemannian **O**ptimizer (**LORO**). At each LORO update step, the low-rank factor pairs are jointly updated to ensure their full-size product moves along the steepest descent direction on the low-rank manifold, without the need to compute any memory-intensive full-size matrices or gradients. Hence, our LORO finds low-rank models that achieve high performance comparable to full-size pretrained models, while significantly reducing memory usage and accelerating both training and inference. A LLaMA 1B model pretrained with LORO achieves a perplexity score of 2\% better than the full-size baseline, with a 54\% reduction in model memory, a $\times1.8$ speedup in training, and a $\times2.2$ speedup in inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on memory-efficient pretraining for decoder-only transformer models, particularly in the pretraining setting. It introduces the Low-rank Riemannian Optimizer (LORO), which maintains a low-rank parameterization throughout training and inference. A central challenge in standard low-rank pretraining is that separately optimizing low-rank factors introduces redundant gradient information, which hinders learning; LORO addresses this by using Riemannian optimization to jointly update factors along the low-rank manifold’s steepest descent. Through periodic exact updates and low-cost approximations, LORO reduces memory usage, increases training speed, and achieves lower perplexity than baseline methods for low-rank transformer training.

### Strengths
I think the main formulation of the paper, which is to use Riemannian optimization to jointly update factors along the low-rank manifold’s steepest descent, is a novel and interesting approach to the problem of low-rank pretraining. The paper is generally well-written and the math is clear and easy to follow. I particularly liked the method section, where the authors devlop the solution by systematically addressing the memory and computational overheads. 

The experimental results in the pre-training setting are strong and show that LORO can achieve competitive performance with reduced memory and computation.

### Weaknesses
The main problem I see with the paper is that the authors do not provide a rigorous analysis supporting their central claim that independent updates of the low-rank factors are inefficient. They state that separately optimizing the factors B and A introduces redundant information from the full gradient, which hinders learning, but this claim is not systematically studied or empirically validated. I think this is a major weakness of the paper and should be addressed in a revision. Specifically, it would be good to see some evidence that this phenomenon is common and that it is a significant problem in practice. Additionally, it would be good to also see how LORO is able to overcome this issue and why it is more efficient than other methods in this regard.

Minor: Some other related works that can be cited:

1. Adam-mini: Use Fewer Learning Rates To Gain More, Zhang et al
2. BlockLLM: Memory-Efficient Adaptation of LLMs by Selecting and Optimizing the Right Coordinate Blocks: Ramesh et al

### Questions
Refer to the weaknesses section and please share your views on this.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel pretraining method that combines Riemannian optimization with Low-Rank Adaptation (LoRA). The authors aim to enhance the update process of the low-rank factors by integrating Riemannian optimization, which purportedly allows for more effective use of information during parameter updates and reduces redundancy caused by subspace overlap. The paper also introduces a well-designed mechanism to avoid full-size weight and gradient computation, reducing the computational cost during pretraining and resulting in inference-time acceleration for the proposed LORO method.

### Strengths
Overall, the paper presents a clear theoretical framework and demonstrates impressive experimental results. However, I remain skeptical about the results.

### Weaknesses
1. As part of the motivation, the authors assert that "separately optimizing the low-rank factors
overlooks the intricate structure of the low-rank parameterization and fails to guide their product
toward the steepest loss descent on the low-rank matrix manifold." This statement appears to be
largely intuitive. I believe that this claim requires a clearer analytical breakdown and more
substantial theoretical justifications. Specifically, the authors need to rigorously demonstrate why the standard low-rank gradient update, which independently updates the low-rank factors, is suboptimal compared to their proposed Riemannian approach. The argument that it fails to capture the "intricate structure" needs to be formalized with mathematical analysis, showing how the standard update deviates from the true gradient on the low-rank manifold. It is not sufficient to simply state that it is intuitive; a concrete analysis of the gradient update is needed to support this claim.

2. The paper mentions that to stabilize training, they apply a 5-step linear learning rate warmup and
refresh the Adam statistics at each exact LORO update step. In prior work, changing the
parameters of the Adam optimizer required careful handling, as restarting the optimizer state
often led to loss spikes. However, the proposed method seems to avoid this issue. It would be
beneficial if the authors could provide a more detailed explanation or proof regarding why LORO
exhibits robustness to this situation, particularly in comparison to previous methods where loss
spikes were problematic. The authors should analyze the specific properties of their update rule that make it less sensitive to optimizer state resets, perhaps by examining how the gradient landscape changes after the Riemannian update, and why this change is less prone to causing loss spikes.

3. The authors indicate that not every step in training involves a Riemannian update. From the
ablation study provided, it appears that using K= 500 and K= 250 and yields similar performance.
This raises questions about the necessity of the Riemannian update step. Specifically, I am
concerned that the performance improvement may not stem from Riemannian optimization itself,
but rather from the fact that the Riemannian update step refreshes the optimization subspace. It
is possible that standard low-rank steps are already sufficient for good training performance. A
more detailed ablation study isolating the effects of the Riemannian updates would help clarify
their contribution to the overall performance of the method. The ablation study should include a comparison with standard low-rank training using the same update frequency, with and without optimizer state refreshing, to isolate the effect of the Riemannian update from the optimizer refresh and the update frequency.

4. In the non-Riemannian update steps, the authors adopt the update rule in (10). The authors claim that this is a reasonable approximation of the Riemannian update step. However, intuitively, this appears to simply scale down the learning rate for low-rank pretraining,
which would be equivalent to standard low-rank pretraining. Previous work has shown that vanilla
low-rank pretraining often underperforms, so it is unclear why LORO’s approximate update step
achieves strong empirical results. I would appreciate further clarification or experiments that
explain why this approximation works well in practice. The authors need to provide a more detailed analysis of why this scaled-down update rule, which appears similar to standard low-rank training with a reduced learning rate, can achieve better results. It is necessary to demonstrate that this approximation is not simply a learning rate adjustment but has a specific mechanism that contributes to the observed performance gains.

### Questions
See above.

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
This paper propose a Riemannian update scheme for low-rank pretraining of large laguage models(LLM). The proposed scheme utilize a Riemannian gradient step (for every $K$ iterations) on the low-rank manifold (represented by SVD) for efficient Riemannian optimization. Numerical experiments are provided to show the efficiency of the proposed approach comparing to the existing low-rank pretraining approaches.

### Strengths
The paper is well-organized. The proposed algorithm is theoretically motivatived by Riemannian optimization and does not require much more computational overhead by updating the Riemannian step every $K$ steps. The proposed approach yields good performance in the experiments in the paper.

### Weaknesses
The effecitveness of the proposed approach is still under-explored both theoretically and numerically; Comparing the low-rank approach, I still have some doubts on the reliability of this work.

I have following comments and concerns regarding the paper:

1. The effecitveness of the proposed approach is still under-explored: The authors claim that the goal of the proposed approach is to (Line 82) "train a low-rank parameterized language model from scratch to achieve performance comparable to the full-size baseline". According to the scaling law (which might not be 100% applicable here), the primary indicator of the final model performance should be the model size, and this approach is using **exactly** same number of parameters as the low-rank approach. This makes me really wonder if the low-rank approach is highly underestimated in Figure 1 and Table 1. Maybe it's due to initialization/random seed in the Galore paper. The authors might want to comment on this, especially consider that their update is identical to low-rank except for the Riemannian step in every $K$ steps
2. Continuing above point, since the algorithm only update Riemannian step for every $K$ steps, I would expect to see a clear improvement at the Riemannian step (since other steps are same as low-rank, and low-rank is performing badly), say in Figure 4 (and the curve of low-rank should also be included in Figure 4). However seems that the lose is just decreasing steadily for $K=250$ or $500$. Again, the authors might want to comment on this.
3. One additional experiment I would recommend doing is that, updating the Riemannian step for every iteration or very frequently, and see if it clearly outperforms low-rank/sltrain. And then say that due to the commputational cost, oen could jsut update the Riemannian step for every $K$ iterations.
4. The inference time of the proposed method should also be the same as the low-rank approach?

### Questions
I have following comments and concerns regarding the paper:

1. The effecitveness of the proposed approach is still under-explored: The authors claim that the goal of the proposed approach is to (Line 82) "train a low-rank parameterized language model from scratch to achieve performance comparable to the full-size baseline". According to the scaling law (which might not be 100\% applicable here), the primary indicator of the final model performance should be the model size, and this approach is using **exactly** same number of parameters as the low-rank approach. This makes me really wonder if the low-rank approach is highly underestimated in Figure 1 and Table 1. Maybe it's due to initialization/random seed in the Galore paper. The authors might want to comment on this, especially consider that their update is identical to low-rank except for the Riemannian step in every $K$ steps
2. Continuing above point, since the algorithm only update Riemannian step for every $K$ steps, I would expect to see a clear improvement at the Riemannian step (since other steps are same as low-rank, and low-rank is performing badly), say in Figure 4 (and the curve of low-rank should also be included in Figure 4). However seems that the lose is just decreasing steadily for $K=250$ or $500$. Again, the authors might want to comment on this.
3. One additional experiment I would recommend doing is that, updating the Riemannian step for every iteration or very frequently, and see if it clearly outperforms low-rank/sltrain. And then say that due to the commputational cost, oen could jsut update the Riemannian step for every $K$ iterations.
4. The inference time of the proposed method should also be the same as the low-rank approach?

I think overall this is an interesting work. But it's still hard for me to believe that the every-$K$-steps Riemannian update could be such a miracle to turn the badly-performing low-rank approach to SOTA, considering no additional model parameters introduced. I'm open to discussion and would like to hear the authors' comment on this.

### Soundness
2

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
3

### Summary
The paper proposes to parameterize the weights as a low-rank matrix for parameter and memory efficient pretraining of LLMs. Instead of separately optimizing two factors using (stochastic) gradient descent, the paper leverages Riemannian geometry of low-rank matrices, and propose efficient gradient computation and update strategies. The pretraining performance is evaluated on LlaMA 60M to 1B models.

### Strengths
1. The paper proposes a novel Riemannian optimization strategy for optimizing low-rank matrices.

2. The proposed gradient and update strategies only through the factorized form are interesting.

3. The performance is strong compared to the baselines and is comparable to the full-rank pretraining.

### Weaknesses
My biggest concern on this work is regarding the empirical simplification using approximated Riemannian update. The paper proposes to use a scaling factor for both the update of B and A. This results in an update which exactly matches the standard update (the same scaling factor can be merged with learning rate). In summary, it appears that for most iterations, Algorithm 1 simply perform standard gradient descent update for the low rank factors and periodically update with Riemannian gradient. This raises the question of whether the periodic Riemannian gradient update results in such a performance improvement.

### Questions
1. How did the experiment initialize the B and A?

2. Have you tried different scaling factors for B and A, and whether using different scaling factors can result in different performance?

### Soundness
3

### Presentation
3

### Contribution
3
