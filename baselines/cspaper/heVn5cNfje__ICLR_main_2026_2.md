---
job_id: 3c3b80bd-32b6-4843-b5da-708f4f9cd795
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: heVn5cNfje.pdf
paper: Unified Data Selection for LLM Reasoning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about LLM training, data selection, entropy-based scoring, and reinforcement learning style post-training, all of which fit squarely within ICLR topics on language models, RL, uncertainty-related metrics, and general machine learning.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, methodology, experiments, quantitative results, related work, and conclusion; while I found several important methodological and empirical weaknesses, they do not rise to the level of an immediate desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find reviewer-directed hidden prompts or explicit attempts to manipulate an automated review. There is some unrelated extraneous text on Pages 22 to 23 that appears anomalous, but it does not contain instructions targeting the review process.

# Expected Review Outcome:
## Summary
This paper proposes High-Entropy Sum (HES), a training-free metric for ranking reasoning traces by summing the entropies of only the top 0.5% highest-entropy tokens in a response. The authors argue that these high-entropy tokens correspond to key forking points in chain-of-thought reasoning, and they apply HES as a unified data selection signal across SFT, RFT, and RL. Empirically, the paper reports that HES-based selection can outperform random or several heuristic alternatives, sometimes allowing models trained on subsets of data to match or exceed full-dataset baselines.

## Strengths
1. The paper addresses a practically important problem. Data selection for reasoning traces is indeed a meaningful bottleneck for SFT, RFT, and RL style reasoning training, and the attempt to use one lightweight scoring signal across all three paradigms is well motivated.

2. The core idea is simple and easy to implement. HES is defined in a straightforward way in **Equations (1) to (3)** on **Page 4**, and the intuition, focusing on a small minority of high-entropy tokens rather than averaging over all tokens, is easy to follow. This simplicity is a real strength compared with approaches that require extra reward models or learned selectors.

3. The paper includes a fairly broad empirical sweep across training paradigms. It is useful that the authors do not restrict the story to SFT only, but also test HES in RFT and RL. Even if I have reservations about some of these experimental designs, the cross-paradigm ambition is broader than many data selection papers.

4. The empirical signal is not entirely trivial. In **Table 1 (Page 6)**, the gap between **Highest-HES 20%** and **Lowest-HES 20%** is very large, and the same directional effect appears again in **Table 2**, **Table 3**, **Table 4**, and **Table 5**. This repeated “top vs. bottom” separation does suggest that HES captures something non-random about the reasoning traces.

5. The paper does include some visualization support for its central premise. **Figure 1 (Page 2)** shows score distributions for correct versus incorrect responses under several entropy-based metrics, and the HES panel does appear more separated than the average-entropy alternatives. Similarly, **Figure 2 (Page 3)** is helpful for clarifying exactly which tokens are counted by each metric, and this figure improves the exposition of the method.

6. I appreciated the small-to-large transfer experiment in **Table 1** using proxy models for selection, since model-dependent scoring is an obvious concern. The result that a 0.6B or 1.7B selector is roughly competitive with self-selection by the 8B model is useful evidence, even though more analysis is still needed.

## Weaknesses
1. **The paper’s central conceptual claim, that HES measures “reasoning quality,” is not actually established, and some evidence in the paper points in the opposite direction.**  
   The paper repeatedly equates higher HES with higher-quality reasoning, for example on **Page 4**, where a higher HES is said to indicate “higher quality.” But the earlier discussion around **Figure 1 (Page 2)** only shows separability between correct and incorrect samples under a specific sampling setup, and even there the metric looks more like a proxy for “difficulty / branching / uncertainty” than quality per se. In fact, in the appendix analysis on **Page 19**, the paper states that “the mean HES for incorrect paths is substantially higher than for correct paths,” which cuts directly against the paper’s main semantic interpretation. If incorrect trajectories can have higher HES on average, then HES is not a clean quality metric in the sense claimed by the title and the method section. At best, it may be a usefulness or pedagogical-value heuristic. That distinction matters, because the paper’s framing overstates what the metric is actually measuring.

