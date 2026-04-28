# Greedy PIG: Adaptive Integrated Gradients

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
Deep learning has become the standard approach for most machine learning tasks. While its impact is undeniable, interpreting the predictions of deep learning models from a human perspective remains a challenge. In contrast to model training, model interpretability is harder to quantify and pose as an explicit optimization problem. Inspired by the AUC softmax information curve (AUC SIC) metric for evaluating feature attribution methods, we propose a unified discrete optimization framework for feature attribution and feature selection based on subset selection.
This leads to a natural \emph{adaptive} generalization of the path integrated gradients (PIG) method for feature attribution, which we call Greedy PIG.
We demonstrate the success of Greedy PIG on a wide variety of tasks,
including image feature attribution, graph compression/explanation, and
post-hoc feature selection on tabular data.
Our results show that introducing adaptivity is a powerful and versatile method for
making attribution methods more powerful.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles feature attribution, which aims to explain model's decision on an input by assigning to each input feature a score showing their contribution. Different from previous work, the paper proposes to formulate it as a subset selection problem (Sec 2.2 and 3.2), i.e. select the optimal set of features that best explain the model's decision. Inspired by Path Integrated Gradients (PIG), the paper relaxes the objective set function to a continuous function on a path in the hypercube. The problem is then solved using Greedy PIG, an application of PIG in multiple rounds which selects a batch of features at a time to add to the optimal set.

The paper shows good performance compared to PIG-based baselines on feature attribution, GNN compression and feature selection on tabular data.

### Strengths
Explainability of deep neural networks is an important topic and the paper tackles an important task toward this goal. Casting feature attribution as subset selection is reasonable. 

The paper rightly points out that the correlation of features could lead to wrong attribution. The proposed Greedy PIG algorithm to address this issue seems to result in better performance than the baselines.

### Weaknesses
The link between subset selection formulation and Greedy PIG seems very weak. The path going from the formulation to the algorithm should be better clarified. In particular:
  - Why does Greedy PID maximize the objective function? The paper claims that formulating feature attribution as an optimization problem has advantages. But the proposed algorithm seems to be an extension of PIG and has nothing to do with maximizing the real object function. The algorithm computes an integral of the gradient along a path, not the gradient itself, and it is unclear why selecting the largest entries of this integrated gradient would lead to a better value of the objective function, especially since Lemma 4.3, which relates PIG scores to marginal gains, only applies when the base set S is empty. This analysis does not hold when some features are already selected, and the paper lacks a proof that the algorithm gradually increases the objective function.
  - Is the continuous objective function a submodular function? The paper seems to lean a lot on the submodularity of set functions to argue for the approximate optimality of Greedy PIG. The objective function is not proven to be submodular, and the connection to submodular optimization literature is therefore weak, making the support for the proposed adaptivity questionable.

The part of  why Greedy eliminates the effect of feature correlation needs clarification. Is there some mathematical evidence to support claims in paragraph "Why Greedy captures correlations"?

The analysis in Sec 4.2 needs clarification
  - Why is it good that attributions correlate with marginal gains at S=0? If marginal gains are what we want, why don't we directly use them? The paper argues that attributions are proxies for marginal gains, but it does not demonstrate why this approximation is necessary or beneficial. A direct comparison to a baseline using marginal gains would be more convincing.
  - The paper suggests that H_ij reflects the correlation between features i and j. Is ther any justification?
  - Lemme 4.4 needs a short proof. Also, it considers a very particular form of "feature redundancy". Is this kind of feature redundancy common in practice?

In general, the paper's writing needs major improvements.

### Questions
How does the performance depend on parameter z in Algorithm 1?
Function g in Eq. 7 is a typo? Another function g is mentioned earlier in Sec 3.3.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the problem of feature attribution as an explicit subset selection problem.  Realizing that the main drawback of the path-integrated gradient (PIG) algorithms is their limited ability to handle feature correlations, the authors propose a natural way to account for correlations by a greedy algorithm, i.e., the correlations between already selected variables with the rest of the unselected variables will be eliminated by the greedy selection strategy. Experiments on a wide variety of tasks, including image feature attribution, graph compression/explanation, and the post-hoc feature selection on tabular data demonstrate the effectiveness of the proposed method.

