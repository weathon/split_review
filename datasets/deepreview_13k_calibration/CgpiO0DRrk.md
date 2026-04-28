# Video Caching at Data-drifting Network Edge: A KD-based Cross-domain Collaborative Solution

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
The explosive growth of video content streaming has led to network congestion and quality decline, making efficient content delivery a significant challenge. To address this, edge caching has emerged as a solution, utilizing mobile edge caching servers like edge base stations (EBS) as a cost-effective approach. Collaborative edge caching has been proposed to address the space limitation of edge servers by enabling cooperation and content sharing among multiple servers, thereby improving caching hit rates (CHR). However, little attention has been paid to the impact of request characteristics on different servers. To tackle this issue, we conducted a study using data collected from Kuaishou company over a period of four weeks, comprising 350 million video requests. Our research findings indicate that request-sparse EBSs significantly impede the overall CHR improvement in the edge caching problem. Knowledge distillation (KD), a technique that transfers knowledge from strong models to weak models, is expected to solve this bottleneck problem. However, traditional KD methods often rely on the assumption of independent and identically distributed data, which may not hold true in real-world scenarios where data drift occurs. We identify two major types of data drift in caching data: temporal drift and spatial drift. To overcome these challenges, we propose an adaptive KD-based cross-domain collaborative edge caching framework, called KDCdCEC, which incorporates three specifically tailored components: i) a slot-wise reinforcement learning agent capable of adapting to EBSs with varying storage sizes, ii) a deep deterministic policy gradient-based algorithm that adaptively configures the reference weights of servers on their partners, and iii) a content-aware request routing mechanism that enhances the decision-making of edge servers. Experimental results show that KDCdCEC outperforms state-of-the-art approaches in terms of average CHR, average latency, and traffic cost.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Collaborative edge caching can offer a cost-efficient strategy for enhancing video caching and streaming. This paper conducted a measurement study and revealed that the primary factor influencing caching performance is the spatio-temporal diversities in request patterns. To tackle the issue of sparse requests in specific Edge Base Stations (EBSs), the paper proposes to use knowledge distillation to transfer knowledge from request-dense EBSs to request-sparse ones. To further account for the spatio-temporal drift in request distribution across EBSs, the paper designs an adaptive KD-based cross-domain collaborative edge caching framework, named KDCdCEC. The proposed framework consists of three major components: 1) a RL agent to make caching replacement decisions in each EBS; 2) a deep deterministic policy gradient-based algorithm to adaptively configure the reference weights for adaptive KD; 3) a content-aware request routing mechanism. Experiment results shows the effectiveness of KDCdCEC under a specific caching setting.

### Strengths
1. In this paper, a novel approach to collaborative edge caching is explored. Rather than concentrating on the sharing of cached content among partners, the paper's primary focus is on the sharing of caching policies among partners. This approach aims to minimize the communication overhead between partners that typically arises from content sharing.
2. The paper applies knowledge distillation to facilitate the training of multi-agent RL in addressing the challenges posed by request heterogeneity and dynamics. The application of  multi-agent RL with knowledge distillation to collaborative caching problem is relatively new.

### Weaknesses
 1. The problem statement or definition of collaborative edge caching in this paper lacks clarity and support.
1) The paper assumes that the EBSs collaborate by sharing caching policies rather than cached content. This assumption gives rise to two problems. Firstly, considering that each EBS has limited cache storage, if they don't share cached content among themselves, every cache miss would necessitate content retrieval from remote CDN servers. Consequently, the potential benefits of collaborative edge caching are constrained since it doesn't significantly reduce backbone traffic. Secondly, the paper also highlights the spatial drift and diversity of request patterns in different EBS domains. This raises a question about the rationale behind advocating the sharing of caching policies among EBSs. For example, if one EBS serves requests with a LRU pattern, while another EBS caters to a LFU pattern, how would these two EBSs benefit from sharing caching policies when their request patterns differ?
2) This paper studies a caching problem with a fixed number of video contents, which significantly deviates from real caching systems where the number of videos or objects varies over time. Furthermore, the paper assumes the CDN server have cached all the videos. However, considering the substantial number of videos (i.e., 2.887 million) mentioned in the evaluation section, this assumption might be overly stringent, as CDNs typically have relatively limited storage capacity.
 2. The presentation of the proposed framework in the paper lacks clarity, and certain claims about the techniques are not well substantiated.
