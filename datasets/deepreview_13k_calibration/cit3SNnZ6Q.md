# Q-Sparse: All Large Language Models can be Fully Sparsely-Activated

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
\vspace{-0.3cm}

We introduce, \textbf{\our{}}, a simple yet effective approach to training sparsely-activated large language models (LLMs). \our{} enables \textbf{full sparsity of activations} in LLMs which can bring significant efficiency gains in inference. This is achieved by applying top-$K$ sparsification to the activations and the straight-through-estimator to the training. We also introduce \textbf{Block \our{}} for batch training and inference. The key results from this work are, (1) \our{} can achieve results comparable to those of baseline LLMs while being much more efficient at inference time;
(2) We present an inference-optimal scaling law for sparsely-activated LLMs; (3) \our{} is effective in different settings, including training-from-scratch, continue-training of off-the-shelf LLMs, and finetuning; (4) \our{} works for both full-precision and 1-bit LLMs (e.g., \textbf{BitNet b1.58}~\cite{bitnet}). Particularly, the synergy of BitNet b1.58 and \our{} (can be equipped with MoE) provides the cornerstone and a clear path to revolutionize the efficiency, including cost and energy consumption, of future LLMs.

\vspace{-0.3cm}

\begin{figure}[h]
    \centering
    \begin{subfigure}{0.4\textwidth}
        \centering
        \includegraphics[width=\linewidth]{pic/fp16_qsparse_scaling.pdf}
    \end{subfigure}
    \begin{subfigure}{0.4\textwidth}
        \centering
        \includegraphics[width=\linewidth]{pic/bitnet_qsparse_scaling.pdf}
    \end{subfigure}
    \includegraphics[width=0.7\linewidth]{pic/qsparse_cropped.pdf}
    \vspace{-0.25cm}
    \caption{\our{} achieves a superior inference-optimal scaling law than the dense models. It saves significant compute of matrix multiplication by top-$K$ sparsification of the activations.}
    \label{fig1}
\end{figure}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method to train sparsely-activated large language models (LLMs) that are more efficient at inference. The authors introduce the use of squared ReLU to enhance sparsity and apply STE to address the gradient vanishing problem during the training of these sparsely-activated LLMs. Experiments are conducted on both dense and quantized models.

### Strengths
1. The paper is well-written and easy to follow.
2. The extension of the scaling law to sparsely-activated LLMs in Section 3 is well-motivated and innovative.
3. Experimental evaluations are comprehensive, including both dense and quantized LLMs, reflecting realistic deployment settings.

### Weaknesses
1. MoE models are also a type of sparsely-activated model. It would be valuable to include a comparison between MoE models and the proposed sparsely-activated models in terms of accuracy and efficiency.
2. A concern lies in the actual inference speedup of the proposed method, especially during the decoding step in batched inference. In batched settings, the columns activated may vary across cases, and in the worst case, it may still be necessary to load all weights during each decoding step. Since the decoding step can be memory-bound rather than compute-bound at certain batch sizes, this could potentially limit the speedup achieved by the proposed method in practice.
3. While empirical results suggest that STE is effective, it remains unclear why gradients should be maintained for non-activated neurons. A more rigorous theoretical discussion or proof would strengthen this point.

### Questions
Given that MoE models are a special type of sparsely-activated model, what are the connections and differences between the scaling law for MoE models and the scaling law proposed here?

### Soundness
3

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
4

### Summary
The authors introduced Q-Sparse that enables full sparsity of activations for efficient inference. They also presented an inference-optimal scaling law for sparsely-activated LLMs. They conducted experiments on commonsense reasoning tasks and MMLU.

### Strengths
1. The sparsely-activated models with around 40% sparsity ratio can perform comparably to the dense baselines with the same model size and training tokens.

2. The performance gap between the sparsely-activated models and the dense baselines decreases as the number of parameters goes up.

### Weaknesses
1. The paper mentioned "Q-Sparse enables full sparsity of activations in LLMs which can bring significant efficiency gains in inference", but there is neither discussion nor experiment about measuring the execution time and/or peak GPU memory usage. Furthermore, the analysis of inference speed-up should be conducted on diverse hardware platforms (e.g., H100, A100, L40) to provide a comprehensive view of the efficiency gains, rather than relying on a single hardware setup.

2. The evaluation for math (e.g., GSM8K, MATH) and code (e.g., HumanEval, MBPP) would be required to ensure that the performance of sparsely-activated models can match the performance of the dense baselines with the same model size and training tokens. Given that  Orca’s capability is designed for open-ended generation, only the evaluation for commonsense reasoning tasks and MMLU seems not enough.

