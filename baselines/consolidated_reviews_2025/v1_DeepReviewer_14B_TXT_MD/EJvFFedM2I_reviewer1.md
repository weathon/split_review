### Summary

The paper introduces a new benchmark for temporal reasoning composed of ten datasets, encompassing various temporal aspects of events such as order, arithmetic, frequency, and duration. The authors evaluate several LLMs in zero-shot and few-shot scenarios, and establish baselines with BERT-based and domain-specific models. The results indicate that the best-performing model lags significantly behind human performance.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a new benchmark for temporal reasoning.
2. The authors provide a comprehensive evaluation of several LLMs and baseline models on the proposed benchmark.
3. The paper is generally well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation behind the choice of the ten tasks is not clear. The authors should provide a more detailed explanation of why these specific tasks were chosen and how they represent the key aspects of temporal reasoning.
2. The contribution of the paper is limited. The datasets used in the benchmark are mostly existing datasets, and the evaluation is mostly a straightforward application of these datasets. The authors should clarify the novelty of the benchmark and how it advances the field of temporal reasoning.
3. The paper lacks a thorough analysis of the results. The authors should provide a more in-depth discussion of the performance of different models on different tasks, and identify the key challenges and limitations of current approaches to temporal reasoning.

### Suggestions

The authors should provide a more detailed justification for the selection of the ten tasks included in their benchmark. While the tasks cover various aspects of temporal reasoning, the paper lacks a clear explanation of why these specific tasks were chosen over others and how they collectively represent the full spectrum of temporal reasoning capabilities. For example, the authors could discuss the specific temporal phenomena that each task is designed to evaluate, and how these phenomena relate to the broader field of temporal reasoning. A more detailed discussion of the task selection process would strengthen the paper's contribution and provide a clearer understanding of the benchmark's scope and limitations. Furthermore, the authors should clarify how the chosen tasks are interconnected and how performance on one task might influence performance on another. This would help to establish the benchmark's validity and demonstrate its ability to provide a comprehensive evaluation of temporal reasoning abilities.

The paper needs to more clearly articulate the novelty and contribution of the proposed benchmark. While the authors use existing datasets, the paper should emphasize how the combination of these datasets into a single benchmark, along with the specific evaluation protocols, advances the field of temporal reasoning. The authors should explicitly state what is unique about their benchmark compared to existing resources. For example, do the tasks cover a wider range of temporal phenomena, or do they provide a more challenging evaluation environment? The authors should also discuss the limitations of existing benchmarks and how their proposed benchmark addresses these limitations. This would help to justify the need for a new benchmark and highlight its significance to the research community. Furthermore, the authors should provide a more detailed explanation of the evaluation metrics used and justify their choice. A more thorough discussion of the evaluation methodology would enhance the paper's credibility and ensure that the results are interpreted correctly.

The paper would benefit from a more in-depth analysis of the experimental results. The authors should provide a more detailed discussion of the performance of different models on different tasks, highlighting the strengths and weaknesses of each model. For example, the authors could analyze why certain models perform well on some tasks but struggle on others. This would provide valuable insights into the specific challenges of temporal reasoning and help to identify areas for future research. The authors should also discuss the limitations of current approaches to temporal reasoning and suggest potential directions for improvement. A more thorough analysis of the results would enhance the paper's impact and provide a more comprehensive understanding of the current state of the field. Additionally, the authors should consider including error analysis to better understand the types of mistakes that models are making and to identify potential biases in the benchmark.

### Questions

1. What is the rationale behind the choice of the ten tasks in the benchmark? How do these tasks represent the key aspects of temporal reasoning?
2. What is the contribution of the paper? The datasets are mostly existing datasets, and the evaluation is mostly a straightforward application of these datasets.
3. Can the authors provide a more detailed analysis of the results and discuss the implications for future research on temporal reasoning?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
