# Evaluating the Generalization Ability of Quantized LLMs: Benchmark, Analysis, and Toolbox

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Large language models (LLMs) have exhibited exciting progress in multiple scenarios, while the huge computational demands hinder their deployments in lots of real-world applications. As an effective means to reduce memory footprint and inference cost, quantization also faces challenges in performance degradation at low bit-widths. Understanding the impact of quantization on LLM capabilities, especially the \emph{generalization ability}, is crucial. However, the community's main focus remains on the algorithms and models of quantization, with insufficient attention given to whether the quantized models can retain the strong generalization abilities of LLMs. In this work, we fill this gap by providing a comprehensive benchmark suite for this research topic, including an evaluation system, detailed analyses, and a general toolbox. Specifically, based on the dominant pipeline in LLM quantization, we primarily explore the impact of calibration data distribution on the generalization of quantized LLMs and conduct the benchmark using more than 40 datasets within two main scenarios. Based on this benchmark, we conduct extensive experiments with two well-known LLMs (English and Chinese) and four quantization algorithms to investigate this topic in-depth, yielding several counter-intuitive and valuable findings, \eg, models quantized using a calibration set with the same distribution as the test data are not necessarily optimal. Besides, to facilitate future research, we also release a modular-designed toolbox, which decouples the overall pipeline into several separate components, {\it e.g.}, base LLM module, dataset module, quantizer module, {\it etc.} and allows subsequent researchers to easily assemble their methods through a simple configuration.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors proposed a benchmark for evaluating the post-training quantized large language models (LLMs) generalization ability. They considered two scenarios and utilized 40 datasets. Additionally, they released a modular-designed toolbox.

### Strengths
The authors conducted comprehensive experiments, providing meaningful results that highlight the impact of calibration data on post-training quantization accuracy.

### Weaknesses
compared to post-training quantization, the influence of data on quantization finetuning methods, such as Q-LoRA, is more significant. This is because the calibration data for post-training quantization is limited, making the model more susceptible to overfitting and data influence in Q-LoRA. 

Regarding the accuracy numbers presented in the table, it's important to know whether they represent a single trial or are averaged across multiple trials. Quantized networks can exhibit variance, and relying on a single trial may not provide reliable guidance. It is crucial to comprehend the inherent variability of a specific PTQ method prior to drawing conclusions regarding the impact of data on quantization accuracy. Specifically, the lack of reported variance makes it difficult to assess the statistical significance of the observed differences in performance across different calibration datasets. Furthermore, the study does not explore the impact of calibration data size, which is a critical factor in post-training quantization.

### Questions
Did the authors experiment with different samples from the C4 dataset? 
Did authors measure variance even when using the same dataset, like C4, but with different examples? 
Understanding these aspects would provide deeper insights into the robustness and reliability of the quantization process.

In line 1249, the authors mentioned: We present the average results with random seeds 42 and 567. Why particular choose 42 and 567 as random seed? What if we use other random seeds, like 0 or 1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper delves into the impact of the calibration set on the generative capacity of quantized LLMs through extensive experiments. In addition, a novel modular-designed toolbox is proposed to decouple the model quantization pipeline into seperate components to help investigate the different modules.

### Strengths
1. This paper thoroughly considers a vast array of datasets and scenarios, which make clear and effective distinctions, to support its experimental conclusions.

2. The quantization methods adopted are all currently mainstream, demonstrating the universality of the experimental discoverages.

### Weaknesses
1. A serious issue is that the authors claim that this article is the first to study the impact of the calibration set on the generative capacity of quantized large models. However, to my knowledge, similar work has already been done previously [1]. Therefore, the authors' statement is quite inappropriate.

2. The number of LLMs using for quantizing in the experiment is too small, and their size is relatively small (7B). This limits the generality of the experimental results to a certain extent.

3. This article appears to be a superficial description and summary of experimental phenomena, lacking in-depth discussion.

### Questions
1. For W1, apart from revising their statement, the authors also need to provide a detailed description of the differences between their research and the mentioned paper. Since the objectives and main content of this work and the mentioned one are extremely similar, failing to provide clear distinctions is a significant issue.

