Now I have all the information I need to produce the consolidated review.

---

## Summary

This paper proposes RLFH (Reinforcement Learning for Hallucination), an online PPO-based method that mitigates LLM hallucination by converting statement-level fact verification into token-level dense rewards. The key innovation is a pipeline that: (1) generates responses from the policy model, (2) uses Mixtral-8x7B to decompose responses into atomic facts and evaluate each for truthfulness (5-class label) and informativeness (5-point scale), (3) traces these judgments back to individual tokens via LCS-based alignment to produce dense token-level rewards, and (4) optimizes the policy via PPO. Experiments on HotpotQA, SQuADv2, and Biography show FactScore improvements over the base model (+17.9%) and over the best learning-based baseline FACT (+2.0%).

## Strengths

1. **Novel fine-grained token-level reward design via atomic fact traceback.** The LCS-based method for converting statement-level fact judgments into token-level dense rewards (Section 3.2) is technically elegant. The ablation on reward granularity (Table 4/5) provides direct evidence that statement-level rewards outperform sentence-level (0.655 vs 0.645) and paragraph-level (0.639), confirming that finer granularity improves hallucination mitigation.

2. **On-policy RL with an automated annotation pipeline.** Unlike prior methods that use static, pre-collected datasets for fine-tuning, RLFH generates responses online and evaluates them via an LLM-based fact assessment framework without human intervention (§3.1.3). The main results (Table 1) show consistent FactScore improvements over all baselines across all three datasets, including out-of-distribution settings (SQuADv2, Biography), suggesting the learned behavior generalizes.

3. **Transparency about the refusal trade-off.** The paper openly acknowledges (Section 4.2) that the response rate drops, analyzes the pattern (Figure 8 shows the model refuses more on questions it originally performed poorly on), and discusses how this relates to conservative uncertainty expression. This transparency allows readers to interpret the reported FactScores with appropriate caution.

## Weaknesses

### Major

1. **The FactScore improvement is confounded by increased refusal rate, and the paper does not correct for this.** FactScore is computed only over *answered* prompts. On HotpotQA, the response ratio drops from 0.910 (Vicuna base) to 0.645 (RLFH) — a 29% relative decrease. A model that selectively refuses hard or uncertain questions can trivially inflate its FactScore. The paper acknowledges this (Section 4.2, lines 233-239) and provides detailed analysis (Figure 8) showing the model refuses more on prompts where it originally performed poorly. However, it never reports a coverage-adjusted metric (e.g., FactScore × response rate, or an F1-like measure over all prompts including refusals as zero-scoring). The data transparency is commendable, but without a combined metric, it is impossible to know how much of the reported gain reflects genuinely better generation versus strategic refusal. On HotpotQA, for example, RLFH has a lower #Cor. (13.05 vs 13.31) and higher #Inc. (8.304 vs 7.363) than FACT when it does answer — the higher FactScore likely comes from per-prompt averaging that dilutes poor answers via selective answering.

2. **The LLM-based reward model is never validated against human judgments, leaving the quality of the feedback signal unknown.** The entire RL pipeline depends on Mixtral-8x7B accurately extracting atomic facts, classifying each into one of five truthfulness categories, and assigning informativeness scores. The paper provides no analysis of the reward model's accuracy, precision/recall per label, calibration, or agreement with human annotations. The ablation on annotation model (Table 6/tab:anno) shows sensitivity across different LLMs but does not validate correctness — differences in output could reflect either better or worse fact-checking ability. Without knowing the false-positive/negative rate of the reward model's fact-checking, the RL objective is a black box. A reward model that misclassifies correct statements as "wrong" could penalize accurate generation and inadvertently encourage different forms of hallucination. This is a critical gap given that the method's novelty and the paper's claim 3 rest on the automated reward framework.

### Minor

3. **The central claim — that the *combination* of on-policy sampling and fine-grained rewards provides benefit beyond either component alone — is not directly tested.** The paper compares RLFH against FACT (off-policy, coarse-grained) and other baselines, but these differ on two dimensions simultaneously. The granularity ablation (Table 4/5) tests statement- vs sentence- vs paragraph-level rewards but keeps everything else (online RL, atomic fact extraction) constant. To substantiate the claim that the specific pairing of *on-policy + fine-grained* is responsible for the gains, the experiment should include at least one of: (a) online PPO with a coarse (response-level) reward from the same reward model, or (b) offline fine-tuning with the same fine-grained token-level rewards on a static dataset. Without this, the paper cannot attribute the gains to the claimed factors over alternative explanations (e.g., online sampling alone, or the specific reward shape).

4. **The improvement over the strongest baseline (FACT) is modest (+2.0% FactScore on average), and no statistical significance is reported.** The average absolute FactScore gains are small: +0.008 on HotpotQA, +0.007 on SQuADv2, +0.017 on Biography. No confidence intervals, standard errors over multiple seeds, or statistical tests are provided. Given the computational expense of PPO with a large reward model, it is not clear whether these gains are statistically distinguishable from noise. Reporting even 2–3 seeds with standard errors would substantially increase confidence.