### Questions
How about conducting experiments for Llama models (e.g., Llama 3 8B)? The reason why I brining it up is that Llama is more popular than Mistral and Qwen, so I believe that using Llama is more beneficial to researchers and engineers.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors analyzes the impact of sparsity on different components and experimental settings of LLM, and propose Q-Sparse to training sparsely activated large languge models.

### Strengths
The authors present valuable works on analyzing the impact of sparsity on LLM.

### Weaknesses
This paper lacks of methodological clarity in terms of novelty and the structure of the paper is not clear. Moreover, methodological novelty is limited since the proposed sparsity method may be considered as trick novelty in different components of LLM.

The core principle of sparsity is not clear and is only explained by formulas, lacking a theoretical explanation.

The proposed sparsity method is more like a trick novelty since it is simple and applied to different components of LLM.

This paper has some findings and is more like an analytical paper, but what guiding significance do the experimental findings in the paper have? This can reflect the contribution of the paper to the LLM field.

It is recommended to provide comparative experiments with different models under different architectures on different datasets. The comparison in Table 1 is not sufficient to illustrate the effectiveness of the method.

### Questions
1. The core principle of sparsity is not clear and is only explained by formulas, lacking a theoretical explanation.
2. The proposed sparsity method is more like a trick novelty since it is simple and applied to different components of LLM.
3. This paper has some findings and is more like an analytical paper, but what guiding significance do the experimental findings in the paper have? This can reflect the contribution of the paper to the LLM field.
4. It is recommended to provide comparative experiments with different models under different architectures on different datasets. The comparison in Table 1 is not sufficient to illustrate the effectiveness of the method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed Q-Sparse to enable full sparsity of activations in LLMs, aiming to improve the efficiency in inference. Different from prior works, Q-Sparse selectively activates the top-K features of each activation tensor. To stabilize the training, Q-Sparse also back-propagates the gradients of the non-activated features using straight-through estimator (STE). It was shown that Q-Sparse could be effectively applied to full-precision and 1-bit LLMs for pre-training, continued-training, and fine-tuning. The paper further presented the inference-optimal scaling law for sparsely activated LLMs, showing that they outperform their vanilla counterparts with the same inference compute budget (i.e. FLOPs).

### Strengths
i) Method. Q-Sparse is simple, yet effective. The proposed top-K sparsification could be implemented in modern compute units (e.g. CPU, GPU)

ii) Performance. Q-Sparse demonstrated superior performance compared to its vanilla counterparts with the same inference compute budget (i.e. FLOPs)

iii) Analysis. The paper provided the scaling law analysis for sparsely activated LLMs, which is potentially valuable to the community.

### Weaknesses
The reviewer has several concerns about the efficiency evaluation.

i) It was claimed Q-Sparse "can bring significant efficiency gains in inference" (L013), "including cost and energy consumption" (L023). However, in the current paper, these claims were only supported by the metrics like activated parameters or FLOPs, which is not fully convincing. Metrics like FLOPs do not have strong correlations with real-world efficiency like wall-clock speed-up, as argued in [1]. The authors are encouraged to demonstrate the inference efficiency of Q-Sparse by metrics that are directly linked to the inference overhead, e.g. speed, throughput, peak-memory usage, energy consumption, etc, as claimed in the abstract.


ii) The reviewer is also expecting some clarifications about the efficiency metrics used in the paper:

A) About the activated parameters. The reviewer agrees with the authors that the I/O for weight loading is one of the major bottlenecks for LLM inference (L038-040), as the weight matrices could be significantly larger than the batched activation tensors. The reviewer wonders how was the number of activated parameter calculated in the evaluation? Specifically, if the weight sharing for batched inputs was considered? This is important as for dense LLMs, the weight matrix may only be loaded once and reused for each input in the batch in GEMM. On the other hand, for sparsely activated LLMs, there were high chances that the full weight matrix may still be loaded if the activated channels, i.e. at least 40% for each input tensor, are uniformly distributed within the batch. In this case, the sparsely activated LLMs may show no I/O benefits compared to the dense LLMs.  

B) About the FLOPs. Compared to the dense LLMs, Q-Sparse introduced extra operations during inference, i.e. dynamically computing the top-K activations for each tensor. The reviewer wonders if their computational overheads were also considered in the FLOP metric. The overheads of such operations could not be ignored as they typically have O(NlogK) complexity (i.e. K >= 40%*N) and cannot be parallelized directly (i.e. reduction).

### Questions
Please refer to Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
