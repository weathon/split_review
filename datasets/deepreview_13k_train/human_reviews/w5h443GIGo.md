# On the Convergence of Symbolic Pattern Forests and Silhouette Coefficients for Robust Time Series Clustering

- Decision: Reject
- Scores: 3, 1, 3

## Abstract
Clustering algorithms are fundamental to data mining, serving dual roles as exploratory tools and preprocessing steps for advanced analytics. A persistent challenge in this domain is determining the optimal number of clusters, particularly for time series data where prevalent algorithms like k-means and k-shape require a priori knowledge of cluster quantity. This paper presents the first approach to time series clustering that does not require prior specification of cluster numbers. We introduce a novel extension of the Symbolic Pattern Forest (SPF) algorithm that automatically optimizes the number of clusters for time series datasets. Our method integrates SPF for cluster generation with the Silhouette Coefficient, computed on a two-stage vector representation: first transforming time series into Symbolic Aggregate approXimation (SAX) representations, then deriving both bag-of-words and TF-IDF vectors. Rigorous evaluation on diverse datasets from the UCR archive demonstrates that our approach significantly outperforms traditional baseline methods. This work contributes to the field of time series analysis by providing a truly unsupervised, data-driven approach to clustering, with potential impacts across various temporal data mining applications where the underlying number of clusters is unknown or variable.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes SPF, a methodology that identifies the number of clusters for time-series data, often a critical parameter for subsequent routines and clustering methods. The idea combines concepts such as SAX, TF-IDF vectors over SAX representations and relies on the Silhouette coefficients to calibrate the number of clusters. Experimental results on several UCR datasets demonstrate the potential of this solution.

### Strengths
S1. Timely and important problem especially due to the rise of IoT applications and the need for unsupervised data exploration
S2. Simply and intuitive ideas
S3. Results support the overall claims in the paper

### Weaknesses
W1. Lack of technical depth

The paper combines existing ideas for solving this problem. Therefore, the technical depth is low, even though the combination of these ideas might be novel. The novelty of combining SAX, TF-IDF, and Silhouette is not sufficiently justified with a theoretical framework. The paper lacks a deeper analysis of why this combination is more effective than other possible combinations or individual methods. The mathematical formulations are not rigorous enough to demonstrate the specific advantages of the proposed method over existing techniques. A more detailed explanation of the underlying mathematical principles and their connection to the empirical results is needed.

W2. Unclear how different methods/distances can be compared

It's unclear how this comparison is meaningful when we need to compare methods relying on different distances. The paper does not clearly articulate how such distances affect the results and it mainly shows results for SAX variants (so inherently for euclidean distance). The paper does not discuss the implications of using different distance metrics within the TF-IDF framework. It is not clear how the choice of distance metric impacts the resulting cluster structures and the overall performance of the method. A more thorough analysis of the sensitivity of the method to different distance metrics is required.

W3. Missing potential baselines

Simple baselines, like assign the objective functions of k-means like algorithms are missing. Also there are tons of variants for internal clusteirng validation. Why Silhouette ? The paper does not justify why the Silhouette coefficient was chosen over other internal clustering validation metrics such as the Davies-Bouldin index or the Calinski-Harabasz index. A comparative analysis of these metrics and a clear rationale for selecting the Silhouette coefficient is missing. Furthermore, the paper lacks a comparison against simpler baselines that directly optimize clustering objectives, such as the k-means objective function, which could provide a more robust evaluation of the proposed method's performance.

W4. Duplicate references or wrong references

Many references are duplicates. Other references does not exist

duplicates
Xiaosheng Li, Jessica Lin, and Liang Zhao. Linear time complexity time series clustering with
symbolic pattern forest. In IJCAI, 2019a.
Xiaosheng Li, Jessica Lin, and Liang Zhao. Linear time complexity time series clustering with
symbolic pattern forest. IJCAI, 2019b.

duplicates
Jaewon Yang and Jure Leskovec. Patterns of temporal variation in online media. In Proceedings of
the Fourth ACM International Conference on Web Search and Data Mining, 2011a.
Jaewon Yang and Jure Leskovec. Patterns of temporal variation in online media. In Proceedings of
the fourth ACM international conference on Web search and data mining, pp. 177–186, 2011b.

it's wrong
John Paparrizos, Paul Boniol, Themis Palpanas, Ruey S Tsay, Aaron Elmore, and Michael J
Franklin. Fast and exact time series motif and discord discovery in trillions of data points. The
VLDB Journal, 31:1079–1101, 2022.

### Questions
W1. Lack of technical depth

The paper combines existing ideas for solving this problem. Therefore, the technical depth is low, even though the combination of these ideas might be novel.

