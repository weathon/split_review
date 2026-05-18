Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces FB-CPR (Forward-Backward representations with Conditional Policy Regularization), a novel unsupervised RL algorithm that grounds the zero-shot capabilities of FB representations by regularizing policy learning toward a dataset of unlabeled behavior trajectories. The key technical innovation is using the FB backward embedding (via ER_FB) to project unlabeled trajectories into the same latent space used for policy parameterization, then employing a latent-conditional discriminator to perform distribution matching in joint state-latent space. The paper demonstrates FB-CPR by training a behavioral foundation model for a 69-DoF SMPL humanoid in MuJoCo, achieving 73.4% of task-specific oracle performance across reward optimization, goal reaching, and motion tracking — outperforming all multi-task and zero-shot baselines — while producing more natural-looking behaviors as confirmed by human evaluation.

## Strengths

- **Novel algorithmic contribution with principled design.** FB-CPR is a non-trivial combination of FB zero-shot RL with conditional adversarial regularization. The use of ER_FB to embed unlabeled trajectories into the existing FB latent space (rather than learning a separate encoder) is clean and well-motivated, and the latent-conditional discriminator enables fine-grained per-motion regularization rather than coarse marginal state matching. (Section 3, Eqs. 7–11)

- **Strong empirical results on a challenging humanoid benchmark.** FB-CPR achieves 73.4% of single-task top-line performance while operating zero-shot, outperforms ASE by more than 1.4× across all categories, and exceeds planning-based methods (DIFFUSER, MPPI with learned models) by large margins. These results are on a high-dimensional (358-dim state, 69-dim action) whole-body control problem with realistic physics, making the evaluation non-trivial. (Table 1, Section 4.1)

- **Human evaluation provides complementary qualitative evidence.** Despite TD3 achieving higher numerical reward, human raters judged FB-CPR as producing more natural-looking behaviors with similar task success rates. This directly supports the claim that regularization toward motion-capture data yields behavior quality that raw reward optimization misses. (Figure 3)

- **Comprehensive ablations validate design choices.** The paper systematically ablates: (i) the unsupervised FB term (→ CALM-like), (ii) the latent-conditioned discriminator (→ marginal state matching), and (iii) the online policy regularization (→ offline FB-AW). Each ablation degrades performance, confirming that all components of FB-CPR are necessary. (Figure 4)

- **Scalability analysis demonstrates data- and compute-efficient scaling.** FB-CPR improves monotonically with both model capacity and dataset size, consistent with foundation-model scaling behavior — a practically useful property suggesting the approach will benefit from future resources. (Figure 4)

- **Exceptional inference efficiency.** FB-CPR requires ~12 seconds per episode vs. ~30 minutes for oracle MPPI and ~5 hours for DIFFUSER, making zero-shot RL viable for near-real-time humanoid control.

## Weaknesses

### Fatal
None.

### Major

- **Non-stationarity of trajectory embeddings in the discriminator loop is not discussed.** The backward embedding \(B\) is learned concurrently via Eq. 5, yet the discriminator (Eq. 9) conditions on \(z = \mathrm{ER}_{\mathrm{FB}}(\tau) = \frac{1}{n}\sum_i B(s_i)\), which shifts as \(B\) evolves during training. The actor's KL regularization also depends on this embedding. The paper states that "binding FB and policy training together... ensures a more stable and consistent learning algorithm" (line 146), but provides no analysis — theoretical or empirical — of the effects of this non-stationarity. While the empirical results show the method works overall, the lack of discussion or any mechanism to address embedding drift (e.g., a target network for \(B\), periodic re-embedding, or an analysis showing drift is negligible) leaves the stability of this core mechanism as an open question. This is not a fatal flaw — many joint representation+policy learning systems tolerate similar non-stationarity — but the paper would be substantially strengthened by acknowledging and analyzing it. (Section 3, Eqs. 5, 9, 11)

### Minor

