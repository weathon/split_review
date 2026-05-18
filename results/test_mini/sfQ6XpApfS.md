Now I have all the information needed. Let me synthesize the review.

## Summary

This paper proposes PiCO, an unsupervised framework for evaluating LLMs via a peer-review mechanism. LLMs answer unlabeled questions and evaluate each other's responses anonymously. Each LLM is assigned a learnable capability weight \( w \), and a response score \( G \) is computed as the weighted sum of evaluations. The framework maximizes the Pearson correlation between \( w \) and \( G \) under the *consistency assumption* that high-capability models are both better evaluators and deserve higher scores. A reviewer elimination mechanism removes low-score models iteratively. Three ranking-alignment metrics (PEN, CIN, LIS) are proposed and evaluated on Chatbot Arena, MT-Bench, and AlpacaEval.

## Strengths

- **Fully unsupervised evaluation pipeline.** The entire process — from collecting unlabeled questions, having LLMs answer and evaluate each other anonymously, to learning confidence weights — operates without any human feedback. This contrasts with supervised approaches like PRE (which requires a qualification exam with human annotations) and is a genuinely different setting from prior work [Abstract; Section 3.2; Eq. 4–5].

- **Consistency optimization produces meaningfully better rankings.** PiCO achieves the best PEN, CIN, and LIS scores across nearly all dataset/data-volume settings in Table 1. For example, on Chatbot Arena (data volume 1.0), PiCO achieves PEN 0.94±0.02 vs. the runner-up PRE at 1.07±0.01 — well-separated means. The learned weights also visibly reduce evaluation bias in the preference-gap heatmaps (Figure 4), showing that the optimization is doing more than random re-weighting. The results are consistent across 15 LLMs and three datasets.

- **The unsupervised elimination mechanism outperforms a supervised counterpart.** Figure 5 shows PiCO achieves lower CIN (better ranking) than PRE's supervised elimination (which requires human-annotated qualification exams) across most elimination counts on all three datasets. This is a concrete empirical result: unsupervised elimination can be not just cheaper but more effective.

- **Ablation study provides empirical support for the core assumption.** Forward Weight Voting (higher weights to stronger models) outperforms Uniform and Backward Weight Voting on PEN and CIN across all datasets (Table "upper"), validating the intuition that better evaluators should receive higher weights. Applying consistency optimization on random initial weights improves results further, showing the optimization extracts additional signal beyond the ordinal ordering.

## Weaknesses

### Fatal
None.

### Major

