Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies grokking (delayed generalization after overfitting) through the lens of neural network robustness. It provides a theoretical link (Lemma 4.1, Theorem 4.2) connecting $l_2$ weight-norm decay to robustness and test accuracy; proposes an adaptive Gaussian-perturbation training method that accelerates grokking on MNIST and modular addition; discovers that standard training fails to learn the commutative law of addition before grokking while perturbed training does; and introduces two new robustness-informed metrics (Perturb Mutual Information and Perturb Entropy) intended to track the grokking moment more tightly than the $l_2$ norm.

## Strengths

- **Novel empirical finding about commutativity in grokking (Section 5):** The paper demonstrates that standard training on the modular addition dataset does not satisfy the commutative law on the training set until *after* grokking occurs, which is a genuinely surprising observation. In contrast, the perturbation-based method learns commutativity immediately after training accuracy reaches 100% (Figure 5). This is a concrete, non-trivial empirical discovery that advances mechanistic understanding of grokking on this task.

- **Perturbation-based training demonstrably accelerates grokking (Section 4.2):** The adaptive Gaussian-noise injection (Eq. 1) is a simple intervention that meaningfully speeds up generalization on both the MNIST and modular addition datasets (Figure 4), with the effect being especially pronounced on the algorithmic dataset. This provides a practical, theoretically motivated technique for reducing the long delay characteristic of grokking, and the adaptive noise schedule ($\sigma = \max(\lambda_1(1-\text{train acc}), \lambda_2)$) is well-motivated by the training dynamics.

- **Theoretical connection between weight-norm decay and robustness (Lemma 4.1, Theorem 4.2):** Lemma 4.1 adapts a known bound (Ma & Ying, 2021) relating the gradient Frobenius norm to weight norm and sharpness. Theorem 4.2 then provides a formal (if simple) argument: weight-norm decay increases the radius $\epsilon(W^*)$ within which one can guarantee correct classification of test points that have a nearby training neighbor. This connection, while basic, goes beyond purely empirical observations in prior work.

- **New robustness-informed metrics proposed (Section 6):** The paper introduces PMI and PE, which are novel applications of matrix information theory to grokking monitoring. Figures 8 and 9 suggest these metrics change more sharply at the grokking moment than the $l_2$ weight norm, opening an interesting direction for tracking the phenomenon.

## Weaknesses

### Fatal
None.

### Major

- **The central theoretical contribution does not deliver on its claimed explanatory power.** Theorem 4.2 is essentially a Lipschitz-based generalization bound: if a $\delta$-fraction of test points lie within $\epsilon(W^*)$ of a training point with the same label, then test accuracy $\ge \delta$. The bound depends on the unknown distribution of distances between train and test points, and nothing in the theorem predicts the *sudden phase-transition* shape that defines grokking. Corollary 4.3 fills this gap by *assuming* a specific parametric form for $\|W^*\|_F^2 S(W^*)$ (truncated linear decay on a log scale) and a Gaussian distance distribution, then fitting the constants $a=1925$, $b=500$, $L=1/2$, $\mu=1/100$ to match the real accuracy curve (Figure 3). This is post-hoc curve fitting, not a predictive derivation from first principles. The paper's claim of having theoretically "explained" grokking or its phase-transition behavior is therefore unsupported by the evidence presented. The theory establishes a *qualitative* link (norm decay helps generalization) but does not constitute a mechanistic explanation of the phenomenon.

- **The PMI and PE metrics are introduced without quantitative validation.** The paper claims these metrics "correlate better" with grokking than the $l_2$ weight norm, but provides only visual inspection of plots (Figures 8, 9). No correlation coefficients (Spearman or Pearson) are reported, no comparison to alternative metrics (e.g., sharpness, margin, normalized weight norm) is given, and the choice of the perturbation strength $\sigma$ (0.1 for MNIST, 0.4 for modular addition) is not justified or ablated. Without quantitative evidence, the claim of superior correlation is not supported. This substantially weakens the contribution of Sections 6–7.

### Minor

- **The perturbation method is evaluated too narrowly.** The method is compared only against standard training (Figures 4, 6). No comparisons are made to natural alternatives such as tuned weight decay, standard data augmentation, label smoothing, or the slingshot mechanism (Thilak et al., 2022). While the method clearly works, its relative value and the specific contribution of the adaptive schedule remain unclear. Hyperparameters $\lambda_1,\lambda_2$ also differ substantially between datasets (0.06/0.03 for MNIST vs. 0.5/0.4 for modular addition) with no ablation or sensitivity analysis shown.

- **The causal link between commutativity learning and perturbation training is asserted, not established.** The paper shows that perturbation training induces commutativity earlier (Section 5.1) and that explicitly enforcing commutativity (abelian degrok) also accelerates grokking (Figure 6). However, the perturbation method likely affects multiple aspects of learning (margin, sharpness, flatness), and the observation that commutativity emerges earlier does not demonstrate it is the *cause* of faster generalization. The causality claim exceeds what the correlational evidence supports, though the paper mostly uses hedged language ("may be explained").

