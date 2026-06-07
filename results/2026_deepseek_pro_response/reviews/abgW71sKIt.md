Now I have enough for final comparison. Let me write the final review.

**Round 2 comparison summary:**

- **STBLLM (6.00, Accept):** Also 1-bit LLM compression. Reviewers noted "incremental novelty," "combination of existing techniques," and "confusing evaluations." Our paper has a stronger diagnostic analysis (Section 3) and clearer evaluation, but similar incremental-novelty concerns.

- **PB-LLM (6.75, Accept):** Partially-binarized LLMs. Cleaner core idea (salient weight protection) but weaker evaluation (only one model size). Our paper has broader evaluation but less method novelty.

- **LLM-QAT (5.00, Reject):** QAT for LLMs. Limited novelty, large precision gaps. Our paper is clearly stronger.

Our paper sits between STBLLM (6.00) and LLM-QAT (5.00). The diagnostic analysis is stronger than STBLLM's, but the AMP theoretical thinness and under-ablated selective strategy pull it below. **Final score: 5.5, Borderline Accept.**

---

## Summary

This paper addresses 1-bit post-training quantization (PTQ) for LLMs. It identifies three failure modes of existing output-matching approaches through diagnostic analysis: layer-wise matching doesn't guarantee block-level improvement, activation errors accumulate causing proxy-target drift, and naive alignment disrupts token similarity in attention. The proposed solution (1) reformulates the objective from activation-conditioned error to output error with closed-form derivations, (2) adds an Attention Matrix Preservation (AMP) mechanism, and (3) selectively applies output alignment only to the last FC layer per block. Experiments across 8 OPT and LLaMA configurations show consistent improvement over existing 1-bit PTQ baselines.

## Strengths

- **Strong diagnostic analysis (Section 3, Figures 1–2):** The paper systematically isolates *why* output matching fails. Figure 1 demonstrates that ARB-X's layer-wise output matching can produce *higher* block-level loss than simple weight alignment, directly falsifying the intuition that output matching should always help. Figure 2 quantitatively tracks how activation-conditioned error diverges from true output error with depth, providing clear evidence of error accumulation. This analysis is the paper's most valuable contribution.

- **Consistent empirical gains across diverse model families and scales (Tables 1–2):** The method outperforms all baselines (PB-LLM, BiLLM, ARB-RC, ARB-X) at comparable bit-widths across 8 model configurations spanning OPT-1.3B through OPT-30B, LLaMA-2-7B/13B, and LLaMA-3-8B. Gains hold across C4, WikiText2, PTB, and zero-shot QA. For the hardest cases (OPT-1.3B, OPT-2.7B), perplexity reductions of 3–5 points over ARB-RC are meaningful and suggest the approach helps most where quantization damage is greatest.

- **Objective reformulation with clean derivations (Section 4, Eqs. 3–8):** Shifting from activation-conditioned error to output error (‖XW − X̂Ŵ‖) is well-motivated by the diagnostic findings. Closed-form solutions are derived for all parameters under the new objective. Table 4 isolates this change and confirms a consistent ~0.7 PPL improvement independent of other components, demonstrating the objective change matters on its own.

## Weaknesses

### Fatal
None.

### Major

- **AMP mechanism has thin theoretical justification and is primarily an architecture-specific fix:** The AMP mechanism (Section 4.1) uses sign(gradient) of a token-similarity element-wise product as a hard binary mask to gate each coordinate between the output-alignment update and no-update (Eqs. 9–11). There is no formal derivation connecting maximizing an element-wise product to preserving attention patterns — the connection is asserted rather than shown. Empirically, Table 3 reveals AMP provides a negligible ~0.13 PPL gain on OPT-6.7B while being critical (~10 PPL) on LLaMA-2-7B. The paper attributes this to RMSNorm vs. LayerNorm differences (line 263: "We hypothesize that this sensitivity arises because LLaMA uses RMSNorm instead of LayerNorm"), but this hypothesis is stated post-hoc and never experimentally tested. This makes AMP feel like an architecture-specific patch rather than a general contribution to 1-bit quantization.

