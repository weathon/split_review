# Escaping Saddle Point Efficiently in Minimax and Bilevel Optimizations

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Hierarchical optimization (including minimax optimization and bilevel optimization) is attracting significant attentions as it can be broadly applied to many machine learning tasks such as adversarial training, policy optimization, meta-learning and hyperparameter optimization. Recently, many algorithms have been studied to improve the theoretical analysis results of minimax and bilevel optimizations. Among these works, one of the most crucial issues is to escape saddle point and find local minimum, which is also of importance in conventional nonconvex optimization. In this paper, thus, we focus on investigating the methods to achieve second-order stationary point for nonconvex-strongly-concave minimax optimization and nonconvex-strongly-convex bilevel optimization. Specifically, we propose a new algorithm named PRGDA  via perturbed stochastic gradient which does not require the computation of second order derivatives. In stochastic nonconvex-strongly-concave minimax optimization, we prove that our algorithm can find an $O(\epsilon, \sqrt{\rho_{\Phi} \epsilon})$ second-order stationary point within gradient complexity of $\tilde{O} (\kappa^3 \epsilon^{-3})$, which matches state-of-the-art to find first-order stationary point. To our best knowledge, our algorithm is the first stochastic algorithm that is guaranteed to obtain the second-order stationary point for nonconvex minimax problems. Besides, in stochastic nonconvex-strongly-convex bilevel optimization, our method also achieves better gradient complexity of $Gc(f, \epsilon) = \tilde{O}(\kappa^3 \epsilon^{-3})$ and $Gc(g, \epsilon) = \tilde{O}(\kappa^7 \epsilon^{-3})$ to find local minimum. Finally, we conduct a numerical experiment to validate the performance of our new method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a stochastic first-order algorithm called PRGDA for nonconvex-strongly-concave minimax optimization. For bilevel optimization in particular, the authors prove convergence to a second-order stationary point with a gradient complexity of $O(\epsilon^{-3})$, which improves upon the previous best result in Huang et al. 2022, which achieved a complexity of  $O(\epsilon^{-4})$.

### Strengths
I think the main strength of this paper is a theoretical improvement of the gradient complexity, as I've summarized above.

### Weaknesses
While I think the theoretical result in this paper is interesting, there are a few reasons that prevent me from giving this paper a higher score.
- The overall presentation is not clear. Specifically, in sections 4 and 5 where algorithm 1 is introduced, the description is very dense and difficult to parse. The authors refer to quite a few previous algorithms such as SREDA, PiSARAH and SPIDER without actually giving a brief summary of what these algorithms do. Also missing from this section is a highlight of what makes PRGDA different from the previous SOTA method in Huang et al. 2022. It is not sufficient to simply state that PRGDA is a stochastic method with a perturbation; the specific mechanisms that allow it to achieve better complexity need to be clearly articulated. The lack of explanation makes it hard to understand the core algorithmic innovation.
- Another major weak point in the presentation is a lack of clearer comparison with prior work. In tables 2 and 3, it is unclear to me if most of these results are actually comparable, since I'm not sure if they use all the assumptions 1-5 in this paper. The assumptions used by each method should be explicitly stated in the tables. Furthermore, the related work is scattered throughout the whole paper, and many prior algorithms are named, but not described at all. Obviously the authors do not need to describe all prior work in detail, but I think it is important to highlight what makes PRGDA different from prior algorithms except from stochasticity and a simple perturbation. For example, it is unclear if the perturbation strategy is novel, or if it is a standard technique used in other algorithms.
- Section 6 is called convergence analysis, so i expected this section to include a discussion of the theoretical innovations of PRGDA that allows the authors to prove a better gradient complexity. However, there is no convergence analysis at all. Instead, only the two main theorems are stated, without any further explanation. This makes it hard to gauge how significant the theoretical guarantees are. For instance, in section 2.3 the authors claim that perturbed GD in the deterministic and stochastic settings are totally different. However, this is not the case at least in Jin et al. [1], where the proof for GD and SGD are quite similar. The analysis for GD and SGD might be more different in bilevel and minimax optimization, but I think it needs to be spelled out in more detail. The authors should elaborate on the challenges in extending the analysis from single-level optimization to the bilevel setting, and how PRGDA addresses these challenges.

### Questions
Please see the weaknesses section.

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
The paper proposes a new algorithm, PRGDA, that combines the ideas of LENA, a
first-order algorithm for escaping saddle points, and SREDA, a variance
reduction method for nonconvex-strongly-concave (NC-SC) minimax optimization.
The authors provide convergence guarantees for the proposed algorithm. For
stochastic NC-SC minimax optimization, this is the first first-order algorithm
to achieve second-order convergence, and it requires $\tilde{O}(\kappa^3
\epsilon^{-3})$ gradient complexity to find an $O(\epsilon, \sqrt{\rho
\epsilon})$ second-order stationary point. For stochastic NC-SC bilevel
optimization, it achieves $\tilde{O}(\kappa^3 \epsilon^{-3})$ and
$\tilde{O}(\kappa^7 \epsilon^{-3})$ gradient complexities for the upper and
lower level functions, respectively. Further experiments are conducted to show
the ability of the algorithm to find local minima instead of saddle points.

### Strengths
* The proposed PRGDA is the first first-order stochastic algorithm for NC-SC
  minimax optimization with a second-order convergence guarantee, and its
  complexity matches the best result for finding a first-order stationary
  point.

* For bilevel optimization, the new method improves upon the complexity of
  existing methods.

