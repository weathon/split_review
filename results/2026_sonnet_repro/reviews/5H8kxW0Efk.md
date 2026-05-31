Now I have a good understanding of the paper. Let me run calibration searches.Let me read the two most relevant middle-band anchors:Now I have enough information. Let me write the final consolidated review.

---

## Summary

This paper proposes Neural Network Ising Machines (NPIM), a new approach that applies algorithm unrolling to Ising machine dynamics for combinatorial optimization. The update function of an iterative Ising machine is parameterized by a compact MLP with time-varying weights expressed in a Fourier basis, trained using a zeroth-order evolutionary strategy (ES) directly against instance reward. Two variants are studied — cNPIM (continuous) and dNPIM (discrete coupling) — and the method is benchmarked against both state-of-the-art neural-CO methods (Table 1) and physics-inspired Ising machine baselines (Table 2). The paper also provides an interpretive analysis showing that the trained network learns to exhibit momentum-like behavior, emerging spontaneously from reward maximization.

---

## Strengths

- **Genuinely novel combination of ideas**: The paper is, to the best of reviewers' knowledge, the first to apply algorithm unrolling to NP-hard CO, and the first to train a neural Ising machine update rule end-to-end via ES. The Fourier basis parameterization of time-varying weights is a clean and principled design choice.

- **Interpretable learned dynamics**: Section 4.1 and Figure 2 provide compelling evidence that the learned algorithm is doing something nontrivial — a single-layer network with fixed weights evolves from greedy descent (all-negative weights) to a momentum-like search (some positive weights) over training, directly correlated with improved ground-state finding. This is concrete, specific, and scientifically interesting.

- **Competitive benchmark results**: dNPIM achieves the best average objective value on 4 of 5 neural-CO benchmarks in Table 1 (MIS-small, MIS-large, MaxCut-small, MaxCut-large) and outperforms CAC, CFC, and dSBM on 4 of 5 G-set Max-Cut groups in Table 2, providing broad empirical validation of the approach.

- **Discrete coupling robustly reduces overfitting**: Section 4.5 and Figures 3b/3e demonstrate a clear behavioral distinction: cNPIM achieves lower median TTS but completely fails on the hardest instances, while dNPIM maintains more uniform performance. This insight about the failure mode of continuous relaxation is specific, grounded, and practically important.

- **Effective bootstrapping enables scaling**: Figures 3a and 3d show that fine-tuning a network pretrained on easier/smaller instances unlocks performance on larger or harder distributions (e.g., N=100→500 SK, WPE hardness transfer), with clear empirical evidence that this is necessary and effective.

---

## Weaknesses

### Fatal
None.

### Major

- **Table 1 comparison is not compute-normalized for the two largest benchmarks.** The caption explicitly states that dNPIM is run "30 times in parallel" and the best solution used, justified by being "less computationally intensive per trajectory." For MIS-large and MaxCut-large, dNPIM takes 1:20 wall-clock versus 0:03 for DiffUCO/SDDS — a 27× difference. For MIS-small, MaxCl-small, and MaxCut-small, the time is comparable (0:02 each), so the comparison is fair there. But the two cases where NPIM claims the most impressive numerical gains (MIS-large: 40.297 vs. 39.97; MaxCut-large: 2988.551 vs. 2974.60) are also the cases with the largest runtime disparity. The paper does not show whether dNPIM at matched compute (one trajectory, 0:03 budget) achieves similar advantages. This is not necessarily fatal — the reported numbers may hold at matched cost — but the paper does not demonstrate this.

- **Table 2 TTS is measured in iterations, but the per-iteration MLP cost is unaccounted for.** The paper justifies this metric by stating: "the compute intensive matrix vector product is the computational bottleneck for each algorithm." However, the NPIM dynamics add a per-iteration MLP forward pass over a context buffer of depth $T_c$, applied to all $N$ spins at each step. Baseline algorithms (CAC, CFC, dSBM) have only simple closed-form updates without any neural component. For large $N$ and nontrivial $T_c$/$D$, this MLP pass may not be negligible relative to the $O(N^2)$ matrix-vector product. The paper does not measure or bound this overhead. If the MLP pass adds 20–30% to wall-clock time, the claimed 3–4× TTS advantage over CAC in some groups (e.g., N=800, T, +/-: 5.51e+04 vs 3.38e+05) could be partially eroded. The claim of iteration-count equivalence to wall-clock time needs empirical validation.

