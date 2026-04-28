# TransNormerLLM: A Faster and Better Large Language Model with Improved TransNormer

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
We present TransNormerLLM, the first linear attention-based Large Language Model (LLM) that outperforms conventional softmax attention-based models in terms of both accuracy and efficiency. TransNormerLLM evolves from the previous linear attention architecture TransNormer~\citep{qin-etal-2022-devil} by making advanced modifications that include positional embedding, linear attention acceleration, gating mechanism, tensor normalization, and inference acceleration and stabilization. 
Specifically, we use LRPE~\citep{qin2023linearized} together with an exponential decay to avoid attention dilution issues while allowing the model to retain global interactions between tokens.
Additionally, we propose Lightning Attention, a cutting-edge technique that accelerates linear attention by more than twice in runtime and reduces memory usage by a remarkable four times.
To further enhance the performance of TransNormer, we leverage a gating mechanism to smooth training and a new tensor normalization scheme to accelerate the model, resulting in an impressive acceleration of over $20\%$. 
Furthermore, we develop a robust inference algorithm that ensures numerical stability and consistent inference speed, regardless of the sequence length, showcasing superior efficiency during both training and inference stages.
We also implement an efficient model parallel schema for TransNormerLLM, enabling seamless deployment on large-scale clusters and facilitating expansion to even more extensive models, \ie LLMs with 175B parameters. We validate our model design through a series of ablations and train models with sizes of 385M, 1B, and 7B on our self-collected corpus. Benchmark results demonstrate that our models not only match the performance of state-of-the-art LLMs with Transformer but are also significantly faster.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes the TransNormerLLM model that builds on recent advancements in linear attention model techniques such as TransNormer with gating as model architecture, LRPE with exponential decay for position encoding. This work also speeds up causal Linear attention computation to make it io-aware.  Furthermore, model parallelism is introduced for the SGLU and GLA blocks for efficient large-scale distribute training. The architectural and efficient training techniques lead to faster training while matching the performance of the Transformer architecture. Finally, a robust inference for exponential decay attention is presented for numerical stability.

### Strengths
- The paper is well-written clearly explaining the contributions and motivations.
- The experiments are well-conducted, with thoughtful ablations and comparisons to extensive range of baselines. This is an important advancement showing that linear attention can match the Transformer performance at scale. Overall I think this work will help to significantly reduce the computation and better scale LLMs. 
- Detailed information regarding the corpus, pseudo-codes, model hyper-parameters is provided,  aiding reproducibility.

### Weaknesses
- One suggestion would be to explicitly state what is meant by exponential decay position encoding in section 3.1.1.  My understanding is in this case $a_{st} = q_s^T k_t \lambda^{(s-t)}$. Please correct me if I am wrong.
- While the training efficiency is provided for TransNormerLLM models larger than 7B is provided, the performance on benchmarks is not included. It would be beneficial to include those results if possible.

### Questions
- Although the pre-training performance is on par with that of Transformer models, have any experiments on fine-tuning the models been conducted?
- In Algorithm 3, why is an explicit mask $M \in R^{N \times N}$ necessary? Is it for general attention?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes TransNormerLLM, an improved linear attention-based large language model (LLM) that outperforms conventional softmax attention models in both accuracy and efficiency. 

- The key contributions include:

1. Replacing the TransNormer's DiagAttention with Linear Attention and using LRPE (Learnable Relative Positional Encoding) with exponential decay to allow global token interactions while avoiding attention dilution. 

2. Introducing Lightning Attention to accelerate linear attention by 2x during training and reduce memory usage by 4x.

3. Using a gating mechanism for training stability and simplified GLU/normalization for faster processing. 

4. Developing a robust inference algorithm for consistent speed regardless of sequence length.

5. Implementing efficient model parallelism to scale the model up to 175B parameters. 

6. Validating the model on a 6TB corpus and benchmarking 385M, 1B and 7B parameter models, showing competitive performance to Transformer LLMs while being faster.

### Strengths
- The work addresses a key limitation of standard Transformer models - the quadratic complexity w.r.t sequence length - through the use of linear attention. This could enable scaling to much longer contexts.

- The modifications to the original TransNormer architecture, especially Lightning Attention and robust inference, significantly improve efficiency and stability.

- Thorough ablation studies validate the impact of each proposed technique. The benchmarking shows the models match state-of-the-art Transformer LLMs in accuracy while being faster.

