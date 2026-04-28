# Efficiency Pentathlon: A Standardized Benchmark for Efficiency Evaluation

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 3, 5

## Abstract
Rising computational demands of modern natural language processing (NLP) systems have increased the barrier to entry for cutting-edge research while posing serious environmental concerns. Yet, progress on model efficiency has been impeded by practical challenges in model evaluation and comparison. For example, hardware is challenging to control due to disparate levels of accessibility across different institutions. Moreover, improvements in metrics such as FLOPs often fail to translate to progress in real-world applications.
In response, we introduce efficiency \name, a benchmark for holistic and realistic evaluation of model efficiency. \name focuses on inference, which accounts for a majority of the compute in a model’s lifecycle. It offers a strictly-controlled hardware platform, and is designed to mirror real-world applications scenarios. It incorporates a suite of metrics that target different aspects of efficiency, including latency, throughput, memory overhead, number of parameters, and energy consumption, hence the name {\bf Penta}thlon. 
It also comes with a software library that can be seamlessly integrated into any codebase and enable evaluation. 
As a standardized and centralized evaluation platform, \name can drastically reduce the workload to make fair and reproducible efficiency comparisons. 
While initially focused on natural language processing (NLP) models, \name is designed to allow flexible extension to other fields.
We envision \name will stimulate algorithmic innovations in building efficient models, and foster an increased awareness of the social and environmental implications in the development of future-generation NLP models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a benchmark for evaluating model efficiency (compared with most benchmarks on performance), in particular, for LLM inference. It compares different use case scenarios for calling an LLM as well as using several metrics to evaluate the inference efficiency and environmental impacts.

### Strengths
* Propose several use case scenarios for model inference, like batching, streaming, offline, etc.
* Propose several metrics to measure the model inference efficiency as well as environmental impact

### Weaknesses
 * Benchmark selection is a bit limited, only a few tasks are chosen. For instance, there is no typical (monolingual) language generation task

### Questions
* Figure 3 (a) and (b) are exactly the same? Is it a coincidence or mistake?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces `Pentathlon`, a benchmark created for the comprehensive and realistic evaluation of model inference efficiency. Pentathlon provides a strictly controlled hardware platform, including GPUs and CPUs, and incorporates a suite of metrics targeting different aspects of efficiency, including latency, throughput, memory overhead, parameter count, and energy consumption. As a standardized and centralized evaluation platform, Pentathlon aims to significantly reduce the workload required for fair and reproducible efficiency comparisons. While its initial focus is on natural language processing (NLP) models, Pentathlon is designed to be flexibly extended to other fields.

### Strengths
-   Clarity: The paper is exceptionally well-written, offering a comprehensive presentation of the Pentathlon benchmark suite. The authors provide a detailed explanation of its design, which emphasizes equitable model comparisons and incorporates testing settings for both CPUs and GPUs.
  
-   Thoughtful Metric Selection: Pentathlon's use of five carefully chosen evaluation metrics addresses critical properties of models, ensuring that the benchmark accurately assesses key aspects of efficiency.
    
-   Visual Aid: The inclusion of radar charts is a notable advantage, as they effectively illustrate the strengths and weaknesses of models, making it easier for readers to comprehend the benchmark's findings.
    
-   Centralized Benchmarking: While the concept of centralized benchmarking isn't entirely novel, it remains highly valuable for gaining a deeper understanding of the diverse impacts algorithms have on model efficiency. Pentathlon offers a structured and standardized approach to this essential process.
    
-   Realistic Workloads: The authors' meticulous design of workloads to mirror batching scenarios and real-world service loads enhances the reliability of the benchmark's results, ensuring they are more reflective of practical use cases.

### Weaknesses
1.  Hardware Flexibility: While the authors have outlined CPU and GPU settings, it remains unclear whether the benchmark suite can easily accommodate other hardware platforms. Given the growing popularity of new platforms like Metal, ROCm, Mali, and Vulkan, it's essential to address the adaptability of Pentathlon to ensure it remains relevant and applicable to diverse hardware configurations. Moreover, certain models, such as Llama-70b, may require multiple high-end GPUs like A100 or H100 for distributed inference, highlighting the need for flexibility in hardware options. The current description lacks details on how the benchmark would handle multi-GPU setups, which are increasingly common for large models.
    
