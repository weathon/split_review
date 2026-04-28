# Progressive Mixed-Precision Decoding for Efficient LLM Inference

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In spite of the great potential of large language models (LLMs) across various tasks, their deployment on resource-constrained devices remains challenging due to their excessive computational and memory demands. Quantization has emerged as an effective solution by storing weights in reduced precision. However, utilizing low precisions (\textit{i.e.}~2/3-bit) to substantially alleviate the memory-boundedness of LLM decoding, still suffers from prohibitive performance drop. In this work, 
we argue that existing approaches fail to explore the diversity in computational patterns, redundancy, and sensitivity to approximations of the different phases of LLM inference, resorting to a uniform quantization policy throughout.
Instead, we propose a novel phase-aware method that selectively allocates precision during different phases of LLM inference, achieving both strong context extraction during prefill and efficient memory bandwidth utilization during decoding. To further address the memory-boundedness of the decoding phase, we introduce \textbf{P}rogressive \textbf{M}ixed-\textbf{P}recision \textbf{D}ecoding (PMPD), a technique that enables the gradual lowering of precision deeper in the generated sequence, together with a spectrum of precision-switching schedulers that dynamically drive the precision-lowering decisions in either task-adaptive or prompt-adaptive manner. 
Extensive evaluation across diverse language tasks shows that when targeting Nvidia GPUs, PMPD achieves 1.4$-$12.2$\times$ speedup 
in LLM linear layers
over fp16 models, while when targeting an LLM-optimized NPU, our approach delivers a throughput gain of 3.8$-$8.0$\times$ over fp16 models and up to 1.54$\times$ over uniform quantization approaches while preserving the output quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors point out that different stages of LLM inference require different quantization bit-widths. In oracle experiments, they discovered that increasing the model weight bit-width during the prefill phase can enhance model performance. They also find that using a higher bit-width in the early stages of decoding helps maintain model performance. Based on these findings, the authors search for different quantization bit-widths for the prefill and decode stages. Additionally, they use an optimized scheduler to gradually reduce the model bit-width during decode stage. Using these two schemes, the quantized model can ensure output quality on the challenging MT-Bench task. Meanwhile, the quantized model achieves a throughput improvement of 3.8-8.0× on NPU and a linear layer acceleration of 1.4-12.2× on GPU.

### Strengths
1. Compared to previous methods of mixed-precision quantization within models, this paper innovatively considers introducing mixed-precision quantization at different stages of LLM inference.

2. This paper not only validates the algorithmic performance of the proposed method but also measures the hardware performance like speedup ratio and throughput on both GPUs and NPUs.

### Weaknesses
1. In Section 3.1 of this paper, the experiment results are insufficient to demonstrate the validity of Motivation One.

    - First, the authors only increase the bit-width during the prefill stage and found that model performance was better than that when using uniform bit-width, but do not increase the bit-width during the decode stage to evaluate model performance. Therefore, the results do not demonstrate that the prefill and decode stages have different error resilience. 

    - Secondly, this section only presents the model's outputs for three specific inputs, lacking quantitative results.

    - It is recommended that the authors supplement the results of high-precision decoding with low-precision prefill and provide performance of the model on MT-Bench to support Motivation One.

2. In Section 4.1 of this paper, the authors search for the optimal bit-widths for the prefill and decode stages assuming that the decode stage is conducted with a uniform bit-width. However, during actual inference, the model bit-width in the decode stage gradually decreases. Therefore, it cannot be guaranteed that the previously found results remain optimal. Then what is the significance of this search step? Is it possible to directly use the bit-width of the prefill stage as the starting point for the bit-width decrease in the decode stage?

3. In Section 4.3 of this paper, the authors design the Task-Agnostic Learned Scheduler to predict the steps at which the bit-width should decrease during the decode stage. Theoretically, the optimal precision switch points may depend on both the model's inputs and the outputs. However, this scheduler only uses the token features generated during the prefill stage as input. Is it reasonable to overlook the information from the model's generated content?

4. The experimental results in this paper are not comprehensive enough. First, the maximum parameter size of the model used in the experiments is 7B, and larger models are not evaluated. Secondly, the paper only provides GPU speedup ratios for the linear layers and does not present end-to-end speedup data.

