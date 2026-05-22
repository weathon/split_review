Now I have a clear picture. Let me synthesize the review.

---

## Summary

This paper proposes Neural Network Ising Machines (NPIM), a method that learns the update dynamics of an Ising machine by parameterizing them with a small MLP and training via zeroth-order optimization — effectively applying algorithm unrolling to NP-hard combinatorial optimization for the first time. The authors introduce continuous (cNPIM) and discrete (dNPIM) coupling variants, analyze emergent behaviors like momentum-like dynamics and overfitting tendencies, and benchmark against both neural CO methods and classical Ising machines. The method achieves strong results on G-set Max-Cut benchmarks and competitive performance on standard neural CO benchmarks.

## Strengths

- **Genuinely novel synthesis of three distinct ideas**: The paper is — to the best of my knowledge — the first to apply algorithm unrolling to NP-hard CO (specifically Max-Cut/Ising), combining it with an Ising machine dynamical framework and zeroth-order optimization. This is not an incremental combination; each component serves a clear purpose (Section 3.2–3.4).

- **Strong, clean results on classical Ising machine benchmarks (G-set, Table 2)**: dNPIM achieves the lowest median TTS on three of five G-set instance groups when compared against CAC, CFC, and dSBM — all well-established Ising machines. Using TTS in *iterations* avoids hardware-specific timing confounds and provides a credible head-to-head comparison. The paper notes that algorithm parameters for the baselines are also tuned per instance type (Section 5, paragraph 2), making the comparison reasonably fair.

- **Insightful analysis of learned dynamics**: The contrast between cNPIM and dNPIM in Section 4.5 is valuable. The observation that cNPIM achieves higher average success rates but fails on the hardest instances — while dNPIM is more reliable — is a practical and non-obvious finding grounded in the discrete-vs-continuous coupling distinction. The instance-wise scatter plots (Figures 3b, 3e) against CAC make this concretely visible.

- **Practical contributions via bootstrapping and fine-tuning (Section 4.3–4.4)**: The demonstration that networks pre-trained on small/easy instances can be fine-tuned to harder distributions, with measurable out-of-distribution generalization (Figures 3a, 3d), is a useful result for practitioners and shows the method is not brittle.

- **Well-motivated use of zeroth-order optimization**: The paper provides a clear rationale (Section 2.4, Section 3.4) for why backpropagation and policy gradient are ill-suited to long Ising machine trajectories, and why zeroth-order optimization is a natural fit. This design choice is well-justified.

## Weaknesses

### Fatal

None.

### Major

- **Uncontrolled sampling budget in the neural CO benchmark comparison (Table 1)**: dNPIM is evaluated using the best of 30 parallel trajectories ("top 30"), while the comparison methods (DiffUCO, SDDS, LTFT) are not granted an equivalent multi-sample budget. The paper is transparent about this — the table caption explicitly states the protocol — and argues that dNPIM is less computationally intensive per trajectory. For small instances (MIS-small, MaxCut-small, MaxCl-small), dNPIM matches competitor wall-clock time (0:02) while running 30 trajectories, which is reasonable. However, for large instances (MIS-large, MaxCut-large), dNPIM requires 1:20 versus competitors' 0:03 — a ~27× time difference the paper attributes partly to dense-vs-sparse implementation differences. The claim that dNPIM achieves better solution quality in four of five cases cannot be fully assessed without either (a) reporting dNPIM's single-trajectory performance or (b) running competitors with an equivalent parallel budget. This weakens the headline neural CO benchmarking claim, though the G-set results (Table 2) remain credible.

### Minor

- **No estimate of statistical variability for the architecture sweep (Figure 3c)**: The scatter plot aggregates different network configurations but it is unclear whether each point represents a single training run or a mean over multiple seeds. Without repeat experiments, the claimed trend of improvement with more parameters is suggestive but not statistically grounded. The single-parameter sweeps deferred to Appendix C.1 are also unavailable in the main text for verification.

- **Qualitative nature of the momentum emergence analysis (Section 4.1)**: The interpretation of weight sign changes as evidence of momentum is interesting but remains illustrative. No independent measure of momentum (e.g., autocorrelation of variables, comparison to a control) is provided. The paper appropriately presents this as an observation rather than a rigorous finding, but readers should treat it as a qualitative anecdote.

- **G-set training requires instance-family-specific synthetic data generation**: The paper generates separate training sets for each G-set graph family (Section 5, paragraph 2; Appendix I). Hand-designed Ising machines like CAC and dSBM do not require this per-family tuning. While the paper notes that baseline algorithm parameters are also tuned per instance type, the learned method has an additional dependence on synthetic data generation that complicates the "learned dynamics are inherently superior" interpretation of Table 2. This is a scope/trade-off concern, not a flaw.

- **Reward function details deferred to appendix**: Section 3.4 mentions two reward functions but provides no summary of what they optimize (e.g., binary success rate vs. approximation-ratio-based reward). Since the reward fundamentally shapes the learned algorithm, a brief in-text summary would improve self-containedness.

### Trivial

- No run-to-run variability (confidence intervals, box plots) is reported for TTS or success rates, which would strengthen the statistical presentation.

