# LLM-QAT: Data-Free Quantization Aware Training for Large Language Models

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Several post-training quantization methods have been applied to large language models (LLMs), and have been shown to perform well down to 8-bits.  We find that these methods break down at lower bit precision, and investigate quantization aware training for LLMs (LLM-QAT) to push quantization levels even further.  We propose a data-free distillation method that leverages generations produced by the pre-trained model, which better preserves the original output distribution and allows quantizing any generative model independent of its training data, similar to post-training quantization methods.  In addition to quantizing weights and activations, we also quantize the KV cache, which is critical for increasing throughput and support long sequence dependencies at current model sizes.  We experiment with LLaMA models of sizes 7B, 13B, and 30B, at quantization levels down to 4-bits.  We observe large improvements over training-free methods, especially in the low-bit settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study QAT approach for LLMs. The unique challenge of applying QAT on LLMs is the data composition. At the pre-training stage, various different kinds of data sources are mixed and it is difficult to all kinds of data on the fine-tuning stage. To avoid this issue, the authors propose data-free self-distillation which consists of two steps - 1) auto-regressive generation of random sequences from the non-quantized model and 2) knowledge distillation using the generated sequences as inputs to teacher and student models. In the knowledge distillation process, the authors find that soft logit based cross entropy loss works the best. Using the proposed method, the authors quantize LLaMA 7B, 13B and 30B models for various quantization bits (4 and 8 bits for weights, 6, 8 and 16 for activations, 4, 8, 16 for KV cache). The proposed LLM-QAT maintain the quality well for 8 bit weights and activations, while showing some quality degradations for 4 bits. The authors add some ablation studies including comparison between different data source and generated sequences, different quantization methods, and distillation targets.

### Strengths
- Overall, the paper is well motivated and well organized. 
- The proposed knowledge distillation method is well described and easy to follow.
- Data-free knowledge distillation is a novel approach.

### Weaknesses
 - Even though the quantized models still maintain the quality closely, there exist non-trivial gaps especially when the weights are quantized to 4-bits. Especially, with additional training (QAT), it is expected the quality is very close to the floating point unquantized model. Also, some PTQ methods such as (Li, Qingyuan, et al. "FPTQ: Fine-grained Post-Training Quantization for Large Language Models." arXiv preprint arXiv:2308.15987 (2023).) claims better quality.

 - In page 4, the activations are weights are -> activations and weights are?
- In page 5, whether the quantize models -> quantized models.
- Why 3-5 tokens? What exact number is used?

### Questions
- In page 4, the activations are weights are -> activations and weights are?
- In page 5, whether the quantize models -> quantized models.
- Why 3-5 tokens? What exact number is used?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a data free distillation approach for quantization aware training (QAT) for LLMs to address limitations related to obtaining large-scale training data and complex pre-training procedures. The paper proposes utilizing tokens generated from the generative model as the fine-tuning dataset and demonstrates that this setup works better in practice than using subsets of the original data used for training as it provides a better representation of the original data distribution. Using the data free distillation technique and existing quantization methods, the authors demonstrate better results, particularly for lower precisions, on LLaMA models of sizes 7B, 13B, and 30B than PTQ techniques from literature while quantizing weights, activations and the KV cache to lower precisions (as low as 4-bits).

### Strengths
The paper motivates the problem well, and quantizing large language models to lower precisions for faster inference is a very relevant research problem today.

The paper is generally well written, and includes experiments comparing various quantization techniques and also includes ablation studies on dataset choices. 

This is the first application of QAT to large language models, although previous works (for example [1] have demonstrated QAT results for BERT). 




[1] https://openreview.net/pdf?id=EZQnauHn-77

### Weaknesses
The techniques utilized in the paper (QAT using StatsQ and LSQ, MinMax quantization, knowledge distillation) have been shown to work in the quantization setting before, so the contributions are not particularly novel. Effectiveness of MinMax for language models due to outliers has also been demonstrated earlier.

While the results are generally better than PTQ techniques, specially as precision is lowered (this is usually the case for low precision scenarios - QAT performs better than PTQ), the gaps are still quite large compared to full precision to be practically useful, specially for the 4-bit case, and I am not entirely convinced from the limited ablation studies that fine-tuning on a subset of the original data would not yield comparable results. While practically useful, the algorithmic contribution in this work is weak.

### Questions
For the dataset ablation study, have the authors considered using a subset of each dataset and comparing that to generated data, instead of exclusively fine-tuning using a single dataset? 

Perhaps using a combination of real and generated data might close the accuracy gap further?

Have the authors considered using a larger teacher model for the distillation data generation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
LLM-QAT paves the way for quantization-aware training (QAT) of large language models (LLMs) using cross-entropy-based logit distillation. For both weights and activations, LLM-QAT adopts the symmetric MinMax quantization format. This decision was based on an empirical analysis that took into account the outliers in LLMs. Specifically, they adopted per-token activation quantization and per-channel weight quantization. Furthermore, because the key-value cache consumes a non-negligible amount of memory, LLM-QAT quantizes the key-value cache to 8-bit or even 4-bit to increase throughput. While LLMs are sensitive to the training dataset, LLM-QAT explores training datasets for QAT that generalize well to other tasks. The empirical results of their experiments justify LLM-QAT's formulation of the quantization function and data selection. Evaluation results show that LLM-QAT offers competitive performance compared to training-free methods such as round-to-nearest (RTN) and SmoothQuant.

