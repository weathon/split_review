# KV Prediction for Improved Time to First Token

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
\label{sec:abstract}
Inference with transformer-based language models begins with a prompt processing step. In this step, the model generates the first output token and stores the KV cache needed for future generation steps. This prompt processing step can be computationally expensive, taking 10s of seconds or more for billion-parameter models on edge devices when prompt lengths or batch sizes rise. This degrades user experience by introducing significant latency into the model's outputs. To reduce the time spent producing the first output (known as the ``time to first token'', or \textit{TTFT}) of a pretrained model, we introduce a novel method called KV Prediction. In our method, a small \textit{auxiliary} model is used to process the prompt and produce an approximation of the KV cache used by a \textit{base} model. This approximated KV cache is then used with the base model for autoregressive generation without the need to query the auxiliary model again. We demonstrate that our method produces a pareto-optimal efficiency-accuracy trade-off when compared to baselines. On TriviaQA, we demonstrate relative accuracy improvements in the range of $15\%-50\%$ across a range of TTFT FLOPs budgets. We also demonstrate accuracy improvements of up to $30\%$ on HumanEval python code completion at fixed TTFT FLOPs budgets. Additionally, we benchmark models on an Apple M2 Pro CPU and demonstrate that our improvement in FLOPs translates to a TTFT speedup on hardware.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper uses a smaller model based approach to predict the KV cache content to reduce the TTFT and the improve the prefill stage latency of LLM serving.

### Strengths
The idea of KV cache prediction based on Auxiliary model seems unique, though there are potential issues (as described in the weakness).

### Weaknesses
1. The code has not been released yet! However, the authors claimed that as a part of their contributions. Anyway, releasing code can not be inferred as a technical contribution.

2. The paper mainly focuses on works of token eviction to justify the claim of TTFT increase. However, there are works like KV cache quantization example, KIVI [1], GEAR [2], for which this may not be true always under all settings. Additionally, for complex reasoning tasks KV quantization have shown more promise as opposed to eviction [2], so please do compare with such approaches!

3. There are system level works like Sarathi [3], and Etalon [4] that tried to reduce the prefill and decode times through lossless approaches. The authors referred to orthogonal approaches like pruning, but not these relevant lossless approaches!

4. There are existing works that tried to reduce TTFT, including Minference [5], and SeerAttention [6]. Please compare your work with them.

5. The method would increase the memory data transfer for the KV cache as opposed to the baseline.

6. The method would increase the memory requirement due to storage need of an auxiliary model.

7. The results are not comprehensive, please demonstrate on popular LLMs like LLaMA, OPT, Phi etc. on tasks like PG19, GSM8k-5shot, XSUM, passkey retrieval to understand the merit of the proposed approach.

8. The approach requires training to do KV compression which might not be feasible on device, and most of the existing KV compression settings are assumed to be training free due to the underlying assumption of it to be an inference time optimization. Brining training in the loop would significantly limit its application as such assumptions wont be valid.

### Questions
Please refer to weakness.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel method to reduce the time to first token.  It uses a small auxiliary model to predict the KV cache for the base model. Experiments on TriviaQA and humaneval demonstrates the effectiveness in achieving a pareto-optimal efficiency-accuracy trade-off when compared to existing baselines.

### Strengths
Reducing the time to the first token is a crucial and challenging problem. This paper conducts extensive experiments and makes significant efforts to design KV prediction, which demonstrates effectiveness in achieving a Pareto-optimal trade-off between efficiency and accuracy.

### Weaknesses
1. Based on the experimental results, the base model performance can be easily affected after applying the proposed method.  Compared to other methods that can indirectly reduce time to the first token, such as quantization, is the Pareto curve of KV prediction still considered optimal?

2. Could the authors provide additional performance results on challenging reasoning tasks (e.g., GSM8K/MATH) to assess whether this method impacts the base model's performance?

### Questions
see the weaknesses section.

### Soundness
2

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
3

### Summary
This paper addresses the latency issues in transformer-based language models during inference, particularly the time to first token (TTFT), which is the delay before producing the first output token. In large models, this delay is caused by the prompt processing step, where the model generates the initial output token and creates a key-value (KV) cache for subsequent tokens. This step can be especially slow on edge devices with billion-parameter models, leading to a degraded user experience.
To accelerate TTFT, the authors introduce KV Prediction, a technique that uses a small auxiliary model to precompute an approximation of the KV cache for the base model. This approximated cache enables faster autoregressive generation without repeatedly querying the auxiliary model. The method achieves a pareto-optimal balance of efficiency and accuracy compared to other approaches. For example, in tests on TriviaQA, KV Prediction yields accuracy gains of 15%-50% across various TTFT FLOPs budgets, and on HumanEval for Python code completion, it improves accuracy by up to 30% at fixed FLOPs budgets. Benchmarks on an Apple M2 Pro CPU show that these FLOP savings translate into faster TTFT on real hardware. The authors also plan to release their code to support reproducibility.

### Strengths
- Proposes a new method for accelerating the prefilling stage of LLM, using a smaller model
- Gives detailed explanation of the training process.

### Weaknesses
 - The method is only tested on OpenELM family models, thus the generalizability remains a question. This is the major concern.
- For the CPU inference, shouldn’t we also consider TPOT? From Table 3, there are some improvements over auxiliary-only and base models, but they also improve TPOT. With this consideration, is low TTFT but high TPOT worthy? How about the total execution time?
- For HumanEval, the advantages are not as obvious as in TriviaQA, as shown in Figure 4. This makes the generalizability of the proposed method on a broad range of benchmarks remains a question. Why not test on more datasets?

### Questions
The problems raised in weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Long TTFT degrades users' experience of edge devices. Therefore, the authors propose KV Prediction, a technique that utilizes an auxiliary model to predict a larger base model's initial value of KV-Cache. The method is evaluated on benchmarks, TriviaQA and HumanEval. On TriviaQA, relative accuracy improvements are in the range of 15%−50% across a range of TTFT FLOPs budgets. On HumanEval Python code completion, accuracy improvements can be up to 30% at fixed TTFT FLOPs budgets. The authors also explore the efficiency-accuracy trade-off space. Real-world validation on an Apple M2 Pro CPU confirms that improvement in FLOPs translates to a TTFT speedup on hardware.

### Strengths
1. The algorithm is clearly defined and well explained.
2. The efficiency-accuracy trade-off is well studied through empirical experiments.

### Weaknesses
1. At line 066, the paper claims that "We release our code". However, there is no link to the code. Could the authors provide the like or clarify the code release plan?
2. Possible incorrect estimation of FLOPs: In Secture 4.4 Line 303 claims that "The FLOPs-per-token compute cost of transformers inference can be estimated as 2P, where P is the number of parameters in the model". However the caculation in Kaplan et al., 2020 is $C = 2P+2n_{layer}d_{attn}N$ because $n_{ctx}=N$. The second term cannot be omitted. Therefore, the claim that "The total FLOPs required for prompt processing for N tokens is NP" is wrong, and thus Figures 3, 4, and 5 are questionable. Could you address this discrepancy and update the results if necessary?

### Questions
1. What is the measured extra memory that Auxilary Model uses?
2. Have the authors tried to co-optimize the algorithm with the Neural Engine on Apple M2 Pro CPU? If not, why? If so, what is the conclusion?

### Soundness
2

### Presentation
3

### Contribution
2
