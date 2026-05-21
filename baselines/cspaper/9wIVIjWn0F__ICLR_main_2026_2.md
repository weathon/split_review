---
job_id: 2aa92f1e-808e-4561-a795-22849749d91b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 9wIVIjWn0F.pdf
paper: Regression-Based Test-Time Adaptation of Vision-Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on test-time adaptation for vision-language models, uncertainty/confidence estimation, and representation learning under distribution shift.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methods, experiments, quantitative results, and conclusion. While I have substantial concerns about novelty, methodological specification, and claim strength, these issues do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Regression-based Test-Time Adaptation (RTA) for CLIP-like vision-language models. The main idea is to train, offline, a regression model that maps per-view logits to a predicted pseudo cross-entropy loss, then use this predicted loss at test time to rank augmented views and ensemble the top-ranked ones instead of relying on entropy-based view selection.

Empirically, the paper reports improvements over several TTA baselines on ImageNet-style single-label benchmarks, 10 cross-domain datasets, and three multi-label datasets. The paper also includes analyses intended to motivate the method, including a “ceiling TTA” experiment using true label cross-entropy, t-SNE and correlation visualizations, and sensitivity studies on the number of augmented views and regression samples.

## Strengths
1. The paper addresses a relevant problem. View selection is indeed a central ingredient in many CLIP test-time adaptation pipelines, and questioning whether entropy is the right proxy is a reasonable research direction.

2. The method is operationally simple. An offline regressor that predicts a per-view score from logits, followed by top-$k$ selection and ensembling, is easy to understand at a high level and potentially practical if it truly transfers across tasks and domains.

3. The empirical scope is fairly broad in the main paper. The authors evaluate on ImageNet variants, 10 cross-domain datasets, and multi-label benchmarks, with results for both RN50 and ViT-B/16. This breadth is useful and goes beyond a single benchmark story.

4. Some of the reported gains are non-trivial. In **Table 3**, the improvements over strong baselines on ImageNet-A and ImageNet-R are noticeable, especially for RN50. For example, RN50 RTA improves over BCA on IN-A and IN-R. Likewise, in **Tables 5 and 6**, the gains over ML-TTA on MSCOCO/VOC/NUSWIDE suggest the method is not obviously limited to single-label classification.

5. The “oracle ceiling” analysis is a useful sanity check, even if it is unsurprising. **Tables 1 and 2** clearly show that selecting views using true label cross-entropy vastly outperforms entropy-based selection. This does support the high-level motivation that a better proxy for per-view correctness could matter materially.

6. **Figure 1** communicates the intended contrast between existing entropy-based pipelines and the proposed regression-based ranking fairly clearly. Even though the conceptual picture is simplified, it helps the reader understand what component is being replaced.

## Weaknesses
1. **The central learning target is conceptually under-motivated and partly tautological.**  
   The paper repeatedly frames the key finding as a “strong regression mapping” between logits and label cross-entropy loss, but for single-label classification the label cross-entropy is already a deterministic function of the logits and the label:
   \[
   \mathcal{L}_{\mathrm{CE}}(y \mid s) = -\log \frac{e^{s_y}}{\sum_k e^{s_k}}.
   \]
   This is exactly **Equation (4)** on **Page 5**. So the only genuinely unknown quantity is the label index \(y\), not some mysterious nonlinear relation from logits to loss. Put differently, the method is learning to predict “how likely the predicted pseudo-label is to be correct” from the logit vector. That may still be useful, but the current presentation inflates this into a broader claim than the formulation supports. This matters because the paper’s novelty and scientific framing hinge on this claimed discovery.

2. **There is a serious mismatch between the main-method formulation and the actual cross-dataset inference story.**  
   In the main paper, **Equation (3)** and **Equation (4)** define training on logits over the task label set of size \(L\), and **Equation (8)-(10)** on **Page 6** are written as if the same logit vector is used at test time. However, this does not explain how one regression model trained once can be applied to arbitrary target datasets with different label spaces. The main text claims task independence, but the notation assumes a shared label set. The appendix later introduces a different mechanism, namely using logits against a fixed 1000-class “base category set” for regression and a separate target label set for classification. That is a major missing piece and should have been in the main paper. As written, the core method in the main paper is underspecified for exactly the setting the paper claims to solve.

3. **The mathematical notation is sloppy and sometimes incorrect enough to hinder verification.**  
   There are multiple inconsistencies:
   - In **Equation (3)** on **Page 5**, the left-hand side is \(s_l^{\mathbf{x}^{\text{reg}}}\) but the text says “the logit for \(j\)-th class,” mixing \(l\) and \(j\).
   - In **Equation (8)** on **Page 6**, the superscripts and subscripts are wrong: it writes \(s_{ij}^{\mathbf{x}_{ij}^{\text{reg}}}\) while the surrounding text is about a test view \(\mathbf{x}_i^{\text{test}}\). This is not a cosmetic issue because this equation defines the inference features.
   - **Equation (9)** and **Equation (10)** continue using \(\mathbf{x}^{\text{reg}}\) / \(\mathbf{x}_i^{\text{reg}}\) notation inside the test-time phase, again conflating training and inference domains.
   - **Algorithm 2** says line 7 uses Eq. (8), but Eq. (8) itself is malformed and not aligned with the algorithm.
   
   These are exactly the kinds of notation problems that make it difficult to assess whether the method is rigorously specified. For a paper whose contribution is mostly methodological rather than theoretical, precise specification matters a lot.

