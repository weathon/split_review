## Summary

The paper proposes Neural Network Parameterized Ising Machines (NPIM), which apply algorithm unrolling to dynamical Ising machines for combinatorial optimization. The update function of an Ising machine is parameterized by a small MLP whose weights are time-modulated using a Fourier basis, allowing the machine to learn adaptive annealing schedules. Training uses a zeroth-order (evolutionary) optimization method to sidestep vanishing/exploding gradient issues. Two variants—cNPIM (continuous coupling) and dNPIM (discrete coupling)—are evaluated against both neural CO baselines and physics-inspired Ising machines on Max-Cut, MIS, and G-set benchmarks, achieving competitive or state-of-the-art performance.

---

## Strengths

- **Novel and well-motivated combination**: The fusion of algorithm unrolling (L2O), dynamical Ising machines, and zeroth-order evolutionary optimization is genuinely new and clearly positioned relative to all three literatures. The choice of zeroth-order training over backpropagation or policy-gradient methods is well-justified by the vanishing/exploding gradient argument for long-horizon Ising trajectories, and supported by ablations in Appendix E.

- **Strong empirical results**: dNPIM achieves best-in-class results in 4/5 tasks in Table 1 (against DiffUCO, SDDS, LTFT) and dominates on most G-set categories in Table 2 (R,+ / R,+- / T,+- / P,+-), often by an order of magnitude in TTS, with only the unweighted planar instances being an exception.

- **Interpretable emergent dynamics**: Section 4.1 provides a concrete and insightful visualization of how momentum-like dynamics emerge from training: early-epoch networks learn greedy descent (all negative weights), while later-epoch networks develop positive weights that push the system out of local minima. This is a genuine scientific observation rather than just an ablation.

- **Parameter efficiency**: With as few as ~50 parameters, NPIM achieves strong competitive performance. The Fourier temporal basis is a principled and compact way to express smoothly varying annealing schedules without per-step parameters.

- **Empirical insight on cNPIM vs. dNPIM overfitting**: The paper characterizes an important behavioral difference—cNPIM effectively optimizes a relaxed continuous problem and "overfits" to easier instances while failing on hard ones (Figure 3b vs. 3e), while dNPIM is more balanced. This finding is practically useful and not obvious a priori.

---

## Weaknesses

### Fatal
None.

### Major

- **Scalability of training is a fundamental bottleneck**: The zeroth-order evolutionary strategy incurs overhead that grows with parameter count, limiting the network to ~50–100 parameters in practice. The authors acknowledge this in Section 6 but do not quantify the training cost scaling, nor do they demonstrate that the ~50-parameter saturation point is truly sufficient for harder or structurally different problem classes. For industrial-scale problems, this ceiling on expressivity may be limiting.

- **Fine-tuning per instance distribution reduces practical generality**: In Table 2, the model is fine-tuned *separately for each G-set graph type* (random/toroid/planar, weighted/unweighted). While instance-specific tuning is also done by the Ising machine baselines, this undermines the claim of a generalizable learned algorithm and raises the question of whether the performance difference is an algorithm advantage or a tuning advantage. The out-of-distribution results in Section 4.4 show clear degradation, and bootstrapping is necessary even to reach good training performance on large instances.

- **Wall-clock time comparison in Table 1 is unfavorable and the explanation is speculative**: dNPIM runs 30 parallel trajectories to reach "top 30" performance, which yields 1:20 minutes for MIS-large versus 0:03 for DiffUCO/SDDS (a ~26x slowdown). The authors attribute this to using dense PyTorch matrix operations rather than the sparse libraries used by competitors—but this is speculation, not a demonstrated equivalence. A fair comparison would require profiling or a sparse implementation.

### Minor

- **TTS in Table 2 is in units of iterations, not wall-clock time**: Different algorithms have different per-iteration cost, so reporting iteration-based TTS without a cost-per-iteration analysis prevents a full comparison of actual runtime efficiency.

- **Reward function is central to training but fully deferred**: The reward function (Appendix F, not included in the reviewed text) drives all training decisions, yet only its general form is described in the main paper. The paper cannot be fully evaluated without knowing whether the reward function introduces implicit biases.

- **The claim that NPIM beats CAC is instance-count sensitive**: Figure 3b shows that cNPIM achieves lower TTS on easy instances while *completely failing* (TTS → ∞) on several hard ones. The median-based comparison in Table 2 hides this variance. For applications requiring worst-case guarantees this is a meaningful distinction.

### Trivial

- Figure captions appear duplicated in the paper (once as an alt-text caption and once as a full descriptive caption), which is likely a parser artifact.

---

## Nice-to-Haves

- An empirical assessment of training wall-clock time vs. number of parameters would help readers understand how much the zeroth-order scalability bottleneck constrains practical use.
- A sparse-graph implementation experiment to verify whether the Table 1 time gap is indeed implementation overhead or algorithmic.
- A single end-to-end test on a non-Ising problem (e.g., SAT or TSP) even at small scale would greatly strengthen the generalization claim made in the discussion.

---

## Novel Insights

The central novel insight is that expressive Ising machine dynamics—including momentum, escape from local minima, and adaptive annealing—can emerge entirely from data-driven zeroth-order training of a compact MLP, without any hand-engineering of the update rule. The trajectory of network weights in Figure 2 constitutes qualitative evidence that the optimizer discovers physics-inspired heuristics organically. Additionally, the observation that continuous coupling (cNPIM) causes instance-wise overfitting to a relaxed problem while discrete coupling (dNPIM) produces more uniform generalization across hard and easy instances is a practically useful insight with design implications for future Ising machine architectures.

---

## Suggestions

- Provide a concrete breakdown of training cost (epochs × trajectories × problem size) for each benchmark setting to make reproducibility and scaling behavior clear.
- Consider a "soft discrete" intermediate (e.g., using a temperature-scaled sigmoid rather than a hard sign) to explore the cNPIM/dNPIM tradeoff space more systematically.
- Quantify the instance variance in Table 2 results (e.g., interquartile range of TTS) in addition to medians, so that instance-wise reliability is visible alongside average performance.

---

## Score and Decision

The paper makes a genuine and well-supported contribution at the intersection of algorithm unrolling, neural CO, and dynamical Ising machines. The novelty is real—not just a component swap but a demonstrated system that achieves competitive performance with an unusually small learned representation. The main weaknesses (training scalability ceiling, per-distribution fine-tuning, and a wall-clock disadvantage in Table 1) are significant but acknowledged and do not invalidate the core claims. The interpretability analysis is a scientific asset. Overall the paper is a solid contribution to the neural CO and Ising machine communities.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>