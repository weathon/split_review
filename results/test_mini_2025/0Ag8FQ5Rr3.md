Now I have sufficient calibration. Let me write the final review.

**Round 1 bracket**: Between weak anchors (avg ~3) and strong anchors (avg ~8) → plausible range [4, 7].

**Round 2 narrowing**: The most relevant anchors — "Systematic Outliers" (6.0), "From Attention to Activation" (5.67), and the very closely related "House of Cards" (5.25, rejected) — suggest the paper sits in the 5.5–6.5 range. Comparing directly: better than "House of Cards" (5.25) because the finding is more precise (single scalar vs. top-k rows) and the paper has concrete quantization demonstrations; comparable to "Systematic Outliers" (6.0) and "From Attention to Activation" (5.67).

**Final score**: 6.0

---

## Summary

This paper discovers that a single scalar parameter ("super weight") in the `down_proj` of an early transformer layer is disproportionately important for LLM quality. For Llama-7B, pruning this one weight drops zero-shot accuracy from 70.1% to 35.1%, while pruning the next 7,000 largest-magnitude weights *combined* only drops accuracy to 69.2%. The paper provides a data-free identification method (detecting activation spikes in one forward pass), a directory of super weight coordinates for 8 models across 4 families, and a mechanistic analysis showing super weights induce "super activations" that persist throughout the model and suppress stopword likelihood. It further shows that preserving super outliers improves round-to-nearest quantization: for W8A8 activation quantization, the method is competitive with SmoothQuant (achieving 71–83% of its improvement) while being data-free; for weight quantization, super weight preservation allows larger block sizes with less quality loss.

## Strengths

- **A single scalar can outweigh thousands of outliers.** Table 1 provides striking evidence: pruning the super weight drops zero-shot accuracy from 70.1 → 35.1, while pruning 7,000 other outlier weights (including ones larger in magnitude) only drops from 70.1 → 69.2. This is the first demonstration that a *single* scalar parameter can be more impactful than thousands of other outliers combined — a much stronger claim than prior work's finding about fractions like 0.01%.

- **Data-free identification requiring only a single forward pass.** The method (Section 3.1) locates super weights by detecting spikes in `down_proj` input/output activations. Unlike calibration-dependent methods (SmoothQuant, AWQ), this requires no training data or hyperparameter tuning beyond choosing layer and coordinates from the spike pattern.

- **Activation quantization competitive with SmoothQuant without calibration data.** Table 3 shows that restoring the single scalar super activation in round-to-nearest W8A8 achieves 71–83% of SmoothQuant's perplexity improvement over naive quantization across Llama-7B/13B/30B (e.g., Llama-7B Wiki-2: Ours 5.74 vs SmoothQuant 5.71 vs naive 5.83). This is notable because SmoothQuant uses calibration data for per-channel scales, while the proposed method uses zero data.

- **Mechanistic dissection with controlled ablation.** The "Prune SW + restore SA" experiment (Table 1) shows that restoring the super activation recovers ~42% of the quality loss caused by pruning the super weight, cleanly demonstrating that super weights operate *partially* through super activations rather than being fully explained by them.

- **Amplifying super weights can improve zero-shot accuracy.** Figure 6 shows that scaling the super weight by a factor between 1.0 and 2.0 yields a small but consistent accuracy increase over the original model across Llama-7B/13B/30B — a surprising result from modifying a single scalar.

- **Directory of super weights across model families.** Table 2 lists exact layer/weight/coordinate indices for Llama, Llama-2, Mistral, OLMo, and Phi-3 models, enabling direct reproduction. The observation that instruction fine-tuning does not change super weight positions is a practically useful finding.

## Weaknesses

### Major

- **Full pruning validation is only shown for one model.** Table 1's dramatic pruning result (accuracy 70.1→35.1, perplexity ×1000) is only demonstrated with full metrics for Llama-7B. The directory in Table 2 lists coordinates for 8 models, but the paper does not provide per-model Table-1-style verification that pruning the claimed coordinate(s) causes catastrophic quality degradation in every listed model. While the stopword analysis (Figure 5) covers 3 models and quantization experiments cover additional models, the central claim that "pruning the super weight destroys the model" is only rigorously quantified for one architecture. The directory is presented as a core contribution but is not uniformly validated.

- **Weight quantization experiments lack comparison to standard baselines.** The activation quantization experiments (Table 3) properly compare to SmoothQuant, but the weight quantization experiments (Section 5.2, Figure 7) compare only to vanilla round-to-nearest (RTN). The paper discusses AWQ and SqueezeLLM (Section 5.2.1) and notes that they handle super weights implicitly, but never runs them as baselines. Without this comparison, the claim that "preserving the super weight and clipping other outliers improves round-to-nearest for large block sizes" is demonstrated relative to a naive baseline, but its practical value relative to methods practitioners actually use is unsubstantiated.

### Minor

