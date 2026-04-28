# FISTAPruner: Layer-wise Post-training Pruning for Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Pruning is a critical strategy for compressing trained large language models (LLMs), aiming at substantial memory conservation and computational acceleration without compromising performance. However, existing pruning methods typically necessitate inefficient retraining for billion-scale LLMs or rely on heuristically designed metrics to determine pruning masks, leading to performance degradation. This paper presents, for the first time, a LASSO-like convex optimization model crafted to induce sparsity in LLMs. By leveraging the FISTA, we introduce FISTAPruner, a novel method that includes a cumulative error elimination mechanism within decoder layers and supports parallel pruning for unstructured pruning. Additionally, we extend this method to 2:4 semi-structured pruning. We comprehensively evaluate FISTAPruner on models such as OPT and LLaMA variants with 125M to 70B parameters under unstructured and 2:4 semi-structured sparsity, showcasing superior performance over existing methods across various language benchmarks. Notably, it can remove 50% of the model parameters for LLaMA-3-70B while retaining 98.6% and 95.6% of the zero-shot task performance under these two sparsity patterns, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes FISTAPruner, a layer-wise pruning method designed for both unstructured and semi-structured pruning, targeting efficient sparsification of large language models (LLMs). This approach utilizes the FISTA method (Fast Iterative Shrinkage-Thresholding Algorithm) to facilitate efficient convergence. Additionally, it employs a LASSO-like convex optimization model to effectively enhance sparsity in LLMs. To address the cumulative output error between the full and pruned models due to the sequential output error transfer across transformer decoder layers, the authors utilize layer-wise pruning with an intra-layer error correction mechanism.

Experiments conducted on various model sizes, ranging from 125M to 70B parameters—including OPT, LLaMA, LLaMA-2, and LLaMA-3—across datasets such as WikiText-2-raw, PTB, and C4, demonstrate that FISTAPruner outperforms existing baseline methods (e.g., SparseGPT, Wanda, Wanda+DSnoT, SparseGPT+PERP, and Wanda+PERP) in terms of model performance after pruning.

### Strengths
(+) The method effectively incorporates FISTA for efficient pruning during the post-training process, leading to faster optimization and enhanced performance
(+) By effectively employing LASSO to identify pruned weights with targeted sparsity, the approach minimizes reliance on heuristic-based methods, thereby improving overall effectiveness in the pruning process.
(+) The authors enhance the proposed method by developing an algorithm that enables semi-structured pruning, allowing for practical acceleration on real-world hardware.

### Weaknesses
(-) The paper requires experiments to compare FISTAPruner with other methods that have similar computational costs. Existing baseline methods, such as SparseGPT and Wanda, do not involve retraining during pruning. In contrast, FISTAPruner conducts retraining in the process of finding W∗. Although DSnoT and PERP are used instead of retraining, their computational costs are lower than the layer-by-layer approach employed in FISTAPruner. So, it is necessary to compare their performance under similar computational cost conditions (e.g., training on SparseGPT is performed layer by layer).
(-) The benefits of using FISTA over traditional gradient descent methods are not sufficiently explained, which may leave readers unclear about its specific advantages in this context.

### Questions
1. In line 89, the paper states, "Our results confirm that FISTAPruner can efficiently create sparse networks from pretrained LLMs without retraining." However, the process of finding the pruned weights W* seems to function similarly to retraining. Could you clarify this point, as it may cause confusion for readers?
2. In line 306, the paper states, "We treat each decoder layer as an independent pruning unit, enabling parallel pruning across multiple decoder layers on different devices." However, the proposed method conducts pruning sequentially. Can you explain how parallel pruning is achieved alongside sequential pruning? A more detailed explanation or revision would be helpful.

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
3

