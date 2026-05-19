### Summary

This paper introduces the concept of "model kinship" to enhance the effectiveness of model merging. Inspired by biological evolution, the authors propose that the degree of similarity between models (measured by the change in weights from a base model) can predict the potential benefits of merging. The authors conduct experiments to show that models with higher kinship exhibit greater potential for performance improvement through merging. They propose a Top-k Greedy Merging with Model Kinship strategy, which leverages kinship to guide the merging process. Experimental results demonstrate that this approach can lead to better performance on benchmark datasets compared to the vanilla greedy merging strategy.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces the concept of "model kinship" as an indicator of potential performance gains in model merging. This novel perspective provides a new way to understand and predict the effectiveness of merging different models.

2. The paper is well-structured and clearly explains the concept of model kinship, its calculation, and its application in guiding model merging. The authors provide a comprehensive analysis of the relationship between model kinship and performance gains.

3. The paper provides a detailed explanation of the proposed Top-k Greedy Merging with Model Kinship strategy. The authors clearly outline the steps involved in calculating model kinship, selecting the best-performing models, and merging them based on their kinship scores.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that model kinship is a reliable indicator of merging potential. However, the authors do not provide a theoretical justification for this assumption. It is unclear why the similarity of weight changes between models should directly correlate with the potential for performance improvement after merging. The paper lacks a rigorous analysis of the conditions under which this assumption holds true, and it does not explore potential scenarios where high kinship might lead to negative outcomes, such as catastrophic forgetting or interference. A more thorough theoretical foundation is needed to support the claim that kinship is a reliable predictor of merging effectiveness.

2. The paper relies on a specific metric (similarity of weight changes) to define model kinship. While this approach is practical, it may not capture all aspects of model similarity that are relevant to merging. Other factors, such as the functional similarity of the models or the diversity of their learned representations, could also play a crucial role in determining the success of merging. The paper does not explore alternative definitions of model kinship or discuss the limitations of the chosen metric. This reliance on a single metric limits the generalizability of the findings and raises questions about the robustness of the proposed approach.

3. The experimental evaluation is limited to a specific set of models and datasets. While the results are promising, it is unclear whether the proposed approach would generalize to other models, architectures, or tasks. The paper does not provide a comprehensive analysis of the sensitivity of the results to different experimental settings. The lack of a broader evaluation makes it difficult to assess the practical applicability of the proposed method and raises concerns about its robustness across diverse scenarios.

### Suggestions

To strengthen the theoretical foundation of the proposed model kinship concept, the authors should provide a more rigorous analysis of why the similarity of weight changes between models should correlate with the potential for performance improvement after merging. This analysis should include a discussion of the underlying mechanisms that link weight change similarity to merging effectiveness. For example, the authors could explore how the shared and unique components of weight changes contribute to the overall performance of the merged model. Furthermore, the authors should investigate potential scenarios where high kinship might lead to negative outcomes, such as catastrophic forgetting or interference, and propose strategies to mitigate these risks. A more thorough theoretical analysis would significantly enhance the credibility of the proposed approach.

To address the limitations of relying on a single metric for model kinship, the authors should explore alternative definitions of model similarity that go beyond the similarity of weight changes. This could include metrics based on functional similarity, such as the similarity of the models' outputs on a set of test tasks, or metrics based on the diversity of their learned representations, such as the distance between the models' feature spaces. The authors should also discuss the trade-offs between different metrics and justify their choice of metric based on the specific characteristics of the models and tasks being considered. A more comprehensive analysis of different metrics would provide a more robust and generalizable approach to model kinship.

To improve the generalizability of the experimental results, the authors should conduct a more comprehensive evaluation across a wider range of models, architectures, and tasks. This evaluation should include a diverse set of models with different sizes and architectures, as well as a variety of tasks with different levels of complexity. The authors should also investigate the sensitivity of the results to different experimental settings, such as the choice of merging strategy, the number of models being merged, and the specific datasets being used. A more thorough evaluation would provide a more robust assessment of the practical applicability of the proposed method and increase the confidence in its generalizability.

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
