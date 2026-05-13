# DREAM: Dual Structured Exploration with Mixup for Open-set Graph Domain Adaption

- Decision: Accept
- Scores: 8, 8, 3, 5, 8

## Abstract
Recently, numerous graph neural network methods have been developed to tackle domain shifts in graph data. However, these methods presuppose that unlabeled target graphs belong to categories previously seen in the source domain. This assumption could not hold true for in-the-wild target graphs. In this paper, we delve deeper to explore a more realistic problem open-set graph domain adaptation. Our objective is to not only identify target graphs from new categories but also accurately classify remaining target graphs into their respective categories under domain shift and label scarcity. To solve this challenging problem, we introduce a new method named Dual Structured Exploration with Mixup (DREAM). DREAM incorporates a graph-level representation learning branch as well as a subgraph-enhanced branch, which jointly explores graph topological structures from both global and local viewpoints. To maximize the use of unlabeled target graphs, we train these two branches simultaneously using posterior regularization to enhance their inter-module consistency. To accommodate the open-set setting, we amalgamate dissimilar samples to generate virtual unknown samples belonging to novel classes. Moreover, to alleviate domain shift, we establish a k nearest neighbor-based graph-of-graphs and blend multiple neighbors of each sample to produce cross-domain virtual samples for inter-domain consistency learning. Extensive experiments validate the effectiveness of the proposed DREAM in comparison to various state-of-the-art approaches in different settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes DREAM for open-set graph domain adaptation, which incorporates a graph-level representation learning branch as well as a subgraph-enhanced branch to jointly explores graph topological structures from both global and local viewpoints.

### Strengths
1.	The problem of open-set graph domain adaptation is novel.
2.	The paper is well organized and clearly written.
3.	The proposed method is clever and interesting.

### Weaknesses
1. The format of references is not uniform, such as [4] and [5]. This should be addressed to adhere to the conference's style guidelines.

2. The paper introduces open-set graph domain adaptation, but it does not clearly delineate the distinctions between this problem and the more general universal domain adaptation (UDA). While both address domain shifts, UDA typically deals with scenarios where both source and target domains can have private, unknown classes. A more thorough discussion on how the proposed model, DREAM, might be extended or adapted to handle the more complex UDA setting would strengthen the paper. Specifically, how would the model account for the possibility of unknown classes in the source domain, a scenario not explicitly considered in open-set adaptation where unknown classes are assumed to only exist in the target domain?

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel method called DREAM for open-set graph domain adaptation, which aims to accurately classify target graphs into their respective categories under domain shift and label scarcity. DREAM incorporates a graph-level representation learning branch as well as a subgraph-enhanced branch, which jointly explores graph topological structures from both global and local viewpoints. The method also amalgamates dissimilar samples to generate virtual unknown samples belonging to novel classes and establishes a k nearest neighbor-based graph-of-graphs to alleviate domain shift. Extensive experiments demonstrate the superiority of DREAM over state-of-the-art methods.

### Strengths
1. Novelty: The paper introduces a new problem of open-set graph domain adaptation, which accommodates unlabeled in-the-wild target graphs from unseen classes. The proposed method, DREAM, is a novel approach that employs two branches to investigate structural semantics and integrates them into a trustworthy and domain-invariant framework. 
2. Effectiveness: The paper demonstrates the remarkable effectiveness of DREAM when compared to state-of-the-art methods in various challenging scenarios. In particular, the performance gain of DREAM over the best existing method is up to an impressive 15.5%. 
3. Flexibility: DREAM is a flexible method that can handle open-set scenarios and mitigate domain shift. It generates virtual unknown samples belonging to novel classes for additional supervision in the open-set scenarios and constructs a k nearest neighbor-based graph-of-graph to generate cross-domain counterparts using multi-sample mixup, which helps to improve cross-domain consistency. 
4. Clarity: The paper is well-written and easy to understand. The authors provide clear explanations of the problem formulation, methodology, and experiments, making it accessible to a wide range of readers.

