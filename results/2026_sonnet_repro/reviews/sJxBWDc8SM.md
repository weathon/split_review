Now let me do the calibration search to properly score this paper.Round 1 bracket: **5 to 7**. Let me narrow with Round 2.Now I have enough calibration data to write the final review. Let me compare:

- **iVy7aRMb0K (4.5, rejected)**: Similar premise (training difficulties ≠ capacity limits), but narrower scope and a single fix. The paper under review is substantially more comprehensive.
- **pymXpl4qvi (6.0, accepted)**: SSM bottlenecks — theoretical + empirical. Paper under review is comparably empirical but more comprehensive, without theoretical component.
- **QFgbJOYJSE (5.75, accepted)**: Theoretical SSM–Transformer comparison. Similar relevance.
- **sZJNkorXMk (6.67, accepted)**: Stronger theoretical grounding. Paper under review is weaker theoretically.
- **PdaPky8MUn (8.0, accepted)**: "Never Train from Scratch" — operates at LM scale, broader task set, data-driven priors. Clearly stronger and more impactful.

**Round 1 bracket: 5–7. Round 2 narrows to 5.5–6.5.** The paper under review is more comprehensive empirically than the 5.75 anchor but has no theory and its central thesis slightly overclaims. The 6.0 anchor (Understanding Bottlenecks) is comparable in scope. I place this at **6.0**.

---

## Summary

This paper conducts a large-scale empirical investigation (3,000+ runs, ~20,000 GPU hours) comparing SSMs (Mamba, Hyena) and Transformers on two synthetic benchmarks — multi-query associative recall (MQAR) and copying — highly correlated with language modeling performance. The central finding is that SSMs exhibit a critical optimization instability: success is confined to an extremely narrow learning rate window, which can confound evaluations and lead to misleading conclusions about architectural expressivity. Careful hyperparameter tuning reverses key prior conclusions (notably Arora et al., 2023), and a targeted ablation identifies Mamba's 1D convolution as critical to single-layer expressivity.

---

## Strengths

1. **Narrow LR window reverses prior conclusions (Figure 1, 2):** Figure 1 shows, concretely and across five seeds, that Mamba and Hyena achieve high accuracy only in a very narrow learning rate window (e.g., peak near 1e-4 for Mamba vs. near-perfect across three orders of magnitude for Attention). This directly implicates optimization as a confounder in Arora et al.'s comparisons, where the SSM-favorable learning rates were outside the Zoology grid.

2. **Properly-tuned Mamba solves MQAR at small hidden size (Figure 2):** With the finer LR grid, Mamba achieves near-perfect accuracy at sequence length 512 with model dimension 64, directly contradicting the published claim that hidden size must match sequence length. This is a concrete, falsifiable contribution.

3. **Contrasting scaling laws (Figures 3–4, Table 1):** Single-layer experiments establish that SSMs benefit from width while Transformers require depth: 1-layer Attention fails regardless of width (Figure 3), while 1-layer Mamba with sufficient width succeeds. Table 1 confirms on copying that deeper-but-narrower Mamba (24L × 1024) fails while wider-but-shallower Mamba (12L × 1408) solves the task at matched parameter count. This is a practical and reproducible finding.

4. **Mechanistic ablation pinpoints conv1d (Table 2):** Removing conv1d from 1-layer Mamba drops accuracy from 99% to 2% — the same failure point as 1-layer Attention. Conversely, adding conv on QKV in a 1-layer Transformer recovers 99% accuracy. This is a tight, bidirectional ablation that gives a specific mechanistic link.

5. **DeltaNet as architectural direction (Figure 7):** DeltaNet achieves Transformer-level LR robustness, and the paper links this to Householder matrices avoiding decay-induced vanishing gradients. This provides a concrete architectural pointer for future work on optimization-stable SSMs.

---

## Weaknesses

### Fatal
None.

### Major

- **Central thesis overclaims "mainly optimization"**: The abstract declares: *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* This is contradicted by the paper's own results. Hyena still fails at low widths even under optimal LR (Figure 2, Hyena row, small model dimensions), single-layer Transformers cannot solve MQAR regardless of width or tuning (Figure 3), and Section 7 acknowledges that "while the original 2-layer Mamba is robust to convolution removal, removing it from a 1-layer Mamba reduces its accuracy to the same failure point as the 1-layer Transformer." The more defensible claim — that optimization instability is a *significant and previously underweighted* factor, alongside expressivity differences — is what the data actually support. The Discussion is somewhat more careful ("lies not just in their theoretical expressivity"), but the abstract and Introduction overstate it. This is a framing mismatch, not a fatal flaw, but it misleads readers about the paper's actual findings.

### Minor

- **"Fundamental mismatch in the loss landscape" is inferred, not measured**: The paper claims a "fundamental mismatch in the loss landscape" (abstract and Section 3) but never directly measures the landscape. No gradient norms, no sharpness analysis, no loss surface visualization is provided. The evidence is entirely task-performance sensitivity to LR, which cannot distinguish between "SSM loss landscape is intrinsically sharper" and "SSM's optimal LR is smaller and thus easier to miss with a coarse grid." This weakens the mechanistic story without invalidating the empirical finding.

- **Induction head observation (Section 6) is elevated beyond its evidential support**: The paper observes a loss bump in 1-layer Attention training and writes: "we hypothesize that during this phase transition, the Attention mechanism *attempts* to form induction heads." This is an interesting observation, but the paper provides no attention pattern analysis, no circuit-level evidence, and no comparison to the canonical 2-layer bump timing. In the bullet-point contributions list, this appears as a confirmed "finding" rather than a hypothesis. The observation itself is valid and interesting; it should remain, but framed as a hypothesis throughout.

