# SHIELD: Multi-task Multi-distribution Vehicle Routing Solver with Sparsity & Hierarchy in Efficiently Layered Decoder

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
Recent advances toward foundation models for routing problems have shown great potential of a unified deep model for various VRP variants. However, they overlook the complex real-world customer distributions. In this work, we advance the Multi-Task VRP (MTVRP) setting to the more realistic yet challenging Multi-Task Multi-Distribution VRP (MTMDVRP) setting, and introduce SHIELD, a novel model that leverages both sparsity and hierarchy principles. Building on a deeper decoder architecture, we first incorporate the Mixture-of-Depths (MoD) technique to enforce sparsity. This improves both efficiency and generalization by allowing the model to dynamically choose whether to use or skip each decoder layer, providing the needed capacity to adaptively allocate computation for learning the task/distribution specific and shared representations. We also develop a context-based clustering layer that exploits the presence of hierarchical structures in the problems to produce better local representations. These two designs inductively bias the network to identify key features that are common across tasks and distributions, leading to significantly improved generalization on unseen ones. Our empirical results demonstrate the superiority of our approach over existing methods on 9 real-world maps with 16 VRP variants each.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Multi-Task Multi-Distribution Vehicle Routing Problem (MTMDVRP), an extension of the MTVRP. The MTMDVRP effectively captures the complexities inherent in real-world industrial applications by incorporating various realistic customer distributions. To address these challenges, the authors propose a neural solver, SHIELD, which integrates soft clustering, Mixture of Experts, and Mixture-of-Depths (MoD), demonstrating remarkable generalization across various variants of VRP.

### Strengths
1.This paper introduces the MTMDVRP,, a variant of vehicle routing problems that aligns more closely with practical scenarios. 

2.By effectively combining MoE and MoD, and soft clustering, the proposed neural solver SHIELD demonstrates outstanding performance across a range of VRP variant tasks. 

3.The authors conduct extensive ablation experiments that involve nearly all modules, including MoD, MoE, and soft clustering, with detailed descriptions of the experimental procedures and results.

### Weaknesses
1. The meanings of $\mathcal{D}_t, z_t, t_t, l_t$ and $o_t$ in Figure 1 are not clearly defined. All symbols used in the figure should be adequately introduced in the text.


2. Section 4, Methodology, lacks clarity in its description and does not comprehensively explain the forward process of the model. First, in Section 4.3, the $k$ and $N-k$ are introduced, followed by $\beta$ and other components. However, the transition to $\beta$ feels abrupt, necessitating multiple readings for clarity. Additionally, the calculation of $\alpha_d$ in lines 312-319 appears abrupt, and the term $W_{\theta}^{T}$ is not sufficiently explained either beforehand or subsequently. I recommend that the authors reorganize the logic in Section 4 to facilitate a clearer understanding of the paper's core concepts.


3. As mentioned in the paper, the introduction of MoD and soft clustering enhances generalization; however, the generalization capabilities for larger-scale problems have not yet been tested. Therefore, I think the results of larger-scale experiments should be also presented. 


4. Although the effects of soft clustering are briefly discussed in lines 468-472, this section is concise and does not adequately explain the advantages of this method. I suggest that the authors provide a detailed experimental comparison between SHIELD-MoD and SHIELD to offer a more intuitive and in-depth understanding of the benefits introduced by this approach.

### Questions
1. Please refer to the weaknesses. I am particularly concerned about weaknesses 3 and 4.

2. I think the authors should provide a unified introduction to all symbols and mathematical notations used throughout the paper. For example, including a dedicated section for the Preliminary may significantly facilitate reader understanding.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new setting for the classic VRP problem called MTMDVRP and the proposes SHIELD, a novel architecture for solving the problem. SHIELD makes use of recent deep learning architecture to enforce sparsity in the network. Although the proposed method achieved good results on several dataset, the main claims are somewhat unjustified.

### Strengths
- The paper makes use of recent advances in deep learning architecture in VRP, an important problem.
- The paper proposes the multi-distribution setting for VRP. However, the lack of discussion leaves me uncertain about the importance of the new setting.

### Weaknesses
 - The multi-distribution setting is not described and discussed in enough detail although it is the main contribution of this paper. Why MTMD is important? How the distribution set $\mathcal{Q}$ is created and sampled? Where is the MD part in the training of SHIELD? 
