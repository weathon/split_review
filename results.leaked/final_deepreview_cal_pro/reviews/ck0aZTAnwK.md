Now I can write the final consolidated review.

---

## Summary
This paper studies language model pre-training under fixed data and unlimited compute. The authors show that standard recipes overfit under data constraints, then demonstrate that using much higher weight decay (up to 30× standard practice) yields a regularized recipe whose validation loss follows a power law in parameter count. They propose evaluating recipes by the asymptote of their scaling law — the loss limit as parameter count or ensemble size goes to infinity — rather than by performance at a fixed compute budget. Ensembles of smaller models achieve lower asymptotes than single large models, and composing parameter and ensemble scaling yields the best results, with estimated data-efficiency gains of up to 5.17× over the baseline. These gains can be compressed into smaller models via distillation and transfer to downstream benchmarks.

## Strengths
- **Novel and well-motivated framing**: The idea of using power-law asymptotes to characterize performance under infinite compute is creative and useful. It transforms a practical observation (data is growing slower than compute) into a principled evaluation framework. The paper clearly motivates why compute-optimal or parameter-constrained metrics are the wrong lens for this regime.

- **Clean, systematic empirical narrative**: The paper builds its case step by step — first establishing that standard recipes overfit (Section 2), then showing that proper regularization enables monotonic parameter scaling with a well-defined asymptote (Section 3), then demonstrating that ensembling achieves a better asymptote (Section 4), then composing both (Section 4.3). Each section directly motivates the next, producing a coherent story.

- **Multiple complementary findings**: The paper does not stop at scaling laws — it also shows that ensemble gains survive distillation (preserving 83% of the improvement at 8× smaller inference cost), that self-distillation can improve a model without training anything larger, and that validation-loss improvements transfer to downstream benchmarks (9% average improvement on PIQA, SciQ, ARC Easy). These results strengthen the practical relevance of the asymptotic analysis.

- **Practical insight about weight decay**: The finding that optimal weight decay in data-constrained regimes is 30× larger than the commonly used default of 0.1 (from Brown et al., 2020) is a concrete, actionable takeaway for practitioners.

## Weaknesses

### Fatal
None.

### Major
- **Extrapolation from sparse data with unquantified uncertainty**: The paper's key quantitative results (asymptotes of 3.43, 3.34, 3.17; data efficiency of 5.17×) come from fitting 3-parameter power laws to only 4 data points (parameter counts 150M, 300M, 600M, 1.4B). With 4 points and 3 free parameters, the asymptote estimate is heavily determined by the behavior at the largest measured point plus the assumed functional form. The sensitivity analysis (Appendix I.1) reports variance across 3 seeds but does not address instability of the asymptote estimate under alternative functional forms or fitting procedures. The data-efficiency numbers compound this through multiple levels of extrapolation: K→∞ asymptotes feed into N→∞ asymptotes, which feed into data-scaling laws. The paper acknowledges the laws are "expected to be noisy" (Section 5.3) but never quantifies how this noise propagates. The qualitative direction of the findings is likely correct, but the precise numerical claims (2.29×, 3.03×, 5.17×) are not well-supported by the evidence presented.

- **Limited scale relative to stated ambition**: The paper studies a regime relevant to a future where "compute vastly exceeds data," but all experiments use only 200M–1.6B tokens and models up to 1.4B parameters — orders of magnitude below modern pre-training scale. While small-scale studies can provide useful insights, the paper's extrapolations to larger token counts (Section 5.3) are purely model-based with no out-of-distribution validation. A single validation point at a larger scale (e.g., 10B tokens) would substantially strengthen the credibility of the extrapolation methodology.

### Minor
- **Ensemble hyperparameters chosen heuristically**: The joint scaling recipe (Section 4.3) uses a heuristic of "2× epochs and 0.5× weight decay" rather than the coordinate-descent hyperparameter optimization that Section 3 showed was critical. While the justification is deferred to Appendix D.4 (present in the original submission), the contrast between the careful tuning in Section 3 and the heuristic in Section 4.3 weakens confidence that the reported ensemble asymptotes represent the best possible ensemble performance.

