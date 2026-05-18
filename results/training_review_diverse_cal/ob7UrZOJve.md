I now have a thorough understanding of the paper and the reviews. Let me synthesize the final review.

## Summary

This paper identifies a structural inefficiency in standard decoder-style LLMs — attention matrices in deeper layers degenerate to rank-1, single-column matrices ("lazy layers") — and proposes Inheritune, a training recipe that initializes a smaller model with early layers from a larger pre-trained reference model, then progressively grows and retrains it until performance matches the reference. On GPT-2 Large (36→18 layers) and XLarge (48→24 layers), Inheritune produces smaller models that achieve lower validation loss than the full-sized reference after the same 100K steps (e.g., 18-layer: 2.80 vs 2.85; 24-layer: 2.64 vs 2.65). Similar trends hold in a no-data-repetition regime (FineWeb_Edu, 100B tokens).

## Strengths

1. **Empirical discovery of lazy layers in standard LLMs.** The paper provides clear evidence (Figure 1) that attention matrices in deeper layers of GPT-2 Medium and Large collapse to rank-1, single-column structures — extending prior theoretical results on rank collapse to practical decoder-only architectures with residual connections and layer norms. This finding is novel and clearly demonstrated.

2. **Clear and convincing results for GPT-2 Large and XLarge.** An 18-layer GPT-2 Large trained with Inheritune achieves *lower* validation loss (2.80) and higher Lambada accuracy (34.64) than the full 36-layer reference (2.85/34.14) in a single round at the same 100K step count (Table 1). The 24-layer XLarge result (2.64 vs 2.65) follows the same pattern. These are the cleanest experiments and genuinely support the paper's thesis.

3. **Consistent superiority over initialization baselines.** Inheritune outperforms stacking, hybrid-stacking, and half-width initialization across all model sizes (Table 2), establishing that the benefit comes from the specific choice of inherited layers — not just from having a warm-start initialization.

4. **Robustness in the no-data-repetition regime.** On FineWeb_Edu (100B tokens), Inheritune-derived 16-layer models match the validation loss of full-size references and achieve higher average zero-shot downstream accuracy (48.08 vs 47.74 for Medium; 49.75 vs 49.44 for Large†) — showing the method is not an artifact of data repetition.

5. **Attention visualization confirms method's effect.** Figure 2 shows that Inheritune-trained models maintain focused attention patterns in their deeper layers, unlike the uniform patterns in the standard model's later layers — directly connecting the method to the diagnosed problem.

## Weaknesses

### Fatal
None.

### Major

1. **GPT-2 Medium comparison uses 3× the training steps of the reference.** The paper's flagship Medium experiment (24→16 layers) required three rounds of growth (12→14→16 layers, 100K steps each = 300K total), while the 24-layer reference was trained for only 100K. The "Steps = 100K" label for Ours in Table 1 is ambiguous — it describes each round, not total compute. The closest same-size comparator (16-layer random init at 200K) achieves 2.83 vs. Inheritune's 2.81, but we do not know whether the reference would improve with 200K or 300K training. This undermines the "matching" claim for the Medium case specifically. The Large and XLarge experiments (single round, same steps) are clean and not affected by this issue, but the paper's most detailed case study has a significant confound.

### Minor

2. **Ambiguity in the growth procedure (Algorithm 1).** The algorithm states "Grow $\mathcal{M}_{\text{tgt}}$ by inheriting additional layers" and the text says "can be initialized with lazy layers," but it is never specified precisely which layers are added and from where for the Medium experiment (12→14→16). Are they taken from corresponding positions in the reference model (e.g., layers 12–13, then 14–15)? Are they randomly initialized? The DistillBERT-style baseline description is more specific about layer indices than the Inheritune growth procedure itself. This matters for reproducibility and for understanding whether the method reuses the very layers it diagnoses as ineffective.

3. **FineWeb experiments lack clarity on growth rounds.** Section 5 states that all models are trained for 100K steps and that Inheritune variants are trained "following Algorithm 1." If the Medium variant (24→16 layers, starting from k/2=12) required multiple growth rounds, the total step count would exceed 100K — but the caption claims the models match the reference "despite using fewer layers" without clarifying total compute. If only a single round was used, the paper should state this explicitly.

