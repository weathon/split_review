# INS: Interaction-aware Synthesis to Enhance Offline Multi-agent Reinforcement Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Data scarcity in offline multi-agent reinforcement learning (MARL) is a key challenge for real-world applications. Recent advances in offline single-agent reinforcement learning (RL) demonstrate the potential of data synthesis to mitigate this issue.
However, in multi-agent systems, interactions between agents introduce additional challenges. These interactions complicate the synthesis of multi-agent datasets, leading to data distortion when inter-agent interactions are neglected. Furthermore, the quality of the synthetic dataset is often constrained by the original dataset. To address these challenges, we propose **INteraction-aware Synthesis (INS)**, which synthesizes high-quality multi-agent datasets using diffusion models. Recognizing the sparsity of inter-agent interactions, INS employs a sparse attention mechanism to capture these interactions, ensuring that the synthetic dataset reflects the underlying agent dynamics. To overcome the limitation of diffusion models requiring continuous variables, INS implements a bit action module, enabling compatibility with both discrete and continuous action spaces. Additionally, we incorporate a select mechanism to prioritize transitions with higher estimated values, further enhancing the dataset quality. Experimental results across multiple datasets in MPE and SMAC environments demonstrate that INS consistently outperforms existing methods, resulting in improved downstream policy performance and superior dataset metrics. Notably, INS can synthesize high-quality data using only 10% of the original dataset, highlighting its efficiency in data-limited scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses data scarcity in offline multi-agent reinforcement learning (MARL), emphasizing the unique challenges in synthesizing high-quality multi-agent datasets due to complex inter-agent interactions. The authors propose Interaction-aware Synthesis (INS), a method that uses diffusion models with sparse attention to accurately model these interactions and a bit action module to support both discrete and continuous actions. INS also includes a selection mechanism to prioritize high-value transitions. Experiments in MPE and SMAC environments show that INS outperforms current methods, enhancing downstream policy performance and dataset quality. Remarkably, INS can synthesize effective data using only 10% of the original dataset, demonstrating its efficiency in data-scarce scenarios.

### Strengths
- The paper was well-written. It's easy to understand the motivation, contributions, and methodology of the proposed work
- Collecting datasets for multi-agent reinforcement is hard. Also, generating datasets in the multi-agent scenario is non-trivial due to the difficulty of modelling the interaction between the agents.
- The experiments are complete and promising.

### Weaknesses
 - In terms of novelty, the proposed solution looks like simply applying a diffusion model for generating trajectories with additional attention mechanisms across the agents, which is a lack of novelty.



### Questions
- Is the proposed approach scalable in terms of a large number of agents?
- It seems that the objective of the trajectory generation process only guarantees whether the generated trajectories are realistic or not. There is no mechanism to implicitly guide the diffusion model to enhance the quality of the trajectories (accumulated rewards of trajectories).

### Soundness
3

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
4

### Summary
This paper introduces INS, a method for synthesizing high-quality multi-agent datasets to enhance offline multi-agent reinforcement learning. INS leverages diffusion models and incorporates a sparse attention mechanism to capture inter-agent interactions, ensuring the synthetic dataset reflects the underlying agent dynamics. The method also includes a select mechanism to prioritize high-value transitions, improving dataset quality. The experimental results demonstrate the effectiveness of INS.

### Strengths
- The paper is well-organized.
- Considering both dataset diversity and high-value transitions is valuable.

### Weaknesses
 - On Line 087, the authors claim that "INS is the first data synthesis approach for offline MARL." However, on Line 118, in the related works section, the authors mention that "recent studies extend diffusion models to the MARL domain, applying them to trajectory generation [1]." This statement suggests that the authors are not the first to engage in data synthesis work within the offline MARL domain. Furthermore, upon reviewing the relevant literature, the reviewer found additional papers that have also conducted data generation tasks in offline MARL [2]. Therefore, the reviewer believes that the authors have overclaimed their contribution. It is important to acknowledge the pioneering work in the field, and the authors should provide a more accurate representation of their contribution in relation to prior art.

 - The authors claim to introduce a sparse attention mechanism to capture inter-agent interactions, utilizing the method sparsemax, which was originally proposed in the NLP field. However, upon reviewing the literature, the reviewer found that sparsemax has already been applied in the MARL domain [3,4], reducing the novelty of this aspect of the work. Furthermore, the formulation of the sparsemax (equations 3-6) shows overlap with [4]. The authors should acknowledge the existing use of sparsemax in MARL and clarify how their implementation differs from or improves upon previous applications. A detailed comparison with related works would strengthen the paper's contribution and novelty.

 - The authors propose the use of Bit Action as an alternative to one-hot action representation for action generation. However, the reviewer has a concern regarding the orthogonality of each action in the Bit Action representation. Non-orthogonal actions may lead to ambiguity in the action space, potentially affecting the outcomes.

 - The selection proportion parameter in the authors' method lacks flexibility and requires tuning for different tasks.

 - The synthetic method comparison is limited to SynthER. A more comprehensive comparison should be conducted, including both single-agent methods mentioned in the related works and multi-agent methods [1,2].

