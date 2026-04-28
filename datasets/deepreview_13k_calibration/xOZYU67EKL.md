# MMD-NSL: Mixed Multinomial Distribution-based Neuro-Symbolic Learning

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 6, 3, 3, 5

## Abstract
Neuro-symbolic learning (NSL) aims to integrate neural networks with symbolic reasoning approaches to enhance the interpretability of machine learning models. Existing methods mostly focus on the long dependency problem of symbolic learning. The important challenge of complex categorization is largely overlooked. To bridge this gap, we propose the Mixed Multinomial Distribution-based NSL MMD-NSL framework. It seamlessly integrates the handling of long dependency chains and complex semantic categorization within Knowledge Graphs (KGs). By introducing a continuous Mixed Multinomial Logic Semantic Distribution, we extend traditional Markov Logic Networks (MLN) to incorporate context-aware semantic embeddings. Our theoretical innovations, including a bijective mapping between MLNs and continuous multinomial distributions, enable the capture of intricate dependencies and varied contexts crucial for NSL tasks.
The framework leverages a bilevel optimization strategy, where a transformer-based upper level dynamically learns mixing coefficients akin to attention mechanisms, while the lower level optimizes rule weights for learning both context and rule patterns. Extensive experiments on the DWIE benchmarking datasets demonstrate significant advantages of MMD-NSL over four state-of-the-art approaches. It achieves 10.47% higher F1-scores on average than the best-performing baseline across 23 sub-datasets. It advances continuous probabilistic models for neuro-symbolic reasoning and complex relational tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces a framework for neuro-symbolic learning called Mixed Multinomial Distribution-based NSL (MMD-NSL). The primary aim of the framework is to address two core challenges in NSL: managing long dependency chains and handling complex semantic categorization within knowledge graphs. This work propose a mixed multinomial logic semantic distribution to integrate both context-aware semantics and long-range dependencies, building upon traditional Markov Logic Networks.

The framework leverages a bilevel optimization strategy: the upper level, powered by transformer-based architectures, dynamically learns mixing coefficients analogous to attention mechanisms, while the lower level optimizes rule weights to capture context-specific dependencies.

### Strengths
The proposed MMD-NSL framework is novel in its combination of mixed multinomial distributions and bijective mapping between MLNs and continuous multinomial distributions. This dual approach uniquely extends MLNs to incorporate context-aware embeddings, bridging symbolic logic and continuous representations, which is both creative and forward-thinking.

The paper’s bilevel optimization strategy is technically sound and thoughtfully designed, enabling a transformer-based upper level to dynamically learn context-sensitive mixing coefficients while optimizing rule weights in the lower level.

### Weaknesses
1.Lack of Comparisons with More Diverse Baselines: The paper does not benchmark against a sufficiently broad spectrum of established baselines, which is essential for assessing relative performance comprehensively.

2.Distinction between Neuro-symbolic Learning and Causal and Temporal Reasoning: The differences between neuro-symbolic learning you've pointed out  and causal reasoning, temporal reasoning remain unclear. Clarifying how neuro-symbolic learning diverges from or intersects with causal and temporal reasoning approaches could enhance understanding of its unique capabilities and limitations.

3.Lack of Detailed Description for Training and Optimization Settings: The paper does not sufficiently detail the settings for training and optimization, which are crucial for replicating the results and understanding the model's performance under specific conditions.

### Questions
See the section on weakness. We will increase the score based on the answer to the question.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the Mixed Multinomial Distribution-based NSL (MMD-NSL) framework, which adeptly addresses the challenge of complex categorization by seamlessly integrating the handling of long dependency chains with complex semantic categorization within KGs. Extensive experimental results demonstrate the effectiveness of the proposed method'.

### Strengths
1. The introduction of the Mixed Multinomial Distribution in the field of NSL for addressing complex classification issues exhibits novelty. 
2. Both theoretical and empirical analyses are comprehensive, with theoretical findings establishing MMD-NSL as a more general form of classical NSL, thereby making a contribution to the NSL field.

### Weaknesses
In general, the experiments of the paper are relatively weak.  Firstly, there is a limited comparison of the proposed algorithm with other notable approaches such as DeepProblog [1] and Semantic Loss [2].  Secondly, despite the authors conducting experiments on numerous datasets, these datasets appear to be predominantly toy and simplistic.



### Questions
1. The author uses a bilevel optimization algorithm, can further elaborate its efficiency?
2. The algorithm for solving the bilevel optimization does not seem to obtain the optimal solution. Can its convergence be proved?

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
This paper develops an embedding-based, optimizable probabilistic framework that can be bijectively mapped to the MLN framework. Within this framework, the rule discovery and reasoning tasks are extended by incorporating the ontology information of entities in the rule head. A bilevel optimization strategy is employed to optimize the proposed model. Experimental results demonstrate the superiority of the proposed method.

### Strengths
1.	The bijective mapping between MLNs and continuous multinomial distributions is a valuable contribution.
2.	Incorporating ontology information into rule learning is a sensible approach.

### Weaknesses
1.	Ontology information is not fully utilized in the framework; it should also be applied to the tail part of the rule. This enhancement would make the paper more comprehensive and increase its contribution.
2.	The experimental design lacks a key analysis: how the two components—the ontology information and the MLN-based probabilistic framework—individually contribute to the observed improvements.
3.	Certain aspects of the algorithm are unclear. For instance: 1) How are the rules generated? 2) How is  n_j  calculated for each newly generated rule?