- The benefits of MoD is hypothetical (line 285-288). The author did not provide evidence to their claims of the benefits of MoD. If they could show evidence of under- and over-processing of tokens lead to bad results, the paper would be stronger. 
- The finding in this paper seems to contradict that of MoD ((Raposo et al., 2024), the paper on which this paper is based on but the author didn't discuss it. Line 188 states that MoD makes the performance slightly worse but this paper report possitive result with MoD. 
- The reason for choosing the 9 countries is not stated in the paper. What is the performance of the proposed method on other countries in the dataset?
- It is unclear that the proposed method really improves OOD generalization. What I can see from the tables is that SHIELD performs well InD so it performs well OOD. Other methods seem to have the about same OOD - InD performance gap with SHIELD (table 1). From the data, it is hard to conclude that MoD improves OOD generalization. 
- There is no comparison on model size and speed. The author showed that by increasing the size of MVMoE, they can get better results. A natural questions is that whether the performance improvement of SHIELD simply due to its higher capacity? 
- The writing is not good. There are many hard to understand statements and incorrect uses of words. Instead of using complex words, I think the author should use simple language to clearly explain their ideas.

### Questions
Please address the questions and weaknesses in the previous section.

### Soundness
2

### Presentation
2

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
This paper studies the multi-task multi-distribution scenario of Vehicle Routing Problems (VPRs), and propose a new method from the perspective of sparsity. Specifically, it employs the Mixture-of-Depths (MoD) architecture in the decoder of neural solvers, which can select active layers for each token. Meanwhile, inspired by previous works on the benefit of clustering nodes for instance representations, it further extends the input of the decoder with additional information of the cluster centroids. Experiments show that compared with MVMoE, a previous work on multi-task VRPs, the proposed method can achieve better performance.

### Strengths
The writing of this paper is generally good. Experiments demonstrates the superior performance compared with previous method MVMoE.

### Weaknesses
1. The motivation of this paper is weak. The main contribution of this work is the introduction of MoD to the neural solvers for VRPs. However, MoE and MoD share similar ideas from the perspective of sparsity (MoE achieves sparsity on width and MoD achieves sparsity on depth), and the advantages of employing MoD instead of MoE in sub section 4.2 are not convincing. Specifically, the explanation that MoD allows for variable computation per token, while true, does not inherently justify its superiority over MoE, which also offers flexibility through different expert paths. The argument that MoD better aligns with the Information Bottleneck principle is not sufficiently supported by empirical evidence or a rigorous theoretical analysis. The provided visualizations in Figure 3 and 4 are not compelling, as the interpretations are subjective and lack quantitative backing. For instance, the claim that Figure 3 shows crucial decision-making steps requiring more compute is not clearly demonstrated, and the relationship between the three maps in Figure 4 is difficult to discern, making the conclusions drawn from them weak.
2. As the benefit of clustering nodes has already been discussed in previous works, the contribution of adapting it in the proposed method is very limited. The paper does not adequately explore the novelty of applying soft-clustering to the specific context of multi-task multi-distribution VRPs. While soft-clustering has shown promise in other domains, its integration here seems incremental without substantial new insights or adaptations that address the unique challenges of the proposed problem setting. The context-based prompt, while mentioned, is not detailed enough to understand its specific contribution beyond standard soft-clustering techniques.
3. As multi-task VRPs and multi-distribution VRPs have already been studied in previous works respectively, the necessity and challenges of the proposed multi-task multi-distribution VRPs should be discussed. Meanwhile, the specific advantages of the proposed method SHIELD on the scenario of multi-task multi-distribution should be better clarified. The paper does not convincingly demonstrate that the proposed method is uniquely suited for the combined multi-task multi-distribution scenario. The benefits of MoD and soft-clustering, while potentially helpful, do not inherently address the specific complexities arising from the combination of multiple tasks and distributions. The paper lacks a clear explanation of how these components interact to provide a synergistic advantage in this specific scenario.

### Questions
1. As computational efficiency is one of the main advantages of the employed MoD, what about the comparison inference time?
2. Is the proposed method SHIELD tailored for the scenario of multi-task multi-distribution? What about its performance on the scenario of multi-distribution?
3. What about the performance on problem instances with more than 100 nodes?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper propose a variant setting of VRP，which is called Multi-Task Multi-Distribution VRP (MTMDVRP). And it introduces an impressive learning model SHIELD, a neural solver that leverages sparsity through a customized NCO decoder with MoD layers and hierarchy through context-based cluster representation. At the same time, necessary experiments are conducted to support the model performance.

### Strengths
The authors of this paper consider the generalization of tasks and distribution in VRP at the same time, which is a good attempt. In addition, they proposed the innovative network learning architecture SHIELD, introduced the clustering layer to enhance the hierarchical expression ability of the model, and added the MoD layer in the decoding to take into account the sparsity, which is impressive in the field of machine learning to solve combinatorial optimization problems.

### Weaknesses
The new setting proposed in this paper adds additional expectations for distribution. I think this is not a very unique innovation, and it is essentially using different distribution instances of non-uniform distributions during training, which seems to naturally enable the model to perform well on other non-uniform distributions during the test stage. If it is only trained on uniform distribution, it will be more impressive to generalize to non-uniform distributions during the test phase. There is a crucial weakness that the solution time is not reflected in the experiment, which makes it difficult to understand the computational efficiency of the algorithm. What’s more, the baselines compared in the experiment are a bit small. There have been many works on VRP in top conferences in recent years, but they are not reflected in the baselines in this experiment. Specifically, the lack of comparison with other neural combinatorial optimization methods that also incorporate attention mechanisms or graph neural networks is a notable omission. The paper also lacks a detailed analysis of how the sparsity induced by the MoD layers impacts the solution quality and computational cost, beyond just stating that it improves sparsity. It would be beneficial to see a more granular analysis of the sparsity patterns and their correlation with performance.

### Questions
1 What computational complexity will the introduction of MoD layers and context-based cluster representation cause? Can the time for model solution be supplemented in the experiment? This is crucial to understand the computational efficiency of the algorithm. It is unacceptable to have no time measurement at all.
2 Can the latest work on VRP solution in recent years be supplemented in the baseline in the experiment?
3 In the new setting proposed in this paper, for the expectation of distribution q, does q obey a specific distribution or have a specific classification?
4 If the model is trained only on a uniform distribution, will it still perform well on a cross-distribution test? Can this be supplemented in the experiment?

### Soundness
2

### Presentation
3

### Contribution
3
