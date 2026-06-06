## Summary

This paper empirically investigates why modern recurrent models (SSMs such as Mamba and Hyena) underperform Transformers on associative recall (MQAR) and copying tasks. The central finding is that SSMs exhibit extreme sensitivity to learning rate: success is confined to a very narrow LR window, while Transformer performance is robust across nearly three orders of magnitude. Correcting for this confound in prior work (Arora et al. 2023, Jelassi et al. 2024) substantially improves SSM performance. Additional contributions include: contrasting width-vs-depth scaling laws for SSMs vs. Transformers, ablation of the 1D convolution as an expressivity-critical component, observation of a loss bump in single-layer Attention resembling (but not completing) induction head formation, and DeltaNet as a more stable SSM variant.

---

## Strengths

- **LR sensitivity is demonstrated rigorously and concretely (Figure 1)**: Attention maintains near-perfect accuracy across a wide LR range; Mamba and Hyena collapse to near-zero outside a narrow spike. This is the core finding and it is cleanly shown.
- **Proper tuning reverses published conclusions (Figure 2)**: A finer LR grid enables Mamba to solve MQAR at model dimension 64, sequence length 512 — a configuration previously claimed to require hidden size ≈ sequence length. This is a direct, falsifiable refutation of a prior claim.
- **Contrasting scaling behavior is a useful architectural insight (Table 1, Figures 3–4)**: The paper shows SSMs benefit from width while Transformers benefit from depth, demonstrating that parameter-count matching via depth alone misleads parameter-matched comparisons for SSMs. Table 1 (Mamba: 12 layers × 1408 width = 100%; 24 layers × 1024 width = 16%, both ~150M params) cleanly illustrates this.
- **Table 2 ablation is mechanistically tight**: Removing conv1d from 1-layer Mamba drops accuracy from 99% to 2% (matching 1-layer Attention); adding conv to Attention lifts it to 99%. This provides a specific architectural link between the single-layer expressivity gap and one identifiable module.
- **Empirical scope is substantial**: 3,000+ runs, ~20,000 GPU hours, two benchmarks, multiple architectures, and ablations — appropriate for the claims being made.

---

## Weaknesses

### Fatal
None.

### Major

- **Central thesis is overclaimed relative to the paper's own evidence.** The abstract states: *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* Yet the paper's own data shows persistent expressivity differences: Hyena still fails at low widths (Section 4), single-layer Attention cannot solve MQAR regardless of width or LR (Figure 3), and single-layer Mamba without its conv1d degrades to 2% — matching 1-layer Attention (Table 2). These are expressivity differences, not optimization artifacts. The Discussion (Section 8) is actually more accurate: "a crucial differentiator lies not just in their theoretical expressivity, but in their fundamental learnability." The abstract's "mainly" overstates what the data support, and there is a notable tension between the abstract framing and the Discussion framing within the same paper. This mismatch risks misleading readers and weakens the paper's credibility in what is otherwise a sound empirical study.

### Minor

- **The "fundamental mismatch in the loss landscape" interpretation is inferred, not measured.** The paper repeatedly uses "fundamental mismatch in the loss landscape" (Abstract, Introduction) as a characterization of the LR sensitivity finding. However, the paper never directly measures landscape properties: no sharpness or curvature analysis, no gradient norm trajectories across the LR range, no formal characterization of the loss geometry. As written, the paper cannot distinguish between "the SSM loss landscape is intrinsically sharper" and "the SSM's optimal LR happens to be smaller, making it easier to miss with a coarse grid." The language should be qualified or the claim should be supported with at least simple gradient norm measurements.

- **The induction head interpretation in Section 6 is a hypothesis but is partly elevated to a finding.** Section 6 appropriately uses "we hypothesize that during this phase transition, the Attention mechanism *attempts* to form induction heads" and notes this is "based on previous work." However, the introduction's bullet points and abstract discuss the single-layer dynamics as a finding without the same caveat. No attention pattern analysis, timing comparison, or circuit-level evidence is provided to confirm the hypothesis. The observation that a loss bump exists in 1-layer Attention (Figure 6) is real and interesting; the interpretation as attempted-induction-head should remain explicitly labeled as a hypothesis throughout.

- **DeltaNet stability explanation is a hypothesis without supporting evidence.** Section 7 attributes DeltaNet's LR robustness to Householder matrices avoiding vanishing gradients, but this is stated as a conjecture ("We hypothesize this is the main distinction") without any gradient norm analysis or comparison to Mamba/Mamba2 training trajectories. This is a plausible and useful hypothesis, but the discussion should not present it as a confirmed explanation.

