# Harnessing Input-adaptive Inference for Efficient Vision-and-Language Navigation

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
An emerging paradigm in vision-and-language navigation (VLN) is the use of history-aware multi-modal transformer models. Given a language instruction, these models take observation and history as input and predict the most appropriate action for an agent. While employing these models has significantly improved performance, the scale of these models can be a bottleneck in practical settings where computational resources are limited (e.g., in robots). In this work, we present a novel input-adaptive navigation method for efficient VLN. We first characterize the overthinking problem in VLN and show that none of the existing input-adaptive mechanisms successfully reduce overthinking without causing significant performance degradation. Our method addresses this problem by developing three adaptive algorithms deployed at different levels: (1) We develop an adaptive approach that improves spatial efficiency; we only process a subset of panoramic views at each observation of an agent. (2) We also achieve model-level efficiency by developing adaptive thresholding for the early-exit method we employ, based on the importance of each view in navigation. (3) To achieve temporal efficiency, we design a caching mechanism to avoid processing views that an agent has seen before. In evaluations with six VLN benchmark tasks, we demonstrate over a 2$\times$ reduction in computation across two off-the-shelf VLN agents.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work proposes a mixture of techniques leveraging spatial significance and temporal continuity as well as an adaptation of the MuE early exit protocol to alleviate the compute burden of VLN models. The authors show an average reduction by over half of GFLOPs to run the models with drops in success rate performance within 10% of the full model.

### Strengths
The paper is well motivated and shows how providing models with better data design, i.e. doing some signal extraction amongst the input noise, can substantially help model efficiency.

The main strength of the work is its clarity in the design of solutions. 
- Each of the spatial consideration, temporal hashing and adaptive early exit thresholding are intuitive and simple.
- The combination of the three ingredients is straightforward (for the most part see questions) 

The paper's numerical results are comprehensive and consider a variety of relevant benchmarks, showing the merit of the technique. The numerical results obtained are good and proving not only the soundness but also the impact of adaptive input data curation.

### Weaknesses
The paper tackles a specific setting, that of VLNs, but more specifically a data pipeline that consists of panorama views (36 precisely) and focuses on simple ways to filter out unnecessary noise in the data and reduce superfluous ViT computations in the image encoder.
- This choice of problem is in my view a bit restrictive, although VLNs are popular models and have attracted a lot of work and attention, they are constantly evolving. Hence focusing on the 36 image panorama as well limiting the application to ViT encoders leaves out room for applications to variants (depth or multimodal sensing, state space models etc...)
- Given the limited applicability context, one would expect a highly specified solution, yet the protocol proposed is quite simple and feels like it could be refined further (additional work on customizing the adaptive MuE perhaps, more specific selection of neighboring views with higher useful information content and so on)

In other words, the setting is not large enough for simple techniques to prove their merit in terms of universality and practicality. Also, the techniques are not tailored enough to the specific setting to maximize the potential gains of the approach and achieve maximal efficiency and performance.

It is unclear what the significance of the result is in practice. The authors express their hope that their "results will inspire future research on developing efficient navigation methods and their deployment in real-world VLN settings."
The gain of a factor of 2 in GFLOPs is not a gain of orders of magnitude and some VLN models are already running on board larger hardware in the real world. The work does not reduce the size of the models (compression) or provide gains large enough to enable such large models to run on edge devices.

Along these lines the paper would be much improved if the authors showed real-world experiments, where in practice the 2x gain offers behavior gains that are desirable from the human user's point of view.

At the clarity level, although the paper is globally well written and easy to follow, some concepts and parts of the protocol are brushed over and require more precision (see questions). Also, a big gap is a per technique analysis, i.e. what how much pulling relies on masking non useful frames vs time similarity hashing vs adaptive MuE as well as combinations (3 individual, and 3 combinations of 2 out of 3 techniques to compare to the 3 simultaneously). Slight adjustments to the techniques should allow a meaningful comparison along these lines.

### Questions
- What is a navigable view? This concept central to the filtering of frames as well as the structure of the solution is repeatedly used without being rigorously introduced.
     - How are navigable views identified amongst the 36?

- Lines 201-209 offer a very vague justification of the reasons behind the failure of vanilla MuE. The authors just acknowledge differences in behavior after a couple of steps and conclude "Processing fewer transformer layers can lead to an inaccurate understanding of the visual surroundings. As shown in the bottom-right figures, while the bathroom is consistently visible across multiple steps (t P r2, 10s) in the panorama, the MuE agent fails to recognize it and makes sub-optimal decisions at each navigation step."
     - Why does it fail to recognize it? which views are quitting early? the useful ones ? With only 36 views one would be able to maybe look into the model to get more insight

