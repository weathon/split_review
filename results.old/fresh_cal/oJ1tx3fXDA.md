Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary
This paper proposes a **Generalized Heavy-Ball Momentum** (GHB) formulation for federated learning, where the momentum term is computed as a decayed average over τ past momentum terms rather than just the previous one. The key insight is that τ>1 allows incorporating gradient information from clients selected in multiple past rounds, providing a more robust estimate of the global direction under partial participation. The authors present **FedHBM**, a communication-efficient variant where clients locally compute the correction term using stored previous models (adaptive τᵢ determined by the client's own sampling interval). Controlled experiments show τ≈1/C is optimal (matching theoretical prediction), and large-scale results on Landmarks, iNaturalist, and Stackoverflow show gains over FedAvg, FedProx, SCAFFOLD, FedDyn, and MimeMOM.

## Strengths
1. **Novel formulation with clear motivation and empirical validation**: The GHB formulation (eq. 7–8) is a principled generalization of heavy-ball momentum that recovers classical momentum at τ=1. Figure 1 systematically varies τ and confirms (a) τ>1 is crucial, (b) τ≈1/C is optimal as predicted, and (c) performance is robust to overestimating τ. This directly supports the paper's core claim that accumulating information across rounds counteracts client drift.

2. **Consistent and substantial gains across multiple settings**: The paper reports a +20.6% top-1 accuracy improvement over FedAvg on CIFAR-10 ResNet under worst-case heterogeneity (Table 1), and improved results on realistic large-scale tasks (e.g., +7.6% on iNaturalist MobileNet, Table 2). These gains are based on careful hyperparameter tuning and 5-run averages.

3. **Communication-efficiency measured concretely**: Table 3 quantifies that FedHBM reduces communicated bytes and wall-clock time by over 60% to reach FedAvg's accuracy, backing the "communication-efficient by design" claim with per-task metrics.

4. **Adaptive τᵢ variant is clever and practical**: FedHBM eliminates the 1.5× per-round overhead of vanilla GHB by letting stateful clients store the previous model and compute the correction term locally when they participate again. This is a practically motivated design that addresses a real deployment constraint.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Failure claims for competing methods lack supporting evidence**: Section 5.3 states that MimeMOM "despite extensive hyperparameter tuning using the authors' original code, we were unable to achieve convergence" and calls this "the first work to report these failure cases." No convergence curves, hyperparameter search ranges, or ablation details are provided for these failure cases. While the claim may be true, the evidence is insufficient for such a strong assertion. (SCAFFOLD's failure is corroborated by citations to prior work, which is adequate.)

2. **No measure of variability reported**: Results are reported as averages over 5 runs, but no standard deviations, confidence intervals, or error bars are shown anywhere in the paper (Figures 1–2, Tables 1–3). Given that improvements over baselines are sometimes in the range of a few percent, the reader cannot assess whether the reported gains are statistically reliable or consistent across runs.

3. **The central equivalence (eq. 7 → eq. 8) relies on an appendix lemma**: The derivation showing that eq. 7 (decayed average of τ momentum terms) is equivalent to eq. 8 (model-difference form) is deferred to Lemma expr_ghb in the appendix. Since the main text claims this equivalence, including at least a sketch of the algebraic steps would allow readers to judge whether it is exact or approximate without consulting the supplement.

4. **No ablation on momentum coefficient β or local steps J against τ**: The paper systematically ablates τ but does not explore interactions with β or Jᵢ (the update rule uses β/τJᵢ). The sensitivity of the method to these combined hyperparameters is unknown.

5. **Memory/computation trade-off of stateful clients unmentioned**: FedHBM requires clients to store a model snapshot until their next participation. For large models (e.g., ViT), this doubles client-side memory. This practical constraint is not discussed.

### Trivial
- The abstract states existing approaches "are not communication efficient" (line 6), but FedDyn does not increase per-round communication. The paper's own results show FedDyn is competitive on simpler tasks, so this blanket characterization is slightly overstated.

## Nice-to-Haves
- **Adaptive server-side baselines (FedAdam, FedYogi)**: The large-scale evaluation omits adaptive server optimizers, which are commonly used in production-scale FL. While these methods address server-side adaptivity rather than client-drift correction (making them somewhat orthogonal), including them would strengthen the "state-of-the-art" comparison.
- **Convergence curves for large-scale experiments**: The paper reports only final accuracy for large-scale tasks. Showing loss/accuracy vs. communication round would directly support the claimed convergence speed advantages.
- **Convergence curves for the MimeMOM failure case**: Even a single plot would make the failure claim credible.

## Removed Points
- **Criticism about equivalence derivation being in the appendix** (Harsh Critic's Critical Issue 1): The paper references Lemma expr_ghb which exists in the original submission. The parser strips appendix content from all papers. This is not a weakness of the paper.
- **Criticism about missing FedAdam/FedYogi being a major gap** (Harsh Critic's Critical Issue 3): The paper's scope is client-drift correction via momentum. Adaptive server optimizers address a different mechanism. Demoted to Nice-to-Have (see above).
- **Complaint that "the limitation section is very brief"**: The paper has a dedicated limitations paragraph (lines 344–347) that explicitly acknowledges the challenge of estimating global direction in extremely large-scale settings. The brevity is appropriate for a conference paper.
- **Several formatting/style nitpicks and speculation-driven criticisms** (e.g., "the bound grows linearly with τ... the paper states robustness without explaining why the bound is loose in practice"): The paper explicitly addresses this — Lemma 2 shows linear dependence on τ, and the text notes that empirical robustness indicates this bound is loose. This is a standard theory-versus-practice acknowledgment, not a flaw.
- **Complaint about "stateless" vs "stateful" confusion**: The paper clearly distinguishes the two scenarios (lines 148–151) and explains the trade-off.
- **General category-driven speculation** ("could the metric be measuring a proxy?", "are confounders controlled?"): These lack specific anchors in the paper's content.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's observation that the gap between Lemma 2's bound (linear in τ) and the empirical robustness (low sensitivity to large τ) is worth the authors' attention, but the paper already acknowledges this gap.

## Suggestions
1. Add standard deviations or error bars to all reported results and figures.
2. Provide at least one convergence curve for the MimeMOM failure case on a large-scale dataset, or include a brief hyperparameter search summary in the supplement.
3. Include a brief sketch of the eq. 7 → eq. 8 derivation in the main text (2–3 lines of algebra).
4. Add a brief discussion of the client memory overhead for stateful FedHBM.
5. (Optional) Include FedAdam or FedYogi as additional baselines on at least one large-scale task.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>