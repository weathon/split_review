# SoftTreeMax: Exponential Variance Reduction in Policy Gradient via Tree Expansion

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
Despite the popularity of policy gradient methods, they are known to suffer from large variance and high sample complexity.
To mitigate this, we introduce \treepol{} -- a generalization of softmax that takes planning into account. In \treepol{}, we extend the traditional logits with the multi-step discounted cumulative reward, topped with the logits of future states. We consider two variants of SoftTreeMax, one for cumulative reward and one for exponentiated reward. For both, we analyze the gradient variance and reveal for the first time the role of a tree expansion policy in mitigating this variance. We prove that the resulting variance decays exponentially with the planning horizon as a function of the expansion policy. Specifically, we show that the closer the resulting state transitions are to uniform, the faster the decay. In a practical implementation, we utilize a parallelized GPU-based simulator for fast and efficient tree search. Our differentiable tree-based policy leverages all gradients at the tree leaves in each environment step instead of the traditional single-sample-based gradient. We then show in simulation how the variance of the gradient is reduced by three orders of magnitude, leading to better sample complexity compared to the standard policy gradient. On Atari, \treepol{} demonstrates up to 5x better performance in a faster run time compared to distributed PPO. Lastly, we demonstrate that high reward correlates with lower variance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new policy gradient, named softtreemax, which combines the tree search within the policy gradient method. The authors . We analyze the gradient variance of SoftTreeMax and reveal how tree expansion helps reduce this variance.

### Strengths
1. The idea of incorporating the tree search within the policy gradient is novel.

2. The variance analysis is solid.

3. The proposed softmax tree method is also extended to infinite action space.

4. Multiple experiments are conducted to demonstrates the necessity of reducing the variance of PG for improving performance and the empirical performance advantage of the proposed method.

### Weaknesses
1. When there is approximation error in the model P and r, what are the variance of SoftTreeMax? Do the claimed exponential variance reduction still hold with the approximate model? Is it worth to make the PG, a model-free method, to a model-based method by combining it with the tree search. The core issue is whether the benefits of variance reduction through tree search outweigh the potential inaccuracies introduced by model approximation, especially in complex environments where accurate models are difficult to obtain. The paper needs to provide a more rigorous analysis of the trade-offs between model bias and variance reduction in this context.

2. Although authors mention that formally proving the conjectured global convergence with fast rate as in (Mei et al 2020b) is subject to future work. It is hard to demonstrate its advantage over the traditional SoftMax policy gradient, or more generally traditional policy gradient methods without comparing the sample complexity between SoftTreeMax policy gradient and traditional SoftMax policy gradient. The main missing piece is that the reduction in variance does not necessarily imply the faster convergence of smaller sample complexity if bringing such variance reduction needs to use a form of policy gradient sacrifice the performance in the deterministic setting (For example, I am not sure whether the proposed SoftTreeMax policy gradient will even converge in the derterministic setting). The paper needs to provide a more thorough comparison of sample complexity, not just wall-clock time, and also needs to address the convergence properties in deterministic or near-deterministic environments.

3. There are some relevant papers that address related problems that authors may need to add to the related work.

(1) Optimization Methods for Interpretable Differentiable Decision Trees in Reinforcement Learning, Andrew Silva, et al,. 2020 AISTATS.

(2) On the Global Optimum Convergence of Momentum-based Policy Gradient, Yuhao Ding, et al, 2022 AISTATS. 

It is important to compare with (1) to evaluate whether this paper is still the first work on proposing a differentiable parametric policy that combines tree expansion with PG. (2) also studies the convergence and the variance reduction for softmax PG. The authors should clarify the novelty of their approach in light of existing work on differentiable decision trees and variance reduction techniques for policy gradients.

### Questions
1. When there is approximation error in the model P and r, what are the variance of SoftTreeMax? Do the claimed exponential variance reduction still hold with the approximate model? Is it worth to make the PG, a model-free method, to a model-based method by combining it with the tree search.

