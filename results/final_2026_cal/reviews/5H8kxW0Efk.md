Now I have all the information I need. Let me compile the final review.

**Calibration Summary:**

Round 1 (Bracketing):
- Weak band (score < 3.5): BRAIN (2.00), Black-White-Box Optimization Network (2.50), DyCO-GNN (2.67), IsingFormer (2.50) — papers with fundamental flaws or withdrawn; the NPIM paper is clearly above these.
- Middle band (3.5–7.5): Unsupervised GNN for CO (4.50, Reject), Smoothing Binary Optimization (4.50, Reject), Learning with Local Search MCMC (5.00, Reject), Unsupervised Ordering for Max Clique (6.00, Reject).
- Strong band (> 7.5): Papers on quantum neural networks, matrix sign methods, protein generation, etc. — topically distant and clearly stronger.

Round 1 bracket: I placed the paper between 4.5 and 6.5.

Round 2 (Narrowing):
- Query 1 (4.5–6.0): Inverse Temperature of Ising (5.50, Accept Poster), Latent Guided Sampling (5.00, Reject), MaskCO (5.50, Accept Poster).
- Query 2 (6.0–7.5): NEXCO (6.67, Accept Poster), RLAF for SAT (6.50, Accept Poster), Neural Graduated Assignment (6.67, Accept Poster).
- Query 3 (3.5–5.5): Black-Box CO with RL (5.33, Reject), CompSGD (4.00, Reject).

Reading the 6.5-level accepted papers (NEXCO, RLAF) showed they have stronger empirical validations and cleaner evaluation protocols than the NPIM paper. The NPIM paper's novelty is solid and its G-set results are strong, but the Table 1 fairness concern and missing training cost are genuine gaps that prevent it from reaching the 6.5 level. Comparing to the 4.5–5.0 Reject papers, the NPIM paper is clearly stronger in novelty, breadth of results, and honest limitation discussion.

Final score: **5.5** — borderline, with genuine contributions that merit revision.

---

## Summary

This paper proposes Neural Network Ising Machines (NPIM), applying algorithm unrolling to learn the update dynamics of a continuous-time dynamical system for solving NP-hard Max-Cut/Ising problems. A small MLP parameterizes the iterative solver and is trained via zeroth-order evolutionary optimization to maximize solution quality. Two variants are introduced: cNPIM (continuous coupling) and dNPIM (discrete coupling). The method achieves competitive performance on G-set Max-Cut benchmarks (best median TTS in 4 of 5 instance groups) and on several neural CO benchmarks.

## Strengths

- **Novel application of algorithm unrolling to NP-hard Ising/Max-Cut.** The paper extends the algorithm unrolling paradigm — typically applied to convex sensing problems — to the non-convex NP-hard setting. Using a small MLP to parameterize the dynamical update rule of an Ising machine is a genuinely new idea in the neural CO landscape.

- **Competitive results on multiple benchmarks.** dNPIM achieves the best median TTS on 4 of 5 G-set instance groups (Table 2), outperforming established Ising machine algorithms (CAC, CFC, dSBM) on weighted random and toroidal graphs. On neural CO benchmarks (Table 1), dNPIM posts the highest solution sizes in 4 of 5 categories.

- **Insightful analysis of learned dynamics.** The paper shows that a simple single-layer network, trained solely to maximize reward, first learns a steepest-descent strategy and then develops positive weights that create an emergent momentum-like effect to escape local minima (Section 4.1, Figure 2). This connects the learned behavior to known physical search strategies.

- **Systematic investigation of architecture-performance tradeoffs.** The paper characterizes how parameter count, network depth, temporal history length, and temporal basis affect success rate (Section 4.2, Figure 3c), finding saturation around ~50 parameters.

- **Honest discussion of overfitting differences between cNPIM and dNPIM.** Section 4.5 identifies that cNPIM achieves higher average reward but fails on harder instances, while dNPIM is more reliable across the board, and provides a plausible explanation based on discrete vs. continuous coupling.

## Weaknesses

### Fatal

None.

### Major

