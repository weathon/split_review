# MoDeGPT: Modular Decomposition for Large Language Model Compression

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Large Language Models (LLMs) have reshaped the landscape of artificial intelligence by demonstrating exceptional performance across various tasks. However, substantial computational requirements make their deployment challenging on devices with limited resources. Recently, compression methods using low-rank matrix techniques have shown promise, yet these often lead to degraded accuracy or introduce significant overhead in parameters and inference latency. This paper introduces \textbf{Mo}dular \textbf{De}composition (\locogpt), a novel structured compression framework that does not need recovery fine-tuning while resolving the above drawbacks. \locogpt partitions the Transformer block into modules comprised of matrix pairs and reduces the hidden dimensions via reconstructing the module-level outputs.
\locogpt is developed based on a theoretical framework that utilizes three well-established matrix decomposition algorithms—Nyström approximation, CR decomposition, and SVD—and applies them to our redefined transformer modules.
Our comprehensive experiments show \locogpt, without backward propagation, matches or surpasses previous structured compression methods that rely on gradient information, and saves 98\% of compute costs on compressing a 13B model.
On \textsc{Llama}-2/3 and OPT models, \locogpt maintains 90-95\% zero-shot performance with 25-30\% compression rates. Moreover, the compression can be done on a single GPU within a few hours and increases the inference throughput by up to 46\%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel model compression method by applying three different matrix decomposition algorithms to three distinct types of computations within Transformers. Compared to previous model compression algorithms, this approach achieves a significant improvement in performance.

### Strengths
1. The authors propose the interesting idea of using three different matrix decomposition algorithms to compress computations in both MLP and Attention.
2. Experimental results demonstrate that the proposed method offers advantages in terms of both performance and efficiency compared to prior pruning and matrix decomposition algorithms.
3. The Appendix includes additional methods and experiments related to group-query attention.

### Weaknesses
1. The authors suggest using three different types of matrix decompositions for three different types of computations within Transformers, but they do not provide motivation for this choice. For example, why is CR decomposition more suitable for Type-2 computation?

### Questions
1. Why does Table 3 include only 50% compression results for models like SparseGPT but lack results for 40% compression? Why is a 40% compression result of MoDeGPT compared to a 50% compression result of SparseGPT?
2. I am curious why magnitude-based and SVD-based compression methods seem to cause model collapse in Table 1, performing worse than random compression (Uniform).
3. The authors applied different compression rates to different layers, but are the compression rates for the three types of computations identical? Based on the analysis in Figure 4, it might be better to allocate a higher compression rate for Attention computations.
4. Why is MoDeGPT more efficient than the baseline at the same compression rate (Figure 3)?

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
2

### Summary
This paper proposes MoDeGPT, which compresses transformers by applying structure decompositions on operations that span *two* weight matrices. The parameter subgroups targeted are the MLP weights, key and query projections, and value and attention output projections. Experimental results show that MoDeGPT is the best no-gradient structured method, and also comparable to the best structured and gradient-based method.

### Strengths
To the best of my knowledge, the method of structured approximations across multiple matrices is novel and the results are strong. For the most part, the paper is well-written.

### Weaknesses
One weakness is the lack of justification for the approximation methods for each weight group. Could you give more intuition behind why each method was chosen? For example, the sentence "Since $W_U$ is inside a nonlinear function $\sigma_s$, we constrain the search space for its approximation to a matrix multiplication $W_U S_k$ for tractability, where $S_k$ is the $k$-column selection matrix" (line 244) only describes the approximation, whereas a justification would explain why Nystrom is a better fit for this problem than other methods.

Another weakness is the relative lack of analysis on the global sparsity allocation. However, this is orthogonal to the main contribution of structured multi-weight approximations.

### Questions
1. In Table 3, is the main claim that although semi-structured methods may outperform MoDeGPT, they are held back by custom GPU support which hinders research velocity?
2. It would be nice to see a throughput versus perplexity graph as well, as opposed to just sparsity vs ppl/throughput, e.g. merge tables 2 and 3.

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
4

### Summary
This paper proposes MoDeGPT, an accurate structured pruning algorithm for LLMs. 
The main idea of MoDeGPT is to define "modules", a novel pruning structure, and apply tailored decomposition algorithms for three different types of modules.
The main strengths of this paper are (1) introducing decomposition algorithms that are not previously used in this domain, (2) proposing a new global sparsity allocation algorithm, and (3) exhaustive experiments and theoretical analysis in Appendix.
However, I have concerns regarding the following: (1) overclaiming regarding the efficiency of MoDeGPT,  (2) lack of experiments regarding large models, e.g., Llama 3 70B, and (3) too simplified proof of Theorem 4.
Therefore, I summarized my concerns in "Weaknesses" and "Questions" and I need to discuss them with the authors.
The score can be increased according to the author's response.

### Strengths
This paper has diverse strengths and I summarize them as follows:

### Method
1. The authors introduce Nystrom approximation, CR decomposition, and SVD to pruning row-column pairs in LLMs. To the best of my knowledge, this is the first work to use Nystrom approximation and CR decomposition to prune LLMs. The authors carefully use them to prune different types of modules.

