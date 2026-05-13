# Clustering with Geometric Modularity

- Decision: Reject
- Scores: 6, 3, 3, 8

## Abstract
Clustering data is a fundamental problem in unsupervised learning with a range of applications in the natural and social sciences. This wide applicability has led to the development of dozens of clustering algorithms. Broadly, these algorithms can be divided as being (i) parametric, e.g. $k$-means, where the centers are parameters and $k$ a hyperparameter, and (ii) non-parametric, e.g. DB-Scan (Ester et al. 1996), which has hyperparameters, but otherwise only uses a density to find clustering. An attractive feature of DB-Scan is not needing to know the number of clusters (usually unknown in practice) in advance. In this work, we propose a new measure of cluster quality, called \emph{geometric modularity} and show how it can be used to obtain an improved algorithm based on DB-Scan. Through experiments on a wide-range of datasets we show that using geometric modularity yields a superior method. Interestingly, our experiments also show that this quantity tracks a \emph{supervised} measure called \emph{normalized mutual information} well, despite using no label information. Finally, we also provide a theoretical justification of the use of this measure by considering a model for well-clusterable data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a new measurement of clustering quality called geometric modularity (GM), which extends the previous definition of modularity on graph data structure to vector-valued data samples. Given a clustering result, GM essentially measures the difference between the data density between intra-cluster and inter-cluster, and thus a higher geometric modularity indicates a stronger evidence of cluster patterns. The authors shows the GM can be evaluated in linear time, and use GM to guide the parameter tuning of commong clustering methods such as DB-SCAN. Experiments demonstrates that the output from DB-SCAN tuned by GM usually yields better cluster quality then existing approach such as OPTICS.

### Strengths
A list of strengths:
- This paper is well-written and easy to follow
- The idea of extending the modularity to vector-valued data is interesting and seems to be effective. The analysis on the linear runtime is important to make the geometric modularity computationall suitable for pratical use. 
- The theoretical analysis on the exact recovery by maximizing the geometric modularity is a good plus, and appers to be technically correct.
- The experiments is comprehensive and demonstrates a significant improvement compared to existing methods.

### Weaknesses
 - Given that the modularity ifself can be used for community detection in network data, and various approaches exist for clustering by maximzing the modularity, such as those mentioned in [1]. I think it is natural to ask if we can also apply similar approahces to the geometric modularity here, without using any auxiliiary tools such as DB-SCAN. If there are any critical challanges e.g. computational complexity, it might be worthy to point these out, and such challenges can be also good motivations for instead applying geometric modularity to DB-SCAN. Currently, it seems like there is a lack of such discussion. 
- I was a little bit confused about the originarity of the geometric modularity, as it is defined very similar to Eq.(1.1) in [2] which is also mentioned by the authors. Therefore, I think in prior to introducing the geometric modularity, it might be better to give a more detailed introducing fisrt on the modularity on unweighted graph, such as  Eq.(1) in [1], then its generalized version on weighted graph, e.g. Eq.(1.1) in [2]. As a result, the geometric modularity can be better motivated and their differences (I think the biggest difference is on the extra parameter $\rho$) is more clearly demonstrated.
- In the experimental results, the performance of OPTICS is dramatically poor compared to the DB-SCAN with geometric modularity. However, given that the high similarity between OPTICS and DB-SCAN, I would not expect such a huge performance gap exists, and thus I am very curious on the root causes, which could fall onto the following two categories from my opinions:
    1. The methodology of OPTICS essentially fails in these datasets, no matter how we choose the hyper parameters
    2. The result of OPTICS is sensitive to the hyper-parameters, and the parameters chosen in the experiments is still far from the optimal one.

- Currently, the answer is still not clear to me eventhough the result in Section A.3 might shed some light. Finding the root cause is important as it provides the more evidence on why we should use geometric modularity rather than OPTICS. If the reason is on the methodology of OPTICS, I would expect to see some plots on the ordered list of reachable distances generated by OPTICS, and see if there is indeed no clear clustering pattern no matter how the steepness is chosen. If the reason is on the hyper-parameters, maybe a wider range of $\xi$ should be verified in Section A.3

### Questions
- Could the author provide some discussion on why we don't consider clustering by geometric modularity itself, and what is the possible challenges on doing this?
- Could the author clarify the originarity of the geometric modularity, and state the main difference between the previous works?
- Could the author explain the siginificant performance gap between OPTICS and DB-SCAN, and see what is the root cause of that? 

