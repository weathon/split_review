- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8
Now I have all the evidence needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes a framework for pre-training Generative Flow Networks (GFlowNets) without task-specific rewards, then fine-tuning them for downstream tasks. It introduces an Outcome-Conditioned GFlowNet (OC-GFN) that learns to reach any specified outcome through contrastive training with off-policy trajectories and an "outcome teleportation" mechanism for efficient credit assignment. For downstream adaptation, the paper derives a direct conversion formula (Eq. 5) and proposes an amortized predictor to approximate the intractable marginalization over outcomes. Experiments across GridWorld, bit sequences, TF Bind, RNA, and AMP generation show that OC-GFN pre-training improves mode discovery and sample efficiency compared to training GFlowNets from scratch.

## Strengths

1. **Novel pre-training paradigm for GFlowNets.** This is the first work to formulate unsupervised pre-training for GFlowNets via outcome-conditioned policies (Section 4.1). The OC-GFN framework is well-motivated by the analogy to goal-conditioned RL and addresses a genuine gap in the GFlowNet literature, where models previously had to be trained from scratch for each new reward function.

2. **Contrastive training with implicit curriculum** (Section 4.1.2, Algorithm 1 steps 4–10). The idea of using off-policy successful trajectories from GAFlowNet as positive examples and on-policy OC-GFN trajectories as negative examples is a practical solution to the sparse-reward problem. Ablation studies (Figures 3b–d, 5a–c) confirm that both contrastive training and outcome teleportation are necessary for scaling to large outcome spaces.

3. **Outcome teleportation for long-horizon credit assignment** (Eq. 4, Eq. 8). The technique of propagating the terminal reward signal to every transition through a modified detailed balance constraint is a sensible approach to sparse-reward challenges. Ablations (Figures 3d, 5d) show it is essential for learning in large bit sequence tasks.

4. **Amortized predictor enables tractable fine-tuning** (Section 4.2, Eq. 10). The paper correctly identifies that the direct conversion formula (Eq. 5) involves an intractable marginalization, and proposes a learnable numerator network N(s'|s) with an auxiliary Q(y|s',s) network trained via a GFlowNet-like loss. GridWorld validation (Figure 3c–d) shows this amortized approach qualitatively matches the target distribution.

5. **Broad empirical validation across multiple domains of increasing complexity.** The paper evaluates on GridWorld (small to large maps), bit sequences (length 20–100), TF Bind 8 (30 tasks), RNA generation (~27 length), and antimicrobial peptides (length 50, 20^50 space). This breadth demonstrates scalability that was missing in prior GFlowNet work. Pre-training success rates are high across all domains (93–100%, Figures 3–8), and downstream mode discovery shows consistent improvements over baselines.

6. **Ability to adapt without full re-training.** The direct conversion formula (Eq. 5) is a notable theoretical property — unlike typical RL fine-tuning that requires policy re-training, the pre-trained OC-GFN can in principle be adapted to new rewards through a weighted marginalization over the learned conditional flows.

## Weaknesses

### Fatal
None. The paper's core approach is sound and the empirical evidence, while having gaps, does not invalidate the main claims.

### Major

1. **TF Bind downstream evaluation only shown for 2 of 30 tasks.** The paper states "We consider 30 different downstream tasks" (line 373) and "tune the hyperparameters on one task, and evaluate on the other 29 downstream tasks" (line 387), but results are shown for only 2 tasks (Figure 7a–d). No aggregate statistics (mean±std across all 29 tasks) are provided. This makes it impossible to assess whether improvements are consistent or cherry-picked. The claim of "consistent and substantial improvements" (line 393, also abstract) is not supported by the data presented.

2. **GridWorld fine-tuning evaluation relies entirely on visual inspection.** The paper shows target distributions and sample distributions as histograms (Figure 3) but reports no quantitative metric such as L1 error, KL divergence, or Wasserstein distance between the empirical sampling distribution and the target reward distribution. The claim that OC-GFN "matches the target distribution" (line 263) is supported only by eyeballing figures. This is a basic omission in a domain where ground-truth marginals are tractable.

3. **Computational cost of pre-training is not controlled.** The pre-training stage trains both a GAFlowNet (for exploration) and an OC-GFN, which uses substantially more environment interactions than the "from scratch" baseline. The paper does not compare methods at matched total interaction budgets or wall-clock time. The improved downstream performance may partially reflect additional computation rather than a property of the pre-training mechanism. This is a standard concern that should be addressed.

### Minor

4. **The "reward-free" framing is imprecise.** The pre-training uses GAFlowNet with intrinsic rewards (exploration bonuses, line 62–66, 145), and the OC-GFN itself uses a binary success reward. The paper states "reward-free pre-training" repeatedly (abstract, lines 26, 38, 102), which could mislead readers into thinking no reward signal of any kind is used. The paper would be more accurate describing this as "task-agnostic pre-training" or "unsupervised pre-training with exploration bonuses," which is consistent with how this is described in the RL literature. The paper is transparent about the GAFlowNet mechanism, so this is a presentation issue rather than a substantive flaw.

