---
job_id: 92fe7579-e07e-4421-9429-d6ae24436221
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 9X2NfyZpR2.pdf
paper: Long-Term Action Anticipation via Transcript-Based Supervision
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies weakly supervised sequence modeling and representation learning for long-term action anticipation in video, with a transformer-based architecture and structured losses.

## Minimum Quality
Pass ✅. The submission contains the expected scientific sections, including abstract, introduction, related work, methodology, experiments, quantitative/qualitative results, and conclusion. While there are substantial clarity and technical specification issues, the paper is still a complete research manuscript rather than something that warrants desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions aimed at automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes TbLTA, a weakly supervised framework for dense long-term action anticipation trained only with action transcripts rather than frame-level action boundaries. The method combines a transformer encoder-decoder, a transcript-to-video temporal alignment module that produces pseudo-labels, transcript-conditioned cross-modal attention, a CTC-based segmentation loss, and a CRF plus duration loss for anticipation. Experiments on Breakfast, 50Salads, and EGTEA aim to show that transcript-only supervision can be competitive with fully supervised long-term anticipation methods.

## Strengths
The paper tackles a meaningful problem. Reducing the annotation burden for dense long-term action anticipation is worthwhile, and moving from dense frame labels to transcripts is a sensible weak-supervision direction. If this setup can be made reliable, it would indeed improve scalability for procedural-video understanding.

The overall pipeline is easy to grasp at a high level. In particular, **Figure 1** gives a concise overview of the claimed contribution, namely that transcripts are used both as supervision through alignment-generated pseudo-labels and as semantic context through cross-modal attention. **Figure 2** is also helpful in showing the intended training-vs-inference split, the role of the temporal alignment block, and how TAS/LTA supervision are connected.

The empirical results are at least promising on some benchmarks. In **Table 1**, the deterministic TbLTA result on Breakfast is surprisingly strong, especially for the 30% observation setting, where the reported average appears to exceed the listed supervised baselines. Even if I have reservations about how to interpret some rows in the table, the results suggest that transcript supervision is not obviously hopeless, which is an encouraging finding for the community.

The ablations do indicate that some of the proposed components matter. In **Table 4**, removing the CRF clearly hurts long-horizon performance, especially on 50Salads, which supports the authors’ claim that sequence-level smoothing is useful for dense anticipation. Likewise, the gap between TbLTA and “w/o cross-att” on Breakfast is fairly noticeable, which suggests the transcript-conditioned fusion is doing more than cosmetic work.

The qualitative examples in **Figure 3** are useful, even if limited. They show that the model can produce reasonably coherent predicted action blocks rather than completely chaotic futures, and they also make visible one of the paper’s key limitations, namely duration prediction errors. I appreciate that the visualizations are aligned with the stated task rather than showing only classification scores.

## Weaknesses
I have substantial concerns about the technical specification and empirical presentation. The high-level idea is interesting, but the current paper leaves too many core pieces underspecified or internally inconsistent for me to be confident in the claimed contribution.

1. **The method is assembled from many existing ingredients, and the paper does not convincingly isolate what is actually new beyond the application setting.**  
   The alignment module is adopted from ATBA (**Section 3.1, Page 5**), the CTC supervision is standard (**Section 3.2.2, Equation 4, Page 6**), the decoder is adapted from prior LTA work (**Page 5**), and the CRF is explicitly inspired by TCCA (**Page 5**). In principle, a careful recombination for a new problem can still be publishable, but then the burden is on the paper to clearly explain what the new technical contribution is. Here, the novelty claim mostly reads as “first transcript-only LTA pipeline” rather than a distinct modeling advance. That makes the evaluation and technical clarity even more important, and unfortunately both are shaky.

2. **The mathematical definition of the cross-modal attention block is unclear and appears dimensionally inconsistent.**  
   In **Equation 1 (Page 5)**, the symbol \(A\) is first introduced as transcript embeddings \(A \in \mathbb{R}^{N \times d}\), then overwritten by the output of attention through  
   \[
   A \leftarrow \mathrm{softmax}\left(\frac{AW_Q(\hat{X}W_K)^\top}{\sqrt d} + \log M\right)\hat{X}W_V.
   \]
   This in-place redefinition is already confusing. Then in **Equation 2**,  
   \[
   \hat{X} \leftarrow \hat{X} + \left(M^\top \odot \sigma(AW_g)\right)A,
   \]
   the dimensions do not obviously line up. If \(A\) is now the attended text representation, then \(\sigma(AW_g)\) has shape \(N \times 1\), \(M^\top\) has shape \(T \times N\), and the Hadamard product requires broadcasting that is not specified. The final multiplication by \(A\) is also ambiguous because it depends on whether \(A\) is \(N \times d\) before or after the previous reassignment. This is not a cosmetic notation complaint, it makes it hard to know what is actually implemented. The authors should rewrite this block with distinct symbols for text tokens, attention weights, and fused outputs, and explicitly state tensor shapes.

