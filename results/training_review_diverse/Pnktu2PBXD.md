Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes DDR (Differentiable Data Rewards), a method that applies Direct Preference Optimization (DPO) with rollout-based rewards to jointly optimize a knowledge refinement module and a generation module in a two-agent RAG pipeline. The core idea is to use system-level rewards from rollouts to construct preference pairs for DPO training, thereby aligning data preferences across RAG modules. Experiments on knowledge-intensive tasks (NQ, TriviaQA, HotpotQA, WoW, T-REx, MARCO QA) with MiniCPM-2.4B and Llama3-8B show consistent improvements over Vanilla RAG and the SFT-based baseline RA-DIT, with evidence of better handling of knowledge conflicts and noisy documents.

## Strengths

- **Novel application of DPO to multi-agent RAG optimization.** The paper is the first to apply DPO with rollout-based rewards to jointly optimize a knowledge refinement module and a generation module in a RAG pipeline, moving beyond SFT approaches like RA-DIT. The method is clearly motivated and the DPO formulation (Eq. 2–3) is sound.

- **Consistent and substantial empirical gains.** DDR outperforms both Vanilla RAG and RA-DIT across all six evaluated knowledge-intensive tasks. The improvement on MiniCPM-2.4B is approximately 5% over RA-DIT, and the trend holds for Llama3-8B (Table 1). The gains are consistent across both backbone LLMs.

- **Demonstrated ability to mitigate knowledge conflict.** In the "Internal Knowledge" scenario (Table 4, where parametric knowledge is correct but RAG misleads), DDR reduces the performance drop by over 10 percentage points compared to Vanilla RAG, while RA-DIT shows no such improvement. This directly supports the paper's claim that DDR helps balance internal and external knowledge.

- **Robustness to noisy retrieved documents.** Figure 3 shows that DDR maintains consistent improvement over Vanilla RAG as the number of noisy retrieved documents increases, whereas RA-DIT exhibits inconsistent and sometimes degraded performance. This is a practically meaningful advantage.

- **Ablation studies isolate the primary source of gains.** Table 2 shows that optimizing only the generation module (RAG-DDR (Only V_Gen)) accounts for most of the improvement, while optimizing only the knowledge refinement module yields limited benefit. This clarifies where DDR's effectiveness comes from.

## Weaknesses

### Fatal
None.

### Major

- **The RA-DIT baseline is reproduced without retriever finetuning, weakening the comparison.** The paper explicitly states (Section 4, Baselines) that it "do[es] not finetune the retriever during our reproduction process" of RA-DIT, justifying this by saying the retriever (bge-large) is "sufficiently strong." However, the original RA-DIT paper finetunes both retriever and generator; retriever finetuning is part of what defines RA-DIT. By omitting it, the paper compares DDR against a weaker version of the baseline. The claim that "RA-DIT still underperforms compared to Vanilla RAG on certain knowledge-intensive tasks" (which is itself atypical) may be partly an artifact of this reproduction choice. While the frozen-retriever setting is a legitimate experimental design choice for isolating the effect of different training methods (SFT vs. DPO), the paper should either (a) run RA-DIT with retriever finetuning to establish the full baseline, or (b) explicitly rename the comparison to "RA-DIT (generator-only)" and discuss how retriever finetuning might affect results. As it stands, the central empirical claim ("DDR significantly outperforms SFT methods") rests on a comparison against a potentially weakened baseline.

### Minor

- **Knowledge refinement module training procedure is underspecified.** Section 3.2 describes constructing DPO preference pairs for $V_{KR}$ by identifying the document $d_i$ that "leads the agent system to achieve the highest evaluation reward" when included, and $d_j$ with the lowest reward. However, the paper does not explain how the effect of a *single* document is isolated when the generation module sees the *full set* of retained documents. If all other document decisions are held fixed while evaluating each document individually, the preference signal depends on the current configuration, making it potentially noisy. The paper provides no analysis of whether these preference pairs are stable or meaningful. This does not necessarily invalidate the approach—the ablation shows that $V_{KR}$ optimization contributes limited improvement anyway—but it leaves a central component of the method's training procedure unclear and non-reproducible.

- **Rollout sampling strategy for preference pair construction is not specified.** For the generation module (Section 3.2), the paper says responses are "sampled" with and without retrieved documents, and the highest/lowest reward responses become positive/negative pairs. The number of samples per query, the selection mechanism (top-1 vs. bottom-1 vs. margin-based), and the number of pairs per training example are not reported. This is essential for reproducibility.

- **Training/evaluation dataset overlap is not clarified.** The paper uses 32,805 training samples from "ten datasets covering two tasks" but does not name these datasets. The evaluation uses NQ, TriviaQA, HotpotQA, WoW, T-REx, and MARCO QA. If any of these evaluation datasets overlap with the training data, the reported results would reflect in-distribution performance rather than generalization. The paper should state explicitly whether the evaluation datasets are held out from training.