Of course, please let me know if I missed anything. I would be very glad to raise my score if these questions can be properly addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper describes a quality measure for clustering called "geometric modularity",
which is used to tune DBSCAN's radius-parameter (called DBSCAN-mod).
The authors show that the ground-truth labels of well-seperable idealized data maximizes the geometric modularity. 
They found that DBSCAN-mod can achieve the ground-truth under these idealized circumstances.
Experimentally, the authors discovered that DBSCAN-mod often achieves a higher adjusted mutual information (AMI) than the OPTICS algorithm and observe.

### Strengths
Using the graph-theoretical modularity measure for community structures, to assess clustering is a reasonable proposition.
The paper considers a large body of 15 real-world benchmark datasets.
The paper discusses the impact of outliers on the result.

### Weaknesses
1. The proposed geometric modularity seems identical to Newman's weighted modularity [2004, https://journals.aps.org/pre/abstract/10.1103/PhysRevE.70.056131], 
but this link to a well-established variant has not been made by this paper. The authors fail to acknowledge that the modularity function, when applied to a fully connected graph with edge weights derived from a Gaussian kernel (or similar), is a well-studied approach in spectral clustering and graph partitioning. The paper should clarify the novelty of their approach in the context of this existing literature.

2. The experimental evaluation lacks in depth.
The claim that DPC did not result 'in any meaningful results' is not supported by facts. The authors only compare against OPTICS. Widely-used modularity-optimizing algorithms (albeit parametric and on weighted adjacency matrices), are not part of the experimental evaluation. There is no experiment showcasing the limitations of the tuning procedure under noise or high-dimensional data. The computational complexity analysis is not particularly insightful and of practical use. Specifically, the paper does not provide a rigorous analysis of the time complexity of the local search heuristic, which is crucial for understanding the scalability of the proposed method. The analysis should include a discussion of the worst-case scenario and how it scales with the number of data points and clusters.

