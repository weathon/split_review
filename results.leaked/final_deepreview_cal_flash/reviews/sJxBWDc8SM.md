Now let me write the final consolidated review.

## Summary

This paper presents an extensive empirical study (3,000+ runs, ~20,000 GPU hours) comparing Transformer and modern recurrent model (Mamba, Hyena) learning dynamics on multi-query associative recall (MQAR) and copying tasks. The central finding is that SSMs' performance is confined to an extremely narrow window of learning rates, while Transformers are robust across a wide range — a critical optimization instability that confounds prior expressivity comparisons. The paper also identifies contrasting scaling strategies (SSMs benefit from width, Transformers from depth), shows that 1-layer Mamba can solve MQAR while 1-layer Transformers cannot (attributing the latter to a failure of induction head formation), and traces 1-layer Mamba's expressivity to its convolutional component. Newer architectures like DeltaNet are shown to mitigate the optimization brittleness.

## Strengths

1. **Optimization instability as a confounder in prior work (Figure 1 §3)**: The paper convincingly demonstrates through extensive learning-rate grid searches that Mamba and Hyena achieve high MQAR accuracy only within a narrow LR window, while Attention maintains robustness across orders of magnitude. Critically, the LRs used in prior work (Arora et al., 2023) fall outside these windows, directly showing that prior negative results may have been confounded by suboptimal tuning rather than fundamental incapacity. This is a clean, impactful finding.

2. **Contrasting width-vs-depth scaling strategies (§4, Figure 4, Table 1)**: The paper shows that SSMs scale primarily with width (hidden dimension), while Transformers scale with depth. This is not merely parametric — a deeper-but-narrower Mamba with the same parameter count as a wider one fails on the copy task while the wider one succeeds (Table 1). This corrects a common methodological error of matching parameters without accounting for architectural scaling preferences.

3. **Mechanistic role of convolution identified through clean ablations (§7, Table 2)**: Removing the 1D convolution from 1-layer Mamba drops accuracy to 2% (matching 1-layer Transformer failure), while adding a convolution to 1-layer Transformer boosts accuracy to 99%. This provides a concrete architectural mechanism linking SSM and Transformer expressivity in the shallow regime.

4. **Induction-head-like dynamics in single-layer Transformers (§6, Figure 6)**: The paper observes that 1-layer Transformers exhibit a loss bump resembling induction head formation (previously only seen in multi-layer models), yet this fails to translate into accuracy gains. This provides new insight into the role of depth in making induction heads functional.

5. **DeltaNet shown to overcome LR instability (§7, Figure 7)**: Evaluating newer architectures, DeltaNet maintains high accuracy across a wide LR range unlike Mamba and Mamba2, providing evidence that the identified optimization brittleness can be addressed architecturally and pointing to a concrete path forward.

6. **Scale and rigor of empirical work**: The paper reports over 3,000 runs, establishing robust statistical support for its claims about learning rate sensitivity and scaling behavior.

## Weaknesses

### Fatal

None.

### Major

- **Central thesis overreach (Abstract, §1)**: The paper's stated central thesis — *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics"* — overstates the evidence. The paper's own results show that 1-layer Transformers **cannot** solve MQAR while 1-layer Mamba **can**, which is an expressivity difference. The paper's actual contribution is better and more defensibly framed as: *optimization stability is a larger differentiator than previously appreciated, and when both architectures have sufficient capacity (e.g., 2-layer), the remaining gap is primarily about learnability, not expressivity.* The current framing makes the paper vulnerable to the very criticism it levels at prior work — overclaiming based on incomplete analysis. This should be corrected; the paper's findings are strong enough to stand on their own without the overstated binary claim.

### Minor

- **Lack of clarity on Figure 6's experimental configuration (§6)**: The paper does not specify what sequence length or KV-pair count Figure 6 uses, making it difficult to reconcile with Figures 3 and 4. Figure 3 shows 1-layer Mamba failing across multiple configurations (seq len 64–512), while Figure 4 specifically shows failure at seq len 256 / KV pairs 64. Figure 6 then shows 1-layer Mamba (width 64) succeeding — but without stating the task configuration. If Figure 6 uses a different (easier) configuration than Figures 3–4, this should be transparently stated. The harsh critic's claim of a "fatal contradiction" is unfounded (it relies on assuming identical configurations without evidence), but the paper should remove this ambiguity.

- **Mild internal inconsistency on Mamba's dynamics (§6)**: The Figure 6 caption describes Mamba's learning dynamics as "smooth," but the text claims "a significant loss bump" for Mamba. While these could both be true in different senses, the paper should clarify what it means — a loss bump is not typically described as smooth.

- **Copy task validation is thin (§5)**: The copy task results rest on only one LR-sensitivity plot (Figure 5) and one scaling table (Table 1). Given that the paper makes claims about cross-task generality, this section reads as a sketch rather than a thorough validation.

