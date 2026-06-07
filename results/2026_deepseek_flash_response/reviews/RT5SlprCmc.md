Now I have strong calibration data. Let me synthesize everything into the final review.

**Calibration Summary:**
- **Round 1 bracket:** 4.5–6.5 (clearly above 3.0–3.33 weak anchors, clearly below 8.0 strong anchors)
- **Round 2 narrowing:** Compared to TOiageVNru (6.00, Accept) — slightly weaker due to evidential gap; compared to F07ic7huE3 (5.50, Accept) — comparable but different weakness profile; compared to 9SwObx9Jdn (4.75, Reject) and oEzY6fRUMH (4.75, Reject) — clearly stronger. Final position: ~5.0.

---

## Summary

This paper proposes two algorithms (MadDist and TDMadDist) for learning the Minimum Action Distance (MAD) — the minimum number of actions to transition between states — from state-only trajectories, without requiring actions or rewards. It introduces a scale-invariant loss function and a simple quasimetric (d_simple) for asymmetric distance estimation, along with a benchmark suite of environments with known ground-truth MAD. Empirical results show MadDist achieves high correlation with true MAD and near-perfect success rates on long-horizon planning tasks, outperforming the QRL and Hilbert baselines.

## Strengths

- **Scale-invariant loss (Eq. 5) that prevents long-range pairs from dominating training.** By dividing the squared error by $(j-i)^2$, MadDist's main objective addresses a concrete limitation of prior work (Steccanella & Jonsson's unscaled Eq. 2) where the magnitude of estimation error grows with trajectory length. This is a principled improvement clearly motivated in the paper (lines 145–146).

- **A diverse benchmark suite with known ground-truth MAD enables the first systematic evaluation of MAD approximation quality.** The environments span deterministic/stochastic dynamics, discrete/continuous states, symmetric/asymmetric transitions, and noisy observations (lines 208–218). The use of Spearman correlation, Pearson correlation, and Ratio CV (lines 197–203) provides a more rigorous assessment than any prior work, which had no ground-truth comparison.

- **MadDist achieves near-perfect success rates on tasks requiring global coherence.** In Table 1, MadDist scores $1.00 \pm 0.00$ on PM Large Navigate, PM Large Stitch, PM Medium Navigate, and PM Medium Stitch, and $0.99 \pm 0.07$ on PM Giant Stitch. The Stitch environments require composing information across disconnected trajectory segments — demonstrating genuine global structure learning rather than just local fitting.

- **Clear formal characterization of MAD as a linear programming problem (Eq. 1).** The derivation linking MAD to the all-pairs shortest path problem on the determination graph makes the learning objective well-posed and clarifies why triangle inequality constraints are sufficient.

- **Empirical demonstration that handling asymmetry matters.** KeyDoorGridWorld and CliffWalking have irreversible transitions, and the symmetric Hilbert baseline substantially underperforms on these, supporting the paper's central thesis that asymmetry is necessary, not optional.

## Weaknesses

### Major

- **Missing baseline from the most directly related prior work.** The paper states that MadDist is "similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss" (line 137). Yet this prior work is not included as a baseline anywhere in the experiments. The two claimed innovations — quasimetric and scale-invariant loss — cannot be individually validated without ablations that isolate each. QRL tests a different quasimetric formulation (IQE with Lagrangian optimization), and Hilbert tests symmetric vs. asymmetric distance, but neither isolates the scale-invariant loss contribution. This is a structural gap in the paper's evidence for its own claimed improvements.

- **TDMadDist's bootstrapping does not implement a correct Bellman operator for MAD.** The true MAD satisfies $d_{\text{MAD}}(s_i, s_j) = \min_{a: \mathcal{P}(s_{i+1}|s_i,a) > 0} (1 + d_{\text{MAD}}(s_{i+1}, s_j))$ — a minimization over **all reachable next states**. TDMadDist's target (Eq. 8) uses $1 + d_{\theta'}(s_{i+1}, s_j)$ where $s_{i+1}$ is the specific next state on the observed trajectory, not the result of a minimization over actions. The min of two upper bounds ($j-i$ and $1+d_{\theta'}(\cdot)$) is still an upper bound with no guarantee of tightness. The paper provides no theoretical justification for convergence to the correct MAD. (This issue mainly affects TDMadDist, which empirically underperforms MadDist, but the method is presented as a contribution without acknowledging this design mismatch.)

### Minor

- **The phrasing "significantly outperforms" overstates what the evidence supports on some metrics.** In Figure 3, MadDist and QRL achieve similar Pearson correlations (~0.9) on KeyDoorGridWorld and CliffWalking; MadDist's advantage is most visible in the Ratio CV metric. In Table 1, several success rates have overlapping standard deviations (e.g., QRL's $0.87 \pm 0.21$ vs. MadDist's $0.93 \pm 0.17$ on PM Giant Navigate). The paper does not report statistical significance tests.

- **Seed count inconsistency.** Section 7 (line 220) states "All reported results are means over **five** independent runs," but Figure 3 captions (lines 230, 232, 238, 240) consistently state "**three** random seeds." This is a basic reporting discrepancy that should be resolved.

### Trivial

- None.

## Nice-to-Haves

