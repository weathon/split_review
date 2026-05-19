- Decision: Reject
- Avg Score: 2.33
- Scores: 3, 3, 1
I now have all the information needed. Let me construct the final consolidated review.

## Summary

This paper tackles zero-shot environmental generalization in RL — transferring policies across environments with different observation spaces, dynamics, and visual perspectives. It introduces a structured state space model (Definition 3.1) that decouples invariant task representation from environment-specific background, analyzes the resulting "non-optimizable gap" (Proposition 3.3), and proposes Non-Parameterized Randomization (NPR), which randomizes task-agnostic environment components without requiring a parameterized environment model. Theorem 4.1 provides a lower-bound guarantee. Empirical results on MuJoCo→BabyAI, CarRacing→Torcs, and 2D→3D generalization show NPR significantly outperforming pixel-based baselines (e.g., 28–45% success vs. 0–1% for baselines).

## Strengths

1. **Novel structured framework for environmental generalization**: Definition 3.1 explicitly decouples the invariant task representation \( \psi_t(I) \) from environment-specific background \( \xi_t^e \), going beyond prior formulations (Block-MDPs, Epistemic MDPs) that assume a shared state space across tasks. The discussion in Section 3.1 ("Difference with Previous Models") clearly delineates this advance.

2. **Formal identification of a non-optimizable gap**: Proposition 3.3 decomposes the generalization error into an optimizable invariant-learning term and a "non-optimizable" term depending on unseen environment distributions. This formal diagnosis of why zero-shot environmental generalization is inherently hard is a genuine conceptual contribution over prior work.

3. **NPR method with theoretical justification**: Theorem 4.1 proves that training with non-parameterized randomized backgrounds provides an optimizable lower bound on the return in unseen environments, with the gap controlled by distribution similarity. Remark 4.2 provides an argument for why parametric methods incur an additional discrepancy term. This provides theoretical motivation for a model-free augmentation approach.

4. **Strong empirical results on challenging tasks across structurally different environments**: Tables 1–3 show NPR achieving zero-shot success rates and rewards far exceeding all baselines (e.g., 43% vs. ≤1% in navigation tasks; 195.5 vs. ≤−13.3 reward in car racing; 28% vs. 0% on 2D-to-3D generalization). These tasks go well beyond the standard sim-to-real or distribution-shift benchmarks in the literature.

## Weaknesses

### Fatal

None.

### Major

1. **Insufficiently clear experimental setup for observation-space bridging**. The paper claims zero-shot generalization across environments with fundamentally different state spaces (e.g., MuJoCo→BabyAI, 2D→3D) but does not clearly specify how the observation interface is shared between training and testing environments. Lines 162–164 state "we choose the most advanced pixel-based RL methods as baselines for a fair comparison" and mention "pixel observation by CNN," which implies pixel observations were used. However, the paper never explicitly confirms that *all* environments (including the MuJoCo training environment) were rendered as pixel observations, nor does it describe the input representation used by NPR itself versus the baselines. Since this is a zero-shot transfer across environments with incompatible native state spaces, the reader cannot assess whether the comparison is fair or whether the positive results follow from the method versus from an unstated representational choice. This is the most significant weakness — it undermines interpretability of the headline results.

2. **Proposition 3.3 equation is garbled/uninterpretable**. The bound in lines 95–97 contains `|S^e|S^e|^2` as a floating term with no clear meaning, and the overall structure of the inequality is ambiguous. The underbrace labeled "invariant learning error" appears to cover only \(L_\psi|A|\cdot|\hat{I}_1-\hat{I}_2|\), but the subsequent `|S^e|S^e|^2` term seems to multiply into the transition-probability difference without a clear operator or interpretation. As presented, this equation cannot be evaluated for correctness or tightness, which weakens the central theoretical diagnosis that the paper builds upon.

3. **Theorem 4.1 bound depends on the distribution of unseen environments, limiting practical applicability**. The gap term \(\alpha\) in Theorem 4.1 contains \(D_{KL}(\rho(e) \parallel \rho(\hat{\xi}_t))\) (line 128), which requires the distribution of *unseen* test environments \(\rho(e)\). The paper acknowledges this through qualitative discussion ("if the injected noise conforms to the change of the environments, \(\alpha\) will be a little constant") but provides no principled way to ensure this condition holds beyond "expert priors" (line 143). No analysis of how sensitive the bound is to misspecification of the randomization distribution is given. This makes the theoretical guarantee largely a post-hoc framing rather than a predictive or actionable tool.

