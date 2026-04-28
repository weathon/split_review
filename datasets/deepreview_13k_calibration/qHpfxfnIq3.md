# ToolComp: A Multi-Tool Reasoning & Process Supervision Benchmark

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 8, 5, 3

## Abstract
Despite recent advances in AI, the development of systems capable of executing complex, multi-step reasoning tasks involving multiple tools remains a significant challenge. Current benchmarks fall short in capturing the real-world complexity of tool-use reasoning, where verifying the correctness of not only the final answer but also the intermediate steps is important for evaluation, development, and identifying failures during inference time. To bridge this gap, we introduce ToolComp, a comprehensive benchmark designed to evaluate multi-step tool-use reasoning. ToolComp is developed through a collaboration between models and human annotators, featuring human-edited/verified prompts, final answers, and process supervision labels, allowing for the evaluation of both final outcomes and intermediate reasoning. Evaluation across six different model families demonstrates the challenging nature of our dataset, with the majority of models achieving less than 50% accuracy. Additionally, we generate synthetic training data to compare the performance of outcome-supervised reward models (ORMs) with process-supervised reward models (PRMs) to assess their ability to improve complex tool-use reasoning as evaluated by ToolComp. Our results show that PRMs generalize significantly better than ORMs, achieving a 19\% and 11\% improvement in rank@1 accuracy for ranking base and fine-tuned model trajectories, respectively. These findings highlight the critical role of process supervision in both the evaluation and training of AI models, paving the way for more robust and capable systems in complex, multi-step tool-use tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new dataset, ToolComp for complex planning involving the use of 2 or more tools. The dataset involves the use of 11 different tool calls across 485 different prompt and final answers. The final dataset consists of 1731 per step level annotations. The authors extensively compare the performance of instruction tuned models on the process supervision label prediction, as well as performance improvement in using PRMs vs ORMs when training to use as Reward Models.

### Strengths
> Tool use is an important area, and having more dataset/benchmark contributions in this area is useful. The use of step level supervision/verification also is proving to be a promising area making this contribution pretty timely.

> The empirical comparisons in this paper with existing IT checkpoints in zero-shot evals are pretty extensive and thorough

### Weaknesses
 > The contributed dataset is relatively small. With just 485 prompts, and 1731 per step level annotations. It makes it hard to justify using this dataset for large scale model training and pragmatically can only be used as a benchmark. 

> The experiments in section 5 lack sufficient details. I had to go into the details of the experiments in the Appendix to understand Section 5 better.

> Fig 3 compares Base vs SFT on verification using PRMs vs ORM. It is unclear if here was the Llama 3.1 Instruct the base model used for sampling trajectories or the final reward model. 

> Is the synthetic data mentioned as training data in Section 5 and Appendix E part of the dataset that is released with this paper? Why / why not?

### Questions
> Fig 3 compares Base vs SFT on verification using PRMs vs ORM. It is unclear if here was the Llama 3.1 Instruct the base model used for sampling trajectories or the final reward model. 

> Is the synthetic data mentioned as training data in Section 5 and Appendix E part of the dataset that is released with this paper? Why / why not?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new benchmark aimed at evaluating models’ ability to use multiple tools in multi-step tasks. The task prompts and golden answers in this benchmark are generated collaboratively by both LLMs and human annotators. Each instance is manually inspected to ensure task feasibility and answer accuracy, underscoring the rigor of the dataset. Additionally, the authors train two types of reward models, ORM and PRM, to assess their effectiveness in enhancing model performance on tool-usage tasks, demonstrating through experiments that PRM outperforms ORM.

### Strengths
1. The motivation for this paper is strong, addressing a gap in the field by providing a dataset that supervises the process of tool usage rather than just the final outcome, allowing for accurate evaluation of multi-step tool-use reasoning.
2. The method of generating queries and answers combines LLM outputs with human validation and careful inspection of each instance in the dataset, ensuring high efficiency.
3. For dataset evaluation, the authors implement LLM grading to avoid the limitations of exact-match grading, which can evaluate some complex answers.
4. The authors present a thorough analysis demonstrating the strong correlation between step-wise reasoning accuracy and final answer accuracy, and they provide additional evidence through reward model training that process rewards are critical for this task.

