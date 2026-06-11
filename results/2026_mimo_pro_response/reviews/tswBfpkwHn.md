Now I have all the data I need. Let me write the final review.

## Summary
This paper presents the first theoretical analysis of one-layer Mamba's training dynamics and ICL generalization in the presence of outlier-contaminated prompts. By decomposing Mamba into a linear attention layer plus a nonlinear gating layer (Eq. 3), the paper proves that Mamba tolerates test-time outlier fractions approaching 1, while one-layer single-head linear Transformers are limited to α < 1/2. The paper further characterizes the ICL mechanism — linear attention performs pattern selection while gating suppresses outliers and induces exponential index-based local bias — and validates these insights empirically.

## Strengths
- **Clean architectural decomposition enabling direct comparison (Eq. 3):** The paper derives a closed-form expression showing one-layer Mamba equals a linear attention layer modulated by sigmoid-based gating functions G_{i,l+1}(w). This decomposition is the analytical backbone: setting G=1 recovers the linear Transformer, isolating gating as the sole architectural difference and enabling rigorous comparison.
- **Concrete quantified robustness gap (Theorems 2 & 4):** Theorem 2 (Condition c) shows Mamba generalizes when α < min(1, p_a·l_tr/l_ts), approaching 1, while Theorem 4 restricts linear Transformers to α ∈ [0, 1/2]. This is a measurable difference directly attributed to nonlinear gating, validated in Figure 2 across three outlier labeling regimes (label flipping, targeted, random), where Mamba maintains error < 0.01 for α up to 0.8 while linear Transformers fail for α > 0.5.
- **Mechanistic characterization with empirical validation (Corollaries 1 & 2):** Corollary 1 proves linear attention concentrates on context examples sharing the query's relevant pattern (Eq. 16). Corollary 2 proves gating suppresses outliers (Eq. 17: ≤ O(poly(M₁)⁻¹)) and induces exponential decay by index distance (Eq. 18: ≥ Θ(1/2^{j−1})). These predictions are verified experimentally in Figures 3 and 4 for three-layer Mamba, demonstrating the theory's explanatory reach beyond the one-layer analytical setting.
- **Honest trade-off analysis and sensitivity disclosure:** Remark 4 explicitly acknowledges that linear Transformers converge with smaller batch sizes, fewer iterations, and milder constraints. Table 1 transparently reveals Mamba's structural vulnerability: accuracy drops from 99.73% to 82.73% when outliers are positioned closest to the query (CQ), directly attributable to the exponential decay in Eq. (18). This honest documentation of a limitation strengthens credibility.
- **Generalization to distribution-shifted outliers (Theorem 2):** Test-time outlier patterns v_s' can be arbitrary linear combinations of training outliers with different magnitudes and a higher fraction α (Eq. 11), capturing realistic distribution shift. This goes beyond requiring test outliers to match training outliers exactly.

## Weaknesses

### Fatal
None

### Major
- **Comparison scope limited to linear Transformers reduces practical significance of the headline result.** The paper's central claim (α → 1 vs α < 1/2) applies specifically to one-layer single-head linear Transformers where G=1. The paper consistently qualifies "linear" throughout (Section 3.4 title, Contribution 2, Theorems 3-4, Remark 6), and Remark 6 acknowledges that large softmax Transformers can achieve favorable robustness. However, since the nonlinear gating being analyzed is contrasted against an architecture lacking its own nonlinearities, the structural comparison partly explains the gap: any architecture with an additional nonlinear component can outperform its gating-free counterpart in outlier suppression. The paper would be significantly strengthened by a more extended discussion in the main text (beyond Appendix B.1) of how the α < 1/2 threshold might change for softmax attention, even qualitatively.

