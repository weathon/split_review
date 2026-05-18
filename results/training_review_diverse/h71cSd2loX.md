I have thoroughly read the paper and verified all reviewer claims against the actual content. Let me now synthesize the final review.

---

## Summary

This paper derives two DPO variants — DPO-RK and DPO-D — that replace the Bradley-Terry preference model with the Rao-Kupper and Davidson models, respectively, which explicitly assign probability to tied outcomes alongside wins and losses. Experiments on NMT (WMT21 ZH-EN, IWSLT17 FR-EN) and summarization (TL;DR) show that these variants incorporate tied pairs into training without the task-performance degradation that standard DPO exhibits, while achieving stronger regularization (lower KL to the reference policy) and better-calibrated reward margins on held-out pairs.

## Strengths

- **Clean theoretical derivation from established models**: The paper correctly adapts the Rao-Kupper and Davidson tie-extensions of the Bradley-Terry model into the DPO framework, producing well-specified loss functions (Eqs. 13–14, 17–18). The gradient analysis showing that tie updates drive the reward margin toward zero while win updates increase it is both correct and insightful, providing a mechanistic explanation for the observed regularization effect.

- **Consistent empirical benefits across three tasks and two tie models**: On all three tasks (Figs. 2 and 5), DPO-RK(CP+TP) and DPO-D(CP+TP) achieve task performance (BLEURT, win-rate) similar to DPO(CP) and clearly better than DPO(CP+TP), while operating at lower KL divergence. The fact that both models produce analogous results strengthens the claim that the key insight is modeling ties generally, not tuning to a specific model.

- **Improved classification of ties vs. clear preferences**: Table 1 shows that DPO-RK(CP+TP) with β=0.1 achieves 73.1% overall accuracy (74.5% CP, 71.7% TP) on held-out WMT18 ZH-EN data, while DPO(CP) achieves only 60.1% with severely imbalanced TP accuracy (33.1%). This directly demonstrates that the proposed variants learn to distinguish ties from clear preferences, not merely to ignore ties.

- **Well-behaved reward margin distributions on held-out data**: Table 2 shows DPO-RK(CP+TP) yields mean reward margins near zero on tied pairs (0.0 across all β) with small std (1.8–2.9), while DPO(CP) produces very high variance (std > 60) and bimodal preference probabilities (Fig. 5). This confirms the models generalize appropriately to unseen tied pairs.

## Weaknesses

### Fatal
None.

### Major

- **Gap between motivation (human-annotated ties) and experimental evidence (synthetic ties)**: The paper motivates its work by noting that practical DPO pipelines (Llama 3, Qwen2) produce ties that are discarded, arguing these expensively collected judgments should be used. Yet in all experiments ties are constructed algorithmically: in NMT as the two translations with the smallest BLEURT difference, and in summarization as the pair with the smallest reward margin under a DPO model. These are clean, deterministic proxies that may not replicate the noise, labeler disagreement, or genuine ambiguity of real human tie judgments. The paper does not include any experiment with human-annotated ties, nor does it discuss the limitations of the synthetic construction or argue why results should transfer. The central claim — that these variants "motivate and enable the use of tied pairs in available preference data" — is incompletely supported because the paper never uses the kind of data it motivates from. This is a substantive gap, but it does not invalidate the paper's core methodological contribution (deriving tie-compatible DPO variants and showing they function correctly with ties under controlled conditions).

### Minor

- **No sensitivity analysis for the tie-hyperparameters ν**: The paper sets ν<sub>RK</sub>=3 and ν<sub>D</sub>=1 based on the assumption that "equally-matched items will tie with a probability of 1/2." This assumption is not argued for or justified, and there is no demonstration that performance is robust to these choices. If the method's usefulness depends on calibrating ν per dataset and annotator population, the paper provides no guidance. A sensitivity analysis (e.g., varying ν<sub>RK</sub> from 1.5 to 6 on one dataset) would substantially strengthen the work.

