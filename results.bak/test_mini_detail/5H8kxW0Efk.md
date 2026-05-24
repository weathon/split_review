## Summary

This paper applies algorithm unrolling to dynamical Ising machines for NP-hard Max-Cut/Ising problems. The authors parameterize the update step of a continuous dynamical system with a small MLP (using time-dependent weights via a Fourier basis) and train it via zeroth-order evolutionary optimization. They compare against neural-CO methods (Table 1) and classical Ising machines (Table 2 on G-set benchmarks), demonstrating that learned dynamics can outperform handcrafted ones on most G-set families. The paper also provides interpretability analysis showing the emergence of momentum-like behavior during training.

## Strengths

1. **Novel application of algorithm unrolling to NP-hard combinatorial optimization.** Prior algorithm-unrolling work focused on convex problems or ILP; this paper is the first to unroll a dynamical Ising machine into a small neural network for the Max-Cut/Ising problem. The parameterization (Sections 3.2–3.3) with a small MLP, odd symmetry constraints, and Fourier-basis time modulation is clean and well-motivated.

2. **Strong G-set results using proper metrics (Table 2).** On four of five G-set families (weighted random graphs), dNPIM achieves substantially better median Time-to-Solution than the handcrafted CAC, CFC, and dSBM baselines — e.g., TTS of 6.55e4 vs. 4.31e5 (CAC) on R, +/- instances. These comparisons use the standard TTS metric that accounts for success probability, and the baselines are also tuned per instance type, making this a fair and credible head-to-head.

3. **Insightful analysis of learned dynamics (Section 4).** The single-layer network study (Figure 2) convincingly shows the network evolving from greedy steepest descent to a momentum-equipped strategy. The distinction between cNPIM (continuous coupling, prone to instance-level overfitting) and dNPIM (discrete coupling, more robust) is well-supported by the scatter plots in Figures 3b/3e and provides practical design guidance.

4. **Good use of zeroth-order optimization.** The motivation for avoiding policy gradient / backpropagation over long rollouts (vanishing gradients, noisy credit assignment) is clearly articulated in Section 2.4, and the empirical success at training networks with up to ~140 parameters validates the approach.

5. **Honest treatment of limitations.** The paper acknowledges training-instance dependence (fine-tuning required per problem family), scalability limits with zeroth-order methods, the failure on planar graphs, and the need for better explainability.

## Weaknesses

### Fatal
None.

### Major

- **Unfair comparison protocol in neural-CO benchmarks (Table 1).** dNPIM is evaluated as "top 30" — 30 independent parallel trajectories with the single best solution selected — while the baselines (DiffUCO, SDDS, LTFT) are reported as single samples/rollouts with much shorter runtimes (e.g., 0:03 vs. 1:20 on large instances). The paper acknowledges this ("top 30") but does not account for the asymmetry: running 30 trajectories and cherry-picking the best inflates solution quality relative to a single-trajectory comparison. Time comparisons are also not apples-to-apples because dNPIM consumes more total compute (30× trajectories for large instances). This does **not** undermine the G-set results (Table 2, which uses TTS properly), but it overstates dNPIM's standing relative to prior neural-CO work. The authors should either report the median over 30 runs, run baselines with equivalent compute budgets, or explicitly adjust for the selection effect.

### Minor

- **No variance/error bars on Figure 3c (success rate vs. parameters) and Table 1.** Given the stochastic nature of both the dynamics and the zeroth-order training, reporting some measure of variance (across instances or training seeds) would strengthen confidence in the claims.

- **The failure on planar unweighted graphs (G-set P, +) is not investigated.** dNPIM's TTS is 4.42e7 vs. CAC's 1.81e6 on this family — a 24× degradation. The paper mentions this briefly but offers no analysis of what structural property of planar graphs causes the learned dynamics to fail. A brief investigation would deepen the contribution.

