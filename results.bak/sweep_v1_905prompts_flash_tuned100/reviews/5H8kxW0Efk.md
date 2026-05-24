Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper proposes Neural Network Ising Machines (NPIM), a method that applies algorithm unrolling to dynamical Ising machines for the NP-hard Max-Cut/Ising problem. The update dynamics of an iterative Ising solver are parameterized by a small MLP with a temporal Fourier basis, and the parameters are trained via zeroth-order evolutionary optimization. The method is evaluated on both neural-CO benchmarks (MIS, MaxClique, MaxCut) and classical Ising machine benchmarks (G-set). Results show dNPIM achieves the best solution quality on 4/5 neural-CO benchmarks and the lowest median TTS on 4/5 G-set instance types compared to handcrafted Ising machine algorithms (CAC, CFC, dSBM). The paper also analyzes the learned dynamics, showing emergence of momentum-like effects and discussing overfitting differences between continuous and discrete coupling variants.

## Strengths

1. **Genuine novelty in combining algorithm unrolling with dynamical Ising machines.** Section 3.3 (Eqs. 4–7) provides a clean parameterization of Ising machine update dynamics with a small MLP and a temporal Fourier basis. To the best of the paper's knowledge, this is the first application of algorithm unrolling to an NP-hard combinatorial optimization problem of this type — a nontrivial extension beyond the convex and sensing problems where unrolling is typically applied.

2. **Competitive performance on Ising machine benchmarks (G-set).** Table 2 shows dNPIM achieves the lowest median time-to-solution on 4 of 5 G-set instance types (N=800 R,+, R,+/- , T,+/- , P,+/-) compared to CAC, CFC, and dSBM. Because TTS is measured in iterations (not wall-clock time), this comparison is fair and directly demonstrates that the learned dynamics can outperform carefully handcrafted Ising machine algorithms. On the P,+ group where dNPIM lags, the paper acknowledges this honestly.

3. **Emergence of interpretable dynamics from a pure reward signal.** Figure 2 shows how a single-layer network (M=1, Tc=10) transitions from all-negative weights (greedy descent) to weights with positive connections that produce a momentum-like escape effect from local minima. This provides direct evidence that effective search dynamics can be learned from scratch, and the visualization is illuminating.

4. **Thoughtful analysis of the cNPIM vs. dNPIM tradeoff.** Section 4.5 and Figures 3b/3e demonstrate that cNPIM (continuous coupling) achieves higher average success rates but fails catastrophically on some hard instances, while dNPIM (discrete coupling) is more robust. This is a substantive empirical finding that informs algorithm design choices.

5. **Parameter efficiency and transfer learning.** The architecture uses as few as ~50 parameters (Figure 3c) and the paper demonstrates fine-tuning from N=100 to N=500 SK instances (Figure 3a), showing practical scalability through transfer.

## Weaknesses

### Fatal
None.

### Major

1. **The wall-clock time comparison in Table 1 is not interpretable.** The paper runs 30 trajectories in parallel and takes the best ("top 30"), while it is unclear whether the baselines (DiffUCO, SDDS, LTFT) use any equivalent multi-start. Furthermore, the paper acknowledges the time gap on large instances "could have something to do with the sparse graph library used for the results... as opposed to the dense PyTorch matrix-matrix product used in our implementation." This means the time columns mix algorithmic and implementation differences in an unquantifiable way. The table should either report solution quality only (with explicit discussion of computational budget) or provide a controlled timing comparison where both dNPIM and baselines use comparable sparse implementations. As presented, a reader cannot tell whether a 1:20 vs. 0:03 gap on MIS-large is fundamental or implementational.

2. **The TTS results in Table 2 mask a nontrivial failure rate on some G-set groups.** Figure 3e shows that on N=800 instances, dNPIM has infinite TTS (never finds the target cut) on a subset of instances. The paper reports only *median* TTS per group in Table 2, which can be finite even when a substantial fraction of instances are unsolved. For example, on the planar "P,+" group at N=800, dNPIM's median TTS is 4.42e07 vs. CAC's 1.81e06 — roughly 24× worse — and the paper does not report what fraction of P,+ instances dNPIM actually solves at all. Without the solved fraction, a reader evaluating dNPIM as a *reliable* solver cannot assess whether its strong median performance on other groups comes at the cost of occasional total failure. A column showing solve rate (or TTS at 99% target across instances) per group should be added.

3. **Training cost is not characterized anywhere in the paper.** The paper's core claim is that effective Ising machine dynamics can be *learned* from data. Yet the main text provides no information about: the number of epochs/function evaluations used during training, the wall-clock cost of training (e.g., "training dNPIM for the G-set experiments took X hours on a single A100 GPU"), the number of problem instances per epoch, or the total compute budget. Without this, the reader cannot assess whether the method is practical or a proof of concept. The paper references Appendix F and G for training details, which are stripped, but even a rough characterization in the main text (e.g., "training required approximately 500 epochs, each evaluating 256 trajectories across 64 instances") would address this gap.

### Minor

