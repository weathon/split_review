# Beyond Predefined Depots: A Dual-Mode Generative DRL Framework for Proactive Depot Generation in Location-Routing Problem

- Decision: Reject
- Avg Score: 4.25
- Scores: 1, 8, 5, 3

## Abstract
The Location-Routing Problem (LRP), which combines the challenges of facility (depot) locating and vehicle route planning, is critically constrained by the reliance on predefined depot candidates, limiting the solution space and potentially leading to suboptimal outcomes. Previous research on LRP without predefined depots is scant and predominantly relies on heuristic algorithms that iteratively attempt depot placements across a planar area. Such approaches lack the ability to proactively generate depot locations that meet specific geographic requirements, revealing a notable gap in current research landscape. To bridge this gap, we propose a data-driven generative DRL framework, designed to proactively generate depots for LRP without predefined depot candidates, solely based on customer requests data which include geographic and demand information. It can operate in two distinct modes: direct generation of exact depot locations, and the creation of a multivariate Gaussian distribution for flexible depots sampling. By extracting depots' geographic pattern from customer requests data, our approach can dynamically respond to logistical needs, identifying high-quality depot locations that further reduce total routing costs compared to traditional methods. Extensive experiments demonstrate that, for a same group of customer requests, compared with those depots identified through random attempts, our framework can proactively generate depots that lead to superior solution routes with lower routing cost. The implications of our framework potentially extend into real-world applications, particularly in emergency medical rescue and disaster relief logistics, where rapid establishment and adjustment of depot locations are paramount, showcasing its potential in addressing LRP for dynamic and unpredictable environments.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper focuses on a DRL framework for location routing problems in which potential depot locations are not fixed a priori but can be freely determined in a continuous plane. The authors propose a generative DRL approach that generates potential depots and subsequently derives an LRP solution.

### Strengths
see weaknesses

### Weaknesses
I am afraid to write such a negative review, which will clearly be a disappointment for the authors, but in my opinion this paper should not be published for the reasons outlined below. I hope that my concerns will still help the authors to refine their research in the future.

1) As the authors point out in the literature review part of their work, research on solving LRPs without predefined depot locations is very scarce. From my experience in academia and practice, there is a good reason why this research is scarce: solving an LRP without predefined depot locations is a problem that is hardly of interest to the underlying applications.
The depots which are placed when solving an LRP are typically warehouses or logistics hubs. Suitable locations for such buildings are usually sparse, which is why there always exists a predefined discrete set of potential locations, which makes the problem proposed by the authors obsolete. 
If one wants to identify suitable regions for depots, one usually solves a facility location problem and uses a cost approximation for routing costs as in such a setting where the problem is solved in a continuous plane, the error made by placing the depot locations at points that are not available as a location is high and outweighs a potential accuracy win on getting accurate routing costs.

2) While I believe that utilizing DRL for vehicle routing problems is still in its infancy and holds potential for many promising research contributions, I doubt that aiming to solve strategic planning problems with similar methodologies for two reasons: first, when solving a strategic problem the sunk costs are very high. In this case, one favors solution quality and accuracy, realized in classical combinatorial or robust optimization approaches, over fast decision-making, which is the main advantage of a DRL approach. Second, while one can easily create many training instances for an operational problem by collecting daily or hourly data, this is different for a strategic problem that is solved once every 10 to 20 years. I do not see any reasonable way to create the 1,280,000 instances the authors require for training.

Ignoring the unrealistic training process, a superior solution quality could justify the method proposed by the authors from a purely academic perspective. However, the reported solution quality is inferior to that of existing classical approaches. Here it might be worth mentioning that the reference solutions claimed to be the state of the art by the authors are roughly 15 years old. Many papers have improved upon these so that the gap between the proposed methodology and the actual state of the art is much larger.

Based on these main concerns, I see neither a pracitcal nor an academic value in the work proposed and recommend to not publish it.

