# Towards Establishing Guaranteed Error for Learned Database Operations

- Decision: Accept
- Scores: 8, 5, 8, 3

## Abstract
Machine learning models have demonstrated substantial performance enhancements over non-learned alternatives in various fundamental data management operations, including indexing (locating items in an array), cardinality estimation (estimating the number of matching records in a database), and range-sum estimation (estimating aggregate attribute values for query-matched records). However, real-world systems frequently favor less efficient non-learned methods due to their ability to offer (worst-case) error guarantees — an aspect where learned approaches often fall short. The primary objective of these guarantees is to ensure system reliability, ensuring that the chosen approach consistently delivers the desired level of accuracy across all databases. In this paper, we embark on the first theoretical study of such guarantees for learned methods, presenting the necessary conditions for such guarantees to hold when using machine learning to perform indexing, cardinality estimation and range-sum estimation. Specifically, we present the first known lower bounds on the model size required to achieve the desired accuracy for these three key database operations. Our results bound the required model size for given average and worst-case errors in performing database operations, serving as the first theoretical guidelines governing how model size must change based on data size to be able to guarantee an accuracy level. More broadly, our established guarantees pave the way for the broader adoption and integration of learned models into real-world systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors consider the problem of providing
guarantees for learned database operations. In particular, they
consider indexing, cardinality estimation, and range-sum estimation,
and provide error guarantees for these three operations in both the
worst and average case (in the latter, they consider uniform
distribution on queries, and a second scenario where any distribution
can be used). Besides, they provide an experimental evaluation
comparing their error bounds with the errors obtained by training
different models on datasets sampled from different distributions.

### Strengths
* As pointed out by the authors, for database operations like
  indexing, learned estimators have empirically been shown to
  outperform some well-known traditional methods. However, such
  learned estimators are not widely used as no guarantees on their
  errors are known. In this sense, this paper makes a significant
  contribution by providing such guarantees for some useful database
  operations.

* The experimental evaluation provides some evidence that the bounds
  provided in the paper are meaningful.

* The paper is well written, with clear statements of the problems studied and the results obtained.

### Weaknesses
 * The cardinality estimation queries considered in the paper are
  restrictive. For such queries to be useful in practical database
  systems, they should include more complex queries, in particular,
  the join operator. In fact, one of the most important cardinality
  estimation tasks in databases is the estimation of the size of a
  join query, which is witnessed by the large number of research
  articles on this subject.

* The range-sum estimation queries considered in the paper are also
  restrictive. In particular, including other forms of aggregation
  would be very useful for practical database applications.

### Questions
* Could you please comment on the two points mentioned in Weaknesses.
  In particular, could you please comment on the possibility of using
  the ideas of the paper to provide error guarantees for aggregate
  operators min, max, and average.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work investigates the minimal size of models (minimal number of bits needed to represent model parameters) that can approximate ranks and (weighted) orthogonal range counts with a guaranteed maximal additive error (epsilon). It derives formulas for the worst/average-case model size and compares them with empirical results of a limited empirical result.

### Strengths
S1) Theoretical results are accompanied by empirical results.

S2) Results provide some insight into the practical complexity of approximating some database operators for multidimensional numerical data with learned models.

S3) The paper is generally easy to read and understand.

### Weaknesses
W1) Presentation a bit misleading: The paper gives the impression as if the results apply to general database operators over all sorts of tabular data (e.g., SQL queries over mix of categorial/numerical data) while the results are limited to orthogonal/axis-aligned range queries (intersection of range selections along each dimensions). In general the limitations of this work are not outlined clearly.

W2) Significance unclear: The empirical study is too limited to give a clear idea how much predictive power is gained via the derived formulas and the general discussion does not clearly explain the implications for learned indexing and related topics. Non-learned baselines such as random sampling are missing.

