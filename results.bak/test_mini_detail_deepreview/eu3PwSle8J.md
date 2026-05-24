Now I have sufficient calibration. Let me synthesize the consolidated review.

**Bracket assessment:**
- Round 1 bracketing: The paper is clearly above the weak band (scores 1.4-3.0 — papers with unserious methods or trivial contributions) and above the middle band (4.25-5.50 — papers with significant flaws like PFT at 4.25 and SPIN at 5.50). It sits well above ISE (6.00), which is the most directly comparable paper (ISE is the baseline method AIR improves upon). The initial bracket is 6–8.
- Round 2 narrowing: The paper is stronger than ISE (6.00) on which it builds. It is comparable to "Catastrophic Jailbreak" (7.00) — both have a clear contribution, thorough evaluation, and minor weaknesses. The paper is clearly below the "Safety Alignment Should be Made More Than Just a Few Tokens Deep" (9.50), which is a breakthrough-level paper.
- **Final score: 7.0.** This is a well-executed paper with a clear contribution, thorough evaluation, and addressable weaknesses.

---

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks. The core insight is that prior methods inject instruction hierarchy (IH) signals only at the input layer (via delimiters or segment embeddings), and these signals degrade through deeper layers. AIR addresses this by adding trainable per-layer embeddings that inject IH signals into every decoder layer. Evaluations on Llama-3.2-3B, Qwen-2.5-7B, and Llama-3.1-8B with both SFT and DPO training show that AIR reduces gradient-based attack success rates by 1.6×–9.2× compared to the best prior method (Delim/ISE), while maintaining comparable utility.

## Strengths

- **Concrete diagnostic motivating the approach:** Figure 3 quantitatively shows that cosine similarity between representations of different privilege levels increases across decoder layers for Delim and ISE (e.g., ISE climbs from ~0.55 to ~0.92), while AIR maintains lower similarity (~0.55 to ~0.88). This provides direct empirical justification for the paper's central hypothesis that input-only IH signals degrade.

- **Consistent and large ASR reductions across diverse settings:** Table 1 reports that AIR achieves the lowest GCG ASR across all three models and both SFT/DPO training methods (e.g., Llama-3.2-3B SFT: AIR 4.1% vs. Delim 38%, a ~9.3× improvement; Llama-3.1-8B DPO: AIR 2.8% vs. ISE 4.0%). The pattern holds for the Astra attack with even larger margins (up to 145× for SFT). These improvements are consistent and systematic, not cherry-picked.

- **Comprehensive and fair evaluation:** The evaluation covers three model sizes (3B, 7B, 8B), two training paradigms (SFT, DPO), four static attacks, two gradient-based attacks (GCG, Astra), and two benchmarks (AlpacaFarm, SEP). All IH mechanisms are trained under identical procedures (same data, same epochs, same optimizer), ensuring apples-to-apples comparison. The parameter overhead is quantified (0.4M params, 0.005% for Llama-3.1-8B).

- **Minimal utility degradation with some improvements:** Figure 6 shows AIR's AlpacaEval win rate is within 2% of the non-adversarial baseline (None) in all cases, and in several cases AIR actually *improves* utility (e.g., Qwen-2.5-7B DPO: AIR 91.9% vs. None ~80%). On the SEP benchmark (Figure 8), AIR with DPO achieves the best utility×separation tradeoff for every model.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No ablation isolating injection depth as the causal factor.** The paper's core claim is that injecting IH signals at *all layers* (rather than just the input) drives the robustness improvement. The comparison between AIR (all-layer) and ISE (input-only embedding) is reasonably clean — both use additive trainable embeddings — but ISE uses a single shared embedding table while AIR uses per-layer tables with slightly more parameters. A direct ablation varying injection depth within AIR (e.g., input-only AIR, every-other-layer AIR, last-three-layers AIR, full AIR) would isolate the layer-wise injection as the causal mechanism and rule out confounds from per-layer specificity or extra parameters. The existing evidence is convincing but correlational; such an ablation would raise it to causal.

- **Logit-based ASR for gradient-based attacks, not generation-based.** For GCG and Astra, ASR is measured as "the likelihood (from model's logits) of generating the target phrase 'hacked!'" (Section 5.4). This is a proxy metric — high logit likelihood does not guarantee that a sampling-based generation will actually output the phrase under decoding. While the large margins (e.g., 4.1% vs. 38%) make it very unlikely that the pattern would reverse under generation-based metrics, the paper should validate this with greedy-decoding ASR for at least a subset of the gradient-based attack results to align with standard practice in the security literature.

- **Figure 3 (representation collapse diagnostic) shown only for Llama-3.2-3B.** The trend that motivates the entire approach is only demonstrated on the smallest model. Showing similar plots for Qwen-2.5-7B and Llama-3.1-8B would increase confidence that the degradation generalizes across model families and scales.

- **Utility improvements over None are not discussed.** The paper states AIR "generally does not significantly degrade model utility" (Section 6.1), but Figure 6 shows AIR sometimes achieves *higher* win rates than the non-adversarial None baseline (e.g., Qwen-2.5-7B DPO). This is an interesting and potentially important positive side-effect that warrants discussion (e.g., do the IH embeddings act as structured regularization?).

### Trivial

- The caption of Figure 6 could be more precise — the text says "no significant degradation" while the figure shows AIR sometimes outperforming None.

## Nice-to-Haves

