# Zero-shot Mixed Precision Quantization via Joint Optimization of Data Generation and Bit Allocation

- Decision: Reject
- Avg Score: 6.33
- Scores: 6, 5, 8

## Abstract
Mixed-precision quantization (MPQ) aims to identify optimal bit-widths for layers to quantize a model.
On the other hand,
zero-shot quantization (ZSQ) aims to learn a quantized model from a pre-trained full-precision model in a data-free manner, which is commonly done by generating a synthetic calibration set used for quantizing the full-precision model. While it is intuitive that there exists inherent correlation between the quality of the generated calibration dataset
and the bit allocation to the model's layers, 
all existing frameworks treat them as separate problems. This paper proposes a novel method that jointly optimizes both the calibration set and the bit-width of each layer in the context of zero-shot quantization. Specifically, we first propose a novel data optimization approach that takes into consideration the Gram-Gradient matrix constructed from the gradient vectors of calibration samples. We then propose a novel scalable quadratic optimization-based approach to identify the model's bit-widths. These proposals will then be combined into a single framework to jointly optimize both the calibration data and the bit allocation to the model's layers.
Experimental results on the ImageNet dataset demonstrate the proposed method's superiority compared to current state-of-the-art techniques in ZSQ.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel framework for zero-shot mixed-precision quantization (ZMPQ) that combines data generation and bit allocation optimization, focusing on improving quantization outcomes for deep learning models without access to original data. The approach introduces Gram-Gradient matrix-based data optimization and a scalable quadratic optimization for bit-width allocation, outperforming state-of-the-art methods on ImageNet benchmarks.

### Strengths
1.	Proposes a unique, joint optimization approach for data generation and bit allocation, filling a gap in zero-shot mixed-precision quantization research.
2.	Demonstrates superior or comparable performance to existing state-of-the-art methods under low-bit settings and varied model budgets, with results verified on multiple architectures (ResNet-18, ResNet-50, MobileNetV2).
3.	As a complex system, the paper offers a well-rounded suite of ablation studies that demonstrate the robustness of the method

### Weaknesses
I am not familiar with the work related to Mixed-precision quantization task. This paper is intuitive and reasonable on the whole. However there are some problems of clarity in the writing
1. Certain proofs, such as the explanation of Equation (6) and the construction and application of the Gram-Gradient matrix, are highly technical, demanding considerable background knowledge from the reader. The explanation provided for Equation (6), in particular, feels insufficient for those not deeply versed in the topic. Specifically, the connection between the Gram matrix and the optimization of the generated data is not clearly established, leaving the reader to infer the underlying mathematical justification. The paper needs to elaborate on how the Gram matrix facilitates the generation of data that is effective for quantization, and why this approach is superior to other data generation techniques.
2. The paper would benefit from additional figures or qualitative results to aid in understanding complex concepts such as gradient matching, which currently lack sufficient illustration. The notion of gradient matching is central to the method, yet the paper does not provide any visual or intuitive explanation of how the gradients of the generated data align with the gradients of the original data. This makes it difficult to grasp the effectiveness of the proposed data generation process. A visualization of the gradient distributions or a comparison of gradient directions would be beneficial.
3. Table 1 and 2, could provide more detail on the W/A notation (e.g., clarifying 2/2 and */2) to enhance interpretability. The current notation is ambiguous, especially the use of the asterisk. It is not immediately clear what the asterisk represents in the context of mixed-precision quantization, and more explanation is needed to ensure that the reader can fully understand the experimental setup and results.

### Questions
Some of the suggestions for clarity mentioned above.

### Soundness
4

### Presentation
3

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
This paper for the first time proposes a mechanism that combines zero-shot quantization and mixed-precision quantization.On the basis, the paper proposes a joint optimization framework between bit-width allocation and synthetic data generation. However, during the entire optimization process, these two parts are carried out alternately and iteratively. There is still a lack of a deeply coupled mechanism for joint optimization.

### Strengths
The inherent correlation between the quality of the generated calibration dataset and the bit allocation to the model's layers are considered. The paper is well-organized and clearly stated. I would suggest accepting it after the following concerns are addressed.

