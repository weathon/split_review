---
job_id: 9e1d8ce5-cf8e-40d1-a449-11b7f96a0d5f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GODFBZhFcX.pdf
paper: From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining LLM-based planning, uncertainty-aware reasoning, decentralized decision making, and embodied multi-agent cooperation in robotics-like simulated environments.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, method, experiments, results/analysis, and conclusion; while several methodological details are underspecified, the submission clears the minimum bar for review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-targeting prompts, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes PCE, a Planner-Composer-Evaluator framework for embodied multi-agent planning under partial observability. The main idea is to extract implicit assumptions from an LLM planner’s reasoning trace, organize them into a decision tree whose internal nodes represent assumptions and leaves represent actions, and then score each scenario-action path using likelihood, gain, and cost to select actions while reducing reliance on frequent communication. Experiments on C-WAH and TDW-MAT, across three LLM backbones, plus ablations and a small user study, are presented to support the claim that structured uncertainty handling improves task performance and communication efficiency.

## Strengths
1. The paper targets a meaningful problem. Multi-agent embodied planning under partial observability with costly communication is a real bottleneck for current LLM-agent systems, and the paper is right to focus on uncertainty handling rather than treating more communication as a free fix.

2. The central idea is intuitive and practically relevant. Converting latent assumptions in reasoning traces into explicit scenario branches is a sensible way to make hidden uncertainty actionable. Even if some pieces are heuristic, the overall framing is useful and easy to relate to agent failures in these environments.

3. The modular decomposition is clear at a high level. **Figure 1** is effective in showing where PCE sits in the standard embodied-agent stack, and **Figure 2** does a good job illustrating the transition from planner reasoning trace, to composer-generated scenario tree, to evaluator-selected action. In particular, **Figure 2(c)** makes the intended decision rule visually understandable, namely that action choice is not taken directly from the planner output but from the highest-scoring scenario leaf after uncertainty restructuring.

4. The empirical results are consistently favorable on the reported benchmarks. In **Table 1**, PCE is best on C-WAH total steps for all three backbones, with substantial margins over CoELA, CaPo, and CoTS, and also clearly lower communication counts than communication-heavy baselines. In **Table 2**, PCE is again best on TDW-MAT total performance across all three backbones and categories, which suggests the method is not tied to a single backbone or a single environment.

5. The ablation is reasonably informative. **Table 3** shows that removing Planner, Composer, or Evaluator degrades performance, which at least supports the claim that the full pipeline matters. **Figure 3** is also helpful in making the paper’s intended point that scaling model size or reasoning depth alone does not close the gap to structured uncertainty handling.

6. The paper goes beyond pure benchmark numbers by including a human-facing evaluation. The user study is limited, but the attempt to assess whether selective communication is perceived as more aligned and trustworthy is a useful addition. **Figure 4** communicates this result clearly enough at a glance.

7. The method is general in the sense that it does not depend on hidden model internals or specialized training. Operating on text reasoning traces and available actions makes the framework easier to transplant across LLM backbones than methods requiring fine-tuning or task-specific learned uncertainty modules.

## Weaknesses
1. **The mathematical formulation of the evaluator is not internally consistent with the implemented scoring protocol.**  
   In **Section 4.4, Pages 6-7**, the paper defines normalized scores in $[0,1]$, with
   \[
   \mathbb{E}[\text{gain}] = \mathcal{L}(\mathcal{S}) \cdot \mathcal{G}(a),
   \quad
   U(\mathcal{S}, a) = \mathbb{E}[\text{gain}] - \lambda C(a),
   \]
   and
   \[
   C(a)=\alpha d(a)\mathbf{1}\{\mathrm{move}(a)\} + \beta \ell(a)\mathbf{1}\{\mathrm{comm}(a)\}.
   \]
   However, the actual **Evaluator prompt in Figure 10 / Pages 29-30** asks the LLM to output integer scores in $\{1,\dots,5\}$ for Likelihood, Gain, and CostPenalty, with hand-written buckets such as “$1$ = communication or short move less than $3$m”, “$5$ = long movement across multiple rooms”. This is not a cosmetic issue. The paper presents one scoring model in the method section and apparently implements another in the prompts. It is therefore unclear whether the reported results correspond to the continuous utility in the paper, a discretized heuristic utility, or some post-hoc mapping between the two. This matters because the evaluator is the core decision mechanism of PCE. The paper needs to specify the exact instantiated utility used in experiments, including whether Likelihood/Gain/Cost are normalized to $[0,1]$, kept on a 1-5 ordinal scale, or transformed before computing $U$.

