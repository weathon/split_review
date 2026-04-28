# Rapid Selection and Ordering of In-Context Demonstrations via Prompt Embedding Clustering

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
While Large Language Models (LLMs) excel at in-context learning (ICL) using just a few demonstrations, their performances are sensitive to demonstration orders. The reasons behind this sensitivity remain poorly understood. In this paper, we investigate the prompt embedding space to bridge the gap between the order sensitivity of ICL with inner workings of decoder-only LLMs, uncovering the clustering property: prompts sharing the first and last demonstrations have closer embeddings, with first-demonstration clustering usually being stronger in practice. We explain this property through extensive theoretical analyses and empirical evidences. Our finding suggests that the positional encoding and the causal attention mask are key contributors to the clustering phenomenon. Leveraging this clustering insight, we introduce Cluster-based Search, a novel method that accelerates the selection and ordering of demonstrations in self-adaptive ICL settings. Our approach substantially decreases the time complexity from factorial to quadratic, saving 92% to nearly 100% execution time while maintaining comparable performance to exhaustive search.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors investigate the few-shot setting and the order of given demonstrations/examples in the prompt. Analyzing the last hidden state of the last layer of decoder-only transformers, they study the clustering property, which prompts sharing the first and last demonstration. Experiments are conducted in two domains: classification and reasoning. Each is divided into two tasks, and the classification sub-tasks are further modified into symbolic ones.
The explanation proposed is that this property depends highly on the causal attention mask and the positional encoding. The first demonstration clustering depends on the causal attention mask. However, the last demonstration clustering depends on a more complex interplay of the causal attention mask and the positional encoding.
Following their findings, the authors propose a selection and ordering method based on the uncovered clusters. Experiments are conducted using their methods with an already-used entropy-based search. They compare their methods with an oracle and unmodified entropy methods. Their findings show that the clustering-based method while suffering a slight drop in performance, their method is more than 90% faster.

### Strengths
* Running large language models is costly, and few-shot in-context learning is a common approach to alleviate the cost. The proposed method is simple and greatly reduces search time, making a practical contribution. 
* Even though the theoretical assumptions are strong, their partial derivative analysis is original and clearly advocates for the clustering property.
* The cluster-based search proposed by the authors is well explained.

### Weaknesses
 * Too little evidence of clustering is given on the classification tasks, and clustering is unclear on The 2D projection (Figure 1, Figure 4). The visual clustering in the 2D projections is not compelling, especially for the classification tasks, where the separation between clusters is not distinct. It's difficult to ascertain if the observed patterns are genuine clusters or artifacts of the dimensionality reduction technique. A quantitative measure of cluster quality, such as silhouette scores or Davies-Bouldin index, would be beneficial to support the visual claims.
* Few experiments have been done varying the number of demonstrations and the pool size; it would be really beneficial to give some insight on the scaling possibility of the method. The experiments primarily focus on a limited number of demonstrations and pool sizes. It's unclear how the proposed method scales with larger demonstration pools and varying numbers of demonstrations. Specifically, the impact on clustering quality and the effectiveness of the selection method with a larger pool size and more demonstrations should be investigated. This is crucial for understanding the practical applicability of the method in real-world scenarios.
 * A more thorough analysis of the results would be appreciated to confirm the findings, for example: Do the prompts sharing a close representation share similar scores? (what is the standard deviation ?) How does the performance change with the number of intermediate demonstrations? ( Some insights are given, but more results would greatly improve the demonstration). The analysis lacks a detailed examination of the relationship between the similarity of prompt representations and their corresponding performance. It would be valuable to see a correlation analysis between the distance in the representation space and the performance scores. Furthermore, the impact of varying the number of intermediate demonstrations on the overall performance needs a more in-depth analysis, including statistical significance tests.
* Not enough selection methods are considered for comparison in terms of time and scores. The comparison is primarily limited to an entropy-based search and an oracle method. It would be beneficial to compare the proposed method with other selection techniques, such as those based on diversity or uncertainty, to provide a more comprehensive evaluation of its effectiveness. This would help to contextualize the performance of the proposed method relative to existing approaches.
* A table showing time performance and or gap with other methods is needed. The paper lacks a clear quantitative comparison of the time performance of the proposed method with other selection methods. A table showing the actual time taken by each method, along with the corresponding performance scores, would be essential for evaluating the practical benefits of the proposed approach.

### Questions
* How does a variant of Figure 3b with demonstrations instead of chunks of text compare?
* Do the prompts that share a close representation get similar scores? (what is the standard deviation ?)
* How does the performance change with the number of intermediate demonstrations? ( Some insights are given, but more results would significantly improve the demonstration)

