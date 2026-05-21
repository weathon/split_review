## Summary

This paper integrates hardcoded n-gram induction heads (borrowed from Akyürek et al.) into transformers for in-context reinforcement learning. The authors adapt Algorithm Distillation by inserting n-gram attention layers that explicitly compute n-gram statistics from the input sequence, rather than relying on the model to learn them. They evaluate on Dark Room, Key-to-Door, and Miniworld (pixel-based) environments, reporting improvements in hyperparameter sensitivity and data efficiency.

---

## Strengths

1. **Well-motivated architecture modification.** The connection between induction heads (Olsson et al.), higher-order n-gram emergence (Akyürek et al.), and simplicity bias in ICRL (Edelman et al.) is clearly drawn. The paper identifies a concrete problem — the difficulty of learning higher-order induction heads during ICRL training — and proposes a targeted architectural solution. This is a sensible and clearly motivated intervention.

2. **Convincing hyperparameter sensitivity results on discrete environments.** Figure 2 shows that the n-gram model finds optimal hyperparameters in ~20 random assignments on Dark Room with 1K histories, versus >400 for the baseline. The gap is large, the trend is consistent across multiple data conditions, and the EMP protocol avoids cherry-picking. This is the strongest evidence in the paper and directly supports the claim that n-gram heads reduce training instability.

3. **Thorough ablations on n-gram parameters and negative control.** Sections 4.4–4.5 are well-executed. Table 1(a,b) shows that varying n-gram length (1–3) and layer insertion position causes only small EMP differences (±0.05), and Table 1(c) shows a permuted (broken) n-gram mask performs identically to the baseline. These experiments convincingly demonstrate that the additional hyperparameters do not complicate tuning and that a flawed n-gram does not hurt performance.

---

## Weaknesses

### Fatal

None.

### Major

1. **The VQ encoder confound prevents isolating the n-gram mechanism in pixel-based environments.** In the Miniworld experiments (Figures 5–6, Section 4.3), the n-gram method uses a separately-pretrained Vector Quantization (VQ) model to convert each image into a discrete 4×4 codebook index matrix, which is then used for n-gram matching (Section 2.3). The baseline (Algorithm Distillation without n-gram heads) presumably processes raw RGB images via a standard CNN encoder — the paper never states that the baseline also receives the VQ-quantized representation or that its encoder is matched. If the baseline sees raw pixels while the n-gram method sees pre-quantized discrete tokens, then any performance difference could be due to the VQ representation rather than the n-gram attention pattern itself. This is a structural confound: the comparison on pixel-based environments cannot isolate the claimed mechanism. The claim that n-gram heads "can be used in environments with visual observations" (line 50) is the paper's third contribution and requires a clean comparison to support it.

