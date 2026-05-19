## Summary
# Final Review Report

## Summary

This paper proposes TreeDQN, an off-policy reinforcement learning method for learning branching heuristics in Branch-and-Bound (B&B) solvers for Mixed Integer Linear Programs (MILPs). The key technical innovations are: (1) modeling the variable selection process as a tree Markov Decision Process (tree MDP) and proving the contraction property of its Bellman operator, (2) using a mean-squared logarithmic error (MSLE) loss function that optimizes the geometric mean of expected return to handle long-tailed tree-size distributions, and (3) adapting the Double Dueling DQN architecture with experience replay for sample-efficient off-policy learning.

The method is evaluated on five NP-hard benchmark tasks (Combinatorial Auction, Set Cover, Maximum Independent Set, Facility Location, Multiple Knapsack) and an additional Balanced Item Placement task from the ML4CO competition. Results show that TreeDQN outperforms prior RL-based branching methods (FMCTS and tmdp+DFS) on in-distribution test tasks, achieves competitive performance with Imitation Learning on most tasks while substantially surpassing it on Multiple Knapsack, and demonstrates moderate generalization to larger transfer instances.

**Strengths:** Clean problem formulation via tree MDP with theoretical contraction guarantee; practical MSLE loss that empirically improves training stability; comprehensive evaluation across multiple NP-hard benchmarks with statistical significance testing; strong results on Multiple Knapsack and Balanced Item Placement tasks.

**Weaknesses:** Contraction proof has logical gaps (bound depends on circular reasoning about tree node counts); training-testing distribution mismatch due to different node selection policies is under-analyzed; the method's advantage over Imitation Learning is marginal on 4 of 5 test tasks; transfer generalization is mixed, with TreeDQN underperforming baselines on some tasks.

## Strengths
**S1. Clean theoretical framing via tree MDP.** The paper correctly identifies that the standard temporal MDP is insufficient for modeling B&B variable selection and adopts the tree MDP framework. The proof attempt for contraction in mean, despite some gaps, represents a genuine effort to provide theoretical grounding for value-based RL in tree-structured environments.

**S2. Practical contribution of MSLE loss.** The MSLE loss function is a simple yet effective modification to DQN that empirically stabilizes training under high-variance returns. The ablation study cleanly demonstrates its advantage over standard MSE loss across all five benchmark tasks, with statistical significance on three tasks.

**S3. Comprehensive evaluation across diverse NP-hard benchmarks.** The paper evaluates on five different combinatorial optimization problem types with both in-distribution and transfer (larger) instances. The use of geometric mean, geometric standard deviation, Wilcoxon signed-rank tests, P-P plots, and winning rates provides a thorough statistical analysis that goes beyond simple point estimates.

**S4. Strong results on challenging tasks.** On Multiple Knapsack, TreeDQN achieves a geometric mean tree size of 290 vs IL's 670 (a 57% reduction). On the Balanced Item Placement task (Appendix D), TreeDQN achieves the highest cumulative dual integral (5958) with significantly fewer LP solves than IL, demonstrating practical value on real-world-inspired problems.

**S5. Sample efficiency.** TreeDQN requires only 200-850 training episodes to reach its best checkpoint, compared to tmdp+DFS requiring thousands (up to 22,500). This is a meaningful practical advantage given the computational cost of solving MILPs.

**S6. Code availability.** The authors provide anonymous code, supporting reproducibility.

## Weaknesses
**W1. Contraction proof is not rigorous.** The proof of Theorem 4.1 (contraction in mean) has several logical gaps. The derivation drops the discount factor $\gamma$ without comment, and the claim that $\mathbb{E}[p_+ + p_-] = (N-1)/N$ uses a circular argument: $N$ (the total number of nodes) is itself a random variable determined by the branching process that $p_+, p_-$ are meant to characterize. Furthermore, the proof assumes $p_+, p_-$ are state-independent, which is acknowledged as "close to" the B&B pruning process but not formally justified. If this key theoretical claim cannot be made rigorous, the paper should either provide a complete proof under well-specified assumptions or downgrade the claim to a heuristic justification. (See Page 5 - Section 4.1 annotation)