### Strengths
* Investigate a quantization format to mitigate perplexity loss, drawing from their observations about the presence of outliers in quantization-aware training (QAT).
* Provide new empirical insights on the selection of the knowledge distillation dataset and its associated loss.
* Offer comprehensive experimental results spanning various bit-widths for weight, activation, and key-value cache.
* Exhibit overall strong quality and clarity in the presentation.

### Weaknesses
 * Compare LLM-QAT only to training-free methods such as round-to-nearest (RTN) and SmoothQuant [4]. 
    * Although AdaRound [1], AdaQuant [2], and FlexRound [3] are post-training quantization (PTQ) methods, they still utilize a training set (small calibration set) in a layer-wise or block-wise manner. Given that these PTQ methods adopt a similar knowledge distillation scheme (even though the loss term is very different), it would be beneficial to report results comparing LLM-QAT with these methods (at least one of them), which can be viewed as non-training-free quantization methods.
* The arguments would be more convincing with additional references and explanations for why LLM-QAT primarily focuses on the W4A8 quantization format. For instance, regarding the W8A8 integer quantization, SmoothQuant [4] showcases actual latency acceleration results.  It is not clear why the authors chose to focus on W4A8, especially given that W8A8 has demonstrated practical speedups and is a more common target for hardware acceleration. The paper would benefit from a more detailed discussion on the trade-offs between different bit-widths and the specific hardware considerations that motivated the choice of W4A8.


### Questions
* Are there experimental results available for other models?
* Do models other than LLaMA exhibit similar trends in quantization format settings?
* In Section 4, "Related Works", I kindly suggest modifying the last sentence: "A single random initial token allows LLMs to autonomously generate data suitable for QAT fine-tuning. To the best of our knowledge, this has not been studied in existing literature." LLM-QAT employs a knowledge distillation (KD) scheme for quantization-aware training (QAT), and a previous method named ZeroQuant [1] also uses the KD scheme. Even though these methods primarily focus on post-training quantization, they also utilize a training dataset for quantization. Specifically, ZeroQuant presents data-free quantization that employs random data for generative language models.
* There are typos in the manuscript, notably in sections 2.2.2 and 3.3. I suggest revising them.

[1] Yao, Zhewei, et al. "Zeroquant: Efficient and affordable post-training quantization for large-scale transformers." Advances in Neural Information Processing Systems 35 (2022): 27168-27183.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates the data-free quantization-aware training on large language models. Without the available training data, it proposes to make the LLMs generate data by themselves and study several sampling strategies. Experiments are done on a wide variety of datasets including common sense reasoning, perplexity evaluation, and MMLU. It also conducts experiments across several bit-widths on the LLaMA model.

### Strengths
* Using LLMs to generate data is very natural. The paper makes a combination of it and data-free quantization, which can be a challenge for QAT.

* The paper considers several datasets to evaluate, especially include the MMLU and TriviaQA datasets in the appendix.

* The writing of the paper is clear and easy to follow.

### Weaknesses
 * As using LLMs to generate data is not a very new thing [1][2], can the paper give more detailed analyses about the synthetic method or the synthetic results like sentence coherence and data diversity? I think this can increase the soundness of the proposed method. Specifically, the paper should provide quantitative metrics on the diversity of the generated data, perhaps using metrics like type-token ratio or n-gram overlap with existing datasets. Furthermore, an analysis of the semantic coherence of generated sentences compared to human-written text would strengthen the claim that the synthetic data is of sufficient quality for quantization-aware training.

  [1]. Generating Faithful Synthetic Data with Large Language Models: A Case Study in Computational Social Science

  [2]. CLASP: Few-Shot Cross-Lingual Data Augmentation for Semantic Parsing


* Experiments parts are not very solid:
  * The 4-6-16 setting of experiments is a little bit strange and unfriendly to hardware. I think the paper should move 4-4-4 experiments that take 4-bit weight and activations from the appendix to the main body. The 4-4-4 setting is more aligned with common quantization practices and would allow for a more direct comparison with other methods optimized for 4-bit quantization. This would also better demonstrate the practical applicability of the proposed method in resource-constrained environments.
  * I find the fifth row in Table 1 looks strange It seems that the performance of GPTQ is really slow, even slower than RTN with 4-8-16 bits. This result is counter-intuitive, as GPTQ is generally expected to outperform RTN, especially at lower bit-widths. It is necessary to re-examine the experimental setup for GPTQ, particularly the calibration data used. Using a calibration dataset that more closely matches the evaluation dataset might yield more representative results.
  * Experiments can be more convincing if the paper also conducts on other structures like LLaMA-2, and others take the vanilla Transformer structure as LLaMA adopts a different one. Conducting experiments on a wider range of model architectures, including those with standard Transformer structures, would help to establish the generalizability of the proposed method. This is crucial for demonstrating that the approach is not overly tailored to the specific architecture of LLaMA.
  * Experiments can be better if the paper could compare with some recent papers [3] and [4]. These papers represent the state-of-the-art in quantization for large language models, and a direct comparison would provide a clearer picture of the proposed method's performance relative to the current best practices. 

  [3]. Outlier Suppression+: Accurate quantization of large language models by equivalent and effective shifting and scaling 

  [4]. OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models

### Questions
Based on my practical experience and discussion with some people in this field, we find quantizing KV cache with per-token quantization on LLaMA models will not incur much accuracy decline, even on a 4-bit case. However, results in the main table seem to give an opposite conclusion. Also, the paper claims that distribution for LLaMA models is usually symmetric. However, we find products of the output of gate and up functions in LLaMA are not so.

I do not put the above points in the weakness part temporarily because I think this requires more discussion with the authors. Others questions please check the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
