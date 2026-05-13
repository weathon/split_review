# Expected Sliced Transport Plans

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
The optimal transport (OT) problem has gained significant traction in modern machine learning for its ability to: (1) provide versatile metrics, such as Wasserstein distances and their variants, and (2) determine optimal couplings between probability measures. To reduce the computational complexity of OT solvers, methods like entropic regularization and sliced optimal transport have been proposed. The sliced OT framework improves efficiency by comparing one-dimensional projections (slices) of high-dimensional distributions. However, despite their computational efficiency, sliced-Wasserstein approaches lack a transportation plan between the input measures, limiting their use in scenarios requiring explicit coupling. In this paper, we address two key questions: Can a transportation plan be constructed between two probability measures using the sliced transport framework? If so, can this plan be used to define a metric between the measures? We propose a "lifting" operation to extend one-dimensional optimal transport plans back to the original space of the measures. By computing the expectation of these lifted plans, we derive a new transportation plan, termed expected sliced transport (EST) plans. We prove that using the EST plan to weight the sum of the individual Euclidean costs for moving from one point to another results in a valid metric between the input discrete probability measures. We demonstrate the connection between our approach and the recently proposed min-SWGG, along with illustrative numerical examples that support our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
They propose a novel method to give transport plans between disctrete distributions on Eucledian spaces named "expected sliced transport plan".
Although sliced Wasserstein distances in previous studies are computationally efficient in comparison to Wasserstein distance itself, they do not propose concrete transport plans between distributions.
To address this problem, they consider computationally efficient transport plans between distributions via slicing and lifting discussion.
It is shown that the proposed plans induce a metric for probability distributions.
In addition, they examine the performance of plans in several numerical experiments.

### Strengths
They succeed in proposing sliced transport plans inducing metric sfor probability measures.
As they claim, previous studies for sliced Wasserstein distances do not necessarily provide concrete transport plans.
While their results are only for discrete measures, I believe that it should be applicable to many problems in the real world.

In addition, they propose a tempered measure $\sigma$ on $\mathbb{S}^{d-1}$ in Section 3.2, which makes the performance of transport better.
This result gives motivation to consider general distributions on $\mathbb{S}^{d-1}$ and corresponding expected sliced transportation other than the uniform distribution.

### Weaknesses
While the motivation is computational efficiency, they do not argue it sufficiently. The discussion starting at Line 432 should be the only part referring to the computational complexities, but I believe that this is insufficient. Their claim is that the computational complexities of the proposed method does not change w.r.t. the temperature parameter $\tau$ while that of the entropic OT changes w.r.t. the regularization parameter $\lambda$. What the author(s) should compare here is not the complexities **within** the algorithms but those **between** the algorithms. Specifically, a more detailed analysis of the computational cost of the slicing operation and the subsequent 1D optimal transport calculations is needed. The authors should provide a breakdown of the time complexity for each step, including the projection of data points onto the slices, the sorting required for the 1D transport, and the final aggregation of the transport plans. Furthermore, the practical implications of the choice of $L$ (number of slices) on the overall runtime should be discussed, as this parameter directly impacts the computational burden. The current discussion lacks a comparative analysis with other methods, such as standard optimal transport solvers, in terms of both theoretical complexity and empirical runtime.

### Questions
On a very minor point: it can be better to unify the representations "transportation plan" and "transport plan".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to use a "lifting" technique to recover a transportation plan from sliced transportation maps. The lifted transportation plan applies to labels of discrete measures, They proved that the plan marginalizes to the original measures. Furthermore, the authors compute the expectation of the lifted transportation plan and plug the expectation into the original transportation problem. They finally proved that this transportation cost induced by their expected lift plan defines a metric. The authors later show empirical evidence for convergence of their new plan and distance with toy data and their metric properties with a MNIST variant.

### Strengths
+Paper is clear. 

+The lifting technique is a good fit for translating the sliced OT problem back to the OT problem on the original measures.

+The authors' proposed contributions are well demonstrated in the paper, with the exception of (4) since their results are preliminary.

### Weaknesses
-One thing that I expected from the paper but didn't find is purpose of answering the two key questions.

First question "Can a transportation plan be constructed between two probability measures ...". Also in line 61, "limiting their applicability to problems that require explicit coupling between measures." What problems require explicit coupling between measures? Does this paper solve those problems?

Second question, "can this plan be used to define a metric between the measures". Maybe the interpolation experiment shows a little bit of the usage of the metric properties. Other than that, from reading this paper, I don't see the reason of studying the metric properties.

-The empirical results are weak because the dataset is too simple to prove its usefulness in real applications. They're at most for proof of concept.

### Questions
In 144: "As a result, it is more convenient to work with lifted transport plans." 
Is plan the emphasis of the sentence? Instead of maps? And the difference between, as implied in this paper, is that maps apply to the support and plans apply to labels?


Please read proof the paper, to fix minor errors like "on the -(the) labels" in line 14, "the weights of +(the) optimal transport", and "the reason why we make this choice -(if) +(is)" in line 211

### Soundness
3

### Presentation
3

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
The paper introduces expected sliced optimal transport plans with four contributions: computational efficiency, a distance for discrete probability measures, theory and experiments demonstrating equivalence with Wasserstein distances, and use case demonstrations.

### Strengths
- The topic, approach, and technical exposition were all excellent. 
- The theoretical results were interesting and clear. 
- The empirical results were interesting including the synthetic demonstrations and real world use cases.

### Weaknesses
 - I found it hard to understand what the paper was aiming for from the introduction. The intent of the paper came into sharper focus for me well after the start of the technical section. Currently the introduction is relatively abstract in motivating the approach. I wonder whether the authors wouldn't be better served by more concrete motivations earlier. Often this is done by having a figure to illustrate the approach. Maybe figure 1 could be this if it were earlier? However, that figure would benefit from more explanation. 
- The introduction focuses on computational efficiency; however, I don't see any empirical results demonstrating this point. Because the datasets being used here aren't huge by machine learning standards, it seems important to be precise about what is meant by this claim. 

Minor confusions / questions that arise while I was reading: 
- "Traditional models scale cubically" What methods are being invoked here? 
- "However, the number of iterations required for convergence typically increases as the regularization parameter decreases, which can offset the computational benefits of these methods." I don't understand this critique. 
- Around line 46: I see the citation to Cuturi there, but the discussion is inadequate: "Various approaches have been 046 developed to address this challenge, including entropic regularization (Cuturi, 2013)," 
- Why are we introducing transport maps in equation 5?

### Questions
Please see above.

### Soundness
4

### Presentation
3

### Contribution
3
