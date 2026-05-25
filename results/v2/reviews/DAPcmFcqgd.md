Now I have all the calibration data I need. Let me organize my final review.

**Calibration Summary:**

Round 1 bracket: 3.0–5.5 (lower-mid range based on topical similarity and weakness patterns)

Round 2 narrowing:

| Anchor | Avg Score | Round/Query | Comparison to MoEP |
|--------|-----------|-------------|---------------------|
| MOEfication by Experts as Masks (762u1p9dgg) | 3.40 | R1-topic-low | Similar weakness profile (weak experimental validation, missing ablations), but MoEP has clearer method |
| NanoMoE (04RLVxDvig) | 3.00 | R1-topic-low | Weaker experiments (toy only), MoEP is stronger |
| Free-MoE (J8LYjgi7nH) | 3.50 | R2-weakness | Similar rating, MoEP is clearer but also missing ablations |
| LokiLM (bppG9srkpR) | 3.60 | R2-weakness | Similar—no ablations, kitchen-sink. MoEP has more architectural novelty |
| Structural Pruning via NAS (VAwgL8kPvr) | 4.67 | R2-weakness | Stronger experiments, MoEP is weaker on evidence |
| Dense Backpropagation (huy8g3iKy0) | 5.50 | R1-weakness | Stronger methodology, MoEP is weaker |
| Quantifying Variance (E2RyjrBMVZ) | 4.17 | R1-weakness | Better experimental methodology |

The low-band anchors (2–4) share MoEP's key failure: thin experimental evidence for the central claim, missing ablations, and confounded comparisons. The mid-band anchors (4.5+) had more rigorous evaluation. MoEP is clearly in the lower band—the architecture idea is interesting but the experimental backing is insufficient.

The Round-1 bracket was 3.0–5.5. Round 2 anchors confirm MoEP sits at the lower end of this range, comparable to the 3.4–3.6 rejects but with slightly more architectural novelty. Score: **3.5**.

---

Now let me write the final review.

**FILTERING DECISIONS (Harsh Critic points):**

1. "Evidence for main claim is thin" (single seed, no error bars) → **KEEP as Major**. Grounded in paper (single seed=42, no error bars reported). 

2. "MoEP-SwiGLU comparison is uninformative and unfair" → **KEEP as Major**. Grounded in Table 1/2. Changes expert type, FFN type, AND parameter count (38M vs 28M).

3. "No ablations isolate the contribution of any component" → **KEEP as Major**. Paper has no ablations. Grounded observation.

4. "Claims about 'outperforming all BabyLM baselines' are misleading" → **KEEP as Minor**. The paper qualifies this in Section 5.1 but the intro claim is unqualified.

5. "Background disproportionately long" → **REMOVE**. Subjective style preference, not a substantive weakness.

6. "Missing parameter breakdown" → **WEAKEN to Minor**. A nice addition but not critical.

7. "Load-balancing loss uses negative entropy" → The critic is factually wrong here. L = -∑ p_i log p_i IS the standard entropy (not negative entropy). However, the real issue (missing λ sign/values) is valid. Let me reframe: **KEEP as Minor** with corrected framing.

