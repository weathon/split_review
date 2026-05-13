# Linear Partial Gromov-Wasserstein Embedding

- Decision: Accept
- Scores: 8, 6, 6, 6, 8

## Abstract
The Gromov–Wasserstein (GW) problem, a variant of the classical optimal transport (OT) problem, has attracted growing interest in the machine learning and data science communities due to its ability to quantify similarity between measures in different metric spaces. However, like the classical OT problem, GW imposes an equal mass constraint between measures, which restricts its application in many machine learning tasks. To address this limitation, the partial Gromov-Wasserstein (PGW) problem has been introduced, which relaxes the equal mass constraint, enabling the comparison of general positive Radon measures. Despite this, both GW and PGW face significant computational challenges due to their non-convex nature. To overcome these challenges, we propose the linear partial Gromov-Wasserstein (LPGW) embedding, a linearized embedding technique for the PGW problem. For $K$ different metric measure spaces, the pairwise computation of the PGW distance requires solving the PGW problem $\mathcal{O}(K^2)$ times. In contrast, the proposed linearization technique reduces this to $\mathcal{O}(K)$ times. Similar to the linearization technique for the classical OT problem, we prove that LPGW defines a valid metric for metric measure spaces. Finally, we demonstrate the effectiveness of LPGW in practical applications such as shape retrieval and learning with transport-based embeddings, showing that LPGW preserves the advantages of PGW in partial matching while significantly enhancing computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
The authors propose the linear partial Gromov-Wasserstein (LPGW) embedding, a linearization technique for the PGW problem. Theoretically, they prove that LPGW admits a metric with certain assumptions, and numerically, they demonstrate that the utility of the proposed LPGW method in shape retrieval and learning with transform-based embedding tasks. They illustrate that the LPGW- based method can preserve the partial matching property of PGW, while significantly improving computational efficiency.

### Strengths
1. The paper is well organized and easy to follow.
2. The paper contains many details, which is very helpful for understanding.
3. The experiment is promising, justifying theoretic part.

### Weaknesses
1. The paper, though overall well motivated, is mostly combining existing methods and theoretical novelty is limited, with discussions following from the the original ideas and definitions of linearized/partial GW/OT. A further question: what if TV is replaced by a general divergence for unbalanced formulation as in [1]? Specifically, the core idea of using a linear embedding to represent the displacement between measures, while effective, is a direct extension of the linearized optimal transport framework. The adaptation to the partial setting, while non-trivial, primarily involves incorporating mass creation/destruction, which conceptually follows from the partial OT literature. The paper does not explore alternative divergences beyond total variation (TV) for the unbalanced formulation, which could lead to different properties and potentially better performance in certain applications. For instance, using a Kullback-Leibler (KL) divergence might offer a more natural fit for probabilistic interpretations, and exploring such alternatives would strengthen the contribution.


2. Discussion of related works: the term "linearization" is from the tangent structure of gauged GW space as is first pointed out in [2]. Mapping based unbalanced GW formulations are also studied in [3],[4]. The paper should more clearly distinguish its contributions from existing work on unbalanced GW, particularly those that utilize mapping-based approaches. The current discussion does not fully capture the nuances of these methods, and a more detailed comparison would be beneficial. For example, how does the proposed method compare to approaches that directly learn mappings between measures in the unbalanced setting, in terms of computational complexity and performance?


3. Minor comment: 
If the barycentric LGW is the version to use as in the second equality of (10), then this should be stated in the paper. Notation $\gamma^1\wedge\gamma^2$ on line 260 seems to be incorrect and should be $\inf_A \gamma^1(A\cap E)+\gamma^2(A^C\cap E)$.

### Questions
I am not an expert in this area.

### Soundness
4

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
This paper studies the linear partial Gromov-Wasserstein (GW) alignment problem. Specifically the paper extends ideas from linearized GW and partial GW, and combines them to LPGW which inherits the merits of both method and is applicable to wider tasks. To formulate, the paper gives detailed account for how to incorporate general measure instead of probability measures, and how to coordinate different marginals. Extensive numerical experiments are presented, showcasing better performance.

### Strengths
The paper is well motivated and the study of the proposed formulation is very thorough, covering both general and special cases under suitable assumptions. The proposed algorithm combines the advantages from both partial GW and linearized GW, and extensive experiments supports this extension.

### Weaknesses
I believe that the paper is of a limited novelty. Indeed, both the linearized GW problem and the partial GW problem have appeared in previous works. Combining these two approaches to obtain a linearized partial GW problem appears to be incremental progress on the important question of efficient computation for the GW problem.

