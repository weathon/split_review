Now I have a clear picture of the paper. Let me compose the final review.

---

## Summary

This paper proposes a cosine-similarity-based method to analyze the read-write (RW) functionality of gated neurons in transformer LLMs. It introduces a taxonomy of neuron classes (strengthening, weakening, conditional variants, etc.) based on cosine similarities between weight vectors. Analyzing 12 models, the paper documents a universal pattern: early-middle layers are dominated by (conditional) strengthening neurons, while late layers contain more weakening neurons. Ablation experiments on OLMo-7B show that weakening neurons — despite being rare — have outsized influence on attribute rate and output entropy. A conditional ablation method further attributes this influence to activations where the gate value is negative, providing the first mechanistic evidence (concurrent with Kong et al. 2025) that negative Swish values matter for model behavior, not just training dynamics.

## Strengths

- **Cross-model validation of a universal weight pattern.** Figure 1(a) shows that the median cos(w_in, w_out) transitions from positive in early layers to negative in late layers across 9 different LLMs (Gemma-2, Llama-2/3, Mistral, OLMo, Qwen2.5, Yi), spanning 2B–9B parameters. This consistent trend is strong evidence that the strengthening-then-weakening pattern is a general property of gated transformers, not a single-model artifact.

- **Causal evidence that weakening neurons are disproportionately influential.** Section 6.1 shows that zero-ablating just 243 weakening neurons in OLMo-7B produces a large, sustained effect on attribute rate starting from layer ~10 onward, whereas ablating the same number of random neurons from the same layers shows no effect (Figure 3a). This contrast directly supports the claim that a very small neuron class has outsize functional importance.

- **First mechanistic demonstration that negative Swish values matter for model function.** Section 6.2 introduces conditional ablation (splitting activations by the signs of x_gate and x_in) and shows that the sharpening effect of weakening neurons on entropy is driven by the x_gate<0, x_in<0 case. This contradicts the common assumption that negative gate values are only useful for training differentiability, and is cited as a concurrent finding with Kong et al. (2025).

- **Novel methodological contribution: weight-based RW analysis for gated neurons.** The cosine-similarity framework provides a simple, lightweight tool for classifying neuron RW functionality that requires only the model weights (no activations). This contrasts with prior neuron analysis that focuses on activation contexts or output weights alone.

## Weaknesses

### Fatal
None.

### Major

- **Functional ablation evidence is restricted to a single model (OLMo-7B).** The weight-based patterns are shown across 12 models (Section 5), which is a strength. However, all ablation experiments that establish the *functional importance* of weakening neurons are performed on only one model. The paper makes strong general claims ("we discover a small class of neurons that is highly influential," "for the first time, we observe a mechanism involving negative gate values") without testing whether these findings replicate in even one additional model (e.g., Llama-3.2-3B or Gemma-2-2B). The authors acknowledge this limitation ("to save resources, we focus on a single model"), but the centrality of the functional claims to the paper's contribution makes this a significant evidential gap. Until at least one additional model is tested, the generality of the causal findings remains uncertain.

- **The comparison showing that other neuron classes lack influence is deferred entirely to the appendix.** The paper's core functional claim — that weakening neurons are uniquely or disproportionately influential — depends on demonstrating that other classes do *not* produce similar effects. The main text (Section 6.1) states "In the appendix (figures 14 to 16) we show results for other neuron classes, all of which are indistinguishable from the 'clean' line." While the information exists, deferring this central comparison to the appendix means the reader cannot evaluate the specificity of the reported effect from the main paper. Given that this contrast is the basis for the paper's headline result, it should appear in the main text.

### Minor

- **The taxonomy threshold (±0.5) is stated without sensitivity analysis.** Section 4.2 introduces a threshold of τ = ±0.5 to classify neurons into prototypical categories. The paper does explore continuous alternatives (marginal plots, scatter plots), which mitigates this concern. However, the main classification results (Figure 1b) and the count of weakening neurons (243) depend on this specific threshold. A sensitivity analysis showing how robust the reported distributions are to varying the threshold would strengthen the paper.

- **No error bars or variance estimates for ablation results.** The ablation numbers for attribute rate and entropy (Figure 3) are reported as single values from a single run on a 20M-token dataset. Some measure of variability (e.g., bootstrapped confidence intervals, multiple independent runs with different random seeds) would help the reader assess whether the reported effects are statistically reliable, especially for comparisons with other classes in the appendix.

- **Conditional ablation analysis lacks a quantitative breakdown of activation conditions.** Section 6.2 describes the four sign-based conditions for x_gate and x_in. The paper states that negative gate activations are "relatively rare" but does not report the fraction of activations falling into each condition. A quantitative breakdown would strengthen the argument that infrequent negative-gate activations nevertheless drive the sharpening effect.

- **Activation frequency correlation shown for one model.** Section 7 reports a strong negative correlation between cos(w_in, w_out) and activation frequency, with correlations of at least −0.71 in most layers of OLMo-7B. While the paper states these results and provides per-layer correlations, the detailed visualization (Figure 4) is for one layer of one model. The claim's generality would be strengthened by showing that this pattern holds across additional models.

- **Case study is limited to two neurons.** Section 8 examines one strengthening and one weakening neuron. While the paper positions this as a qualitative illustration, the claim that "weakening neurons are much harder to interpret" is not supported by a single example. Additional case studies (the paper mentions more are in the appendix, which was stripped) would strengthen this discussion.

