# Scaling Laws for Precision

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Low precision training and inference affect both the quality and cost of language models, but current scaling laws do not account for this. In this work, we devise ``precision-aware'' scaling laws for both training and inference. We propose that training in lower precision reduces the model's \textit{effective parameter count}, allowing us to predict the additional loss incurred from training in low precision and post-train quantization. For inference, we find that the degradation introduced by post-training quantization increases as models are trained on more data, eventually making additional pretraining data actively harmful. For training, our scaling laws allow us to predict the loss of a model with different parts in different precisions, and suggest that training \textit{larger} models in \textit{lower} precision may be compute optimal.  We unify the scaling laws for post and pretraining quantization to arrive at a single functional form that predicts degradation from training and inference in varied precisions. We fit on over 465 pretraining runs and validate our predictions on model sizes up to 1.7B parameters trained on up to 26B tokens.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript provides a thorough investigation into the impact of bit precision on inference performance and introduces a scaling law that correlates performance with precision. The paper is commendable for its extensive experimental validation. The study addresses a significant problem in the field of deep learning optimizations and offers practical insights for efficient model deployment. The manuscript is well-structured and the arguments are clearly presented

### Strengths
Strengths:

1. The paper tackles an important issue with the introduction of a bit precision scaling law. While this topic has been explored before, the theoretical scaling law presented in this work offers valuable guidance for the efficient deployment of models in real-world applications. The implications of this work could be transformative for the field.

2. The authors have provided a wealth of experimental results that not only validate the existing scaling laws across different model sizes but also demonstrate the generalizability of previously unseen scenarios. This thorough experimental section strengthens the paper's contributions and is persuasive.

3. The manuscript is particularly strong in its methodological rigor, with a clear articulation of the scaling laws and their implications for precision in deep learning models.

### Weaknesses
no clear weakness.

### Questions
potential typos: 

1. row303: P_a and =P_{kv} as well

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the scaling law for precision, including exploring the #parameters, #tokens, pretraining precision, and inference precision.
The paper first introduces the background via (1) giving a decent introduction to quantization, (2) presenting the existing scaling laws on #parameters and #tokens, and (3) experimental setup.
Then the paper introduces the scaling laws for post-train quantization, and quantized training, sharing interesting findings.
Finally, a unified scaling law is introduced.

### Strengths
(1) The paper studies a meaningful topic, the scaling laws of precision, which is a new topic following the scaling law of data and parameters.

(2) The paper gives a good presentation. I especially appreciate the introduction to quantization. I'm not familiar with how quantization works in detail, so it helps a lot.

(3) The paper shows interesting findings in Sec. 3.1 Fig. 2: more pretraining tokens result in lower performance for post-train quantization with a high quantization rate.

(4) The paper shows interesting findings in Sec. 4.1 Fig. 3: KV cache is more sensitive to the change of precision when precision is low, but when precision is high, KV cache is more robust to the change of precision compared with weights and activations.

(5) The paper shows interesting findings in Sec. 4.3 Fig. 6: there would be cases where training in low precision leads to better evaluation loss.

(6) The paper generally shows that the proposed scaling law works well in the experimental setting of the paper.

### Weaknesses
 (1) The paper uses the dataset Dolma for experiments. Though it's hard, it would be interesting to see how pretraining data affects this law.

(2) The paper uses the OLMo-style models for experiments. It would be great to give a general introduction to OLMo-style. Are they transformer-based model? While the abstract states the scaling law for language models, there would be other types of language models other than OLMo-style models, such as SSM.

### Questions
I respect the amount of experiments to support that the proposed scaling law works well. However, the counterintuitive findings are more attractive to me. The paper summarizes the findings in Fig 1. Could the author further explain the underline reasons/mechanism of such counterintuitive phenomenons?

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
This paper explores how precision -- specifically, low-precision training and inference -- affects the performance and compute cost of large language models. The authors propose new "precision-aware" scaling laws to predict the degradation in model performance when trained or quantized at different precision levels. Their work is motivated by the increasing trend toward low-precision training, driven by the need to reduce computational costs while maintaining model quality. While previous research has focused on scaling laws that balance model size and dataset size (for example Hoffmann et al. Chinchilla scaling laws), these do not account for the role of precision. The authors argue that precision is a critical factor that influences both compute efficiency and model performance, especially as hardware evolves to support lower precisions. They aim to fill this gap by developing scaling laws that incorporate precision as a third variable alongside model size and dataset size.

