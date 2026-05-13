# Stochastic Bandits Robust to Adversarial Attacks

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
This paper investigates stochastic multi-armed bandit algorithms that are robust to adversarial attacks, where an attacker can first observe the learner's action and \emph{then} alter their reward observation.
    We study two cases of this model, with or without the knowledge of an attack budget $C$, defined as an upper bound of the summation of the difference between the actual and altered rewards. For both cases, we devise two types of algorithms with regret bounds having additive or multiplicative $C$ dependence terms.
    For the known attack budget case, we prove our algorithms achieve the regret bound of ${O}((K/\Delta)\log T + KC)$ and $\tilde{O}(\sqrt{KTC})$ for the additive and multiplicative $C$ terms, respectively, where $K$ is the number of arms, $T$ is the time horizon, $\Delta$ is the gap between the expected rewards of the optimal arm and the second-best arm, and \(\tilde{O}\) hides the logarithmic factors.
    For the unknown case, we prove our algorithms achieve the regret bound of $\tilde{O}(\sqrt{KT} + KC^2)$ and $\tilde{O}(KC\sqrt{T})$ for the additive and multiplicative $C$ terms, respectively.
    In addition to these upper bound results, we provide several lower bounds showing the tightness of our bounds and the optimality of our algorithms.
    These results delineate an intrinsic separation between the bandits with attacks and corruption models~\citep{lykouris2018stochastic}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper develops stochastic multi-armed bandit algorithms that are robust against adversarial attacks. These attacks can alter the reward the learner observes, and the adversary decides to alter the reward with full knowledge of the action selected by the learner and the realization of the corresponding reward. This way, the model introduces complexities beyond the corruption model, where the adversary has to decide whether or not to corrupt the rewards before having this piece of information. The authors present algorithms for both known and unknown attack budgets with additive and multiplicative regret bounds with respect to the attack budget, providing theoretical proofs of tightness and empirical validations.

### Strengths
1) The paper explores an under-studied area of stochastic bandits where adversarial attacks are present and obtains novel results as well as improving prior work about the already studied corruption model.
2) The theoretical bounds are tight (up to log terms), with mathematical proofs for each statement.
3) Experimental results to validate the theoretical claims are provided.
4) The authors do a good job clarifying the differences between corruption and attack models, highlighting the need for specialized approaches.

### Weaknesses
1) The paper explores an under-studied area of stochastic bandits where adversarial attacks are present and obtains novel results as well as improving prior work about the already studied corruption model.
2) The theoretical bounds are tight (up to log terms), with mathematical proofs for each statement.
3) Experimental results to validate the theoretical claims are provided.
4) The authors do a good job clarifying the differences between corruption and attack models, highlighting the need for specialized approaches.

1) The implications for practical settings, such as recommendation systems or online auctions, could use some expanding. It is unclear how the specific attack model, where the adversary has full knowledge of the learner's action and reward realization, translates to real-world scenarios. For instance, in a recommendation system, it's not always feasible for an adversary to have such precise information to manipulate rewards. The paper should elaborate on the plausibility of this attack model in different applications.
2) Unfortunately, all the proofs are relegated to the appendix.

1) Is the uniqueness of the best arm really needed? What happens if this assumption is not fullfilled?

2) Could you provide concrete applications addressed by your model?

There are a few typos:

091 - To address with MAB with -> To address the MAB with 
103 - Show that which type -> Show which type
185 - Lipchitz -> Lipschitz

### Questions
1) Is the uniqueness of the best arm really needed? What happens if this assumption is not fullfilled?

2) Could you provide concrete applications addressed by your model?

There are a few typos:

091 - To address with MAB with -> To address the MAB with 
103 - Show that which type -> Show which type
185 - Lipchitz -> Lipschitz

### Soundness
4

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
4

### Summary
The paper investigates the classical MAP problem in the adversarial attack setting. The authors provide several tight results covering the case when the attack budget is known/unknown, multiplicative and additive bounds, as well as lower bounds.

### Strengths
- This paper addresses a gap in the literature, recognizing that adversarial attacks have not been thoroughly explored within the classical multi-armed bandit (MAB) framework and effectively filling this gap.
- The authors examine both additive and multiplicative bounds, providing a clear comparison that shows which approach performs better based on the attack budget C.
- Figures 1 and, especially, Figure 2 nicely illustrate the results of attack-based multiplicative and additive bounds, offering a well-structured presentation that I haven't seen in comparable works with this level of detail.
- I also like seeing the clear separation between corruption and attack results/settings in one place.
- The paper presents novel findings and situates them within the existing literature, demonstrating that the derived upper bounds are tight (known C case).

### Weaknesses
1. Algorithm Design: I didn’t notice any novel or original elements in terms of algorithm design. The PE algorithm has been applied in this context in prior work (cited below), and the idea of using CORRAL has already been explored in similar settings, such as in Misspecified Gaussian Process Bandit Optimization. However, I only find this to be a minor weakness of the paper. 

2. Terminology: I like the terminology of “attacks” to distinguish it from the classical “corrupted” setting. However, if the authors intend to introduce this terminology shift, they should properly credit the original paper that first explored this setting and provided robust algorithms: “Corruption-Tolerant Gaussian Process Bandit Optimization.” To my knowledge, this was the first work to present robust algorithms for scenarios in which the attacker can observe the learner's decisions.

3. Literature Review: The literature review in this paper can be improved. The reference section is also too brief and lacks organization. For example, Bogunovic et al. (2020), as cited, do not address the linear setting; this is covered in other relevant papers that are not cited, such as Stochastic Linear Bandits Robust to Adversarial Attacks and A Robust Phased Elimination Algorithm for Corruption-Tolerant Gaussian Process Bandits.