- **Results are presented without statistical confidence.** All accuracy/metric plots appear to be single runs. Given the stochasticity of both the method (random perturbations) and training (random seeds), multiple runs with error bands are necessary to assess reliability and variance. This is a standard expectation for empirical ML papers.

### Trivial

- **Commutative-law regularizer details underspecified.** The abelian degrok regularizer (Section 5.1) adds an MSE loss between logits of $a+b$ and $b+a$ with a coefficient of 100, but no explicit formula is given, and no sensitivity to this large coefficient is shown.

- **MNIST training subset size not stated.** The paper says it "follows the setup of (Liu et al., 2022b)" but does not specify the exact training subset size used for the MNIST grokking experiments.

- **The conclusion mentions "bigger models" vaguely.** "Future work may include trying to find the grokking phenomenon on bigger models" — it is unclear whether this refers to models larger than the ones used (a 3-layer MLP and a 1-layer transformer) or a different direction.

## Nice-to-Haves

- A comparison of the adaptive noise schedule against a *fixed-strength* noise schedule would help isolate the benefit of the adaptive component.
- An ablation sweeping $\lambda_1$ and $\lambda_2$ would clarify sensitivity.
- For the PMI/PE metrics, reporting the correlation with test accuracy (e.g., Spearman's $\rho$) and comparing to the $l_2$ norm would be a natural addition.
- Multiple random seeds with error bands would significantly strengthen the empirical conclusions.

## Removed Points

These points are flagged to be removed — treat them with caution, as they reflect reviewer errors or formatting artifacts rather than genuine paper weaknesses.

1. **"Theorem 4.2 is garbled (min{1, } cut off)"** — The garbled expression is a parser artifact from PDF extraction; the original submission does not have this issue. The substantive criticism about the theorem's explanatory weakness is retained in Major weaknesses above.

2. **"Lemma 4.1 is a known result"** — The paper explicitly cites Ma & Ying (2021) for this lemma. Attributing it to a known source is not a weakness and is standard academic practice.

3. **"No code or reproducibility details"** — Requesting complete code/training logs for a conference submission is beyond standard expectations. The paper provides sufficient methodological detail (architecture, optimizer, hyperparameters) for a skilled practitioner to reproduce the results.

4. **"The paper should also discuss limitations"** — A discussion of limitations would improve the paper, but its absence is not a weakness of the scientific contribution.

5. **Generic demands for "missing related works"** — Not included as we cannot verify the existence of unmentioned works.

6. **Strength Finder's Supporting Strength 1 ("Phase-transition simulation matches real accuracy")** — This strength conflicts with the verified weakness that the corollary involves post-hoc curve fitting. Per the rule that "when a strength and weakness disagree, the weakness wins," this claimed strength is moved here.

## Novel Insights

The most genuinely novel observation to emerge from the review process is the separation of the paper's contributions into two tiers: (a) the commutativity finding, which is empirically solid and genuinely surprising, and (b) the theoretical and metric-based contributions, which are substantially weaker than the paper's framing suggests. The paper's value lies primarily in the empirical discovery about commutative-law learning dynamics and the demonstration that a simple input-perturbation intervention can accelerate grokking — not in the claimed theoretical explanation. The commutativity finding (Section 5) is the strongest part of the paper and could be developed further into a standalone contribution if paired with a more rigorous causal analysis disentangling robustness from commutativity.

## Suggestions

1. **Re-frame the theoretical contribution honestly.** Remove or substantially soften claims of "explaining" grokking or its phase transition. Present Theorem 4.2 as a qualitative demonstration that weight-norm decay *can* benefit generalization (a necessary but not sufficient condition for grokking), not as a mechanistic explanation. The Corollary 4.3 curve-fitting exercise could be moved to an illustrative toy example with clear caveats.

2. **Quantitatively validate the PMI/PE metrics.** Report the Spearman or Pearson correlation between each metric and test accuracy over training, and compare to the same correlation for the $l_2$ weight norm. Sweep the perturbation strength $\sigma$ and report how the correlation varies.

3. **Add basic statistical confidence.** Report results over at least 3–5 random seeds with error bands for all core experiments (Figures 4, 5, 6).

4. **Compare the perturbation method to at least one natural baseline** (e.g., tuned weight decay, or the slingshot mechanism) to help the reader gauge the method's added value.

## Score and Decision

**Originality:** 6/10 — The commutativity finding is novel; the robustness perspective is not entirely new but the specific application to grokking is reasonably original.  
**Importance of question:** 7/10 — Grokking is an active area and understanding it better matters.  
**Claims well-supported:** 3/10 — The theoretical explanation is substantially weaker than claimed; the new metrics lack quantitative validation.  
**Soundness of experiments:** 4/10 — Single runs, no baselines for the perturbation method, no quantitative evaluation of metrics.  
**Clarity of writing:** 5/10 — The paper is readable but the theory section is confusing and the contribution claims outpace the evidence.  
**Value to community:** 5/10 — The commutativity finding and the perturbation intervention have value, but the overclaimed theory and unvalidated metrics reduce net impact.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>