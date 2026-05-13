# DFRot: Achieving Outlier-Free and Massive Activation-Free for Rotated LLMs with Refined Rotation

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Rotating the activation and weight matrices to reduce the influence of outliers in large language models (LLMs) has recently attracted significant attention, particularly in the context of model quantization.
Prior studies have shown that in low-precision quantization scenarios, such as 4-bit weights and 4-bit activations~(W4A4), randomized Hadamard transforms can achieve significantly higher accuracy than randomized orthogonal transforms.
Notably, the reason behind this phenomena remains unknown.
In this paper, we find that these transformations show substantial improvement in eliminating outliers for common tokens and achieve similar quantization error.
The primary reason for the accuracy difference lies in the fact that randomized Hadamard transforms can slightly reduce the quantization error for tokens with massive activations while randomized orthogonal transforms increase the quantization error.
Due to the extreme rarity of these tokens and their critical impact on model accuracy, we consider this a long-tail optimization problem,
and therefore construct a simple yet effective method: a weighted loss function.
Additionally, we propose an optimization strategy for the rotation matrix that involves alternating optimization of quantization parameters while employing orthogonal Procrustes transforms to refine the rotation matrix.
This makes the distribution of the rotated activation values more conducive to quantization, especially for tokens with massive activations.
Our method enhances the Rotated LLMs by achieving dual free, \textit{Outlier-Free} and \textit{Massive Activation-Free}, dubbed as DFRot.
Extensive experiments demonstrate the effectiveness and efficiency of DFRot.
By tuning the rotation matrix using just a single sample,
DFRot achieves a perplexity improvement of 0.25 and 0.21 on W4A4KV4 and W4A4KV16, respectively, for LLaMA3-8B, a model known for its quantization challenges.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method, DFRot, designed to address outliers encountered when quantizing large language models (LLMs). The method initializes with a Hadamard matrix and adapts to activation outliers. It is then applied to LLaMA/Mistral models under W4A4 settings to verify its effectiveness.

### Strengths
1. The paper is well-written and clearly structured, making it easy to follow.
2. The method’s motivation is substantiated by experimental results, lending it credibility.

### Weaknesses
1. The authors extensively emphasize that RH outperforms RO and effectively handles massive outliers, which RO cannot. However, this appears trivial and unworthy of further investigation. Firstly, it is evident that RH, by its construction as a Hadamard matrix, can distribute outliers evenly across channels, which RO, as a randomly initialized orthogonal matrix, cannot accomplish. Secondly, as already noted, numerous works, such as QuaRot [1], have employed Hadamard rotation matrices and confirmed the effectiveness of RH. Lastly, the paper lacks theoretical analysis on this point. The authors do not provide a clear definition of RO and RH, leaving the reader to infer their properties, which is a significant oversight. The core issue is not just that RH works better, but why this difference arises from the properties of the matrices themselves, a point that needs more rigorous analysis.
2. The novelty and effectiveness of the method seem limited. Numerous prior studies have explored learnable matrices, including SpinQuant [2] and DuQuant [3]. **There is a noticeable lack of comparison with these methods, both in terms of methodological differences and performance metrics.** From my perspective, the results in the paper do not outperform any of these works [2, 3]. Additionally, the model size used (≤13B) is relatively small, which limits the persuasiveness of the results. The comparison with SpinQuant is relegated to the appendix and lacks a thorough performance analysis, focusing instead on speed and efficiency. The authors claim SpinQuant overfits on WikiText-2, but this is not substantiated by experiments on different calibration datasets or other benchmarks. The performance gap between DFRot and SpinQuant on the LLaMA 2-7B model is also quite small, making the results less convincing.
3. The method does not include evaluations related to actual memory reduction or speedup. Furthermore, the paper lacks a visualization of the quantization error, which would be valuable for understanding the method's effectiveness.

### Questions
1. Is the rotation matrix a Diagnol Block matrix, or a full $D\times D$ matrix, where $D$ is the hidden dimension size?
2. How similar is the final matrix obtained by your method and the Hadamard matrix used for initialization? If the similarity is small, it suggests that the method’s effectiveness may rely more on the Hadamard matrix than on your training approach.
3.It would be helpful if the authors provided visualizations comparing 1) original activation; 2) activation transformed by QuaRot; 3) activation transformed by their method, to better demonstrate the effectiveness of trained matrix.
5. Do different layers or projections share a common rotation matrix? Will this method lead to increased memory or time costs during the inference phase?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study the difference between two rotation matrices used for post training quantization, and shows some empirical evidence explaining their difference in performance. Specifically, the random hadamard transformation is better at reducing quantization error for tokens with massive activations in 4 bit activation quantization. Using these insights, the authors take the framework for inserting rotations into an LLM architecture proposed by QuaRot, and learn a subset of those rotation matrices. Their optimization uses a weighted sum between the tokens with massive activations and those without. Experiments are provided on Llama2 7b, 13b, llama3 8b, and mistral 7b.