- **No measures of variance reported.** Results tables lack standard deviations, confidence intervals, or any measure of statistical significance. This makes it impossible to assess whether the reported improvements (especially on smaller subsets like the Internal Knowledge scenario) are reliable or within the noise. This is particularly important given that single-epoch training with LoRA can exhibit variability across runs.

- **Using the evaluation metric as the reward signal without overfitting analysis.** The reward $S(y_T)$ for DPO is computed using the same automatic metrics (Rouge-L, Accuracy) used for final evaluation. While this is common practice in RL from automated feedback, the paper claims DDR "avoids overfitting to training signals" compared to SFT without providing direct evidence. Some indirect evidence exists (response length preservation in Figure 1c, generalization to noisy documents), but a more direct analysis (e.g., does reward correlate with held-out performance? Do preference pairs remain stable across training steps?) would substantially strengthen this claim.

## Nice-to-Haves

- Compare against a REINFORCE-based or other RL-based RAG optimization method to more directly demonstrate the advantage of DPO's implicit reward modeling over explicit reward-based RL.
- Include a leave-one-out or Shapley-value analysis to validate the document-level preference construction for the knowledge refinement module.
- Report results with multiple random seeds to assess variance.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the reasons stated:

1. **"Differentiable" in the name is overblown.** (from harsh critic) — The method uses DPO, which provides a differentiable training objective from rewards. While the term could be more precise, this is a naming preference, not a substantive flaw. Removed as trivial naming nitpick.

2. **Knowledge refinement training is "likely flawed."** (from harsh critic) — Downgraded from "likely flawed" to "underspecified." The paper's approach (evaluating each document's inclusion reward) is a reasonable approximation; the issue is lack of clarity about how individual-document effects are isolated, not a fundamental methodological error.

3. **"No comparison against other RL-based RAG optimization methods (REINFORCE, STEP-DPO)"** — STEP-DPO and Agent Q are not RAG-specific methods; they address multi-step reasoning in different settings. REINFORCE-based RAG optimization is not an established baseline. Demanding comparison against methods not designed for the same setting is scope creep. Moved to Nice-to-Haves.

4. **"Three scenarios described post-hoc"** — The scenarios (Has-Answer, Miss-Answer, Internal Knowledge) are clearly defined in Section 4.3 with descriptions of how they categorize evaluation data. This is a reasonable analysis, not a weakness.

## Novel Insights

Beyond the paper's own contributions, an interesting observation emerging from the reviews is the asymmetry between SFT and DPO for RAG: SFT (RA-DIT) compresses response distributions towards canonical answers (shorter, more rigid), while DPO (DDR) preserves the base model's output length distribution while improving accuracy. This suggests that DPO's preference-based learning may better preserve the model's pre-existing knowledge structures while adding task-specific alignment, whereas SFT's maximum-likelihood objective overwrites them. The paper's finding that most gains come from the generation module alone (not the knowledge refinement module) further suggests that for strong retrievers, the bottleneck in RAG is not document selection but the generator's ability to selectively attend to useful information while resisting noise—a finding that aligns with recent work on RAG faithfulness.

## Suggestions

1. **Fix the RA-DIT baseline.** Either run RA-DIT with retriever finetuning as in the original paper, or clearly rename the comparison and add a discussion of what retriever finetuning might contribute. Without this, the paper's headline empirical claim is compromised.

2. **Specify the rollout sampling details.** Report the number of samples per query for both the generation and knowledge refinement modules, how preference pairs are selected from these samples, and how many pairs are used per training example.

3. **Clarify training/evaluation data separation.** List the 10 training datasets and explicitly state whether any of the six evaluation datasets overlap.

4. **Add variance estimates.** Report results from at least 2–3 seeds with standard deviations, especially for the scenario-based analysis where sample sizes may be small.

5. **Address the reward overfitting concern** by showing that DPO training reward correlates with held-out validation performance, or that preference pair rankings remain stable across training steps.

## Score and Decision

This paper makes a genuine contribution: applying DPO with rollout-based rewards to RAG optimization is a reasonable and well-motivated idea, the experiments are broad (2 backbones, 6 tasks), and the analyses provide useful insights (knowledge conflict mitigation, noise robustness, ablation isolating the generation module as the primary source of gains). The weaknesses are real but mostly addressable: the RA-DIT baseline concern is the most significant, but the paper's core comparison (DPO vs. SFT with the same frozen retriever) remains interpretable even if the "RA-DIT" label is imprecise. The underspecification issues (knowledge refinement training, rollout details, data overlap) are clarity problems that can be fixed.

On originality: the method is novel in applying DPO to multi-agent RAG. On importance: the problem of RAG optimization is timely and relevant. On soundness: the experiments are reasonable but the RA-DIT baseline issue and missing variance estimates temper confidence. On clarity: the method description is clear at a high level but lacks important details for reproducibility.

The paper is a borderline-to-weak accept: the contribution is real, the experiments support the main claims directionally, but the RA-DIT baseline issue and several underspecification gaps require attention.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>