### Trivial
None beyond the noted framing tensions.

---

## Nice-to-Haves

- **Loss landscape visualization or gradient norm analysis** during training (e.g., across the LR range) would directly substantiate the "fundamental mismatch in the loss landscape" claim, turning an interpretation into a measured result.
- **Actual attention pattern analysis during the Section 6 loss bump** — comparing attention patterns before/after the bump to canonical induction head patterns in 2-layer models — would cleanly confirm or rule out the induction head hypothesis.
- **Brief scaling to a third setting** (e.g., a character-level LM, or a slightly more naturalistic task) would help assess whether the width-vs-depth scaling principle generalizes beyond MQAR and copying, even if the paper appropriately scopes itself to these benchmarks.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Figure 3 caption discrepancy (Harsh Critic)**: The critic notes that Figure 3's caption may contradict the main text regarding 1-layer Attention performance. Given the paper's text is internally consistent (Section 4 clearly states 1-layer Attention fails regardless of width) and the caption issue is almost certainly a PDF parsing artifact, this is removed.
- **Figure 4 caption framing (Harsh Critic: "constant accuracy with increasing parameters")**: This is a minor and speculative presentation nitpick about how to describe a depth-vs-width effect. Removed as trivial.
- **Overclaiming scope at large scale** (Harsh Critic): The critic suggests the LR sensitivity claim might "vanish at larger scale." The paper explicitly acknowledges this limitation in the Discussion and labels downstream LM validation as future work. The criticism is already addressed.
- **Strength: "addressing an important problem in SSM vs. Transformer comparison"** (Strength Finder, implicit): Generic importance claim, removed per filtering rules. Replaced by specific grounded strengths above.
- **Request for confidence intervals / statistical tests** (implicit in broader reproducibility concerns): Single-run evaluation is standard at this benchmark scale; requiring error bars is not standard in this community for these experiments. Removed as not applicable per community norms.

---

## Novel Insights

The most genuinely novel observation is that optimization instability is a *reproducible confound* that can reverse published claims about SSM expressivity — not merely a vague concern about hyperparameter sensitivity, but a demonstrated phenomenon where SSM performance swings from near-zero to near-perfect purely on the basis of LR selection. The clean Table 2 ablation linking the single-layer expressivity gap to the presence/absence of a 1D convolution is the paper's most mechanistically precise contribution. Together, these findings reframe the SSM–Transformer comparison: the empirical literature has been partially confounded by inadequate hyperparameter search, and future comparisons should treat optimization quality as a methodological requirement, not a secondary concern.

---

## Suggestions

1. **Revise the abstract's central thesis** from "mainly because of their optimization dynamics" to language that matches the paper's Discussion: e.g., "optimization stability is a significantly underweighted factor alongside expressivity" — this is both more accurate and still a strong, publishable claim.
2. **Add at least one gradient-level experiment** (gradient norm over training steps at three LRs: below, inside, and outside the narrow window) to ground the "landscape mismatch" language in direct measurement.
3. **Clearly separate hypothesis from finding in Section 6 and corresponding bullet points** — the induction-head-formation claim should be consistently labeled as a hypothesis in the abstract and introduction.
4. **Flag the depth/width scaling principle explicitly as benchmark-scoped**: one sentence in the Discussion noting that the width-for-SSMs/depth-for-Transformers generalization is established only on MQAR and copying would appropriately calibrate reader expectations.

---

## Score and Decision

**Originality**: The contribution is re-evaluation rather than a new method, but the methodological finding is concrete, reproducible, and non-obvious. Medium-high originality.
**Importance**: The SSM vs. Transformer debate is highly active; a well-documented identification of a systematic confound is directly useful to the community. High importance.
**Claims supported**: Core empirical claims (LR sensitivity, scaling behavior, Table 2 ablation) are well-supported. Abstract-level framing overclaims the central thesis. Mixed.
**Soundness**: Methodology is solid; 3000+ runs, controlled comparisons, careful baselines. One minor issue: inductive interpretations are treated too confidently in framing.
**Clarity**: Generally well-written and well-organized. One tension between abstract framing and Discussion conclusions.
**Community value**: High — directly applicable to anyone training or comparing SSMs.

This is a genuine, useful empirical contribution with a well-executed core finding and one significant framing problem in the abstract. The framing problem is fixable and does not invalidate the contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>