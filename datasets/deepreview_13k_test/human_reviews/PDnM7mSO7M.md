# Large Language Model Evaluation via Matrix Nuclear-Norm

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
As large language models (LLMs) continue to evolve, efficient evaluation metrics are vital for assessing their ability to compress information and reduce redundancy. While traditional metrics like Matrix Entropy offer valuable insights, they are computationally intensive for large-scale models due to their \( O(n^3) \) time complexity with Singular Value Decomposition (SVD). To mitigate this issue, we introduce the Matrix Nuclear-Norm, which not only serves as a metric to quantify the data compression proficiency of LLM but also provides a convex approximation of matrix rank to capture both predictive discriminability and diversity. By employing the \( L_{1,2}\text{-norm} \) to further approximate the nuclear norm, we can effectively assess the model's information compression capabilities. This approach reduces the time complexity to \( O(n^2) \) and eliminates the need for SVD computation. Consequently, the Matrix Nuclear-Norm achieves speeds 8 to 24 times faster than Matrix Entropy for the CEREBRAS-GPT model as sizes increase from 111M to 6.7B. This performance gap becomes more pronounced with larger models, as validated in tests with other models like Pythia. Additionally, evaluations on benchmarks and model responses confirm that our proposed Matrix Nuclear-Norm is a reliable, scalable, and efficient tool for assessing LLMs' performance, striking a balance between accuracy and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes using matrix nuclear-norm as a new metric to evaluate the LLM performance. The major benefit is the computational efficiency can reduce to O(n^2) as compared with the recently new metric matrix entropy. A set of experiments were conduced to show the matrix nuclear-norm evaluation/ranking is consistent with other metrics.

### Strengths
1. proposing a new metric for LLM evaluation. As the hottest area in ML/AI, contributing a new metric for LLM evaluation might be fundamental and impactful.

### Weaknesses
1. The biggest concern from my end is that the contribution might be incremental and limited. The work is motivated by matrix entropy, a very recently proposed metric (a few month ago), which has not fully established the value in LLM community. I'd be quite conservative to its true usage or value before considering any efficiency improvement on it. 

2. The efficiency improvement from O(n^3) to O(n^2) is not valuable in practice. If n is small (e.g., less than 1K), such complexity change can be ignored. On the other hand, if n is super large, say, 10K or 100K, O(n^2) is far from being adequate to be scalable. It will be good to provide some algorithms or approximations that attains O(n) or O(n log n) time complexity that is "truly" efficient and scalable. 

3. The presentation and notation are quite confusing and/or contradiction, yet without clarification. For example, in Eq(1), i believe elements of A are real-valued probabilities, then in line 143, it claims "involves the number of unique categories in matrix A". What does it mean? Isn't the number of unique categories the column number of A or something else? in Line 188, it says "since A is typically sparse, with only a few non-zero responses in each category". Following eq(1), A should be a dense probability matrix, then why is A typically sparse? is A now a binary matrix?

### Questions
see above

### Soundness
2

### Presentation
2

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
In this work, the authors propose to measure the compression abilities of LLMs using a modified $L_{1,2}$ norm that aims at approximating the nuclear norm of the output probabilities obtained from LLMs when evaluated on sentences. More formally, given a sentence of $m$ tokens, and a dictionary of size $C$, the authors propose to approximate the nuclear norm of the output probabilities $A\in[0,1]^{m\times C}$ obtained from an LLM by considering the mean of the $m$ largest (assuming that $m<C$) $l_2$ norms of the column vectors of $A$. They justify their approach by showing that when the Frobenius norm of $A$ is maximized, that is when the entropy of the row probability measures is minimized, then their approximation is close to the nuclear norm of $A$. They advocate that the proposed metric is more efficient than computing directly the nuclear norms, which would require a cubic complexity, as they only require a quadratic number of operations. They also perform an extensive experimental evaluation of the proposed metric on various LLM families, tasks, and datasets.

### Strengths
The main strength of the paper is undoubtedly the extensive empirical evaluation conducted by the authors to evaluate the proposed metric. Specifically, the authors examine a broad range of LLMs, including the Cerebras-GPT models (from 111M to 13B parameters), the Pythia models (from 14M to 12B parameters), the DeepSeek series, the LLaMA3 series, the QWEN 2 series, the Vicuna series, as well as Gemma 7B and Mistral 7B. They also evaluate these models across a diverse set of tasks and datasets, encompassing pre-training, instruction tuning, RLHF, benchmarking, prompt-based learning, and evaluation datasets. In addition, while the theoretical results presented lack some formal rigor and occasionally omit key arguments, they do provide useful insights, particularly by drawing connections between the proposed metric and the nuclear norm.

### Weaknesses
While the paper provides an extensive empirical evaluation of the proposed metric, its relevance for evaluating LLMs remains unclear. The authors frequently draw conclusions that do not align with the experimental results. Additionally, the writing contains numerous issues, which at times makes the content difficult to follow. One particularly concerning point is the authors' assertion that their metric enables the evaluation of LLMs' compression capabilities. This claim lacks both theoretical and empirical support. Furthermore, the authors repeatedly claim to outperform other metrics, though this assertion does not seem meaningful without proper context, as the metrics are not directly comparable. Certain statements also appear inaccurate, such as those regarding the convergence of their metric with respect to the sample size in Figure 4. The proofs presented lack formal rigor, often omitting key arguments needed to substantiate the results. Additionally, numerous notations are introduced without clear definitions. Overall, it would be beneficial for the authors to focus on explicitly defining the objective of measuring the nuclear norm (or rank) of the output matrix, which could serve as a foundation for evaluating the approximation capabilities of their estimator.

