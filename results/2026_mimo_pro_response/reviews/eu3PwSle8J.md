Now I have a clear picture from the calibration. Let me finalize my review.

**Round 1 bracket**: Based on the calibration anchors, I estimate the paper falls in the 6.5–7.5 range. The paper is clearly above the ISE baseline (6.00, same topic, accepted with uniform 6s), comparable to ArrAttack (7.00, accepted, strong experiments on LLM security), and below the Shallow Safety Alignment paper (9.50, a fundamental insight). The PFT paper (4.25, rejected, weaker evaluation) and AutoHijacker (4.25, rejected) are clearly below this paper.

**Round 2 narrowing**: The paper's contribution (extending per-layer IH injection with systematic evaluation and strong results) is a clean step above ISE. It shares the "solid engineering improvement with good experiments" profile of the 6.5-7.5 band. The single-model motivation weakness prevents it from reaching the 7.5+ range, but the strong empirical results keep it above 6.5.

Final score: **7.0**

---

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a defense against prompt injection attacks in LLMs that injects instruction hierarchy (IH) signals into every decoder layer rather than only at the input layer. The method adds layer-specific trainable embedding tables to each decoder block, introducing ~0.005% extra parameters. Evaluations across three models (3B, 7B, 8B), two training methods (SFT, DPO), and multiple attack types demonstrate 1.6×–9.2× reduction in ASR on GCG attacks and up to 145× reduction on Astra attacks compared to the next-best IH injection method, with minimal utility degradation.

## Strengths
- **Large and consistent robustness gains across models and attacks**: Table 1 shows AIR achieves the lowest ASR on gradient-based attacks across all three models and both training paradigms, with specific examples like Llama-3.2-3B SFT GCG dropping from 38% (Delim) to 4.1% (AIR), and Astra dropping from 14.5% to 0.1%.
- **Conceptually clean and well-motivated method**: Section 4 draws an explicit analogy between AIR's per-layer injection and the evolution from input-only positional encodings to RoPE, grounding the contribution within a well-established architectural trend. Equation 1 is simple and clear.
- **Extremely low parameter overhead**: Section 4 quantifies that AIR adds only 0.4M extra parameters to Llama-3.1-8B (0.005% increase) with negligible inference cost.
- **Systematic evaluation design**: All three IH injection mechanisms (Delimiters, ISE, AIR) are evaluated with both SFT and DPO training across three model scales, enabling clean attribution of improvements to the injection mechanism. This goes beyond what any single prior work explored.
- **Multi-benchmark evaluation**: Results on both AlpacaFarm (static + gradient-based attacks) and the SEP benchmark demonstrate the gains are not benchmark-specific, with AIR-DPO achieving the best utility×separation tradeoff on SEP (Figure 8).
- **Minimal utility degradation**: Figure 6 shows at most <2% win rate degradation compared to non-adversarially trained baselines, with several configurations actually improving utility (e.g., Llama-3.2-3B DPO: 85.4% vs. 80.3% baseline).

## Weaknesses

### Fatal
None

### Major
- **Core motivational analysis only demonstrated on one model**: Figure 3 — the foundational evidence that IH signals degrade through decoder layers — is computed only on Llama-3.2-3B with 100 prompts from AlpacaEval (Section 3, line 87: "we encode 100 prompts from the AlpacaEval dataset...of the Llama-3.2-3B model"). The paper studies three models in its robustness experiments but does not replicate this analysis on Qwen-2.5-7B or Llama-3.1-8B. If the cosine similarity degradation pattern differs across architectures, the central motivational narrative weakens. The strong empirical results still stand, but the explanation of *why* AIR works rests on ungeneralized evidence.

### Minor
- **Unexplained Delim cosine similarity of 1.0 in Figure 3**: The Delim method shows exactly 1.0 cosine similarity across all decoder layers (lines 117-124), yet the paper offers no discussion. If delimiters don't create directionally distinct representations between privilege levels — which would suggest they shouldn't effectively distinguish privilege levels, contradicting their strong performance on static attacks — the diagnostic utility of cosine similarity is undermined for comparing IH methods. At minimum, this anomaly warrants a brief explanation or hypothesis.
- **Overgeneralized claim about DPO superiority**: Section 6.1 states (line 242): "adversarial training with DPO yields more robust models than SFT, corroborating results from SecAlign." While this holds for Delim and ISE, the pattern is mixed or reversed for AIR: on Astra, AIR-SFT achieves 0.1% vs AIR-DPO's 23.8% for Llama-3.2-3B and 0.1% vs 1.0% for Llama-3.1-8B. On GCG, AIR-SFT is better for Llama-3.2-3B (4.1% vs 5.2%). The paper should note that AIR partially disrupts the SFT/DPO gap rather than generalizing across all injection methods.

