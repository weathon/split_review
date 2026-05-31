Now let me run the calibration search to bracket the paper's score.Round 1 bracket: **5.0–7.0**. The closest topical anchors are ARB-LLM (7.00) and PB-LLM (6.75), which are both *baselines* in this paper. The paper under review extends ARB-LLM but has a notable failure case. Let me read those anchors and narrow the range.Good anchors read. Now Round 2 — narrowing within 5.0–7.0.Let me read the STBLLM anchor (6.00) and OmniQuant (6.40) to sharpen the calibration.Now I have enough information to write the final consolidated review.

---

## Summary

This paper investigates why naive output alignment fails for 1-bit post-training quantization (PTQ) of LLMs, identifying three failure modes: (1) layer-wise output matching does not guarantee block-level improvement, (2) quantization error accumulates across layers, causing the alignment target to drift from the true full-precision output, and (3) indiscriminate output alignment can degrade token-similarity structure and thereby attention masks. To address these, the paper proposes a selective last-layer output alignment strategy, reformulates the quantization objective using the true full-precision input X (Output Error) instead of the accumulated-error quantized input X̂, and introduces the Attention Matrix Preservation (AMP) mechanism that guards token-similarity structure via a masked update rule. Experiments on OPT (1.3B–30B) and LLaMA-2/3 families show consistent improvements over ARB-RC and ARB-X on C4 and WikiText2, with a significant unexplained failure on LLaMA-2-7B PTB.

---

## Strengths

- **Systematic diagnostic analysis grounding all three motivating observations (Section 3, Figures 1–2).** Figure 1 directly shows that ARB-X increases block-level loss on specific layers of LLaMA-2-7B despite reducing layer-level loss, providing concrete motivation for selective output alignment. Figure 2 quantifies error accumulation: the MSE between quantized and full-precision outputs grows with depth under ARB-X, and the token-similarity matrix diverges from the full-precision baseline—directly grounding the AMP motivation.

- **AMP mechanism yields large, measurable improvement on LLaMA architectures.** Table 3 shows removing AMP raises LLaMA-2-7B perplexity from 19.25 → 29.12 on C4 and 15.42 → 26.24 on WikiText2 (>10-point gap). The AMP objective (Equations 9–10) is derived from a principled token-similarity preservation criterion, and the masked update rule in Equation 11 is cleanly formulated.

- **Strong, consistent gains on OPT.** The method achieves the best perplexity across all OPT model sizes (1.3B–30B) on all three evaluation datasets (C4, WikiText2, PTB)—improvements range from 0.22 to 4.85 PPL on C4—and also achieves the best average QA accuracy (up to +0.59 pp over the strongest baseline ARB-RC).

- **Efficient closed-form optimization.** Equations 5–8 derive closed-form optimal solutions for α_c, B, and α_r incorporating the cross-term S = X̂ᵀX, maintaining efficiency without expensive iterative solvers and extending the ARB-RC parameterization to the Output Error objective.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained catastrophic failure on LLaMA-2-7B PTB (Table 2): perplexity 3166 vs. ARB-RC at 763.19 and ARB-X at 681.24.** The full-precision model achieves 37.91. While all 1-bit methods struggle on this benchmark (BiLLM: 5243; ARB-RC: 763; ARB-X: 681), the proposed method is 4.6× worse than the best baseline. The paper's single-sentence dismissal—"the large perplexity indicates that the metric cannot provide a meaningful evaluation"—is not a valid justification, because the baselines achieve far lower values on the same metric. This failure directly contradicts the paper's central claim of "consistent" improvement and raises an unresolved question: does AMP interact catastrophically with PTB-distribution inputs, or does the selective-layer strategy break down on this architecture + dataset combination? Without a diagnostic explanation, the robustness of the method cannot be assessed.

### Minor

- **The "last FC layer only" design choice in Section 4.2 is asserted but not ablated.** The paper states this layer "has the most direct impact on the block loss" as motivation, but provides no experiment comparing this choice against alternatives (e.g., attention output projection vs. MLP down-projection, first vs. last FC layer in each block, or applying to all layers). This is the structural differentiator from naive output alignment, and its correctness is assumed rather than demonstrated.

- **AMP remains a heuristic with limited understanding of failure conditions.** The update rule (Eq. 11)—keeping a parameter at its pre-optimal value when the AMP gradient sign conflicts with the main objective's optimum—has no convergence guarantee and is not ablated against alternatives (e.g., a jointly weighted objective). The dominant performance gains come from AMP (Table 3: ~10 PPL), yet when and why AMP fails (as evidenced by the LLaMA-2-7B PTB result) is not analyzed.

- **Framing overstates the contribution of the Output Error reformulation.** Table 4 shows that switching from Activation-conditioned Error to Output Error yields only ~0.72 PPL improvement on C4 for LLaMA-2-7B, while AMP accounts for the bulk of the gains (29.12 → 19.25 on C4, Table 3). The error-accumulation narrative in the Introduction—while diagnostically correct—is positioned as a primary driver, but empirically it is a secondary effect.

- **Block-level failure analysis (Figure 1) is restricted to a single model (LLaMA-2-7B).** The conclusion that ARB-X "does not necessarily improve block-level loss" is drawn from one architecture and one calibration set, which limits the generality of the stated finding.

### Trivial

- **RMSNorm hypothesis in Section 5.3 is speculative and not tested.** The paper hypothesizes that LLaMA's greater sensitivity to AMP arises from RMSNorm (vs. OPT's LayerNorm), which is stated explicitly as a hypothesis and is never verified experimentally.

