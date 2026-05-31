Now let me write the final review.

## Summary

This paper systematically compares SSMs (Mamba, Hyena, Mamba2, DeltaNet) and Transformers on associative recall (MQAR) and copying tasks, using 3000+ runs. The core finding is that SSMs require extremely narrow learning rate windows to succeed, while Transformers are robust across orders of magnitude. This optimization brittleness re-contextualizes prior claims about SSM expressivity limits: with proper tuning, Mamba can solve MQAR at sequence lengths far exceeding hidden dimension. The paper also reveals opposing scaling preferences (width for SSMs, depth for Transformers) and shows that 1-layer Mamba (but not 1-layer Transformer) can solve MQAR. Ablations identify the 1D convolution as critical for 1-layer Mamba's expressivity, and DeltaNet is shown to overcome the stability gap.

## Strengths

**S1. Clear demonstration of SSM optimization fragility.** Figure 1 shows Mamba and Hyena achieving high MQAR accuracy only within ~0.5 order-of-magnitude of learning rate, while Attention maintains near-perfect accuracy across 4+ orders of magnitude. This is a clean, well-controlled result from a fine-grained LR grid, directly contrasted with prior coarser grids that missed the optimal window. The result is robust across two tasks (MQAR and copy) and multiple architectures.

**S2. Proper tuning rescues SSMs at long sequences.** Figure 2 shows that with the correct learning rate, Mamba solves MQAR at sequence length 512 with hidden dimension 256 — a configuration where the Zoology replication (using Arora et al.'s LR grid) fails. This directly supports the claim that prior negative results were partly confounded by suboptimal optimization choices.

**S3. Opposing width-vs-depth scaling behaviors.** Figures 3–4 and Table 1 collectively show that 1-layer Mamba/Hyena improve with width while 1-layer Attention fails regardless of width; 2-layer Attention succeeds even at small widths. Table 1 on the copy task is particularly striking: a 24-layer Mamba with 150M parameters achieves only 16% accuracy, while a 12-layer Mamba with the same parameter count (wider) achieves 100%.

**S4. DeltaNet overcomes the optimization gap.** Figure 7 shows DeltaNet maintaining high MQAR accuracy across a wide learning rate range (similar to Transformers), unlike Mamba/Mamba2. The paper connects this to the Householder update rule avoiding the vanishing-gradient problem in diagonal-decay A matrices — a concrete architectural diagnosis.

**S5. Convolution ablation provides precise mechanistic link.** Table 2 shows that removing convolution from 1-layer Mamba drops accuracy from 99% to 2% (matching 1-layer Attention), and adding convolution to Attention raises accuracy from 2% to 99%. This cleanly isolates the source of 1-layer expressivity and supports the paper's central mechanistic analysis.

## Weaknesses

### Fatal
None.

### Major

**M1. The central claim overreaches the evidence.** The paper states (line 39): *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* This maximalist framing is undermined by the paper's own evidence. The different scaling behaviors (SSMs need width, Transformers need depth; Figures 3–4) and the fact that convolution is required for 1-layer Mamba expressivity but not for Transformers are genuine architectural/expressive differences. The paper's own results also show that even with optimal tuning, Hyena underperforms Attention at low widths (Figure 2). The paper's abstract and conclusion use a more measured framing ("not just in their expressivity but in their fundamental learnability"), but the introduction's strong dichotomy sets up expectations the evidence cannot fully meet. The paper would be more credible with a framing like "optimization is a critical, underappreciated confounder in architecture comparisons" rather than treating it as a replacement for expressivity explanations.

### Minor

**M2. Induction head analysis (Section 6) is suggestive but not conclusive.** The paper observes a loss bump in 1-layer Transformers that "resembles" induction head formation and hypothesizes that the model "attempts" to form induction heads. While the paper uses appropriately cautious language, loss curves alone cannot distinguish induction head formation from other optimization phenomena (e.g., saddle point dynamics, batch noise effects). The original induction head literature (Olsson et al. 2022) relied on mechanistic attention-pattern analysis, which is not provided here. This does not invalidate the section, but the claim is notably weaker than the rest of the paper's evidence.

**M3. Validation only on synthetic tasks.** The paper acknowledges this in Section 8: *"validating these dynamics on downstream language modeling tasks is a critical next step."* However, this is a genuine limitation that reduces the strength of the broader claims about learnability vs. expressivity. MQAR and copying are highly correlated with in-context learning but are not actual language modeling. Even a small-scale perplexity evaluation would substantially strengthen the bridge from synthetic to real tasks.

### Trivial
None.

## Nice-to-Haves

- Measuring gradient norms during training to directly test the hypothesized vanishing/exploding gradient mechanism would strengthen the paper's own causal explanation for the narrow LR window.
- The heatmaps in Figure 3 are described textually; the actual figures in the submission would benefit from clearer annotations.

## Removed Points

- **Table 2 contradicts equivalence thesis (removed):** The harsh critic claimed that Mamba w/o conv = Transformer (both 2%) contradicts the paper's thesis. However, the paper explicitly uses this result to argue for a "strong mechanistic link" — the result supports rather than undermines the paper's analysis. The paper does not claim Mamba-without-convolution is equivalent to Transformer-with-convolution.
- **2-layer Hyena persistent gap (removed):** The paper acknowledges this gap and attributes it to the memory bottleneck. This is an architectural issue but does not refute the paper's claim that optimization is a confounder — the paper acknowledges expressivity differences exist.
- **Scaling behavior reveals fundamental differences (removed):** The paper presents this as an empirical finding, not as counter-evidence to its own thesis. The paper's claim is that optimization has been *underappreciated*, not that no architectural differences exist.
- **"Conflates can learn with equivalent learnability" (removed):** The paper's abstract and conclusion use the measured framing "not just in their expressivity but in their fundamental learnability." The stronger phrasing in the introduction is a framing issue (captured in M1) but this broader critique overstates the paper's overreach.
- **All formatting/style/typo criticisms (removed):** These are parser artifacts, not author errors.
- **Missing related works (removed):** Per instructions, as I cannot verify missing references.
- **Reproducibility nitpicks (removed):** The paper includes a reproducibility statement and refers to an appendix for full hyperparameter details.
- **Various generic criticisms from Strength Finder:** Generic praise ("important problem") and generic criticisms mixed into specific weaknesses were filtered per the merging rules.

## Novel Insights

None beyond the paper's own contributions. The paper itself provides the central novel insight: that SSM optimization dynamics, specifically narrow LR windows, systematically confound expressivity comparisons. This observation, while simple in retrospect, is empirically well-supported and has practical consequences for how the community should evaluate these architectures.

## Suggestions

1. **Recalibrate the central claim.** Change the introduction's strong dichotomy ("not in terms of expressive power but mainly because of") to something like "optimization dynamics are a critical confounder that has been underappreciated in prior expressivity comparisons." The abstract and conclusion already use more measured language; the introduction should be aligned.
2. **Add mechanistic evidence or tone down the induction head claim.** Either include attention-pattern analysis (e.g., examining attention maps during the loss bump) or explicitly label the hypothesis as requiring further validation. The current framing sits between speculation and evidence, which weakens an otherwise strong empirical paper.
3. **Add gradient norm measurements.** The paper hypothesizes that SSM instability stems from vanishing/exploding gradients. Directly measuring gradient norms during training would provide causal evidence for this mechanism and substantially strengthen the paper's explanatory power.
4. **Include a small-scale downstream validation.** Even one experiment showing that the narrow LR window transfers to a downstream language modeling task (e.g., perplexity on a small LM benchmark) would address the key generalizability concern.

## Score and Decision

**Score calibration:**

*Round 1 (bracketing):* Three parallel searches over score bands (0–3.5, 3.5–7.5, 7.5+). Low-band anchors (~3.0) were clearly weaker papers — this paper is substantially stronger than those. High-band anchors (7.6–8.0) were exceptionally clean, theoretically grounded papers (Small-scale Proxies, Never Train from Scratch). The paper under review sits in the middle band.

*Round 1 bracket:* **5.0–7.0**.

*Round 2 (narrowing):* Searched within (4.5–6.5) and (6.0–8.0) for topically similar papers. Read in full:
- Zoology (6.33) — Directly related (same task, MQAR). This paper is more rigorous on the optimization axis but less broad. Similar or slightly stronger.
- Understanding Bottlenecks of SSMs (6.00) — Theoretical/empirical SSM limitations. Similar quality, comparable contribution.
- On Limitation of Transformer for Learning HMMs (5.25) — Empirical architecture comparison. This paper is clearly stronger.
- State Space Models Provably Comparable (5.75) — Theoretical SSM expressivity. This paper has stronger empirical contribution.
- Small-scale Proxies (8.00) — Clean experimental design, clear practical recommendations. This paper is weaker.

The paper is better than Zoology (6.33) and Understanding Bottlenecks (6.00) in terms of experimental thoroughness and actionable findings, but not as cleanly framed as the 7.5+ papers.

*Additional round-2 anchors (not read in full):* 5.75 (QF), 6.00 (EG), 6.00 (pym), 6.25 (PJj), 6.33 (LY), 6.50 (GeU), 6.75 (xwK), 7.33 (hwS).

*Final score:* **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>