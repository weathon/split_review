Here is the consolidated review.

## Summary

This paper investigates knowledge distillation (KD) for multi-label visual recognition tasks. The core contribution is Tempered Logit Distillation (TLD), which applies temperature scaling to the sigmoid activation function (yielding a "tempered sigmoid") rather than the standard softmax. The authors show empirically that (1) vanilla sigmoid is not inherently superior to tempered softmax for multi-label KD (contradicting recent claims), (2) both have intrinsic limitations, and (3) setting τ < 1 in tempered sigmoid creates a hardness-aware gradient that concentrates distillation on informative samples. Extensive experiments on COCO, PASCAL-VOC, and NUS-WIDE across classification, detection, and segmentation demonstrate consistent gains over prior logit-based and feature-based distillation methods.

## Strengths

1. **Controlled motivation experiment (Table 1) clearly refutes prior claims.** The paper isolates the effect of activation functions by removing confounding factors (advanced distance functions, re-weighting) and shows vanilla sigmoid does not outperform tempered softmax under matched conditions. This directly contradicts the central premise of L2D and BCKD and provides compelling motivation for the proposed method.

2. **Principled theoretical analysis of hardness-aware gradient (Eq. 8).** The derivation that ∂ℒ_TLD/∂z_i^s = τ(𝐩̃_{i,τ}^s − 𝐩̃_{i,τ}^t) is clean and correct. The analysis showing that τ < 1 drives teacher predictions toward ground-truth [1,0], amplifying gradients on hard samples, while τ ≥ 1 spreads loss uniformly, is both insightful and well-supported.

3. **Consistent SOTA performance across three tasks and three datasets.** Tables 2–9 show TLD outperforms vanilla KL and BCE by clear margins (e.g., +1.5–1.7 mAP in detection, Tables 2–4 in classification). TLD with logit-only distillation even exceeds or competes with sophisticated feature-based methods (CWD, RM, MGD, PKD) designed specifically for each task.

4. **Opposite optimal τ regime compared to softmax, with visual validation.** Table 10 demonstrates the striking reversal: TLD peaks at τ < 1 (optimal ~0.5) while KL peaks at τ > 1 (optimal ~4–10). Figure 4 directly visualizes that TLD with τ < 1 concentrates loss on semantic foreground regions (person's hand, surfboard edge), while KL with τ < 1 penalizes background. This is a novel empirical finding specific to multi-label distillation.

5. **Compatibility with feature-based distillation and self-KD.** Tables 2, 8, and 9 show TLD can be combined with FitNet, MGD, PKD for additional gains. Table 11 shows TLD works in self-KD (same architecture) with +2.54% mAP in classification and +1.1% in detection, demonstrating robustness.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Table 1 does not report the τ values used for tempered softmax and tempered sigmoid rows.** The entire motivation hinges on this comparison, yet the caption and surrounding text omit the τ settings. The ablation in Table 10 later shows that optimal τ differs dramatically for KL (τ ∈ {2,4,10}) and TLD (τ ∈ [0.25,1)). Without knowing which τ values were used in Table 1, the reader cannot verify that the comparison was fair. The paper should explicitly state (e.g., "KL used τ=10, TLD used τ=0.5") and confirm these are reasonable choices (consistent with their own ablation and prior work).

2. **No variance or multi-run statistics.** All results appear to be single runs. For comparisons where margins are narrower (e.g., Table 7 vs. CWD/RM), variance information would substantially strengthen the evidence. Given that single-run evaluation is common in large-scale CV benchmarks, this is a minor concern for the main results (which have comfortable margins), but reporting 3-run mean ± std for at least the key comparisons would improve reproducibility.

3. **"Overstrict presumption" is referenced but not explained.** The paper states (line 18) that BCKD "based on an overstrict presumption, argued that the tempered softmax leads to loss vanishing" but does not clarify what this presumption is. While the reader can consult the BCKD paper, a brief explanation would make the narrative self-contained.

### Trivial
- The incomplete sentence "Due to the page limitation, we attach all the experimental settings, e.g." (line 152) is a formatting artifact from PDF extraction; the original submission presumably contains the full text. This does not affect the review.

## Nice-to-Haves

- A brief analysis of why the "better teacher, better student" pattern (Table 5) might differ from the "better teacher, worse student" phenomenon in single-label KD, tested across other distillation methods for context.
- An ablation on the balancing factor λ (Eq. 7) for at least one setting to confirm stability.
- A brief note on training overhead (TLD adds no parameters but changes the activation; a runtime comparison would be useful for practitioners).

## Removed Points

**Harsh Critic's "missing experimental settings in main paper"** — Removed because the sentence "Due to the page limitation, we attach all the experimental settings, e.g." is clearly truncated by the PDF parser. The hard rule states that missing appendix content is a parser artifact, not an author error, and must be removed from consideration.

**Harsh Critic's "extreme small τ degrading performance not empirically demonstrated"** — Removed because this point is a theoretical note (line 133) in the gradient analysis section. It is a natural prediction from the theory that would not change the paper's core claims; the ablation in Table 10 implicitly covers this by including τ=0.25 which still performs well.

**Harsh Critic's "better teacher better student not tested for other methods"** — Removed because the paper presents this as an observation about TLD, not as a comparative claim. Criticizing the absence of a broader comparative study that would be tangential to the paper's focus is scope creep.

**Strength Finder's generic/superficial strengths** — None found; all claimed strengths are specific, evidenced, and concrete.

## Novel Insights

The reviewers converge without manufacturing a novel insight beyond what the paper itself provides. None beyond the paper's own contributions.

## Suggestions

1. **Add the τ values to Table 1's caption or a footnote.** State the τ used for each row and justify the choices (e.g., "KL uses τ=10 following standard practice; TLD uses τ=0.5 based on our ablation in Table 10"). This is the single most actionable fix.
2. **Add 3-run mean ± std for the main results** (at least Tables 2 and 6) to address the variance concern.
3. **Briefly explain what BCKD's "overstrict presumption" is** in a single sentence to improve readability.

## Score and Decision

This paper makes a clear, well-supported contribution with a simple but insightful modification — temperature-scaled sigmoid — and validates it extensively across three tasks and datasets. The weaknesses are minor and easily addressable. The work is novel (the opposite τ regime for sigmoid vs. softmax in multi-label KD is a genuine finding), well-executed experimentally, and practically useful.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>