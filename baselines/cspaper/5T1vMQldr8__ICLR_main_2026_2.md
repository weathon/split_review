---
job_id: eac6731f-b51a-4794-93e2-3c71fcec4af9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5T1vMQldr8.pdf
paper: Mitigating Reward Extrapolation Errors in Offline Preference-Based RL via Attention-Guided Subgoal Discovery
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically offline reinforcement learning, preference-based RL, reward modeling, and representation learning via attention/CVAE-based subgoal discovery.

## Minimum Quality
Pass ✅. The paper includes the expected core components, abstract, introduction, related work, method, experiments, quantitative results, qualitative analysis, and conclusion/limitations. There are substantial clarity and methodological issues, but they do not rise to the level of an automatic desk rejection based on the provided text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious prompt-targeting text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies offline preference-based reinforcement learning under reward extrapolation error caused by distribution shift between preference-labeled trajectories and trajectories used during offline policy optimization. The proposed method, SPOT, uses attention weights from a Preference Transformer to identify high-importance states as subgoals, trains a conditional VAE to generate subgoals conditioned on state-action pairs, and adds a similarity-based shaping reward during offline RL. Experiments are reported on D4RL locomotion, Robosuite, and Meta-World, together with ablations on top-$K$ filtering, shaping design, extrapolation error plots, and qualitative subgoal visualizations.

## Strengths
The paper addresses a real and important issue in offline preference-based RL, namely the mismatch between the support of preference-labeled data and the data encountered during policy optimization. This is a meaningful problem setting, and the paper is well aligned with current interest in making reward learning more reliable in offline RL pipelines.

The central idea is intuitive and reasonably well motivated. Using attention weights from a preference model to identify potentially preference-relevant waypoints, then using those as an auxiliary shaping signal, is a coherent design. The overall framework in **Figure 1** helps communicate the intended two-stage pipeline, specifically the separation between subgoal extraction/training on preferred trajectories and reward shaping during offline RL. Even though some implementation details remain underspecified, the diagram makes the proposed mechanism easier to follow than the prose alone.

The empirical coverage is broader than many papers in this niche. **Table 1** includes locomotion, Robosuite manipulation, and Meta-World tasks, rather than focusing on a single benchmark family. The method also appears competitive on average, and it is helpful that the paper reports means and standard deviations rather than only best-seed numbers.

The paper includes several useful diagnostic components beyond the main benchmark table. The top-$K$ ablation in **Table 2**, shaping-method ablation in **Table 3**, query-efficiency analysis in **Table 4**, and the extrapolation-error plots in **Figure 2** all aim to connect the method to its claimed mechanism rather than merely reporting end-task return. This is the right instinct scientifically.

I also appreciate the attempt to analyze the learned subgoals qualitatively. The hopper examples in **Figure 3** are simple, but they are at least directed toward checking whether the predicted subgoals are temporally meaningful rather than arbitrary reconstructions.

## Weaknesses
1. **The core methodological claim, that the approach mitigates extrapolation error by keeping learning within the training distribution, is asserted much more strongly than it is actually established.**  
   This is the paper’s main scientific issue. In Section 4.1.3 on **Page 5**, the paper states that “The CVAE framework ensures that generated subgoals remain within the training distribution. This is achieved via the KL divergence term...” That is far too strong. A KL regularizer of the form
   \[
   D_{\mathrm{KL}}\!\left(q_{\phi}(z\mid g_t,s_t,a_t)\,\|\,p_{\psi}(z\mid s_t,a_t)\right)
   \]
   regularizes latent distributions, but it does not by itself guarantee that decoded samples $\hat g_t$ remain in-distribution in the state space, nor that they are safe, support-matched, or reachable under the offline dynamics. This matters because the entire method justification depends on generated subgoals being distributionally reliable. As written, the paper over-claims a guarantee it does not prove or empirically validate in the main paper.

