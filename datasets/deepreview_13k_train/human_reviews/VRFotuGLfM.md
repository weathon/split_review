# DiffMove: Human Trajectory Recovery via Conditional Diffusion Model

- Decision: Reject
- Scores: 6, 6, 8, 6, 5

## Abstract
Recovering human trajectories from incomplete or missing data is crucial for many mobility-based urban applications, e.g., urban planning, transportation, and location-based services. Existing methods mainly rely on recurrent neural networks or attention mechanisms. Though promising, they encounter limitations in capturing complex spatial-temporal dependencies in low-sampling trajectories. Recently, diffusion models show potential in content generation. However, most of proposed methods are used to generate contents in continuous numerical representations, which cannot be directly adapted to the human location trajectory recovery. In this paper, we introduce a conditional diffusion-based trajectory recovery method, namely, DiffMove. It first transforms locations in trajectories into the embedding space, in which the embedding denoising is performed, and then missing locations are recovered by an embedding decoder. DiffMove not only improves accuracy by introducing high-quality generative methods in the trajectory recovery, but also carefully models the transition, periodicity, and temporal patterns in human mobility. Extensive experiments based on two representative real-world mobility datasets are conducted, and the results show significant improvements (an average of 11% in recall) over the best baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides an innovative self-supervised model DiffMove to recover trajectories using a conditional diffusion model. The model uses multiple losses to learn: 1) the trajectory location encoder that projects raw points to effective trajectory embeddings, 2) the conditional embedding denoiser that generates the target trajectory location embedding with the help of historical and current trajectory embeddings, and 3) the final embedding decoder to map the denoised embeddings back to their locations.

Extensive experiments have demonstrated the SOTA performances of DiffMove on both GPS and check-in trajectories, strong robustness against various historical trajectory location missing rates, and efficacy of main model components by ablation studies. It would be better if there were visualizations and efficiency analysis.

### Strengths
1. This paper delivers a novel method of human mobility modeling using a conditional diffusion model.  The noising and denoising happen on trajectory embeddings, which benefits the effective denoising operations for trajectory representation learning.

2. Trajectory modeling in a format of each user on each day helps with capturing user-wise periodic moving patterns. And current and historical controlled embedding denoiser ensures the effective feature extraction from such formatted data, contributing to capability of capturing spatiotemporal dependencies in low-sampling rate trajectories. 

3. The model DiffMove achieves SOTA performance across extensive experimental settings with high robustness. Combined with its innovation, it can be impactful in trajectory recovery and human mobility pattern modeling.

### Weaknesses
1. The paper makes substantial improvements from TRILL (Deng et al., 2023) but could be better if included more datasets to show the generalization of DiffMove on diverse datasets.


2. Efficiency analysis is missing. If there is no improvement in efficiency, is it causing longer running time than the baselines do?

3. If there are visualizations of the effects of the denoising process of embeddings would be better.

### Questions
1. In Section A.7, can you clarify how you “gather data on road network” for location representation?

2. What’s the running time of DiffMove compared to baselines? (just a rough comparison)

3. Can you specify what kind of information is learned by the denoising process based on the trajectory embeddings?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces DiffMove, a conditional diffusion-based trajectory recovery method designed to recover missing locations from sparse human mobility data. DiffMove improves accuracy by transforming trajectory locations into an embedding space for denoising and recovering missing locations through an embedding decoder. The model effectively captures the spatial and temporal patterns in human mobility, and integrates multiple conditional feature extraction modules to systematically address spatial-temporal dependencies.

### Strengths
1. This paper employs a conditional diffusion-based trajectory recovery method to achieve high-quality generation and accurate trajectory recovery.
2. This paper innovatively designs and integrates multiple conditional feature extraction modules to address the complexity of spatial-temporal dependencies.
3. This paper conducts extensive experiments on two representative real-world mobility datasets, with results showing significant improvements over the baseline.

### Weaknesses
1. The limitation noted in line 44, “The previous approaches have limitations in complex, sparse, irregular, and uncertain scenarios inherently in human mobility,” requires further elaboration. Specifically, does the proposed method address these limitations, and if so, how?
2. Additionally, it would be beneficial for the authors to compare their approach with more recent trajectory recovery models such as SimiDTR [a] and RNTrajRec [b]. A recent work called Diff-RNTraj [c] also shares a similar approach; a discussion of the distinctions between this work and the proposed model would further strengthen the paper.
3. Some minor errors include: 
① to obtain incoming/outgoing aggregated node embedding eI,s/eo,s,
② the formula representation of the cosine similarity between the imputed target embeddings and location embeddings
[a] Zhang, Yupu et al. “SimiDTR: Deep Trajectory Recovery with Enhanced Trajectory Similarity.” International Conference on Database Systems for Advanced Applications (2023)
[b] Y. Chen, H. Zhang, W. Sun and B. Zheng, "RNTrajRec: Road Network Enhanced Trajectory Recovery with Spatial-Temporal Transformer," 2023 IEEE 39th International Conference on Data Engineering (ICDE), Anaheim, CA, USA, 2023, pp. 829-842, doi: 10.1109/ICDE55515.2023.00069
[c] T. Wei et al., "Diff-RNTraj: A Structure-aware Diffusion Model for Road Network-constrained Trajectory Generation," in IEEE Transactions on Knowledge and Data Engineering, doi: 10.1109/TKDE.2024.3460051.

