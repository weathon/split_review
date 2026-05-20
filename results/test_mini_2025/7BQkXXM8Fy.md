## Summary

This paper conducts a large-scale empirical study of design choices in diffusion planners for offline RL, training over 6,000 models to evaluate action generation strategies, planning strides, denoising network backbones, network depth, and guided sampling algorithms. Based on the findings, the authors propose Diffusion Veteran (DV), a simple baseline that achieves state-of-the-art scores on Kitchen (83.8), AntMaze (83.2), and Maze2D (163.6). Key insights include the advantage of separate action generation (inverse dynamics) in high-dimensional action spaces, the competitiveness of Monte Carlo sampling with selection over guided sampling, and the superiority of Transformer over U-Net as a denoising backbone.

## Strengths

- **Large-scale systematic study filling a clear gap.** The paper trains 6,000+ models to ablate design choices that prior work handled inconsistently (action generation, planning stride, network backbone, guided sampling). This density of controlled comparisons (Sections 4.1–4.5) moves beyond the piecemeal decisions in previous diffusion planning papers and provides a useful reference for practitioners.

- **Action generation insight with a clear empirical boundary.** The finding that "Separate" (inverse dynamics) dramatically outperforms "Joint" in high-action-dimension tasks (Kitchen: 73.6 vs. 62.9 on Mixed, 94.0 vs. 53.7 on Partial; AntMaze: 80.0 vs. 49.9 on Large-Diverse) while both are comparable in low-dim Maze2D (Section 4.1, Figure 3) provides a principled, data-driven rule for resolving an inconsistency in prior work. This is actionable and non-obvious.

- **Strong baseline across multiple benchmarks.** DV achieves SOTA average performance on three task families (Kitchen 83.8, AntMaze 83.2, Maze2D 163.6 in Table 1), surpassing prior diffusion planners (Diffuser, DD, HD) and diffusion policies (DQL, IDQL). The margin in Kitchen (83.8 vs. next best 72.5 from HD) is substantial.

- **Attention visualization providing mechanistic evidence.** The analysis of Transformer attention weights (Figure 5b) shows that the model attends ~25 timesteps ahead and that this characteristic length is invariant across planning strides (6 steps × 4 stride ≈ 25 steps × 1 stride). This offers a mechanistic explanation for why Transformers outperform U-Net's locally-biased convolutions in planning tasks.

- **Practical, distilled takeaways.** Section 4.8 provides seven concrete recommendations (e.g., separate action generation, try jump-steps, Transformer backbone, MCSS when data contains near-optimal trajectories) that practitioners can directly apply. The taxonomy of when planning vs. policy methods are preferable (Section 4.6, Figure 8) is also useful.

## Weaknesses

### Fatal

None.

### Major

- **Internal contradiction between the jump-step claim and Figure 4.** Section 4.2 states: *"One crucial result we found is that jump-step planning is beneficial in almost all cases, despite the fact that most previous work used dense-step planning."* However, Figure 4 and its caption show that performance *decreases* as stride increases across all environments, and the star indicating DV's choice is at Stride=1 (dense-step). The caption explicitly states: *"In all environments, the performance generally decreases as the planner stride increases, with the star indicating the optimal stride."* Takeaway 3 ("Implementing jump-step planning can be highly beneficial") likewise contradicts the paper's own primary evidence. This is not a minor phrasing issue — the paper cites Figure 4 as evidence for the claim it directly contradicts. The text must be corrected to reflect what the data actually shows, or new evidence supporting jump-step must be presented. Note: this does not undermine the paper's other contributions, but it is a material error in a stated key takeaway.

### Minor

- **Transformer vs. U-Net claim slightly overstates the evidence.** The paper claims Transformer outperforms U-Net in "8 out of 9 sub-tasks." From the numerical table in Figure 5(a), the count appears to be 7 out of 9 (Antmaze-M and Antmaze-H favor U-Net). Even acknowledging possible OCR noise in the figure values, the claim is close to the data but not exact. The more important point — that Transformer is broadly preferable as a backbone — remains well-supported; the paper should simply report the exact numbers and temper the phrasing slightly.

- **Model selection procedure is underspecified.** The paper trains 6,000 models via "grid search and manual tuning" to obtain the best results (Section 3.2), then uses DV as the reference for controlled comparisons. It does not state whether the best configuration was selected on a held-out validation set or by examining test performance. Given the scale of the search, the concern about overfitting to the evaluation set is legitimate. A brief clarification (even one sentence) about how DV was chosen would resolve this.

- **Baseline comparisons lack matched experimental conditions.** DV's results are averaged over 500 seeds and come from extensive hyperparameter tuning, while baseline numbers are taken from literature (Table 1 caption). The paper does not discuss whether the baselines were tuned with comparable budgets or whether the same data splits were used. This does not invalidate the SOTA claim given the margins (especially Kitchen: 83.8 vs. 72.5), but it should be acknowledged.