5. **The theoretical propositions (Propositions 1 and 2) are basic consistency results rather than substantive theoretical contributions.** Proposition 1 (line 180–183) states that if the OC-GFN loss is zero for all trajectories and outcomes, the policy reaches the target outcome. Proposition 2 (line 253–256) states that if the amortized loss is zero for all (s,s',y), the predictor estimates the desired sum. These follow directly from the loss definitions and provide no convergence guarantees, rates, or insight into when the method might fail. While such consistency checks are common in the GFlowNet literature as sanity checks, the paper presents them as formal justifications (Sections 4.1, 4.2), which overstates their evidential weight.

6. **The amortized predictor training dynamics are under-specified.** The loss (Eq. 10) involves a product of two learned networks (N and Q) that are jointly optimized "in a GFlowNet-like procedure" (line 277). The paper does not discuss how degenerate solutions (e.g., both networks converging to zero, or compensating errors) are avoided, nor does it provide diagnostics (e.g., whether Q(y|s',s) produces plausible outcome distributions, or whether N(s'|s) converges to similar values across initializations). The GridWorld validation partially mitigates this concern, but the training dynamics remain opaque.

7. **Outcome teleportation's effect on the proportional sampling property is not analyzed.** The modified DB constraint (Eq. 4) incorporates the terminal reward R(x|y) into every transition. While the paper motivates this as "reward decomposition" (line 170), it does not analyze whether the resulting flows F(s|y) and policies P_F(s'|s,y) still satisfy the marginal condition P_T(x|y) ∝ R(x|y) that would be expected from a standard GFlowNet. The downstream conversion (Eq. 5) uses these learned quantities, and any distortion from the teleportation modification would propagate. The empirical success on GridWorld (Figure 3c) suggests the impact is limited in practice, but the paper would benefit from a theoretical or diagnostic analysis.

8. **Statistical reporting is incomplete.** While the paper states results use 3 seeds with mean and std (line 293), many downstream plots (e.g., Figures 6, 7, 8, 9) show only single curves or show curves without visible error bars. The RNA results (Figure 8) show "averaged normalized" modes across 4 tasks without per-task breakdowns, making it impossible to assess variability across tasks.

### Trivial
- The paper uses the term "goal teleportation" (line 31) and "outcome teleportation" (line 162) inconsistently.
- Figure numbering in the text (the raw paper references "Figure 6", "Figure 7", etc., which are the figure labels used in the PDF) is adequate but some captions are missing the "(a)", "(b)" subfigure references in the extracted text.

## Nice-to-Haves
- On GridWorld, computing the L1 distance or KL divergence between the empirical sampling distribution and the target reward distribution would provide a simple quantitative validation of the conversion formulas (Eq. 5 and the amortized approach).
- An ablation comparing OC-GFN pre-training against a simpler exploration strategy (e.g., uniform random sampling for generating outcomes) would help isolate whether the GAFlowNet's structured exploration is essential.
- A table reporting aggregate performance (with means and standard deviations) across all 29 TF Bind downstream tasks would significantly strengthen the empirical claims.
- Runtime or wall-clock time comparisons would help contextualize the extra computational cost of pre-training.

## Removed Points
These points from the reviewers were identified as inaccurate, speculative, or not appropriately scoped:

1. **"The relevant comparison is GFN from scratch, but the significance of the improvement is not quantified"** (Harsh Critic, bit sequences): The paper DOES compare against GFN from scratch (line 364). The comparison is present; the critic misread this section. REMOVED.

2. **"Outcome teleportation is essentially behavioral cloning of successful trajectories"** (Harsh Critic): This characterization is inaccurate. The OT modification incorporates the terminal reward into each transition's loss, but the OC-GFN remains a conditional policy trained with both successful and unsuccessful trajectories (via the contrastive learning procedure). It is not cloning successful trajectories. REMOVED.

3. **"Not compared to any other pre-training approaches from RL (e.g., DIAYN, SMM, APS)"** (Harsh Critic): The paper explicitly discusses unsupervised RL pre-training in the Related Work section (lines 77–79) and states that those methods learn reward-maximizing policies, which is fundamentally different from GFlowNets' proportional-sampling objective. Adapting these methods to GFlowNets is outside the paper's scope. REMOVED (scope creep).

4. **Strengths about "theoretical grounding"** (Strength Finder, points 2): The strength finder overstates the value of the propositions. These are basic consistency results, not deep theoretical contributions. MOVED TO Removed Points (the weakness above already addresses this).

5. **Missing appendix, missing proofs in appendix, absent references, or formatting/style nitpicks**: The PDF parser strips appendix sections; these exist in the original submission. REMOVED per hard rules.

## Novel Insights
The two-source review structure reveals a tension that the paper does not fully resolve: the outcome-conditioned GFlowNet framework is intuitively appealing, but the key technical novelty — outcome teleportation (Eq. 4) — modifies the standard flow equations in a way that is simultaneously crucial for learning efficiency (validated by ablations) and theoretically unexamined for downstream conversion. The paper could strengthen its core contribution by explicitly analyzing whether the teleportation-modified flows preserve the property that a weighted combination over outcomes yields the correct downstream policy, or whether the amortized predictor implicitly corrects any distortion. This interplay between a practically necessary modification and its theoretical implications is the paper's most interesting unresolved axis.

## Suggestions

1. Add quantitative metrics (L1 distance or KL divergence) for the GridWorld fine-tuning evaluation (Figure 3). The ground-truth target distribution is available by construction — this is a trivial addition that would substantially strengthen the validation of both conversion methods.
2. Report aggregate statistics across all 29 TF Bind downstream tasks in a table (mean ± std of modes discovered, top-100 scores). Showing only 2 tasks leaves the main claim unsubstantiated.
3. Add a controlled computational budget comparison: either match total environment interactions between pre-training + fine-tuning and training-from-scratch, or explicitly report the extra cost.
4. Discuss or provide diagnostics for the amortized predictor training (e.g., correlation between N(s'|s) estimates and ground-truth marginals on GridWorld, or sensitivity to initialization).
5. Reframe "reward-free" as "task-agnostic" or "unsupervised" pre-training to more accurately describe the method, while acknowledging the use of intrinsic motivation for exploration.
