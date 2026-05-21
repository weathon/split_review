---
job_id: b9eacd6d-69c8-4f08-9860-ba8e2d3de9dd
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: RT5SlprCmc.pdf
paper: Learning the Minimum Action Distance
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly in scope for ICLR, focusing on self-supervised representation learning, metric learning, and reinforcement learning, with applications to planning and goal-conditioned RL.

## Minimum Quality
Pass ✅ The paper contains the expected scientific structure, including abstract, introduction, related work, method, experiments, results, and conclusion. There are important technical and empirical weaknesses, especially around incomplete specification of one objective and evaluation gaps, but they do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies how to learn the minimum action distance (MAD) between states in an MDP using only state trajectories, without rewards or action labels. The authors propose two learning objectives, MadDist and TDMadDist, that fit a trajectory-based quasimetric embedding, introduce a simple ReLU-based quasimetric, and evaluate the approach on a suite of environments with known ground-truth MAD, including asymmetric and stochastic settings. The paper also reports a downstream planning experiment in PointMaze-style environments using the learned distance as a heuristic.

## Strengths
The paper tackles a well-motivated problem. Learning a dynamics-aware state distance from trajectories alone, especially one that can represent asymmetry, is relevant to representation learning and goal-conditioned RL. The motivation in Sections 1 and 2 is clear, and the distinction between MAD and expected temporal distance is important and useful.

I appreciate that the paper explicitly focuses on asymmetry rather than quietly using a symmetric surrogate for an inherently asymmetric quantity. That matters in environments such as KeyDoorGridWorld and CliffWalking, and the paper is right to call out this mismatch in prior symmetric embedding methods.

The main empirical setup is reasonably broad. The environments span deterministic/stochastic dynamics, discrete/continuous spaces, and asymmetric transitions. The subset visualized in **Figure 2** helps communicate that the benchmark is not just one toy gridworld repeated several times. In particular, the inclusion of KeyDoorGridWorld and CliffWalking is well aligned with the paper’s asymmetry claim, while the OGBench mazes test longer-horizon structure.

The qualitative trends in **Figure 3** are directionally supportive of the main claim that MadDist learns a better MAD proxy than the two chosen baselines in several asymmetric settings. In the KeyDoorGridWorld plots, MadDist reaches high correlation quickly while also driving the ratio CV down more aggressively than QRL and Hilbert. In CliffWalking, MadDist appears to match or slightly exceed QRL in correlation while substantially improving the scaling consistency. This figure is one of the more convincing parts of the paper because it shows both ranking/fit quality and calibration-like behavior over training, not just one terminal number.

The downstream planning results in **Table 1** are also encouraging. MadDist is consistently the strongest method across all six OGBench PointMaze settings, and the margin over Hilbert is very large. The especially strong results on the Stitch settings are potentially interesting, because those datasets require composition across disconnected short demonstrations. If these results hold under careful scrutiny, they suggest that learning a trajectory-grounded asymmetric distance can be practically useful, not only numerically correlated with ground truth.

The paper is also generally readable at a high level. **Figure 1** is an effective conceptual overview: hidden environment structure, observed trajectories, learned encoder, and resulting embedding space. For readers outside the immediate subcommunity, this helps situate the contribution quickly.