2. **The subgoal construction is underspecified in a way that affects reproducibility and possibly correctness.**  
   In Section 4.1.3 on **Page 4**, the paper says triplets $(s_t,a_t,g_t)$ are sampled from preferred trajectories “where $s_t$ and $a_t$ is a corresponding state-action pairs between $g_{t-1}$ and $g_t$.” This is ambiguous. If a trajectory contains multiple selected subgoal states from Eq. (5), how exactly is a single target $g_t$ assigned to each intermediate $(s_t,a_t)$? Is it the next selected subgoal in time, the nearest in Euclidean distance, all future subgoals, or sampled uniformly? **Algorithm 1**, line 13 on **Page 20**, says “Construct triplets $(s_t,a_t,g_t)$ with $g_t \in S_g(\sigma;K)$,” which is even more ambiguous because it suggests any selected subgoal may be paired with any state-action in the trajectory. This is not a cosmetic detail. Different assignment rules change the conditional distribution $p(g\mid s,a)$ that the CVAE is meant to model, and therefore change the semantics of the shaping reward.

3. **There is a mathematical inconsistency in the cosine-similarity training term in the algorithm, and the notation around the CVAE decoder/generator is sloppy.**  
   In the main text, Eq. (8) on **Page 5** defines
   \[
   \mathcal{L}_{\text{sim}}=-\frac{1}{2}\left(1+\frac{\hat g_t\cdot g_t}{\|\hat g_t\|\|g_t\|}\right),
   \]
   which is fine. But in **Algorithm 1**, line 19 on **Page 20**, the cosine similarity is written as
   \[
   c_t = \frac{\hat g_t^\top g_t}{\|\hat g_t\|_2 \|\hat g_t\|_2},
   \]
   using $\|\hat g_t\|_2$ twice and omitting $\|g_t\|_2$. That is simply inconsistent with Eq. (8). Also, Eq. (10) on **Page 5** writes $\hat g_i=G_\phi(s_i,a_i)$ and describes $G_\phi$ as “the trained CVAE decoder network,” even though the decoder parameters in Section 4.1.3 are denoted by $\theta$, not $\phi$. These are not fatal on their own, but they are exactly the sort of notation and equation mismatch that creates doubt about whether the method was specified carefully enough.

4. **The reward shaping formulation is not connected to standard policy-invariant shaping theory, and the paper blurs this point.**  
   Eq. (13) on **Page 5** defines
   \[
   r_{\text{final}}(s_i,a_i,s_i') = r_{\text{model}}(s_i,a_i) + \lambda r_{\text{shape}}(s_i',\hat g_i).
   \]
   This is a direct additive reward modification, not potential-based shaping in the sense of Ng et al. The paper does mention in Section 5.2.2 that policy invariance cannot be ensured with predicted rewards, which is fair, but many surrounding claims still read as if the shaping “preserves the original task objectives” in a strong sense. That is not established. In fact, because $r_{\text{shape}}$ depends on a generated target and cosine similarity in raw observation space, the resulting objective can favor states that are visually or geometrically similar to predicted subgoals while not necessarily corresponding to better true returns. This matters especially in robotic manipulation tasks where observation coordinates can mix heterogeneous quantities.

5. **The experimental results are mixed, and the paper overstates “consistent superiority” and “state-of-the-art” based on Table 1.**  
   The text in Section 5.1 on **Pages 6-7** claims “consistent superiority” and “state-of-the-art performance across multiple benchmarks.” **Table 1** does not support that wording. SPOT has the best average score, but on several individual tasks it is clearly not the best method: on `hop-m-r`, DTR exceeds SPOT; on `walk-m-e`, MR/DTR exceed SPOT; on `lift-mh`, MR/HPL exceed SPOT by a large margin; on `can-ph`, DTR and even Oracle exceed SPOT; on `drawer-open`, MR and IPL exceed SPOT substantially. This is not a nitpick. If the paper wants to sell a mechanism for improving reliability across domains, the pattern of large wins in some settings and noticeable losses in others needs a more careful discussion than “consistent superiority.”