- **The "first humanoid behavioral foundation model" claim could be more precisely scoped.** The paper states FB-CPR yields "the first humanoid behavioral foundation model that can be prompted to solve a variety of whole-body tasks" (abstract). However, ASE (Peng et al., 2022) is acknowledged as "the closest BFM approach to ours" (line 161) and is itself a large-scale skill embedding for simulated humanoids. While FB-CPR's specific zero-shot *reward optimization* capability is genuinely novel, the broad "first" claim risks an unnecessary debate. Rephrasing to "first zero-shot whole-body BFM supporting reward optimization, goal reaching, and tracking" would be more accurate and avoid the issue.

- **Latent space distribution mixture weights are unspecified in the main text.** The distribution \(\nu\) is described as a mixture of three components (ER_FB trajectory embeddings, B(s) goal states, and uniform over the hypersphere, line 142), but the mixing proportions are not given. These may be in the appendix (stripped by parsing), but including the values or at least the search range in the main text would aid reproducibility.

- **Limited explanation for why planning baselines failed.** The paper notes that "MPPI with a learned model and H-GAP performed poorly across all tasks" and omits them (line 176), but does not discuss *why* they failed (e.g., model accuracy issues, action space dimensionality, coverage limitations). A brief diagnosis would help readers assess the difficulty of the environment and understand where planning approaches fall short relative to FB-CPR.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing against a version where trajectories are embedded using a *fixed* (pre-trained) FB model would cleanly isolate whether the benefit of FB comes from the latent space structure or the online embedding updates.
- A brief empirical analysis of embedding drift during training (e.g., cosine similarity of ER_FB(τ) for the same trajectory at different training stages) would directly address the non-stationarity concern.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Missing statistical confidence for baseline comparisons" (Harsh Critic #2):** The paper explicitly states "We report mean and standard deviation across the 5 seeds" for Table 1 (line 165). The critic's claim that only FB-CPR has error bars contradicts the paper's description. Since the table is a parsed image, the critic may have misread it. Removed as factually inconsistent with the paper text.

2. **"Overstatement of 'first humanoid behavioral foundation model'" (Harsh Critic #3):** The paper's claim is specifically about zero-shot *reward optimization + goal reaching + tracking*. ASE can be directed via skill embeddings but does not perform zero-shot reward optimization. The critic's objection overlooks this qualifier. Removed as a misunderstanding of the paper's scope.

3. **Latent space justification (from "Other Observations"):** The critic asks for weighting/scheduling of mixture components. These details are standardly deferred to the appendix, and the main text gives a clear rationale for each component. Downgraded from a weakness to a minor observation about reproducibility (included above).

## Novel Insights

The most interesting observation emerging from the reviews is that the non-stationarity concern (Weakness #1) actually cuts both ways. The critic correctly identifies that B evolves during training, creating a moving target for the discriminator. But the paper's discussion (line 146) claims this binding improves *stability* — an assertion that is neither supported nor refuted by the current experiments. A targeted analysis of embedding drift (e.g., does ER_FB(τ) converge faster than the discriminator adapts?) could either validate the paper's intuition or reveal a genuine instability that future work should address. The fact that the overall method works well across 45+50+990 tasks despite this potential issue is itself noteworthy — it suggests the joint training dynamics are more robust than a simple "moving target" concern would imply, which is practically informative even if not fully explained theoretically.

## Suggestions

- Add a brief analysis or discussion of the non-stationary embedding issue: either (a) empirically demonstrate that ER_FB(τ) converges early in training and drift is negligible, or (b) adopt a simple mitigation (e.g., a frozen copy of B for labeling dataset trajectories, updated every K steps) and show it does not hurt performance. This would significantly strengthen the paper's algorithmic soundness.
- Tighten the "first humanoid behavioral foundation model" claim by explicitly noting the zero-shot and multi-task-type qualifiers.
- Report the mixture weights for the latent distribution ν (even approximate values) in the main text.
- Add a sentence explaining the likely failure mode of MPPI with learned model and H-GAP in this setting.

## Score and Decision

The paper makes a solid contribution: a novel algorithm with strong empirical validation on a challenging problem, comprehensive ablations, human evaluation, and scaling analysis. The main weakness — the unaddressed non-stationarity in the joint training loop — is a real concern but does not invalidate the results (the method clearly works). It is an issue of understanding and analysis rather than a fundamental flaw. The paper would benefit from revision but the core contribution is clear, well-evaluated, and practically significant.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>