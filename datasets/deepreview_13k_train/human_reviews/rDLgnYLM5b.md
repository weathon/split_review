# Interleaved Scene Graph for Interleaved Text-and-Image Generation Assessment

- Decision: Accept
- Scores: 6, 8, 8, 6, 8

## Abstract
Many real-world user queries (e.g.~\textit{``How do to make egg fried rice?''}) could benefit from systems capable of generating responses with both textual steps with accompanying images, similar to a cookbook.
Models designed to generate interleaved text and images face challenges in ensuring consistency within and across these modalities.
To address these challenges, we present \textsc{ISG}, a comprehensive evaluation framework for interleaved text-and-image generation. \textsc{ISG} leverages a scene graph structure to capture relationships between text and image blocks, evaluating responses on four levels of granularity: holistic, structural, block-level, and image-specific. This multi-tiered evaluation allows for a nuanced assessment of consistency, coherence, and accuracy, and provides interpretable question-answer feedback.
In conjunction with \textsc{ISG}, we introduce a benchmark, \textsc{ISG-Bench}, encompassing 1,150 samples across 8 categories and 21 subcategories. This benchmark dataset includes complex language-vision dependencies and golden answers to evaluate models effectively on vision-centric tasks such as style transfer, a challenging area for current models. 
Using \textsc{ISG-Bench}, we demonstrate that recent unified vision-language models perform poorly on generating interleaved content. While compositional approaches that combine separate language and image models show a 111\% improvement over unified models at the holistic level, their performance remains suboptimal at both block and image levels.
To facilitate future work, we develop \textsc{ISG-Agent}, a baseline agent employing a \textit{``plan-execute-refine''} pipeline to invoke tools, achieving a 122\% performance improvement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a multi-level evaluation framework, INTERLEAVED SCENE GRAPH (ISG), along with a benchmark dataset, ISG-BENCH, to address the challenges of evaluating multimodal interleaved text-and-image generation tasks. Additionally, the authors propose ISG-AGENT, a compositional generation framework designed to explore the upper limits of interleaved generation with a structured agent-based workflow.

### Strengths
1. Propose a novel ISG framework and ISG-BENCH benchmark dataset that fill a notable gap in the evaluation of multimodal interleaved generation. 
2. The multi-level evaluation in ISG, combining visual question answering (VQA) with reasoning-based questions, offers a fine-grained approach to assess the structure and quality of generated content in complex multimodal tasks.
3. The creation of ISG-BENCH, covering 21 multimodal generation tasks, provides a standardized dataset for researchers.

### Weaknesses
1. The description of the methodology could be more detailed, for example, in terms of the experimental setup. Specifically, the paper lacks clarity on the exact configurations of the models used for both the ISG-AGENT and the baseline comparisons. Details regarding the training procedures, such as the number of epochs, learning rates, batch sizes, and optimization algorithms, are missing. Furthermore, the paper does not specify the hardware used for the experiments, which is crucial for reproducibility. The description of how the VQA and reasoning-based questions are generated and integrated into the evaluation framework is also vague, making it difficult to understand the precise methodology.

2. While ISG-AGENT performs well across tasks, it still exhibits notable shortcomings in specific areas. The paper does not provide a detailed analysis of the types of errors that ISG-AGENT makes, nor does it offer insights into why these errors occur. For example, it would be beneficial to understand if the agent struggles more with specific types of visual reasoning or with particular text generation patterns. A more granular analysis of the failure cases would be valuable. Additionally, the paper does not explore the limitations of the compositional approach itself, such as potential bottlenecks in information flow between different modules or the impact of error propagation from one module to another.

### Questions
Please refer to weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new benchmark for evaluating the interleaved text-and-image generation tasks. While previous multimodal benchmarks only focus on evaluating vision understanding ability where only text outputs are required, this benchmark designed 21 text-image generation tasks with 1150 samples in total. The benchmark have multiple-level of evaluation including structure, block, image, and holistic levels. They also propose a ISG-Agent, which utilize external tools to fulfill the requirements of the benchmarks. Results show that existing models fall short of the benchmark and ISO-Agent performs significantly better than baseline models.

