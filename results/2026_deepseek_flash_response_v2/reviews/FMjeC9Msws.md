## Summary

This paper presents a large-scale empirical study (400k+ GPU-hours) proposing a sigmoidal compute-performance scaling framework for RL training of LLMs. The authors systematically ablate design choices (off-policy algorithm, loss function, precision, normalization, curriculum, etc.), characterizing each by its effect on asymptotic performance (A) and compute efficiency (B). The findings are distilled into the SCALERL recipe, validated at 100,000 GPU-hours where the sigmoidal extrapolation from 50k GPU-hours closely matches actual extended training. The paper demonstrates that stable, scalable RL recipes follow predictable sigmoidal trajectories, enabling extrapolation from smaller-scale runs.

## Strengths

1. **Predictive validation at 100,000 GPU-hours**: Figure 1a shows that fitting Equation (1) on the first 50k GPU-hours of an 8B dense run correctly extrapolates to 100k GPU-hours, with extended points closely tracking the predicted curve. This is direct evidence that RL compute-performance can be modeled and predicted at scales far beyond the fitting range, a result not previously established in the literature.

2. **Leave-one-out ablations at 16k GPU-hours each confirm that most components modulate efficiency, not asymptote**: Section 4 and Figure 5 show that when each SCALERL component is individually reverted, the asymptotic parameter A stays near 0.610 across variants while B varies substantially (1.62–2.01). This demonstrates that design choices shift efficiency rather than ceiling, validated with far more compute per ablation than prior RL studies.

3. **Cross-recipe comparison with extended validation**: Figure 2 fits sigmoids to five distinct recipes (DeepSeek GRPO, Qwen-2.5 DAPO, Magistral, MiniMax-M1, SCALERL) and verifies extrapolations by running each method longer. Extended points align with predicted curves for stable recipes, confirming the framework generalizes beyond a single method.

4. **Predictable scaling across multiple axes (model size, generation length, batch size)**: Section 5 demonstrates that the framework predicts performance when scaling generation length (14k→32k tokens), model size (8B→17Bx16 MoE), and batch size, with extrapolations matching extended training in each case.

5. **Actionable individual findings**: The isolation of FP32 precision at the LM head (Figure 4c, A: 0.52→0.61) and CISPO/GSPO vs. DAPO (Figure 4b, A: ~0.59 vs. 0.52) provide practitioners with clear, scaling-validated insights rather than point comparisons.

## Weaknesses

### Fatal

None.

### Major

1. **The scaling framework is validated through within-run extrapolation, not cross-condition prediction.** The core demonstrations (Figures 1, 2, 5, 6) follow the same pattern: fit on the first half of a run's own trajectory, extrapolate to the second half. This is self-consistency on a single trajectory, not the kind of cross-conditional prediction that makes pre-training scaling laws powerful (predicting a 175B model's loss from runs at 1B, 10B). The paper's abstract promises "predictive scaling methodologies comparable to those established for pre-training," and the introduction invokes the "science of RL scaling" (line 48), but the delivered framework is a within-run monitoring and extrapolation tool. While the paper acknowledges generalization limitations (line 241), the framing throughout sets expectations of cross-conditional power that are not demonstrated. This gap between framing and delivery runs through the entire paper.

### Minor

2. **No uncertainty quantification on fitted parameters.** The paper reports A, B, C_mid as point estimates from nonlinear curve fitting (4-parameter sigmoid) without confidence intervals or bootstrap estimates. In the short-run ablation regime (3.5k–4k GPU-hours), the early portion of a sigmoid is relatively flat, making asymptotic estimation fragile. Without uncertainty quantification, it is unclear whether reported differences in A and B are meaningful or within noise. The appendix may discuss fit robustness, but the main text lacks any quantification of uncertainty.

3. **Downstream generalization evidence is incomplete.** AIME-24 results (Figure 1b) are shown only for SCALERL, not for the baselines compared in Figure 2 or the LOO variants in Figure 5. Without this, readers cannot assess whether iid validation improvements translate to harder held-out problems, or whether some methods generalize better per unit of validation gain. The paper acknowledges this gap (line 241) but it remains a limitation in the evidence.

4. **FP32 precision fix accounts for a substantial portion of SCALERL's advantage.** Figure 4c shows FP32 improves A from 0.52 to 0.61 (~17%). The paper is transparent about this, but the degree to which SCALERL's superiority over baselines (Figure 2) follows from this implementation fix rather than algorithmic design is unclear. If baselines did not use FP32 at the head, the comparison partly reflects engineering rather than scalable methodology.

5. **Fitting 4-parameter sigmoids on short-run data may be fragile for asymptotic estimation.** Many ablations use only 3.5k–4k GPU-hours (lines 123–124), and the paper notes some choices "destabilize beyond this scale." For unstable methods, the fitted A is essentially an artifact of early truncation. While the paper is transparent about this, comparisons of A values between stable and unstable methods are not on equal footing.

### Trivial

None.

## Nice-to-Haves