### Weaknesses
1. There seems a lot of modules in the DREAM, it’s better to analysis the complexity of the proposed method. Specifically, the paper introduces a graph-level representation learning branch and a subgraph-enhanced branch. While these components are crucial to the method's performance, a detailed complexity analysis would provide a clearer understanding of the computational cost associated with each module and the overall framework. This analysis should consider both time and space complexity, particularly in comparison to existing graph domain adaptation methods.
2. What I am concern is the scalability of this model, i.e., whether this method can be applied into the dynamic graph scenario for learning. The current formulation of DREAM appears to be designed for static graphs. However, many real-world scenarios involve dynamic graphs where nodes and edges change over time. Adapting DREAM to such scenarios would require significant modifications. It would be valuable to discuss the potential challenges and limitations of applying DREAM to dynamic graphs, such as the need for continuous updates to the graph-of-graphs and the computational cost of handling evolving graph structures.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of open-set graph domain adaptation. The proposed method extracts graph structure representations using complementary branches. The graph-level representation branch uses a MPNN followed by attention layer for aggregation. The subgraph branch split each graph into several subgraphs using graph clustering and extract representations with GNNs. The method also includes dissimilar source samples in the latent space, and a k-nearest neighbor-based graph where nodes represent graph samples and are combined to generate new samples.

### Strengths
1. The paper studies open-set graph learning, which is an interesting and practical setting.

2. The paper presentation includes rich contents, with tables and figures well organized.

3. The conducted experiments look correct and include analysis from multiple views including ablation studies and sensitivity analysis.

### Weaknesses
1. Novelty overclaimed and related works not well addressed. The authors claim that "we are the first to study open-set graph domain adaptation". However, the problem studied is no difference with the existing open-world graph classification, such as [1], where the task is to classify each unlabeled graph example into either one of the known classes or a corresponding novel class. Moreover, it also closely resembles the open-world graph learning works like [2,3], where the learning goal is to classify nodes belonging to seen classes into correct groups, but also classify nodes not belonging to existing classes to an unseen class. The paper lacks a thorough review of related literature. In addition to open-world graph works, fields such as (graph) OOD detection is also closely related and should be discussed in the related works.

2. Following the above point, the experiments should include open-world graph learning related baselines. Currently only general graph classification methods are compared. The lack of comparison with methods designed for open-world or open-set scenarios makes it difficult to assess the proposed method's effectiveness in the intended context. Specifically, including baselines that can handle novel classes would provide a more appropriate benchmark for the proposed method's performance.

3. The method design include a lot of modules but lack support and motivations. Why is the attention mechanism necessary for aggregation? The paper does not provide a clear justification for using an attention mechanism over simpler aggregation methods. Why can the graph-of-graph design generate plausible cross-domain virtual features? There is no theoretical or empirical evidence provided to support this claim. For the objective why are $L_S, L_T, L_{DA}$ added without weights? The paper does not explain the rationale behind this design choice, and it is unclear how this affects the optimization process. The overall method seems complex and farraginous and unclear why it works.

### Questions
See Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for open-set graph adaptation, called DREAM. It combines attention mechanisms to enhance features at the graph level. Additionally, the network also includes a subgraph-enhanced branch. To address the open-set scenario, a special classifier and manifold mixup techniques are employed. In terms of adaptation, this paper utilizes the k-nearest neighbor and multi-sample mixup method.

### Strengths
The experimental results have shown improvement, and the charts and figures in the experiments are clear and easy to understand.

### Weaknesses
The contribution of the article is not clear. While the author elaborates on their method in detail, it is not evident how this work contributes in comparison to others.
There are some issues with the symbols in certain equations in this article. Should 'v' in Equation (1) be adjusted or corrected to 'h'? In Equation (4), 'g' and 'h' represent different entities but appear in the same position as 'p_\theta(y| )'. Equation (11) seems unrelated to the subsequent formulas, and it maybe appear unnecessary.
The paper does not compare with methods of graph domain adaptation or methods for open-set graph classification. It is insufficient to only compare with graph classification and open-set classification algorithms.

