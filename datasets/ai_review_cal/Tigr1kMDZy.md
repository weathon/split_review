- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6
Here is the final consolidated review.

---

## Summary

This paper studies how language models imitate incorrect few-shot demonstrations. Using the logit lens to decode predictions from intermediate layers, the authors identify two phenomena: (1) *overthinking* — models given false demonstrations perform better at intermediate layers than at the final layer, suggesting harmful imitation occurs late in processing; and (2) *false induction heads* — specific attention heads in late layers that attend to and copy incorrect labels, whose ablation reduces the accuracy gap between correct and incorrect prompts by 38.9% on GPT-J. The behavioral phenomenon (overthinking) is demonstrated convincingly across 11 models and 14 datasets; the mechanistic claim (false induction heads as a cause) is causally tested on one model (GPT-J) with correlational support across others.

## Strengths

- **Broad cross-model and cross-dataset validation of the overthinking phenomenon**: The paper demonstrates that intermediate-layer accuracy degrades at late layers when models receive incorrect few-shot demonstrations across 11 diverse models (GPT-J, GPT-NeoX, Pythia variants 410M–12B, Llama2-7B, and instruction-tuned variants) and 14 classification datasets (Section 4, Figure 4). This goes well beyond prior single-model studies and convincingly establishes that overthinking is a general behavioral pattern.

- **Causal identification of false induction heads with controlled ablation**: The paper defines a prefix-matching (PM) score to identify attention heads that are both label-attending and class-sensitive, then ablates the top 5 such heads in GPT-J. This reduces the accuracy gap between correct and incorrect prompts by 38.9% on average across 14 datasets, while random-head ablations have negligible effect (Section 5, Table referenced at line 227). The inclusion of a label-promoting verification using head-level logit lens (lines 233–247) strengthens the causal story.

- **Controlled experimental design isolating the mechanism**: The paper systematically compares permuted labels, random labels, half-correct labels, and semantically unrelated labels (Sections 3.2, 6). This controls for alternative explanations (e.g., mere randomness vs. specific copying of false content) and shows that overthinking is specifically tied to the ground-truth content of false labels, not just label inconsistency.

- **Component-level ablation isolating attention heads from MLPs**: By independently zeroing attention heads and MLPs in late layers, the paper shows that attention heads account for most of the overthinking effect (Section 4, line 195). This finer-grained localization supports the attention-head mechanism before the head-level analysis begins.

## Weaknesses

### Fatal
None.

### Major

- **Central causal mechanism tested on only one model (GPT-J)**. The paper demonstrates overthinking behaviorally across 11 models (Section 4) and shows that PM scores rise around critical layers for all models (line 218). But the causal intervention that establishes the mechanistic claim — ablating false induction heads — is performed exclusively on GPT-J (line 222: "We select the 5 heads from GPT-J with the highest PM scores"). The claim that "false induction heads cause overthinking" as a general phenomenon is therefore supported by causal evidence on one model and only correlational evidence (PM score trends) on others. This does not invalidate the contribution for GPT-J, but it means the paper's generality claim outruns its evidence. Ablation on at least one additional model family (e.g., Pythia-6.9B or Llama2-7B) would substantially strengthen the paper.

### Minor

- **The logit lens is the sole method for identifying overthinking, with acknowledged but not addressed reliability concerns**. The paper relies on the logit lens to decode intermediate predictions and identify critical layers. The Discussion (lines 263–271) acknowledges that the tuned lens (Belrose et al., 2023) provides a more reliable alternative and notes that Belrose et al. validated overthinking with it, but the paper does not present those results itself. While the behavioral phenomenon appears robust, the precise localization of critical layers could be sensitive to this methodological choice.

