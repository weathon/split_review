Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes Causal Transfer Learning (CTL), a method for out-of-domain (OOD) text classification that uses pre-trained language models (PLMs) as paired "environments" to identify causal features via a contrastive loss, combined with a front-door adjustment using token-level local features (Φ). The paper is evaluated on semi-synthetic (Yelp, Amazon) and real-world sentiment analysis datasets, showing consistent improvements over SFT and other baselines.

## Strengths

- **Novel use of PLMs as paired environments for causal feature learning**: The core idea of leveraging the pre-trained model (M₀) and fine-tuned model (M₁) as two environments with shared causal factors but different spurious factors is clever and practically relevant. The paper correctly instantiates this via Algorithm 1 Step 4, where both $\bar{r}_0 = \mathbf{M}_0(\bar{x}_i)$ and $\bar{r}_1 = \mathbf{M}_1(\bar{x}_i)$ come from the **same input text** $\bar{x}_i$, consistent with the paired-representation identification theorem (von Kügelgen et al., 2021). This is a meaningful, low-cost approach to obtaining multi-domain-like supervision without domain-labeled data.

- **Consistent and substantial empirical gains**: Across all three datasets and all OOD shift levels (70% → 10%), CTL consistently outperforms SFT. The gains are large and practically significant: e.g., on Yelp OOD 10%, CTL achieves 58.40 F1 vs. SFT 49.24 (+19% relative); on the real-world dataset at OOD 10%, CTL achieves 49.22 vs. SFT 37.78 (+30% relative). Results are averaged over 5 runs, and the box plots (Figures 2-3) confirm the advantage is not due to noise.

- **Informative ablation study**: The paper tests four variants (CTL, CTL-N, CTL-C, CTL-Φ). The degradation of CTL-N (using both C and Φ without the do-operator) compared to CTL, especially in the real-world experiment (49.22 vs. 15.05 at OOD 10%), supports the claim that the front-door adjustment helps block spurious paths. CTL-Φ's sharp degradation with increasing shift confirms Φ captures spurious information. CTL-C's strong standalone performance validates the value of learning invariant causal features.

- **Formal causal motivation for why SFT fails**: Proposition 1 and Equation (1) provide a clear decomposition $P(Y|X) = \sum_U P(Y|U,X) P(U|X;\sigma)$, cleanly explaining why the conditional estimator breaks under distribution shift. This sets up a rigorous foundation for pursuing the interventional estimator $P(Y|\text{do}(X))$.

- **Systematic controlled evaluation**: The further analysis (Section 6.3) examines sensitivity to spurious correlation strength, training data size, and inference sample size, showing that CTL's advantage holds across varied conditions.

## Weaknesses

### Fatal
None.

### Major

1. **The front-door adjustment derivation is not supported by the paper's causal graph.** The proof of Theorem 2 (Equation 4) attempts to derive $P(y|\text{do}(x)) = \sum_{\Phi'} P(y|\Phi', c)P(\Phi')$ using the front-door criterion. However, in Figure 1(c), the causal structure is $\Phi \rightarrow C \rightarrow Y$, meaning $C$ lies *between* $\Phi$ and $Y$, not the reverse. The front-door criterion requires a mediator that intercepts all directed paths from the treatment to the outcome. Since $C \rightarrow Y$ is direct, $\Phi$ is not on any path from $C$ to $Y$, and the derivation step marked "Frontdoor Criterion & Assumptions 3 and 4" is not justified by the graph the authors have drawn. The final formula may still be a reasonable heuristic, but it is not a valid front-door adjustment as claimed. This undermines the paper's central theoretical claim of a "principled" causal estimator.

2. **The paper's assumptions are stronger than claimed.** The paper repeatedly advertises "mild assumptions" (abstract, lines 8 and 33). In practice, Assumptions 1-4 impose a quite specific causal structure: the Decomposition assumption (inputs separable into causal C and spurious S), Paired Representations (two environments with shared C), Local Features (Φ generated from R₁), and Sufficient Mediator (Φ's effect on Y fully mediated by C). These are substantive structural commitments that are not validated for any real NLP task. Assumptions 3 and 4, in particular, impose a particular relationship between token-level features and causal variables that is neither obvious nor justified. The paper would benefit from acknowledging the strength of these assumptions rather than calling them "mild."

3. **Limited baseline set.** The paper compares against SFT, SFT0, SWA, and WISE. While SWA and WISE are relevant PLM robustness baselines, standard OOD generalization methods from NLP — such as IRM, CORAL, DANN, Mixup, or distributionally robust optimization (DRO) approaches — are absent. Without these comparisons, it is difficult to assess whether CTL is competitive with the broader field or merely beats the most basic baselines. The paper's claim of "superior generalizability compared to existing approaches" is not fully supported by the baselines included.

### Minor

4. **The front-door adjustment adds modest value on semi-synthetic data.** On the Yelp semi-synthetic dataset at OOD 10%, CTL-C (57.75) is very close to CTL (58.40), suggesting most of the gain comes from learning C rather than the adjustment. On Amazon, the gap is larger (53.40 vs. 56.40), and on real-world data the gap is substantial (42.25 vs. 49.22). The paper would benefit from a more nuanced discussion of when and why the front-door adjustment helps, rather than treating it as uniformly beneficial.

5. **The "single-domain" framing is somewhat overstated.** The method uses the pre-trained model (trained on large, diverse corpora) as one of the two paired environments. While this is a practical and clever workaround, it means the method does not operate on single-domain data in the strict sense. The paper partially acknowledges this (line 33: "a natural additional source of domain data"), but the abstract and contribution framing ("single-domain scenarios") overstates the novelty relative to multi-domain methods.