- An analysis of how behavior policy coverage and dataset size affect the quality of the upper bounds and the learned MAD would strengthen the paper's practical guidance. The method depends on trajectories providing informative upper bounds, and this limitation is not discussed.
- Statistical significance testing would clarify whether the differences in Table 1 are meaningful given the observed standard deviations.

## Removed Points

*These points were raised by the reviewers but are removed per policy; they are listed here for completeness and should be treated with caution.*

- **d_simple justification being thin:** The ablation comparing quasimetric choices is referenced in Appendix E (stripped). Per policy, missing appendix content is not a valid weakness.
- **Missing hyperparameter analysis:** Hyperparameter details and analyses reside in the stripped appendix.
- **Garbled Eq. 9:** This is a PDF parsing artifact, not an author error.
- **Hilbert baseline thinly described:** Implementation details and hyperparameters are in the stripped appendix; such reproducibility nitpicks are excluded per policy.
- **Criticism about the paper's missing related works:** Per policy, I cannot judge whether related works are missing without external sources.

## Novel Insights

The harsh critic's observation about TDMadDist's bootstrapping — that it uses the observed next state rather than minimizing over actions, and therefore does not correspond to the correct Bellman optimality operator for MAD — is a genuinely insightful theoretical point that goes beyond what the paper acknowledges. The paper presents TDMadDist as a straightforward TD extension, but this critique reveals a structural mismatch between the algorithm and the quantity it aims to learn. This is worth the authors' serious attention even though MadDist (the direct method) does not share the same flaw and empirically outperforms TDMadDist.

## Suggestions

1. **Include Steccanella & Jonsson (2022) as a baseline**, ideally with ablations that separate the quasimetric and the scale-invariant loss. This directly tests the paper's claimed innovations.
2. **Either provide theoretical justification for TDMadDist's convergence** (showing conditions under which the bootstrapped min-of-upper-bounds target converges to MAD) or reposition it as an exploratory variant and clearly acknowledge its limitations.
3. **Resolve the seed count discrepancy** between the main text (5 seeds) and the figure captions (3 seeds).
4. **Temper the "significantly outperforms" framing** to match what the evidence supports, particularly on metrics where MadDist and QRL are comparable.

## Score and Decision

**Score: 5.0 — Borderline reject.** The paper has genuine contributions (scale-invariant loss, benchmark suite, strong empirical results on MadDist) but the missing baseline from the most directly comparable prior work and the unresolved theoretical issue in TDMadDist are significant gaps that prevent the paper from meeting the ICLR bar in its current form. With major revisions addressing these issues, the paper could become a solid acceptance.

**Decision: Reject**

---

### Calibration Anchors

| Path | Avg Score | Round | Comparison to This Paper |
|------|-----------|-------|------------------------|
| 5AbtYdHlr3 (Safe Action Model Learning) | 3.00 | R1 | Weaker — narrower scope, less convincing evaluations |
| NRRHkJE03w (Conservation Principles) | 3.00 | R1 | Weaker — different subfield, less rigorous evaluation |
| 324fOKW1wO (Driving Decision Transformer) | 3.33 | R1 | Weaker — lacks novelty, unconvincing results |
| Q1Hr9dVfDS (Continual RL) | 3.00 | R1 | Weaker — limited empirical contribution |
| GwKNdRc9Bj (Action Distances for Reward Learning) | 3.75 | R1 | Weaker — narrower scope, limited domains |
| x7Q0uFTH2a (Weak Bisimulation Metric) | 3.75 | R1 | Weaker — ad-hoc losses, less systematic evaluation |
| oEzY6fRUMH (State Chrono Representation) | 4.75 | R1/R2 | Weaker — less convincing results, overclaimed framing |
| 9SwObx9Jdn (Geodesics with Actor-Critic) | 4.75 | R2 | Weaker — only 2 toy tasks, limited applicability |
| Ch9rHRomYe (vMF Exploration) | 5.25 | R2 | Comparable — both have real contributions and notable gaps |
| F07ic7huE3 (Bisimulation Metric for MPC) | 5.50 | R2 | Comparable — similar quality, different weakness profiles |
| **This Paper** | **5.0** | **—** | **—** |
| TOiageVNru (Physics-informed TD Metric Learning) | 6.00 | R1/R2 | Slightly stronger — better baseline coverage, more thorough eval |
| tGQirjzddO (Latent Diffusion in Offline RL) | 6.33 | R2 | Stronger — more mature field, cleaner technical contributions |
| hxUMQ4fic3 (Neural SDE for Offline RL) | 6.67 | R2 | Stronger — more rigorous theoretical treatment |
| EW6bNEqalF (Offline RL in RDPs) | 7.00 | R2 | Stronger — theoretical guarantees, cleaner evaluation |
| LYG6tBlEX0 (H-GAP Humanoid Control) | 7.33 | R2 | Stronger — more comprehensive evaluation on harder tasks |
| cNmu0hZ4CL (Neural Population Dynamics) | 8.00 | R1 | Stronger — unanimous strong scores, different subfield |
| 7BLXhmWvwF (Geometry-aware RL) | 8.00 | R1 | Stronger — unanimous strong scores, different subfield |
| g7ohDlTITL (Flow Matching on Geometries) | 8.00 | R1 | Stronger — unanimous strong scores, different subfield |
| bH6T0Jjw5y (T-IB Markov Processes) | 8.00 | R1 | Stronger — unanimous strong scores, different subfield |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>