5. This paper has misunderstandings regarding some concepts. For example, the maximum context length of LLMs (CL) refers to the sum of the model's maximum input and output lengths, but in Section 4.3, the paper incorrectly asserts that CL is the model's maximum output length.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work tackles the difficulty of deploying large language models (LLMs) on resource-constrained devices by introducing a “phase-aware” quantization method that adapts precision to different inference stages, unlike traditional uniform quantization approaches. The authors develop Progressive Mixed-Precision Decoding (PMPD), a technique that lowers precision progressively as the generated sequence deepens, using schedulers to adapt precision based on tasks or prompts. Experimental results demonstrate that PMPD provides substantial speedups on Nvidia GPUs and optimized NPUs, while preserving output quality and surpassing the performance of both fp16 and uniform quantization models.

### Strengths
- The author discusses many design choices, with their pros and cons.
- The discussion on the tolerance of quantization in different depths of the decoding stage is informative

### Weaknesses
 - The paper does not discuss much about how they do the precision switching in their implementation, which could be a potential risk of memory usage (loading the same model with different precision) or additional latency (loading the model weight on the fly).
- The accuracy results are all based on MHA models, lacking discussion on other types of models like GQA models.

### Questions
1. How do you implement the precision switch operation during the decoding stage? And what is the actual cost of such switching?

2. How's the result on Llama3? Or other GQA models?

3. How's your method compared with static quantization methods like GPTQ and AWQ both for accuracy and efficiency?

### Soundness
2

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
3

### Summary
Authors propose a novel phase-aware method that selectively allocates precision during different phases of LLM inference: use higher precision during prefill stage and then reduce precision for efficient memory bandwidth utilization during decoding.
They introduce Progressive Mixed-Precision Decoding (PMPD) which controls gradual lowering of weights precision in the generated sequence with task-adaptive or prompt-adaptive manner. It is weights only post training quantization(PTQ) which adaptively controls weights precision depending on decode stage (prefill, decode) and decoded token. They use  Any-Precision LLM (Park et al., 2024), as PTQ which keeps multiple weight precisions with no memory footprint overhead.

Authors show that PMPD achieves 1.4−12.2x speedup in LLM linear layers over fp16 models (on Nvidia GPUs).
Also throughput gain of 3.8−8.0x over fp16 models and up to 1.54× over uniform quantization (on NPU) approaches while preserving the output quality.

### Strengths
PMPD vs. Baselines: Both schedulers deliver lossless performance on the CNN/DM and Dialogsum datasets with up to 33% reduction in bitwidth, highlighting their ability to effectively capture context and generate high-quality outputs.

Novelty in applying different precision for model weights depending on input token during decode mode.

Conducted thorough experiments on LLM edge-deployable models.

Produced End-to-end NPU throughput and Speedup comparison vs fp16 model. Shows that PMPD achieves a significant speedup of 3.8-8.0× over fp16 across various models and datasets.

Good ablation studies showing that  indicating that PMPD-Learned is effectively learning patterns in the KV cache

### Weaknesses
Q: in Table 1, PMPD-Static has better accuracy score in 11 cases; PMPD-Learned has better accuracy score in 3 cases; PMPD-Static uses less bits 5 cases; PMPD-Learned uses less bits 4 cases. It looks like PMPD-Learned under-performing on both accuracy and bits usage in comparison to PMPD-Static. Please analyze why PMPD-Learned underperforms compared to PMPD-Static. I see that PMPD-Learned is preferable in case when validation data are missing, because PMPD-Static can not be trained on data which are missing validation data sets.

Q: Authors report 1.4−12.2x speedup in LLM linear layers over fp16 models for PMPD methods. Please also add speed up in comparison to 3bit and 4bit baseline models (you show it in Figure 5 and Table 3, but do not report in the abstract of the paper).

Q: One of the goal of this paper is to show that proposed quantization approach has no accuracy drop in comparison to the float baseline model. Float baseline is missing in Table 1, so it is hard to make a conclusion that proposed methods do not drop accuracy in comparison to float baseline. Please include the float baseline results in Table 1 or explain why you chose not to include them (for example in Figure 5 you show fp16 latency of evaluated models). Same comment for Table 2.

