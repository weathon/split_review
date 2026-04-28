# HGM³: Hierarchical Generative Masked Motion Modeling with Hard Token Mining

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Text-to-motion generation has significant potential in a wide range of applications including animation, robotics, and AR/VR. While recent works on masked motion models are promising, the task remains challenging due to the inherent ambiguity in text and the complexity of human motion dynamics. To overcome the issues, we propose a novel text-to-motion generation framework that integrates two key components: Hard Token Mining (HTM) and a Hierarchical Generative Masked Motion Model (HGM³). Our HTM identifies and masks challenging regions in motion sequences and directs the model to focus on hard-to-learn components for efficacy. Concurrently, the hierarchical model uses a semantic graph to represent sentences at different granularity, allowing the model to learn contextually feasible motions. By leveraging a shared-weight masked motion model, it reconstructs the same sequence under different conditioning levels and facilitates comprehensive learning of complex motion patterns. During inference, the model progressively generates motions by incrementally building up coarse-to-fine details. Extensive experiments on benchmark datasets, including HumanML3D and KIT-ML, demonstrate that our method outperforms existing methods in both qualitative and quantitative measures for generating context-aware motions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work suggests a text-to-motion generation model, using the combination of three existing techniques:
1. Masked VQ-VAE in the motion domain:
    1. Hierarchical (MoMask by Guo et al., 2024)
    2. Masking based on confidence (Pinyoanuntapong et al. 2024b)
2. Hard token mining (HTM) in the imaging domain (Wang et al., 2023a)
3. hierarchical semantic graph representation in the language domain (Shi & Lin, 2019) + Graph Attention Network (GAT) (Velickovic et al., 2018)

------------------------------------
**Post rebuttal comment:**

Following the rebuttal, I am raising my score toward acceptance.

### Strengths
- Impressive and thoughtful choice of SOTA works.
- Clear writing (mostly).
- Reproducibility: implementation details are given and, more importantly, the authors plan to release their full code and setup.

### Weaknesses
 **Major weaknesses**

- Novelty: This work combines existing SOTA works (see "Summary" above). While this work demonstrates solid engineering execution in integrating existing techniques, its novel contribution to the field is questionable. Please discuss any new theoretical insights or algorithmic innovations beyond the integration of existing techniques. 
- Technical soundness: How is the loss of the residual transformer (L_res) incorporated into the overall network loss? Can you clarify the summation range in Eq. 1 of Sec. A.2? I believe it should be from i=1 to V. Could you provide a diagram showing the architectural flow between the masked and residual transformers?"
- Qualitative results: To fully assess the quality and naturalness of the generated motions, I recommend including a supplementary video. While the paper includes qualitative figures, they cannot be validated for dynamic motion artifacts such as jitteriness and foot sliding.
- Quantitative results: For most metrics, results are only marginally better and sometimes marginally worse. I would call that comparable. There is, however, a notable improvement for HML3D FID. 

**More weaknesses**

- Some technical descriptions need more clarification or need to be corrected (see "Questions" below).
- I suggest concatenating the supp to the main paper to allow mutual references and better reader experience. This is allowed in ICLR.

### Questions
Questions and Comments:

- Masked and residual transformers: Do they predict all tokens together (i.e., predict $\mathcal{M}$ tokens for the masked transformer and $n$ tokens for the residual one)? Or, are they causal? (by causal I mean that for the residual transformer, predict tokens according to their temporal order where each prediction is conditioned on the previously predicted tokens; for the masked transformer it probably means conditioning masked tokens on those already predicted). If the prediction is causal, then a prediction of an $n$ length motion requires an n-step loop, hence each iteration in Sec. 3.4 has an internal loop within it. Please explain.
- L209.5 Eq. 4): Rephrase. it seems you wanted to describe k and M, but described M only.
- L220 (Eq. 5):  The L_pred objective focuses on ranking losses by relative magnitude rather than exact values. Therefore, $\hat{\ell}$ (and G) should be interpreted as predicting the values with the topological ordering of token losses, not as estimating the precise reconstruction loss. 
- L249: "At each step": do you mean "at each epoch"? The index k is related to epochs (L242), not to steps.
- L 249: Does it mean $\mathcal{M} = \gamma(\tau_k)\cdot n$ ? I don't see anywhere in the paper how $\mathcal{M}$ is defined.
- L339: where is the probability distribution taken from?
- Sec. A.2, A.3: Fig. 2 depicts the residual transformer in one block, in blue Fig. 3 depicts the same blue block multiple times, but relates to it as sub-blocks of the residual transformer from Fig. 2. This is misleading. Please clarify the differences and similarities between the sub-blocks and make their notation more consistent.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors investigate the hard token learning challenge within MoMask's native training scheme and enhance the model's text comprehension by integrating hierarchical textual conditions. Experiments and ablations demonstrate that this implementation improves MoMask's performance.

