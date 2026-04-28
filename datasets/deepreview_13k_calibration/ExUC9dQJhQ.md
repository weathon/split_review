# Certified Robustness to Data Poisoning in Gradient-Based Training

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5

## Abstract
Modern machine learning pipelines leverage large amounts of public data, making it infeasible to guarantee data quality and leaving models open to poisoning and backdoor attacks. Provably bounding model behavior under such attacks remains an open problem. In this work, we address this challenge by developing the first framework providing provable guarantees on the behavior of models trained with potentially manipulated data without modifying the model or learning algorithm. In particular, our framework certifies robustness against untargeted and targeted poisoning, as well as backdoor attacks, for bounded and unbounded manipulations of the training inputs and labels.
    Our method leverages convex relaxations to over-approximate the set of all possible parameter updates for a given poisoning threat model, allowing us to bound the set of all reachable parameters for any gradient-based learning algorithm. 
    Given this set of parameters, we provide bounds on worst-case behavior, including model performance and backdoor success rate. We demonstrate our approach on multiple real-world datasets from applications including energy consumption, medical imaging, and autonomous driving.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper attempts to provide provable guarantees on the behaviour of models trained with potentially manipulated data without modifying the model or learning algorithm. The method uses convex relaxations to over-approximate the set of all possible parameter updates for a given poisoning attack, and provide bounds on worst-case behaviour.

### Strengths
The paper proposes a framework, with a (claimed to be novel) bound propagation strategy, for computing bounds on the
influence of a poisoning adversary on any model trained with gradient-based methods,  from the above, a series of proofs are suggested to bound the effect of poisoning attacks, finally, empirical evaluation are proposed to illustrate the approach.

### Weaknesses
While I might have missed the rationale for computing the set of all reachable trained models given how loose such (worst-case) bounds can be, the approach seems to claim novelty while overlooking important previous contributions, in particular, the use of influence functions in robust statistics, and their revival in modern machine learning.

Cook, R. D. Detection of influential observation in linear regression. Technometrics, 19:15–18, 1977.

Cook, R. D. Assessment of local influence. Journal of the Royal Statistical Society. Series B (Methodological), pp. 133–169, 1986.

Cook, R. D. and Weisberg, S. Characterizations of an empirical influence function for detecting influential cases in regression. Technometrics, 22:495–508, 1980.

Cook, R. D. and Weisberg, S. Residuals and influence in regression. New York: Chapman and Hall, 1982.

Koh, P.W. and Liang, P., 2017, July. Understanding black-box predictions via influence functions. In International conference on machine learning (pp. 1885-1894). PMLR.

### Questions
My main question would be on how this approach compares (in terms of computing the exact influence of a poisoned dataset) to the finer analysis in the references provided above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This submission considers the problem of providing provable robustness guarantees to training-time adversarial attacks. Specifically, the considered perturbation models admits changes to a constrained number of $n$ feature vectors and $m$ labels, with optional constraints on their norm. The adversary's objective is to perform a succesful targeted or untargeted poisoning attack, or a backdoor attack.  
Unlike prior work, the authors propose to generalize existing convex relaxation based methods for neural network verification to (1) determine a reachable set of model parameters at training time and (2) at inference time determine a reachable set of model outputs given this parameter sets.  
The reachable set of model parameters is iteratively expanded with each gradient step.
Given the perturbation model and bounds from the previous iteration, lower and upper bounds for the gradients are determined via convex relaxation while (1) considering worst-case choices of inputs and parameteers for $max(m,n)$ inputs and (2) worst-case choices of parameters for the remaining inputs.  
The strength of the resultant bounds for different perturbation model parameters are evaluated by training a model from scratch on a simple regression dataset and dimensionality-reduced MNIST, as well as fine-tuning on two other vision datasets.

### Strengths
* This submission proposes a novel solution to an extensively studied problem (susceptibility to training-time attack), which has received renewed attention due to the current excitement around language models.
* The problem is well-motivated via references to prior work on poisoning attacks.
* The method is clearly distinguished from prior aggregation-based approaches.
* The idea of applying iterative reachability analysis to SGD is very natural. It is somewhat surprising that no one has tried this ansatz before, i.e., the work closes a very obvious gap in existing literature.
* Rather than proposing a completely new relaxation approach, the work expands the well-established CROWN method (soundness appears to be good).
* The method is applicable to a very general perturbation model.
* The in-depth discussion of the method and its limitations in Section 3.4 is commendable.
* The work opens various obvious avenues for future work that could be of interest for the wider robust ML community (refining single- and multi-neuron bounds, generalizing beyond feed-forward networks, enforcing consistency of perturbations between gradient steps etc.)
* The manuscript is well-structured, beginning with a high-level approach (Paramaeter-space certification) and a specific instantiation of this approach (Abstract gradient training), before discussing the technical details of its individual components.

### Weaknesses
 * I agree with the authors' argument that the approach taken by this method is orthogonal to prior work. Nevertheless, the experiments would be significantly more informative if one were to use prior work as baselines. Instead of demonstrating "the method for verifying robustness does in fact verify robustness for sufficiently small perturbations", one could demonstrate "the verification method fills a useful niche in the certified-accuracy/runtime space for certain dataset / model sizes".
* The authors claim that their procedure was applicable to any first-order optimizer like Adam (see ll.198-199). This claim appears to be incorrect, since it would require a reachability analysis of the optimizer's internal state (moments etc.). Instead, the method appears to be limited to vanilla SGD.
* The submission does not include an implementation. Since the proposed method is rather involved, and implementing verifiers requires significant care, this significantly hinders reproducibility. I would strongly encourage the authors to provide code.
* Even if one were to try and reimplement the method, the description of hyperparameters and other aspects of the experimental setup is hardly sufficient to reproduce any of the results (see Appendix J). I would strongly encourage the authors to upload experiment configurations with their code.
* The discussion of related work is mostly relegated to Appendix A. This is an integral part of the paper and should (maybe with slightly more concise writing) be moved to the main text.