4. **The paper does not adequately specify the pseudo-label generation procedure, even though the method depends on it critically.**  
   The first stage learns from “pseudo-label cross-entropy loss” and says pseudo-labels are obtained “by filtering high-confidence samples” on **Page 5**. But many important details are absent from the main paper: what data source exactly is used, how class imbalance is handled, whether pseudo-label confidence is measured by max softmax or some other criterion, whether the threshold is backbone-specific, and how much label noise remains after filtering. The implementation paragraph on **Page 7** mentions “sampling by logit-based equal-interval from 5,000 samples with threshold \(\ge 0.8\),” but this is still too vague for such a central component. Since the target is computed from pseudo-labels, label noise directly affects the regression target and therefore the final view ranking. Without a careful description, reproducibility and validity are weakened.

5. **The main empirical claim, “trains once on diverse unlabeled data and adapts to any test distribution,” is overstated relative to the evidence.**  
   The paper repeatedly claims broad transfer to arbitrary distributions, for example in the contribution bullets on **Page 2** and conclusion on **Page 9**. But the evidence in the main paper is much narrower: one offline regressor trained on a particular source, evaluated on a standard suite of image classification datasets under the same CLIP backbone. This is not enough to justify “arbitrary distributions.” The experiments show some transfer across a set of natural image benchmarks, not arbitrary distributions. The wording should be reduced to match the empirical support.

6. **The comparison to prior work is incomplete and selectively framed around entropy-based methods.**  
   The paper positions the contribution as replacing entropy-based confident-view selection, but the broader TTA landscape now contains several alternatives that are not simply entropy minimization. Even within the cited set, some methods use memory, cache, or more structured objectives. The paper’s narrative on **Pages 1-3** overstates the dichotomy “existing methods only use single-instance entropy, ours uses broader information.” This framing is too convenient. At minimum, the paper should discuss more carefully whether RTA is best understood as a learned confidence estimator for view ranking, rather than as a fundamentally different TTA paradigm.

7. **The “ceiling TTA” section is motivating but not scientifically deep, and the presentation of the tables is problematic.**  
   In **Tables 1 and 2** on **Page 4**, the HLCE rows appear malformed, e.g. entries like “75.415.1” and “50.218.7,” which seem to concatenate the score and improvement without formatting. This makes the tables harder to parse and raises concerns about proofreading. More importantly, the result itself, selecting views using ground-truth labels beats entropy, is expected. It motivates the search for a better proxy, but it does not itself validate that the proposed regressor captures the right signal. The paper leans quite heavily on this section rhetorically.

8. **The visualization evidence is weak relative to the claims made from it.**  
   The paper uses **Figure 2** to argue there is a “significant structural relationship” between logits and label cross-entropy loss. But t-SNE is a nonlinear projection optimized for local neighborhood structure; color gradients in 2D plots are suggestive at best and should not be treated as strong evidence of a learnable predictive relationship in the original high-dimensional space. Similarly, **Figure 3** only shows that some individual features have monotonic correlations with the target, which is not surprising. These figures are fine as intuition pumps, but the manuscript over-interprets them. A stronger analysis would report actual regression quality in the main paper, such as rank correlation between predicted and true LCE, top-$k$ overlap, or calibration of the ranking signal.

9. **The experiments do not isolate why RTA works.**  
   The main benchmark tables, especially **Table 3** and **Table 4**, show aggregate performance improvements, but there is little mechanistic validation in the main paper. For instance, there is no comparison against simpler learned confidence surrogates, such as using max logit, margin, temperature-scaled confidence, or a shallow logistic model trained to predict pseudo-label correctness. Without these controls, it is unclear whether the gain comes from the specific regression formulation, from using external offline data, or simply from learning a better monotonic ranking than entropy. This matters for novelty: if a simple confidence calibrator gives the same gains, the contribution becomes much narrower.

10. **The multi-label setting is insufficiently explained.**  
   The method is defined using single-label cross-entropy in **Equation (2)** and **Equation (4)**, yet the paper reports multi-label results in **Tables 5 and 6**. The main paper does not clearly explain how the regression target is defined in the multi-label case, whether it predicts binary cross-entropy aggregated over labels, ranking loss, or something else. Since ML-TTA is specifically a multi-label TTA baseline, this omission is important. A method paper should not require the reader to infer that the implementation must have been altered.