5. **Conceptual tension between the "knowledge boundary" framing and the use of external ground-truth documents as rewards.** The paper frames hallucination as misalignment between generation and the model's *internal* knowledge boundaries (Section 1, Introduction), but the reward model punishes statements that conflict with *external* reference documents, not statements that the model itself would internally affirm or deny. The method is better characterized as enforcing factual consistency with a trusted external source — a different (and arguably simpler) setting — rather than teaching the model to respect the boundaries of its own knowledge. This does not invalidate the method, but the framing is somewhat mismatched with the experimental setup.

### Trivial

- None beyond what is addressed above. The paper is generally well-written and the method is clearly described.

## Nice-to-Haves

- A coverage-adjusted metric such as "Expected FactScore" = FactScore × (%Res.) across the full prompt set, or reporting correct/incorrect facts per prompt in the full set (counting refusals as zero correct and zero incorrect).
- Human validation of the reward model's judgments on a sample of atomic facts (precision, recall, F1 per truthfulness label).
- A 2×2 factorial ablation: (online vs. offline) × (fine-grained vs. coarse) to directly test the claim about the combination.
- Ablation on the reward balance coefficients (α, β) to understand the interaction between the truthfulness and informativeness terms, since the refusal rate increased despite the informativeness term being designed to prevent it.
- Cross-evaluation of FactScore using human judgments to rule out evaluation bias from using GPT-4 (since the reward model is Mixtral).

## Removed Points

These points are flagged to be removed from consideration; treat them with caution.

1. **"Key hyperparameters and reward mapping details omitted from the main paper"** — The reviewer criticizes missing Table \ref{tab:func} (function settings for *f* and *g*, coefficients α/β). This table is in the appendix, which the parser strips from all papers. Per instruction: weaknesses about absent appendix content are removed. The f/g function values and α/β coefficients exist in the original submission.

2. **"The paper should also cover additional methods from related work"** — The reviewer suggests adding comparisons to Cheng et al. 2024, Kang et al. 2024. Requests to broaden the baseline set beyond what is reasonable are removed as scope creep. The paper already compares against FACT (the most directly relevant learning-based method), DOLA, ITI, and 4 aligned baselines.

3. **"Missing analysis of atomic fact quality / reward distribution"** — The reviewer asks for a breakdown of how many statements fall into each truthfulness category. While interesting, this is a minor analysis addition and does not threaten the core claims.

## Novel Insights

The most interesting observation across the reviews is the interplay between granularity and refusal: the paper's own data show that the finest-grained reward (statement-level) achieves the highest FactScore but also the lowest response ratio (Table 4/5), and the highest #Inc. This suggests that fine-grained token-level rewards may be particularly effective at teaching the model *when to say nothing* (a key knowledge-boundary behavior), but less cleanly effective at improving precision on the questions it does answer. The paper's interpretation — that this reflects learning knowledge boundaries — is plausible but incomplete without disentangling the reward shape's effect on refusal policy from its effect on generation quality. This tension between coverage and precision is endemic to hallucination mitigation and deserves more explicit treatment than the paper currently provides.

## Suggestions

1. **Add a coverage-adjusted metric.** Report "Expected FactScore" = FactScore × (%Res.) across all prompts, or report an AUROC-style curve varying a refusal threshold. Report #Cor. and #Inc. per prompt in the full set including refusals as zeros. This directly addresses the most serious confound.

2. **Validate the reward model on a human-annotated sample.** Even 100–200 atomic facts with human judgments would provide critical confidence that Mixtral's truthfulness classifications are accurate enough to drive RL. Report precision, recall, and F1 per label.

3. **Add the 2×2 factorial ablation.** The most scientifically clean addition would be online-PPO-with-coarse-reward and offline-fine-tuning-with-fine-grained-reward conditions. If compute is limited, prioritizing the former (online + coarse) would be most informative, as it directly tests whether the gains come from online sampling or fine granularity.

4. **Report results from at least 2–3 random seeds with standard deviations** to establish that the gains over FACT are not noise.

5. **Rename or reframe the contribution.** The method aligns generations with *external* ground-truth documents, not *internal* knowledge boundaries. The paper should either: (a) reframe as "enforcing factual consistency with trusted external sources" (which is accurate and still valuable), or (b) add experiments that explicitly test internal knowledge boundary alignment (e.g., self-consistency checks, probing-based refusal on uncertain knowledge).

## Score and Decision

**Originality:** Good — token-level dense rewards from atomic fact traceback via LCS is novel, though the high-level idea (RL for factuality) builds on prior work.

**Importance of research question:** High — hallucination mitigation is a critical problem.

**Claims support:** Weak — the central claim is not fully supported due to the refusal confound, unvalidated reward model, and missing factorial ablation. The transparency of the paper is appreciated but does not substitute for corrected metrics.

**Soundness of experiments:** Adequate but incomplete — the main results show consistent improvement, but the evaluation confound and missing ablations weaken the conclusions.

**Clarity of writing:** Good — the method is well-described and the pipeline is clearly illustrated.

**Value to community:** Moderate — if the method is validated more rigorously, the fine-grained reward design and LCS-based traceback technique would be useful tools.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>