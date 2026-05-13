# GC4NC: A Benchmark Framework for Graph Condensation on Node Classification with New Insights

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Graph condensation (GC) is an emerging technique designed to learn a significantly smaller graph that retains the essential information of the original graph. This condensed graph has shown promise in accelerating graph neural networks while preserving performance comparable to those achieved with the original, larger graphs. 
Additionally, this technique facilitates downstream applications like neural architecture search and deepens our understanding of redundancies in large graphs. 
Despite the rapid development of GC methods, particularly for node classification, a unified evaluation framework is still lacking to systematically compare different GC methods or clarify key design choices for improving their effectiveness. 
To bridge these gaps, we introduce \textbf{GC4NC}, a comprehensive framework for evaluating diverse GC methods on node classification across multiple dimensions including performance, efficiency,  privacy preservation, 
denoising ability, NAS effectiveness, and transferability.  
Our systematic evaluation offers novel insights into how condensed graphs behave and the critical design choices that drive their success. These findings pave the way for future advancements in GC methods, enhancing both performance and expanding their real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper establishes a comprehensive benchmark framework for evaluating GC methods across multiple dimensions including performance, privacy preservation, denoising ability, scalability, and NAS effectiveness. The authors present a novel evaluation scheme that integrates a variety of metrics to assess the efficacy and robustness of GC methods under different operational scenarios.

### Strengths
1. The framework, GC4NC, provides a standardized protocol that allows for the fair comparison of various GC methods on node classification across multiple critical dimensions such as performance, scalability, transferability. This systematic approach to evaluation is both comprehensive.
2. By being the first to systematically benchmark privacy preservation and denoising capabilities across various GC methods, the paper provides valuable insights that could lead to the development of more robust and privacy-aware graph processing techniques.
3. The manuscript is well-written with a logical flow that systematically presents the research questions, methodology, experimental setup, and findings.

### Weaknesses
1. The authors have adopted a fair evaluation protocol that includes training a 2-layer GCN with 256 hidden units on the reduced graph. While this setup might seem standardized, it could fail to represent the true predictive performance of the GCN model, as different hyperparameters such as the number of layers, dropout, and hidden units can significantly impact the node classification results on different datasets.

   In light of this, it is recommended that the authors consider adjusting the hyperparameters based on more generalized settings, as detailed in Table A3 from [1], to ensure that the evaluation of the GC methods can be reliably generalized across different graph types and setups. 

   [1] GC-Bench: An Open and Unified Benchmark for Graph Condensation. 

2. The paper addresses privacy preservation as one of the evaluation metrics for GC methods. However, the methods utilized to evaluate privacy do not seem to cover a broad spectrum of attack scenarios. This limitation might restrict the applicability of the results to real-world conditions, where adversarial attacks can be far more sophisticated and complex.

### Questions
Can the authors provide additional insights or results on how varying these parameters (such as the number of layers, dropout rates, and hidden units) might affect the outcomes of GCN models on both the whole and the condensed graphs?

### Soundness
3

### Presentation
3

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
In this paper, the authors propose a benchmark for graph condensation, i.e., compressing a large graph into a much smaller graph while preserving valuable information. Specifically, the proposed benchmark covers many aspects, such as unified evaluation protocols, efficiency, privacy preservation, denoising abilities, transferability, application to neural architecture search (NAS), etc. Many graph condensation methods are compared, and some insights for graph condensation are also observed.

### Strengths
1.	The proposed benchmark compares graph condensation methods from many aspects besides predictive accuracy.   
2.	The paper is well-written and easy to follow in general.   
3.	Source codes are available to evaluate the effectiveness of the benchmark.

### Weaknesses
1.	My major concern is how significant the proposed benchmark contributes to the graph machine learning community. Specifically, as explained in the paper, there are some earlier or concurrent works for graph benchmarking. As shown in Table 6 in the Appendix, these benchmarks seem to have their own advantages, e.g., this paper claims it has compared more methods, GC-Bench has considerably more datasets and broad tasks, and GCondenser has features such as continual learning and impact of validators, etc. The paper claims their unique advantages include comparing robustness and privacy preservation. However, the paper does not provide sufficient explanations for why these two factors are most important or challenging for graph condensation.  
2.	As a benchmark, I would also encourage the authors to provide more usage information, e.g., if users would like to add a new dataset, implement their own method and compare with baselines, propose a new setting, etc., how they could use the proposed method, and what are some potential difficulties, etc.   
3.	As I am not particularly familiar with graph condensation, it would also be valuable if the authors could discuss how this benchmark and the discovered insights could benefit general graph machine learning researchers.

