Now I have all the information I need to write the final consolidated review. Let me organize my findings and write it.

Key verified findings:

1. **MCTS reward does not encode answer correctness**: This is TRUE and directly verifiable from §3.3 (lines 98-110). The reward is binary: +α for "Non-failure" (=the planner produces any result without a crash), −α for "Failure" (=execution error). The paper itself acknowledges: "it is not sure whether the result is correct as ground truth." However, the harsh critic's claim that this "invalidates the core planning advantage claim" is somewhat overstated — the MCTS still provides the benefit of (a) steering away from paths that crash, (b) exploring multiple solutions that can be voted/summarized. The reward helps avoid repeated failures, even if it can't distinguish correct from incorrect answers. So this is a legitimate MAJOR concern about the gap between the claim ("backpropagating the result's reward" guiding toward better solutions) and reality, but it does not completely invalidate the planner since multi-solution exploration + voting is still meaningful.

2. **Ablation sample sizes are very small**: TRUE. The paper explicitly states (line 122): "For ablation studies, we randomly sample 10 samples per question type from train, resulting in a total of 30 questions (s train)." The diagnostic experiments use 90 videos (line 161). Table 3a shows N=1→4 improvement from 43.3→65.7 on just 30 samples. This IS a major concern.

3. **Unfair baseline comparison with ViperGPT**: PARTIALLY TRUE but needs nuance. The paper filters ViperGPT's failed executions (60/900) and reports only on successful ones (840/900). The paper DISCLOSES this (line 102, 142). However, the paper doesn't explicitly report whether DoraemonGPT has comparable execution failures. Since DoraemonGPT uses a different architecture (not code generation), the failure modes are different. But the comparison is still asymmetric. The harsh critic's point that "if DoraemonGPT's failures are included in its score while ViperGPT's failures are excluded, the comparison is unjust" is valid — however, filtering OUT ViperGPT's failures actually FAVORS ViperGPT (improves its score from 38.1 to 40.8), so this asymmetry actually works against the author's method. Per the hard rules: "REMOVE criticisms that are factually wrong or misunderstand the paper" and "REMOVE 'weaknesses' about unfair comparison with other methods if the asymmetry favors the baseline and not the author's method." Since filtering ViperGPT's failures IMPROVES ViperGPT's score, the asymmetry favors the baseline. This should be REMOVED.

4. **Motivating example gap**: The abstract talks about "guiding students through multi-step laboratory experiments" but evaluation is on NExT-QA. The paper does have an in-the-wild example (Fig 3) that addresses this lab experiment case, so this is partially addressed. This is a minor concern.

5. **N=2 barely qualifies as MCTS exploration**: TRUE and significant. The paper uses N=2 for main experiments (line 130), meaning at most 2 solutions are explored. The ablation showing N=1→N=4 uses only 30 samples. This is a real tension.

6. **No UCB-style exploration constant**: TRUE but minor — this is a design choice, and the Softmax approach is a valid alternative.

7. **Strength Finder's claim about "13.2% in average accuracy"**: Let me check — the paper says "outperforms ViperGPT by 19.3/5.6/15.2/13.2 (Acc_C/Acc_T/Acc_D/Avg)", so 13.2% Avg improvement. But this uses the filtered ViperGPT scores. Still, the improvement is substantial.

