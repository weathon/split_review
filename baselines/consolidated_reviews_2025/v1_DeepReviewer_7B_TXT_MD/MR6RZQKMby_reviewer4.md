### Summary

This paper introduces the concept of model kinship, inspired by biological evolution, to guide the merging of large language models (LLMs). The authors propose a new model merging strategy called Top-k Greedy Merging with Model Kinship, which leverages model kinship to enhance performance on benchmark datasets. The paper also presents a preliminary explainability analysis of model kinship. The authors provide empirical evidence that model kinship can be used to guide the merging process and improve performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel concept of model kinship, which is inspired by biological evolution, and provides a new perspective on model merging.
2. The authors conduct extensive experiments to demonstrate the effectiveness of model kinship in guiding the merging process and improving performance on benchmark datasets.
3. The paper provides a preliminary explainability analysis of model kinship, which is a valuable contribution to the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that model kinship is a reliable indicator of merging potential. However, the authors do not provide a theoretical justification for this assumption. It is unclear why the similarity of weight changes between models should directly correlate with the potential for performance improvement after merging. The paper lacks a rigorous analysis of the conditions under which this assumption holds true, and it does not explore potential scenarios where high kinship might lead to negative outcomes, such as catastrophic forgetting or interference. A more thorough theoretical foundation is needed to support the claim that kinship is a reliable predictor of merging effectiveness.
2. The paper relies on a specific metric (similarity of weight changes) to define model kinship. While this approach is practical, it may not capture all aspects of model similarity that are relevant to merging. Other factors, such as the functional similarity of the models or the diversity of their learned representations, could also play a crucial role in determining the success of merging. The paper does not explore alternative definitions of model kinship or discuss the limitations of the chosen metric. This reliance on a single metric limits the generalizability of the findings and raises questions about the robustness of the proposed approach.
3. The experimental evaluation is limited to a specific set of models and datasets. While the results are promising, it is unclear whether the proposed approach would generalize to other models, architectures, or tasks. The paper does not provide a comprehensive analysis of the sensitivity of the results to different experimental settings. The lack of a broader evaluation makes it difficult to assess the practical applicability of the proposed method and raises concerns about its robustness across diverse scenarios.

### Suggestions

To strengthen the theoretical foundation of the proposed model kinship concept, the authors should provide a more rigorous analysis of why the similarity of weight changes between models should correlate with the potential for performance improvement after merging. This analysis should delve into the underlying mechanisms that link weight change similarity to the effectiveness of merging. For example, the authors could explore how shared and unique components of weight changes contribute to the overall performance of the merged model. Furthermore, the authors should investigate potential scenarios where high kinship might lead to negative outcomes, such as catastrophic forgetting or interference, and propose strategies to mitigate these risks. A more thorough theoretical analysis would significantly enhance the credibility of the proposed approach.

To address the limitations of relying on a single metric for model kinship, the authors should explore alternative definitions of model similarity that go beyond the similarity of weight changes. This could include metrics based on functional similarity, such as the similarity of the models' outputs on a set of test tasks, or metrics based on the diversity of their learned representations, such as the distance between the models' feature spaces. The authors should also discuss the trade-offs between different metrics and justify their choice of metric based on the specific characteristics of the models and tasks being considered. A more comprehensive analysis of different metrics would provide a more robust and generalizable approach to model kinship.

To improve the generalizability of the experimental results, the authors should conduct a more comprehensive evaluation across a wider range of models, architectures, and tasks. This evaluation should include a diverse set of models with different sizes and architectures, as well as a variety of tasks with different levels of complexity. The authors should also investigate the sensitivity of the results to different experimental settings, such as the choice of merging strategy, the number of models being merged, and the specific datasets being used. A more thorough evaluation would provide a more robust assessment of the practical applicability of the proposed method and increase the confidence in its generalizability.

### Questions

1. How does the concept of model kinship relate to existing theories of model merging and ensemble learning? Can the authors provide a more detailed comparison with related work?
2. The paper assumes that model kinship is a reliable indicator of merging potential. Can the authors provide more theoretical justification for this assumption? Are there any scenarios where high kinship might lead to negative outcomes?
3. The paper relies on a specific metric (similarity of weight changes) to define model kinship. Are there other metrics that could be used to define model kinship, and how would they compare in terms of effectiveness and robustness?
4. The experimental evaluation is limited to a specific set of models and datasets. Can the authors provide more details about the experimental setup and discuss the limitations of the current evaluation?

### Rating

6

### Confidence

3

**********
