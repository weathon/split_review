---
job_id: 7eb37552-9f6e-4a9b-9676-653f7498b8c4
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: CrCPeM5fRB.pdf
paper: SDSC: A Structure-Aware Metric for Semantic Signal Representation Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly about self-supervised representation learning for time series, with a proposed reconstruction objective and empirical evaluation on downstream forecasting and classification.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion; while I have substantial concerns about novelty, mathematical framing, and empirical support, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes the Signal Dice Similarity Coefficient (SDSC), a reconstruction objective for time-series self-supervised learning that measures local structural overlap via sign agreement and magnitude overlap, instead of relying on pointwise distance such as MSE. The method is integrated into the reconstruction branch of SimMTM while keeping the contrastive branch fixed, and the paper evaluates SDSC and a hybrid SDSC+MSE loss on pre-training, forecasting, and classification tasks.

## Strengths
The paper has a reasonably clear central idea: isolate the effect of the reconstruction loss by changing only the SimMTM reconstruction branch and keeping the contrastive objective fixed. That controlled setup is a sensible experimental design choice for answering the paper’s stated question.

The proposed objective is computationally lightweight. As defined in **Equation (5)**, SDSC is a simple pointwise computation with linear complexity in sequence length, and this is a practical advantage over alignment-based losses such as SoftDTW. The paper also does a decent job explaining the intuition behind the construction from Dice overlap to signed signal overlap.

The qualitative examples in **Figure 1** are useful for conveying the authors’ motivation. In particular, **Figure 1(c)**, together with **Table 1**, makes the point that two signals can have the same MSE while looking structurally very different. Even though I think some of the rhetoric around MSE is overstated, these examples do help readers understand what type of discrepancy SDSC is designed to emphasize.

Similarly, **Figure 2** is helpful for presentation. It concretely shows how the continuous overlap intuition is turned into a discrete summation, and that makes **Equations (4) and (5)** easier to parse than they would be from text alone.

There is some empirical signal, especially in frozen in-domain classification. In **Table 5**, SDSC improves the averaged in-domain frozen-encoder score from 69.15 to 70.34, and the hybrid loss is similarly competitive at 70.26. This is not a huge jump, but it is at least aligned with the paper’s claim that emphasizing local structural fidelity can help when the encoder is used as a fixed representation extractor.

The paper is also commendably explicit that SDSC is not a global alignment method and does not address temporal shifts or warping. That limitation is stated in the main paper rather than hidden away.

## Weaknesses
1. **The contribution is more incremental than the paper presents, and the terminology is overstated.**  
   At a high level, the method is a Dice-style overlap adapted to signed continuous signals via pointwise gating and minimum magnitude overlap, see **Equations (2) to (5)** on **Page 5**. That is a reasonable engineering idea, but the paper repeatedly frames SDSC as a “metric” and even says it is “theoretically sound” because it is bounded. Boundedness alone does not make something a metric in the mathematical sense. The paper proves only \(0 \leq \mathrm{SDSC} \leq 1\) in **Lemma 1** on **Page 26**; it does not establish symmetry explicitly, identity of indiscernibles under the smoothed version, or triangle inequality. In fact, what is defined is much closer to a similarity coefficient than a metric. This matters because the paper’s title and positioning lean heavily on the word “metric,” and that wording gives the contribution a stronger theoretical flavor than what is actually supported.

2. **Several conceptual claims about MSE are exaggerated or imprecise.**  
   The introduction states that distance-based metrics are “invariant to waveform polarity” and may assign low error to semantically reversed signals. That is not generally true. For a sign-inverted signal \(R=-E\), the MSE becomes \(\frac{1}{T}\sum_t (E_t+E_t)^2 = \frac{4}{T}\sum_t E_t^2\), which is typically large, not polarity-invariant. The paper’s own example in **Figure 1(a)** and **Table 1** achieves low MSE for inversion only under “low-amplitude conditions,” which is a very special setup. Likewise, the claim in **Figure 1(c)** and the surrounding text that a zero signal and a \(2\times\)-scaled waveform can have identical MSE is true for the specific toy waveform shown, not a general pathology of MSE. This matters because the motivation section turns a few carefully chosen examples into sweeping statements about MSE, and that weakens the scientific positioning.