- **Downstream evaluation is limited**: The three benchmarks (PIQA, SciQ, ARC Easy) are appropriate for the model scale but are relatively easy tasks where performance differences may saturate quickly. The 9% relative improvement is over an intentionally weak baseline (unregularized model) and the absolute error reduction is modest. This is not a flaw per se — the paper is primarily about validation loss scaling — but it limits how strongly the downstream results support the claim that data-efficiency gains transfer to capabilities.

- **Standard recipe baseline could be strengthened**: The standard recipe tunes learning rate and epoch count but fixes weight decay at 0.1, while the regularized recipe additionally tunes weight decay. This is a fair comparison between "standard practice" and the proposed improvement, and the paper's core claim is precisely that standard weight decay values are too low. However, including a variant where weight decay is also tuned for the "standard recipe" would disentangle "better hyperparameter tuning in general" from "the regularized recipe being different," strengthening the paper's contribution.

### Trivial
- The self-distillation result (Figure 8, green star) is a single data point without error bars or ablations. While suggestive, it would benefit from at minimum reporting variance across seeds.

- The paper reports power-law exponents like 1.02 (Section 3) with two decimal places but the fits come from only four points; reporting confidence intervals or standard errors would better reflect the uncertainty.

## Nice-to-Haves
- Bootstrapping over the fitted points or comparing alternative functional forms (e.g., without an asymptote term, or with different exponents) would substantially strengthen confidence in the asymptote estimates.
- A correlation or diversity analysis of ensemble member predictions would help support the mechanism claim about ensembles (the multi-view hypothesis from Allen-Zhu and Li, 2023).
- Scaling to one or two additional token counts for a subset of recipes would provide an out-of-distribution validation of the extrapolation methodology.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Central claims rest on extrapolations from four data points at tiny scale"** — partially retained above but the harsh critic's framing as "the entire quantitative edifice is not trustworthy" was overly strong. The paper is transparent about its scale and characterizes its analysis as preliminary. The qualitative insights remain valuable.

- **"The standard-recipe baseline is not fairly configured"** — weakened and reframed above. The comparison is between standard practice and an improved recipe; this is a legitimate experimental design choice, not an unfair comparison. The paper's claim is precisely that standard weight decay is too low.

- **"The 'no compute constraints' framing is in tension with the paper's actual contributions"** — removed. The paper is internally consistent: infinite compute enables asymptotic analysis; data efficiency compares recipes; distillation addresses inference cost (a separate concern from training compute). These are different parts of a coherent argument, not a contradiction.

- **"Section 2 overfitting curves are unsurprising"** — removed. Demonstrating known phenomena in a specific setting to establish a baseline is reasonable scientific practice, not a weakness.

- **"The reader cannot assess whether the claimed 'locally optimal' hyperparameters are genuinely near-optimal or merely adequate" (reference to stripped appendix)** — removed per hard rule: the appendix exists in the original submission. Criticisms rooted in missing appendix content are parser artifacts.

- **"The amount of synthetic data generated (D'), the sampling temperature, and the distillation training procedure are not specified in the main text"** — removed per hard rule: these details are in Appendix F, which exists in the original submission.

- **"The ensemble recipe uses hyperparameters... without justification beyond a reference to a stripped appendix"** — partially removed for the same reason, but the contrast between careful Section 3 tuning and Section 4 heuristics is retained as a minor weakness.

- **"The paper does not discuss the relationship between validation loss improvements and downstream capability improvements at larger scales"** — removed as scope creep. The paper evaluates at its own scale and acknowledges limitations.

- **"The ensemble member independence assumption is never examined"** — moved to Nice-to-Haves. This is a worthwhile analysis but not a weakness of the paper's core claims.

