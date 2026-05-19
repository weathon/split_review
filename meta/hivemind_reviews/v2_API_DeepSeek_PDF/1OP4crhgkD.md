## Summary
# Final Review Report

## Summary

This paper presents SAMA (Semantically Aligned task decomposition in MARL), a framework that uses pretrained language model (PLM) prompting with chain-of-thought to generate semantically meaningful subgoal decompositions for cooperative multi-agent reinforcement learning under sparse rewards. SAMA addresses two key limitations of prior automatic subgoal generation (ASG) methods: (1) the high sample complexity of end-to-end learning task planning from sparse rewards, and (2) the "over-representation" problem where diversity-promoting mechanisms produce task-irrelevant subgoals. The framework consists of three core components: PLM-based goal generation/decomposition/assignment, language-grounded MARL for subgoal execution, and self-reflection for error recovery. Experiments on Overcooked (five layouts) and MiniRTS demonstrate that SAMA achieves comparable final performance to state-of-the-art methods while requiring approximately 5-10x fewer environment interactions.

**Strengths:** The paper identifies a practically important problem (sample inefficiency in sparse-reward MARL) and proposes a novel integration of PLM-based planning with language-grounded MARL. The self-reflection mechanism is a sensible addition to handle PLM hallucination. The experimental evaluation covers diverse challenging layouts.

**Key weaknesses:** (1) The conceptual framing via "disentangled representation learning" is overstated—SAMA does not perform disentangled representation learning in any technical sense. (2) The claimed sample efficiency advantage lacks rigorous statistical validation (variance, significance tests, controlled budgets). (3) PLM-generated reward functions have no quality validation, creating a cascading error risk. (4) The MiniRTS experiment conflates PLM contribution with the existing RED system by using oracle prompts and pretrained initialization. (5) The introduction and contribution statements are vague and would benefit from concrete, falsifiable claims.

**Novelty:** External literature verification was unavailable in this run (Retrieval-Disabled Mode); novelty conclusions are marked as deferred manual verification. Based on manuscript evidence alone, the core idea of using PLM prompting for subgoal decomposition in MARL appears novel, though conceptually related to prior work on PLM-based planning (DEPS, ELLM, Plan4MC, GITM) and language-grounded RL (EMMA, RED).

## Strengths
1. **Problem relevance.** The paper tackles a genuine challenge in cooperative MARL: sample inefficiency under sparse rewards. The motivation that ASG methods generate task-irrelevant subgoals due to diversity-promoting objectives is well-identified and practically important.

2. **Novel integration.** Combining PLM-based planning with language-grounded MARL is a technically interesting synthesis of two research directions. Using PLMs as a source of commonsense priors for subgoal decomposition (rather than learning it from scratch) is a reasonable design choice that aligns with the paper's sample-efficiency goal.

3. **Self-reflection mechanism.** Acknowledging PLM limitations (hallucination, long-horizon reasoning errors) and incorporating a self-reflection loop for replanning is a practical and honest design feature. The mechanism is clearly described and integrated into the overall framework.

4. **Comprehensive evaluation on Overcooked.** The paper evaluates on five distinct Overcooked layouts with varying coordination requirements, comparing against a reasonable set of baselines including self-play, population-based training, and prior ASG methods. The use of 10 random seeds demonstrates awareness of stochasticity.

5. **Transparent cost reporting.** The appendix provides detailed economic and computational cost estimates for PLM queries, including per-episode costs for GPT-3.5 and GPT-4, which helps readers assess the practical trade-off between sample efficiency and computational overhead.

6. **Well-structured method description.** The three-component architecture (task decomposition, language-grounded MARL, self-reflection) is clearly separated and mapped to the four sub-problems (a-d), making the framework easy to understand.

## Weaknesses
1. **Overstated conceptual framing (Page 2-3).** The paper's connection to disentangled representation learning (DRL) is metaphorical rather than technical. SAMA does not learn disentangled representations; it uses PLMs to generate text subgoals. The term "disentangled decision-making" is introduced without formal definition, which may mislead readers about the paper's technical contribution.

