# Contractive Systems Improve Graph Neural Networks Against Adversarial Attacks

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Graph Neural Networks (GNNs) have established themselves as a key component in addressing diverse graph-based tasks. Despite their notable successes, GNNs remain susceptible to input perturbations in the form of adversarial attacks. This paper introduces an innovative approach to fortify GNNs against adversarial perturbations through the lens of contractive dynamical systems. Our method introduces graph neural layers based on differential equations with contractive properties, which, as we show, improve the robustness of GNNs. A distinctive feature of the proposed approach is the simultaneous learned evolution of both the node features and the adjacency matrix, yielding an intrinsic enhancement of model robustness to perturbations in the input features and the connectivity of the graph. We mathematically derive the underpinnings of our novel architecture and provide theoretical insights to reason about its expected behavior. We demonstrate the efficacy of our method through numerous real-world benchmarks, reading on par or improved performance compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces massage passing layers in the context of graph representation learning, inspired by differential equations with contractive properties, that have promising capabilities in improving the robustness of GNNs. This claim is then further strengthened by a complete theoretical analysis and extensive benchmark covering many GNN architectures & threat models.

### Strengths
- Paper is well written.
- Complete theoretical analysis supported by strong results.

### Weaknesses
Unfortunately, the paper is not self-contained for readers with no background in contractive systems and dynamical systems. Since I'm not familiar with these techniques, it's hard for me to point out any weaknesses beyond educated guesses.

### Questions
I do not have major questions about the manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces a novel approach to enhance the robustness of Graph Neural Networks (GNNs) against adversarial perturbations using contractive dynamical systems. The authors establish the mathematical foundations of their architecture, offering theoretical insights into its expected behavior. Through real-world benchmarks, they validate its effectiveness, achieving comparable or superior performance to existing methods. The paper's contributions encompass a new GNN architecture, a theoretical framework for behavior analysis, and empirical proof of its ability to bolster GNN resilience against adversarial attacks.

### Strengths
1. The paper addresses the critical issue of improving GNNs' robustness against adversarial attacks. It introduces an innovative approach to enhance Graph Neural Networks' (GNNs) robustness against adversarial perturbations by employing contractive dynamical systems. The simultaneous evolution of node features and adjacency matrices is a unique aspect of this approach, demonstrating a high degree of originality.

2. The paper provides a rigorous mathematical derivation of the proposed architecture and comprehensive empirical evaluations. The authors offer theoretical insights into the expected behavior of their method, and empirical results affirm its effectiveness in bolstering GNNs against adversarial attacks.

3. The paper is well-written, ensuring clarity and accessibility for readers.

### Weaknesses
No obvious weaknesses from my perspective.

### Questions
1. What are the assumptions behind Theorem 1 & 2?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce an approach to enhance the robustness of GNNs against adversarial perturbations by leveraging the concept of contractive dynamical systems.

### Strengths
1. The paper presents a novel architecture, CSGNN, that innovatively integrates the principles of contractive dynamical systems to enhance the robustness of GNNs against adversarial poisoning attacks.
2. The simultaneous evolution of node features and the adjacency matrix is a distinctive feature that can potentially offer intrinsic resistance to adversarial perturbations.
3. The authors fortify their claims with a rigorous theoretical analysis.

### Weaknesses
1. Inadequate Literature Review: The paper's glaring omission of pivotal related works is concerning. The idea of enhancing NN robustness via dynamical systems isn't novel, even within the GNN realm. The authors' failure to acknowledge, let alone differentiate their work from seminal papers [1][2][3][4][5], is a significant oversight.

2. Lack of Clear Motivation: The paper's design choices seem arbitrary, with many equations appearing devoid of clear rationale. For example:
>The reasoning behind assuming a piecewise constant function in eq(6).
>The ambiguity surrounding the gradient operator of $A$ in eq(8).
>The seemingly ad-hoc design of eq(8) and its alignment with the paper's theorems.
>The choice to enforce symmetry on $\tilde{\mathbf{K}}_l$.
>The intricate design of the adjacency matrix update in eq(14) lacks clear justification.
The paper should not be a mere mathematical exercise; it should be accessible and provide clear motivations for design choices.

3. Reproducibility Concerns: The absence of code hinders the verification of the paper's claims. Critical aspects, such as adherence to the adjacency update mechanism in eq(14) and the positive definiteness of $\tilde{\mathbf{K}}_l$, remain unchecked.

