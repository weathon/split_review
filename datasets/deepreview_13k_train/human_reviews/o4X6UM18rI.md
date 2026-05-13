# Bayes-Nash Generative Privacy Protection Against Membership Inference Attacks

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Membership inference attacks (MIAs) expose significant privacy risks by determining whether an individual’s data is in a dataset. While differential privacy (DP) mitigates such risks, it faces challenges in general when achieving an optimal balance between privacy and utility, often requiring intractable sensitivity calculations and limiting flexibility in complex compositions. We propose a game-theoretic framework that models privacy protection as a Bayesian game between a defender and an attacker, solved using a general-sum Generative Adversarial Network (general-sum GAN). The Bayes Generative Privacy (BGP) response, based on cross-entropy loss, defines the attacker’s optimal strategy, leading to the Bayes-Nash Generative Privacy (BNGP) strategy, which achieves the optimal privacy-utility trade-off tailored to the defender’s preferences. The BNGP strategy avoids sensitivity calculations, supports compositions of correlated mechanisms, and is robust to the attacker’s heterogeneous preferences over true and false positives. A case study on binary dataset summary statistics demonstrates its superiority over likelihood ratio test (LRT)-based attacks, including the uniformly most powerful LRT. Empirical results confirm BNGP’s effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a Bayesian game model for formalizing the risk of disclosure with respect to data sharing. In this framework, the defender aims to minimize his privacy loss under a specified level of utility while the attacker aims at maximizing its membership advantage. A Generative Adversarial Network (GAN) approach is proposed for training the perturbation mechanism and model the interactions with the attacker.

### Strengths
-The related work section clearly summarizes the previous work on the quantification of privacy leakage as well as how to address formally the privacy-utility trade-off. 

-The considered membership inference attack setting is clearly explained and formalized. The proposed approach aims to provide a firm foundation for developing optimal privacy mechanisms. An illustrative example based on the sharing of summary statistics is used to illustrate the proposed framework. 

-To valide the proposed framework, experiments have been conducted on three datasets and the success of the resulting MIA has been compared against other state-of-the-art approaches. The results clearly demonstrate the potential of the approach with respect to other existing ones.

### Weaknesses
 -The writing of the introduction is a bit confusing for someone who is not already familiar with the concepts used in this paper. It would help to rephrase it but also to provide an outline of the structure of the paper. 

-Overall, the writing of the paper is highly technical and while the detailed proofs of the different lemma and theorems are given in Appendices, it would be great to provide some intuition or a sketch in the main paper. 

-Some information are currently missing in the description of the experiments such as the value of the parameter epsilon used as well as the experimental details for the Adult and MNIST dataset.

-Actually, the framework considered that the data of each participant is just a binary value while in the majority of the setting (such as learning a machine learning model), the profile of the user is a feature vector. 

-The training of a GAN is known to be difficult as some challenges have been addressed such as avoiding the overfitting of the discriminator to the generator. Ideally, it is good to also assess the privacy protection provided by training some external models, which is currently lacking in the current experiments.

### Questions
Please the main points raised in the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper focus on the privacy protection against MIA under data sharing scenarios. They propose a Bayesian game model for the data sharing with the defender minimizes a combination of expected utility and privacy loss, while the Bayes-rational attacker maximizes privacy loss. To approximate a Bayes-Nash equilibrium, the author then propose a GAN-style algorithm. They also introduce Bayes-Nash generative privacy and Bayes generative privacy risk, and prove the composition and post-processing properties for BGP risk. Experiments are conducted to demonstrate the performance of the proposed approach in genomic summary statistics sharing scenario.

### Strengths
* A Bayesian game model is proposed for the privacy-preserving data sharing process
* New privacy measure is proposed with composition and post-processing propoerties
* Both theoretical analysis and empirical results are provided for the proposed Bayesian game-theoretic method
* Notations are clearly defined

### Weaknesses
 * Since v(p, b) and the loss function be analyzed are proxies, the analysis of the approximation error should be provided.
* It would be better to provide the complexity analysis of the proposed method, along with the runtime of the defense mechanisms used in the experiments.

