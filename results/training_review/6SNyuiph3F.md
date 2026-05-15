Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces the "chat vector," a simple parameter-space operation obtained by subtracting the weights of a pre-trained LLM (LLaMA2) from its chat-tuned counterpart (LLaMA2-chat). Adding this vector to a model that has undergone continual pre-training (CP) on a non-English language corpus aims to transfer instruction-following, safety alignment, and multi-turn dialogue capabilities to that target language without requiring supervised fine-tuning (SFT) or reinforcement learning from human feedback (RLHF). The method is evaluated primarily on Traditional Chinese (LLaMA2-13B), with additional experiments on Korean (llama-2-ko-7b) and Simplified Chinese (Chinese-LLaMA), using Vicuna benchmark, Real Toxicity Prompts, and Safety Prompts.

## Strengths

- **Simple, computationally efficient method.** Replacing the standard CP→SFT→RLHF pipeline with CP + a single arithmetic addition in parameter space is conceptually elegant and dramatically reduces training cost. The paper explicitly quantifies this efficiency advantage over the multi-stage RLHF pipeline.

- **Demonstrated improvement in instruction following across multiple languages.** The evidence (Table 1) shows that adding the chat vector to a continually pre-trained model substantially boosts GPT-4 evaluation scores — e.g., from 1.90 to 6.32 for Traditional Chinese and from 1.57 to 4.10 for Korean — indicating that chat ability can be transferred cross-lingually.

- **Generalization beyond a single language or base model.** The method is tested on three language variants (Traditional Chinese, Korean, Simplified Chinese) and two base model families (LLaMA2-13B, Chinese-LLaMA-13B), lending credence to the claim that the effect is not language-specific.

- **Transparent acknowledgment of a key limitation with attempted mitigation.** Section 5.5 honestly reports that adding the chat vector to Chinese-LLaMA causes excessive English output, and experiments with a 0.5 scaling factor to trade off language purity against instruction-following quality. This scientific transparency is commendable.

- **Preservation of multi-turn dialogue.** Figure 2 provides a concrete demonstration that the chat-vector-augmented model retains conversational context ("lightning bolt" disambiguation) that is lost in the baseline without the vector, despite the fine-tuning data containing only single-turn examples.

## Weaknesses

### Fatal
None.

### Major

1. **No target-language RLHF baseline.** The paper frames itself as "restructuring the conventional training paradigm from CP→SFT→RLHF to CP+chat vector," yet never compares against a model that actually underwent RLHF (reward modeling + PPO) in the target language. The strongest baseline is CP→FT, which lacks the RLHF component entirely. Without a direct comparison, it is impossible to know whether the chat vector reproduces the effects of RLHF or merely provides general instruction-following ability inherited from LLaMA2-chat's SFT stage. This gap undermines the paper's central claim about replacing RLHF.

2. **English-language response bias is a real, unsolved structural limitation.** The chat vector is derived from LLaMA2-chat (an English-centric model) and inherently carries English-distribution chat behavior. While the main Traditional Chinese model with FT achieves 97.5% target-language output, the problem is acute for Chinese-LLaMA and for models without FT (79.2% for llama2→CP+chat vector on Vicuna). The 0.5 scaling mitigation reduces the bias but also degrades instruction-following and safety. This is not a minor implementation detail — it reveals that the method overlays English chat patterns rather than learning to chat natively in the target language, and the paper's contribution (line 23) that "the resultant model responds precisely in the target language" is only partially supported.

3. **Evaluation metrics are not validated for the target languages.** (a) Perspective API was designed for English content; its toxicity scoring on Traditional Chinese text is unverified. (b) The GPT-4 evaluation on Vicuna benchmark uses GPT-4 as both the reference (assigned a perfect 10) and the judge, introducing systematic bias toward GPT-4's own generation style. (c) The safety evaluation uses GPT-3.5 with an ad-hoc function-call protocol rather than validated Chinese safety benchmarks or human judgments. These methodological concerns weaken the evidential basis for the paper's quantitative claims.

### Minor

1. **Multi-turn dialogue evidence rests on a single qualitative example.** Figure 2 shows only one case study. While the demonstration is illustrative, a single example does not constitute robust evidence of multi-turn capability. Quantitative metrics (e.g., context retention rate across many turns, language consistency in multi-turn settings) are absent.

2. **No confidence intervals, significance tests, or variance reporting.** All reported results are point estimates without measures of uncertainty. While single-run evaluations are common in LLM benchmark papers, the absence is notable given the paper's strong comparative claims.

3. **The abstract and conclusion overstate the strength of the evidence.** Phrases like "superior efficacy," "significant solution," and "integration of linguistic knowledge and alignment with human values can be achieved through basic vector addition" go beyond what the experiments demonstrate, particularly given the missing RLHF baseline and the English-bias limitation.

### Trivial
None.

## Nice-to-Haves

- An ablation study isolating the contribution of the SFT component vs. the RLHF component of the chat vector (e.g., using a model that underwent only SFT, not RLHF, as the source).
- Layer-wise analysis of which parts of the chat vector drive instruction-following vs. language shift vs. safety behavior.
- Systematic language-purity reporting (percentage of target-language tokens per response) across all evaluation prompts, not just a single table of aggregate proportions.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's claim that the core claim is "fundamentally incompatible" and "misleading" is removed as overblown: the paper's Traditional Chinese model (with FT) achieves 97.5% correct-language output, and the English-bias issue is specifically documented for Chinese-LLaMA. The method does equip LLMs with new-language chat capabilities for the primary case study.
- The critic's note about "Training datasets are described but not released" is removed per hard rules (availability criticism of cited resources).
- The critic's note about "no discussion of whether the chat vector should be scaled or normalized per layer" is removed as a scope-creep demand (the paper explicitly frames the method as simple uniform addition).
- Strength Finder's claim about "Multi-faceted evaluation" supporting the paper's claims is retained as a strength of scope but is qualified by the verified weakness that several evaluation tools are unvalidated for the target languages.

## Novel Insights

None beyond the paper's own contributions. The core insight — that a simple parameter-space difference between a chat model and its base can transfer chat behaviors to a continually pre-trained non-English model — is the paper's main novelty, and the reviewers surface no additional interpretation beyond what the authors provide.

## Suggestions

1. **Add a target-language RLHF baseline.** Even a small-scale RLHF (e.g., training a reward model on ~10K examples and running a few PPO steps) would allow a direct comparison and test whether the chat vector actually reproduces RLHF effects. Without this, the paper cannot substantiate its framing as replacing the RLHF stage.

2. **Validate or replace Perspective API for Chinese toxicity evaluation.** Either provide evidence that Perspective API scores correlate with human judgments on Traditional Chinese text, or use a toxicity detection tool validated for Chinese.

3. **Increase the number and rigor of multi-turn evaluations.** Provide quantitative metrics across many dialogue turns (e.g., context retention accuracy, language consistency) rather than relying on a single qualitative example.

4. **Tone down the claims in the abstract and conclusion** to match the experimental scope. The paper's genuine contribution — a simple, cheap method that improves chat abilities — does not require overstated language about "superior efficacy" or "significant solution."

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>