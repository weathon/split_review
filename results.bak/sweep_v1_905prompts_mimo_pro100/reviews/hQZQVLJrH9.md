Good. Now I have all the information needed. Let me write the final review.

## Summary

This paper establishes a first-order equivalence between activation steering (frozen weights, perturb activations) and influence functions (fixed activations, perturb weights), proving that any steering vector can be represented as a signed influence weighting over training data and vice versa (Theorem 4.2). The framework yields: (i) an Influence-Aligned Steering (IAS) vector construction via pseudoinverse; (ii) a feasibility diagnostic γ(x) based on principal angles between Jacobian subspaces; and (iii) a spectral optimality theorem identifying the norm-budget-optimal steering direction as the leading eigenvector of a Fisher-influence matrix.

## Strengths

- **Novel theoretical unification of two previously disconnected fields.** Theorem 4.2 establishes a constructive duality between steering vectors and training-data influence weightings, with the IAS vector given by a closed-form pseudoinverse (Eq. 2–4). This is not merely a conceptual analogy — it provides an explicit signed measure ρ_s over training examples with an L1-minimality guarantee (Corollary 1). This duality is genuinely new and provides a principled bridge between activation-steering and influence-function communities.

- **Practical and interpretable γ diagnostic.** Theorem 5.1 gives a tight bound √(1−γ²) on the relative logit error of the IAS vector, where γ is the smallest principal-angle cosine between the activation- and parameter-to-logit Jacobian subspaces. This single scalar tells practitioners when steering can faithfully replicate influence-based interventions — a tool neither prior steering work nor influence-function work offered. The layer-depth ablation (Figure 2) showing γ rising from 0.64 (L0) to 0.94 (L11) in GPT-2 Medium provides empirical support for this diagnostic.

- **Spectral optimality theorem (Theorem 5.3) provides a principled steering direction.** The paper identifies the top eigenvector of Σ (a Fisher-influence correlation matrix) as the norm-budget-optimal steering direction, replacing ad hoc direction selection with a closed-form spectral recipe. The ImageNet validation (Figure 3, ResNet-50, z=3.55, p=0.005) demonstrates this produces directions far in the tail of the random-direction null distribution.

- **First-order equivalence empirically validated.** Figure 1 demonstrates near-collinearity (cosine 0.978) between predicted first-order logit shifts from IAS and actual realized shifts across 5000 prompt-token pairs, directly confirming the core theoretical prediction.

## Weaknesses

### Fatal
None.

### Major

- **Slope of 1.50 in Figure 1 indicates substantial second-order effects that the paper does not confront.** While cosine 0.978 demonstrates collinearity, the slope of 1.50 between predicted and actual logit shifts means actual shifts are 50% larger than the first-order prediction on average. This is a significant deviation from linearity — the paper describes this as "consistent with the expected linear regime" (line 243) without acknowledging that a slope of 1.50 implies second-order terms are roughly half the magnitude of first-order terms. The paper does not systematically vary perturbation magnitude α to quantify where the linear approximation breaks down, leaving practitioners without a concrete operating range. Since the entire framework's value proposition rests on the first-order approximation being quantitatively predictive, this gap is significant.

- **Empirical validation is drastically undersized relative to claims.** The paper uses only GPT-2 Medium (345M parameters) with 50+50 steering examples and 500 evaluation prompts, yet the abstract and introduction promise tools that "scale to billion-parameter models" (line 29) and "a single, efficient workflow for controllability and data provenance" (line 38). No experiments are run on larger language models, no multi-model evidence is provided, and the ImageNet experiment (Section 7.4) tests only spectral-direction significance — not the core steer-influence equivalence or γ diagnostic. A paper making strong practical workflow recommendations needs substantially more empirical grounding.

- **The ρ_s data attribution — arguably the most actionable component — is never tested.** The paper repeatedly emphasizes that the signed measure ρ_s "points straight to the most causal training documents" (line 122) and "pinpoints the fewest training examples to relabel/remove/examine" (Section 4.1 practical payoff). Yet no experiment computes ρ_s on actual training data, inspects top-weighted examples, or validates that removing/relabelling them changes behavior. This is the core practical promise of the paper and it remains entirely undemonstrated.