4. Lower Bound Claim: The paper claims that the lower bound result of Ω(KC) is new; however, this result is already established in Stochastic Linear Bandits Robust to Adversarial Attacks (see Appendix C.3). The proof and exposition provided here are quite similar to those in the mentioned paper.

5. Venue Suitability: I’m not entirely sure this paper is a strong fit for ICLR, as I’m not aware of similar works published at this venue previously. This is a consideration for the authors, as they might find broader reach at an alternative venue.

6. Clarity of Comparison (Lines 417-422): The comparison in this section is unclear, and I would appreciate a clearer exposition/steps, especially since the reference provided here is incorrect.

### Questions
See 4 and 6 in the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies the design of stochastic bandits algorithms robust to adversarial attacks. In particular, the paper considers an easier setting in which the learner is aware of the attacker budget, and a harder setting in which the learner is not aware of the attacker budget. These results are complemented by lower bounds. Finally, the authors provide an experimental analysis that shows the effectiveness of the proposed approach.

### Strengths
The paper advances the state of the art on algorithms robust to adversarial attacks. The paper is well-written and the relationship/improvement relative to previous work is well described.

### Weaknesses
The technical contribution is quite weak. For instance, the algorithmic approaches follow previous work and the analysis is not very involved. Specifically, the algorithms appear to be adaptations of existing techniques for stochastic bandits, with modifications to handle the adversarial setting. The analysis, while providing bounds, does not seem to introduce fundamentally new proof techniques or insights. The core ideas, such as using an explore-then-commit strategy or variants of the successive elimination algorithm, are well-established. The novelty of the analysis seems limited to adapting these existing techniques to the specific adversarial model considered in the paper. The paper would benefit from a more detailed explanation of the specific modifications made to existing algorithms and a deeper analysis of the challenges introduced by the adversarial model.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies stochastic bandit algorithms which are robust to adversarial attacks under a strong adversary that can see the observed arm before attacking.   
The paper considers settings with unknown budget cost or known budget cost $C$.
In the known budget case, they provide a gap dependent $((\frac{K}{\delta}) \log T  + KC))$ upper bound that matches the lower bound. They also give gap-independent extensions with upper bounds of $\tilde{O}(\sqrt{KTC})$ or $\tilde{O}(\sqrt{KT} + KC)$ bound.

For the unknown case, they show two stopping criteria-based algorithms, one with an additive dependence in C: $O(\sqrt{KT} + KC^2)$. They show an algorithm that gets $O(T^\alpha)$ regret without corruptions, must have at least $O(T^\alpha + C^\beta)$ regret for $\beta \geq \frac{1}{\alpha}$, thus this upper bound matches this lower bounds in exponents of $C$ (given that it has $\sqrt{T}$ dependence without $C$). Similarly, they give algorithms with multiplicative dependence on $C$ for the regret, that is  $\tilde{O}(\sqrt{KC}T^{\frac{2}{3}})$ or $\tilde{O}(KC\sqrt{T})$.

The paper also provides experimental evidence showing the effectiveness of their algorithms against the attack strategies developed by Jun et al. 2018 comparing it will other corruption-robust MAB algorithms studies in the literature.

### Strengths
1. The paper differentiates between attack and corruption models of manipulating multi-armed bandits. It provides insights into the difference between corruption and attacks in terms of the required corruption/attack budget and thus the increased difficulty in preventing attacks compared to corruption.

2. For the successive elimination algorithm SE-WR with increased confidence, also used in Lykouris et al. (2018), the paper shows a tighter regret bound, by better analysis of the concentration results which leads to $O(KC)$ term instead of a gap dependent term in  Lykouris et al. (2018).

3. The authors also give a gap-independent bound for SE-WR and extend the SE-WR algorithm to work in the unknown attack budget settings. They also provide an analysis of the resulting algorithms. 

4. The paper also provides experimental evidence showing the effectiveness of their algorithms against the attack strategies developed by Jun et al. 2018 in comparison with multiple MAP defense strategies proposed in the literature.

### Weaknesses
1. The results or the discussion do not clarify whether gap-dependent results can be obtained for the unknown horizon setting.


2. Since this paper focuses on making the distinction between attacks and corruption, it seems the main difference is in the inability to use randomization to reduce the scale of the attack, resulting in the need for deterministic algorithms where potentially any arm suffers from all of the corruptions. Thus in the known corruption level case, the results for the setting are directly implied by earlier. (Although this work does a tighter analysis in terms of gaps). A thorough analysis of the lower bounds comparing the setting rather than just comparing the dependence on $K$  could benefit the reader. 

3. Experimental results don't have confidence bars, and in the case of no corruptions with known budgets, the STOP algorithms perform worse than other methods. Some discussion on the performance in the absence of corruption is warranted.

Nit:
1. In general, the writing of the paper is very focused on presenting as many results are possible and is very dense in terms of results. The paper could have been formatted better with more discussions around interpreting the results rather than having so many results in the main paper.

 2. There are some typos and inconsistencies in the theorem statements and proofs. For eg in proof of Lemma 14:
  i) the constants are changed from 36 to 64 in $N_k$.
  ii) Line 798, it should be 'triggered' instead of 'trigger'
   iii) Similarly lines 804 to 807 on page 15 in the same proof have $\delta$ with subscripts.

### Questions
1. Can you please mention how the lower bounds change or are implied from the corruptions setting to the attack setting in case of unknown horizons?

2. Can you please explain if the gap-dependent results in the unknown corruption case can be obtained for the algorithms under consideration? 

3. Can you please explain why the algorithms potentially perform worse in low corruption settings in the experiments?

### Soundness
3

### Presentation
2

### Contribution
2