2. **HES is likely heavily confounded with response length, and the paper does not adequately disentangle this.**  
   This is one of the biggest issues for me. HES is a *sum* over top-percentile token entropies. Even with percentile normalization, the number of included tokens scales roughly with sequence length, so longer traces can get larger HES almost by construction:
   \[
   HES_{\text{relative}} = \sum_{t \in T_{\text{top-}p}} H_t, \qquad |T_{\text{top-}p}| \approx pN .
   \]
   If the expected entropy of selected tokens is comparable across traces, then \(HES_{\text{relative}}\) grows approximately linearly with \(N\). The paper claims the relative threshold makes the metric “robust to variations in length” on **Page 4**, but no derivation or empirical decorrelation analysis is provided. The results in **Table 1 (Page 6)** actually strengthen this concern: the **Length-20%** baseline reaches **30.67 AVG**, while **Highest-HES-20%** gives **31.14 AVG**, which is a fairly small improvement relative to the strength of the claims. In RFT, **Length** is also often close to **Highest-HES** in **Table 5 (Page 8)**. If the method’s gains over length are this modest, the authors need a much sharper analysis showing that HES is not mostly rediscovering long traces. For example, they should report rank correlation between HES and length, or compare against a normalized version such as
   \[
   \frac{1}{|T_{\text{high}}|^\alpha}\sum_{t\in T_{\text{high}}} H_t
   \]
   for \(\alpha \in \{1/2,1\}\), or perform matched-length comparisons.

3. **The mathematical specification of the core metric is sloppy and in places inconsistent.**  
   The notation in **Equation (1)** on **Page 4** is not well defined. “\(\text{rank}(H_t)\ge 1-p\)” is ambiguous unless rank is explicitly normalized to \([0,1]\), and even then it is unusual notation for selecting the top \(p\) fraction of tokens. It would be clearer to define an ordered sequence \(H_{(1)} \ge \cdots \ge H_{(N)}\) and sum the top \(k=\lceil pN\rceil\) values:
   \[
   HES_{\text{relative}} = \sum_{i=1}^{\lceil pN\rceil} H_{(i)} .
   \]
   The definition of \(AvgHE\) in **Equation (3)** is also muddled. The text says it is “designed to isolate the average complexity of key-fork tokens, different from \(AvgHE\),” which is self-contradictory. More importantly, the notation quietly switches from \(HES\) to \(HES_{\text{relative}}\), and the set \(T_{\text{high}}\) is not rigorously specified for every variant. These are not fatal mathematical errors, but for a paper whose entire contribution is a scoring rule, the formal definition should be much cleaner than this.

4. **The RFT formulation in Section 2.1 is mathematically incorrect or at least badly misstated.**  
   On **Page 2**, the RFT step says
   \[
   Y = \operatorname*{argmax}_{y_i \in \{y_1,\ldots,y_m\}} R(y_i),
   \]
   while also describing \(Y\) as a “response subset.” But \(\arg\max\) returns a maximizing element or set of ties, not a subset of arbitrary size \(k\). This becomes especially problematic because the actual experiments in **Section 4.2** later use \(k\in\{2,4,8\}\) responses per query. So the preliminary notation does not match the actual procedure. If the intended operator is “select top-\(k\) by score,” then the paper should say so formally, e.g.
   \[
   Y = \text{TopK}\left(\{y_i\}_{i=1}^m; R, k\right).
   \]
   This may sound pedantic, but the mismatch between formalism and experiment makes it harder to trust the methodological presentation.