### Weaknesses
1. The evaluation is limited to general LLMs, without testing LLMs specifically fine-tuned for tool use. Including specialized tool-use LLMs could yield deeper insights into model performance in this particular task domain and highlight differences in tool-specific reasoning abilities.
2. Figure 8 (line 1206) reveals that among the 11 tools included, only four are frequently used, while the rest appear in very few instances. This usage pattern, particularly in the ToolComp-Chat subset, may introduce biases that limit generalizability. Additional analysis of tool usage distribution in the ToolComp-Enterprise subset could provide a more balanced view and potentially address these biases.

### Questions
1. In Section 3.2 (Prompt Creation) and Appendix A.1, the authors mention that initial IC examples are crafted by human annotators and subsequently expanded with examples generated by GPT-4 Turbo. Given this approach, could reliance on GPT-4 Turbo alone in prompt generation lead to a model-specific skill bias in these tasks? Would diversifying prompt generation across several LLMs reduce this risk and potentially improve generalization?
2. The ToolComp-Enterprise set has around 50% more instances than ToolComp-Chat, though Chat is designed for broader, general-purpose applications. Since general use cases are often more prevalent in real-world scenarios, wouldn’t it make sense for the Chat set to have more examples to reflect typical model usage?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces ToolComp, a benchmark for evaluating LLMs on complex reasoning using multiple tools. Data from the benchmark is created semi-automatically. The prompts, intermediate steps and the final answers are first generated by the LLMs and then checked and revised by annotators. LLMs are then asked to 1) reason over the prompts for complex reasoning and to 2) select the human-corrected answer versus the model-generated incorrect answer from intermediate steps. The authors further study how multi-step tool-use in ReAct format benefits from using process reward models (PRM) versus outcome reward models (ORM), by training the RMs using additionally generated data.

### Strengths
1. The benchmark introduced in this paper, i.e. ToolComp, is novel, sound and solid.
- Novelty: They novelly benchmark LLM-as-a-judge on intermediate steps in multi-step tool use. (Cf. Table 1)
- Soundness: 1) The way they evaluate LLMs on multi-step tool use is sound and they also incorporate 95% CIs which makes the results more convincing. 2) The setup of Chat and Enterprise is reasonable. 3) The LLM-as-a-judge evaluation is sound and serves as an important benchmark for both LLM evaluation and PRM training (as the author study later in the paper).
- Solidness: The benchmark is heavily supervised, and the authors have done well-round study on the data and statistics of the benchmark.
2. The comprehensive study on PRM versus ORM in ReAct format 1) further strengthens the value of the LLM-as-a-judge evaluation 2) paves the way for future study on PRMs for multi-step tool use.
3. The paper is coherent, dense and fluent.

### Weaknesses
1. The author mentioned that ToolComp is complex. However, from Table 1 we can only know that it has fewer number of tools. It'll be more convincing if the authors can report quantitative comparisons, e.g., accuracy of LLMs, to other benchmarks. Or, it will also be more convincing if the authors can elaborate on why the other tools are not included.
2. As the authors mentioned in Table 2, the Llamas should be used with constrained decoding to guarantee valid outputs. It is unclear whether constrained decoding is still used in the experiments from Figure 3.
- If it's not the case, would the performance boost come from learning the correct output format (which might also be one of sources of the performance gain from SFT).
- If it is the case (still using constrained decoding), is it possible to study whether the PRM can still work without constrained decoding? That said, can PRM also provide supervision over format correctness? I think including more ablations can help readers and researchers better understand how and when PRMs that trained in this way work.

### Questions
1. I think the experiments in the paper are insightful, and the only question I want to ask is the one the authors mentioned in the limitation chapter:
**Is there any chance for the authors to train the PRM using human-generated process rewards?** A simple demonstration would be really helpful. But I know it would be either labor-intensive or lacking fair comparison if trained on the subset of ToolComp. Thus, I will not reduce my score if the authors could not address the question.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ToolComp, a comprehensive benchmark designed to evaluate multi-step tool-use reasoning capabilities of AI systems. ToolComp consists of 485 human-edited prompts that require chaining together multiple tool calls, accompanied by human-verified final answers and step-by-step process supervision labels. The authors evaluate the performance of various state-of-the-art models on ToolComp, assessing their ability to reach the correct final answer and their intermediate reasoning ability. Additionally, the paper compares the performance of process-supervised reward models (PRMs) and outcome-supervised reward models (ORMs) on ToolComp, demonstrating that PRMs generalize better than ORMs in improving complex tool-use reasoning. Key contributions include:

1. A comprehensive evaluation framework with both final answer and step-wise assessment
2. Evaluation of 16 models across 6 families on complex tool-use tasks
3. Analysis comparing process-supervised vs outcome-supervised reward models
4. Human-verified ground truth labels and process supervision annotations

### Strengths
1. ToolComp is a well-designed and comprehensive benchmark that addresses a gap in existing benchmarks by focusing on complex, multi-step tool-use reasoning.
2. The inclusion of human-verified process supervision labels is a strength, enabling a more nuanced evaluation of models' intermediate reasoning abilities.
3. The evaluation of various state-of-the-art models on ToolComp provides a clear understanding of the current landscape and challenges in this area.
4. The comparison between PRMs and ORMs is insightful and highlights the importance of process supervision in improving tool-use reasoning capabilities.

### Weaknesses
1. Limited analysis of tool interaction patterns and failure modes. Specially, the paper does not provide a detailed analysis of the specific failure modes or error patterns observed in the evaluated models, which could be valuable for further improving these models. Specifically, it lacks a breakdown of where in the reasoning process models fail (e.g., tool selection, input generation, output parsing) and what types of errors are most common (e.g., incorrect tool usage, inability to handle tool outputs). This makes it difficult to pinpoint the exact bottlenecks in model performance.
2. Limited discussion of benchmark biases and limitations. The paper does not thoroughly discuss potential biases introduced during the benchmark creation process, such as human annotator biases in step correction, constraints imposed by the need for unambiguous prompts, and the influence of the generator model used to create initial trajectories. These biases could affect the generalizability of the benchmark and the conclusions drawn from it.
3. Unclear scalability of process supervision approach. The paper does not provide sufficient evidence to demonstrate how well the process supervision approach scales to more complex tool combinations. It is unclear whether the benefits of process supervision will persist as the number of tools and the complexity of tool interactions increase. This is a critical consideration for real-world applications where tool use may involve intricate sequences and dependencies.
4. Focus solely on text-based tasks, which may limit the generalizability of the findings to other modalities or domains. The benchmark's exclusive focus on text-based tasks restricts its applicability to scenarios involving other modalities, such as vision or audio. This limits the generalizability of the findings and raises questions about how well the models would perform in multi-modal environments.

### Questions
1. How representative are the synthetic training examples compared to human-verified ones?

2. What are the key patterns in how models chain different tools together?

3. How well does the process supervision approach scale to more complex tool combinations?

4. Could the authors elaborate on potential biases in the benchmark construction?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a new multiple tool-using benchmark named ToolComp. For each query, it not only labels the final answer similar to current benchmarks,  but also labels each reasoning/tool calling step for the whole problem solving procedure. ToolComp is developed through a collaboration between models and human annotators to ensure a accurate labelling.  The authors perform a comprehensive experiments to demonstrate the challenging nature of the dataset.

### Strengths
1. The authors perform comprehensive experiments on multiple LLMs families which may provides certain insights to the community.
2. With concerte implementation details, I could easily follow the whole paper to know how the work is actually done.

### Weaknesses
1.  I think the motivation for constructing this benchmark appears somewhat artificial: multi-step reasoning often requires
the evaluation for partial correctness or step-wise correctness of the reasoning trajectories. Why we need step-wise correctness? From the perspective of users relying on LLM for tool-using,  the primary concerns are always certain metrics: performance, cost, latency etc. The authors didn't provide a comprehensive justification for their motivation in the paper but with only few sentences in the introduction. This lack of clarity is a core issue within the study.

2. The labels utilized in this benchmark may not be accurate. Manually annotated ReAct trajectories do not necessarily serve as definitive golden labels. This benchmark seems to encourage LLM models to overfit specific ReAct reasoning chains rather than to develop correct reasoning paths. Defining the optimal trajectory is indeed challenging, so employing simpler yet meaningful metrics—such as accuracy, latency, and cost—would be more effective.

### Questions
Both ToolComp and ToolBench are evaluated through LLM with certain prompts and finally go through manual verfications.
Why you claim ToolBench doesn't have a verified final answer in Table 1?

### Soundness
2

### Presentation
3

### Contribution
2