- **Selective layer-wise strategy is a significant design choice with no ablation or rigorous support:** Section 4.2 reveals in a single sentence that output alignment is applied only to the last FC layer of each block, with weight alignment used for all other layers. Given the paper's core motivation is to fix output alignment, restricting it to one layer per block is a dramatic simplification. There is no ablation comparing output alignment on all layers vs. last FC only vs. other subsets. The justification ("it has the most direct impact on the block loss") is stated without evidence. This unexamined design choice may be doing substantial work, and without understanding why it is necessary, the paper's claim to have addressed the output-alignment problem is weakened.

### Minor

- **Reframing mismatch around "calibration data":** The first contribution claims the paper "systematically examine[s] the influence of calibration data on 1-bit PTQ," and the conclusion repeats "investigated the role of calibration data." But the paper contains no experiments varying calibration dataset, size, or data distribution. What it actually examines is the choice of optimization objective (weight error vs. activation-conditioned error vs. output error). Reframing the contributions around optimization objectives would be more accurate.

- **PTB regression on LLaMA-2-7B:** On PTB, the proposed method achieves 3166 PPL vs. ARB-RC's 763 (full precision: 37.91). While all 1-bit methods struggle severely on PTB for LLaMA-2-7B (BiLLM: 5243, PB-LLM: 657), the regression relative to ARB-RC — the method the proposed approach directly builds on — warrants more than a brief dismissal ("the metric cannot provide a meaningful evaluation").

- **Incremental contribution over ARB-RC:** The method inherits its parameterization (Ŵ = diag(α_r) B diag(α_c)), alternating optimization framework, and closed-form derivation approach directly from ARB-RC. The three modifications are: (a) output-error objective (well-motivated), (b) AMP (architecture-specific), and (c) selective application (under-ablated). The diagnostic analysis in Section 3 adds significant value, but the method itself is a modest extension of existing work.

### Trivial

- **Equation (2) typo:** The left-hand side of Eq. 2 reads ‖X̂Ŵ − X̂Ŵ‖ which is identically zero. Based on context and the trace form on the right side, it should read ‖X̂W − X̂Ŵ‖.

## Nice-to-Haves

- Test the RMSNorm hypothesis directly by running AMP/no-AMP on architectures with LayerNorm vs. RMSNorm and measuring token-similarity degradation.
- Ablate the output-error reformulation in complete isolation (no AMP, applied to all layers) to isolate how much gain comes from the objective change alone.
- Ablate the selective layer-wise choice to understand which layers benefit from output alignment vs. weight alignment.
- Report per-token or per-sample statistics on PTB/LLaMA-2-7B to diagnose whether the collapse is driven by outliers or is systematic.
- Report compression ratios including scaling factors α_r, α_c, not just weight bits.

## Removed Points

These points are flagged to be removed, treat them with caution.

- *"AMP is theoretically weak and empirically unnecessary for OPT — potentially fatal"* → Demoted from fatal to major. The theoretical thinness is real but does not invalidate the core results. AMP does provide a small gain on OPT (0.13 PPL), so "unnecessary" overstates the case; more accurately, it is "minimally beneficial" on OPT.

- *"No experiment that swaps normalization layers"* → Removed as a standalone weakness. This is subsumed under the AMP major weakness and appears as a nice-to-have suggestion.

- *"Does not discuss why BitNet achieves competitive performance"* → Removed. BitNet is a training-based approach; the paper's scope is PTQ. Scope creep.

- *"Analysis uses ARB-X as the sole representative of output matching"* → Removed. ARB-X is the primary output-matching method in 1-bit PTQ. The conclusions are appropriately qualified as being about ARB-X's implementation; there are few alternatives to compare against.

- *"No measure of variance across seeds/calibration sets"* → Removed. Single-run evaluation is standard practice for large-scale LLM PTQ. This is a field convention, not a paper-specific flaw.