### Strengths
1. This paper presents first benchmark to evaluate the models that can generate interleaved text-and-image models, which differs fundamentally from previous vision understanding benchmarks like MMMU. The benchmarks feature an important usage of multimodal models for content generation, and can greatly impact the community if well-maintained and updated.
2. The design of ISG-Agent is reasonable and novel, achieving state-of-the-art performance on the ISG-Bench. The introduce of Planning, Tool-usage, and refinement works well in practice.
3.  The analysis part brings many insights such as MLLM-as-a-Judge cannon evaluate well due biases like "image-qualtiy bias", etc.

### Weaknesses
1. The evaluation still uses GPT-4o as a judge, which can bring a lot of bias, as section 4.2 states. The 
2. It might be a bit unfair to compare ISG-Agent with another model that can generate interleaved text and images in a whole, as the agent still uses external tools and additional inference tokens for planning, etc. I am not saying ISG-Agent is not good. But it should also be compared with other agents for a fair comparison.

### Questions
1. What's the cost of evaluating a new model on the ISG-Bench since evaluation heavily relies on the GPT-4 in the process
2. While you recognize the potential bias of using MLLM as a judge for evaluating image quality, did you figure out any ways to mitigate the bias? Have you conducted any human studies to understand how will these kinds of biases affect the evaluation of the benchmark?
3. How many resources does ISG-Bench need to finish a query in the ISG-Bench? Is it comparable with using other models like show-o to directly generate the outputs?
4. There are many samples in your datasets that have images in the query. Have you ever conducted any study that removes the image in the query and keeps only the text part, then conduct the evaluation in a text-input-only setting? This is to see the gap between the normal setting and make sure that these images in the query are really important to generate a good response, which is now a pretty common analysis for the vision understanding benchmarks.

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
This paper presents a unified approach for evaluating interleaved multimodal text-and-image generation using a novel framework called INTERLEAVED SCENE GRAPH (ISG), which assesses generation accuracy at four granular levels through atomic question-based visual verification. Additionally, it introduces ISG-BENCH, a benchmark of 1,150 samples across 21 generation tasks, and ISG-AGENT, a compositional agent framework designed to explore the limits of interleaved generation. The study’s experiments reveal that, while ISG enables precise evaluation aligned with ground truth and human preferences, existing models often fail in accurate instruction-following, particularly in vision-dominated tasks, highlighting areas for improvement in multimodal generation research.

### Strengths
- This is a timely work that studies the critical and underexplored challenge of evaluating the recent popular unified models.

- ISG-BENCH provides a comprehensive benchmark with 1,150 carefully designed samples across 21 tasks, supporting standardized evaluation in multimodal generation.

- The paper conducts extensive multi-granular evaluations, offering a thorough assessment that reveals limitations in current models.

- The proposed ISG-AGENT explores the upper bounds of interleaved generation, highlighting strengths and limitations within the framework.

- The paper is very well written and organized.

### Weaknesses
 - The model evaluation is relatively complex, as many steps involve MLLMs and LLMs to assess results. Given that the author's proposed task is more challenging, how reliable are current MLLMs and LLMs in this evaluation? Specifically, the reliance on these models for both question generation and answer verification introduces a potential for cascading errors. If the MLLM generates a flawed question, the subsequent answer verification, even if accurate relative to the flawed question, will not reflect the true performance of the evaluated model. This raises concerns about the robustness of the evaluation framework.

- Some tasks seem overly simplistic and not directly relevant to multimodal generation—for instance, Image Decomposition, which resembles a basic computer vision task. The inclusion of tasks like simple segmentation raises questions about the benchmark's focus. It's unclear why a task that can be effectively addressed by traditional computer vision methods is included in a benchmark designed to evaluate unified multimodal models. This dilutes the benchmark's focus on the unique challenges of interleaved text-and-image generation. Has there been any explanation of the criteria used to filter these task categories?

### Questions
- I believe the intent of this benchmark should be to establish samples that are well-suited to tasks requiring both text and image generation for optimal performance, correct? If the agentic approach can yield good results, might this indicate that the benchmark isn't ideally suited for evaluating a unified model? If the benchmark contains some tasks that only a unified model could perform well, that would be even better.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
the paper proposed one multimodal benchmark, named ISG-BENCH, and one agent-based approach to tackle the problem. the focus is the interleaved image-text data as the model output, which is a promising direction in the field. in the benchmark, there are 4-level evaluation methods, which is structure, block, image, and holistic. these provide multiple perspectives to study the model performance. the proposed agent-based approach also achieves the best among all the existing and the baseline approaches.