## Novel Insights
The most genuinely novel insight from this work is the proposal to compare training recipes by the **asymptote** of their scaling law rather than by performance at a fixed compute or parameter budget. This is a simple but powerful reframing: under infinite compute, what matters is where the scaling curve plateaus, not where it crosses a particular budget line. The paper demonstrates that different recipes (parameter scaling, ensemble scaling, joint scaling) have different asymptotes, and that the asymptote metric leads to actionable conclusions — for example, that at sufficiently large total parameter counts, training multiple smaller models and ensembling them is better than training one large model. This metric could be adopted by other researchers studying data-constrained pre-training.

## Suggestions
- The single highest-impact improvement would be to validate the extrapolation methodology at one larger scale (e.g., 10B tokens). Even a single data point showing that the asymptote estimated from 200M-token experiments predicts behavior at 10B tokens would dramatically strengthen the paper.
- Report confidence intervals on asymptote estimates, either through bootstrapping or by comparing fits with and without an asymptote term. This would help readers distinguish robust findings from fitting artifacts.
- Add the weight-decay-tuned variant of the standard recipe to the comparison. If the standard recipe with tuned weight decay still underperforms the regularized recipe, it strengthens the contribution; if it matches, the contribution becomes a finding about the importance of weight decay in data-constrained regimes, which is also valuable.

---

## Score Calibration

**Round 1 Bracket**: Based on the initial calibration search, the paper plausibly falls in the **4.5–6.5** range. The upper anchor at 6.50 ("Language models scale reliably with over-training") has substantially stronger empirical validation (104 models, up to 6.9B parameters). The lower-middle anchors at 5.20–5.25 ("Hitchhiker's Guide," "Scaling Laws for Multilingual," "Time Transfer") have stronger methods or datasets but less creative framing.

**Round 2 Narrowing**: Compared to "No Free Lunch from Random Feature Ensembles" (5.60), the paper under review has a more practical setting and a broader empirical story (regularization → ensembles → joint scaling → distillation → downstream), but weaker theoretical backing and similar concerns about limited scale of evidence. Compared to "A Hitchhiker's Guide to Scaling Law Estimation" (5.20), the paper under review has a more novel and focused contribution but less thorough empirical methodology. The paper is somewhat weaker than "Language models scale reliably with over-training" (6.50), which demonstrates the same kind of scaling-law extrapolation with far more extensive validation.

**Final Score**: The paper lands between the 5.60 and 6.50 anchors — stronger in framing and narrative coherence than the 5.60 anchor, but with thinner evidence than the 6.50 anchor. I assign **6.0**. The core idea (asymptote as metric) is good and the empirical story is clean and internally consistent, but the quantitative claims rest on multi-level extrapolation from limited data points without uncertainty quantification. The paper would benefit from stronger validation but makes a sufficiently novel and well-structured contribution.

**Anchor comparison summary**:
- `xGM5shdGJD` (5.20, Round 1): Scaling law estimation best-practices guide. Paper under review has more novel framing, comparable empirical rigor.
- `T2h2V7Rx7q` (5.25, Round 1): Multilingual scaling laws. Paper under review has broader scope of methods studied.
- `MLhquJb1qN` (5.25, Round 2): LR and batch size in infinite data limit. Paper under review addresses a more impactful question with more comprehensive experiments.
- `PtgfcMcQd5` (5.50, Round 2): Information-theoretic scaling law framework. Paper under review has cleaner empirical validation.
- `7rzA6aEASo` (5.60, Round 2): No free lunch from random feature ensembles. Paper under review has broader empirical scope (regularization, distillation, downstream) but weaker theoretical grounding.
- `iZeQBqJamf` (6.50, Round 1): Scaling laws with over-training. Stronger empirical validation than paper under review; paper under review has more creative framing.
- `vPOMTkmSiu` (6.60, Round 1): Scaling laws for MT downstream tasks. Stronger empirical depth; paper under review addresses a more fundamental pre-training question.
- `c61unr33XA` (7.00, Round 2): Dataset distillation via KD. Different topic; stronger novelty and validation.
- `5HCnKDeTws` (6.75, Round 2): LLM finetuning scaling. Different topic; more thorough experiments.
- `wg1PCg3CUP` (8.00, Round 1): Scaling laws for precision. Clearly stronger — more extensive validation and broader implications.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>