1) The paper claims that the RL agent is slot-wise and can adapt to EBSs with different storage sizes. However, it's noted that the action space of the RL agent is C \times C, where C seems a fixed number across all EBSs throughout the paper (including the evaluation section). If C does indeed differ among EBSs, then during knowledge distillation, how do you handle the variable input state size, which is 2C \times F?
2) What is the content-aware request routing mechanism? I did not find any technique description about it.
3) The paper uses the names and notations interchangeably, which leads to confusion regarding the number of neural networks within the proposed framework, their specific functions, and how they are trained, particularly in the case of the popularity network.
4) What is the ration behind the design of the reward in Equation 1? As the reward is determined by consecutive cache misses to the same cache slot, if that cache slot stores a popular video, the delay of reward for the popular video is much longer than the delay of reward in the situation of storing an unpopular video at the slot. This further indicates that the training data (i..e, the transition tuple (s, a, \tao, s’)) can be potentially imbalanced. 
5) How does the reference weight agent adapt to dynamic partner lists? If two EBSs are no longer pattern, it seems the corresponding action network parameter in the reference weight agent should be zero. Then, how do you enforce this when training the reference weight agent?
6) it is unclear how the proposed framework update reference partner list.
7) The training location and process of the RL agents and neural networks are not detailed in the paper, and additional information is not provided. For example, what is the training convergence speed and time of the RL agents? What is the size of training data for different EBS domain. This is important as the edge server often has limited computation and storage resources. 
 3. The paper's evaluation results are not sufficiently robust or convincing. What is the reason to choose a cache size of 32? The caching size should be related to the total active video content number. Besides, the proposed framework should be evaluated on various caching size setting.
 4. The related work section misses literatures about multi-agent RL and multi-agent RL with knowledge distillation. Consider the following examples:
Leonardos, Stefanos, et al. "Addressing Out-Of-Distribution Joint Actions in Offline Multi-Agent RL via Alternating Stationary Distribution Correction Estimation." Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023.
Tseng, Wei-Cheng, et al. "Offline Multi-Agent Reinforcement Learning with Knowledge Distillation." Advances in Neural Information Processing Systems 35 (2022): 226-237.
Gao, Zijian, et al. "KnowSR: Knowledge Sharing among Homogeneous Agents in Multi-agent Reinforcement Learning." arXiv preprint arXiv:2105.11611 (2021).

### Questions
See questions in the Weakness section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a DRL video caching mechanism at the edge level with knowledge transfer capabilities among edge base stations (EBS). Using real-dataset, the authors analyzed the data and observed that caching is affected by the sparsity of request distribution (temporal and spatial drifts) at the edge caches, thus KD-based approach is proposed for sharing the requests and drift knowledge among EBSs. Evaluation results show improvement in terms of cache hit rates compared to some approaches, e.g. LRU, LFU, ..etc.

### Strengths
- Real dataset is used and some insights from data are provided 
- Using RL to model the evicting policy and decides which file to evict.
- Nice problem and good visualization. 
- Very detailed evaluation results and a good combination of KD sharing and DRL algorithm.

### Weaknesses
 - The DRL formulation is not capturing some key factors of streaming systems dynamics including different video file-size distribution and EBS heterogeneities.
- DRL state representation seems to only look at one aspect - the file request in a given past window and does not account for other factors such as its retrieval time (latency), size, popularity ...etc. Size and retrieval time are both important factors and will play a role in transition from one state to another. How the proposed model will change accordingly?
  - For example, one big file needs to replace a few small files and thus the action will change (action will no longer be binary but rather will need to span a few entries in the action matrix and hence the action will be very hard (combinatorial problem) - which video files to evacuate in order to place the new big file)
- Reward seems to be designed to only capture the local reward and no global term. How to ensure consensus in terms of convergence? No convergence analysis is provided.
- Scalability and scaling the algorithm to cover the more general form of different file sizes and servers differences will make the state space and action space (NP Hard, comb. problem) very large and thus very complex to solve. 
- Each EBS serves a distinct region (no overlap, as per the paper) and optimizing each EBS individually should be sufficed in my opinion. How sharing among servers will help here?
- How is the three defined temporal metrics related to video file arrival rate?. Why not adopting arrival rate instead since it is widely used and correlate/encapsulate at least two of these three metrics?