- Provide quantitative prediction error metrics (e.g., relative error between predicted and observed pass-rate at the extrapolation point, RMSE over the extrapolation region) rather than visual assessment alone.
- Demonstrate at least one cross-condition prediction: fit on one configuration (e.g., batch size X) and predict another configuration (batch size 2X) using a parameterized version of Equation 1 that incorporates the varying axis.
- Report downstream (AIME-24 or similar) results for the baselines and LOO variants to strengthen the generalization evidence.

## Removed Points

Points from the harsh critic or strength finder that were removed per filtering rules:

1. **Baseline comparison fairness (Harsh Critic #1)**: The critic questioned whether baselines in Figure 2 were faithfully re-implemented and whether the comparison was staged, noting that the main text lacks details referenced in Appendix A.17. Per hard rules, the parser strips appendices from all papers; the details exist in the original submission. This criticism is removed.

2. **Reward overfitting / data contamination concern**: Raised as a speculative risk ("raises the risk that...") without concrete evidence from the paper — not a specific identified problem.

3. **Related work described as "ungenerous"**: Opinion-based characterization, not a concrete weakness.

4. **Generic strengths from Strength Finder**: Strengths about the problem being "important" or "timely" without specific evidence were removed as generic/superficial.

5. **Formatting/style nitpicks**: Removed per hard rules on parser artifacts/presentation issues.

6. **FP32 being dismissed as "hardware/implementation issue"**: The paper clearly identifies this and incorporates it as a validated design choice. The concern is retained but softened to Minor #4 (implementation advantage concern) rather than dismissed entirely.

## Novel Insights

The most interesting finding emerging from the reviews is the asymmetry between the "forward" ablations (starting from baseline, where individual choices shift both A and B) and the "backward" LOO ablations (reverting from SCALERL, where choices mostly affect B while A remains stable). This suggests that individual improvements interact synergistically: the cumulative effect is robust to reverting any single component, but each component's marginal contribution is modest. The paper surfaces this finding (line 240), but its implications for RL recipe design — that good recipes are built from many small efficiency gains rather than a single decisive breakthrough — could be more prominently featured as a key takeaway.

## Suggestions

1. Add confidence intervals or bootstrap uncertainty estimates on fitted A and B parameters throughout, particularly for the short-run ablations.
2. Either demonstrate that baselines used comparable implementation quality (e.g., all using FP32 at the LM head, similar off-policy setups) or explicitly acknowledge that SCALERL's advantage partially reflects implementation engineering rather than scalable methodology alone.
3. Report downstream results (AIME-24 or similar) for the baselines and LOO variants to strengthen generalization evidence.
4. Re-frame the central claim: the paper delivers a practical within-run extrapolation framework, not cross-conditional scaling laws comparable to pre-training. Adjust the abstract and introduction accordingly.

---

### Calibration Details

**Round 1 — Bracketing:**
- *Weak anchors (<3.5)*: "Improving Language Understanding Capabilities of LLMs Using RL" (3.00), "Honesty to Subterfuge" (3.00), "The Role of Task Complexity in Emergent Abilities" (3.00). Our paper is clearly far stronger than these.
- *Middle anchors (3.5–7.5)*: "Does RLHF Scale?" (5.50), "Scaling Laws for Imitation Learning in Single-Agent Games" (6.20), "A Hitchhiker's Guide to Scaling Law Estimation" (5.20), "LLMs Are In-Context Reinforcement Learners" (3.75). Our paper is stronger than all of these in terms of scale, methodology, and clarity of results.
- *Strong anchors (>7.5)*: "Scaling Laws for Associative Memories" (7.60), "Scaling Laws for Precision" (8.00), "Data Scaling Laws in Imitation Learning for Robotic Manipulation" (8.00), "RM-Bench" (8.00). These papers have cleaner novel contributions and broader validation.

**Round 2 — Narrowing:**
- *Middle-high anchors (5.5–7.0)*: "An Emulator for Fine-tuning LLMs using Small LMs" (6.50), "Inference Scaling Laws" (5.75), "Scaling Laws for IL in Single-Agent Games" (6.20), "From Reward Shaping to Q-Shaping" (5.67). Our paper is comparable to the 6.50 anchor and clearly stronger than the 5.67–5.75 ones.
- *High anchors (7.0–8.5)*: "Motif" (7.25), "Data Scaling Laws for Robotic Manipulation" (8.00), "WizardMath" (8.00). Our paper is weaker than these (cleaner novel contributions, broader validation).

**Final bracket**: 6.0–7.0. The paper sits solidly above mixed-quality papers (5.5–6.2) but below papers with clean novel contributions or broad validation (7.5+). Within this bracket, the paper is closest to the 6.50 anchor ("Emulator for Fine-tuning") in terms of contribution type and quality. Its large-scale empirical validation, systematic ablation methodology, and practical recipe make it a strong paper, but the overclaiming in framing and lack of uncertainty quantification prevent it from reaching the 7+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>