11. **The “negligible additional cost” claim is asserted rather than properly quantified in the main paper.**  
   The abstract and conclusion claim negligible additional cost, but the main paper does not provide runtime or memory comparisons against entropy-based methods. Since the method requires computing extra logits for the regression stage and invoking a learned model for every augmented view, the overhead may indeed be small, but that should be reported. This is especially relevant because some baselines also incur test-time optimization, while others do not.

12. **The gains, while real, are often modest against the strongest baselines, which weakens the contribution claim.**  
   In **Table 3**, for ViT-B/16 the improvement over Zero is small on some datasets, and in **Table 4** the average gain over BCA for ViT-B/16 is only \(68.70 - 68.59 = 0.11\). That does not invalidate the method, but it does matter for the paper’s significance. The text on **Pages 7-8** reads more triumphantly than the margins support. The contribution might be a useful tweak, but the paper currently sells it as a broad replacement for existing TTA methodology.

13. **Some claims are stated too categorically and are not backed by failure analysis.**  
   For example, the introduction on **Page 2** says cache or memory based methods “will immediately fail” once the distribution deviates significantly from historical distribution. That is simply too strong and not supported by evidence in this paper. Similar overstatements appear around “any target domain” and “arbitrary distributions.” This matters because overclaiming makes it harder to trust the paper’s carefulness elsewhere.

14. **Presentation quality is uneven despite the simple idea.**  
   Beyond the equation issues, there are many smaller but accumulating presentation problems: awkward phrasing, inconsistent dataset naming (e.g., IN-V vs ImageNet-V2, IN-K vs what appears elsewhere as IN-S/ImageNet-Sketch or ImageNet-K), and occasional typos such as “NeurlPS.” These may seem minor individually, but together they reduce confidence in the precision of the work.

## Questions
1. The main paper says the regression mapping is learned from logits and pseudo-label cross-entropy, but the cross-dataset setting in **Table 4** and the multi-label setting in **Tables 5-6** are not actually specified by the main equations. Please explain, in the main-paper formulation, exactly what the input feature vector to the regressor is for:
   - ImageNet-like benchmarks,
   - cross-domain datasets with different label sets,
   - multi-label datasets.
   If the intended mechanism is “fixed base-category logits for regression, target-category logits for classification,” that needs to be stated explicitly and consistently in the main method.

2. Can the authors report regression quality directly in the main paper? For example:
   - Pearson/Spearman correlation between predicted and true LCE,
   - top-$k$ overlap between predicted-low-loss and true-low-loss views,
   - Kendall-\(\tau\) of the ranking.
   This would make the central claim much more convincing than t-SNE alone.

3. How sensitive are results to the pseudo-label filtering threshold and regression-data source? The current implementation uses confidence \(\ge 0.8\) and 1,000 selected samples. A simple sensitivity table in the main paper would help establish robustness.

4. Please compare against simpler view-ranking baselines trained offline, such as:
   - maximum softmax probability,
   - logit margin,
   - temperature-scaled entropy,
   - a linear or logistic model predicting pseudo-label correctness from logits.
   If RTA still wins clearly, that would strengthen the claim that the gain is not just generic calibration.

5. For the multi-label experiments, what exact target does the regressor predict? If it is not the single-label CE from **Eq. (4)**, the paper should define the multi-label objective explicitly.

6. Can the authors provide test-time cost numbers, at least relative wall-clock or per-image latency against Zero / TDA / ML-TTA? The “negligible cost” claim would be much more credible with actual measurements.

7. In **Figure 4**, performance seems to saturate with more views. Does RTA remain better than entropy-based selection at low-view regimes such as \(N=8\) or \(N=16\), where TTA is more practical? A direct comparison curve would be useful.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the paper as presented. The work studies test-time adaptation for image classification benchmarks and does not appear to introduce unusual privacy, fairness, safety, or human-subject issues within the scope of the submission.

## Soundness Rating
2: fair. The empirical results suggest the method can help, but the core method specification is incomplete in the main paper, several equations/algorithms are inconsistent, and key claims are stronger than the evidence provided.

## Presentation Rating
2: fair. The paper is readable at a high level, and **Figure 1** is helpful, but notation errors, underspecified settings, malformed tables, and overclaiming substantially hurt clarity.

## Contribution Rating
2: fair. Learning an offline view-ranking score for CLIP TTA is a potentially useful idea, and the benchmark coverage is decent, but the conceptual novelty feels narrower than claimed and the gains over strongest baselines are not consistently strong enough to support the paper’s broader positioning.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a plausible and potentially useful idea here, and the benchmark results are encouraging. However, the paper in its current form overstates the conceptual contribution, leaves important parts of the method unspecified in the main text, and does not provide enough rigorous evidence that the proposed regression formulation, rather than a simpler learned confidence surrogate, is the real source of the gains. With a cleaner formulation, stronger ablations, and tighter claims, this could become a solid paper, but I do not think the current version quite clears the ICLR bar.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. I am familiar with CLIP-style test-time adaptation and checked the main methodological details and empirical evidence carefully.