# PUMA: Secure Inference of LLaMA-7B in Five Minutes

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
With ChatGPT as a representative, tons of companies have began to provide services based on large Transformers models. However, using such a service inevitably leak users' prompts to the model provider. Previous studies have studied secure inference for Transformer models using secure multiparty computation (MPC), where model parameters and clients' prompts are kept secret. Despite this, these frameworks are still limited in terms of model performance, efficiency, and deployment. To address these limitations, we propose framework \puma\ to enable fast and secure Transformer model inference. 
Our framework designs high quality approximations for expensive functions such as $\gelu$ and $\softmax$, and significantly reduce the cost of secure inference while preserving the model performance. Additionally, we design secure Embedding and LayerNorm procedures that faithfully implement the desired functionality without undermining the Transformer architecture. \puma\ is about $2\times$ faster than the state-of-the-art  framework \mpcformer (ICLR 2023) and has similar accuracy as plaintext models without fine-tuning (which the previous works failed to achieve).  
\puma\ can even evaluate LLaMA-7B in around 5 minutes to generate $1$ token. To our best knowledge, this is the first time that a model with such a parameter size is able to be evaluated under MPC.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a model that utilizes multi-party computation techniques to perform the LLAMA-7B model while preserving the privacy of the client's data. In this process, an optimization of the approximation method for the GeLU function was carried out, and softmax, embedding, and layer normalization methods were all implemented using MPC, achieving an end-to-end implementation. Through these techniques, the computational time has been reduced by approximately 2 times compared to the existing implementation, MPCformer.

### Strengths
1. Completion of end-to-end implementation of a large language model using multiparty computation techniques.
2. Achieving inference that is twice as fast as the previously published MPCformer model.
3. The operation of the GeLU function in a different manner compared to the conventional approach.

### Weaknesses
1. Most of the methods appear to be simple adaptations of existing techniques, lacking any distinctive novel approach. While the results are impressive from an industrial perspective, it raises doubts about whether they are suitable for ICLR, which places a strong emphasis on academic contributions.

2. While it claims to perform twice as fast as MPCformer, the paper lacks precise explanations of why each technique is superior to the existing ones, making it challenging to assess their effectiveness. Specifically, the paper does not provide a breakdown of the computational cost for each component (e.g., GeLU, softmax, embedding, layer normalization) in both their method and MPCformer, making it difficult to pinpoint the source of the speedup.

3. The primary technical contribution seems to be the approximation of the GELU function. However, without a clear comparison to existing approximations, it is challenging to assess the value of this technique. The paper introduces variations in polynomial computation based on the range of x, but it is not evident how this approach is superior to the conventional method of approximating the GELU function in terms of computational efficiency. It is unclear if this piecewise polynomial approximation offers a significant advantage over other established methods like minimax polynomial approximations or rational function approximations, which are commonly used for approximating non-linear functions in MPC.

4. Regarding the meaningful academic contributions in softmax, embedding, and layerwise normalization, it is not clear where they lie, making it difficult to discern the significance of these contributions. The paper does not discuss the specific challenges in implementing these components in an MPC setting, nor does it highlight any novel techniques or optimizations that were required to achieve this end-to-end implementation. It is unclear if these implementations are straightforward adaptations of known MPC protocols or if they involve any novel insights.

### Questions
1. Provide numerical evidence of how the computations involved in our method for approximating the GELU function offer advantages in terms of computational and communication costs compared to existing techniques that achieve the same level of accuracy.

2. Convince that the techniques employed in softmax, embedding, and layerwise normalization go beyond mere combinations of existing methods and provide non-trivial technical contributions.

3. Explain what specific factors contributed to the 2x performance improvement compared to MPCformer and quantitatively specify the performance gains achieved by each factor.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a secure Transformer inference framework in 3PC.

### Strengths
+ Simple but effective approximations for GELUs.
+ End-to-end framework for Secure LLM Inference.
+ Extensive evaluations.

### Weaknesses
The protocols in this work seem limited contributions and are mainly taken from prior works.

### Questions
1. What is the cost of secure inference on LLaMA-7B when extending it to a common input length e.g., 128?
2. Does the polynomial approximation of GELU affect the accuracy of large models such as LLaMA-7B because it seems to cause a relatively large error?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes PUMA, a 3PC inference protocol for Transformers.

### Strengths
The 3PC setting for LLM is timely.

### Weaknesses
1. Limited novelty. The provided protocols are straightforward and contain no novel design or construction.
2. Compared with the baseline, the protocol advantages seem to all come from RSS.
2. Overclaim the experimental performance. The title of this paper is Secure Inference of LLaMA-7B in Five Minutes. However, it is overclaimed. 5 minutes is only when the input and output are 4 and 1 token respectively, which is obviously not in line with the practical service setting.

### Questions
See above.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper brings together a bunch of recent techniques for semi-honest, honest majority 3 server multi party computation and supplements them with a few custom designed gadgets. These are then used to approximate GeLU based neural networks in MPC. They have an experimental section analysing how quickly it runs and the accuracy/precision of the resulting protocol.

### Strengths
The paper brings together a bunch of SOTA work well.
It does provide some new approximations, e.g. of GeLU, which seem like useful components for future work.
The paper is well laid out and easy to follow.
The resulting protocol is runnable with fairly large models and gets good approximations.

### Weaknesses
The paper seems some what incremental in nature with the new contributions being slightly limited in scope.
It is dubious whether the ability to generate one token from a language model in 5 minutes between three parties in the semi-honest honest majority model is likely to have any applications in the imminent future. But this is a step closer to something practical being possible.

### Questions
Are you aware of any plausible near term application that this technology is close to good enough to be deployed for?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