### Questions
In Eqn.2, why the coefficient of two terms are different (1-\gamma, \gamma)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a game-theoretic framework for private generative models. Privacy risk is measured by vulnerability to membership-inference attacks. The defender is a randomized generative model that processes a dataset drawn by a population by a neural network. The defender. The attacker is modelled as a Bayesian agent with a membership prior that infers membership by applying a discriminator neural network to output generated by the defender. The paper describes attacker and defender losses that are minimized simultaneously using GAN techniques.

### Strengths
The paper proposes a novel framework for generative privacy and experimental results demonstrate that Bayesian membership-inference attacks in the framework can be uniformly stronger than a frequentist attack.

### Weaknesses
The paper is difficult to read due to cumbersome notation and a lack of motivating exposition.

In particular, the paper contains a high number of symbols such as $\hat{\mathcal{L}}^\sigma_A(G_{\lambda_D}, H_{\lambda_A})$ and $\textrm{BN}[G; \sigma]$ that are complex and somewhat difficult to memorize. I found this to distract from the important concepts presented in the paper. To give a couple of examples:
- You could consider fixing some values like the distributions $\sigma$ and $\theta$ at some conspicuous location in the text (since they do not appear to be treated as variables outside of e.g. Prop 1) and then replacing symbols like $\textrm{Adv}(h_A, \sigma, \theta, \gamma; g'_D)$ with something like $\textrm{Adv}^\gamma(h_A, g'_D)$.
- Some notation like $\mathcal{L}^\sigma_A(G_{\lambda_D}, H_{\lambda_A}; \gamma)$ seems to have more "moving parts" than necessary and could be replaced with something like $\hat{\mathcal{L}}^\gamma_A(G, H)$ (assuming you need to maintain $\gamma$ as a variable)
- There are many sets such as $\texttt{Br}[G; \sigma, \gamma]$ introduced, which require extra back-and-forth to recall their meaning. They could be replaced by a phrase "$H^*$ is a best response to $G$" or by a short formula like $H^* \in \underset{H}{\operatorname{argmin}}  \mathcal{L}^\sigma_A(G, H)$.

In addition, a number of main results such as Theorem 1 are difficult to interpret due a lack of clear explanation. It would be helpful to expand a bit on what "a BNGP mechanism using CEL ensures robust privacy protection" (l299) means. As another example, Definition 4 felt a bit unclearly motivated and a bit difficult to parse. The exposition given for Proposition 5 could also be clarified.

Overall, the paper would benefit from broad notational simplification as well as clear intuitive exposition for technical definitions and theorems.

l247: "Therefore, we use $\ell_U(\| \delta \|_p)$ as the utility loss for the defender." Does this account for the effect of clipping?

l269: "This equilibrium is a reformulation of the $\sigma$-BNE using neural networks." Are we guaranteed that the equilibrium exists for typical classes of neural networks?

l295: Theorem 1 assumes that "that given any $G$, $\mathcal{L}_D$ increases as the TPR or the $\textrm{Adv}(H,\sigma,\theta,0.5; G)$ increases." Can the authors explain this assumption a bit further and speak to whether it is realistic?

l445: Figure 1(a) shows a non-concave tradeoff curve (blue) for a likelihood-ratio test attacker. This is surprising to me because Neyman-Pearson ensures the LRT attacker realizes the tradeoff curve of the mechanism and these curves must be concave/convex (see e.g. Proposition 2.2 in Dong, Roth, and Su 2019). How can this be explained?

The following are small typographical issues:
- l63: abbreviation CEL used before definition
- l74: LRT not defined yet
- l93.5: "quantify" -> "quantifies"
- l223.5: "differentable"
- l262-263: $\mathcal{L}_D$ defined for the second time; $\mathcal{L}_A^\sigma$ seems to conflict with existing notation $\mathcal{L}_A$ from l202
- l268: it is a bit confusing to me to use "risk" to refer to a discriminator network rather than a scalar quantity
- l445: Some of the legends in Figure 1 mention "defender" but I assume that "attacker" is what is meant.

### Questions
l247: "Therefore, we use $\ell_U(\Vert \delta \Vert_p)$ as the utility loss for the defender." Does this account for the effect of clipping?

l269: "This equilibrium is a reformulation of the $\sigma$-BNE using neural networks." Are we guaranteed that the equilibrium exists for typical classes of neural networks?