- **No error bars, confidence intervals, or multiple seeds**: The paper does not report any measure of variance for its quantitative results. For methodological claims relying on fine-grained comparisons (e.g., comparing frontiers across methods), it is unclear whether differences are meaningful or within the noise of single runs. While multiple runs of 7B models are expensive, the paper should at minimum acknowledge this limitation.

- **Circularity in summarization tie construction**: In TL;DR, ties are selected as the pairs with minimal reward margin under a DPO model trained on the same data. This means the "tied pairs" may be those easiest for DPO to marginalize, rather than genuinely tied summaries. The paper is transparent about this procedure, and the NMT experiments (2 of 3 tasks) are not subject to this concern, but it weakens the summarization experiment as independent evidence.

### Trivial
None.

## Nice-to-Haves

- A small-scale experiment with human-annotated tie judgments (even on a subset of TL;DR data) would directly address the main gap between motivation and evidence.
- A discussion of how the models behave when ties are mislabeled (noisy tie annotations) would be relevant for real-world deployment.
- A brief note on computational overhead relative to standard DPO would be helpful.

## Removed Points

- **"Claim of no degradation not fully supported without matched-KL comparison"** — The paper already shows full frontier curves (Figs. 2, 5), which is the standard and appropriate way to present this comparison. One can visually assess that DPO-RK/D reach similar peak performance to DPO(CP) at lower KL. The demand for a specific "matched KL" comparison is not a genuine weakness.
- **"Synthetic ties in summarization introduces circularity; this is a weaker experimental design than NMT"** (moved from Major to Minor) — Already addressed in Minor weaknesses above. The paper is transparent about this, and the NMT results independently support the claims.
- **"Paper should discuss robustness to mislabeled ties"** — Scope creep; this is a reasonable future direction but not a weakness of the current paper.
- **"Computational overhead not mentioned"** — Trivial omission.
- Some generic strengths from the Strength Finder (e.g., "this paper addressed an important problem") — dropped as they lack specific content.

## Novel Insights

The paper's gradient analysis revealing that DPO-RK and DPO-D produce sign-flipping update behavior on ties (driving the reward margin toward zero) while DPO continues to push margins apart is worth highlighting: it shows analytically why simply adding tied pairs to DPO fails — the loss function is fundamentally misspecified for ties. The observation that the regularization (lower KL) effect appears even in standard DPO(CP+TP), albeit at the cost of task performance, is also insightful and supported by the theory (Eq. 6 showing the ideal DPO target margin on ties is zero).

## Suggestions

1. **Add a human-tie experiment**: Even a small-scale annotation of the TL;DR or NMT data with a tie option would directly address the gap between framing and evidence, and would significantly strengthen the paper for a high-stakes venue.
2. **Add a sensitivity analysis for ν**: Vary ν<sub>RK</sub> and ν<sub>D</sub> on one dataset (e.g., WMT21) and report task performance and KL. If performance is stable, this is an asset; if sensitive, the paper should acknowledge it and discuss principled ways to set ν.
3. **Acknowledge the single-run limitation**: State whether results are from one run or multiple, and add a brief note about computational constraints.
4. **Discuss the synthetic-tie limitation explicitly**: A paragraph in the experimental section or conclusion addressing how synthetic ties may differ from human ties and why the results are expected to transfer would improve the paper's honesty and completeness.
5. **Add error bars or variance estimates** where feasible, or at minimum report the number of runs performed.

## Score and Decision

This paper makes a clean, well-motivated methodological contribution with consistent empirical support across multiple tasks. The main weaknesses — the synthetic-ties gap and the lack of sensitivity analysis — are significant but not fatal to the core contribution. The paper would be materially improved by addressing the gap between its human-tie framing and synthetic-tie evidence, but the technical results are sound and the derivations are valuable. I recommend acceptance with the expectation that the authors address the synthetic-ties limitation in a discussion or future work section.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>