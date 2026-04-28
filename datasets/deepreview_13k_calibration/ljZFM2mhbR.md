# DAG-SHAP: Feature Attribution in DAG based on Edge Intervention

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Shapley value-based feature attribution methods face challenges in scenarios with complex feature interactions and causal relationships, even when a causal structure is provided. The assumption on the attribution objects of existing methods often deviates from practical scenarios as they cannot capture the exogenous influence of features through each edge in the causal graph, leading to unreasonable interpretations. To overcome these limitations, we propose a novel feature attribution method called DAG-SHAP, which is based on edge intervention. DAG-SHAP treats the exogenous contributions in each ongoing feature edge as an individual attribution object ensuring that both externality and exogenous contributions of features are appropriately captured. Additionally, we introduce an approximation method for efficiently computing DAG-SHAP. Extensive experiments on both synthetic and real datasets validate the effectiveness of DAG-SHAP. Our code can be found in the anonymous repository at \url{https://anonymous.4open.science/r/dag-30F2}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces a Shapley attribution method that is based on utilizing a given causal DAG by using edge interventions rather than interventions on nodes/variables directly. By this, the method aims at capturing both exogenous contributions and effects between features. The authors show in different artificial and real-world data sets that their method is better at capturing the relevance of features than related works when there are complex causal interactions between them.

### Strengths
+ Well-motivated solution and a mostly fair comparison with related work
+ Identifies a key issue with existing methods
+ Clearly lists desired properties, although the authors lack mathematical proofs that their method fulfills these
+ Fair and comprehensive empirical validation on both synthetic and real datasets

### Weaknesses
- Lack of theoretical guarantees and proofs that the proposed methods fulfill the desired properties
- Limited discussion of computational complexity and scalability for large DAGs, especially when they go beyond the rather small examples in the experiments
- A rather minor concern: The assumption of known causal structure may be unrealistic in many real applications
- While many important related papers are discussed, some fairly relevant papers are missing (see Questions section for more details)
- It seems the main contribution is rather using the MDN model for modeling the interventions to compute $\mathbb{E}[Y | do(x_s)]$, rather than the Shapley definitions. Strictly speaking, using the formalism in the referenced works, one could use an MDN there as well to compute the quantities. For instance, while the intrinsic causal influence paper defines functional causal models of the form $Y = f(PA_X, N_Y)$, this can be represented via an MDN as modeling of $N_Y$ is not required in a structural causal model as long as it represents a generative model as given in the MDN case. That being said, the novelty here stems particularly from using an MDN, rather than from the Shapley definitions.

### Questions
The paper is generally well written and addresses an important problem. My two main concerns are, however, a lack of theoretical guarantees that the method truly fulfills the desired properties and some comparison with related work in a similar direction. For the theoretical aspects, I appreciate the list in the appendix, but these are mostly argumentative rather than mathematical proofs, which is the most important aspect when providing a novel attribution technique. Regarding the related work, you have a great comparison, but including a discussion about the following papers can be helpful:  
- "Feature relevance quantification in explainable AI: A causal problem" by Janzing et al.  
- "Quantifying intrinsic causal contributions via structure preserving interventions" by Janzing et al.  

Both papers argue similarly for attributing causal influences. While the first work argues via hard-interventions, something you explicitly want to avoid, the second work has a similar approach towards attribution of influences. Your approach still seems to differ from these works, but a comparison can be insightful.

Generally, the simple example to illustrate the idea is helpful and maybe you could use this to explicitly show that the most related works would not capture the right contributions.

A few remarks/questions:
- The e_s notation with and without bold S is often hard to distinguish, maybe consider using a different notation that points out the difference more clearly.
- How does the computational complexity of DAG-SHAP scale with the number of vertices and edges in the graph? What are the practical limitations for large-scale applications?
- The work lacks some discussion about the practical modeling assumptions of your functions f. Some remarks on the impact of inaccurate modeling assumptions could be insightful.


**After rebuttal**  

It seems the main contribution is rather using the MDN model for modeling the interventions to compute $\mathbb{E}[Y | do(x_s)]$, rather than the Shapley definitions. Strictly speaking, using the formalism in the referenced works, one could use an MDN there as well to compute the quantities. For instance, while the intrinsic causal influence paper defines functional causal models of the form $Y = f(PA_X, N_Y)$, this can be represented via an MDN as modeling of $N_Y$ is not required in a structural causal model as long as it represents a generative model as given in the MDN case. That being said, the novelty here stems particularly from using an MDN, rather than from the Shapley definitions.

I have carefully considered all of the authors responses and truly appreciate the time and effort in addressing my concerns. Nevertheless, I will stick to my initial rating as I still have concerns that the novelty lies in the estimation method rather than the Shapley part. That being said, I am not strongly advocating for rejection, and if the other Reviewers see significant novelty here, I am also okay with this. To reflect this, I have decreased my confidence score.

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
3

### Summary
This paper modifies the popular Shapley-based framework for feature importance to satisfy certain properties related to causal inference. These include: "causality", such that attributions detect features' causal interactions towards the response, "externality", such that attributions also consider causal paths to the response through other variables, and "exogeneity", such that attributions do not confound other variables' influence towards the response. It is shown that previous Shapley based approaches, including on/off-manifold Shapley, causal Shapley, and Shapley flow, fail one or more of these criteria due to their treatment of other variables and/or their strict reliance on topological ordering. Given the underlying causal graph, the proposed solution, DAG-SHAP, obeys the desired properties, by considering interventions at the level of edges, rather than vertices. An algorithm is presented for practical evaluation, which is empirically tested on one simulated data example and two real datasets, where DAG-SHAP performs better than the other Shapley-based alternatives.

### Strengths
The development of causality-based feature importance methods are an important field, since many researchers want to gain insights about how variables interact, while most feature importance methods remain model-based, in order to optimize model performance rather than gain insights about relationships in the data.

Externality and exogeneity are interesting and relatively well-founded causal axioms. Axioms for feature importance, particularly with respect to "explaining the data", are quite early in their devlopment and seem to be subject to frequent debate. Although I disagree that every causal feature importance method must obey externality to coherently explain how features explain the response, I see the appeal in guaranteeing it, in order to identify more layers of the causal structure.

Edge-based interventions are an interesting approach for obtaining coherent causal interpretations. The derivations for proving that DAG-SHAP obeys the desired properties (given that the causal graph is already known) appears to be sound.

Code is provided.

### Weaknesses
It seems that like Causal Shapley, DAG-SHAP also relies on prior causal knowledge. In particular, it seems to rely on knowledge of the causal graph, since only valid topological orderings are considered when averaging edge permutations. This is an extremely strong assumption, as the entire motivation behind many causal based feature importance methods is to learn information about the unknown causal structure of the data. Indeed, it is not required by either MCI or UMFI. If this is the case, then this strong assumption should be emphasized in the paper, as DAG-SHAP would only be applicable if the causal structure is already known, and serve to provide more detailed causal interpretations, in this setting.

By restricting discussion and comparision just to other Shapley-based methods, this does not consider many approaches which seek to explain relationships in the data, beyond just Shapley-based approaches. For example, MCI (ICML 2021) and UMFI (AISTATS 2023) were developed to learn aspects like causal interactions from the data, rather than just the model itself. The paper should clarify the distinction between methods that aim to explain model behavior versus methods that aim to explain relationships in the data generating process, and how DAG-SHAP fits into this landscape.

The discussion of externality and exogeneity should be clarified earlier (for example, externality is only defined in Section 3, while there is ample discussion beforehand). I also think that the motivation behind these axioms can be strengthened. An intuitive toy example is provided, but there should be more insight into why these properties are important. The paper should also discuss the limitations of these axioms. For example, while externality aims to capture indirect effects, it is not clear why one would not simply redefine the response variable to directly capture the effect of interest, rather than relying on a feature importance method to capture the compounded effects along a causal chain. Furthermore, the paper should clarify why efficiency and additivity are necessary or even desirable properties for causal interpretation, as these properties are primarily motivated by the Shapley value's application in cooperative game theory, which does not necessarily align with the goals of causal inference.

On a related note, the discussion of the empirical evaluation should relate more explicitly to the proposed theory. The bulk of the paper discusses externality and exogeneity and why the proposed method works, while others fail. Although these properties are clearly relevant in the provided empirical experiments, the discussion can be more focused to tie back to these ideas in depth. In its current form, I also find the explanation in the desirable attribution section (L429) to be lacking. Specifically, the paper claims that the variance of the attribution scores is indicative of externality, but this is not intuitive. The variance of attribution scores can be influenced by various factors, such as the numerical scales of the variables, the quality of the data, or the sampling procedure used to estimate the Shapley values. It is not clear why variance is a reliable indicator of externality, and the paper should provide a more rigorous justification for this claim.

Nits:

I think that there is too much focus on previous Shapley methods in the main text (Section 2.2). I think that this can be moved to the appendix.

The use of \mathcal{N} for the main features/vertices {1, ..., N} does not seem standard, as this notation typically represents the set of natural numbers. I would recommend [n] or V.

### Questions
Can the authors confirm the requirement of knowing the causal graph before running DAG-SHAP in order to satisfy causality, externality, and exogeneity? Do they think that this condition can be weakened while providing the same guarantees? If not, how do the authors see the motivation/practical benefit of the method, given the causal graph is already known?

Given externality, why is it that vertices with multiple paths to the response (ex. X1, X2 in the synthetic data example) are not given higher mean attribution score, but rather higher variance? This seems to suggest that in practice, analysts should look at the variance of attribution scores to rank features rather than just the means, and this seems a bit counter-intuitive. In practice, high variance can be indicative of many other factors, such as the quality of the data. As such, I remain unconvinced by the desirable attribution.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel feature attribution method that utilizes the Directed Acyclic Graph (DAG) among features and the target variable Y to enhance Shapley value-based feature attribution methods by capturing the exogenous influence of a feature. The novelty lies in calculating Shapley values for the edges in the DAG and using aggregated edge-based Shapley values for feature attribution.

### Strengths
•	The paper is well-written, with an example that effectively illustrates the core ideas and solutions. The authors have put in significant effort to make the paper easily readable, which is greatly appreciated.

•	The analysis of limitations in existing Shapley value-based feature attribution methods is comprehensive.

•	The idea of estimating Shapley values for edges in a DAG is interesting.

### Weaknesses
The primary limitation is that the proposed method relies on a known DAG. In most real-world scenarios, the DAG is unknown, and it generally cannot be learned directly from data. If a DAG is available, it is possible to estimate the causal effect of features on Y. Why not use a well-defined causal effect for feature attribution, such as the average causal effect of a feature on Y, instead of introducing a new DAG-SHAP value?


Additional Concerns Regarding Clarity

•	The notation do(variable=v) in a DAG is well-defined in causal inference, but do(edge=e) is not. A formal definition of do(edge=e) is required, along with justification that this intervention yields a valid causal measure. Specifically, what causal measure does the DAG-SHAP value represent?

•	The edge intervention causal Shapley value of a variable is defined as the sum of attribution values for its outgoing edges in Equation (4). My questions regarding this definition are as follows:

1.	Do the edges in paths that do not terminate at Y contribute to explaining Y? If not, how should these edges be excluded?

2.	In a general causal graph, edges can originate from Y, such as $Y \to X$. How should the edge intervention causal Shapley value be calculated for such edges? Should we include Y when calculating the outgoing edges from Y?

•	In the experiments, vertex splitting for causal structure is considered a desirable benchmark for attribution. I assume that this is one of a few desirable benchmarks. My point is that using the term Mean Absolute Error may be misleading, as there is no objective ground truth in feature attribution.

Minor: 

•	After Equation (1), the terms exogenous contribution of the feature and exogenous contribution of another feature should be explained to clarify the problem definition.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

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
The paper proposes a novel feature attribution method called DAG-SHAP, which enhances existing Shapley value-based methods by focusing on edge intervention in Directed Acyclic Graphs (DAG). It aims to address the challenges in capturing exogenous contributions and externality in complex feature interactions with causal relationships. The authors also propose an efficient approximation algorithm to compute DAG-SHAP values, validated by experiments on synthetic and real datasets. The contributions include advancing causal feature attribution methods, particularly by addressing limitations in existing Shapley-based models.

### Strengths
The introduction of edge intervention in DAGs for feature attribution is a creative approach, differentiating DAG-SHAP from existing Shapley-based methods. The paper provides a thorough theoretical analysis, including proofs of the properties DAG-SHAP satisfies, such as causality and externality. The proposed approximation method for computing DAG-SHAP is practical for real-world applications, as demonstrated by experiments on both synthetic and real datasets. The experiments are well-designed and provide clear comparisons with existing methods, highlighting the advantages of DAG-SHAP.

### Weaknesses
The paper proposes an approximation algorithm, but it lacks sufficient discussion on computational complexity and performance optimization, especially for large datasets or more complex DAG structures. The scalability and efficiency of the algorithm in such scenarios remain unclear. Specifically, the paper does not provide a rigorous analysis of how the approximation error scales with the number of nodes and edges in the DAG, nor does it discuss the impact of DAG density on the computational cost. Additionally, while the paper validates DAG-SHAP’s effectiveness on simpler datasets, it does not include experiments on more complex models, such as deep neural networks with deeper DAG structures. Demonstrating its performance on high-dimensional or deeper DAGs would strengthen the research. Moreover, the computational cost of the algorithm for large-scale datasets is not fully addressed. As the number of edges and vertices increases, the complexity of calculating Shapley values grows significantly, and the paper would benefit from a deeper exploration of the trade-offs between efficiency and accuracy, especially in real-time or large-scale applications. The paper also does not discuss the memory footprint of the algorithm, which could be a limiting factor when dealing with large DAGs.

### Questions
1. Can the authors clarify the computational trade-offs of the approximation algorithm in large-scale datasets? Would it be practical for deep neural networks with highly complex DAG structures?
2. The paper claims that DAG-SHAP captures exogenous contributions more accurately than previous methods. Could the authors provide additional examples or scenarios where existing methods fail in capturing exogeneity, aside from those already included in the synthetic dataset?

### Soundness
2

### Presentation
3

### Contribution
3
