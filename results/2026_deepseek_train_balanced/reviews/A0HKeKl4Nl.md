## Summary

This paper investigates whether fine-tuning alters a pretrained model's underlying capabilities or merely learns minimal "wrappers" on top of them. Using controlled synthetic settings (PCFG-based counting tasks and Tracr-compiled transformers) with mechanistic interpretability tools (pruning, probing, attention visualization, and a proposed "reverse fine-tuning" method), the paper shows that fine-tuning rarely deletes pretraining capabilities; instead, it learns localized transformations that can be undone by pruning a handful of neurons or by a few gradient steps of reverse fine-tuning. The paper also provides a TinyStories validation as a bridge toward more realistic language models.

## Strengths

- **Pruning directly quantifies wrapper localization (Fig. 6).** Removing just 5–15 neurons from a fine-tuned PCFG model restores pretraining task accuracy while degrading fine-tuning task accuracy. This provides a concrete, neuron-level measurement of how localized fine-tuning changes are—far more specific than prior behavioral or loss-landscape analyses.

- **Reverse fine-tuning (ReFT) provides a controlled measure of capability persistence (Fig. 9).** Capabilities revive in 0.1–1K gradient steps vs. 4.5K+ for a directly fine-tuned baseline. The comparison is well-designed: Scr.+FT starts from the same pretrained checkpoint, so the speedup directly measures how much of the capability survived fine-tuning.

- **Systematic operationalization of capability relevance via controlled spurious correlations.** The paper distinguishes "strongly relevant" vs. "weakly relevant" capabilities by controlling the spurious correlation level $C_{\mathtt{Tr}}$ and the sampling prior $\mathcal{P}_{\mathtt{T}}$ (Section 4). This allows the paper to show mechanistically—rather than just behaviorally—that weakly relevant capabilities get wrapped while strongly relevant ones are amplified.

- **Multi-tool convergence strengthens robustness.** The paper explicitly acknowledges that individual tools (probing, pruning, attention visualization) have known pitfalls (line 173), and uses convergence across all of them plus ReFT to mitigate this. Findings are consistent across both compiled (Tracr) and learned (PCFG) settings.

- **TinyStories extension demonstrates the phenomenon is not a synthetic artifact.** The paper replicates its key findings (probe persistence, sample-efficient ReFT recovery) on TinyStories-Instruct models, showing the wrapper phenomenon extends beyond toy counting tasks to language generation (Section 5, Fig. 10, Table 1).

## Weaknesses

### Fatal

None.

### Major

- **The safety claim in the abstract is unsupported by the evidence presented.** The abstract states that the results indicate "practitioners can unintentionally remove a model's safety wrapper merely by fine-tuning it on a, e.g., superficially unrelated, downstream task" (line 8). The paper's experiments are entirely on counting token occurrences in synthetic strings (PCFGs) and character-counting in Tracr-compiled transformers, with a TinyStories validation about generating stories with or without "twists." There is no experiment that tests safety alignment (e.g., refusal to produce toxic content, honest answering, or any of the behavioral capabilities that safety alignment targets). The leap from "counting token 'a' in a synthetic string" to "safety alignment in LLMs" is not supported by any experiment in the paper. This is a framing issue: the headline claim goes well beyond what was actually measured. The rest of the paper's contribution would stand better if the safety claim were removed or severely qualified.

- **No variance or statistical significance reporting.** All results are reported as point estimates with no confidence intervals, standard deviations, or indication of multiple runs. This was verified across the entire paper (grep for "variance," "error bar," "standard deviation," "confidence interval," "random seed," "multiple run"—no matches). For an empirical study making broad claims about the nature of fine-tuning, the absence of any statistical rigor weakens the reader's confidence that the observed patterns are robust rather than idiosyncratic to a single run or data split. This is especially consequential for the central quantitative claims (pruning counts in Fig. 6, ReFT step counts in Fig. 9).

### Minor