**W2. Training-testing node selection mismatch is under-analyzed.** The paper trains with DFS node selection but switches to SCIP default at test time. The authors acknowledge a "gap" and assert it is "often considered moderate" without supporting evidence. This distribution shift threatens both the validity of the Markov property at test time and the generalization of the learned policy. An ablation comparing DFS-evaluated vs. SCIP-default-evaluated performance is needed to quantify this gap. (See Page 3 - Section 2.2 Tree MDP annotation)

**W3. Marginal advantage over Imitation Learning on most tasks.** On 4 of 5 test tasks, TreeDQN achieves geometric mean tree sizes within 2-5% of Imitation Learning (IL), and these differences are smaller than the reported geometric standard deviations (which are multiplicative factors of 2-6x). The only clear win is on Multiple Knapsack. This weakens the claim that the method "produces smaller trees" as a general statement — the primary advantage over IL appears to be sample efficiency and the ability to surpass the expert on specific tasks, not universally smaller trees. (See Page 7 - Evaluation Table 3 annotation)

**W4. Mixed transfer generalization.** On transfer tasks, TreeDQN does not uniformly outperform prior RL methods: FMCTS has better geometric mean on Combinatorial Auction (1375 vs 1567), and tmdp+DFS wins on Maximum Independent Set (1713 vs 4541). The claim in the abstract that the method "produces smaller trees compared to previous reinforcement learning methods" is not consistently supported in the transfer setting. (See Page 8 - Transfer results annotation)

**W5. Node-limit censoring affects transfer comparisons.** For transfer tasks, instances reaching the 200,000 node limit are assigned that limit as their tree size. Table 9 shows that TreeDQN has 4, 6, and 23 such terminated instances across tasks. This downward-biases the geometric mean, making TreeDQN appear better on hard instances than it actually is. The paper should report which instances hit the node limit and present results with and without censoring. (See Page 8 - Transfer results annotation)

**W6. Limited ablation scope.** The only ablation compares MSLE vs MSE loss. No ablation isolates the contribution of the dueling architecture, target network, experience replay, or the GCNN backbone. Without these, it is unclear which components are critical for the observed performance gains. (See Page 8 - Ablation Study annotation)

## Key Issues
### Issue 1 (Critical): Contraction proof has logical gaps that undermine theoretical contribution

**Location:** Page 4-5, Section 4.1

**Evidence:** The proof claims $\mathbb{E}[p_+ + p_-] = (N-1)/N < 1$ by noting that "the number of edges is one less than the number of nodes" in a finite rooted tree. This is a structural property of a fully constructed tree, not a probabilistic statement about per-node branching probabilities during the B&B process. Since $N$ (tree size) is itself determined by the branching decisions that $p_+, p_-$ are meant to characterize, the argument is circular. The discount factor $\gamma$ also disappears from the contraction factor without explanation.

**Impact:** If the contraction claim cannot be rigorously justified, the theoretical foundation for applying DQN to tree MDP is weakened from "proven convergence guarantee" to "heuristic extension." This affects the paper's second major claimed contribution (proving contraction property).

**Required action:** Provide a corrected proof under well-defined assumptions, or downgrade the claim from "proved" to "heuristic justification supported by empirical evidence." A proper proof would either: (a) show contraction in expectation under a different norm, (b) assume a uniform upper bound $p_+ + p_- \leq c < 1$ on each node, or (c) prove contraction for terminal rewards without bootstrapping.

### Issue 2 (Major): Training-testing distribution gap is unquantified

**Location:** Page 3, Section 2.2 (Tree MDP)

**Evidence:** The paper trains with DFS node selection but evaluates with SCIP default node selection. The authors state: "This gap is often considered moderate and does not affect the performance significantly" — without providing any experimental evidence for this claim.

**Impact:** If the distribution shift is significant, the reported test/transfer results may not reflect the performance of the policy under the training-time conditions. The gap could also explain why TreeDQN underperforms tmdp+DFS on some transfer tasks, as tmdp+DFS may handle the shift differently.

**Required action:** Add an ablation comparing DFS-evaluated performance vs. SCIP-default-evaluated performance for all methods. This would quantify the gap and validate (or refute) the claim that the gap is moderate.

### Issue 3 (Major): The method's improvement over Imitation Learning is marginal on most tasks

**Location:** Page 7, Table 3

