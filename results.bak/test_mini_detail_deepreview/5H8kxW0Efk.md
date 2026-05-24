Now I will write the consolidated final review.

## Summary

This paper proposes Neural Network Ising Machines (NPIM), applying algorithm unrolling to dynamical Ising machines for solving Max-Cut/Ising problems. The core idea is to parameterize the update step of an Ising machine with a small MLP and train it via zeroth-order evolutionary optimization, learning effective search dynamics from data. The paper introduces two variants (continuous coupling cNPIM and discrete coupling dNPIM) and benchmarks against both neural CO methods and classical Ising machine algorithms. The strongest evidence is on G-set benchmarks (Table 2), where dNPIM achieves lower time-to-solution on 4/5 instance groups against CAC, CFC, and dSBM.

## Strengths

- **Novel application of algorithm unrolling to NP-hard combinatorial optimization.** The paper is the first to apply algorithm unrolling to NP-hard Max-Cut/Ising problems, parameterizing the entire dynamical update with a learnable MLP. This is well-supported by experiments: Table 2 shows dNPIM outperforms handcrafted Ising machine baselines (CAC, CFC, dSBM) in TTS on 3/5 G-set groups (N=800,R,+; N=800,R,+/-; N=800,T,+/-), and Table 1 shows dNPIM achieves the best solution quality on 4/5 neural CO benchmarks.

- **Insightful analysis of learned dynamics.** The analysis in Section 4.1 (Figure 2) goes well beyond typical benchmark reporting. The paper shows that a single-layer network trained only to maximize success rate spontaneously learns a momentum-like effect to escape local minima — early in training all weights are negative (greedy steepest descent), while later positive weights emerge that kick the trajectory out of meta-stable states. This provides genuine interpretability into what the network learns.

- **Careful comparison of continuous vs. discrete coupling.** Section 4.5 provides a well-supported analysis of the trade-offs between cNPIM and dNPIM. Figure 3b shows cNPIM overfits to easy instances (many hard instances remain unsolved), while Figure 3e shows dNPIM is more robust across the difficulty spectrum. This gives practical deployment guidance and demonstrates methodological maturity.

- **Honest and transparent presentation of limitations.** The paper explicitly discusses the timing confound in Table 1 (lines 172–173, attributing it to dense vs. sparse implementation), the bootstrapping failure mode (Section 4.3), and the need for fine-tuning across distributions (Section 4.4). This transparency strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

- **The timing confound in Table 1 weakens the practical competitiveness claim for large instances.** On MIS-large and MaxCut-large, dNPIM reports 1:20 (minutes) while DiffUCO and SDDS report 0:02–0:03 — two orders of magnitude slower. The paper attributes this to a dense PyTorch matrix product vs. the sparse library used in competing work, but this remains speculative. While the paper acknowledges the issue in text, Table 1 presents all entries in the same format without any visual distinction (e.g., a footnote, asterisk, or color coding) flagging that the large-instance times are implementation-confounded. A reader scanning the table would reasonably infer that dNPIM is not practically competitive on large instances. The G-set results (Table 2, which uses the implementation-agnostic TTS metric) provide cleaner evidence of algorithmic competitiveness, but the neural CO benchmark presentation undermines the paper's broader competitiveness claims.

- **Training distribution dependence is a significant practical limitation that is under-acknowledged in the paper's framing.** The method requires fine-tuning for different problem sizes (Fig 3a), hardness parameters (Fig 3d), and can only be trained from scratch on easier instances (Section 4.3's bootstrapping failure mode). The paper's abstract claims "efficient and scalable algorithms," but the method is essentially a distribution-specific learned solver: it works well on the distribution it was trained on but degrades predictably under shift. Classical Ising machines (CAC, CFC, dSBM) work out of the box on any instance of a given class with only hyperparameter tuning, whereas NPIM requires a separate training/fine-tuning pipeline per target distribution. This contrast is not discussed, and the scope of the "scalable" claim should be qualified.

### Minor

- **The evaluation only varies problem size and hardness parameter, not graph structure.** The OOD experiments (Section 4.4) vary SK problem size and WPE hardness, but do not test whether learned dynamics transfer across structurally different graph families (e.g., train on SK, test on random regular graphs or G-set random graphs). This leaves open the question of whether the method learns a generalizable strategy or just a distribution-specific heuristic. A negative result would also be informative.

- **The "top 30" strategy in Table 1 introduces an asymmetry.** dNPIM runs 30 parallel trajectories and selects the best, while the reported competitor results (DiffUCO, SDDS) appear to be per-trajectory. The footnote justifies this by saying dNPIM per-trajectory cost is lower, but without a per-trajectory ablation the reader cannot assess how much of dNPIM's solution quality advantage comes from the learned dynamics vs. the multi-trajectory search. This is not a fatal flaw but a clarity concern.

### Trivial
None.

## Nice-to-Haves
- A wall-clock-time vs. solution quality scatter plot for the neural CO benchmarks (Table 1) would turn the timing confound into an informative trade-off visualization.
- Comparison with a simpler learned baseline (e.g., tuning just the diagonal terms of a Hopfield network or a single learned parameter) would help isolate the benefit of learning full dynamics.
- A complexity analysis of the zeroth-order training procedure (function evaluations per epoch, scaling with parameter count) would help practitioners assess training cost.

