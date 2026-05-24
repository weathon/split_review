Now I have enough context. Let me compose the final review.

## Summary

This paper proposes PiCO, an unsupervised peer-review framework for ranking LLMs. Multiple LLMs answer unlabeled questions and evaluate each other's responses, with each model assigned a learnable confidence weight \(w\). A consistency optimization maximizes the correlation between \(w\) and a weighted response score \(G\), producing a ranking the authors claim aligns with human preferences. Experiments on Chatbot Arena, MT-Bench, and AlpacaEval with 15 LLMs show rank-correlation improvements over baselines including PRD, PRE, and Claude-3 API.

## Strengths

- **Novel unsupervised evaluation direction with peer-review framing.** The idea of having LLMs evaluate each other without any human feedback and using a learnable confidence weight is genuinely novel. The paper correctly identifies a practical need — human evaluation is slow and costly, and existing LLM-as-a-judge approaches require expensive models or human annotations.

- **Strong empirical results across diverse datasets and metrics.** Table 2 shows PiCO consistently achieves the highest Spearman's \(S\) and Kendall's \(\tau\) and lowest Permutation Entropy across all three datasets (Chatbot Arena, MT-Bench, AlpacaEval). On Chatbot Arena, PiCO achieves \(S=0.90\) and \(\tau=0.77\) at full data volume, matching or surpassing Claude-3 API while being fully unsupervised. Gains are consistent across data volumes (1.0, 0.7, 0.4).

- **Practical advantage over supervised methods demonstrated.** Table 3 shows PiCO achieves 100% Precision@8 and 83.2% RBP@8 on Chatbot Arena with **zero** human annotation cost, vs. PRE which requires ~7k annotations for 87.5% Precision@8 and 78.0% RBP@8. This concretely validates the practical motivation.

- **Controlled toy experiment validates the consistency assumption.** Table 1 shows that forward-weighting (higher weights to stronger models) improves rank correlation, and PiCO's consistency optimization further improves over random initial weights (e.g., on MT-Bench: from 0.74 Uniform to 0.90 after optimization). This directly supports the core premise.

- **Learned weights reduce evaluation bias.** Figure 3 shows that re-weighting with learned confidence weights substantially reduces preference gap (PG) values — the heatmaps shift from showing strong positive PG (bias) toward values near zero — supporting the claim that the optimization mitigates self-favoring biases in weaker models.

## Weaknesses

### Fatal
None.

### Major

- **The optimization algorithm for solving Eq. (8) is not specified.** The paper states the objective — maximize Pearson correlation between \(w\) and \(G\) — but never describes how this optimization is actually performed. The text says "we randomly initialize the ability weights and employ our consistency optimization to adjust the weight" but provides no update rule, gradient computation, closed-form solution, or iterative scheme. Since \(G\) is a linear function of \(w\), the problem is well-defined, but the paper does not state which algorithm solves it (gradient ascent? alternating minimization? eigenvector computation?). This is not a minor omission — it makes the method non-reproducible from the paper alone and prevents assessment of whether the optimization is sound. The existence of a code release partially mitigates this, but a paper should stand on its own description.

- **The "loss" plotted in Figures 5 and 6 is never defined.** Figure 5 shows "average training loss" for different numbers of eliminated reviewers, and Figure 6b shows a "Loss" curve over training epochs. The paper never states what this loss function is. The only objective mentioned in Section 2.2 is maximizing Pearson correlation (Eq. 8). If the loss is simply negative Pearson correlation (or a related transformation), this should be stated explicitly. Without this definition, the "automatic learning" of the elimination threshold at 60% and the "stability validation" cannot be properly evaluated.

### Minor

- **The "automatically learned" elimination threshold claim is weakly supported.** Section 3.3 states that 60% elimination is "learned automatically" because the loss curve reaches a minimum at 9 out of 15 models across all three datasets. This is a post-hoc observation, not a principled learning process — the procedure is: try all thresholds, pick the one where loss is lowest. Whether the 60% point generalizes beyond this specific set of 15 models is unknown, and the claim of "automatic learning" overstates what is actually happening (threshold selection via grid search on the training loss).

- **The preference gap analysis shows bias reduction but does not prove human alignment.** Figure 3 demonstrates that re-weighting with learned confidence weights reduces the preference gap. This is a necessary condition for alignment (reducing self-serving bias is good) but not sufficient — a system could have low bias among models while still being misaligned with human preferences. The real evidence for human alignment comes from Tables 2-4, which directly measure rank correlation with human preferences.

### Trivial
None.

## Nice-to-Haves