- **Comparison fairness in Table 1 is not adequately established.** dNPIM results use a "top 30" protocol (best solution from 30 parallel trajectories), while the paper does not specify whether competing methods (DiffUCO, SDDS, LTFT) also use multiple trials, best-of-N reporting, or solution refinement. The justification that per-trajectory cost is lower is stated but unsupported by evidence. Moreover, on large instances dNPIM wall-clock time is substantially higher (1:20 vs. 0:03 for DiffUCO on MIS-large and MaxCut-large). The paper attributes this to implementation details (dense vs. sparse libraries), which is plausible but undercuts the argument that 30 runs are fair. Without knowing the baselines' evaluation protocol, readers cannot assess whether the reported advantages are genuine or artifacts of asymmetric comparison. This concern does *not* affect the G-set results (Table 2), where TTS inherently accounts for multiple trials.

- **Training cost is not reported.** The method requires training a neural network on instances drawn from the same distribution as the test instances (per-problem-class fine-tuning), and the paper states that training from scratch on hard instances is not possible without bootstrapping from smaller instances. Yet no information is provided about training epochs, wall-clock time, number of training instances, or compute budget for any benchmark. This is fundamental to evaluating whether the data-driven approach adds net value over classical heuristics (CAC, dSBM, CFC) that require no training. The paper's claimed advantage of "learning efficient and scalable algorithms" cannot be assessed without quantifying the training investment.

### Minor

- **No standard deviations or error bars for dNPIM results in Table 1.** Competing methods report ± values (e.g., DiffUCO: 19.42 ± 0.03 on MIS-small); dNPIM reports only point estimates (19.9). For Table 2, only median TTS is reported without spread (e.g., interquartile range), limiting the reader's ability to assess reliability. The scatter plots (Figures 3b/e) partially address this for one experimental condition but not for the benchmark tables.

- **Planar-instance failure is acknowledged but not analyzed.** On unweighted planar G-set graphs (N=800, P, +), dNPIM's TTS (4.42e07) is a factor of ~24 worse than CAC (1.81e06). The paper attributes this to future work without exploring why planar unweighted graphs are structurally challenging for the learned dynamics. A diagnostic linking performance to graph properties (degree distribution, cycle structure, sparsity) would strengthen the paper.

- **Choice of zeroth-order optimizer over alternatives is not motivated in the main text.** The paper references Appendix E for numerical comparisons with backpropagation and policy gradient methods, but the main text provides only a qualitative rationale (vanishing gradients, reward attribution). Making the key design justification self-contained would improve readability.

### Trivial

None.

## Nice-to-Haves

- A brief discussion of how the method compares to other neural Max-Cut methods (Karalias & Loukas 2021, Schuetz et al. 2022) beyond the benchmarked set, even if noting that they follow different paradigms.
- An ablation study isolating the contribution of the Fourier temporal basis vs. simpler parameterizations (the paper notes Fourier has "only a minor effect" but defers details to the appendix).
- Per-instance results for Table 1 (currently provided for G-set in the stripped appendix) would improve transparency on instance-level variability.

## Removed Points

- *"Section 2.3 claim about algorithm unrolling is narrowly scoped"* — The paper explicitly states "algorithm unrolling has not been explored for NP-hard combinatorial optimization with the exception of ILP" and cites the relevant ILP work. The statement is accurate for its framing (unrolling of physics-inspired dynamical systems). **Removed**: not a substantive weakness.

- *"Missing comparison with Karalias & Loukas 2021 and Schuetz et al. 2022"* — The paper cites both works in the related literature (Section 2.1) and benchmarks against Sanokowski et al. (2025), which provides comparisons to these and other methods. **Removed**: asking for additional baselines beyond the already competitive set is scope creep for a single paper.

- *"No ablation on the training algorithm"* — The paper provides a rationale for zeroth-order optimization (vanishing gradients, reward attribution) and references Appendix E for detailed numerical results with alternative estimators. The appendix is stripped, but the main text does address the choice. **Removed**: partially addressed in the main text; the appendix content cannot be verified.

- *"Method requires fine-tuning per distribution (limitation)"* — The paper discusses this limitation explicitly in Sections 4.4 and 6 (Conclusions). The harsh critic's formulation largely restates what the paper already acknowledges. **Removed**: the paper is already honest about this trade-off; inflating it into a weakness adds no new information.

