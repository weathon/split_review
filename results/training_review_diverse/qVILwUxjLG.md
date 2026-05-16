Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces Neural Predictive Ensemble Sampling (NeuralPES), a scalable deep neural network-based contextual bandit algorithm for non-stationary environments. The algorithm combines three ensembles — reward models, sequence models (which predict future reward model parameters), and predictive models — to strategically prioritize the acquisition of information with lasting value. The paper provides regret bounds for a linearized version (LinPS) showing that the algorithm's exploration naturally avoids investing in transient information, and validates the approach empirically on an AR(1) synthetic environment and two real-world recommendation datasets (MIND, KuaiRec), where NeuralPES significantly outperforms neural bandit baselines and their sliding-window variants.

## Strengths

1. **Novel algorithm design that explicitly targets lasting-information seeking at scale.** NeuralPES is the first algorithm to combine deep neural network-based scaling with a principled exploration mechanism designed for non-stationary environments (Section 4, Algorithm 2). The three-ensemble architecture (reward, sequence, predictive models) is clearly motivated and differentiated from prior heuristic methods that simply discount or window past data. The theoretical intuition (Section 4.4.1) — that targeting θ_{t+2} rather than θ_{t+1} strategically prioritizes enduring information — provides a clean conceptual grounding.

2. **Theoretical regret bounds that quantitatively connect algorithm design to information durability.** Theorem 1 and Corollaries 1–2 provide upper bounds on the regret of LinPS (the linearized version) under abrupt-change and AR(1) models. The bounds smoothly interpolate between the stationary TS bound (when changes are absent) and a vanishing bound (when parameters are redrawn each step), formally confirming that LinPS stops investing in transient information. This goes beyond the heuristic discounting/windowing of prior non-stationary methods and directly supports the algorithm's design rationale.

3. **Strong and consistent empirical results on real-world datasets.** Table 1 shows NeuralPES achieving the highest average reward/CTR/rating across all three experiments (AR(1) logistic: 0.5850 ± 0.0023; MIND 1-week CTR: 0.1552 ± 0.0013; KuaiRec 2-month rating: 1.3421 ± 0.0016), outperforming all six baselines including sliding-window variants designed for non-stationarity. The experiments span 1 week and 2 months of real user interaction data, demonstrating both relevance and longevity of the advantage. The MIND experiment (Figure 3b,c) shows adaptation to day-of-week seasonality, while the KuaiRec experiment (Figure 4) shows sustained advantage.

4. **Computation-aware design.** The paper explicitly avoids the matrix inversion required by Neural UCB/Neural TS (Section 5), making the algorithm feasible with modern architectures on a single A100 GPU. This practical consideration is meaningful for deployment.

5. **Informative ablation studies.** Figure 5 shows that removing the predictive model (Neural Sequence Ensemble) causes performance collapse, and that the regularization term (Equation 6) for addressing loss of plasticity is critical — providing clear evidence that both components are essential to the algorithm's success.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Overclaimed interpretation of regret bounds in the i.i.d. limit.** The paper states (line 381) "then the regret of LinPS is zero that LinPS achieves optimal" and (line 431) "achieves 0 regret and is such optimal" when θ_t is i.i.d. or changes every step. While this conclusion *does* follow mathematically from the stated Theorem 1 bound (which becomes Regret(T) ≤ 0, hence Regret(T) = 0), the bound itself relies on information-theoretic techniques (Russo & Van Roy 2016, Liu et al. 2022) that capture the *cost of learning* but may not capture the irreducible one-step prediction error in such rapidly-changing environments. The practical claim of "optimal" is thus stronger than the bound can support. The authors should either (a) clarify that the bound captures information-theoretic regret from learning about future parameters, which is zero when there is nothing to learn, and that this does not mean the algorithm incurs zero *actual* regret, or (b) qualify "optimal" as meaning "optimal with respect to the bound's scope." This does not undermine the algorithm's empirical success or its theoretical grounding, but the presentation oversells the result.

2. **Missing experimental comparison with predictive sampling (Liu et al. 2023).** The paper frames NeuralPES as addressing the scalability limitations of predictive sampling — the direct predecessor that also seeks lasting information. Yet no experimental comparison is provided, even on the synthetic AR(1) setting where predictive sampling might be computationally tractable. While the paper's primary empirical contribution is demonstrating scalability (by comparing against scalable neural baselines), a direct comparison on a small-scale version would help substantiate the claim that NeuralPES retains predictive sampling's information-seeking property while scaling. As it stands, the reader must take this on faith from the theory.