2.  Software Environment Assumptions: The paper primarily focuses on a specific software environment, potentially overlooking the fact that various software stacks, such as TVM and Cutlass, may require an additional step called tuning. This tuning phase optimizes the compilation stack for the given hardware, which can significantly improve model performance. However, the tuning process itself may not always be efficient and can be time-consuming. It's crucial to consider these software-related aspects for a more comprehensive evaluation. The paper does not specify how the benchmark accounts for the variability introduced by different optimization levels or tuning strategies within these software stacks.
    
3.  Controlled Hardware vs. Cloud-Based Platforms: While the controlled hardware setting provides fairness and accuracy, it may not fully cater to researchers who heavily rely on cloud-based platforms like AWS, Azure, or Google Cloud. Many recent large language models (LLMs) are built and deployed on cloud platforms, and their efficiency and latency results may significantly differ from those obtained in a controlled environment. To make Pentathlon more applicable to a wider range of real-world scenarios, consideration could be given to extending the benchmarking to include cloud-based machines and their specific challenges. The paper should address how the benchmark results on controlled hardware correlate with performance on cloud-based systems, as these environments often have different resource constraints and virtualization overhead.

### Questions
1.  What level of effort is required to expand Pentathlon to accommodate a new hardware platform or incorporate a new model into the benchmark?
2.  Beyond the BLEU score, are there additional metrics available within Pentathlon to assess model quality, such as perplexity or other relevant NLP-specific metrics?
3.  How can you distinguish the impact of "algorithmic innovations" from other efficiency-related factors in the Pentathlon benchmark?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents Pentathlon, a benchmark for holistic and realistic evaluation of model efficiency. The benchmark offers a strictly controlled hardware platform and incorporates metrics to measure efficiency, including latency, throughput, memory overhead, number of parameters, and energy consumption. The authors also provide a software library that can seamlessly integrate into any codebase and enable evaluation.

### Strengths
- The paper introduces a standardized and centralized evaluation platform, which can reduce the workload to make fair and reproducible efficiency comparisons and stimulate algorithmic innovations in building efficient models.

### Weaknesses
 - The paper is more like a technical report, which may suit a benchmark or industry track. It would be great if the authors could provide additional scientific findings and conclusions through the evaluations. This work has provided a relatively comprehensive and mature evaluation benchmark. With more inspiring and interesting findings and conclusions based on the evaluations, the paper would be more valuable to the community.

- There are many datasets designed for large language model evaluation. Using classical tasks (e.g., machine translation, mathematical reasoning, and classification) makes the experiments less convincing.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Evaluating the model efficiency is an important evaluation aspect for practical applications. The paper claimed that existing metics, such as FLOPs often did not reflect the advantages of the models in real-world applications. So, it proposes efficiency Pentathlon, a benchmark of holistic and realistic evaluation of model efficiency, including five ways: standard hardware enviroment, four distinct evaluation scenarios, diverse metrics for comprehensive efficiency evaluation, a evaluation software library, and flexiable evaluations. The established benchmark contain three NLP tasks and the corresponding datasets (WMT14 DE-EN, GSM8K, RAFT). The evaluation results show that the proposed Pentathlon could drastically reduce the workoad to make fair and reproducible effciency comparisons.

### Strengths
1) Efficiency evaluation is very important for model evlaution and seldomly addressed before.
2) The proposed five evaluation aspects are interesting and novel.

### Weaknesses
1) The whole paper is not very clear. In the section 2,  the reason that considering the proposed five aspects for effeciency evaluation is not described clearly.
2) The experimental parts are not very suffcient. Only two tasks are selected which makes the results not very convincing.

### Questions
1) Table 1 is not very clear. What is the schema meaning in table 1, such as Acc., TP., Latency, Mem., etc. The authors should describe them in the tabel title.
2) What did only three kinds of NLP tasks are selected? I concern what are the results in other NLP tasks.
3) Why this benchmarks could be trusted and applied when evaluting the real-applications. The authors should prove the advantages of the proposed benchmarks and plantforms.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