2. For W2, in the past research, it has been proven that larger LLMs are less sensitive to quantization. Therefore, due to the time constraint of the rebuttal, there is no need to extend the experimental models to various sizes. It suffices to provide experimental data on the largest model (e.g., llama2-70B) to demonstrate that the current conclusions remain valid.

3. For W3, one of the main contributions of a benchmark is to provide guidance for future work. Therefore, the authors should offer some appropriate suggestions based on the experimental results. For example, they should recommend which dataset is best suited as a calibration set for future quantization methods to achieve optimal results. In more detail, although different calibration sets may yield varying results, a comprehensively optimal dataset should be selected for calibration.

4. The athors should further describe the definition of IID and OOD which appears abruptly. Does IID means the different or the same dataset under the same subject?


[1] Miles Williams and Nikolaos Aletras. 2024. On the Impact of Calibration Data in Post-training Quantization and Pruning. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 10100–10118, Bangkok, Thailand. Association for Computational Linguistics.

### Soundness
3

### Presentation
3

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
This paper explores the generalization performance of quantized LLMs and introduces a comprehensive benchmark suite alongside a modular toolbox. The study examines how calibration data distribution affects generalization, revealing two key insights:
1. Tasks exhibit varying sensitivity to quantization, with some tasks showing improved performance under low-bit quantization.
2. Consistency between calibration and test data distributions does not consistently yield optimal performance.

### Strengths
- **Extensive Empirical Evaluation**: The study conducts comprehensive experiments across multiple datasets and quantization methods, providing valuable insights into LLM generalization under different calibration scenarios.
- **Practical Contribution**: The proposed modular toolbox is a significant resource for the evaluation and application of quantized LLMs, potentially benefiting the broader research community.

### Weaknesses
1.  **Lack of Guidance on Calibration Data Selection**: Although the paper presents intriguing findings, it does not offer concrete criteria or methods for selecting calibration data to enhance the generalization of quantized LLMs. This limits its practical impact and novelty.
2.  **Visualization Issues**: 
    - Radar charts (Figures 2, 5, and 6) lack marked magnitudes for the scores on the radius, and text overlays reduce clarity.
    - The task types, while indicated by background colors, are not explicitly labeled. An additional legend would make the visualizations more intuitive.

### Questions
1. The paper highlights task-specific sensitivities to quantization. Could the authors provide more detailed analysis or theoretical insights into why some tasks are more robust than others?
2. Given that the evaluation could potentially be performed by extending existing toolboxes, what is the necessity of developing a new quantization and evaluation framework?

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
This paper addresses the gap in understanding how data impacts the generalization abilities of quantized large language models (LLMs). By benchmarking with over 40 datasets and experimenting with popular LLMs, the study reveals the non-optimal performance of models quantized with calibration data matching the test data distribution. Additionally, the authors provide a modular toolbox to support future exploration into LLM quantization.

### Strengths
1. Very large experimental workload. The authors implemented a Python package integrating various LLM quantization models, based on which a large number of experimental results were measured. 
2. From the perspectives of IID and OOD, detailed experimental data provide useful insight into the generalization performance of quantifying LLM.

### Weaknesses
1. This paper does not propose new algorithms but rather tests quantization algorithms proposed by other researchers before. Can the authors provide some more insights, such as: does the generalization performance of different quantization algorithms differ?
2. Eq1 simply uses the number of samples where the performance of the I.I.D calibration set exceeds that of the OOD to evaluate, which is actually a little crude. LLM evaluation is a dirty task, and the accuracy of only higher a little does not mean that the model is better. This will weaken the validity of the paper's conclusions. It is recommended to have some statistical technical hypotheses and tests (like the Box-and-Whisker Plot or standard deviation).

### Questions
1. Will MI continue to be developed to support new LLM quantization algorithms? 
2. L462-L464, the authors utilize a dataset consisting of 128 random segments and each containing 512 tokens. This is actually a bit odd, as 128*2048 token length calibration sets are more common. Therefore, does the size of the calibration set affect the generalization performance of the quantization model? For example, different sequence numbers (e.g. 1,16, 128, 512, 1024) and lengths (e.g. 128, 512, 1024, 2048). 
3. Similarly, the author mainly discusses the 7B-13B size model in this paper. Will the conclusion change for the 70B+ model? Intuitively, the 70B model would be more redundant and easier to quantify.

### Soundness
2

### Presentation
3

### Contribution
2
