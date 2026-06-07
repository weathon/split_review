Here is my final consolidated review:

---

## Summary

This paper introduces DaVinci, a two-stage framework (SFT + GRPO-based RL) that parses rasterized scientific diagrams into executable TiKZ code. The contributions are threefold: (1) a curated 30K-pair dataset TiKZ30K with drawing-order normalization and comment injection as planning scaffolds; (2) a hybrid reward function that uses vectorized PDF representations (via PyMuPDF) to compute spatio-textual and geometric rewards without relying on OCR; (3) achieving a 97.60% compile rate (Pass@1) on the DATiKZv3 benchmark, substantially exceeding both open-source and proprietary baselines on this metric.

## Strengths

1. **Near-perfect compile rate with clear attribution to RL post-training.** Table 1 shows DaVinci-7B achieves 97.60% Pass@1 vs DaVinci-SFT-7B at 84.50% — a 13.1-point absolute gain from the GRPO stage. This dominates all baselines including GPT-5-Default (72.88%), Claude-Sonnet-4 (84.87%), and Gemini-2.5-Pro-Thinking (69.93%). The gap is large and measured on a standardized test set.

2. **Data-side innovations (code reordering + comment injection) are cleanly validated.** Table 4 provides a controlled ablation: reordering alone raises Pass@1 from 69.74% to 78.78% (+9.04%), and adding comment annotations further raises it to 84.50% (+5.72%). This is causal evidence that the paper's key data-level contributions — drawing-order normalization and planning-scaffold comments — are effective and separately isolable. The 15-point total gain from data alone is the paper's strongest individual result.

3. **Vectorized-representation reward is a genuinely clever idea with supporting evidence.** Extracting text and geometric primitives from the compiled PDF (via PyMuPDF) rather than relying on OCR avoids error propagation from visual text recognition. Table 5 confirms that adding R_text + R_geom to the base image-level reward improves the task-specific textual reward (37.23 → 42.28), geometric reward (41.44 → 44.10), MSE (64.58 → 62.30), and SSIM (73.07 → 74.01).

4. **Human evaluation with sound methodology.** The Best-Worst Scaling setup uses six annotators with strong inter-annotator agreement (split-half reliability ρ = 0.72–0.79). DaVinci-7B achieves the top BWS score among non-proprietary models (μ = 0.365, p_best = 0.47) and outperforms GPT-5-Default and Claude-Sonnet-4-Thinking in the proprietary group.

5. **Explicit temporal decontamination.** Training data is restricted to sources published by December 2023 with the test set containing data from January 2024 onward — a rigor detail often absent in this area.

## Weaknesses

### Major

None. The core claims are supported by evidence, and the methodology is sound.

### Minor

1. **"Error-free" extraction claim is overstated.** The paper repeatedly describes its text and geometric extraction from vectorized PDFs as "error-free" (lines 34, 40–41, 52, 122). In practice, PDF extraction via PyMuPDF depends on the correctness of the LaTeX rendering pipeline and can be lossy for math symbols encoded as glyphs without Unicode mappings, ligature handling, or non-standard font encodings. The paper's own matching algorithm (Section 3.3) uses Levenshtein distance with an adaptive threshold, suggesting that even in the vectorized pipeline, exact matching sometimes fails. The approach is a genuine improvement over OCR — and this should be the framing — but "error-free" is an over-commitment. This is a presentation issue, not a methodological flaw.

2. **Reward ablation shows mixed results on the headline perceptual metric.** In Table 5, DreamSim — arguably the most reliable perceptual metric used — decreases from 85.00 (Base: R_img + R_pass) to 84.75 (Base + R_text + R_geom). While other metrics improve and the task-specific textual/geometry rewards increase substantially, the best-performing DreamSim configuration is the simplest one. The paper should discuss this more candidly.