l295: Theorem 1 assumes that "that given any $G$, $\mathcal{L}_D$ increases as the TPR or the $\textrm{Adv}(H,\sigma,\theta,0.5; G)$ increases." Can the authors explain this assumption a bit further and speak to whether it is realistic?

l445: Figure 1(a) shows a non-concave tradeoff curve (blue) for a likelihood-ratio test attacker. This is surprising to me because Neyman-Pearson ensures the LRT attacker realizes the tradeoff curve of the mechanism and these curves must be concave/convex (see e.g. Proposition 2.2 in Dong, Roth, and Su 2019). How can this be explained?

The following are small typographical issues:
- l63: abbreviation CEL used before definition
- l74: LRT not defined yet
- l93.5: "quantify" -> "quantifies"
- l223.5: "differentable"
- l262-263: $\mathcal{L}_D$ defined for the second time; $\mathcal{L}_A^\sigma$ seems to conflict with existing notation $\mathcal{L}_A$ from l202
- l268: it is a bit confusing to me to use "risk" to refer to a discriminator network rather than a scalar quantity
- l445: Some of the legends in Figure 1 mention "defender" but I assume that "attacker" is what is meant.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a Bayesian game model for privacy-preserving data sharing, particularly focusing on defending against membership inference attacks (MIAs). The authors propose a GAN-style algorithm to approximate a Bayes-Nash equilibrium, balancing the defender's privacy and utility concerns against an attacker's attempts to maximize privacy leakage. The model incorporates Bayes-Nash generative privacy and Bayes generative privacy risk, accounting for the attacker's heterogeneous preferences towards true and false positives. The method is applied to genomic data summary statistics, demonstrating its effectiveness over state-of-the-art privacy-preserving approaches. The paper also establishes conditions for the equivalence between Bayes-Nash generative privacy and pure differential privacy and shows the composition and post-processing properties of BGP risk. Empirical results validate the theoretical analysis, illustrating the superiority of the Bayesian game-theoretic approach in protecting privacy while maintaining data utility.

### Strengths
1. The paper presents a novel approach to privacy protection by modeling the interaction between a defender and an attacker as a Bayesian game, which allows for a more nuanced understanding of privacy risks.
2. The paper introduces a GAN-style algorithm to approximate the Bayes-Nash equilibrium, providing an efficient way to train models in the context of privacy protection.
3.  The paper offers both theoretical analysis and empirical results, demonstrating the effectiveness of the proposed method in protecting privacy while maintaining data utility.
4.  The paper is generally good to follow.

### Weaknesses
1. Some notations used in the paper are confusing. 
2. The game-theoretical framework of the interplay between attacker and defender needs more justification. Specifically, the rationale for modeling this interaction as a Bayesian game, and the specific choices for the utility functions of both the attacker and defender, require more detailed explanation. The paper should clarify why a Bayesian game is the most appropriate model compared to other game-theoretic frameworks, and how the chosen utility functions accurately reflect the real-world incentives of both parties. For instance, the attacker's utility function seems to only consider the trade-off between true and false positives, but not the cost of performing the attack itself, which may not be realistic in practice. 
3. The experimental results are thin at the moment and lacks enough illustration. The paper should provide more details about the experimental setup, including the specific datasets used, the parameter settings for the algorithms, and the evaluation metrics. The current results are not convincing enough to demonstrate the effectiveness of the proposed method. For example, the ROC curves in Figure 1 lack detailed explanations of the experimental settings, making it difficult to interpret the results. Furthermore, the comparison with state-of-the-art methods is not sufficiently comprehensive.

### Questions
1. The derivation of Equation (2) needs more elaboration, what does \theta represent in the equation?
2. Inference cost is considered in the attacker's decision but not the defender's. More justifications are needed for such modeling. What will happen if defense cost is also considered?
3. From the experimental results, it seems that the Bayesian attack proposed in the paper is the best-performed attack. Does different settings of prior information affect the attacking results?
4. What is the difference of experimental settings of results shown in Figure 1a and 1b? According to Figure 1b, does it mean that Bayesian defender is inferior than fixed-threshold LRT defender? (Note that this is an examplar question, I find the results section quite thin and unconvincing).

### Soundness
3

### Presentation
3

### Contribution
3