W3) Literature: The related work discussion is too limited in scope. It does not discuss VC dimensionality of orthogonal range queries (which is well-known and discussed in the referenced works), epsilon approximations in the computational geometry literature and data summaries in the database literature that pose questions that are similar in spirit to the model size question just with non-learned models such as samples and histogram-based data structures. Examples of related work in the aforementioned topics:

- Mustafa, N. H., & Varadarajan, K. R. (2017). Epsilon-approximations and epsilon-nets. arXiv preprint arXiv:1702.03676.

- Suri, S., Tóth, C. D., & Zhou, Y. (2004, June). Range counting over multidimensional data streams. In Proceedings of the twentieth annual symposium on Computational geometry (pp. 160-169).

- Shekelyan, M., Dignös, A., & Gamper, J. (2017). Digithist: a histogram-based data summary with tight error bounds. Proceedings of the VLDB Endowment, 10(11), 1514-1525.

- Cormode, G., Garofalakis, M., Haas, P. J., & Jermaine, C. (2011). Synopses for massive data: Samples, histograms, wavelets, sketches. Foundations and Trends® in Databases, 4(1–3), 1-294.

- Wei, Z., & Yi, K. (2018). Tight space bounds for two-dimensional approximate range counting. ACM Transactions on Algorithms (TALG), 14(2), 1-17.

W4) Minor issues

- p.3, Preliminaries, "specifics" => "specifies"
- p.6, Learned Cardinality Estimation, "estiamtion" => "estimation"
- p.10, Related Work, "hyperparametr" => "hyperparameter"

### Questions
Q1) What are the limitations of this work?

Q2) What is a non-trivial prediction that is enabled by the results in this this work?

Q3) What topics in the literature are related to the studied topic and how do the results in this work relate to the results from the related topics (e.g., how much better is a learned model than random sampling / other summaries)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors prove lower bounds on model sizes for various learned database components (indexing, cardinality estimation, and range-sum estimation) for a given maximum error and domain size across any dataset. For example, using the author's theorems, one can compute a lower bound on the number of bits a learned index structure must use to achieve a worst-case error over all databases of N rows and domain size U. The authors also give results for average case error, assuming either a uniform or an arbitrary query distribution.

### Strengths
This paper tackles an important problem. Existing learned index structures either grow unbounded to support a specific error (e.g., PGM index), or have an unbounded error but a specific size (e.g., RMI). In the former case, the author's bounds can be used to estimate the size of the fixed-error index structure ahead of time. In the latter case, where the model size is fixed ahead of time and the error is determined during training, the author's bounds can be used to estimate an initial model size from the desired error, or to compute an estimate of the error from the size of the model. Interestingly, the authors show that the domain size is relevant for worse case behavior but not for average case behavior.

### Weaknesses
While the bounds given by the authors certainly help bring our understanding of learned database components closer to that of traditional data structures, it is not clear to me how these bounds could be used in systems today. The most I seem to be able to say with the author's bounds is "if your learned index uses S bytes of memory, then for a given domain size, there exists a dataset size n for which your index must have an error larger than e." 

It is not clear to me how to use these bounds to size a particular structure with a fixed error, which would be useful for estimating the size of error-bounded indexes. Nor is it clear to me how to use these bounds to estimate the error of a fixed-size structure. Further, the authors fall short of actually *constructing* either (1) a dataset of size `n` and domain size `u` for which a particular index cannot achieve an error better than `e` for a given size, or (2) a index structure that can actually achieve the given error bounds at the specified size. The lack of concrete constructions makes it difficult to assess the tightness of the bounds and their practical relevance beyond theoretical insights. For example, if the lower bounds are derived from highly contrived datasets that are unlikely to occur in practice, their utility for real-world system design is limited. 

That said, this paper is still a useful contribution for practitioners like me! Using the worst-case error bounds for indexing given in table 1, setting n=200M, u=2^32, e = 8, I get sizes remarkably close to the exhaustive search performed by the cited learned index papers (7MB). So, even if these bounds are not exactly what database folks need, they appear to be a useful heuristic.

