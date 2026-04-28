# Temporally coherent visualisation of time-dependent data

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Dimension reduction algorithms aim to embed high-dimensional datasets into a low-dimensional space in such a way that important structural properties, such as clusters and manifolds, are preserved. Most such methods are designed for static data, and naively applying them to time-dependent data can lead to unstable embeddings which do not meaningfully capture the temporal evolution of the data. In this paper, we propose a new variant of the t-SNE algorithm for time-dependent data, TC-tSNE (Temporally Coherent t-SNE) in which an extra term is added to the cost function to promote temporal coherence: the notion that a data point which has a similar position in two time frames should be embedded to similar positions at those times. Importantly, this notion captures temporal similarities over the entire time domain and can therefore capture long-range temporal patterns, not just local ones. We demonstrate the effectiveness of our method for visualising dynamic network embedding, and we evaluate our method on six benchmark datasets using a collection of metrics, which capture the structural quality and the temporal coherence of the embeddings. We compare our method with existing dynamic visualisation algorithms and find that it performs competitively.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes, TC-tSNE, a new dimensionality reduction for visualizing temporal datasets. TC-tSNE adds a temporal coherency term on top of t-SNE. Experimental results show that the method delivers more coherent visualizations.

### Strengths
(S1) The paper targets the important problem of the visualization of temporal datasets.

(S2) The proposed local temporal coherence can apply to a neighbour embedding algorithm.

(S3) The experiments show that the method has a comparative performance with previous solutions.

### Weaknesses
 (W1) Experiments: One of the paper's weakest points is the lack of proper evaluation of synthetic datasets exposing a diverse range of patterns. In particular, it is not clear how the method works on datasets with periodic changes or anomalies. The experiments should include datasets with clear temporal patterns, such as oscillating or cyclical data, to properly assess the method's ability to capture these dynamics. Furthermore, the method's robustness to outliers and abrupt changes in the data trajectory needs to be evaluated using synthetic datasets with controlled anomalies.

(W2) The experiments in Figure 4 show no significant advantage compared to previous methods. For instance in the sort dataset TC-tSNE fairs much lower than competitors in terms of spatial consistency. The spatial consistency metric should be analyzed more carefully, and the authors should provide a more detailed explanation of why their method performs poorly in this specific case. It is important to understand the limitations of the proposed approach and to identify the types of datasets where it might not be suitable.

(W3) There are no experiments showing the impact of hyperparameters ($\lambda$ for instance) on the results. Is the parameter $\lambda$ to be tuned for any dataset or does there exist a good configuration that holds with different data? A sensitivity analysis of the hyperparameter $\lambda$ is crucial to understand its influence on the resulting embeddings. The authors should investigate how different values of $\lambda$ affect the temporal coherence and spatial consistency of the visualizations. This analysis should include a range of values for $\lambda$ and should be performed on different datasets to determine if there is a generalizable configuration.

(W4) Ìn line 388 other dimensionality reduction techniques are used to show the results in Figure 1. However, since TC-tSNE is already a dimensionality reduction method, why not use that directly? It is unclear why the authors use other dimensionality reduction techniques to visualize the results of TC-tSNE. If TC-tSNE is a dimensionality reduction technique, it should be used directly to visualize the data. The use of other techniques introduces an unnecessary step and makes it difficult to assess the performance of TC-tSNE.

(W5) Clarity: The paper should report how to compute the evaluation metrics and their meaning. The evaluation metrics used in the paper should be clearly defined, and their meaning should be explained. This is crucial for the reproducibility of the results and for the reader to understand the performance of the proposed method.

(W6) The paper states that they report the average of four metrics. How can you average across different metrics? Averaging metrics with different scales and meanings is not a sound practice. The authors should justify why they average these metrics and should consider using alternative methods for combining them, such as a weighted average or a composite score.

(W7) The paper claims that its methodology generally applies to different embeddings, yet it shows the applications only with TSNE. How can it be applied to UMAP? Some experiments in this regard should be shown. The authors should provide experimental results with other embedding techniques, such as UMAP, to support their claim that the method is generally applicable. This would demonstrate the versatility of the proposed approach and would make the paper more convincing.