W2. Unclear how different methods/distances can be compared

It's unclear how this comparison is meaningful when we need to compare methods relying on different distances. The paper does not clearly articulate how such distances affect the results and it mainly shows results for SAX variants (so inherently for euclidean distance)

W3. Missing potential baselines

Simple baselines, like assign the objective functions of k-means like algorithms are missing. Also there are tons of variants for internal clusteirng validation. Why Silhouette ?

W4. Duplicate references or wrong references

Many references are duplicates. Other references does not exist

duplicates
Xiaosheng Li, Jessica Lin, and Liang Zhao. Linear time complexity time series clustering with
symbolic pattern forest. In IJCAI, 2019a.
Xiaosheng Li, Jessica Lin, and Liang Zhao. Linear time complexity time series clustering with
symbolic pattern forest. IJCAI, 2019b.

duplicates
Jaewon Yang and Jure Leskovec. Patterns of temporal variation in online media. In Proceedings of
the Fourth ACM International Conference on Web Search and Data Mining, 2011a.
Jaewon Yang and Jure Leskovec. Patterns of temporal variation in online media. In Proceedings of
the fourth ACM international conference on Web search and data mining, pp. 177–186, 2011b.

it's wrong
John Paparrizos, Paul Boniol, Themis Palpanas, Ruey S Tsay, Aaron Elmore, and Michael J
Franklin. Fast and exact time series motif and discord discovery in trillions of data points. The
VLDB Journal, 31:1079–1101, 2022.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The manuscript presents an extension of the symbolic pattern forest (SPF) algorithm for clustering of time series data. Using bag-of-words on the symbolic representation, TF-IDF vectors are constructed. The best clustering is selected as the one that maximises the silhouette coefficient (SC).

### Strengths
S1. The paper addresses the relevant problem of automatically determining the number of clusters.
S2. The empirical evaluation makes use of a large number of benchmarking datasets.

### Weaknesses
W1. The method assumes that silhouette coefficient is a suitable metric for finding the best number of clusters, without justifying this choice. This is a major concern as the silhouette coefficient considers (Euclidean) distance to cluster centres, which is not aligned with the clustering objective of the SPF method. The paper should provide justification for using the silhouette coefficient, or discuss potential limitations of this choice given the SPF method's clustering approach. Moreover, the silhouette coefficient is a well-known metric, so it is unclear what the novelty should be.
W2. The empirical evaluation does not consider the SPF method, but only weak baselines constructed from the proposed method, meaning that the empirical evaluation does not allow assessment of the performance of the proposed method with respect to state of the art. It is important to compare directly to SPF in the experiments, in order to demonstrate improvement over state of the art.
W3. The empirical evaluation only considers performance metrics accuracy and near-miss-rate, different from other work in the field, and in the SPF paper (e.g. NMI), making it impossible to compare with those works directly.
W4. The discussion of related work is overly brief, and fails to present clear assessment of the suitability of existing methods and metrics. E.g. Davies-Bouldin Index and its perceived suitability for the task. Also, there is a large body of work on similarity assessment of time series or clustering of time series, e.g. Keogh et al 2005, Rakthanmanon  et al 2012, Paparrizos et al 2015. The paper should discuss these, and explain differences and similarities with the proposed method.
W5. On the other hand, references UTSAD and STGAT seem out of context, as they do not address clustering of time series. The paper should clarify the relevance of UTSAD and STGAT to the proposed work, or remove these references if they are indeed not directly related.
W6. The paper contains several redundant sections, such as the description of SAX.
W7. There are some minor issues, such that Li et al 2019 appears twice in the references, there is a typesetting error in the definition of pi_i(T_i).

### Questions
N/A

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The submission proposes an extension to the SPF algorithm, a clustering approach for clustering time series with linear complexity. The extension allows for the automatic determination of the number of clusters. It is done by performing optimization on the silhouette score using either Bag of Words or TF-IDF.

### Strengths
(S1) Incorporating BoW and TF-IDF with the concepts of the SPF algorithm sounds like a very sensible approach. Both are a good choice for term-based similarity evaluation and are still commonly used in other settings.

(S2) Aside from minor issues, the submission is well-written and easily understandable while providing an extensive overview of the formulas related to the problem.

(S3) The problem setting is significant as k-estimation is a significant part of clustering in general, which also applies to the setting of time series clustering. The usage of SPF is well-founded due to its low complexity. Introducing k-estimation to the approach helps mitigate one of its weaknesses.

### Weaknesses
 (W1) Novelty: The abstract of the submission makes the claim that there are no time series clustering methods capable of working without the specification of cluster number k. However, such methods exist already:

a) “Spectral Clustering for Time Series” by Fei Wang and Changshui Zhang (2005) is able to discover the optimal number of clusters based on the eigenstructure using a threshold on the value of the eigenvalues.
b) “Clustering Time Series with Hidden Markov Models and Dynamic Time Warping” by Tim Oates et. al. (1999) also provides a way to estimate the number of clusters based on Dynamic Time Warping. However, even if the submission is not the only method that does k-estimation on time series, it is still a valid and useful direction. It also appears to be the only method that does so for the Symbolic Pattern Forest algorithm.
c) The paper “Trendlets: A novel probabilistic representational structures for clustering the time series data” by Johnpaul C I et al. (2020) uses the Silhouette Score for cluster number analysis for time series as well, though it does so based on hierarchical clustering methods. This paper should be explicitly covered in related work or even a competitor.

(W2) Despite TF-IDF being considered the better of the two proposed strategies, there is no actual description of the performance metrics outside of the graph and the overall relative performance value. Similarly, near misses should be added to the text for BoW. The results of both BoW and TF-IDF are the same in the Tables in the supplementary files, though Figure 1 claims that TF-IDF performed slightly better. It is unclear what metric is used to determine the relative performance, and the lack of statistical significance testing makes it difficult to assess the actual differences between the two approaches. The specific values for the performance metrics should be included in the main text, not just in supplementary material.

(W3) As the method works by optimizing the silhouette score, both the values for the score and the actual clustering performance with the given parameters should be indicated. While the cluster numbers match, the detected clusters may not necessarily correspond to the actual ground truth clusters, which could further mean that different cluster numbers may lead to a better performance. Furthermore, an analysis of the stability of the parameters should have been performed, especially as the method has multiple parameters, which themselves include an upper and lower bound. Additionally, an intuition behind choosing the parameters should be given if they strongly affect the performance. The paper should also include a discussion on the sensitivity of the silhouette score to different parameter settings and how this impacts the final clustering results. It's also not clear if the silhouette score is the best metric for this task, and other metrics should be considered.

(W4) Regarding the actual experiment, a better analysis of the behavior should be done, considering under what conditions the k-estimation of each of the three approaches failed and whether or not a reason behind it could be established. The section on Relative Improvement is redundant as it only recontextualizes prior results, and the space could be used to do a more in-depth result analysis instead. Similarly, the remaining 2 pages could have been used for this. The paper should include a more detailed analysis of the failure cases, including specific examples of datasets where the proposed method performs poorly and a discussion of the reasons for these failures. This would provide a more comprehensive understanding of the method's limitations.

(W6) Neither the parameter w nor the alpha ranges seem to be specified anywhere. The code is unavailable, though it should be possible to reimplement given the information provided. Still, this hampers the reproducibility of the results. The lack of specific parameter values and the absence of code make it difficult to reproduce the results and validate the claims made in the paper. This is a significant issue that needs to be addressed.

(W7) There should be citations for TF-IDF and BoW. Other papers also do not consistently do it, so it is not a major issue. Nonetheless, it would have been better if it had been done. Furthermore, UCI should be cited upon first mention outside of the abstract, not just at a later point.

Minor Issues:
* Linear time complexity time series clustering with symbolic pattern forest by Li et. al., is cited twice as 2019a and 2019b despite referring to the same paper 
* The formatting appears to be broken for lists, as they are just written in a line without comma separation (see line 291 and lines 314-315) 
* A similar issue happened with the variables for the optimization problem, as they are also not properly separated in line 305
* The subscript on several equations appears to be broken (see (22)/319 and (23)/321)
* The near miss metric should probably be more dynamic based on the ground truth cluster number, as claiming 2 clusters for a 3-cluster setting seems more problematic than claiming 70 for 71 true clusters. The chosen datasets generally only have a few clusters, so the current definition isn’t problematic for the submission. It may be relevant for the extension to the full UCI database, however. 
* The formulation for Near Misses, as currently given, would also include all correctly determined cluster counts but does not do so in the evaluation.

### Questions
(Q1) How would you modify the paper to address the issues regarding related work? How does the proposed method compare to other k-estimation approaches on time series data?

(Q2) What effect do the properties of the chosen UCI datasets have on the performance of the k-estimation using the proposed technique, and how does the clustering performance change on them depending on the chosen k? Is the performance of the SPF algorithm with the ground truth k always the best one, or could other parametrizations outperform it?

(Q3) How impactful are the parameters of the proposed method?

(Q4) Is there any advantage to using BoW over TF-IDF (or the other way around)?

### Soundness
2

### Presentation
2

### Contribution
2
