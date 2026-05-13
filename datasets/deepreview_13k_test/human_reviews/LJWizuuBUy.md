# SWAP: Sparse Entropic Wasserstein Regression for Robust Network Pruning

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
This study addresses the challenge of inaccurate gradients in computing the empirical Fisher Information Matrix during neural network pruning. We introduce \texttt{SWAP}, a formulation of Entropic Wasserstein regression (EWR) for pruning, capitalizing on the geometric properties of the optimal transport problem. The ``swap'' of the commonly used linear regression with the EWR in optimization is analytically demonstrated to offer noise mitigation effects by incorporating neighborhood interpolation across data points with only marginal additional computational cost. The unique strength of \texttt{SWAP} is its intrinsic ability to balance noise reduction and covariance information preservation effectively.
Extensive experiments performed on various networks and datasets show comparable performance of \texttt{SWAP} with state-of-the-art (SoTA) network pruning algorithms. Our proposed method outperforms the SoTA when the network size or the target sparsity is large, the gain is even larger with the existence of noisy gradients,  possibly from noisy data, analog memory, or adversarial attacks. Notably, our proposed method achieves a gain of 6\% improvement in accuracy and 8\% improvement in testing loss for MobileNetV1 with less than one-fourth of the network parameters remaining.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Robust Network Pruning With Sparse Entropic Wassertein Regression

In this paper, the authors propose a method to prune neural networks. In particular, in the Sparse Linear Regression Formulation of network pruning, the authors replace the first $l_0$ regression term with Wasserstein regression. Theoretical justifications and empirical experiments show that the proposed pruning strategy is effective and robust against gradient/data noise.

### Strengths
- The paper is well-written and the problem is well-motivated.
- The proposed method has desirable properties and shows improved performance over previous methods, especially at larger sparsity.

### Weaknesses
- “The noise level σ is set to be the standard deviation of the original gradients”. Why is this the noise level for both gradients and data? I would like to see a more detailed explanation how how the noise is added to data and gradients.
- Can the authors also provide an accuracy table for Table 2 and Table 3?

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a technique for pruning (sparsification) of neural networks that relies on robust estimation of the empirical Fisher Information Matrix as a surrogate for the Hessian of the training loss.  Earlier work has relied on a decomposition of the FIM to motivate a sparse LR formulation of an MIQP framework. 

In contrast, in this work the authors propose a framework to address instances of contaminated gradients. In this situation, one must leverage robust estimators of the FIM, or risk a significant drop in empirical performance. By studying the original MIQP problem from the perspective of entropic Wasserstein regression, the authors propose a variation of the sparse LR formulation which amounts to substituting the 2-Wasserstein distance with entropic regularization for the quadratic regression loss. Notably, without entropic regularization, the formulation is equivalent to that of the sparse LR framework. 

Theoretically, the authors demonstrate that pruning via entropic Wasserstein regression exactly corresponds to gradient averaging using Neighborhood Interpolation, with the entropic regularization term governing the size of the neighborhood. Algorithmically, the method is simple and computationally efficient. Finding solutions to the problem is done via coupling sinkhorn iterations with SGD. Numerically, the performance of the method exceeds that of previous work and is competitive with the state of the art. 

The method is simple and implies an elegant interpretation, as explored by the authors. Numerically, improvements over existing methods are observed- particularly when the training gradients are corrupted by noise. However, there is a significant number of grammatical mistakes and instances of poor phrasing. I do recommend this paper for acceptance, but suggest that the authors devote more time to proofreading the manuscript.

### Strengths
The following are the primary strengths of this paper:

- The authors propose a straightforward (but novel) modification to the sparse LR framework for neural network pruning. The modification amounts to an additional regularization term grounded by an interpretation using the principles of optimal transport. The optimization problem remains efficiently solvable. 

- The authors motivate their method via an analysis of the robustness  properties exhibited by solutions to their optimization problem. Namely, by proving that pruning using their technique implicitly corresponds to gradient averaging via a certain neighborhood interpolation and naturally trades off between a measure of robustness and the quality of the covariance estimator.

- Additional discussions on sample complexity, ablations on the sparsity and regularization parameter, and alternative methods for computation of the EWR solution are comprehensive and provided in the appendix.

- The method proposed by the authors improves results over existing methods, particularly when the training gradients are corrupted by noise. 

- Code is provided by the authors as a github link, which is appreciated.

### Weaknesses
As a reviewer, I highlight that I am unfamiliar with the current state-of-the-art pruning techniques. I defer to other reviewers regarding the thoroughness of the comparative experiments.However, the method seems grounded. The structure of the manuscript is OK. The writing and clarity of this paper could be significantly  improved. In particular, many phrases and statements are unclear, beginning with the abstract:

_This study unveils a cutting-edge technique for neural network pruning that judiciously addresses noisy gradients during the computation of the empirical Fisher Information Matrix (FIM)._

Additionally, some choices could be better motivated. E.g. the pruning step (step 10 of alg 1) as a projection onto the l-0 norm ball. However, as (reasonably) referenced by the authors, analysis of the optimization problem lies outside the scope of the paper. 

Throughout the main text, there are many typos and grammatical errors. Although the draft is readable in its current form, I would suggest the authors carefully review the manuscript and improve the writing- e.g. the following are some examples:
- Now let’s comparing the covariance between…
- Intuitively, a large dataset of high-quality training samples diminishes concerns over gradient noise, making the empirical fisher a close approximation to the true fisher.
- Importantly, this seamless trade-off eludes the combination of the Euclidean distance with gradient averaging.
- Remark that LR is a special case of EWR…

### Questions
I may have missed it, but it is not obvious to me what kind of assumption is made regarding the noise. Additionally, it is unclear what kind of noise is introduced in the experiments. What kinds of noise can this method be a good choice for? What is an appropriate choice of the regularization weight for different kinds / magnitudes of noise?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reformulate the network pruning problem into an Wasserstein distance regularized sparse linear regression problem. The author shows that the ordinary sparse linear regression is just a special case when only diagnal entries exists in the transportation matrix. The authors also show that it can be viewed as neighborhood size control, which trade off between covariance capturing and gradient noise reduction. Numerical results show improvement on MLPNet, ResNet20 and MobileNetV1 architectures, over existing magnitude prunning or CVS approaches.

### Strengths
1. The reformulation is novel as far as I know. The author successfully connect the reformulation to existing sparse regression set up, which makes a good story here.
2. The analysis on neighborhood control is also insightful.

### Weaknesses
1. The experiments are weak, without test on state-of-the-art architectures like transformers, or larger models like ResNet50, making it suspicious that the proposed approach does not work well on larger model sizes.

### Questions
Why using 0.84, 0.74, 0.75, 0.63 ... values in Table 2 and 3? This is very uncommon and even in Table 1, the results are following traditional sparsity levels.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new network pruning method based on Wasserstein distance. Under the convex hull distance equality, the problem is reformulated using Neighborhood Interpolation. Under this formulation, the authors analyzed that compared to the traditional LR formulation, this method learned a data-adaptive gradient averaging weights to smooth noise in gradient estimation. An iterative optimization method is provided. Experiments on several backbones and datasets demonstrated the utility.

### Strengths
1. The noise corruption in gradient estimation considered in this paper is an interesting and important problem. 
2. The idea of leveraging Wasserstein distance, especially the reformulation through neighborhood interpolation in combating noise is interesting. 
3. The authors have conducted supportive experiments to validate the advantages. Particularly, I like Figure 9 which illustrates the distribution of learned $\Pi_t$ as the noise level varies. 
4. The paper is well-organized and written.

### Weaknesses
1. Is it possible to conduct a convergence analysis for algorithm 1? If it is difficult, does the main challenge lie in the simultaneous optimization of $\Pi_t$?
2. It would be more interesting to compare with more baselines, in addition to the LR method.

### Questions
Just to be curious, as the main contribution lies in better estimating the gradient under the existence of noise, is it possible to extend the proposed method to other applications beyond network pruning?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Computation of the empirical Fisher Information Matrix (FIM) is an important part of neural network pruning and subjected to 
noisy gradients. As a solution, this paper proposes an entropic Wasserstein regression (EWR) formulation to address the issue above. The method EWR is demonstrated to able to implicitly enacts gradient averaging using Neighborhood Interpolation, resulting in a balance in capturing gradient covariance and reducing gradient noise.  The paper demonstrates the proposed methods in combatting noisy gradients through theoretical analysis (section 3), and empirical evidence (section 4, 5). The empirical evidence is showcased using various models and vision datasets.

### Strengths
1. Provide clear motivation about combating against noise that may comes from different aspects. 
2. Provide theoretical analysis for the proposed method and empirical evidence.

### Weaknesses
1. Is it possible to show an analysis in term of computational expense incurred, as the scale of the model increases?

### Questions
1. Suggestion to change some of the cited references to be included in parentheses for better presentation. Eg in page 3 Computing the distance between .... (Nadjahi et al., 2020).
2. In the introduction, GPT-4 is used an example of model with substantial size and complexity, Is it possible to show case such a pruning in a language model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
