---
job_id: 78f04f6b-8edc-4a65-a77c-0b63e202ef45
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: M14YpuTejd.pdf
paper: Understanding the Task and Data Misconceptions in Online Map Based Motion Prediction for Autonomous Driving and a Boundary-Free Baseline
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is about a benchmark, evaluation protocol, and baseline for motion prediction with online maps in autonomous driving, which fits ICLR topics on datasets/benchmarks, representation learning for vision/robotics, and applications to autonomy.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, related work, problem setup/method, experiments, quantitative results, and conclusion. While I have substantial concerns about novelty, methodology, and clarity, these are review-level issues rather than desk-reject-level omissions or fatal integrity flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies the recently introduced protocol of online-map-based motion prediction for autonomous driving, where an online mapping model is trained first and its outputs are then used by a downstream motion prediction model. The main contribution is OMMP-Bench, a revised benchmark/protocol that changes the data split, revises evaluation to focus on moving non-ego agents and distance-stratified results, and analyzes the effect of map range and map element types. The paper also proposes a simple “boundary-free” baseline that augments the motion predictor with image features from the online mapping model to alleviate the lack of map context for far-away agents.

## Strengths
The paper tackles a real and under-discussed evaluation issue in a new sub-area. The central observation in **Section 3.2** and **Figure 3** is sensible: in a two-stage pipeline, generating motion-training inputs using a map predictor on data it has already seen can create a distribution mismatch relative to validation-time map predictions. Even if one may debate how severe this is in practice, it is a worthwhile benchmarking concern.

I appreciated that the paper is not just proposing another downstream model, but trying to clean up task formulation and evaluation. The discussion around agent selection in **Section 3.4**, together with **Figure 8** and **Table 6**, makes a convincing case that evaluating only the ego vehicle, or averaging over many nearly static/easy cases, can hide important differences between methods. **Table 6** is especially useful here: the gap between “Static” and “Moving Non-Ego Far” is dramatic, so the paper is right that metric design strongly affects what conclusions one draws.

The benchmark-oriented analyses are reasonably broad. In particular, **Table 5** gives a useful ablation on map element types, and the result that centerlines are especially informative for motion prediction is plausible and practically relevant. Likewise, **Table 7** reports results across two map models and two motion models rather than a single cherry-picked stack.

The proposed image-feature baseline is simple and empirically helpful. In **Table 4** and **Table 7**, the “img” variant tends to improve especially for far non-ego agents, which matches the claimed motivation in **Section 3.3**. The visualization in **Figure 7** also communicates the intended idea clearly: unlike a fixed local map crop, image features can still provide some scene evidence for distant agents.

The paper is generally easy to follow at a high level. **Figure 1** provides a compact overview of the paper’s argument structure, and **Figure 4** helps visualize the spatial-overlap problem in the default split versus the proposed split.

## Weaknesses
1. **The paper’s main benchmark claim is plausible, but the empirical evidence does not cleanly isolate the claimed cause.**  
   The core claim in **Section 3.2** is that the default protocol creates a train-validation gap because the online map model predicts on its own training data when generating inputs for motion-model training. However, **Table 1** compares four split settings that simultaneously change multiple things: data partition, spatial overlap, training data size, and whether the map model and motion model see the same scenes. Because these factors are entangled, the table does not rigorously show that the observed gain is specifically due to “eliminating the train-val gap” rather than, for example, reducing overlap bias or changing the effective scene diversity.  
   This matters because the paper is framed as correcting a misconception in the field. For such a claim, the evidence should be more diagnostic. A cleaner test would measure online map quality on the sets used for motion training/validation and directly correlate that shift with downstream forecasting degradation, or compare motion training using cached predictions from held-out scenes versus in-sample scenes while keeping scene count fixed.

2. **There is an internal inconsistency about what is actually evaluated, which weakens the benchmark definition.**  
   In **Page 2, Section 1**, the paper states, “in OMMP-Bench, we propose to only evaluate non-ego agents.” But **Figure 8** and **Section 3.4** later say the proposed protocol evaluates “ego vehicle and other moving agents,” and **Table 7** explicitly includes an “Ego” block. These are not minor wording slips, because benchmark definitions need to be unambiguous.  
   The inconsistency affects interpretation of several claims. If ego is still reported, is it part of the official score or only auxiliary? If the benchmark focuses on moving non-ego agents, why is ego given equal presentation weight in the main result table? Right now the benchmark objective, primary metric, and reporting convention are not stated crisply enough.