3. **Practical considerations not discussed.** The algorithm requires storing historical last-layer weights w_{m,1:t-1} for each particle (used by TrainSequenceNN and TrainPredictiveNN). This memory cost grows linearly with time and is not discussed. Additionally, several hyperparameters (M, L, τ, τ_seq, τ_pred, K, K') are introduced without sensitivity analysis, and the paper does not report wall-clock time or computational overhead relative to baselines. These are standard practical concerns that could affect deployment decisions.

4. **Justification for two-step-ahead prediction.** The algorithm predicts two steps ahead (θ_{t+2}) via the sequence model and trains the predictive model using w_{m,j+2}. The paper provides some intuition (Section 4.4.1: "θ_{t+2} better represents valuable information"), but a more explicit theoretical or empirical argument for two steps versus one would strengthen the presentation.

### Trivial
- None.

## Nice-to-Haves

- A direct comparison with predictive sampling on a small-scale synthetic experiment, even if only on the AR(1) logistic setting with reduced dimensionality, would strengthen the central thesis.
- Hyperparameter sensitivity analysis on M (ensemble size) and L (sequence length) would improve reproducibility guidance.
- Cumulative regret curves (in addition to the running average figures) would provide a different lens on the results.
- A brief wall-clock time comparison with baselines would help practitioners assess the computational trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Misleading interpretation of the regret bound — the bound being zero does not imply the algorithm actually incurs zero regret."** Removed because this claim is mathematically incorrect: if a proven upper bound says Regret(T) ≤ 0 and regret is non-negative by definition, then Regret(T) = 0 follows. The real issue is whether the bound's scope captures all sources of regret (upgraded to Minor above as an interpretive overclaim). 
2. **"The evaluation protocol for KuaiRec may suffer from counterfactual bias."** Removed because KuaiRec (Gao et al. 2022) is a well-known full-interaction dataset providing ratings for nearly all user-item pairs in the observed windows. The paper states "set of videos alongside with their corresponding ratings," consistent with this property. The critic's concern stems from a misunderstanding of the dataset.
3. **"Figure 1 caption issue — spoiler figure referenced before algorithm defined."** Removed as a format/style nitpick. Teaser figures are standard practice in ML papers.
4. **"The paper reports only average performance at the end of the experiment."** Removed as factually inaccurate. The paper provides figures showing performance over time (Figure 3a–e).
5. **"The literature review could be more precise / missing non-stationary neural methods."** The critic acknowledges "if there are none, that is fine," making this not a genuine weakness.
6. **Strength Finder claim about computational practicality** — kept but downgraded from standalone strength to a supporting note; it's addressed adequately in the paper.
7. **"The theoretical novelty is limited to framing"** (from Section-by-Section). Removed as a subjective negative framing of what is a standard way of building on prior proof techniques; the corollaries are new and non-trivial.

## Novel Insights

The reviewers raise an interesting tension that the paper does not fully resolve. The bound says zero regret when θ_t is i.i.d., but intuitively, a learner faced with completely unpredictable parameters should still incur positive regret from guessing. The resolution — that the bound captures the *learning* component of regret but not the irreducible prediction error from a stochastic environment — is implicitly present in the information-theoretic framework (Russo & Van Roy 2016) but the paper glosses over this subtlety. This suggests a general caveat for information-theoretic regret bounds in non-stationary settings: they primarily measure the efficiency of *adaptation*, not the absolute performance ceiling.

## Suggestions

1. In the theoretical discussion (lines 381, 431), replace "achieves 0 regret and is such optimal" with something like: "the information-theoretic component of regret vanishes, indicating that LinPS does not waste effort on transient information." Add a sentence noting that this does not imply zero *actual* regret since the irreducible one-step prediction error is outside the bound's scope.
2. Add a small-scale comparison against predictive sampling on the AR(1) logistic experiment, even if only for a short horizon, to empirically verify that NeuralPES retains the information-seeking behavior of its predecessor.
3. Briefly discuss the memory cost of storing w_{m,1:t-1} and note whether this poses a practical bottleneck.
4. Provide a brief intuitive justification for why two-step-ahead (rather than one-step) is the right choice — e.g., a small ablation or a theoretical argument that two steps is sufficient to filter transient noise in the parameter process.

## Score and Decision

The paper makes a genuine contribution: a scalable neural bandit algorithm with a principled exploration mechanism for non-stationary environments, supported by theoretical analysis and strong empirical results on real-world data. The identified weaknesses are minor — interpretive caution in the theory, a missing-but-not-fatal comparison, and some practical documentation gaps. None undermine the core contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>