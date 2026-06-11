I have all the calibration information I need. Let me now write the final consolidated review.

## Summary

**Bracket determination (Round 1):** After comparing against anchors across all bands, the paper clearly exceeds the strong-reject band (<2.5) and the 2.5–4.5 band. It sits well above papers with fundamental flaws. Within the 4.5–6.1 band, it is stronger than "A Multi-Power Law for Loss Curve Prediction" (6.00) which tested only up to 400M parameters with a purely empirical law. Comparing to the 6.0–7.5 band anchors — "Straight to Zero" (6.33), "Language models scale reliably" (6.50) — the paper is comparable or slightly stronger. **Initial bracket: 5.5–7.0.**

**Narrowing (Round 2):** Reading the topically closest anchors in full confirms the paper is stronger than "Scaling Optimal LR Across Token Horizons" (6.00) — broader scope, better theoretical grounding (noisy-quadratic model), and demonstrated applications beyond prediction. It is slightly stronger than "Straight to Zero" (6.33) — more findings, more applications, and a model release. It is comparable to "Language models scale reliably with over-training" (6.50). The paper has no fatal or major flaws; its weaknesses are framing and presentation issues. **Final score: 6.5.**

**Anchor trail (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| yx8bU8T5ZN.md | 2.33 | R1 | Much weaker — fundamental flaws |
| 8TbqoP3Rjg.md | 2.00 | R1 | Much weaker — narrow scope |
| BDisxnHzRL.md | 4.25 | R1 | Weaker — narrower scope, no model release |
| D5v491uCzm.md | 4.25 | R1 | Weaker — less novel contribution |
| FxNNiUgtfa.md | 7.25 | R1 | Stronger — more rigorous, but different topic (knowledge capacity) |
| KnoS9XxIlK.md | 6.00 | R1, R2 | Weaker — tested only up to 400M, purely empirical |
| PlZIXgfWPH.md | 5.75 | R1 | Weaker — different focus (landscape analysis) |
| 9D9VoONnn6.md | 5.67 | R1 | Different focus (theoretical HPO complexity) |
| Zihqr7qqpg.md | 4.67 | R1 | Weaker — narrower (HPO criteria study) |
| o9YC0B6P2m.md | 6.75 | R1, R2 | Comparable/lower — was rejected for fundamental equation flaws; our paper has no such flaws |
| iZeQBqJamf.md | 6.50 | R1, R2 | Comparable — both solid empirical studies |
| hrOlBgHsMI.md | 6.33 | R1, R2 | Slightly weaker — narrower scope, weaker theory |
| 5HCnKDeTws.md | 6.75 | R1 | Different topic (finetuning scaling) |
| WYL4eFLcxG.md | 6.00 | R2 | Weaker — narrower (only LR scaling), no applications |
| zfeso8ceqr.md | 6.00 | R2 | Different topic (optimizer comparison) |
| jjfve2gIXe.md | 6.50 | R2 | Different topic (emergent abilities) |

---

## Summary

This paper extends the training-loss-curve (TLC) collapse phenomenon from small-scale μP experiments (Qiu et al., 2025 on chess-move prediction) to practical LLM training up to 3.9B parameters with AdamW, weight decay, and co-scaled architectures. It identifies the normalized AdamW timescale τ, tokens-per-parameter ratio (TPP), and LR schedule as the three controls governing collapse, and demonstrates two applications: (1) using collapse residuals for early detection of training pathologies, and (2) using collapse for principled early stopping in hyperparameter tuning. The paper also releases the Celerity model family.

## Strengths

- **Extends collapse from toy μP experiments to practical LLMs.** Prior work (Qiu et al., 2025) demonstrated TLC collapse only on small autoregressive tasks (chess moves) with vanilla Adam and no weight decay. This paper shows collapse holds up to 3.9B parameters under AdamW with weight decay, co-scaled width/depth/batch size, across three fixed-TPP bands (20, 80, 234 TPP) — a non-trivial empirical extension.

- **Identifies τ as the unifying control determining TLC shape.** Section 3 (Fig. 3) shows that sweeping learning rate η, weight decay λ, or batch size B independently yields near-identical normalized curves whenever τ is matched. This goes beyond prior work by demonstrating τ's role as a *shape determinant*, not just an optimizer state variable. The noisy-quadratic model (Eq. 3) formalizes why the curvature factor h cancels under normalization — providing a theoretical basis for scale invariance.

- **Real-world diagnostic application with demonstrated impact.** The paper reports (Sec. 4, lines 204–206) that collapse residuals from a 1.8B run flagged a numerical instability at ~60% of training, while the raw loss curve showed no visible anomaly until ~90%. The team used this signal to identify the root cause (a loss kernel bug triggered at specific microbatch sizes) and successfully restart from before the divergence. This is an *in-production* validation, not a retrospective analysis.

- **Parametric surrogate model for early stopping.** The surrogate (Eqs. 4–5) fit on 111M-scale data transfers to 3.3B parameters (1000× fewer FLOPs). The "predicted best" early-stopping strategy (Fig. 9) selects optimal hyperparameters with negligible loss gap after 10–30% of training, outperforming the "current best" heuristic used in practice.

- **Celerity models on the compute-efficiency Pareto frontier.** Fig. 2 shows Celerity positions at the upper-left of accuracy-vs-compute against multiple open LLM families, with a specific comparison: Celerity achieves comparable accuracy to BTLm with 75% fewer training FLOPs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "signature of compute-efficient training" framing (Abstract, line 31) overstates what the evidence can support.** The paper shows that efficient training setups (optimal τ for fixed TPP) produce collapse and that inefficient setups (varying TPP/τ as in Llama-2) do not. This is consistent with collapse being a *consequence* of the recipe rather than an independent diagnostic that practitioners could check without already knowing the recipe is correct. The Llama-2 family in Fig. 1 (left) does not collapse, yet was clearly trained to high quality — so lack of collapse does not necessarily indicate inefficiency. The paper would be stronger framing collapse as a useful regularity that arises under well-understood conditions rather than an "independent marker." The conclusions could be recalibrated to match what the evidence shows without losing impact.

- **The theoretical narrative (Section 3) is built on μP, but Celerity uses CompleteP (line 164) without discussing whether the relevant scale-invariance properties transfer.** Section 3's analysis — scale invariance of curvature, hyperparameter transfer, the noisy-quadratic model — is grounded in μP. Yet Celerity uses CompleteP, with a single sentence stating it "was more efficient/reliable than μP" and a reference to an appendix figure. The paper does not discuss whether the curvature consistency (Noci et al., 2024) that theoretically explains collapse under μP also holds under CompleteP. This decouples the paper's theoretical narrative from its empirical flagship. The empirical results stand on their own (collapse is clearly observed in Celerity), but the theoretical framing should acknowledge this gap.

- **The early stopping evaluation (Sec. 5) is limited to λ (weight decay) tuning at two model sizes with only two baselines ("random" and "current best").** While "current best" is a realistic baseline (used in practice by Almazrouei et al., 2023), the evaluation does not compare against established HPO approaches such as successive halving, learning-curve extrapolation (Domhan et al., 2015), or Bayesian optimization with early termination. Additionally, the compute cost of training the 111M-scale surrogate models is not factored into the claimed savings — only the large-scale training budget is considered. The 10–30% savings figure may overstate the net benefit if the surrogate training cost is non-negligible.

- **No error bars or variance estimates for Celerity's downstream evaluation.** The 7-task average in Fig. 2 is presented without uncertainty. Given that the paper highlights collapse as robust "to the noise from inter-run variation" (citing Qiu et al., 2025), and that per-task breakdowns are relegated to the appendix, the absence of inter-run variance in Celerity's own evaluation is a notable omission.

### Trivial
None that survive filtering.

## Nice-to-Haves

- An explicit explanation of how τ was optimized for each TPP band (swept at small scale and transferred? what optimality criterion?). This is important for reproducibility.
- Sensitivity analysis of the normalization method. Eq. (1) uses final loss as the denominator, but the paper shifts to "early-align" normalization during training (line 194). The properties of different normalization choices and their impact on collapse quality are not explored.
- Expanding the early stopping evaluation to include τ or learning rate tuning (not just λ) would strengthen the generality claim.

## Removed Points

These points were raised by reviewers but are removed because they misread the paper or are not valid upon verification:

- **"Collapse at 234 TPP is acknowledged to be imperfect — in a way that undercuts the main claim."** (Harsh Critic #3): The paper is transparent about this at line 202, explaining the divergence as train/val dissociation. The core claim is about training loss curves, which do collapse. This is a caveat the paper openly acknowledges, not a weakness.
- **"The Celerity compute-efficiency evaluation mixes models from different years."** (Harsh Critic #4a): Standard practice in LLM model comparison papers.
- **"The Celerity Fit line is circular — fitted to Celerity points."** (Harsh Critic #4b): The fitted line is an extrapolation tool, not a frontier claim. The frontier claim is based on the data point positions.
- **"BTLm comparison is hard to evaluate."** (Harsh Critic #4c): The paper gives a specific quantitative claim (comparable accuracy with 75% fewer FLOPs), which is a meaningful comparison point.
- **Strength Finder generic strengths** (e.g., "this paper addresses an important problem"): These add no information and are removed.

## Novel Insights

The most interesting thing that emerges from these reviews is not present in the paper's own claims: the tension between the τ-based collapse framework and the fact that practitioners using raw-loss heuristics ("current best") have been doing something that is simultaneously reasonable (it works OK at some scales) and unreliable (it fails at 1.7B but works at 3.3B, per Fig. 9). The collapse-based method *unifies* these regimes by providing a principled alternative, but the paper does not highlight this specific failure pattern of standard practice as a motivation. Similarly, the training/validation divergence at 234 TPP is framed as a caveat but could be reframed as a finding: collapse on training loss is necessary but not sufficient for good generalization, and the divergence point itself may serve as an overfitting early warning. These are latent insights in the paper that only surface clearly when read in conjunction with the critiques.

## Suggestions

1. **Recalibrate the "signature" claim.** Replace the "signature of compute-efficient training" language with a more precise framing: "when τ and TPP are held fixed across scales and τ is chosen optimally for that TPP, collapse follows; failure to collapse under fixed-τ conditions signals a deviation from the assumed scaling regime." This is equally compelling but actually supported.

2. **Acknowledge the μP/CompleteP gap explicitly in the main text.** If CompleteP shares the relevant scale-invariance properties (consistent curvature), state this with a citation. If it does not, discuss what the theoretical analysis in Section 3 implies for Celerity and whether collapse under CompleteP stems from different mechanisms.

3. **Add at least one established HPO baseline** (e.g., successive halving or power-law extrapolation per curve) to the early stopping evaluation. Even a single additional baseline would significantly strengthen the claim.

4. **Provide a net-compute accounting for the early stopping procedure**, including the cost of training 111M-scale surrogate models, so readers can assess the actual savings.

5. **Add error bars or per-task breakdowns** to the downstream evaluation in the main text.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>