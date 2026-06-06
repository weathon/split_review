## Summary
This paper re-evaluates OOD generalization claims for programmatic policies across three benchmarks (TORCS, Karel, Parking), arguing that the observed advantage of programmatic over neural policies stems from experimental confounds (aggressive reward functions and full observability) rather than intrinsic representational differences. It proposes a conceptual framework (expressivity + discoverability) and identifies a principled boundary — tasks requiring instance-scaling working memory — where programmatic representations genuinely outperform fixed-capacity neural architectures, illustrated via a FUNSEARCH proof-of-concept synthesizing a BFS policy.

---

## Strengths

- **TORCS reward confound (Table 1):** Reducing the speed coefficient β from 1.0 to 0.5 allows DRL policies to generalize to unseen race tracks (76% on G-TRACK-1, 69% on AALBORG) where they previously failed completely. This is a concrete, specific finding: a single reward hyperparameter accounts for the originally reported neural-programmatic gap.

- **Karel PPO+a_{t−1} result (Table 2):** A feedforward policy augmented solely with the agent's last action generalizes to 100×100 grids on STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER, while fully observable ConvNet and LSTM baselines fail. The contrast is stark (e.g., 1.00/1.00/1.00/1.00 at 100×100 vs. 0.00/0.00/0.01/0.00 for ConvNet), making this the paper's strongest empirical contribution.

- **Working memory boundary (Section 5):** The argument that exact pathfinding requires Θ(|V|) memory, which indexing vertices requires Ω(log|V|) bits, and that fixed-capacity neural architectures cannot therefore generalize OOD on such tasks is principled and substantive. This is the paper's most original theoretical contribution.

- **Expressivity/discoverability framework (Section 2–5):** Definitions 2 and 3 provide a structured vocabulary for analyzing the source of generalization gaps, and the paper uses it coherently to interpret all three benchmarks — a useful conceptual advance for the field.

---

## Weaknesses

### Fatal
None.

### Major

- **Parking results undercut the headline claim.** The abstract states neural policies "can match or exceed" OOD generalization of programmatic ones, but Parking (Section 4.3) is the clearest counterexample in the paper's own data. PSM degrades from 0.26 to 0.16 success rate (a drop of 0.10), while DQN degrades from 0.86 to 0.18 (a drop of 0.68). By the "Successful-on-100" metric, PSM has 2/30 models that reliably generalize; DQN has 0/15. The paper acknowledges this but frames it as "challenging for both," pivoting to the claim that DQN achieves a marginally higher average test success rate (0.18 vs. 0.16). This framing is not analytically satisfying: on the metric most relevant to the paper's claim (systematic OOD generalization), PSM fares substantially better. The paper does not attempt any training modifications to close this gap (e.g., different reward shaping, curriculum), and the expressivity/discoverability framework is not used to explain *why* neural policies fail here. This should be addressed head-on — either via new experiments or by clearly reframing Parking as a domain that motivates the working-memory analysis, rather than presenting it as a near-tie.

- **Karel "fix" qualitatively changes the observation space.** The paper frames restricting the agent to local (adjacent-cell) observations as removing "spurious correlations" from full observability. But switching from full observability (as LEAPS uses) to partial observability changes the problem class: the partial-observability setting is a different POMDP. The result that PPO+a_{t−1} generalizes well is demonstrated on this different, structurally easier task, not the original benchmark. The paper's conclusion — that neural policies can match programmatic ones in Karel — is valid only under weaker observability than the original comparison. This distinction should be made explicit, and the claim should be scoped accordingly.

### Minor

- **Asymmetric sampling in TORCS.** Among seeds run with DRL(β=0.5), only 13/30 and 4/15 successfully learn the training task; generalization fractions are computed only over these subsets. By contrast, NDPS results from Verma et al. use 3 seeds, all of which generalize. The paper does not flag this asymmetry. A 76% generalization rate among the ~43% of seeds that learned the training task is a weaker result than it appears and deserves a caveat.

- **LSTM failure in Karel left unexplained.** The paper observes that LSTM "often also fails to learn how to solve even the smaller problems" (Section 4.2) but offers no analysis. The contrast between LSTM's collapse and the simple last-action augmentation's success is the most intriguing empirical finding in the Karel section, yet no mechanism is investigated (optimization difficulty? overfitting to full observations?). Adding even a brief diagnostic would significantly strengthen the narrative.

- **Expressivity equivalence for TORCS is asserted, not demonstrated.** The claim that the TORCS DSL and ReLU networks induce comparable function classes is stated informally in Section 5 with reference to Orfanos & Lelis (2023). Whether the approximation argument applies to the exact conditional structure of the TORCS language is not demonstrated. Since expressivity equivalence is load-bearing for the claim that the TORCS gap is purely discoverability-driven, a more careful treatment would help.

### Trivial

- The conjecture in Section 4.4 — "NDPS and PROPEL would not generalize to OOD problems if they could find better optimized policies" — is presented as an explanatory remark but is never tested. It could be labeled explicitly as a conjecture or moved to future work.

---

## Nice-to-Haves