8. "λ hyperparameter values not reported" → **KEEP as Minor**. Grounded (Table 3 doesn't include them).

9. "Checkpoint selection concern" → **KEEP as Minor**. Reasonable concern about "fast evaluation" tasks not being specified.

10. "Table hard to read" → **REMOVE**. Formatting nitpick.

11. "Training dynamics show MoEP is less stable" → **KEEP as Minor**. Valid observation.

12. "No comparison to standard MoE that increases total params" → **WEAKEN to Nice-to-have**. Outside the paper's stated scope.

**FILTERING DECISIONS (Strength Finder):**

1. "Fixed parameter count while adding sparsity" → **KEEP**. Specific evidence in Table 2.

2. "Outperforms the BabyLM strict-small baselines" → **KEEP but quality as conditional**. MoEP outperforms GPT-2 baseline but not GPT-BERT causal (without AoA). Rephrase.

3. "Faster early learning" → **KEEP**. Supported by Appendix A.3.

4. "Systematic evaluation with diverse task suite" → **KEEP**. 14 tasks, standardized pipeline.

5. "Ablation on expert complexity" → **REMOVE**. This is NOT a clean ablation (confounded comparison). The Strength Finder mischaracterizes it.

**FUNDAMENTAL ISSUES CHECK:**
- 3 Major weaknesses survive (single seed/no error bars, no ablations, confounded SwiGLU comparison).
- These collectively undermine the core claim (can't be sure the 0.9-point gap is real or attributable to the proposed architecture).
- Score must be ≤ 3.5 per the rule. Score = 3.5.

Let me write the review now.

Actually, wait. Let me re-examine the "negative entropy" concern. The paper writes:

L_balance = -∑ p_i log p_i

This IS the standard Shannon entropy H(p) = -∑ p_i log p_i. It's positive (for probabilities). 

Then: L = L_CE + λ_block L_balance_block + λ_expert L_balance_expert

If λ > 0: Minimizing L means minimizing L_CE + λ*H(p). Minimizing entropy means making the distribution less uniform (more collapse). This is the OPPOSITE of load balancing.

The paper says "to encourage the use of stable expert and block utilization without collapse" - so they want balanced utilization. Using entropy as a loss with positive λ would encourage collapse, not balance.

So either:
1. λ is negative (entropy bonus/maximization) - common in RL for exploration
2. The formulation is different from what's written
3. λ is positive and the formulation is wrong for load balancing

The critic says the paper uses "negative entropy" which would maximize entropy. But -∑ p_i log p_i is entropy, not negative entropy. If they used negative entropy (∑ p_i log p_i), that WOULD maximize entropy when added as a loss [since minimizing ∑ p_i log p_i means minimizing a negative quantity, which... let me think more carefully].

Actually, if L_balance = -∑ p_i log p_i (entropy), and we add it with λ > 0:
Min L = L_CE + λ*H(p)
Minimizing λ*H(p) means reducing entropy → more collapse → BAD for load balancing.

If we use negative entropy: L_balance = ∑ p_i log p_i (which is ≤ 0 since p_i ≤ 1)
Minimizing ∑ p_i log p_i (a negative number) means pushing it more negative, which means... actually ∑ p_i log p_i is also ≤ 0 (since log p_i ≤ 0). Making it more negative means making p_i smaller... Hmm, this is getting complicated.

The standard approach in many MoE papers is to use a load balancing loss like:
L_balance = α * N * ∑ f_i * P_i
where f_i is the fraction of tokens routed to expert i and P_i is the average routing probability. This penalizes imbalance.

The paper's approach (using entropy) is less standard. The issue is real but the critic's framing is wrong. Let me keep the concern but fix the framing.

Actually, re-reading the critic:
"The load-balancing loss (Eq. 2) uses negative entropy, which would maximize entropy (encouraging uniform routing)."

Wait, the critic says L = -∑ p_i log p_i is "negative entropy." But -∑ p_i log p_i IS the standard entropy (Shannon entropy). It's not "negative entropy." Negative entropy would be +∑ p_i log p_i.

However, the critic's overall point is valid: if we treat this as a loss to be minimized (λ > 0), then minimizing -∑ p_i log p_i means minimizing entropy, which encourages collapse. The critic correctly identifies that this is a problem, though their terminology is slightly off.

Let me reframe: The paper uses standard entropy as a load-balancing loss. For this to encourage uniform routing (which is the intended goal), it would need to be maximized (or used with negative λ). The paper doesn't clarify the sign or value of λ, leaving the formulation ambiguous.

OK, I'll include this as a Minor weakness with corrected framing.## Summary

This paper proposes MoEP (Modular Expert Paths), a sparse decoder-only architecture that combines layer-level top-k routing across parallel Transformer blocks with MoE-style linear projections to add token-level sparsity while keeping the total parameter count fixed. Evaluated on the BabyLM strict-small track, MoEP achieves macro-average scores of 49.00 (excluding AoA) vs. 48.10 for the authors' own GPT-2 baseline and 46.60 for the official BabyLM GPT-2 baseline, with the same 28M parameters. The paper also presents a SwiGLU-based variant and a training dynamics analysis suggesting faster early learning.

---

## Strengths

- **Fixed-parameter sparsity is demonstrated concretely.** Table 2 shows that MoEP has exactly 28M parameters, matching the dense GPT-2 baseline, even though it introduces multiple parallel blocks and expert routing. This directly supports the central architectural claim that sparsity can be added without increasing total parameters.

- **Directional improvement over the matched GPT-2 baseline.** MoEP achieves a higher macro average (49.00 vs. 48.10, Table 1) than the authors' own GPT-2 trained under identical conditions. While the gap is small and not statistically validated, it is at least directionally consistent with the claim.

- **Faster early learning is qualitatively documented.** Appendix A.3 shows that MoEP reaches its best evaluation scores at the 30M-word checkpoint and exhibits more comprehensive early learning than GPT-2, supporting the claim about improved sample efficiency.

- **Standardized evaluation on a diverse task suite.** The paper follows the full BabyLM strict-small protocol covering 14 zero-shot and fine-tuned tasks (Table 1), and releases code and model checkpoints for reproducibility.

---

## Weaknesses

### Major

- **Central result rests on a single run with no uncertainty quantification.** The main claim—that MoEP outperforms GPT-2—depends on a 0.9-point macro-average difference (49.00 vs. 48.10, Table 1). This is reported from a single training run (shared seed = 42) with no error bars, confidence intervals, or multiple seeds. Given the typical variance of BabyLM evaluation tasks, the observed gap could be within the noise floor. The shared seed ensures deterministic comparison but does not establish that the difference is meaningful or reproducible.

- **No ablations isolate the contribution of any architectural component.** The architecture combines (a) MoE shrink/grow blocks, (b) parallel layers with block-level top-k routing, and (c) a specific depth/width allocation that keeps total parameters equal to GPT-2. None of these choices is ablated. For example:
  - What if the parallel layers are dense (all P blocks active) instead of routed?
  - What if the MoE blocks are removed and the parallel stack operates directly at reduced dimension?
  - What if a simple dense model with a different depth/width tradeoff achieves similar results at 28M parameters?
  Without ablations, the paper cannot attribute the observed results to the proposed routing or sparsity; the gains could come from the changed depth-width allocation.

- **The MoEP vs. MoEP-SwiGLU comparison is confounded and uninterpretable.** MoEP-SwiGLU has 38M parameters vs. 28M for MoEP (Table 2), changes the expert type (linear → SwiGLU) *and* the FFN type in full layers (MLP → SwiGLU) simultaneously. The paper concludes that "lightweight linear experts are better at small scale" (Section 5.1), but this comparison cannot support that conclusion due to three simultaneous confounds (expert type, FFN type, parameter count). A controlled comparison at matched 28M parameters would be needed.

### Minor

- **The claim of outperforming "all BabyLM baselines" is misleading as stated.** The introduction (Section 1) says MoEP "was able to outperform all BabyLM strict-small baseline models." This is true only for the macro average *including* AoA (44.50 vs. 41.20 for GPT-BERT causal, Table 1). When AoA is excluded—arguably the more representative comparison since most models lack AoA scores—GPT-BERT causal achieves 54.10, substantially higher than MoEP's 49.00. Section 5.1 clarifies the AoA dependence, but the abstract and introduction do not.

- **The load-balancing formulation is ambiguous.** Equation 2 defines L_balance = -∑ p_i log p_i, which is the standard Shannon entropy. For this to encourage uniform routing (the stated goal), it must be *maximized* during training, which requires a negative λ coefficient when added to the cross-entropy loss as in Eq. 3. The paper describes λ as a "learning weight" without specifying its sign or value (Table 3 omits λ entirely). This makes the actual optimization unclear.

- **"Fast evaluation" task specification is missing.** The paper selects the final checkpoint based on "best fast-evaluation score" (Section 4) but does not describe what tasks constitute fast evaluation. If these overlap with the final BabyLM evaluation tasks, there is a risk of overfitting the checkpoint selection to the test set.

- **Lambda hyperparameters are not reported.** Table 3 lists all training hyperparameters but does not include λ_block or λ_expert from Eq. 3, which control the strength of the load-balancing regularizers. This omission hurts reproducibility.

- **Training dynamics reveal potential instability, not just faster learning.** Appendix A.3 shows MoEP "later begins to overfit" and its task scores "regress toward zero" after 90M words, while GPT-2 continues improving on some tasks. This contradicts the contribution claim of "stable training" and suggests modular routing may accelerate overfitting rather than providing sustained benefits.

### Trivial

- None

---

## Nice-to-Haves

- **Efficiency metrics would strengthen the "Compact and Efficient" framing.** The title promises efficiency, but no FLOPs per token, training throughput, or wall-clock time to best checkpoint are reported. Adding these would substantiate the efficiency claim.

- **A comparison against a standard MoE variant that *does* increase total parameters** (matching active parameters) would clarify whether MoEP's fixed-parameter sparsity provides a practical benefit over conventional MoE.

- **A parameter breakdown table** showing the distribution across components (full layers, MoE blocks, parallel layers) would aid reproducibility and verify the parameter-matching claim at a glance.

---

## Removed Points

These points were flagged during filtering but are not included in the main weaknesses above:

- **"Background is disproportionately long"** — Subjective style preference, not a substantive weakness. Removed.
- **"Table 1 is hard to read"** — Formatting/visual nitpick. Removed.
- **"Negative entropy" framing of load-balancing loss** — The critic misidentifies -∑ p_i log p_i as "negative entropy"; it is standard Shannon entropy. The actual ambiguity (missing λ sign/values) is preserved as a Minor weakness above with corrected framing. Removed (original framing).
- **Strength Finder: "Ablation on expert complexity"** — The MoEP vs. MoEP-SwiGLU comparison is confounded and cannot be interpreted as an ablation. Removed.
- **"No comparison to standard MoE that increases params"** — This is outside the paper's stated scope (fixed-param sparsity is the contribution). Moved to Nice-to-Haves.

---

## Novel Insights

The harsh critic's observation that MoEP's training dynamics show faster initial learning but potential overfitting later—and that this weakens rather than supports the "stable training" claim—is a genuinely insightful reframing that goes beyond what the paper itself acknowledges. The Strength Finder correctly notes the architectural novelty (fixed-param sparsity via layer-level routing), and both sources agree that the main weakness is evidentiary rather than conceptual.

---

## Suggestions

1. **Run at least 3–5 seeds and report confidence intervals.** Without this, the 0.9-point gap cannot be distinguished from noise. If the gap disappears with multiple seeds, the central claim collapses.

2. **Add controlled ablations within the same 28M parameter budget.** The most informative would be: a dense variant with no routing (all parallel blocks active), a variant without the MoE shrink/grow blocks, and a variant with a standard depth-width tradeoff at 28M.

3. **Re-run the SwiGLU comparison at 28M parameters** (e.g., by reducing the number of parallel layers or expert count) before drawing any conclusion about linear vs. SwiGLU experts.

4. **Clarify the load-balancing optimization** — specify the sign and value of λ_block and λ_expert, and explain how the entropy formulation (Eq. 2) is optimized to encourage balanced routing.

5. **Qualify the "outperforms all baselines" language** in the abstract and introduction to reflect the AoA dependency, or remove it and focus on the GPT-2 comparison which is the paper's primary point.

---

## Score and Decision

Based on the calibration analysis: the low-band anchors (3.0–3.6) that share MoEP's failure modes (thin experimental evidence, missing ablations, confounded comparisons) consistently received scores of 3–4 and were rejected. The mid-band anchors (4.5+) had stronger experimental methodology that MoEP lacks. The paper has a genuinely interesting architectural idea, but the three major weaknesses collectively undermine the core claim: without error bars, ablations, or a controlled SwiGLU comparison, the evidence is insufficient to conclude that the proposed routing and sparsity mechanisms are responsible for the observed results. Score reflects a paper with a promising direction but evaluation that falls short of conference standards.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>