### Questions
See Weaknesses.

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
The paper makes a significant high-level contribution by extending data synthesis from single-agent reinforcement learning (RL) to multi-agent reinforcement learning (MARL), which is an important advancement. However, I have some concerns and suggestions.

### Strengths
The paper represents the first attempt to apply data synthesis techniques to multi-agent reinforcement learning (MARL). The experiments are carefully designed and provide strong support for the proposed method. Additionally, the writing is clear and accessible, making the paper easy to follow.

### Weaknesses
See questions.

### Questions
1.Clarity of Motivation: The detailed motivation for addressing the unique challenges of data synthesis in MARL seems somewhat unclear. While agent interactions are indeed a key issue, other challenges such as partial observability and environmental non-stationarity also play significant roles. I encourage the authors to delve deeper into these challenges and explain how their proposed method tackles them.

2.Modeling Agent Interactions: Relying solely on an attention mechanism to model agent interactions may be overly simplistic. In the MARL domain, modeling agent relationships is a complex and standalone research topic. Would employing more sophisticated methods for agent relationship modeling enhance the model's effectiveness? 

3.Generation of Global States: I noticed that the generated data includes joint actions and joint observations but seemingly not the global state. How is this generated data applied to value decomposition models like QMIX that require global state information? 

4.Consistency with Environment Dynamics: How does the method ensure that the generated data conforms to the environment's dynamic model? If the generated state transitions are invalid, could this negatively impact the pre-training process? I recommend including theoretical analysis or experimental results to demonstrate the validity and effectiveness of the generated data.

5.Computational Efficiency: Utilizing diffusion models in MARL might introduce computational efficiency challenges. Could the authors provide experimental data or analysis to illustrate the computational efficiency of the proposed method?

Overall, the research shows potential, but addressing the above issues is essential to enhance the credibility and impact of its contributions.

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
4

### Summary
In this paper, the authors propose INS, a novel multi-agent reinforcement learning (MARL) data synthesizer aimed at enhancing the performance of offline MARL algorithms. INS leverages a diffusion model to generate synthetic data and employs a sparse attention architecture and a value-based selection mechanism to improve the data quality. Compared to the naive extension of a single-agent diffusion-based data synthesizer to multi-agent tasks (MA-SynthER), INS demonstrates significant improvements.

### Strengths
- The paper is clearly presented and easy to follow. The idea is simple yet effective.
- The authors made several incremental improvements (Bit Action, Sparse Attention, Value-Based Selection) to progressively transform SynthER into INS. The motivation and methods for each improvement are convincing and predictably effective.
- In the ablation studies, the authors use many figures and tables to illustrate the contribution of each improvement and explain the reasons behind these gains. This level of detail provides valuable insights for future research.

### Weaknesses
 - In my view, the novelty is somewhat limited. INS is essentially an improved version of SynthER in the MARL context, and the ideas of sparse attention and value-based selection are neither difficult to conceive nor novel, as these methods have already been widely applied.
- The experimental results are somewhat disappointing. First, many results in Table 1 do not show significant improvements over MA-SynthER. For example, in the SMAC-8m-good task, while the mean score improves by 0.1, the standard deviation is around 1.0, making the increase in the mean unconvincing. Second, SynthER has demonstrated its ability to significantly improve the sample efficiency of Online RL in the experiments. Including similar experiments for INS would help enrich the paper’s content and better showcase its capabilities.

### Questions
- See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
