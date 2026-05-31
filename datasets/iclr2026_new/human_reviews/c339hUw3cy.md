## Human Reviewer 1

### Summary
The paper makes a solid and well-motivated contribution to kernel generation. It introduces the ConCuR dataset based on the novel observation that concise reasoning traces improve kernel generation, and presents KernelCoder, a state-of-the-art model capable of producing correct and efficient CUDA kernels. The work is clearly written, experimentally strong, and supported by thorough ablation studies.

### Strengths
The paper presents a substantive and well-motivated contribution to the challenging task of kernel generation.

1. The authors make an insightful observation that concise reasoning traces lead to better kernel generation performance. Building on this finding, they construct a new dataset (ConCuR) specifically designed around this principle.
2. The proposed model, KernelCoder, demonstrates strong technical quality. It is a state-of-the-art model capable of generating correct and efficient CUDA kernels.
3. The paper is clearly structured and well-presented. The motivation, methodology, and results are logically connected, making it easy to follow the authors’ reasoning and understand the contributions.
4. The experimental results show that KernelCoder consistently outperforms both frontier and fine-tuned models on KernelBench Level 1 and Level 2 benchmarks. The inclusion of an ablation study further strengthens the work by demonstrating the effectiveness of the dataset curation pipeline.

Overall, the paper offers novel insights and practical advancements for the field of kernel code generation. Through the creation of the ConCuR dataset and the development of KernelCoder, the authors provide a meaningful contribution that can inspire future research on reasoning-based code generation.

### Weaknesses
1. DeepSeek-R1 appears to be a very strong general-purpose reasoning model. When compared with KernelCoder, which is specifically trained for kernel generation, the performance gap does not seem particularly large. 
2. The paper should provide more information about the *Correctness Analysis* setup — including how many random inputs were used for validation, and what tolerance thresholds were applied when judging correctness.
3. It is unclear why KernelBench Level 3 experiments were not included. A justification for this maybe helpful.
4. In Section 3.4, for the second part of the dataset, the authors select samples achieving 5× speedup. The rationale for this specific threshold is not explained. It would be interesting to know how results might change with alternative thresholds (e.g., 3× speedup).
5. It would be valuable to include the performance of DeepSeek-R1-0528 in Table 5 for a more complete comparison.
6. Why choose Kevin to create dataset. possible to use DeepSeek-R1-0528? Or rounded to use kernelCoder to create dataset for next round training.
7. The dataset was created using Kevin, but the motivation for choosing this model over others (e.g., DeepSeek-R1-0528) is not fully explained. And is it possible to use KernelCoder itself to create dataset for next round training.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
Authors propose data generation and curation strategy for kernel generation using LLMs. Authors emphasize on generating chain-of-thought representation along with kernel code for supervised finetuning (SFT) of LLMs. Authors further demonstrate the efficacy of this strategy for SFT on opensource models. Authors point out two key and non-intuitive observations: 1) shorter reasoning lengths lead to better performance and 2) generated kernel performance improvement is not correlated to reasoning length. Authors compare their results with both open and closed source frontier models. KernelCoder, LLM finetuned with ConCuR strategy, outperforms frontier models in generating correct kernels though it lacks in obtaining performant ones.

### Strengths
1. ConCuR leverages generated chain-of-thoughts (CoT) for better refinement of LLMs.
2. To avoid overthinking related issues, shortest reasoning lengths are selected out of datapoints with highest speedup.
3. To account for high speedup cases, authors also select data points with >5x speedup over baseline.

