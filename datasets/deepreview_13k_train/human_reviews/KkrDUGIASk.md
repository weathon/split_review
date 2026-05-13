# An Extensible Framework for Open Heterogeneous Collaborative Perception

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Collaborative perception aims to mitigate the limitations of single-agent perception, such as occlusions, by facilitating data exchange among multiple agents. However, most current works consider a homogeneous scenario where all agents use identity sensors and perception models. In reality, heterogeneous agent types may continually emerge and inevitably face a domain gap when collaborating with existing agents. In this paper, we introduce a new open heterogeneous problem: \textit{how to accommodate continually emerging new heterogeneous agent types into collaborative perception, while ensuring high perception performance and low integration cost?} To address this problem, we propose \textbf{HE}terogeneous  \textbf{AL}liance (HEAL), a novel extensible collaborative perception framework. HEAL first establishes a unified feature space with initial agents via a novel multi-scale foreground-aware Pyramid Fusion network. When heterogeneous new agents emerge with previously unseen modalities or models, we align them to the established unified space with an innovative backward alignment. This step only involves individual training on the new agent type, thus presenting extremely low training costs and high extensibility. To enrich agents' data heterogeneity, we bring OPV2V-H, a new large-scale dataset with more diverse sensor types. Extensive experiments on OPV2V-H and DAIR-V2X datasets show that HEAL surpasses SOTA methods in performance while reducing the training parameters by 91.5\% when integrating 3 new agent types.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a novel question surrounding the task of multi-agent collaborative perception, duly considering the scenario where new collaborators continually join the perception system in real-world settings. This is a highly intriguing question, directly impacting the deployment of multi-agent collaborative perception systems.

The author proposes a highly concise solution, introducing the HEAL framework, which is capable of accommodating the features acquired by the agents newly joining the system. The experimental results demonstrate that the proposed new framework is effective in accommodating agents newly incorporated into the system, and achieves state-of-the-art results. 

In conclusion, this is a highly intriguing piece of work.

### Strengths
1. Presents a highly intriguing new question, effectively addressing the challenges faced during the deployment of multi-agent collaborative perception systems.

2. The approach in this paper is notably succinct and efficient; the authors design a novel backward alignment mechanism for individual training. This method constructs an alignable feature space, facilitating subsequent updates of features transmitted by other agents.

### Weaknesses
1. The intermediate fusion method employed in this paper doesn't seem to address the issue of new agents joining as effectively as late fusion does. Specifically, while the authors propose a backward alignment mechanism, it is unclear how this mechanism handles the inherent domain shift between different sensor modalities and configurations that new agents might introduce. The paper lacks a detailed analysis of how the feature space is adapted to accommodate these shifts, which could lead to suboptimal performance when new agents with significantly different sensor characteristics join the system.

2. This paper has only conducted experiments on two datasets, one of which is generated for the first time in this paper. It is hoped that the author can introduce more experiments to substantiate. The limited number of datasets raises concerns about the generalizability of the proposed method. The newly generated dataset might not fully represent the diversity of real-world scenarios, and the absence of experiments on more established datasets makes it difficult to compare the proposed method with existing approaches under varied conditions.

### Questions
1. In this paper, the authors claim that agents newly joining the system may struggle to align well in the feature space due to data distribution differences. However, is training a unified feature space an effective solution? Given that data discrepancies arising from different sensors inherently result in domain differences, this discrepancy poses a significant challenge in the domain adaptation field. Is the method proposed in this paper suitable for addressing this issue?

2. The author raises a novel question, thus it would be prudent to utilize more datasets to verify the efficacy of the proposed method. This is because some schemes[1] solely employing distillation can achieve significant improvements in accuracy. In the open-source datasets they used, there are also newly joining agents, similar to the DAIR-V2X dataset used in this paper. It is hoped that the author can supplement with more extensive experiments to substantiate the reliability of the raised question and the effectiveness of the proposed method.

3. Referring to the article on late fusion[2], I believe that late fusion seems to be a more effective solution to the problem posed in this paper. While the process of late fusion indeed has some issues with error accumulation, [2] has adeptly mitigated some of the past problems of late fusion through trajectory prediction. At the same time, employing late fusion can maximally avoid the issue of aligning features extracted by different agents, fundamentally resolving the problem posed in this paper. I hope that the author can conduct a comparative analysis between the methods of these two papers.

[1]. Z. LI, et al. MKD-Cooper: Cooperative 3D Object Detection for Autonomous Driving via Multi-teacher Knowledge Distillation. IEEE Transactions on Intelligent Vehicles, 2023.

[2]. S. Wei, et al. Asynchrony-Robust Collaborative Perception via Bird's Eye View Flow. NIPS 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces HEterogeneous ALliance (HEAL), an innovative framework designed to enhance collaborative perception by accommodating continually emerging heterogeneous agent types, addressing the domain gap issue in existing systems. The framework establishes a unified feature space that aligns new, diverse agents through a cost-effective and secure backward alignment process, requiring only individual training for the new agents. This approach not only minimizes training costs and maximizes extensibility but also safeguards the model details of the new agents. The authors also introduce a new extensive dataset, OPV2V-H, to advance research in heterogeneous collaborative perception. Experiments reveal that HEAL outperforms state-of-the-art methods, showing a remarkable reduction in training parameters by 91.5% while integrating three new agent types.

### Strengths
1. The paper introduces a interesting open heterogeneous collaborative perception setting. Agents with different sensor can collaborate for vision tasks. This is an interesting and practical setting.
2. Multi-scale feature fusion and the 'late participation' strategy is reasonable for such tasks.
3. A dataset contribution. Experiments are extensive. Presentation of the paper is good.