### Trivial
- **Different attack step counts for SFT vs. DPO not fully justified**: SFT models are optimized for 50 gradient-based attack steps vs. 200 for DPO (line 190). The paper acknowledges this asymmetry but does not fully justify it. While within-training-method comparisons remain fair, this limits cross-training-method robustness comparisons.

## Nice-to-Haves
- Extend Figure 3 cosine similarity analysis to Qwen-2.5-7B and Llama-3.1-8B to generalize the core motivational claim.
- Ablate which decoder layers benefit most from AIR (early vs. middle vs. late) to deepen understanding.
- Report error bars/variance for Table 1 ASR numbers; the paper already shows standard deviation in Figure 7's loss curves, so the data exists.
- Report AlpacaFarm win rate numbers in the main text rather than only in Figure 6 for precise comparison.

## Removed Points
These points are flagged to be removed, treat them with caution.
- The harsh critic's claim that the "145× significantly understates the improvement" is incorrect — the 145× figure is exact for Llama-3.2-3B SFT Astra (Delim 14.5% / AIR 0.1% = 145×). The critic's own recalculation (258×) appears erroneous.
- Weaknesses about testing on larger models (70B+) and using a fixed adversarial target phrase ("hacked!") are scope creep — 3B-8B models are standard in this literature and the fixed target is a reasonable simplification.
- Criticism about the abstract being "slightly broader" than the comparison is a minor nitpick that doesn't affect the paper's validity.

## Novel Insights
The paper's most interesting observation is that AIR partially eliminates the advantage DPO has over SFT in prior work — for AIR, SFT often matches or exceeds DPO robustness, particularly on Astra attacks. This suggests that per-layer IH injection reduces the need for preference-based adversarial training, as the architectural modification itself provides stronger privilege enforcement. The paper does not explicitly develop this insight, but it's visible in the data and worth highlighting.

## Suggestions
- Extend Figure 3 to all three models to generalize the core motivational analysis — this is the single highest-leverage improvement.
- Add a brief paragraph explaining or hypothesizing why Delim achieves 1.0 cosine similarity across all layers.
- Note explicitly in Section 6.1 that AIR partially disrupts the DPO>SFT pattern observed for other methods, as this is a noteworthy finding in its own right.

## Calibration Report

**Retrieved anchors across all rounds:**

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| sjWG7B8dvt.md (ISE) | 6.00 | 1, 2 | Direct baseline; AIR is a clear improvement with better evaluation and results |
| 6Mxhg9PtDE.md (Shallow Safety Alignment) | 9.50 | 1 | Higher impact — fundamental insight reframing safety alignment; AIR is more incremental |
| l3bUmPn6u5.md (PFT) | 4.25 | 1, 2 | Weaker evaluation, narrower problem; AIR is clearly stronger |
| 3MDmM0rMPQ.md (Inverse Prompt Engineering) | 3.00 | 1 | Much weaker contribution; clearly below AIR |
| rnJxelIZrq.md (Hypergraph Defense) | 6.50 | 1 | Novel perspective but unclear motivation; AIR has cleaner contribution |
| sULAwlAWc1.md (ArrAttack) | 7.00 | 1 | Strong experiments, similar profile; AIR is comparable |
| tTPHgb0EtV.md (Booster) | 8.00 | 1 | Alignment-stage solution; higher-scoring but different scope |
| kUH1yPMAn7.md (Safety Layers) | 6.00 | 2 | Related topic; AIR has stronger empirical results |
| 2VmB01D9Ef.md (AutoHijacker) | 4.25 | 2 | Attack paper, weaker; clearly below AIR |
| qIN5VDdEOr.md (LLMs know instruction following) | 6.00 | 2 | Different approach to instruction following internals |

**Bracketing**: Round 1 bracket: 6.5–7.5. The paper is clearly above ISE (6.00) and PFT (4.25, rejected), comparable to ArrAttack (7.00), and well below Shallow Safety Alignment (9.50). The systematic evaluation and strong results push it above 6.00-6.50 papers, while the single-model motivation analysis prevents it from reaching 7.5+.

**Final score**: 7.0 — a solid, well-executed paper with a clean idea, strong empirical validation, and minor weaknesses that don't undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>