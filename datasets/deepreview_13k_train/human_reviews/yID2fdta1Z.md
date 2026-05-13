# Robust Graph Neural Networks via Unbiased Aggregation

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
The adversarial robustness of Graph Neural Networks (GNNs) has been questioned due to the false sense of security uncovered by strong adaptive attacks despite the existence of numerous defenses.
In this work, we delve into the robustness analysis of representative robust GNNs and provide a unified robust estimation point of view to
understand their robustness and limitations.
Our novel analysis of estimation bias motivates the design of a 
robust and unbiased graph signal estimator. 
We then develop an efficient Quasi-Newton Iterative Reweighted Least Squares algorithm to solve the estimation problem, which is unfolded as robust unbiased aggregation layers in GNNs with theoretical guarantees.
Our comprehensive experiments confirm the strong robustness of our proposed model under various scenarios, and the ablation study provides a deep understanding of its advantages.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper provides some analysis of the robustness of various GNNs and present a unified perspective to understand their strengths and limitations.  The paper identifies an issue with estimation bias in $\ell_1$-based robust graph smoothing and proposes a robust and unbiased graph signal estimator to address this bias. The Quasi-Newton IRLS algorithm is introduced, which can be integrated into GNNs as feature aggregation layers.

### Strengths
1. The paper provides some analysis of the robustness of various GNNs, offering valuable insights into their performance under adversarial attacks.

2.  The introduction of the Quasi-Newton IRLS algorithm, which can be integrated into GNNs as feature aggregation layers, is both innovative and practical.

### Weaknesses
1. The paper's central claim regarding the estimation bias introduced by $\ell_1$-based robust estimation lacks sufficient theoretical and empirical support. The assertion that this bias significantly degrades model performance, particularly under heterophilic edge attacks, is not rigorously proven. The numerical simulations, while illustrative, raise several concerns:

- The rationale for designating certain data points as "outliers" is unclear and appears arbitrary. A more rigorous definition of outliers within the context of the Gaussian distribution used for sample generation is needed.

- The behavior of the estimation in the third plot, where a large portion of data is labeled as outliers, warrants further investigation. The persistence of the estimation at the center of the "clean" samples suggests the influence of factors not adequately addressed in the paper. It is premature to attribute this behavior solely to the proposed method's effectiveness.

- The proposed method provides a simplified approximation of a single step in GNN aggregation. Even if the numerical example were entirely valid, it does not convincingly demonstrate the robustness of the method within the broader context of GNNs. The claim that single-step gradient descent aligns with the theoretical guarantees requires more rigorous justification, especially considering the variability of $W^k$ across different layers.

2. The derivation of $W$ in eq(7) is not clearly explained. A more detailed explanation of its computation is necessary for a thorough understanding of the proposed method.

3. The statement "which not only provides clear interpretability but also covers many classic GNNs as special cases" is an overstatement. The term "covers" is inaccurate in this context. The paper does not fully encompass classic GNNs as special cases but rather offers an approximate perspective on them through the lens of Graph Signal processing. This distinction should be clarified.

4. The paper does not adequately address the limitations of the proposed method. The method's applicability might be restricted to datasets that inherently assume homophily, similar to other defense mechanisms that prune heterophilic edges. This limitation should be explicitly acknowledged and discussed.

5. The lack of reported computational costs is a significant omission. Without this information, it is difficult to assess the practical feasibility of the proposed approach in real-world scenarios.

6. The experimental section is insufficient, particularly regarding the range of attacks considered. A more comprehensive evaluation should include poison and evasion attacks, white-box and black-box scenarios, and both injection and modification types.

### Questions
1. Can you address and provide clarity on the concerns highlighted in the weaknesses section?
2. The citation style throughout the manuscript is inconsistent. Can you rectify this?

### Soundness
2 fair

### Presentation
3 good

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
The authors propose a unifying perspective on three "successful" graph defenses against adversarial structure perturbations. They argue that all models are instances of the so-called ElasticGNN. Moreover, the authors propose a practical optimization algorithm for the devised non-smooth objective that can approximate an L1 estimator. The resulting GNN-layer is called RUNG. The authors provide empirical evidence regarding the efficacy of their method - especially for large perturbation budgets.

### Strengths
1. Unified perspective on effective and established defenses
2. New optimization approach for an ElasticGNN derivative
3. Method shows strong empirical performance, especially for large perturbation budgets
4. The authors evaluate their defense using adaptive attacks and study the transferability of the perturbations between models

