# Integrative Decoding: Improving Factuality via Implicit Self-consistency

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Self-consistency-based approaches, which involve repeatedly sampling multiple outputs and selecting the most consistent one as the final response, prove to be remarkably effective in improving the factual accuracy of large language models. Nonetheless, existing methods usually have strict constraints on the task format, largely limiting their applicability. 
In this paper, we present \emph{Integrative Decoding} (ID), to unlock the potential of self-consistency in open-ended generation tasks. ID operates by constructing a set of inputs, each prepended with a previously sampled response, and then processes them concurrently, with the next token being selected by aggregating of all their corresponding predictions at each decoding step. In essence, this simple approach implicitly incorporates self-consistency in the decoding objective. % decoding algorithm that
Extensive evaluation shows that ID consistently enhances factuality over a wide range of language models, with substantial improvements on the TruthfulQA (+11.2\%), Biographies (+15.4\%) and LongFact (+8.5\%) benchmarks. The performance gains amplify progressively as the number of sampled responses increases, indicating the potential of ID to scale up with repeated sampling. } %Moreover, ID demonstrates strong robustness to generation tasks of varying text lengths, varying model scales, and varying sampling strategies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The "Self-consistency" approach consists in  sampling from a LLM  a set of many different outputs  to select the final hypothesis as the most consistent one with respect to this set. This kind of approach  really helps to improve the "factuality"  of the output. 
This paper builds on this line of research to Integrative Decoding (ID). It allows the use of self consistency approach text generation tasks. The idea :-) is to extend the decoding objective with a consistency term. This new objective can be estimated with a smart and integrative prompt. Experiments show nice  improvements on many benchmarks like TruthfulQA, Biographies and LongFact.

### Strengths
This idea is simple and effective. The theoretical formulation is clear, while in practice the solution is relatively straightforward.  The experimental results clearly support the claims.

### Weaknesses
The extra cost of this approach is maybe not worst than the other self-consistency based methods. However this drawback could be discussed in the paper. It could be nice to provide inference time, even if it is not the claim of the paper.

In equation 4, there are two terms f and G. Then their sum is approximated by the inference with the new prompt. Did you try to recover these two terms given this approximation, to see if your motivation sounds ?

### Questions
In equation 4, there are two terms f and G. Then their sum is approximated by the inference with the new prompt. Did you try to recover these two terms given this approximation, to see if your motivation sounds ?

### Soundness
4

### Presentation
3

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
In this work, the authors propose a new decoding method called "Integrative Decoding" so that self-consistency can be obtained. The experiments shows that this decoding method can improve factuality. The improvements are shown in three benchmarks (TruthfulQA, Biographies, and LongFact).

### Strengths
1. A new decoding method is proposed to improve consistency. Higher factuality are obtained in the experiments.

2. The evaluations are done over six series of LLM with varying scales and multiple benchmarks (TruthfulQA, Biographies, and LongFact).

3. In the analysis, as the number of sampled responses increases, the performance is improved.

### Weaknesses
1. It is reasonable that consistency is obtained with this decoding method. However, factuality improvement seems unclear. Improvements seems more possible If the model is well calibrated. Some discussions can be done in this perspective. 

2. In the evaluation of these experiments, LLM (GPT-4) is used for factuality evaluation. However, there is no human annotation results. Miss match could happen for the evaluation. It could cause the actual improvements.

3. The cost of the proposed decoding method is high: double context length is need, and more inference steps (the same as the number of sampled responses). For long-form generation, it is hard and inefficient.

### Questions
According to Figure 3, the claim "The performance of integrative decoding progressively improves with more sampled responses across six LLMs." seems wrong. For the three models (Llama3, Gemma2, and GLM4), accuracy is increasing, then decreasing. Could you have a check?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes integrative decoding (ID), an extension of leveraging self-consistency to enhance the factuality of LLM generations. Specifically, the authors first sample N responses and subsequently use each as a prefix for prompting the LLM to answer the same question again. Finally, a better response is created by ensembling the generations at token-level. Experimental results on three benchmarks validate the effectiveness of the proposed method.

### Strengths
1. The writing is clear, and the proposed method is simple and effective.
2. Rather than selecting a response from a set of candidates, ID integrates them through generation, which is interesting.

### Weaknesses
1. The main limitation is the lack of comparison with atomic self-consistency approaches [1][2][3]. The study only compares its method with some older baselines (e.g., USC and SR), which have been significantly surpassed by more recent works.
2. The related work section could benefit from discussing the use of self-consistency for uncertainty estimation (e.g., [4]). Self-consistency is not only an approach to improve factuality but is also considered a better estimator of LLM confidence. Incorporating these discussions could potentially deepen the motivation behind this research direction.

### Questions
Please see the above-mentioned weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Integrative Decoding (ID), a new decoding strategy for improving the factual accuracy of LLM by incorporating self-consistency during decoding. ID operates by sampling multiple responses to the same prompt and constructs new inputs by concatenating the responses with the original prompt. Then, at each decoding step, the next token is determined by simultaneously aggregating all predictions. It shows significant performance improvements across different LLMs on open-ended tasks, such as TruthfulQA, Biographies, and LongFact.

### Strengths
1. The paper is easy to follow.
2. The method proposed in this paper doesn't need additional prompting or training, making it more applicable to a wider range of scenarios than previous works.
3. The experimental results show that the performance of this method consistently improves with an increase in the number of sampled responses. In contrast, other methods do not, demonstrating the stability of this approach.

### Weaknesses
1. Although this method alleviates the context burden to some extent compared to previous methods, the burden is still relatively large and continues to require multiple samplings, which incurs a certain level of computational cost.
2. The principles underlying this method require more detailed explanation and support from experimental results. Especially the reasonableness of the assumption.
3. In the "3.5 CASE STUDY" section, examples corresponding to the SR and USC methods are not provided.
4. Although this paper mentions that ID can maintain coherence, it lacks quantitative evaluation results regarding the coherence and fluency of the responses generated by this method.

### Questions
1. Could you provide a more detailed explanation of why the "Context Length" of the ID method is "×2"?

### Soundness
3

### Presentation
3

### Contribution
3