2. **Insufficient statistical rigor in experiments (Page 8).** The claim of "5-10x sample efficiency improvement" is not accompanied by rigorous statistical evidence. Learning curves lack error bars/confidence intervals. The x-axis scaling varies across layouts (1.25e5 to 2.5e5 timesteps per tick), making direct comparison difficult. No significance tests are reported for final performance differences.

3. **PLM-generated reward functions lack validation (Page 6).** The training pipeline relies on PLM-generated Python code snippets to provide binary reward signals for language-grounded MARL. The paper provides no analysis of code quality validation: no compilation rate, no accuracy against ground-truth subgoal completion detection, no analysis of false positive/negative rates. This cascading dependency chain (D_state -> D_subgoal -> D_code) creates significant risk of training on incorrect reward signals.

4. **Self-reflection cost hidden from metrics (Page 7).** Self-reflection trials consume environment steps through reset-recovery cycles, but these steps are excluded from reported empirical performance. If a significant fraction of total environment interactions occurs during self-reflection, the claimed sample efficiency may be artifactually inflated.

5. **MiniRTS experiment confounds PLM contribution (Page 9).** The MiniRTS evaluation uses (a) oracle prompts with ground-truth enemy composition and attack graph, and (b) RED's pretrained policy as initialization. Results therefore conflate PLM planning with the existing RED system's capabilities. A proper ablation would compare SAMA's PLM planner against a non-PLM baseline within the same system.

6. **Vague contribution statements (Page 3).** The three listed contributions mix framework-level, mechanism-level, and performance-level claims. Contribution 3 ("demonstration of considerable advantage in sample efficiency") is a performance claim rather than a scientific contribution. Contributions 1 and 2 would benefit from concrete, falsifiable wording.

7. **Missing baseline fairness concerns (Page 8). COLE, a key baseline, targets zero-shot coordination rather than sample efficiency. Directly comparing sample efficiency between methods designed for different objectives is potentially misleading. The paper acknowledges this partially but does not adjust the narrative accordingly.

8. **Markov assumption for task planning unverified (Page 3).** The paper assumes task-level planning is Markovian (depends only on current context), but long-horizon tasks may require temporal dependencies (e.g., tracking gathered resources, cooldown timers). No empirical verification of this assumption is provided.

## Key Issues
### Issue 1 (Major): PLM-generated reward functions lack quality validation
**Location:** Page 6 - Training Dataset Generation paragraph
**Risk:** Cascading errors from PLM-generated states → subgoals → reward code can produce incorrect training signals. The paper provides no compilation rate, no accuracy against ground-truth labels, and no analysis of false positive/negative rates for the reward functions.
**Fix:** (a) Report the percentage of generated code snippets that compile and execute without error. (b) For a held-out set of states with ground-truth subgoal completion labels, report precision/recall of the PLM-generated reward functions. (c) Add a human validation step for a random subset of reward functions.

### Issue 2 (Major): Sample efficiency claim lacks statistical rigor
**Location:** Page 8 - Overcooked results analysis
**Risk:** The paper claims "5-10x sample efficiency improvement" without error bars on learning curves, without significance tests, and with varying x-axis scales across layouts. The claim may not hold under rigorous statistical comparison.
**Fix:** (a) Add confidence intervals or standard deviation bands to all learning curves. (b) Report the exact number of environment steps required to reach a specified performance threshold (e.g., 90% of final converged reward) for each method. (c) Perform paired bootstrap significance tests between SAMA and each baseline at convergence.

### Issue 3 (Major): MiniRTS experiment confounds PLM contribution
**Location:** Page 9 - MiniRTS case study
**Risk:** The use of oracle prompts (with ground-truth enemy composition) and RED's pretrained policy means the experiment measures whether PLM prompting can approximate oracle commands, not whether SAMA provides a fundamentally better approach. The comparison with ROMA (trained from scratch) is not controlled.
**Fix:** (a) Add an ablation where the PLM planner is replaced with random subgoal selection or a simple heuristic. (b) Test SAMA without oracle information (e.g., using only observable enemy units). (c) Compare against RED without the PLM (RED without oracle commands) as a more informative baseline.

