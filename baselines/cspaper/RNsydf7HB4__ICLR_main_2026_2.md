---
job_id: 4a31a74d-5b8f-4350-8b21-eb71fd7e6396
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: RNsydf7HB4.pdf
paper: GAMA: A Neural Neighborhood Search Method with Graph-aware Multi-modal Attention for Vehicle Routing Problem
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through reinforcement learning, learning on graphs, and learned optimization for combinatorial search in VRP.

## Minimum Quality
Pass ✅. The paper contains the expected core sections, including abstract, introduction, related work, methodology, experiments/results, and conclusion. While there are substantial issues in technical clarity, experimental rigor, and positioning, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes GAMA, a learning-to-improve method for CVRP that formulates operator selection in local search as an RL problem. The method encodes the problem instance graph and the current solution graph with a dual GCN backbone, then applies self-attention, cross-attention, and gated fusion to build a state representation for PPO-based operator selection. Experiments on synthetic CVRP instances and selected benchmark instances report improvements over several neural baselines, together with ablations on the attention and gating components.

## Strengths
1. The paper addresses a meaningful problem setting. Learning adaptive operator selection for VRP local search is a sensible and relevant direction, especially because many learned routing methods still struggle to match strong improvement-based search pipelines once solution quality, rather than raw inference speed, becomes the focus.

2. The state representation is richer than in older operator-selection approaches that only use coarse scalar search statistics. Encoding both the distance graph and the evolving solution graph is a reasonable design choice, and the paper makes a plausible case that these are complementary modalities.

3. The architectural decomposition is intuitive. In **Figure 1**, the pipeline from current instance/solution to dual graph encoding, attention-based fusion, and operator selection is visually clear and helps understand the intended data flow. In particular, the figure makes explicit that the method is not merely concatenating handcrafted features with a graph embedding, but trying to model interactions between instance geometry and current routing structure before policy prediction.

4. The empirical comparison against neural learning-based baselines is reasonably broad in the main paper. **Table 1** includes both learning-to-construct methods and learning-to-improve methods, and the results suggest that GAMA is competitive, especially on larger synthetic instances. On CVRP100, for example, GAMA at \(T=20k\) reports better average cost than DACT and L2I.

5. The ablation direction is appropriate. **Table 2** and **Figure 2** attempt to isolate the effects of cross/self-attention and gated fusion, rather than treating the encoder as an inseparable black box. Even though I have concerns about interpretation, it is still a strength that the paper tries to test these components explicitly.

6. The generalization experiment, although limited, is directionally useful. **Table 3** indicates that the method can transfer zero-shot to benchmark instances larger and structurally different from the training distribution, which is an important property for learned search methods.

## Weaknesses
1. **The paper has multiple technical inconsistencies and underspecified equations in the core method, which weakens confidence in soundness.**  
   The most obvious example is in **Equation (3)** on **Page 6**, where the paper defines
   \[
   Q_m = H W_m^Q,\quad K_m = H W_m^Q,\quad V_m = H W_m^V.
   \]
   This sets \(K_m\) equal to \(H W_m^Q\) rather than \(H W_m^K\), despite the text stating that \(W_m^Q, W_m^K, W_m^V\) are separate learnable projections. This is either a typo in a central equation or an actual modeling mistake. If it is a typo, it should have been caught; if it is intentional, the architecture differs from standard self-attention and needs justification. This matters because the claimed contribution hinges on the attention design, and errors in the definition of attention projections directly affect reproducibility and the validity of the claimed mechanism.

2. **The MDP and reward specification are confusing and at places internally inconsistent.**  
   On **Page 3**, the state is denoted \(s_t\), then the encoder maps the current state “into a unified representation \(s_t\)” again, overloading the symbol and blurring the difference between raw state and learned embedding. On **Page 4**, the reward is defined as
   \[
   r_t = f(\delta_0) - f(\delta_{(k)}^*), \forall t \in \mathcal{T}_k,
   \]
   where all transitions in a phase receive the same terminal phase reward. But **Algorithm 1** defines \(r^{(k)} = f(\delta^{(0)}) - f(\delta_{(k)}^*)\) at line 19, with phase indexing that is not aligned cleanly with the earlier notation. It is also unclear whether PPO is trained with delayed sparse rewards only at shake boundaries, whether intermediate rewards are zero, and how episode truncation interacts with unfinished phases. These are not cosmetic details. In policy gradient training, reward assignment and trajectory segmentation are central to the optimization problem, and ambiguity here makes the method difficult to assess or reproduce.