### Strengths
This paper has the following strengths:

- Introduce the Hard Token Mining (HTM) into the motion generation task for the first time and prove its effectiveness.
- Design a Hierarchical Generative Masked Motion Model (HGM$^3$) and use the text conditions with different granularity to enhance the text-motion matching performance.
- Qualitative and quantitative results demonstrate the effectiveness of the proposed method.

### Weaknesses
For weaknesses, I have the following comments:

- From an innovation perspective, it’s quite limited. The overall pipeline of the paper is essentially a **replica** of Hard Patches Mining (Wang et al., CVPR 23), merely validated for effectiveness in motion generation. The core idea of masking hard tokens based on reconstruction loss is directly adopted, and the architectural modifications seem incremental. The paper lacks a detailed analysis of how the specific characteristics of motion data necessitate changes to the original Hard Patches Mining framework, beyond simply applying it to a new domain. A more thorough investigation into the unique challenges of motion data and how the proposed method addresses them would be beneficial.

- As for the proposed Hierarchical Text Graph, while providing more textual information obviously enhances the model's text-motion alignment, a more straightforward approach like using CLIP token-level features would likely be more effective and simpler than this **complex** method (parsing, CLIP, graph, etc.). The paper does not adequately justify the necessity of the graph structure, especially given the potential for simpler alternatives. The use of a Graph Attention Network (GAT) adds further complexity, and the paper does not provide a clear explanation of why this specific architecture is superior to other methods for incorporating token-level features. If the performance of using CLIP token-level features is inferior to the Hierarchical Text Graph, please provide a comparative experiment to demonstrate this.

-  This paper is a well-executed A+B **technical report** with clear and complete experiments, but it offers limited practical value for real-world applications. The experiments, while thorough, primarily focus on quantitative metrics and lack a compelling demonstration of how the generated motions translate to real-world scenarios. The paper would benefit from a more in-depth discussion of the potential applications and how the proposed method addresses the specific needs of those applications.

### Questions
Could Figure 4 show more examples and include **heatmaps of the distribution of the predicted reconstruction loss**, like in Hard Patches Mining (Wang et al., CVPR 23)?

Missing cites:
- MotionGPT: Human Motion as a Foreign Language
- MotionLCM: Real-time Controllable Motion Generation via Latent Consistency Model
- StableMoFusion: Towards Robust and Efficient Diffusion-based Motion Generation Framework
- Mofusion: A framework for denoising-diffusion-based motion synthesis

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper works on the text-to-motion task and proposes two modules to specifically enhance the generative masked modeling-based motion generation. The first contribution is to apply a hard-mining training strategy to replace random masking when training the masked transformer, which facilitates the model to better generate the hard motions. Another contribution is using a graph-based hierarchical text embedding to replace the CLIP text embedding, which provides a better semantic understanding and leads to improved generation quality. Experiments show that the proposed two modules lead to better quantitative and qualitative results compared to the baselines.

### Strengths
1. This paper proposes a hard-token mining training strategy that uses additional networks to predict masks of the hard-to-predict tokens. Compared to the random masking strategy used in previous generative masked modeling-based motion generation works, this hard-mining strategy effectively facilitates the models to learn the hard motions.

2. The proposed hierarchical graph-based semantic embedding provides an enhanced text embedding compared to the CLIP text encoder embedding used in previous works. The proposed hierarchical semantic embedding well captures both the fin-grained and global semantics, leading to improved generation results.