### Strengths
the proposed benchmark is a multi-granular evaluation set for interleaved text-and-image generation. this provide options to study the model performance through various perspectives. 

the proposed benchmark scale is the largest by far, as shown in the paper Tab 1, consisting of 1k+ samples, in 21 categories. this could be the primary contribution to the community.

the agent-based approach utilizes a "Plan-Execute-Refine" structure, with tool use. This compositional approach shows promise in generating high-quality outputs and provides a strong baseline for further research.

### Weaknesses
the primary contribution could be the benchmark with multi-granularity evaluation. on one hand, this is great to provide more options. on the other hand, this may suggest this work is a combination of multiple existing approaches, e.g. by combining openleaf and interleavedbench. although the work provides some unique features, e.g. structure-level evaluation, however, the most important evaluation metric could be the holistic evaluation, which has already been studied in the literature. 

the multi-granularity evaluation is performed by different approaches. would be it possible to use only one approach (e.g. MLLM) to evaluate all these perspectives in a more unified, simpler, more elegant way?  

considering the holistic evaluation may be the most important, it is better to show more study on why the proposed MLLM-as-the-judge is a good judge, e.g, how the evaluation is aligned with the human judgement. if approach A is better than approach B from MLLM-as-the-judge, is it also true for human judgement? what kind of failure cases could be with the MLLM-as-the-judge.

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a new evaluation method and benchmark for the interleaved image-text generation task, which aims to generate coherent image text contents for queried use cases, such as instruction generation, visual storytelling, and others (Table 2, Figure 3). For evaluation, the study presents converting multimodal queries into atomic questions for a better scoring than MLLM-based evaluations. The constructed benchmark contains 1150 samples covering 21 generation scenarios. In addition to existing methods, an agent framework named ISG-AGENT is also proposed to enhance the performance.

### Strengths
1. The proposed evaluation aims to address the problem that MLLM evaluation alone is not reliable. This is a valid question, and the proposed improvements: (1) multi-granular evaluation; (2) converting to question answering, do serve as an effective add-on for evaluation.

2. The benchmark covers a wide range of evaluation scenarios for the interleaved image-text generation.

3. The paper is presented well, with sufficient discussion on evaluation pipeline, related works, and evaluation categories.

### Weaknesses
1. One concern is on the definition of the task “interleaved image-text generation,” related to the discussion in the first paragraph of introduction. The current definition of the task is based on the application scenarios, which are valid and of good application value. However, it fails to provide extra insights to the task, including what are the unique challenges, and how to balance the categories and samples in the evaluation benchmark.

For the categories and samples percentage, the benchmark already covers a wide range of scenarios (Table 2, Figure 3). But the motivation of the percentage and construction remains unclear: why certain scenarios are selected, how to decide between 50/100 samples, and whether there is an “ideal” distribution to follow for the task. 

2. The experiment evaluates various interleaved generative frameworks.

Related to the task’s unique challenge discussions, it would be helpful to discuss whether the image and text generation can be disentangled: providing insights on whether agent systems or naturally multimodal (unified) models (e.g., GPT4o and others) are more promising in the future. The experiments discuss the performance of existing models in these two lines, but fail to suggest future directions on them.

The current observation is that the open-sourced “unified model” is much worse compared with agent systems. This is partially because some of the better unified models are not open-sourced. It would be interesting to add a few examples compared with the demos shown in their paper/webpage, to provide insights on “future better unified models.” (e.g., https://openai.com/index/hello-gpt-4o/ Explorations of capabilities: Visual narratives - Sally the mailwoman) And when both directions have comparable base capacity, what are there relative strengths and weaknesses.

3. The “GT” in abstract and Table 1 still works on pre-selected evaluated models, instead of extending to arbitrary new models to evaluate. Therefore, the evaluation could still remain noisy similar to MLLM-scoring.

### Questions
1. In Table 1, for OpenLeaf (An et al., 2023), why is the number of samples 30 instead of 660 listed in the paper?

2. It would be helpful to discuss the plan on setting up and maintaining the automatic evaluation benchmark for easier and wider use.

3. More examples on the evaluation questions, and category examples are helpful.

### Soundness
3

### Presentation
3

### Contribution
2