## Removed Points
- **Point 3 (justification for zeroth-order optimization deferred to Appendix E):** REMOVED. The main text (Section 2.4) provides a clear conceptual justification (vanishing/exploding gradients make backprop infeasible; policy gradient gives noisy reward attribution over many small steps). Appendix E would contain supporting numerics. Per hard rule: the parser strips appendix content; the appendix exists in the original submission. The conceptual justification in the main text is adequate for a reader to understand the motivation.
- **"Formattings nitpicks" from the strength finder about Fourier basis selection:** REMOVED. The paper already notes in Section 3.3 that "the specific choice of temporal basis... has only a minor effect on performance," which adequately addresses this concern.
- **Generic "strengths" from strength finder about the problem being important:** REMOVED per the filtering rule — these are generic and lack specific evidence linking to the paper's contributions.

## Novel Insights
The most insightful observation emerging from the reviews is that the paper's analysis of learned dynamics (Section 4.1) is itself a significant contribution that goes beyond what most neural CO papers provide. The demonstration that a network can spontaneously learn momentum as an emergent property from a simple success-rate objective — and that this can be directly visualized and interpreted in terms of network weights — gives the community a concrete example of "algorithm discovery" through learning. This stands in contrast to the typical neural CO paper that reports benchmark tables with little understanding of what was actually learned. The contrast between cNPIM and dNPIM (continuous vs. discrete coupling) further enriches this picture by showing that coupling choice affects whether the model overfits to easy instances or maintains robustness. These insights suggest the method is not just a black-box solver but a framework for studying what dynamics are effective for Ising problems.

## Suggestions
1. Add a footnote or asterisk to Table 1 explicitly noting that the timing for dNPIM on large instances is implementation-confounded (dense PyTorch vs. sparse library) and may not reflect algorithmic superiority.
2. In the abstract and introduction, qualify the "scalable" claim to clarify that the method requires per-distribution training/fine-tuning, unlike classical Ising machines.
3. Include a cross-structure generalization experiment (e.g., train on SK, test on G-set random graphs) to clarify the method's transferability scope.
4. Provide an ablation on the number of parallel trajectories ("top 30") to show how solution quality varies with trajectory count.

## Score and Decision

### Calibration Report

**Round 1 (bracketing):** Three queries on neural CO / Max-Cut / algorithm unrolling topics.

| Paper | Avg Score | Round | How it compares |
|---|---|---|---|
| iWCfiDxLIY (GREAT — edge-based GNN for TSP) | 3.00 | R1 | Much weaker — limited novelty, weak experimental support |
| SrnTGdJKYG (Neural Deconstruction Search for VRP) | 3.00 | R1 | Much weaker — limited scope, incremental |
| OcTUquFXfx (Global minima of energy landscapes) | 2.60 | R1 | Different domain, weaker |
| NIhRwzqhUz (Partially Dynamic TSP) | 3.00 | R1 | Much weaker — limited novelty |
| CpiJWKFdHN (ROS — GNN for Max-k-Cut) | 5.67 | R1/R2 | Similar domain. ROS faced concerns about limited novelty (similar to prior work) and missing baselines. NPIM has clearer novelty (first algorithm unrolling for NP-hard CO) and stronger analysis (momentum emergence, cNPIM vs dNPIM). **NPIM is somewhat stronger.** |
| 9qtswuW5ux (QRF-GNN — GNN for QUBO) | 4.25 | R1 | Incremental over PI-GNN; limited novelty. NPIM is clearly stronger in novelty and analysis depth. |
| yEwakMNIex (RedCO — Unified neural solvers) | 6.25 | R2 | Accepted. More comprehensive in scope (multi-task CO), but concerns about scalability and applicability. NPIM has better analysis depth but less breadth. **NPIM is slightly weaker.** |
| 6JDpWJrjyK (DISCO — diffusion solver for CO) | 5.75 | R2 | Rejected. Incremental novelty concerns. NPIM has stronger novelty. |
| CFLEIeX7iK (Neural solver selection) | 5.75 | R2 | Rejected. Limited novelty over existing algorithm selection. |

**Round-1 bracket:** 5.5 – 6.5.

**Round 2 (narrowing):** Compared against the most topically similar anchors. NPIM is clearly above the 4.25 (QRF-GNN) and 5.67 (ROS) rejected papers in terms of novelty and analysis quality, but below the 6.25 accepted RedCO paper in comprehensiveness. The timing confound in Table 1 and the training distribution dependence are real concerns that hold it below 6.25.

**Final score rationale:** The paper presents genuine novelty (algorithm unrolling for NP-hard CO) and unusually strong analysis (momentum emergence, coupling comparisons), supported by competitive G-set results. The main weaknesses (timing confound, distribution dependence) are real but acknowledged. The paper sits at **6.0**, above typical rejected neural CO papers (4-5.75 range) but below comprehensive accepted works (6.25+).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>