4. **Connection between lazy-layer motivation and the method is not fully closed.** The paper shows that early layers make good initializations and lazy layers make poor ones, but the method does not directly demonstrate *remediating* lazy layers (e.g., by showing that a layer that was lazy in the reference becomes effective after retraining in Inheritune). The ablation (Table 4) shows that attn+MLP w/o layernorm initialization (2.80) performs similarly to the full method (2.81), suggesting the benefit may stem from good initialization of attention+MLP weights rather than specifically from avoiding degenerated layers. A direct analysis of attention rank evolution in Inheritune-trained vs. random-init models would strengthen the claimed mechanism.

### Trivial

5. The "Steps = 100K" column in Table 1 for the Medium Ours entry is technically true per-round but does not convey total training steps. A footnote or clearer column label would avoid confusion.

6. The distillation comparison at 50K steps (Figure 3) would benefit from an explicit statement that *all* models in that plot — Inheritune, KD, DistillBERT, and random-init — were trained for exactly 50K steps from their respective starting points. (The text says KD baselines are trained for 50K and the caption says Inheritune "after 50K steps," but the symmetry could be clearer.)

## Nice-to-Haves

- A FLOPs analysis (training and inference) would contextualize the practical efficiency claim, especially given the Medium compute discrepancy.
- An analysis of when lazy layers emerge during pre-training (early vs. late) could inform whether Inheritune could be applied during reference pre-training rather than post-hoc.
- A small-scale experiment on a more recent architecture (e.g., Pythia or LLaMA-style) would strengthen generality claims, but is not required for acceptance as a GPT-2-focused methods paper.

## Removed Points

The following criticisms from the reviewers were assessed against the paper text and found to be invalid, misinformed, or scope-creepy:

- **"Downstream evaluation is thin" (harsh critic):** The paper's primary claim is about validation loss; downstream (Wikitext, Lambada for OWT; 5 tasks for FineWeb) is secondary. The FineWeb experiments include a reasonable benchmark suite.
- **"Comparisons with distillation are limited / steps not matched":** The paper states both KD baselines are trained for 50K steps and Figure 3 compares all models at 50K. The critic partially misread the section; steps *are* matched in that experiment.
- **"The 'various sizes' claim is overstated":** The paper demonstrates 12, 14, 16 (Medium), 18 (Large), and 24 (XLarge) layers — clearly multiple sizes.
- **"Missing generality on other architectures":** A valid research direction but asking for experiments on LLaMA-style models for a GPT-2-focused methods paper is scope creep.
- **"No analysis of attention degeneration across training checkpoints":** Interesting supplementary analysis but not a weakness of the presented work.
- **"Lack of validation on held-out losses":** The paper already includes downstream evaluations.
- **Strengths from Strength Finder that are generic:** None that conflict with verified weaknesses; all strengths kept.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight the paper itself does not already articulate.

## Suggestions

1. **Fix the Medium experiment comparison.** Either (a) train the 24-layer reference for 300K steps and report its loss, (b) design a single-round Medium experiment (e.g., start at 16 layers directly), or (c) acknowledge the compute trade-off explicitly and recast the Medium claim accordingly.

2. **Specify the growth procedure precisely.** State which layers are added (reference layers or random) and at which indices, for each growth step in Algorithm 1 and the Medium experiment.

3. **Clarify the FineWeb growth rounds.** Specify whether the Inheritune variants in Section 5 required multiple growth rounds or were trained in a single round, and report total step counts accordingly.

4. **Add a control for the 24-layer reference at 200K/300K steps in Table 1** for all model sizes, not just the same-size random-init baselines, to establish the ceiling of extended training.

5. **Strengthen the mechanistic story** by showing attention rank evolution during Inheritune training (e.g., for layers that were lazy in the reference but become active after retraining). This would close the loop between the diagnosis and the method.

## Score and Decision

The paper identifies a genuine and understudied phenomenon, proposes a simple and principled method, and provides convincing evidence for GPT-2 Large and XLarge that smaller models can match or exceed larger ones. The GPT-2 Medium experiment has a significant compute confound, and several clarity issues need resolution, but these do not invalidate the core contribution. The method is straightforward, well-motivated, and the results on larger models are clean.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>