### Questions
Please check the questions in the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates collaborative edge caching in spatiotemporal data-drifting edge scenarios. Through the analysis of real-world measurement data, the authors observed correlations in requests across both spatial and temporal dimensions. They also observed a notable relationship between the volume of requests and the Cache Hit Ratio (CHR). Leveraging these insights, they introduced an adaptive collaboration framework named KDCdCEC. Extensive experiments, including comparisons with existing strategies, show the efficacy of their proposed approach. The paper further provides how KDCdCEC dynamically adapts its caching strategies based on user activity variations and domain-specific characteristics.

### Strengths
-	This paper proposes a novel approach to handle cache performance in spatiotemporal data-drifting edge scenarios. The paper’s attention to both request-dense and request-sparse domains provides a more intricate understanding of caching dynamics, differentiating it from conventional generalized solutions.
-	By analyzing real-world measurement data, the authors ensure that their findings and proposed solutions are grounded in actual user behaviors and scenarios. The proposed KDCdCEC framework has been rigorously tested against other strategies, providing a comprehensive view of its efficiency and superiority. 
-	Addressing the collaborative edge caching problem in the context of spatiotemporal data drift is highly relevant, especially in an era where data is continuously generated, and its patterns of access constantly evolve. Further, this paper’s findings could have practical implications, potentially influencing how edge caching is approached in various real-world scenarios, from tech hubs to university zones to parks.

### Weaknesses
 - In the system model, the state representation includes the number of requests over intervals for C cached videos and the top-C videos selected based on their feature modulus from the uncached pool. This approach might miss out on caching videos that are about to become popular, especially if their current feature modulus isn't among the top-C. The use of feature modulus, while seemingly capturing some aspects of video popularity, might not be the most reliable indicator of future demand, especially when considering the dynamic nature of content popularity. The paper does not provide a clear justification for equating the number of uncached videos considered to the number of cached videos (C) in the state representation, nor does it explain why the number of requests is the sole feature considered for state representation, potentially omitting other relevant factors influencing caching decisions, such as video recency or content type.
- The paper could benefit from a more rigorous complexity analysis of the proposed framework, specifically detailing its computational complexity in terms of time and space requirements, and how these scale with the number of edge nodes, videos, and users. Furthermore, a comparison with other algorithms in terms of complexity would be valuable. Understanding the overhead of the proposed approach is crucial for assessing its feasibility in real-world systems, especially those with limited resources. The current experiments on traffic cost, while informative, do not fully address the computational and memory requirements of the algorithm itself.
- The paper could be enhanced by explicitly discussing its limitations and potential direction for future work. This should include a discussion on the sensitivity of the proposed approach to different parameters, and scenarios where it might not perform optimally. A more thorough exploration of alternative features beyond just the number of requests, such as user preferences or video metadata, should also be considered. Providing such discussions would give readers a more comprehensive view and could guide subsequent research in this area.

### Questions
-	To improve readability, it might be helpful to  re-locate Figures 1 and 2 to their references in Section 2-1, even though they are currently located in Section 1.
-	In eq. (1), the terms r^i_t and r^j_t are defined as the cumulative numbers of requests to the content in i-th cache slot and j-th candidate video sequence, respectively. It might be clearer to use distinct notations for each, to avoid potential confusion between the cache slot and the candidate video sequence.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Edge base stations (EBS), a cost-effective algorithm, is a well solution to address network congestion and quality decline caused by explosive growth of video content streaming. To tackle this issue, the authors proposed KDCdCEC, an adaptive knowledge-distillation based cross-domain collaborative edge caching framework to overcome the temporal drift and spatial drift in the caching data simultaneously. The authors fully analyzed and verified the data and experiments, but there is a high degree of redundancy in writing and poor sense of paragraph hierarchy.

### Strengths
1. The research topic and method have practical significance and can effectively reduce the network congestion problem.
2. The authors measure and analyze the video requests in the real world, and the experimental results verify the effectiveness of their method.

### Weaknesses
1. The methods compared in the articles are all before 2020, so they are not timely and persuasive. It’s better to compare it with the latest methods, such as Edge Caching or KD related.
2. Many of the hyper-parameters are given directly, without explanation and associated hyper-parameter analysis experiments.
3. The readability of the article is not good, and the framework of the overall model may be better explained in the main content.
4. For data analysis, the author proposed temporal drift and spatial drift, and designed different algorithms for them respectively. However, the experimental analysis lacks a stronger explanation for temporal and spatial, or the lack of relevant results indicates whether each part is right.

### Questions
How exactly is the data collected and will it be used as a public data set?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