Furthermore, the theoretical properties of the LPGW problem appear quite limited. Many of the results require the existence of a Monge map for the PGW problem, but sufficient conditions for these assumptions to hold are not discussed in the main text. This assumption is quite strong and, as such, these results appear to be of a limited applicability.  Specifically, the reliance on a Monge map for Proposition 3.1(2,3,4) and Theorem 3.2(3) is a significant limitation, as it restricts the scope of these results to scenarios where such a map is guaranteed to exist, which is not always the case in practical applications. The paper would benefit from a more thorough discussion of the implications of this assumption and potential alternatives when it does not hold.

The approximated LPGW is, in practice approximated as (20). This appears to be a very coarse approximation in general; no justifications are provided for when this might be a reasonable approximation. The connection between the theoretical LPGW distance and its practical approximation in Equation (20) is not sufficiently justified. The paper should provide a more detailed analysis of the approximation error introduced by this simplification, including conditions under which the approximation is accurate and bounds on the error.

Finally, the experiments do not present any significantly new applications. The experiments in 4.1 and 4.2 are essentially the same as those from (Beier et al., 2022) the experiment in 4.3 is similar to that  from S. Nieter, R. Cummings, Z. Goldfeld, Outlier-Roubust Optimal Transport: Duality, Structure, and Statistical Analysis, AISTATS 2022. The main distinction is that a random rotation is performed on the dataset in the current paper, but this appears a bit contrived in the setting of MNIST.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a modification of a variant of the Gromov-Wasserstein (GW) distance, known as the Partial GW (PGW) problem,  which enables to compare gauged measure (gm) spaces whose measures have different total masses. The modification consists of applying the linearization strategy proposed in (Beier et al., 2022) to the PGW problem, yielding the so-called Linear PGW discrepancy (LPGW). It is shown that if the PGW problem admits a solution that is induced by a deterministic map, then the LPGW problem recovers the PGW problem. For the purposes of computation, an approximated LPGW problem is considered. The paper concludes with some numerical experiments which exhibit the empirical performance of the proposed approach.

### Strengths
The paper is, in my opinion well-written, and the theoretical findings appear correct. In the experiments, the LPGW algorithm compares favorably to the other approaches considered.

### Weaknesses
1. The equivalence between LGW and GW (Proposition 2.1) and between LPGW and PGW (Proposition 3.1) critically relies on the existence of a Monge mapping. However, proving the existence of such a mapping for the GW problem requires satisfying strict conditions [A]. This raises concerns about the robustness of these approximations in practical scenarios where Monge mappings may not exist. The paper would benefit from 
    - providing theoretical bounds on the approximation error when a Monge mapping does not exist;
    - including empirical experiments comparing performance on datasets known to violate Monge mapping conditions;
    - discussing potential modifications to make the method more robust when Monge mappings do not exist.
  
2. The computational implementation of LPGW relies on two layers of approximations. First, the authors approximate LPGW using aLPGW, as introduced in Equation (18). Then, Equation (20) further approximates the aLPGW formulation. However, the paper lacks both theoretical guarantees and empirical evaluation of the error introduced by these sequential approximations. It would be beneficial if the authors could
    - provide theoretical error bounds for each approximation step;
    - include ablation studies quantifying the empirical error introduced at each approximation stage;
    - discuss the tradeoffs between computational efficiency and approximation accuracy.
  
3. The paper primarily compares LPGW with PGW and LGW. However, other GW approximation methods could offer meaningful insights into the strengths and weaknesses of LPGW. Notably, comparisons with Low-Rank GW [B] and Sliced GW [C] could demonstrate whether LPGW provides any unique computational or approximation advantages.

### Questions
1. Many results in the paper depend on the assumption that a Monge map exists. Can the authors comment on sufficient conditions for such a result to hold?

2. Proposition 3.3 holds when $\lambda$ is sufficiently large. Can the authors clarify this condition further in the main text? Moreover, if $\lambda$ is too large, the regularizer dominates so there appears to be some tradeoff in terms of minimizing the first part of the objective. 

3. In the numerical experiments, in the experiments on MNIST, it seems that PGW would offer the best comparison (vs LOT and LGW which do not account for noise). Could these results be included?

4. I believe that the robustness to noise is the most interesting feature of the PGW formulation. I would recommend that this be addressed more clearly in the text.

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
3