3. **The binary mask \(M\) used in the cross-modal attention is underdefined, and that matters because it is central to the proposed multimodal design.**  
   The paper says on **Page 5** that \(M \in \{0,1\}^{N \times T}\) “restricts each action \(a_i\) to a temporal neighborhood around its predicted occurrence,” but the neighborhood construction is never specified in the main paper. How wide is the neighborhood, how is it derived from soft pseudo-labels, what happens for repeated transcript labels, and how is \(\log M\) handled numerically when \(M=0\)? Since **Equation 1** literally adds \(\log M\), zero entries correspond to \(-\infty\), which is fine in principle, but only if the masking policy is precisely defined. This is a core part of the method, not an implementation footnote.

4. **The CTC formulation is internally inconsistent with the rest of the paper.**  
   In **Section 3.2.2 (Page 6)**, the text says CTC provides supervision “for both the TAS head and the anticipation decoder,” but immediately after that the loss is defined only as \(\mathcal{L}_{TAS} = \gamma_2 \mathcal{L}_{CTC}\). The anticipation decoder instead seems to be supervised by the CRF and duration losses in **Section 3.2.3**. Also, the paper defines predicted action probabilities as \(\pi = [\pi_1,\dots,\pi_{\alpha T}]\), suggesting only the observed portion, but in **Equation 4** the path probability is written as a product from \(t=1\) to \(T\). This is not a minor typo because the paper repeatedly emphasizes that full-video segmentation is used during training, including in **Figure 2** and on **Page 4**. It is therefore unclear whether CTC is applied to the observed interval, the full video, or something else.

5. **The anticipation supervision is conceptually muddled under weak supervision.**  
   In **Equations 5 and 6 (Page 6)**, the CRF objective is written with a target “ground-truth anticipation sequence” \(\mathcal{Y}_{\text{LTA}}\). But by construction, the paper only has access to the full transcript, not the observed/future split, and the boundary index \(k^*\) is explicitly unknown on **Page 4**. The paper says ATBA partitions the transcript into \(\mathcal{Y}_{\text{obs}}\) and \(\mathcal{Y}_{\text{future}}\) (**Page 5**), but the mechanism for obtaining a stable future target sequence for CRF training is not explained. This is a key issue because the anticipation loss depends on a sequence target that is itself latent and noisy. The paper should spell out whether \(\mathcal{Y}_{\text{LTA}}\) is derived from pseudo-label collapse, transcript truncation, or some other heuristic. Right now the objective reads as if a ground-truth future transcript exists, which contradicts the weakly supervised setup.

6. **The duration loss in Equation 7 is not well specified, and its target appears self-referential.**  
   On **Page 7**, the model stores class-wise duration estimates \(\hat d \in \mathbb{R}^{|C|}\) from the segmentation head’s own predictions, then supervises predicted durations with
   \[
   \mathcal{L}_{\text{dur}} = \frac{1}{T_{\text{pred}}}\sum_{i=1}^{T_{\text{pred}}} (\hat{\delta}_i - \hat{d}_{y_i})^2.
   \]
   Several problems arise. First, \(\hat{\delta}_i\) is described as a “per-segment” duration, but the summation runs over \(T_{\text{pred}}\), which elsewhere denotes future frames, not future segments. Second, \(y_i\) is undefined here, is it a frame label, a decoder token, or a pseudo-label segment class? Third, the target \(\hat d_{y_i}\) comes from the model’s own running prior rather than any ground-truth or externally validated proxy. This may be a useful heuristic, but then it should be presented and justified as such, not as a clean self-supervised duration objective. The small average gain on 50Salads in **Table 4** also suggests this module may be much weaker than the prose implies.

7. **The experimental tables are difficult to interpret and contain apparent formatting or labeling errors.**  
   **Table 1 (Page 8)** is especially problematic. Under 50Salads, “Ours (TbLTA) - Top1” appears twice, with two very different performance profiles. The surrounding text says stochastic results are also reported, but the table does not clearly label which row is deterministic and which is stochastic, beyond the footnote “* means stochastic protocol,” which is itself not mapped cleanly to the duplicated rows. Similar issues appear for Breakfast. This matters because the strongest claims in the paper, such as being competitive with or better than supervised methods, depend on a precise reading of this table. At minimum, the rows need to be relabeled and separated unambiguously.

8. **The evidence for the headline claim, “competitive with fully supervised methods,” is thinner than the writing suggests.**  
   The paper highlights that TbLTA is sometimes competitive with supervised approaches, especially on Breakfast (**Section 4.2, Page 8**). That is true in some reported settings, but the story is much less convincing on 50Salads and EGTEA. In **Table 2 (Page 9)**, TbLTA is clearly below the supervised baselines overall and on frequent classes, only improving on rare classes. On 50Salads in **Table 1**, the deterministic results remain substantially below the best supervised numbers. So the empirical picture is mixed, not uniformly strong. I would encourage the authors to tone down the rhetoric and separate “promising proof of concept” from “competitive replacement.”