### Minor

- **Detoxification comparison (Table 1) shows IAS underperforming CAA on both metrics without discussion.** IAS scores 0.0164 mean toxicity vs. CAA's 0.0150, and IAS has higher perplexity (13701 vs. 13291). The paper presents this table silently. If IAS and CAA optimize different objectives and the comparison is not apples-to-apples (which is plausible), the paper should say so explicitly and explain what unique value IAS provides.

- **Layer choice (ℓ=8) is not justified by the paper's own heuristic.** Section 4.2 proposes: "pick the smallest layer index with γ ≥ 0.7." Since γ increases monotonically from 0.64 (L0) to 0.94 (L11), this heuristic would suggest an early layer (~L2-3), not L8. The paper does not report whether results change at different layers, or why L8 was chosen over the heuristic's recommendation.

- **The γ diagnostic is not validated as a predictive tool.** The paper proposes γ as a pre-check: "small γ ⇒ skip steering" (Section 4.2). However, no experiment measures γ across multiple layers/models and shows that steering succeeds when γ is high and fails when low, measuring actual behavior change (not just logit shift).

- **Generalization bound (Theorem 6.1) follows directly from Pinto et al. (2024).** The Rademacher-complexity result plugs the rank-k IAS structure into an existing bound from Pinto et al. The bound is vacuous unless k/d is very small. This is a reasonable addition but limited in novelty and practical impact.

### Trivial
None.

## Nice-to-Haves

- Demonstrate the full workflow end-to-end: steer → compute ρ_s → identify causal training examples → remove them → show behavior changes.
- Validate γ as a predictive diagnostic across multiple layers and at least one larger model.
- Systematically vary perturbation magnitude α and characterize the regime where first-order approximation holds (e.g., show how the slope changes with α).
- Discuss the IAS vs. CAA comparison honestly, explaining the different optimization objectives and what IAS offers that CAA does not.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Core theoretical equivalence is straightforward linear algebra repackaged"** — While the underlying tools (pseudoinverses, principal angles) are standard, the specific duality construction, γ diagnostic, spectral optimality theorem, and ρ_s data attribution connection are non-trivial contributions that go beyond textbook linear algebra. The harsh critic overstates this.

- **"The heuristic would suggest layer 10–11"** — Factually incorrect. The paper's heuristic says "smallest layer index with γ ≥ 0.7," which given the monotonic increase from 0.64 to 0.94 would suggest approximately L2-3, not L10-11. The broader point that L8 isn't justified is retained above with corrected reasoning.

- **"Theorem 6.2 is essentially a restatement of Theorem 5.1"** — Theorem 6.2 is stated differently and provides a distinct impossibility result (no activation perturbation can achieve more than ρ-fraction of desired displacement when γ ≤ ρ). While related to Theorem 5.1, it serves a different purpose (impossibility vs. error bound).

- **"The feasibility assumption is unexamined"** — While it's true that no experiment directly measures how often Im(J_θ→y) ⊆ Im(J_h→y) holds, the γ diagnostic itself serves as an empirical measure of this assumption's validity, and Figure 2 does measure γ across layers.

- **"Claims about 'first' to give closed-form map"** — Per hard rules, I cannot verify whether prior work established this connection. The paper's claim (line 275) stands as stated.

## Novel Insights

The paper's genuinely novel contribution is the constructive proof that activation steering and influence functions are first-order duals of each other, with the signed measure ρ_s providing a direct bridge from any steering intervention to a weighting over training examples. The γ principal-angle diagnostic is a practical tool that neither community had before, and the spectral optimality theorem (Theorem 5.3) replacing ad hoc direction selection with a principled Fisher-based recipe is a clear advance. However, the experimental validation does not yet demonstrate these tools working at scale or in the full end-to-end workflow the paper envisions.

## Suggestions

1. **Address the slope-1.50 issue directly.** Run experiments varying α and plot the slope vs. perturbation magnitude. Report the operating range where the first-order approximation is quantitatively accurate (e.g., slope between 0.9 and 1.1). This is critical for practitioners.

