# In-context Time Series Predictor

- Decision: Accept
- Scores: 3, 8, 6, 8

## Abstract
Recent Transformer-based large language models (LLMs) demonstrate in-context learning ability to perform various functions based solely on the provided context, without updating model parameters. To fully utilize the in-context capabilities in time series forecasting (TSF) problems, unlike previous Transformer-based or LLM-based time series forecasting methods, we reformulate "time series forecasting tasks" as input tokens by constructing a series of (lookback, future) pairs within the tokens. This method aligns more closely with the inherent in-context mechanisms, and is more parameter-efficient without the need of using pre-trained LLM parameters. Furthermore, it addresses issues such as overfitting in existing Transformer-based TSF models, consistently achieving better performance across full-data, few-shot, and zero-shot settings compared to previous architectures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a model named "In-context Time Series Predictor" (ICTSP), designed specifically for time series forecasting (TSF). Unlike traditional Transformer-based models, ICTSP adopts a novel input token structure, resulting in improved performance.

### Strengths
ICTSP model transforms time series forecasting tasks into input tokens, aligning closely with the inherent mechanisms of the Transformer model and efficiently leveraging its contextual learning capabilities.

### Weaknesses
1. The innovation appears limited. While the paper extensively discusses the approach from an in-context learning perspective, the methodology itself seems simplistic and more akin to a heuristic trick due to excessive textual explanation without solid theoretical support.

2. The paper does not address whether this model could be applied to other time series tasks, such as classification, interpolation, or anomaly detection. The utility of the model appears confined to the forecasting tasks, necessitating stronger performance to justify its specialized use.

3. The significant improvements in zero-shot tasks over full-data tasks lack detailed explanations. The paper does not sufficiently clarify why the ICTSP demonstrates a pronounced advantage in few-shot and zero-shot learning scenarios than in full-data tasks

### Questions
The provided link to the code repository is inaccessible, which hinders the reproducibility of the results. Could you please update or fix the link to the source code?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents the In-context Time Series Predictor(ICTSP), which utilizes the in-context capabilities for time series forecasting tasks. It proposes an innovative way to construct the tokens with context examples, showing promising results across multiple experimental settings.

### Strengths
1. The writing is clear and fluent.
2. This paper's motivation is relatively novel. It proposes utilizing the in-context learning capabilities of large language models (LLMs) for time series forecasting tasks. 
3. The experiments are comprehensive, encompassing various experimental settings and datasets.

### Weaknesses
1. The formulation of TSF transformers is not sufficient. As far as I am concerned, there are some methods [1,2] that utilize patching embedding to form the input tokens. These methods cannot be simply categorized as Temporal-wise Transformer or Series-wise Transformer in Section 2.2

2. The baselines results for baselines are collected from source papers. However, this paper applies different input time series length from these papers, which may lead to an unfair comparison.

3. The details of Computational Costs and Table.5 are not provided.

### Questions
Based on the listed weakness,
1. Can you add more discussions for these methods based on patching embedding from an ICL perspective?
2. For the Full-data TSF setting, can you rerun the baselines under the same experimental settings?  Alternatively, you could articulate the rationale behind your experimental settings, which would make the comparisons more convincing.
3. Can you provide more details for Computational Costs? What are the number of layers and hidden dimensions of different models?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper present In-context Time Series Predictor (ICTSP), a new framework of doing time series forecasting. It formulates the time series prediction task into the form of in-context learning, such that in the input data is split into a few forecasting examples to guide the model complete the target prediction with the adjacent input. Experimental results demonstrate the method’s effectiveness.

### Strengths
1. **Novel Framework**: The paper proposes an innovative approach to time series forecasting by adopting in-context learning, which could inspire further research and development in this field.
2. **Comprehensive Experiments**: The authors present extensive experimental results, including ablation studies, which provide a robust foundation for evaluating ICTSP’s effectiveness.
3. **Clarity of Presentation**: The paper is well-written and clearly presented, facilitating a good understanding of the approach and its contributions.

### Weaknesses
1. **Comparative Fairness**: The baselines use an input length of 512, while ICTSP utilizes an input length of 1440. This discrepancy could impact the fairness of the comparisons, potentially giving ICTSP an advantage due to the increased context window. The longer input sequence might allow ICTSP to capture longer-range dependencies that are not accessible to the baselines, leading to an unfair comparison of model capabilities rather than just architectural differences.
2. **In-context Example Selection**: ICTSP frames forecasting as an in-context learning task, but it uses adjacent historical data as context examples. This approach raises questions about whether the model truly learns from in-context examples or simply benefits from a longer input window and encodes the input tokens in a different manner. The use of adjacent data might not be a true test of in-context learning, as the model could be leveraging temporal dependencies within the input sequence rather than learning from the provided context examples in a generalizable way.
3. **Model Reduction Analysis**: Although the paper highlights the adaptive model reduction feature of ICTSP, there is limited visualization or analysis to support this claim. The paper lacks a detailed examination of how the model adapts its structure based on the input data, making it difficult to verify the effectiveness of this feature. Without concrete evidence, it remains unclear whether the model reduction is a significant contributor to performance or merely a byproduct of the architecture.

### Questions
1. Could you provide results with ICTSP’s input length ($L_I$) set to 512 for a more equitable comparison with other baselines in Table 1 and 6?
2. Could you conduct an ablation study on in-context examples, possibly using randomly selected examples (without look-ahead bias) instead of adjacent history to clarify the influence of this design choice?
3. Could you provide more detailed analysis or visualizations related to the Adaptive Model Reduction to support its impact on performance?
4. How does ICTSP handle cross-channel dependencies, especially in cases with specific inter-channel relationships in the data (like traffic)?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new in-context learning framework for time series forecasting by using "time series forecasting tasks" as input tokens. They show that this new framework outperforms the more traditional Temporal-wise Transformers and Series-wise Transformers across full-data, few-shot, and zero-shot settings.

### Strengths
In-context learning for time series forecasting is an important problem with wide applications. As far as I can tell, using "time series forecasting tasks" as input tokens is a new and interesting idea, and the authors demonstrate that it indeed has utility using systematic benchmarks. The approach has a "category theory" flavor to it, and the differences from earlier frameworks are well explained.

### Weaknesses
In terms of presentation, I think there is room to make it more accessible to readers not directly working in the same field. In particular, more detailed explanation and illustration of the "using time series forecasting tasks as input tokens" idea and how it is implemented could be helpful.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
4