3. **Algorithm 1 contains several apparent errors or at least highly confusing statements.**  
   On **Page 4**, line 9 has a malformed policy selection expression \(a_t \leftarrow \pi_\theta(s_t))\). More seriously, line 13 updates the incumbent best solution as \(\delta^* = \delta_t\) when the condition checks whether \(f(\delta_{t+1}) < f(\delta^*)\). This looks wrong; the update should presumably use \(\delta_{t+1}\). Line 16 manually increments \(t=t+1\) inside a `for timestep t = 1 to T` loop, which is algorithmically inconsistent. These are not small editorial blemishes because the algorithm is the paper’s operational core. When pseudocode has state-update mistakes and loop-control inconsistencies, it raises reasonable concern that the implementation details may diverge from the written method.

4. **The paper overstates the empirical conclusions relative to what the tables actually show.**  
   In **Section 4.3** on **Page 8**, the text says GAMA “maintains superior solution quality across all instance sizes” relative to classical solvers. But **Table 1** does not support that as written. On CVRP20, HGS average cost is 6.0812 and GAMA \(T=20k\) average cost is 6.0810, which is only a tiny edge; on best cost, HGS is 6.0807 versus GAMA 6.0806, again extremely marginal. On CVRP50, GAMA \(T=20k\) average cost 10.3533 is close to HGS average 10.3548 and LKH3 best 10.3879 is worse, but the margin is still modest. These are not “significant” improvements in the ordinary sense unless backed by variance estimates or paired tests against the strongest baselines in the main table. The presentation repeatedly speaks in broad superiority language when the actual gains, especially on small and medium sizes, are often very small.

5. **The comparison against strong classical solvers is not fully fair or sufficiently analyzed.**  
   **Table 1** mixes “best cost”, “average cost”, and runtime, but LKH3 has no average cost entries at all, HGS has only one average, and neural methods are executed 30 times independently. This makes the comparison uneven. More importantly, the paper argues that GAMA is superior while also showing that strong hand-engineered methods such as HGS and LKH3 remain extremely competitive, especially at small sizes and often with better or comparable runtime. If the paper wants to claim practical relevance, it should analyze equal-time regimes or solution-quality-vs-time curves in the main paper, not only final values at fixed \(T\). As written, the evaluation is tilted toward validating the learned method rather than answering the more important question: when should one actually prefer GAMA over strong classical search?

6. **The ablation evidence is weaker than the narrative suggests, and some reported statistics are puzzling.**  
   In **Table 2** on **Page 8**, the gains on CVRP20 and CVRP50 are extremely small, sometimes at the fourth decimal place, yet the prose attributes them to meaningful representational advantages. On CVRP100, the gain is larger, but the standard deviation of GAMA is reported as **0.0215**, compared with **0.0042** for GAMA_NG and **0.0053** for GENIS. That is actually much higher variance for GAMA, which does not align cleanly with the paper’s stability claims. Then **Figure 2** is used to argue that GAMA has “notably lower variance and better median performance across all time budgets,” but the figure only shows CVRP50 and the visual differences are fairly modest. This creates a mismatch between the data and the interpretation. If the claim is lower variance, the authors need broader evidence and more careful statistical reporting.

7. **Important implementation details are deferred away from the main paper even when they are necessary to evaluate the method.**  
   The paper repeatedly says that key details are in the supplementary material, for example the full definition of \(\mathcal{G}_{\text{dis}}, \mathcal{G}_{\text{sol}}, \mathcal{X}_t\) on **Page 3** and the operator details in **Section 3.1**. Some of this information does appear later in the appendix, but in the main paper the method remains under-specified at crucial points. For instance, if \(\mathcal{G}_{\text{dis}}\) is a fully connected weighted graph, **Equation (2)** uses the standard normalized GCN propagation
   \[
   H = \sigma(\hat D^{-1/2}\tilde G \hat D^{-1/2} X W),
   \]
   but the paper never explains whether \(\tilde G\) contains raw Euclidean distances, similarities, thresholded neighborhoods, or some normalized adjacency. Using raw distances as adjacency weights is not innocuous, because larger distances then produce stronger propagation weights unless transformed. This is a mathematically important ambiguity, not a minor omitted detail.

8. **The method is only weakly positioned against the broader learned neighborhood-search literature, including graph-based operator-selection approaches.**  
   The paper cites a number of older and recent works, but the discussion of what is genuinely new relative to prior learned local search or neural neighborhood search is still thin. The proposed method is essentially a combination of dual graph encoders, cross/self-attention, gated fusion, and PPO-based operator selection. That may be a useful engineering combination, but the paper does not convincingly explain why this is more than a fairly incremental architectural remix over existing graph-based learned improvement frameworks. This matters because ICLR is not only about obtaining a better leaderboard number; it also requires sharp scientific positioning and a clear articulation of what conceptual bottleneck is being resolved.

