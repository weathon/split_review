# Multi-Draft Speculative Sampling: Canonical Architectures and Theoretical Limits

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We consider multi-draft speculative sampling, where the proposal sequences are sampled independently from different draft models.  At each step, a  token-level draft selection scheme takes a list of valid tokens as input and produces an output token whose distribution matches that of the target model. Previous works have demonstrated that the optimal scheme (which maximizes the probability of accepting one of the input tokens) can be cast as a solution to a linear program. In this work we show that the optimal scheme can be decomposed into a two-step solution: in the first step an importance sampling (IS) type scheme is used to select one intermediate token; in the second step (single-draft) speculative sampling is applied to generate the output token.  For the case of two identical draft models we further 1) establish a necessary and sufficient condition on the distributions of the target and draft models for the acceptance probability to equal one and 2) provide an explicit expression for the optimal acceptance probability.  Our theoretical analysis also motives a new class of token-level selection scheme based on weighted importance sampling. Our experimental results demonstrate consistent improvements in the achievable block efficiency and token rates over baseline schemes in a number of scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Previous papers showed the optimality for a token selection rule when one token was chosen from the draft model. The authors do the same for the case when two tokens are selected. The authors decompose the problem of token selection into two steps --- first select one of K tokens using an importance weighted sampling technique, and then using the optimal single token selection proposed in previous papers. Finding the optimal token selection rule then reduces to finding the best importance weighted sampling technique.

The authors then show a necessary and sufficient condition for the existence of an optimal token selection rule where two tokens are selected from the draft. They then present an algorithm to solve the resulting linear program faster than the O(n^2) standard solution.

The authors compare the Importance sampling algorithm with SpecInfer on various tasks, and show that IS comes closer to optimal than SpecInfer.

### Strengths
The results in the paper are quite original and significant, to my knowledge, which is a bit limited. The experiments show that the proposed algorithm works well in practice.

### Weaknesses
I would have liked the presentation in Section 4 to be a little clearer - request you to write out the full linear program, and then explain the truncation a bit more - what is the truncated program computing? Specifically, it would be helpful to see the explicit form of the linear program with all variables and constraints before any truncation is applied. This would allow the reader to understand the exact optimization problem being solved. The explanation of the truncation procedure could also be more detailed. It's not immediately clear how the truncation affects the solution and what the truncated program is actually optimizing. For example, what is the relationship between the optimal solution of the full program and the truncated one, and what are the potential trade-offs introduced by the truncation? 

In the experiment section, please include results for Temperature < 1, which is much more common in practice. It's important to evaluate the performance of the proposed method under realistic conditions. The current experiments only consider a temperature of 1.0 for the target model, which is not representative of typical usage scenarios. It would be beneficial to see how the method performs with lower temperatures, as this could reveal potential limitations or areas for improvement. For instance, how does the acceptance rate and block efficiency change as the temperature decreases, and are there any specific temperature ranges where the method performs particularly well or poorly?

### Questions
I would like to see a comparison to the results in https://openreview.net/forum?id=9KxnxWOBA5

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the problem of multi-draft speculative sampling and makes new observations and provides a new algorithm. Of the new observations, Theorems 2 and 3 standout which characterize the optimal acceptance rate for two drafts and further show when the acceptance rate is one. The new algorithm exploits certain structure in the optimal transport problem and provides a clever approximate solution.

### Strengths
The paper is well written and easy to follow. Theorems 2 and 3 are novel and the experimental results are convincing.

### Weaknesses
See questions section below.

- In Figure 3, experiments are conducted for draft temperatures > 1.0. However typically, target model temperature is often set to 1.0 or less than 1.0. Given this, I was expecting draft temperatures also to be <= 1.0. I was wondering how these draft temperatures were chosen?

- Would it be possible to say how the gap between the proposed approach and previous approaches vary as the target model temperature varies from 0.0 to 1.0?

- Theorems 2  and 3 provide a nice characterization of acceptance probability. However, given two distributions p, q, evaluating the condition seems to require 2^{vocabulary size} number of computations. Is there a faster way to evaluate these quantities?

- There are some approximate ways to solve the optimal transport by Sinkhorn methods e.g., https://amsword.medium.com/a-simple-introduction-on-sinkhorn-distances-d01a4ef4f085. I was wondering if these ideas are applicable here?

- Architectures in ML, typically refer to neural architectures. Given several works which propose different drafting methods for speculative decoding, I was thinking "canonical architectures" refers to some new drafters. It might be good to clarify this distinction early on in the paper.

- Can you please expand on what token rate means? Is it the number of tokens / second?

### Questions
- In Figure 3, experiments are conducted for draft temperatures > 1.0. However typically, target model temperature is often set to 1.0 or less than 1.0. Given this, I was expecting draft temperatures also to be <= 1.0. I was wondering how these draft temperatures were chosen?

- Would it be possible to say how the gap between the proposed approach and previous approaches vary as the target model temperature varies from 0.0 to 1.0?

- Theorems 2  and 3 provide a nice characterization of acceptance probability. However, given two distributions p, q, evaluating the condition seems to require 2^{vocabulary size} number of computations. Is there a faster way to evaluate these quantities?

