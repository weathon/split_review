Now let me write the final consolidated review.

## Summary

TD-JEPA introduces a temporal-difference (TD) latent-predictive loss for unsupervised zero-shot RL. The method trains separate state and task encoders (ϕ, ψ), a policy-conditioned multi-step predictor (T), and latent-space policies end-toenned from offline, reward-free transitions. Theoretically, it shows that optimizing the TD-JEPA loss implicitly minimizes successor measure approximation losses (gradient matching, Theorems 1–3), provides a non-collapse guarantee (Theorem 2), and bounds zero-shot policy evaluation error (Theorem 4). Empirically, it matches or outperforms eight baselines across 65 tasks / 13 datasets from ExoRL and OGBench, achieving particularly strong results on pixel-based domains (DMC_RGB: 628.8 ± 5.5, the highest among all methods).

## Strengths

- **Novel TD latent-predictive loss for offline multi-policy learning (Eq. 7, 9):** Unlike prior Monte-Carlo variants (BYOL-γ, MC-JEPA) that require on-policy rollouts, the TD formulation can be estimated from single-step offline transitions drawn from arbitrary data. This is a fundamental algorithmic enabler for training from reward-free offline data.

- **Gradient matching between latent-predictive and successor-measure losses (Theorems 1, 3):** The analysis shows that under standard assumptions (A1–A3, shared with prior work), the gradients of the TD-JEPA loss w.r.t. the representations coincide with those of direct successor measure approximation losses. This rigorously connects the practical self-supervised objective to the quantity needed for zero-shot RL, extending prior single-policy, one-step analyses to the multi-policy TD setting.

- **Non-collapse guarantee for TD latent-prediction (Theorem 2):** The paper proves that under a continuous-time relaxation with optimal predictors, representation covariance remains constant over time, preventing collapse from the bootstrapped ("doubly latent-predictive") structure — a nontrivial extension of earlier results (Tang et al. 2023) to the TD case.

- **State-of-the-art pixel-based zero-shot performance (Table 1, DMC_RGB: 628.8 ± 5.5):** TD-JEPA achieves the highest mean return among eight methods on DMC from pixels — a setting where prior zero-shot methods have notably struggled. It is also competitive on OGBench_RGB (41.34 ± 0.45). This represents a concrete empirical advance.

- **Thorough empirical methodology:** Evaluation across 65 tasks / 13 datasets covering locomotion, navigation, and manipulation with both proprioceptive and pixel observations. The probability-of-improvement analysis (Figure 2) demonstrates robustness, not just peak performance. Ablations (Figure 3) cleanly isolate the benefit of policy-conditioned multi-step prediction and asymmetric encoders.

- **Fast adaptation with frozen representations (Figure 4):** Pre-trained TD-JEPA representations, when frozen during downstream offline or online RL, enable sample-efficient learning that often matches or exceeds training from scratch, demonstrating practical reusability beyond zero-shot evaluation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **BC regularization on OGBench: could be more explicit about uniform application.** The footnote says "We additionally apply BC regularization in OGBench based on Park et al. (2025b), as detailed in App. E.6." The main text states "each method is tuned over comparable hyperparameter grids and adopts the same architecture" (line 253), which implies uniform treatment. However, the paper would benefit from stating explicitly that the same BC regularization is applied to all methods, removing any ambiguity for a reader who skips the footnote or does not track the fair-comparison commitment.

2. **Theory–practice gap on the "predictors trained faster than representations" assumption.** Theorem 2 assumes predictors are trained at a faster rate than representations to keep covariance constant, but the paper does not discuss whether this is enforced in the practical algorithm or what the consequences are if the assumption is violated. While this is a standard idealization in the theory literature (following Tang et al. 2023), a brief remark on how the empirical implementation relates to this assumption would strengthen the bridging of theory and practice.

### Trivial

None.

## Nice-to-Haves

- A concise hyperparameter table (e.g., regularization coefficient λ, representation dimensions, EMA rate) in the main text would improve self-containedness, though these details presumably reside in the appended appendix.
- A brief discussion of why TD-JEPA underperforms on specific OGBench tasks (e.g., cube-double, scene with proprioception) relative to some baselines would be informative.
- A comparison of training time or parameter count with simpler methods would help practitioners assess the computational overhead of training four networks plus an actor.

