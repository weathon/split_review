Now let me write the final consolidated review.

## Summary

This paper proposes MadDist (and a TD variant TDMadDist) for learning the Minimum Action Distance (MAD) from state-only trajectories, without rewards or action labels. The key ideas are: (1) using quasimetrics (asymmetric distance functions) instead of symmetric metrics to capture directional structure in environments with irreversible dynamics, (2) a scale-invariant loss that prevents long-range trajectory pairs from dominating the training objective, (3) a simple new quasimetric called d_simple, and (4) a suite of benchmark environments with known ground-truth MAD. The paper evaluates against QRL (which also uses a quasimetric) and a symmetric Hilbert-space baseline, reporting improved MAD correlations and higher downstream planning success rates.

## Strengths

- **Scale-invariant loss (Equation 5) corrects a genuine weakness of prior work.** Prior work (Steccanella & Jonsson 2022, Equation 2) uses an unnormalized squared error where states farther apart on a trajectory dominate the loss purely due to larger error magnitudes. MadDist's normalized loss `(d_theta(s_i,s_j)/(j-i) - 1)^2` removes this bias. The empirical benefit is visible in Figure 3's Ratio CV plots, where MadDist achieves consistently lower CV than QRL across all three shown environments.

- **Diverse benchmark suite with known ground-truth MAD enables systematic evaluation.** The environments (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze variants, OGBench) span stochastic/deterministic dynamics, discrete/continuous state spaces, and symmetric/asymmetric transitions, all with computable ground-truth MAD. This goes beyond prior work and allows the three metrics (Spearman ρ, Pearson r, Ratio CV) to isolate what each method captures or misses.

- **Downstream planning results demonstrate practical utility.** Table 1 shows MadDist achieving success rates of 1.00 ± 0.00 on 4 of 6 OGBench PointMaze planning tasks, substantially outperforming QRL (best 0.97 ± 0.09) and the Hilbert baseline (best 0.67 ± 0.28). This provides direct evidence that the learned distance transfers to goal-oriented planning, not just correlation in embedding space.

- **Clear framing of the asymmetry problem.** The paper correctly motivates why symmetric metrics are structurally insufficient for MAD in environments with irreversible transitions (key pickup in KeyDoorGridWorld, falling shortcuts in CliffWalking), and grounds this in the quasimetric formalism.

## Weaknesses

### Major