### Trivial
None.

## Nice-to-Haves
- Sensitivity analysis for the taxonomy threshold (±0.5) against alternative choices.
- Confidence intervals or bootstrapped variance for ablation results.
- Per-condition activation frequency breakdown in Section 6.2 (what fraction of activations fall into each of the four sign conditions).
- Activation frequency correlations shown for at least one additional model.
- A quantitative breakdown of the number of weakening neurons per layer across models, beyond the threshold-based categorization.

## Removed Points
- **"Nine vs. twelve model inconsistency"**: Removed. The abstract mentions "nine different LLMs" showing the pattern; Section 5 explains that 12 models were analyzed in total and Figure 1(a) shows "the nine larger models" (omitting three smaller ones: OLMo-1B, Qwen2.5-0.5B, Llama-3.2-1B). The paper is internally consistent.
- **"Contradiction between text and Figure 3b histogram description"**: Removed. The "centered around 0" description comes from the automatic OCR image captioning, not from the paper's own text. The paper's caption explicitly states that weakening neurons "decrease the entropy by about 10 nats." There is no contradiction in the paper itself.
- **"Missing limitations discussion in conclusion"**: Removed. While a limitations paragraph would improve the paper, this is a presentation preference rather than a substantive weakness.
- **"Missing related works"**: Removed per instructions — I cannot verify what the paper cites versus omits without external knowledge.
- **Generic weaknesses about evaluation rigor, unfair comparisons, missing proofs in appendix**: Removed per filtering rules.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add at least one additional model to the ablation experiments.** Even a smaller model (e.g., Llama-3.2-3B or Gemma-2-2B) would significantly strengthen the claim that weakening neurons are universally influential. This is the single highest-impact improvement.
2. **Move the comparison with other neuron classes (currently in appendix figures 14–16) to the main paper.** A single panel in Figure 3 showing that strengthening, conditional strengthening, etc., are indistinguishable from the clean line would allow the reader to directly evaluate the specificity of the weakening-neuron effect.
3. **Report confidence intervals or bootstrapped variability for the ablation metrics.** This would help the reader assess whether the observed effects are statistically meaningful.
4. **Report the frequency distribution of the four activation conditions** (x_gate>/<0, x_in>/<0) for weakening neurons, to contextualize the claim that negative-gate activations are "rare but important."
5. **Include a brief justification of the ±0.5 threshold in the main text** and show that the main conclusions (e.g., layer-wise class distribution) are robust to reasonable variations.

---

## Calibration Details

**Round 1 — Bracketing:**
- Weak anchors (high_score=3.5): avg scores 3.00–3.25. These are papers with limited contributions or flawed methodology (e.g., "Llamas (mostly) think in English" at 3.0, "Interpreting Adversarial Attacks" at 3.0). The current paper is clearly stronger — it has a novel method, consistent cross-model empirical patterns, and causal ablation evidence.
- Middle anchors (low_score=3.5, high_score=7.5): avg scores 4.33–6.50. These span from borderline reject to solid accept. Key anchor: "Uncovering hidden geometry in Transformers" (5.33, rejected) — a paper with interesting analysis but scattered results. The current paper is more focused and has cleaner causal evidence. "Tracing Representation Progression" (6.5, accepted poster) — a paper with solid experiments but limited novelty. The current paper's contribution is somewhat more novel but has narrower functional evidence (single model).
- Strong anchors (low_score=7.5): avg scores 7.60–9.00. These are clearly stronger papers with deeper theoretical analysis or broader empirical scope. The current paper does not reach this tier.

**Round 1 bracket: between 4.0 and 6.5.**

**Round 2 — Narrowing:**
- Lower-middle anchors (3.0–4.5): "Mechanistic Insights: Circuit Transformations" (3.75), "MLPs for NLP" (3.75). The current paper is notably stronger than these.
- Upper-middle anchors (5.0–7.0): "Interpretability Illusions" (avg 5.6, rejected), "NeurFlow" (avg 6.5, accepted poster), "Explaining Modern Gated-Linear RNNs" (avg 6.25, accepted poster).

**Comparative assessment:**
- The current paper is stronger than "Interpretability Illusions" (5.6 avg, rejected), which was a narrow case study on a toy Dyck-language task. The current paper tests real LLMs and finds meaningful cross-model patterns.
- The current paper is weaker than "NeurFlow" (6.5 avg, accepted poster), which had more extensive multi-dimensional evaluation, despite having a less clean contribution. The single-model functional analysis and appendix-deferred comparisons in the current paper are clear weaknesses that NeurFlow did not share.
- The current paper is comparable to "Explaining Modern Gated-Linear RNNs" (6.25 avg, accepted poster), which unified multiple architectures under a single framework. The current paper's contribution is similarly clean but its evidence base is narrower (single-model ablation).

**Final score: 5.5.** The paper makes a genuinely novel contribution with the cosine-similarity RW analysis framework, the cross-model weight patterns, and the conditional ablation finding about negative gate values. However, the central functional claims rest on evidence that is (a) limited to one model for all causality experiments, and (b) defers the critical comparison with other classes to the appendix. These gaps prevent acceptance at the ICLR threshold.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>