### Weaknesses
1. There is no real-world experiments. There are some dataset like nuScene/nuPlan, Waymo and etc including data of different sensors. It would be nice to show some real examples.
2. It would be interesting to include a bit discussion on related works for cooperation for driving tasks, e.g. [1][2][3]
3. I don't find a code release. Would be nice to release the code for supplementary or public github repo.

### Questions
1. The paper mentioned new agent privacy issue. I assume the late participate will require the new agent to access the fused feature to do the update according to equations in Section 4.3. Will the fused feature release some privacy of the old agents to the new agent?
2. For the experiments setting, are there any case agent exits the cooperation during training? How the framework will do to deal with this situation.
3. I am wondering if there are some simple experiments to show real world cases as I mentioned in the weak point.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work presents a novel training schema and fusion network for heterogeneous cooperative perception where agents may have different kinds of modalities/sensor configurations. The proposed framework aligns the BEV features from different modalities to the common feature space and fuses them to reason 3D object detections.

### Strengths
* The proposed training design is simple yet effective for faster convergence and higher performance. 
* The proposed methods achieve outstanding performance.

### Weaknesses
 * When comparing with other SOTA algorithms, is the same training strategy used for a fair comparison? Is the main performance boost from the training strategy or the multi-modal fusion design? 
* The fusion model design (except the residual part) shows similarity with existing methods like who2com/where2comm/disconet. Please justify and highlight the differences and novelty. Please also benchmark the performance under the same training strategy with only different fusion networks so as to demonstrate the effectiveness of the proposed fusion module. 
* How to ensure each modality can be aligned to the common feature space? For example, it may be hard to extract the 3D features 
from camera/radar data which are expected to be as good as (aligned) as the LiDAR features. From 6, we can see that camera bev features are more vague than LiDAR features, which could not show the aligned effect. Please justify this design choice.  
* Can the network scale to different sensor modality combinations? For example, changing/fixing the ego modality with dynamic collaborator sensor modalities. What is the sensitivity of the network with respect to this sensor modality combination ratio?
* The 5 hour training time is for single modality. What is the overall training time and the associated time for the compared model?
* The author argued that "late fusion is suboptimal due to the communication latency". However, as shown in DiscoNet/V2X-ViT/V2VNet etc., intermediate fusion methods usually require larger bandwidth requirements than late fusion, which can even lead to potentially larger communication latency compared with late fusion. 
* The node level weight prediction seems to stem from the proposed training strategy, not a novel architectural or model-level design. The explicit foreground estimators also require further justification. Why do methods like Where2comm lack an estimator and supervision when it uses the detection head to generate a spatial confidence map that is trained and supervised?

### Questions
* The author argued that "late fusion is suboptimal due to the communication latency". However, as shown in DiscoNet/V2X-ViT/V2VNet etc., intermediate fusion methods usually require larger bandwidth requirements than late fusion, which can even lead to potentially larger communication latency compared with late fusion. 
* How the result of HM-ViT is reproduced? Is the heterogeneity used for all 4 modalities? Or only two modalities are used as the original paper? 
* What is the inference time of the proposed method? 
* What is the influence of the modality choice in the base collaboration training?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This article introduces a novel problem about collaborative perception, which is extensible heterogeneous agent collaborative perception. To address this problem, a novel extensible collaborative perception framework.is proposed, which includes a novel Pyramid Fusion method. In addition, a new large-scale database is proposed based on OPV2V. The introduced problem is interesting and has significance in engineering. However, the explanation of certain content is not clear enough.

### Strengths
1. The introduced extensible heterogeneous agent collaborative perception problem is interesting and has significance in engineering.
2. The proposed HEAL framework is novel and holds state-of-the-art performance.
3. A new large-scare database is proposed to facilitate the research of heterogeneous collaborative perception.

### Weaknesses
1. The content of the Section 3 is somewhat limited, please make some extensions or merge it with other sections.
2. The article has not mentioned how to extract features from different modalities and convert them into the required BEV features. Specifically, the transformation of raw sensor data (LiDAR point clouds and camera images) into a Bird's-Eye-View (BEV) representation is not clearly described. The process of converting point clouds into BEV features, whether through voxelization or other methods, needs to be detailed. Similarly, the method for projecting image features into the BEV space, including the handling of depth information, should be explicitly stated.
3. The article has not mentioned how to perform spatial transformation and alignment of the features from heterogeneous agents in different coordinate systems. Please clarify this. The process of aligning features from different agents, which may have different poses and coordinate systems, is not clearly explained. The method for transforming these features into a common coordinate system, including the specific mathematical operations and transformations used, needs to be elaborated.
4. During the training of the new-type agent, the new agent seems not to get collaborative information from other agents, which may have an impact on perception performance. This should be explained. It is unclear whether the new agent is trained in isolation or if it benefits from the collaborative information of other agents during training. The impact of this training strategy on the overall performance, especially the new agent's perception capabilities, should be discussed.
5. On the other hand, the Pyramid Fusion module and detection head haven’t been affected by new type agents. It means that new-type agents did not participate in collaborative perception during the training process. This could be better clarified. The role of new agents in the collaborative perception process is unclear, particularly whether their features are integrated into the Pyramid Fusion module and detection head during training. The mechanism by which new agents contribute to the overall collaborative perception should be explained.
6. The claim of the performance of the proposed Pyramid Fusion should be supported by experiment results and observations, please supplement relevant ablation experiments.

### Questions
1. What’s the structure of the encoder in the proposed framework?
2. Will the number of input channels for the Pyramid Fusion module change when a new agent is added?
3. Why can the performance of this method be improved so much on AP70? 

Sincerely,

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