### Questions
See Weaknesses above

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
3

### Summary
This paper has introduced a framework, GC4NC, for testing graph condensation (GC) methods on node classification from various aspects. The insights they reported include that 1) trajectory matching methods generally obtain better results, 2) some methods can preserve privacy while keeping condensation ratio, 3) GC methods demonstrate their denoising ability against structural noise, and so on. The authors have shared their anonymous code in which the results in the paper are reproducible.

### Strengths
1. The categorizations of existing GC methods are well summarized. Also, an evaluation protocol and design choices are well-structured, e.g., structure-free vs. structure-based and graph property preservation. 
2. This paper provides a framework in which researchers and developers can test various GC methods in a unified setting. On the framework, the authors conducted comprehensive experiments with 15+ methods on 7 datasets. 
3. The authors discuss 11 observations in total through the experiments from various aspects. While each observation is relatively shallow, the observations are helpful for the community.

### Weaknesses
1. While the paper provides experimental results from various aspects, some descriptions are insufficiently explained and insights are shallow. For example,
    1. In lines 288-291, what factors of the datasets affect the performance? Why does Averaging achieve the best performance on Yelp? Why do Arxiv and Reddit have significant room for improvement? 
    2. In lines 350 and 351, the paper describes “GC methods can still perform well when the Instance Per Class (IPC) is as low as 1” but I found the significant drops of most methods at the leftmost plots in Figure 3. 
2. It is hard to see the legends and characters in all figures.
    1. Figure 1 requires an effort to understand the correspondence between plots and methods. 
    2. In Figure 2, the legend overlaps the bar plots. 
    3. In Figures 3, 4, and 5, characters are very small.

### Questions
Can you clarify unclear points I raised in the Weakness section?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents GC4NC, a benchmark for evaluating graph condensation methods on node classification. GC4NC assesses performance, efficiency, privacy, denoising, NAS effectiveness, and transferability, revealing key insights into design choices like trajectory matching and structural synthesis. It provides a robust benchmark to support fair comparisons and future advancements in GC methods.

### Strengths
1. The paper addresses a significant gap by providing a unified and multi-dimensional evaluation protocol. It allows systematic comparisons and insights into GC methods, including under-explored aspects such as privacy preservation and denoising ability.
2. The findings offer novel insights, such as the trade-offs between GC performance and efficiency, the privacy benefits of GC methods, and how certain GC methods enable better transferability across GNN architectures.
3. The paper promises an open-source codebase for GC4NC, promoting reproducibility and further experimentation.

### Weaknesses
1. From Table 6, in comparison with the existing works GCondenser [1] and GC-Bench [2], this paper's GC4NC is less comprehensive than GC-Bench. The advantage of GC4NC over GC-Bench lies in its inclusion of more Coreset & Sparsification methods; however, this is not a primary research focus for graph condensation.
2. Insufficient discussion of graph-level methods. Numerous studies focus on graph-level datasets, and it is essential to incorporate these works into the comparison framework.
3. Insufficient inclusion of representative baselines. The paper lacks comparisons with several key methods, such as Mirage [3]. As GC4NC categorizes methods from a structural perspective, Mirage tackles the problem using computation trees. Omitting Mirage may limit the comprehensiveness of this work.
4. The paper categorizes the evaluated methods as structure-based and structure-free, which contrasts with the more detailed classifications typically seen in recent surveys. While this choice may emphasize the importance of structural elements, structure is just one component of an effective condensed graph. This simplified categorization overlooks a deeper examination of key technical strategies in graph condensation, such as gradient matching, trajectory matching, and distribution matching, that are essential for a comprehensive understanding and meaningful comparison of these methods.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