- An ablation varying the number of privilege levels \(K\) (e.g., \(K=2,4\)) to test scalability beyond \(K=3\).
- An analysis of learned embedding norms per layer to understand whether certain layers learn stronger IH signals.
- A brief note on training FLOP overhead (though the parameter overhead is already given and inference overhead is negligible).

## Removed Points

**These points are flagged to be removed, treat them with caution:**
- Concerns about missing appendix content (adversarial dataset in Appendix B.1, Astra details in Appendix C). Per instructions, these sections are stripped by the parser and exist in the original submission. Not valid criticisms.
- Request for adaptive attacker analysis. The critic notes this is "a reasonable direction for future work rather than a requirement." Removed as scope creep.
- Criticism about "no evaluation of embedding dimension or initialization sensitivity." This is speculative and not a standard requirement for this type of contribution.
- The Strength Finder's generic strength about the paper addressing an important problem — true but generic, removed.
- Strength about the RoPE analogy providing "principled motivation" — this is a supporting analogy, not a core strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective on the paper that the authors themselves did not articulate.

## Suggestions

1. **Add an injection-depth ablation.** The most impactful addition would be to compare: (a) AIR embeddings at input layer only; (b) AIR at uniformly spaced layers (e.g., every 4th layer); (c) AIR at only the last three layers; and (d) full AIR. This would confirm the causal role of multi-layer injection.

2. **Report generation-based ASR for gradient attacks.** Run greedy-decoding generation on the attacked prompts (after GCG/Astra optimization) for at least one model+training combination to validate that the logit-based ASR translates to actual generation outcomes.

3. **Extend Figure 3 to at least one additional model** (e.g., Llama-3.1-8B) to show the representation-collapse diagnostic generalizes beyond the smallest model.

4. **Briefly discuss the utility improvement** seen in some AIR configurations over the non-adversarial baseline, with a plausible explanation.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `5kMwiMnUip.md` (NEMESIS) | 1.40 | R1 | Weak jailbreak paper; unserious method. Current paper is vastly stronger. |
| `MV5j4Qpq7N.md` (System-Prompt Attention) | 2.33 | R1 | Weak defense; limited evaluation. Current paper is much stronger. |
| `3MDmM0rMPQ.md` (Inverse Prompt Engineering) | 3.00 | R1 | Generic defense; weak results. Current paper is clearly better. |
| `lUyYX9VFgA.md` (Code-of-Thought) | 3.00 | R1 | Weak safety eval paper. Not comparable quality. |
| `l3bUmPn6u5.md` (PFT) | 4.25 | R1 | Prompt injection defense with weak attacks, unclear problem framing. Current paper is substantially stronger — evaluates on GCG/Astra, multiple models, clear contribution. |
| `0VZP2Dr9KX.md` (Baseline Defenses) | 5.25 | R1 | Survey/evaluation; mixed reviews (3,5,8,5). Current paper proposes a novel method and is more focused. |
| `PNHGYziAsL.md` (SPIN) | 5.50 | R1 | Inference-time defense with threshold sensitivity and limited models. Current paper is stronger — training-time architectural improvement with clean evaluation. |
| **`sjWG7B8dvt.md` (ISE)** | **6.00** | **R2** | **Most directly comparable — AIR's baseline. Accepted with 6,6,6,6. Current paper's method (AIR) clearly outperforms ISE, has stronger attack evaluation (GCG, Astra vs. just static), and provides a deeper diagnostic (Figure 3, SEP). The current paper is stronger.** |
| `8EtSBX41mt.md` (SEP benchmark) | 6.67 | R2 | Benchmark/dataset paper. Different contribution type but solid accepted paper. |
| `YzxMu1asQi.md` (Scaling Laws for Attacks) | 6.50 | R2 | More theoretical attack analysis. Different contribution type. |
| `e9yfCY7Q3U.md` (Improved GCG) | 6.25 | R2 | Incremental improvements to an attack. The current paper proposes a novel defense and is a stronger contribution. |
| **`r42tSSCHPh.md` (Catastrophic Jailbreak)** | **7.00** | **R2** | **Novel attack finding, comprehensive (11 models), scores 6,6,8,8. Comparable quality to current paper — both have a clear novel contribution and thorough evaluation with minor weaknesses.** |
| `eC4WlSZc4H.md` (Robustness Over Time) | 6.75 | R2 | Longitudinal study; rejected despite 6.75 (one reviewer gave 5). Different contribution type. |
| `6Mxhg9PtDE.md` (Shallow Safety Alignment) | 9.50 | R1 | Breakthrough-level paper with broad implications. Current paper is not at this level. |
| `syThiTmWWm.md` (Cheating Benchmarks) | 7.75 | R1 | Critique/analysis paper, different genre. |
| `tc90LV0yRL.md` (Cybench) | 8.67 | R1 | Benchmark framework paper. Different contribution type. |

**Round 1 bracket:** 6–8 (above middle anchors 4.25–5.50, below top anchors 7.75+).

**Round 2 narrowing:** The paper sits between the ISE paper (6.00) and the Shallow Safety Alignment paper (9.50). It is comparable to Catastrophic Jailbreak (7.00) — both have a clear novel contribution with thorough, multi-model evaluation and minor, addressable weaknesses. The current paper's evaluation is slightly more systematic (identical training procedures across methods, multiple benchmarks) but has slightly less breadth in models (3 vs. 11). The ISE paper at 6.00 is the most directly comparable baseline: the current paper improves upon ISE's method, evaluates against stronger attacks, and provides more diagnostic analysis — it is a clear step up.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>