- **Stopword suppression claim could be better isolated.** The paper states "super weights suppress stopword likelihood" and supports this with evidence that removing the super weight increases stopword probabilities 2–10× (Figure 5). However, removing the super weight also destroys the model (perplexity ×1000, accuracy to guessing). Under these conditions, the model is producing broken output, and the dominance of stopwords could be a generic failure mode of a broken language model rather than evidence of a specific functional role of the super weight. A controlled experiment targeting only the logit channels responsible for stopwords while preserving overall distribution quality would strengthen the mechanistic claim.

- **Identification method lacks precise algorithmic specification.** The identification procedure (Section 3.1) is described as "plotting extreme outliers" and detecting spikes, with no quantitative threshold (e.g., "a value is an outlier if it exceeds X standard deviations"). While the approach is illustrated for Llama-7B (Figure 3), the absence of a precise, reproducible procedure makes it unclear whether other researchers can reliably identify super weights in new models, or whether the detection is robust to the choice of prompt.

### Trivial

- None.

## Nice-to-Haves

- A robustness test of the identification method across multiple prompts (e.g., 10 different prompts from Wikitext-2) to verify whether the same super weight coordinate is always found.
- For the weight quantization experiments, even a single comparison point (e.g., running AWQ at the same block sizes shown in Figure 7) would substantially strengthen the practical claims.
- The choice of the median (rather than zero or another value) to replace the super activation before quantization could be briefly justified or ablated.

## Removed Points

- **"The paper does not compare to AWQ/SqueezeLLM at all"**: Removed because the paper does compare to SmoothQuant for *activation* quantization (Table 3). The missing comparison is specific to *weight* quantization.
- **"No per-weight verification for the entire directory"**: Downgraded from Fatal/structural to Major. The paper validates the core phenomenon on Llama-7B with full metrics, and provides partial supporting evidence (stopword analysis, quantization) on other models. The directory is presented as a resource rather than the paper's central claim.
- **"No fixed threshold for identification"**: Moved to Minor. The paper describes a procedure using activation spikes; for a discovery paper this is reasonable, though specifying a threshold would improve reproducibility.
- **"Mistral-7B results are weak and hand-waved"**: Removed. The paper explicitly hypothesizes about LayerNorm suppression and the results are still positive (14–25% improvement over naive). The paper is transparent about this variation.
- **"Choice of median not justified"**: Removed as a nitpick. The median is a natural choice to avoid introducing an outlier into the quantization range, and this is a minor design decision.
- **"Abstract phrasing should reflect variance"**: Removed (formatting nitpick).
- Various formatting, scope, and reproducibility nitpicks removed per filtering rules.

## Novel Insights

The review surfaces one genuine insight beyond the paper's own contributions: the paper's data-free identification method and its competitive quantization results together suggest that super activations could serve as a "free lunch" signal — a simple diagnostic that any model analysis pipeline can run in one forward pass to identify the most brittle point in the model. The paper does not frame it this way, but the implication is that if a single activation outlier can be identified and protected cheaply, it might be a useful general debugging tool for understanding why quantization or pruning fails on specific models, beyond the specific RTN improvement shown.

## Suggestions

1. **Validate the super weight directory systematically.** For each model in Table 2, run the same experiment as Table 1: prune the claimed super weight(s) and report perplexity/zero-shot accuracy; prune an equally large set of non-super outlier weights from the same tensor. This would transform the directory from a suggestive list into a confirmable resource.
2. **Add weight quantization baselines.** Compare against AWQ or SqueezeLLM at the same block sizes used in Figure 7. Even one comparison table would make the weight quantization claims much more convincing.
3. **Specify a quantitative detection threshold** for the identification method, and report whether the detected coordinate is robust to the choice of prompt.
4. **Reframe the stopword analysis** as a correlation with an interesting mechanistic hypothesis rather than a definitive causal claim, or add a cleaner controlled experiment.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

### Calibration Anchors Used

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "House of Cards: Massive Weights in LLMs" (LvuSFvGShf) | 5.25 | R1 (weak) | Very similar topic (massive weights critical to LLM quality). The current paper has a more precise finding (single scalar vs. top-k rows), a practical quantization application, and better writing — stronger overall. |
| "Systematic Outliers in Large Language Models" (rLX7Vyyzus) | 6.00 | R1/R2 | Similar topic (outlier analysis in LLMs). Accepted poster. Both papers are empirical analyses; current paper has a more surprising single-scalar finding and concrete downstream use, but narrower validation scope. Comparable quality. |
| "From Attention to Activation" (IjduZQK8gM) | 5.67 | R1/R2 | Studies two LLM phenomena + quantization benefit. Accepted poster. Current paper is similarly structured (phenomenon + application) and at least as strong empirically. |
| "FPTQ" (ykhRO1mAg3) | 4.00 | R1 | Quantization method paper, rejected. The current paper is stronger because its core finding (super weights) goes beyond a quantization trick. |
| "SpQR" (Q1u25ahSuy) | 6.50 | R1 | Outlier-aware quantization. Current paper differs in being primarily a discovery/analysis paper with quantization as application, not a methods paper. |