2. Although authors mention that formally proving the conjectured global convergence with fast rate as in (Mei et al 2020b) is subject to future work. It is hard to demonstrate its advantage over the traditional SoftMax policy gradient, or more generally traditional policy gradient methods without comparing the sample complexity between SoftTreeMax policy gradient and traditional SoftMax policy gradient. The main missing piece is that the reduction in variance does not necessarily imply the faster convergence of smaller sample complexity if bringing such variance reduction needs to use a form of policy gradient sacrifice the performance in the deterministic setting (For example, I am not sure whether the proposed SoftTreeMax policy gradient will even converge in the derterministic setting).

3. There are some relevant papers that address related problems that authors may need to add to the related work.

(1) Optimization Methods for Interpretable Differentiable Decision Trees in Reinforcement Learning, Andrew Silva, et al,. 2020 AISTATS.

(2) On the Global Optimum Convergence of Momentum-based Policy Gradient, Yuhao Ding, et al, 2022 AISTATS. 

It is important to compare with (1) to evaluate whether this paper is still the first work on proposing a differentiable parametric policy that combines tree expansion with PG. (2) also studies the convergence and the variance reduction for softmax PG.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes SoftTreeMax, which uses planning to reduce the policy gradient variance. In particular, the authors proposed two variants, i.e., C-SoftTreeMax and E-SoftTreeMax, where logits are re-defined as Eq. (2). They show that the variance of the proposed gradient decays exponentially w.r.t. $d$ (trajectory depth). They also characterize gradient bias by approximation errors. Experiments on Atari shows that the proposed methods achieve better performance and lower variance than PPO.

### Strengths
1. The paper is well-written, with clear introduction of the settings, methods, and results.
2. Combining policy gradient and tree search seems very interesting.
3. Experiments verify the proposed methods, an they look promising.

### Weaknesses
1. It is confusing to me where the exponential decay of variance is from, i.e., from the design or the fact that the policy is nearly deterministic, and therefore not clear to me if reducing both gradient and variance would benefit (please see the question below).

Looking at Lemma 4.1 and Lemma 4.3, it seems the exponential decay of variance is from $\nabla_\theta \log{ \pi_{\theta}(\cdot | s) } $. If $\pi_{\theta}(\cdot | s)$ has softmax parameterization then this basically means the policy is nearly deterministic? If this is true, then this also means the policy gradient has to be close to zero (softmax policy has almost zero gradient near deterministic policies), which is expected to slow down the convergence. Could you explain why reducing both gradient and variance to exponentially small would help learning?

### Questions
Looking at Lemma 4.1 and Lemma 4.3, it seems the exponential decay of variance is from $\nabla_\theta \log{ \pi_{\theta}(\cdot | s) } $. If $\pi_{\theta}(\cdot | s)$ has softmax parameterization then this basically means the policy is nearly deterministic? If this is true, then this also means the policy gradient has to be close to zero (softmax policy has almost zero gradient near deterministic policies), which is expected to slow down the convergence. Could you explain why reducing both gradient and variance to exponentially small would help learning?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article introduces a new family of policies called SoftTreeMax, which are a model-based generalization of the popular softmax used in reinforcement learning (RL). SoftTreeMax policies replace the standard policy logits with the expected value of trajectories that originate from specific states and actions. These policies aim to reduce the high variance of policy gradients and improve RL performance.

The article contains theoretical analysis, including variance bounds for SoftTreeMax, that demonstrates how the gradient variance decays exponentially with the planning horizon. Additionally, the article discusses how the gradient bias introduced by an approximate forward model diminishes with the approximation error.

Experimental results comparing SoftTreeMax to distributed Proximal Policy Optimization (PPO) demonstrate that SoftTreeMax leads to better sample complexity and improved performance in various Atari games, with significantly lower gradient variance.