4. **Method description is qualitative without algorithmic specification**. Section 4.2 describes NPR through high-level examples ("randomize the structure of the environment, randomize the background... randomize the spatial relationship of all the existing objects") without pseudocode, a precise algorithmic description of how randomization is applied episode-by-episode, or specification of randomization schedules. The mention of "soft randomizing with a continuous and slow episodic change" (line 145) is qualitative. This makes the method difficult to reproduce or ablate systematically.

### Minor

1. **Baseline performance is near-zero across all tasks**. All baselines achieve 0–4.4% success rates and strongly negative rewards across all task settings. While this is consistent with the paper's claim that existing methods cannot solve these tasks, the paper would be substantially strengthened by showing (a) that baselines can learn the *training* tasks without randomization (Figure 3c suggests they can in non-randomized settings), and (b) ablating whether the near-zero generalization stems from representational mismatch versus genuine inability to handle distribution shift. Without this, concerns about whether baselines were optimally configured for these unprecedented tasks cannot be fully dismissed.

2. **Limited statistical reporting**. Results are reported with 3 seeds (500 test episodes). Given the high variance inherent in zero-shot generalization tasks, confidence intervals or effect sizes would improve credibility. The paper lacks significance tests against baselines.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment where NPR is compared to parametric DR on a continuum of distribution shifts (both parametric and non-parametric) would cleanly isolate the claimed advantage of non-parameterized randomization.
- An analysis of how the amount/intensity of randomization affects learning stability and generalization performance.
- Feature visualization or saliency analysis to illuminate what the policy learns from the invariant representation versus the randomized background.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated:

- **"Proof is in a stripped appendix"** — Removed per hard rule: the parser strips appendices from all papers; they exist in the original submission.
- **"No hyperparameter tuning details"** — Removed as a reproducibility nitpick beyond what is standard for a main-text submission.
- **"The evaluation is measuring survival of a training mishap"** — Speculative framing not grounded in specific evidence in the paper; removed.
- **"The No-Rand ablation shows a trivial failure because MuJoCo states can't be processed by BabyAI"** — The paper states it uses pixel-based methods, so this specific criticism is factually misinformed.
- **"Paper does not compare to Block-MDPs / Epistemic POMDPs"** — The paper explicitly discusses these comparisons in Section 3.1 ("Difference with Previous Models"); removed.
- **"A CNN processing MuJoCo vector states is inappropriate"** — The paper states it uses pixel observations for baselines; the critic assumes the opposite, so this is factually incorrect.
- **"Proposition 3.4 is not generally true"** — The proposition conditions on "sparse reward 1 of the final state," which makes the stated equivalence mathematically valid under that specific reward structure; the critic missed this conditioning.
- **"Missing related works"** — Removed per hard rule (cannot verify existence of missing references without external knowledge).
- **Generic formatting/style nitpicks** — Removed per hard rule.

## Novel Insights

The harsh critic raises a genuinely useful observation that the harsh critic themselves did not fully develop: the paper's experimental setup combines two distinct challenges — (1) zero-shot generalization across *environments* (different dynamics, layouts, visual appearances) and (2) zero-shot generalization across *observation modalities* (vector vs. pixel, 2D vs. 3D, 3rd-person vs. 1st-person). Because NPR operates by randomizing environment-level structure, it is inherently addressing challenge (1), but challenge (2) requires an architectural decision about observation encoding (e.g., using a CNN for pixel inputs). The paper conflates these two challenges in its experiments without disentangling which one is the source of the improvement. A cleaner experimental design would separate the two: first verify that NPR works when the observation modality is held constant (e.g., both train and test use pixel observations from different environments), then separately test modality generalization. This insight suggests a concrete path for strengthening the empirical evaluation without changing the core method.

## Suggestions

1. **Clarify the observation interface**. Explicitly state whether all environments (train and test, NPR and baselines) used pixel observations from a shared rendering pipeline, or whether different methods used different input representations. If pixel observations were used, describe the rendering setup and resolution. This single clarification would resolve the most significant barrier to evaluating the paper's claims.

2. **Fix Proposition 3.3**. The garbled equation must be corrected. Even a corrected form would benefit from a derivation sketch showing how the bound is obtained from Assumption 3.2 and standard RL value-difference bounds.

3. **Add a training-task performance table**. Show that all methods (NPR and baselines) achieve reasonable performance on the training distribution before evaluating zero-shot transfer. This would rule out the concern that baseline failure is simply due to inability to learn the training task.

4. **Provide a minimal algorithmic description** of NPR (e.g., pseudocode for one episode of training) so the method can be implemented from the description alone.

5. **Discuss how expert priors for randomization are obtained** in each evaluation setting and analyze sensitivity to randomization choices (e.g., what happens if the randomization distribution does not cover the test distribution).