- **TinyStories validation has methodological gaps.** (a) The recovery trajectories in Table 1 are notably non-monotonic (e.g., F+MM at $\eta_M$: 31% → 88% → 50% → 75%); this pattern is unexplained and undermines the claim of clean, sample-efficient recovery. (b) The evaluation of whether generated stories contain a "twist" relies on a "fine-tuned GPT-3.5 classifier" with no reported validation accuracy, no error analysis, and no discussion of reliability. (c) The "Not in PT" baseline is described as "pre-trained on data w/o twists"—it is unclear whether this means a model pretrained from scratch on a modified TinyStories dataset or the same architecture with twist-related weights removed; these two scenarios have very different interpretations. These issues do not invalidate the TinyStories results but make them less rigorous than the main synthetic experiments.

- **Probing evidence is sometimes over-interpreted as functional evidence.** The paper's capability definition (Definition 1) relies on linear probe detection, and the caption of Fig. 7 states "This indicates pretraining capabilities persist after fine-tuning" based solely on probe accuracy. Probe-detectable information does not imply functional use in the forward pass. The paper largely mitigates this through complementary pruning experiments (which are functional), but the language occasionally conflates "information persists in representations" with "the capability is functionally intact." This is a presentational imprecision rather than a fatal flaw.

- **No architectural details in the main text.** The paper never reports model sizes (number of layers, hidden dimension, number of heads, total parameters) for any of the experiments. This makes it impossible to assess what "5–15 neurons" means as a fraction of total parameters. The paper references the appendix, but these details are important for interpreting the core quantitative claims.

- **Tracr models have no training history.** The paper uses compiled (never-trained) transformers and treats fine-tuning dynamics as analogous to trained models. A model with hand-assigned weights and no pretraining distribution may exhibit different fine-tuning behavior than one that learned capabilities via gradient descent. The paper mitigates this by centering the PCFG experiments (which involve real training) as the primary evidence, but the Tracr results are presented as supporting evidence without fully acknowledging the gap.

### Trivial

- None.

## Nice-to-Haves

- **Characterizing the wrapper's structure.** The paper calls the transformation $g$ a "wrapper" but does not identify its parametric form (e.g., specific attention heads, MLP neurons, or a low-rank update analogous to LoRA). Showing that the wrapper has a simple, identifiable structure would significantly strengthen the mechanistic story beyond the current phenomenological description.

- **Systematic sweep of recovery speed.** The reverse fine-tuning analysis could be sharpened by reporting recovery speed as a function of fine-tuning duration, learning rate, and spurious correlation strength with error bars. The current presentation (single figure + one table with non-monotonic entries) is suggestive but not definitive.

## Removed Points

These points were considered but removed for the reasons given; they should be treated with caution if consulted.

- **"Scr.+FT baseline is underspecified"** — Removed. The paper's description at line 236 ("initialized with parameters pre-trained to count $\mathtt{O_{FT}}$") is clear in context: the pretrained model was trained on $\{\mathtt{a, b, c}\}$, so "pretrained to count $\mathtt{O_{FT}}$" refers to that checkpoint. The paper explicitly contrasts the two initialization states (Scr.+FT vs. ReFT). The critic's confusion appears to stem from misreading.

- **Deferred appendix content / missing proofs** — Removed per system rules. The PDF parser strips appendices from all papers; they exist in the original submission.

## Novel Insights

Beyond synthesizing the inputs, the key meta-insight is that the harsh critic's most pointed structural criticism (safety overreach) and the strength finder's most grounded praise (pruning and ReFT quantification) are compatible: the paper's experimental methodology is genuinely strong for the synthetic counting setting, but the framing consistently aims for a significance level that the evidence cannot support. The paper would be more compelling if it leaned into what it actually measures—controlled mechanistic analysis of fine-tuning dynamics—and dropped the pretense of safety relevance. The multi-tool convergent evidence design is a methodological strength worth preserving; what needs fixing is the storytelling.

## Suggestions

1. Remove the safety claim from the abstract and introduction, or replace it with a more measured statement about the implications for capability "deletion" in general. The paper's contribution stands on its own as a mechanistic analysis of fine-tuning in controlled settings.
2. Add variance reporting (multiple seeds, error bars) to the key figures (pruning, probing, ReFT recovery speed) in a revision. This is the single most impactful technical improvement.
3. Provide validation accuracy for the GPT-3.5 classifier used in TinyStories evaluation, and explain the non-monotonic recovery patterns in Table 1.
4. Report model architectural details (layers, hidden dimension, heads, total parameters) in the main text so readers can interpret the "5–15 neurons" claim in context.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>