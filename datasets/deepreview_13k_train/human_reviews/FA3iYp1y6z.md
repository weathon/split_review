# Low-Rank Correction for Quantized LLMs

- Decision: Reject
- Scores: 6, 6, 5, 5, 3

## Abstract
We consider the problem of model compression for Large Language Models (LLMs) at post-training time, where the task is to compress a well-trained model using only a small set of calibration input data. 
In this work, we introduce a new low-rank approach to correct for quantization errors of \emph{activations} in LLMs: we propose to add low-rank weight matrices in full precision that act on the \emph{unquantized} activations. We then solve a joint optimization problem over the quantized representation of the weights and additional low-rank weight matrices to quantize both weights and activations.
We focus on the case of 4-bit weight-and-activation quantization (W4A4). Using ranks equivalent to 10\% of the original weight matrix size, our approach reduces the accuracy gap with the original model by more than 50\%. Using ranks equivalent to 30\% of the original weight matrix,  the accuracy gap is closed completely. We demonstrate our results on four recent LLMs, namely Llama-2, Llama-3, Phi-3 and Mixtral models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes LRC (Low Rank Correction), a method to perform error correction for quantization of weights *and* activations (a common approach to perform model compression in LLMs). They add a full precision low-rank weight matrices in the forward pass that act on the unquantized activations and accounts for errors arising from both weights and activations.

### Strengths
- They paper is written well and easy to understand. The scheme they propose is sound and intuitive in its formulation.
- Their method can use any weight quantization technique as a subroutine (they use GPTQ in the paper), which allows other tools/papers to plugin their own method.
- They perform sensible ablations in order to clearly identify the impact of the weight only quantization vs activation quantization, and when low rank error correction offers value. Moreover, they also show that the quantization is replaceable by any technique which can use the weight matrix and the covariances matrices to output a quantized version.