### Summary
The paper introduces FISTAPruner, a novel method for pruning large language models (LLMs) post-training to achieve significant sparsity, thereby reducing memory footprint and computational demands without compromising model performance. The authors introduce a LASSO-like convex optimization model tailored for layer-wise pruning, utilizing the Fast Iterative Shrinkage-Thresholding Algorithm (FISTA) to induce sparsity. A another innovation is the integration of an intra-layer error correction mechanism that mitigates cumulative errors across decoder layers during the pruning process. Additionally, FISTAPruner is extended to support 2:4 semi-structured pruning, aligning with hardware acceleration capabilities. Comprehensive experiments on various models (OPT, LLaMA) demonstrate that FISTAPruner outperforms state-of-the-art methods such as SparseGPT, Wanda, DSnoT, and PERP across multiple benchmarks, including perplexity and zero-shot task performance.

### Strengths
1. The paper presents a unique approach by integrating FISTA with a LASSO-like model, which is innovative in the context of LLM pruning.
2. The results demonstrate that FISTAPruner can prune up to 50% of model parameters while retaining high accuracy, outperforming existing methods like SparseGPT and Wanda.
3.  The integration of an intra-layer error correction mechanism is novel, which may avoid error cumulation.

### Weaknesses
 **1. Major Weakness:**   The intra-layer error correction mechanism is briefly mentioned but could benefit from a more detailed explanation and analysis. It raises the question of whether other methods (e.g., SparseGPT and Wanda) could achieve better performance if integrated with this mechanism.

### Questions
**1. Major Question:** In Wanda [1], they prune model weights by choosing the smallest $|W| ||X||_2$. While in your methods, you prune weights by minimizing the discrepancy of $||W^\*X^\*-WX||_2$. What's the difference between your sparsity objective with that of Wanda?   

**2. Minor Question:** In the paper, the error correction mechanism is applied solely within individual layers. Why is the error correction confined to intra-layer applications rather than being implemented across the entire model? In my understanding, extending the error correction mechanism globally could further mitigate the phenomenon of error accumulation throughout the network. 


[1] A SIMPLE AND EFFECTIVE PRUNING APPROACH FOR LARGE LANGUAGE MODELS, ICLR 2024

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author proposed an LLM pruning algorithm that uses “FISTA” (Fast Iterative Shrinkage-Thresholding Algorithm) to identify optimal pruning masks. The author demonstrates the utility of the proposed technique across many state-of-the-art LLMs and with both structured and unstructured sparsity. The improvement over prior art is, however, small.

### Strengths
- This work is theoretically grounded, and provide some guarantees on convergence time.
- This work shows strong results in structured 2:4 pruning setup.
- This paper is overall well-written and easy to understand.

### Weaknesses
 - It’s unclear to me what’s new in this work relative to, say, SparseGPT, which also sets up pruning as an optimization problem and generally yields similar results as this work in unstructured pruning setup. It occurs to me that the fundamental difference appears to be that this work uses a different optimizer to solve essentially the same problem.
- While in structured 2:4 pruning setup this work yields substantial improvement, it is unclear why this is the case.
- Neither “Amount of Calibration Data” nor “Warm Start” is actually ablation study. Please do proper ablation studies by removing specific features of your algorithm design.

### Questions
Question:
- Can you discuss difference between this work and sparseGPT?
- Can you perform ablation studies on 2:4 structured sparsity

### Soundness
3

### Presentation
4

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
This paper proposes FISTAPruner, an accurate pruning algorithm for large language models (LLMs).
The main ideas of FISTAPruner are (1) intra-layer error correction, (2) FISTA-based optimization algorithm, and (3) adaptive hyperparameter tuning algorithm.
The authors conduct exhaustive experiments to verify the effectiveness of FISTAPruner, and find that FISTAPruner is more accurate than existing algorithms; specifically, it shows almost 5% higher average accuracy on zero-shot tasks when pruning Llama-3 70B.
The main strength of this paper lies in its high accuracy and exhaustive amounts of experiments.
However, the novelty and writing quality of this paper are insufficient.

### Strengths
The main strengths of this paper are as follows:

1. The authors achieve meaningful accuracy improvement in diverse settings. For example, FISTAPruner shows almost 5% higher accuracy than the second-best algorithm, i.e., SparseGPT, when pruning Llama-3 70B models.