### Summary
This paper introduces the Linear Partial Gromov-Wasserstein (LPGW) embedding, a computationally efficient approximation of the Partial Gromov-Wasserstein (PGW) problem, which relaxes mass constraints for comparing measures across different metric spaces. By reducing the pairwise complexity from $\mathcal{O}(K^2)$ to $\mathcal{O}(K)$, LPGW preserves the partial matching capabilities of PGW while enhancing scalability. The authors provide theoretical guarantees and validate LPGW through experiments in shape retrieval and transport-based learning tasks.

### Strengths
1. The paper is well-written and easy to follow.
  
2. The authors introduce the Linear Partial Gromov-Wasserstein (LPGW) embedding, which addresses the computational challenges of PGW. They also provide a formal proof of the equivalence between LPGW and PGW under the PGW-Monge mapping assumption, contributing to the theoretical foundation of the method.
  
3. The paper presents a method to approximate LPGW efficiently, reducing computational overhead. Furthermore, the authors conduct extensive numerical experiments to demonstrate the effectiveness and computational advantages of LPGW.

### Weaknesses
The authors claim that given K metric measure spaces, their algorithm can compute the distance between them in O(K) time. This claim was not supported with a time-complexity analysis and therefore remains unsubstantiated. It would strengthen the paper significantly to add a dedicated section, if even a small one, to prove the time-complexity (perhaps space-complexity if there's a tradeoff). Lastly, I believe the authors did not provide sufficient explanations for their experiments. For example, the simulation on the MNIST dataset, no clarifications are given on the details of training. For example, the authors state they will use a logistic regression for classification; this model is meant for binary classification and does not simply work on categorical cases. How exactly did they use logistic regression to predict classes when they range from 0-9? Furthermore, does this work with other models such as neural networks? It is always encouraged to be as specific as possible for reproducibility.

### Questions
1. Could the authors extend the approximation results for LGW and LPGW to scenarios where the Monge mapping may not exist?
  
2. Could the authors provide empirical or theoretical results on the error introduced by the two layers of approximation? Specifically, how much error is accumulated when transitioning from LPGW to aLPGW (Equation (18)) and then from aLPGW to the final approximation (Equation (20))?
  
3. Proposition 3.1 (3) provides a result when the cost function $g_Y$​ is an inner product. Could this result be extended to the case of squared Euclidean distance with additional assumptions? This would be relevant since [A] also explores the existence of Monge mappings under squared Euclidean costs.
  
4. In the elliptical disks experiment, the choice of reference space has a significant impact on performance. Could the authors provide practical guidance or heuristics for selecting reference spaces to optimize the performance of LPGW?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors of this paper aim to improve on the partial Gromov-Wasserstein (PGW) method by creating linear partial Gromov-Wasserstein (LPGW) embedding. They begin the paper with a succinct coverage of optimal transport (OT). They further begin with covering the 2-Wasserstein distance, a common choice for OT-based methods, and proceed to lay out the fundamentals of the Gromov-Wasserstein (GW) distance. Next, the authors give a breakdown of the linear embedding technique, linear Gromov-Wasserstein (LGW). The mass constraint on OT methods motivated the creation of partial Gromov-Wasserstein, or PGW. Similar to the linearization of GW, the authors introduce the linearization of PGW through known techniques such as approximations; their work was further inspired by the need of having a faster solution for computing the distance between K different metric spaces. The authors claimed their algorithm can improve computing the PGW distances between K metric measure spaces from O(K^2) to O(K). While the authors have done a great job with the mathematical formulations, they have not provided a time-complexity analysis to back up their statement. Lastly, I believe the authors did not provide sufficient explanations for their experiments. For example, the simulation on the MNIST dataset, no clarifications are given on the details of training. For example, the authors state they will use a logistic regression for classification; this model is meant for binary classification and does not simply work on categorical cases. How exactly did they use logistic regression to predict classes when they range from 0-9? Furthermore, does this work with other models such as neural networks? It is always encouraged to be as specific as possible for reproducibility.

### Strengths
The paper mathematically backs up their introduction of the linear partial Gromov-Wasserstein embedding algorithm. They also clearly demonstrate how previous work led to their contributions by breaking down and introducing each step along the way.

### Weaknesses
The authors claim that given K metric measure spaces, their algorithm can compute the distance between them in O(K) time. This claim was not supported with a time-complexity analysis and therefore remains unsubstantiated. It would strengthen the paper significantly to add a dedicated section, if even a small one, to prove the time-complexity (perhaps space-complexity if there's a tradeoff).

### Questions
Can you provide a time-complexity analysis to support your claim on a linear computation of the distances between K metric measure spaces?

### Soundness
3

### Presentation
3

### Contribution
4
