Now I have all the information I need. Let me compose the final consolidated review, carefully cross-referencing every claim against the paper.

---

## Summary

This paper proposes PiCO, an unsupervised evaluation framework where LLMs answer unlabeled questions and serve as anonymous peer reviewers for each other. Each LLM is assigned a learnable confidence weight \(w\), and response scores \(G\) are computed as weighted vote tallies. The optimization maximizes the Pearson correlation between \(w\) and \(G\), grounded in the "consistency assumption" that stronger models are both better evaluators and produce higher-quality answers. A reviewer elimination mechanism iteratively removes low-scoring models. The method is evaluated on Chatbot Arena, MT-Bench, and AlpacaEval using three ranking-alignment metrics (PEN, CIN, LIS) and outperforms several baselines including the supervised PRE.

## Strengths

1. **Novel unsupervised direction for LLM evaluation.** The core idea — using LLMs as peer reviewers of each other's outputs without any human-annotated data — is timely and practically motivated. The paper explicitly contrasts with supervised alternatives (e.g., PRE) and shows that an unsupervised approach can produce rankings that align well with human preferences. Evidence: Abstract (line 4–5), Section 2.2 discussion, and Table 1 results.

2. **Empirical validation of the consistency assumption via ablation.** The ablation study (Table II, lines 356–361) shows that "Random Weight + Consistency Optimization" (PEN 1.17, CIN 17.50 on MT-Bench) systematically outperforms Forward Weight Voting (PEN 1.32, CIN 21.00), Uniform, and Backward voting. This directly validates that the learned weights contribute beyond any fixed weighting scheme and confirms the consistency assumption is empirically grounded.

3. **Demonstrated bias reduction through learned confidence weights.** Figure 3 (lines 297–298) contrasts raw preference-gap heatmaps with re-weighted ones after consistency optimization. Models known to be weaker (ChatGLM-6B, Mpt-7B) receive lower learned weights, and the system-level evaluation bias is visibly reduced. This provides mechanistic insight into why the optimization helps.

4. **Consistent improvement over strong baselines across data volumes.** In Table 1, PiCO achieves the best scores on nearly all data fractions (1.0, 0.7, 0.4) across all three datasets and all three metrics. For example, on Chatbot Arena at full data: PiCO achieves PEN 0.94 vs. next-best PRE 1.07, CIN 12.00 vs. 15.00, LIS 10.00 vs. 9.00. The advantage holds even at 40% data, suggesting robustness.

5. **Unsupervised elimination matching or exceeding supervised elimination.** Figure 4 shows PiCO's CIN consistently lower than PRE's across varying numbers of eliminated reviewers, despite PRE requiring human-annotated qualification exams for elimination. This strengthens the paper's claim that the fully unsupervised pipeline is viable.

## Weaknesses

### Fatal
None.

### Major

1. **Consistency optimization algorithm is underspecified, preventing reproducibility.** The paper's central technical contribution (Eq. G, lines 143–148) is to maximize Pearson correlation between \(w\) and \(G\) with \(G = M w\), but it never states *how* this optimization is performed. No optimizer is named (SGD? closed-form? fixed-point iteration?), no learning rate, no update rule, no stopping criterion, no initialization scheme for \(w\). The paper says "we only introduce this straightforward implementation to validate our idea" (line 148), but without specifying the algorithm, the reader cannot distinguish the method from an arbitrary fixed-point heuristic. The ablation in Table II shows the optimization improves results, but the reader cannot replicate it. This is not a minor omission — the optimization is the core claimed contribution. The paper must specify the algorithm to be considered a complete methodological contribution.

2. **Reviewer elimination mechanism is vague on critical operational details.** The mechanism is described in one sentence (line 156): "It iteratively removes the lowest-scoring LLM from the 'reviewer queue' for the next consistency optimization stage, until 60% of models are eliminated." Several essential details are missing:
   - **What score is used to determine "lowest-scoring"?** Is it the learned weight \(w_j\) or the response score \(G_j\)? These are different quantities.
   - **How is the first elimination decided** before any optimization has been run? The paper describes elimination happening iteratively with re-optimization, but the initial ranking before the first optimization is unclear.
   - **What is the exact iterative protocol?** Does one optimize to convergence, eliminate one model, then re-optimize from scratch or warm-start?
   - **The 60% threshold is neither justified nor ablated.** Figure 4 shows CIN as a function of eliminated reviewers, which partially addresses this, but the paper never discusses why 60% was chosen or how stable the results are near that threshold.
   
   These gaps make the elimination mechanism non-reproducible and leave questions about whether the results are robust to arbitrary design choices.

### Minor

3. **The three "proposed" metrics (PEN, CIN, LIS) are existing measures, not novel inventions.** The paper presents them as contributions (lines 8, 55: "We propose three metrics called PEN, CIN, and LIS"). However:
   - PEN is permutation entropy, cited to Bandt & Pompe (2002).
   - CIN is the count of inversions (= unnormalized Kendall tau distance), cited to CLRS.
   - LIS is the classic longest increasing subsequence problem.
   
   The paper cites the original sources for each, so the authors are not claiming to have invented these concepts from scratch. The language "propose" is an overstatement — these are standard ranking-comparison statistics applied to this specific problem. The contribution is in the *application* of these metrics to the peer-review evaluation setting, which is a reasonable but modest methodological choice, not a novel metric contribution.

