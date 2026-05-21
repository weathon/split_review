---
job_id: dc87293a-21c2-44ab-9e97-6a3547d2c784
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: GMlZt4fZSY.pdf
paper: MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly in scope for ICLR, focusing on language model pretraining, data curation, representation learning for language, and efficient training of compact reasoning models.

## Minimum Quality
Pass ✅. The paper includes the expected scientific components, namely abstract, introduction, related work, methodology, experiments/results, and conclusion, and it provides substantial empirical evidence, even though some methodological details and claim boundaries need tightening.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies how to train sub-billion-parameter language models with stronger reasoning ability using a fully open training recipe and substantially fewer pretraining tokens than commonly assumed necessary. The main proposal is a data-centric pipeline that combines leave-one-out analysis, influence-based dataset reweighting for pretraining, and iterative influence-based rejection/compression during mid-training, followed by standard SFT stages, yielding the MobileLLM-R1 family.

## Strengths
The paper addresses an important and timely question, namely whether strong reasoning behavior in small language models really requires extremely large proprietary corpora. This is a meaningful question for the ICLR community because it touches both scientific understanding of scaling/data efficiency and practical deployment constraints.

The empirical results are strong overall, especially for the fully open setting. The comparisons in **Table 2** are particularly valuable because they try to isolate the contribution of pretraining and mid-training from post-training by applying the same reasoning SFT corpus across models. Under that controlled setup, the gains of MobileLLM-R1 over SmolLM2 and OLMo-2 are substantial, especially at 360M and 950M. That table supports the core claim better than the broader headline comparisons because it reduces the “maybe it is just better SFT” objection.

The paper does more than present a model, it also exposes a fairly complete recipe. The release orientation, dataset lists, mixing ratios, and stage-by-stage training description are useful for the community. Even if some algorithmic pieces build heavily on prior ideas such as influence estimation, the overall package is much more reproducible than many small-reasoning-model papers.

Several figures help communicate the story well. **Figure 2** gives a clear high-level view of the three-stage pipeline, making it easier to see where the claimed contributions lie, namely pretraining mixture design, mid-training compression, and then standard post-training. **Figure 3** is also one of the more convincing parts of the paper because it visualizes cross-domain effects in the leave-one-out analysis rather than only reporting end metrics. The observation that removing FineWeb-Edu hurts all three capability probes is interesting and supports the paper’s argument that broad web data acts as “glue” across domains.

The influence-based datamixing results in **Figure 4** are directionally compelling. The fact that the proposed mixture improves perplexity trends on math, code, and general reasoning probes relative to the original mixture, without directly optimizing benchmark accuracy, is a good sign that the method is not completely benchmark-chasing.

The scaling/benchmark comparisons are impressive for a sub-billion open model. In **Figure 8** and **Table 8**, the 950M base model appears genuinely competitive with or stronger than several larger open baselines on GSM8K and HumanEval, and in **Figure 9** and **Table 9** the post-trained 950M model is competitive with much stronger partially open models on some reasoning tasks. Whether every comparison is perfectly apples-to-apples is debatable, but the overall empirical signal is difficult to dismiss.

I also appreciated that the paper includes some negative or nuanced findings rather than a one-note victory lap. For example, **Table 1** shows trade-offs between symbolic reasoning and factual knowledge retention, and Appendix D.2 explicitly states that extra RL does not necessarily help already SFT-trained small models. Those choices make the paper feel more scientifically grounded.

## Weaknesses
1. **The methodological novelty is narrower than the paper sometimes suggests, and the paper does not clearly disentangle what is genuinely new from what is inherited from prior influence-based data mixing work.**  
   The core pretraining weighting mechanism in **Section 2.2** is explicitly built on AutoMixer, with Eq. (2) as standard influence estimation and Eqs. (4)-(5) aggregating scores to dataset-level weights. The paper’s contribution seems to be mainly the adaptation of this machinery to capability-specific probing sets and cross-capability aggregation. That is a reasonable contribution, but the presentation sometimes reads as if a substantially new optimization framework has been introduced. I think the paper would be stronger if it stated more plainly: what is reused, what is modified, and what empirical benefit each modification yields. Right now, the conceptual increment is somewhat blurred by the broad framing.

2. **The central claim that roughly 2T high-quality tokens are “sufficient” is not established as cleanly as the abstract and introduction imply.**  
   There are at least two confounds. First, the actual training recipe uses **4.2T training tokens** in pretraining, since the paper states that the model is pretrained with 4.2T tokens sampled/resampled from about 1.8 to 2T source data. Second, the final model quality also depends materially on a nontrivial mid-training stage plus large-scale reasoning SFT, including 6.2M reasoning samples with long contexts in **Table 4** and **Table 7**. So the paper really shows that a compact model can become strong with a carefully curated open pipeline whose *unique-source pretraining corpus* is around 2T tokens, not that 2T tokens alone suffice for reasoning emergence in the stronger headline sense. This matters because the paper’s main rhetorical punchline is about data sufficiency, and that claim should be stated more carefully.