- *"No discussion of computational scaling with problem size"* — Section 6 discusses scaling with problem size and number of parameters, and Figure 3a shows TTS vs. N. The per-iteration cost (O(N²) matrix-vector product) is standard. **Removed**: the paper covers this adequately.

## Novel Insights

None beyond the paper's own contributions. The strength finder and harsh critic both surface the same core observations that the paper itself presents: the method is novel, the results are competitive, the top-30 evaluation protocol is a fairness concern, and the training cost is unreported. No genuinely novel synthesis emerges from combining the two reviews.

## Score and Decision

**Final Score: 5.5**

**Decision: Borderline / Major Revision Required**

**Calibration anchors used:**

| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| XthfAAfnVd | 2.00 | R1 weak | BRAIN (withdrawn) — fundamentally flawed; NPIM is much stronger |
| JrZMFC6Jgo | 2.50 | R1 weak | Black-White-Box Opt Network (withdrawn); NPIM is clearly stronger |
| ZS4fa5FgTD | 2.67 | R1 weak | DyCO-GNN (withdrawn); NPIM is stronger |
| yQuTa0yukr | 2.50 | R1 weak | IsingFormer (Reject); NPIM is stronger |
| j8f7IWhKNQ | 4.50 | R1 mid | Unsupervised GNN for CO (Reject) — iterative refinement GNN; NPIM has stronger novelty and comparable results |
| 0bgCa3XAnT | 4.50 | R1 mid | Smoothing Binary Optimization (Reject) — theoretical but limited experiments; NPIM has stronger empirical validation |
| MSi0whiWQA | 5.00 | R1 mid | Learning with Local Search MCMC (Reject) — good theory, narrow tasks; NPIM is comparable or stronger |
| VVbKS5Ar3A | 6.00 | R1 mid | Unsupervised Ordering for Max Clique (Reject) — creative but marginal gains; NPIM has broader empirical support |
| DyDTtBUBEd | 5.50 | R2 narrow | Inverse Temp of Ising (Accept Poster) — theoretical estimation, different task; NPIM comparable quality |
| psUjNnLhl9 | 5.50 | R2 narrow | MaskCO (Accept Poster) — masked generation for CO; NPIM comparable but with evaluation gaps |
| 084SvT55yk | 6.67 | R2 narrow | NEXCO (Accept Poster) — diffusion-based CO, strong results, cleaner eval; NPIM weaker on evaluation rigor |
| NfWrLOKnfk | 6.50 | R2 narrow | RLAF for SAT (Accept Poster) — clean empirical story; NPIM has stronger novelty but weaker evaluation |
| EKqBgn6bea | 5.33 | R3 narrow | Black-Box CO with RL (Reject); NPIM is moderately stronger |

**Bracket progression:** Round 1 placed the paper in (4.5, 6.5). Round 2 narrowed to (5.0, 6.0) by comparing against accepted papers at 5.5 (MaskCO) and 6.5 (NEXCO, RLAF). The NPIM paper has genuine novelty and competitive G-set results that place it above the 4.5-5.0 Reject papers, but the evaluation fairness concern (Table 1) and missing training cost data prevent it from reaching the 6.5 level of the cleanly-evaluated accepted papers. The final score of 5.5 reflects a borderline paper with real contributions that needs major revision on evaluation transparency.

## Suggestions

1. **Clarify the evaluation protocol for Table 1.** Specify whether competing methods also use multiple trials or best-of-N, and report dNPIM results under a single-trajectory protocol alongside the top-30 results. Alternatively, align all methods to the same protocol (e.g., same number of function evaluations or same wall-clock budget).

2. **Report training cost.** Provide the number of training instances, epochs, wall-clock time, and approximate compute budget (GPU-hours) for each benchmark. This is essential for readers to evaluate whether the data-driven approach is practically useful relative to training-free classical heuristics.

3. **Add variability estimates.** Report standard deviations or confidence intervals for dNPIM in Table 1, and per-group TTS spread (e.g., IQR) for Table 2, to match what competing methods provide.

4. **Diagnose the planar-instance failure.** Include a brief analysis of why unweighted planar graphs (P,+) are challenging — e.g., correlation with graph properties like degree distribution, sparsity, or treewidth — even if the diagnosis is preliminary.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject (with major revision path)</decision>