1. **No standard deviations or confidence intervals for dNPIM in Table 1.** The baselines (DiffUCO, SDDS) report standard errors, but dNPIM reports only point estimates. For instance, on MIS-small, dNPIM achieves 19.9 vs. SDDS's 19.62±0.01 — it is unclear whether this ~0.3 difference is statistically meaningful given the small absolute scale. The paper should report the distribution of dNPIM's solutions over multiple runs.

2. **The "top 30" multi-start comparison is asymmetric.** Running 30 trajectories in parallel and taking the best, while baselines may use single trajectories, gives dNPIM an advantage on solution quality that is not reflected in the time costs shown for the baselines (which may not include multi-start). The paper should clarify whether the baseline timings include equivalent multi-start or multi-trajectory evaluation, and if not, the quality advantage may partially stem from greater computational effort rather than superior per-trajectory dynamics.

3. **No direct comparison between NPIM and the CAC dynamics it builds on, controlling for training distribution.** The paper compares NPIM against CAC on G-set (Table 2), which is an out-of-distribution evaluation since NPIM is fine-tuned on G-set-like training instances while CAC's parameters were tuned for the G-set as well. A controlled comparison on the SK instances (which are in-distribution) between NPIM and a well-tuned CAC would directly answer whether learning adds value over simply tuning a fixed algorithm's hyperparameters.

### Trivial
- Table 1 would benefit from a footnote clarifying whether baseline times include single or multiple trajectories.

## Nice-to-Haves
- **Success rate per G-set group**: Reporting the fraction of instances solved within a reasonable budget (alongside median TTS) would significantly strengthen the reliability analysis. The paper mentions instance-wise data is in Table 4 (appendix), but this should be summarized in the main text.
- **Ablation of temporal basis choice**: The paper states Fourier/Chebyshev/Legendre have minor effect and the dominant factor is M (number of modes). A Pareto frontier plot of performance vs. M for fixed total parameter count would be informative, especially since the zeroth-order optimizer's cost scales with P.
- **Sensitivity analysis of the zeroth-order optimizer hyperparameters**: The paper relies on a specific evolutionary strategy (Reifenstein et al., 2024) but does not discuss sensitivity to population size, learning rate, or covariance initialization.

## Removed Points
- *Criticism about missing appendix details (hyperparameters, reward formulation equations)*: Standard practice to defer implementation details to appendix; not a weakness of the paper as submitted.
- *Criticism about the absence of bias justification (odd symmetry)*: The paper explicitly motivates this design choice in Section 3.3 ("in order for the algorithm to respect the symmetry of the Ising problem we want the resulting function to be odd"). The reviewer's demand for an ablation is a nice-to-have, not a weakness.
- *Strength Finder's claim about "superior TTS on G-set" without caveat*: Kept but qualified with the TTS failure mode issue above.
- *Generic strengths about "addressing an important problem"*: Removed as nonspecific.

## Novel Insights

The harsh critic's observation that the time comparison in Table 1 is difficult to interpret, combined with the finding that dNPIM's strong median TTS on G-set (Table 2) coexists with a nontrivial failure rate on the hardest instances, reveals a structural tension in the paper: the strongest evidence for the method (G-set TTS) is iteration-based and therefore fair, but the evidence most visible to the neural-CO community (Table 1) is the least controlled. The paper's own discussion of the cNPIM/dNPIM overfitting tradeoff (Section 4.5) actually provides the conceptual framework for understanding this tension — dNPIM trades average-case optimality for worst-case robustness. This is a genuinely interesting finding that the paper could elevate into a central claim rather than treating it as a secondary observation.

## Suggestions

1. Restructure the empirical contribution around the G-set iteration-based results (Table 2) as the primary evidence, and either remove or heavily caveat the wall-clock time column in Table 1.
2. Add a column to Table 2 reporting the fraction of instances solved per G-set group.
3. Add a paragraph in Section 5 (or the experimental setup) characterizing training cost: total number of epochs, function evaluations per epoch, and approximate wall-clock time on the hardware used.
4. Report standard deviations for dNPIM's results in Table 1.

## Score and Decision

**Round-1 bracket**: 5.0–7.0 (based on three queries bracketing weak anchors avg<3.5, middle anchors 3.5–7.5, and strong anchors >7.5).

**Round-2 narrow**: The closest anchors to this paper are:
- *Non-Equilibrium Dynamics of Hybrid Continuous-Discrete Ground-State Sampling* (6.00, Accept) — similar Ising/ground-state sampling domain, comparable level of methodological contribution and empirical thoroughness. The NPIM paper has more novel technique combination but slightly less polished evaluation; roughly comparable overall.
- *Unified Neural Solvers* (6.25, Accept) — a multi-task CO paper with good novelty but questioned applicability. NPIM has clearer evidence that its method works on the target problem.
- *Neural Solver Selection* (5.75, Reject) — a framework paper with limited novelty. NPIM is clearly more novel.
- *PQQA* (6.75, Accept) — strong method with thorough experiments. NPIM has comparable novelty but weaker empirical characterization (training cost, timing).

**Final score**: 6.0. The paper presents a genuinely novel approach with competitive results on standard benchmarks, but the evaluation has meaningful gaps (timing comparison interpretability, TTS failure rate reporting, training cost characterization) that prevent it from being a strong accept. The core contribution — that learned Ising machine dynamics can compete with handcrafted ones — is supported.

**Decision**: Accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>