## Removed Points

- *Harsh critic's concern about EMA rate not given in algorithm box*: This is a parser artifact; the target network update via EMA is mentioned in the algorithm and the rate presumably appears in the appendix. Removed per Hard Rules (nitpick about trivial implementation detail).
- *Harsh critic's concern about missing hyperparameter grid in main text*: Standard practice to place such details in the appendix. Removed per Soft Rule (weakness not standard in the field).
- *Harsh critic's "missingss" about the double stop-grad being unusual*: The algorithm clearly shows stop-grad operations and justifies the design choice; this is an observation, not a weakness.
- *Harsh critic's theory assumptions being restrictive*: The critic correctly notes this is standard practice and the paper acknowledges relaxations are possible. Not a weakness — removed.
- *Strength Finder claims that are generic or about problem importance*: Removed (e.g., "TD-JEPA addresses an important problem" — generic, not grounded in specific evidence).

## Novel Insights

The most interesting insight that emerges from combining the theoretical and empirical analyses is that **TD latent-prediction implicitly factorizes policy-conditional successor measures**, and this factorization is what enables the zero-shot transfer. The gradient-matching argument (Theorems 1, 3) reveals that the seemingly unrelated self-supervised loss of predicting latent states is actually optimizing the same quantity that successor-feature-based methods (FB, RLDP, HILP) explicitly target — but without needing a contrastive loss or a separate successor feature estimator. This explains why TD-JEPA works well from pixels: the latent-prediction objective naturally co-adapts the state and task encoders to the data distribution, whereas contrastive methods (FB) may struggle when pixel representations are still being learned.

## Suggestions

1. In the main text, explicitly state that "the same BC regularization is applied uniformly to all baseline methods on OGBench" (or if it is not, clarify the difference and justify it).
2. Add a brief sentence in Section 4 or after Theorem 2 noting how the "faster predictor rate" assumption relates (or does not relate) to the empirical training procedure — even a caveat that "while our practical algorithm does not explicitly enforce this, the orthonormality regularization (Algorithm 1) provides a complementary stabilization mechanism" would help readers.
3. Consider adding a single-paragraph "limitations" discussion to the conclusion, addressing the theory-practice gap and any known failure cases (e.g., tasks where the successor measure factorization is inherently high-rank).

## Score and Decision

**Round 1 bracket:** Based on calibration search, the paper clearly sits above the weak anchors (avg scores 2.0–3.33, all withdrawn/rejected) and substantially below top-tier papers in other areas (avg 8.0 on unrelated topics). The most relevant anchor is RLDP (avg 6.5, Accept Poster), a similar paper on latent dynamics prediction for zero-shot RL. Initial bracket: 6.0–8.0.

**Round 2 narrowing:** Compared to the RLDP anchor (avg 6.5, scores [6,6,6,8]): TD-JEPA has more novel theory (gradient matching for TD losses vs. standard next-state prediction), more extensive experiments (65 tasks / 13 datasets vs. fewer), and achieves SOTA on the challenging pixel-based setting where RLDP operates on proprioception. The paper is also better written and more clearly structured. Compared to the "Zero-Shot Adaptation of BFMs" anchor (avg 6.0): TD-JEPA has broader scope and more extensive experiments, though the adaptation paper addresses a different problem (unseen dynamics). RLDP is the closest point of comparison, and TD-JEPA is clearly a stronger paper on that anchor.

**Final calibration:** The paper is stronger than the RLDP anchor (6.5) across multiple dimensions (theoretical novelty, experimental breadth, pixel-based SOTA) but does not reach the transformative impact level of an 8+ paper. The minor issues (BC regularization explicitness, theory-practice gap acknowledgment) are genuine but not threatening to the core claims.

**Score:** 7.0 — Strong accept. Well-executed, novel contribution to zero-shot RL with both theoretical and empirical substance.

**Decision:** Accept

<score>7.0</score>
<decision>Accept</decision>