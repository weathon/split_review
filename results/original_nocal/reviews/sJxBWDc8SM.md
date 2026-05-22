I have verified all the claims. Let me now write the final consolidated review.

## Summary

This paper conducts a large-scale empirical study (3,000+ runs, ~20,000 GPU hours) comparing Transformers and modern recurrent models (Mamba, Hyena) on associative recall (MQAR) and copying tasks. It demonstrates that SSMs exhibit severe learning rate sensitivity — their success is confined to a narrow LR window that prior work (Arora et al., 2023) missed, recontextualizing previous expressivity comparisons. It also shows that SSMs favor width over depth (while Transformers favor depth over width), that a 1-layer Transformer shows a loss bump reminiscent of induction head formation without accuracy gain, and that architectural components (convolution, gating) are critical for 1-layer expressivity. The central message is that optimization stability, not just expressivity, is a key differentiator between these architecture families.

## Strengths

1. **Clear demonstration of critical LR sensitivity in SSMs (Figures 1, 5).** The paper shows that Mamba and Hyena achieve high accuracy only within an extremely narrow learning rate window (e.g., Mamba peaks at ~0.0001), while Attention maintains near-perfect accuracy across orders of magnitude. This directly challenges prior work whose fixed LR grids missed these narrow optima, and is supported by dense LR sweeps (roughly 10 values per order of magnitude).

2. **Well-controlled scaling experiments reveal contrasting width/depth preferences (Figures 3, 4; Table 1).** A 1-layer Transformer never solves MQAR regardless of width (accuracy ~2% across all dimensions), whereas properly tuned Mamba solves it even at small widths. On the copy task (Table 1), scaling Mamba in width (12 layers, width 1408) yields 100% accuracy, while scaling in depth (24 layers, width 1024) yields only 16% at the same parameter count. This concretely demonstrates that architectures must be scaled along their preferred axes.

3. **Architectural ablation cleanly isolates the source of 1-layer expressivity (Table 2).** Adding a 1D convolution to a 1-layer Attention model boosts accuracy from 2% to 99%, and removing the convolution from a 1-layer Mamba drops accuracy from 99% to 2%. This pinpoints the convolution as the mechanistic driver of the shallow-model performance gap. The S6 mixer alone (without gating) retains full expressivity, further narrowing down the critical component.

4. **Large-scale controlled experimental setup.** Over 3,000 runs with 5 seeds per configuration, systematically varying learning rates, model dimensions, sequence lengths, and architectures. This thoroughness provides a reliable foundation for the paper's claims about sensitivity and makes the negative results (e.g., 1-layer Attention failure) credible.

5. **Cross-task validation.** The LR instability (Figure 5) and scaling behavior (Table 1) are independently confirmed on a second synthetic task (copying), strengthening generality beyond MQAR.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Overstated central thesis in one sentence.** The introduction states (line 43): *"Transformers differ from SSMs **not in terms of expressive power** but mainly because of their optimization dynamics."* This absolute framing is contradicted by the paper's own evidence: (a) Section 4 acknowledges that "a sizable gap with Transformers can still be observed at low widths (e.g. Hyena)" (line 144), and (b) Section 7 shows that adding a convolution to a 1-layer Transformer enables it to solve MQAR — an architectural/expressivity fix, not an optimization one. The abstract and discussion use a more defensible framing (*"not just in their expressivity but in their fundamental learnability"*), which is fully supported. The one sentence on line 43 should be harmonized to match the paper's nuanced conclusions.

2. **Induction head interpretation lacks mechanistic evidence.** Section 6 interprets a loss bump in the 1-layer Transformer as the model *"attempt[ing] to form induction heads"* (line 192). The paper uses appropriately cautious language ("resembles," "hypothesize"), and the raw observation (a loss bump without accuracy gain in a 1-layer model) is novel and interesting. However, no attention-pattern analysis, head attribution, or ablation is provided to support the induction head interpretation. The paper would be stronger with even a simple qualitative inspection of attention maps during the bump, or by tempering the claim to simply note the loss bump as an unexplained empirical observation.