8. **Strength Finder's "67.8% vs 49.9%" for Table 3c**: This can't be verified from text (it's in an image table), but the paper does claim MCTS outperforms DFS and other baselines. The sample size concern still applies.

Now let me write the review.</think>## Summary

DoraemonGPT is an LLM-driven agent for dynamic video tasks that constructs a task-related symbolic memory by decoupling spatial-temporal video attributes into space-dominant and time-dominant structures, queries these memories via specialized sub-task tools, and uses a Monte Carlo Tree Search (MCTS) planner to explore the large planning space and produce multiple solutions that are summarized or voted into a final answer. The system is evaluated on the NExT-QA benchmark, where it outperforms prior LLM-driven agents (ViperGPT, VideoChat) and achieves competitive results against supervised models.

## Strengths

- **Spatial-temporal decoupling of video memory is a clean and conceptually motivated design.** The division into space-dominant memory (instance-centric: tracking, actions, trajectories) and time-dominant memory (frame-level captions, ASR, OCR) maps well to the structure of video understanding tasks. Ablation in Table 4 confirms the two memories are complementary: combining them yields the best performance (65.7%), while either alone drops substantially (SDM: 42.2%, TDM: 46.7%).
- **The overall system design is comprehensive and fully implemented.** The pipeline from video input through symbolic memory construction, tool-based querying, and MCTS planning is completely specified, integrating multiple foundation models (YOLOv8, Deep OC-Sort, BLIP, Whisper, etc.) into a coherent architecture with plug-and-play knowledge tools.
- **Meaningful improvements over LLM-driven baselines on the main evaluation set (900 questions).** DoraemonGPT outperforms ViperGPT by 13.2% Avg and VideoChat by 3.0% Avg on NExT-QA s_val, demonstrating practical effectiveness of the overall system design—particularly the strong causal reasoning performance (52.3% vs. MIST's 51.7%, the previous supervised SOTA).
- **The multi-solution exploration paradigm provides genuine practical benefit.** Even with the simplified reward signal, generating N=2 solutions and voting/summarizing them is a useful mechanism that helps recover from single-path failures (as shown in the in-the-wild example, Fig. 3, where failed SQL queries are bypassed via tree branching).

## Weaknesses

### Fatal
None.

### Major

- **The MCTS reward signal does not encode answer correctness, creating a gap between the claimed planning advantage and what the reward actually provides.** The paper's abstract and §3.3 claim the planner "iteratively finds feasible solutions by backpropagating the result's reward," but the reward is strictly binary: +α for any non-crashing result and −α for execution failures (lines 100–106). The paper itself explicitly acknowledges this ("it is not sure whether the result is correct as ground truth," line 106). This means the MCTS backpropagation steers the search toward paths that *don't crash*, not toward *correct answers*. A confidently wrong answer receives the same positive reward as a correct one, so the softmax node selection $P(v_i) = \text{Softmax}(R_i)$ cannot preferentially guide exploration toward better solutions. The core contribution claim about MCTS "guiding" search is overstated: the main benefit comes from (a) avoiding repeated failures and (b) multi-solution voting/summarization—both of which could be achieved with simpler strategies (e.g., generate N solutions independently and vote). This does not invalidate the system entirely—the multi-solution mechanism itself is useful—but it fundamentally undermines the claimed novelty of the MCTS *backpropagation-guided* search.

- **Ablation sample sizes are far too small to support claims about MCTS superiority over baselines.** Table 3a/b ablations are conducted on only **30 samples** (10 per question type from the training set), and the diagnostic experiments (Table 3c) use **90 samples** (line 122, 161). The claimed improvement from N=1 to N=4 (43.3%→65.7%, Table 3a) and MCTS over DFS (Table 3c) are on these tiny subsets with no confidence intervals or statistical tests. At 30 or 90 multiple-choice questions, differences of a few percentage points are well within random variation. The main experiments use N=2 (line 130), meaning the system barely explores beyond a single solution, yet the core evidence for why MCTS itself (vs. simple multi-sampling) helps comes from these underpowered ablations.

### Minor

- **Tension between N=2 in main experiments and the claimed importance of MCTS exploration.** The paper uses N=2 for its main evaluation due to "accuracy-cost trade-offs" (line 130), meaning at most 2 solutions are explored. With N=2, the MCTS selection/backpropagation mechanism has minimal opportunity to meaningfully redirect search. The paper does not compare N=2 MCTS against a trivial "generate 2 independent solutions and vote" baseline that would isolate whether the tree structure itself adds value or whether the improvement is simply from sampling multiple solutions.
- **The paper does not report DoraemonGPT's own failure rate.** While the paper transparently discloses filtering ViperGPT's failed executions (60/900), it does not report whether DoraemonGPT has any execution failures on the same 900-question evaluation set. Reporting this would clarify the effective coverage of each system.

### Trivial
None.

## Nice-to-Haves

- An oracle-reward experiment (using ground-truth during search) would establish an upper bound showing whether the MCTS mechanism could benefit from a better reward signal, and how much performance is leaving on the table due to the binary reward.
- Comparing MCTS with N solutions against a "sample N independent solutions and vote" baseline would cleanly isolate the value of the tree structure vs. the value of multi-solution aggregation.
- Confidence intervals or bootstrap results on the 900-question main evaluation set would strengthen the empirical claims.

## Removed Points

These points are flagged to be removed, treat them with cautious:

- **Unfair baseline comparison with ViperGPT (Harsh Critic Issue #3):** The critic claims the comparison is unfair because ViperGPT's failed executions are filtered out. However, filtering ViperGPT's failures *improves* ViperGPT's scores (from 38.1 to 40.8 Avg), meaning this asymmetry *favors the baseline*, not the author's method. Per the hard rules, criticisms about unfair comparisons where the asymmetry favors the baseline are removed. The paper also transparently discloses this filtering.
- **Motivating example gap (Harsh Critic §Abstract/Introduction):** The critic notes the gap between the "guiding students through multi-step laboratory experiments" framing and NExT-QA evaluation. The paper does address this with a dedicated in-the-wild example (Fig. 3, §4.3) showing exactly this lab-experiment scenario. The gap is therefore partially addressed and at most minor.
- **"Sub-task tools are just prompt engineering" (Harsh Critic §3.1):** This is a dismissive characterization. Designing specialized sub-agents with tailored prompts and SQL-based querying for different reasoning types (When/Why/What/How/Count/Other) is a valid modular architectural contribution regardless of implementation mechanism.
- **No UCB exploration constant (Harsh Critic §3.3):** The use of Softmax over rewards rather than UCB is a reasonable design choice. Standard MCTS variants use different selection policies, and the paper's approach is coherent. This is at most a minor point about an alternative design, not a weakness.
- **Strength Finder: "Adaptive reward backpropagation mechanism" as a strength:** This is removed because the reward signal's weakness (it doesn't encode correctness) directly undermines the claimed strength of the backpropagation mechanism. One cannot claim "adaptive reward backpropagation" is a strength when the reward being backpropagated carries limited information.
- **Strength Finder: "Superior exploration capability of the MCTS planner" (with specific numbers from Table 3a/c):** This strength is significantly weakened by the tiny sample sizes (30 and 90 samples). The numbers cited (43.3%→65.7%, 67.8% vs. 49.9%) are from underpowered ablations; they are not reliable enough to serve as strong evidence for this claim. Downgraded to supporting but caveat-laden evidence.
- **"MIST comparison conflates paradigm differences" (Harsh Critic §4.2):** Comparing LLM-driven agents against supervised SOTAs is standard practice and informative for readers. The comparison is clearly labeled with model types in Table 2.

## Novel Insights

The review reveals an important structural insight: the MCTS planner in DoraemonGPT functions effectively as a *failure-avoidance and multi-solution aggregation* mechanism rather than a *correctness-guided search* mechanism. The gap between these two capabilities is the paper's central tension. The system's actual performance gains likely derive from (1) the well-designed symbolic memory architecture and (2) the practical benefit of generating multiple independent solutions and aggregating them, both of which are genuine contributions—but neither requires the MCTS backpropagation machinery. A simpler "sample N solutions independently, then vote" strategy might achieve comparable gains, and the paper does not rule this out. This distinction matters for the paper's novelty claim.

## Suggestions

- Run a simple "N-independent-samples + voting" baseline on the 900-question s_val set and compare against N=2 MCTS. If the gap is small, the contribution should be reframed around the memory architecture and multi-solution aggregation rather than MCTS-guided search.
- Report DoraemonGPT's execution failure rate on s_val alongside ViperGPT's for complete transparency.
- Even a proxy reward based on LLM self-assessed confidence (e.g., prompting the LLM to rate its certainty) would be more informative than the current binary signal and would make the MCTS backpropagation mechanism meaningfully functional.

## Score and Decision

The paper makes genuine contributions in its symbolic memory architecture (spatial-temporal decoupling) and demonstrates practical improvements over baseline LLM-driven agents on a standard benchmark. However, the central novelty claim—MCTS-guided search via reward backpropagation—is significantly undermined because the reward does not encode answer correctness, and the empirical evidence for MCTS superiority over simpler alternatives relies on underpowered ablations (30–90 samples). The system works, but the claimed mechanism for *why* it works is not convincingly demonstrated. The paper would be substantially stronger with either a correctness-aware reward or a clean comparison against simpler multi-sampling baselines at proper scale.

**Originality:** Moderate—the symbolic memory design is clean but the MCTS contribution is partially overstated.  
**Importance of research question:** Good—extending LLM agents to dynamic video understanding is important.  
**Claims well supported:** Partially—main results on 900 questions are reasonable, but ablations and MCTS claims are weakly supported.  
**Soundness of experiments:** Limited by small ablation sample sizes and lack of critical baselines.  
**Clarity:** Good—system design is clearly described.  
**Value to community:** Moderate—useful system design but the MCTS contribution needs substantiation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>