### Weaknesses
1. Empirical evaluation only using Cora ML and Citeseer is insufficient. Consider larger graphs like ogbn-arxiv as well. The current evaluation is limited to relatively small datasets, which may not fully capture the scalability and robustness of the proposed method on more complex graph structures. Specifically, the performance on graphs with significantly more nodes and edges, such as those found in the ogbn-arxiv dataset, could reveal potential limitations not apparent in smaller datasets.
1. Computational complexity and cost are neither discussed nor evaluated. The paper lacks a detailed analysis of the computational resources required by the proposed RUNG method. This includes both time and memory complexity, which are crucial for assessing the practical applicability of the method, especially on large-scale graphs. A comparison with the computational cost of baseline methods would also be beneficial.
1. The authors should provide an ablation study on how the design choices affect the performance. The paper does not sufficiently explore the impact of various design choices on the overall performance of RUNG. For example, the effect of different penalty functions, the choice of optimization algorithm (IRLS vs QN-IRLS), and the influence of hyperparameters such as \(\gamma\) and \(\lambda\) are not thoroughly investigated. A detailed ablation study is needed to understand the contribution of each component.
1. The authors should show that their method breaks. For example, complement Figure 2 with a setting where the method fails. The paper lacks an analysis of the limitations of the proposed method. Specifically, it would be beneficial to explore scenarios where the method fails or performs poorly. This could be achieved by extending the simulation in Figure 2 to include cases with higher outlier ratios, beyond the breakdown point of the estimator, to demonstrate the boundaries of the method's robustness.
1. The authors state "The simulation in Figure 2 verifies that our proposed estimator (η(x) := ργ(∥x∥2)) recovers the true mean regardless of the increasing outlier ratio." Which is somewhat misleading since the asymptotically optimal breakdown point of a location estimator is 50% (under certain assumptions, e.g., without constraining the value range of the estimation). The claim that the estimator recovers the true mean regardless of the outlier ratio is inaccurate. While the estimator may perform well under certain conditions, it is crucial to acknowledge the theoretical limitations of location estimators, particularly their breakdown point. The statement should be revised to reflect these limitations more accurately.

Minor:
1. It would be interesting to see how the perturbations of RUNG transfer to the other defenses as well
1. Section 2.2 could benefit from some notes on the composition of multiple GNN layers
1. The dimension-wise median, is differentiable almost everywhere (similarly to sorting). There are only differentiability issues if the "center element" changes.

### Questions
1. Can the authors elaborate more on how the model behaves if the perturbation strength is very high? I.e., does the model then effectively become an MLP?
1. How does RUNG defy the breakdown point?
1. 10 layers of "graph smoothing" seems to be a lot! How does RUNG perform with fewer steps (e.g. as low as 2-3 as commonly used on Cora/Citeseer)?

I am willing to raise the score if the questions are being resolved and the empirical evaluation is improved (see above).

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes the robust GNN models including SoftMedian, TWIRLS, and  ElasticGNN from a unified view of robust estimation. Building on this analysis, the authors introduce a robust unbiased aggregation method, further developing an efficient Quasi-Newton iterative reweighted least squares algorithm. However, the empirical validation seems somewhat limited, confined to two small graphs and a single attack setting.

### Strengths
The paper provides a unified view of $l_1$-based robust graph signal smoothing for three robust GNNs.

It introduces an unbiased graph signal estimator, which is unfolded into feature aggregation layers, aiming to enhance the robustness of GNNs.

### Weaknesses
1. The definition of $l_1$-based graph smoothing is not clear. The MCP function $\rho_\gamma$ used in Equation 4 and Equation 7 is not defined.

2. The paper does not provide an analysis of the computational complexity of RUNG, leaving its efficiency and applicability to larger datasets, such as Ogbn[1], unclear. Additionally, numerical experiments are limited, being only applied to Cora-ML and Citeseer datasets. It would be beneficial to see how RUNG performs on larger-scale datasets.

3. The description of the attack setting in Section 4.1 lacks clarity. Could you provide more details on how the adaptive evasion attack is designed based [2] you referenced? Specifically, what type of perturbations are performed during the attack - are they feature perturbations, graph topology perturbations, or both?

4. The robustness validation of RUNG in the paper is notably insufficient, solely relying on the PGD attack.
A comprehensive assessment using various attacks, as detailed in references [3][4][5][6], is necessary for a credible demonstration of RUNG's robustness.

5. Implementation code was not provided.

### Questions
How to calculate the derivative in the $W_{ij}^{(k)}$ of Equation (7)?

The hyperparameter of $\lambda$ and $\gamma$  appears crucial in the model. Could you provide an ablation study to demonstrate the impact of varying these values? It would be insightful to understand how sensitive the performance of RUNG is to the selection of  $\lambda$ and $\gamma$.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a robust model (RUNG) based on unbiased aggregation. Specifically, the authors first unify a few robust GNNs through the lens of $l_1$-based graph smoothing, while they still suffer from accuracy degradation when subjected to large attack budgets. To build a robust model against attacks with a large budget, authors introduce a robust and unbiased estimator by minimizing an objective function with a minimax concave penalty. Subsequently, an efficient Quasi-Newton iterative algorithm is used to optimize the objective function, from which RUNG is derived. Experimental results demonstrate that RUNG outperforms the baseline (defense) GNNs on CoraML and Citeseer, under most attack settings.

### Strengths
- Overall, the paper is well-written.
- The unified view of robust estimation on prior GNNs is interesting.
- Authors have considered adaptive attacks.

### Weaknesses
 - The proposed method relies on a strong assumption of graph homophily, raising concerns about the performance of RUNG on heterophilic datasets. Thus, conducting additional experiments on heterophilic graphs is necessary. Otherwise, authors should explicitly discuss this limitation in the manuscript. Furthermore, the claim that defense of GNNs on heterophilic graphs is largely unexplored is not accurate, as several prior studies, such as GNNGuard and GARNET, have explicitly addressed this setting.