### Minor
- **Condition (a) of Theorem 2 restricts test-time outliers to a positive-sum cone but is under-discussed.** Eq. (11) requires test outliers v = Σλᵢvᵢ* + u with Σλᵢ ≥ L > 0. This means, e.g., v' = -v₁* - v₂* - v₃* (sum = -3) would not be covered. Remark 3 notes the condition "captures a wide range of possible outlier patterns," but the restriction to positive-sum combinations is a non-trivial constraint. The experimental test outliers (line 241) deliberately satisfy this condition (sums: 0.9, 0.5, 0.3). A brief discussion with concrete examples of when this condition fails, or an experiment probing the boundary, would make the generalization claim more credible.
- **One-layer binary classification restriction limits generalizability claims.** The paper acknowledges this (line 29: "aligned with the scope of state-of-the-art theoretical studies"), which is fair. However, the three-layer experiments in Section 4.2 are presented as evidence that theoretical insights extend to deeper architectures. The paper could be more explicit about which aspects (gating suppression, exponential decay) are expected to persist vs. which might be artifacts of the single-layer setting.

### Trivial
None

## Nice-to-Haves
- Brief qualitative discussion in the main text about how the α < 1/2 threshold might differ for softmax Transformers, to help readers scope practical implications.
- An experiment or discussion probing when Condition (a) of Theorem 2 fails — testing with negative-sum outlier combinations to characterize the boundary of the guarantee.
- Discussion of whether architectural modifications (e.g., bidirectional scanning) could mitigate the outlier-position sensitivity revealed in Table 1.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh critic's framing concern about "linear" being buried in the abstract:** Upon verification, the abstract explicitly says "compared to the analysis of linear Transformers under the same setting" and "exceeds the threshold that a linear Transformer can tolerate." The paper consistently uses "linear Transformers" in Contribution 2 (bolded), Section 3.4 title, Theorems 3-4, and throughout. The framing is accurate and consistent, not misleading.
- **Harsh critic's claim that the result is "less surprising" because Mamba has nonlinearities and the linear Transformer does not:** This is a structural observation about the experimental design, not a flaw. The paper's contribution is precisely *isolating and quantifying the effect of nonlinear gating*, which requires comparing against the gating-free variant. This is the standard methodological approach in the ICL theoretical literature (line 187).
- **Harsh critic's concern about initialization specificity (diagonal δ):** This follows established conventions in prior ICL theory work and is not a novel choice warranting scrutiny.
- **Harsh critic's concern about κ_a bound tightness:** Standard sufficiency condition in this literature; demanding tightness analysis is scope creep for a theory paper.
- **Strength finder's claim about multi-layer validation:** The three-layer experiments in Section 4.2 are suggestive but not rigorous validation of theoretical generalization — they verify mechanism predictions (Corollaries 1-2) qualitatively, not the convergence/generalization theorems quantitatively.

## Novel Insights
The decomposition of Mamba into linear attention + nonlinear gating (Eq. 3) provides a clean analytical lens for understanding SSM architectures as attention variants with an additional suppression mechanism. The characterization that gating simultaneously suppresses outliers (Eq. 17) and induces exponential index-based decay (Eq. 18) — with the decay creating a structural vulnerability when outliers are positioned near the query (Table 1: 99.73% → 82.73%) — is a genuine insight connecting architectural structure to positional sensitivity in ICL. This dual role of gating (robustness benefit + position sensitivity cost) is a non-trivial finding that extends beyond existing ICL theory for Transformers.

## Suggestions
- Add a paragraph in the main text qualitatively discussing how the α < 1/2 threshold might change for softmax Transformers, given that softmax itself introduces nonlinearities that could provide some outlier suppression.
- Include an experiment testing with outlier patterns whose coefficient sums are negative or zero, to empirically characterize the boundary of Theorem 2's Condition (a).
- Discuss whether the local bias from Eq. (18) could be mitigated architecturally (e.g., bidirectional scanning), given the sharp performance drop in Table 1's CQ setting.

## Score and Decision

