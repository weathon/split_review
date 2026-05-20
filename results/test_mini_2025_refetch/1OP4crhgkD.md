Now I have strong calibration. Let me write the final consolidated review.

**Round 1 bracket:** 4.0 – 6.5  
**Round 2 narrowing:** Comparing against YOLO-MARL (4.0, rejected), DPM (5.4, rejected), MAZero (6.5, accepted poster), and Text2Reward (7.0, accepted spotlight).

SAMA is noticeably stronger than YOLO-MARL (better writing, more domains, more structurally novel) and comparable to DPM but with weaker evaluation (no ablations — DPM has them). It is below MAZero which had a fairer comparison setup and cleaner evaluation.

---

## Summary

This paper introduces SAMA, a framework that uses pretrained language models (GPT-3.5/4) with chain-of-thought prompting to generate semantically aligned goals, decompose them into subgoals, and assign them to agents in cooperative MARL. A language-grounded MARL policy learns subgoal-conditioned behaviors from offline datasets, and a self-reflection mechanism replans when subgoal execution fails. Experiments on Overcooked (5 layouts) and MiniRTS show that SAMA achieves comparable or better performance than automatic-subgoal-generation (ASG) baselines while using substantially fewer environment interaction steps.

## Strengths

1. **Novel framework architecture for PLM-guided MARL.** SAMA proposes a three-tier pipeline — goal generation, goal decomposition into subgoals, and subgoal-to-agent assignment — all driven by PLM prompting with chain-of-thought. This is a structurally coherent and underexplored approach to injecting commonsense priors into cooperative MARL, going beyond existing work that either hand-crafts rules or learns subgoal representations entirely from scratch (Section 3.2).

2. **Strong empirical results on two distinct, challenging domains.** On Overcooked (Figure 5), SAMA reaches near-SOTA performance using ~5–10% of the environment timesteps required by ASG baselines (MASER, LDSA, ROMA, FCP, COLE) across all five layouts. On MiniRTS (Figure 6), SAMA, initialized from RED's pretrained policy, approaches RED's oracle-command win rate while ASG baseline ROMA (trained from scratch) remains far behind. The two-domain demonstration goes beyond many single-domain LLM+RL papers.

3. **Self-reflection mechanism for online correction without human supervision.** SAMA's reset-recovery procedure (Section 3.4) detects subgoal failures via PLM-generated code evaluators and triggers replanning (regeneration, re-decomposition, or re-assignment). This closes the loop between PLM planning and RL execution, addressing a known weakness of open-loop PLM planners.

4. **Automated preprocessing pipeline.** The task manual generation from LaTeX source (Section 3.1) and state/action translation via LangChain reduce the manual engineering burden of applying SAMA to new environments, supporting the claim of transferability.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablations prevent attribution of performance gains.** The framework has four interacting components: PLM-based goal generation, PLM-based decomposition/assignment, language-grounded MARL, and self-reflection. There are **zero ablation experiments** in the paper (confirmed by grep for "ablation" / "ablate" — no matches). Without isolating these components, it is impossible to know whether the gains come from the PLM's commonsense priors, the specific prompting strategy, the self-reflection mechanism, the language-grounded architecture, or simply having a pre-defined subgoal set. This is the single most significant evaluation gap.

2. **Comparison fairness and sample efficiency framing.** The ASG baselines (MASER, LDSA, ROMA, FCP, COLE) learn subgoal representations from scratch via end-to-end RL, while SAMA injects external commonsense knowledge via GPT-3.5/4. The headline claim of requiring "merely approximately 10% of the training instances" counts only environment interaction timesteps and **excludes** the cost of: PLM queries for task manual generation, offline dataset generation (states, subgoals, code snippets for reward functions), and self-reflection trials. The paper acknowledges PLM costs in Section 3.3 but does not quantify them or include them in the efficiency comparison. The practical total cost (PLM API calls + wall-clock time + environment steps) is unreported.

