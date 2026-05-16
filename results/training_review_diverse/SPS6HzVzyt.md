Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper identifies and systematically characterizes **context-parametric inversion** — a failure mode where instruction finetuning (IFT) initially improves a model's reliance on context under knowledge conflicts, but then progressively reduces it as training continues, even while standard benchmarks (MMLU, GSM8k, SQuAD, ARC) keep improving. The authors demonstrate this phenomenon across three model families (Llama, Mistral, Pythia), three IFT datasets (TULU, Alpaca, UltraChat), and three knowledge-conflict evaluation sets. Through controlled experiments they isolate the cause to **non-context-critical datapoints** (where context is redundant with parametric knowledge), present a theoretical analysis in a one-layer transformer formalizing the gradient dynamics, and explore mitigation strategies with honestly reported limitations.

## Strengths

1. **Novel and important empirical discovery.** The paper documents a genuinely non-obvious failure mode of instruction finetuning — context reliance first increases then *decreases* — and demonstrates it consistently across 3 model families × 3 IFT datasets × 3 conflict evaluation sets. The observation that standard benchmarks continue improving during the same period makes this distinct from classical overfitting or forgetting. This alone is a valuable contribution.

2. **Causal isolation of the mechanism.** The paper does not stop at observing the phenomenon. The controlled filtering experiment (Section 4.3): removing the 25% of datapoints with lowest target perplexity without context (i.e., isolating "context-critical" data) eliminates the drop in context reliance. This directly identifies non-context-critical datapoints as the driver, going beyond correlational analysis.

3. **Carefully designed evaluation benchmarks.** The paper creates two new knowledge-conflict datasets (Counterfactual Biographies with algorithmic entity substitutions avoiding NQ-Swap noise, and Counterfactual World Facts with controlled answer positioning) that address known limitations in prior benchmarks (explicitly discussed in Section 3.2). The inclusion of CFQuotes (Memo Trap) extends the analysis beyond QA-style conflicts to general instruction-following.

4. **Theoretical formalization of the gradient dynamics.** The theoretical section (Section 5) provides a formal account in a one-layer transformer showing that context-critical points dominate gradients early (due to higher loss) while non-context-critical points dominate later, shifting attention back to parametric knowledge. The paper is appropriately cautious — it explicitly states "we do not make any causal claims" about deep networks and marks the attention correlation as corroboration only.

5. **Honest reporting of mitigation limitations.** The mitigation experiments (Section 6) transparently show partial success: counterfactual augmentation helps only on similar tasks and degrades SQuAD; QK-only finetuning improves some datasets but not others. The paper does not oversell these results, which strengthens overall credibility.

## Weaknesses

### Fatal
None.

### Major

1. **No error bars or multiple runs for the core inversion plots (Figs. 1, 3, 4, 5, 6).** The central claim — that context reliance "gradually decreases as instruction finetuning progresses" — rests entirely on single-run trajectories. The paper shows the pattern across many settings (3 models, 3 IFT datasets, 3 conflict datasets), which provides qualitative robustness. However, we cannot assess whether the inversion is statistically significant or whether the later-stage variation is within evaluation noise. For example, could the drop on some settings be comparable to run-to-run variability? Adding even 3 random seeds per setting would significantly strengthen the evidential foundation. This is the paper's most consequential empirical gap.

2. **Arbitrary filtering threshold without sensitivity analysis (Section 4.3).** The paper uses a 25% threshold to remove "non-context-critical" datapoints (lowest perplexity without context) and reports that context reliance "barely drops" on this filtered set. However: (a) No sensitivity analysis is provided — would the inversion reappear at 20% or 30%? Is 25% near a phase transition? (b) The filtering is done at initialization, but the model's parametric knowledge evolves during finetuning; a point labeled "non-context-critical" at step 0 may change status later. This is not discussed. Since this experiment is the central controlled evidence for the causal mechanism, the lack of threshold validation weakens the causal claim.

### Minor