Q: It would be great to add in Table 1, other state of the art post training quantization methods, e.g. :
* Fast and Efficient 2-bit LLM Inference on GPU: 2/4/16-bit in a Weight Matrix with Asynchronous Dequantization
* QuIP: 2-Bit Quantization of Large Language Models With Guarantees or (QuIP#: Even Better LLM Quantization with
Hadamard Incoherence and Lattice Codebooks)
* GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers

Please explain why above methods were not included as baselines, and how your method compares conceptually to these approaches if direct comparison is not feasible.

### Questions
Q : What quantization method is used for Baseline-l and Baseline-h?

Q: Why GPTQ are not presented as baselines in Table 1?

Q: How would you explain that PMPD-Static has better performance in comparison to PMPD-Learned on Table 1?

Q: Please explain what precision range was used for training PMPD shown on Table 1, e.g. (2bits, 3bits, 4bits) for all experiments or you use (2bits 3bits) for one one set of experiments and (3bits, 4bits) for another set of experiments?

Q: For PMPD method you will need to keep pre-computed e.g. 2bits 3bits weights and then switch between different precision depending on input token, please explain how do you avoid overhead of keeping weights with different set of precision in memory in comparison to a baseline method which keeps weights with one set of precision e.g. 3bits only?

Q: On Table 1, experiment on data Dialogsum, how do you explain that Baseline-l with 2bits has accuracy 10.2 / 75.5 but PMPD-Static with the same amount of bits = 2.0bits has better accuracy 25.0 / 88.2? Please explain what set of bits PMPD-Static uses, e.g. if it was trained with (2bits 3bits) then it means that PMPD-Static used only 2bits during inference, so that final number of bits is 2.0 (reported in Table 1).

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
4

### Summary
The paper proposes phase-aware precision/quantization recipe which allocates higher bit depth for the prefill phase and lower/adaptive bit depth for the decoding phase in LLMs. They motivation is based off of previous work & representative examples shown in the paper that the prefill phase (language understanding phase) is likely to benefit from lower quantization errors than the decoding phase.
Additionally, authors propose a well executed "adaptive" precision strategy in the decoding phase, where the precision is reduced after every few steps of the generation. 
The experiments on three small-scale mobile LLMs are show the effectiveness of the approach in terms of quality and latency/throughput of the kernels as compared to the other methods which use fixed bit-depth through out the generation.

### Strengths
It is very critical to address the memory-boundedness of small LLMs operating on mobile phones. Quantization is the most prevalent method for model compression but suffers from quality-latency tradeoff. The paper proposes "adaptive" precision in the decoding stage, by training a "precision scheduler", which is very interesting. It exploits the fact that later half of the tokens in the generation process can afford higher quantization error in the weights. Evaluation shows that the proposed methods achieves better (or at-least maintains) better quality than high bit-depth quantization methods, while increasing the throughput which is critical for mobile performance of small LLMs. The motivation is clear and backed with relevant prior work.

### Weaknesses
1) There is a lot of repetition of concepts in the first few pages of the paper. The same idea is explained several times in the first three sections. It maybe better to show more representative examples similar to Figure 2 -- perhaps some high level stats/evals on how different tasks/models perform when changing the precision in the decode/prefill phase.
2) The work misses several critical LLM benchmarks around Math, reasoning and especially long context. It would be interesting to see the effect of the proposed approach on a wider range of LLM evals. 
3) This experimentation section fails to provide more statistics on evaluation, for example, what is the average decode length for the three tasks for the thee models, what is the impact of changing N (the number of "switches" in precision during decoding phase). It is not entirely clear what precision the scheduler choses and for how long at each decoding step, -- for three different tasks and the three models.

### Questions
1) IMO the most interesting section of the paper is the scheduler design in Section 4.3. As such a lot of core ideas/implementation details of the scheduler are relegated to the Appendix. It maybe better to add scheduler model/training design to the main paper, while reducing redundant text in the introduction, methodology and the motivation section. 
2) When adding the constraint in line 325-327, it's not entirely clear how is N chosen, is this a hyper-parameter, what is recommended value? Does it depend on task/model that were studied? A detail ablation can be performed in the experiment section, but a brief summary for practioners can be provided here.
3) Table 1 caption says the phi-1.5 models are 2/4 bit, but the table itself shows they are 2/3 bit?

### Soundness
3

### Presentation
4

### Contribution
3
