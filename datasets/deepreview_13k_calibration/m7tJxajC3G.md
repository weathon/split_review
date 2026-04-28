# Federated Causal Discovery from Heterogeneous Data

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 5, 8, 5, 5

## Abstract
Conventional causal discovery methods rely on centralized data, which is inconsistent with the decentralized nature of data in many real-world situations. This discrepancy has motivated the development of federated causal discovery (FCD) approaches. However, existing FCD methods may be limited by their potentially restrictive assumptions of identifiable functional causal models or homogeneous data distributions, narrowing their applicability in diverse scenarios. In this paper, we propose a novel FCD method attempting to accommodate arbitrary causal models and heterogeneous data.
We first utilize a surrogate variable corresponding to the client index to account for the data heterogeneity across different clients.
We then develop a federated conditional independence test (FCIT) for causal skeleton discovery and establish a federated independent change principle (FICP) to determine causal directions. These approaches involve constructing summary statistics as a proxy of the raw data to protect data privacy. Owing to the nonparametric properties, FCIT and FICP make no assumption about particular functional forms, thereby facilitating the handling of arbitrary causal models. We conduct extensive experiments on synthetic and real datasets to show the efficacy of our method.git}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel constraint-based federated causal discovery method, FedCDH, specifically tailored for heterogenous data distributions mostly existent in FL. Novelty is twofold: Using summary statistics as a surrogate for skeleton discovery and introducing a surrogate variable to model distribution changes. The paper is very well written and shows promising results.

### Strengths
(1) Topic is very relevant causal inference and ICLR communities. 

(2) Nicely written paper with lots of background material and well-documented code.

(3) Federated causal discovery from heterogeneous data is challenging in theoretical and realistic experiment settings. 

(4) Ability to operate over general functional models.

### Weaknesses
(1) Communication cost for small sample size. The method relies on transmitting summary statistics, specifically covariance tensors, between clients and the central server. While this approach can reduce communication overhead for large datasets, the size of the covariance tensor, which is in $\mathbb{R}^{d'×d'×h×h}$, could become comparable to or even larger than the raw data when the sample size *n* is small, especially if the number of variables *d'* and the number of basis functions *h* are not small. This could negate the benefits of using summary statistics and potentially increase communication costs compared to directly sharing the raw data, especially when considering the overhead of constructing these tensors.

(2) Why have a maximum number of clients of 10? The experimental setup seems limited by the number of clients considered. While the method may be applicable to a larger number of clients, the experiments only explore up to 10 clients, which may not fully demonstrate the scalability of the proposed method in more realistic federated learning scenarios where the number of clients can be much larger.

### Questions
(1) Why the assumption " We set the sample size of each client to be equal." is required? Data heterogeneity can come in number of samples, too. Having unequal samples across clients is realistic.

(2) How the datasets are divided into clients is unclear to me.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the problem of federated causal discovery, where one wishes to recover the causal structure of some domain given datasets from multiple independent sources. The authors address this problem by proposing a procedure that leverages summary statistics, rather than individual observations, from each source. The work proposes KCIT, and in order to allow for the adaptation to the federated setting random fourier features are used for an approximation. The work also proposes a federated version of the individual change principle, also leveraging summary statistics. Empirical results are provided which show favorable performance.

### Strengths
This paper proposes a very sensible extension to existing work on conditional independence testing and the invariance condition to the federated learning setting. The authors lay out the proposed method well, and the approach is easy to follow and understand. In addition, the experimental results show nice performance in comparison to other methods.

### Weaknesses
In my view the largest issue with this method is that there are a few places that lack sufficient specificity. The authors use the kernel conditional independence test as a basis, but don't appear to specify the necessary assumptions on the underlying functional forms, same for the invariance principle. For example, while kernel methods are flexible, they still rely on assumptions about the smoothness of the underlying functions, and it's not clear if these assumptions are explicitly stated or justified in the context of the federated setting. It also isn't clear to me how we should expect the behavior of the federated approach to compare to its non-federate counterpart, e.g., what assumptions are necessary on the number of samples per domain? What is loss of power between the federate and non-federated tests? The authors appeal to random fourier features, which seems necessary (or at least some approximation appears to be necessary) but it isn't clear to me under which conditions we should expect this algorithm to not pay a price for this approximation. Specifically, how does the choice of the number of random Fourier features impact the approximation quality and the statistical power of the test? I certainly could be missing something, but the proofs provided appear to rely on large sample properties, but it's really unclear to me when those start to kick in, e.g. when should we expect the test to converge? How many samples before the summary statistics applied to the random Fourier features become a reliable representation of the underlying distribution for a given source?

### Questions
All of my questions are largely laid out above. In general, it would be good to get a sense of the finite sample behavior of the proposed method.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a constraint-based federated causal discovery method suitable for heterogeneous data. That is, the paper assumes different but related structural causal models at each client and seeks to discover the global structural causal model where local differences are modeled using domain-specific effective parameters for each variable and a set of domain-specific the pseudo-confounders. The paper proposes to use the Hilbert-Schmidt independence criterion and a (federated) independent change principle, based on the partial cross-covariance operator on a reproducing kernel Hilbert space, which captures non-linearities in the relationship of variables based on the chosen kernel. To make computations tractable, it approximates the kernel with random Fourier features. It shows that these criteria can be computed from summary statistics based on the kernel matrices.

### Strengths
- federated causal discovery is a relevant and interesting problem
- the method is well motivated and theoretically sound
- good empirical performance

### Weaknesses
 - the method requires that the different domains are known in the application