2. **The "27× less data" claim is not properly supported.** The paper claims (lines 48, 132, 182) that the n-gram method reduces data requirements by a factor of 27× compared to Algorithm Distillation. The evidence mixes an internal comparison (n-gram vs. baseline on 100 goals) with an external reference (the original AD paper's result at 2048 goals). Specifically: (a) the paper's own baseline on 100 goals plateaus, so the internal comparison only shows that n-gram outperforms baseline at the same data quantity — this is consistent with the HP sensitivity results but does not establish a specific data-reduction factor; (b) the 27× factor extrapolates by citing Laskin et al.'s reported requirement of 2048 goals (2048/100 ≈ 20.5, not 27) without running their own baseline at that scale within the same evaluation framework; (c) the arithmetic is explained only in the stripped appendix (Appendix B), so the reader cannot verify whether the factor accounts for differences in histories per goal, total transitions, or other meta-parameters. The paper would be strengthened by directly comparing both methods at multiple controlled data scales (as in Figure 1) and reporting the factor from their own data.

### Minor

1. **Limited scope of evaluation.** The experiments are confined to simple grid-world environments (Dark Room, Key-to-Door) and one 3D environment (Miniworld). The paper acknowledges this as a limitation (Section 6), but the narrow scope means the contribution is more of a proof-of-concept than a broadly validated method. Generalizing to more complex domains (continuous control, richer visual environments) would significantly increase impact.

2. **Missing architecture and data statistics details.** The paper does not report basic architectural parameters (number of transformer layers, attention heads, embedding dimension, optimizer, learning rate schedule) or data statistics (total number of transitions in the training set, number of histories per goal, average trajectory length). These details are needed to assess reproducibility and to properly evaluate the data efficiency claims. While some of this may be in the stripped appendix (Appendix C), the main text should provide enough information for a reader to understand the experimental setup.

### Trivial

None.

---

## Nice-to-Haves

- A controlled experiment in pixel-based environments where the baseline *also* receives VQ-derived tokens (but without n-gram attention) would cleanly isolate the effect of the n-gram pattern from the VQ representation.
- Running the baseline at 2048 goals in the same evaluation framework (rather than citing an external paper) would make the 27× claim self-contained.
- Reporting error bars on the EMP curves in Figures 2 and 4 (as is done in Figure 6) would help assess the variance across HP search runs.
- A brief analysis of failure cases (e.g., why does the method still fail with only 10 goals in Dark Room?) would clarify the boundaries of the improvement.

---

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the reasons given:

- **"Evaluation protocol conflates hyperparameter search speed with data efficiency"** — The paper has separate sections for HP sensitivity (Section 4.1) and data efficiency (Section 4.2), and Figure 1 provides a direct comparison of return vs. number of training goals without the HP search confound. In Section 4.2, the EMP metric is used with both methods evaluated at the same low-data condition (100 goals), so the comparison is valid for showing that n-gram outperforms baseline under limited data. The criticism overstates the issue.

- **Missing related works** — Removed per instruction (no external sources to verify).

- **Formatting/style nitpicks** — Removed per instruction (parser artifacts, not author errors).

- **"The paper does not analyze failure cases"** — This is a reasonable suggestion but is better placed in Nice-to-Haves than as a weakness.

- **Strength Finder's claimed strength about "27× data reduction"** — Removed because it conflicts with the verified weakness about the claim being unsupported.

- **"No error bars on the main EMP curves"** — EMP is by construction an expectation over HP search runs; error bars on EMP would require multiple independent HP searches, which is uncommon.

---

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviews did not surface an observation about the paper that the authors themselves do not already articulate.

---

## Suggestions

1. **Fix the pixel-based confound.** Either (a) run the baseline with the same VQ encoder (but without n-gram attention), or (b) explicitly state that both models receive the same input representation and clarify what that representation is.
2. **Replace the 27× claim with controlled internal evidence.** Train both methods at multiple data quantities (64, 128, 256, 512, 1024, 2048 goals) and report the data reduction factor from within the paper's own experimental framework. This eliminates reliance on an external reference and makes the claim verifiable.
3. **Report basic architecture and data statistics in the main text** (number of layers, heads, embedding dimension, total transitions, histories per goal).

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing, 3 queries):**
- Weak anchors (< 3.5): "Demonstration Distillation for Efficient In-Context Learning" (avg 3.40), "Towards Autonomous Agents" (avg 2.50), "Language Decision Transformers" (avg 3.00), "ADAPTER-RL" (avg 3.00). These papers had fundamental flaws (unsupported claims, lack of clarity) and were all rejected.
- Middle anchors (3.5–7.5): "LLMs Are In-Context Reinforcement Learners" (avg 3.75, withdrawn), "In-context learning and Occam's razor" (avg 5.60, rejected), "How does representation impact in-context learning" (avg 4.50, rejected), "In-Context Learning for Games" (avg 4.50, rejected).
- Strong anchors (> 7.5): "Mechanistic basis of data dependence and abrupt learning" (avg 9.00, oral), "When can transformers reason with abstract symbols?" (avg 7.60, poster), "Retrieval Head Mechanistically Explains Long-Context Factuality" (avg 8.00, oral). These papers had rigorous theoretical or empirical contributions and were accepted.

**Initial bracket: between 3.5 and 7.5.** The paper has a valid idea and clean ablations, placing it above the weakest band, but the evaluation confounds prevent it from reaching the strong band.

**Round 2 (Narrowing within the bracket):**
- Middle-low anchors (3.5–5.5): "LLMs Are ICRL" (avg 3.75), "RA-DT" (avg 4.67, rejected with scores 1,5,8), "In-Context Learning for Games" (avg 4.50, rejected), "How does representation impact ICL" (avg 4.50, rejected).
- Middle-high anchors (5.5–7.5): "nGPT" (avg 6.50, accepted poster), "Stack Attention" (avg 6.67, accepted spotlight), "Few Heads are Enough" (avg 5.67, rejected), "MoH" (avg 5.75, rejected).

**Narrowing judgment:** The n-gram ICRL paper is weaker than the middle-high anchors (nGPT, Stack Attention) which were accepted at top venues with stronger empirical validation. It is comparable to the middle-low anchors. Compared to RA-DT (avg 4.67), this paper has better ablation studies but suffers from a more central confound (the VQ issue undermines one of its three claimed contributions). Compared to "In-Context Learning for Games" (avg 4.50), both papers present interesting ideas with evaluation gaps. I place this paper slightly below RA-DT due to the VQ confound affecting a core contribution claim.

**Final score: 4.5**

The paper proposes a sensible architectural modification and provides convincing evidence for improved hyperparameter sensitivity in discrete environments. However, the pixel-based evaluation has a confound (VQ encoder not controlled for across methods), and the headline 27× data efficiency claim relies on an external comparison rather than a controlled internal experiment. These issues prevent the paper from being accepted in its current form but are fixable within a revision cycle.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>