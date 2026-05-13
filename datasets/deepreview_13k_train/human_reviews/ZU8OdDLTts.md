# ARB-LLM: Alternating Refined Binarizations for Large Language Models

- Decision: Accept
- Scores: 8, 5, 8

## Abstract
\vspace{-3.5mm}
Large Language Models (LLMs) have greatly pushed forward advancements in natural language processing, yet their high memory and computational demands hinder practical deployment. Binarization, as an effective compression technique, can shrink model weights to just 1 bit, significantly reducing the high demands on computation and memory. However, current binarization methods struggle to narrow the distribution gap between binarized and full-precision weights, while also overlooking the column deviation in LLM weight distribution. To tackle these issues, we propose ARB-LLM, a novel 1-bit post-training quantization (PTQ) technique tailored for LLMs. To narrow the distribution shift between binarized and full-precision weights, we first design an alternating refined binarization (ARB) algorithm to progressively update the binarization parameters, which significantly reduces the quantization error. Moreover, considering the pivot role of calibration data and the column deviation in LLM weights, we further extend ARB to ARB-X and ARB-RC. In addition, we refine the weight partition strategy with column-group bitmap (CGB), which further enhance performance. Equipping ARB-X and ARB-RC with CGB, we obtain ARB-LLM$_\text{X}$ and ARB-LLM$_\text{RC}$ respectively, which significantly outperform state-of-the-art (SOTA) binarization methods for LLMs.
As a binary PTQ method, our ARB-LLM$_\text{RC}$ is the first to surpass FP16 models of the same size.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a novel post-training quantization method alternating Refined Binarization for quantizing LLM using binary weight. The existing methods suffering the mis-alignment from the distribution of the binarized weight with the full precision counterparts. The existing method also didn't address the column-wise deviation. The proposed framework progressively refines binarization parameters to minimize the quantization error. The proposed framework has 4 components. 1. alternating refined binarization which iteractively update the binarized weight. 2. The proposed method is also improved by calibration data. 3. A more accurate binarization can be achieved by column-wise scaling factor. 4. A column-group bitmap strategy was applied in the paper to improve quantization by maximizing bitmap utilization through salient and non-salient division. The experiment results show impressive results.

### Strengths
1. The proposed ARB-LLM method is innovative, which also addresses a critical problem in binary quantization.
2. The experiments on various LLM families demonstrate the superiority of the proposed methods.
3. The paper also provides thorough ablation studies the effectiveness of the individual components of ARB-LLM.

### Weaknesses
1. The main weakness of the paper is the evaluation seems limited to perplexity and average accuracy. The paper would be more interesting if there were trade-offs on more tasks.


### Questions
Does the proposed method perform consistently on 7 zero-shot QA datasets?

Is the binarized model able to get reasonable performance on long context, math and reasoning dataset?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper describes an Alternating Refined Binarization (ARB) framework for performing post-training quantization (PTQ) of 1-bit for large language models (LLM). The framework is based on the observation that there is a distribution gap between the binarized weights and the floating-point weights. Through the iterative refinement process of ARB, the quantization error can be reduced. The authors also provide two variants that use calibration data and address column deviation. They conduct experiments on OPT and LLAMA models, achieving better results compared to other binary PTQ methods such as BiLLM.

### Strengths
The paper identifies and addresses the distribution shift between floating-point weights and binary weights through an iterative refinement method. The study shows that through the ARB process, the quantization error decreases.

The paper further extends the method by adding a calibration dataset and column-wise scales, resulting in better performance compared to BiLLM models.

The paper offers a comprehensive ablation study and time/memory analysis, showing the trade-offs of each component.

### Weaknesses
The authors claim that the weight bit is 1.11 bits, but based on the memory comparison, the model takes approximately 3GB of memory on the Llama-7B model, which is similar in size to GPTQ-3bit of the same model, with inferior performance. Can the authors clarify this?

It seems the approach works better on the older OPT model than the Llama family, with Llama3's performance, in particular, being much worse than floating-point. Can the authors showcase the performance on more recent models like Phi/Llama3.2 to address this concern?

### Questions
1. Can the authors provide any runtime inference metrics to showcase the practical feasibility of the proposed implementation?

2. Could the authors introduce the meaning of each term in equation (6) so that the reader can understand without referring to prior papers?

3. Can the authors clarify the actual memory consumption and compare it to PTQ methods under the same memory budget?

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
Authors propose to ALTERNATING REFINED BINARIZATION (ARB) which is based on BiLLM paper. They introduce correction term δµ to the original mean µ, effectively mitigating the distribution shift. As a result α, B and µ have to be refined.

They further extend ARB to ARB-X and ARB-RC, where 
ARB-X is extension of ARB with calibration data and loss function which is based on papers Optimal Brain Compression and GPTQ.

ARB-RC introduces a column-wise scaling factor αc to better handle parameter variations across columns, while eliminating the redistribution parameter µ to enhance compression in LLM.

In addition they combine ARB-X and ARB-RC with weight partition strategy based on columngroup bitmap (CGB).
And call final versions as ARB-LLMX and ARB-LLMRC respectively, which outperform state-of-the-art (SOTA) binarization methods for LLMs.

ARB-LLMRC outperforms FP16 models of the same size (in GB).

### Strengths
Authors proposed several improvements of BiLLM method and show that ARB-LLMRC outperforms FP16 models of the same size (in GB) and outperforms BiLLM (it is SOTA of LLM post training binarization)

Extensive ablation study of the proposed methods showed effectiveness of Effectiveness of ARB, ARB-LLMX, ARB-LLMRC its combination with CGB and calibration data size, iteration number and group number.

Conducted extensive experiments on the LLaMA, LLaMA-2, and LLaMA3 families. 

They did a thorough analysis of time and memory consumption for proposed methods.

They will release all the code and models.

### Weaknesses
Q: On Figure 1, authors show Pareto curve and demonstrate that  ARB-LLM-RC outperforms the same-size FP16 models and previously published binarized models. So authors show an improvements over previous models binarization, but it does not show the whole picture in terms of pareto curve: they only compare binarized models vs fp16 (on Figure 1). But it will be informative to show also 4bits and 8bits models. For example paper "The case for 4-bit precision: k-bit Inference Scaling Laws" shows that in terms of pareto curve, for the same model size, 4bits has the best accuracy. In addition to 4bits and 8bits it would be great to plot 3bits too on pareto curve (given that 3bits is already presented in multiple Tables in this paper).

Q1: Is it ARB second-order binarization is called in the paper " higher-bit representation, i.e., second-order binarizatio".  Is effectively 2bits quantization? 

Q2: Please explain why BiLLM accuracy in Table 2 does not match the results in the original BiLLM paper (shown in Table 3 LLaMA and LLaMA2)

### Questions
Q1: Is it ARB second-order binarization is called in the paper " higher-bit representation, i.e., second-order binarizatio".  Is effectively 2bits quantization? 

Q2: Please explain why BiLLM accuracy in Table 2 does not match the results in the original BiLLM paper (shown in Table 3 LLaMA and LLaMA2)

### Soundness
3

### Presentation
3

### Contribution
3