- **DeltaNet stability explanation is also a hypothesis**: The claim that DeltaNet's stability stems from Householder matrices avoiding vanishing gradients (Section 7) is offered as a hypothesis attributed to Trockman et al. (2024), with no gradient norm analysis to verify it in this paper's setting. This is fine as a pointer but should not be presented as an established finding.

### Trivial

None that survive filtering.

---

## Nice-to-Haves

- **Direct landscape measurement**: Gradient norm trajectories or sharpness analysis for Mamba vs. Attention at the same task would convert the "loss landscape mismatch" interpretation from inference to evidence — and would directly support or qualify the central thesis.
- **Attention pattern visualization for the loss bump**: Showing attention maps during and after the 1-layer bump would confirm or refute the induction head hypothesis clearly.
- **At least one larger-scale or LM experiment**: A brief experiment on a downstream task (even a small-scale pretrained setting) would substantially broaden the scope of the claim. The paper acknowledges this as future work, which is acceptable.
- **Scope of the depth/width dichotomy**: The claim "recurrent models benefit from width while Transformers benefit from depth" is stated as a general principle but is grounded only in these two synthetic tasks at small scale. Flagging this as a property observed in this specific setting would be more precise.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **[Harsh Critic: "missing expressivity analysis / 2-layer Transformer still matches SSMs"]**: The critic notes that 2-layer Attention matches or exceeds SSMs in many conditions and calls this a problem for the thesis. The paper acknowledges the depth-width dichotomy explicitly and frames 2-layer Attention as performing differently (not better) than 1-layer Attention — the comparison is intentional and the paper's scope is about how optimization confounds comparisons, not that SSMs dominate everywhere. REMOVED as misunderstanding scope.

- **[Harsh Critic: "Figure 3 caption contradiction"]**: The harsh critic notes the caption describes "high accuracy for Attention across all dimensions" in Figure 3 while the text says single-layer Attention cannot solve the task. This is a PDF parsing artifact where the image description was extracted incorrectly — the text and its caption (line 126: "Attention models can no longer solve the task") clearly match. REMOVED as parser artifact.

- **[Harsh Critic: "Figure 4 caption is misleading"]**: The extracted image description says "Attention models show constant accuracy with increasing parameters," which contradicts the actual caption at line 138 ("attention-based models benefit from scaling in depth"). REMOVED as parser artifact.

- **[Strength Finder: "training dynamics provide concrete evidence that loss landscapes differ qualitatively"]**: The loss bump observation is interesting, but it does not provide direct evidence about landscape geometry — it provides evidence about training dynamics, from which landscape differences are inferred. WEAKENED and merged into the minor weakness above.

- **[Strength Finder: generic importance framing]**: Dropped framing like "the paper addresses an important and timely question" as too generic.

---

## Novel Insights

The most genuinely novel insight is the bidirectional conv1d experiment in Table 2: the fact that removing conv1d from 1-layer Mamba reduces it to the same failure point as 1-layer Attention (2%), while adding conv on QKV to 1-layer Attention recovers full performance (99%), establishes a tight mechanistic equivalence. This is not merely an ablation of Mamba — it is a positive result showing that a single architectural component (locality induction via conv1d) is the minimal sufficient add-on for expressivity in shallow sequence models, regardless of whether the base architecture is recurrent or attention-based. Combined with the DeltaNet observation, the paper opens a design axis (decay vs. orthogonal state transitions) for improving optimization stability in SSMs.

---

## Suggestions

1. **Revise the central thesis**: Change "mainly because of their optimization dynamics" to "in large part because of their optimization dynamics, alongside expressivity differences that become apparent in unfavorable settings." The abstract already has a more nuanced conclusion ("lies not just in their theoretical expressivity"), but the thesis statement on page 2 should match.
2. **Add gradient norm or sharpness measurements** along training for Mamba vs. Attention to directly ground the "loss landscape mismatch" claim.
3. **Keep the induction head hypothesis as a hypothesis** in all contexts, not just in the Section 6 text; revise the contribution bullet in the introduction accordingly.
4. **Add at least a brief note quantifying the LR window width** (e.g., how many orders of magnitude Attention tolerates vs. Mamba) to make the instability more precise.

---

## Score and Decision

**Anchors consulted:**

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| iVy7aRMb0K.md (Mimetic Init) | 4.50 | R1 | Similar premise; this paper is far more comprehensive and general |
| QFgbJOYJSE.md (SSMs Comparable) | 5.75 | R1 | Theoretical paper; comparable scope, this paper is more concrete empirically |
| pymXpl4qvi.md (Bottlenecks of SSMs) | 6.00 | R1/R2 | Closest analog; this paper is more comprehensive empirically, less theoretical |
| EGjvMcKrrl.md (SSM Optimization) | 6.00 | R2 | Theoretical+empirical; comparable contribution level |
| sZJNkorXMk.md (Autocorrelation Init) | 6.67 | R2 | Stronger theory; this paper weaker theoretically |
| PdaPky8MUn.md (Never Train From Scratch) | 8.00 | R1 | Operates at LM scale with broader tasks; clearly stronger |

**Bracket from Round 1:** 5–7.
**Narrowed by Round 2:** 5.5–6.5.

The paper is most comparable to the 6.0 anchors (pymXpl4qvi, EGjvMcKrrl). It is more empirically comprehensive than both — 3,000+ runs, two tasks, multiple architectures, a clean mechanistic ablation — but lacks theoretical grounding and has an overclaimed central thesis. On balance, it sits at **6.0**: a genuine empirical contribution that shifts how the community interprets prior comparisons, with minor overreach in framing and some mechanistic claims that remain hypotheses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>