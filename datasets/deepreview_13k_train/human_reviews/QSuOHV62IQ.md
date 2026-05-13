# Latent Variable Identifiability in Nonlinear Causal Models with Single-domain Data under Minimality Condition

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
The identifiability of latent variables given observational data is one of the core issues in the field of disentangled representation learning. Recent progresses have been made on establishing identifiablity theories for latent causal models. However with much restrictions or unrealistic assumptions, their practicality on real applications are limited. In this paper, we propose a novel identifiablity theory for learning latent variables in nonlinear causal models, requiring only single-domain data. We prove that all latent variables in a powerset bipartite graph can be identified up to an invertible transformation, if the generation process of observable data is globally invertible, latent variables are independent, and shared latent variables entail minimal information. Experiments on synthetic data support the conclusions of our theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper's main contribution is the introduction of a novel identifiability theory for latent variables in nonlinear causal models, using only single-domain data. It proposes a reduction process converting general causal models into powerset bipartite graph structures, proving that latent variables can be identified under mild conditions: invertibility, independence, and a new minimality condition. This theory provides a framework for designing algorithms to uniquely identify latent variables in scenarios with limited data. One main issue is that it claims that every model can be converted to a powers bipartite graph, but did not give any proof. Another weakness is that in all the examples in the paper, observable variables are children of latent variables, which is quite restricted and unrealistic.

### Strengths
The problem that the authors try to attack, i.e. latent causal discovery is crucial in causal discovery. It helps uncover hidden factors influencing observed data, enabling more accurate modeling of causal relationships. Identifying latent variables can improve understanding of complex systems, enhance predictive accuracy, and support tasks like disentangled representation learning, domain adaptation, and generalization to distributional shifts. Without addressing latent variables, causal models may miss key drivers, leading to incomplete or biased conclusions.

### Weaknesses
There are two main issues of the proposed approach.

(1) The conversion of SCM to a power-set bipartite graph is not proved to be correct.

(2) The assumption that observable variables are children of latent variables are too restrictive and inpractical.

### Questions
See above.

### Soundness
2

### Presentation
2

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
Identifiability analysis of latent (causal) variables is a fundamental challenge in causal/disentangled representation learning. This work introduces a straightforward powerset bipartite graph, which defines an equivalence class of general causal models capable of generating the same observed distribution. We present identifiability analysis tailored to this specific graph structure and extend the analysis to provide deeper identifiability insights. Simulations are conducted to validate the theoretical claims.

### Strengths
Identifiability analysis of latent variable models is both challenging and fundamental.

The identifiability analysis for this specific graph structure seems to be robust.

The relationship between the unknown nature of latent dimensions and the minimality condition is interesting.

### Weaknesses
As a theory paper, I take the details of claims very seriously. However, I found some claims to be overly casual, lacking reasonable justification.

1) The claim that 'multi-domain data are usually hard to acquire' seems overly strong. I do not think this is the case. Additionally, the references cited to support this point (e.g., Matsuura & Harada, 2020; Creager et al., 2021) primarily propose methods for handling multi-domain problems rather than the difficulty of acquiring such data, and therefore do not support the claim.

2) The claim that 'any underlying structural causal model (SCM) can be reduced to an equivalent SCM with a powerset bipartite graph (PBG) structure' also seems overly strong. I understand that, in latent space, generating the same observed data can result from multiple graph structures, leading to a large equivalence class. This is a key reason why non-identifiability results often arise, and many works aim to address this challenge. Given this, it seems reasonable that some transformations between potential graph structures could result in a standardized structure. However, the claim that 'any underlying SCM can be reduced to a powerset bipartite graph' appears unsupported. At the very least, the authors should provide rigorous theoretical backing for this claim. The reduction process needs to be explicitly defined, including the transformations and assumptions required to achieve the PBG structure.

3) Additionally, as an initial step in this work, it would be helpful to clarify which graph structures can be reduced to a powerset bipartite graph, which cannot, and what the associated costs of this reduction might be. For example, are there specific types of causal relationships or graph topologies that are incompatible with the PBG structure? Furthermore, if the powerset bipartite graph structure is critical, it would be valuable to present real applications that justify its importance. The current lack of concrete examples makes it difficult to assess the practical relevance of this specific graph structure.

4) The identifiability results in Theorem 1 appear to be sound. However, some implicit assumptions should be explicitly stated. For example, in reviewing the proof for Theorem 1, I noticed that it presumes mutual independence across all dimensions of each latent variable (e.g., z[i]⊥z[j] for the vector z). However, this assumption—that each zi​ is mutually independent—is not clearly stated in Theorem 1 itself. It is crucial to clearly list all assumptions to avoid ambiguity. The theorem statement should explicitly mention the independence assumptions, or if they are not required, clarify the conditions under which the theorem holds without them.

5) In general, non-identifiability is common in nonlinear ICA. However, applying sparsity constraints to the mixing process from latent to observed data can achieve identifiability, as demonstrated in this work. Prior studies, such as Zheng, Yujia, Ignavier Ng, and Kun Zhang's 'On the Identifiability of Nonlinear ICA: Sparsity and Beyond' (NeurIPS 2022), provide in-depth analysis on leveraging sparsity for identifiability. A clear comparison between this work and prior approaches is essential but appears to be missing here, making it difficult to fully understand this work's unique contributions. The authors should clearly articulate how their sparsity constraints differ from existing approaches and what advantages their method offers.

6) Again, the experiments on real data are not directly provided, which significantly weakens the claim regarding the importance of the powerset bipartite graph.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes an identifiability theory for nonlinear causal models with latent variables using only single-domain data. A minimality condition that has been implicitly used in most previous work has been formalized and leveraged for identification.

