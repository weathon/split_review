Now I have enough calibration data. Let me finalize the review.

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a method for defending against prompt injection attacks by injecting instruction hierarchy (IH) signals at every decoder layer of an LLM rather than only at the input layer. The core insight—supported by a cosine similarity diagnostic (Figure 3) showing IH signal degradation through layers—is that per-layer IH injection yields substantially stronger robustness than input-only injection (ISE, Delimiters). Evaluated across 3 models, 2 training methods (SFT, DPO), multiple attacks, and 2 benchmarks, AIR achieves consistently lower ASR against gradient-based attacks with minimal utility degradation.

## Strengths
- **Direct diagnostic evidence for the core hypothesis.** Figure 3 shows cosine similarity between hidden representations of differently-privileged tokens increases (IH signal degrades) through decoder layers for Delim (1.00→1.00) and ISE (0.55→0.92), while AIR maintains lower similarity (0.55→0.88). This directly validates the motivating hypothesis that input-only IH injection is insufficient.
- **Large, consistent ASR reductions against gradient-based attacks (Table 1).** AIR achieves the lowest ASR for GCG and Astra across all three models and both training methods. For GCG-DPO: Qwen-2.5-7B 1.6% vs. next-best ISE 7.7% (4.8×); Llama-3.2-3B 5.2% vs. next-best Delim 29.1% (5.6×). For Astra-SFT: Llama-3.2-3B 0.1% vs. next-best Delim 14.5% (145×).
- **Comprehensive evaluation matrix (3 models × 2 training methods × 3 IH mechanisms × multiple attacks).** This enables clear attribution of gains to the injection mechanism. The paper evaluates combinations not explored in prior work (e.g., ISE+DPO, AIR+DPO), systematically mapping the design space.
- **Minimal utility degradation (Figure 6).** AIR maintains win rates comparable to non-adversarially trained baselines—<2% degradation at most (Qwen-2.5-7B with DPO).
- **Negligible parameter and inference overhead (Section 4).** For Llama-3.1-8B with 3 privilege levels, AIR adds only (32+1)×3×4096 = 0.4M parameters (0.005% increase). Inference cost is a table lookup + addition per layer.
- **Well-structured analogy to positional embedding evolution (Section 4).** The parallel between AIR's layer-wise IH injection and the evolution from input-only positional encodings to RoPE grounds the design in established architectural reasoning.

## Weaknesses

### Fatal
None

### Major

- **Missing ablation to decompose per-layer vs. input-level contributions.** As shown in Figure 2c and Equation 1, AIR includes ISE-style input-level augmentation plus per-layer augmentation at every decoder layer—making AIR a strict superset of ISE with ~33× more IH embedding parameters for a 32-layer model. The paper's core claim is that per-layer injection is the key advance (Section 1: "injecting IH signals recurrently across all layers of the LLM"). Without an ablation comparing (a) AIR-full, (b) AIR with per-layer-only (no input-level augmentation), and (c) ISE (input-only), it is impossible to determine whether the gains come from the per-layer mechanism specifically or simply from having vastly more total IH signal capacity. This is the single most important missing experiment.

- **Unequal attack budgets between SFT and DPO without justification.** Line 190: "we optimize a 100-token random prefix for 200 (DPO models) or 50 (SFT models) steps." This 4× difference is stated but never justified—no convergence evidence (e.g., ASR plateau plots) is provided showing 50 steps is sufficient for SFT models. Figure 7 shows loss curves but with different x-axis ranges for SFT (visually appears to plateau early) and DPO. This asymmetry means SFT results carry less evidentiary weight: AIR-SFT's 4.1% ASR at 50 steps on Llama-3.2-3B may understate vulnerability relative to AIR-DPO's 5.2% at 200 steps on the same model. The headline "1.6× to 9.2× reduction" spans both settings without acknowledging this.

### Minor

- **Inconsistent headline claim.** The paper states "1.6× to 9.2× reduction in ASR" (Abstract, line 9; Introduction, line 35; Conclusion, line 264). However, computing AIR vs. next-best defense from Table 1 for GCG: DPO ratios are 5.6× (Llama-3.2-3B), 4.8× (Qwen-2.5-7B), 1.43× (Llama-3.1-8B); SFT ratios are 1.76× (vs. ISE for Llama-3.2-3B), 1.62× (Qwen-2.5-7B), 1.6× (Llama-3.1-8B). The GCG range against next-best defense is approximately 1.4× to 5.6×. The "9.2×" may come from comparing to Delim rather than next-best (Llama-3.2-3B SFT: 38/4.1=9.3×), which would be an inconsistent comparison basis since Delim is not the second-best method.

- **Single fixed adversarial instruction.** All robustness evaluations use "print exactly 'hacked!'" (line 187). While standard in the literature, the paper does not acknowledge this as a limitation or discuss sensitivity to different adversarial objectives.

- **Notable outlier case underexplored.** AIR-DPO achieves 23.8% ASR against Astra on Llama-3.2-3B (Table 1), substantially higher than AIR's performance in other DPO settings (0.9%–1.6%). The paper defers Astra discussion to Appendix C but does not discuss this outlier in the main text.

### Trivial
None