### Strengths
1. The authors connect feature attribution and feature selection with a unified discrete optimization framework based on subset selection.
2. Experiments on a wide variety of tasks, including image feature attribution, graph compression/explanation, and the post-hoc feature selection on tabular data demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The novelty of the proposed method is limited. By simply combining feature attribution and feature selection with a unified discrete optimization framework based on subset selection, the authors introduce limited insight into tackling this problem. Equation 7, which introduces the greedy selection, is a straightforward extension of Equation 1, lacking a substantial theoretical contribution or a novel perspective on the underlying problem. The core idea of iteratively selecting features based on integrated gradients, while intuitive, does not introduce a fundamentally new approach to feature attribution.
2. The proposed Greedy PIG may introduce a sub-optimal problem. By greedily selecting the top-attribution features computed by integrated gradients in each round, the proposed method cannot guarantee a global optimal solution for the feature attribution problem. The method's reliance on a greedy approach means that once a feature is selected, its influence on subsequent feature selections is not re-evaluated, potentially leading to a suboptimal set of features. Further, if seeking the global optimal solution for the feature attribution problem is not the goal of this submission, it may be better for the authors to demonstrate that a satisfactory solution will be attained by the proposed method, perhaps by providing a theoretical analysis of the approximation quality or empirical evidence of convergence to a stable solution.
3. This paper is not well-written, and more explanation is needed to deeply follow this paper. For example, "feature attribution, the softmax information curve (SIC) of Kapishnikov et al. (2019) can be recovered from (Eq. 3) by setting G(S) to the softmax output of a target class (see Eq. 4)." is quite confused. The connection between the proposed method and existing methods like SIC is not clearly explained, making it difficult to understand the advantages and limitations of the proposed approach. The paper lacks sufficient detail on how the proposed method relates to and improves upon existing feature attribution techniques.

### Questions
1.  A typo in the second paragraph of the introduction section: "on considers an entire dataset. For literature surveys, see (Zhang et al., 2021) for feature attribution and interpretability see and (Li et al., 2017) for feature selection."

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an improvement over Integrated gradients by advocating to make it adaptive. They do so by recursively taking the top-k attribution features, adding it to the current baseline, and recomputing the path gradients. The authors then show that their attribution method outperforms previous modifications to integrated gradients on several performance AUC metrics.

### Strengths
1. I like the idea of adaptively choosing the baseline in order to break the redundancies between features involved. However, I think this aspect of the paper has not been properly evaluated by the authors. I expand on this in the weakness section.

2. The proposed modification to integrated gradients outperforms previous methods in literature in AUC curves which show that their method chooses features that are more important for prediction than other attribution methods.

### Weaknesses
The motivation of this work is not adequately backed up with theory or experiments. Moreover the writing is weak making the paper hard to read. I would expand on this in the following points. 

1. The stated motivation for greedy PIG is to make the attributions more robust to feature correlations. However this aspect has never been explicitly evaluated in experiments. Lemma 4.4 is an attempt to theoretically justify why integrated gradients would fail when redundant features are present, however no proof is provided in the paper to evaluate the correctness of the statement. Moreover, it is not clear how greedy PIG solves the issue stated in Lemma 4.4. Clarifying this would further strengthen the motivations of this work.

2. The Proof of Lemma 4.3 is not clear. Why is the hessian bounded by K? What is the non-correlation property of g? What is \bar{H}. The authors say this is average on a path from w to w_{i}. What is the formulae for computing this average? how is the path computed? what is w_{I}. The details should be clarified to the reader. 

3. More generally, it is not clear to me what g is in the paper. Is it the neural network function f as in equation 1? Section 3.3 says this is a continuous extension that allows optimization of equation 3, however equation 3 is never optimized in their greedyPIG algorithm. It is unclear how the continuous relaxation g is used in practice, and how it relates back to the original function f.

4. For the experiments, what is the value of z, chosen for the greedy-PIG algorithm in each instance. An ablation study on the effect of z (the number of top-z features selected in each iteration) on the different metrics would be interesting as it would show the robustness of the method on the choice of z. If one would want to break correlations, is the ideal value z=1? 

5. It is not clear what is the Sequential Gradient, the authors refer to in this paper. Is it eq (1) evaluated at one single point instead of a discretization on N points? If yes, how is this point selected? how accurate is this estimation?

5. Please describe what the point game is in more detail. I understand it was proposed in an earlier paper, so I recommend this be added to the appendix. Otherwise it is not clear to the reader at all what is been shown. Is the network (that is explained) trained on a new dataset that includes images arranged in a 3x3 grid, or is it through the same network? If yes does it not affect the performance of the original network which was trained on clean imageS?  The statement "We generate 2x2 grids of the highest prediction confidence images, and obtain the attribution results for each class" is unclear. What does highest prediction confidence images mean? How are the attribution results obtained?

### Questions
Refer to the weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This research study bridges the gap between two domains of deep learning: attribution and feature selection. They propose a novel unified theoretical framework. The resulting method, although similar to previous work, uses feature selection in order to increase the robustness of the attribution evaluation. Their result show that the proposed Greedy PIG vastly outperforms some previous methods in terms of Softmax AUC and KL divergence AUC.

### Strengths
In my opinion, explainability and compression are of paramount importance in deep learning. In this paper, the authors show a limitation of existing methods. As a result, Greedy PIG is specifically designed to mitigate this issue and achieves remarkable results.

### Weaknesses
I have three concerns with this work as it stands.
1. The method is designed to perform well when evaluated using the Softmax AUC which is not the most commonly used metric (insertion and deletion scores are). How the Greedy PIG compare with other methods using these metrics?
2. A recent method IDGI [1] was introduced 
3. Although ConvNets are still popular, the study would strongly benefit from an evaluation on Transformers, e.g. ViT.

### Questions
On top of my previous concerns, I would like to ask if the authors could the authors share their code (at least on an example). I am intrigued by the difference in performance with GIG which in my understanding is very similar to the proposed method

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