**Evidence:** On Combinatorial Auction (56 vs 58), Set Cover (53 vs 56), Max Independent Set (42 vs 42), and Facility Location (323 vs 324), TreeDQN and IL produce nearly identical geometric mean tree sizes. The differences are within the multiplicative geometric standard deviations (e.g., 58 ± 3 vs 56 ± 3 for Comb.Auct means the 1-sigma ranges heavily overlap: [58/3, 58×3] ≈ [19, 174] vs [56/3, 56×3] ≈ [19, 168]).

**Impact:** The paper's headline claim of "producing smaller trees" is supported primarily by the Multiple Knapsack result. On 4 of 5 tasks, the method does not produce meaningfully smaller trees than IL. This should be prominently discussed and the claims bounded accordingly.

**Required action:** Reframe the narrative to emphasize sample efficiency and the Multiple Knapsack result as the primary empirical contribution, rather than claiming universal improvement in tree size.

### Issue 4 (Major): Transfer results contradict the abstract's claim of universal improvement over prior RL methods

**Location:** Page 8-9, Table 5

**Evidence:** On transfer tasks: FMCTS outperforms TreeDQN on Combinatorial Auction (1375 vs 1567), tmdp+DFS outperforms TreeDQN on Maximum Independent Set (1713 vs 4541). These are not marginal differences — TreeDQN is 2.65× worse on Max Independent Set.

**Impact:** The abstract states "produces smaller trees compared to previous reinforcement learning methods" without qualification. This is not consistently true for transfer tasks and misleads readers about the method's generalization capability.

**Required action:** Qualify the abstract and conclusion to acknowledge that while TreeDQN excels on in-distribution test tasks and some transfer tasks, it does not universally outperform all baselines in the transfer setting.

### Issue 5 (Moderate): Node-limit censoring biases transfer results

**Location:** Page 8, Table 5, Table 9

**Evidence:** For instances exceeding the 200,000 node limit, the paper uses the limit as the tree size. Table 9 shows termination counts vary across methods. If TreeDQN consistently terminates more instances (or fewer) than baselines, the censoring procedure affects the relative ranking.

**Required action:** Report the mean/median tree size *excluding* terminated instances alongside the censored results. Alternatively, use survival analysis techniques to handle the censored data properly.

## Actionable Suggestions
### Suggestion 1 (Must): Fix the contraction proof

**Problem:** The proof of Theorem 4.1 uses circular reasoning by relating per-node branching probabilities to the total tree node count $N$, which is itself a random variable determined by the branching process.

**Fix:** Provide a corrected proof with one of these approaches:
- **Option A (preferred):** Prove that the tree Bellman operator is a contraction in expectation under the assumption that for all states $s$, $p_+(s) + p_-(s) \leq c < 1$ uniformly. This avoids the circular node-count argument.
- **Option B:** If the uniform bound cannot be guaranteed, prove contraction for the terminal-reward case (no bootstrapping), where the tree Bellman operator reduces to the immediate reward.
- **Option C:** If neither proof is feasible, clearly state that the contraction property is a heuristic motivation rather than a proven guarantee, and provide empirical evidence of convergence (e.g., loss curves showing TD-error decreasing).

### Suggestion 2 (Must): Quantify the training-testing node selection gap

**Problem:** The paper switches from DFS (training) to SCIP default (testing) node selection without quantifying the distribution shift.

**Fix:** Add an experiment that evaluates all methods under both DFS and SCIP default node selection on the test set. Report the relative change in tree size for each method. If the gap is indeed moderate (e.g., <10% relative change), this validates the claim. If not, the results under SCIP default should be interpreted with caution.

### Suggestion 3 (Must): Bounded framing of empirical claims

**Problem:** The abstract claims "requires less training data and produces smaller trees compared to previous reinforcement learning methods" without qualifications.

**Fix:** Revise the abstract and conclusion to reflect the nuanced results:
- On in-distribution test tasks, TreeDQN improves over prior RL methods (FMCTS, tmdp+DFS) by 5-30% in geometric mean tree size.
- On transfer tasks, improvements are task-dependent (best on 3 of 5 tasks).
- TreeDQN is competitive with Imitation Learning on most tasks and substantially better on Multiple Knapsack.
- The primary advantage is sample efficiency (fewer training episodes and off-policy learning).

### Suggestion 4 (Must): Handle node-limit censoring properly

**Problem:** Transfer results use the node limit (200k) as the tree size for terminated instances, which creates a downward bias.