4. Computational Overheads: The complete matrix representation in eq(14) suggests significant computational demands. The authors should elucidate the memory and time overheads.

5. Narrow Attack Scope:
The paper exclusively focuses on poisoning attacks. Is this indicative of the theorems being specifically tailored for such attacks? The theorem statements, including their assumptions and conclusions, don't seem to impose such constraints. What is the rationale behind primarily considering poisoning attacks? Reference [6] suggests that injection attacks pose a greater threat than poisoning attacks. The authors should address these concerns and expand their experiments to include injection attacks, irrespective of the model's performance against them.
Additionally, the inclusion of black-box attacks in the evaluation is necessary.
The model exhibits suboptimal performance on the Pubmed dataset. Does this suggest that the efficacy of your models and theorems is dataset-dependent? It would be insightful to understand how the model fares on different datasets, especially those characterized by heterophily.

6. Lack of Large-Scale Graph Datasets:
The current evaluation is limited to smaller datasets such as Cora, Citesser, and Polblogs. It would be beneficial to see how the model performs on more extensive, widely-recognized datasets like the ogbn series.

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A neural diffusion GNN model coupling the evolution of both node features and graph adjacency matrix is proposed. Analytical studies on the contractive properties of this model across model layers are provided.

### Strengths
Using a diffusion process to model the joint evolution of node features and graph adjacency matrix seems to be novel. Numerical experiments indicate that such an approach can provide robustness against adversarial attacks.

### Weaknesses
1. The analytical results show contractive properties of the feature/adjacency matrix evolution across model layers for a given input. I am unclear how this proves robustness of the GNN model to input or structure perturbation. Specifically, in eq. (10) of Theorem 2, $\mathbf{A}$ is fixed, but clearly $\Psi_{X_l}^{h_l}$ is impacted by $\mathbf{A}*$. Therefore, eq. (11) cannot be directly applied here as $\Psi_{X_l}^{h_l}$ and $\Psi_{Y_l}^{h_l}$ are two different functions. The paper does not adequately explain how the *individual* contractivity of feature/adjacency matrix evolution implies robustness of the *overall* system to perturbations. The contractivity of the adjacency matrix update alone does not guarantee the stability of the entire coupled system, especially when the feature dynamics are also involved. 

2. Missing comparison to the work “On the robustness of graph neural diffusion to topology perturbations,” NeurIPS 2022. What are the additional things we learn from this current paper? The results in the NeurIPS 2022 paper relate explicitly to robustness w.r.t. input perturbations.

3. Please give more information on the attack type. Is it inductive, modification/injection, whitebox/blackbox?  

4. What is the adaptive attack procedure? It seems the paper simply uses unit tests from Mujkanovic et al. (2022). These cannot be considered to be adaptive attacks for the proposed model. Mujkanovic et al. (2022) has emphasized this point too: "we cannot stress enough that this collection does not replace a properly developed adaptive attack". The authors should not claim robustness against adaptive attacks based on these unit tests, as they do not adapt to the specific model being evaluated. 

5. GNNGuard is mentioned but not used as baseline in Table 1. 

6. The attacks used do not seem strong enough (I am unclear of their settings as well). E.g., in Table 1, even under 25% attack, GCN still has >40% accuracy. In other related papers on GNN adversarial attacks (e.g., Fig. 1 of Mujkanovic et al. (2022)), usually GCN would have performed much worse with accuracies below 20-30%.

7. There are many other adversarial attacks like injection attacks. This paper only tests on modification attacks using Metattack and NETTACK. If the paper's focus is only on modification attacks, one can argue that the paper title and abstract do not reflect the technical content. Moreover, what is the motivation to focus only on modification attacks? Are these more important in practice?

### Questions
1. Please give more information on the attack type. Is it inductive, modification/injection, whitebox/blackbox?  

1. What is the adaptive attack procedure? It seems the paper simply uses unit tests from Mujkanovic et al. (2022). These cannot be considered to be adaptive attacks for the proposed model. Mujkanovic et al. (2022) has emphasized this point too: "we cannot stress enough that this collection does not replace a properly developed adaptive attack".

1. GNNGuard is mentioned but not used as baseline in Table 1. 

1. The attacks used do not seem strong enough (I am unclear of their settings as well). E.g., in Table 1, even under 25% attack, GCN still has >40% accuracy. In other related papers on GNN adversarial attacks (e.g., Fig. 1 of Mujkanovic et al. (2022)), usually GCN would have performed much worse with accuracies below 20-30%.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
