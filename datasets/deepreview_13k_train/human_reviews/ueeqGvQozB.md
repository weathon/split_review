# ML4MILP: A Benchmark Dataset for Machine Learning-based Mixed-Integer Linear Programming

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
Machine learning (ML)-based approaches for solving mixed integer linear programming (MILP) problems have shown significant potential and are growing in sophistication. Despite this advancement, progress in this field is often hindered by the mixed and unsorted nature of current benchmark datasets, which typically lack carefully categorized collections of homogeneous instances.
To bridge this gap, we propose ML4MILP, a new open-source benchmark dataset specifically designed for evaluating ML-based optimization algorithms in the MILP domain. Based on the proposed structure and embedding similarity metrics, we used a novel classification algorithm to carefully categorize the collected and generated instances, resulting in a benchmark dataset encompassing 100,000 instances across more than 70 heterogeneous classes.
We demonstrate the utility of ML4MILP through extensive benchmarking against a comprehensive suite of algorithms in the baseline library, consisting of traditional exact solvers and heuristic algorithms, as well as ML-based approaches. Our ML4MILP is open-source and accessible at: https://anonymous.4open.science/r/ML4MILP-6BE0.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on developing a benchmark ML4MILP to evaluate machine learning (ML) based methods for solving mixed-integer linear programs of MILPs. The benchmark includes MILP instances from various existing MILP benchmark suites such as MIPlib and previous competitions such as ML4CO, as well as synthetically generated large scale instances from canonical MILP instances. For each set of problem instances, the authors obtain both a structural embedding as well as a neural embedding for each problem instance, where the neural embeddings are obtained by representing the MILP instances as bipartite graphs, and leveraging a graph autoencoder. These embeddings are utilized to generate inter-class distances and intra-class distances. These distances are used to highlight the homegeneity and heterogeneity of various classes of instances, and utilized to split heterogeneous classes in smaller homogeneous classes. Given these classes of MILP instances, various off-the-shelf MILP solvers (such as Gurobi) and ML based techniques (such as Predict+Search) are evaluated for a given runtime threshold, and their objective values and gap estimates are presented.

### Strengths
Standardized benchmarks are often very useful in the development of any particular area, so a benchmark for evaluating ML based schemes for solving MILPs can be very useful for the area.

### Weaknesses
While I can understand the motivation for having homogeneous instances within a class, heterogeneity also might be beneficial to illustrate generalization performance of solvers. I currently do not see this topic being much discussed in the paper.

Analyses of benchmark experiments is limited and only performed qualitatively based on raw numbers and visualizations. Maybe the authors could consider adding some statistical analyses on top of hypotheses so that they can illustrate an empirical workflow on the benchmark?

The presentation of the benchmarking results in Section 4.3 could be improved and more detailed. See also questions below.

The overall contribution (introduction of the benchmark and showing the lack of homogeneity of existing classes of instances of benchmarks based on similarity evaluation metrics with respect to structure and neural embedding distances) is somewhat limited in scientific insight and currently results in me having a hard time to vote for acceptance at a main ML and DL conference such as ICLR. Maybe submitting the paper to a Benchmark and Dataset track of a suitable conference might be more targeted?



### Questions
Beyond some of the questions raised in the weakness, here are some additional questions for my own understanding:

- (Q1) How does this benchmark compare and contrast against the benchmark created for the ML4CO Neurips competition (Gasse et al., 2022)? How does this competition benchmark (and the existence of MIPlib) affect the "first open-source benchmark dataset" claim in line 74?
- (Q2) Is the GNN autoencoder learned for each problem "class" or one encoder across all problems? It seems like it is the first, but it is not clear why we should not just consider all instances to train the graph autoencoder.
- (Q3) What is Figure 2 supposed to show? The figure on the left is not a bipartite graph so what is it showing?
- (Q4) It seems like the "Structural Embeddings" discussed in lines 214-215 and 230-232 are manually crafted structural features of any given MILP. Is that correct?
- (Q5) Figure 8 is quite unclear and needs further elaboration. If each color block is a problem, how are bars stacked up? From Table 3, it seems lower gap is better, but then it is not clear whether higher score is better or worse. For the conversion of a particular gap estimate $x$ to a score $\text{Score}(x)$, it is not clear what are the $\mu, \sigma$, and how many samples of scores are generated from the normal distribution.
- (Q6) Why such focus on the graph autoencoder based representations of MILPs? If we want a metric between graphs, can we not employ any graph kernels [A] to find pairwise similarities (which are then extended to compute inter-class and intra-class distances)?
- (Q7) The training curves in Figures 6 & 7 are oddly very drastic for the orange curves (after reclassification). This seems a bit odd. While the x-axis does not have tick labels, it seems like all the learning happens in a single epoch, which is a bit odd. What is it about the set of problem instances that all the learning happens in a single epoch? Is this consistent with existing papers? 

