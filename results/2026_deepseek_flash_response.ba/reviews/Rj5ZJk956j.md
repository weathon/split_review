Now I have enough calibration context. Let me write the final review.

## Summary

This paper introduces a weight-based method for analyzing gated neurons in transformer LLMs by computing cosine similarities between their three weight vectors (w_gate, w_in, w_out), yielding a taxonomy of "read-write" (RW) functionalities. Applying this across 12 LLMs (0.5B–9B parameters, 6 families), the paper discovers a universal strengthening-then-weakening pattern across layers and identifies a small class of "weakening neurons" that activate disproportionately often. A conditional ablation method reveals that part of their influence comes from negative gate values — a surprising finding since negative Swish values were assumed relevant only to training dynamics.

## Strengths

1. **First systematic read-write analysis tailored to gated neurons (SwiGLU/GEGLU).** Prior work on input–output cosine similarity was either applied to non-gated ReLU models (GPT-2) without interpreting results or mentioned only in a footnote. The gated case adds genuine complexity (three weight vectors vs. two), and the paper constructs a novel six-category taxonomy (Table 1, Section 4.2) that is conceptually new for the now-dominant gated architecture family used in Llama, Gemma, OLMo, Mistral, and Qwen.

2. **Cross-model universality demonstrated with quantified evidence across 12 LLMs.** The paper validates the strengthening-then-weakening pattern across 12 models from 6 families at scales from 0.5B to 9B parameters. Figure 1(a) shows all models exhibiting the same positive-to-negative transition in median cos(w_in, w_out) across layers. The paper reports specific numbers: 25% of neurons are input manipulators, rising to 50% in early-middle layers (Section 5), and a quantified negative correlation between cos(w_in, w_out) and activation frequency of at least −0.71 in all but the last two layers (Section 7). Most interpretability work covers 1–3 models; this breadth is a distinctive strength.

3. **Conditional ablation method that isolates a previously undocumented mechanism.** Section 6.2 introduces a novel method that ablates only specific sign-conditioned activations (four cases based on the signs of x_gate and x_in). The paper shows that case (iii) — x_gate < 0, x_in < 0 — reproduces the entropy-sharpening effect of weakening neurons as a whole (Figure 3(b), bottom-left), while the other three cases do not. This is a genuinely creative methodological contribution and a surprising finding about the functional role of negative gate values.

## Weaknesses

### Major

1. **Functional-importance claims rest on ablation experiments from a single model (OLMo-7B).** The paper's strongest headline claims — that weakening neurons have "outsized influence," that they "sharpen" the output distribution, and that negative gate values drive a functionally important mechanism — are supported exclusively by ablation experiments on OLMo-7B. The cross-model analysis (Section 5) convincingly establishes that weakening neurons *exist* across architectures with consistent weight-space signatures, but whether they are *actually functionally influential* is tested on exactly one model. The paper explicitly acknowledges this choice ("to save resources, we focus on a single model," p. 5), but the mismatch between the broad claims in the title/abstract and the narrow evidential base is a significant weakness.

2. **No variance or uncertainty reported for any ablation experiment.** The attribute-rate plot (Figure 3a) shows single lines with no error bars, confidence bands, or indication of variability across random seeds or data subsets. The entropy histograms show aggregate distributions with no measure of uncertainty. The baseline is a single draw of "random neurons from the same layers." Without knowing whether these results are stable under different random baselines or different data samples, the quantitative comparisons are difficult to assess. This limits the evidential quality of the paper's most striking conclusions.

### Minor

1. **Novelty claim about negative gate values is somewhat over-broad.** The paper states that negative gate values were "often assumed [to be] only useful for training dynamics" and that it provides "the first time [observing] a mechanism involving negative values of the Swish activation function." The Swish function's negative range is well-known (it is Swish's defining advantage over ReLU). The paper cites a single reference (Lee, 2023) to support the claim that negative values were thought relevant only to training. The actual finding — that negative *gate* values have functional importance in *gated activation functions* specifically — is genuinely interesting and defensible as novel when properly scoped. The framing should be calibrated to what is actually new rather than implying a discovery about Swish's negative range in general. (The paper's concurrent acknowledgement of Kong et al. (2025) is good practice but does not fully resolve the framing issue.)

2. **Key methodological detail deferred to appendix without sufficient in-text motivation.** The weight preprocessing step (Section 3.2) — multiplying w_in and w_out by the sign of cos(w_gate, w_in) — is critical to the entire cosine-similarity classification scheme, yet its justification is entirely relegated to the appendix. While deferring details is common practice, a brief intuitive explanation of why this is necessary and what would go wrong without it should appear in the main text.

3. **Negative result for other RW classes reported only in the appendix.** The claim that other RW classes are "indistinguishable from the clean line" (Figure 3 caption) is a strong negative result that appears only in the appendix (figures 14–16). Given that this negative result is critical for establishing that weakening neurons are uniquely influential, it merits at least a summary in the main text.