2. **Demonstrate ρ_s data attribution on at least one realistic task.** Take a known failure mode (e.g., a biased output), compute IAS and ρ_s, inspect top-weighted training examples, and validate by removing/relabelling them. This single experiment would dramatically strengthen the paper's practical contribution.

3. **Add one larger model (GPT-2 Large/XL or a modern small LM).** Repeat the γ ablation and first-order equivalence check to establish that the framework's assumptions hold beyond a single architecture size.

4. **Discuss Table 1 honestly.** Acknowledge that IAS underperforms CAA on detoxification, explain why this might be expected (different optimization objectives), and clarify what unique value the IAS construction provides beyond raw detoxification performance.

## Score and Decision

**Calibration anchors retrieved:**

| Round | Anchor | Avg Score | Comparison |
|-------|--------|-----------|------------|
| 1 | z1yI8uoVU3 (Steered Representation Measurement) | 3.0 | Weaker — purely empirical, no theory |
| 1 | fdvSCcB7i8 (Feature Level Instance Attribution) | 3.0 | Weaker — incremental, no unification |
| 1 | v5lmhckxlu (Linear-Nonlinear Feature Influence) | 3.4 | Weaker — less novel contribution |
| 1 | qJkCEcd50n (Manipulating Influence Attributions) | 3.0 | Weaker — narrow attack paper |
| 1 | 9wjGUN65tY (Conceptors for Steering) | 5.0 | Similar — theoretical steering framework with limited experiments; this paper has stronger theoretical contribution (duality vs. optimal affine steering) |
| 1 | 2XBPdPIcFK (ActAdd / Steering with Activation Engineering) | 5.0 | Different focus — purely empirical steering paper |
| 1 | KjBG4JNOc2 (Enhancing Training Robustness via Influence) | 6.2 | Comparable — influence-based method with experiments on real data; this paper has more novel theory but weaker experiments |
| 1 | HE9eUQlAvo (What Data Benefits My Classifier) | 6.4 | Slightly stronger — cleaner practical story with demonstrated data selection |
| 1 | PBjCTeDL6o (UNI: Unlearning-based Interpretations) | 8.0 | Stronger — comprehensive experiments across architectures |
| 1 | esYrEndGsr (IF for Diffusion Models) | 8.0 | Stronger — scalable method with broad validation |
| 1 | uHLgDEgiS5 (Temporal Dependence of Data Influence) | 8.0 | Stronger — cleaner theoretical contribution with good experiments |
| 1 | 8xxEBAtD7y (Unifying Mechanistic Interpretations) | 7.3 | Stronger — more complete experimental validation |
| 2 | dVq2StlcnY (Subgraph Multilinear Extension) | 5.75 | Comparable — theoretical framework with limited experiments |
| 2 | v675Iyu0ta (Interpretability Illusions) | 5.6 | Similar level — interesting finding but limited scope |
| 2 | INqLJwqUmc (Narrowing Info Bottleneck for CLIP) | 5.25 | Similar — theoretical contribution with limited experiments |
| 2 | 6zVElUoc6l (Interpretability of Ensembles) | 5.6 | Similar — theoretical analysis, limited experiments |
| 2 | 9m02ib92Wz (DataInf) | 6.0 | Comparable — scalable influence with clean experiments; this paper has more novel theory but weaker practical validation |
| 2 | Vz0CWFMPUe (TimeInf) | 5.8 | Similar — novel method with limited evaluation |

**Bracket:** Round 1 placed the paper between 5.0 and 6.5. Round 2 narrowed this to 5.5–6.0.

**Final positioning:** The paper has a genuinely novel theoretical contribution (the steering-influence duality) that exceeds the conceptors paper (5.0, rejected) in theoretical depth. However, its empirical validation is significantly weaker than DataInf (6.0, accepted) which demonstrated its method at scale on multiple models. The slope-1.50 issue and untested ρ_s data attribution are real concerns that DataInf and the diffusion IF paper (8.0) did not face — those papers demonstrated their core practical claims. The paper sits below 6.0 due to its unvalidated practical promises but above 5.5 due to the genuine novelty and elegance of its theoretical framework.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>