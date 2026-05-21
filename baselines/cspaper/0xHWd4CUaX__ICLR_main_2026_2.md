---
job_id: c45099a1-9426-4fa1-aa0f-2a8f60ecfd2f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0xHWd4CUaX.pdf
paper: Contrastive Code Graph Embeddings for Reinforcement Learning-Based Automated Code Refactoring
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining self-supervised representation learning on code graphs with reinforcement learning.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, methodology, experiments, results, and conclusion/discussion; despite substantial technical and empirical weaknesses, it is still a research paper rather than an incomplete manuscript.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes an automated code refactoring framework that combines contrastive pre-training of code graph embeddings with PPO-based reinforcement learning. The method uses syntax-preserving graph augmentations for self-supervised representation learning, then incorporates the learned embeddings, traditional code-quality metrics, and a semantic-preservation signal into a composite reward. Experiments on several code datasets report improvements over rule-based, learning-based, and RL-based baselines, with ablations and cross-language transfer results intended to support the contribution of the different components.

## Strengths
The paper targets a practically meaningful problem, automated code refactoring, and frames it in a way that is relevant to ICLR, namely as a representation learning plus RL problem rather than purely a software-engineering heuristic system. That high-level framing is reasonable and potentially interesting to the community.

The method combines several components that fit together coherently at a conceptual level: graph-based code representations, contrastive pre-training, RL fine-tuning, and a semantics-aware reward. Even if I have serious concerns about the technical execution, the overall pipeline is easy to understand.

The ablation in **Table 2** is directionally useful. In particular, the reported drop from the full model to “w/o contrastive pre-training” and “w/o semantic tests” is at least consistent with the paper’s claimed intuition that both representation quality and semantic checking matter. I appreciate that the authors attempted to isolate the contributions of these components, rather than only presenting one headline table.

**Figure 1** also communicates the intended training benefit clearly: the proposed method appears to converge more quickly than GraphRL and reaches its plateau earlier. As a presentation device, this figure is one of the clearer parts of the paper, and it helps the reader see what the authors mean by “embedding-guided” improvement in training efficiency.

The paper includes a qualitative section and a transfer section, which is better than restricting the empirical story to a single in-distribution benchmark.

