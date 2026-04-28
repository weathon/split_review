# Thetan Berserker: Fast and Stochastic Distance-based Clustering

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
Clustering is a challenging NP-hard problem. Polynomial approximations are of paramount importance for identifying intriguing hidden representations of data at reasonable execution times. In this work, we propose a novel clustering algorithm called Thetan Berserker (TB). TB is a centroid-based clustering method controlled by a single distance parameter. TB revitalizes an old family of sequential algorithms which are adored for their speed but are known to be order sensitive. In addition, TB enables widely used algorithms such as KMeans and DBSCAN by improving their initial conditions. Theoretical aspects are provided in detail along with extensive comparisons and benchmarks. Examples of real world applications are provided using publicly available data of different dimensionalities. A wide range of performance boosts in clustering accuracy, memory usage, and runtime are reported. By dramatically reducing clustering ambiguities, while staying at incredibly low complexity, TB creates a new standard for clustering.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce Thetan Berserker, a centroid- and distance-based clustering method that is based on a sequential approach, Thetan Sequential (TS). The method is tested on low-dimensional data and as a way to find superpixels in images.

### Strengths
S1) The approach is straightforward and easy to follow.

S2) Time and memory efficient regarding the experiments performed on low-dimensional data.

S3) The proposed method depends on one hyperparameter only.

### Weaknesses
W1) Experimental evaluation is not sufficient

a) The main claim of the paper highlights speed and efficiency. However, the experiments are performed only on low-dimensional data. What does the performance look like on high-dimensional data? Please also include competitors aimed at speed, e.g., [0,1]. Furthermore, for comparing runtimes between different methods, they should be implemented in the same language as python implementations are per se slower than such in C or cython.

b) The comparison across different clustering algorithms is performed on only one main synthetic dataset (with different settings). Please add your competitors’ performance in Table A1 (benchmark datasets) and give the properties of the evaluated datasets.

c) It would be interesting to include the baseline TS in the experiments.

d) The presented real-world use cases, superpixel and processing 3D brains, show different issues. The results of TB finding superpixels are compared to other methods finding superpixels, but not to other standard clustering methods like meanshift that performed very well in the simulated dataset. The experiments on brain scans do not seem very stable and neither baselines nor comparative methods are included here .

W2) There is an explanation regarding how theta can be determined, but I am missing further information concerning the robustness and intuition for the choice of the parameter.

W3) The self-defined metric for “Apparent Centroid distance” (AC) is used throughout the analysis. However, its computation is unclear and not given formally - do you only consider distances that are smaller than 0.1? If so, why this “magic number”?

W4) Almost all figures have a way too small font size so that they are not readable.

### Questions
Q1) How do you handle noise in the evaluation (for (H)DBSCAN/ TBSCAN results)?

Q2) How were the hyperparameters determined across the study, for the competitors as well as for your method? Which values were tried out and according to which criteria did you decide for the ones used in the end?

Q3) How robust are the results regarding different choices for theta?

Q4) How are the comparative methods chosen for the individual experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a major algorithm called Thetan Bereserker (TB) with 4 supporting minor algorithms (TS, TSR, TBK, TBSCAN). TB needs one parameter (distance) to perform, tries to address the order sensitivity problem and to estimate the number of cluster, while keeping the runtime low. Moreover, the method is tested in a rigorous way.

### Strengths
Overall, it is a strong paper and here are few points that I found interesting and strong about this paper:
1- The runtime is consistently low across the experiments
2- There is a reasonable mathematical framework to support the algorithm
3- It need only one parameter
4- It has a good coverage in the results section and ablation studies

### Weaknesses
 There are a few aspects that the paper can be improved:
1- The organization of the paper makes it hard to read. The figure placements forces going back and forth between pages. They are either placed too early or too late. This makes them to seem out of context and irrelevant despite them being useful and informative.
2- The details such as What is the data? What is the sub-sampling strategy? How many runs were there?,... for the study on the robustness of the algorithm is a bit vague.
3- The paper lacks embedding based clustering analyses. That is, it is not obvious which combination of the algorithms would yield the best clusters on text clustering.
4- I could not find noise and outlier sensitivity discussion on the paper.

### Questions
I see that there are TBK and TBSCAN inspired by KMEANS and DBSCAN, was there any research tracks to explore spectral clustering methods as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel centroid-based clustering paradigm that sequentially processes input samples, assigning data points to clusters based solely on a distance threshold. A common challenge with sequential clustering algorithms is the sensitivity of clustering results to the input order of the data. The proposed method, named TB (Thetan Berserker), addresses this issue by incorporating previously computed centroids with input samples to update or merge existing cluster centers. This approach enforces inter-cluster distances to exceed a predefined threshold, thereby reducing unnecessary clusters. Empirically, the method requires only a few iterations to achieve effective clustering results. The algorithm’s sequential nature ensures memory efficiency, and its limited number of iterations needed enhances time efficiency. Additionally, the proposed algorithm can be integrated with other traditional clustering methods for further refinement, introducing a new paradigm for sequential clustering.