- Authors leverage QN-IRLS to approximate the inverse Hessian matrix to address the scalability issue. However, the experiments are only conducted on two small graphs, making it unclear whether the proposed approach would still work on large graphs. The paper lacks a thorough analysis of the computational complexity of the proposed method, and the empirical evaluation does not include experiments on larger datasets to demonstrate scalability.
- The accuracy improvement under small attack budgets is less convincing. For instance, the accuracy gap between RUNG and the runner-up model is often smaller than the standard deviation, as observed under local attacks with a 20% budget on CoraML. My concern is that RUNG might underperform the baselines with a new random seed, considering that the authors obtained averaged accuracy using only 5 different random splits. The paper should provide more evidence to support the robustness of RUNG under small attack budgets, possibly by increasing the number of random splits or providing statistical significance tests.
- Authors have not performed sensitivity analyses on critical hyperparameters such as $\lambda$ and $\gamma$. It's unclear how these hyperparameters affect the performance of RUNG. The paper should include a detailed analysis of how the performance of RUNG varies with different values of these hyperparameters, and provide guidance on how to select appropriate values for different datasets and attack scenarios.
- Some recent defense models (e.g., [1, 2, 3]) are not compared in this work. The paper should include a more comprehensive comparison with recent state-of-the-art defense methods, particularly those that have demonstrated strong performance in similar settings. It is not sufficient to claim that some of these methods are similar to existing baselines without empirical verification.
- Typo: the runner-up model is SoftMedian rather than RUNG-$l_1$ under the 5% attack budget in Table 2.

### Questions
- What is $\beta$ in Section 2.3? I would suggest authors to use another notation, since $\beta$ has been used for SoftMedian.
- How do authors perform adaptive PGD attack on Jaccard-GCN, which preprocesses the adjacency matrix?
- Authors mention SVD-GCN as one of the baselines. Where are the results of SVD-GCN?
- It's unclear to me whether the defense under large attack budgets is practical. Is there any realistic application/scenario where an attacker can largely perturb the graph structure?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper reviews the estimation bias of several representative GNNs. It proposes a quasi-Newton iterative reweighted LS algorithm to optimize a GNN model, whose loss is based on the minimax concave penalty. This penalty alleviates the bias in typical GNN models and is also more robust.

### Strengths
The paper proposes a quasi-Newton iterative reweighted LS algorithm to optimize a GNN model, whose loss is based on the minimax concave penalty. This penalty alleviates the bias in typical GNN models and is also more robust.

### Weaknesses
1. The paper is not well-written, with notations that are not always defined. E.g., the superscript (0) first appears in eq. (1) but has never been defined. In addition, the paper uses a strange definition of $\ell_1$ norm to mean either the usual 1-norm or the 2-norm. The $\ell_2$ "norm" in this paper is defined to be the square of the usual 2-norm. This is technically not a norm! The inconsistent use of notation and non-standard definitions make it difficult to follow the technical details and could lead to misinterpretations of the proposed method. The lack of precise definitions for key terms like the superscript (0) and the redefinition of $\ell_1$ and $\ell_2$ norms are significant issues that need to be addressed for clarity and correctness.

2. The contributions are weak as the formulation is essentially based on TWIRLS with the MCP penalty by Zhang, 2010. Robustness issues in Lasso regression have also been well-studied. The paper doesn't adequately highlight the novelty of applying the MCP penalty in the context of GNNs, especially given its prior use in TWIRLS. The connection to existing work on robust Lasso regression is also not sufficiently explored, potentially missing opportunities to leverage existing theoretical results or provide a more rigorous analysis of the method's properties. The paper needs to clearly differentiate its contributions from the existing literature on TWIRLS and robust Lasso regression to establish its significance.

3. Most of the cited works are from 2021 or before. The authors are missing recent GNN robustness works like “On the robustness of graph neural diffusion to topology perturbations", NeurIPS 2022 and “Graph-coupled oscillator networks", ICLR 2022. The lack of engagement with more recent literature on GNN robustness raises concerns about the paper's awareness of the current state of the field. The absence of comparisons with state-of-the-art methods limits the evaluation of the proposed method's performance and its practical relevance. A more comprehensive literature review and comparison with recent advances are necessary to demonstrate the paper's contribution to the field.

4. The experiments are limited with tests only on Cora and CiteSeer. Attacks like TDGIA and MetaGIA are not considered. The evaluation is not comprehensive, as it only uses two datasets and does not include more sophisticated attacks. This limited experimental setup raises concerns about the generalizability of the results and the robustness of the proposed method under different attack scenarios. Expanding the experimental evaluation to include more datasets and attack methods is critical to validate the method's effectiveness and robustness.

### Questions
1. A quasi-Newton optimization approach is proposed. Is this related to standard quasi-Newton optimization procedures like BFGS, Broyden, etc.?

1. RUGE is claimed to be unbiased. Is this true and is it proven? An analytical robustness measure is also not provided.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
2 fair