## Weaknesses
1. **The central methodological claims are undermined by underspecified and internally inconsistent mathematical formulations.**  
   Several equations look plausible at first glance, but on closer reading they are not defined precisely enough to support the method. For example, in **Equation (2)** on **Page 3**, the InfoNCE denominator is written as  
   \[
   \sum_{k=1}^{N}\mathbb{P}_{k\neq i}\exp(sim(z_i,z_k)/\tau),
   \]
   which is not a valid standard notation for excluding the anchor from the denominator. If the intent is an indicator, then it should be explicit; if the intent is a probability, the equation is wrong as written. This matters because the paper’s main representation-learning component rests on this objective.  
   Similar issues recur in **Equation (4)** on **Page 4**, where negatives are defined as all \(G' \in \mathcal{B}\), but it is unclear whether the positive partner \(G_2\) is included in the denominator, whether both views of all batch elements are used symmetrically, and how many views are sampled per input. These are not cosmetic omissions; they affect the actual optimization problem.

2. **The reward design is not scientifically well justified, and parts of it are conceptually questionable.**  
   The paper claims to move beyond handcrafted rewards, but **Equation (5)** on **Page 4** still uses a manually weighted linear combination of manually chosen code-quality metrics, a hand-scaled embedding-dynamics term, and a semantic penalty. In other words, the method still heavily depends on hand-designed reward shaping. The new part is that one reward component is derived from learned embeddings, but the fusion itself is heuristic.  
   More importantly, the term  
   \[
   \Delta \mathbf{h}_t = \|\mathbf{h}_t - \mathbf{h}_{t-1}\|_2
   \]
   is rewarded through \(+\alpha \tanh(\beta \Delta \mathbf{h}_t)\). This assumes that larger movement in embedding space is beneficial, yet **Figure 2** on **Page 8** only shows correlation with syntactic improvement, not causal evidence that rewarding embedding displacement produces better refactorings. A large change in latent space could just as easily reflect instability or semantically risky edits. The paper does not justify why “move farther” is a reward target rather than an analysis statistic.

3. **The exploration policy in Equation (6) is not a valid action-conditional policy as written.**  
   On **Page 4**, the paper defines
   \[
   \pi_{\text{explore}}(a|s)\propto \exp\left(-\frac{1}{2}(\mathbf{h}_s-\mathbf{h}^*)^\top \Sigma^{-1}(\mathbf{h}_s-\mathbf{h}^*)\right).
   \]
   The right-hand side does not depend on the action \(a\) at all. So this is not an action distribution unless the missing action dependence is encoded elsewhere, which is not stated. At best, this is a state score or visitation bias, not a policy over actions. Since embedding-guided exploration is presented as a key contribution in **Section 4.3**, this missing piece is a serious technical flaw, not a minor notation issue.

4. **The semantic-preservation formulation is inconsistent across sections and insufficiently specified.**  
   In **Section 4.2** on **Page 4**, semantic preservation is defined as a binary test outcome,
   \[
   \delta_t = \mathbb{I}[\text{test}(G_t)=\text{test}(G_{t-1})].
   \]
   Then in **Section 4.5** on **Page 5**, \(\delta_t\) becomes a soft score based on normalized Hamming distance between execution traces:
   \[
   \delta_t = 1 - \frac{1}{L}\sum_{k=1}^{L}\mathbb{I}[\text{trace}_k(G_{t-1})\neq \text{trace}_k(G_t)].
   \]
   These are materially different definitions. Is \(\delta_t\) binary or continuous? Is it based on test pass/fail equality or trace agreement? The reward in **Equation (5)** uses \(1-\delta_t\), so this ambiguity directly affects the training signal. For a paper whose selling point is balancing syntactic improvement with semantic preservation, this inconsistency is a major problem.

5. **The graph encoder and policy architecture are too vaguely described to support reproducibility or even clear interpretation.**  
   The paper says the encoder uses “graph attention layers” in **Section 4.1**, and the policy network in **Section 4.4** again uses attention weights in **Equation (7)**. But it is not clear whether the same GAT architecture is used in both the pre-trained encoder and the RL policy, whether the policy operates on graph nodes or graph-level pooled embeddings, and how the concatenated representation \([\mathbf{h}_t;\mathbf{q}_t]\) interfaces with node-level attention coefficients \(\omega_{ij}\). There is a mismatch between graph-level features and node-level attention notation.  
   This is more than an exposition complaint. If the policy is graph-level, then **Equation (7)** is the wrong object to present as the core policy mechanism; if it is node-level, then action selection and graph pooling are missing.

6. **The experimental setup is too opaque to support the strong comparative claims in Table 1.**  
   **Table 1** on **Page 6** reports surprisingly clean wins across every metric, but the setup needed to trust those results is missing. The paper does not say how train/validation/test splits are constructed for each dataset, whether projects are split by repository to avoid leakage, how many seeds are used, or whether numbers are averages with standard deviations. That is especially important for RL, where variance can be large.  
   The “Generalization Score (GS)” is described only as “performance on unseen project types (cross-validation),” which is far too vague. What are the folds? What constitutes a project type? Is GS an average of other metrics, a normalized score, or a separate task-specific criterion? Without a formal definition, the best-looking number in **Table 1**, arguably the 72.4 GS of the proposed method, is not actually interpretable.

7. **Key baselines are weakly specified and in some cases poorly matched to the task.**  
   The baseline section on **Pages 5-6** mixes rule-based static analyzers, general code models, RL systems, and a hybrid method, but does not explain how each baseline is adapted to the exact refactoring environment, action space, or semantic-checking setup. For example, comparing against PMD and Checkstyle may be useful as rough rule-based references, but they are not competitive learning-based refactoring agents.  
   Even among the learned baselines, the descriptions are thin. It is unclear whether Graph2Edit, Code2Seq, RLRefactor, GraphRL, and NeuroRefactor are retrained under a common environment and budget, or whether results are taken from different settings. This matters because **Table 1** is the paper’s main evidence of superiority, and without fair, aligned baseline implementation details, the comparison is hard to trust.

8. **The reported empirical evidence lacks uncertainty estimates and statistical rigor.**  
   None of the results tables, **Table 1**, **Table 2**, or **Table 3**, include standard deviations, confidence intervals, or significance testing. For RL and code transformation tasks, that omission is substantial. A reported difference like 90.5 vs. 93.8 in SP, or 67.2 vs. 72.4 in GS in **Table 1**, may or may not be meaningful depending on variance across random seeds and dataset splits.  
   Likewise, **Figure 1** shows only one learning curve per method with no error band. Since the paper explicitly argues faster convergence, the absence of seed variation weakens that claim considerably.

9. **The ablation study is useful but still insufficiently diagnostic.**  
   **Table 2** on **Page 7** removes broad components, but it does not answer several key questions. There is no ablation over the specific augmentations used in contrastive pre-training, even though subtree masking, edge rewiring, and identifier shuffling are all central design choices in **Section 4.1**. There is no comparison between fixed and jointly fine-tuned encoders, despite the decision in **Section 4.6** to freeze \(f_\theta\) during RL. There is also no ablation on the reward weights \(\mathbf{w}_q, \alpha, \beta, \gamma\), even though the method is evidently sensitive to these hand-chosen coefficients.  
   The paper therefore attributes gains to broad conceptual components without showing which design choices within those components actually matter.

10. **The transfer claims are overinterpreted relative to the evidence provided.**  
    In **Section 5.4** and **Table 3** on **Page 8**, the paper claims cross-language generalization by evaluating a model trained over Java on Python and C++. However, the only baselines shown are rule-based tools, PyLint and Cppcheck, not language-adapted learning or RL baselines. That is not enough to establish strong transfer of learned representations.  
    Also, the reported SP of the proposed method is actually lower than the rule-based tools in both target languages, 88.9 vs. 90.4 for Python and 91.2 vs. 93.1 for C++, while SI is higher. So the result is a trade-off, not a uniformly stronger transfer capability. The text on **Page 7** says the method “maintains reasonable performance” and “outperform[s] language-specific rule-based tools,” but that statement is only partially true and should be phrased more carefully.

11. **Some claims tied to the figures are suggestive rather than evidential.**  
    **Figure 2** on **Page 8** reports a Pearson correlation \(r=0.72\) between embedding movement and SI. But the figure only supports correlation, not the paper’s stronger narrative that embedding dynamics “capture meaningful refactoring signals” in a way suitable for reward shaping. Since the same quantity is fed into the reward, there is a risk of circular interpretation unless the analysis is carefully separated from training.  
    **Figure 3** on **Page 9** is also difficult to evaluate scientifically. It shows changing proportions of reward component dominance across refactoring stages, but the notion of “dominance” is not defined. Is dominance measured by absolute contribution magnitude, gradient attribution, normalized reward share, or action-selection sensitivity? As presented, the figure is visually plausible but methodologically unclear.

12. **The paper’s novelty relative to prior combinations of graph representations, contrastive learning, and RL is limited and not sharply articulated.**  
    The authors position the work as replacing handcrafted rewards with learned representations, but in practice the method is a combination of existing ingredients: GNN/GAT code representations, contrastive pre-training, RL with PPO, and reward shaping with static metrics plus tests. That combination may still be publishable if demonstrated rigorously, but the paper does not clearly identify what is genuinely new at the algorithmic level versus what is an integration of known tools.  
    This matters because the evidence is not strong enough to compensate for a modest methodological step. If the paper is mainly an integration paper, then the empirical validation and clarity must be stronger than what is currently shown.

13. **Presentation quality is below ICLR expectations for a technically ambitious paper.**  
    There are many grammatical issues and awkward phrases throughout, for example on **Page 1** (“objecting to code quality”), **Page 2** (“Recent lemon deep learning technologies”), and **Page 4** (“when they are amounting correct refactoring actions”). More importantly, these are symptoms of a broader problem: many sentences are hard to parse, and key technical choices are described imprecisely.  
    The references and dataset naming also raise concerns. For instance, the paper introduces “CodeRef (Wang et al., 2024)” on **Page 5**, but the cited reference list on **Page 11** appears to correspond to “RepoTransBench,” not an obviously matching refactoring benchmark name. That may be a citation mismatch or a shorthand, but the paper leaves the reader guessing.

## Questions
1. Please provide a precise, corrected definition of the contrastive objective in **Equations (2) and (4)**. Specifically, what exactly is in the denominator, how are positive and negative pairs sampled, how many augmented views are generated per graph, and is the loss symmetric over both views? A mathematically clean statement here would increase my confidence substantially.

2. Please clarify the semantic-preservation signal \(\delta_t\). Is it binary as defined in **Section 4.2** or continuous as defined in **Section 4.5**? If both are used, where exactly is each used, and how does this interact with the reward in **Equation (5)**?

3. For **Equation (6)**, how does the exploration distribution depend on the action \(a\)? As written, it is only a function of state embeddings. If there is a missing action-conditioned scoring function or sampling mechanism, please specify it formally.

4. Please define the RL environment in a reproducible way: what is a state, what are the discrete actions, what transitions are allowed, what causes episode termination, and what constraints enforce syntactic validity of code after each action?

5. For **Table 1**, please report variance across multiple random seeds and explain dataset splits in detail. In particular, how is **GS** computed? Is it a weighted average of other metrics or a separately measured criterion? Without this, the table is hard to interpret.

6. For the baselines in **Table 1**, were all learned methods retrained in the same environment with the same datasets and evaluation protocol, or are some values drawn from prior reports? A careful apples-to-apples clarification is essential.

7. For **Table 2**, could you add ablations over the three augmentation types in **Section 4.1** and over freezing vs. fine-tuning the encoder during PPO? Those experiments would make the role of contrastive learning much more convincing.

8. For **Figure 2**, was the plotted correlation computed on held-out data and independently of the reward optimization process? If not, the analysis risks being partly tautological. Please clarify.

9. The paper states in **Section 6.3** that the system supports codebases with up to 1 million lines of code “in our experiments,” but there are no corresponding quantitative results, memory/runtime tables, or figures. Can you provide evidence for this claim in the main paper?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics red flags are apparent from the paper itself. The work concerns automated code refactoring and does not present obvious fairness, privacy, or human-subject issues in its current scope.

## Soundness Rating
2: fair. The high-level idea is plausible, but several core equations and algorithmic components are underspecified or inconsistent, and the empirical methodology does not adequately support the strongest claims.

## Presentation Rating
2: fair. The paper is readable at a coarse level, and some figures and tables help, but technical exposition, notation, and writing quality are not at the level needed for a clear scientific contribution.

## Contribution Rating
2: fair. The problem is interesting and the integration is potentially useful, but the methodological novelty is limited and the evidence for a meaningful advance over prior approaches is not yet convincing.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a reasonable high-level idea and some promising signals, especially the attempt to combine learned code representations with RL for refactoring. However, the current version has too many substantive issues, including mathematically unclear core components, inconsistent definitions, weak experimental specification, insufficiently rigorous evaluation, and overclaimed conclusions relative to the evidence. With a cleaner formulation and much stronger experimental discipline, this could become a solid submission, but I do not think the present version clears the ICLR bar.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details because the paper leaves several central components insufficiently specified.