### Strengths
(S1) Experiments -- The proposed method TB is simple yet effective, as demonstrated by a simulation dataset and two benchmark datasets. The experiments are conducted thoroughly, including ablation studies. These reveal key characteristics of TB, such as equidistant partitioning and rapid convergence in reducing cluster numbers.

(S2) Theoretical Depth -- Detailed theoretical proof with simple examples: The paper includes a detailed theoretical proof with simple examples and, aside from some minor confusing parts, is generally well written. The proofs of the theorems illustrate the impact of input data sequence ordering on clustering results and provide the functional assumptions for TB, specifically on selecting the distance threshold to ensure robustness against different sequence orderings of input data. The sequential processing approach for data clustering enhances the algorithm's scalability, which is beneficial.

### Weaknesses
 (W1) The introduction and related work sections are tiny and need extension. The proposed method is a sequential algorithm with the whole dataset available beforehand. However, a clear categorization of different clustering algorithms, including TB’s position, is missing.

(W2) The paper emphasizes its minimal hyperparameter requirements, specifically needing only the distance threshold. However, KMeans also requires one major hyperparameter: the number of clusters. Setting the distance threshold for TB is as challenging as defining the number of clusters. Could you provide some tutorials on setting the appropriate distance threshold and empirical evidence on the sensitivity of the TB distance threshold to clustering performance in the appendix?

(W3) Soundness of the method: While the paper provides a theorem, it lacks a theoretical proof explaining why the method converges so quickly when merging Berserker centroids. Instead, it relies on a case study with simulation data. This leaves a gap in theoretical validation for convergence, as empirical results based on a single simulation dataset are limited.

(W4) Practical limitations of the method: The method relies on a key assumption, namely the minimum inter-cluster distance must exceed the distance threshold, and both the inter-cluster distance and the threshold must be greater than the diameters of the hyperspheres bounding the clusters. The authors do not discuss how challenging it is to find this appropriate distance threshold satisfying this assumption in detail, nor do they provide a sensitivity study of the assumption violations and potential strategies for real-world data.

(W5) Unfair comparison of TB with state-of-the-art superpixel algorithms: In Table 2, TB's boundary recall accuracy drops significantly to 0.271 when compared to SLIC, another simple yet effective algorithm for superpixel clustering. However, this result differs from the findings in the paper NSLIC: SLIC superpixels based on nonstationarity measure,' (Fig. 3a). The boundary recall accuracy for SLIC can reach at least 0.6, depending on the number of superpixels and the compactness parameter.

(W6) Formatting of the paper: The paper has a 10-page limit, and I noticed minimal line spacing between figures and paragraphs, such as between lines 124 and 125 or between lines 141 and 142.

### Questions
(Q1) Improvements of the description of the approach:
(a) Predicting \theta: Please clarify the method for predicting an appropriate distance threshold (page 7, line 366). The application of random walks to estimate distances across clusters is unclear. In Figure 5, different inter-class distances are generated in the simulation; intuitively, greater inter-class distances reflect more separation between points. However, how can these distributions reliably determine the distance threshold, inferring the minimum distance between points from different classes?
(b) Centroid update: How will the Berserker centroids be updated? In the pseudocode for Algorithm 1, line 136, there is a reference to “assign to closest cluster and update centroid,” but it would be helpful to specify the centroid update process. Additionally, how can TB be effectively combined with other methods, such as KMeans and DBSCAN?

(Q2) Theoretical proof of the runtime: Provide a theoretical proof of the runtime, specifically addressing why fast convergence is achieved from a stochastic perspective.

(Q3) Experiment evaluations: For methods benchmarking, we suggest hyperparameter optimization on other state-of-the-art algorithms to enable a fair comparison. If time constraints are an issue, please include the hyperparameter settings for the evaluated methods in the appendix.

(Q4) Related work: Since TB is a distance-based clustering method, it would be helpful to include a categorization of clustering methods, distinguishing between distance-based and other types, because many clustering methods depend on distance metrics

### Soundness
3

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
This paper presents a centroid-based clustering algorithm named Thetan Berserker. 
This method is a parameterized by a single parameter which represents a distance threshold. This approach seems to improve the clustering metrics and runtime.

### Strengths
- The problem addressed in this paper is interesting and important.
- This paper uses a metaphore.

### Weaknesses
 - The contribution is not significant enough, and the approach lacks originality.

 - The paper is not self contained.

 - The quality of the presentation of the paper are very poor.

### Questions
- The problem should be formally introduced before introducing the proposed approach, some recalls would help to make the paper self contained.

- It seems like the authors used drastically \vspaces{}, which makes the paper hard to read (for example alg1 and table 1). 

- The quality of the figures should be improved, for example, the values in Figure 4 are hard to read. 

- The authors stated to report the Adjusted rand score (ARS) in the first paragraph of the 5th section but this is not reported in their results.  Why ?

### Soundness
2

### Presentation
2

### Contribution
2