- *"Catastrophic PTB results undermine confidence — fatal"* → Demoted to minor. All methods fail on PTB/LLaMA-2-7B; the regression vs. ARB-RC on this one metric/model combination is notable but does not undermine the broad empirical results.

- *"Zero-shot QA relegated to appendix"* → The paper includes average QA accuracy (AveQA) in Table 1 for OPT models. LLaMA zero-shot results are in appendix. This is a reasonable presentation choice for space.

- *Strength removed: "Selective layer-wise strategy grounded in block-level analysis"* → Conflicts with the verified major weakness that this choice is under-ablated and under-justified. While the design was motivated by the Figure 1 finding, the paper provides no evidence that restricting to the last FC layer specifically is the right choice.

- *Strength removed: "Principled reformulation" as standalone* → Merged into the existing strength on objective reformulation, which already covers this.

## Novel Insights

The paper's most genuinely novel insight is the empirical decomposition of "output alignment" into two distinct objectives — activation-conditioned error (‖X̂W − X̂Ŵ‖) versus true output error (‖XW − X̂Ŵ‖) — and the demonstration that these systematically diverge as quantization proceeds through transformer blocks (Figure 2). The finding that layer-wise optimization of the former can increase block-level loss (Figure 1) challenges a widely-held intuition in PTQ and provides a clear motivation for the proposed objective reformulation. This diagnostic framework is a useful contribution to understanding PTQ behavior beyond the specific method proposed.

## Suggestions

- Reframe the paper around optimization objectives for 1-bit PTQ rather than "calibration data." The paper's real contribution is the diagnostic analysis of output-matching failure modes and the improved objective, not anything about calibration data per se. Contribution #1 should be rewritten accordingly.
- The paper would be strengthened by presenting itself primarily as an analysis paper with a simple, well-justified fix (the output-error objective), with AMP and selective application as supplementary heuristics. This would better align claims with what is actually demonstrated.

## Score and Decision

**Calibration anchors consulted:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| TJo6aQb7mK (Ternary LM pretraining) | 2.86 | R1 | Weaker: different approach (pretraining), narrower scope |
| 6Mdvq0bPyG (EfficientQAT) | 3.00 | R1 | Weaker: limited novelty, unfair comparisons, poor results |
| vw0NurJ7UX (PrefixQuant) | 3.00 | R1 | Weaker: activation quantization only |
| 0T8vCKa7yu (CVXQ) | 3.00 | R1 | Weaker: convex optimization approach, limited evaluation |
| ykhRO1mAg3 (FPTQ) | 4.00 | R1 | Weaker: limited novelty, unsupported speed claims |
| AEvu2ifH1r (PTNQ) | 3.67 | R1 | Weaker: non-linear quantization, different scope |
| mDBsBB1enO (LLM-QAT) | 5.00 | R2 | Weaker: QAT not PTQ, limited novelty, larger precision gaps |
| 0Ag8FQ5Rr3 (Super Weight) | 4.60 | R2 | Different scope: outlier identification, not quantization |
| 6XUSDvBFkV (STBLLM) | 6.00 | R2 | Comparable: 1-bit LLM compression, similar "incremental" concerns, but our diagnostic analysis is stronger |
| rAcgDBdKnP (OSTQuant) | 6.20 | R2 | Slightly stronger: cleaner method motivation, orthogonal transformations |
| B9klVS7Ddk (LLM-KICK) | 6.75 | R2 | Different scope: benchmark paper, not a quantization method |
| BifeBRhikU (PB-LLM) | 6.75 | R1/R2 | Stronger: cleaner core idea (salient weight protection), but narrower evaluation than ours |

**Round 1 bracket:** 4.5–6.5

**Round 2 narrowing:** The paper is clearly above LLM-QAT (5.00) and comparable to STBLLM (6.00). It shares STBLLM's incremental-novelty character but has a stronger diagnostic analysis. It sits below PB-LLM (6.75) due to the AMP theoretical thinness and under-ablated selective strategy. Final placement: **5.5**, borderline accept — the diagnostic analysis and consistent empirical results warrant acceptance, but the methodological gaps prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>