---
job_id: 658e34df-63e4-47bb-ad8f-8332916811ba
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: y7VeiCT7HG.pdf
paper: Probability of Matching for Pareto Coverage
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically probabilistic methods, Bayesian optimization, uncertainty-aware acquisition design, and applications to physical sciences.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While I have substantial concerns about novelty, formulation, and empirical support, these rise to the level of a negative review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided manuscript text and figures.

# Expected Review Outcome:
## Summary
This paper studies batch multi-objective Bayesian optimization and proposes a new acquisition perspective called Probability of Matching, intended to favor batches that are both Pareto-optimal and diverse enough to cover the Pareto set. The practical method derived from this idea, qEHVI-SF, combines qEHVI with a space-filling term based on the minimum Euclidean distance within the batch and to previously evaluated points. The paper evaluates the method on two benchmark problems and a materials discovery case study, using standard MOBO metrics as well as a design-space coverage metric called Expected Minimum Distance (EMD).

## Strengths
The paper addresses a real and important issue in batch MOBO, namely that hypervolume-based methods can overconcentrate on certain regions of the Pareto front and may not recover diverse Pareto-optimal designs. The emphasis on design-space coverage, rather than only objective-space coverage, is practically meaningful in domains such as materials discovery where multiple distinct designs can map to similar objective values.

The empirical study is reasonably broad in terms of task types. The paper includes synthetic-style benchmarks, a higher-dimensional real-world benchmark, and a materials inverse design case study. This is better than a paper that only demonstrates behavior on toy 2D fronts.

The central empirical trend is visually consistent across several figures. In **Figure 1** on Pages 7 and 8, the qEHVI-SF curves often show lower EMD and competitive or better hypervolume over iterations than qEHVI and QSVGD, especially in the GM setting. Even without exact numerical confidence intervals in the figure, the qualitative pattern the authors want to highlight is clear: the proposed method tends to avoid the obvious degradation in coverage that standard qEHVI shows for some batch sizes. Likewise, **Figure 2** suggests that rediscovery ratio in the alloy tasks often favors qEHVI-SF, which supports the paper’s motivation that design-space coverage matters in rediscovery-oriented applications.

The runtime analysis is a useful inclusion. **Table 1** directly addresses a practical concern, namely whether the additional space-filling term makes qEHVI-SF too expensive. The reported runtime appears broadly comparable to qEHVI and QSVGD in many settings, and the paper is right to discuss that the hypervolume component dominates at larger numbers of objectives.

The paper is also honest in at least one respect: the conclusion explicitly acknowledges that the connection between the distance heuristic and the true coverage probability remains unclear. That limitation is important and, to the authors’ credit, it is not entirely buried.

## Weaknesses
I have substantial reservations about the paper’s conceptual formulation, mathematical precision, and the degree to which the experiments actually validate the claimed probabilistic interpretation. In its current form, the work feels like a distance-reweighted qEHVI heuristic wrapped in stronger probabilistic language than the paper really justifies.

1. **The core “Probability of Matching” formulation is not well-defined for the setting considered, and Equation (7) is conceptually shaky.**  
   On **Page 4, Equation (7)** defines
   \[
   P(\mathbf{X}=\mathcal{X}^*) = P(\mathcal{X}^*\subseteq \mathbf{X}, \mathbf{X}\subseteq \mathcal{X}^*) = P(\mathbf{X}\subseteq \mathcal{X}^*) P(\mathcal{X}^*\subseteq \mathbf{X}\mid \mathbf{X}\subseteq \mathcal{X}^*).
   \]
   This is elegant on paper, but the event itself is ill-matched to the actual MOBO problem discussed in the manuscript. In many continuous problems, \(\mathcal{X}^*\) is an infinite or continuum-valued set, while \(\mathbf{X}\) is a finite batch of size \(q\). Then the event \(\mathbf{X}=\mathcal{X}^*\) is impossible except in degenerate cases. The paper partially acknowledges this later by replacing exact inclusion with coverage via unions of radius-\(r\) balls, but then the object being optimized is no longer the stated Probability of Matching. This matters because the paper’s main conceptual claim is precisely that it derives a principled probabilistic acquisition; yet the derivation effectively jumps from a set-equality probability to a heuristic coverage proxy without a rigorous bridge.