2. **The decision-tree construction is underspecified enough that reproducibility and scientific interpretability suffer.**  
   In **Section 4.3, Page 6**, the Composer is said to use a “local ranking policy” to choose the next assumption, prioritizing assumptions that “most reduce uncertainty” and “most strongly influence subsequent action choice,” but this ranking policy is never operationally defined beyond “approximated using LLMs’ commonsense reasoning.” The stopping rule is similarly vague: expansion stops at depth $D$ or “when further splits would not materially affect action choice.” This is the heart of the method, yet the paper does not define what counts as “materially affect,” how branch consistency is checked, how duplicate or semantically equivalent assumptions are merged, or how the system handles contradictory branches produced by the LLM. **Figure 2(b)** gives an attractive cartoon of the process, but the actual algorithm remains mostly prompt-level intuition. For a paper making a structural-method claim, this is too loose.

3. **The paper repeatedly uses strong wording such as “principled,” “rational,” and “systematically” without enough evidence that the method deserves those labels.**  
   The evaluator is entirely LLM-judged, the composer’s branching policy is heuristic, and the probabilities are explicitly not true probabilities. This is fine as a pragmatic agent framework, but the paper sometimes writes as if the method is closer to a well-defined decision-theoretic planner than it actually is. For instance, **Section 4.4** says “ranking leaves by $U(\mathcal{S},a)$ yields a rational action choice under uncertainty,” which overstates the case given that both $\mathcal{L}$ and $\mathcal{G}$ are subjective LLM scores rather than calibrated estimates. I would strongly encourage the authors to tone down these claims and present PCE as a heuristic structured reasoning framework rather than as a principled uncertainty estimator in the formal sense.

4. **Some of the main empirical claims are stronger than what the tables actually show.**  
   On **Page 8**, the paper claims PCE outperforms baselines in “success rate, task efficiency, and token usage,” and the abstract similarly says “comparable token usage.” That characterization is too generous. In **Table 1**, PCE does have favorable or comparable usage on C-WAH for GPT-4o mini and GPT-OSS:20B, but not for Gemma3:4B, where REVECA is lower. In **Table 2**, PCE is substantially *higher* in usage than CoELA for all three backbones, sometimes by a very large margin, for example 197,807 vs 113,059 tokens for GPT-4o mini, and 184,809 vs 98,350 for Gemma3:4B. So the cleaner claim supported by the tables is: PCE improves task performance and drastically reduces communication frequency relative to several communication-centric baselines, but token usage is mixed and often notably higher than the lightest baseline. The current wording overstates cost-efficiency.

5. **The experimental scale is not fully convincing for some of the claims made in the introduction and conclusion.**  
   C-WAH uses only **10 episodes** and TDW-MAT uses **24 episodes** (**Section 5, Page 7**). That is not useless, but it is fairly small given the stochasticity one expects from LLM-based multi-agent planning. The paper reports averages but no standard deviations, confidence intervals, bootstrap intervals, or per-episode scatter. This makes it hard to tell whether the improvements are robust across tasks or driven by a few favorable episodes. This is especially important when comparing systems that may have high run-to-run variance due to LLM nondeterminism and prompt sensitivity. A stronger paper would report repeated runs or at least uncertainty estimates around the means.

6. **The ablations are helpful but still leave causal ambiguity.**  
   **Table 3** shows that removing any module hurts performance, but the ablations are not all equally interpretable. For example, “w/o Planner” produces an enormous token increase, whereas “w/o Composer” lowers communication to 0.26 and lowers token usage below full PCE, yet only modestly hurts steps. This suggests a more nuanced story than “each module is indispensable.” In fact, the Composer seems to buy some performance at the cost of extra inference, and the paper does not really unpack that trade-off. Similarly, **Figure 3** compares PCE against “Planner only,” but it does not isolate whether the gain comes primarily from explicit branching, from evaluator scoring, or simply from additional structured prompting. Since the paper is making a mechanism claim, the analysis should be more surgical.

7. **The user study is too small and too thinly specified to carry much evidentiary weight.**  
   The user study in **Section 5.3, Page 10** involves **12 participants**, all in one environment, and the protocol description is brief. It is unclear how much participants truly collaborated versus observed, how task order was randomized, whether there was any learning effect, and how many trials each participant completed per condition. **Figure 4** is visually clean, but the study is better viewed as anecdotal support than strong validation. The paper should not lean too heavily on trust/usefulness claims from this experiment.