**Fix:** Report both censored and uncensored geometric means. For uncensored reporting, exclude terminated instances and note the sample size. Alternatively, use the Kaplan-Meier estimator or similar survival-analysis approach for the expected tree size.

### Suggestion 5 (Nice-to-have): Expand ablation study

**Problem:** Only the MSLE vs MSE loss is ablated.

**Fix:** Add at least two additional ablations:
- **Architecture ablation:** Compare Double Dueling DQN vs. standard DQN with MSLE loss.
- **Discount factor sensitivity:** Test $\gamma \in \{0.9, 0.99, 1.0\}$ to assess sensitivity.
- **Experience replay size:** Compare buffer sizes to understand the effect on sample efficiency.

### Suggestion 6 (Nice-to-have): Improve introduction narrative

**Problem:** The introduction spends excessive space on generic RL success stories and insufficient space on the specific technical gap in branching.

**Fix:** Restructure the introduction to: (a) concisely motivate why branching matters, (b) identify the specific limitations of existing learning-based methods (bias-variance trade-off between FMCTS and tmdp+DFS), (c) state how TreeDQN resolves this trade-off, and (d) preview key results. (See annotation on Page 1 - Introduction.)

### Suggestion 7 (Nice-to-have): Clarify tree MDP reward notation

**Problem:** The reward function is inconsistently defined as $r(s)$, $r(s,a,s^\pm_{t+1})$, and $r(s,\pi(s))$ at different points.

**Fix:** Standardize the notation. Define $r(s,a)$ as the reward for taking action $a$ in state $s$, independent of the child states (which are determined by $p_+, p_-$). This simplifies the Bellman equation to $V(s_t) = r(s_t, a_t) + p_+ V(s^+_{t+1}) + p_- V(s^-_{t+1})$.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

**Target Structure (4-5 sentences):**

- **S1 (Problem + Domain):** "Branch-and-Bound (B&B) solvers for Mixed Integer Linear Programs (MILPs) depend critically on the branching heuristic for variable selection, but existing heuristics are either computationally expensive (Strong Branching) or designed for general-purpose use rather than distribution-specific adaptation."

- **S2 (Gap):** "Learning branching rules via reinforcement learning is challenging because B&B generates tree-structured search spaces with high-variance tree sizes, and prior RL methods suffer from a trade-off between sample efficiency (FMCTS) and unbiased learning (tmdp+DFS)."

- **S3 (Method):** "We propose TreeDQN, an off-policy DQN method that models variable selection as a tree Markov Decision Process (tree MDP). We prove contraction of the tree Bellman operator under mild assumptions and introduce a mean-squared logarithmic error (MSLE) loss that optimizes the geometric mean of expected return, stabilizing learning under long-tailed tree-size distributions."

- **S4 (Key Results):** "On five NP-hard benchmark tasks, TreeDQN reduces B&B tree size by 5-57% compared to prior RL-based branching methods and achieves competitive performance with Imitation Learning while requiring substantially fewer training episodes. On the challenging Balanced Item Placement task, TreeDQN achieves the highest dual integral among all tested methods."

- **S5 (Bounded Implication):** "These results demonstrate that combining tree-structured value learning with a geometric-mean objective yields a sample-efficient branching heuristic, with particular strength on problems where strong heuristics produce large search trees."

### Introduction Outline (Revised)

**Current structure assessment:** The current introduction has two paragraphs: (1) generic background on combinatorial optimization and B&B plus a broad RL success list, (2) challenges and proposed solution. The main issues are lack of a clear gap statement, excessive RL success examples, and insufficient positioning against prior ML-for-branching work.

**Proposed new structure (4 paragraphs):**

**Paragraph P1 — Problem and motivation (Big Picture)**
*Role:* Establish why branching matters and why learned heuristics are needed.
"Combinatorial optimization problems in logistics, finance, and manufacturing are often formulated as MILPs and solved via B&B. The efficiency of B&B depends critically on the branching heuristic — the rule for selecting which fractional variable to split at each node. While human-crafted heuristics like Strong Branching produce small search trees, they are computationally expensive. Moreover, practitioners often solve tasks from a specific distribution, so a branching rule adapted to that distribution could substantially reduce solve times."