### Issue 4 (Major): Overstated conceptual framing via DRL
**Location:** Page 2-3 - DRL paragraph
**Risk:** The paper's framing as "disentangled decision-making" is not technically accurate—SAMA does not perform disentangled representation learning. This may mislead reviewers and readers about the nature of the contribution.
**Fix:** Replace "disentangled" with more precise terminology such as "semantically structured" or "commonsense-guided" subgoal decomposition. Remove the DRL comparison or reframe it as loose inspiration rather than technical connection.

### Issue 5 (Major): Self-reflection cost hidden from metrics
**Location:** Page 7 - Self-Reflection section
**Risk:** Self-reflection trials consume environment steps that are excluded from reported performance. If this overhead is substantial, the claimed sample efficiency is inflated.
**Fix:** (a) Report the average number of self-reflection trials per episode and the average environment steps consumed during reset-recovery. (b) Provide learning curves that include self-reflection steps in the x-axis to show true sample efficiency. (c) Add an ablation comparing SAMA with and without self-reflection.

## Actionable Suggestions
### S1 (Must): Validate PLM-generated reward functions
**Pages 6-7.** Add a quality analysis of the PLM-generated code snippets D_code. Report: (a) compilation success rate, (b) precision and recall on a held-out manually labeled set of states for each subgoal type, (c) the percentage of subgoals where the PLM-generated reward function disagrees with an oracle script-based reward. If any subgoal type has precision below 90%, provide a manual correction or fallback mechanism.

### S2 (Must): Add statistical rigor to learning curves
**Page 8.** Add standard deviation bands or 95% confidence intervals (over the 10 random seeds) to all learning curves in Figure 5 and Figure 10. Report the number of environment steps to reach 90% of the final converged reward for each method. Perform paired permutation tests (or Wilcoxon signed-rank) comparing SAMA's final performance against each baseline.

### S3 (Must): Ablate PLM contribution in MiniRTS
**Page 9.** Add an ablation that replaces the PLM planner with: (a) random subgoal selection from the valid subgoal set, (b) a simple scripted subgoal generator (e.g., always build counter units), and (c) SAMA without oracle information (only observable enemy units). Compare win rates and sample efficiency.

### S4 (Must): Report self-reflection overhead
**Page 7.** Report the average number of self-reflection trials per episode, the average environment steps consumed per trial, and the total self-reflection cost as a fraction of total environment steps. Provide learning curves that include these steps in the x-axis.

### S5 (Nice-to-have): Reframe DRL connection
**Pages 2-3.** Replace the "disentangled representation learning" framing with more precise terminology. Suggested replacement: "Inspired by the ideal of semantically meaningful factorization in DRL, we propose a coarser but more practical approach: leveraging PLMs as a source of commonsense priors to directly generate semantically meaningful subgoals." Remove "disentangled decision-making" and replace with "semantically structured decision-making" or "commonsense-guided task decomposition."

### S6 (Nice-to-have): Clarify contribution statements
**Page 3.** Rewrite contribution 1 to state a specific capability enabled (e.g., "SAMA is the first framework to combine PLM-based task-level planning with language-grounded MARL for subgoal execution, eliminating the need for end-to-end learning of subgoal decomposition"). Rewrite contribution 3 to be a specific empirical finding rather than a generic performance claim.

### S7 (Nice-to-have): Add ablation on object extraction
**Page 5.** Move the object extraction ablation from Appendix H (assuming it exists) to the main paper, or at least cite specific numbers. The claim that object extraction "considerably constrains the goal space" should be backed by quantitative comparison of subgoal space size and sample efficiency with/without extraction.

### S8 (Nice-to-have): Justify Markov assumption
**Page 3.** Provide empirical evidence that the Markov planning assumption holds in the tested environments. For example, test whether providing the planner with the last k states (instead of just the current state) changes PLM output quality or task success rate.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current storyline follows: credit assignment problem → exploration limitation → subgoal methods → ASG over-representation → DRL inspiration → SAMA solution. The main weakness is that the DRL framing is misleading and the transition from "problem" to "solution" is not tight enough—the reader must infer why PLMs (rather than learned representations) are the natural answer to the over-representation problem.

### Alternative Storyline Candidate 1 (Recommended)

**Arc:** Practical problem → Concrete gap → Commonsense intuition → Technical solution → Empirical validation.