### Questions
**Questions:**
- why assume $L$ hidden confounders? How is L set in practice? Could we simply choose $d$ or $2^d$? In the theoretical evaluation, $L$ is assumed to be equal to the number of datapoints n which goes to infinity. Isn't that a problematic assumption, or did I misread the proof of Thm. 4?
- How does sharing local kernel matrices affect privacy?

**Detailed Comments:**
- The notation with bold $\mathbf{\psi}$ and normal $\psi$ is visually hard to distinguish.
- The formulation with an underlying causal graph and an augmented causal graph is not clear to me. For me it made sense to either assume an underlying "augmented" graph that captures local differences, or to assume an underlying graph and local interventions - these interventions are then modeled via the augmented graph. If the latter is the case, this should be clarified.
- Is it necessary to consider $\mho$ an observable variable? In the experiments, some additional information is used to decide the domain, but in general this is rarely possible. E.g., in [1] the domain is infered. What happens if you assumed that every client has a different domain and $\mho$ is the client index? 


[1] Mian, Osman, Michael Kamp, and Jilles Vreeken. "Information-theoretic causal discovery and intervention detection over multiple environments." Proceedings of the AAAI Conference on Artificial Intelligence, AAAI-23. 2023.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a novel FCD method attempting to accommodate arbitrary causal models and heterogeneous data. Specifically, they first utilize a surrogate variable corresponding to the client index to account for the data heterogeneity across different clients. Then they develop a federated conditional independence test (FCIT) for causal skeleton discovery and establish a federated independent change principle (FICP) to determine causal directions. These approaches involve constructing summary statistics
as a proxy of the raw data to protect data privacy. Owing to the nonparametric properties, FCIT and FICP make no assumption about particular functional forms, thereby facilitating the handling of arbitrary causal models. Extensive experiments on synthetic and real datasets could show the efficacy of the proposed method.

### Strengths
This paper features a detailed theoretical analysis and addresses a highly challenging problem.

### Weaknesses
This paper is relatively difficult to read, and it is not very comprehensible, making it not conducive for others to follow and reproduce the work. While the paper presents a list of theorems, the specific challenging problem being addressed is not clearly explained. The connection between the theorems (Theorem 4, 5, 6, and 8 in particular) and the overall contributions of the paper is quite ambiguous. For instance, it is unclear how the proposed summary statistics in Theorem 8 sufficiently represent all the statistics required for FCIT and FICP, and how this representation ensures the preservation of data privacy.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the problem of federated causal discovery from heterogeneous data, and proposes a novel constraint-based method called FedCDH, which can accommodate arbitrary causal models and heterogeneous data. It constructs the summary statistics to protect data privacy and further proposes federated conditional independence test (FCIT) and federated independent change principle (FICP) for skeleton discovery and direction determination. The experimental results on synthetic and real datasets show the efficacy of the proposed method.

### Strengths
1. The paper addresses the issue of heterogeneous data in federated causal discovery and relaxes the assumptions of causal models, which are critical problems.
2. The paper proposes a novel constraint-based method for effectively conducting federated causal discovery from heterogeneous data.
3. The paper provides detailed proofs for the presented theorems and lemmas. Extensive experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The paper conducts numerous experiments; however, it should provide a more in-depth analysis of the underlying reasons behind the experimental results, rather than just stating the observations. For instance, while the paper reports F1 scores and SHD, it lacks a discussion on why specific methods perform better or worse under certain conditions. A deeper dive into the characteristics of the datasets and how they interact with the proposed method would be beneficial. Specifically, the paper should analyze the impact of varying degrees of heterogeneity on the performance of different methods.
2. The section of method overuses symbols, leading to difficulties in understanding. The sheer number of symbols introduced, often without clear and consistent definitions, makes it challenging to follow the mathematical derivations and the overall logic of the proposed approach. For example, the use of multiple Greek letters and subscripts, while mathematically precise, can hinder the reader's ability to grasp the core concepts quickly. A more streamlined notation would greatly improve the clarity of the method section.
3. The presentation of this paper can be largely improved for clarification. The writing style is often dense and lacks intuitive explanations. The paper jumps between different concepts without providing sufficient context, making it difficult for the reader to follow the line of reasoning. For instance, the introduction of the surrogate variable and its role in the augmented graph could be explained more clearly and intuitively.

### Questions
1. In the penultimate paragraph of page 2, the authors say ‘Let k be the client index, and ℧ be the domain index’, what’s the difference between client and domain?
2. In the last paragraph of page 2, the authors say ‘When the data is heterogeneous, there must be some causal models changing across different domains. The changes may be caused by the variation of causal strengths or noise variances.’ The authors should better clarify what is the change of causal models.
3. In the first paragraph of page 3, ψ(℧) and θi(℧) are functions of ℧, and ℧ is a positive integer from 1 to k. Actually, ℧ is a value defined by the authors, and does it have an impact on the results when it takes different values?
4. In the fourth paragraph of page 3, as indicated by the authors, ℧ and Vi are connected by unobserved domain-changing variables ψ(℧) and θi(℧), so what does it mean of ‘If there is an edge between surrogate variable ℧ and observed variable Vi on Gaug’?
5. The authors should improve the presentation quality of the paper and fix typos. For example:
(1) In the second paragraph of page 5, ‘therefore, we would like to …’ -> ‘Therefore, we would like to …’.
(2) In the second paragraph of the Section of A6.4 Results of Computational Time, ‘The results are exhibited in Table A3.’ -> ‘The results are exhibited in Table A1’.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