**Retrieved anchors (all rounds):**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Scaling IC-Light | u1cQYxRI1H | 0.50 | 1 | Unrelated topic (image harmonization) |
| KL Divergence GFlowNets | Uj0h13lVrR | 1.00 | 1 | Unrelated topic, weak paper |
| Nemesis Jailbreaking | 5kMwiMnUip | 1.40 | 1 | Unrelated topic, weak paper |
| Financial Markets NN | nSDOkm0SKo | 1.00 | 1 | Unrelated topic, weak paper |
| Mamba Neural Operator (PDEs) | VtP7CamOR5 | 3.00 | 1 | Mamba-related but PDE domain, rejected |
| Multimodal Instruction Tuning Hybrid SSM | cagNCwQEEN | 3.40 | 1 | SSM-related but vision, rejected |
| Normalization in Mamba | YK8eO7BEkJ | 3.00 | 1 | Mamba study, limited scope, rejected |
| Self-predictive Mamba MARL | 7ZyFjPUeJp | 3.00 | 1 | Mamba for RL, unrelated domain |
| Mamba Lyapunov-Stable | i9RTCC6whL | 4.67 | 1 | Mamba theory, scattered focus, rejected |
| SSMs learn in-context by GD | 52XG8eexal | 4.00 | 1 | SSM + ICL theory, limited novelty |
| Learning Mamba as Continual Learner | 1TXDtnDIsV | 4.67 | 1 | Mamba + CL, different domain |
| Mimetic Init for SSM Recall | iVy7aRMb0K | 4.50 | 1 | SSM init, different focus |
| Mamba (original) | AL1fq05o7H | 6.25 | 1 | Original Mamba paper (high variance) |
| LongMamba | fMbLszVO1H | 6.75 | 1 | Mamba engineering, different type |
| Samba hybrid SSM+attention | bIlnpVM4bc | 6.67 | 1 | Hybrid architecture, different focus |
| AR-NTP ICL Emerges | gK1rl98VRp | 6.00 | 1+2 | ICL theory, comparable quality |
| Oscillatory SSMs (LinOSS) | GRMfXcAAFh | 8.00 | 1 | New SSM architecture, much stronger |
| Context-Parametric Inversion | SPS6HzVzyt | 8.00 | 1 | ICL phenomenon, different focus |
| Amortized Control SSM | 8zJRon6k5v | 8.00 | 1 | SSM for time series, unrelated |
| Temporal Dependence of Influence | uHLgDEgiS5 | 8.00 | 1 | Data influence, unrelated |
| In-context vs In-weight Learning | aKJr5NnN8U | 6.50 | 2 | ICL theory with gating, comparable |
| Nonlinear Transformers for CoT | n7n8McETXw | 6.50 | 2 | Very similar: first training dynamics analysis, comparable structure |
| Trained Transformer Classifiers | jwsPS8yRe4 | 6.00 | 2 | ICL generalization theory, comparable |
| SSMs Comparable to Transformers | QFgbJOYJSE | 5.75 | 2 | SSM vs Transformer theory, weaker |
| Spatial-Mamba | iDe1mtxqK5 | 7.00 | 2 | Vision SSM, different focus |
| MambaTS time series | vEtDApqkNR | 5.60 | 2 | Mamba engineering, rejected |

**Round 1 bracket: 5.5 – 7.0**

The paper is clearly above the 4.0–4.67 anchors (more complete theory, cleaner framework, better experiments) and comparable to the 6.0–6.5 anchors. The most relevant comparison is "Training Nonlinear Transformers for CoT Inference" (avg 6.50), which has the same structure (first theoretical analysis of training dynamics, one-layer model, distribution-shifted test data, mechanism characterization) and similar scope limitations. Our paper adds the outlier robustness angle and the dual mechanism characterization (pattern selection + outlier suppression), but is limited by the linear Transformer comparison scope.

**Round 2 narrowed to: 6.0 – 7.0, landing on 6.5**

The paper is a solid, well-executed theoretical contribution with genuine first-results for Mamba in the ICL setting. It sits squarely in the accept range for this type of work, matching the quality level of comparable accepted papers at 6.0–6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>