### Weaknesses
 * I suggest that the author motivate and discuss in the paper why, in minimax optimization, we aim to find the local minimum of the primal function in the first place. In minimization problems, this is natural. However, in games, we care about equilibria. For instance, [1] discussed the significance of the local minimax point in this area, while [2] mentioned that a second-order stationary condition implies a local minimax point (Fact 1). Nevertheless, the relationship between saddle points of the primal function and the local minimax point remains somewhat unclear to me. Do they not intersect at all? Why should we escape these saddle points? What happens in bilevel optimization?

* Although the work proposes the first first-order stochastic algorithm for NS-SC minimax optimization with second-order convergence and improves the complexity for bilevel problems, the techniques seem similar to existing methods, namely, LENA [3] and SREDA. Could the author elucidate the novelty in the algorithm design or proof techniques? Specifically, the adaptation of LENA's perturbation strategy and SREDA's variance reduction to the minimax setting needs more detailed explanation. How do these techniques interact, and what are the key challenges in combining them for this specific problem?

* Regarding the experiments, how did the author choose the hyper-parameters? Were these hyper-parameters optimized for each algorithm? While the sensitivity of StocBio + iNEON to hyper-parameters is discussed, I am curious about the fairness of the comparison. It is unclear if the reported performance differences are due to the algorithm itself or due to a suboptimal hyperparameter selection for the baselines. Furthermore, the discussion of batch size is vague; the exact batch sizes used for each method and how they were chosen should be clearly stated.

* Some claims appear unsound:
    - Theorems 1 and 2 should also include assumptions regarding noise. This is only mentioned in the appendix during the proof of these theorems. Additionally, the noise assumption (Equation 13) is not "bounded variance" but should be termed as bounded noise or bounded noise support, which is stronger than bounded variance. The implications of this stronger assumption should be discussed.
    - "PRGDA is the first algorithm that is guaranteed to obtain second-order stationary point for stochastic nonconvex minimax optimization problems." However, newer versions of the cited paper (Chen et al. (2021b)) introduce a stochastic version. This should also be reflected in Table 1; for instance, Cubic-GDA should be marked in the "Stochastic" field. The comparison should be updated to reflect the current state of the art.
    - Some references appear to be inaccurate, for example, "including intuitive methods SGDmax (Jin et al. (2019))", and "SGDmax (Jin et al. (2019)) is an intuitive double loop algorithm". These claims should be verified and corrected.

* Some notations either are not introduced or are only formally defined in later sections, such as:
    - "$Gc$" in the abstract.
    - "$\Phi$" is introduced early on but is only defined in section 3.
    - "SFO" is not defined. I assume it stands for "stochastic first-order oracle".
    - "$JV$" and "$HV$" in Theorem 2 are not defined.

### Questions
Could the author clarify the concerns in Weaknesses 1-3?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a perturbed stochastic gradient method for bi-level and minimax optimization. Crucially, the gradient complexity of their proposed methods (suppressing the condition number dependence) achieve \tilde{O}(\epsilon^{-3}) gradient complexity in order to find a second order critical point.  This seems to match the best gradient complexity known among stochastic methods converging just to a critical point.

### Strengths
The theoretical result is quite strong, polynomially improving upon the gradient complexity of the best known result (improving from \epsilon^{-4} to \epsilon^{-3}).  I appreciate the inclusion of condition number dependence in the results as well.  The example chosen for the numerical result is also quite illustrative and well chosen.

### Weaknesses
The main weakness is the presentation of the paper.  I provide a few (small) comments here.

Minor comments:

- The paper makes strong smoothness assumptions (which do seem to be standard in the literature), but it would be useful to include references to methods which do not require such strong assumptions, such as Chen, et. al (https://arxiv.org/pdf/2306.12067.pdf).  

- There are several small issues riddled throughout that should be resolved before publication.  To give one such example (among several), Assumption 2 is not quite precise: There should be a quantifier on \xi, \zeta (e.g. I suppose this should hold for almost every \xi and \zeta).

- The authors never define HV and JV as stated in Theorem 2.  I assume these are the number of required Hessian and Jacobian vector products.

- The description of the algorithm is fairly difficult to follow.  I would recommend moving the second empirical result on hyper-representation learning to the appendix and perhaps using the extra space to more clearly explain the algorithm.

### Questions
1. This question is a bit broader than the scope of the paper, but answering it would help quite a bit in terms of clarity.  The authors mention a lower bound of Zhang et. al (2021) which is achieved for deterministic algorithms by Lin, et. al (2020b).  Could the authors clarify the situation on the lower bound in the specific setting they consider? E.g. with the smoothness assumptions imposed by Assumptions 2, 3 and strong convexity Assumption 1, are there known results for lower bounds on reaching a second order stationary point as considered here? It is interesting to improve upper bounds as done in this paper, but some guidance on lower bounds would either (i.) situate and clarify the results quite a bit if known or (ii.) strengthen the results significantly if not known. 

2. Regarding the numerical experiments, the trajectory of the proposed algorithm exhibits some interesting behavior which would be nice to clarify.  In particular, should the reader interpret the flat regions (e.g. Figure 1.(a) iterations 10^{4} – 2\cdot 10^{4}) as while the algorithm is trying to escape from a bad critical point? Moreover, there seem to be distinctions in the convergence behavior in the different phases.  It is a bit hard to tell, but the proposed method seems to enjoy linear convergence to the first critical point and thereafter sublinear convergence behavior (with different rates of convergence, for instance at iterate 4*10^{4} in Figure 1.(a)).  Could the authors clarify this a bit?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