**Paragraph P2 — Gap in prior work (Gap)**
*Role:* Summarize prior learning-based approaches and their limitations, creating a clear gap.
"Prior work has explored learning branching rules via imitation learning (IL) and reinforcement learning (RL). IL agents mimic Strong Branching but cannot surpass it. RL methods, on the other hand, can potentially learn better-than-expert heuristics. FMCTS (Etheve et al., 2020) uses off-policy Q-learning with DFS but suffers from bias due to stale data. tmdp+DFS (Scavuzzo et al., 2022) models B&B as a tree MDP and uses unbiased REINFORCE, but is sample-inefficient because each gradient step requires solving a batch of MILPs. A method that combines the sample efficiency of off-policy learning with the stability of value-based methods remains an open challenge."

**Paragraph P3 — Proposed solution (Solution)**
*Role:* Introduce TreeDQN and its three key components, explaining how each addresses a specific challenge.
"TreeDQN addresses the above challenges through three components. First, we adopt the tree MDP framework to naturally represent the tree-structured B&B process, and prove that the tree Bellman operator is contracting in mean — justifying the use of DQN-style value iteration. Second, we introduce an MSLE loss function that optimizes the geometric mean of expected return, which is more robust to the long-tailed tree-size distributions characteristic of imperfect branching. Third, we combine off-policy experience replay with Double Dueling DQN, enabling sample-efficient learning without the bias from stale trajectories."

**Paragraph P4 — Key results and paper structure (Evidence Preview + Contribution)**
*Role:* Preview results, state contributions, and outline paper structure.
"We evaluate TreeDQN on five NP-hard benchmarks and a real-world-inspired task. On in-distribution test tasks, TreeDQN produces smaller B&B trees than prior RL methods and matches or exceeds Imitation Learning performance, with the largest gains on problems where Strong Branching struggles—reducing tree size by 57% on Multiple Knapsack. On transfer to larger instances, TreeDQN generalizes competitively on three of five tasks. The method converges with 200-850 training episodes, an order of magnitude fewer than on-policy RL. Our main contributions are: (i) theoretical contraction analysis of the tree Bellman operator, (ii) the MSLE loss for geometric-mean optimization in RL, and (iii) empirical demonstration of sample-efficient branching learning."

### Alternative Storyline Candidates

**Candidate A — "Theory-First" Storyline** (recommended only if contraction proof is fixed)
Focus: Tree MDP theory → Contraction guarantee → Algorithm design → Empirical validation.
*Better if:* The authors can provide a rigorous contraction proof.
*Worse if:* The proof remains heuristic.

**Candidate B — "Practical Advantage" Storyline** (better matches current evidence)
Focus: Sample efficiency → Off-policy value learning → MSLE for stability → Empirical results.
*Better if:* The authors want to de-emphasize theory and highlight practical gains.
*Worse if:* Reviewers expect strong theoretical contribution for ICLR.

**Recommended: Candidate B** — The current evidence supports sample efficiency and MSLE stability more strongly than the contraction claim, which has gaps. Framing the paper around practical RL improvements for branching would be more defensible.

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: B&B branching is hard to learn]
    |
    v
[Gap: RL methods have bias-variance trade-off]
    ├── FMCTS: sample efficient but biased (off-policy)
    └── tmdp+DFS: unbiased but sample inefficient (on-policy)
    |
    v
[TreeDQN Solution]
    ├── Tree MDP formulation (+ contraction theorem)
    ├── MSLE loss (geometric mean optimization)
    └── Off-policy DQN with experience replay
    |
    v
[Evidence]
    ├── In-distribution test: TreeDQN > FMCTS, tmdp+DFS on 5/5 tasks
    ├── In-distribution test: TreeDQN ≈ IL on 4/5, >> IL on 1/5 tasks
    ├── Transfer: TreeDQN > baselines on 3/5, worse on 2/5 tasks
    ├── Ablation: MSLE > MSE, significant on 3/5 tasks
    └── Balanced Item Placement: TreeDQN > IL, SCIP, SB
    |
    v
[Key Weakness: Contraction proof not rigorous]
    |
    v