### Questions
see weaknesses

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a DLR approach for the Location-Routing Problem that generates possible depot locations either in an exact way (by proposing exact locations for the depots) or in a probabilistic way (by providing a Gaussian probability distribution where depot locations can be efficiently sampled). The DLR approach employs a multi-head attention model as a critic model which is capable of assessing the depots generated by the generative model. The approach is tested extensively on synthetic and real data and compared to other approaches in the literature.

### Strengths
The paper is very dense (probably conditions by the page limits) but the authors make a rather good job in providing a clear overview and a good discussion. The quality of the paper is high, as the experiments and the results shown are able to capture a wide range of the implications of the approach. The experiments are extensive and all important details and parameters are provided.
The novelty of the presented approach is mainly driven by the generative approach used for generating depot locations alongside the routes for each problem instance. The authors do overall a good job in motivating the novelty of their contributions.

### Weaknesses
Although the appendix provides the pseudocode for the main components of their approach, source code is missing. This could hinder the ability to reproduce the results obtained.
The authors, probably due to the page limits, seem to be forced to reduce the size of the tables and the figures in the main text considerably, which negatively affects the quality of the exposition. For instance, the font size in tables is very small, making it difficult to read and compare values, and the plots in figures lack sufficient resolution to discern finer details. This is particularly problematic when trying to understand the nuances of the experimental results.
In general, one cannot dismiss the impression that the authors are not only providing technical details in the appendices, but also including content that would have gone into the main text were it not the page limits. This impression gets reinforced specifically in B.4 where authors address limitations and future work, two topics that typically included into the main text and not in the appendices. In the introduction, there is no overview of the structure of the paper as usual.

### Questions
- In Table 1 and Table 3 what is the meaning of boldface and asterisk? It cannot be best result so far, as e.g. in Table 3 different results for the same row are marked with asterisk. The authors could better explain this in the caption or in the main text.
- Figure 2 is rather small, it would be helpful to increase size if page limits allow for this.
- I strongly recommend to include a link to publicly available source code to increase the reproducibility of the study.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a deep reinforcement learning framework to address the location-routing problem (LRP) for the situation where there are no predefined depot candidates. The framework includes two models: 1. depot generative model (DGM) that generates depots either deterministically or as a multivariate Gaussian distribution for sampling, and 2. multi-depot location-routing attention model (MDLRAM) that   takes the generated depots and the customer requests, and outputs the routing solution to minimize the cost. The authors claim that the main advantage of using the proposed framework lies in the flexibility and the inference speed: the modular framework can be used together or individually, adapted to different scenarios, proactively propose depot placement on the fly, and gives solutions to the routing problem faster.

### Strengths
1. Originality: the paper solves a novel LRP problem where there are no predefined depot candidates.
2. Quality: the paper motivates the methodology pretty well. The experimentation and validation of the method seems to be quite rigorous: the paper contains comprehensive evaluation of the framework across different datasets and problems of different scales. It also compares the proposed method with various baselines including exact method.
3. Clarity: the paper provides a clear explanation of the framework. The description of the models is detailed, including structure, objective functions, and training strategy.
4. Significance: the paper has the potential for large impact as it studies a less-studied problem, i.e., LRP without predefined depot candidates.  for the research community, there could be follow-up works on the problem. for real-world applications, the authors also made the case that for use cases including medical rescue and disaster relief, the ability to proactively generate new depot locations is beneficial.