(W8) The paper proposes a notion of temporal coherence that considers all timestamps t using Eq. 3. However, this definition is problematic and sensitive to outliers and fluctuating behaviours. In particular, if the point at some time t deviates substantially from another at time t+k, then the temporal coherence would try to smoothen these points far apart, but among other time stamps instead the opposite behaviour can be observed. The definition of temporal coherence should be revisited to address the sensitivity to outliers and fluctuating behaviors. The current definition might lead to undesirable smoothing of the data trajectory, especially when there are abrupt changes or anomalies.

(W9) Building on W3. While it is clear the motivation that a single timestamp is not sufficient, it is not clear why an unweighted sum of coherence across timestamps is sound. Wouldn't be better to discount points further in time from t? Why not consider a weighted sum? The authors should justify why they use an unweighted sum of coherence across timestamps. A weighted sum, where points further in time are discounted, might be more appropriate for many applications. The authors should explore this alternative and provide a rationale for their choice.

### Questions
As stated in the weak points, there are several clarification points, such as (W4,W6,W7,W8) as well as additional missing experiments (W1, W2, W3, W7, W9) that I would like to see.

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
5

### Summary
To address the current lack of effective dimension reduction and visualization methods for time-dependent data, this paper proposes TC-tSNE (Temporally Coherent t-SNE), which adds an extra term to the cost function to promote temporal coherence. The proposed method can capture long-term temporal patterns while maintaining good spatial embedding quality.

### Strengths
1.The paper first introduces the importance of visualizing time-dependent data and the challenges it faces. It then clearly articulates the problem to be solved through a comprehensive review of previous methods. The writing is coherent and smooth, allowing readers to understand the significance of the work. 
2.The method description combines straightforward narration with complete mathematical derivation, presenting the proposed algorithm clearly. 
3.The effective use of visual images makes the experimental results very intuitive.
4.In the comparison of visualization results, the proposed method demonstrates good temporal and spatial coherence. It better reflects the patterns of data changes compared to other visualization algorithms.

### Weaknesses
1.There are still some areas in the paper where the descriptions are unclear and may confuse readers. For example, in the formula shown in line 101, many variables (such as n, T, and λ) are not timely explained, with some variables only clarified in Section 3.1, while the parameter 𝜆 is not defined anywhere in the paper. Line 257 references equation (3.2), but this equation does not appear in the text. Additionally, which two papers are referred to in line 381 as "Both of the aforementioned papers"?
2.Although the experimental display in the paper is quite intuitive, it does not present any quantitative data. Currently, in Figure 4, it is unclear which hyperparameter was used for each data point in the experiments. The authors might consider using tables to present some important results, with the complete results provided in the appendix.
3.The experiments in the paper are insufficient. On one hand, the paper uses t-SNE as the spatial cost function and SNE as the temporal cost function. The rationale for this is that clustering may not be meaningful in the temporal domain, as explained in line 179. However, this claim lacks corresponding experimental evidence. Moreover, did the authors try using other cost functions? On the other hand, in line 259, it is stated that the proposed method can be easily plugged into accelerated algorithms; did the authors conduct related experiments?
4.Figure 3 presents the performance of other methods and aims to compare it with the performance of the proposed method shown in Figure 1. However, Figures 1 and 3 use different vertical scales, making it difficult to make a fair visual comparison.

### Questions
1.Line 111 describes the "Guided" method, but it does not analyze its limitations as done earlier in the text. Since this method does not solely guarantee short-term temporal coherence and does not significantly impact spatial quality like the "Global" method, what specific problems does the proposed method address in relation to the "Guided" method?
2.In line 394, the hyperparameters used in the TC-tSNE method are described. Were these hyperparameters selected based on experience or experiments?
3.The experimental results presented in Figure 4 are not convincing. For example, the performance of Global PCA appears to be similar to or even better than that of the proposed method, except on the fashion dataset.
4.Is there any open-source code available to replicate the experimental results in this paper to enhance credibility?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new variant of the t-SNE algorithm, called Temporally Coherent t-SNE (TC-tSNE), which aims to handle time-dependent data while maintaining spatial and temporal coherence. The goal is to allow stable embeddings that capture the temporal evolution of data points, which is a challenge for existing dimension reduction techniques like t-SNE and UMAP, designed for static data. TC-tSNE addresses this by adding a temporal coherence term to the cost function, ensuring that data points with similar positions at different time points remain close in the embedding space. The method is compared against several existing strategies across six benchmark datasets.

### Strengths
- The paper identifies the limitations of existing approaches for handling time-dependent data and presents a novel modification to t-SNE that explicitly promotes temporal coherence.
- The method can be plugged into any neighbor-embedding algorithm.