[A] Kriege, Nils M., Fredrik D. Johansson, and Christopher Morris. "A survey on graph kernels." Applied Network Science 5 (2020): 1-42.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces ML4MILP, a benchmark of mixed inter linear programs (MILP)s containing 100.000 instances across more than 70 dataset classes defined via structure and embedding similarity metric based on bipartite graph representations.
ML4MILP tries to fill the gap of having a large scale, standardized benchmark for evaluating mixed inter linear program solvers.
The authors demonstrate utility of the benchmark by comparing traditional exact solvers and heuristic algorithms and ML-based approaches on their benchmark.

### Strengths
The paper appears to present an original benchmark collection targeted to the MILP domain with relevance for the ML and DL community due to ML-based approaches becoming popular in this field.
The paper in general but especially the introduction and related work are written well and give a nice self-contained overview of existing solvers and techniques as well as existing related benchmarks and generally the lack of a larger standardized benchmark for MILPs.
Based on structural and embedding distance between instances of benchmarks, the authors show that existing benchmarks often are more heterogeneous than the MILP benchmark they propose which allows for some insight with respect to the structure of the proposed and existing benchmarks.

### Weaknesses
The authors have used spectral clustering with euclidean distance as a measure for classification of the dataset instances. This choice of this approach needs to be substantiated better. Specifically the choice and implementation of the clustering method, including the choice of parameters and number of clusters needs to be provided. A discussion on the scalability of this method is also required. The lack of justification for using spectral clustering with Euclidean distance is a significant concern, especially given the high dimensionality of the embedding space. The authors should elaborate on why this method is suitable for capturing the underlying structure of the MILP instances, and how the parameters, such as the number of clusters, were chosen. Furthermore, the computational cost of spectral clustering, which involves eigenvalue decomposition, can be prohibitive for large datasets. A discussion on the scalability of this method, particularly with respect to the 100,000 instances, is crucial.

The use of the phrase "ML-based algorithms" should be clarified. This is a very broad term and could be seen in multiple contexts based on the reader's domain of expertise. As such, it may be better to call out the scope clearly. The term "ML-based algorithms" is too broad and lacks specificity. The authors should clearly define which machine learning algorithms are being considered. For example, are they referring to supervised learning algorithms, unsupervised learning algorithms, or both? Are they considering specific types of models, such as neural networks, support vector machines, or decision trees? This lack of clarity makes it difficult to assess the scope and relevance of the work.

Details on the specific steps for computation of structural and neural embeddings should also be included. For example, is there a reference for (2), what happens in limiting cases? What is |I| ? The description of the structural and neural embeddings lacks sufficient detail. For the structural embedding, the authors should provide a reference for equation (2) or explain its origin. They should also discuss the behavior of the embedding in limiting cases, such as when the number of constraints or variables is very large or very small. Furthermore, the meaning of |I| should be explicitly defined. For the neural embeddings, the architecture of the neural network used to generate the embeddings, the training data, and the training procedure should be described in detail. The lack of these details makes it difficult to reproduce the results.

It is not clear how reclassification of the dataset leads to addressing issues such as loss leading to NaN values. More analysis is required to substantiate such a claim. The claim that reclassification of the dataset addresses issues such as loss leading to NaN values is not adequately substantiated. The authors need to provide a clear explanation of how the reclassification process mitigates this problem. Specifically, they should explain why the reclassification leads to more stable training and prevents NaN values. A more detailed analysis of the relationship between the dataset structure, the reclassification process, and the occurrence of NaN values is required.

The repository link provided is not accessible, it returns a connection timeout error.

Limitations in the current and possible (specific) directions for future work should be included.

Some other aspects of the paper:
The graph (Figs 6 and 7) legend has a typo for 'befor'. The horizontal axis labels are also missing. What is shown on the Y-axis - change in loss function values or absolute values? How do we interpret this?
The tables could be made concise, especially when lot of the values in the tables are repetitive (Tables 10,11,12 for eg.)

### Questions
In L269 you mention that you "carefully gathered a substantial number of MILP instances through various means". The word "carefully" is used a lot in context with the selection of instances but it is not really explained, how the selection process was performed. Which exactly were criteria for selection instances "carefully"?

Figure 3 shows also anytime performance curves. Is there any reason why such curves were not presented for some benchmarks in the main paper or appendix?

Having a huge benchmark of many instances may risk that users select a subset of instances to benchmark on to reduce computational burden. Do the authors officially recommend to benchmark algorithms always on all instances? 

In Section 4.2 which optimizer and loss function was used for the GNN?

Table 2 and 3 appear to show somewhat redundant information, e.g., one shows the objective function values and the other the gap in optimality. Maybe one table could be moved to the appendix to free up some space for additional visualizations of results or statistical analysis of results?

Figure 8 is quite difficult to digest due to many information but also color gradients being used that however represent factor levels (i.e., the ML4MILP benchmark instances). Maybe the authors could find some easier way to visualize this, i.e., separate colors for IP and MILP or split the figure and use qualitatively different colors instead of a color gradient?