- Test whether NDPS still generalizes under β=0.5: if NDPS with the cautious reward generalizes at the same rate as with β=1.0, the reward change alone does not explain why NDPS succeeded — it only explains why DRL failed. This control would sharpen the discoverability argument considerably.
- For the Parking domain, systematically vary training conditions (reward shaping, sparse observations, curriculum) to test whether the PSM–DQN gap can be closed. A null result would itself be valuable, motivating the working-memory analysis in Section 5.
- Report FUNSEARCH's total run count and failure rate for the BFS experiment, not just "three successful runs." Even a single-task proof-of-concept benefits from knowing how reliable the synthesis process is.
- The working-memory argument is compelling for *exact* generalization. Clarify whether approximate generalization (e.g., near-optimal performance on larger instances without provable correctness) is also excluded for fixed-capacity architectures, as this matters for benchmarks like NetHack where human-level approximate play is the practical target.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

- **"β changes the problem, not just learning" (Harsh Critic):** The critic argues that changing β changes the objective the agent optimizes, making it a different problem. However, the paper's response — that the test metric does not reward speed, only track completion, so β=0.5 is a better-aligned training objective — is a reasonable rebuttal. The spirit of the TORCS benchmark is track-following generalization, not speed maximization. Demoted to a minor framing quibble, not retained as a weakness.

- **FunSearch proof-of-concept is too thin (Harsh Critic):** Partially valid (see Minor section on missing failure rate), but the core critique — that BFS's provable correctness is a property of BFS, not of FUNSEARCH — is somewhat unfair. The paper is clear that the proof-of-concept demonstrates *synthesis*, not guarantees about the synthesis process itself. The main substance of this criticism is absorbed into the nice-to-have about reporting failure rates.

- **Strength Finder: Parking as "near-tie":** The claim that "DQN achieves a higher average success rate on the test set (0.18 vs. 0.16)" is technically true but misleading as a strength. Given that DQN drops from 0.86 to 0.18 while PSM drops from 0.26 to 0.16, and that DQN has 0/15 reliable generalizers vs. PSM's 2/30, the Parking result is at best neutral for the paper's argument. This specific framing of Parking as a strength is removed.

- **Harsh Critic on missing control (β=0.5 for NDPS):** This is elevated to a Nice-to-Have rather than a weakness, as the paper's scope is re-evaluation, not exhaustive ablation design.

- **Harsh Critic: "working memory argument applies only to exact pathfinding":** Valid as a scope clarification but absorbed into Nice-to-Haves; it is not a flaw in what the paper actually claims.

---

## Novel Insights

The paper's most genuinely novel insight is that the programmatic-vs-neural OOD generalization comparison in prior work was confounded at the *discoverability* level, not the *expressivity* level. This means that the real question — when do programmatic representations provide an inherent advantage — had not yet been studied. The paper then provides a principled answer grounded in computational complexity: fixed-capacity neural architectures cannot express solutions to problems whose working memory requirements grow with input size, and this is not merely a practical limitation but a structural one. Framing the generalization debate through expressivity and discoverability, and then locating the genuine boundary in instance-scaling memory requirements, is a conceptual contribution that is applicable beyond the three specific benchmarks studied.

---

## Suggestions

1. **Reframe Parking explicitly.** Present the Parking result as a finding that motivates Section 5 — "here is a case where the confound explanation is insufficient, suggesting representational differences are at play" — rather than implying a near-tie that doesn't exist by the paper's own metrics.
2. **Run the NDPS-β=0.5 control.** This costs little experimentally and would either strengthen or sharpen the discoverability argument.
3. **Scope the Karel claim.** Add a sentence explicitly noting that PPO+a_{t−1} is evaluated under partial observability, which was not the setting in LEAPS, and that this reflects both a confound removal and a task reformulation.
4. **Add failure-rate data for FUNSEARCH.** Even a table with total runs and success rate over all runs would substantially strengthen the proof-of-concept.
5. **Mechanistically analyze LSTM failure.** Visualize what input features the LSTM attends to on small grids, or ablate which training conditions lead to failure, to turn a descriptive result into an explanatory one.

---

## Assessment on Key Axes

- **Originality:** Moderate-to-good. Re-evaluation papers are inherently derivative, but the expressivity/discoverability framework and the working-memory boundary are original contributions. The Karel and TORCS findings are genuinely novel despite being about prior work.
- **Importance:** High. If the field's understanding of why programmatic policies generalize is systematically wrong, correcting it matters.
- **Claims supported:** Partially. TORCS and Karel claims are reasonably supported (with caveats about Karel's changed observability). The headline "match or exceed" claim is not supported for Parking.
- **Soundness of experiments:** Moderate. Real methodological concerns in TORCS (asymmetric sampling), and the Karel fix is more than a mere pipeline adjustment.
- **Clarity:** Good overall; the expressivity/discoverability framework is well-explained, though its connection to individual experiments could be made more explicit.
- **Value to the research community:** Moderate-to-high. The re-evaluation findings and the principled boundary around working memory are directly actionable for researchers in programmatic RL.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>