- **No error bars in the main text for key comparisons.** The paper reports variance only in the (missing) appendix. The main text shows point estimates for comparisons like Transformer vs. U-Net and MCSS vs. CG/CFG. Including standard deviations or confidence intervals from the 500 seeds would significantly strengthen the empirical claims.

### Trivial

- Figure 5(a) OCR description contradicts its own data table (the description says Transformer wins all Antmaze sub-tasks; the table shows U-Net winning two). This is likely an artifact of describing a multi-colored figure, but it creates confusion in the text.

## Nice-to-Haves

- A summary heatmap or factorial table showing performance across all swept configurations would increase the paper's value as a reference, beyond the one-at-a-time control-variable comparisons.
- Reporting total GPU-hours (the paper mentions energy consumption but gives no concrete metric) would help contextualize the study's scale.
- A brief discussion of the planning horizon parameter \(H\), which is a key design choice that is swept but never analyzed in the main text.

## Removed Points

- **Criticism about missing appendix / proofs / references:** The parser strips these sections from all papers; they exist in the original submission. Removed per hard rules.
- **Criticism about the "Thinking, Fast and Slow" analogy being disconnected:** This is a discussion section analogy presented as speculative future direction, not a core claim. The paper does not claim experimental support for it. Removed as scope creep.
- **Criticism about MCSS conflating critic quality with guidance method:** This concern is acknowledged but the paper does not claim to control for this; it reports an empirical finding. Demoted from weakness to nice-to-have since addressing it would strengthen the analysis but is not a flaw in what was done.
- **Criticism about missing related work:** Per hard rules, I do not have external sources to verify completeness.
- **Strength Finder's claim about jump-step being beneficial:** This strength is directly contradicted by Figure 4. Removed per the rule that when a strength and verified weakness disagree, the weakness wins.
- **Generic strengths about the paper addressing an "important problem":** Removed as generic/superficial.
- **Formatting nitpicks and typos:** Removed per hard rules — these are parser artifacts.
- **Strength about "counter-intuitive findings" including jump-step:** Merged with the contradiction weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear contradiction between the jump-step claim and Figure 4, which is a problem the paper itself needs to resolve. The reviews do not identify any new insight about the paper's methodology or results that the authors had not already presented.

## Suggestions

1. **Resolve the jump-step contradiction.** The simplest fix: correct the text in Section 4.2 and Takeaway 3 to reflect that dense-step (stride=1) performed best in these experiments. If the appendix contains evidence supporting jump-step in other configurations, cite that properly. The text and figure must tell the same story.

2. **Clarify model selection.** Add one sentence explaining whether DV was chosen via a held-out validation set or by examining test results. This is a quick fix that addresses the overfitting concern.

3. **Provide exact numerical backing for Transformer vs. U-Net.** Report means and standard deviations from the 500 seeds, and adjust the "8 out of 9" claim to match the data precisely.

4. **Add error bars to all main-text figures** (or at minimum, note in captions where they can be found in the appendix).

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| btpgDo4u4j (Efficient Planning with Latent Diffusion) | 6.75 | R1 (mid) | Stronger — proposes new method, no internal contradictions. Our paper weaker. |
| tGQirjzddO (Reasoning with Latent Diffusion in Offline RL) | 6.33 | R1 (mid) | Comparable in contribution type (diffusion+RL), but no self-contradiction. Our paper slightly weaker. |
| o3pJU5QCtv (EC-Diffuser) | 6.25 | R2 | Similar score tier, proposes new method. Our paper has the contradiction issue. |
| WNxlJJIEVj (Contrastive Diffuser) | 5.25 | R1 (mid) | Weaker — incremental method, comparable results. Our paper has broader study. |
| x1SfON9HvT (Diffusion Modulation via Env Mechanism) | 3.75 | R1 (mid) | Weaker — rejected. Our paper has stronger empirical evidence. |
| PH7ja3T0vN (State Combinatorial Generalization) | 4.50 | R1 (mid) | Weaker — rejected. Our paper has more comprehensive evaluation. |
| ZGqlkqAt18 (Diffusion-Guided Safe Policy Opt) | 3.00 | R1 (low) | Unrelated topic, much weaker. |
| ANvmVS2Yr0 (Generalization in diffusion models) | 8.50 | R1 (high) | Unrelated topic, stronger. |

**Round 1 bracket:** 4.0 – 7.0  
**Narrowing rationale:** Within this bracket, the paper is stronger than rejected papers (3.75–5.25) due to the breadth of its study and the strong DV baseline. It is weaker than accepted papers proposing new methods (6.33–6.75) because of the internal contradiction in Section 4.2.  
**Final position:** Between "Contrastive Diffuser" (5.25, Reject) and "Reasoning with Latent Diffusion" (6.33, Accept). The paper's contribution as an empirical study is genuine and useful, but the jump-step contradiction prevents it from reaching the 6.5+ tier. Score set at 6.0 — marginally above the acceptance threshold, conditional on resolving the contradiction.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>