**Minor weaknesses**:
* While the authors provide asymptotic bounds on runtime complexity, they do not specify the wall-clock time needed for veryifing the different models in the experiment section. This would make it easier to gauge the practical feasibility of the proposed method.
* Based on the asymptotic runtime complexity, the use of small-scale models, and fine-tuning instead of training from scratch, the method appears to be hardly scalable to real-world settings -- except for some  special cases. I do, however, not consider this a major weakness, as this work represents a first step in a novel research direction.
* The definition of targeted attacks (Eq. 4) assumes the existence of a single, data-independent set of safe outputs $S$. However, what constitutes a safe output may often be data-dependent (e.g., whether steering left/right is safe depends on whether the ground truth direction is left/right in the PilotNet dataset from Fig. 5). It should be easy to generalize the proposed method to this use case, since one just has to evaluate the model output bounds differently.
* The definition of backdoor attacks (Eq. 5) does not enforce that the model should have high accuracy on unperturbed samples. As such, the guarenteees are likely to be very loose upper bounds on unnoticable backdoor attacks. It would probably be better to solve a constrained optimization problem over the set of reachable model parameters.
* Prior work on parameter-level verification for Bayesian NNs is mentioned, but it is not explained why these methods are not applicable to the considered problem. For instance, Wicker et al. (2020) [1] appear to determine a "safe" set of weights such that only some desired set of outputs is reachable, which is essentially inverse to Theorem 3.1.

### Questions
* Shouldn't we use $\mathrm{SEMin}_{m+n}$ in Theorem 3.3, since the $m$ feature vectors and $n$ labels that are perturbed can belong to disjoint sets of samples (see see ll.117-118)?
* Aside from increased computational cost, are there any reasons why you decided to extend CROWN instead of more recent methods like ($\alpha,\beta$)-CROWN, MN-BAB etc.?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to certify the robustness of a model trained on possibly poisoned dataset through the robustness of its parameters. Specifically, the model performance is bounded by the worst-case performance over all possible parameters that can be trained over all possible poisoned datasets under a capability constraint on the attacker. The authors therefore propose to certify a parameter-space bounds, and provide a practical algorithm when the model is a fully-connected neural network. The authors demonstrate their certified accuracy through the proposed method on various datasets.

### Strengths
1. The paper is well-organized and easy to follow.
2. This paper provides an alternative perspective to certify the model performance through the robustness of model parameters.
3. The topic of AI security and robustness regarding malicious model attacks attracts a signficant amount of attention in recent years.

### Weaknesses
 **Major Concerns:**

1. While it is intuitive that the variation of model parameters can serve as a tool to evaluate its robustness, the guarantee it could provide is extremely loose, at least as presented in this work. In particular, the authors consider the worst-case parameter interval against all possible poisoning dataset as in Eq. (6), and relax it further to Eqs. (8) and (9). It is questionable how useful such a valid but loose bound will be. This concern is to some extent confirmed by the experimental results. Examples include (i) in Fig 1, either a small perturbation level or a small number of poisoning data points is considered to avoid meaningless result. In Fig 1(c), flipping only 4 labels causes an almost void certified bound. (ii) in Appendix H, the authors acknowledge that their bound is extremely loose compared to real-world attacks and corresponding model performance. The core issue is that the parameter space bound, while theoretically sound, might be too coarse to provide meaningful robustness guarantees in practice. The relaxation from Eq. (6) to Eqs. (8) and (9), while necessary for tractability, appears to significantly inflate the uncertainty region, leading to potentially vacuous certificates. The experimental results, particularly the sensitivity to even small label flips, highlight this practical limitation.

2. The practical evaluation of Eq. (6). As acknowledged by the authors in Section 3, obtaining an parameter interval by Algorithm 1 is intractable in general. The authors provide an approach to solve Eq. (10) for fully-connected neural networks only.  It seems too ambitious to derive the reachable parameter interval against all potential attacks. Even if we can somehow approximate it, as mentioned in the first point, this interval may turn out to be vacuous. The restriction to fully-connected networks is a significant limitation, as many modern architectures rely on convolutional or other specialized layers. The computational cost of approximating the reachable parameter interval, even for fully-connected networks, is also a concern. The authors need to more clearly address the scalability of their approach and its applicability to more complex models.

3. Attack goals formulated in Section 2.2. While authors claim the goal of the attacker is to maximize the training loss such as Eqs. (3), (4) and (5), it makes more sense to consider controlling the generalization error or the test loss, because people are generally more interested in the test performance. To this end, the experiments should also report the certified and true performance on test datasets. Moreover, Eq. (5) is more similar to adversarial attacks instead of backdoor poisoning. A backdoor poisoning attack has dual goals of preserving the performance of clean data and ensuring the accuracy of the backdoored data in terms of the target label. The formulation of the attack goal as maximizing training loss, rather than directly targeting test performance, raises questions about the practical relevance of the certified bounds. A more realistic attack model would consider the attacker's objective as influencing the model's generalization behavior. The current formulation also conflates backdoor poisoning with adversarial attacks, which have distinct objectives and mechanisms.

**Minor Concerns:**
1. It is unclear to me what is the close-form solution to Eq. (10) for neural networks in terms of $\epsilon, \nu, n, m$. An algorithm explaining these details will help readers better understand it.

2. Some results are neither proved or properly referred, such as Theorem 3.3 and B.1, and Proposition 1 and 2.

### Questions
Please see the Weakness section above.

### Soundness
3

### Presentation
3

### Contribution
2
