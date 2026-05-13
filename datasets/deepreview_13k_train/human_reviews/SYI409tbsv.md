# Towards a Unified Framework of Clustering-based Anomaly Detection

- Decision: Reject
- Scores: 5, 6, 3, 6, 3

## Abstract
Unsupervised Anomaly Detection (UAD) plays a crucial role in identifying abnormal patterns within data without labeled examples, holding significant practical implications across various domains.
Although the individual contributions of representation learning and clustering to anomaly detection are well-established, their interdependencies remain under-explored due to the absence of a unified theoretical framework. Consequently, their collective potential to enhance anomaly detection performance remains largely untapped.
To bridge this gap, in this paper, we propose a novel probabilistic mixture model for anomaly detection to establish a theoretical connection among representation learning, clustering, and anomaly detection.
By maximizing a novel anomaly-aware data likelihood, representation learning and clustering can effectively reduce the adverse impact of anomalous data and collaboratively benefit anomaly detection. Meanwhile, a theoretically substantiated anomaly score is naturally derived from this framework. Lastly, drawing inspiration from gravitational analysis in physics, we have devised an improved anomaly score that more effectively harnesses the combined power of representation learning and clustering.
Extensive experiments, involving 17 baseline methods across 30 diverse datasets, validate the effectiveness and generalization capability of the proposed method, surpassing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary: This paper proposes an unsupervised anomaly detection framework called UniCAD, which unifies representation learning, clustering, and anomaly detection. Traditional methods often treat these components separately, which limits their potential to enhance each other. UniCAD introduces a probabilistic mixture model that maximizes an "anomaly-aware" data likelihood to jointly optimize representation learning and clustering, reducing the impact of anomalies. Additionally, UniCAD derives an anomaly score with theoretical support, enhanced by a gravitational force-inspired metric that leverages relationships between samples and clusters. The proposed method outperforms baseline methods in terms of average rank

### Strengths
The proposed framework introduces an integrated approach to unsupervised AD by jointly optimizing representation learning, clustering, and AD within a single model. The analogy of gravitational force for anomaly scoring is interesting. On average, the proposed method outperforms the selected baselines in terms of average performance.

### Weaknesses
1. The model jointly learns a mixture model similar to DAGMM and incorporates a clustering objective as a constraint. While the techniques used in this combination are relatively common in AD, this is not necessarily an issue if the combination demonstrates a unique synergy. The significance of the paper could be improved if the authors provided more insight into why this specific combination is more advantageous than others. For instance, how would performance differ if hypersphere-based constraints like Deep SVDD were combined with mixture models, or if other SSL methods were paired with the clustering objective? A more detailed ablation study exploring different combinations of these components would be beneficial to demonstrate the specific advantages of the proposed approach. Furthermore, the novelty of combining these specific techniques needs to be more thoroughly justified, perhaps by highlighting limitations of existing methods that this particular combination overcomes.

2. Some recent baselines are missing. There are several comprehensive surveys on AD available through Google Scholar, and benchmark papers such as ADBench from NeurIPS 2022 could serve as a useful reference point. Specifically, the evaluation should include more recent deep learning-based anomaly detection methods that have shown strong performance on similar datasets. The absence of these baselines makes it difficult to assess the true performance of the proposed method relative to the state-of-the-art.

3. The default neural network architecture is fairly basic. It might be worth exploring stronger backbones, such as those based on transformers or more complex convolutional networks, as these could have a significant impact on the evaluation results. The current architecture might be limiting the potential of the proposed method, and exploring more advanced architectures would provide a more comprehensive evaluation of the core ideas. The impact of the backbone choice on the overall performance should be investigated and reported.

4. A diagram of the proposed framework would greatly enhance clarity and help readers better understand the model's structure and components. A clear visualization of the data flow, the different modules, and the interactions between them would significantly improve the accessibility and understanding of the proposed method.

### Questions
1. In the main results, Isolation Forest appears to perform surprisingly well and is, on average, the best-performing baseline method. Could you provide a discussion on this observation?

2. I noticed that several GAD methods are included in the appendix, despite my understanding that the focus of this paper is on AD for i.i.d. data. Why were these methods chosen over other i.i.d. data baselines, such as those for images? It would be helpful if the authors could explain their inclusion. Additionally, if the authors find it important to include GAD baselines, it is recommended to compare them with more recent methods, e.g., those published in 2023 and 2024.

3. Will the proposed framework be effective for image AD?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new heuristic to compute the anomaly scores under a mixture of models assumption which is motivated by the laws of gravitation. Instead of using scalar addition of the probabilities to compute anomaly score, the proposed technique uses vector addition.