## Weaknesses
1. **The specification of TDMadDist is incomplete in the main paper, and this is not a minor typo.**  
   The most serious issue is in **Equation 9 on Page 6**, where the definition of $\mathcal{L}_r'$ is visibly truncated:
   \[
   \mathcal{L}_{r}^{\prime}=\mathbb{E}_{\tau\sim\mathcal{D},(s_{i},s_{j})\sim\tau,s_{r}\sim\mathcal{S}_{\mathcal{D}}}\left[(d_{\theta}(s_{i},s_{i+1}\right.
   \]
   The sentence below informally states that the objective should make $d_\theta(s_i,s_r)$ equal to $1+d_{\theta'}(s_{i+1},s_r)$, but the actual loss is not written in the main paper. This matters because TDMadDist is one of the paper’s two headline algorithms, and the exact form of the loss determines optimization behavior, scaling, and even whether the comparison to MadDist is meaningful. A reviewer should not have to reconstruct the objective from prose or infer it from the appendix. This directly weakens the paper’s soundness and reproducibility.

2. **The mathematical formulation of the global MAD optimization is not fully coherent once the paper moves beyond finite state spaces.**  
   In **Equation 1 on Page 4**, the objective maximizes
   \[
   \sum_{(s,s')\in\mathcal{S}^2} d(s,s').
   \]
   This is sensible for finite $\mathcal S$, and the paper correctly connects it to all-pairs shortest paths. However, a few lines later the paper claims that when $\mathcal S$ is continuous, “there still exists a solution” even though states cannot be enumerated. At that point the objective itself is no longer well-defined as written, because summation over an uncountable state space is not meaningful without replacing it by an integral or a measure-theoretic formulation. The paper cannot have it both ways: either Equation 1 is a finite-state characterization only, or the continuous-state extension needs a proper reformulation. This matters because continuous-state environments are central in the experiments.

3. **The closest prior baseline is missing from the main empirical comparison.**  
   The paper discusses the method of Steccanella and Jonsson (2022) in **Section 4** and positions MadDist in **Section 6.1** as closely related but improved, yet that method is absent from the main experimental comparison in **Section 7**. This is the most natural baseline for the direct-distance-learning claim because MadDist is introduced as a variant of that approach, with two changes highlighted by the authors themselves: use of a quasimetric and a scale-invariant loss. Without this baseline, it is hard to disentangle whether the gains come from asymmetry modeling, the revised loss, the constraint handling, or simply different implementation and tuning choices. Comparing only to QRL and Hilbert makes the empirical story look cleaner than it really is. For a paper whose central claim is “we learn MAD more accurately,” omitting the nearest MAD-learning predecessor is a significant gap.

4. **The novelty of the proposed “simple quasimetric” is modest, and the paper overstates its distinctiveness relative to the level of technical development in the main text.**  
   The proposed distance in **Equation 3 on Page 5**,
   \[
   d_{\text{simple}}(x,y)=\alpha\max(\mathrm{relu}(x-y)) + (1-\alpha)\frac{1}{d}\sum_i \mathrm{relu}(x_i-y_i),
   \]
   is a convex combination of very basic ReLU-reduced asymmetric coordinate differences. The appendix shows triangle inequality by combining coordinatewise subadditivity and max/sum aggregation, which is fine, but this is a fairly lightweight construction. That by itself would not be a problem if the paper framed it modestly as a practical simplification. Instead, the introduction and conclusion pitch it as a substantial methodological contribution. The empirical ablation in Appendix E may suggest it works well, but in the main paper the technical case for why this construction should be preferred, beyond simplicity and observed performance, is thin.

5. **The experimental claims are stronger than the evidence shown in the main paper.**  
   The paper repeatedly states broad superiority, but the main text shows only a subset of environments in **Figure 3**, and the full results are deferred to the appendix. The discussion on **Page 8** says MadDist “outperforms the QRL and Hilbert baselines in all environments,” yet that claim is not verifiable from the main-paper figures alone. For ICLR main-track standards, strong universal claims should be directly supported in the main paper, especially when the benchmark suite is a core contribution.

6. **There are inconsistencies in the reporting of seeds and uncertainty, which undermines confidence in the empirical protocol.**  
   On **Page 8**, the empirical setup says “All reported results are means over five independent runs.” However, the caption of **Figure 3 on Page 9** says shaded regions are minimum and maximum across three random seeds. **Table 1** is later described in Appendix H as using three seeds. The appendix figures also alternate between three and five seeds. These inconsistencies may be explainable, but right now they make it unclear which numbers are based on which protocol. This matters because some of the reported standard deviations in **Table 1** are quite large, for example QRL on PM Giant Navigate and TDMadDist on several tasks, so the exact evaluation budget is not a trivial detail.

7. **The fairness of the baseline tuning is not convincingly established.**  
   In Appendix D.4, the paper states that for QRL, the authors observed that one hyperparameter setting suggested for short-horizon environments “led to better performance overall,” and they used that broadly. That is not automatically wrong, but the tuning protocol is under-described. Was the same amount of effort spent tuning MadDist, TDMadDist, and Hilbert? Were settings chosen using a validation criterion disjoint from the reported test statistics? The paper does not explain this clearly. Since representation-learning methods can be quite sensitive to margin-like parameters, projector sizes, and negative-pair sampling, this ambiguity affects the credibility of the claimed margins.

8. **The downstream planning experiment is useful but not yet conclusive evidence of practical superiority.**  
   **Table 1 on Page 9** shows strong success rates for MadDist, including several perfect or near-perfect entries. However, the planning setup in Appendix H uses the true simulator and a random-shooting MPC-style planner. That means the experiment is not purely evaluating the learned representation in isolation, nor is it evaluating end-to-end control under realistic model uncertainty. More importantly, because the planner uses the true simulator, the problem becomes “how good is the learned distance as a ranking heuristic over short simulated rollouts,” which is narrower than the paper’s broader practical claims. I do not object to this experiment, but the paper should present it as a limited downstream sanity check, not as decisive evidence of planning utility.

9. **Some environment definitions and “ground-truth MAD” claims are more approximate than the wording suggests.**  
   For PointMaze on **Page 8** and Appendix G, the “ground-truth MAD” is obtained by discretizing the maze and running Floyd-Warshall on the resulting graph. That is not the exact MAD of the underlying continuous-control system, it is a discretized approximation. Again, this is a reasonable engineering choice, but the phrasing in the main paper often treats the benchmark as if exact ground truth were known uniformly across all settings. This is especially relevant when differences between methods are interpreted very strongly.

10. **Presentation quality is uneven, with several notation and exposition issues that get in the way of careful assessment.**  
   Beyond the truncated **Equation 9**, there are smaller but still important issues: the notation around sampling state pairs from trajectories varies; the paper sometimes switches between $d_\theta$ and $d_\phi$-style notation across main text and appendix; and the explanation of TDMadDist’s Bellman-style target on **Page 6** is informal enough that one has to reverse-engineer the intended target. **Figure 1** is conceptually helpful, but it also illustrates a broader issue: the pipeline sketch is cleaner than the actual technical specification. The paper reads more polished at the motivation level than at the method-definition level.

11. **The paper does not sufficiently analyze failure modes, especially for TDMadDist.**  
   In **Figure 3**, TDMadDist is often substantially weaker than MadDist and sometimes weaker than QRL, yet the paper gives little explanation beyond a brief positive spin. Since TDMadDist is one of the two proposed algorithms, the reader deserves a more serious analysis of why the TD-style bootstrapping underperforms. Is it bias from inaccurate targets, instability from asymmetry, poor negative-pair structure, or mismatch with the upper-bound constraints? Without that analysis, the second half of the proposed method feels underdeveloped.

12. **Literature positioning is good in parts, but still somewhat selective around adjacent metric-learning formulations for goal-conditioned RL.**  
   The related work does a decent job covering QRL, Hilbert representations, temporal distances, and Laplacian approaches. Still, the positioning would be stronger if the paper more clearly distinguished when it is learning a shortest-support reachability notion versus broader goal-conditioned metric surrogates. As written, some comparisons risk sounding broader than they are. This is not the main problem here, but it contributes to overclaiming.

## Questions
1. Please provide the complete expression for **Equation 9** in the main paper, not only in prose. I would also like a short derivation or at least a precise explanation of why this particular TD-style random-pair objective is the right analogue of Equation 6.

2. Can the authors clarify the status of **Equation 1** for continuous state spaces? If the optimization view is intended only for finite $\mathcal S$, please say so explicitly. If it is intended more generally, what replaces the sum over $\mathcal S^2$?

3. Why is the Steccanella and Jonsson (2022) method not included as a baseline in the main experiments? This is, to my reading, the most directly comparable predecessor to MadDist. Adding it, especially on the asymmetric gridworlds, would substantially increase my confidence in the empirical claims.

4. Please clarify the seed counts and reporting protocol. The main text says five independent runs, **Figure 3** says three seeds, and **Table 1** appears to use three seeds. Which results are based on three vs. five runs, and why?

5. How were hyperparameters selected for all methods? In particular, were QRL, Hilbert, MadDist, and TDMadDist tuned under a comparable budget using a validation criterion that did not involve the reported evaluation metrics on the test environments?

6. For the PointMaze and OGBench environments, to what extent does the discretized shortest-path computation correspond to the actual continuous-control MAD? Some quantitative sensitivity analysis to discretization resolution would help.

7. TDMadDist is consistently weaker than MadDist in the main paper. Do the authors have an explanation grounded in optimization behavior or target bias? Even a short ablation isolating the effect of the bootstrap target versus direct trajectory supervision would be helpful.

8. In **Table 1**, MadDist is sometimes perfect while QRL and especially Hilbert are much lower. Can the authors report whether this remains true under a stronger planner or a purely nearest-neighbor retrieval style evaluator, to show the result is not overly coupled to the chosen random-shooting setup?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper. The work is methodological, uses simulated environments, and does not involve human subjects or sensitive data.

## Soundness Rating
2: fair. The core idea is plausible and some experiments are supportive, but the incomplete specification of TDMadDist, the finite/continuous formulation mismatch, and the missing closest baseline prevent me from viewing the technical claims as fully well-supported.

## Presentation Rating
2: fair. The high-level story is readable, and some figures are helpful, but several important details are missing or inconsistent, especially **Equation 9**, notation across sections, and seed/reporting inconsistencies.

## Contribution Rating
2: fair. The focus on action-free learning of asymmetric MAD is relevant and potentially useful, but the methodological step beyond prior work is moderate, and the empirical case is weakened by omissions in comparison and analysis.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a good problem, some genuinely promising results, and a sensible asymmetry-focused framing. Still, for ICLR main track, the current version falls short because one proposed objective is incompletely specified, the math is not fully clean, and the empirical evaluation omits the most direct prior baseline.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially regarding the mathematical presentation, the missing baseline, and the interpretation of the experimental evidence. It is unlikely, though not impossible, that I missed a clarification hidden outside the main paper.