6. **The average metric in Table 1 hides substantial heterogeneity and is not entirely cleanly comparable.**  
   **Table 1** mixes normalized D4RL scores with success rates on Robosuite and Meta-World, and then averages them into a single “Average” column. The paper notes that the oracle average excludes Meta-World, but the comparison remains awkward because these metrics have different semantics and scales, even if numerically all lie near $[0,100]$. Moreover, averaging across such diverse tasks can exaggerate a few large gains while washing out major failures. Since the main claim is robustness to extrapolation error, I would have liked per-domain averages, win/tie/loss counts, or a more distribution-aware summary. As presented, the “highest mean performance of 78.82” on **Page 7** is not especially convincing evidence of broad superiority.

7. **The extrapolation-error analysis is suggestive, but it is not strong enough to validate the claimed mechanism.**  
   In Section 5.3 on **Pages 7-8**, the paper defines extrapolation error as the absolute difference between predicted reward and “ground truth reward,” then says that because true ground-truth rewards are unavailable, it uses “human-labeled rewards from the dataset as proxy ground truth.” This is conceptually muddy. Offline preference datasets provide pairwise preferences, not a canonical dense per-state reward. If the authors instead use environment rewards from benchmark datasets, that should be stated explicitly and separated from human labels. If they derive pseudo-rewards from preferences, then the extrapolation-error quantity is model-dependent and much weaker than implied. **Figure 2** visually suggests that higher similarity to predicted subgoals correlates with lower error, and that SPOT has lower OOD error than PT, but the figure alone does not establish causality. In particular, states near generated subgoals may simply be easier states where the base reward model is already more accurate. A stronger mechanism check would control for state density or trajectory phase.

8. **The qualitative evidence in Figure 3 is too thin to support the strong interpretation given in the text.**  
   The paper claims on **Page 8** that the predicted subgoals are “approximately one timestep forward” and that this “empirically validates the quality and effectiveness” of the subgoal generation mechanism. **Figure 3** shows only two paired examples from hopper, and the visual differences are modest. It does not convincingly establish a temporal offset, nor does it validate that the predicted state is actually reachable or causally useful for policy learning. The authors are trying to extract a lot of scientific meaning from what is essentially an anecdotal illustration. The same concern applies, though to a lesser extent, to the additional visualizations in the appendix.

9. **Several ablations are too narrow to justify the broader design choices.**  
   **Table 2** only uses two tasks and 3 seeds to analyze the top-$K$ criterion. That is not enough to justify fixing $K=10\%$ broadly across all domains. Similarly, **Table 3** studies only two environments and a limited set of shaping formulations, with some highly unstable behavior, for example negative distance collapsing on `walk-m-r` at $\lambda=0.5, 1.0`, and cosine similarity collapsing at $\lambda=-1.0`. This actually suggests the shaping term is quite sensitive. Yet the paper presents $\lambda=1$ as a generally good setting without any held-out tuning protocol described in the main paper. Since reward shaping is central to the method, this limited ablation weakens the confidence in the proposed design.

10. **The fairness of some baseline comparisons is unclear, especially for extended implementations on unsupported domains.**  
   On **Page 16**, the appendix states that for CPL and DTR on Robomimic/Meta-World, where original implementations do not exist, the authors “matched CPL’s training hyperparameters to those used by our proposed method” and similarly matched DTR hyperparameters to their model for newly added domains. That may be practical, but it is not clearly fair. A baseline under author-chosen hyperparameters, especially on unsupported tasks, can easily be made weaker than necessary. Since **Table 1** uses these numbers as evidence of superiority, the paper needs a clearer fairness argument in the main text, not only an appendix remark.

11. **The relation to prior work is not sharply positioned enough, especially around what is actually new versus a combination of existing components.**  
   The paper combines an attention-based preference model, heuristic subgoal extraction by top-$K$ attention and above-average reward filtering, CVAE-based conditional subgoal generation, and reward shaping during offline RL. Each ingredient is fairly standard individually, so the novelty lives in the combination and in the specific use of PT attention for preference-aligned subgoal discovery. That is a reasonable contribution, but the paper’s writing often treats the idea as more conceptually distinct than it appears. I would have liked a clearer discussion of what exact prior limitation is not already addressed by trajectory-return regularization, reward-free preference optimization, or goal-conditioned/shaped offline RL methods.

