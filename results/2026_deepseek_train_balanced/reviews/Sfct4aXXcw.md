## Summary
The paper introduces RRPO (Reward-Rational Partial Orderings), a theoretical framework that interprets human feedback as Boltzmann-rational partial orderings over trajectories, generalizing the RRC framework to be practical for high-dimensional settings. From this, the authors derive LEOPARD, an algorithm that simultaneously learns from preferences, positive/negative demonstrations, and demonstration rankings. Experiments on four Gymnasium environments compare LEOPARD against AILP and a DeepIRL+RLHF pipeline.

## Strengths
- **RRPO overcomes a key limitation of RRC** — Unlike RRC, which requires optimizing over the entire trajectory space for demonstration feedback, RRPO operates only over directly-accessible trajectories (Section 3.1, Eq. 5, and Section 6.1). This is a genuine practical improvement that makes the framework applicable to general, high-dimensional settings where the trajectory manifold is unknown.
- **LEOPARD outperforms the standard pipeline across all four environments** — Figure 2 shows that when both preferences and positive demonstrations are available, LEOPARD achieves higher ground-truth reward than "DeepIRL then RLHF" in every environment tested, and beats AILP on three of four. The method also supports negative demonstrations and rankings that baselines cannot handle.
- **Theoretical guarantee on loss minimization** — The paper proves (line 129) that when the RRPO loss is below log(2), all reward differences between ordered trajectory fragments must have the correct sign. This is a clean analytical property absent from methods like DeepIRL, whose maximum-entropy loss is unbounded from below (Section 4).
- **Demonstration ranking exploitation without domain-specific assumptions** — LEOPARD exploits relative rankings of demonstrations without requiring domain-specific properties such as inverse kinematics models, unlike prior methods like Mehta & Losey (2023) (Section 6.1).

## Weaknesses

### Major

1. **Synthetic-only evaluation misaligned with human-feedback framing** — The paper consistently frames the method as learning from "human data" and "human feedback" (abstract, introduction, contributions). However, all experiments (Section 4, line 153) use synthetic feedback generated from the ground truth reward function: preferences sampled using the sigmoid of the ground truth reward difference, and demonstrations from agents trained on the ground truth reward with rankings determined by it. There is no human-in-the-loop evaluation, no injected noise, no robustness study against human-like inconsistencies or cognitive biases. This means the experiments primarily demonstrate internal consistency (can the method recover a reward from clean signals produced by that same reward?) rather than practical applicability with real human feedback. The Limitations section (6.2) does not identify this as a core limitation. While synthetic evaluation is common in reward learning, the paper's rhetorical framing — including claims of applicability to "LLM / foundation-model finetuning" and "high dimensional robotics" (line 225) — overstates what the evidence supports.

2. **Asymmetric outlier removal on Cliff Walking** — The paper discloses (line 195) that 25% of AILP runs and 28% of DeepIRL→RLHF runs on Cliff Walking were removed as outliers due to catastrophic cliff falls. No mention is made of whether any LEOPARD runs were similarly excluded. When a quarter to a third of baseline runs are removed and the central claim is that LEOPARD outperforms baselines, this asymmetry can fully determine that outcome. Standard practice would be to report results both with and without outliers, or to use robust statistics (e.g., median). The catastrophic failures themselves are informative about baseline robustness, and discarding them without symmetric treatment weakens the comparison.

3. **Mixed evidence for the multi-feedback superiority claim** — Contribution 3 states that "learning from many types of feedback can be superior to focussing on only one." The paper's own results are equivocal: on Half Cheetah, "training only on preferences was better than using a full feedback mixture" (line 200). On Lunar Lander, "error bars there are large, and we caution against drawing clear conclusions." On Ant, "both setups involving negative demonstrations did poorly." The claim itself is hedged ("can be") but the contributions list presents it as a headline finding. The evidence supports at most that some feedback mixtures help on some environments under specific conditions, not a general claim about multi-type feedback superiority.

### Minor

4. **DeepIRL hyperparameter handling creates asymmetric comparison** — The paper notes that DeepIRL's "reward model training epochs" is difficult to tune and provides sensitivity analysis in the appendix. LEOPARD avoids this hyperparameter but has its own tuning knobs (rationality coefficients β, number of gradient steps per iteration) that are not explored with comparable depth. The asymmetry in hyperparameter treatment favors the proposed method.

5. **Rationality coefficient β is underspecified** — The paper introduces β_j (line 123) as a critical parameter controlling how sharply ordering violations are penalized. It states β values should be equal for the same feedback type but does not discuss how they are set (learned, fixed, or tuned), what values were used in experiments, or how sensitive results are to their choice. Different β values could significantly change which method performs best.

6. **Computational complexity unaddressed** — The RRPO loss (Equation 5) involves a product over (trajectory × partial ordering) pairs, i.e., O(|D| × |C|). With multiple feedback types and agent trajectories accumulating over iterations, this could scale poorly relative to baselines. The paper notes that sparse partial orderings make many terms unity (line 123) but does not report training time or discuss scaling behavior.

7. **Statistical reporting lacks seed counts and numerical tables** — Results are presented only as line plots with shaded standard errors (Figures 2–4), without tables of final numerical values or an explicit statement of the number of seeds/repetitions per condition in the main text. This makes it difficult to precisely compare final performance across methods.

### Trivial

None.

## Nice-to-Haves
- **Noise/robustness ablation**: Even without human data, an ablation that injects noise into preferences (e.g., random flips) or mis-ranks demonstrations would probe robustness to imperfect feedback, strengthening the connection to real human use.
- **Timing/complexity comparison**: Reporting per-iteration wall-clock time relative to baselines would help practitioners assess practical trade-offs.
- **Numerical summary table**: A table of final mean rewards with standard errors/confidence intervals would improve precision over visual inspection of figures.

## Removed Points
The following points from the inputs were filtered:
- **"DeepIRL comparison is incomplete" (as fatal/major framing)**: The paper provides hyperparameter sensitivity in the appendix (Figures 7–9 referenced in captions), which is standard practice. Demoted to Minor.
- **"Theoretical novelty is just Plackett-Luce adaptation"**: The paper explicitly acknowledges the Plackett-Luce connection (line 115). The novelty lies in applying partial-order encodings to reward learning, not in claiming a new statistical model. The critic's own assessment calls it a "genuine improvement in practical applicability."
- **"Synthetic feedback is fatal"**: While the synthetic-feedback gap is a real major weakness, it does not invalidate the core theoretical contribution (RRPO) or the algorithm design. The issue is overclaiming relative to evidence, not invalidity of the method.
- **"No human study" as stand-alone fatal flaw**: Merged into the synthetic-feedback weakness rather than treated separately, and downgraded from fatal to major because the method's theoretical validity does not depend on human experiments.
- **Strength Finder's generic strengths about "addressing an important problem"**: Removed as superficial/unspecific. Only evidence-grounded strengths retained.
- **Missing related works**: Removed per instructions (no external sources to confirm existence).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Reframe the paper's claims to match the evidence: present RRPO/LEOPARD as a theoretically-grounded method for combining multiple feedback types with synthetic proof-of-concept validation, and reserve strong practical claims about human data for future work with human-subject evaluation.
2. For the Cliff Walking outlier issue, report results both with and without outliers, or use median-based statistics and justify the approach.
3. Add a noise-injection ablation (e.g., random preference flips, mis-ranked demonstrations) to probe robustness.
4. Report β values used in experiments and study sensitivity to this parameter.
5. Add a summary table of final numerical results with seed counts and confidence intervals.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Borderline Accept</decision>