### Strengths
- I think looking at the massive activations is a sensible thing for investigating RH vs RO. 
- And I think that the resulting approach which takes advantage of these insights is interesting.
- Overall I do like the story of this paper, which I see as trying to gain understanding between 2 rotation matrices, and using this understanding to improve the method.

### Weaknesses
I have concerns about this paper. Overall, I think the writing could use work. It's also unclear why the authors only target the "R1" rotation matrices. But more significantly, I think they should include experiments comparing to SpinQuant. This is the more appropriate comparison, because this method also learns their rotation matrices. Finally, I think that there should be a inference time consequence to this method that I think the authors should make more clear. 

Some other comments:
- I find the difference between random hadamard and random orthogonal confusing, because hadamard transform is orthogonal. 
- I found the language describing the relative strengths/weaknesses of RO/RH (e.g. paragraph starting L77) to be confusing. 
- I think the writing in Section 3 could be improved. I believe that 3.1 describes how to integrate rotation matrices into the architecture. But I think readers unfamiliar with QuaRot can be confused. I think that some summary sentences describing the overall goal, and pointing readers to QuaRot for further details, would be helpful. I see that QuaRot is cited, but only for a RMSNorm equality, it is not clear from the text that QuaRot actually describes the overall approach of a way to integrate rotations. 
- I'm unconvinced by the line of argument in Section 3.2. The authors say that the activation quantization error in Fig 2 is not that different between "RH" and "RO", but the overall PPL from Table is significantly different. How Fig 2 is just from a single layer, and I honestly think it's hard to tell from the plots if there is a significant difference or not. Are there perhaps some summary statistics about activation errors that the authors can share?

### Questions
- One suggestion: hadamard transformation is orthogonal, and therefore I think the contrast of hadamard vs orthogonal is not entirely accurate and a bit confusing. Perhaps the first time this comparison is made specify this difference, and then I think it's ok as a shorthand to say hadamard vs orthogonal.
- Per Section 3.1, why do the authors only target rotation matrices R1? and not R2,R3,R4?
- Also, R1 will be applied to the input activations, and therefore will need to be applied during inference. What are the computational costs?
- What exactly are the RO matrices? RH have been proposed by QuIP#, but it is unclear what the RO matrices are.
- Another reason why I think the naming of "random orthogonal" matrices is misleading: the authors are making claims about RH vs RO performance, but as far as I can tell "RO" is simply the matrices generated by the SpinQuant paper. It's more accurate to say that the rotations matrices from these two papers are being compared.
- The authors provide an empirical observation, that RH is better at reducing the quantization error for tokens with massive activations in 4 bit activation quantization. But why is this the case?
- what does the "time" row in Tab 2 mean? is this training or inference?
- Why don't the authors compare to SpinQuant? Comparing Llama2-7b 4-4-4 Tab 1 in the SpinQuant paper to Tab2 in this paper, appears that SpinQuant achieves a better wikitext 2 ppl of 5.9, vs DFRot which achieves 6.2. If I've made an incorrect comparison, please let me know. The baselines between the two papers looked to be comparable.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the quantization problem for transformer architectures. It begins with an analysis of the impact of outliers—activations with unusually large values—on the performance of quantized models. The authors propose a commonly used approach of mitigate this issue: they rotate weight matrices and embedding vectors in the KV cache. The novelty of their approach is in using a learnable rotation matrix, designed to reduce quantization error specifically for outlier activations. This matrix is optimized via a cost function that prioritizes minimizing quantization error for these outliers. The authors introduce an iterative algorithm that appears computationally efficient for minimizing this cost function. The paper demonstrates the performance of the proposed method under 4-bit quantization in a series of experiments.

### Strengths
Quantization is a crucial problem, as memory constraints significantly limit the scalability of large language models. This paper tackles an important and timely research question, making it a compelling contribution to the field.

### Weaknesses
The presentation could be improved, as key details are missing that would help better position the work relative to existing methods and verify the authors' claims. For example, the paper does not adequately differentiate its method from SpinQuant and Quip, both of which also apply a learned rotation matrix to model weights before quantization.

Moreover, recent advancements in KV cache quantization are not sufficiently discussed. The practical performance of DFRot, for example, could have been compared to other recent approaches, such as:

- Liu, Zirui, et al. "Kivi: A tuning-free asymmetric 2bit quantization for kv cache." arXiv preprint arXiv:2402.02750 (2024).
- Zandieh, Amir, Majid Daliri, and Insu Han. "QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead." arXiv preprint arXiv:2406.03482 (2024).