12. **Presentation quality is uneven, and there are many language/notation errors that interfere with trust.**  
   Examples include inconsistent indexing in Eq. (3) on **Page 3**, where the notation mixes $t$, $i$, and $H$ somewhat carelessly; grammar issues throughout Sections 3-5; mismatch between “state-level importance weights” and attention over state-action pairs; and several over-strong textual claims that are not supported by the evidence. The paper is readable overall, but it needs a serious polishing pass. For a methods paper with multiple interacting models, this level of imprecision matters.

## Questions
1. **How exactly are CVAE training targets $g_t$ assigned to each state-action pair $(s_t,a_t)$?**  
   Please provide a precise rule. If multiple subgoals satisfy Eq. (5) within a preferred trajectory, is $g_t$ the next subgoal in time, the nearest future subgoal, a random selected one, or something else? A clear definition here would significantly increase my confidence in the method.

2. **Can the authors clarify the inconsistency between Eq. (8) and Algorithm 1, line 19?**  
   The algorithm currently uses $\|\hat g_t\|_2\|\hat g_t\|_2$ in the cosine denominator, which appears incorrect. Please confirm the intended formula and whether the implementation follows Eq. (8).

3. **What exactly is the “ground truth reward” used in Section 5.3 and Figure 2?**  
   Is this the environment reward available from benchmark datasets, a preference-derived proxy, or something else? The current text says “human-labeled rewards from the dataset as proxy ground truth,” which is confusing for pairwise preference data. Please define this precisely.

4. **Can the authors provide stronger evidence that the gains come specifically from attention-guided subgoals rather than generic auxiliary shaping?**  
   For example, what happens if subgoals are selected uniformly from preferred trajectories, from high predicted reward only without attention, or from attention only without the reward filter? This would directly test whether the attention mechanism adds value beyond a generic goal-conditioning heuristic.

5. **How sensitive is the method to the representation used in the cosine similarity shaping term?**  
   In Eq. (11), the similarity is computed directly between the next state and the predicted subgoal. Is this done in raw observation space for all domains, including robotic manipulation? If so, why is cosine similarity in that space an appropriate progress metric? Evidence with normalized features or learned embeddings would help.

6. **How were hyperparameters selected, especially $\lambda=1$ and $K=10\%$?**  
   Since the ablations in Tables 2 and 3 use only a small subset of tasks and show sensitivity, please clarify the tuning protocol and whether any test-task information leaked into design selection.

7. **Can the authors comment on the substantial failures or regressions in Table 1?**  
   In particular, `lift-mh`, `can-ph`, and `drawer-open` are not small misses. What task characteristics cause SPOT to underperform there? A candid failure analysis would strengthen the paper considerably.

8. **Can the authors show whether the generated subgoals are actually in-distribution or reachable?**  
   Since a central claim is that the CVAE keeps subgoals within the data support, a quantitative check would be useful, for example nearest-neighbor distances to dataset states, likelihood under a held-out density model, or short-horizon reachability statistics.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns were identified from the paper. The work is a methodological study on offline preference-based RL using standard benchmark datasets and simulated control/manipulation tasks.

## Soundness Rating
2: fair. The main idea is plausible and some empirical evidence is provided, but several core claims are overstated, key methodological details are underspecified, and the mechanism analysis is not strong enough to fully support the paper’s central narrative.

## Presentation Rating
2: fair. The paper is readable and the high-level pipeline is understandable, especially with Figure 1, but there are multiple notation inconsistencies, ambiguous definitions, and over-strong statements that reduce clarity and trust.

## Contribution Rating
2: fair. The paper tackles an important problem and proposes a sensible combination of attention-guided subgoal extraction and shaping, but the novelty is moderate and the evidence does not yet elevate it to a clearly strong contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and addresses an important problem, but in its current form the specification is too loose, the mechanism claims are stronger than the evidence, and the empirical story is less consistent than the paper suggests.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the method description, equations, figures, and tables, and the main concerns are grounded in the paper’s own presentation.