### Questions
Please refer to ‘Weaknesses’ section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
### Summary:
The paper introduces a novel exploration approach for reinforcement learning (RL) called Dream Dual Structured Exploration (DREAM). The main focus is to address the challenges of efficient exploration in sparse reward environments.

#### Key Contributions:
1. **Dual Structured Exploration:** The authors propose a two-pronged exploration strategy. The first component involves traditional intrinsic motivation where agents receive rewards for novel behaviors. The second component is a "dream" mechanism, where agents hallucinate or simulate possible future scenarios to guide their exploration.
  
2. **DREAM Model:** This model is central to the paper. It's a generative model that simulates future trajectories based on the agent's past experiences. By imagining potential future outcomes, the agent can better decide where to explore next. This approach aims to improve exploration efficiency, especially in environments where rewards are sparse and hard to find.
  
3. **Empirical Evaluation:** The authors validate the effectiveness of DREAM through a series of experiments in various RL environments. The results demonstrate that DREAM outperforms several state-of-the-art exploration strategies, especially in challenging sparse-reward settings.

4. **Scalability and Flexibility:** The DREAM approach is shown to be scalable and can be combined with other RL algorithms. This adaptability makes it a promising tool for a wide range of applications.

### Strengths
#### 1. Originality:
The paper introduces several original concepts and techniques that add value to the domain of reinforcement learning (RL) exploration.

- **Dual Structured Exploration:** The combination of traditional intrinsic motivation and a "dream" mechanism is a unique and innovative approach. While intrinsic motivation is a well-established concept in RL, the idea of agents simulating or hallucinating future scenarios (dreaming) to guide their exploration is a fresh take on the exploration challenge.
  
- **DREAM Model:** The generative model that simulates future trajectories based on past experiences is a novel concept. It effectively bridges the gap between traditional exploration techniques and forward-thinking strategies, allowing agents to anticipate potential outcomes.

#### 2. Quality:
The paper demonstrates high quality in both its theoretical constructs and empirical evaluations.

- **Theoretical Foundation:** The underlying principles of the DREAM model and dual structured exploration are well-justified and rooted in established RL concepts.
  
- **Empirical Evaluation:** The experiments conducted are comprehensive, covering multiple RL environments. The results not only validate the efficacy of the DREAM approach but also provide insights into its potential advantages over other state-of-the-art methods.

#### 3. Clarity:
The paper is well-structured and presents its concepts in a clear and organized manner.

- **Presentation:** The flow of the paper, from introducing the problem to detailing the solution and its evaluation, is logical and easy to follow.
  
- **Figures and Diagrams:** The included visual aids, such as graphs and flowcharts, effectively complement the textual content, aiding in the understanding of the proposed concepts and results.

- **Mathematical Formulations:** The mathematical representations and formulations, particularly those related to the DREAM model, are clearly articulated. While they require a foundational understanding of RL, they are accessible to the target audience.

#### 4. Significance:
The contributions of this paper have considerable significance in the domain of RL exploration.

- **Addressing a Crucial Challenge:** Efficient exploration in sparse reward environments is a longstanding challenge in RL. The DREAM approach offers a potential solution, making it a valuable contribution to the field.
  
- **Scalability and Flexibility:** The adaptability of the DREAM approach, which can be combined with other RL algorithms, broadens its applicability and potential impact. This adaptability implies that DREAM could be foundational for future RL research and applications.

- **Potential for Further Research:** The concepts introduced open up avenues for further exploration, refinement, and application in other RL scenarios or even beyond RL.

### Weaknesses
 #### 1. Generality of the DREAM Model:
While the DREAM model shows promise in the explored environments, the paper could benefit from a deeper discussion on its generality across diverse environments. 
**Actionable Insight:** Test the DREAM model in a broader set of RL environments, particularly those that have different dynamics or complexities than the ones currently evaluated. This would provide a more comprehensive understanding of where the model excels and where it might face challenges.

### Questions
How does the DREAM model scale with increasing complexity of the RL environment, especially in terms of computational resources and time? Does the "dream" mechanism become more resource-intensive in more complex scenarios?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
