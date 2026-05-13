# HiBO: Hierarchical Bayesian Optimization via Adaptive Search Space Partitioning

- Decision: Reject
- Scores: 6, 8, 6, 5, 6

## Abstract
Optimizing black-box functions in high-dimensional search spaces has been known to be challenging for traditional Bayesian Optimization (BO). In this paper, we introduce HiBO, a novel hierarchical algorithm integrating global-level search space partitioning information into the acquisition strategy of a local BO-based optimizer. HiBO employs a search-tree-based global-level navigator to adaptively split the search space into partitions with different sampling potential. The local optimizer then utilizes this global-level information to guide its acquisition strategy towards most promising regions within the search space.  A comprehensive set of evaluations demonstrates that HiBO outperforms state-of-the-art methods in high-dimensional synthetic benchmarks and presents significant practical effectiveness in the real-world task of tuning configurations of database management systems (DBMSs).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work aims to improve the performance of approaches such as Trust Region Bayesian Optimisation (TuRBO) over higher dimensional search spaces by employing a meta algorithm that partitions the search space into more or less promising regions (in terms of containing the optimum). The main result is that the proposed meta algorithm outperforms vanilla TuRBO and other baselines (e.g., GP-based BO) for a variety of benchmarks over synthetic datasets as well as a real-world relational database tuning task. While the proposed approach appears to be more of a meta algorithm, it is empirically only explored paired with TuRBO.

### Strengths
S1. Originality: Simple but well-thoughtout ideas for well-motivated problem.

S2. Originality/Significance: Promising empirical results that indicate significant performance improvements over a variety of benchmarks.

S3. Clarity/Quality: Great figures illustrating main ideas and paper easy to follow; relevant works seem to be discussed and compared against.

### Weaknesses
W1. Significance: While the empirical results are promising, theoretical results have not been explored despite a simpler approach.

W2. Limitations: Empirical study could focus more on identifying instances where HiBO struggles.

W3. Significance: Empirical study of proposed approach limited to using TuRBO as a local optimizer.

### Questions
Q1. What made developing the approach challenging and what kind of theoretical properties could potentially be derived?

Q2. What are limitations of the approach and in which settings would it be expected to perform worse?

Q3. What other local optimisers could in HiBO be used instead of TuRBO and do they also get a performance boost when used with HiBO instead of just on their own?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes HiBO, an algorithm that performs Bayesian optimization over high-dimensional spaces in a hierarchical manner, in which a global navigator adaptively partitions the search space into partitions with diverse sampling potential and a local Bayesian optimizer integrates global-level partitioning information to guide its acquisition strategy towards promising search space regions and hence accelerate the convergence to a local optimum. The proposal is shown to perform better than a selection of previous methods on synthetic data and is also applied to tune database management systems.

### Strengths
S1. Reasonable and well-argued proposal.
S2. Adaptive partitioning strategy appears to be novel in this context of exploration/exploitation.
S3. Experimentation on synthetic and real benchmarks.

### Weaknesses
W1. Ignores previous work on exactly the same topic of hierarchical Bayesian optimization.
W2. Ignores previous work on exactly the same application area of database tuning.
W3. Missing rationale and justification on the inclusion and exclusion of related works.

### Questions
The paper makes an interesting proposal and dives into the domain of adaptivity perhaps more than previous work has done.
However, the paper falls short in terms of its relationship to related work in two respects:

1. The notion of Hierarchical Bayesian Optimization Algorithm has been introduced by Pelikan and Goldberg in Hierarchical Bayesian Optimization Algorithm. Scalable Optimization via Probabilistic Modeling 2006: 63-90. The present paper does not discuss its relation to this precedent.

2. The assessment of DBMS knob tuning does not feature the most recent works in the area, by Zhang et al., even though these works are duly cited.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper tackles the problem that Bayesian Optimization methods do not scale well in high-dimensional search spaces (cf. curse of dimensionality) without structure. In this context, the authors propose HiBO, a hierarchical Bayesian Optimization approach that uses global-level space partitioning information to guide the acquisition strategy of local BO modelling – which is based on the TuRBO framework of Eriksson et al. (2019) -- more effectively regarding sampling efficiency. 