- The model parallelism enables scaling up to 175B parameters, allowing large-scale pre-training. The efficiency gains are impressive and impactful.

- The code and models will be open-sourced, promoting further research and application of efficient transformers.

### Weaknesses
- The novelty of the work is fairly incremental, building directly on prior work like TransNormer and Flash Attention. None of the modifications substantially advance the state-of-the-art.

- While the techniques improve efficiency, the gains in accuracy over standard TransNormer appear marginal based on the results. The ablations also suggest the contributions are optimizations rather than modelling improvements.

- Lightning Attention, while providing speed and memory gains, is not particularly novel, simply applying similar ideas from Flash Attention.

- The robust inference modification is motivated through mathematical derivations, but the practical benefits are unclear. There is no evidence it improves stability or accuracy.

- The pre-training data is underspecified, making fair comparison to other models difficult.

### Questions
- What is the actual impact of the robust inference modification in practice? Any quantitative results?

- Can the authors provide more details on the pre-training data characteristics and compute resources used? Is there any testing data leakage problem?

- The gains over standard Transformers appear quite large but the gains over TransNormer are marginal. Why is this the case? Can you show the training curves for the models?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes several incremental changes upon TransNormer including: positional embedding, gated linear units and layernorm. The authors claim that the resulting model is not only more effective, but also more efficient during both training and inference, compared with the original TransNormer.

### Strengths
- Extensive empirical results with detailed ablation on the proposed changes
- Detailed evaluation of both training and inference

### Weaknesses
- changes are incremental, thus the work lack technical contribution
- the training and inference algorithms are not novel (explained more blow)
- the results are not convincing due to baseline setup and implementations

Training efficiency: From the appendix, it seems the implementation of the linear attention is a direct adaptation of Flash-Attention2 (I further assume it’s based on the Triton implementation of Flash-Attention2). It’s unfair (and not meaningful) to compare the flash-attention optimized Transnormer with a plain Pytorch Transformer. 

Baseline: for fair comparison, the baseline Transformer should also positional embeddings or gated linear units (which are straightforward to be added to Transformer as well). 

Robust inference: the proposed new inference algorithm is rather trivial. It’s more natural (and conventional in the literature) to include the decay factor in the recurrence (i.e., $ h_t = \lambda \  h_{t-1} + k_t v_t^\intercal $ ) rather than in the input and output.

### Questions
Can you compare against RetNet[1] in Sec 4.2? Transnormer is quite similar to RetNet with the very similar design of decay and positional embeddings. It'd be useful for authors to clarify the difference and make empirical comparisons.  

1. Retentive Network: A Successor to Transformer for Large Language Models

### Soundness
3 good

### Presentation
2 fair

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
This paper presents TransNormerLLM and claims the first linear attention-based LLM that outperforms conventional softmax-based models in terms of both accuracy and efficiency.

The adopted techniques include (1) LRPE position encoding together with an exponential decay to avoid attention dilution issues; (2) a gating mechanism following Flash; and (3) Lightning Attention to accelerate the training process.

Experiments on various scale LLM models trained on self-collected corpus demonstrate outstanding performance.

### Strengths
1. The pioneering work focusing on the linear attention-based LLM. This direction is of great interest and significance to the community.

2. Combine various tricks to make linearized LLM work, including the aforementioned LRPE position encoding, gated linear attention or MLPs, and lightning attention.

3. Through evaluation and ablation studies to reveal the core techniques that make linear attention work.

### Weaknesses
1. How does your linear attention handle the autoregressive decoding? As of training, you can feed the network with a batch of inputs with long token dimensions. But when it comes to the generation phase, I am afraid that only limited tokens are used to generate the next token. Then do you still have benefits for inference?

2. The paper reads like a combination of various tricks as a lot of techniques were discussed in the previous paper, like LRPE, Flash, and Flash Attention. Especially for the Lightning Attention vs. Flash Attention, I did not find any difference between these two. The gated mechanism was also introduced in Flash paper. These aspects leave us a question in terms of the technical novelty of this paper.

3. It looks like during training, you are still using the quadratic attention computational order as indicated in Equ. 10? I suppose it was to handle the masking part. But that loses the benefits of training with linear attention complexity.

4. In terms of evaluation, although in the abstract, the authors claim that the linearized LLM extends to 175B parameters, most experiments are conducted on 375M models. For the large parameter size settings, the author only reports the memory and latency cost savings. The accuracy information is missing, without which I feel hard to evaluate the linearized LLMs.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