### Questions
1. How are the visited locations specifically represented, and how are the masked locations embedded?
2. Better comparison with existing work and better motivate the usage of the diffusion model.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors modify the widely studied diffusion model for trajectory recovery, an acknowledged problem in the spatio-temporal community. The authors design DiffMove, adapting diffusion models to address two challenges in the recovery problem. On two real-world datasets, DiffMove outperformed SOTA methods on multiple metrics.

### Strengths
(1) This paper is well-written. The introduction is very clear and easy to follow—appreciation to the authors to make our lives easier. 

(2) The experiments are solid with ablation studies and robustness analysis.  

(3) The trajectory recovery is an interesting problem and probably enables multiple downstream applications.

### Weaknesses
(1) In Section 3.1, the authors might need to specify how many locations are missing in the trajectory. The number of missing locations is fixed or random will make a difference to the final solutions. 

(2) Some writing issues. In line 060, does the authors mean “cannot be fully exploited”? In line 160, Eqn(2) is not easy to identify in the manuscript.
 
(3) It would be great if the authors could discuss the fundamental differences and similarities between trajectory recovery and generation. From the reviewer’s perspective, they both generate some trajectory points. 

(4) In the abstract, the 11% improvement of recall, might misleading the readers. It might be more appropriate to report the improvement compared to the best baseline models,as shown in Table 1. 

(5) There are multiple losses in the training process, how do different losses matter to the final performance? Also, how to determine the coefficients for each loss; 

(6) One major concern is the claim about predictive and generative models for trajectory recovery in the second paragraph of the Introduction section. From the reviewer’s understanding, the recovery task is to infer one of the multiple points that happened in the past. Thus, predictive or generative seems similar to me. Also, could you explain whether these papers are predictive recovery or generative recovery? [1][2][3] 

(7) I have some concerns about Fig.1. The first “Raw Current Trajectory” has 9 points, but the “Masked Locaitons” have 2 points and the “Current Trajectory” has 4 points after the random masking. So, where are the other points? 

(8) The format should be consistent. e.g., the legend of Fig.1 and Fig.1, the period is missing in FIg.2. 

(9) It seems most baselines are not from recent papers. Recently, there are many papers about trajectory learning, e.g., trajectory generation. Could you explain the rationale of choosing baseline models? 


[1] TrajWeaver: Trajectory Recovery with State Propagation Diffusion Model

[2] RNTrajRec: Road Network Enhanced Trajectory Recovery with Spatial-Temporal Transformer

[3] MTrajRec: Map-constrained trajectory recovery via seq2seq multi-task learning

### Questions
No further questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The task of this manuscript is the imputation of human mobility trajectory data. Two challenges are proposed: (1) Traditional diffusion models aim for imputation of continuous numerical values, which can be directly obtained through denoising. In contrast, the goal of trajectory recovery is to represent locations as discrete IDs, allowing for a fuller utilization of the transitional and periodic patterns of human trajectories. (2) Besides the temporal dependencies of the current sample, the denoising process should also consider the transitional and periodic dependencies between the current sample and historical samples. To address these challenges, this manuscript introduces DiffMove. To tackle the first challenge, DiffMove converts discrete trajectories into an embedding space, inferring the embedding representations of missing locations through conditional diffusion, and then passing them to a Missing Location Decoder to obtain location IDs. To address the second challenge, DiffMove designs a Spatial Conditional Block based on graph neural network and attention mechanism to learn the spatial transitional and periodic patterns of both current and historical trajectories. Additionally, a Target Conditional Block is introduced to extract knowledge of the missing locations of the current trajectory from historical trajectories. Experiments conducted on two mobility datasets (Geolife and Foursquare) show that DiffMove outperforms the baseline by an average of 11% in recall rate.

### Strengths
This manuscript focuses on the interpolation task using diffusion models on human mobility trajectory data and presents two practical challenges: converting discrete trajectories into continuous values that can be processed by diffusion models, and utilizing information from historical trajectories to guide the recovery of missing locations in the current trajectory. Additionally, extensive experiments are conducted to demonstrate the effectiveness of the proposed model.

### Weaknesses
1. Some sentences in this manuscript are not fluent.

2. The model lacks innovation, as its overall framework is similar to CSDI[1].

3. The selected datasets for the experiments are insufficient, and the baseline models chosen for
comparison do not include advanced models from recent years.

[1] Tashiro Y, Song J, Song Y, et al. Csdi: Conditional score-based diffusion models for probabilistic time series imputation[J]. Advances in Neural Information Processing Systems, 2021, 34: 24804-24816.

### Questions
1. How are the GPS trajectory points in the Geolife dataset converted into discrete location representations (since GPS is continuous and location is discrete)? Cover to discrete regions?

2. How do the baseline models selected for the comparative experiments incorporate historical information? The baselines in this manuscript mainly focus on prediction task, how do they perform imputation task?

