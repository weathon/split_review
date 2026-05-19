- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have verified all claims against the actual paper content. Here is the final consolidated review.

---

## Summary

This paper proposes a systematic evaluation framework for activation steering in LLMs, introducing a steering effect matrix and three metrics — Format-Preserving Rate (FPR), Steering Success Rate (SSR), and Side-Effect Rate (SER). The authors apply additive steering to Llama3-8B, Llama2-7B, and Exaone-8B across three datasets (Paradetox, SubjQA, Jailbreak) and examine effects on query tokens, longer same-task contexts, and irrelevant tasks. The key empirical findings are that format preservation depends on layer depth (upper layers above 0.7 preserve format well), steering success varies by model/dataset/layer/alpha, long-context effects weaken substantially, and steering induces measurable side effects on irrelevant tasks.

## Strengths

- **Systematic evaluation framework with three complementary metrics.** The paper goes beyond prior work (which typically measures only whether the output flips to the intended label) by tracking format preservation (FPR), intended steering success (SSR), and unintended side effects (SER) within a 3×3 steering effect matrix (Section 3, Figure 3). The matrix format makes outcome categories explicit and enables conditional normalization (e.g., SSR+ for format-preserved cases). This provides a structured vocabulary for thinking about steering effects that was previously missing from the literature.

- **First empirical evaluation of steering effects on longer contexts and irrelevant tasks.** Sections 6.3 and 6.4 (Figures 8 and 9) show that steering a single earlier token has weak in-context persistence (SSR drops below 0.5 on later same-task prompts) and unexpectedly modifies outputs on completely unrelated tasks (SER increases with context length). Prior steering studies (e.g., Liu et al., Arditi et al., Turner et al.) evaluate only the immediate query token; this paper provides the first systematic evidence about how steering effects propagate beyond the immediate generation.

- **Cross-model and cross-dataset validation with consistent findings.** The experiments use three models (Llama3-8B, Llama2-7B, Exaone-8B) and three datasets (Paradetox, SubjQA, Jailbreak) across multiple steering strengths and layers (Figures 5, 7, 8). The finding that format is preserved only in upper layers (above 0.7) and that steering success varies sharply by layer and model is demonstrated across all combinations, lending robustness to the conclusions.

- **Counterfactual-style comparison cleanly isolates steering effects.** Comparing base generation (no steering) with steered generation for the same input (Section 3.3) attributes changes to the steering intervention rather than to model randomness or prompt variation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Definitional imprecision in the SER metric for the relevant task (Section 3.3).** The verbal description states that the Steering Side-Effect Rate in the Relevant Task measures "when the positive label is not achieved" (line 105). However, the target set $\mathcal{T}_{\mathrm{rel.fail}}$ includes $S_{y\rightarrow y}$ (base=yes, steered=yes), which is a case where the positive label *is* achieved. This inconsistency makes the metric's intended interpretation ambiguous. The authors should either exclude $S_{y\rightarrow y}$ from the fail set (since the output is "yes") or clarify what semantic notion of "failure" justifies its inclusion. This issue does *not* invalidate the paper's overall experimental results — the SSR and FPR definitions are sound, the irrelevant-task SER definition is reasonable, and the qualitative trends (format preservation at upper layers, SSR varying with layer/alpha, long-context decay) would be preserved with a corrected definition — but it is a genuine imprecision that should be fixed.

- **No statistical reporting.** All bar charts and point plots (Figures 5–9) are presented without error bars, confidence intervals, or results across multiple seeds. The metrics are proportions computed over 1000 samples, so sampling variance is non-trivial. Claims like "SSR drops below 0.5" (Section 6.3) or "SSR is higher at the 0.3 layer depth than at 0.4 layer depth" (Section 6.2) would be more convincing with variance estimates. This is standard practice for empirical NLP/ML evaluations and should be addressed.

- **Steering direction mapping is underspecified.** Section 5 states that the authors "cluster positive and negative labels by evaluating samples for generation rather than using the original label" (line 139), referencing Arditi et al. (2024). However, the paper does not explicitly state, for each dataset, what the "yes" direction corresponds to in terms of the original task concept (e.g., for Paradetox: does "yes" mean the output is non-toxic? For Jailbreak: does "yes" mean the output is harmful/safe?). This makes it harder for readers to interpret what SSR actually measures — success at making the model say "yes," or success at activating the intended concept.