2. This paper conducts extensive experiments covering diverse models from OPT to Llama-3 to show the robustness of FISTAPruner. FISTAPruner consistently shows comparable or the highest accuracy (or the lowest perplexity) in all cases.

3. The figures in this paper are straightforward to understand.

### Weaknesses
I summarize the weakness of this paper below. I use the symbols [M] and [m] for each numbering to distinguish between major and minor weaknesses.

### Method
The main weakness of this paper is the lack of originality (or novelty). We summarize the weaknesses of the proposed method as follows.
1. [M]  Error correction, the first idea, is just using the output of the pruned previous linear operators, and this idea is already used in previous works. Furthermore, the authors ignore the "inter-layer errors" induced by the pruning of previous layers when they correct errors.

2. [M] The authors make use of the existing optimization algorithm, FISTA, without any modification. Introducing L1 regularization for pruning is a prevalent idea and there is no novelty.

3. [M] The authors propose a new hyperparameter tuning algorithm, which has no specific name, but there is no explanation of the strength or novelty of this algorithm. There are no experiments that compare the performance of this algorithm with previous hyperparameter tuning algorithms.


### Writing
The followings are the weaknesses in writing.

4. [M] The main contribution of this paper is to use FISTA algorithm to prune LLMs. However, explanation about FISTA is too insufficient. It would better introduce the basics of FISTA in Section 2 (Background) and explain the modification to use FISTA for pruning LLMs in Section 3.2.

5. [M] According to "1.", it is hard to agree with the statement "Instead of pruning each operator in isolation like existing works" in line 148.

6. [m] Minor issues in writing:

  6.1  (line 193) "The proposed optimization model 3" -> "The proposed optimization model in Equation 3"

  6.2 (line 262) "Theorem 3.3" -> "Theorem 1"

  6.3 (All equations) Use bold texts for representing matrices and vectors following the guideline of ICLR. It would be better to use blackboard bold S for representing a set of permissible sparsity patterns in Equation 1.

  6.4 (All tables) Move captions of tables above the tables following the guideline of ICLR.

  6.5  This paper does not contain the "Reproducibility Statement" which is encouraged by ICLR.

  6.6 (Table 6) There are too many bold texts in Table 6.


### Experiments

7. [m] The authors compare the performance of FISTAPruner with limited competitors without justification. The authors should compare the performance of FISTAPruner with structured pruning algorithms [1,2] or justify their selection of competitors.

### Questions
1. What's the difference between FISTA, and L1-regularized training using SGD w/ momentum?

2. Is there any reason you use outdated models such as OPT and Llama-1? How about using the latest models such as Phi, Gemma, and Mistral, if you want to use diverse models?

3. Could you compare the performance of your "Adaptive hyperparameter tuning" algorithm with existing hyperparameter search algorithms, e.g. BOHB [3]?

4. Are DSNoT and PERP (1) competitors or (2) compatible algorithms? If (1) competitors, then how about integrating Tables 2 to 4 as a single table? If (2) compatible algorithm, then how about integrating Tables 3 and 4? In this case, it would be better to compare the performance of "FISTAPruner" with "FISTAPruner + DSnoT" and "FISTAPruner + PERP" to show the compatibility.

5. What is the main point of the Section "Warm Start"? Could you clarify the takeaway of this section?

### References
[1] Ma, Xinyin, Gongfan Fang, and Xinchao Wang. "Llm-pruner: On the structural pruning of large language models." Advances in neural information processing systems 36 (2023): 21702-21720.

[2] Song, Jiwon, et al. "SLEB: Streamlining LLMs through Redundancy Verification and Elimination of Transformer Blocks." arXiv preprint arXiv:2402.09025 (2024).

[3] Falkner, Stefan, Aaron Klein, and Frank Hutter. "BOHB: Robust and efficient hyperparameter optimization at scale." International conference on machine learning. PMLR, 2018.

### Soundness
2

### Presentation
1

### Contribution
1