### Strengths
The methods introduced in this paper are shown to reliably reduce the variance of PG, which is derived theoretically and then verified in experiments. The paper is clearly written, provides mathematical proofs and practical implementations of the results, and seems like a meaningful incremental contribution.

### Weaknesses
Lack of experiments with probabilistic environments.

### Questions
- What do you mean by "reward and variance are negatively correlated" on page 8?
- The definition of Var_x(X) seems to have a typo.
- How would you expect the sampling variance to impact the policy gradient if the expectations cannot be computed exactly?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose SoftTreeMax in this paper, which is a new method that aim to mitigate the high sample complexity and large variance of policy gradient methods by employing planning. It extends traditional logits with the multi-step discounted cumulative reward and the logits of future states. It is shown that tree expansion helps reduce gradient variance. The variance decays exponentially with the planning horizon, and the closer the induced transitions are to being state-independent, the faster the decay. With approximate forward models, the resulting gradient bias diminishes with the approximation error while retaining the same variance decay. SoftTreeMax reduces the gradient variance by three orders of magnitude in Atari, leading to better sample complexity and improved performance compared to distributed PPO.

### Strengths
The paper proposes a novel approach, SoftTreeMax, to mitigate the large variance and high sample complexity for policy gradient methods by leveraging tree expansion and softmax. While there have been related works that study the softmax operation in policy gradient or value-based approaches, SoftTreeMax is unique in its focus on tree expansion to reduce variance. The paper is well-written and easy to follow, with most claims being well-discussed within the paper. The problem of mitigating large variance and high sample complexity for policy gradient methods is a significant challenge in RL, and SoftTreeMax provides a promising solution.

### Weaknesses
One weakness of the paper is in its experimental evaluation section. While the paper presents promising results for SoftTreeMax in Atari, some of the claims made are not well-supported. For example, the paper does not include enough baselines to make a fair comparison with SoftTreeMax. This makes it difficult to determine the extent of SoftTreeMax's improvement over existing methods. Specifically, the comparison to distributed PPO, while showing a reduction in variance, does not sufficiently demonstrate the method's advantage in terms of sample efficiency or final performance against other state-of-the-art algorithms designed to address similar challenges. The paper should include comparisons against algorithms that also focus on reducing variance and improving sample complexity, such as those that incorporate baseline techniques or other advanced policy gradient methods.

Additionally, the paper lacks in-depth comparison with other related methods. While the paper compares SoftTreeMax with distributed PPO, it does not provide a comprehensive comparison with other state-of-the-art methods in the field. This makes it difficult to determine the generalizability of SoftTreeMax and its performance in comparison to other methods. The paper should explore how SoftTreeMax compares to methods that utilize similar tree-based planning or those that employ alternative approaches to variance reduction. Without these comparisons, it is hard to assess the true novelty and practical impact of the proposed method.

### Questions
> Policy gradient methods suffer from large variance and high sample complexity. To mitigate this, we introduce —a generalization of softmax that employs planning.

However, in the experimental evaluation part, only PPO is used as the baseline algorithm. There have been many efforts to reduce the variance and improve sample complexity for policy gradient methods (e.g., including a baseline). It is therefore better to also compare state-of-the-art approaches that also solve the same problem.

> We do so by sub-sampling only the most promising branches at each level. Limiting the width drastically improves runtime, and enables respecting GPU memory limits, with only a small sacrifice in performance.

Doesn’t this also introduce additional variance by sub-sampling and pruning?

>  For depths $d \geq 3$, we limited the tree to a maximum width of 1024 nodes and pruned trajectories with low estimated weights.

Does it suffer from a limitation when used with a larger value of $d$, which may lead to a more significant limitation of the allowed maximum width considering costs?

> Figure 3: Reward and Gradient variance: GPU SoftTreeMax (single worker) vs PPO (256 GPU workers).

Does it perform more sample-efficient than baseline methods (not compared in terms of final performance or actual wall-clock time)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