3. Experiments show that the proposed two components can effectively enhance the generation quality of generative masked modeling-based methods, and outperforms the baselines both qualitatively and quantitatively.

### Weaknesses
1. This paper proposes two components that can specifically enhance generative masked modeling-based motion generation. Although the proposed components are effective, there is not much new knowledge from this paper.  Hard mining is used in the cited reference Hard Patch Mining (HPM) (Wang et al., 2023a) for the image domain and it employs a teacher-student model that transitions from completely random masking to focusing on difficult image patches, in the same spirit as this paper. The hierarchical graph-based embedding is proposed in the reference Act As You Wish, Jin et al. (2024) and proved effective for diffusion-based text-to-motion. This paper applies these two methods to the niche problem of masked modeling-based text-to-motion and achieves enhanced performance.

2. As a motion generation work, this submission does not include any video or animation visualization of motion results. I would strongly suggest including some video results, at least for the sequences presented in Figures 3, 4, and Appendix C.

3. Some technical details regarding text conditioning require further explanation. Line 205 states that the text embedding is from CLIP,  but from other sections I infer that it should be the proposed hierarchical semantic embedding. Moreover, Appendix Figure 2 indicates that the residual transformer uses the text embedding directly from CLIP instead of the hierarchical embedding. What is the reason for not using the hierarchical semantic embedding? I would appreciate additional explanations of the text conditioning used in this work.

### Questions
1. The citations in the text of the submitted PDF do not contain clickable links, which makes it hard to match the in-context citation with the reference works. This is not a factor for grading but can make the life of reviewers easier.

### Soundness
3

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
4

### Summary
The paper introduces a novel framework with two main components: Hard Token Mining (HTM) and a Hierarchical Generative Masked Motion Model (HGM3). HTM focuses on difficult-to-learn motion areas, while HGM3 represents sentences with different levels of granularity, enabling contextually accurate motion generation by decomposing motion descriptions into hierarchical semantic graphs with three levels: motions, actions, and specifics. This global-to-local structure enables a deep understanding of motion descriptions and provides fine-grained control over motion generation. Experiments show that the propose method out perform state of the art methods for both HumanML3D and KIT dataset.

### Strengths
- This work is the first to integrate hierarchical semantic graphs into a masked motion model, offering an innovative approach in this area.
- The literature review effectively outlines the background on text-to-motion, masked motion models, and the challenges in existing methods.
- Comprehensive experiments with detailed comparisons.
- The experiments demonstrate that the proposed method achieves state-of-the-art (SoTA) performance across multiple datasets.

### Weaknesses
 - It is a bit confusing that $HGM^3$ is used both as the name of a component and as the name of the whole model ($HGM^3 + HTM$).
- $HGM^3$ component:
  - Since the main idea of $HGM^3$ is inspired by GraphMotion [1], it would strengthen the contribution if the authors could demonstrate the differences in applying GAT to a masked model.
  - The $HGM^3$ component is not well described. It is unclear how 1) motions, 2) actions, and 3) specific elements work within the Graph Attention Network. Specifically, how are these different levels of abstraction represented and processed by the GAT? Are they encoded separately and then combined, or are they integrated at the node level? The lack of clarity makes it difficult to assess the novelty of the approach.
  - There are no details provided on the "twelve types of edges representing various relationships between nodes" mentioned in Section 3.3. What are these edge types? How do they capture the relationships between motion, action, and specific elements? Without this information, it is hard to understand the graph structure and its impact on the model's performance.
- The visualization in Figure 4 is unclear. A few more samples (or a video supplement, if easier) may help clarify the results. The current figure does not provide sufficient insight into the quality of the generated motions, particularly how well they align with the input text descriptions.
- It is unclear if the model truly requires a student-teacher architecture. (I don’t fully understand this part—I’ve also addressed this in the questions section.)

### Questions
- HTM?
  - What is the output of HTM? What is the different between G(student) and F(student) models?
  - What is the motivation of student-teacher architecture? To prevent model collapse? If yes, I think it's better to have ablation study on this.
- $HGM^3$
  - How the integration of Graph Reasoning to masked model is different from GraphMotion?
  - Does Motion-Action-Specific embeddings applied to Residual layers?

### Soundness
3

### Presentation
2

### Contribution
2