- **No reporting of variance across calibration runs.** Small perplexity differences (e.g., 0.22–0.5 on LLaMA-2-13B) may not be reproducible.

---

## Nice-to-Haves

- A small ablation on selective-layer placement (last vs. first FC layer, attention vs. MLP output projection) would convert the design choice from intuition to evidence with minimal compute.
- A diagnostic experiment on the LLaMA-2-7B PTB failure—e.g., examining whether AMP masking or the layer-selection strategy behaves differently on PTB-domain input distributions—would directly address the most salient weakness while strengthening the method's mechanistic story.
- The overhead analysis, currently deferred to Appendix D, warrants at least a brief numerical summary in the main text, as "minimal overhead" is an advertised property.
- Quantifying variance across 2–3 calibration seeds would help distinguish signal from noise in the smaller improvements on LLaMA.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Equation 2 typographical error (both sides read X̂Ŵ).** Removed per the hard rule on formatting/parser artifacts. The correct formulation is stated in prose at line 19 and the subsequent Gram-matrix expansion is internally consistent.
- **Overhead analysis deferred to appendix.** Removed per the hard rule on missing/stripped appendix content.
- **Convergence guarantee for AMP update rule.** The harsh critic flags the absence of a convergence guarantee. This is a reasonable theoretical concern but demanding convergence proofs for a heuristic masking rule goes beyond what is standard in empirical PTQ papers; demoted to Nice-to-Have.
- **Variance / confidence intervals.** Removed from major weaknesses and moved to Trivial/Nice-to-Have; single-run evaluation is the norm in this subfield.
- **Framing of Figure 1 (caption says "ARB-X generally shows lower loss").** The harsh critic frames this as the paper misrepresenting the figure. Reading the paper directly (line 56–60), the caption accurately describes the figure; the text's argument is specifically about the exceptions. This criticism is based on a misreading.
- **Strength Finder claim of "14 of 15 combinations."** Partially true for Tables 1 and 2 combined, but this framing obscures that 15 of the 15 combinations include the catastrophic PTB failure. Removed as an overstated strength.

---

## Novel Insights

The paper's most genuinely novel observation—though underdeveloped—is that architecture choice (RMSNorm vs. LayerNorm) may determine whether output alignment is safe or catastrophic, and that token-similarity matrix preservation is the critical mechanism underlying this architecture sensitivity. If the PTB failure on LLaMA-2-7B could be diagnosed through this same lens (AMP preserving directional structure but interacting poorly with OOD token distributions), it would turn a weakness into a further diagnostic insight. The AMP formulation itself—framing quantization safety as preservation of the token-similarity proxy matrix—is a useful conceptual reframing for the 1-bit PTQ literature.

---

## Suggestions

1. **Diagnose the LLaMA-2-7B PTB failure specifically.** Check whether disabling AMP (reverting to baseline) recovers reasonable PTB performance; if yes, the AMP mechanism is responsible and the paper should characterize when AMP helps vs. hurts.
2. **Add a two-row ablation table for the "last FC layer" design choice** on one model/benchmark (e.g., LLaMA-2-7B C4) comparing last vs. first FC layer vs. attention output. This is the cheapest experiment with the highest explanatory value.
3. **Quantify error accumulation as a function of domain shift** (C4 → PTB) to explain whether the PTB failure is a calibration-distribution mismatch or a method failure.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| ZU8OdDLTts.md (ARB-LLM) | 7.00 | R1 | Direct predecessor with more novel contributions (ARB-RC, ARB-X, CGB all proposed there); paper under review is incremental relative to it |
| BifeBRhikU.md (PB-LLM) | 6.75 | R1 | Another 1-bit LLM paper; more diverse (PTQ+QAT); paper under review is roughly comparable |
| 6XUSDvBFkV.md (STBLLM) | 6.00 | R2 | 1-bit LLM binarization with incremental novelty; comparable to the paper under review in scope and novelty level |
| 8Wuvhh0LYW.md (OmniQuant) | 6.40 | R2 | PTQ with learnable block-wise calibration; broader scope but also criticized for limited novelty; paper under review has stronger analysis but a worse failure case |
| rAcgDBdKnP.md (OSTQuant) | 6.20 | R2 | PTQ with orthogonal/scaling transforms; similar evaluation breadth; paper under review is more focused |

**Round 1 bracket: 5.0–7.0.** Round 2 narrowed this to **5.0–6.5**.

**Positioning:**  
- This paper is clearly below ARB-LLM (7.00) — that paper introduced the ARB family from scratch; this paper is a targeted improvement on top of it.
- The paper is roughly comparable to STBLLM (6.00), which also had incremental novelty and evaluation concerns.
- The catastrophic, unexplained LLaMA-2-7B PTB failure — where the proposed method is 4.6× worse than its own baselines without explanation — is more concerning than the issues in STBLLM. This is a testable failure that the paper dismisses rather than diagnoses.
- The AMP analysis section is stronger than STBLLM's methodology section, but the lack of ablation on the selective-layer choice and the heuristic AMP update rule are genuine gaps.

**Final: 5.5, borderline reject.** The paper has real contributions (Section 3 analysis is solid; AMP is novel and effective on most benchmarks; OPT results are consistently strong), but the unexplained catastrophic failure on LLaMA-2-7B PTB directly undermines the consistency claim, and the dominant mechanism (AMP) lacks analysis of its failure conditions. These are not superficial concerns — they reflect an incomplete understanding of when the method works. The issues are fixable (a targeted diagnostic experiment on the PTB failure and a 2-row ablation on layer selection would substantially change the picture), but in the current form the paper is not ready for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>