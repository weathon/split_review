# Enhancing Clustered Federated Learning: Integration of Strategies and Improved Methodologies

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
Federated Learning (FL) is an evolving distributed machine learning approach that safeguards client privacy by keeping data on edge devices. However, the variation in data among clients poses challenges in training models that excel across all local distributions. Recent studies suggest clustering as a solution to address client heterogeneity in FL by grouping clients with distribution shifts into distinct clusters. Nonetheless, the diverse learning frameworks used in current clustered FL methods create difficulties in integrating these methods, leveraging their advantages, and making further enhancements.  
To this end, this paper conducts a thorough examination of existing clustered FL methods and introduces a four-tier framework, named HCFL, to encompass and extend the existing approaches. Utilizing the HCFL, we identify persistent challenges associated with current clustering methods in each tier and propose an enhanced clustering method called HCFL$^{+}$ to overcome these challenges. Through extensive numerical evaluations, we demonstrate the effectiveness of our clustering framework and the enhanced components. Our code will be publicly accessible.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript proposes a holistic federated learning framework to enhance classification performance by grouping clients into clusters. The framework comprehensively integrates the hard and soft partitional clustering, and clustering with and without automatic cluster number determination. Comphrehensive theoretical and empirical evidence have been provided to illustrate the effectiveness of the proposed method. Moreover, the paper is generally well-written and easy to follow.

### Strengths
1. A holistic FL framework incorporating different clustered FL methods for more comprehensive FL. The research problem is important, and this work contributes to fixing the shortcomings of the existing related works.
2. Comprehensive experimental evaluation has been conducted to illustrate the effectiveness of the proposed method.
3. The paper is well written with a clear demonstration of the motivations and problems for solving.

### Weaknesses
1. This work focuses on using clustering techniques to enhance the classification accuracy of FL. The difference between this type of research and the fully unsupervised federated clustering should be discussed to avoid potential misunderstandings.

2. The efficiency issue is listed as one of the challenges in Section 4.1. But only the final number of clusters is reported accordingly. More discussions about the time and space complexity of this work, or even corresponding evaluation results are preferable.

3. The source code is not opened in the current version.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The contribution formalizes a general pipeline/framework for clustered federated learning, on the one hand via a cost function, on the other hand via algorithmic choices (as it is not easy to include the objective of an optimum clustering number into costs in a meaningful way). This leads to an improved variant, where the data per client can belong to different clusters, and extensions of at the moment rare soft clustering schemes. The benefit is evaluated in both, comparative studies and ablation studies. A comparably long appendix addresses how to compute an EM scheme based on the costs, how to design data, what happens for linear parts, and some more insight.

### Strengths
The article addresses the important problem of efficient federated learning in the presence of data shift. 
It provides a very detailed experimental analysis. 
It also takes some effort to substantiate the observations with theoretical insight. 
Moreover, the authors promise to release the code open source.

### Weaknesses
The proposal left me a bit puzzled, as the specific contribution is somewhat unclear. On the one hand, the contribution promises a general framework/principle how to model FL with clustering. Here, the costs are rather obvious, as is the four-tier modeling, given the existing work how to model clustering; hence I am not sure what exactly is the contribution, is it the specific way of implementation, or specific guarantees which can be given? In how far is this modeling surprising/challenging and what exactly is the contribution, please specify (eg is it the better implementation? It would help if you could either provide specific benefits which arise from there which would not have been possible without this abstraction, or to provide examples where it is not obvious that the method falls under this common framework. 

The improved version allows the individual assignment of data of one client. Here an according EM scheme is derived (a bit lengthy but straightforward), soft clustering is considered (which seems also straightforward given the existing work on soft clustering and its algorithms). Personally, I find the definition of a new way to measure distances w.r.t. drift most interesting, albeit very shortly presented. Here references to existing technologies how to deal with drift are missing (such as decomposition of sets of data with drift into some where the drift is homogeneous, e.g. moment trees and Kolmogorov trees). I suggest to have a closer look at the (exhaustive) literature on learning with drift in the incremental setup. 

I find the presentation suboptimal as the main part of the work reads almost trivial in wide parts, whereas some important insight seems to be hidden in the appendix. It would help if the main take aways of the appendix would be highlighted. Moreover (as already said before), please more clearly highlight why the holistic framework is not trivial, and benefitial with specific non-trivial results/examples.

### Questions
What is the overall objective of FL in a learning theoretical sense, i.e. how exactly would the generalization error which is targeted be expressed?
What would be naturally occurring drift/shift in  such scenarios and how does this match with the shift modelled in experiments?
What are results if the clustering itself is evaluated (eg having ground truth on the data distributions)?
How personalized are the models? And how does this scale with the required number of data as regards valid generalization?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces HCFL, a holistic framework for Clustered Federated Learning (CFL) that integrates existing methods. HCFL+ builds on this by addressing key challenges in HCFL, improving the effectiveness. Extensive experiments show the effectiveness of the proposed method.

### Strengths
The problem is well motivated and interesting. The algorithm proposed is novel, with solid theoretical analysis and extensive experimental studies. The paper is well structured and written.

### Weaknesses
For clustered based FL algorithm, there is a recent work [1] to conduct clustering based on the inferred label distributions. The authors are suggested to discuss about this clustering strategy.

Could the authors provide more experiments on a wider range of beta (e.g., from 0.1 to 1.0), to show the effectiveness on different levels of data heterogeneity?

Also, there are setups such as C=2,C=3 in [1]. Such settings are also suggested to be studied. If the proposed algorithm can perform well across various data heterogeneity partitions, the paper can be stronger.

### Questions
Please see weaknesses. Generally, I think this is a solid work. I will adjust the score based on author response.

### Soundness
3

### Presentation
3

### Contribution
3