## Nice-to-Haves

- Re-running the neural CO comparison with a common computational budget (equal number of trajectories for all methods, or reporting single-trajectory performance for dNPIM) would either confirm or qualify the Table 1 claims without changing the paper's scope.
- Quantitative evidence for momentum-like effects (e.g., autocorrelation analysis of the $x_i$ variables) would elevate Section 4.1 from anecdote to diagnostic.
- Reporting mean and standard deviation over multiple training seeds for the architecture sweep (Figure 3c) would increase confidence in the parameter-scaling claims.
- A brief summary of the reward functions in the main text (Section 3.4) would improve readability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim that the Table 1 comparison is "fatal" and "invalidates the claimed performance advantage"**: Downgraded to Major. The paper explicitly discloses the "top 30" protocol. For small instances, dNPIM achieves 0:02 for 30 trajectories — same as competitors' time, making the comparison fair in wall-clock terms for those cases. The concern is legitimate but not fatal, and the G-set results (Table 2) provide independent corroboration.

- **Harsh critic's concern about training/test split for MIS/MaxClique benchmarks**: The paper says it used "the same graph instances as described in Sanokowski et al. (2025)." While the main text doesn't detail train/test splits, this information is presumably in the stripped appendix. Without evidence of overlap, this is speculative — removed.

- **Harsh critic's claim that the architecture sensitivity analysis fails to "decompose the separate influences of T_c, D, and M while controlling for total parameters"**: The paper explicitly references Appendix C.1 for single-parameter sweeps and appropriately hedges the claim ("doesn't seem to have a large effect"). The main point — that parameter count matters more than architectural allocation — is reasonable given the presented evidence. Removed as an overstatement.

- **Strength Finder's "competitive performance on standard neural-CO benchmarks"**: This strength is partially undermined by the fairness concern (Major weakness above). Retained but qualified — the G-set results provide stronger evidence.

- **Strength Finder's "emergence of momentum-like dynamics" as a core strength**: The paper itself treats this as qualitative/illustrative, not a proven finding. Downgraded; not listed as a standalone strength.

- **Strength Finder's generic strengths**: "Practical design choice with dNPIM vs cNPIM" and "avoidance of backpropagation difficulties" are already captured in the strengths above and not separately listed.

## Novel Insights

The most interesting emergent insight from the reviews is methodological: this paper sits at the intersection of two evaluation cultures — neural CO (where wall-clock time and best-of-K sampling are standard) and classical Ising machines (where TTS in iterations and per-instance tuning dominate). The tension in Table 1 arises precisely because the authors are trying to speak to both communities with a single protocol, and the standards don't perfectly align. This is not a weakness of the paper per se but a sign that hybrid methods like NPIM need hybrid evaluation protocols. The G-set results (Table 2, using iteration-normalized TTS) are actually the more convincing evidence for the method's quality, and future work in this space would benefit from prioritizing such protocol-agnostic metrics.

## Suggestions

- The highest-leverage revision: report dNPIM's single-trajectory performance on the Table 1 benchmarks alongside the "top 30" results, or apply the same best-of-K protocol to at least one competitor (e.g., SDDS) on the large instances. This would transparently address the budget concern.
- Add seed-based variability (error bars or confidence intervals) to Figure 3c and the architecture analysis, even if only for a subset of configurations.
- Move a one-paragraph summary of the two reward functions (binary success vs. approximation-ratio-based) from Appendix F into Section 3.4.
- Consider framing the G-set results (Table 2) as the primary empirical contribution, with Table 1 as supplementary evidence, to reduce reliance on the budget-imbalanced comparison.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| BlSIKSPhfz (Hybrid Continuous-Discrete Ground-State Sampling) | 6.00 | R1/R2 | Most comparable: Ising problems, hybrid dynamics, accepted. Our paper is cleaner and has more comprehensive benchmarks. |
| peNgxpbdxB (SDDS — Scalable Discrete Diffusion Samplers) | 6.00 | R1/R2 | SDDS is a baseline in our Table 1. Our paper outperforms it. Accepted at 6.00. |
| 6JDpWJrjyK (DISCO — Diffusion Solver for CO) | 5.75 | R1/R2 | Rejected; criticized for incremental novelty. Our paper has stronger novelty (first algorithm unrolling for NP-hard CO). |
| yEwakMNIex (RedCO — Unified Neural Solvers) | 6.25 | R2 | Broader scope but more concerns about applicability. Comparable quality. |
| jKhNBulNMh (Symb4CO — Symbolic Discovery for CO Branching) | 6.67 | R2 | Stronger paper with more rigorous validation and clearer practical impact. Our paper is below this tier. |

**Round 1 bracket:** 5.5–7.0 (between weak anchors at 2.6–3.0 and strong anchors at 8.0–9.0).

**Round 2 narrowing:** The paper lands between BlSIKSPhfz/peNgxpbdxB (both 6.00, accepted) and yEwakMNIex (6.25, accepted). The G-set results are genuinely strong, and the method is novel. The Table 1 fairness concern is real but disclosed and partially mitigated for small instances. The paper is clearly above the 5.75 rejected tier (DISCO) but below the 6.67 tier (Symb4CO). Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>