## Summary

WeCAN is an end-to-end reinforcement learning framework for heterogeneous DAG scheduling featuring task-pool compatibility coefficients. The paper's three main contributions are: (1) a weighted cross-attention (WeCA) layer that integrates compatibility coefficients multiplicatively outside the softmax normalization to embed environment information while preserving adaptability to varying pool/task type counts; (2) a longest-directed-distance GNN (LDDGNN) to capture task dependency structure; and (3) a single-pass skip-action mechanism, backed by theoretical analysis of the optimality gap in list-scheduling-based generation maps, which enables the scheduling policy to represent optimal solutions via a surjective generation map. The approach achieves up to 18.1% makespan improvement over the best heuristic and up to 9.5% over the best neural baseline on TPC-H and Computation Graph benchmarks.

---

## Strengths

- **WeCA outside-softmax design with principled motivation and ablation evidence.** Section 3.1 motivates the outside placement with a concrete counterexample: two tasks with identical attributes but different compatibility profiles receive identical embeddings under the inside (log-form) variant, while the outside variant distinguishes them. Table 3 confirms this quantitatively—replacing WeCA with its inside variant raises TPC-H-30 makespan from 19908 to 20729 (~4% degradation), and removing WeCA layers almost entirely eliminates improvement over Tetris (0.5% vs. 14%).

- **Skip-action mechanism with formal surjectivity grounding.** Section 4 and Theorem 1 rigorously characterize the optimality gap of list scheduling and demonstrate that the skip-augmented generation map forms a surjection onto feasible schedules. Figure 3 validates this directly: WeCAN with skip achieves 8.3–8.9% improvement over HEFT on the heavy-task benchmark, while WeCAN without skip loses 2.3–0% relative to that heuristic, and CP regresses further (−4.8%/−3.9%).

- **Consistently strong and statistically reported empirical results.** Tables 1 and 2 cover TPC-H instances with 275–918 tasks and three Computation Graph types, with means and standard deviations over random seeds. WeCAN-S(256) achieves best-in-class across all six benchmarks, demonstrating robustness.

- **Robust cross-environment generalization.** Figure 2 shows that WeCAN-S(256) maintains 6.7–20.4% improvement over the best heuristic under four out-of-distribution environment fluctuations (more pools, pool types, tasks, task types), substantially outperforming One-Shot-S(256) (0.9–10.2%), directly validating the architecture's adaptability claim.

- **Computational efficiency at single-pass quality.** WeCAN-Greedy runs in 0.15–1.72 s on TPC-H instances (vs. HEFT 0.18–1.86 s), and even WeCAN-S(256) at 2.43–10.43 s remains within the same order of magnitude as One-Shot-S(256), while delivering markedly better makespan.

- **LDDGNN superiority validated against alternatives.** Table 3 shows that both forward GAT (20747) and bidirectional GAT (20873) underperform LDDGNN (19908) on TPC-H-30, providing direct ablation evidence for the DAG-specific GNN design.

---

## Weaknesses

### Fatal
None.

### Major

- **PRO-BALM baseline appears in Figure 3 without any introduction, citation, or description.** The table accompanying Figure 3 lists five conditions—WeCAN-S(256), WeCAN-inside-S(256), PRO-BALM, WeCAN-S(256) (no-skip), and CP—but "PRO-BALM" is never defined, named, or cited anywhere in the main text. Without knowing what PRO-BALM is (a prior method? an ablation variant?), readers cannot assess whether WeCAN's 8.3–8.9% improvement represents a meaningful or modest gain relative to this intermediate point. The Figure 3 results are the primary empirical validation of the skip-action mechanism's benefit, so this gap directly undermines the key ablation.

- **No comparison against RL baselines that the paper explicitly critiques.** Section 1 names Wang et al. (2025) and Zhadan et al. (2023) as directly related heterogeneous RL schedulers with specific methodological deficiencies (compatibility averaging, fixed-size embeddings). Yet neither appears in the experimental comparisons—only PPO-BiHyb (Wang et al., 2021) and One-Shot (Jeon et al., 2023) are included as RL baselines. Given that the paper builds its architectural motivation directly on the limitations of these omitted methods, showing a head-to-head result (or explicitly stating why these cannot be run on the problem setup used) is necessary for a complete empirical case.

### Minor

- **Skip-action ablation is confined to the modified heavy-task benchmark, making its contribution on standard benchmarks ambiguous.** Table 3's ablation rows do not include skip vs. no-skip on TPC-H-30/50 standard benchmarks. WeCAN-S(256) achieves 18964 in Table 1 while "WeCA+LDDGNN" in Table 3 achieves 19908 on TPC-H-30—a ~5% gap that could be attributable to skip, sampling strategy differences, or model configuration differences. The paper cannot currently tell the reader whether skip helps on standard (non-heavy-task) instances, which matters for understanding when to use it.

- **TPC-H dataset is substantially modified but the modification's scope is underemphasized.** Section 5.1 states: "We use the version sorted by Wang et al. (2021), and add additional random memory constraints and task types." These additions constitute a significant departure from the original TPC-H benchmark, making results not directly comparable to any prior work using standard TPC-H. A brief clarifying sentence about why these modifications were necessary would help readers calibrate the results.

### Trivial