### Soundness
2

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
The paper explores the issue of demonstration order sensitivity in large language models (LLMs) during in-context learning (ICL) and uncovers a clustering phenomenon in the embedding space, where prompts with the same first and last demonstrations tend to cluster together. Through theoretical analysis and empirical evidence, the paper identifies that this clustering effect stems from the interaction of causal attention masks and positional encoding. Moreover, they propose a "Cluster-based Search" method that significantly reduces the computational complexity of selecting and ordering demonstrations while maintaining high model performance.

### Strengths
1. Clear Argumentation: The paper is well-structured, with clear explanations that make the objectives and contributions easy to follow.
2. Robust Proofs: The theoretical analysis is thorough, supporting the proposed mechanisms in in-context learning.
3. Comprehensive Experiments: The experiments are detailed and varied, effectively demonstrating the method’s efficacy across multiple tasks.

### Weaknesses
1. The models used in this study seem somewhat outdated. Models with the equivalent size should include newer architectures, such as LLaMA 3, Phi, or similar. Why were these not used? The choice of older models limits the generalizability of the findings to current state-of-the-art LLMs. Specifically, the attention mechanisms and pre-training data of models like LLaMA 3 and Phi could interact differently with the proposed clustering phenomenon, potentially invalidating some of the conclusions drawn from older architectures.
2. The datasets and tasks included in the study are limited. For instance, why is there no mathematical task such as GSM8k included in the paper? The lack of mathematical reasoning tasks is a significant omission, as these tasks often reveal different aspects of LLM capabilities and sensitivities to prompt ordering. The current selection of tasks might not fully capture the breadth of scenarios where the proposed method could be applied or where its limitations might become apparent. The absence of tasks requiring complex reasoning limits the scope of the paper's claims.
3. While the authors highlight the importance of the first and last demonstrations in ICL, the figures in the paper suggest that the first demonstration may be particularly or even most significant. However, in the cluster-based method, the authors did not conduct an ablation study that uses only the first or only the last demonstration in clustering to analyze the contributions of the first and last demonstrations independently. This lack of ablation makes it difficult to assess the relative importance of the first and last demonstrations, and whether the method could be simplified by focusing solely on the first demonstration.

### Questions
My main concerns have been listed above. I look forward to the authors' response and am willing to reopen and adjust the score upward.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studied the ordering effects of demonstrations in in-context learning (ICL) and claimed that the first and last demonstrations are the most crucial ones for effective demonstrations using both empirical and theoretical analyses. Based on this observation, this paper proposed a cluster-based search method to find out effective demonstration orders (considering only the first and last demonstrations instead of all demonstrations), which will not suffer from the efficiency issue in Exhaustive Search. The experiments showed that the proposed method achieve small drop in accuracy but significant improvement in efficiency.

### Strengths
* The proposed idea of cluster-based search is simple yet effective for ICL.
* The performance of the proposed method, especially efficiency improvement, is very promising.

### Weaknesses
 * Some claims are not well supported by the empirical analyses. The cluster structure of GPT-2 model in Figure 1 seems unclear, compared to the other two LLMs. Figure 3 (a) shows that the clusters also share the same second demonstrations with high percentage, and for the two bottom figures, the percentage of sharing the same second demonstrations is even higher than the percentage of sharing the same last demonstrations. These observations may be conflict with the main claim of this work. Also, the analyses about the last demonstration seem to be less convincing, e.g., lines 340-346.
* The theoretical analyses are counter intuitive. According to Prop. 4.1, the embedding of the transformer layers will eventially the same if two promopts share the same first input token. I cannot understand this claim in the proof also, in which the authors mentioned that "if causal attention mask is applied, then x_1(t) = x'_1(t) for all t >= 0." I am not sure why this assumption holds. Intuitively, if this proposition holds, I may infer that only the first demonstration will affect the performance and the last demonstration will not matter too much, which is different from the authors' claim.
* More comprehensive experiments are required. In Table 1, the case of Random demostrations is not included. It would be useful to also compare with Random ordering as in Table 2. Also, they authors used k=4 in the experiments, it might be also important to evaluate larger k values, e.g., 10 or 20. The main claim of this paper is that the demonstrations in the middle are not very important to the performance of ICL, but using only a few demonstrations in the middle (as in the experiments) may not be as convincing as using many demonstrations in the middle.

### Questions
Please refer to my concerns in the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