3. **The mathematical formulation is under-specified for the actual multivariate SSL setting used in experiments.**  
   The main definition in **Equations (4) and (5)** is written for two scalar functions \(E(t)\) and \(R(t)\). But SimMTM operates on multivariate time series, and the paper does not clearly state how SDSC is aggregated across channels. Is the loss computed per channel and averaged, summed jointly over time and variables, or applied after flattening? This is not a cosmetic issue. For multichannel signals, different aggregation choices can materially change optimization behavior. Related notation is also inconsistent: **Equation (6)** writes \(\mathcal{L}_{sdsc}=1-SDSC(E(S),R(S))\), while earlier notation uses \(E(t)\), \(R(t)\), and \(s \in S\). The denominator adds \(\epsilon\) only in the discrete approximation in **Equation (5)**, not in the continuous definition in **Equation (4)**, and the paper assumes uniform sampling and unit-width rectangles in **Figure 2** without discussing irregular sampling. These gaps make reproduction and interpretation harder than they should be.

4. **The optimization story is shakier than the paper admits.**  
   The core gating term is \(H(E(t)R(t))\) in **Equation (4)**, replaced by a sigmoid in **Equation (7)**. However, the main paper does not analyze the gradient behavior in any serious way. The appendix is revealing here: in **Table 8(a)**, the SDSC gradient norm is exactly 0.0000 for the “Inverted” and “Zero” examples. That means the unsmoothed objective has completely dead regions for some of the very failure cases used to motivate the method. The sigmoid relaxation helps, but the main paper does not derive gradients, discuss calibration of \(\alpha\), or explain how optimization behaves near sign changes where \(E(s)R(s)\approx 0\). Since the method is proposed as a training loss, this is not a side detail. A loss with broad flat regions can optimize poorly even if it is intuitively appealing as an evaluation score.

5. **The empirical gains on the main downstream tasks are very small, and the claims should be narrower.**  
   The strongest practical claim is that SDSC improves representation quality. But for forecasting, the averaged fine-tuning results in **Table 4** are essentially tied: MSE gives 0.295/0.316, SDSC gives 0.294/0.316, and Hybrid gives 0.294/0.316. Those are vanishingly small differences. On the full results in **Table 19**, the pattern is the same, some tiny wins, some tiny losses. For fine-tuned classification in **Table 6**, SDSC is not consistently better and is often slightly worse than MSE or PCC on the averages. The paper therefore has at best a conditional empirical message: SDSC can help in some frozen, in-domain settings, but there is little evidence for a broad downstream advantage. The conclusion on **Page 10** goes beyond what the tables really support.

6. **The most favorable results are in a narrow slice of the evaluation, and cross-domain evidence is weak or negative.**  
   The headline positive result is frozen in-domain classification in **Table 5**, where SDSC beats MSE on the average by about 1.2 points. But in the same table, SDSC is slightly worse than MSE in cross-domain average performance, 47.28 vs 47.63. In **Table 6**, after end-to-end fine-tuning, SDSC again does not improve the average over MSE. This is important because a representation-learning paper should ideally show that the learned features transfer robustly. Here, the improvements appear fragile and concentrated in one evaluation mode.

7. **The analysis around Figure 3 and Table 3 is too anecdotal to support the stronger interpretive claims.**  
   **Figure 3(a)** reports a Pearson correlation of \(-0.324\) between MSE and SDSC for ETTh1 under MSE-based pre-training, and **Figure 3(b,c)** compares SDSC distributions at fixed MSE \(1.5 \pm \epsilon\). But \(\epsilon\) is not specified in the main paper, the analysis is on a single dataset, and the differences in **Table 3** are small, standard deviation 0.0280 vs 0.0249 and IQR 0.0418 vs 0.0384. Without uncertainty estimates or replication across datasets, this reads more like an illustrative observation than strong evidence that MSE-based SSL is “unreliable” while SDSC is “consistent.” The paper should tone this down.

8. **Baseline selection and fairness are not entirely convincing.**  
   The paper compares against MSE, SoftDTW, PCC, and SI-SNR, but some of these baselines are obviously unhappy in this setting, and the paper acknowledges that SI-SNR uses a different scale and sometimes fails to converge, see **Table 2** and the note below it on **Page 7**. That makes those numbers hard to interpret. More importantly, the paper discusses DILATE in **Section 2.1** and again in the conclusion as a stronger alignment-based alternative in some settings, but does not include it experimentally. Since one of the paper’s central themes is reconstruction objectives beyond MSE, omitting one of the most directly relevant alternatives weakens the empirical positioning.