### Strengths
1. The proposed heuristic appears simple yet effective
  2. The paper is well written
  3. The experimental section is strong
  4. Ablation experiments are very useful

### Weaknesses
1. Comparison with gravitation is a stretch and should be left out. While in some sense using vector addition might appear intuitive, mathematically, the underlying data generative model under a Mixture of Models assumption is probabilistic which does not correspond to any 'force' based model; probability at any point does not have a direction. Therefore, the reasoning behind the use of vectors can only be taken as a heuristic with little formal rigorous justification. Despite this weakness, the paper shows a potential for effectiveness and is quite novel.

2. The paper lacks a discussion on the computational complexity of the proposed method. Vector addition, while conceptually simple, might introduce overhead depending on the dimensionality of the probability vectors and the number of mixture components. This aspect needs to be addressed to fully assess the practical applicability of the method, especially in high-dimensional settings.

3. The paper does not explore the sensitivity of the method to the choice of mixture components. The performance of mixture models is often highly dependent on the selection of appropriate components. It is unclear how the proposed vector-based anomaly score would behave if the mixture model is not a good fit for the data, or if the components are not well-separated. This is a critical aspect that needs further investigation.

### Questions
N/A

### Soundness
3

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
4

### Summary
This paper proposes an unsupervised anomaly detection method based on clustering. The clustering approach relies on a latent representation and a t-distribution, which has been applied in density estimation tasks for decades.

In addition to clustering, the authors propose likelihood-based and gravity-based anomaly scoring methods with neighbor averaging.

### Strengths
The paper employs understandable mathematical notations, unlike the majority of deep learning papers.

### Weaknesses
The t-distribution-based clustering approach is established. The gravity-based, likelihood-based, and neighbor averaging techniques are also well-known in the field, raising concerns about the paper's novelty.

Additionally, the paper appears to mischaracterize previous research. The use of mixture models for anomaly detection has been documented for at least 25 years (e.g., Yamanishi et al., KDD 2000). Latent subspace-based formulations are also known, such as in Pesevski et al. (2018).

### Questions
Elaborate on the novelty in light of existing works.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an unified approach to anomaly detection by
combining clustering, representation learning and anomaly detection
via maximising the likelihood of the observed data.  The likelihood of
data is deomposed into the anomaly indicator multipled by the
likelihood of clustered data.  The likelihood of clustered data is a
mixture model with cluster prototypes/centrods and covariance, which
is learned via EM.  Clustering is based on learned representations of
the data via a feature extractor.  The anomaly indicator is zero if an
instance is some predeteremined lowest percentile in the likelihood of
clustered data.  That is, the anomaly indicator is zero if the
instance is unlikely.  The anomaly score is one over the likelihood of
clustered data.

Pointing out the similarity between Newton's gravitational law and the
their likelihood of clustered data, they propose incorporating
direction in addition to magnitude in calculating the anomaly score.
The direction is from the instance to a prototype/centroid.  They call
this method vector sum.

The overall loss function has the negative log likelihood of data and
the reconstruction loss of an autoencoder for the input instances.

They compare their method UniCAD with 10 existing algorithms over 29
tabular datasets.  Empricial results indicate UniCAD with vector sum
has a higher average rank.  Ablation studies indicate the contribution
of different components.

### Strengths
Unifying representation learning, clustering, and anomaly deteciont 
into a single likelihood expression is insteresting.

Inspired by physics, incorporating direction in addition to distance
in calculating anomaly score is interesting.

Empirical results indicate that the method has a higher average rank
than 10 existing methods.  

The paper is generally well written.

### Weaknesses
The clustering approach is similar to typical learning of Gaussian
Mixture Models (GMMs) with EM, except with a t-distribution instead of
a Gaussian distribution. The use of a t-distribution instead of a Gaussian is a minor modification and does not fundamentally change the underlying clustering methodology. The core idea of iteratively updating cluster assignments and parameters via an Expectation-Maximization framework remains the same, thus limiting the novelty of this component.

Only two of the 10 existing algorithms involve representation
learning.  Without representation learning, an algorithm is in an
inherent disadvantage when compared to UniCAD. This makes the comparison somewhat unfair, as the playing field is not level. The performance gains of UniCAD might be partially attributed to the inclusion of representation learning, rather than the core anomaly detection method itself. It would be more convincing to compare against methods that also incorporate representation learning to isolate the contribution of the proposed approach.


### Questions
With vector sum, an instance in between two protoypes/centroids could
have an anomaly score of zero, because the two directions are
opposite. Is that desirable?