- **No ablation isolating which design choices drive the improvement over QRL.** MadDist differs from QRL in multiple aspects simultaneously: (a) a different loss function (scale-invariant regression with contrastive regularization vs. QRL's Lagrangian optimization), (b) a different quasimetric (d_simple is used for MadDist but the paper doesn't explicitly state this in the main text — see Minor), and (c) different supervision structure (direct path-length regression over arbitrary trajectory pairs vs. QRL's locality-constrained optimization). Without ablations that isolate these factors — e.g., MadDist with IQE vs. MadDist with d_simple, or MadDist with the unnormalized loss from Equation 2 — the paper cannot substantiate which of its claimed innovations drives the reported gains. The quasimetric ablation is relegated to Appendix E (stripped), and neither the loss design nor the supervision structure is ablated at all. This weakens the paper's central claim that its specific methodological choices are responsible for the improvement.

### Minor

- **Seed discrepancy between Figure 3 and the empirical setup.** Figure 3's caption (lines 230, 232, 238, 240) states "minimum and maximum values across three random seeds," while Section 7 (line 220) states "All reported results are means over five independent runs (random seeds)." This is an inconsistency that needs clarification: were the Figure 3 results obtained with 3 seeds or 5?

- **Equation 9 is garbled.** The equation for L'_r (line 171) contains `d_theta(s_i, s_{i+1} + d_{theta'}(s_{i+1}, s_r) - 12(9))` — a term that adds a scalar to a state vector and includes a nonsensical `12(9)` fragment. The surrounding text describes a sensible TD objective (`make d_theta(s_i, s_r) equal to 1 + d_{theta'}(s_{i+1}, s_r)`), but the equation does not match this description. This needs correction.

- **Which quasimetric MadDist uses in the main results is not specified.** The paper defines d_simple, d_WN, and d_IQE (Section 5), and states that QRL uses IQE (line 204). But the main results in Figure 3 and Table 1 do not state which quasimetric is used by MadDist or TDMadDist. If MadDist uses d_simple while QRL uses IQE, the comparison conflates method choice with quasimetric choice. The paper references an ablation in Appendix E, but this information should be in the main text.

- **TDMadDist's underperformance is inadequately explained.** The paper acknowledges (line 226) that "TDMadDist underperforms the MadDist and QRL algorithm," yet presents it as a "novel algorithm" contribution. The only justification — "its strong performance relative to Hilbert highlights the advantages of our quasimetric approach even when paired with a TD-based objective" — is weak, since the comparison to Hilbert is already established by MadDist. The paper would benefit from explaining why the TD bootstrap fails (e.g., target network instability, bootstrapped target collapse), or from reframing TDMadDist as a negative result that yields insight.

- **Hilbert baseline comparison somewhat inflates the apparent advantage.** The Hilbert method (Park et al., 2024b) learns a symmetric Euclidean distance, which is structurally incapable of capturing asymmetric MADs. The paper acknowledges this (line 206: "to demonstrate the benefits of methods that explicitly model the quasimetric nature"). However, presenting it alongside QRL as a co-equal baseline in the discussion (line 226: "MadDist outperforms the QRL and Hilbert baselines") makes the "outperforms all baselines" claim broader than the meaningful comparison (which is against QRL). The Hilbert comparison has value as an illustrative ablation, but its placement inflates the apparent margin of improvement.

- **Perfect standard deviations in Table 1 raise ceiling-effect questions.** MadDist achieves 1.00 ± 0.00 on 4 of 6 OGBench tasks. While success rate is bounded and zero-variance perfect performance is possible with enough trials and a sufficiently easy test, the paper describes these environments as "large-scale" and "challenging." Zero variance across 5 seeds suggests either a ceiling effect (tasks are too easy to discriminate methods) or an evaluation protocol with insufficient variation. Including a more fine-grained metric (e.g., planning regret relative to optimal) would strengthen the evidence.

### Trivial

- Equation 10 (line 177) uses `θ' ← (1 - β)θ' + βθ` which is a standard EMA update, but the text says "updated via an exponential moving average with hyperparameter β." Note that here β is the rate toward the online parameters — this is correct but sometimes β is used the other way; consider clarifying.
- The claim on line 78 that MAD provides "more realistic distance estimates than the SSP" is imprecisely phrased — MAD is a lower bound on SSP, not more realistic; the paper later clarifies this.

## Nice-to-Haves

- An ablation within the MadDist framework comparing the scale-invariant loss (Equation 5) against the unnormalized loss (Equation 2) while holding all other design choices (quasimetric, contrastive regularization, constraint loss) constant would directly test whether scale invariance drives improvement.
- A discussion of trajectory coverage requirements: the method relies on random-policy trajectories, but would benefit from analysis of what happens when coverage is insufficient (behavior policy never visits certain transitions).

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- **"d_simple is trivial"** — This is a subjective assertion. The paper shows that this simple quasimetric works well and provides an ablation in Appendix E (stripped) comparing it against alternatives. Whether a construction is "trivial" is a matter of opinion, not a verifiable weakness.
- **"No comparison against goal-conditioned value function approaches"** — This asks the paper to address problems outside its stated scope. The paper compares against the most relevant prior work (QRL, which also uses quasimetrics, and Hilbert, which illustrates the need for asymmetry).
- **"Hilbert comparison is uninformative" (as originally framed)** — The paper transparently states the purpose of this comparison (line 206). Calling it "uninformative" ignores its value as a controlled ablation showing the importance of asymmetry. The merged review keeps the related concern about presentation/framing as a Minor weakness, not the stronger original claim.
- **Strengths removed from Strength Finder** — Generic strengths about the problem being "important" or "well-motivated" are removed. Only concrete, evidenced strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface evaluation weaknesses (lack of ablations, seed discrepancy) but do not generate new scientific insights beyond what the paper itself provides.

## Suggestions

1. **Add ablations** isolating (a) the scale-invariant loss vs. unnormalized loss, (b) d_simple vs. IQE as the quasimetric within MadDist, all else held constant. This is the single most impactful improvement.
2. **Resolve the seed discrepancy** between Figure 3 (3 seeds) and Section 7 (5 seeds), and ensure all results are consistent.
3. **Correct Equation 9** to match the textual description (make d_θ(s_i, s_r) equal to 1 + d_{θ'}(s_{i+1}, s_r)).
4. **Explicitly state** in the main text which quasimetric each method uses in each experiment.
5. **Either explain why TDMadDist underperforms** or downgrade its status from "novel algorithm" to a failed experiment that yields insight.
6. **Address the ceiling effect** in Table 1 by reporting a more fine-grained metric (regret relative to optimal) or increasing task difficulty.

---

### Calibration Report

**Round 1 (Bracketing):** Five queries across score bands for papers on distance metric learning, state representation, and quasimetric methods.
- **Strong reject (<2.5):** Papers at 1.5–2.0 — unserious contributions, poorly motivated. Our paper is far above this.
- **Weak (2.5–4.5):** Papers at 3.75–4.33 (e.g., "Weak Bisimulation Metric" at 3.75, "Exploiting Action Distances" at 3.75). These have partial merit but significant flaws. Our paper is stronger.
- **Middle (4.5–6.1):** Papers at 4.75–6.00 (e.g., "State Chrono Representation" at 4.75, "MIND" at 4.75, "Physics-informed TD Metric Learning" at 6.00). Our paper fits in this range.
- **Strong accept (6.0–7.5):** Papers at 6.50–6.75 (e.g., "STARC" at 6.50, "Episodic Novelty Through Temporal Distance" at 6.75). More thorough evaluation, stronger theoretical grounding.
- **Exceptional (>7.5):** Papers at 8.0. Our paper is clearly below this.

**Round 2 (Narrowing 4.5–6.5):** Additional queries targeting 3.5–5.5 and 5.0–7.0.
- Read full reviews of "Distributional Distance Classifiers" (avg 6.00, rejected) — a goal-conditioned RL paper with mixed reviews and evaluation gaps. Similar quality.
- Read "MIND" (avg 4.75, rejected) — representation learning with clearer evaluation gaps than our paper.
- Read "Physics-informed TD Metric Learning" (avg 6.00, accepted) — more thorough evaluation, real-world validation, stronger theoretical grounding. Our paper is weaker.
- Read "STARC" (avg 6.50, accepted) — tight theoretical contribution, clean evaluation. Our paper is weaker.

**Final bracket:** Our paper is above the 3.75–4.75 range (clearer contributions, better results) but below the 6.0+ range (evaluation thoroughness, theoretical grounding). The paper has genuine contributions but the lack of ablations isolating design choices and several presentation issues prevent it from being a clear accept.

**Anchors consulted:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| /.../473sH8qki8.md | 2.00 | R1 | Much weaker — unserious contribution |
| /.../x7Q0uFTH2a.md | 3.75 | R1, R2 | Weaker — significant presentation issues |
| /.../GwKNdRc9Bj.md | 3.75 | R1 | Weaker — limited contribution |
| /.../oEzY6fRUMH.md | 4.75 | R1, R2 | Somewhat weaker — overlapping confidence intervals |
| /.../jkonJu7ScD.md | 4.75 | R2 | Similar quality, our paper has clearer contribution |
| /.../qofh48zW3T.md | 6.00 | R2 | Similar quality but rejected — our paper's issues are comparable |
| /.../TOiageVNru.md | 6.00 | R1 | Stronger — more thorough evaluation and real-world validation |
| /.../wPhbtwlCDa.md | 6.50 | R2 | Stronger — tight theoretical contribution |
| /.../I7DeajDEx7.md | 6.75 | R1 | Stronger — clean evaluation, clearer claims |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>