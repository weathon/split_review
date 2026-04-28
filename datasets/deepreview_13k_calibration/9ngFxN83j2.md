# Towards Understanding Token Selection in Self-Attention: Successes and Pitfalls in Learning Random Walks

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 3, 8, 6

## Abstract
As a key component of the transformer architecture, the self-attention mechanism is known for its capability to perform token selection, which can often significantly enhance model performance. However, when and how self-attention can be trained to perform effective token selection remains poorly understood in theory. In this paper, we study the problem of using a single self-attention layer to learn random walks on circles. We theoretically demonstrate that, after training with gradient descent, the self-attention layer can successfully learn the Markov property of the random walk, and achieve optimal next-token prediction accuracy by focusing on the correct parent token. In addition, we also study the performance of a single self-attention layer in learning relatively simpler "deterministic walks" 
on circles. Surprisingly, in this case, our findings indicate that the self-attention model trained with gradient descent consistently yields next-token prediction accuracy no better than a random guess. This counter-intuitive observation that self-attention can learn random walks but struggles with deterministic walks reveals a potential issue in self-attention: when there are multiple highly informative tokens, self-attention may fail to properly utilize any of them.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes the gradient dynamics of one-layer transformer (with parameters V and W, which is self-attention pairwise logits) on predicting the next state of Markov chains in two synthetic cases (1) when the Markov chain is a random walk on a circular graph and (2) when the Markov chain is a deterministic walk (either clockwise or counter-clockwise). The conclusion is surprising: for random walk the Transformer is able to fully model the transition matrix of Markov chain (in V), and the prediction accuracy is optimal, while for deterministic walk, the prediction is random and V converges to all 1 matrix (Theorem 3.2). The paper also performs experiments to justify the results.

### Strengths
1. The paper performs rigorous mathematical study to analyze gradient dynamics in the specific Markov cases. 
2. The paper is relatively well-written.

### Weaknesses
1. I am a bit skeptical about whether Theorem 3.2 is empirically meaningful. The initial condition in the theoretical analysis is W = V = 0, which may lead to the all 1 matrix V in Theorem 3.2. What if the symmetry is broken and there is some small initial noise of W and V? In that case, will the transformer converge to something similar to Theorem 3.1? I checked the appendix and it looks like the Theorem 3.2 is indeed due to perfect symmetry in attention scores (Lemma C.3) and the gradient of V (Lemma C.2). Note that Task 1 already has noise in its input/output relationship, which Task 2 does not have. This may lead to sharp contrast between Theorem 3.1 and 3.2, which is not an issue empirically.

If Theorem 3.2 is purely because the symmetry initialization, then it would hurt the generalization of the main conclusion. If theoretical study is non-trivial with random initialization, authors can also use experiments to demonstrate that the conclusion still holds with small random initialization. 

2. How does this analysis extend to more general cases? Can it handle more general Markov chains? What if there is FFN and nonlinearity on top of the attention layer?

### Questions
1. Could the authors investigate how small random initializations of W and V affect the convergence behavior described in Theorem 3.2? This would help clarify whether the observed behavior is solely due to the symmetric initialization or if it persists under more realistic conditions.

2. Could the authors comment on how their analysis might extend to more complex Markov chains, such as those with large and compositional state/action spaces, or non-uniform transition probabilities? Additionally, it would be helpful if they could discuss the potential impact of adding nonlinearities or feed-forward layers to the transformer architecture on their theoretical results.

------
After the discussion, I raised the score from 5 to 6.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the ability of the self-attention mechanism in transformers to perform token selection by examining its performance in learning two types of sequential data: random walks vs deterministic walks on circles. The authors theoretically demonstrate that a single-layer self-attention mechanism can successfully learn the transition probabilities of random walks but fails to predict deterministic walks. This contrast reveals a limitation of self-attention when dealing with multiple equally informative tokens.

### Strengths
- The paper provides a theoretically rigorous examination of token selection by self-attention in transformers. However, analysis is limited to a very specific implementation in a simplified model with a single attention layer.
- If confirmed in more complex architectures and outside of toy problems, the results could be important.