- **The skip coefficient functional form $u_{\pi_{skip}} = u_a(1-k/2n)^{u_b} + u_c$ is presented as principled but not ablated against simpler alternatives** (e.g., linear decay $u_a(1-k/2n) + u_c$). The paper correctly explains *why* the form must be monotone decreasing in $k$, but not why this polynomial form is preferred. This is a minor concern—the form is mathematically adequate and empirically validated—but a brief discussion or simple comparison would round out the justification.

---

## Nice-to-Haves

- **Quantitative comparison against an exact solver (e.g., Gurobi on MILP formulation) on small instances.** The paper establishes a MILP formulation in Section 2.1 and frames skip as closing an optimality gap. Showing how far from optimal WeCAN lands—even for 20–30 node problems—would directly quantify the residual gap and ground the theoretical claims empirically.

- **Training convergence curves comparing skip vs. no-skip.** Section 4.2 argues that the skip design "clusters most poor solutions in the high-$u_a$, high-$u_c$ region," reducing training variance. A reward-variance or convergence-speed comparison between skip-enabled and skip-free training would concretely validate this structural claim, which is currently asserted without direct empirical support.

- **Promoting to main text the quantitative analysis of skip benefit vs. heavy-task fraction.** The paper references (in Section 4.2 and Appendix C) that skip benefit grows with heavy-task percentage. Including even one figure in the main paper showing this trend would directly connect the theoretical prediction to empirical validation without requiring readers to consult the appendix.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The skip score functional form is a fatal/structural problem"** (Harsh Critic framing elevated this to near-structural): The paper provides functional justification (monotone decreasing, prevents endless idling, preserves single-pass efficiency) and Theorem 1 part iv proves the form is sufficient. The lack of an ablation comparing polynomial vs. linear decay is a minor evidential gap, not a structural flaw. Demoted to Trivial.

- **"Theorem 2 is tautological"** (Harsh Critic): The critic notes that Theorem 2 essentially says "a map satisfying Assumption 1 can find an optimal solution." While the theorem statement is indeed downstream of the assumption, the non-trivial contribution is the proof in Appendix A that the skip-augmented map satisfies Assumption 1. Since appendix proofs exist in the original submission, this criticism is not a valid weakness. Removed.

- **"Section 4.2's claim about clustering poor solutions in high-$u_a$, high-$u_c$ region is asserted without training curve evidence"**: Valid observation as a nice-to-have, but the theoretical argument in Section 4.2 is internally consistent even without empirical training curves. Moved to Nice-to-Haves.

- **"Time comparison between WeCAN-S(256) and One-Shot-S(256) needs deeper analysis"** (Harsh Critic): The paper explains this (generation map runtime dominates), and the observation holds qualitatively. The absence of a formal runtime breakdown is not a scientific flaw. Removed.

---

## Novel Insights

The skip-action mechanism is noteworthy not just as an engineering trick but as a theoretical bridge: the paper formalizes the observation that list scheduling is an injection rather than a surjection onto feasible schedules, proves this creates an irreducible optimality gap in specific problem classes (heavy tasks), and then constructs an enlarged reduced space (via skip) that restores surjectivity without multi-round inference. The design principle that maps poor solutions into a concentrated region of parameter space (high $u_a$, high $u_c$) to reduce training variance is a structurally interesting and transferable idea for neural combinatorial optimization methods that rely on generation maps more generally. The WeCA outside-softmax placement for compatibility coefficients likewise captures a general principle: for attention mechanisms over heterogeneous resources, weighting after normalization (rather than in log form before normalization) preserves absolute compatibility magnitude rather than just relative compatibility rank.

---

## Suggestions

1. Define and cite PRO-BALM in Figure 3 explicitly—this is critical for the ablation to be interpretable.
2. Add a row to Table 3 (or a supplementary table) showing WeCAN without skip on the standard TPC-H benchmarks, so the skip contribution can be isolated from the WeCA/LDDGNN contribution.
3. For RL baselines from the heterogeneous scheduling literature (Wang et al., 2025; Zhadan et al., 2023), either add a direct comparison or add one sentence to Section 5.1 explaining why these cannot be evaluated on the modified TPC-H setup.
4. Clarify that the TPC-H results use a modified version with memory constraints and task types added, to avoid confusion with unmodified TPC-H results in prior work.

---

## Evaluation on Key Axes

**Originality:** High. The WeCA outside-softmax design, LDDGNN, and the formal surjectivity analysis of skip action are all technically novel. The connection between list-scheduling's injection property and its optimality gap is a crisp conceptual contribution.

**Importance of research question:** High. Heterogeneous DAG scheduling with compatibility coefficients is directly relevant to data centers, ML compilers, and cloud platforms. The identified gap (adaptability to variable pool/task configurations without fixed embeddings) is practically significant.

**Claims well-supported:** Mostly yes, with the exception of PRO-BALM being undefined in Figure 3 and missing comparison against Wang et al. (2025)/Zhadan et al. (2023), the paper provides strong empirical evidence. The theoretical claims are formally stated and proof-sketched.

**Soundness of experiments:** Good. Tables 1 and 2 include standard deviations, the ablation study in Table 3 is systematic and covers all key components, and Figure 2 explicitly tests generalization to unseen environments. The skip ablation is the weakest section due to PRO-BALM ambiguity.

**Clarity of writing:** Good overall with a localized serious gap: PRO-BALM in Figure 3 is undefined. The paper is otherwise well-organized.

**Value to the research community:** High. The WeCA mechanism and the surjectivity-based skip analysis are transferable ideas. The empirical benchmarks (TPC-H + Computation Graphs) provide concrete reference points.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>