The experiments are confusing. Which experiments focus on model quantization, and which are aimed at KV cache quantization? It is unclear what is being quantized in the experiments, as the method does not seem to quantize the KV cache or the model weights directly. The paper states that it quantizes activations, but it is not clear what this means in the context of the transformer architecture. Specifically, it is unclear if this refers to the input to the attention or feedforward layers, or some other intermediate representation. The lack of clarity makes it difficult to understand the scope and impact of the proposed method.

In Section 3.4, the authors mention that quantization is regarded as clustering, but the explanation is vague. Are the authors suggesting clustering the rows of matrix X? Each row is a high-dimensional vector, and clustering such vectors directly would likely yield random and meaningless results. Practical clustering-based quantization methods typically partition the coordinates of high-dimensional vectors into smaller blocks, applying clustering to these blocks. A more precise explanation here would improve clarity.

### Questions
- What is the main difference between SpinQuant and Quip and your proposed method? Can you differentiate yourself from these methods?

- In Section 3.4, the authors mention that quantization is regarded as clustering, but the explanation is vague. Are the authors suggesting clustering the rows of matrix X? Each row is a high-dimensional vector, and clustering such vectors directly would likely yield random and meaningless results. Practical clustering-based quantization methods typically partition the coordinates of high-dimensional vectors into smaller blocks, applying clustering to these blocks. A more precise explanation here would improve clarity.

- The experiments are confusing. Which experiments focus on model quantization, and which are aimed at KV cache quantization?

- How does the proposed method perform in comparison to the aforementioned KV cache quantization methods?

Additionally, I would like to note: please try to address my concerns, and rest assured that I will consider raising my score if you provide sufficient results during the rebuttal.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors proposed a rotation-based post-training quantization (PTQ) scheme for the quantization of LLMs.
First, the authors empirically analyzed why random Hadamard transforms lead to better performance compared to random orthogonal transforms; the key reason is that random Hadamard transforms handle massive outliers much better than random orthogonal transforms. 
Second, the authors presented how to optimize the random matrix that leads to the effective quantization of massive outliers; alternating optimization of quantization parameters and the rotation matrix has been presented.
Finally, the efficacy of the proposed method has been demonstrated via extensive experiments.

### Strengths
1. The authors analyzed why random Hadamard transforms lead to better performance compared to random orthogonal transforms.
2. The proposed weighted loss function is well-motivated and reasonable based on the above finding.
3. The claims presented by the authors are well supported by experimental results.

### Weaknesses
1. Some statements contradict each other (see Questions below).
2. Experiments are limited to some specific cases.
  - The size of LLMs is larger than 7B for which the performance gap between the conventional and proposed methods is not that noticeable.
  - The utilized weight quantizers (RTN and GPTQ) are not state-of-the-art.
  - The activation quantization configuration is dynamic per-token quantization, which is very difficult and expensive to implement in real hardware.

### Questions
1. Clarity on the proposed method and experimental setup
  - When measuring the quantization error in Section 3.2, the l2-norm of the activation perturbation (Eq.(1)) was used? If yes, the reviewer thinks that the final task loss degradation, rather than the activation quantization error itself, needs to be used as a metric.
  - How to determine the clip ratio $\alpha$ and $\beta$ has not been mentioned in Section 3.4.
  - When optimizing the rotation matrix (with fixed quantization parameters), it seems that the proposed weighted loss function in Eq.(2) has NOT been used. The corresponding solutions in Eqs. (8) and (10) consider all activations equally, regardless of whether activations being normal activations or massive outliers. In such a case, the authors did not consider massive outliers as in existing works.
  - While the authors mentioned that they performed the iterative optimization process with just one round (line 351), the number of iterations has been specified as 100 in line 371.

2.  More experiments are needed.
  - The size of LLMs used in the experiments is larger than 7B for which the performance gap between the conventional and proposed methods is not that noticeable for W4A4. The reviewer recommends conducting experiments with OPT models whose size varies from 125M to 66B.
  - From Table 2, the performance gap between QuaRot and DFRot reduces greatly when the weight quantizer changes from RTN to GPTQ. The reviewer thinks that if a better weight quantizer (e.g., aespa [1]) has been used, the gap between QuaRot and DFRot is very marginal. Please show the results with better weight quantizers.
  - From Figures 9 and 10, when the activation clipping is used, the performance gap between DFRot and no rotation is reduced. The reviewer thinks that the gap between QuaRot and DFRot becomes smaller if the activation clipping is used. Please show the results when applying activation clipping to both QuaRot and DFRot.
  - While most conventional works consider the per-token dynamic activation quantization, such a setting is expensive to implement in real-world scenarios. Please show the results for the **per-tensor static** activation quantization.

[1] Towards next-level post-training quantization of hyper-scale transformers, arXiv 2024.

### Soundness
2

### Presentation
3

### Contribution
2