3. **Oracle prompt design in MiniRTS undermines generality.** Section 4.2 states: "we establish an oracle prompt design strategy following the ground truth of enemy units and the attack graph." This means SAMA receives privileged information about the opponent's composition — information analogous to what the RED oracle baseline explicitly uses. The MiniRTS results therefore show that SAMA + oracle information ≈ RED (oracle commands), which does not demonstrate that SAMA can discover sensible strategies autonomously in zero-shot or few-shot settings. The oracle dependency should be scoped out or the prompt strategy should be ablation-controlled.

4. **Core motivational claim ("over-representation" of subgoals) is asserted but never empirically validated.** The paper's introduction states that ASG methods "may result in the 'over-representation' of subgoals, generating numerous spurious subgoals of limited relevance to the actual task reward" (Section 1). This premise motivates the entire PLM-based approach, yet the paper provides **zero quantitative analysis** of subgoal diversity, relevance, or redundancy from any baseline method. A simple comparison of the number of distinct subgoals generated by SAMA vs. MASER/LDSA/ROMA over a fixed number of environment steps would address this.

### Minor

5. **PLM-generated reward function accuracy is not evaluated.** The binary reward functions that drive language-grounded MARL training are Python code snippets generated by the PLM (Section 3.3). If these are incorrect, the policy receives corrupted training signals. The paper reports no accuracy, ablation, or failure-mode analysis of this critical component.

6. **Self-reflection is not ablated or analyzed.** The hyperparameter of 3 maximum reflections (Section 3.4) is stated but not justified empirically. How often is self-reflection triggered? What fraction of failures does it recover from? Are 3 iterations sufficient? Without this analysis, the self-reflection mechanism's contribution is opaque.

7. **Prompt sensitivity is acknowledged but untested.** The paper notes that "the efficacy of PLM remains contingent upon prompt selection" (Section 5) and Appendix F contains all prompts, but no sensitivity analysis across prompt variants is provided. For a method whose core operation is prompt-based, this is a notable gap.

8. **The "disentangled decision-making" framing is rhetorical overreach.** The paper draws inspiration from disentangled representation learning (Bengio et al., 2013) but does not perform representation learning, factor isolation, or any of the formal properties associated with disentanglement. The connection is metaphorical, which risks confusing readers about what the paper actually contributes.

### Trivial
- Figure 5 caption says "Pretrain learning curves" which is ambiguous — it is unclear whether these are training curves, evaluation curves, or learning curves of the language-grounded policy specifically (Section 4.1 clarifies they are evaluation-based curves, but the caption is unclear).

## Nice-to-Haves
- An ablation replacing the PLM planner with a rule-based or random subgoal generator would isolate whether PLM commonsense or simply having pre-defined subgoals drives performance.
- A PLM-cost table (environment steps + API calls + wall-clock time for each method) would let readers evaluate the practical trade-off the paper claims.
- Testing on a third domain without a LaTeX paper (e.g., an environment where the task manual must come from a different source) would strengthen the generality claim.
- A prompt-sensitivity study across 3–5 prompt variants per domain would improve confidence in the robustness of the approach.

## Removed Points
- **"The Markov assumption on task planning is problematic"** (Harsh Critic): The paper explicitly states the Markov assumption on planning scope in Section 2 ("we presume that task planning adheres to Markov properties"). This is a deliberate modeling choice, not an oversight. The PLM implicitly tracks state via its context window, which is how this class of approaches handles cross-round dependencies.
- **"Missing comparison with LLM-based planning methods like Voyager, DEPS, SayCan"** (Harsh Critic): These are single-agent methods for environments very different from Overcooked/MiniRTS. There are no established LLM-based MARL planners to compare against; demanding such comparisons is outside the paper's scope.
- **"The task manual generation from LaTeX is fragile"** (Harsh Critic): The paper explicitly notes this approach is one design choice; claiming fragility without evidence is speculative.
- **Strength about "generalizability beyond two domains"** (Strength Finder): Testing on two domains is good but not exceptional for a single paper. "Generalizability" is overstated.
- **Strength about "automated task manual generation" as a core strength** (Strength Finder): This is a useful engineering contribution but not a core conceptual strength; moved here.
- **"Not all environments have LaTeX papers"** (Harsh Critic): True by stated scope. The paper does not claim universal applicability.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface any unexpected synthesis that the paper itself does not already articulate.