3. **No confidence intervals or significance tests for automatic metrics.** Table 1 presents all metrics as point estimates. Several comparisons are close (e.g., DaVinci-7B SigLIP = 93.93 vs GPT-5 SigLIP = 93.79; DaVinci-7B SSIM = 73.65 vs Claude-Sonnet-4 SSIM = 73.45), and without uncertainty quantification it is impossible to assess whether these differences are meaningful or within noise range.

### Trivial

None.

## Nice-to-Haves

- Reporting how non-compiling outputs are handled in image-level metric computation (e.g., setting DreamSim = 0 for non-compiling outputs would give a more complete picture).
- Including compile rate or Pass@1 in the reward ablation (Table 5) to show whether the reward variants differ on this critical dimension.
- Discussing the computational cost of the data processing pipeline (especially the reliance on Qwen3-Coder-480B for code reordering).

## Removed Points

These points were flagged in the inputs but are removed after cross-checking against the paper:

- **Harsh Critic #1 (proprietary model claim is not uniformly supported):** The paper's abstract and conclusion specifically say "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4" — it does not claim to surpass Gemini-2.5-Pro. The body text (Section 4.3) acknowledges Gemini's advantages on some metrics. The paper is selective about which models it claims to surpass, and for the named models, the claim is supported. Removed because the criticism misreads the actual claim.

- **Strength Finder's generic strengths about problem importance:** Dropped per filtering rule — they lacked specific, verifiable content connected to the paper's evidence.

- **Criticism about "no human evaluation of proprietary model group" or related framing:** The human evaluation results (Table 3) are presented and discussed; the paper acknowledges Gemini's superiority. This is not a hidden result.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Tone down the "error-free" language to "extraction without raster-based OCR" or "vector-native extraction" — the genuine advantage (avoiding OCR error propagation) is strong enough without overclaiming.
2. Add bootstrap confidence intervals to Table 1, or at minimum report pass@k with variance across multiple seeds.
3. Include Pass@1 in the reward ablation table (Table 5) — this is essential for disentangling whether the reward components affect correctness or only image quality.
4. Qualify the "surpasses proprietary models" claim in the abstract to note that this holds for compile rate and several image metrics, while acknowledging that Gemini-2.5-Pro leads on others.

## Score and Decision

**Calibration anchors used across rounds:**

| Paper | Path | Avg Score | Round | Comparison to DaVinci |
|-------|------|-----------|-------|----------------------|
| Sketch2Diagram | KvaDHPhhir | 6.25 | R2 | Same domain (TikZ generation). DaVinci has larger dataset, more baselines, RL post-training. Slightly stronger. |
| FiSAO | cJQ1K2fjpD | 6.20 | R1 | Token-level rewards for VLM alignment. Similar rigor, DaVinci has cleaner ablations. Comparable. |
| CraftRTL | 8KQzoD5XAr | 7.00 | R2 | Verilog code generation with data improvements. Cleaner execution, fewer framing issues. Slightly stronger. |
| ScImage | ugyqNEOjoU | 5.33 | R2 | Scientific text-to-image benchmark. Less rigorous. DaVinci is clearly stronger. |
| RL Hallucination | bO31lfEdos | 5.00 | R1 | RL for object hallucination. Less comprehensive. DaVinci is stronger. |
| SVG-to-Text | pwlm6Po61I | 5.67 | R2 | SVG-based LLM visual understanding. Related area. DaVinci is more rigorous and better evaluated. |

**Round 1 bracket:** 5.5–7.0. The paper is clearly above the low-scoring rejects (3–5) and below top-tier papers (7.5+).

**Round 2 narrowing:** Comparing against Sketch2Diagram (6.25), CraftRTL (7.00), and FiSAO (6.20), DaVinci is best aligned with the 6–7 range. It is stronger than Sketch2Diagram on evaluation breadth and technical depth (RL adds more than data augmentation), comparable to FiSAO in overall contribution, and slightly below CraftRTL where the narrative is tighter and framing more precise. The paper's weaknesses (overstated "error-free" claim, modest reward ablation on DreamSim, no confidence intervals) are real but minor — they do not threaten the core contributions, which are solid.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>