- **The choice of 70% layer for long-context experiments (Section 6.3) is stated but not justified.** The paper fixes layer=70% and α=1 for the k-shot experiments without explaining why these specific values were selected. While the preceding results (Section 6.1) show that layers above 0.7 preserve format well, making 0.7 a reasonable choice, the text should make this connection explicit.

### Trivial
None.

## Nice-to-Haves

- **Compare against existing evaluation approaches.** The paper argues that token-based evaluation is preferable to logit-based evaluation (Section 3), giving two reasonable arguments. However, no experiments demonstrate that logit-based metrics would give different or less informative results. A direct comparison would strengthen the case for the proposed framework.

- **Discuss the scope limitation to yes/no formats.** The current evaluation framework only works for yes/no generation tasks. The paper could acknowledge this limitation and discuss how the framework might generalize to other output formats.

- **Add baseline comparison to no-steering or random-steering conditions.** A comparison with random-direction steering would help isolate whether the observed side effects are specific to concept steering or simply a general effect of perturbing hidden states.

## Removed Points

These points from the reviewer inputs were removed with justifications:

- *"No analysis of steering magnitude alpha"* — **Factually wrong.** The paper explicitly uses α ∈ {0.2, 0.4, 0.6, 0.8, 1.0, 5.0} (line 172), Figure 7 is described as "Evaluation on steering effects across different α values" (line 181), and Section 6.2 discusses how SSR varies with alpha (lines 192–194).
- *"Definitional errors undermine the validity of every quantitative claim" / "fatal flaw"* — **Overstatement.** The $S_{y\rightarrow y}$ issue in $\mathcal{T}_{\mathrm{rel.fail}}$ affects one element of one metric's definition. The SSR, FPR, and irrelevant-task SER definitions are coherent, and the core experimental trends would not collapse with a corrected definition. This is a minor imprecision, not a structural error.
- *"Figures are redundant"* — Subjective presentation preference.
- *"Related work is overly long"* — Subjective judgment.
- *"The 'consequence generation' framing is undersupported"* — The paper tests three concrete cases (query, relevant task, irrelevant task) that directly correspond to the stated framing.
- *"No absolute FPR values reported"* — The paper reports $\delta_{\text{format}}$, which is the meaningful quantity (change in format preservation due to steering). Absolute FPR values are not required to interpret the results.
- *"alpha=5.0 is extreme"* — A minor presentational observation, not a substantive weakness.
- *"Missing related works"* — Cannot be confirmed without external sources.
- *Formatting/style nitpicks about presentation* — Parser artifacts or subjective preferences.

## Novel Insights

The two reviewers largely converge on the paper's strengths (the evaluation framework fills a genuine gap) but diverge on severity. The harsh critic's "fatal flaw" framing of the $S_{y\rightarrow y}$ inclusion in $\mathcal{T}_{\mathrm{rel.fail}}$ is not supported by the paper's actual content: this is a definitional imprecision that can be resolved in a short clarification without altering any experimental conclusions. The more interesting insight that emerges from reading the reviews together is that the paper's core empirical findings — particularly the layer-dependent format collapse and the attenuation of steering effects in longer contexts — are genuinely novel despite the metric-definition roughness. The strength finder correctly identifies that the paper contributes the *first* systematic evidence of steering side effects on irrelevant tasks, which is a finding the community needs regardless of whether the $S_{y\rightarrow y}$ entry is resolved one way or the other. Neither reviewer identified a deeper methodological flaw (e.g., that the yes/no task doesn't capture what it claims to, or that the counterfactual comparison is confounded).

## Suggestions

1. **Clarify the SER definition in Section 3.3.** Remove $S_{y\rightarrow y}$ from $\mathcal{T}_{\mathrm{rel.fail}}$ if the intent is truly "when the positive label is not achieved," or add an explicit justification if it is intentionally included (e.g., if SER measures "any case where steering did not turn a non-yes into yes"). Ensure the verbal description and mathematical definition are aligned.

2. **Add statistical rigor.** Report bootstrap confidence intervals or standard deviations for all metrics. At minimum, run the key experiments (Figures 5, 7, 8) with at least 3 random seeds for steering vector computation and demonstration selection.

3. **Explicitly state the steering direction per dataset.** For each of Paradetox, SubjQA, and Jailbreak, state what the "positive" (yes) concept is and how the binary labeled samples map to the yes/no generation task.

4. **Consolidate overlapping figures.** Figures 5 and 6 both address format and steering outcomes; consider merging or moving some content to the appendix to streamline the presentation.

---