- **P1 (Problem):** Cooperative MARL with sparse rewards suffers from severe sample inefficiency because agents must learn both what to do (task planning) and how to do it (low-level control) from sparse feedback.
- **P2 (Prior gap):** Existing ASG methods attempt to learn subgoal decomposition end-to-end but require massive samples and produce task-irrelevant subgoals due to unconstrained diversity objectives.
- **P3 (Key insight):** Humans solve this by using commonsense—we know ingredient preparation precedes cooking without trial-and-error. PLMs encode similar commonsense about sequential and collaborative tasks.
- **P4 (Solution):** SAMA decouples task-level planning (what subgoals to pursue) from low-level control (how to execute subgoals). PLMs handle planning via prompting; language-grounded MARL handles execution via learned policies.
- **P5 (Evidence):** Experiments show SAMA achieves comparable performance with 5-10x fewer environment steps, validating the benefits of injecting commonsense priors.

### Alternative Storyline Candidate 2 (More conservative)

**Arc:** Value decomposition+x → limitations of "x" = ASG → specific failure mode (over-representation) → proposed remedy.

- Focuses on the "value decomposition+x" framework as the organizing principle throughout.
- Positions SAMA as a new "x" that replaces learned subgoal decomposition with PLM-based decomposition.
- Less emphasis on DRL inspiration, more emphasis on practical sample efficiency.

### Abstract Outline (Recommended)

- **S1 (Domain + problem):** Cooperative MARL with sparse rewards faces sample inefficiency due to the dual challenge of temporal and structural credit assignment.
- **S2 (Prior gap):** Automatic subgoal generation (ASG) methods address this via end-to-end learning of subgoal decomposition, but require massive samples and generate task-irrelevant subgoals.
- **S3 (Proposed method):** SAMA uses PLM prompting with chain-of-thought to generate semantically meaningful goals, decompose them into subgoals, and allocate them to agents, augmented by self-reflection for error recovery.
- **S4 (Mechanism):** A language-grounded MARL policy learns to execute natural-language subgoals by grounding them in non-textual observations via PLM-generated reward functions.
- **S5 (Result):** On Overcooked (5 layouts) and MiniRTS, SAMA achieves comparable final performance with approximately 5-10x fewer environment interactions than prior ASG methods.

### Introduction Outline (Recommended, 4 paragraphs)

- **P1 (Stakes + problem):** "Cooperative MARL under sparse rewards suffers from ... The credit assignment problem operates at two scales ... Current methods follow a value decomposition+x framework, where x addresses temporal credit assignment."
- **P2 (Prior solutions and their limits):** "Exploration-based x methods improve task selection but fall short ... Subgoal-based ASG methods provide dense goal-directed rewards but learn task decomposition end-to-end, requiring massive samples and producing irrelevant subgoals due to diversity pressure."
- **P3 (Key insight and proposed approach):** "We observe that humans use commonsense to focus on functional subgoals. PLMs encode similar knowledge. We thus propose SAMA, which replaces learned subgoal decomposition with PLM-based prompting, achieving semantically meaningful task planning without training."
- **P4 (Contributions):** "We contribute (1) SAMA, a hierarchical framework decoupling PLM-based task planning from language-grounded MARL execution; (2) a fully automated preprocessing pipeline for translating environments to text; (3) empirical demonstration of 5-10x sample efficiency gains on Overcooked and MiniRTS."

## Priority Revision Plan
### P0 (Critical — must fix before resubmission)

| ID | Revision | Effort | Impact | Location |
|----|----------|--------|--------|----------|
| P0.1 | Validate PLM-generated reward functions (compilation rate, precision/recall against held-out labels) | 1-2 weeks for labeling + analysis | High: establishes training signal reliability | Page 6, Section 3.3 |
| P0.2 | Add statistical rigor: error bands, significance tests, step-to-threshold reporting | 1-2 weeks for re-running + analysis | High: supports main sample efficiency claim | Page 8, Section 4.1 |
| P0.3 | Ablate PLM contribution in MiniRTS: non-PLM baselines, no-oracle variant | 1-2 weeks for experiments | High: disentangles PLM vs RED contribution | Page 9, Section 4.2 |
| P0.4 | Report self-reflection overhead (trials/episode, steps consumed) and include in learning curves | 1 week for logging + analysis | High: ensures sample efficiency claim is not inflated | Page 7, Section 3.4 |