## Nice-to-Haves
- Evaluate the cosine similarity diagnostic on deeper models (e.g., Llama-3.1-8B with 32 layers) to verify it generalizes beyond the 28-layer Llama-3.2-3B used in Figure 3.
- Report wall-clock training times for AIR vs. ISE vs. Delim to substantiate the claim that training overhead is "similar to prior works" (line 103).
- Decompose the Astra attack into its warm-start phase vs. GCG phase to understand where AIR's defense is most effective.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh critic's "lack of adaptive/architecture-aware attack evaluation"**: The paper evaluates against GCG and Astra, both of which use full model gradients (implicitly exploiting architectural information). Astra even includes an architecture-aware attention-loss warm-start. While an attack specifically targeting AIR's per-layer embedding tables is conceivable, gradient-based attacks already propagate through all layers and would naturally target these embeddings. This is a reasonable nice-to-have, not a methodological gap.
- **Harsh critic's "generalization beyond single adversarial target"**: Evaluating with multiple adversarial instructions would strengthen the paper but is standard practice across the prompt injection defense literature—prior work (ISE, SecAlign, StruQ) all use similar fixed-target evaluation.
- **Strength finder's Figure 3 values slightly off**: The strength finder stated "Delim reaches 0.92, ISE reaches 0.88" at layer 25; actual values from the paper's table are Delim=1.00, ISE=0.92. This is a minor error in the strength finder, not in the paper.

## Novel Insights
The paper's diagnostic contribution—using cosine similarity analysis to demonstrate IH signal degradation through decoder layers (Figure 3)—is genuinely useful beyond the method itself. It provides a principled, measurable basis for the per-layer injection design choice and could guide future defense mechanism design. The analogy to the evolution from input-only positional embeddings to per-layer RoPE (Section 4) is a clean conceptual framing that connects the IH defense problem to well-understood architectural insights. The systematic mapping of prior defenses onto the {IH injection mechanism} × {training technique} matrix (Section 5.3) is also a useful contribution for the community.

## Suggestions
1. **Add an ablation study**: Compare AIR-full vs. AIR-per-layer-only (remove input-level augmentation) vs. ISE (input-only). This is the single most impactful addition for understanding the method's contribution.
2. **Equalize or justify attack budgets**: Either use 200 GCG steps for both SFT and DPO, or provide convergence evidence (e.g., ASR vs. step plots for SFT models showing plateaus before step 50).
3. **Verify the headline numbers**: The "1.6× to 9.2×" claim should be checked against Table 1 with a consistent comparison basis (always vs. next-best defense, not vs. arbitrary baselines).

## Calibration Report

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| sjWG7B8dvt.md (ISE) | 6.00 | 1 | Direct predecessor; less comprehensive evaluation, no DPO combination, no cosine similarity diagnostic. Current paper is clearly stronger. |
| l3bUmPn6u5.md (PFT) | 4.25 | 1 | Weaker evaluation, narrower scope, rejected. Current paper substantially stronger. |
| V01FPV3SNY.md (RA-LLM) | 5.33 | 1 | Less comprehensive defense evaluation, rejected. Current paper stronger. |
| Q3oAX9HoH2.md (Nested Gloss) | 4.00 | 1 | Attack paper, weaker methodology, rejected. Current paper much stronger. |
| 3MDmM0rMPQ.md (IPE) | 3.00 | 1 | Weak safety paper, rejected. Current paper much stronger. |
| lUyYX9VFgA.md (CoDoT) | 3.00 | 1 | Weak safety paper, rejected. Current paper much stronger. |
| 5kMwiMnUip.md (NEMESIS) | 1.40 | 1 | Very weak jailbreak paper, rejected. Current paper much stronger. |
| 6QBHdrt8nX.md (SafetyAnalyst) | 3.33 | 1 | Weak safety moderation paper, rejected. Current paper much stronger. |
| tTPHgb0EtV.md (Booster) | 8.00 | 1 | Strong alignment paper with clean methodology. Current paper not as strong. |
| SPS6HzVzyt.md (Context-Parametric) | 8.00 | 1 | Strong theoretical insight paper. Current paper not as strong. |
| Bo62NeU6VF.md (Backtracking) | 8.00 | 1 | Novel safety technique with strong results. Current paper not as strong. |
| oZtt0pRnOl.md (DP ICL) | 8.00 | 1 | Strong privacy+ICL paper. Current paper not as strong. |
| YzxMu1asQi.md (Scaling Laws) | 6.50 | 2 | Accepted; interesting empirical finding but questioned practicality. Comparable contribution level. |
| eC4WlSZc4H.md (Robustness Over Time) | 6.75 | 2 | Interesting longitudinal study but rejected. Current paper has comparable or better methodology. |
| 4FIjRodbW6.md (TAR) | 5.83 | 2 | Accepted; tackles tamper-resistant safeguards. More ambitious threat model but similar evaluation depth. |
| 0VZP2Dr9KX.md (Baseline Defenses) | 5.25 | 2 | Survey/baseline study, rejected. Current paper stronger. |
| PNHGYziAsL.md (SPIN) | 5.50 | 2 | Prompt injection defense, rejected. Current paper stronger. |
| MsRdq0ePTR.md (PI Benchmark) | 5.25 | 2 | Benchmark paper, rejected. Current paper stronger. |

**Round 1 bracket:** Between 4.5 and 8.0. The paper is clearly above all rejected papers in the 4-5.5 range and above ISE (6.00), but below the top-tier accepted papers at 8.0.

**Round 2 narrowing:** Anchors cluster around 5.25-6.75. The Scaling Laws paper at 6.50 (accepted) is a close comparator—both are empirical studies with interesting findings and moderate novelty. The current paper is slightly stronger than Scaling Laws in evaluation comprehensiveness but has the missing ablation issue.

**Final positioning:** The paper is clearly above ISE (6.00) due to its stronger evaluation, broader design space exploration, and diagnostic evidence. It is comparable to the Scaling Laws paper (6.50) in overall contribution quality. The missing ablation prevents a 7.0+ score. The numerical inconsistencies and unexplained attack budget difference are minor issues that don't threaten the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>