- **The PM score is computed only on the toy Unnatural dataset, and the head selection procedure is not validated on the other 14 datasets**. The paper computes PM scores on Unnatural (line 217), selects the top 5 heads, and then ablates them on all 14 datasets with positive results. The generalization is empirically demonstrated (the ablation works across datasets), but the paper does not check whether the same heads would be top-ranked using PM scores computed on each dataset individually. A consistency check would strengthen confidence that the Unnatural-based selection is not idiosyncratic.

- **No variance or confidence intervals reported for the key ablation result**. The 38.9% reduction in the accuracy gap (line 227) is reported as a point estimate across 14 datasets. Given the number of datasets, reporting standard errors or per-dataset variability would help assess the reliability of this effect.

- **The "critical layer" definition uses an ad hoc heuristic whose sensitivity is not examined**. The critical layer is defined as "the layer at which the accuracy gap first reaches half of its final value" (footnote, line 183). For Llama2-7B, a range of layers 13–17 is reported, suggesting the divergence is less sharp for some models. The paper does not examine how sensitive this definition is to the choice of threshold.

### Trivial

- The number of ablated heads (5) is stated without justification in the main text. The appendix varies this number (line 382), which addresses the concern, but a brief reference in the main text would be helpful.
- The paper does not discuss whether the identified false induction heads overlap with, are a subset of, or are distinct from the standard induction heads identified by Olsson et al. (2022), which the paper draws from.

## Nice-to-Haves

- Validate causal head ablations on at least one additional model family (Pythia or Llama2).
- Compute PM scores on a subset of non-toy datasets to verify head selection consistency.
- Fit a piecewise linear or changepoint model to the layerwise accuracy curves to formalize the critical layer definition, rather than the ad hoc "half final gap" heuristic.
- Discuss whether the false induction heads overlap with standard induction heads (Olsson et al., 2022).

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"The PM score normalization is not derived from any principle"* — The normalization 1/(#labels−1) is a standard way to penalize attention to incorrect labels under a uniform baseline. The design is reasonable, not arbitrary. Removed because the criticism is overstated and not a genuine weakness.
- *"The logit lens might produce unreliable results at early-to-middle layers"* as a Fatal or Major concern — The paper explicitly addresses this in the Discussion (comparing to probing, citing Belrose et al. validation). The concern is acknowledged and partially mitigated. Demoted to Minor above.
- *"The paper could report confidence intervals"* — Kept as Minor above (it is a reasonable suggestion, not a removed point).
- *"The overthinking framing vs. Kaya et al. should be clarified"* — A very minor conceptual note. The paper uses "overthinking" as an analogy, not a direct import of Kaya's definition; the conceptual difference is clear from context. Removed as a nitpick.
- Strength Finder's *"Logit lens as a scientific tool rather than engineering shortcut"* — This is a generic framing observation, not a concrete strength of the paper's evidence. Removed.
- Strength Finder's *"Component-level ablation isolating attention heads from MLPs"* — This is valid, but it is part of the broader story rather than a standalone strength. Merge into the strengths about controlled design.

## Novel Insights

None beyond the paper's own contributions.

The reviews surface a clear structural tension: the behavioral phenomenon (overthinking) is demonstrated broadly across 11 models, while the causal mechanism (false induction heads) is causally tested on only one. The paper does not hide this — the limitation is inherent in the scope of the ablation study — but the consolidated review should not inflate it into a fatal flaw. Conversely, the paper's genuine strengths (broad cross-model validation of the phenomenon, controlled behavioral experiments, careful three-property definition of false induction heads) are well-grounded and should not be discounted.

## Suggestions

1. **Highest leverage**: Perform the head ablation study on at least one other model (Pythia-6.9B or Llama2-7B). Even a single additional causal test would transform the paper from a single-model mechanistic study into a broadly applicable finding.
2. Compute PM scores on a few of the 14 non-toy datasets to verify that the same or similar heads would be selected, validating that Unnatural-based selection is representative.
3. Add standard errors or per-dataset breakdown to the 38.9% ablation result.
4. Include a brief mention in the main text that the choice of 5 heads is supported by the appendix analysis that varies the number.
