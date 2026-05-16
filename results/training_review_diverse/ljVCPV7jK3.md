Now I have all the information needed to produce the consolidated review. Let me write it.

## Summary

This paper proposes FairDSR, a framework for improving the fairness-accuracy tradeoff under the "demographic scarce regime" where sensitive attributes are only partially available. The key idea is to train an uncertainty-aware attribute classifier using self-ensembling and MC dropout, then enforce fairness constraints (via exponentiated gradient) only on samples whose sensitive attributes are predicted with low uncertainty. The authors show empirically that samples with uncertain sensitive attributes are already harder for the downstream classifier to discriminate against, so focusing fairness constraints on low-uncertainty samples yields better tradeoffs. Experiments on five datasets and an ablation using conformal prediction support the core hypothesis.

## Strengths

- **Well-motivated and clean hypothesis.** The paper identifies a clear, non-obvious insight: uncertainty in the sensitive-attribute classifier is not just noise to marginalize but a signal that can be exploited to improve fairness-accuracy tradeoffs. Table 1 (tab:data-info) shows a clear correlation: datasets where the attribute classifier has higher average uncertainty (e.g., LSAC: 0.66) already exhibit lower fairness violations (ΔDP=0.014), while datasets with lower uncertainty (e.g., Adult: 0.15) have much higher violations (ΔDP=0.18). This directly validates the central premise.

- **Empirical validation across multiple dimensions.** The paper does not rely on a single experiment. It shows: (a) training without fairness constraints on high-uncertainty samples reduces unfairness (Figure 1, all 5 datasets), (b) the main FairDSR (certain) method with fairness constraints on low-uncertainty samples improves tradeoffs on Adult and Compas (Tables 2–3), (c) the consistency-loss ablation (Figure 4) isolates the contribution of self-ensembling, and (d) the conformal prediction experiment (Figure 5, Table 4) validates the hypothesis under a completely different, theoretically grounded uncertainty measure. This multi-pronged evidence makes the core claim robust.

- **Conformal prediction validation is a strong addition.** The experiment showing that using conformal prediction sets to identify low-uncertainty samples achieves better Pareto fronts than even true sensitive attributes (Figure 5) is particularly compelling. It demonstrates that the finding is not an artifact of the specific MC-dropout implementation and generalizes to principled uncertainty quantification frameworks. Table 4's result—92% fairness improvement with 8% accuracy drop when training on uncertain samples—is striking.

- **Three practical variants address different deployment scenarios.** FairDSR (certain), FairDSR (weighted), and FairDSR (uncertain) give practitioners choices depending on whether accuracy preservation, fairness maximization, or ethical concerns about inferring sensitive attributes are paramount. This is a thoughtful design choice that increases the framework's practical utility.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming the comparison to true-sensitive-attribute models.** The abstract states the framework "can outperform models trained with fairness constraints on the true sensitive attributes in most benchmarks." The evidence does not cleanly support this. On Adult (Table 2), FairDSR (certain) is *comparable* to VanilaFairness—not clearly better: DP 0.007 vs 0.005 (slightly worse), EOP 0.015 vs 0.021 (slightly better), accuracy 0.830 vs 0.829. On Compas (Table 3), the comparison reveals a *different tradeoff* rather than dominance: FairDSR (certain) achieves higher accuracy (0.676 vs 0.634) but *worse* fairness on all three metrics (DP 0.085 vs 0.032, EOP 0.067 vs 0.039, EOD 0.074 vs 0.041). The remaining three datasets (New Adult, CelebA, LSAC) lack detailed comparison tables in the main text. "Outperform" implies Pareto dominance, which is not shown. The paper's genuine contribution—improving tradeoffs compared to standard proxy-based methods—is well-supported and does not require this stronger claim. **Toning this down (e.g., "achieves competitive or better tradeoffs compared to methods using true sensitive attributes on several benchmarks") is essential before publication.**

- **Single fairness mechanism evaluated despite claiming two.** The Preliminaries section (line 49) states the study "focuses on ... exponentiated gradient and adversarial debiasing," but all main experiments use only exponentiated gradient. The paper asserts "we observed similar results with different ... fairness mechanisms" (line 272) without showing any evidence. Since the effectiveness of uncertainty-based sample selection could depend on how the fairness mechanism interacts with the subset of selected samples, results for at least one additional mechanism (or an explicit statement that only exponentiated gradient was used) are needed to support the generality claim.

### Minor

- **Only 2 of 5 datasets have full comparison tables in the main text.** Detailed numerical results are presented for Adult and Compas in the main tables. The remaining three datasets (New Adult, CelebA, LSAC) appear only in figures (Figure 1 for no-fairness analysis, and references in ablation/supplementary). While the figures provide visual evidence, the lack of a summary table across all datasets makes it difficult to assess the method's relative performance on the full benchmark suite. A compact table (or an extended version of the existing tables) covering all five datasets in the main text would substantially strengthen the empirical case.

- **Missing implementation details needed for reproducibility.** The attribute classifier's MLP architecture (number of layers, hidden units), dropout probability *p*, number of MC samples *T*, and the Gaussian warmup schedule for *R* and *λ* are not specified (lines 127, 88, 98). The threshold *H* tuning is described as selecting the "best-performing" value on a validation set (line 127), but the optimization criterion (e.g., accuracy at a fixed fairness level, or a combined score) is not stated. These details are important for independent reproduction.