### Minor

- **Training cost and bootstrapping process are undercharacterized.** The paper states that "training a network from scratch at the larger problem size ($N=500$) is not possible" (Section 4.3) and that for G-set benchmarks, a separate fine-tuning is performed for each graph type (Section 5). However, the paper never reports how long training takes (GPU hours), how many training instances are needed for each fine-tuning stage, or how sensitive the results are to the choice of training distribution. Competitors (CAC, CFC, dSBM) also tune hyperparameters per instance type, so the spirit of comparison is fair, but the practical cost of achieving the reported NPIM numbers remains opaque. This limits reproducibility and makes it hard to assess the overall compute budget.

- **The TTS target computation is ambiguous when NPIM exceeds Goto et al. (2021) cut values.** The paper states: "We use the cut values reported in these works when computing TTS." If dNPIM finds a higher cut value than the Goto et al. target on any instance (plausible given Table 1's trend), TTS for that instance would be evaluated against a target that was already beaten — potentially inflating the apparent TTS advantage. The paper should clarify whether any target cut values were exceeded and, if so, how TTS was computed for those instances.

- **cNPIM's failure on hardest instances is underweighted.** Section 4.5 and Figure 3b show that despite achieving better median TTS, cNPIM places many hard instances on the "never solved" horizontal line. The paper's framing that "cNPIM achieves larger reward and smaller TTS for median difficulty" buries the practical significance of this worst-case failure. For applications where any hard instance must be solved, cNPIM is disqualifying. Since the paper's main claims rest on dNPIM, this is worth clearer disclosure.

### Trivial

- The nonlinear activation $f_{\text{nl}}(x) = x + \tanh(x)$ in Eq. (5) is not motivated beyond being a nonlinear activation. A sentence explaining why this specific choice was made (or confirming insensitivity) would be helpful.

---

## Nice-to-Haves

- A compute-matched version of Table 1 (single dNPIM trajectory at the same 0:02–0:03 budget as DiffUCO/SDDS) would substantially strengthen the neural-CO comparison claims.
- Wall-clock profiling of the MLP forward pass overhead relative to the matrix-vector product in the NPIM loop, even a single data point, would validate the iteration-count TTS metric.
- The analysis in Section 4.1 (emergence of momentum) is the most scientifically interesting part of the paper. Extending this analysis to G-set instances — showing whether the same momentum-then-annealing structure emerges for structured graphs — would make the contribution more compelling.
- Framing the bootstrapping procedure explicitly as curriculum learning, with a description of the curriculum and its training distribution, would help readers reproduce the training regime.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[REMOVED] Novelty of algorithm unrolling vs. GNN-based learned-iterate CO**: The harsh critic raised a concern that the boundary between NPIM and GNN-based methods is blurry. This is speculative — the paper provides a concrete technical distinction (parameterizing the update function of a dynamical Ising machine with a small time-modulated MLP trained via ES, rather than message-passing over a graph). The novelty claim stands as stated.

- **[REMOVED] Maximum dominating set omission**: The paper gives a principled reason for this omission: "not directly mappable to the quadratic Ising problem." MIS and Max-Clique are equivalent to the Ising problem (Section 3.1, Appendix A), so their inclusion is consistent. This is not an inconsistency.

- **[REMOVED] Missing related works**: Per hard rules, we do not critique missing citations.

- **[REMOVED] Reward function definition deferred to appendix**: This is an appendix stripping artifact. The reward function is defined in Appendix F of the original submission. The paper does describe the training setup and references the functional form in Section 3.4.

- **[REMOVED — Strength Finder's generic strengths]**: "Simplicity and flexibility of the method make it generalizable" — too generic. "Method avoids gradient issues by using ES" — this is true but is simply a restatement of the design choice; not an independent strength.

- **[REMOVED] Hardware specification details (batch size, parallelism matching)**: The paper states "NVIDIA A100 GPU" in Table 1's caption and notes that implementation differences (sparse vs. dense libraries) could explain speed differences. Demanding full replication-level hardware specification is beyond the scope of the paper.

---

## Novel Insights

The paper's most novel scientific contribution is that a simple Fourier-basis-parameterized MLP, when trained by ES purely for reward, spontaneously learns dynamics qualitatively analogous to physically-motivated Ising machine heuristics (momentum, annealing) — without any explicit physical prior. This "emergence" result (Section 4.1, Figure 2) is concrete and verified, and suggests that algorithm unrolling may be a general and interpretable framework for discovering effective heuristic search dynamics, not just for Ising problems but potentially for a wider class of discrete optimization problems. The comparison between cNPIM and dNPIM also yields an underappreciated insight: continuous relaxation during learning can produce algorithms that optimize a proxy landscape that diverges from the true discrete problem on hard instances, while discrete coupling enforces faithfulness to the original search space at the cost of per-instance speed.

---

## Suggestions

1. Add a single table row or figure showing dNPIM's performance on MIS-large and MaxCut-large with a matched 0:03 time budget (single trajectory), to demonstrate whether the advantage over SDDS holds at equal compute.
2. Profile and report the MLP forward-pass overhead (e.g., fraction of total wall-clock time per iteration) for the G-set experiments at $N=800$, to justify the iteration-count TTS metric.
3. Report total training time (GPU hours) and approximate number of training instances used for each fine-tuning stage in the main text (even a rough number), to make the practical cost of achieving the reported results transparent.
4. Clarify in Table 2 or its caption whether any NPIM solutions exceeded the Goto et al. (2021) cut targets, and how TTS was computed for those instances.

---

## Score Calibration

**Round 1 anchors:**
- NIhRwzqhUz (3.0): Dynamic TSP, rejected — much simpler contribution, lower quality.
- BlSIKSPhfz (6.0): Hybrid continuous-discrete Ising dynamics, accepted — closely related topic.
- 9EfBeXaXf0 (6.75): QQA for CO, accepted — competitive learning-based solver.
- 5t57omGVMw (8.0): Learning solver parameters (linear systems) — theoretical guarantees, higher rigor.

**Initial bracket: 5.5–7.0**

**Round 2 anchors:**
- BlSIKSPhfz (6.0): Less novel than NPIM (combines two existing methods without learned parameterization), inconsistent empirical results, accepted. NPIM is more novel but has evaluation gaps — roughly comparable.
- 9EfBeXaXf0 (6.75): QQA for CO with broader benchmarks, cleaner compute-matched evaluation, accepted. NPIM's evaluation has gaps relative to this.
- CpiJWKFdHN (5.67): GNN-based Max-k-Cut solver, rejected — less novel, fewer baselines. NPIM is clearly stronger.
- yEwakMNIex (6.25): Unified neural solver for CO, accepted — broader problem scope but similar novelty level.
- T5Xb0iGCCv (6.67): Neur2RO for robust optimization, accepted — cleaner methodology and evaluation.

**Narrowing:** NPIM is stronger than BlSIKSPhfz (6.0) in novelty and breadth of results, but the compute normalization issue in Table 1 and the unvalidated iteration-count TTS metric in Table 2 prevent it from reaching 9EfBeXaXf0 (6.75) or T5Xb0iGCCv (6.67). The paper is closest to BlSIKSPhfz + a small upward premium for novelty and cleaner architecture, settling at **6.0**.

---

**Originality:** High — first application of algorithm unrolling + ES to NP-hard CO; novel Fourier-basis weight parameterization  
**Importance of research question:** High — learned Ising machine dynamics is an active frontier  
**Claims vs. evidence:** Moderate — some benchmark claims oversell due to compute gaps  
**Soundness of experiments:** Moderate — methodology sound, execution has gaps (compute normalization, TTS metric justification)  
**Clarity:** Good — well-organized, honest about limitations  
**Value to community:** Good — competitive performance, interesting analysis, flexible framework  

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>