8. **There are missing or weakly addressed comparisons to adjacent uncertainty-aware planning literature.**  
   The related work is reasonably broad for embodied multi-agent communication baselines, but the paper is thinner on prior work that also tries to make uncertainty explicit in planning or in LLM-assisted embodied control. As one example, work on asking before acting / information gathering in embodied decision making seems directly relevant to the paper’s communication-vs-action framing and would help sharpen what is actually distinctive here. Likewise, modular LLM-plus-planner formulations for planning under uncertainty are important context when the paper claims a shift in planning paradigm. The current positioning is good against communication-heavy embodied-agent baselines, but less sharp against the broader uncertainty-aware planning landscape.

9. **Some notation and action modeling choices are awkward or potentially misleading.**  
   In **Section 4.4**, the cost definition assumes
   \[
   \mathbf{1}\{\mathrm{move}(a)\}+\mathbf{1}\{\mathrm{comm}(a)\}=1.
   \]
   This encodes a mutually exclusive move-vs-communication dichotomy, but the actual environments contain more than pure move actions, such as checking, grasping, open/close, put-in, and drop actions. It is unclear how these are mapped into the cost model. Are all non-communication actions assigned a movement cost via associated travel distance? What about low-distance manipulation after arrival? Since many action choices in the benchmarks are not simply “move to room” versus “send message,” the current notation compresses too much and leaves the real cost accounting ambiguous.

10. **Presentation is decent overall, but some important content lives in prompts and appendix-style detail rather than in the main methodological description.**  
   A lot of the actual method is prompt engineering, including the output formats, branch semantics, and evaluator scoring rubric, which only becomes fully visible in **Figures 8-10** and the prompt pages. This is informative, but it also exposes that the main text abstracts away several implementation choices that materially affect behavior. In a paper centered on converting reasoning traces into explicit scenario trees, those choices should be summarized more concretely in the method section itself.

## Questions
1. Please clarify the exact evaluator used in the experiments. Did you compute
   \[
   U(\mathcal{S}, a)=\mathcal{L}(\mathcal{S})\mathcal{G}(a)-\lambda C(a)
   \]
   with $\mathcal{L},\mathcal{G},C \in [0,1]$, or were Likelihood/Gain/CostPenalty taken directly from 1-5 LLM scores as in **Figure 10**? If there is a mapping, please provide it explicitly.

2. Can you provide a more algorithmic specification of the Composer in **Section 4.3**? In particular: how is the “local ranking policy” instantiated, how is branch consistency checked, how do you avoid semantically duplicate assumptions, and what exact condition triggers early stopping before reaching depth $D$?

3. Were the benchmark results averaged over one run per episode or multiple runs with different random seeds / decoding randomness? Reporting variance or confidence intervals for **Tables 1-3** would substantially increase confidence in the claims.

4. The paper states that PCE achieves “comparable token usage,” but **Table 2** shows PCE using substantially more tokens than CoELA across all backbones. Can the authors revise this claim, or explain why they still consider the usage comparable in practice?

5. For the user study, please clarify the exact protocol: number of trials per participant per condition, randomization or counterbalancing, whether participants directly controlled a partner or only observed and responded, and whether the same tasks were used across methods.

6. A useful rebuttal would include at least one concrete failure analysis. Under what kinds of planner hallucinations or composer mistakes does PCE still fail, and does the evaluator reliably suppress them?

7. Since **Table 3** suggests “w/o Composer” remains fairly competitive on steps while using fewer tokens, can the authors better quantify when Composer is worth its added overhead? A per-environment or per-task breakdown would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is evaluated in simulated household environments and does not appear to involve sensitive private data or high-risk deployment claims in the main submission.

## Soundness Rating
3: good. The overall empirical story is reasonably convincing and the method is coherent, but the evaluator formulation and parts of the algorithm are underspecified enough that I cannot call the paper technically airtight.

## Presentation Rating
3: good. The paper is readable and the high-level story is clear, with helpful figures, but several critical implementation and mathematical details are either inconsistent or left too implicit.

## Contribution Rating
3: good. The paper makes a useful contribution by reframing uncertainty handling in LLM-based embodied cooperation around structured assumptions rather than pure communication, although the conceptual and methodological novelty is more moderate than the paper sometimes suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The idea is relevant, the results are consistently strong enough to matter, and the paper is likely useful to the embodied-agent community. That said, the paper needs to clean up the evaluator formulation, moderate a few overclaims, and better specify the tree-construction procedure.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the area, though some implementation details are not fully checkable from the main paper alone.