- **No explicit limitations discussion.** The paper does not discuss when the method might fail or underperform. The ablation on LSAC (where average uncertainty is 0.66 and fairness is already low) suggests the method's benefits diminish when the attribute classifier has high overall uncertainty. This should be acknowledged as a limitation, along with the computational overhead of the two-phase training (self-ensembling + MC dropout + separate label classifier training).

### Trivial

- The paper would benefit from clearly stating in a single place that the reported tables (e.g., Tables 2–3) show a single operating point (the one minimizing fairness violation) while the tradeoff curves (Figure 2) show the full Pareto front. Currently the selection criterion for the tabular operating point is implicit.

## Nice-to-Haves

- Include a compact summary table comparing FairDSR against the most relevant baselines (CGL, FairDA, proxy-based methods) across all five datasets, even if abbreviated (e.g., showing ΔDP and accuracy at a single well-justified operating point).
- An analysis of how the ratio of labeled sensitive data (|\mathcal{D}_2| size) affects the method's advantage would strengthen practical guidance. The paper notes this is in the supplementary, which is good.
- A brief discussion of the computational cost of FairDSR relative to simpler proxy baselines would help practitioners assess the tradeoff.

## Removed Points

These points from the reviewers are removed or downgraded from their original framing; treat them with caution:

- **"Inappropriate and misleading baseline comparisons (ARL, DRO, CVarDRO, KSMOTE)."** The paper explicitly acknowledges (line 268) that "methods aiming to improve worst-case group accuracy (ARL, DRO, CVarDRO) do not necessarily improve fairness in terms of demographic parity or equalized odds." Including these methods as additional reference points is standard practice in fairness papers—they serve as calibration points showing that different objectives lead to different outcomes on group fairness metrics. The paper does not claim to beat them at their own game. This is not a weakness.

- **"Abstract imprecision about prior work."** The critic claims the abstract's statement about prior work showing proxy attributes can improve fairness is "imprecise" because Awasthi et al. focused on bias assessment. However, the Introduction (line 13) separately cites Gupta et al. for the claim about improving fairness via proxy. The abstract does not attribute the claim to a specific paper. This is not a meaningful imprecision.

- **"Tables report a single operating point, unclear how selected."** The paper states (line 148) "train each baseline to achieve minimal fairness violation," explaining the selection criterion. This is implicit but present. The concern is downgraded to trivial.

- **"Consistency loss coupling could lead to collapse."** The teacher-student coupling via EMA is a well-established technique (Mean Teacher, Tarvainen & Valpola 2017) with known stability properties, and the paper cites prior work for the Gaussian warmup. This is a standard approach, not a methodological gap.

## Novel Insights

The most striking finding in this paper—one that goes beyond the paper's own framing—is the confirmation that the *same* uncertainty signal can be exploited in two opposite ways that both improve fairness: (1) enforcing fairness constraints on *low*-uncertainty samples yields better constrained optimization, and (2) training without any fairness constraints on *high*-uncertainty samples already yields fairer models. The conformal prediction experiment (Table 4) quantifies this second effect dramatically: 92% fairness improvement with only 8% accuracy loss. This suggests a deeper principle: uncertainty in the attribute space is not merely a nuisance but actually indicates regions where the decision boundary is already less biased, which has implications beyond the demographic scarce regime—it suggests that models could be made fairer simply by identifying and leveraging data regions where sensitive attributes are inherently hard to predict.

## Suggestions

1. **Reframe the central claim.** Replace "outperform models trained with fairness constraints on the true sensitive attributes" with a more precise statement: "achieves fairness-accuracy tradeoffs competitive with or better than methods using true sensitive attributes on several benchmarks, while significantly outperforming standard proxy-based approaches." The paper is strongest when comparing against methods operating under the same information constraints, and the current overclaim distracts from this genuine contribution.

2. **Complete the empirical picture.** Add a summary table (or extend an existing table) showing results across all five datasets for FairDSR variants and the most directly comparable baselines (CGL, FairDA, proxy methods). If space is tight, a compact table with ΔDP and accuracy at a fixed operating point would suffice.

3. **Show results for at least one additional fairness mechanism** (adversarial debiasing, as mentioned in Section 3), or explicitly limit the scope of the claim to exponentiated gradient and note that other mechanisms are future work.

4. **Add a limitations paragraph** discussing when the method's advantage diminishes (e.g., high baseline uncertainty datasets like LSAC) and the computational overhead of the two-phase training.

5. **Provide missing implementation details** in the main text or supplementary: MLP architecture, dropout probability *p*, number of MC samples *T*, Gaussian warmup schedule, and the specific metric used to tune threshold *H*.

## Score and Decision

The paper addresses an important problem with a clean, well-motivated idea. The experimental validation is multi-faceted (five datasets, three FairDSR variants, consistency-loss ablation, conformal prediction ablation, confidence-interval comparison), and the core hypothesis is convincingly supported. The main issues are: (1) overclaiming in the abstract that is not backed by the evidence, and (2) missing results for a second fairness mechanism and a full cross-dataset summary table. These are all addressable in revision and do not undermine the paper's genuine contribution.

The paper meets the bar for acceptance, but the authors should address the overclaiming and complete the empirical picture for it to be a strong paper.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>