### Weaknesses
 - The paper's focus on one-layer transformers and a single overly simple toy task limits its generalizability to more complex and realistic scenarios involving deep transformers. It is not clear whether the effect observed would arise in more complex settings. Specifically, the analysis does not consider the impact of multiple attention heads or feed-forward networks, which are crucial components of practical transformer architectures. The conclusions drawn from this simplified model may not hold when these additional complexities are introduced.
- The initialization of all weights to zero seems to be the main cause for the problem, since it would break the symmetry in the initial softmax weighting (as per step 1 of "training dynamics in learning deterministic walks"). It is unclear if the observed failure to learn deterministic walks is a fundamental limitation of self-attention or an artifact of this specific initialization scheme. The paper should explore other initialization strategies to determine the robustness of the findings.

- A more thorough validation with a wider range of token representations and architectures is required to support the conclusions of the paper. The current analysis is limited to a specific token representation and a single-layer transformer. It is not clear if the observed phenomena would generalize to other token representations, such as learned embeddings, or to more complex architectures with multiple layers and different attention mechanisms.

- Minor: positional embeddings were concatenated here, but in practical applications they are typically added element-wise; I am not sure if this would have an impact on the observed phenomenon.

### Questions
See above in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The current work introduces two case studies that highlight a rather counter-intuitive phenomena — that transformer models can effectively learn to predict the next token in a simple random walk task along a graph, but fail to learn this task when the walk is deterministic. The authors put forward theoretical reasons as to why this is the case and proceed to empirically show that their theory holds. The theoretical argument is elegant and makes an initially puzzling finding intuitively obvious, which I really liked.

### Strengths
1. The paper is overall well written and easy to follow (except for maybe Section 2.1, more later).
2. The authors give a theoretical account of the phenomena they are studying, complete with proofs supporting their point (though I only skimmed them, so cannot vouch for their correctness). Additionally, they give an intuitive, non-formal argument for why transformes succeed and fail in their test cases, which I find convincing.
3. The authors support their conclusion with empirical tests, though I think they could — and should do — more (see below).
4. The previous literature is well surveyed, though I admit that is not my primary area of expertise, so I am unlikely to know if there is anything missing.

### Weaknesses
There are two main issues in my opinion with this article:

1. The insight the authors gain from their test cases are interesting, but it their proof is based on a particular assumption — initialisation of the attention matrices to zero. How often does this happen in practice though? I understand that other assumptions such as aggregating key and query matrices into a single one to facilitate their analysis, but the other one seems a bit artificial. While this doesn’t invalidate the insight, it would be good to either see: 
    1. Experimental evidence for what happens if they use standard initialisations
    2. A good reason as to why this is not needed beyond “it makes our analysis easier”.
2. Related to the above, while the work is well situated within it’s literature, I am not convinced on how this is “interesting”. To what does this novel insight apply? Is there a specific domain or task where the authors believe this is a problem? If it is, have other researchers proposed a solution, in which case this work would be an explanation for those issues (which is good in my opinion)?

### Questions
My questions are embedded within the weaknesses.

246 - “series” instead of “serious”

There might be more, I am terrible at spotting these.

As it stands, I recommend reject. But I think the issues are fixable, mostly by addressing the concerns outlined above.

### Soundness
4

### Presentation
4

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
This paper presents an intriguing observation about self-attention mechanisms. It finds that self-attention excels at learning the Markov property of random walks but struggles with deterministic walks, which are much simpler. This suggests that if all tokens contain similar informative features, self-attention may fail to learn them effectively. The paper also provides robust experiments to support this observation.

### Strengths
+ The paper is well-written and easy to follow.
+ The observation is intriguing and sheds light on training strategies and feature selection for transformer-based models.
+ It provides a solid theoretical analysis.
+ The experiments effectively support the findings.

### Weaknesses
 - Lacks experiments with real-world data.
- Only tests on single-layer self-attention. It would be beneficial to scale up to multi-layer and multi-head self-attention to explore the results further.

### Questions
According to the weaknesses. 

Similar to a single-layer neural network, where a naive perceptron struggles as a good learner, a deep neural network with multiple linear layers can fit various functions and tasks. Given the prevalence of large language models (LLMs) today, and the shift in focus towards them, I wonder if scaling up self-attention—whether in width (multi-heads) or depth (number of layers)—would still present the same issues identified in this study?

### Soundness
3

### Presentation
4

### Contribution
4