Please find below some additional comments:
 - The proof of Theorem 1 is not complete: some (main) arguments are not exposed.
 - $C_p(A)$ is introduced but never defined formally. The conclusion obtained in Eq. (5) is not clear, as $C_p(A)$ has never been defined.
 - The notation "top" is used in Eq.(9) without any clear explanation or definition.
- Notations and indices are not consistent throughout the paper.
- $\Sigma_{\mathcal{S}_i}$ in Eq.(13) is never properly defined.
- In section 5.2.1 the authors conclude in l.341 that the metric considered achieves comparable evaluation accuracy to Matrix Entropy, however, the figure presented for this experiment only compares time complexities.
- In l.379, the authors claim that their metric showcases superior accuracy, however, the meaning of this sentence is not clear to me. In which sense did the author show that the metric considered is more effective than others?
 - typo l. 115: Shannon Entropy only applies to nonnegative matrices

### Questions
- What is the purpose of evaluating the nuclear norm of the output matrix?
- If the goal is to measure the diversity of the prediction, why not consider directly the entropy as defined in Eq. (1)?
 - In which sense does the nuclear norm enable the measurement of the compression capabilities of LLMs?
 - Is the proposed estimator an efficient approximation of the nuclear norm in practice?
 - How one can compare the proposed metric with others? More precisely, in which sense the proposed metric demonstrates superior accuracy compared to traditional metrics?

### Soundness
2

### Presentation
1

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
This paper proposes the **Matrix Nuclear-Norm** as a novel metric to evaluate **Large Language Models (LLMs)** by addressing the computational limitations associated with traditional metrics like **Matrix Entropy**. The Matrix Nuclear-Norm reduces the time complexity from \(O(n^3)\) (as required by Singular Value Decomposition) to \(O(n^2)\) and provides a convex approximation of matrix rank to evaluate predictive discriminability and diversity in LLMs. Extensive experiments demonstrate that the proposed metric provides faster and comparable evaluation of LLMs compared to Matrix Entropy, making it a practical tool for large-scale model assessments.

### Strengths
- The primary strength lies in the scalability improvement over **Matrix Entropy**, reducing time complexity from \(O(n^3)\) to \(O(n^2)\), which is substantial, particularly for evaluating larger models like **Cerebras-GPT** and **Pythia** series. The experiments demonstrated significant gains, with the proposed approach being 8 to 24 times faster for different model sizes (e.g., from 111M to 13B parameters), making it much more feasible for large-scale practical applications.

### Weaknesses
- The **motivation** and **background story** for the proposed method are not well articulated, making it difficult to grasp why the method is particularly suitable for evaluating LLMs. The presentation lacks a clear narrative explaining the unique properties of LLMs that make Matrix Nuclear-Norm an especially effective evaluation metric. As it stands, it seems that the same method could be applied to any deep NLP model, leaving the reader questioning what makes LLMs distinct in this context.


 - The explanation regarding **related work**, specifically **Matrix Entropy**, is inadequate, which hinders the reader's understanding of how Matrix Nuclear-Norm compares to previous efforts and why it offers a better alternative. A more thorough and detailed comparison is necessary to fully communicate the advantages and limitations of each method.



- The **notation** throughout the paper is used inconsistently, which introduces ambiguity and impedes readability. There are even some inconsisten points. For example, the paper initially claims that the computational complexity is **\(O(n^2)\)**, but in lines 338-339 mentions **\(O(nm + n \log n)\)** without sufficient context to clarify the conditions under which each complexity holds. 



- The **Figure 2 legend** is too small to be legible, which makes interpreting the results challenging. Moreover, in Figure 2(d), the proposed method exhibits an unexpected trend on **Dolly-15K** and **HH-RLHF**, where the performance diverges from other datasets, yet the authors do not provide sufficient discussion or analysis of these anomalies. Addressing such unexpected trends would help clarify the robustness and potential limitations of the proposed method.

### Questions
see weakness

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
3

### Summary
As large language models (LLMs) expand, efficient metrics are essential for assessing data compression. Traditional methods like Matrix Entropy are computationally intensive, but our proposed Matrix Nuclear-Norm offers a faster, \(O(n^2)\) alternative without requiring SVD. This method is \(8\)–\(24\) times quicker for large models, accurately evaluating compression and diversity in a scalable, efficient way, as validated on models like CEREBRAS-GPT and Pythia.

### Strengths
Matrix Nuclear-Norm Proposal: We introduce a novel method using the nuclear norm, reducing the computational complexity of evaluating language models from O(n^3) to O(n^2). This reduction lessens the reliance on SVD, making Matrix Nuclear-Norm a more efficient alternative to Matrix Entropy.

Comprehensive Experimental Validation: Extensive tests on models of various sizes confirm that Matrix Nuclear-Norm effectively assesses model compression, with values decreasing as model size increases, showcasing its robust evaluative capacity.

Benchmark Testing and Ranking: We conducted inference tests on popular benchmark datasets, AlpacaEval and ChatbotArena, ranking models by performance. The results show that Matrix Nuclear-Norm efficiently and accurately evaluates the inference capabilities of medium and smaller models, demonstrating its potential for broad applications in model assessment.

### Weaknesses
There are many notations used without definition.

### Questions
Please check ${\mathcal D}$ in  equation (4). Please avoid using (1) and (2) in lines 206 and 207. Please check $\hat A$ in (9). Please check Algorithm 1 carefully, such as $x_i$ and Steps 2 and 3.

### Soundness
3

### Presentation
3

### Contribution
3