- How does the budgeted batch inference (introduced line 284) work? It might be a method from a cited paper, but it seems like a crucial underlying piece of the puzzle and might require additional explanation.

- Algorithm 1 shows that navigable views undergo a separate treatment from proximity views. If I understand this correctly navigable views go through the ViT with no early exit or time similarity checks. There is thus no compute gain for these and the gains are only made on masked views (spatial, no compute at all) and proximity views (both hashing and early exit). Can the authors confirm that that is indeed the case?
    - Whether affirmative or not this would require, at least at my level of understanding, a bit clarification in the main text as the algorithm notes are not elucidating enough regarding these crucial aspects of the solution.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an efficient input-adaptive inference method for vision-and-language navigation (VLN) to address computational “overthinking,” where models perform excessive calculations unnecessarily. The approach combines three adaptive strategies: selective processing of critical views (spatial), dynamic thresholding for early exits (model-level), and caching of repeated views (temporal). Evaluated on six VLN benchmarks, this method achieves substantial computational savings—up to 60%—with minimal performance loss, offering a practical solution for improving VLN efficiency in resource-constrained settings.

### Strengths
1. The paper introduces an innovative approach to enhancing efficiency in vision-and-language navigation (VLN) by addressing "overthinking"—the unnecessary computation in model decision-making. The authors propose a unique combination of adaptive methods across spatial, model-level, and temporal dimensions. This combination is well-suited to VLN, where inputs are sequential and often contain redundancies.
2. The method is well-designed, clearly breaking down the adaptive components into three strategies: spatial locality, model-level efficiency, and temporal locality. The paper is generally well-written.
3. The proposed method has practical implications for VLN tasks in resource-constrained environments, such as robotic navigation. By demonstrating a 60% reduction in computation with minimal impact on performance, the work provides a valuable solution for deploying VLN agents in real-world scenarios where computational resources are limited.

### Weaknesses
1. While the paper effectively introduces adaptive mechanisms (spatial, model-level, and temporal), there is limited theoretical analysis of each mechanism's impact on VLN performance and generalization. For example, the paper could explore how the choice of k (in the k-extension) or the aggressiveness of the adaptive thresholding influences model stability and long-term performance in complex environments. Specifically, the analysis lacks a discussion on how the k-extension impacts the agent's ability to recover from errors or adapt to unseen environments. Furthermore, the paper does not delve into how the thresholding mechanism might affect the model's learning dynamics, potentially leading to instability if the thresholds are not carefully tuned.
2. Some formulae and symbols, such as those in the k-extension and thresholding sections, could benefit from additional clarification and consistent notation to improve readability. For instance, consistently defining parameters and variables at the start of each section would reduce potential confusion. The paper should also clarify the exact mathematical operations involved in the k-extension, particularly how the non-navigable views are selected and weighted. Similarly, the thresholding section could benefit from a more precise definition of how the thresholds are determined and how they relate to the model's confidence scores.
3. The paper provides a robustness analysis under various visual corruptions, but it treats the proposed method as a single unit. A more detailed breakdown of how each mechanism (spatial, model-level, temporal) contributes to robustness under different corruptions (e.g., which mechanism is most affected by motion blur or low lighting) would offer valuable insights. For example, it would be beneficial to understand if the k-extension is more susceptible to motion blur due to its reliance on spatial context, or if the thresholding mechanism is more vulnerable to low lighting conditions due to its dependence on model confidence scores. Such an analysis would provide a more nuanced understanding of the method's strengths and weaknesses.
4. The caching mechanism, which leverages locality-sensitive hashing (LSH) to avoid recomputing similar views, is a valuable addition. However, the paper does not fully explore how this caching performs under different levels of scene variability or how effective it is when environmental conditions shift significantly (e.g., new objects or layouts). A more detailed sensitivity analysis on the caching's impact across different types of VLN tasks or environmental settings would help establish a clearer understanding of when this mechanism is most beneficial. The paper should also investigate the impact of hash collisions on the caching performance and how the choice of hash function affects the overall efficiency and accuracy.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents three methods that improves the computational efficiency for vision-and-language navigation (VLN), especially in the context of visual input processing. The goal of proposed methods is selecting a subset of 36 panoramic views while maintaining the overall VLN performance. Experimental results show that the proposed algorithms (early-exit, spatial locality, and temporal locality) improve the computational efficiency in several VLN benchmarks.

