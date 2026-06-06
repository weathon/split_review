## Summary

GoalRank is a generator-only ranking framework for industrial recommender systems, trained with group-relative reward optimization. The paper (1) theoretically proves that a sufficiently large single generator outperforms any finite Multi-Generator–Evaluator (MG-E) system in KL approximation error, (2) derives a group-relative training objective from an entropy-regularized oracle policy, and (3) validates the framework with offline benchmarks and large-scale online A/B tests on a 500M+ DAU platform.

---

## Strengths

- **Production-scale A/B validation**: Table 4 reports statistically significant improvements across all five business metrics (App Stay Time +0.149%, Watch Time +0.197%, Effective View +1.212%, Like +0.227%, Comment +0.802%) when GoalRank fully replaces the production MG-E system, which runs tens of generators and evaluates hundreds of candidate lists. This is the paper's most compelling result — GoalRank + MG-E has been deployed to the full user traffic.

- **Comprehensive offline gains across three diverse datasets**: Table 1 shows GoalRank outperforming all baselines (generator-only, G-E, and MG-E) across five metrics on ML-1M, Amazon-Book, and the Industry dataset, with improvements statistically significant at p < 0.05 over five independent runs. The consistency across datasets and metrics reduces the probability of cherry-picking.

- **Empirical scaling behavior**: Figure 3 demonstrates monotonically increasing performance for GoalRank from 1M to 0.1B parameters across all four metrics on Industry-0.1B, while baselines (DNN, RankMixer, PIER, MG-E) plateau or saturate. This directly supports the theoretical prediction about model size.

- **Robustness of the group-relative mechanism**: Tables 2 and 3 confirm that GoalRank remains above all baselines even at suboptimal group sizes (|ℬ| = 3 or 100 vs. optimal 8–20) and even under heavy reward noise (λ = 0.5), providing reassuring evidence of practical robustness.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained offline–online gap**: GoalRank achieves +25% H@6 offline (Industry dataset) yet only +0.149% Watch Time online. While the online gains are real and significant at platform scale, a gap of this magnitude is substantial and informative. Common causes include distribution shift, the fact that offline labels are derived from an MF-based retriever (biasing ground-truth toward MF-compatible items), or reward model overfitting to the offline signal. The paper presents both results side by side (Tables 1 and 4) without any discussion of this discrepancy, which is arguably the most informative diagnostic in the paper. Understanding *why* massive offline improvements compress to small online lifts would substantially increase the credibility of both sets of results.

- **Unexplained AUC anomaly in MG-E rows**: In Table 1, as the number of generators increases from 3 to 100, AUC *falls* substantially on ML-1M (G-3: 60.73, G-20: 81.76, G-100: 76.48), while single-generator models achieve AUC of 86.87–92.47. This counter-intuitive pattern — more generators degrading AUC even as hit-ratio metrics improve — is not explained anywhere. It likely reflects a metric–architecture mismatch (AUC may be computed over a different item space than H@6), but the omission of any discussion is a gap that undermines the credibility of the MG-E baseline characterization.

### Minor

- **"Evidence upper bound" is standard MaxEnt RL duality**: The derivation in Section 3.2 shows that τ log Z = sup_π {𝔼[r] + τH(π)}, which is a textbook result in the soft actor-critic / maximum-entropy RL literature. The paper presents this as a novel "evidence upper bound of the one-stage optimization objective," but it is simply the free-energy identity from entropy-regularized MDPs. The group-relative normalization in Eq. (4) is the genuine practical contribution; the surrounding derivation is oversold as a new bounding result. The paper should either clarify what is new in this derivation or reframe it honestly as motivation. Additionally, the group-relative policy normalization closely parallels Group Relative Policy Optimization (GRPO), a connection not acknowledged.

- **Theorem 1 is an existence result at unlimited capacity, not a fixed-compute argument**: The theorem states that for any k-mixture of generators with width ≤ α, *there exists* a larger generator with width ≥ kα + n that achieves strictly smaller KL error. This is essentially universal approximation applied to the policy space. It does not address the practically relevant question of whether, at a fixed compute/parameter budget, a single generator beats a MG-E system of equivalent size. The paper frames the theorem in Sections 1, 3.1, and 5 as the "theoretical foundation" proving generator-only superiority, when it proves only that an arbitrarily large generator can be superior in principle. The empirical evidence is far stronger than the theorem, and the paper would benefit from more precisely scoping what the theorem does and does not establish.

- **GoalRank architecture in Table 1 not stated in the main text**: The main text says "the hidden embedding dimension of all models is fixed at 128," which strongly implies GoalRank also uses 128 dimensions for Table 1. However, the specific architecture (layers, attention heads, parameter count) is deferred to Appendix D.2, which is not accessible in the reviewed version. Given the scale of the improvements (+25–30%), the comparison fairness hinges on this detail being confirmed in the main text — a single sentence stating GoalRank's parameter count for Table 1 would resolve this.