1. **Memorization control experiment limited to one evaluation set.** The controlled study filtering fact-overlapping examples from Alpaca (Section 4.1) is demonstrated only on CFCapitals. Showing this holds across all three conflict datasets (CFBio, CFWorldFacts, CFQuotes) would make the argument more complete. The logic is sound, but the coverage is narrow.

2. **Alternative explanation not discussed: model learning "skepticism" of counterfactual contexts.** The paper attributes the inversion to optimization dynamics (non-context-critical data dominating later gradients). A plausible alternative is that the model learns to distrust contexts that contradict its parametric knowledge as a general strategy, especially if many training examples have plausible contexts aligned with the world. The filtering experiment partially addresses this, but an explicit discussion would strengthen the paper.

3. **The theory section, while appropriately caveated, lacks a bridging synthetic experiment.** The theoretical analysis uses a one-layer transformer with frozen head and structured embeddings; the real experiments use deep LLMs. A synthetic experiment training on a controlled mixture of C and C+S points (as defined by the theory) and verifying the inversion occurs would directly bridge this gap and strengthen the claim that the toy theory captures the relevant dynamics.

### Trivial
None of note.

## Nice-to-Haves

- A human evaluation of the coherence of the CFBio entity substitutions would strengthen the benchmark validation.
- A discussion of how context-parametric inversion relates to broader instruction-following degradation literature beyond catastrophic forgetting would enrich the framing.
- For the CFWorldFacts dataset, a systematic analysis of answer position effects would further validate the design.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure 5a caption is cut"**: The captions appear complete in the paper text. This is a parser artifact, not an author error.
- **"CFWorldFacts may have its own biases (certain factual relations easier to override)"**: Speculative without evidence; the paper already acknowledges this is a generated dataset and controls for answer positioning. No concrete bias is identified.
- **"CFBio description is brief, more detail needed"**: The paper provides sufficient detail for reproducibility; the description includes the key design choice (algorithmic entity substitutions vs. deep learning based). Additional detail would be nice but is not a weakness.
- **"Human evaluation of coherence needed for CFBio"**: A nice-to-have, not a weakness. The dataset uses systematic algorithmic substitution which is more reliable than the NQ-Swap issues it addresses.
- **"Comparison to other similar phenomena / forgetting of context reliance"**: The paper already discusses the distinction from catastrophic forgetting (non-monotonic drop + standard benchmarks improve). The critic's reframing does not add new substance.
- **"Reproducibility details missing (random seeds, hyperparameters)"**: These are standard details for an appendix (which is stripped by the parser). The main paper covers the essential experimental design.

## Novel Insights

Beyond the paper's own contributions, a key meta-insight emerges from the reviews: the inversion phenomenon highlights a fundamental tension in how IFT datasets are constructed. Datasets like Alpaca and TULU contain many examples where context is redundant with parametric knowledge — not because of sloppy curation, but because it is natural to write instructions that reference common knowledge. The paper shows that this widespread redundancy, harmless at first glance, systematically undermines the very capability IFT is supposed to improve (context following). This suggests that dataset designers need to think about *gradient competition dynamics*, not just surface-level task coverage.

## Suggestions

1. **Add error bars** from at least 3 random seeds for the core inversion plots. If compute is a constraint, even bootstrapped confidence intervals over evaluation samples for a single run would provide useful information about the reliability of the observed drops.

2. **Perform sensitivity analysis** on the context-critical filter threshold (e.g., 10%, 25%, 50%) and show the perplexity distribution with the chosen cutoff marked. Also discuss whether the classification is stable during finetuning or whether points migrate between categories.

3. **Add a synthetic control experiment** training a model on a controlled mixture of C and C+S points, as defined by the theory, to verify the inversion arises in that setting. This would directly bridge the toy theory and the real experiments.

4. **Extend the memorization control** to show that the inversion persists after filtering fact-overlap for all three conflict datasets, not just CFCapitals.

5. **Add a brief discussion** of the "skeptical model" alternative explanation and why the evidence favors the gradient-competition account.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>