### Trivial

- None beyond the clarity issues already noted.

## Nice-to-Haves

- A diagnostic analysis of gradient norms or state-transition matrix properties during training would strengthen the claimed link to vanishing gradients in SSMs, but this goes beyond the paper's stated scope.
- The central thesis would be better served by a more nuanced framing emphasizing the *interaction* of expressivity and learnability rather than a binary distinction.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Harsh Critic's "fatal contradiction" between Figure 4 and Figure 6**: This point is removed because it assumes without evidence that Figure 6 uses the same (seq len 256, KV pairs 64) configuration as Figure 4. The paper does not state Figure 6's configuration, so there is no verified contradiction — only a clarity gap, which is kept as a Minor weakness above.

2. **Missing diagnostic analysis of why the LR window is narrow (gradient norms, etc.)**: Removed as scope creep — the paper provides a plausible mechanism (product of matrices, citing Trockman et al.) and the requested analysis goes beyond what the paper claims to deliver.

3. **Reproducibility nitpicks (undisclosed hyperparameters, etc.)**: Removed per hard rules — the paper states all experimental details are in Appendix A.2 (which was stripped by the parser).

4. **Missing related works**: Removed per hard rules — I cannot independently verify the existence of missing references.

## Novel Insights

The most novel insight from the reviewer inputs is that the harsh critic's "fatal contradiction" between Figure 4 and Figure 6 reveals a deeper tension in the paper: the paper simultaneously wants to claim (a) that 1-layer SSMs can solve MQAR (to show they are expressive), and (b) that SSMs scale better with width (to argue optimization instability is the key differentiator). But the existence of configurations where 1-layer SSMs *cannot* solve MQAR (like Figure 4's seq len 256 / KV pairs 64) does not contradict the paper's thesis — it merely shows that the difficulty is configuration-dependent. The paper would benefit from explicitly acknowledging this configuration-dependence and framing its claims around *when* each architecture can or cannot solve the task.

## Suggestions

1. Reframe the central thesis to acknowledge expressivity differences (e.g., 1-layer Transformers truly cannot solve MQAR) and position the optimization instability finding as an *additional* critical factor that prior work overlooked, not as a replacement for expressivity.
2. Explicitly state the experimental configuration (sequence length, KV pairs) used in Figure 6's dynamics analysis, and discuss how it relates to the configurations in Figures 3 and 4.
3. Clarify whether the "significant loss bump" claimed for Mamba in the Section 6 text is visible in a different run or configuration than what Figure 6 displays, or reconcile the description with the figure caption.
4. Strengthen the copy task section with additional experiments or analysis, or soften the claims of cross-task generality.

## Score and Decision

**Calibration.** I retrieved 14 anchors across two rounds. Round 1 bracketed the paper between weak anchors (avg ~2.5–3.0 on tangential topics) and strong anchors (avg ~7.6–8.0 on theoretical/architectural papers). The most topically relevant anchors were in the middle band (4.5–6.25). Round 2 refined within 4.5–7.0.

Anchors used for comparison:
- QFgbJOYJSE (5.75, Accept): Theoretical SSM-Transformer comparison. Our paper is more empirically grounded and has more actionable insights. → Our paper is moderately stronger.
- iVy7aRMb0K (4.50, Reject): Initialization to improve SSM recall. Our paper identifies a more fundamental problem (optimization stability) and provides broader analysis. → Our paper is clearly stronger.
- pymXpl4qvi (6.00, Accept): Identifies recency bias and over-smoothing in SSMs. Our paper has comparable rigor but covers more dimensions (LR sensitivity, scaling, ablations, newer architectures). → Comparable, perhaps slightly broader.
- zfeso8ceqr (6.00, Accept): Empirical optimizer comparison for LLMs. Similar empirical methodology and scale. Our paper has more surprising findings. → Comparable.
- LgzRo1RpLS (6.25, Accept): Mamba long-context extension. Different contribution type; our paper's findings are more fundamental.
- WYL4eFLcxG (6.00, Accept): LR scaling laws. Different focus; similar methodological rigor.
- TBJCtWTvXJ (6.20, Reject): Optimizer analysis. Lower relevance.

**Round 1 bracket:** 4.5–7.5. **Round 2 narrowing:** comparison to 4.5–6.25 anchors confirms the paper sits in the 5.5–6.5 range. The paper's empirical contributions are genuinely valuable and address an important gap in the literature, but the central overreach and clarity issues prevent it from being a strong accept.

**Final score: 6.0 — Accept.** The paper presents convincing evidence that optimization stability is a critical confounder in SSM-vs-Transformer comparisons, identifies practically important scaling behaviors, and provides clean mechanistic ablations. The weaknesses are addressable: the central framing needs recalibration (not "not expressive power" but "optimization matters more than previously thought") and the experimental configurations need better documentation. I expect these to be fixable in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>