2. The authors propose a novel global sparsity allocation algorithm with entropic regularization. If this algorithm contributes a lot to improving the accuracy of the pruned models, then this algorithm can be broadly used in pruning.

### Experiments
3. The authors conduct exhaustive experiments to show the superiority of MoDeGPT. Their experiments not only covers accuracies, but also inference speed and pruning cost.

4. The authors analyze the effect of MoDeGPT in a detailed way. They also analyze the sparsity patterns.

### Writing

5. The contents are well-organized and easy to read. Specifically, the authors assign unique colors for each module type and consistently use them. This was very helpful to understand this paper.

### Weaknesses
### Method

1. In the caption of Figure 1, the authors insist that their new pruning structure avoids the need for extra adapters. However, SliceGPT's adapters are introduced to improve accuracy and can be removed for inferencing without (dimensional) errors. Therefore, that statement should be modified.

2. The main contribution of this paper is introducing diverse decomposition algorithms and applying them to the proper modules. However, there are lack of explanations of the characteristics of these decomposition algorithms and justification for using them for each type of module.

3. The proof of Theorem 4 is too simplified and hard to understand. There are lack of explanations to get Equation 33. The authors impose a strong assumption that epsilon becomes infinity which indicates the uniformness of phis.

### Experiment

4. The authors emphasize that MoDeGPT is an efficient pruning algorithm, for example, in Lines 475-477, but MoDeGPT requires expensive pruning costs more than 8 hours for pruning Llama-2 13B models. According to SELB [1], most of pruning algorithms requires less than 16 minutes for pruning Llama-2 13B models. Therefore, it is an overclaiming to insist that MoDeGPT is an efficient algorithm. 

5. There are lack of competitors. The authors should compare their results with state-of-the-art pruning algorithms, especially layer (or block) pruning algorithms, such as SLEB [1]. Layer pruning algorithms provide significant inference speedup and should be included in Figure 3.

### Writing

6. The second paragraph of the Introduction is too detailed and hard to find the main point. It is hard to capture "these challenges" in the third paragraph after reading.

7. The criteria of Table 1 are ambiguous. (1) "No backward propagation" seems like an indirect criteria of pruning efficiency, but MoDeGPT is slow without requiring backpropagation. (2) What is the threshold of maintaining accuracy? (3) SparseGPT supports 2:4 pruning which is treated as a (semi-)structured pruning algorithm.

### Questions
1. Can MoDeGPT outperform "efficient" competitors, such as SliceGPT [2], SLEB, if the competitors perform fine-tuning on the sample dataset to have the same pruning cost as MoDeGPT?

2. Could you elaborate on the detailed explanation of the proof for Theorem 4? Is it permissible to assume that epsilon is large enough to simplify the problem?

3. Does the proposed Global Sparsity Allocation outperform OWL [3]'s strategy?

4.  Does MoDeGPT outperform competitors when pruning gigantic models, e.g., Llama-3 70B?

5. What are the characteristics of Nystrom approximation, CR decomposition, and SVD, and why do we have to use them as proposed in this paper?

### References

[1] Song, Jiwon, et al. "SLEB: Streamlining LLMs through Redundancy Verification and Elimination of Transformer Blocks." arXiv preprint arXiv:2402.09025 (2024).

[2] Ashkboos, Saleh, et al. "Slicegpt: Compress large language models by deleting rows and columns." arXiv preprint arXiv:2401.15024 (2024).

[3] Yin, Lu, et al. "Outlier weighed layerwise sparsity (owl): A missing secret sauce for pruning llms to high sparsity." arXiv preprint arXiv:2310.05175 (2023).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MoDeGPT, a novel training-free compression method for large language models.  It presents a systematic framework for categorizing approximation challenges in Transformer compression, complete with error guarantees. MoDeGPT demonstrates significant performance gains. This method outperforms prior approaches in compression, and achieves a 46% increase in inference throughput.

### Strengths
The paper has the following strengths：

(1) The paper presents a novel training-free compression method called MoDeGPT, applies matrix decomposition at the module level for the first time, and extends the theoretical foundation for weight decomposition in language models.

(2) The paper offers a comprehensive literature review and theoretical analysis, demonstrates significant performance improvements through experimental results, and provides error guarantees along with a theoretical framework.

(3) The method outperforms previous approaches in compression performance, achieves a 46% increase in inference throughput, and enhances the practical value of large language models.

### Weaknesses
The Weaknesses of the paper are listed as follows：
(1) MoDeGPT shows intrinsic bias, performing well on some zero-shot tasks but poorly on others, and currently lacks a solution for bias removal.
(2) Overfitting of the model to calibration data prevents the compression method from generalizing across most tasks.

### Questions
The specific questions and suggestions are listed below:

(1)Do you consider evaluating on more diverse tasks to verify the method's generalizability?

(2)In the specific experiments, could you provide the chosen rank size for the matrix decomposition or an analysis of the related experiments?

### Soundness
3

### Presentation
3

### Contribution
3