3. The DDPM has significant computational overhead. If there are many location points, using an adjacency matrix will further increase the time cost and memory usage. How can computational efficiency be ensured?

4. The denoising network simultaneously employs structures like GCN, cross-attention, and transformers. Could a complex network design affect the prediction performance? Based on experience, the inclusion of GCN may not yield good results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the issue of human trajectory recovery, specifically focusing on reconstructing a user's missing visited locations during specific time intervals. The study highlights the challenges posed by current methods in dealing with the complexities, irregularities, and uncertainties that are inherent in human mobility patterns.

To tackle these challenges, the paper introduces the use of diffusion models and proposes a novel approach called DiffMove. This approach adapts diffusion models for discrete location recovery and integrates both historical and recent trajectory data. DiffMove includes a Trajectory Location Encoder module, which transforms discrete location indices into continuous embeddings, and a Conditional Embedding Denoiser that extracts valuable information from past and recent trajectories to enhance the diffusion model's conditional information.

The performance of DiffMove is evaluated using two human mobility datasets, where it is compared against several leading methods in human mobility prediction and recovery.

### Strengths
1. In practical terms, the human trajectory recovery problem addressed in this paper is relevant.

2. DiffMove, introduced in this paper, is straightforwardly designed to employ diffusion models for recovering missing locations in human trajectories. The method's design and implementation are clearly outlined, ensuring reproducibility.

3. The experiments clearly demonstrate the superior performance of the proposed method.

### Weaknesses
1. I find the framing of the problem regarding human trajectory recovery in this paper somewhat debatable. As outlined in Definition 3.1, each trajectory point signifies a location visited by a user within a specific time frame (of 30 minutes). A point is considered missing if the location isn't observed during that interval. There are two scenarios where this approach might be inappropriate:
    - When a user visits a location, such as a movie theater, and remains there for an extended period, it is expected that they won't visit other locations during subsequent intervals. These should not be marked as missing locations. If these intervals are instead recorded as the location where the user stayed, two questions arise: 1) Practically speaking, how can we determine how long a user stayed at one location when such data is typically not available in check-in datasets like FourSquare? 2) The trajectory would consist of consecutive repetitive locations, making recovery quite trivial.
    - If a user visits a location (e.g., fast food restaurant) and then moves to another within minutes, the 30-minute interval may not accurately capture their movements.

2. The paper's motivation could be articulated more effectively. In the introduction, it states that there are "limitations in complex sparse, irregular, and uncertain scenarios inherently in human mobility," which is somewhat vague. This does not clearly illustrate how these limitations are tackled by the proposed method. Furthermore, claims like "traditional methods typically provide a biased deterministic imputed trajectory" suggest an intention to highlight probabilistic generation's advantages over deterministic methods; however, the proposed approach neither focuses on probabilistic generation nor evaluates this aspect experimentally.

3. The proposed method lacks substantial novelty in its design. The challenge presented—"the imputation targets of conventional diffusion models are continuous numerical values"—and the solution of mapping discrete location indices into continuous embedding space appear standard given existing latent diffusion [1-2] and discrete diffusion [3] solutions. Integrating historical and recent trajectory information via Spatial Conditional Block seems straightforward and primarily involves combining existing components.

4. The paper's illustrations could be clearer. Specifically, components in Figure 1 lacks appropriate labels, leading to vague references such as "the blue and white location icons in trajectories" and "shown in the top right part of Figure 1." This can cause potential confusion for readers.

5. I recommend including comparisons or discussions on some missing related works regarding human mobility trajectory recovery methods; certain comparison methods [4] could be addressed here. While recognizing that settings differ slightly on trajectory recovery, discussing GPS trajectory recovery/imputation methods [5-6] might also prove beneficial.


[1] Li, Xiang, et al. "Diffusion-lm improves controllable text generation." _Advances in Neural Information Processing Systems_ 35 (2022): 4328-4343.

[2] Lovelace, Justin, et al. "Latent diffusion for language generation." _Advances in Neural Information Processing Systems_ 36 (2024).

[3] Lou, Aaron, Chenlin Meng, and Stefano Ermon. "Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution." _Forty-first International Conference on Machine Learning_.

[4] Xi, Dongbo, et al. "Modelling of bi-directional spatio-temporal dependence and users’ dynamic preferences for missing poi check-in identification." _Proceedings of the AAAI conference on artificial intelligence_. Vol. 33. No. 01. 2019.

[5] Ren, Huimin, et al. "Mtrajrec: Map-constrained trajectory recovery via seq2seq multi-task learning." _Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining_. 2021.

[6] Chen, Yuqi, et al. "Rntrajrec: Road network enhanced trajectory recovery with spatial-temporal transformer." _2023 IEEE 39th International Conference on Data Engineering (ICDE)_. IEEE, 2023.

### Questions
1. (Relate to W1) Could the authors explain the reasoning behind how they have framed the problem of human trajectory recovery?

2. (Relate to W2) Could the authors elaborate on the challenges associated with human trajectory recovery, discuss the limitations of current methods, and describe how their proposed approach addresses these challenges and limitations?

### Soundness
2

### Presentation
2

### Contribution
2