5. **The RL section does not convincingly show that HES is a principled RL signal rather than a batch-curriculum heuristic.**  
   The paper frames HES as establishing a unified metric across SFT, RFT, and RL, but the RL experiment in **Section 4.3** is really a selective subsampling strategy within GRPO rollouts, not a replacement reward or a theoretically motivated policy objective. In **Table 6 (Page 9)**, the best method, **Pos-High, Neg-Rand**, improves average score from **20.63** for **Full-Batch** to **21.30**. This is a small gain, and the story is fragile because several alternatives cluster closely around 20. In addition, “positive” means already successful trajectories, so the method is using ground-truth task correctness first and HES second. That is a much weaker claim than “HES can serve as a training-free reward signal,” which is asserted in the abstract and introduction. The RL evidence supports a selective replay or curriculum statement, not the much broader reward-signal framing.

6. **The experimental setup leaves open serious concerns about evaluation noise and statistical significance.**  
   Nearly all conclusions are drawn from single reported averages without variances, confidence intervals, or multiple-run seeds. Given that many claimed improvements are around 0.5 to 1.5 points, this matters a lot. For instance, in **Table 1 (Page 6)**, **Highest-HES-20%** is **31.14 AVG** versus **Highest-ES-20%** at **30.92**, and versus **Length-20%** at **30.67**. Without seed variance, these are very hard to interpret. Likewise in **Table 5 (Page 8)**, several per-query and global-pool comparisons are close enough that run-to-run noise could change the ordering. A paper making a broad unifying claim should not rest on single-seed deltas of this size. At minimum, the authors should report mean ± std over several fine-tuning runs for key comparisons.

7. **The baseline set is not strong enough to justify the breadth of the claims.**  
   The paper compares mainly to random, length, heuristic difficulty, average entropy, total entropy, and a few ablations. That is a reasonable start, but for a paper making a general claim about data selection for long-CoT reasoning, the experimental positioning is too narrow. There is little engagement with stronger or more targeted data selection strategies beyond simple heuristics. Even within the paper’s own setup, it would be important to compare against length-controlled entropy selection, diversity-aware selection, or hybrid quality-diversity selection, especially since the authors themselves note in **Section 4.2** that preserving query diversity seems crucial. The current experiments mostly show that HES beats weak baselines, not that it is the right selection principle more generally.

8. **The claim of “unified” data selection is overstated relative to what is actually demonstrated.**  
   The title and contributions section promise unified data selection for reasoning. In practice, the paper presents three rather different uses of the same score: offline subset filtering in SFT, candidate ranking among already-correct traces in RFT, and positive-trajectory subsampling in RL. These are not the same problem. In SFT, HES ranks static demonstrations. In RFT, it ranks only among correctness-filtered candidates. In RL, it is not even used as reward, but as a post hoc selector among successful rollouts. This is more accurately “one scalar heuristic applied in several settings,” not a unified formulation with a consistent objective across paradigms.

9. **The paper’s figure-based evidence is suggestive but also reveals some tension with the narrative.**  
   **Figure 1 (Page 2)** is the key visual evidence, and it does support the claim that HES separates correct and incorrect samples better than average entropy in that particular setup. However, the panel also seems to show HES as a discriminator of *sample type* rather than a direct measure of correctness-aligned quality. That distinction becomes important given the appendix statement that incorrect paths can have higher HES. Similarly, **Figure 3 and Figure 4 (Page 10)** show that peak performance often occurs around 20% or 80% retained data, but the curves are not universally sharp, and in some cases the gains look modest. The sensitivity plots suggest that HES is somewhat useful, but not nearly decisive enough to support the stronger rhetoric in the abstract.

10. **There are several writing and presentation issues that undermine confidence.**  
   The paper contains many small but noticeable problems: duplicated paragraph titles in **Section 4.2.2** on **Pages 7 to 8**, grammar issues such as “making the model to deconstruct” on **Page 4**, inconsistent naming between **Highest-ES**, **HES**, and **Entropy Sum**, and formatting problems in **Table 6 (Page 9)** where the header appears broken. More concerningly, the appendix includes clearly extraneous content on **Pages 22 to 23** that is unrelated to the paper. Even if accidental, this suggests the manuscript has not been carefully cleaned. None of these alone would be decisive, but together they weaken the presentation.