Sec 3.3.2.  Why can an autoencoder reduce a shortcut solution?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses a long standing problem of anomaly detection. To this end, the authors propose a unified framework. This framework simultaneously incorporates 3 important ideas: recovering latent view of data (representation learning), leveraging spatial patterns in data (clustering), and preventing the outliers from contaminating the data model (anomaly detection). Inspired by classical mechanics, the authors further improve the framework by using vector summation in outlier scoring. Extensive experiments with 30 datasets and over a dozen baselines show that the proposed framework can generally outperform previous methods.

### Strengths
Several aspects caught my attention when I was reading this paper. Each aspect has strengths and weaknesses. Thus each aspect will be discussed twice, once here and once in the "Weaknesses" section.

Framework: Simultaneous incorporation of representation learning, clustering, and outlier filtering is a powerful framework. It has the most potential compared to considering these factors in isolation or ignoring some of these factors. It is also helpful that the method is applicable in inductive setting.

Physics-inspired design: The use of the vector sum improves performance. It also makes an interesting and thought-provoking read.

Evaluation: The authors evaluated their method using a large number of datasets (30) and baselines (17).

Presentation: Overall, the paper is well-written and easy to follow. Providing a comprehensive study in Appendix has been very useful.

### Weaknesses
Framework (theory): The authors did not provide a solid theoretical foundation behind the propose framework. For example, is Algorithm 1 guaranteed to converge? Is it possible that the algorithm will indefinitely oscillate, e.g., considering points 1, 2, 3 outliers in one iteration, then considering 4, 5, 6 in the next iteration, then considering 1, 2, 3 outliers again, then considering 4, 5, 6 outliers, etc. Moreover, Equation 1, while making intuitive sense, does not appear to correspond to any coherent statistical model. E.g., in a statistical model, one would expect that any point has a probability of being an outlier, even if it's not in the top l by score. Also, does the equation imply that for outliers p(x | params)=1? Given that a point is an outlier, what is p(x | params, x is outlier)?

Framework (novelty): There has been a long history of robust model fitting, including the idea of ignoring potential outliers (e.g., in RANSAC). The proposed framework is an instantiation of this idea. The paper has some novelty, but the novelty is not ground breaking.

Physics-inspired design: Vector sum is an aspect that I found quite interesting, but also most worrying. Thank you for including a deep dive example in Appendix Figure 4. However, what if the central cluster was just a regularly sized cluster? In this case, would a point in the centre of the central cluster receive a very high outlier score (because all "forces" neutralize)? But intuitively, this would be the least abnormal point in the data. I know that in the experiments using the vector sum appeared to increase performance, but I would have liked to see a deep dive from some of these datasets. I don't understand why using vector sum is not harming performance. Also, in Figure 2, you cannot compare the score relative to (mu_1, mu_2) with the score relative to (mu_3, mu_4), because these will be probabilities conditioned on different parameters. That is, you cannot compare outlier scores from different model estimates.

Evaluation (overfitting): Thank you for providing hyperparameter analysis. However, it does show that selecting the right values is important. This raises the concern of whether the parameters were overfit to the datasets. Even though the same setting were used for all datasets, I'm concerned whether the result was overfitted (overfit to the mega-dataset consisting of 30 datasets).

Evaluation (stat. significance): I'm concerned whether critical difference diagrams in Appendix Figure 5 imply that the winning method is not statistically significantly different from the 2nd, 3rd, etc. This is based on horizontal lines crossing several methods.

Presentation: There has been some minor issues with writing
- There is a typesetting issue with citations. Citations should be in brackets. E.g., according to Smith (Smith et al., 2010) or according to Smith [3]
- Some parts of the paper mention 17 baselines, while other parts mention 15
- Items 1, 2, 3, ... in the Introduction are mentioned before Figure 1 is cited
- Why are some arrows crossed in Figure 1?
- The paper mentions "Based on the aforementioned advantages of MMs, ... ", but there were no discussion of MM. Also, acronym MM is not defined
- In Section 3.3.1 (M-step), J is not defined
- In Section 4.4, what does "omitting the likelihood maximization loss" mean?
- Color coding in Table 1 is very confusing. To me "green" is something good, and I though "green" denoted the winner

### Questions
- What was the process of selecting values for parameters l and K for the purpose of experiment in Table 1?
- In Appendix Figure 4, if the central cluster was just a regular cluster, would the point near the centre of the central cluster receive a very high outlier score?

### Soundness
2

### Presentation
3

### Contribution
2