### Weaknesses
 - The method handles temporal and spatial coherence independently, which may limit its capacity to capture complex relationships between time and space. Specifically, the current formulation does not explicitly account for scenarios where the spatial relationships between points change over time, such as when two points swap positions. This independent treatment may lead to suboptimal embeddings when the temporal dynamics are closely intertwined with spatial changes.
- The current version does not explore a more robust treatment of seasonality, trends, or abrupt changes in time-series data. The method treats all time points equally, which may not be appropriate for data with periodic patterns or sudden shifts. For instance, a dataset with strong seasonal variations might benefit from a model that explicitly incorporates these patterns, rather than treating each time point as an independent snapshot. Similarly, the method's performance during abrupt changes in the data distribution is not explored, which could be a significant limitation in real-world applications.
- Rather than numerous visualizations, it would be helpful to provide only a few clear examples where TC-tSNE outperforms other methods with clear descriptions. Specifically, Figure 4 is difficult to interpret, and the authors make a weak claim that TC-tSNE "sometimes achieves the best temporal and spatial metrics and is never among the worst." The results should describe clearly and support the claims made in the paper. The current presentation of results makes it difficult to assess the true benefits of the proposed method.

### Questions
- How could the TC-tSNE algorithm be adapted to handle better important aspects of temporal data, such as seasonality? Would incorporating additional temporal regularization improve its performance?
- How does the algorithm perform when significant noise or irregularity exists in the time series? Are there mechanisms that could improve its robustness to such noise?
- The current approach applies to relatively moderate-sized datasets. How does the method scale for large-scale data where considering all possible pairs may not be feasible?

### Soundness
2

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
4

### Summary
Despite the prevalence of time-dependent data, temporal data visualization has received far less attention than static data visualization. This paper studies this important problem of temporal data visualization, and presents a new strategy for temporally coherent visualization of time-dependent data, which aims to achieve high temporal and spatial coherence simultaneously. The paper does a nice job of summarizing existing temporal data visualization paradigms and their limitations, and based on that, proposes a new strategy to learn low-dimensional time-evolving representations of the data with high structural and temporal coherence. Experimental results involving multiple datasets are provided, including the case study using the UASE network embeddings, which shows that the proposed method leads to an improved visualization of time-dependent data, compared to several existing temporal data visualization methods.

### Strengths
S1. This paper studies an important problem of visualizing time-dependent data. Despite the prevalence of time-dependent data, most works on data visualization have focused on static data, and visualization of time-dependent data has received much less attention comparatively. This work presents a new approach for this problem, which aims to achieve high temporal and spatial coherence simultaneously.

S2. The motivation and intuition of the proposed idea is simple and clear. The paper does a nice job of presenting an overview of existing strategies for temporal data visualization, which shows the limitations of existing paradigms, and how the proposed approach improves upon them.

S3. The case study using the UASE network embeddings demonstrates the improved visualization quality of the proposed method in comparison to the visualizations obtained with various existing approaches.

### Weaknesses
W1. Technical contributions of this work are somewhat limited. While this work presents a new approach different from existing temporal data visualization techniques, most of the technical heavy lifting of the proposed approach is done by a direct application of existing algorithms, namely, SNE and t-SNE, which makes the technical innovations of this work limited.

W2. Quantitative performance of the proposed TC-tSNE method is not particularly better than existing methods, and lacks an in-depth analysis. While the case study in Section 5 shows the benefits of the proposed method, it is done only for one dataset. In quantitative evaluation (Section 6), which involves six datasets, the proposed approach does not outperform existing approaches in many cases, in terms of the spatial and temporal metrics used in the paper. Further, the result analysis given in the paper is too brief (“sometimes achieving the best temporal and spatial metrics, and is never among the worst”), which does not provide much insight into the obtained results; a more in-depth discussion and analysis would be needed.

W3. The paper would need to provide further discussion/analysis and more details, including the following.
* Complexity analysis of the proposed algorithm
* Ablation studies of the proposed method (e.g., performance using t-SNE objective (instead of SNE objective) for the time dimension)
* description and statistics of the datasets used for experiments
* explanation of the evaluation metrics (what they aim to measure, their equations, whether higher values are better, etc)

### Questions
Please refer to the comments above for suggestions.

### Soundness
2

### Presentation
3

### Contribution
2