- **The optimization problem is underspecified and lacks any analysis.** The paper states "argmax_w Consistency(G,w)" using Pearson correlation (Eq. G), but provides no description of how this argmax is computed (gradient descent? closed-form? how many iterations?), no convergence analysis, no discussion of fixed points or uniqueness, and no regularization. Because \( G = A \cdot w \) (each G_j is a linear combination of w components), the objective is maximize PearsonCorr(w, A·w). While this is a well-defined optimization (not "ill-posed" as the critic claims — it's continuous on a compact domain), the paper treats it as a black box. Without understanding the optimization landscape or at least showing the learned w explicitly (e.g., a table of final weights per model), readers cannot assess whether the learned weights are meaningful or merely artifacts of a poorly-understood optimization. This is the paper's most significant methodological gap.

- **No standard rank correlation metrics reported.** The paper introduces PEN, CIN, and LIS but never reports Kendall's τ, Spearman's ρ, or any normalized rank correlation that would allow direct comparison with prior work and give readers an intuitive sense of effect size. CIN is essentially the raw inversion count (related to Kendall τ by a constant factor) and its range depends on the number of models (15), so the claimed "gain of 2.5" on CIN has no clear practical interpretation. Adding normalized Kendall τ would make the results more interpretable and comparable.

- **No statistical significance testing.** Results are reported as means ± std over 4 seeds, but several comparisons show overlapping error bars (e.g., AlpacaEval 0.7: PiCO PEN 1.17±0.08 vs. PRE 1.21±0.04; PiCO LIS 8.75±0.43 vs. PRD 8.25±0.83). The paper's claim of "consistent superiority" would be strengthened by paired significance tests or bootstrap confidence intervals.

### Minor

- **The ablation "anomaly" requires explicit explanation.** Random Weights + Consistency Optimization outperforms Forward Weight Voting (which uses weights w=[1,0.9,...,0] based on ground-truth order). The critic claims this is "anomalous" — it is not: Forward Weight Voting assigns arbitrary magnitudes based on the correct *order* but these magnitudes (linear decay from 1 to 0) are not necessarily optimal for the evaluation data. The consistency optimization finds better magnitudes data-adaptively. This is a *feature* of the method, not a bug, but the paper should explain this clearly rather than leaving it to the reader to infer.

- **The choice of non-standard metrics needs justification.** PEN is borrowed from time-series complexity, CIN is nearly identical to Kendall tau distance (unnormalized), and LIS is uncommon in ranking evaluation. The paper does not explain why these are preferable to or more informative than established rank correlation measures. While using them is not a flaw, failing to motivate their choice or show how they relate to standard measures limits interpretability.

- **No explicit table of learned weights w.** Showing which specific models receive high/low weights (e.g., does GPT-3.5 get a high weight? does ChatGLM-6B get a low weight?) would directly validate the consistency assumption and let readers see whether the optimization produces interpretable, sensible weights. Currently only aggregated PG heatmaps are shown.

### Trivial

- The 60% elimination threshold is presented without any sensitivity analysis. While Figure 5 explores varying the number of eliminated models and shows PiCO is competitive across the range, the final choice of 60% feels arbitrary. A brief discussion would help.

## Nice-to-Haves

- Adding the ground-truth human ranking as an oracle upper bound in Table 1 would help readers calibrate how much room for improvement remains.
- A sensitivity study on the reviewer pool composition (what if only strong or only weak models are used as evaluators?) would strengthen the analysis.

## Removed Points

- **"Ill-posed optimization objective (degenerate solutions)"** — The critic claims maximizing Pearson correlation between w and A·w is "self-referential with degenerate solutions." This is inaccurate. Pearson correlation between w and A·w is a well-defined continuous function on a compact domain; a maximum exists. Many standard methods (e.g., PCA, CCA, spectral clustering) optimize objectives where the same variable appears both in prediction and target. The real issue is lack of analysis (convergence, uniqueness), not ill-posedness, which I have moved to Major weaknesses.
- **"Forward Weight Voting uses ground truth so optimization shouldn't beat it"** — Removed because it reflects a misunderstanding: Forward Weight Voting uses the ground-truth *order* but assigns arbitrary linear magnitudes (1,0.9,...,0), not optimal weights. The data-driven optimization discovering better magnitudes is expected, not anomalous. I kept an explicit explanation as a Minor weakness because the paper should address this confusion head-on.
- **"PEN/CIN/LIS ranges are dataset-dependent, making gains uninterpretable"** — This applies equally to all methods compared within the same dataset, so it does not disadvantage PiCO. CIN is reported with raw values that are used for all methods; the comparison is fair. The real concern (lack of normalized metrics) is folded into the Major weakness above.
- **Minor wording nitpicks from the critic about "the paper reports only means and stds over 4 seeds"** — This is standard practice in many ML evaluation papers. The absence of significance tests is a real issue (kept in Major), but single-run evaluation with std over seeds is not itself a flaw.
- **Strength Finder's claim that "metrics enable fine-grained comparison"** — This is generic and over-claimed. Dropped because PEN/CIN/LIS measure the same ordinal alignment that Kendall's τ would measure; nothing uniquely "fine-grained" about them compared to standard alternatives.

## Novel Insights

None beyond the paper's own contributions. The reviews do not reveal a pattern or insight that the paper's authors have missed.

## Suggestions

1. **Specify the optimization algorithm.** Describe how argmax is computed (e.g., gradient-based? grid search? closed-form for the correlation objective?). Report convergence behavior and show the learned w values explicitly in a table.
2. **Add normalized rank correlation metrics.** Report Kendall's τ (which is \(1 - \frac{2\cdot CIN}{m(m-1)/2}\)) and Spearman's ρ alongside PEN/CIN/LIS to make results interpretable and comparable.
3. **Add statistical significance.** At minimum, report bootstrap confidence intervals or permutation test p-values for the key comparisons (PiCO vs. PRE, PiCO vs. PRD).
4. **Explain the ablation result explicitly.** A sentence like "Forward Weight Voting uses linearly decreasing weights based on ground-truth order, but these magnitudes are arbitrary; consistency optimization finds data-adaptive weights that better fit the evaluation data" would prevent reader confusion.
5. **Justify or remove the 60% elimination threshold.** Since Figure 5 already varies the elimination count, either explain why 60% is the right default or state that the method is robust across choices.

## Score and Decision

**Calibration anchors (all from the deepreview_13k_calibration set):**

| Paper | Avg Score | Comparison to PiCO |
|-------|-----------|-------------------|
| PRD (CbmAtAmQla) — Peer Rank & Discussion | 4.25 / Reject | Same sub-area (peer-review LLM eval). PRD's improvements were also limited and metrics non-standard. PiCO is slightly stronger due to fully unsupervised setting and more comprehensive experiments. |
| "Truthfulness Without Supervision" — Peer Prediction (EW62GvCzP9) | 4.67 / Reject | Unsupervised evaluation topic. Had theoretical guarantees, which PiCO lacks. Similar weakness in practical significance of results. About on par. |
| Auto-Arena (pMp5njgeLx) | 5.75 / Reject | Most comparable framework (automated peer evaluation of LLMs). Auto-Arena had stronger reported correlations (92.14%) and effective experiments, but similar methodological concerns. PiCO's unsupervised consistency optimization is a novel angle but less compelling than Auto-Arena's clear headline numbers. |
| LLMBar (tr0KidwPLc) | 7.33 / Accept | Stronger meta-evaluation benchmark with human annotation, thorough analysis. PiCO is not in the same tier — lacks the careful control and interpretability. |
| "Trust or Escalate" (UHPnqSTBPO) | 8.00 / Accept | Principled approach with provable human-agreement guarantees. PiCO has no comparable theoretical grounding. Significantly weaker paper. |

PiCO proposes a genuinely novel unsupervised evaluation direction with a clean idea (consistency optimization for peer review among LLMs). The experiments are reasonably thorough across three datasets. However, the paper has three significant issues: (1) The core optimization is underspecified — no algorithm details, no convergence analysis, learned weights never shown, making it hard to evaluate what the method actually does; (2) No standard rank correlation metrics are reported, making comparison with prior work difficult; (3) No statistical significance testing, and some improvements are modest with overlapping error bars. The ablation study actually supports the method but is presented in a way that risks confusion. The paper is closest in quality to Auto-Arena (avg 5.75, Reject) and slightly above PRD (avg 4.25, Reject) and the Peer Prediction paper (avg 4.67, Reject). It does not reach the level of the 7+ papers, which offer more rigorous methodology or theoretical guarantees.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>