3. **The mathematical description of the proposed baseline is underspecified, and Equation (1) is too vague to support reproducibility or technical scrutiny.**  
   In **Section 3.3**, the feature extraction pipeline is described as projecting each agent onto “an image feature” and then computing  
   \[
   \hat{A}_i = \operatorname{DeformAtt}(A_i, p_i, I_{T(i)}).
   \]
   But several key ingredients are missing or inconsistent:
   - The notation \(\{I_1,\dots,I_{N_c}\}\in\mathbb{R}^{H\times W}\) is dimensionally incomplete. Each image feature should have channel dimensions, typically \(I_c\in\mathbb{R}^{H\times W\times D}\) or \(I_c\in\mathbb{R}^{D\times H\times W}\).  
   - \(p_i\) is used in Equation (1) but not properly defined in the preceding paragraph.  
   - \(T(i)\) maps an agent to one image, but an agent may be visible in multiple cameras or none. The paper does not define how the camera is selected, how multi-view aggregation is handled, or what happens under occlusion/truncation.  
   - Deformable attention itself has sampling offsets, attention weights, and reference points; none are specified.  
   Since the proposed baseline is one of the paper’s headline contributions, this lack of formalization matters. At minimum the paper should specify the query/key/value tensors, the multi-camera selection or fusion rule, and the exact projection/sampling mechanism.

4. **Some empirical claims are stronger than what the reported numbers support.**  
   In **Section 3.3**, the paper argues that missing map elements for far-away agents is a major issue, and **Figure 6** qualitatively supports that point. However, the quantitative evidence in **Table 3** is much weaker than the rhetoric suggests: with ground-truth maps, extending from \(30\times 60\)m to \(100\times 100\)m changes minADE only from 0.6154 to 0.6003, and minFDE from 1.2382 to 1.2243. These are real but fairly small differences.  
   Similarly, **Table 4** shows the “img” baseline improves over prior online-map variants, but the gains are modest for the aggregate metric. This is not a problem by itself, but the text repeatedly uses language such as “severe” and “SOTA performance,” while the supporting numbers are relatively incremental and only shown on the proposed benchmark with limited baselines. The paper should calibrate its claims more carefully.

5. **The experimental scope is narrow for a paper whose main contribution is a benchmark/protocol.**  
   OMMP-Bench is evaluated only on nuScenes, which the authors justify in **Section 3.1** because it contains raw camera data, HD maps, and trajectories together. That is understandable, but then the generality claims should be toned down. More importantly, even within nuScenes the experiments cover only two map models, **MapTR** and **MapTRv2-CL**, and two motion predictors, **HiVT** and **DenseTNT**.  
   For a benchmark paper, one wants stronger evidence that the proposed conclusions are robust across modeling families. For example, the recommendation to use all map elements, or the conclusion that image features are better for far agents, may depend heavily on HiVT/DenseTNT design choices. The paper currently reads more like a case study on a narrow stack than a mature benchmark standard.

6. **The split construction is presented as carefully checked, but important implementation details are missing from the main paper.**  
   In **Section 4.1**, the new split is summarized by scene counts, and **Figure 4** visualizes overlap reduction. However, the actual construction procedure is not adequately specified in the main paper. What exact geometry criterion defines overlap? Is overlap measured by drivable area polygons, map elements, ego poses, or scene bounding boxes? Why is **5%** overlap between motion train and map train acceptable if the premise is to avoid leakage through static maps?  
   This matters because the split itself is the central artifact. If others cannot reconstruct it from the main text, the scientific value of the benchmark is reduced, even if code is planned for release.

7. **The comparison in Table 1 raises confounds that are not discussed.**  
   In **Table 1**, Split 1 (Ours) outperforms Split 3 (Default), which supports the authors’ narrative. But Split 4, where nuScenes train is split into two disjoint 50% subsets, also performs similarly to Split 1 and even slightly better on some metrics. This suggests that simply enforcing disjointness between map-training and motion-training subsets inside the original protocol may already address much of the issue, without requiring the full benchmark redesign.  
   The paper does not engage with this possibility. That is important because it weakens the argument that OMMP-Bench, as a whole, is the necessary fix rather than one possible implementation among several.

