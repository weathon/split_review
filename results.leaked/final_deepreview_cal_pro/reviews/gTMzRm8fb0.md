Now let me compose the final review. I have a thorough understanding of the paper and the calibration anchors.

---

## Summary

GoalRank proposes a training framework for large generator-only ranking models that challenges the prevailing Generator–Evaluator paradigm in recommender systems. The authors first prove (Theorem 1) that a sufficiently large single generator can achieve strictly better approximation to the optimal ranking policy than any finite mixture of small generators with an evaluator, with error approaching zero as model size grows. They then introduce a group-relative optimization principle: a reward model scores a group of candidate lists, intra-group normalization produces a reference policy, and the generator is trained via cross-entropy to match this reference. The method is evaluated on two public datasets, two industrial datasets, and a large-scale online A/B test on a platform with over half a billion users, showing substantial improvements over baselines.

## Strengths

- **Theorem 1 provides a genuine theoretical foundation.** The proof that a larger generator-only model can achieve strictly smaller KL-divergence to the optimal policy than any finite k-mixture of small generators — and that this error can be driven to zero — is a non-trivial result that substantiates the motivation for the generator-only paradigm. The definitions and formalism (Sections 3.1) are clean and properly set up.

- **The group-relative optimization principle is novel and practical.** Constructing a reference policy via intra-group reward normalization (Equation 4: subtract mean, divide by standard deviation, apply softmax) and training the generator to match it (Equation 5) is an original training criterion. Rather than requiring an oracle reward model, it exploits the intuition that within a group of lists with large reward gaps, a biased reward model preserves relative order. This is a creative solution to the problem of training with imperfect reward signals.

- **Strong empirical validation with real-world deployment.** The offline results (Table 1) show consistent, statistically significant improvements over a comprehensive set of baselines across three datasets (e.g., +17.12% H@6 on ML-1M, +25.39% on Industry). The online A/B test (Table 4) on a half-billion-user short-video platform shows gains on App Stay Time, Watch Time, Effective Views, Likes, and Comments — confirming the method works at industrial scale. The ablation on reward model bias (Table 3) demonstrates robustness: even with 50% Gaussian noise injected, GoalRank still outperforms the strongest baselines.

- **Clear empirical scaling behavior.** Figure 3 shows GoalRank's metrics improve steadily from 1M to 0.1B parameters, while all baselines (DNN, RankMixer, PIER, MG-E) show weak or saturating scaling. This provides empirical validation for the capacity argument in Theorem 1.

## Weaknesses

### Fatal

None.

### Major

- **Evaluator usage is asymmetric between GoalRank and baselines, confounding the paradigm comparison.** GoalRank uses the reward model (evaluator) as a training signal — the reference policy is computed from reward scores and the generator is trained to imitate it. The Generator–Evaluator and Multi-Generator–Evaluator baselines use exactly the same evaluator, but only at inference to select among candidate lists; the generators in those baselines are trained with conventional losses (pointwise, pairwise, listwise) never exposed to the evaluator's scores. This means the experiment compares "generator-only trained with evaluator distillation" against "generator(s) trained without evaluator distillation + evaluator selection at inference." The large performance gaps (e.g., +25% H@6 on Industry) cannot be confidently attributed to the generator-only architecture versus the training signal from the evaluator. A controlled baseline where G-E or MG-E generators are also trained to optimize the evaluator's signal (e.g., via RL with the evaluator as reward, or distillation from the evaluator's best list) would disentangle these factors. The paper's claim that the generator-only *paradigm* is superior — as distinct from the claim that the *training method* works — requires this control.

### Minor

- **The claimed "derivation" of the training objective from theory is overstated.** Section 3.2 is presented as deriving the training objective, and the abstract/introduction refer to "deriving an evidence upper bound." In reality, Section 3.2 (a) defines the oracle policy as a Boltzmann distribution over ideal rewards, (b) notes ideal rewards are inaccessible, and (c) proposes that a biased reward model with group-relative normalization can serve as a surrogate when reward gaps within a group are large. There is no formal upper bound or quantitative guarantee connecting the surrogate to the oracle. The reasoning is heuristic and the intra-group normalization (dividing by σ_B in Equation 4) is a plausible design choice, not a derived consequence. This does not invalidate the method — it clearly works — but the paper overstates the theoretical rigor of the transition from Theorem 1 to the training recipe.

- **Missing ablations for key design choices.** The group-relative normalization (subtract mean, divide by standard deviation, softmax) is not compared against simpler alternatives: a standard softmax of raw rewards, a learned temperature, or using the evaluator's hard top-1 ranking as a target. The auxiliary ranking policies that populate the groups are described only as delegated to the appendix; their contribution is not ablated (e.g., what happens with random lists, with a single generator's lists, or with no auxiliary policies). Table 2 ablates group size and Table 3 ablates reward model bias, but neither isolates whether the specific normalization formula in Equation 4 matters relative to alternatives.

