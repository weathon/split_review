# MIA-Bench: Towards Better Instruction Following Evaluation of Multimodal LLMs

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We introduce MIA-Bench, a new benchmark designed to evaluate multimodal large language models (MLLMs) on their ability to strictly adhere to complex instructions. Our benchmark comprises a diverse set of 400 image-prompt pairs, each crafted to challenge the models' compliance with layered instructions in generating accurate responses that satisfy specific requested patterns. Evaluation results from a wide array of state-of-the-art MLLMs reveal significant variations in performance, highlighting areas for improvement in instruction fidelity. Additionally, we create extra training data and explore supervised fine-tuning to enhance the models' ability to strictly follow instructions without compromising performance on other tasks. We hope this benchmark not only serves as a tool for measuring MLLM adherence to instructions, but also guides future developments in MLLM training methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MIA-Bench, a benchmark designed to evaluate multimodal large language models (MLLMs) on strict adherence to complex instructions. Based on a dataset of 400 image-instruction pairs, MIA-Bench assesses the performance of 29 popular MLLMs, highlighting that current MLLMs struggle with precise instruction adherence. In addition, the paper also explored the supervised fine-tuning (SFT) method based on the LLaVA-NeXT model and achieved positive results, demonstrating the potential effectiveness of this method in improving model instruction adherence.

### Strengths
(1) MIA-Bench fills a gap in existing benchmarks by focusing on the ability of multimodal large language models (MLLMs) to adhere to complex instructions, a crucial yet previously underexplored area of evaluation. This benchmark’s design reveals potential deficiencies in models when following strict, multi-layered instructions, supporting the practical deployment of multimodal models in complex, instruction-based tasks.
(2) The MIA-Bench dataset consists of 400 image-instruction pairs covering various instruction types, such as description, length limit, genre, grammar, and OCR. With data from diverse sources, it reflects the variety found in real-world scenarios. This diverse set of instructions enhances the benchmark’s comprehensiveness and real-world applicability.
(3) The paper provides a systematic evaluation of 29 popular MLLMs, analyzing their performance across different instruction categories. This large-scale comparison offers researchers a detailed performance reference and targeted insights for future model improvements.

### Weaknesses
(1) Although the SFT experiments in the paper demonstrate improved performance in adhering to complex instructions, they may lack in terms of model generalization. The results may be specific to the LLaVA-NeXT model, with no validation of applicability to other models, leaving it unproven whether SFT is equally effective for enhancing complex instruction adherence in MLLMs of different architectures and sizes.
(2) The differences between MIA-Bench and other benchmarks are indeed striking, and the authors believe that this may indicate that MIA-Bench's unique design focuses more on evaluating the model's strict instruction-following ability. However, the authors' explanation does not completely rule out the possibility that MIA-Bench itself may have design biases. This explanation is based on speculative experimental results and has not been verified in depth by sufficient experiments.
(3) Although the authors introduced Claude-3-Opus for comparison to mitigate scoring bias, the two models may exhibit similar biases in evaluation. Therefore, using Claude-3-Opus as the sole comparison tool may be insufficient to fully reveal potential scoring biases in GPT-4o.

### Questions
please refer to the weakness part.

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
4

### Summary
This paper proposes MIA-Bench, which mainly focuses on the instruction-following capability of current Large Multimodal Models (LMMs) under complex and compositional instructions. Unlike previous close-ended benchmarks (e.g., multiple choice for MMBench) and open-ended benchmarks (e.g., LLaVA-Bench), MIA-Bench aims to evaluate precise adherence to complex instructions. As for evaluation, the authors leverage GPT-4o as the judge model. The authors have evaluated many representative LMMs on the proposed MIA-Bench.

### Strengths
1. Evaluating the capability of LMMs to adhere to complex instructions is worth studying.
2. Table 2 demonstrates that MIA-Bench is not highly correlated with existing benchmarks.
3. Figure 8 illustrates that MIA-Bench is vision-centric, which is not strongly correlated with the performance of the LLM backbone.

### Weaknesses
In the context of evaluating open-ended freeform responses like MIA-Bench, it is crucial to account for the inherent variability introduced by the judge model. For example, the performance of MM-Vet has been observed to fluctuate by up to 10 points when assessed with different versions of GPT. 

This variability raises several important considerations:

1. **Standard Deviation Reporting:** When evaluating Large Multimodal Models (LMMs) using the same judge model (e.g., GPT-4o) across multiple trials, it is essential to report the standard deviation of the performance metrics.
2. **Detailed Generation Configuration:** The specific generation parameters of the judge model, such as top-p, top-k, temperature, and num_beams, should be explicitly documented.
3. **Impact of Generation Configuration:** It is necessary to investigate whether the above generation configuration of the judge model has a substantial impact on the performance metrics.
4. **Performance Across Different Judge Models:** Detailed performance metrics should be reported for various judge models. Specifically, the performance of LMMs should be evaluated using different versions of judge models, such as Claude-3-Opus, GPT-4o-20240806, GPT-4o-20240513, GPT-4v-20240409, GPT-4-1106-preview, or even open-sourced models (e.g., Qwen2.5 and LLaMA-3.1). This comprehensive approach will help in identifying any model-specific biases and in providing a more reliable assessment of the LMMs.

### Questions
I do not have any further questions. Please refer to the "weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To evaluate and guide the instruction-following capabilities of multimodal models, MIA-Bench introduces a set of benchmarks for multimodal instruction. MIA-Bench primarily measures the abilities of MLLMs on following layered and compositional multimodal instructions and provides a set of multimodal instructions to enhance model performance in these areas.

### Strengths
1. The paper proposes a benchmark for evaluating the abilities of MLLMs on following compositional instructions, covering a variety of categories and tasks, and providing guidance for MLLMs in following complex composite instructions in the future. 

2. The paper proposes a set of instructions that can effectively enhance the ability of MLLMs to follow layered and compositional instructions.

### Weaknesses
1. Since the images in MIA-Bench are sourced from widely used datasets such as COCO 2017, SBU, TextVQA, and Flickr, I believe you should prioritize evaluating whether the current open-source models exhibit any data leakage issues on these datasets to demonstrate that MIA-Bench does not suffer from data contamination.

2.  I notice that the experiments in Table 3 were conducted on LLaVA-Next-13b. Is this done after fine-tuning on a preference-aligned model? If so, I think this continued SFT setup leading to a performance improvement in MIA-Bench, while other benchmarks exhibit varying degrees of decline, is quite intuitive. Could you please provide additional experiments on the impact of mixing generated instructions with original instructions on model performance? Furthermore, I notice that there are only 5000 generated instructions here; how would the model performance on MIA-Bench be affected if the number of instructions were increased?

### Questions
1. The 400 instructions in MIA Bench are manually annotated. It is important to ensure the reasonableness of the sub-instructions, such as whether the length limitation is appropriate. Additionally, has there been any manual verification of the scoring results from GPT-4o to confirm their accuracy and reasonableness?

2. The instructions in MIA-Bench are composed of multiple sub-instructions. How is the number of sub-instructions per instruction determined? Is there a difficulty grading for the instructions, such that a higher number of sub-instructions indicates a greater level of difficulty?

### Soundness
3

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
5

### Summary
The paper introduces MIA-Bench, a benchmark for evaluating the ability of multimodal large language models (MLLMs) to follow complex instructions. The benchmark consists of 400 image-prompt pairs that test the models' compliance with layered instructions to generate accurate responses. The evaluation of various state-of-the-art MLLMs shows significant performance variations, indicating areas for improvement in instruction adherence. The paper also discusses the creation of additional training data and supervised fine-tuning to enhance the models' instruction-following capabilities without affecting their performance on other tasks.

### Strengths
+ The paper presents a new benchmark that rigorously tests multimodal large language models' ability to follow complex instructions, addressing a previously underexplored area.

+ This paper offers a comprehensive set of 400 diverse image-prompt pairs that challenge models with layered instructions, enhancing the assessment of their linguistic and descriptive capabilities.

+ Experiment demonstrates performance improvements in instruction adherence through supervised fine-tuning.

### Weaknesses
- Complex instruction flowing ability might not be the main interests for MLLM users currently, especially when it comes to writting style constraints such as length and genre. Such abilities are mostly evaluated on LLMs.

- The performance of models on MIA-Bench does not necessarily correlate with their performance on other benchmarks, suggesting that excelling in this specific task may not translate to generalized improvements across different multimodal tasks.

### Questions
- In MIA-Bench, are instructions all related to the corresponding image content or randomly picked from a instruction bank?
- Instruction following abilities highly depends on LLMs used in the MLLM models. It would be better to group the performances in Table 1 and Table 2 according to the LLMs' size.

### Soundness
2

### Presentation
3

### Contribution
2