Several numerical experiments including synthetic benchmarks as well as database tuning problems are performed and results are compared to different baseline solutions.

### Strengths
S1 The considered problem is interesting and relevant.

S2 The paper is technically sound and overall well-written.

S3 The methods used are suitable.

S4 The evaluation and comparison against baselines is convincing.

### Weaknesses
W1 The required computational costs and scalability remain somewhat unclear.

W2 It remains unclear whether and which hyper parameters have to be tuned.

W3 Limitations of the paper’s methods could be better discussed.

### Questions
What are the required computational costs?

Does the approach scale?


Which hyper parameters are required (e.g. C_p, see line 263)?

How are they automatically chosen/tuned?


Minor comments:

- line 054: that integrate -> that integrates

- line 084: x and X are not defined

- line 264: What is the set for index p? Does it depend on j?

- line 316: Which sets belong to i, j, and j’?

- the references are not consistent (lower/upper case)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents HIBO, a hierarchical algorithm for optimizing black-box functions in high-dimensional search spaces. HIBO enhances traditional Bayesian optimization by incorporating global search space partitioning into the local acquisition strategy. It outperforms state-of-the-art methods on synthetic benchmarks and demonstrates effectiveness in real-world applications, such as database management system configuration tuning.

### Strengths
S1. The core concept is straightforward and comprehensible.
S2. The topic addressed is intriguing and relevant to current industry needs.
S3. Experiments show the method outperforms existing solutions, proving its effectiveness.

### Weaknesses
W1. The motivation is unclear. It is not evident what the challenges are in introducing structural information of the hierarchy. What are the criteria for optimally utilizing the so-called structural information?
W2. Although this paper dedicates considerable space to discussing the integration of partitioning information, its novelty is limited. Many existing techniques are well-known, which undermines its originality.
W3. There are few real-world experiments, making it difficult to support the claims about black-box functions.

### Questions
Q1. The paper mentions that the HIBO algorithm outperforms existing methods in high-dimensional search spaces. Could you specify its performance improvements across different dimensions?
Q2. When introducing the HIBO algorithm, it mentions using a search tree for space partitioning. Does this approach encounter issues with excessive computational complexity when handling large-scale data? If so, how can this be addressed?
Q3. The HIBO algorithm combines global and local optimization strategies, so how is the optimal balance between the global navigator and the local optimizer determined in practical applications?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In the paper, the authors propose HiBo which uses a hierarchical search space partitioning algorithm to reduce the search space and then apply local BO-based optimizer to sample from the most critical regions. In addition, HiBo uses the upper confidence bounds to evaluate tree node’s sampling potential and hence balance to explorations and exploitations,

### Strengths
The paper studies an important problem of optimizing a black-box function in high dimensional space. 

The overall concept is sound and intuitive, which serves as both a strength and a limitation, as many of the observations rely on heuristics amd emprical observations.

The idea of determining tree depth based on consecutive successes or failures is sound and interesting.

### Weaknesses
Why does HiBo reply on a binary serach tree instead of paritioning each level to multiple clusters? (like R tree) Also doe the serach tree need to be a balanced tree?

I find it challenging to fully appreciate Rule 1 and Rule 3. I think these rules make sense but the author should perhaps give better insights on these two rules.

In fact, one may argue that DBMS tunning is suitable for BO becuase the number of important knobs can be small?

Perhaps I missed it, but what is the workload in sysbench (read-only, write-only, mixed)?

Looking at the appendix C, I believe Table 3 oversimplifies the details, and presenting the results as percentages might not be the most effective approach. For instance, the table states that 'e HiBO introduces additional computational costs during the optimization phase compared to TuRBO, the increase remains minimal .. within 2%.' However, it also shows that the optim execution time increased by 1.5x when transitioning from depth 1 to HiBo. Table 3 should also include S-PITR scores since the claim is the adaptive tree has highest S-PITR score.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2