- There are some approximate ways to solve the optimal transport by Sinkhorn methods e.g., https://amsword.medium.com/a-simple-introduction-on-sinkhorn-distances-d01a4ef4f085. I was wondering if these ideas are applicable here?

- Architectures in ML, typically refer to neural architectures. Given several works which propose different drafting methods for speculative decoding, I was thinking "canonical architectures" refers to some new drafters. It might be good to clarify this distinction early on in the paper.

- Can you please expand on what token rate means? Is it the number of tokens / second?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies the optimal token-level draft selection for a speculative sampling. In particular, speculative sampling is a method for accelerating autoregressive sampling by using smaller "draft" models to generate candidate tokens and a larger model to determine which tokens to accept. The key problem studied in this paper is how to propose tokens to optimize the probability they will be accepted. Importantly, increasing the acceptance probability leads to less calls to the larger model which in theory could increase the tokens per seconds. The key theorem of this paper is to characterize the necessary and sufficient conditions when two tokens are generated by the draft model. Interestingly, unlike the one token case, this paper shows that one can reach probability 1 acceptance even if the draft and large models have different token distributions. Finally, the paper ends with (i) heuristics to practically leverage the proposed sampling scheme, e.g., truncating the token distributions (ii) a heuristic scheme for leveraging the proposed importance sampling to larger sequences and (iii) empirical evidence of the effectiveness of the approach for K=2 and larger.

### Strengths
This paper provides a strong theoretical contribution to a very important topic. Speculative decoding serves as a refreshing and novel direction for accelerating LLM inference. This work puts the multi-draft model selection problem on better theoretical footing.

The results seem to be sound from my reading and no obvious errors were found.

### Weaknesses
By and large the biggest complaint I have with this draft is the background exposition. Prior to reading this I was not familiar with speculative decoding. While I understand space is tight, many key concepts such as the role and form of accepting probability in the speculative decoder were not clearly explained. This is a *key* aspect of the work, and the draft would strongly benefit for giving it more treatment. To be honest, I couldn't understand anything the first time I read the paper and had to go back to the original speculative sampling paper [1] before I could piece things together.

Nevertheless, after reading, I now understand that this paper is targeting the acceptance criteria as it determines the number of candidate tokens used via a Bernoulli like-process.

### Questions
- Could you give some intuition about the conjecture in remark 2. It says that the exponent over the sum of the p-weights should match K (the number of tokens to generate per round). It's not at all clear to me why these should be so tightly coupled and why other lower order terms wouldn't appear.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the problem of multi-draft speculative sampling, where the optimal scheme can be cast as a solution to a linear program. The key idea behind this work is that this optimal scheme can be decomposed into a two-stage solution. Based on this idea, the authors provide some theoretical findings towards the two-stage solution. Motivated by the analysis, the authors propose a new class of token-level selection scheme based on weighted importance sampling, which shows consistent improvement in various scenarios.

### Strengths
1. The introduction of the two-step scheme are simple and intuitive, making it easy to understand.
2. The authors provide a solid theoretical analysis for token-level optimal draft selection.
3. The truncated LP algorithm is novel to the field of speculative decoding and theoretically better than SpecTr.
4. Extensive experiments, including different datasets, different decoding temperature and different draft models demonstrate the effective of proposed method.

### Weaknesses
1. I think the contributions of this work is a little weak. Given that speculative decoding shows poor performance with batch size larger than 1, the multi-draft sampling is usually not an appropriate option for speculative decoding. I think the authors should emphasize the contributions to real-world speculative decoding applications. 
2. While I appreciate that the authors add some examples for better explanation, I think the authors should add a clear notation section with distinct description.
3. For the truncated LP draft selection algorithm, there exists an operation of sorting, which takes a complexity of $O(n\log n)$ and may influence the final speedup. The authors should report its real-world time consuming and compare to vanilla multi-draft selection, especially the empirical results on models with large vocab size, e.g., Llama 3.1 with vocab size 128k. Besides, for multi-draft scenarios with $K > 2$, the authors propose a multi-stage manner, which may affect the final speedup as well.
4.  I think the authors should conduct experiments on more benchmarks (e.g. HumanEval [1], GSM8K [2] and MT-bench [3]) for a fair comparison. Besides, the authors should report the real-world speedup to demonstrate the effectiveness of proposed method.

### Questions
1. Can proposed truncated LP combined with SOTA speculative decoding (e.g. Medusa [4] and Eagle [5]) methods for better performance?
2. Why the authors do not discuss and compare a multi-draft selection method RRS [6]?
3. Could you please discuss the limitations of this paper?

[4] Cai, Tianle, et al. "Medusa: Simple llm inference acceleration framework with multiple decoding heads." *arXiv preprint arXiv:2401.10774* (2024).

[5] Li, Yuhui, et al. "Eagle: Speculative sampling requires rethinking feature uncertainty." *arXiv preprint arXiv:2401.15077* (2024).

[6] Jeon, Wonseok, et al. "Recursive speculative decoding: Accelerating llm inference via sampling without replacement." arXiv preprint arXiv:2402.14160 (2024).

### Soundness
3

### Presentation
3

### Contribution
2