- **The σ* threshold (Eq. 3) is never empirically analyzed**: Section 3.2 introduces a threshold σ* under which the biased reward model preserves the ordering of lists, and states this condition motivates using auxiliary policies. Neither the threshold nor the empirical frequency with which the condition is satisfied are reported anywhere. This is not fatal — the ablations in Table 2 provide indirect evidence — but the gap between the theoretical condition and practical validation is notable.

### Trivial

- Using "scaling law" to describe monotonically increasing performance from 1M to 0.1B parameters (Figure 3) is terminologically imprecise. A scaling law conventionally implies a power-law fit over compute or parameters; the paper does not fit or report such a relationship. This does not change the substance but may attract criticism from reviewers with a strict interpretation.

---

## Nice-to-Haves

- **Ablation isolating group-relative normalization**: The current ablations vary group size (Table 2) and reward noise (Table 3). Neither isolates what group-relative normalization specifically contributes versus simply training with reward-weighted cross-entropy without within-group standardization. Adding a "reward-weighted training, no normalization" ablation would directly establish the value of the core mechanism.

- **Discussion of offline–online gap**: Even a brief discussion of why offline gains compress online (e.g., retrieval set distribution shift, MF-based ground truth) would strengthen the paper and help practitioners interpret their own offline evaluations.

- **Training stability of non-stationary group construction**: Including l_u^θ in the group alongside auxiliary policies creates a mild non-stationarity (since l_u^θ changes as θ is updated). A brief statement on training stability (loss curves, convergence) would address this.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **"Missing related works" (GRPO/DeepSeek-R1 connection)**: The harsh critic identifies a potential connection to GRPO that is not cited. Per reviewer guidelines, absence of a specific related work citation cannot be flagged without confirmation that it was omitted versus in-scope; removed as it could be a missing-citation complaint.

- **Strength Finder: "Theorem 1 provides novel theoretical justification for generator-only superiority"**: Conflict with verified Minor weakness; per filtering rules, the weakness wins. Theorem 1 is a valid capacity result, but it is not as structurally novel as the Strength Finder implies.

- **Strength Finder: "The insight that large reward gaps make relative ordering robust to bias is novel and practical"**: This insight is real and useful, but not independently novel from the group-relative construction — merged into the general strengths paragraph rather than listed as a distinct strength.

- **Harsh Critic's comment on "non-stationary training signal"**: A valid observation, but on-policy RL methods routinely include the current policy's outputs in the training distribution, and the paper partially addresses this by describing group construction (Section 3.3). Demoted to Nice-to-Have.

---

## Novel Insights

GoalRank's most interesting empirical observation — which neither reviewer fully surfaced — is the *differential scaling* behavior in Figure 3: GoalRank benefits dramatically from going from 10M to 0.1B parameters, while baselines essentially saturate. This suggests that group-relative training does not just improve performance at a given scale but *unlocks* a steeper scaling trajectory. If confirmed, this differential scaling is more consequential than the performance gap at any fixed scale. The implication is that the group-relative training objective acts as a better-conditioned loss landscape for large-scale optimization, not merely a better reward signal. This interpretation warrants direct investigation in future work.

---

## Suggestions

1. Add a one-paragraph discussion in Section 4.2 on the offline–online gap, proposing candidate explanations and their implications for metric design in industrial ranking papers.
2. State GoalRank's parameter count for Table 1 experiments explicitly in the main text, alongside the note that baselines also use 128-dimensional embeddings.
3. Reframe the "evidence upper bound" derivation in Section 3.2 honestly as an entropy-regularized RL objective (acknowledging the standard result), then position the group-relative construction as the practical novelty that makes this objective tractable under biased reward models.
4. Restate Theorem 1's scope precisely: it establishes that generator-only models are *expressively at least as powerful* as MG-E given sufficient width, not that they are superior at comparable compute. The empirical evidence, not the theorem, is what supports the latter claim.
5. Report a power-law fit (or explicitly acknowledge it cannot be fitted) for the scaling curves in Figure 3, to substantiate the "scaling law" claim.

---

## Score and Decision

**Originality** (3/5): The group-relative optimization principle is a meaningful engineering contribution, adapting MaxEnt RL ideas to the list-ranking setting. The theoretical framing adds some structure but is not deeply novel.

**Importance** (4/5): Industrial ranking at this scale is a high-impact problem, and the production deployment makes the contribution real.

**Claims supported** (3/5): Offline claims are well-supported within the stated experimental setup; online claims are supported but modest; theoretical claims partially overstate the theorem's implications.

**Soundness** (3/5): The training objective is sound; the theory is correct but limited in scope; the offline–online discrepancy is unexplained.

**Clarity** (3/5): Generally clear, but the "evidence upper bound" framing and "scaling law" terminology introduce imprecision.

**Community value** (4/5): A deployed system with positive A/B results and scaling experiments provides a useful reference point for practitioners and researchers in industrial ranking.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>