3. The empirical results lack context.
That is, the paper does not compare geometric modularity to other `competing' ("internal"/"unsupervised") clustering-quality measures for tuning DBSCAN, including the classical Silhouette coefficient, Davies–Bouldin index, or Dunn index (under CV or model selection criteria). The paper should also explore how the proposed method compares to other parameter selection techniques for DBSCAN, such as those based on k-distance graphs or reachability plots.

4. The writing is unclear, not technical, and includes weasel-words, hyperbole, and unspecific adjectives "few papers", "some", "tracks AMI incredibly well", "better output quality", or "not much has been done". The paper does not properly motivate the usage of AMI well. The paper needs to provide a more rigorous justification for using AMI as the primary evaluation metric, including a discussion of its limitations and potential biases. The authors should also consider using other metrics, such as the V-measure or the adjusted Rand index, to provide a more comprehensive evaluation of the clustering results.

5. The paper does not properly describe their local-search post-processing heuristic, which had a profound impact on the performance, thus inhibiting the reproducibility. The description of the local search heuristic is insufficient for reproducibility. The authors should provide a detailed algorithm description, including the initialization procedure, the neighborhood definition, the acceptance criteria, and the stopping condition. The paper should also discuss the sensitivity of the results to the parameters of the local search heuristic.

6. The paper does not include a Reproducibility Statement and the submission does not include a Reproducibility Package.

### Questions
I don't understand the formal argument and the implication on the identifiability of the optimal solution, of your suggestion to smooth-over the hard-to-optimize (rugged?) solution landscape using isotonic regression. Could you expand on this?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript proposes using geometric modularity as a quality to improve the performance of DB-SCAN. In fact, the proposed algorithm outputs a clustering with the highest geometric modularity. It is also claimed that the geometric modularity has a positive relationship with adjusted mutual information. The empirical study is done with quite a number of datasets and compared with other two methods.

### Strengths
1. The paper is __in general__ well-organized and conveys the contents with clarity.
2. The experiments are analyzed carefully, and the results show good performance of the proposed method.
3. Geometric modularity is known as a 'metric' to evaluate the clustering results. It is good to formally build this connection.
4. It's also good to remind people of the linear computation of the geometric modularity.

### Weaknesses
1. Section 4.1 starts with "Our algorithm is outlined in Section 2". However I am not able to find a procedure such as Alg 1. It is not a big issue but for better clarity I think there should be one.

2. I have three main concerns: (1) limited novelty, which leads to weak theoretical analysis; (2) overclaimed contribution; (3) parameter choice of $\rho$.
- (1) Geometric modularity is used frequently for evaluation if there's no label at all (in contrast to pseudo-unsupervised), it is already a routine to examine clustering results. Therefore introducing an algorithm simply maximizing it does not shed new light. This also leads to a weak theoretical analysis which is basically proving what is assumed. I understand the authors want a "reasonable" datasets. But the point of beyond-worst-case analysis, per my understanding, is to avoid pathological instances but not to design properties of datasets tailored to what we want to prove. In definition 3.1, for example if one item is removed or relaxed, the proof breaks down.

- (2) I agree with the claim that "The unsupervised geometric modularity tracks a supervised measure AMI". But the positive relationship between this two measure is also known to the community, especially in the lens of density-based clustering. I am not sure if any previous work formally states this, but in this paper it is still shown by experiments. But anyway I can stay open to discussion. 

- (3) If I am understanding correctly, the motivation is to get rid of the parameter choice on $\varepsilon$, then what is the point if we have to choose $\rho$ again? Indeed, theorem 3.2 gives a range, but it is subject to other parameters given by the dataset, and according to section 4, it is selected in [0.5, 1]. The selection of $\rho$ is not clearly motivated by any theoretical insight, and the range [0.5,1] seems rather arbitrary, potentially requiring a grid search which defeats the purpose of avoiding parameter tuning.

3. The experiments include quite a number of datasets but not enough clustering methods. For example, SOM, HDBSCAN, or even $k$-means with the best $k$.

### Questions
- I wonder if computing the modularity in linear time is one of the contributions of this work? If not, is it folklore (just a practical heuristic) or proposed by previous work?

- I do not see a straightforward break-down if we apply the geometric modularity to other clustering methods, even $k$-means/median/center. Is there any foreseeable problem?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed a new measurement for evaluating the quality of clustering called geometric modularity. Inspired by the metric modularity in network, for each data point geometric modularity calculates the difference between its “average” distance to the all the rest of the points and those in its cluster. Both theoretical and empirical results are provided which shows the effectiveness of the proposed measurement.

### Strengths
1. A novel measurement for evaluating clustering quality is proposed.
2. The new measurement is linear in computation.
3. Both theoretical and strong empirical results are provided.

### Weaknesses
1. The connection of proposed geometric modularity and density-based clustering is not clearly stated. Specifically, while the definition of geometric modularity is presented as a general measure applicable to any clustering method, its evaluation is exclusively focused on DBSCAN. The paper lacks a clear explanation of why other clustering methods, such as k-means or hierarchical clustering, were not considered, and whether the proposed metric is theoretically or empirically suited for density-based methods only. This raises concerns about the general applicability of the proposed metric.
2. The method described in 4.1 lacks sufficient detail for reproducibility. The paper mentions a search for the optimal epsilon value, but the search range, the granularity of the rho parameter, and the specifics of the local search algorithm are not clearly defined. Without these details, replicating the experimental results is difficult. The description of the local search strategy is particularly vague, making it hard to understand how the optimal parameters are found.
3. The experimental section lacks comparisons with other state-of-the-art clustering algorithms. While DBSCAN is a widely used algorithm, the paper does not compare the performance of geometric modularity with other robust clustering methods, such as HDBSCAN, which is known to be less sensitive to hyperparameter tuning. This absence of comparison limits the assessment of the proposed metric's effectiveness relative to existing methods.

### Questions
1. The connection of proposed geometric modularity and density-based clustering is not directly explained. From the definition of geometric modularity, it can be used for tuning hyper-parameters for any clustering method (the title also implies this) and is not directly related to DBSCAN. But the authors only evaluated it with DBSCAN. The authors are recommended to explain more about this, why not other clustering methods. Maybe it is due to empirical observations, then it would be nice to give evaluations of using geometric modularity on other clustering algorithms. 
2. The method described in 4.1 is not clear enough for the others to reproduce the results. For instance, the searching ranging of \epsilon, granularity of \rho and detailed description of local search. BTW, will the authors open source the code to improve the reproducibility? 
3. The authors are recommended to compare with HDBSCAN, which is known to be robust to hyper-parameters. And its implementation is also available in sklearn.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