### Questions
Q1) I found the main text of the paper to be both overly formal and to give very little intuition about the actual proof. If the main text is just going to go over the results and implications, you might as well drop the formal notation and give intuitive / illustrated examples of each problem and bound.

Q2) That said, I really do wish the authors had tried harder to convey the intuition behind the proof in the main text. Unfortunately, I do not have the required background to parse the appendices. As far as I can tell, the authors assume that a learned structure can, at most, represent 2^n different functions of bitstrings. The authors show an isomorphism between bitstring functions and learned indexing, and then assert that, since only 2^n bitstring functions can be covered, any database admitting more than 2^n values must have at least imperfect prediction. From there, the authors work through to the error bound. I would love to know more!

Q3) A note on error functions: learned index structures today generally care about log-loss (i.e., the average log2 of the absolute differences), since this is the number of binary search steps one will need for the "last mile" search. 

Q4) typo A.1 "on the notions of the notions of"

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper works on establishing the lower bound of the required model size for arbitrary datasets, given a tolerable error parameter. The authors provide worst-case and average-case theoretical analysis for three database operations, i.e., learned index, learned cardinality estimation, and range-sum estimation. Some empirical evaluations are performed. While this appears to be the first theoretical study of such guarantees for the learned model, there are several concerns.

### Strengths
1. The paper is the first to study the guaranteed error for learned database operations.
2. This paper is overall easy to read, though I did not read the proof.

### Weaknesses
1. Concerns about the problem setting -- the studied problem does not quite correspond to the learned DB operators
-- For the learned index, it is fine for the model to make errors as we can maintain some delta to help correct the error. After all, the training and testing data are the same. The typical use case involves using the learned model to predict the approximate location, followed by a local search. The error metric should reflect the cost of this local search, such as the number of steps, rather than the absolute error in the predicted location. This is especially true since the training and testing data are identical, meaning the model is essentially interpolating. The focus should be on how well the model guides the search, not its raw prediction accuracy.
-- For the learned cardinality estimator, the absolute error is not what people are using for evaluation -- q-error is. This is because for a true cardinality of 10K, an error of 100 is more acceptable than an error of 10 for a true cardinality of 10. The absolute error is not a good indicator of the practical impact of the error on query optimization. A small absolute error on a large cardinality can be insignificant, while the same absolute error on a small cardinality can lead to a drastic change in the query plan. The evaluation metric needs to be more aligned with the practical usage of cardinality estimators, which is to guide query optimization, where relative error is more important than absolute error.

2. When people study learned db operators, the main advantage is that the model can adapt to the underlying data and hence derive instance-optimal solutions. However, this paper is studying the worst-case/average scenario, which contradicts to the motivation of using learned model to be instance-optimal. The core idea of learned models is to exploit the data distribution to achieve better performance than traditional methods. By focusing on worst-case or average-case scenarios, the paper misses the point of why learned models are used in the first place. The analysis should focus on how the model adapts to specific data distributions and how this adaptation leads to performance gains, rather than focusing on scenarios that are not representative of the typical use case.

3. It would be great to show more implications of this theoretical results and how can we make use of this theoretical results in practice. It is now unclear. The result shown in Figure 1 does not provide actional items for users. In particular, it seems that different models are having similar average-case lower bounds in terms of error -- which is not quite differentiable. The paper lacks a clear explanation of how the theoretical results can be translated into practical guidelines for users. The results should provide insights into how to choose the right model architecture or how to set the model size based on the desired error rate. The current results are too abstract and do not provide actionable recommendations for practitioners.

### Questions
1. It would be great to better articulate the problem settings (See W1)
2. It would be great to justify the usefulness of worst-case/average-case guarantees instead of instance-level guarantees (See W2).
3. It would be great to show more implications of the theoretical results (see W3)
4. what is the unique property of learned DB operators that are used during the proof? Putting it in another way, is this method applicable to arbitrary functions and not limited to learned DB operators?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