4. **Threshold τ = 0.5 is acknowledged as somewhat arbitrary.** The paper supplements the threshold with continuous analyses (scatter plots, marginal distributions), which is good practice. However, the claim that weakening neurons are "few" depends on this threshold. A brief sensitivity analysis (e.g., how class sizes change with τ = 0.4, 0.6) would strengthen this section.

### Trivial

- Contribution (v) in the introduction is cut off mid-sentence (p. 2). (This is likely a PDF extraction artifact, but should be verified in the original submission.)
- The abstract mentions "nine different LLMs" while the body lists 12 — though this may be because Figure 1(a) plots 9 of the 12, the discrepancy could be clarified.

## Nice-to-Haves

- Running ablation experiments on 1–2 additional smaller models (e.g., Llama-3.2-3B, Gemma-2-2B) would substantially strengthen the functional-importance claims without requiring extreme compute.
- Reporting variance across multiple random-baseline draws (different random neuron selections from the same layers) would improve evidential quality without requiring new model-level compute.
- The two-neuron case study in Section 8 is illustrative but thin. The suggestion that weakening neurons "work together (in superposition)" based on one example is a reasonable hypothesis but should be flagged more explicitly as such.

## Removed Points

The following points from the input reviews were removed:
- **Harsh critic's formatting nitpick about contribution list formatting:** The "cut-off" claim about contribution (v) is kept in Trivial since it's verifiable from the paper text.
- **Harsh critic's claim of "9 vs 12 models inconsistency":** The paper says "nine different LLMs" in the abstract (referring to Figure 1(a), which plots 9 models) and "12 LLMs" in the body (the full catalog). These are consistent when read in context.
- **Harsh critic's claim that Section 7 "largely replicates" Gurnee et al.:** The paper explicitly cites Gurnee et al., acknowledges their finding, and frames its result as an extension to gated activation functions. This is appropriate.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): These were removed per filtering rules because they lack specific content tied to the paper's evidence.
- **Strength Finder's claim that the case study "bridges statistical ablation result with a concrete human-interpretable example":** While partially valid, this conflates the single-neuron analysis (Section 8) with the conditional ablation finding (Section 6.2). The link between the two is present but thin; the strength as phrased overstates the conclusiveness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand functional validation** — either run ablation experiments on at least one additional model (e.g., Llama-3.2-3B) or recalibrate the headline claims to apply to OLMo-7B specifically, with the cross-model weight analysis standing as evidence of the pattern's existence rather than its functional importance.
2. **Add variance information** — report error bars on attribute-rate plots (multiple random-baseline draws, multiple data subsets) and include uncertainty quantification for the entropy comparisons.
3. **Motivate the preprocessing step** in the main text with a brief intuitive justification, rather than deferring entirely to the appendix.
4. **Calibrate the novelty framing** to state clearly that the contribution is about negative *gate* values having a functional role in *gated neurons*, not a discovery about Swish's negative range in general.
5. **Summarize the other-RW-class ablation negative results** in the main text rather than only in the appendix.
6. **Add a sensitivity analysis** for the τ = 0.5 threshold (e.g., class sizes at τ = 0.4, 0.6).

## Score and Decision

**Calibration procedure:**

**Round 1 (bracketing):** Searched three bands: weak (scores < 3.5), middle (3.5–7.5), and strong (7.5+). Weak anchors included papers on "metanetwork" (2.5) and "sparsity beyond TopK" (1.67) — clearly below the current paper. Strong anchors included "Retrieval Head" (8.0) and "Sparse Feature Circuits" (8.0) — papers with near-flawless execution and extensive causal evidence. The paper clearly sits between these extremes. **Round 1 bracket: [5.0, 7.0].**

**Round 2 (narrowing):** Searched within (4.5, 6.5) and (5.5, 7.5) for papers on neuron discovery and weight cosine similarity. Anchors examined in full:
- "What does GPT store in its MLP weights?" (4.00): Narrow case study on a single syntactic phenomenon, incomplete analysis. Our paper is substantially stronger — broader scope, more models, more surprising findings.
- "Gated RNNs discover attention" (5.50): Good theoretical construction but unclear contribution thrust and weak empirical validation. Our paper has clearer contribution but weaker than that paper's formal construction.
- "Discovering Influential Neuron Path in Vision Transformers" (6.00): Thorough evaluation but on vision models only; the contribution is more methodological. Our paper is comparable in rigor but has more surprising empirical findings.
- "DOCS: Quantifying Weight Similarity" (6.60): Well-executed but limited to descriptive analysis of weight similarity patterns. Our paper makes more ambitious functional claims but with thinner evidence. Our paper is slightly weaker than this anchor.
- "Retrieval Head" (8.00): Near-ideal execution — broad model coverage, strong causal evidence, clean evaluations. Our paper is clearly below this.

**Final score: 6.0.** The paper has genuine contributions: a novel taxonomy for gated neurons, broad cross-model validation of the strengthening-weakening pattern, and a creative conditional ablation method revealing a surprising negative-gate mechanism. However, the functional-importance claims outrun the evidence (single model, no error bars), and several presentation/scope issues reduce the overall package. It is a clear borderline accept — strong enough that the core contributions are worth publishing, but with weaknesses that should be addressed.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>