### Weaknesses
# Major
- *Limited Contribution*: The paper stitches together many well known building blocks in the PTQ literature to build a sane, effective technique. In my opinion, it is a sound engineering feat, but still has high overlap with the previous work on the topic by Zhang et al (2024) and Ou et al (2024). The authors do differentiate themselves by the fact that they do a joint optimization over the low rank and quantized matrices which is key to the delta over the previous work. However, this is also a well known technique and has been applied in other works such as [1]
- The experiments are performed on models which do not overlap with the QuaRot paper (their primary baseline) and hence it is difficult to compare directly. Moreover, their method uses additional bits (aka low rank correction factors) and hence comparison to QuaRot is not a strictly fair comparison, a small increase in model size though it may be. The additional memory usage should be explicitly stated in a table column, similar to average bit precision or bits per weight in Ou et al, so that the reader can make an informed choice about the trade-off between memory and accuracy.
- The authors mention a number of contemporary work (Quip, Quip#, LQER etc) but provide an empirical comparison against a very limited baseline (QuaRot).
- The authors claim that they can close the accuracy gap using rank equivalent to 30%, this seems to be true only for Phi3 which the authors present as an unqualified statement. Moreover, I cannot find the corresponding results in the evaluation section

# Minor
- In L431, the authors use the phrase "10% additional ranks" which I believe is not meaningful
- L399-407 sub section "on the effect of rank" does not mention the table/fig where the results can be found
- Table 1, for Phi3, LRC(1) outperforms LRC(5), a weird anomaly since one would expect performance to increase monotonically with iters
- Best results not provided in bold font
# References
1. Saha, Rajarshi, et al. "Compressing Large Language Models using Low Rank and Low Precision Decomposition." arXiv preprint arXiv:2405.18886 (2024).

### Questions
- Why is it necessary to store the low rank matrices in full precision? Couldn't they also be quantized?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies a brand-new approach on the post-training quantization problem of LLMs. In particular, the authors suggest introducing a low-rank adaptation to relieve the accuracy loss of quantization, which uses a small size dataset to generalize their low-rank adaptation matrix U, V. This work is novel and easy to implement.

### Strengths
* The idea of introducing low-rank adaptation to correct the quantization error is good, and trivially effective. In my perspective, these adaptation-based methods are worthy of further and comprehensive study.
* The derivation in this paper provides concise intuition, which is easy to follow.
* The topic of efficient LLM deployment is becoming vital currently, this method has considerable potential in addressing such PTQ problems on LLMs.

### Weaknesses
 * It is not clear how the rank of adaptation would influence the efficiency. This would become my main concern for this paper. I strongly recommend the authors to add an experiment to evaluate its enhancement of memory usage and speed. Specifically, the paper should explore the trade-offs between rank size, memory footprint, and inference speed. A detailed analysis of how different rank sizes impact the computational cost and memory requirements is crucial for practical applications.
* The presentation of this paper is good, but not excellent enough. The authors should add an introduction of GPTQ method and Cholesky in their appendix (since they are parts of the main algorithm) for presenting to the broader audience. The current presentation assumes a level of familiarity with these techniques that may not be universal. A more thorough explanation of these core components would significantly improve the paper's accessibility and completeness.
* The choice of dataset in $X$ should be carefully considered, but I don’t see any analysis about how $X$ will affect the performance. I recommend the authors to add a discussion about this and their assumption for rigorousness. The paper lacks a systematic investigation into how the characteristics of the calibration dataset $X$ influence the performance of the low-rank adaptation. It is essential to explore the sensitivity of the method to different datasets, including variations in size, domain, and diversity, to ensure the robustness and generalizability of the proposed approach.

### Questions
* Please answer the issues and questions in the Weakness and point out my potential misunderstandings. I am happy to discuss and enhance my rate.
* Why is the last line (LRC (5)) for the Mistral model missing both in Table 1 and Table 5?
* From Table 3, LRC fails to beat SVD on average score, can you explain why this happens?

### Soundness
3

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
2

### Summary
This paper introduces a new method called LRC (Low-Rank Correction) for quantizing large language models (LLMs) to 4-bit weights and activations (W4A4) while minimizing accuracy loss. The key idea is to jointly optimize for a quantized weight matrix acting on quantized activations and a full-precision low-rank weight matrix acting on the original unquantized activations. This allows LRC to significantly reduce the quantization error and close the accuracy gap with the full-precision model.

### Strengths
This paper is its novel approach to quantizing large language models to 4-bit weights and activations while maintaining high accuracy. The LRC method's ability to optimize jointly for a quantized weight matrix and a full-precision low-rank correction matrix, which is connected to the original unquantized activations, effectively reduces quantization error. This innovative technique sets LRC apart from previous approaches and demonstrates its potential for enabling highly compressed models with minimal performance degradation.

### Weaknesses
The paper does not analyze the computational cost associated with the added low-rank correction matrix. While the method effectively reduces quantization error, the impact on inference time and memory usage is not thoroughly explored. This is an important consideration for the practical deployment of the LRC method. Specifically, the paper lacks a detailed breakdown of the additional FLOPs and memory accesses introduced by the low-rank correction, making it difficult to assess its real-world efficiency. A comparison against standard quantization techniques, considering both accuracy and computational overhead, is missing.

The authors leave the ideal implementation of the low-rank computation for future work. Without a concrete implementation strategy, it may be difficult for practitioners to immediately adopt the LRC method in real-world applications. Providing guidance or preliminary implementation details, such as pseudocode or a discussion of potential parallelization strategies, could have made the paper more impactful. The absence of a clear path for efficient implementation limits the practical applicability of the proposed method.

Although the paper identifies activation quantization as the primary source of error, it does not propose novel activation quantization schemes. The authors rely on existing techniques like round-to-nearest and suggest that future work on improved activation quantization could lead to better results. Addressing this limitation within the paper could have further strengthened the contribution. The paper should have explored alternative activation quantization methods or at least provided a more detailed analysis of the limitations of round-to-nearest in the context of LRC.

### Questions
How does the computational cost of the low-rank correction matrix scale with the size of the language model? Is there a trade-off between the compression ratio and the computational overhead introduced by LRC?

Can the LRC method be extended to other model compression techniques, such as pruning or knowledge distillation? How would the low-rank correction approach interact with these techniques?

How sensitive is the performance of LRC to the choice of calibration dataset used for computing the activation statistics? Would using a more diverse or domain-specific calibration dataset lead to better results?

The authors suggest that improved activation quantization schemes could further enhance the performance of LRC. What specific properties should these improved schemes have, and how might they be developed?

### Soundness
2

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
3

### Summary
The paper studies post training quantization. They achieve a new SoTA for W4A4. This and the introduction of their algorithm is the main contribution of the paper. The main idea is to solve Equation (2) using alternating minimization by optimizing either for quantized weights or for low rank matrices. The authors also initialize the low rank matrices carefully. In terms of experimental results, the authors report wikitext-2 perplexity as well as from lm-eval (PIQA, HellaSwag, Arc-Easy, Arc-Challenge, Winograd and Lambada). The numbers demonstrate that the introduced approach beat their main benchmark QuaRot. Surprisingly, one iteration of alternating minimization is enough to achieve good performance.

### Strengths
please see summary

### Weaknesses
minor typos:

Line 57: summurized -> summarized

Line 191: "... we drop the dependency in l of our notations" -> replace "in" with "on"

Line 353: "Our ambition is to close the gap between out main benchmark" -> replace "out" with "our"?

Line 405: "equan" -> equal

Line 421: "prononced" -> pronounced

Line 455: "In this work we have not study the computational" -> replace "study" with "studied"

The paper contains several propositions but they lack proofs.

The approach of adding a low rank matrix is similar to approaches in these papers that the authors could cite: "LoRA: Low-Rank Adaptation of Large Language Models" and "QLoRA: Efficient Finetuning of Quantized LLMs".

My main concern with the paper is that it doesn't cite or discuss the above 2 related papers, which seem quite related. Also, the paper lacks several proofs. Furthermore, the paper could consider generative tasks for benchmarks such as gsm8k. Typically, generative tasks are harder for quantized model than multiple choice tasks. Given all this, my overall rating for the paper is "marginally below the acceptance threshold".

### Questions
The paper contains several propositions but they lack proofs.

The approach of adding a low rank matrix is similar to approaches in these papers that the authors could cite: "LoRA: Low-Rank Adaptation of Large Language Models" and "QLoRA: Efficient Finetuning of Quantized LLMs".

My main concern with the paper is that it doesn't cite or discuss the above 2 related papers, which seem quite related. Also, the paper lacks several proofs. Furthermore, the paper could consider generative tasks for benchmarks such as gsm8k. Typically, generative tasks are harder for quantized model than multiple choice tasks. Given all this, my overall rating for the paper is "marginally below the acceptance threshold".

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work presents a low-rank approach aimed at enhancing the performance of post-training quantization. Specifically, it refines the Low-Rank Correction method by incorporating selected low-rank matrices in full precision during the forward pass to help reduce quantization errors. The experimental results indicate competitive performance, showing improvements over current methods, espeically at W4A4 quantization levels.

### Strengths
1. The studied problem is important.
2. This paper provides a new method of low rank correction to consider both weights and activations are quantized situation.
3. This paper shows a good experimatal performance on low bit quantazation W4A4.

### Weaknesses
1. The paper does not provide sufficient proof of the correctness of its algorithm. There is no error analysis for the approximation methods presented. While the authors detail their approach for solving Equations 3 and 4, they do not demonstrate that these solutions are equivalent to Equation 2, which is the main problem of interest. Specifically, the paper lacks a formal proof showing that the iterative optimization of the low-rank correction matrices converges to a solution that minimizes the quantization error defined in Equation 2. The absence of such a proof makes it difficult to assess the theoretical validity of the proposed method.

2. The theoretical analysis provided by the authors is overly simplified. The assumptions of full rank in Propositions 3.3 and 3.4 are questionable. Empirical studies have suggested that activations in large transformer models often exhibit a structure that can be approximated as low rank, making these assumptions potentially unsuitable. The analysis does not adequately address the practical scenarios where the covariance matrices of activations may be ill-conditioned or have low effective rank, which is common in large language models. This limits the applicability of the theoretical results.

3. The paper does not include an analysis of the time complexity associated with adding low-rank weights. This omission leaves a gap in understanding the computational implications of the proposed method. The paper should provide a detailed analysis of the computational cost of the low-rank correction, including the cost of matrix decompositions and the additional forward pass computations. This analysis should compare the computational overhead of the proposed method with existing quantization techniques.

4. The contribution and novelty of the paper are somewhat limited. While the authors improve the accuracy of post-training quantization through low-rank correction, additional analyses on aspects such as time complexity, convergence, and error bounds would enhance the paper’s competitiveness and impact. The paper does not clearly articulate how the proposed method significantly advances the state-of-the-art beyond existing low-rank correction techniques, particularly in the context of simultaneous weight and activation quantization.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2