3. **Some experimental comparisons are not as fair or as interpretable as the paper would like, especially when comparing to partially open or differently post-trained models.**  
   The paper is strongest when comparing fully open models under controlled or at least similar post-training conditions, such as **Table 2**. It is weaker when making broad claims against models like Qwen3 in **Figure 1**, **Figure 8**, **Figure 9**, **Table 8**, and **Table 9**. Those models differ in architecture, tokenizer, optimization recipe, training duration, deduplication, post-training, and likely evaluation protocols beyond what is spelled out here. The paper does acknowledge “fully open” vs “partially open” groupings, which is good, but some textual claims still overinterpret these head-to-heads as evidence specifically for the proposed data curation method. At minimum, the paper should more sharply separate: controlled open-recipe evidence, versus broader contextual comparisons.

4. **The mathematical formulation has several clarity issues and some notation inconsistencies that make the proposed method harder to verify than it should be.**  
   In **Eq. (1)**, the paper defines group impact on a probing dataset using \(\mathcal{D}^{\mathcal{D}}_{\mathcal{C},\mathcal{M},\mathcal{K}}\), but elsewhere the probing set is denoted \(\mathcal{D}^{\mathcal{P}}_{\mathcal{C},\mathcal{M},\mathcal{K}}\). This is likely a typo, but in a method paper these distinctions matter. In **Eq. (3)**, the notation is not really an equation, more a list of influence evaluations, and the dependence on \(x_{\text{test}}\) is inconsistently written compared with **Eq. (2)**. In **Eq. (4)**, \(\mathcal{I}(x_i; \theta_{c,t})\) suppresses the test-distribution dependence entirely, even though that dependence is essential to the meaning of the influence score. In **Eq. (5)**, \(\rho_g = \frac{1}{N_g}\sum_{x_i\in g}\mathcal{I}_{\text{joint}}(x_i)\cdot s_i\) mixes sample-level averaging with token-count normalization, but it is not fully clear whether \(N_g\) is number of tokens in the full source corpus, in the representative subset, or in the post-filtered subset. Since \(s_i\) is already sample length, a precise normalization matters. These are not fatal mathematical errors, but they make the training objective and weighting rule less auditable than they should be.

5. **The “convergence” language in the mid-training compression section is too strong relative to the evidence shown.**  
   In **Section 3** and the discussion around **Figure 5**, the paper states that as samples approach zero or negative influence, the dataset’s information is “largely exhausted” and the process “converges.” What is actually shown in Figure 5 is that the score distribution narrows and shifts; that is an empirical histogram phenomenon, not a proof of convergence in any optimization or statistical sense. There is no theorem here, no monotonic improvement guarantee, and no evidence that zero-influence concentration implies informational exhaustion rather than estimator noise, approximation error in influence computation, or changed alignment with the probes. This wording should be softened, because readers could otherwise mistake an intuitive interpretation for a supported property of the algorithm.

6. **The evidence that the capability-probing datasets are faithful proxies for downstream reasoning is suggestive, but still under-validated.**  
   A great deal of the paper hinges on the representative subsets and probing datasets built in **Section 2.1.1**, yet their validity is mostly argued heuristically. The construction pipeline uses FineWeb-Edu filtering, Ask-LLM scoring, domain prompts, and semantic deduplication, but there is little direct evidence that improvements in NLL on these probes reliably predict benchmark improvements across training stages, model scales, or alternative mixtures. **Figure 4** offers some support, but it is still indirect. Since the whole “benchmark-free” claim depends on these probes being good surrogates, I wanted either a stronger correlation study or a more careful limitation statement.

7. **The paper packs many moving parts into one recipe, which makes causal attribution difficult.**  
   The final gains may come from some combination of architecture choices, tokenizer, two-phase pretraining, the chosen corpora, influence-based weighting, mid-training mixture changes, sample rejection, distillation in mid-training, staged SFT, and reasoning data selection. The paper provides useful ablations on post-training in **Table 1**, and useful comparative evidence in **Table 2**, but there is still no tight ablation isolating, for example, influence-based reweighting versus a simpler heuristic skew toward math/code, or iterative rejection versus just using phase-2 ratios once. This matters because the paper’s scientific value is not only that the final recipe works, but that the proposed selection principle works better than simpler alternatives.

8. **Some figure-based arguments are stronger narratively than scientifically.**  
   **Figure 7** is used to suggest that math knowledge acquired during pretraining transfers to coding ability because HumanEval perplexity drops later after the second phase of mid-training. That is an interesting hypothesis, but the figure alone does not identify transfer direction or mechanism. Many other changes happen between stages, and perplexity on benchmark prompts is at best a loose proxy for coding competence. Likewise, **Figure 1** presents a Pareto-style training efficiency frontier, but the x-axis mixes “approximate pretraining FLOPs” and tokens in a simplified way while comparing heterogeneous model families. It is visually persuasive, but I would be careful about the strength of the conclusion drawn from it.

