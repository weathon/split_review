- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have a thorough understanding of the paper and the two reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper investigates whether LLMs (GPT-2 and GPT-2-medium) exhibit neuron-level spatial differentiation between memorization and generalization behaviors, and whether these behaviors can be predicted and controlled at inference time. Using two synthetic tasks (in-context inference on a variant of bAbI, and arithmetic addition with embedded memorization patterns), the authors collect paired hidden-state representations where nearly identical inputs trigger opposite behaviors, compute neuron-wise mean differences (NMD), train per-layer classifiers, and develop an inference-time intervention that shifts activations along the NMD direction to flip behavior. The intervention achieves up to 83.7% shift rates (in-context inference) with far lower random-baseline rates.

## Strengths

- **Clean pairwise extraction method to isolate behavioral differences**: By rephrasing inputs (reordering sentences in bAbI; swapping addends in arithmetic) and selecting only the ~11%/8.5% of cases where the model's output behavior flips, the paper ensures that extracted hidden-state differences are primarily attributable to the memorization/generalization process rather than to input variation (Section 3.2). This is a methodologically sound design choice.

- **Strong intervention results, especially for the in-context inference task**: Table 1 reports that targeted intervention shifts 83.7% of memorization→generalization and 89.9% of generalization→memorization, while random intervention produces negligible changes (Section 5.1). The hyperparameter analysis (Figure 7) further shows that the effect scales meaningfully with topN and alpha rather than being a threshold artifact.

- **Clear spatial differentiation pattern in the NMD heatmaps**: Figures 3 and 4 show that NMD values are near-zero in early layers and grow progressively in deeper layers, with both tasks exhibiting this pattern. The paper's own observation that the *last* layer differentiates strongly only when output format differs (addition task) while showing no clear differentiation when output format is consistent (inference task) provides an internal consistency check (Section 3.3, point 3).

## Weaknesses

### Fatal

None. The criticisms raised, while real, do not invalidate the paper's core claims when cross-checked against the actual paper.

### Major

- **The output-token confound partially undermines the neural differentiation interpretation, especially for the arithmetic addition task**. In the addition task, memorization outputs a random string (e.g., `<mem-7234f681>`) while generalization outputs a numeric sum (e.g., `2542`) — structurally different output tokens. The NMD in later layers may therefore partly capture planning for distinct output sequences rather than a general-purpose memorization/generalization "mode." The paper acknowledges this for the *last* layer (Section 3.3: "the NMD values in the last layer of GPT-2 show the most significant differentiation, reflecting the divergence in output format") but does not address whether the same confound influences earlier-layer NMD values. This weakens the causal framing ("neurons responsible for controlling memorization and generalization behaviors") relative to a purely correlational finding.

    **However**, the confound is less severe for the in-context inference task, where both behaviors produce color names (e.g., "red" vs. "crimson" — same output type, different tokens), and the last layer *does not* show clear differentiation precisely because the output formats are consistent. The earlier-layer differentiation in both tasks cannot be straightforwardly explained by output-token planning and remains a genuine finding.

- **The random-intervention baseline is too weak to establish specificity**: The baseline applies random shifts to *random* neurons. A stronger test would apply shifts of the same NDM magnitude but to low-correlation neurons, or apply random-magnitude shifts to the same high-correlation neurons. As is, the experiment shows that intervening on correlated neurons *works*, but does not fully establish that the *direction* and *identity* of the NMD-based intervention is what matters rather than any systematic perturbation of a sensitive subset.

### Minor

- **No statistical uncertainty reported**: The NMD heatmaps, classifier accuracy curves, and intervention results (Tables 1–2) are presented as point estimates without error bars, confidence intervals, or multiple-seed runs. This is especially important given the low pair-extraction rates (11%, 8.5%) which could introduce selection bias.

- **Dataset sizes for the pairwise extraction are underspecified**: The paper reports that ~11% and ~8.5% of instances flipped behavior, but never states the final N (how many pairs were collected). The classifier plots show "different quantities of extracted data" without specifying what those quantities are.

- **The classifier evaluation lacks an input-only baseline**: The classifiers use hidden states from each layer, but there is no comparison to a baseline that predicts behavior from input features alone (e.g., bag-of-words or embedding similarity). This makes it unclear how much value the hidden-state signal adds beyond what could be predicted from the input.

- **No per-layer ablation for the intervention**: The intervention applies to top-N neurons across *all layers simultaneously*. Ablating individual layers (or applying the intervention to only late vs. only early layers) would help pinpoint where the behavioral switch actually occurs.

### Trivial

- The paper states "the neurons responsible for controlling memorization and generalization behaviors exhibit a clear spatial characteristic" (Section 3.3) but the evidence is correlational (NMD) rather than causal — the causal evidence comes later in Section 5. This framing mismatch is a minor inconsistency.

## Nice-to-Haves

- Comparing the intervention against an alternative strategy such as logit perturbation or ITI (Li et al., 2024) applied to the same neurons would strengthen the claim that the specific NMD-based shift is the right direction.
- A task where memorization and generalization produce the *same* output (via different reasoning paths) would cleanly separate the neural differentiation claim from the output-token confound. This would be a significant methodological advance but is not required for the current paper's contributions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The pairwise extraction method is underspecified / how were rephrased inputs validated?"** (Harsh Critic) — The paper does specify the method (reorder sentences for bAbI; swap addends for arithmetic) and the rationale. This is adequately specified for a conference paper. *Reason: already addressed in the paper.*

- **"No evidence that the intervention changes *how* the model arrives at its answer"** (Harsh Critic) — The paper's claim is about output-level behavioral control, not about changing internal reasoning paths. Requesting causal tracing is scope expansion beyond what the paper sets out to do. *Reason: scope creep / soft rule.*

- **"No comparison to alternative intervention strategies (adding noise to logits, anti-memorization direction)"** (Harsh Critic) — Moved to Nice-to-Haves. *Reason: nice-to-have comparison, not a core flaw.*

- **"The tasks are artificial and may not generalize"** (Harsh Critic) — Moved from "Critical Issue" to limitations discussion below. The paper already acknowledges this in Section 6. *Reason: paper already addresses this in limitations.*

- **Strength Finder: strengths that are generic or sycophantic** — The Strength Finder's claim about "carefully designed pairwise extraction method" is concrete and retained. Claims about the "importance of the problem" are removed as generic. *Reason: per instructions, remove generic/unsupported strengths.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine confound concern (output-token differences partially overlapping with the memorization/generalization dichotomy) but do not offer a novel synthesis that the paper itself is missing. The most useful takeaway is methodological: the pairwise extraction approach is clever, but the field would benefit from task designs where memorization and generalization produce the same output via different routes to truly separate the two processes.

## Suggestions

1. **Add per-layer intervention ablations** to show which layers are causally responsible for the behavioral switch.
2. **Report error bars or multiple-seed variance** for all quantitative results (NMD, classifier accuracy, intervention rates).
3. **Strengthen the intervention baseline**: apply NMD-magnitude shifts to low-correlation neurons, or apply random-magnitude shifts to high-correlation neurons.
4. **Specify N (number of collected pairs)** clearly for both tasks.