## Suggestions

1. **Conduct ablations as the top priority for revision.** At minimum: (a) replace the PLM planner with a random/goal-prioritized rule-based generator, (b) disable self-reflection, (c) replace GPT-4 with a smaller open-source PLM, and (d) replace the language-grounded MARL policy with a standard MARL algorithm conditioned on the same subgoal set. These experiments will isolate which components drive the sample efficiency gains.

2. **Quantify the over-representation claim** by computing subgoal diversity metrics (e.g., number of distinct subgoals, entropy of subgoal distribution over states) for SAMA vs. the leading ASG baselines over a fixed number of environment steps.

3. **Report total cost transparently.** Add a supplementary table showing environment timesteps, number of PLM API calls per stage (manual generation, dataset generation, evaluation, self-reflection), training wall-clock time, and estimated API cost for each method.

4. **Scope the MiniRTS oracle prompt.** Run an ablation that uses a blind prompt strategy (no enemy unit ground truth) to measure how much performance depends on oracle information, or clearly reposition MiniRTS results as a proof-of-concept for SAMA's ability to follow oracle-quality guidance.

## Score and Decision

### Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| YOLO-MARL | SOXxa4pPGY.md | 4.00 (reject) | R2 | Less novel framework, weaker writing, fewer domains than SAMA. SAMA is clearly stronger. |
| Learning Transferable Sub-goals | OvrmA3GMiX.md | 3.75 (reject) | R1 | Hand-picked goals, incomplete method. SAMA is substantially stronger in framework and evaluation. |
| DPM | VzuPnoSKQ1.md | 5.40 (reject) | R2 | Similar "unfair comparison" concern, but DPM has ablations (which SAMA lacks). SAMA's two-domain eval is broader. Comparable quality, SAMA slightly weaker. |
| Generate explorative goals (LanGoal) | hCfhfwSfCg.md | 2.00 (withdrawn) | R1 | Plagiarism-concern paper with poor writing. SAMA is much stronger. |
| MAZero | CpnKq3UJwp.md | 6.50 (accept) | R2 | Fairer comparison setup (model-based vs model-free, same info), accepted despite single-domain limitation. SAMA has weaker eval rigor. |
| Text2Reward | tUM39YTRxH.md | 7.00 (accept) | R2 | Far more comprehensive evaluation (17+ tasks, ablations, real-world). SAMA has more novel framework but much less rigorous eval. |
| Eureka | IEduRUO55F.md | 6.25 (accept) | R2 | Strong evaluation over 29 environments. SAMA is less thorough. |
| MaestroMotif | or8mMhmyRV.md | 7.75 (accept) | R1 | Most similar in spirit, but with extensive ablations and analysis. SAMA is notably weaker in evaluation depth. |
| Subgoal generation efficiency | nyuaoVnVCa.md | 2.33 (withdrawn) | R1 | Unrelated topic. |

**Round 1 bracket:** 4.0–6.5.  
**Round 2 narrowing:** SAMA sits between the 4.0 rejected papers and the 6.5 accepted papers. Its closest analog is DPM (5.4, rejected) — both have an "unfair comparison" structural issue, but SAMA additionally lacks the ablation studies that DPM's reviewers specifically praised. The paper's core idea is solid and the results are promising, but the evaluation gaps (no ablations, oracle prompt in MiniRTS, selective sample efficiency metric) mean the evidence does not yet support the claims with sufficient rigor.

**Final score:** 5.0 — marginally below the acceptance threshold. The paper has a genuine contribution and a coherently designed framework, but the evaluation as presented has significant gaps that prevent validation of the headline claims. With major revisions including ablations, cost transparency, and fairer comparisons, this could become a solid contribution.

**Decision:** Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>