9. **Benchmark contamination and benchmark-adjacent training choices need sharper discussion.**  
   The paper repeatedly emphasizes “benchmark-free” data optimization, yet **Table 6** shows benchmark-style datasets in mid-training phase 2, including GSM8K, ARC-Easy, ARC-Challenge, OBQA, BoolQ, PIQA, TriviaQA, and NaturalQuestions train splits. Using training splits is not improper, but it does weaken the broader rhetorical framing that benchmark data are not used. Also, because some evaluations are from the same benchmark families, the paper should more explicitly discuss contamination risk and family overlap. This is especially important for small-model reasoning papers, where even modest benchmark overlap can significantly alter conclusions.

10. **Presentation is generally good, but there are enough wording/notation issues that some core claims feel sloppier than they need to be.**  
   Examples include “a established post-training procedure” in the abstract, inconsistent naming such as “StatCoder” vs “StarCoder” near **Section 2.2**, and several notation slips around \(\mathcal{D}^{\mathcal{P}}\) versus \(\mathcal{D}^{\mathcal{D}}\). These are individually minor, but collectively they matter because the paper is making fairly intricate methodological claims. A cleaner, tighter main paper would increase confidence.

## Questions
1. The strongest empirical support for your method comes from the end-to-end recipe, but the scientific contribution would be clearer with more isolation. Can you provide a cleaner ablation separating:
   - uniform mixture,
   - heuristic domain-skewed mixture,
   - AutoMixer-style influence without cross-capability aggregation,
   - your full joint influence with cross-capability aggregation,
   while holding total tokens fixed?  
   This would substantially increase my confidence that the gain comes from the proposed weighting principle rather than from generally “using more math/code data.”

2. Please clarify the mathematical notation in **Eqs. (1), (4), and (5)**. In particular:
   - should the probing dataset be \(\mathcal{D}^{\mathcal{P}}\) rather than \(\mathcal{D}^{\mathcal{D}}\) in Eq. (1)?
   - what is the exact definition of \(\mathcal{I}(x_i;\theta_{c,t})\) in Eq. (4), since the test distribution has disappeared?
   - in Eq. (5), is \(N_g\) the full-corpus token count, representative-subset token count, or sampled-token count?  
   A precise answer here would help assess whether the weighting scheme is well-defined.

3. The paper’s headline says \(\sim 2\)T high-quality data are sufficient, but the actual pretraining uses 4.2T sampled tokens plus mid-training and substantial SFT. Would you be willing to restate the claim more narrowly as “2T unique open-source tokens, when appropriately resampled and followed by mid/post-training, are sufficient to reach these results”? If not, please explain why the stronger wording is justified.

4. Can you provide quantitative evidence that the capability-probing datasets are good surrogates for downstream reasoning? For example, correlations between probe NLL changes and final benchmark changes across multiple mixtures/checkpoints/dataset removals would strengthen the “benchmark-free” claim considerably.

5. In **Figure 5**, the interpretation that influence scores converging toward zero means the data are “exhausted” seems stronger than what the histogram alone supports. Do you have any additional evidence, such as monotonic benefit reduction under continued training, or agreement across different influence estimators/checkpoints, that this is not just an artifact of the estimator?

6. Since **Table 6** includes benchmark train splits in mid-training phase 2, please clarify exactly which downstream evaluations are from overlapping benchmark families and what safeguards were used to ensure no leakage from test/dev sets into tuning or data-mix design. This would help sharpen the boundary between legitimate training usage and potentially optimistic evaluation.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics red flags are apparent from the main paper. The work uses public datasets and focuses on methodology. The main non-ethics concern is evaluation contamination or benchmark-family overlap, but that is a scientific validity issue rather than an ethics-review issue.

## Soundness Rating
3: good. The paper is empirically substantial and the main claims are mostly supported, but several claims are overstated relative to the evidence, and the methodological/mathematical specification needs tightening.

## Presentation Rating
3: good. The paper is readable and generally well organized, with effective figures and tables, but there are enough notation inconsistencies and some over-strong wording that clarity falls short of excellent.

## Contribution Rating
3: good. The paper makes a valuable contribution through a strong open recipe and compelling small-model results, though the conceptual novelty is more in the integrated data-centric recipe than in a sharply isolated new algorithmic idea.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
This is a strong empirical paper with a useful open recipe and results that will interest the community, especially in the fully open small-model setting. My hesitation is that the paper sometimes oversells what is established, and the core methodological novelty is less crisp than the performance tables might suggest. Still, the empirical package is substantial enough that I lean positive.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the small/open LLM training literature, though some implementation-level details of the influence estimation pipeline would benefit from author clarification.