2. **The approximation from “probability of coverage” to a minimum-distance multiplier is not justified, and the leap is much bigger than the paper admits.**  
   In **Section 3.2, Page 5**, the authors argue that because the batch size and ball radius are fixed, increasing coverage corresponds to reducing overlap, and therefore maximizing the minimum pairwise distance is a natural objective. But the actual acquisition in **Equation (8)** uses
   \[
   \mathbb{E}\left[\text{HVI}(\cdot)\cdot \min\{\Delta(\mathbf{X},\mathbf{X}), \Delta(\mathbf{X},\mathbf{X}_n)\}\right].
   \]
   This is a very specific surrogate. It is neither shown to approximate
   \[
   P(\mathcal{X}^*\subseteq A'_{\mathbf{X}} \mid \mathbf{X}\subseteq \mathcal{X}^*)
   \]
   nor even to be monotone with respect to any explicit coverage functional beyond the loose intuition that “farther apart is better”. In multiple dimensions, union-of-ball coverage depends on all pairwise distances and the geometry of \(\mathcal{X}^*\), not only the smallest one. Two batches with identical minimum distance can have very different covered volume. So the actual method is a max-min-distance heuristic, not a probabilistic estimator in any meaningful sense based on the paper’s own exposition. This gap is not cosmetic; it undercuts the main claimed contribution.

3. **The paper claims qEHVI approximates \(P(\mathbf{X}\subseteq \mathcal{X}^*)\), but this is not established and is arguably misleading.**  
   In **Section 3.2, Page 5**, the manuscript states, “we first use normalized qEHVI to approximate \(P(\mathbf{X}\subseteq \mathcal{X}^{*})\)”. qEHVI is an expected hypervolume improvement criterion, not a calibrated probability that every point in the batch is Pareto optimal. The manuscript provides no derivation, no normalization formula, and no argument that the ranking induced by qEHVI is probabilistically meaningful in this sense. This is a serious issue because the entire factorized interpretation depends on assigning one factor to “quality probability” and another to “coverage probability”. At present, this is more metaphor than mathematics.

4. **Equation (8) is underspecified and mathematically awkward relative to the claimed objective.**  
   Still on **Page 5**, the acquisition is written as an expectation of a product between hypervolume improvement and a deterministic distance term. Since the distance term depends only on \(\mathbf{X}\) and observed design points, it can be pulled outside the expectation:
   \[
   \alpha(\mathbf{X}) = \min\{\Delta(\mathbf{X},\mathbf{X}),\Delta(\mathbf{X},\mathbf{X}_n)\}\cdot \mathbb{E}[\text{HVI}].
   \]
   If that is indeed the intended objective, the expression should be simplified and discussed as a multiplicative reweighting of qEHVI. More importantly, the units are odd: hypervolume improvement in objective space is multiplied by Euclidean distance in design space, producing a quantity with no interpretable probabilistic meaning. This does not make the heuristic invalid per se, but it further emphasizes the mismatch between the stated probability framework and the implemented score.

5. **Several definitions and notational choices are sloppy enough to interfere with technical trust.**  
   There are multiple places where the mathematics reads as underpolished. For example, the Pareto front definition on **Page 2, Section 2.1** contains garbled notation, “\(\mathbb{\bar{\beta}}\mathbf{y}'\text{ s.t. }\mathbf{y}'\prec \mathbf{y}\)”, which appears to be a formatting or symbol error in the definition of \(\mathcal{Y}^*\). That is exactly the kind of place where precision matters. In **Equation (6)** on **Page 4**, the QSVGD baseline is written using \(\mathcal{H}\) for both hypervolume and entropy, overloading notation in a confusing way. Also, the expectation there is over \(\mathbf{y}^{(1:\eta)}\), which seems inconsistent with batch size \(q\) and suggests a notation mistake. These are not just typographical nits, because the paper’s main contribution is a new acquisition derivation. When the equations are this loose, confidence in the derivation drops.

6. **The complexity analysis is not very convincing as presented, and parts of it are disconnected from how acquisition optimization is actually done.**  
   In **Section 3.3, Pages 5 to 6**, the paper gives asymptotic expressions involving \(\binom{|\mathcal{X}|}{q}\), effectively counting all possible batches from a candidate set. But the experiments are said to be run in BoTorch with joint optimization, which typically does not enumerate all combinations. So the average-time-per-evaluation discussion seems to mix acquisition evaluation complexity with exhaustive combinatorial search over batches, which is not how the method is implemented. This makes the complexity section feel more decorative than informative. The practical runtime evidence in **Table 1** is actually more useful than the theory section.

7. **The empirical comparisons are too narrow for the paper’s level of claim.**  
   The paper mainly compares against qEHVI and a MOBO-adapted QSVGD. That is thin for a method claiming a new probabilistic acquisition strategy for better Pareto coverage. The related work section itself mentions objective-space coverage-oriented methods such as EMMI and IGD-NS on **Page 3**, yet these do not appear in the experiments. Even if some of these methods are harder to scale or implement in batch mode, the paper needs a clearer argument for why they are omitted, because they are directly relevant to the claim that existing coverage approaches operate in the objective space and have limitations. Without stronger baselines, it is difficult to tell whether the gain comes from the specific proposed idea or simply from adding a repulsion term against previously queried points.

8. **The QSVGD baseline seems under-specified and potentially weakly tuned, which matters because it is the only diversity-aware baseline in the main experiments.**  
   The main paper says on **Page 9** that QSVGD uses a decaying schedule for \(\eta\), and Appendix A.1 says \(\eta_0\) is task-dependent and tuned so the entropy term matches the scale of the hypervolume term. But the main paper does not report the chosen values or the tuning protocol. Since one of the central claims is that the proposed method avoids sensitive hyperparameter tuning, the comparison against a manually scheduled and task-dependent QSVGD baseline is not entirely satisfying. If the baseline is sensitive, then the burden is on the paper to document that tuning carefully and show it is reasonably competitive.

9. **The new EMD metric is useful for this paper’s thesis, but its scope is narrower than the manuscript sometimes suggests.**  
   On **Page 6, Equation (9)**, EMD averages distance from each true Pareto design to the nearest acquired point. This is fine for the discrete candidate-pool settings used in the experiments, especially since Appendix A.1 explains that the true Pareto set is computed by exhaustive evaluation over 10,000 candidates. But in continuous black-box optimization, EMD is not generally available. So as a validation metric, it is appropriate mainly for enumerable benchmark pools or retrospective studies. The paper occasionally talks about EMD as if it were a general MOBO coverage metric, whereas in practice it requires access to the full Pareto set. This should be framed more carefully.

10. **The figures support the paper’s intuition, but they also expose a lack of stronger statistical analysis.**  
   In **Figure 1**, qEHVI-SF indeed appears to dominate on several curves, especially for EMD, but the plots are line summaries without clear uncertainty bands that would let the reader judge the significance of differences over time. The text emphasizes smaller standard deviations, but those are not visually obvious from the main figure. Similarly, **Figure 2** reports mean rediscovery ratios across 20 trials, but the figure format makes it hard to assess variance and significance across methods and batch sizes. Since the paper’s experimental case rests heavily on consistency and robustness across batch sizes, confidence intervals or statistical tests would have materially strengthened the evidence.

11. **Table 1 is less supportive than the text claims in some settings.**  
   The manuscript states on **Page 9** that qEHVI-SF adds minimal overhead. That is true in some cells, but **Table 1** also shows cases where qEHVI-SF is noticeably slower, for example Tri-2 and some \(q=10\) settings, and the standard deviations are very large in several columns for all methods. I am not claiming the runtime story is false, but the presentation is too sweeping. A more accurate takeaway from Table 1 is that qEHVI-SF often has comparable runtime order to qEHVI, but practical cost is noisy and can be materially higher depending on the task.

12. **The paper overstates robustness and generality relative to the evidence.**  
   The main benchmark discussion on **Page 6** explicitly focuses on problems with multiple Pareto-optimal regions in the design space, and Appendix A.2 explains that standard DTLZ/ZDT problems are de-emphasized because they are less favorable for demonstrating the method’s benefit. That is fair as motivation, but it also means the evidence is concentrated on settings chosen to match the proposed inductive bias. So claims such as “general applicability” in the abstract feel too broad. The method may well be useful in the targeted regime of disconnected or spatially dispersed Pareto sets, but the paper should narrow its claims accordingly.

## Questions
1. The main thing I would like clarified is the probabilistic interpretation. Can the authors make precise what quantity is actually being approximated by qEHVI-SF? In particular, what is the exact normalization used to interpret qEHVI as a proxy for \(P(\mathbf{X}\subseteq \mathcal{X}^*)\), and what assumptions connect the distance term in **Equation (8)** to \(P(\mathcal{X}^*\subseteq A'_{\mathbf{X}}\mid \mathbf{X}\subseteq \mathcal{X}^*)\)? A convincing derivation, or a more modest reframing as a heuristic rather than a probability estimator, would increase my confidence.

2. Why is the minimum-distance surrogate in **Equation (8)** the right design choice, as opposed to alternatives such as sum of pairwise distances, covering radius, determinantal criteria, or an explicit union-of-balls proxy? An ablation comparing several coverage surrogates would help determine whether the observed gains are specific to the proposed formulation or just due to adding any repulsive term.

3. Please clarify the exact implementation of “normalized qEHVI” mentioned in **Section 3.2**, since that normalization does not appear in the equations. If this is only a ranking heuristic, say so explicitly.

4. Can the authors provide stronger details for the QSVGD baseline, especially the values of \(\eta_0\), how they were selected per task, and whether the same tuning budget was afforded across methods? This matters for the fairness of the main comparison because QSVGD is the only diversity-aware baseline in the core experiments.

5. Could the authors report uncertainty more explicitly in the main empirical comparisons, for example confidence intervals or standard errors in **Figure 1** and **Figure 2**, and optionally pairwise significance tests for final hypervolume / EMD / rediscovery ratio? The visual trends are suggestive, but stronger statistical evidence would help.

6. Since the work argues that objective-space diversity methods have limitations, it would strengthen the paper to include or at least discuss more directly relevant coverage-oriented MOBO baselines beyond qEHVI and QSVGD. If these methods were infeasible, please explain why concretely.

7. The complexity section would benefit from a more implementation-faithful discussion. Can the authors separate the cost of acquisition evaluation from the cost of acquisition optimization as actually performed in BoTorch, rather than introducing \(\binom{|\mathcal{X}|}{q}\) terms that suggest exhaustive search over batch subsets?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns requiring escalation are apparent from the paper. The materials discovery application is benign in the form presented, and I did not identify privacy, fairness, or human-subject issues in the experiments.

## Soundness Rating
2: fair. The empirical results are suggestive and the implementation appears functional, but the central probabilistic interpretation is not adequately supported, several equations are underspecified or inconsistent, and the baseline comparisons are not strong enough to fully validate the claims.

## Presentation Rating
2: fair. The paper is readable at a high level, but technical exposition is looser than it should be for a method paper, especially around Equations (6) to (8), the Pareto-set notation in Section 2.1, and the mismatch between the conceptual framing and the actual implemented objective.

## Contribution Rating
2: fair. The practical idea of reweighting qEHVI by a design-space repulsion or space-filling term is potentially useful, especially for rediscovery tasks with dispersed Pareto sets, but the paper overstates the conceptual novelty and probabilistic grounding of what is currently a heuristic method.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles a relevant problem and shows promising empirical behavior, but the current version overclaims a probabilistic derivation that is not actually established, and too much of the contribution reduces to a distance-augmented qEHVI heuristic without enough theoretical or empirical support to meet the bar I would expect for ICLR.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially the mismatch between the claimed probability framework and the actual acquisition, the issues in the equations, and the limitations of the empirical validation.