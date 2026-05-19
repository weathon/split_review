### Summary

This paper shows that scale can impact the performance of structure learning, building on previous work by Loh & Bühlmann (2014) and Reisach et al. (2021). It presents conditions under which square-based losses are minimal for incorrect Directed Acyclic Graphs (DAGs) in d-dimensional cases, extending the analysis to non-linear relationships and log-likelihood-based losses. Extensive experiments on synthetic and real-world data confirm these theoretical findings.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. This paper studies a very important problem in the literature. 

2. This paper provides some theoretical justifications on the effect of the scales of variables on the performance of  structure learning.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical results in this paper break down the problem into three specific structures: chain, fork, and collider. However, real-world graphs often consist of a mixture of these structures, and the interactions between them can be complex. The paper does not adequately address how its findings extend to these more realistic scenarios. For instance, it's unclear how the scale sensitivity of individual structures translates to the overall graph structure when these components are interconnected. The analysis seems to assume that the effects of scaling are localized to the specific structure being analyzed, which may not hold true in practice.

2. The paper asserts that condition (A1) is crucial for its theoretical results, but it's unclear why this is the case. While the paper analyzes chain, fork, and collider structures, the underlying mechanisms affecting scale sensitivity might be similar across these structures. For example, if scale differences primarily affect the magnitude of error terms, this mechanism should be consistent regardless of whether the structure is a chain or a fork. The paper needs to provide a more detailed explanation of why the specific decomposition into these structures is necessary for its theoretical results, and how the interactions between these structures might affect the overall scale sensitivity.

3. The proposed solution of using a Scale Robust Loss (SRL) seems overly simplistic. Simply normalizing variables to have equal variance and excluding free variance terms from the loss function might not be sufficient to address the scale sensitivity issue. This approach does not consider the potential impact of non-linear relationships between variables, which could still lead to scale-dependent behavior even after normalization. A more robust approach would involve a more careful consideration of the underlying statistical properties of the data and the specific loss function being used. The paper should explore alternative methods for addressing scale sensitivity, such as using invariant loss functions or developing more sophisticated normalization techniques.

### Suggestions

The paper should provide a more detailed analysis of how its theoretical results extend to complex, real-world graphs. This could involve investigating the interactions between different graph structures and how they contribute to overall scale sensitivity. For example, the authors could explore how scaling a subset of variables affects the structure learning of a larger graph with a mixture of chain, fork, and collider structures. This analysis should go beyond the localized effects of scaling on individual structures and consider the global impact on the entire graph. Furthermore, the paper should provide more concrete examples of how the theoretical results manifest in real-world scenarios, which would help to illustrate the practical implications of the findings. This could involve using real-world datasets to demonstrate how scale differences can lead to incorrect structure learning and how the proposed SRL can mitigate these issues.

The paper needs to provide a more detailed explanation of why condition (A1) is crucial for its theoretical results. This explanation should go beyond simply stating that the analysis is broken down into chain, fork, and collider structures. The authors should explain the specific mathematical reasons why this decomposition is necessary and how it relates to the underlying mechanisms of scale sensitivity. For example, they could discuss how the different orientations of edges in these structures affect the error terms and how this leads to different scale dependencies. Furthermore, the paper should explore the potential limitations of this decomposition and whether it can be generalized to other types of graph structures. This would help to clarify the scope of the theoretical results and their applicability to different scenarios.

The paper should also explore alternative solutions for addressing scale sensitivity beyond the proposed SRL. This could involve investigating invariant loss functions that are inherently robust to scale changes, or developing more sophisticated normalization techniques that take into account the specific characteristics of the data. For example, the authors could explore the use of contrastive learning methods, which have been shown to be effective in learning representations that are invariant to certain transformations. Additionally, the paper should provide a more detailed analysis of the limitations of the proposed SRL and under what conditions it might fail to address the scale sensitivity issue. This would help to provide a more complete picture of the problem and potential solutions.

### Questions

1. How does the theoretical results in this paper extend to complex, real-world graphs that are not simply chains, forks, or colliders? 

2. The paper shows that standard structure learning methods can be affected by the scale of the variables. However, it is not clear to me why this is the case. Across chain, fork, and collider structures, the underlying reasons should be similar. Could you provide some intuitions on why scale differences would lead to incorrect structure learning? 

3. Are there alternative solutions for addressing the scale sensitivity issue beyond the proposed SRL?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