### P1 (Major — should fix for strong resubmission)

| ID | Revision | Effort | Impact | Location |
|----|----------|--------|--------|----------|
| P1.1 | Reframe DRL connection and remove "disentangled decision-making" | 1-2 days for rewriting | Medium: improves conceptual clarity | Pages 2-3 |
| P1.2 | Clarify contribution statements with concrete, falsifiable claims | 1 day for rewriting | Medium: improves positioning | Page 3 |
| P1.3 | Add object extraction ablation to main paper | 1 week for analysis | Medium: supports design claim | Page 5 |

### P2 (Nice-to-have — quality improvement)

| ID | Revision | Effort | Impact | Location |
|----|----------|--------|--------|----------|
| P2.1 | Justify Markov planning assumption empirically | 1 week for experiments | Low-Medium | Page 3 |
| P2.2 | Test sensitivity to reflection limit hyperparameter | 3-5 days | Low | Page 7 |
| P2.3 | Add cost-benefit analysis of PLM query overhead vs sample savings | 1 week | Medium | Appendix E |

### Expected Impact After P0 Fixes

Fixing P0 items would address the four most critical risks: (1) training signal reliability, (2) statistical validity of the core claim, (3) confounding of PLM contribution, and (4) hidden sample cost. After P0 fixes, the paper's empirical claims would be substantially more defensible. P1 fixes would improve conceptual framing and narrative clarity. The paper would then be suitable for a top-tier venue with the understanding that novelty verification is still required (see Novelty section).

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|------------|
| E1: Overcooked - Cramped Room | Test SAMA in simple coordination | Overcooked/Cramped Room, 10 seeds, 400 timesteps/ep | Avg reward per episode | SAMA matches COLE at ~2M steps vs COLE ~10M steps | Sample efficiency | No error bars; single layout |
| E2: Overcooked - Asymm Adv | Test SAMA with asymmetric roles | Overcooked/Asymmetric Advantages | Avg reward per episode | SAMA near COLE performance with ~5x fewer steps | Sample efficiency | COLE targets different problem |
| E3: Overcooked - Coord Ring | Test SAMA with spatial coordination | Overcooked/Coordination Ring | Avg reward per episode | SAMA competitive but not best at convergence | Partial sample efficiency | Performance gap at convergence |
| E4: Overcooked - Forced Coord | Test SAMA with forced cooperation | Overcooked/Forced Coordination | Avg reward per episode | SAMA approaches COLE with ~10x fewer steps | Sample efficiency | Self-reflection cost not counted |
| E5: Overcooked - Counter Circ | Test SAMA with complex layout | Overcooked/Counter Circuit | Avg reward per episode | SAMA competitive but lower than COLE | Partial | PLM long-horizon limitation noted |
| E6: MiniRTS | Test SAMA in real-time strategy | MiniRTS, medium AI, 100 test games, 3 seeds | Win rate | SAMA approaches RED (~75% vs ~85%) | PLM can approximate oracle | Oracle prompts; RED initialization |

### Research-Theme Gap Diagnosis

1. **New knowledge:** The paper demonstrates that PLM-generated subgoals can substitute for learned subgoal decomposition in ASG, improving sample efficiency. However, it is unclear whether this is because PLMs provide better subgoals, or because they avoid the sample cost of learning subgoal representations. The paper does not compare the quality of PLM-generated subgoals vs. learned subgoals (e.g., in terms of task relevance, diversity, or feasibility).

2. **Reproducibility/reusability:** The framework depends on closed-source PLMs (GPT-3.5/GPT-4) and environment-specific prompt engineering. Reproducibility is limited by the reliance on proprietary APIs and the lack of validated reward function code.