- Including pseudocode or a concise algorithm summary would significantly improve clarity.
- An ablation separating the contribution of consistency optimization vs. the elimination mechanism would help understand which component drives the gains.
- Statistical hypothesis testing (e.g., whether PiCO's gains over the runner-up are significant) would strengthen the empirical claims, though the consistent trends across metrics partially address this.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The optimization is circular / self-referential."** (from harsh critic): The objective max Correlation(w, G(w)) where G = M·w is a standard, well-defined optimization problem (finding w that maximizes correlation between w and a linear transformation of w). This is not circular in any pathological sense. The real issue is that the solving algorithm is not specified, not that the objective is self-referential. **Removed — factually overstated.**

- **"Missing related works."** (from harsh critic, implied): The paper adequately covers related work in evaluation benchmarks, human evaluation, and LLM-as-a-judge. **Removed per instruction that missing related works should not be mentioned.**

- **"The results could be artifacts of an ad-hoc procedure."** (harsh critic): Speculative without evidence. The experiments show consistent, reproducible results across datasets, metrics, and data volumes. **Removed — speculation not grounded in paper content.**

- **"Generic strengths" from Strength Finder:** Removed strengths that are generic (e.g., "this paper addressed an important problem"). The retained strengths are specific to the paper's actual evidence.

- **"Circularity concern: w is used both in the score computation and as the quantity being optimized."** (harsh critic): As noted above, this is not circular — G is a function of w (G = M·w), and maximizing correlation(w, M·w) is a specific optimization problem. Whether the solution aligns with human ranking is an empirical question, which the experiments address. The problem is the missing algorithm, not circularity. **Removed — factually mischaracterized.**

- **"The optimizations could exploit consistent bias in the evaluation set."** (harsh critic): This is a general concern that applies to any peer-review system, but the paper's PG analysis (Figure 3) directly shows that the learned weights reduce bias, partially rebutting this concern. The critic provides no evidence that this actually happens. **Removed — speculative, and partially addressed by the paper.**

- **"The paper over-promises by claiming the method re-ranks LLMs to be closer to human rankings without explaining how."** (harsh critic): The paper does explain the mechanism — consistency optimization — even if the algorithmic details are underspecified. Emphasizing the missing algorithm is fair; calling it an over-promise is editorializing. **Removed — merged into the stronger "optimization not specified" point.**

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate the paper's claims without adding new analysis beyond flagging the underspecified optimization, which is independently verifiable from the paper.

## Suggestions

1. **Specify the optimization algorithm explicitly.** Provide the update rule (e.g., gradient-based, or a closed-form solution). Even one paragraph describing how Eq. (8) is solved would transform this from a critical gap to a minor omission.
2. **Define the loss function** used in Figures 5 and 6. If it's negative Pearson correlation (or 1 − Pearson), state this. If it's something else, define it formally.
3. **Reframe the elimination threshold selection** as a heuristic rather than "automatic learning." The post-hoc selection of the minimum-loss threshold is a reasonable design choice but should not be described as learning.
4. **Add an ablation** comparing PiCO with and without elimination, and with and without consistency optimization, to isolate the contribution of each component.

## Score and Decision

### Calibration Summary

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| On Unsupervised Prompt Learning | xRi8sKo4XI.md | 3.00 | R1 (low) | Narrower scope, different problem; PiCO is stronger |
| AIME | Z6kVjQAPNq.md | 3.50 | R2 | Both have methodology gaps, but PiCO has broader experiments and clearer idea |
| LLMs are Effective Text Rankers (PRP) | iwd9sQWnXb.md | 4.50 | R1/R2 | Comparable quality — both have novelty but clarity/reproducibility concerns |
| GED (Preference Graph Ensemble) | rTM95kwzXM.md | 5.25 | R1 (mid) | GED's method is clearly specified with theoretical guarantees; PiCO is weaker on this dimension |
| Unsupervised In-Context Learners | ohJxgRLlLt.md | 5.75 | R2 | Accepted paper with clear methodology; PiCO is weaker methodologically |

**Round 1 bracket:** Between ~3.0 and ~5.75 (narrowing to 3.5–5.5).

**Round 2 narrowing:** PiCO is clearly stronger than AIME (3.5) which had proof errors and limited scope, and is comparable to PRP (4.5) which had similar reproducibility concerns. It is weaker than GED (5.25) which provides a clearly specified algorithm and theoretical analysis. PiCO's underspecified optimization is a genuine gap that GED and the Unsupervised ICL paper do not share.

**Final positioning:** PiCO is most comparable to PRP (4.5) — both have interesting ideas and strong experiments but suffer from methodological clarity issues and reproducibility concerns. PiCO's idea is more novel than PRP's, but the missing algorithmic details are more consequential. The paper sits slightly below the acceptance threshold.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>