9. **The “fair comparison” claim is not fully airtight.**  
   The paper says on **Pages 2, 6, and 7** that keeping InfoNCE unchanged means downstream differences “should be attributed to the reconstruction objective.” That is directionally true, but not fully rigorous. The hybrid loss in **Equation (8)** introduces trainable uncertainty-based weighting parameters, which changes optimization dynamics beyond a plain swap of one fixed reconstruction loss for another. In addition, the paper states in **Section 4.2** that evaluation is conducted at the “best epoch for both pre-training and fine-tuning,” but does not clearly specify the validation protocol used to select those epochs. This does not look like a fatal flaw, but the phrasing is stronger than warranted.

10. **Presentation is understandable overall, but the paper has repeated wording issues and some internal inconsistency.**  
   There are many repeated statements that the setup “isolates” the reconstruction effect, and several passages are more rhetorical than precise. Some notation is awkward, for example \(\mathcal{L}_{si,snr}\) in **Equation (9)**, and some language is misleading, especially around what is and is not captured by SDSC. The title and abstract suggest a fairly broad structural notion, but the body later narrows it to local sign agreement plus magnitude overlap. That narrower claim is actually more defensible, and the paper would benefit from centering it from the start.

## Questions
1. **How exactly is SDSC computed for multivariate time series in SimMTM?**  
   Please specify the tensor-level implementation. Is SDSC computed independently per channel and then averaged, or over all channels jointly? This should be stated explicitly in the main paper, not left implicit.

2. **What is the precise model-selection protocol for the “best epoch” statements in Section 4?**  
   Was pre-training epoch selected using validation reconstruction loss, downstream validation performance, or something else? The answer matters because the paper repeatedly claims that the comparison isolates the reconstruction objective.

3. **Can the authors provide multi-seed statistics for the main downstream tables, especially Tables 4, 5, and 6?**  
   Given how small many of the reported differences are, confidence intervals or mean ± std over several runs would materially increase my confidence.

4. **Can the authors clarify whether SDSC is intended as an evaluation score, a training loss, or both?**  
   If both, please explain how you view the trade-off between its intuitive appeal as a bounded structural similarity and the optimization issues implied by the sign-gating in Equation (4) and the gradient behavior shown in Table 8.

5. **Can the authors sharpen the scope of their claims?**  
   Based on Tables 5 and 6, the strongest evidence seems to be frozen in-domain classification, while cross-domain transfer and fine-tuning do not show a consistent advantage. A more precise framing around where SDSC helps would make the paper more convincing.

6. **Why was DILATE not included experimentally, despite being discussed as a relevant structure-aware baseline in Section 2.1?**  
   Even a limited comparison on one forecasting dataset would strengthen the paper’s empirical positioning.

7. **In Figure 3, what value of \(\epsilon\) was used for the fixed-MSE slice, and how sensitive are Table 3’s concentration results to that choice?**  
   Right now the figure is suggestive, but the analysis is too under-specified to carry much weight.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are apparent from the main paper. The work proposes a reconstruction objective for time-series SSL and evaluates it on standard benchmarks. The paper does mention physiological signals such as EEG/ECG as motivating domains, but there is no deployment claim or new human-subjects component that would require ethics escalation based on the main text.

## Soundness Rating
2: fair. The core method is simple and mostly coherent, but the mathematical framing is loose, the optimization story is underdeveloped, and the empirical evidence only weakly supports the broader claims.

## Presentation Rating
2: fair. The paper is readable and the main idea comes across, helped by Figure 1, Figure 2, and the tables, but the exposition overstates some claims, uses inconsistent terminology, and leaves important implementation details ambiguous.

## Contribution Rating
2: fair. There is a plausible and lightweight idea here, and the frozen in-domain classification results are mildly encouraging, but the contribution feels incremental and the downstream gains are too limited and inconsistent for a stronger rating.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My current view is negative, mainly because the paper overclaims relative to what it actually demonstrates. The idea is simple and potentially useful, but the novelty is modest, the mathematical positioning is not tight enough, and the empirical case is narrow, with tiny gains on forecasting and mixed transfer results. If the rebuttal can convincingly address the multivariate formulation, validation protocol, and especially provide stronger uncertainty-aware evidence that the observed gains are real rather than noise, I could imagine revising upward, but in its current form it falls short of ICLR standards.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation detail not made explicit in the main paper.