[Recommendation: Fix proof or downgrade claim + bounded narrative]
```

## Priority Revision Plan
### P0 — Publication-Critical (Must fix before acceptance)

| Priority | Item | Issue | Action | Expected Impact | Effort |
|----------|------|-------|--------|-----------------|--------|
| P0.1 | Contraction proof | Circular reasoning in Theorem 4.1 proof | Provide corrected proof under well-defined assumptions (uniform bound p+ + p- ≤ c < 1) or downgrade claim to heuristic | Restores theoretical credibility or avoids overclaim | High (theoretical work) |
| P0.2 | Claim bounding | Abstract overclaims universal improvement over prior RL methods | Qualify claims: distinguish in-distribution vs transfer, acknowledge IL-comparable performance on 4/5 tasks | Improves scientific accuracy and reviewer trust | Low (text editing) |
| P0.3 | Node selection gap | Training-testing node selection mismatch unquantified | Add ablation comparing DFS-evaluated vs SCIP-default-evaluated performance | Validates (or quantifies risk of) current evaluation protocol | Medium (extra experiments) |
| P0.4 | Node-limit censoring | Transfer results biased by using node limit as tree size | Report both censored and uncensored geometric means | Improves reliability of transfer conclusions | Low (re-analysis) |

### P1 — High Priority (Strongly recommended)

| Priority | Item | Issue | Action | Expected Impact | Effort |
|----------|------|-------|--------|-----------------|--------|
| P1.1 | Transfer discussion | TreeDQN underperforms baselines on 2/5 transfer tasks | Add explicit discussion of where TreeDQN fails and why | Improves scientific honesty and reader understanding | Low (text) |
| P1.2 | MSLE justification | Connection between MSLE loss and geometric mean of tree size is heuristic | Add explanation of how TD-target bootstrapping interacts with MSLE | Clarifies theoretical scope | Low (text) |
| P1.3 | Reward notation | r(s), r(s,a,s±), r(s,π(s)) used inconsistently | Standardize to r(s,a) throughout | Improves clarity | Low (text) |

### P2 — Quality Improvement (Nice to have)

| Priority | Item | Issue | Action | Expected Impact | Effort |
|----------|------|-------|--------|-----------------|--------|
| P2.1 | Ablation scope | Only MSLE vs MSE ablated | Add architecture ablation (DQN vs Dueling DQN) | Identifies key components | Medium (experiments) |
| P2.2 | Feature description | GCNN features not described | Add brief description of 19 variable and 5 constraint features | Improves reproducibility | Low (text) |
| P2.3 | Validation size | Only 20 validation instances used | Add justification or increase validation set size | Improves checkpoint selection reliability | Low |
| P2.4 | Real-world deployment discussion | No discussion of when TreeDQN would be preferred in practice | Add paragraph on practical use cases (distributions with hard instances where SB struggles) | Strengthens impact | Low (text) |

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0: Publication-Critical]
    ├── Fix contraction proof (theoretical rigor)
    │   └── Option A: Uniform bound assumption → clean proof
    │   └── Option B: Downgrade to heuristic motivation
    ├── Bound empirical claims (scientific accuracy)
    │   └── Qualify abstract + conclusion for transfer and IL comparison
    ├── Quantify train-test gap (validity risk)
    │   └── Ablation: DFS-evaluation vs SCIP-default evaluation
    └── Fix node-limit censoring (transfer reliability)
        └── Report censored + uncensored statistics

[P1: High Priority]
    ├── Add discussion of transfer failures (scientific honesty)
    ├── Clarify MSLE-to-tree-size connection (theoretical scope)
    └── Standardize reward notation (clarity)

[P2: Quality]
    ├── Expand ablation to DQN vs Dueling DQN (component analysis)
    ├── Describe GCNN features (reproducibility)
    └── Discuss practical deployment scenarios (impact)
    
[Expected outcome after revision]
    ├── Clearer theoretical scope (contraction = heuristic or rigorously bounded)
    ├── Well-qualified empirical claims matching evidence
    ├── Quantified understanding of train-test gap
    └── Stronger reproducibility and practical guidance
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 (Tab 3) | In-distribution test: compare TreeDQN vs baselines on 5 tasks | 40 instances × 5 seeds per task; DFS train, SCIP default test | Geometric mean tree size ± geo std | TreeDQN > FMCTS, tmdp+DFS on all tasks; TreeDQN ≈ IL on 4/5, >> IL on Multi-Knapsack | "produces smaller trees" (qualified) | IL comparison not statistically tested; 4/5 tasks show <5% difference |
| E2 (Tab 4) | Test-time execution speed | Same setup as E1 | Mean execution time ± std + Wilcoxon p-values | TreeDQN ≈ IL speed; both >> Strong Branching speed | "faster execution" | Speed advantage over IL is minimal; SCIP default is often faster |
| E3 (Fig 2, Tab 2) | Training convergence | 20 fixed instances, eval every 50 episodes | Geom mean tree size vs episodes; episodes to best checkpoint | TreeDQN converges in 200-850 episodes; tmdp+DFS needs 3000-22500 | Sample efficiency | Only 20 validation instances; checkpoint selection may be noisy |
| E4 (Fig 3) | Primal-dual gap over time | Same tasks as E1 | Gap vs time, over 5 seeds | TreeDQN reduces gap faster than FMCTS, slower than IL on some tasks | "faster gap reduction" | Visual comparison only; no quantitative metric |
| E5 (Fig 4, Tab 8) | P-P plots and arithmetic means | Same tasks as E1 | P-P plots (CDF comparison), arithmetic mean | TreeDQN better on easy instances; complex instances show performance drop | "geometric mean optimization focuses on easy instances" | This is a known limitation, not a strength |
| E6 (Tab 5, Tab 9) | Transfer generalization | Larger instances (different parameters); 200k node limit | Geom mean tree size; termination count | TreeDQN > baselines on 3/5 tasks; worse on 2/5 | Generalization capability | Node-limit censoring biases results; mixed performance |
| E7 (Tab 6, Fig 5) | Ablation: MSLE vs MSE loss | Same tasks as E1 | Geom mean tree size; loss curves; Wilcoxon test | MSLE better on all tasks; significant on 3/5 | MSLE improves training stability | No other ablations (architecture, discount, buffer size) |
| E8 (App D, Tab 13-14) | Balanced Item Placement | 100 test instances; 15-min time limit | Dual integral (reward), #Nodes, #LPs, Primal/Dual bound | TreeDQN achieves highest reward (5958) vs IL (4965) and SCIP (3885) | Sample efficiency on complex tasks | No comparison with FMCTS/tmdp+DFS; reward metric favors methods solving more nodes |

### Research-Theme Gap Diagnosis

**Claim 1 (New knowledge):** The tree MDP contraction property is claimed as new theoretical knowledge, but the proof gaps (Issue 1) weaken this contribution. The MSLE loss function is a practical contribution but its theoretical connection to the geometric mean of final tree size is heuristic.

**Claim 2 (Reproducibility):** The paper provides anonymous code and uses standard benchmarks (Ecole, SCIP). However, the GCNN features are not described, and the 20-instance validation set is small, which partially limits reproducibility.

**Claim 3 (Impact on practice):** The method's main practical value is sample efficiency (off-policy learning) and strong performance on problems where Strong Branching produces large trees (Multiple Knapsack, Balanced Item Placement). However, the mixed transfer results and marginal IL advantage on most tasks limit the scope of practical impact.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: Training-Testing Node Selection Gap Quantification

- **Target Claim:** "The gap between DFS training and SCIP-default testing is moderate"
- **Hypothesis:** Evaluating the TreeDQN policy under DFS node selection at test time yields similar tree sizes to SCIP-default evaluation
- **Minimal Design:** Evaluate all methods (TreeDQN, FMCTS, tmdp+DFS, IL) on 20 test instances with both DFS and SCIP-default node selection
- **Controls/Baselines:** Same methods evaluated under identical settings
- **Metrics:** Geometric mean tree size, percent change, correlation between DFS and SCIP-default rankings
- **Success Criterion:** Ranking of methods is preserved; tree size difference < 15%
- **Estimated Cost:** ~1-2 days on a single GPU server
- **Expected Quality Gain:** Validates the current evaluation protocol (if gap small) or identifies a confound (if gap large)

#### P0 Experiment: Contraction Proof Repair or Downgrade

- **Target Claim:** "Tree Bellman operator is contracting in mean"
- **Action:** Provide a corrected proof assuming uniformly bounded branching (p+ + p- ≤ c < 1 for all states), or explicitly downgrade to heuristic motivation
- **Minimal Design (if downgrading):** Add a paragraph stating "While a rigorous contraction proof under the tree MDP requires additional assumptions beyond standard MDP analysis, the empirical convergence shown in Fig. 2 and 5 suggests the DQN update is stable in practice"
- **Success Criterion:** No circular reasoning in proof; assumptions clearly stated
- **Estimated Cost:** 1-2 weeks for rigorous proof; 1 hour for text downgrade
- **Expected Quality Gain:** Either strengthens the theoretical contribution (if proof fixed) or prevents reviewer rejection (if downgraded)

#### P1 Experiment: Uncensored Transfer Analysis

- **Target Claim:** Transfer generalization results
- **Hypothesis:** The relative ranking of methods changes when terminated instances are excluded
- **Minimal Design:** For each transfer task, compute geometric mean both including and excluding instances that hit the 200k node limit
- **Controls/Baselines:** Same analysis for FMCTS, tmdp+DFS, IL
- **Metrics:** Geometric mean (censored), geometric mean (uncensored), proportion of terminated instances
- **Success Criterion:** The primary conclusions from Table 5 remain stable under both analyses
- **Estimated Cost:** ~1 day (re-analysis of existing data)
- **Expected Quality Gain:** Increases confidence in transfer conclusions

#### P2 Experiment: Architecture Ablation

- **Target Claim:** "TreeDQN's DQN architecture is the key to its performance"
- **Hypothesis:** Standard DQN with MSLE loss performs comparably to Double Dueling DQN with MSLE loss
- **Minimal Design:** Train TreeDQN without dueling architecture and without double Q-learning on 2 tasks (Comb.Auct, Set Cover)
- **Success Criterion:** Performance difference < 10% in geometric mean tree size
- **Estimated Cost:** ~2 days
- **Expected Quality Gain:** Identifies which components are essential

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 Experiments (Publication-Critical)
├── [E-P0.1] Quantify train-test node selection gap
│   ├── Task: Evaluate all methods under DFS + SCIP-default
│   └── Outcome: Validate or refute "moderate gap" claim
└── [E-P0.2] Fix or downgrade contraction proof
    ├── Task: Clean proof under uniform bound, or heuristic downgrade
    └── Outcome: Remove circular reasoning

P1 Experiments (High Priority)
└── [E-P1.1] Uncensored transfer analysis
    ├── Task: Report geometric means with/without terminated instances
    └── Outcome: Verify transfer ranking stability

P2 Experiments (Quality Improvement)
└── [E-P2.1] Architecture ablation
    ├── Task: DQN vs Double Dueling DQN on 2 tasks
    └── Outcome: Isolate key components

Timeline:
Week 1: E-P0.1 (experiments) + E-P0.2 (proof/text work)
Week 2: E-P1.1 (re-analysis) + E-P2.1 (if time permits)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

**Rationale:** The paper presents a well-motivated and empirically sound approach to learning branching heuristics for MILP solvers. The practical contributions (MSLE loss, off-policy DQN for tree MDP, comprehensive evaluation) are meaningful advances over prior work. However, the score is constrained by:

- **Contribution rigor (weight: high):** The theoretical claim of contraction in mean is not rigorously proven (Issue 1), which weakens the paper's main claimed theoretical contribution. (-1 point)
- **Empirical scope (weight: high):** The method's advantage over Imitation Learning is marginal on 4 of 5 test tasks; the abstract overclaims universal improvement. (-0.5 point)
- **Transfer generalizability (weight: medium):** Mixed transfer results are underdiscussed; the claim "produces smaller trees" does not fully hold in the transfer setting. (-0.5 point)
- **Validity (weight: high):** The training-testing node selection gap is unquantified, creating uncertainty about the evaluation protocol. (-0.5 point)
- **Reproducibility (weight: medium):** Code is provided, but GCNN feature details are missing. (-0.5 point)

**Strengths supporting score:** Clean problem framing via tree MDP; practical MSLE loss with empirical validation; comprehensive evaluation with proper statistical testing; strong results on Multiple Knapsack and Balanced Item Placement; sample efficiency advantage over on-policy methods. (+6 points baseline for solid submission with clear contributions)

**Post-Revision Target: [7, 8]/10**

- **Lower bound (7/10):** Achievable if the authors: (a) fix or downgrade the contraction claim, (b) bound empirical claims to match evidence, (c) quantify the train-test node selection gap, and (d) handle node-limit censoring properly. These are all P0 items.
- **Upper bound (8/10):** Achievable if in addition the authors provide cleaner transfer results, add a meaningful architecture ablation, and include a more detailed discussion of failure modes.

The paper has the potential to be a solid conference contribution (7-8 range) after addressing the identified issues, particularly the contraction proof gap and the need for qualified empirical claims.