### Strengths
- The paper addresses the critical problem in VLN when deployed in real-world applications.
- The paper is well-written and easy to understand.

### Weaknesses
 - The paper highlights the practical aspects of VLN when deployed in real-world environments. Ironically, the proposed methods lack practicality in their current form.
  - The method regarding the spatial locality requires "navigable points" in the agent's current position. However, in real-world environments, no navigable points are given to VLN agents. This indicates that we can't directly apply this method to the real-world VLN scenario. How can we apply the spatial locality method when navigable points are not given? One way to address this concern is to investigate the results by employing the waypoint predictor. In the task of vision-and-language navigation in continuous environments (VLN-CE), the work [3] has trained the waypoint predictor that predicts several navigable points in each time step. It would be interesting to see the comparison when given the estimated navigable points and the ground-truth (i.e., known) navigable points.

  - Another concern is about the temporal locality method. The method benefits from the computational efficiency, but it also sacrifices the space complexity of the VLN system. This can be a critical problem when VLN agents should perform long-horizon navigation. I think one way to address this concern is to perform a quantitative analysis of the space-time tradeoffs, especially for longer navigation tasks. In this case, what should be a metric for the memory usage?


- Experiments were conducted in limited settings. Most of experiments are studied in the R2R task, and two VLN models in the paper (HAMT and DUET) are quite outdated. It request the authors to investigate the effect of three proposed methods in longer-horizon VLN tasks (e.g., RxR) with more recent state-of-the-art models (e.g., ScaleVLN [1] or MARVAL [2]). More specifically,

  - The task length of the R2R task is relatively short, so I have concerns that the performance drop of applying the three proposed methods will become more prominent as the task length increases. Can the authors report how performance and computational efficiency vary with task length? I recommend to investigate the RxR task since this benchmark has longer navigation length. Furthermore, comparing the contribution of each method in longer navigation tasks will be an another interesting analysis since it clearly shows which methods are robust to task length.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an input-adaptive navigation method for efficient vision-and-language navigation (VLN) that addresses the overthinking problem common in history-aware multi-modal transformer models. The authors develop three adaptive mechanisms to improve spatial, model-level, and temporal efficiency.

### Strengths
The motivation of this work is strong, as efficiency is indeed a critical issue to address in VLN.

### Weaknesses
1. Although the paper frequently emphasizes efficiency and mentions potential deployment on robots, it only provides GFLOPs as a metric. This is insufficient; additional metrics like model size and inference time should be included. The absence of model size is particularly concerning given that parameter count directly impacts memory footprint, which is a crucial constraint for deployment on resource-limited robotic platforms. Furthermore, GFLOPs, while indicative of computational cost, do not directly translate to real-world inference time due to variations in hardware architecture, memory bandwidth, and software optimization. Therefore, wall-clock inference time on a representative hardware platform should be reported.
2. The approach reduces computation by limiting the number of panoramic views, but this may not address an actual issue. VLN image features are typically pre-extracted offline, eliminating the need for recalculating visual features during navigation. Moreover, recent methods often select candidate views rather than processing all 36 panoramic views, making the proposed solution potentially less relevant. The authors should clarify whether the pre-extracted features are stored per-view or per-location, as this has significant implications for the practicality of their method. If features are pre-extracted per-location, then the proposed method is not applicable. If the features are pre-extracted per-view, then the authors should clarify how their method reduces computation compared to simply selecting a subset of candidate views.
3. The authors appear to lack familiarity with VLN, as related work only covers pre-2018 studies, and the experiments compare only with HAMT (NeurIPS 2021) and DUET (CVPR 2023). This narrow scope of related work and experimental baselines raises concerns about the generalizability and relevance of the proposed method to the current state-of-the-art in VLN. The authors should include more recent and diverse baselines, particularly those focusing on efficient VLN, to properly contextualize their contributions.
4. While GFLOPs are reduced by half, the performance degradation is significant, which may make the results difficult to justify as acceptable. The authors should provide a more detailed analysis of the trade-off between computational savings and performance degradation, including a breakdown of performance across different tasks and environments. A 10% drop in success rate is substantial and requires a more thorough justification, especially when compared to recent methods that achieve similar or better efficiency gains with minimal performance loss.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2