### Questions
Refer to the weaknesses section for the unclear points.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work presents Neuro-Symbolic Learning based on Mixed Multinomial Distributions (MMD-NSL) with the aim of improving performance in handling complex relationships within Knowledge Graphs (KG). To this end, theoretical relations between the presented method and state-of-the-art methods are presented. The performance of MMD-NSL is evaluated on a synthetic and a real-world data benchmark.

### Strengths
1. The experiments show consistent improvements over state-of-the-art NeSy systems on a real-world dataset.

### Weaknesses
1. The presentation overall lacks clarity and needs further refinement. This includes many grammar errors and issues such as exact repetitions within the same page (e.g., "establishing a bijective mapping between MLNs and continuous multinomial distributions," both on lines 66 and 76).

2. The Figures do not support the significance of the contribution well. Figure 1 takes up half a page to demonstrate that a simple synthetic target could be learned. Figure 2 takes up an entire page with a questionable amount of information for the reader. Also, in Figure 2, labels are badly formatted (overlapping numbers) with misleading and inhomogeneous color mapping (e.g., a difference of 0.01 changing the hue completely). Again, some phrases are nearly identical, e.g., between Figure 1 caption and lines 442-446.

3. Given the nature of this contribution, namely a novel NeSy learning architecture, it would be highly desirable to compare performance across multiple datasets instead of a single one.

4. The mathematical presentation is, at times, lacking. For example, in the introduction and overview sections, logical rules are presented as a head implying the body (r_head -> r_1, r_2, ... ,r_n). Traditionally, the opposite is the case, with r_head <- r_1, r_2, ... ,r_n being the way Horn Clauses are written in implication form.

### Questions
Please see the weaknesses section

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the MMD-NSL framework, which extends classic MLNs by incorporating context-aware semantic embeddings, in order to both handling long dependency chains and addressing the complexity of semantic categorization within KGs. This is achieved by introducing a continuous Mixed Multinomial Logic Semantic Distribution. The framework exploit a bi-level optimization exploiting transformer-based attention mechanism in an upper level, while also learning rule weights at the lower level. MMD-NSL shows significant improvements wrt existing sota approaches across several datasets.

### Strengths
The aim and the idea behind the paper seem interesting and the experimental results are good. However I found the paper too confusing, and it is very difficult to assess the concrete contribution of this paper in its current form (see weaknesses and questions).

### Weaknesses
 - Related work discussion is quite limited, for a topic that has been extensively studied by different spots. For instance, modelling logic rules as latent variables has been already considered e.g. in [1] or [2], and also extending MLNs with neural components [3]. Similarly for what concern logic rules in the context of KGs, sota approaches like RLogic [4] or NCRL [5] should be discussed, or also LERP [6] that models contextual information from neighboring sub-graphs of entities in logic rules.
- Too many symbols and statements come out from nowhere, without having been introduced or explained. See both other comments and questions for more details.

OTHER COMMENTS
- "Typically, NSL tasks consider long dependencies expressed as simple logical implications like r_head → r_1 ∧ . . . ∧ r_L" generally is the opposite, sevearl NSL systems rely on Horn clauses of the form r_1 ∧ . . . ∧ r_L → r_head. The implication here has a different meaning, or what the authors mean?
- "We generalize this to tasks formulated as ⟨C(h), rhead,C(t)⟩ → r1 ∧ . . . ∧ rL, where C(·) denotes the NER types of the node", what are "h" and "t"? What is the NER type of  node? These symbols and notions have not been defined before.
- "the first-order logic rule bodies r1 ∧ . . . ∧ rL are", generally the body is a conjunction of literals (e.g. atoms in FOL), hence here I saw only ONE body with L relations. Is there a typo or what the authors mean by body exactly? These terms, as well as what the r_i mean have never been explained.
- Definition 1 is unclear. So you call a Logic Semantic Variable any continuous image by a "relaxation function" F to  a vairable zj based on the embeddings {eNERhead , eNERtail , epath} of G? What are these embeddings?, How they are obtained? What is meant by "based on"? This statement cannot be a formal definition without really stating/formally declaring the mentioned objects that are referred.
- "an semantic" typo
- "LTN represents a fuzzy logic-based extension of MLNs" LTN is not a fuzzy extension of MLN. In LTN the weights of the rules are fixed and cannot be learnt. A fuzzy extension of MLN is given e.g. by PSL [7].

### Questions
1) Can you make a clear example (and maybe it could be useful to add it to the main paper) about long dependency chains and complex 
categorization that you mention all across the paper?
2) "We denote zj | Ck as the j-th rule variable conditioned on the k-th context variable, which specifically corresponds to the structured relation ⟨C(h), rhead,C(t)⟩ → r1 ∧. . .∧rL." Why C is not C_k and r_head r1, ..., rL do not depend on j?
3) "where zj = 1 if the rule zj holds true in G and −1 otherwise" what does it mean that the rule zj holds true in here? It is not explained if each rule is universally quantified or it is ground, wrt which variables or objects, what are the known facts, if it is assumed CWA. 
4) What do denote f_j and z_j in equation 1? According to the beginning of section 3.2 z_j denotes a latent variable for a rule. How this conciliates with MLN where you have rules and each f_j(z_j) is just n_j number of groundings satisfying the rule. Or similarly in PSL with fuzzy relaxations or in NLMN with neural potentials?
5) "Following Definition 1, there are two types of Logic Semantic Variable:" Why only these two types?

### Soundness
2

### Presentation
1

### Contribution
2