4. **Comparison with PRE, while valid, could be better contextualized.** The paper repeatedly highlights that unsupervised PiCO outperforms supervised PRE (lines 251, 328). This is a legitimate and interesting result. However, PRE's supervised elimination uses human-annotated qualification exams, while PiCO's elimination uses scores from its own optimization — these are fundamentally different approaches to elimination, not just different supervision levels. A discussion of whether PRE with an unsupervised elimination variant might narrow the gap would strengthen the analysis.

5. **Pearson correlation objective has mathematical properties that deserve discussion.** The objective \(\text{argmax}_w \text{Corr}(w, Mw)\) has a known structure: because \(G = Mw\) is a linear function of \(w\), the optimization effectively seeks a fixed point where \(w\) and its own linear image are maximally correlated. The solution space may have symmetries (Pearson is scale- and shift-invariant), and convergence properties depend on the eigenstructure of \(M\). The paper acknowledges this is a "straightforward implementation" (line 148), but some analysis or at least empirical diagnostics (convergence plots, sensitivity to initialization) would substantially strengthen confidence that the reported results are not artifacts.

### Trivial

6. The Discussion paragraph (lines 150–151) provides an intuitive example with three scholars but does not connect to a concrete algorithm — this is fine as illustration but should not be mistaken for an algorithmic description.

7. The paper assumes the Chatbot Arena human ranking is ground truth (line 67, 165) without discussing known noise/bias in crowdsourced human preferences. A brief acknowledgement would improve honesty.

## Nice-to-Haves

- **Algorithm pseudocode** for the two-stage pipeline (peer review → iterative elimination → optimization → ranking) would greatly improve clarity.
- **Convergence plots** showing how the Pearson correlation evolves during optimization.
- **An ablation of the 60% elimination threshold** (e.g., vary from 0% to 80% and report CIN with variance).
- **Computational cost estimates** (API calls, wall-clock time) to help readers assess practicality.
- **Reporting Kendall's \(\tau\)** alongside CIN for familiarity with the community-standard metric.

## Removed Points

These points were flagged by reviewers but removed after cross-checking with the paper:

- **"Comparison with PRE is misleading (apples to orangutans)"** — Removed. The paper explicitly acknowledges PRE is supervised (line 189: "supervised process," lines 251, 328) and frames the comparison correctly. Comparing unsupervised vs. supervised methods targeting the same task is standard practice; outperforming a supervised method is a legitimate strength.

- **"Elimination may be implicitly guided by human labels"** — Removed. The elimination uses \(G\) or \(w\) scores derived from the peer-review data, not human labels. Human labels are used only for evaluation (ground-truth ranking), not in the optimization or elimination loop. The feedback loop concern is speculative and unsupported by the paper.

- **"Would eliminating 100% yield better scores?"** — Removed. This is a strawman; eliminating all reviewers would trivially break the method. The paper's Figure 4 already provides an ablation over elimination counts.

- **"The paper conflates evaluation method with ranking method"** — Removed. The paper's goal (line 66–77) is explicitly to produce a ranking; the evaluation IS the ranking. This is a category error by the reviewer.

- **"Random seed / initialization concerns"** — Partially addressed: the paper reports means and stds over 4 seeds (line 194). The reviewer's deeper concern about optimization non-uniqueness is kept under Weakness #5 (Minor).

- **"Missing pseudocode"** — Moved to Nice-to-Haves. Helpful but not a weakness.

- **"Generic formatting/stylistic nitpicks"** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate concerns present in the paper itself (underspecification) without adding new analytical insights that the authors could not have anticipated.

## Suggestions

1. **Specify the optimization algorithm.** Provide the exact update rule, initialization, stopping criterion, and any regularization. A single pseudocode block would resolve the main reproducibility concern.
2. **Clarify the elimination mechanism.** State exactly what score determines "lowest-scoring" (is it \(w\) or \(G\)?), how the first elimination is decided, and the exact iterative protocol (converge-then-eliminate or interleaved?).
3. **Reframe the three metrics** as "adopted evaluation measures" rather than "proposed metrics," or add justification for why this specific combination is uniquely suited to the PiCO framework.
4. **Add convergence diagnostics** (one plot of Pearson(\(w, G\)) vs. iteration on one dataset) and report sensitivity to \(w\) initialization.
5. **Acknowledge the limitation** that human ground-truth rankings (Chatbot Arena) are themselves noisy.

## Score and Decision

The paper proposes a genuinely interesting and well-motivated idea — unsupervised peer-review for LLM evaluation. The experimental results are consistently strong across three datasets and multiple baselines. The ablation study convincingly validates the consistency assumption. However, the paper has a **major reproducibility gap**: the central optimization algorithm and the elimination mechanism are both underspecified to a degree that prevents independent verification and reuse. Given that this is the paper's core claimed contribution, these omissions are serious. The paper can be made acceptable with a revision that specifies the optimization algorithm, clarifies the elimination procedure, and tones down the metrics overclaim. In its current form, the contribution is not fully demonstrated.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>