9. **The EGTEA evaluation is weakly aligned with the paper’s stated task.**  
   The paper frames the contribution as dense long-term action anticipation, forecasting future actions and durations at frame level. Yet for EGTEA, **Section 4.1 (Page 7)** switches to verb mAP under a multi-label classification protocol, and **Table 2** reports only “All / Freq / Rare” verb scores. This is a rather different target from dense frame-wise anticipation. I understand that benchmark conventions differ, but then the paper should be explicit that this experiment is only a partial proxy and not direct evidence for dense anticipation quality.

10. **Ablation evidence is useful but not fully persuasive because the components interact through a complex multi-stage pipeline.**  
   The method uses progressive training, pseudo-label generation, cross-modal attention, CTC, CRF, and duration regularization (**Page 7**). In that setting, small differences in **Tables 3 and 4 (Page 9)** are hard to interpret causally. For example, some ablation changes are modest, and the paper does not report variance across runs, sensitivity to pseudo-label quality, or stability under different initialization. The large pipeline complexity raises a real concern: are the gains due to the proposed ideas, or due to a particular training recipe that may be fragile?

11. **The qualitative evidence partly undermines the strongest claims.**  
   The paper says in **Section 4.4 (Page 9)** that degradation in the future interval remains relatively small. I do not think **Figure 3** fully supports that statement. In the Breakfast example, the main sequence is broadly captured, but duration mismatch is visible. In the 50Salads example, there are several noticeable boundary and duration deviations, and some action ordering appears compressed or shifted. I do not object to including imperfect examples, in fact that is better than cherry-picking, but then the discussion should be more measured.

12. **Presentation quality is below ICLR expectations for a method-heavy paper.**  
   Beyond the technical ambiguities, there are many notation and writing issues: \(\mathcal{Y}\) and \(\mathcal{V}\) are both used for transcripts on **Page 4**; \(T_{\text{pod}}\) in **Equations 5 and 6 (Page 6)** appears to be a typo for \(T_{\text{pred}}\); “does not needs” in the conclusion (**Page 9**) is ungrammatical; and the tables/ablation labels contain visible inconsistencies such as “w/o chc loss” and “w cross-att samples” in **Table 3 (Page 9)**. For a complex weak-supervision paper, these issues materially hinder confidence because the reader already has to infer many missing implementation details.

## Questions
1. **Can the authors precisely define the training target used in the CRF loss?**  
   In **Equations 5 and 6**, what exactly is \(\mathcal{Y}_{\text{LTA}}\) under transcript-only supervision? Is it obtained by splitting the transcript using an estimated \(k^*\), by collapsing frame-wise pseudo-labels, or by another heuristic? A clear answer here would significantly improve my confidence.

2. **Please rewrite the cross-modal attention equations with unambiguous tensor symbols and shapes.**  
   In particular, clarify the dimensions in **Equations 1 and 2**, how the binary mask \(M\) is constructed from pseudo-labels, and how repeated transcript actions are handled. Right now this block is too opaque.

3. **Where is CTC actually applied, observed interval or full video?**  
   **Equation 4** and the surrounding text are inconsistent. Please state the exact sequence length used for CTC, the transcript provided to CTC, and whether the anticipation decoder receives any direct CTC-style supervision or not.

4. **Can the authors clean up and relabel Table 1?**  
   The duplicated “Top1” rows are confusing. Please identify clearly which rows correspond to deterministic vs stochastic evaluation and whether the “Mean” row is the average over stochastic samples or something else.

5. **How sensitive is the method to pseudo-label quality and initialization?**  
   Since the pipeline depends heavily on the temporal alignment stage and progressive training, I would like to know whether performance is stable across different seeds or alignment warm starts. Even a brief summary of variance would help.

6. **Can the authors justify the duration loss more carefully?**  
   What is the exact indexing of \(\hat{\delta}_i\) and \(y_i\) in **Equation 7**, and why is a class-level running prior an appropriate target for per-segment duration prediction? Some additional empirical evidence would be useful because the current formulation looks heuristic.

7. **For EGTEA, why is verb mAP an adequate evaluation for a paper on dense anticipation?**  
   I do not necessarily object to including it, but I would like the authors to clarify how this experiment should be interpreted relative to the main dense frame-wise task.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper. The work uses standard benchmark datasets and focuses on weakly supervised video understanding. I do not see a specific issue requiring formal ethics review based on the information provided in the main paper.

## Soundness Rating
2: fair. The overall idea is plausible and some empirical evidence is encouraging, but several core objectives and equations are underspecified or internally inconsistent, which weakens confidence in the technical claims.

## Presentation Rating
2: fair. The paper is readable at a high level, and Figures 1 and 2 help, but the notation, equations, tables, and some textual descriptions are not clean enough for a method this intricate.

## Contribution Rating
2: fair. The transcript-only supervision setting for dense LTA is interesting and worth exploring, but the technical contribution appears incremental and the current evidence does not fully substantiate the stronger claims.

## Overall Rating
2: Reject, not good enough. The problem is worthwhile and the empirical direction is interesting, but the paper in its current form is too under-specified mathematically, too inconsistent in presentation, and too ambiguous in core supervision details for me to recommend acceptance.

## Reviewer Confidence
4: confident. I am confident in the main concerns above, especially regarding weakly supervised sequence modeling, structured objectives, and the internal consistency of the methodology and experiments.