### Trivial
None.

## Nice-to-Haves

- **Real language modeling validation.** The paper acknowledges this as a limitation (line 239). A small-scale perplexity experiment on WikiText-2 or similar would substantially strengthen the claim that the findings translate beyond synthetic tasks.
- **Investigation of other optimization hyperparameters.** Only base learning rate is varied. Testing cosine schedules, warmup, or different optimizers would clarify whether the narrow LR window is fundamental or mitigable.
- **Gradient norm analysis during training.** The paper hypothesizes that vanishing gradients in the SSM recurrence (via decay in A_k) cause the instability (Section 7), but does not provide direct gradient measurements.
- **Larger-scale DeltaNet experiments.** The DeltaNet results (Figure 7) are limited to dimension 256 due to implementation constraints. Scaling to 512+ would test whether the stability advantage holds at competitive sizes.

## Removed Points

- **"Opposite scaling behaviors" claim is not supported** — The harsh critic challenged this, but the paper's evidence (2-layer Attention succeeds where 1-layer fails regardless of width; 1-layer Mamba succeeds with width; Table 1 shows width > depth for Mamba on copying) supports the characterization. "Opposite scaling behaviors" accurately captures that Attention scales best with depth while SSMs scale best with width. Removed.
- **Missing LR schedule / optimizer experiments** — These are outside the paper's stated scope. The paper focuses on establishing the basic LR sensitivity phenomenon. Removed (moved to Nice-to-Haves).
- **"No evidence that >2 layers doesn't help"** — The paper states this claim (line 144) in context of prior work (Olsson et al., 2022) which established that 2-layer models suffice for MQAR. The claim is supported by the cited literature. Removed.
- **Miscellaneous formatting/presentation nitpicks** from the section-by-section notes — generic, non-substantive. Removed.

## Novel Insights

The most novel insight to emerge from cross-referencing the reviews is that the paper's key contributions are actually separable: (1) the empirical finding that SSMs have a critically narrow LR window (robust, well-supported), and (2) the induction-head-like dynamics in a 1-layer Transformer (a novel observation that is independent of the mechanistic interpretation). The latter could be strengthened or simply reported as an observation without the induction head framing. Additionally, the convolution ablation (Table 2) cleanly deconfounds architecture from optimization in a way that is rarely done in the SSM vs. Transformer literature.

## Suggestions

1. **Harmonize the central thesis.** Replace the overly strong statement on line 43 ("not in terms of expressive power but mainly because of their optimization dynamics") with the more accurate framing used in the abstract and discussion ("not just in their expressivity but in their fundamental learnability").
2. **Either add mechanistic evidence or temper the induction head claim.** If feasible, include attention-map visualizations during the loss bump (even in an appendix). If not, remove the induction head interpretation entirely and report the loss bump as an unexplained observation — the finding is still interesting without the attribution.
3. Add the distribution of hyperparameter grid values used (learning rates tested) as a table, to make it easy for readers to reproduce the sweeps.
4. The paper could mention the "sizable gap at low widths" (line 144) earlier in the introduction to avoid the appearance of overclaiming.

## Score and Decision

Based on my assessment: the paper makes solid empirical contributions on an important question (what differentiates SSMs from Transformers), backed by a large-scale controlled experimental setup. The weaknesses are minor framing issues that do not undermine the core findings. The paper is well-written, the experiments are carefully conducted, and the conclusions (when stated in their softer form) are well-supported.

**Originality**: Good — identifies a practical confound (LR sensitivity) that prior work overlooked.  
**Importance of research question**: High — understanding the SSM-Transformer gap is a central question.  
**Claims supported**: Mostly yes, with one overstated sentence that should be corrected.  
**Soundness of experiments**: Strong — dense hyperparameter sweeps, multiple seeds, cross-task validation.  
**Clarity**: Good, with minor inconsistencies in the central claim.  
**Value to community**: High — provides practical guidance for fair comparison between architectures.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>