8. **The benchmark’s “all map elements” recommendation may not be a fair protocol choice when comparing upstream map models with different output vocabularies.**  
   In **Section 3.5** and **Table 5**, the paper concludes that all available map element types should always be fed into the motion predictor. That is fine for best-case performance, but as a benchmark rule it may systematically favor map models with richer annotation/output spaces, such as ones predicting centerlines, over models designed around a different representation.  
   This matters because a benchmark should separate “better map representation” from “more supervision / more semantic channels.” If a model does not output centerlines by design, it may be penalized for formulation choice rather than actual downstream utility. The paper should discuss whether this is intended and whether comparisons are still apples-to-apples.

9. **Several figures are helpful conceptually but do not fully support the strength of the claims.**  
   **Figure 6** is visually appealing, but it is anecdotal and does not establish the broader conclusion that long-range online maps are not helpful. One can find many scenario-dependent examples in trajectory prediction. Since the quantitative evidence in **Table 3** is relatively small, the figure risks overstating the point.  
   Likewise, **Figure 4** effectively visualizes overlap, but because it is shown only for a few regions, it does not fully replace a formal definition of overlap or a complete statistical characterization of the split.

10. **Presentation quality is uneven, with enough ambiguity and language issues to hinder careful reading.**  
   There are repeated grammatical problems and notation issues, for example “We donate the image features” in **Section 3.3**, “could significantly degenerate” in **Page 2**, and some confusing references such as “shown in Fig. 3 (Upper)” at the end of **Section 3.2**, where the intended lower/proposed protocol seems meant. These are individually minor, but there are many of them. For a benchmark paper, where precise protocol description is essential, this level of imprecision becomes more consequential.

## Questions
1. **Can the authors disentangle the source of the gain in Table 1?**  
   Please provide a more controlled analysis where the number of scenes and disjointness conditions are held constant as much as possible, and where the only manipulated factor is whether motion-model training uses online maps predicted on scenes seen versus unseen by the map model. A direct measurement of map-quality shift between motion-train and motion-val under each split would substantially strengthen the paper.

2. **What is the official benchmark metric and reporting protocol?**  
   The main text alternates between “only non-ego,” “all moving vehicles,” and tables that still report ego separately. Please clarify: what exact metric should future papers optimize and compare on? Is “Moving Non-Ego” the primary score, or are ego and close/far subgroups all official leaderboard metrics?

3. **Please fully specify the image-feature baseline.**  
   I would like a precise definition of the tensors and operations in Equation (1): dimensions of \(I_c\), definition of \(p_i\), whether agents attend to one or multiple cameras, how \(T(i)\) is chosen, what happens when an agent projects outside the image or into occluded regions, and the number of deformable attention sampling points/heads. This clarification could materially increase my confidence in the method.

4. **How sensitive are the conclusions to the choice of motion predictor?**  
   The benchmark conclusions would be more convincing if the authors could show, for example, that the relative benefits of the revised split and the “img” baseline hold for a more diverse set of forecasting architectures, especially more recent transformer-based models beyond HiVT and DenseTNT.

5. **Can the authors quantify the overlap criterion used to build Figure 4?**  
   A formal overlap definition and a table summarizing overlap statistics across all regions would help. In particular, why is \(5\%\) overlap acceptable, and how much would the results change if one enforced a stricter threshold?

6. **On Table 5, is the “all map elements” rule intended as a benchmark requirement or just an empirical recommendation?**  
   If it is a requirement, how should one compare against map models whose output space does not contain centerlines or other richer semantic layers? Clarifying this is important for fairness.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper content. The work is a benchmark and model evaluation study for autonomous driving perception/prediction, and the paper does not introduce obvious new issues around privacy, bias, or deployment beyond standard dataset-use considerations.

## Soundness Rating
2: fair. The paper’s central concerns are plausible and some experiments support them, but the evidence is not clean enough to fully justify several benchmark-level claims, and the proposed method is mathematically underspecified.

## Presentation Rating
2: fair. The high-level story is understandable and some figures are useful, but there are notable inconsistencies, underspecified definitions, and enough writing/notation issues to hurt precision.

## Contribution Rating
2: fair. The benchmark motivation is relevant and potentially useful, but the contribution feels more like a partially validated protocol adjustment plus a simple baseline than a fully convincing benchmark paper for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper raises worthwhile concerns and has some genuinely useful benchmark insights, especially about agent selection and range-stratified evaluation. However, the central benchmark claims are not isolated as rigorously as they need to be, the baseline is underspecified, and the protocol definition still has important ambiguities. I see value here, but in its current form I do not think the paper clears the bar for a main-track ICLR acceptance.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with motion prediction / autonomous driving benchmark design and checked the technical details carefully, but a few implementation details are too underspecified to verify completely.