- **"Scaling law" language is used loosely.** The paper shows that performance improves with model size, which is expected for deep models and is valuable to demonstrate. However, calling this a "scaling law" without fitting a functional form or showing predictive power stretches the term. The empirical trend in Figure 3 is better described as "scaling behavior" or "monotonic improvement with model size."

### Trivial

None that are worth listing.

## Nice-to-Haves

- Scaling the evaluator alongside generators in the MG-E scaling experiment (Figure 3) would strengthen the comparison, since the evaluator may be the bottleneck in the ensemble setting.
- Reporting standard deviations or confidence intervals explicitly for all offline metrics, rather than only noting that differences are significant (p < 0.05), would help readers assess result reliability.
- An error analysis of the reward model's calibration and predictive quality would strengthen the practical story, since the entire training method depends on it.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic point about "Plausibility of extremely large offline gains" as a standalone concern:** This was speculative — the critic suggested baselines might be under-tuned without evidence. The paper reports statistical significance (p < 0.05) and averages over 5 runs. Without concrete evidence of under-tuning, this concern does not stand on its own. It is partially subsumed by the (retained) Major weakness about evaluator asymmetry.

- **Harsh Critic point about "Ensemble comparison for scaling experiment" demanding evaluator scaling:** This is a reasonable suggestion, not a flaw. Moved to Nice-to-Haves.

- **Harsh Critic point about "missing appendix / unavailable appendix":** The parser strips appendices; the original submission has them. Removed.

- **Harsh Critic point about "Variance and statistical rigor":** The paper does report p < 0.05 and 5-run averages. Requesting explicit standard deviations is reasonable but moved to Nice-to-Haves as it does not threaten the core claims.

## Novel Insights

The paper's framing of ranking as minimizing KL-divergence to an optimal policy — and the observation that a biased reward model can still provide useful training signal through group-relative normalization when reward gaps are large — is a genuinely useful perspective. It connects ranking to policy optimization in a way that opens the door to using techniques from RLHF (reference policies, KL minimization) for recommender ranking, which is a productive cross-pollination. The capacity argument (Theorem 1) that a single large model can outperform a mixture of small models, while not entirely surprising given universal approximation theory, is formalized here in a ranking-specific way that gives it practical teeth.

## Suggestions

- The paper would be substantially strengthened by adding a baseline where MG-E generators are trained to optimize the evaluator's signal (e.g., via policy gradient with the evaluator as reward, or by distilling the evaluator's best-ranked list). This single addition would separate the effect of the training signal from the effect of the architecture, clarifying what the group-relative design specifically contributes.
- Reframe Section 3.2 honestly: acknowledge that the recipe is a practically motivated heuristic, not a derived consequence of Theorem 1, and drop the "evidence upper bound" language unless a formal bound is provided.
- Add an ablation comparing Equation 4 against at least a standard softmax of raw rewards — this would demonstrate whether the group-relative normalization is actually pulling weight.

## Score and Decision

**Round 1 bracket:** 6.5–8.0, based on comparison against:
- `sb1HgVDLjN` (6.67, Offline MBO by Learning to Rank): GoalRank is clearly stronger — more substantial theory, broader empirical validation including online A/B test.
- `rfdblE10qm` (8.00, Rethinking Reward Modeling): GoalRank is slightly weaker — the 8.00 paper has tighter theory-practice connection and fewer gaps.

**Round 2 narrowing within bracket:**
- `yarUvgEXq3` (7.33, Safe Collaborative Filtering): GoalRank is comparable. Both have strong theoretical and empirical contributions. GoalRank has the advantage of production deployment and a more ambitious scope; Safe CF has cleaner theory-practice alignment.
- `l0fn10vSyM` (7.00, Semi-Parametric Retrieval): GoalRank is stronger, with more novel theory and more convincing empirical validation.
- `sb1HgVDLjN` (6.67): GoalRank is clearly stronger.
- `HZVIQE1MsJ` (6.50, Learning Generative Judge): GoalRank is clearly stronger.

GoalRank sits at the intersection: it has the production validation and theoretical ambition that distinguish it from typical 6.5–7.0 papers, but the overclaimed theoretical derivation and missing controlled baselines keep it from the 8.0 tier where every component is tightly justified. I settle at **7.0** — an accept with real contributions that would benefit from the revisions outlined above.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>