### Weaknesses
1. The design of MDLRAM seems to be less supported by the motivation of the paper: the paper stresses the importance of proactively generating depot candidates for flexibility. However, the MDLRAM is a fixed model that takes in a fixed set of customers and depots as input and outputs the routing solution. There is no flexibility provided for changing depots or dynamically planning the routing as the DGM is generating the depots. Considering that the performance of MDLRAM is also inferior to SOTA method, it's unclear what major advantage MDLRAM brings. The lack of adaptability in MDLRAM directly contradicts the stated goal of flexible depot selection, as it cannot respond to changes in depot locations generated by the DGM in an iterative or dynamic manner. The model's inflexibility limits its practical use in scenarios where real-time adjustments are necessary.
2. A potential design flaw in the experiments could be that the evaluation of the DGM model depends on the score given on the MDLRAM model. This could potentially introduce bias since the DGM model is trained to score well for the MDLRAM while the MDLRAM does not provide exact solution or SOTA solution. The DGM is essentially optimized to perform well under the constraints and biases of the MDLRAM, rather than towards a globally optimal solution. This dependence raises concerns about the generalizability of the DGM's performance when evaluated with a more accurate or different routing solver. The evaluation process may not accurately reflect the true quality of the generated depot locations.
3. Randomly generating the depot locations seems to be too weak of a baseline. The heuristics mentioned in the Related Works seems to better candidates. The use of random depot generation as a baseline fails to adequately challenge the proposed DGM. Heuristic methods, which incorporate problem-specific knowledge, would provide a more meaningful comparison and better demonstrate the advantages of the DGM. The current baseline does not sufficiently highlight the potential benefits of the proposed approach.

### Questions
1. What is the motivation for MDLRAM? If performance is needed to serve as a good critic model for training DGM, why not use the SOTA method? If flexibility is needed, why not design a more end-to-end framework to connect DGM and MDLRAM and dynamically generate depots and plan routing accordingly.
2. For the evaluation of MDLRAM, for the synthetic data and real-world data settings, different sets of baselines seem to be chosen for comparison. Why is that? The description for the baselines for the synthetic data setting also seems to be lacking. What are ALNS, GA, TS referring to?
3. How would the DGM-Gaussian mode provide more flexibility when compared with the exact mode? Could the authors provide an example of a use case  for the Gaussian mode to motivate it more?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a generative deep reinforcement learning (DRL) method for solving an integrated location-and-routing problem in transportation and logistics. It tests the results using synthetic and real-world datasets.

### Strengths
The authors try to apply methods from the machine learning and artificial intelligence (ML/AI) domain to provide efficient and intuitive results for classical NP-hard location-and-routing problem in Operations Research. The paper aims to overcome the computational challenges of traditional optimization models and approaches through model-free approaches.

### Weaknesses
While the paper aims to bridge the ML/AI and traditional optimization via solving a specific classical problem in transportation, the design of the DRL-based method is mainly heuristic driven. The paper is more close to an academic exercise, rather than an in-depth study. It involves a depot generative model that uses demand information to sample depot locations, and a critic model that scores the generated depot locations to further output location-routing solutions. The motivation behind such a two-module design is missing and by having the two separated procedures (i.e., location and then routes), the optimality of the solutions based on the Deep Reinforcement Learning for the integrated location-routing problem does not seem to be guaranteed anymore. The paper also lacks theoretical analysis about the optimality bound guarantee nor the efficiency of the algorithm. The training strategies are also ad hoc and do not have a firm theoretical ground.

At a high level, while location-routing is a class of classical transportation problems, the version considered in this paper is not considered state of the art, and the literature now has been focusing on optimizing location solutions and controlling dynamic routes (in an online fashion) under uncertain demand and route information. Therefore, how the proposed methods add to the existing knowledge is not clear to me.

### Questions
1.	How the proposed DRL based method compares with classical discrete optimization solutions for location-routing problem?  Any theoretical optimality guarantee that one can prove (even under special problem structures or networks)? 
2.	The numerical studies are comparing with other three approaches from papers using either heuristics or branch and cut published in years 2006, 2009, 2011, for different sizes of networks, but these are not recent work in the related literature and cannot represent the state-of-the-art. Any benchmarks with methods published more recently? 
3.	Can the DRL handle very large-scale instances? What is the solution quality and computational efficiency tradeoff? 
4.	Why deep reinforcement learning? The motivation and connection of DRL with location-routing are not sufficient nor clear.

### Soundness
2

### Presentation
2

### Contribution
2
