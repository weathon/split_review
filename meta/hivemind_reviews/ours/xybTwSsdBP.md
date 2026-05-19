## Summary
The paper proposes **OptBatch**, an online batch selection method for instruction tuning of LLMs. OptBatch combines three ideas: (1) stratified sampling of each batch based on loss values, where samples are selected with probability proportional to exp(loss), (2) farthest-point sampling within strata using a **Hessian gradient** feature (gradient normalized by Adam's second-moment estimate) to maximize inter-sample diversity, and (3) cross-stratum constraints that consider previously selected points when choosing from subsequent strata. Experiments on three large datasets (NetLit, LLaMaQA, WikiMatrix) with two 6-8B models show that OptBatch achieves lower loss at multiple pruning rates and outperforms CCS, InfoBatch, and other online baselines on GPT-4 evaluation, human evaluation, BLEU, and ROUGE metrics.

## Strengths
- **Novel Hessian gradient feature for data selection (derived from Adam's second moment):** The paper proposes using \(H_t = \| \mathbf{g}_t / \sqrt{\hat{\mathbf{v}}_t} \|_{2,\text{axis}=1}\) as the sample representation (Eq. 8), which incorporates global gradient history from the Adam optimizer rather than using raw gradient norms or static embeddings. Figure 9 explicitly compares this against embeddings and raw gradient norms on NetLit and shows the Hessian gradient achieves the lowest loss, providing direct evidence that the feature choice matters.

- **Principled combination of learnability (loss stratification) and diversity (distance maximization):** OptBatch addresses both dimensions simultaneously — stratified sampling with exp(loss) probability targets learnable/under-trained samples, while farthest-point sampling on Hessian gradients within and across strata enforces coverage. This goes beyond CCS (uniform sampling per stratum) and InfoBatch (fixed loss threshold), and the paper supports the design with a Lipschitz-continuity argument connecting gradient coverage to loss bounds (Section 3.1).

- **Consistent empirical advantage across diverse tasks, models, and pruning rates:** On three large-scale datasets (dialogue, QA, translation) and two models (LLaMa3-8B, ChatGLM3-6B), OptBatch achieves the lowest loss across multiple pruning rates (Figures 3–6). The ablation showing loss decreasing from \(\alpha=20\%\) to a minimum at \(\alpha=50\%\) (Figure 6) is particularly interesting — it suggests that a pruned subset can reach lower loss than a larger subset, indicating effective removal of redundant/noisy data.

- **Multi-faceted evaluation beyond loss curves:** The paper includes GPT-4 scoring (60.5% score-5 for OptBatch vs. 52.6% CCS, 43.5% InfoBatch), human evaluation (61.8% vs. 47.5%/47.9%), and reference-based metrics (BLEU-4, ROUGE-1/2/L) on LLaMaQA and WikiMatrix (Tables 1–2). This provides converging evidence across automated, human, and reference-based assessments, at least for the 70% pruning rate.

- **Efficient gradient computation via lm-head layer:** Computing gradients only from the lm-head layer (Section 2.1) and using sequence-level gradients keeps the selection overhead practical, a sensible design choice that the paper explicitly justifies.

## Weaknesses
### Fatal
None. The paper's core claims are supported by evidence, and no verified flaw invalidates its main conclusions.

### Major

- **Insufficiently specified algorithm undermines reproducibility.** The paper describes the selection procedure in prose and Figure 1, but several critical details are missing: (1) the number of strata \(K\) is never stated — Figure 1 illustrates 3 strata but the text never specifies \(K\) or how it is chosen; (2) the allocation rule for determining how many samples \(|S_i|\) to select per stratum is only described as "select \(|S|\) data according to the probability of \(\exp(\mathrm{loss})\) and calculate the number of data in each stratum" — the precise mechanism mapping exp(loss) probabilities to per-stratum counts is undefined; (3) no pseudocode or algorithmic listing is provided for the farthest-point selection with cross-stratum constraints. Without these details, the method cannot be independently reimplemented. *[Verified: Paper never states \(K\), allocation is described only at the prose level in Section 3/Figure 1, no pseudocode.]*

- **No statistical uncertainty reported on any metric.** All loss curves (Figures 3–6) are shown as single lines with no error bars, confidence intervals, or variance estimates. The BLEU/ROUGE scores (Tables 1–2) are reported as point estimates with no variance across runs. Given the modest improvements (e.g., 75.25 vs. 74.96 BLEU-4 on WikiMatrix), it is impossible to assess whether these differences are statistically significant. This is particularly important because the paper's central claim — that OptBatch "outperforms full dataset training" — rests on differences that are numerically small. *[Verified: No variance, error bars, or significance tests anywhere in the paper.]*

- **Computational savings claim lacks empirical runtime validation.** The FLOPs analysis (Section 4.4) provides a theoretical formula showing backward-pass savings at pruning rate \(\alpha\), but (a) it does not account for the overhead of the selection algorithm itself (forward pass for computing losses on all samples, Hessian gradient computation for all samples, pairwise distance computations), and (b) no wall-clock training time measurements are reported. The paper claims "reducing computational cost by 20–40%" and "at least 30%" savings, but these are uncalibrated FLOPs estimates, not measured runtime. Without actual timing data, the practical cost reduction is unverified. *[Verified: No wall-clock times reported anywhere; FLOPs formula omits selection overhead.]*

- **Theoretical section (Lipschitz continuity, Section 3.1) is not self-contained and does not connect to algorithm design choices.** Equation (7) presents an upper bound \(\|\nabla l(x,y;h_S')\| \leq r L_s + \sqrt{\frac{L^2 \log(1/\gamma)}{2n}}\), but none of the symbols \(r, L_s, L, \gamma, n\) are defined in the text, and no derivation is provided. The bound is cited from coreset theory (Sener & Savarese, 2017) but is not adapted to the gradient-based setting of this paper. The claim that "maximizing gradient distances between samples within the subset thus enhances the coverage of the entire dataset" does not follow from the Lipschitz bound as presented. This section reads as decorative rather than functional to the method's justification. *[Verified: Equation (7) appears on line 90 with undefined symbols; no derivation or connection to algorithm is given.]*

### Minor

- **Ablation study is limited in scope.** Figure 9 compares embedding, gradient norm, and Hessian gradient as features, but only at a single pruning rate (70%) on a single dataset (NetLit). There is no ablation that isolates the contribution of the farthest-point selection component vs. random selection within strata, or the contribution of the exp(loss) allocation vs. uniform allocation. These ablations would substantially strengthen the paper's evidence.

- **Reference-based metrics (Tables 1–2) reported at only one pruning rate (70%).** The loss curves show results at multiple pruning rates, but the downstream evaluation metrics are only given for 70% pruning. This limits the assessment of whether OptBatch's advantage holds across different data budgets.

- **FLOPs analysis omits selection overhead.** While the forward pass for computing losses is included (it is part of standard training), the pairwise distance computations for farthest-point sampling and the Hessian gradient computation introduce additional cost that is not quantified. A quantitative estimate of this overhead would help readers assess the net savings.

- **InfoBatch baseline is modified.** The paper states "we increase the threshold appropriately for higher pruning rates" when implementing InfoBatch. While this modification is disclosed, it may change InfoBatch's behavior in ways that could disadvantage it relative to its original formulation. A sensitivity analysis showing performance with and without the modification would clarify this.

- **Held-out evaluation set sizes are not stated.** The paper does not specify what fraction of each dataset was used for evaluation, making it difficult to assess the reliability of the reported metrics.

### Trivial
None of note beyond the parser-level formatting artifacts that are not author errors.

## Suggestions
1. **Fully specify the algorithm:** Provide a pseudocode listing stating \(K\), the exact allocation rule for per-stratum sample counts, and the distance computation procedure (including how cross-stratum distances are handled). This is the single most important improvement for reproducibility.

2. **Add wall-clock time measurements:** Report training time (forward + backward + selection) for Full-Batch, Random, CCS, InfoBatch, and OptBatch at multiple pruning rates on identical hardware. This would substantiate the computational savings claim far more convincingly than FLOPs estimates.

3. **Run experiments with multiple seeds and report variance:** Even 2–3 seeds with standard deviations or confidence intervals would dramatically strengthen the statistical foundation of the results.

4. **Expand ablation studies:** (a) Random vs. farthest-point selection within strata, (b) exp(loss) vs. uniform allocation per stratum, (c) Hessian gradient vs. raw gradient norm (already partially done) — across multiple datasets and pruning rates.

5. **Report downstream metrics at multiple pruning rates** (not just 70%) to show that the advantage generalizes across data budgets.

## Score and Decision

The paper proposes a solid, well-motivated combination of ideas (loss-stratified sampling + farthest-point diversity + Hessian-gradient features) and provides evidence of effectiveness across large-scale experiments with multiple models and evaluation paradigms. The core contribution is interesting and likely useful to the community.

However, the paper is weakened by significant presentation and rigor gaps: the algorithm is underspecified (no \(K\) value, no allocation rule, no pseudocode), no statistical uncertainty is reported on any metric, and the headline computational savings claim is supported only by uncalibrated FLOPs estimates without wall-clock measurements. The theoretical section is non-functional as presented.

These issues are fixable with a major revision, and the underlying method appears sound. In its current form, the evidence supports the method's promise but not the strength of the claims made.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
