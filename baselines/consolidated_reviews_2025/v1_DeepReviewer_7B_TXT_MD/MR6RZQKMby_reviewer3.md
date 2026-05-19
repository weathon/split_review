### Summary

This paper introduces a new metric called model kinship, which is inspired by biological evolution, to guide the merging of large language models (LLMs). The authors propose a new model merging strategy called Top-k Greedy Merging with Model Kinship, which can improve the efficiency and effectiveness of model merging. The paper also provides a comprehensive analysis of model kinship and its relationship with model performance gains. The authors demonstrate the effectiveness of their proposed method through extensive experiments on various benchmark datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel metric called model kinship, which is inspired by biological evolution, to guide the merging of large language models (LLMs). This is a creative and innovative approach that can potentially lead to more effective model merging strategies.
2. The paper provides a comprehensive analysis of model kinship and its relationship with model performance gains. This analysis is crucial for understanding the effectiveness of the proposed method.
3. The paper demonstrates the effectiveness of the proposed method through extensive experiments on various benchmark datasets. The results show that the proposed method can achieve better performance than the vanilla greedy merging strategy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that model kinship is a reliable indicator of merging potential. However, the authors do not provide a theoretical justification for this assumption. It is unclear why the similarity of weight changes between models should directly correlate with the potential for performance improvement after merging. The paper lacks a rigorous analysis of the conditions under which this assumption holds true, and it does not explore potential scenarios where high kinship might lead to negative outcomes, such as catastrophic forgetting or interference. A more thorough theoretical foundation is needed to support the claim that kinship is a reliable predictor of merging effectiveness.
2. The paper relies on a specific metric (similarity of weight changes) to define model kinship. While this approach is practical, it may not capture all aspects of model similarity that are relevant to merging. Other factors, such as the functional similarity of the models or the diversity of their learned representations, could also play a crucial role in determining the success of merging. The paper does not explore alternative definitions of model kinship or discuss the limitations of the chosen metric. This reliance on a single metric limits the generalizability of the findings and raises questions about the robustness of the proposed approach.
3. The experimental evaluation is limited to a specific set of models and datasets. While the results are promising, it is unclear whether the proposed approach would generalize to other models, architectures, or tasks. The paper does not provide a comprehensive analysis of the sensitivity of the results to different experimental settings. The lack of a broader evaluation makes it difficult to assess the practical applicability of the proposed method and raises concerns about its robustness across diverse scenarios.

### Suggestions

The authors should provide a more rigorous theoretical analysis of why model kinship, defined as the similarity of weight changes, is a reliable indicator of merging potential. This analysis should delve into the underlying mechanisms that link weight change similarity to the effectiveness of merging. For example, the authors could explore how shared and unique components of weight changes contribute to the overall performance of the merged model. Furthermore, the authors should investigate potential scenarios where high kinship might lead to negative outcomes, such as catastrophic forgetting or interference, and propose strategies to mitigate these risks. This could involve exploring different merging strategies that take into account the functional similarity of the models, rather than just the similarity of weight changes. The authors should also consider alternative definitions of model kinship that capture different aspects of model similarity, such as the diversity of learned representations or the functional similarity of the models. This would provide a more comprehensive understanding of the factors that influence the effectiveness of model merging.

To address the limitations of the experimental evaluation, the authors should conduct a more comprehensive analysis of the sensitivity of their results to different experimental settings. This should include evaluating the proposed method on a wider range of models, architectures, and tasks. The authors should also explore the impact of different hyperparameters on the performance of the proposed method. This would provide a more robust assessment of the practical applicability of the proposed method and increase the confidence in its generalizability. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed method, including the time and memory requirements for calculating model kinship and performing the merging process. This would help to assess the scalability of the proposed method and its suitability for large-scale model merging tasks.

Finally, the authors should provide a more detailed comparison of their proposed method with existing model merging techniques. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to other approaches. The authors should also discuss the limitations of their method and identify areas for future research. This would provide a more complete picture of the state of the art in model merging and help to position the proposed method within the broader context of the field. The authors should also consider releasing their code and experimental results to facilitate further research in this area.

### Questions

1. How does the concept of model kinship relate to existing theories of model merging and ensemble learning? Can the authors provide a more detailed comparison with related work?
2. The paper assumes that model kinship is a reliable indicator of merging potential. Can the authors provide more theoretical justification for this assumption? Are there any scenarios where high kinship might lead to negative outcomes?
3. The paper relies on a specific metric (similarity of weight changes) to define model kinship. Are there other metrics that could be used to define model kinship, and how would they compare in terms of effectiveness and robustness?
4. The experimental evaluation is limited to a specific set of models and datasets. Can the authors provide more details about the experimental setup and discuss the limitations of the current evaluation?

### Rating

5

### Confidence

4

**********