### Weaknesses
1. The references are all published until 2023. It would be best to provide some references on Mixed-precision Quantization/Zero-shot Quantization in 2024.
2. In Section 3.1, the authors mentioned that “In the realm of zero-shot quantization, the
validation set does not exist, so we only assume it here for explanation”. But the evaluation of model performance is conducted on the ImageNet dataset. Please carefully explain the relation between these two sets. If the validation does not exist, will there be significant changes or simplifications in formulas 6 and 8?
3. Please further explain the derivation process from formula 5 to formula 6.
4. In table 1 & table 2, the bit widths of results obtained using methods from this paper are marked as (*). From quantization setting in section 4.1, weights of some layers are set to 8 bits for initialization. Please calculate the average bit width of these models and fill it in the table, which will be more conducive to comparing the results and demonstrating the superiority of the method.
5. It would be better if the paper could compare the data synthesized in this paper with the data synthesized by existing methods and give deeper explanations or analyses.

### Questions
1. The references are all published until 2023. It would be best to provide some references on Mixed-precision Quantization/Zero-shot Quantization in 2024.
2. In Section 3.1, the authors mentioned that “In the realm of zero-shot quantization, the
validation set does not exist, so we only assume it here for explanation”. But the evaluation of model performance is conducted on the ImageNet dataset. Please carefully explain the relation between these two sets. If the validation does not exist, will there be significant changes or simplifications in formulas 6 and 8?
3. Please further explain the derivation process from formula 5 to formula 6.
4. In table 1 & table 2, the bit widths of results obtained using methods from this paper are marked as (*). From quantization setting in section 4.1, weights of some layers are set to 8 bits for initialization. Please calculate the average bit width of these models and fill it in the table, which will be more conducive to comparing the results and demonstrating the superiority of the method.
5. It would be better if the paper could compare the data synthesized in this paper with the data synthesized by existing methods and give deeper explanations or analyses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
They introduce a jointly optimization framework for zero-shot quantization that alternatively optimize the calibration data and model bit-widths

### Strengths
The authors propose a mixed precision quantization method for ZSQ from the perspective of data quality. I support this work on the good topic.

### Weaknesses
My main concern is that network optimization from a gradient perspective may be passive given the poor quality of the available data, and the intuition is that bypassing the gradient information and using a gradient-free search method may be a better option.

My main concern is that the quantizer configurations of the comparison methods are not well ablated. In Table 1, AdaSG only quantized the weight, and used the naive quantization method of minmax and the naive STE fine-tuning method. However, Genie + MPQ (Ours) uses weight & activation quantization, and AdaRound is used for weight quantization. I expect the authors to carefully list the quantizer baselines of the methods for fair comparison.

I cannot observe the superiority of the proposed generated images from Table I because the quantizer configurations of the comparison methods are not well ablated.

The traditional benchmark on CIFAR data set has not been adopted, and the authors are requested to add explanations.

line235: "When that happens, we call the set X^(T) is k-equivalent to X^(V) . We can optimize this objective, by matching the Gram-Gradient matrix of the two sets, according to Definition 1 and Theorem 3.1" ZSQ does not provide a validation set. I am trying to doubt the assumption in the article that when two samples are from synthetic datasets, their matching does not indicate the correctness of the feature?

The generator configuration is not well aligned with the comparison method because Genie's generator is a newer version and this part needs further ablation.

Lack of overhead analysis.

The 4-bit case is difficult to judge because the task is relatively simple. The existing 3-bit quantization benchmarks still achieve poor accuracy, especially the AdaDFQ benchmarks (GDFQ series). Whether the authors are possible to show the experimental situation of 3bit？

### Questions
1. The quantizer setup. The GDFQ/Qimera/AdaDFQ series compared in this paper all use perchannel quantizer and naive optimization by STE. However, these details are not elaborated for the proposed method.
2. The proposed method also works for conventional PTQ when the calibration data set is assumed not to fit the model statistics, which indicates that the method is not completely limited to ZSQ. Authors should provide more targeted explanations or provide experiments of the proposed method on PTQ for corroboration. Perhaps the proposed method can be used to build benchmarks on PTQ?
3. The traditional benchmark on CIFAR data set has not been adopted, and the authors are requested to add explanations.
4. line235: "When that happens, we call the set X^(T) is k-equivalent to X^(V) . We can optimize this objective, by matching the Gram-Gradient matrix of the two sets, according to Definition 1 and Theorem 3.1" ZSQ does not provide a validation set. I am trying to doubt the assumption in the article that when two samples are from synthetic datasets, their matching does not indicate the correctness of the feature?
5. The generator configuration is not well aligned with the comparison method because Genie's generator is a newer version and this part needs further ablation.
6. Lack of overhead analysis.

### Soundness
3

### Presentation
3

### Contribution
2