- **Training hyperparameters are deferred to appendices.** While the main paper gives a clear high-level description (Section 3.4), details such as the exact reward functions, population size, learning rates, and number of epochs are in the appendix (which the parser strips but exists in the original submission). For a method whose contribution partly rests on the training approach, having these in the main paper or a prominently available appendix would aid reproducibility.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing zeroth-order optimization against policy-gradient methods under identical compute budgets would directly support the claimed advantage of the training approach.
- A version of Table 1 with a fairer comparison (e.g., reporting dNPIM's median or providing matched-compute results) would clean up the paper's strongest weakness with relatively little effort.
- Analyzing how the learned multi-layer dynamics compose the simple momentum strategy from Section 4.1 with higher-order corrections would strengthen the interpretability story.

## Removed Points

- **Criticism about missing appendix content (training hyperparameters, reward functions, gradient equations).** The paper explicitly states "see appendix G" and "described in appendix F." The parser strips appendix sections from all papers; these exist in the original submission. Per filtering rules, this criticism is removed.
- **Criticism that the G-set results "require a training set of similar instances" should be stated more prominently as a limitation.** The paper already acknowledges this in Sections 4.3–4.4 and the Conclusion ("the network is tuned on a specific problem distribution"). The criticism is factually correct but already addressed.
- **Strength claim about "First application of algorithm unrolling to NP-hard combinatorial optimization."** The paper itself notes the ILP exception (Chen et al. 2024), making this slightly overstated. However, it is still the first for Max-Cut/Ising, so the strength is retained in a qualified form.
- **Strength about "Competitive performance on neural CO benchmarks"** — the Table 1 comparison is flawed, so this strength is de-emphasized.
- **Strength about "Systematic analysis of architecture effects"** — kept as supporting, but the lack of error bars weakens it somewhat. Keeping it since the trend is clear even without error bars.
- **Strength about "out-of-distribution generalization and fine-tuning"** — kept as-is since the paper's own analysis is appropriately measured.
- **Formatting/style nitpicks** from reviews are removed.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviews confirms the paper's own framing: the core novelty is applying algorithm unrolling to NP-hard CO with zeroth-order training, and the main empirical support comes from the G-set benchmarks rather than the neural-CO comparisons. The reviews add no new structural insight that the paper's authors would not already be aware of from their own analysis.

## Suggestions

1. **Fix Table 1.** Either report median (not best) over 30 dNPIM runs, report single-trajectory performance, or match the total compute budget (time × trajectories) of the baselines. This is the single change that would most improve the paper's credibility.
2. **Add a short analysis of the planar-graph failure case** (G-set P, +) — even a few sentences speculating on why the learned dynamics struggle on planar unweighted instances would turn an unexplained failure into a useful finding.
3. **Add error bars or standard deviations** to Figure 3c and the dNPIM entries in Table 1 (or state explicitly if only one seed was used).
4. **Explicitly state in the main paper body** that per-instance-type fine-tuning is required (it is currently mentioned in Section 5 and implicitly in Section 4.3, but a clearer upfront statement would help readers).

## Score and Decision

**Calibration Anchors (all rounds):**

**Round 1 (bracketing):**
- **iWCfiDxLIY.md (avg 3.00)**: Withdrawn TSP paper with GNN. Much weaker novelty and results. → NPIM paper is far stronger.
- **N2M8zxPcKp.md (avg 3.00)**: Withdrawn learned-algorithms paper. Limited empirical validation. → NPIM paper is far stronger.
- **CpiJWKFdHN.md (avg 5.67, Reject)**: GNN-based Max-k-Cut. Similar topic. Reviewers found it incremental and lacking baselines. → NPIM paper has stronger novelty (first algorithm unrolling for NP-hard CO) and a more convincing core experiment (Table 2).
- **9EfBeXaXf0.md (avg 6.75, Accept Poster)**: PQQA - Quasi-Quantum Annealing for CO. Strong novelty and comprehensive experiments. → NPIM paper has comparable novelty but a clearer flaw (Table 1 fairness), placing it slightly below this anchor.
- **6JDpWJrjyK.md (avg 5.75, Reject)**: DISCO diffusion solver for CO. Reviewers found it incremental over DIFUSCO. → NPIM paper has stronger novelty and is clearly better than this anchor.

**Round 2 (narrowing):**
- **jKhNBulNMh.md (avg 6.67, Accept Poster)**: Symb4CO - symbolic discovery for branching. Novel approach, strong experiments. → NPIM paper is slightly weaker due to Table 1 issue but comparable in novelty.
- **yEwakMNIex.md (avg 6.25, Accept Poster)**: UniCO - unified CO via problem reduction. Mixed reviews (5,6,8,6). → NPIM paper is comparable in quality with similar novelty assessment.
- **z2z9suDRjw.md (avg 6.25, Accept Poster)**: GOAL - generalist CO agent learner. Novel multi-task approach. → NPIM paper has more foundational novelty in its niche but GOAL has broader scope; comparable quality.
- **CFLEIeX7iK.md (avg 5.75, Reject)**: Neural solver selection. Limited contribution. → NPIM paper is stronger.
- **ln6QnzBd8o.md (avg 4.80, Reject)**: Decision-focused learning. Not directly comparable. Lower quality.

**Round 1 bracket:** Narrowest plausible range was [5.5, 6.75].

**Round 2 narrowing:** The paper sits below the 6.67–6.75 anchors (PQQA, Symb4CO) due to the Table 1 fairness issue, but above the 5.67–5.75 anchors (ROS, DISCO) due to stronger novelty and a solid core experiment. It is comparable to the 6.25 anchors (UniCO, GOAL). Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>