3. **Impact on practice/understanding:** If validated, SAMA could shift ASG research toward PLM-based planning. However, the practical value depends on whether the PLM query cost (monetary and latency) is justified by the sample savings—a trade-off the paper acknowledges but does not fully quantify.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|--------|-------------|------------|----------------|-------------------|---------|------------------|-----------|---------------|
| P0-A | PLM reward quality | PLM-generated rewards have >=90% accuracy | Label 100 states per subgoal type; compare PLM reward vs ground truth | Random reward; oracle script reward | Precision, recall, F1 | Precision >=90%, recall >=85% | 1-2 weeks | High: validates training signal |
| P0-B | Sample efficiency statistical claim | SAMA uses 5-10x fewer steps with p<0.05 | Re-run with logged step-to-threshold; bootstrap test | All baselines | Steps to 90% reward; p-value | p<0.05 vs top 3 baselines | 2 weeks | High: supports main claim |
| P0-C | PLM vs non-PLM planning in MiniRTS | PLM planner outperforms random/scripted subgoals | Replace PLM with random/scripted subgoal selection | SAMA (original), random, scripted | Win rate, steps to build army | PLM > script > random | 1-2 weeks | High: separates PLM contribution |
| P1-A | Object extraction benefit | Extraction improves sample efficiency by >=20% | Compare SAMA w/ and w/o object extraction | SAMA (extraction), SAMA (no extraction) | Steps to 90% reward | >=20% improvement | 1 week | Medium: validates design choice |
| P1-B | Self-reflection sensitivity | Performance robust to reflection limit >=1 | Vary max reflections {0,1,2,3,5} | SAMA (3 reflections) | Final reward, overhead cost | Minimal degradation at limit=1 | 1 week | Medium: informs hyperparameter |
| P2-A | PLM cost-benefit | Net time saving when PLM cost is included | Compare wall-clock time to convergence | All baselines | Wall time to 90% reward | SAMA faster despite PLM overhead | 1 week | Low: practical trade-off analysis |

```text
ASCII Diagram — Experiment Upgrade Plan
Stage 1 (P0, immediate): Reward validation -> Statistical rigor -> MiniRTS ablation
        |
        v
Stage 2 (P1, this month): Object extraction ablation -> Self-reflection sensitivity
        |
        v
Stage 3 (P2, before submission): Cost-benefit analysis -> Markov assumption test
        |
        v
Final: All claims validated with statistical evidence and controlled ablations
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
## Scores

**Final Score: 5.5/10**

**Rationale:** The paper addresses a relevant problem (sample inefficiency in sparse-reward MARL) and proposes a technically interesting synthesis of PLM-based planning with language-grounded MARL. However, the score is constrained by several significant weaknesses:

- **Novelty (4.5/10**: The core idea is reasonable but the conceptual framing via DRL is overstated. Novelty verification is deferred (Retrieval-Disabled Mode), so external literature comparison is unavailable. Based on manuscript evidence alone, the contribution is incremental—combining existing PLM prompting techniques with existing MARL frameworks.
- **Validity/Soundness 5/10**: The main empirical claim (5-10x sample efficiency) lacks statistical rigor. PLM-generated reward functions are unvalidated. Self-reflection costs are hidden from metrics. The MiniRTS experiment conflates contributions.
- **Reproducibility 4/10**: Heavy dependence on closed-source GPT APIs, environment-specific prompt engineering, and unvalidated PLM-generated code. Key hyperparameters and prompt templates are in appendix but reward function quality is unreported.
- **Presentation/Writing 6/10**: Generally well-structured with clear figures. However, overclaims ("disentangled," "innate predispositions," "alternative methods cannot distill"), vague contribution statements, and a few grammatical errors reduce clarity.

**Post-Revision Target: [6.5, 7.5]/10**

**Conditions:** A score in this range is achievable if the authors:

1. (P0) Validate PLM-generated reward functions with compilation rate and accuracy metrics.
2. (P0) Add statistical rigor (error bands, significance tests, step-to-threshold reporting).
3. (P0) Ablate PLM contribution in MiniRTS with non-PLM baselines and no-oracle variant.
4. (P0) Report self-reflection overhead and include it in learning curves.
5. (P1) Reframe the DRL connection with accurate terminology.
6. (P1) Sharpen contribution statements to be concrete and falsifiable.

If all P0 and P1 items are convincingly addressed, the paper would present a solid empirical contribution with a reasonably novel integration of ideas, meriting a score in the 6.5-7.5 range.