### Strengths
- The paper introduces a new dimension to the well-established scaling laws by incorporating precision as a critical factor. This is an important contribution because most prior work focused on model size and dataset size without considering precision, which is increasingly relevant due to hardware advancements supporting lower-precision computations. By doing so, the authors offer a more comprehensive framework for understanding and optimizing model performance under different training and inference conditions.

- The authors fit on over 465 pretraining runs across different precisions (3-bit to 16-bit) and sizes (up to 1.7 billion parameters), providing a robust dataset to validate their proposed scaling laws. The empirical results are consistent with the theoretical predictions, achieving high R^2 values (e.g., R^2 = 0.97 for post-training quantization degradation). 

- The paper offers actionable insights into how low-precision training can be compute-optimal, particularly in scenarios where hardware constraints or cost considerations are paramount. For example, it shows that training larger models at lower precision can sometimes be more efficient than using higher precision, which is a valuable insight for practitioners looking to optimize both performance and computational costs.

### Weaknesses
 - While the paper focuses extensively on integer-type precisions (e.g., 3-bit, 8-bit), it does not explore floating-point types like FP8 or BF16 in as much depth. Given that floating-point formats are widely used in modern hardwares, this omission limits the generalizability of the findings to real-world applications where floating-point precision is common. Specifically, the paper does not address how the different bit allocations between exponent and mantissa in floating-point representations might affect the scaling laws, which could lead to different optimal precision points compared to integer quantization. This could limit the applicability of the scaling laws in environments where floating-point precision dominates, potentially requiring further research to adapt these findings.

- The experiments are conducted on specific hardware setups that support low-precision computations, such as GPUs optimized for integer-type operations. The fitted constants and trends may not generalize well across different hardware architectures or future technologies that handle precision differently. For example, the paper does not consider hardware with native support for floating-point precisions like FP4 or other emerging low-precision formats, which could exhibit different performance characteristics. This may reduce the long-term relevance of the paper’s findings as hardware evolves.

- Maybe I'm missing this, but the paper suggests that compute-optimal precision is around 8 bits but does not deeply explore scenarios where precision drops below 4 bits (e.g., binary or ternary quantization). Given that future hardware may support even lower precisions, this limits the scope of the findings. The paper should consider the challenges of training with extremely low precision, such as the instability of training and the need for specialized architectural modifications, which are not addressed in the current work. This is particularly relevant given the recent interest in binary and ternary networks and their potential for extreme compute savings.

- While pretraining cost optimization is thoroughly explored, inference-time costs -- especially in real-time or latency-sensitive applications -- are not given as much attention. In many practical deployments, inference-time efficiency is more critical than pretraining cost savings. The paper does not analyze the trade-offs between model size, quantization, and inference latency, which is a critical factor for real-world deployment. This imbalance might limit the practical applicability of some of the findings in scenarios where inference-time efficiency is more important than pretraining considerations.

### Questions
I already specified some of them above, but the questions are particularly as in the following:

- While the paper primarily focuses on integer-type quantization, you mention that floating-point quantization  is commonly used in practice, especially in pretraining. Can you elaborate on how your scaling laws might differ when applied to floating-point quantization? 

- You mention in the paper that activations and KV cache are more sensitive to low precision than weights, particularly when precision drops below 4 bits. Could you provide more detailed insights into why activations and KV cache are more sensitive? Is this primarily due to the per-tensor vs per-channel quantization method, or are there other factors at play?

- Your experiments are conducted using specific hardware such as Nvidia H100 GPUs. How do you expect the scaling laws to generalize across different hardware architectures, especially those that may handle precision differently, for example future GPUs with native support for FP4 or binary/ternary quantization?

- Given that your largest model size is 1.7B parameters, do you anticipate any limitations or deviations from your scaling laws when applied to much larger models with hundreds of billions or trillions of parameters?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper propose the scaling laws for precision through replacing the N in the original Chinchilla with the effective parameter count $N_{eff}$ and adding the post-training effects.

### Strengths
1.	The proposed scaling law unify the post train quantization and quantized training into a single functional form.
2.	The finding in the section 4.3 is inspired and the conclusions are consistent with usual experience and give a theoretical explanation.
3.	The experiment is adequate and reasonable and the paper is well written.

### Weaknesses
1.	The paper use the $N(1-e^{P_{w}/\gamma_{w}})$ to fit the left in the figure 3. But I think the power law is the most commonly used in all kinds of scaling law form. I suggest the author could compare the exponential with power law like $N(1- A*P_{w}^{\alpha})$.

### Questions
As shown in above.

### Soundness
4

### Presentation
4

### Contribution
3