11. **The computational efficiency claim is under-supported in the main paper.**  
   The paper repeatedly markets HES as efficient and training-free, but in SFT it still requires a full forward pass over every candidate sequence to obtain token entropies. That may be cheaper than training an auxiliary selector, but it is not “free.” The cost discussion appears only in the appendix, while the main paper makes strong efficiency claims without quantifying the screening overhead. This matters because the observed gains over simple baselines like length are sometimes small, so compute-adjusted benefit should be part of the central evaluation.

12. **The domain generalization claims are weaker than advertised.**  
   The non-math evidence in **Table 3** and **Table 4 (Page 6)** is welcome, but thin. The code and STEM settings use only a few benchmarks, and some results are odd, for example the **HMMT25** behavior in **Table 4** where full-data and 80% HES are both extremely low. The paper presents these tables as proof of broad universality, but with this level of coverage they read more like preliminary transfer checks than a convincing domain-general validation.

## Questions
1. Can the authors provide a direct analysis of the relationship between HES and sequence length? I would like to see at least rank correlation, partial correlation controlling for correctness/difficulty, and matched-length comparisons. If HES still wins clearly under length control, that would materially increase my confidence.

2. Can the authors clarify the intended mathematical definition of **Equation (1)**? Please define ranking unambiguously, specify whether exactly \(\lceil pN\rceil\) tokens are selected, and rewrite the expression in standard order-statistics notation if possible.

3. In **Section 4.2**, what is the exact RFT selection operator? The formal description in **Section 2.1** uses \(\arg\max\), but the experiments use top-\(k\) selection. Please state the exact training set construction mathematically and consistently.

4. For the key results in **Table 1**, **Table 5**, and **Table 6**, can the authors report mean and standard deviation over multiple seeds? At present many improvements are small enough that variance could change the conclusions.

5. The paper often says HES measures “quality,” but the appendix analysis appears to indicate incorrect paths can have higher HES than correct ones on average. Can the authors reconcile this? Is HES actually a measure of complexity, branching, or pedagogical value rather than quality?

6. For the RL experiments, can the authors clarify whether HES is ever used independently of correctness labels? If not, I think the “training-free reward signal” language is too strong. A rebuttal clarifying the intended claim would help.

7. Can the authors quantify the compute overhead of HES screening in the main paper, especially compared with length-based filtering? A rough FLOP or wall-clock analysis would help assess whether the extra complexity is justified.

8. Did the authors tune the 0.5% token ratio using held-out validation data, and if so, on which tasks? The sensitivity curves in **Figure 3** and **Figure 4** are useful, but I want to understand whether any benchmark leakage occurred in choosing this default.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns stood out from the main paper. The work uses public models and datasets, and the submission does not raise direct issues requiring specialized ethics review beyond standard concerns around more capable reasoning models.

## Soundness Rating
2: fair. The central idea is plausible and supported by some empirical evidence, but the claims substantially outrun what is rigorously established, especially regarding what HES actually measures, how much it differs from length, and whether small reported gains are statistically reliable.

## Presentation Rating
2: fair. The high-level idea is understandable, and figures such as **Figure 2** are helpful, but the paper has enough notation issues, inconsistencies, duplicated text, and formatting problems that the presentation falls below the standard I expect for a polished ICLR paper.

## Contribution Rating
2: fair. The problem is important and the heuristic is simple and potentially useful, but the paper does not yet convincingly establish a strong enough scientific contribution beyond an empirical entropy-based scoring trick with limited differentiation from simpler alternatives.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is promising and addresses an important problem, but there are too many unresolved issues around confounding, mathematical precision, baseline strength, and overclaiming for me to support acceptance in its current form. The strongest path to changing my mind would be a convincing rebuttal on the length confound, clearer formalization, and variance-aware evidence for the key empirical gains.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the surrounding literature on LLM reasoning, entropy/probability-based scoring, and post-training pipelines, though I have not independently reproduced the experiments.