### Strengths
1. The considered problem is important and of practical significance.

2. The assumptions have been discussed in detail with examples.

### Weaknesses
1. The theory and methodology in this manuscript appear closely related to those in [1] for several reasons:

   - Both manuscripts decompose the original SCM into basis models, with very similar structures. For instance, Fig. 2 in [1] illustrates a basis model nearly identical to the one in this manuscript. The core idea of decomposing a complex model into simpler, manageable units is not novel, and the specific structure of the basis model presented here does not appear to introduce significant differences from existing approaches.
   - The identifiability theorems for the basis model share many similarities, differing primarily in the minimality assumption. While this manuscript makes the minimality condition explicit, [1] assumes known dimensions, implicitly ensuring minimality. Furthermore, the subspace span assumption in [1] is likely valid asymptotically, which may minimize substantial differences between the identifiability results in the two works. The reliance on a minimality condition, while explicitly stated, does not represent a fundamental departure from the implicit assumptions made in prior work, and the practical implications of this distinction need further clarification.
   - For the general model, both manuscripts employ iterative identification of basis models to achieve global identifiability, following a similar approach. The iterative approach, while a common technique, does not inherently demonstrate novelty, and the specific implementation details of this iterative process need to be more thoroughly examined to highlight any unique contributions.

Given the substantial overlap in the problem setting, theoretical results, and identification procedures, it may be helpful to further highlight the manuscript's unique contributions relative to [1], as the novel aspects are not yet sufficiently pronounced in the current version.


2. The notation could be clarified for better readability. For instance, $j\&2^l$ in line 189 is difficult to interpret within the given context. The use of bitwise operations without clear explanation makes the mathematical formulation less accessible and requires the reader to make additional inferences.

3. There are some questions for both the proofs and experiments. Please kindly refer to the questions for details.

### Questions
1. Could you please explain more on line 777, where it states that $\hat{v}_2$ does not change since the derivative of $v_2$ w.r.t. $s_1$ is zero?

2. The proof of Theorem 1 appears to establish only the nonexistence of certain edges, without addressing the existence of others. Including this additional aspect might provide a complete proof.

3. For evaluating general PBG-SCM identification, would it be more appropriate to use a metric that assesses component-wise identifiability, such as the mean correlation coefficient (MCC)? Since Theorem 2 establishes component-wise identifiability, relying on a metric like $R^2$, typically used for block-wise identifiability, may not fully capture the relevant evaluation criteria.

4. In all theorems, the generating functions are assumed to be invertible. However, in experiments, MLPs are used for the generation of synthetic data. Since MLPs are typically not invertible, it seems that the experiments cannot rigorously verify the theorems?

5. Could you please elaborate further on why previous methods require assumptions that there exists no connection among observed variables? I understand that this is necessary for the identification of latent structure, but not so sure about whether this is the case if we only aim to identify the latent variables. Perhaps elaborating it based on the concrete methods you mentioned in line 156 would be helpful.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides an identification result of latent variables in nonlinear causal models with single-domain data.

### Strengths
1. The theoretical results presented in this paper are sound, the authors provide detailed proofs.

2. This paper is well-organized and easy to follow.

### Weaknesses
1. The result of this paper is too weak, making it insignificant. To simplify the identification problem, it assumes that there is no direct path between observed variables. Even so, it can only identify latent variables in the PBG-SCM obtained by reducing the original SCM substantially. Notably, a PBG-SCM usually corresponds to a large number of SCMs. A latent variable in a PBG-SCM corresponds to the combination of several exogenous noises in the original SCM, which lacks physical meaning. In fact, even the number of latent variables in an SCM is not equal to that in the corresponding PBG-SCM. Therefore, identification of latent variables in the PBG-SCM is far from identification of latent variables in the original SCM, let alone causal relations between latent variables. I list two previous works for comparison. [1] also can only identify a simplified SCM rather than the original SCM, but it does not make the assumption that there is no direct path between observed variables. Moreover, the number of latent variables and causal relations between observed variables in the simplified SCM are same as that in the original SCM. [2] also makes the assumption that there is no direct path between observed variables, but it can identify latent variables and their causal relations.

2. In line 77, the author claims that "all these assumptions are mild, and necessary". First, the authors do not verify that all assumptions are mild, for instance, they are satisfied in most real-world cases or they are the same as or milder than assumptions made by related works. Specifically, I agree that the invertibility assumption is mild because it is used by most related works, but I cannot agree that the minimality assumptions are mild. Second, the authors only prove that minimality assumption is necessary in Proposition 5.1, but the other two assumptions are not proven to be necessary. The necessity of the invertibility assumption is not obvious, as it is not clear if a non-invertible function would necessarily lead to non-identifiability. The independence assumption, while common, also requires more justification for its necessity in this specific context, beyond just stating it is a common assumption.

3. It seems that the identification algorithm based on auto encoder needs to know the dimension of $z$, but in real-world scenarios, this is usually unknown. Given an inaccurate dimension of $z$, the performance is not satisfactory. The paper does not adequately address the practical challenge of determining the correct dimensionality of the latent space, which is a critical issue for the applicability of the proposed method. The sensitivity of the method to this hyperparameter is a significant limitation.

4. Some minor concern: It world be better to give a proof sketch for Theorem 1 and provide some experimental results on real-world dataset.

### Questions
According to [1], SCM consists of a series of assignments and a joint probability of exogenous noises, but in this paper, SCM is a triplet (G,F,P), the authors should list their references.

[1] Peters J, Janzing D, Schölkopf B. Elements of causal inference: foundations and learning algorithms. The MIT Press, 2017.

### Soundness
3

### Presentation
2

### Contribution
1
