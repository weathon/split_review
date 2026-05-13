# Efficient Low-Bit Quantization with Adaptive Scales for Multi-Task Co-Training

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Co-training can achieve parameter-efficient multi-task models but remains unexplored for quantization-aware training. Our investigation shows that directly introducing co-training into existing quantization-aware training (QAT) methods results in significant performance degradation. Our experimental study identifies that the primary issue with existing QAT methods stems from the inadequate activation quantization scales for the co-training framework. To address this issue, we propose Task-Specific Scales Quantization for Multi-Task Co-Training (TSQ-MTC) to tackle mismatched quantization scales. Specifically, a task-specific learnable multi-scale activation quantizer (TLMAQ) is incorporated to enrich the representational ability of shared features for different tasks. Additionally, we find that in the deeper layers of the Transformer model, the quantized network suffers from information distortion within the attention quantizer. A structure-based layer-by-layer distillation (SLLD) is then introduced to ensure that the quantized features effectively preserve the information from their full-precision counterparts. Our extensive experiments in two co-training scenarios demonstrate the effectiveness and versatility of TSQ-MTC. In particular, we successfully achieve a 4-bit quantized low-level visual foundation model based on IPT, which attains a PSNR comparable to the full-precision model while offering a $7.99\times$ compression ratio in the $\times4$ super-resolution task on the Set5 benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The study finds that directly applying co-training to existing QAT methods significantly degrades performance. The main issue identified is the inadequacy of activation quantization scales in the co-training framework. To address this, the authors propose a Task-Specific Scales Quantization method suitable for multi-task co-training.

### Strengths
1. This work effectively incorporates quantization-aware training into co-training and significantly reduces the performance gap between multi-task co-trained models and their 4-bit quantized counterparts.
2. The authors design task-specific learnable multi-scale activation quantizer and SLLD to solve the issues of naive integration.
3. From the experimental results, it appears that the author's techniques are effective.

### Weaknesses
1. In table 1, quantitative results for super-resolution tasks are shown. But I am still curious about the results of deraining and denoising tasks.
2. How about the parameters change of your method?
3. Can you provide the some comparisons with some SOTA single task methods to further demonstrate the superiority of your method?

### Questions
See weakness.

### Soundness
4

### Presentation
4

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
This paper proposes Task-Specific Scales Quantization for Multi-Task Co-Training (TSQ-MTC) to address the performance degradation issue of existing quantization-aware training (QAT) methods when integrated with co-training. The proposed method introduces a task-specific learnable multi-scale activation quantizer (TLMAQ) to enrich the representational ability of shared features across different tasks and a structure-based layer-by-layer distillation (SLLD) to ensure that the quantized features effectively preserve the information from their full-precision counterparts. Extensive experiments on two co-training data scenarios demonstrate the effectiveness of TSQ-MTC, which achieves a 4-bit quantized low-level visual foundation model based on IPT with a PSNR comparable to the full-precision model and a 7.99× compression ratio in the ×4 super-resolution task on the Set5 benchmark.

### Strengths
1. The authors provide a comprehensive evaluation of the challenges of the task, i.e., directly integrating multi-task co-training with QAT. This helps clarify the bottleneck of existing QAT methods and motivates the proposed TSQ-MTC method to address the performance degradation issue.

2. The proposed TSQ-MTC method introduces two novel components, TLMAQ and SLLD, to enhance the representational ability of shared features across different tasks and preserve the information from full-precision features in deeper layers of the Transformer model. 

3. The experimental evaluation across the main text and appendices provides detailed insights into the effectiveness and versatility of the proposed TSQ-MTC method in two co-training data scenarios.

### Weaknesses
1. This paper referred the challenge of computational and memory overhead of co-trained models (Lines 047-049), but the computational complexity and efficiency of the proposed TSQ-MTC method are not discussed in detail. 

2. The authors detailedly analysis the proposed SLLD in Table 4 and Figure B. However, according to the ablation studies provided in Table 3, Table D, Table E, the proposed SLLD has minor improvements in performance given the potential for minor fluctuations in experimental results.

### Questions
As listed in Weaknesses, there are two questions:
1. Could the authors provide the computational cost of training and inference compared to existing QAT methods?
2. Could the authors report the variance of the results of the proposed SLLD method in the ablation studies?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a novel method for multi-task network quantization-aware training, addressing performance degradation caused by model quantization. The approach incorporates two techniques: (1) Task-Specific Learnable Multi-Scale Activation Quantizer (TLMAQ): Addressing the scale conflict in quantizing diverse task features, improving the quantized model's representational capabilities across tasks. (2) Structure-based Layer-by-Layer Distillation (SLLD): Strengthening full-precision model supervision over quantized models, reducing information distortion from quantization.

### Strengths
(1) The proposed method effectively addresses the scale discrepancies among multi-task features, aligning with intuitive expectations.
(2) The novelty is good, the introduction of task-aware quantization into multi-task learning represents an innovative approach.
(3) Method is architecture-agnostic, featuring a wide range of applicability.
(4) originality, quality, clarity, and significance: This paper demonstrates good originality, is well-written, and clearly communicates ideas. Furthermore, the application of quantization to enhance model efficiency holds significant importance for multi-task learning

### Weaknesses
(1) There is a minor error in Section 2.1 - regarding the order of description for the "single-modal task-related data scenario" and the "multi-modal data scenario" are misaligned with the order of "former scenario" and "latter scenario". 
(2) The paper only considered the low-level multi-task scenarios; however, However, it lacks effective exploration of high-level visual tasks. Specifically, Can the proposed method still maintain effectiveness when processing high-level visual multitasking data such as NYUD-v2, Pascal Context and Cityscapes.
(3) The experiment involved a comparison of model quantization techniques, including LSQ (2019) and PAMS (2020). Nevertheless, a comparison with the most recent Quantization-Aware Training (QAT) methods is conspicuously absent.

### Questions
Apart from the points (2) and (3) outlined in the "Weaknesses" section, the following are additional concerns:
(1) While the model design is good and interesting, the model seems a little complex. Would it be possible to provide some comparative analyses regarding the model's speed and complexity?

### Soundness
3

### Presentation
3

### Contribution
3