### Weaknesses
- Illustration in Figure 1 is not completely clear. I would encourage authors to refer other published papers for improving this.
- In section 3.3, it is not clear which model was used (under what conditions) to generate the data.
- In section 3.3, out of 90K total collected kernels, did authors find only 24K kernels to be correct?
- In section 3.5, only 4,892 samples are reported to be used for finetuning. It is not clear what happened to those 90K or 24K data points.
- In section 4.2 the definition of pass@k evaluation (lines 318, 319). Authors should refer to Chen et. la., 2021 human eval (https://arxiv.org/abs/2107.03374) paper for more clarity.
- The data curation pipeline does not inspire scientific innovation. 
- Moreover, authors have not shown any way to determine the correctness of CoT steps. The bare assumption that generated CoTs are correct (even though the corresponding kernel maybe correct) isn't the right approach.
- Performance improvement of generated kernels is of vital importance to justify the cost spent in training/inference/generations. Lacking the details on hardware feedback processing does not inspire confidence in obtaining performant kernels.
- Case study shows naive details and does not show novel generated kernels that truly reflect thinking/reasoning from LLMs.
- Authors' approach achieves very low speedups in general. Other methods/approaches have demonstrated far more speedups in comparison.
- If authors' approach does not produce correct AND performant kernels more often then this approach does not contribute any innovation to the field.

### Questions
- How does this approach scale to low-resource languages such as Triton?
- Authors have not described in detail with evidence why is fast1 for L1 is worse than that of L2 in-spite of having easier problems in L1.
- Also refer to weakness section.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This work presents ConCuR, an SFT curated dataset that pairs PyTorch code, reasoning traces, and corresponding CUDA kernels, claimed to be the first of its kind. Built through an automated synthetic pipeline, ConCuR enables training of KernelCoder, a model fine-tuned specifically for kernel generation. The dataset facilitates stronger reasoning-to-code alignment, leading to state-of-the-art performance on the KernelBench benchmark and outperforming both open-source and proprietary models.

### Strengths
* The work is well-motivated, addressing the high cost and expertise required for developing efficient GPU kernel data.
* The evaluation setup includes a reasonable number and balanced distribution of models, providing adequate coverage for assessing the proposed method’s effectiveness.
* The work presents interesting insights into how reasoning can enhance kernel code generation, highlighting the potential benefits of integrating structured reasoning traces into low-level code synthesis.

### Weaknesses
* Some sections of the manuscript, particularly those describing the data synthesis and curation pipeline, would benefit from language refinement and stylistic polishing to improve clarity and readability.
* The evaluation setup is somewhat limited, relying on a single fine-tuned model and one benchmark (KernelBench). Expanding the evaluation to include additional benchmarks, such as TritonBench, and more diverse fine-tuned models would strengthen the empirical validation and demonstrate broader applicability.
* While the related work section covers key benchmarks and datasets relevant to kernel generation, it lacks a comparative table or structured analysis that clearly contrasts the proposed benchmark with existing ones. Including such a comparison, highlighting differences in dataset size, performance, cost, and methodology, would make the contribution’s advantages more explicit and easier to assess.

### Questions
* Could the authors clarify how task difficulty was considered or quantified during the dataset construction? The manuscript discusses reasoning length as an indicator of difficulty but does not clearly explain how this factor influenced data curation (if it did). Clarifying the role of task difficulty and its potential impact on the reported results would help strengthen the connection between the dataset design and the discussion section.

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes a dataset of reasoning traces for kernel generation that can be used as the basis of future SFT work on kernel llms.
It observes that for traces generated with current-generation LLMs, long traces correlate with _worse_ generation accuracy, and thus suggests to curate the dataset by selecting short traces that resulted in correct kernels.

### Strengths
* An open dataset like the one proposed would be valuable to the community
* The filtering based on trace length seems like an interesting approach.
* The reclassification of kernel bench tasks into more sensible difficulty classes is useful.

### Weaknesses
KernelBench is _not_ a reliable benchmark. Many of its shapes are too small, and the choice of pytorch eager as a baseline means you're mostly profiling against overhead.
To get a meaningful interpretation of the speed of the generated kernels, it would be important to calculate their speed-of-light, i.e., how long they would take to execute based on the GPUs flops and memory bandwidth, and then show what percentage of this speed is achieved.

Furthermore, I'm worried about about dataset contamination. The kernels in KernelBench were chosen because they are common operations, and I'd be surprised if among the 9,789 tasks you selected from kernel book, there was not a significant overlap.
This isn't a bad thing for the dataset to be released in itself (if I want to train a kernel llm, I do want all the popular kernels in the training set, after all), but it makes it hard to trust any of the metrics reported in the paper.

I would also say that the central observation about conciseness should be stated a bit more carefully. When generated by current-generation LLMs, short traces work better than long traces. That might not be the case for better future LLMs that don't "wait" so often, or for human-generated traces.

### Questions
(How) have you ensured that the tasks tested on in kernel bench are not part of the training set from kernel book.

Have you validated that the shapes for which speed-ups are reported are actually of a meaningfully large size. How do they compare against torch compile? What percentage of the speed-of-light is achieved?

For getting the fastest of 10 generations, do you select the time of the fastest run, or do you select the code of the fastest run, and re-time it again independently?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
3