9. **The generalization evaluation is not convincing enough for the strength of the claim.**  
   In **Section 4.4.3** and **Table 3** on **Page 9**, the benchmark evaluation is reduced to a single summary table of average and best gaps over a randomly sampled set of representative instances, while the per-instance details are pushed out of the main paper. The claim is that GAMA “consistently” generalizes better, but the main paper does not show which scales are hard, how performance varies with instance family, or whether the gains hold uniformly rather than being carried by a subset of sampled instances. Since generalization beyond the training distribution is one of the headline claims, the evidence in the main paper is too compact and selective.

10. **Presentation quality is below the standard expected for a method-heavy ICLR submission.**  
   Beyond the mathematical issues already mentioned, there are many writing and editing problems: duplicated or inconsistent notation, grammar issues, undefined references such as “Eq.equation LABEL:eq:eq:d” in **Section 4.3**, inconsistent definitions of \(e\) as \(\{-1,1\}\) on **Page 3** versus \(e=0/1\) in **Appendix A.3**, and stray references to “the proposed GENIS” in **Section 4.1** when the method is GAMA. These collectively make the paper feel insufficiently polished. For a paper whose main contribution is an architectural and algorithmic refinement, clarity is not secondary, it is part of the contribution.

11. **The figures help exposition, but they also expose a gap between conceptual clarity and experimental substantiation.**  
   **Figure 1** gives a fairly comprehensive architecture diagram, yet the paper never maps all of its blocks cleanly to a precise sequence of equations. For example, the figure includes self-attention, cross-attention, gate layers, residuals, FFN, and global optimization features, but the exact layer ordering and whether both modalities go through symmetric operations in every layer are not written as a coherent block update. Likewise, **Figure 2** is used to support the gating claim, but it is restricted to CVRP50 and inference budgets only, while the stronger claims are broader. The figures are useful, but they highlight that the paper tells a cleaner story visually than it proves textually.

## Questions
1. In **Equation (3)**, is \(K_m = H W_m^Q\) a typo, and should it be \(K_m = H W_m^K\)? If yes, please confirm all equations in the attention module and clarify whether the implementation follows standard separate \(Q/K/V\) projections.

2. Please provide a precise, unambiguous definition of the graph matrices used in **Equation (2)**. Is \(\mathcal{G}_{\text{dis}}\) an adjacency matrix, a distance matrix, a similarity matrix, or a thresholded graph? If it contains Euclidean distances directly, why is standard GCN normalization the right operation?

3. Can the authors clarify the exact reward assignment and PPO training pipeline? Specifically, are rewards only assigned when \(C_{notI}\geq L\), what reward is given to transitions before the first shake, and how are incomplete phases handled at episode end?

4. In **Algorithm 1**, should line 13 update \(\delta^*=\delta_{t+1}\) rather than \(\delta_t\)? Also, why is \(t=t+1\) manually updated inside a `for` loop? Please state whether these are pseudocode errors only, and if so, provide corrected pseudocode in the rebuttal.

5. The paper claims that GAMA has lower variance and better stability, but **Table 2** reports a notably larger standard deviation for GAMA on CVRP100 than the ablations. Can the authors reconcile this with the text, and ideally provide paired significance tests or confidence intervals against the strongest baselines?

6. For **Table 1**, could the authors provide a more controlled comparison under matched time budgets, especially against HGS and LKH3? This would substantially strengthen the practical relevance of the claims.

7. For the generalization claims in **Table 3**, please report the exact sampled benchmark instances in the main rebuttal and provide per-instance gaps, not just aggregated averages. I would also like to know whether the random sampling of benchmark instances was fixed before experiments.

8. What exactly distinguishes GAMA from the most closely related graph-based learned neighborhood-search/operator-selection methods beyond architectural layering? A sharper positioning statement would help assess contribution.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
N/A.

## Soundness Rating
2: fair. The overall idea is plausible and the empirical results are nontrivial, but the technical presentation contains enough ambiguities and inconsistencies, especially in the equations and algorithm specification, that the central claims are only partially supported.

## Presentation Rating
2: fair. The high-level story is understandable, and the figures help, but the paper has too many notation issues, pseudocode errors, undefined references, and imprecise claims for a stronger score.

## Contribution Rating
2: fair. The paper targets an important problem and reports some empirical gains, but the conceptual advance over prior graph-based learned improvement methods feels moderate, and the evaluation/positioning do not yet establish this as a clear ICLR-level contribution.

## Overall Rating
2: Reject, not good enough. The paper is promising and not without merit, but in its current form it falls below the bar due to a combination of under-specified mathematics, algorithmic inconsistencies, over-claimed empirical conclusions, and insufficiently sharp positioning against prior learned neighborhood-search methods.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The core problem setting and methodology are within my expertise, and I checked the equations, algorithm, figures, and main tables carefully.