6. **The shuffling-based marginalization is not theoretically justified.** Step 7 of Algorithm 1 shuffles Φ within a mini-batch to approximate the marginalization over Φ′ in the front-door sum, and Step 4 of the inference algorithm does the same with K samples. The paper does not explain why this procedure is a valid estimator of $\sum_{\Phi'} P(y|\Phi', c)P(\Phi')$, nor does it analyze the approximation error. A brief justification or reference to relevant theory would strengthen the paper.

7. **Spurious correlations tested are narrow.** The semi-synthetic experiments inject correlations via stop word counts and the real-world experiment via platform name strings. Both operate at the lexical level. This does not demonstrate that the method handles more realistic spurious correlations (e.g., topic-label confounds, style shifts, demographic biases). The paper acknowledges this in its limitations section but does not address it experimentally.

8. **No ground-truth evaluation of causal feature recovery.** Unlike some causal representation learning papers, this work does not provide an experiment where the true causal features C are known and recovery accuracy can be measured. We must rely entirely on downstream task performance, which conflates the quality of C with the quality of the classifier trained on it.

### Trivial

9. **Notation errors in Algorithm 1.** Step 4 reads "$\bar{r}_1 = \mathbf{M_{1}}(\bar{r}_i)$" which should be $\mathbf{M_{1}}(\bar{x}_i)$ (M₁ takes text input, not representation input).

10. **Hyperparameter sensitivity not reported.** The paper does not discuss sensitivity to the number of patches (set to 10), the entropy weighting in Equation 2, or the inference sample size K.

## Nice-to-Haves

- An experiment on a non-sentiment task (e.g., NLI, as mentioned in the introduction) would strengthen the claim of general applicability.
- A comparison against a simpler representation-regularization baseline (e.g., minimizing L₂ between M₀ and M₁ representations without the causal framing) would help isolate the benefit of the contrastive causal loss.
- Reporting confidence intervals or standard deviations in Table 3 (not just in box plots) would aid comparison.

## Removed Points

- **Criticism 1 (paired-representation identification invalid)** — REMOVED as factually wrong. The reviewer claimed R₀ and R₁ come from different texts. Algorithm 1 Step 4 shows $\bar{r}_0 = \mathbf{M}_0(\bar{x}_i)$ and $\bar{r}_1 = \mathbf{M}_1(\bar{x}_i)$ — both from the **same** text $\bar{x}_i$. The paired-representation assumption (Assumption 2) is correctly instantiated. The fact that $\bar{x}_i$ is sampled with the same label (rather than being the original $x_i$) is a standard data augmentation strategy and does not violate the identification theorem, which requires representations of the same text under two environments.
- **Criticism 5 (R₀ and R₁ from different texts)** — REMOVED as redundant with Criticism 1 and factually incorrect. Same text $\bar{x}_i$ is used for both.
- **Criticism about "not yet released," "cannot be independently verified"** — REMOVED per policy (all cited works exist).
- **Criticism about missing appendix / proofs** — REMOVED per policy (parser strips appendices).
- **Criticism about typos/formatting** — REMOVED per policy (parser artifacts, not author errors).
- **Strength 6 from Strength Finder ("practical use of PLMs")** — RETAINED as it is specific and grounded.

## Novel Insights

The most striking pattern across the ablation results is the asymmetry between CTL-C (using only causal features C) and CTL-N (using both C and Φ without the do-operator). CTL-C performs well while CTL-N collapses under strong OOD shift, particularly on the real-world dataset (42.25 vs. 15.05 at OOD 10%). This suggests that simply concatenating all available features (C + Φ) is actively harmful, because Φ injects spurious information that the classifier cannot ignore. The front-door adjustment in full CTL mitigates this by marginalizing over Φ, recovering much of the performance. This pattern is a genuine empirical finding that deserves more discussion — it suggests the primary value of the do-operator is not in improving the estimate of causal effects per se, but in preventing the classifier from attending to the wrong features. This reframes the contribution: CTL is less about "causal identification" and more about "selective feature usage" guided by the paired-environment structure.

## Suggestions

1. **Fix the front-door derivation.** Either (a) provide a correct derivation that is consistent with the graph, (b) revise the graph to make the front-door pathway explicit, or (c) reframe the contribution without claiming a formal front-door adjustment — the empirical method can stand on its own as a regularized representation learning approach.

2. **Add standard OOD generalization baselines** (IRM, DANN, CORAL, or at minimum a Mixup baseline) to situate the method within the broader NLP robustness literature.

3. **Avoid calling the assumptions "mild"** without justification. Acknowledge their restrictiveness and discuss when they might hold or fail in practice.

4. **Provide theoretical or empirical justification for the Φ-shuffling marginalization** — even a small ablation study varying K would help.

5. **Reframe the "single-domain" claim** to more accurately reflect that the method uses the PLM's pre-training distribution as a second environment.

## Score and Decision

This paper proposes a genuinely interesting approach to OOD generalization by leveraging PLMs as paired environments, supported by solid empirical results across multiple datasets. The core technical contribution — learning invariant causal features by contrasting pre-trained and fine-tuned representations of the same text — is correctly implemented and empirically validated. However, the paper's theoretical centerpiece (the front-door adjustment derivation) is not properly justified by the causal graph. Combined with overclaimed "mild" assumptions, limited baselines, and several under-explained implementation details, this represents a paper with real empirical promise but significant theoretical gaps. The empirical results are strong enough to warrant attention, but the theoretical framing needs substantial revision before the paper's claims can be fully trusted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>