In Appendix D.2 you state:
D.2 "we appreciate the reviewers attention to this detail"
This makes me wonder if this is a re-submission without spending time to clean up the incorporation of previous feedback.
Especially as the section in the main paper concerned with using the standard normal density function on benchmark scores (gap estimates) seems to not have been improved and lacks details and clarification why and how exactly this transformation was performed.
Also, I noted that some descriptions are not really clear here with respect to this transformation.
While the CLT is concerned with the limiting distribution of the sample mean, this is not really applicable here or justifies using the density function of a normal distribution directly to transform the gap scores.
Maybe the authors can improve this section (starting from L509 in the main paper) and explain in detail how and why this transformation was performed?
E.g. what was the reason to not perform a min-max or quantile normalization?
Also, when using the density function of a normal, how is it guaranteed that the transformed scores will be on a range from 0 to 100?

L951 easy - medium - hard <-> tens of thousand, hundreds of thousand and millions of decision variables.
Is this the standard way to classify problems in the related literature or can the authors justify this?

I, personally, found it unusual, that Deepmind is explicitly mentioned two times in the related work section within 20 lines.
Surely, it is important to show that research groups are working on this topic but explicitly mentioning one group of one big tech company does in my opinion not fit the usual style of a scientific paper.
Simply citing the authors, in my opinion, should be enough.

For me, downloading the code from https://anonymous.4open.science does no longer work.
Could it be that the download ability must be refreshed or some functionality is expired?
(The link itself is up but downloading the repository always fails for me.)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present ML4MILP, a benchmarking dataset of 100,000 instances across 70+ classes. They have baselined this library and used GNN to classify the instances, using a statistical structural similarity metric.

### Strengths
The paper presents a review of the state-of-the-art in MILP benchmarks and highlights the shortcomings.
The dataset is provided in three parts, including a baseline library that is benchmarked on SoTA solvers and ML algorithms. The pros and cons of these aspects are well discussed.

### Weaknesses
The authors have used spectral clustering with euclidean distance as a measure for classification of the dataset instances. This choice of this approach needs to be substantiated better. Specifically the choice and implementation of the clustering method, including the choice of parameters and number of clusters needs to be provided. A discussion on the scalability of this method is also required.

The use of the phrase "ML-based algorithms" should be clarified. This is a very broad term and could be seen in multiple contexts based on the reader's domain of expertise. As such, it may be better to call out the scope clearly.

Details on the specific steps for computation of structural and neural embeddings should also be included. For example, is there a reference for (2), what happens in limiting cases? What is |I| ?

It is not clear how reclassification of the dataset leads to addressing issues such as loss leading to NaN values. More analysis is required to substantiate such a claim.

The repository link provided is not accessible, it returns a connection timeout error.

Limitations in the current and possible (specific) directions for future work should be included.

Some other aspects of the paper:
The graph (Figs 6 and 7) legend has a typo for 'befor'. The horizontal axis labels are also missing. What is shown on the Y-axis - change in loss function values or absolute values? How do we interpret this?
The tables could be made concise, especially when lot of the values in the tables are repetitive (Tables 10,11,12 for eg.)

### Questions
a. Provide details on the choice of the classification approach.
b. Include (clarify) details for ML-based algorithms.
c. Include details for embedding computation.
d. Fix and address issues related to loss plots and associated details.
e. Please check the repository access.

### Soundness
2

### Presentation
3

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
The paper introduces ML4MILP, an open-source benchmark dataset for machine learning-based approaches to solving MILP problems, featuring 100,000 instances across over 70 heterogeneous classes. To address the lack of homogeneity in existing MILP datasets, the authors developed novel structural and embedding similarity metrics, along with a new classification method to refine the categorization of less homogeneous datasets. Additionally, the paper includes comprehensive testing to establish baselines for effective benchmarking.

### Strengths
1. ML4MILP offers an extensive benchmark dataset with 100,000 MILP instances in over 70 classes.

2. The paper introduces a novel classification method using structural and neural embedding similarity metrics to enhance the homogeneity of existing MILP datasets.

3. A comprehensive baseline library is provided, facilitating consistent benchmarking and clear comparison across various optimization algorithms.

### Weaknesses
1. There could be potential in combining the structural and neural embedding metrics into a unified measure. Currently, these metrics seem to be more qualitative than quantitative, as shown in Figure 5 where cluster 6 has large distances in both metrics, but the other clusters show discrepancies (e.g., cluster 1 has a higher structural distance than cluster 3, yet a lower neural embedding distance). Merging these metrics might help address such inconsistencies and provide more comprehensive evaluations.

2. It would be valuable to identify classes that are neither too similar nor too different to facilitate benchmarking for transfer learning or other generalization approaches, which would broaden the dataset’s applicability.

3. In the baseline algorithm comparison, the quantified scores only consider solution gaps; including solving time as an additional metric would provide a more holistic assessment of algorithm performance.

### Questions
1. Building on weakness 1, Figure 5 shows that many inner-cluster distances are larger than distances between clusters, which raises questions about the effectiveness of the current metrics in capturing true internal homogeneity.
    
2. It is unclear from the provided details whether the y-axis in Figures 6 and 7 represents change values (relative differences) or absolute loss values.

### Soundness
3

### Presentation
2

### Contribution
3
