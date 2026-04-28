# Hierarchical Graph Learners for Cardinality Estimation

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Cardinality estimation -- the task of estimating the number of records that a database query will return -- is core to performance optimization in  modern database systems. Traditional optimizers used in commercial systems use heuristics that can lead to large errors. Recently, neural network based models have been proposed that outperform the traditional optimizers. These neural network based estimators perform well if they are trained with large amounts of query samples. In this work, we observe that data warehouse workloads contain highly repetitive queries, and propose a hierarchy of localized on-line models to target these repetitive queries. At the core, these models use an extension of Merkle-Trees to hash query plans which are directed acyclic graphs. The hash values can divisively partition a large set of graphs into many sets, each containing few (whole) graphs. We learn an online model for each partition of the hierarchy. No upfront training is needed; on-line models learn as the queries are executed. When a new query comes, we check the partitions it is hashed to and if no such local model was sufficiently confident along the hierarchy, we fall-back onto a default model at the root.  Our experimental results show that not only our hierarchical on-line models perform better than the traditional optimizers, they also outperform neural models, with robust errors rates at the tail.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a workload-driven approach for cardinality estimation aiming at workloads containig repetative queries. The proposal utilizes multiple templatizer to derive hierarchical cardinality estimation models, taking a query plan tree as input and obtaining data with different granularity. It employs general predictors like PostgreSQL to perform cardinality estimation at the lowest level.

### Strengths
- S1: The evaluation experiments used six types of workloads, including up to five-table join queries, and achieved a higher Q-error than MSCN (CIDR2019). It was confirmed that the fine-grained model, H1, achieved the fastest convergence in training and the highest accuracy.

- S2: Since machine learning-based methods often underperform in high-percentile cases, the fallback mechanism is beneficial in practice. As shown in Table 4, the deeper hierarchical fallback mechanism achieves a higher Q-error.

- S3: As a query-driven approach, the featurizer’s ability to characterize predicates is useful.

### Weaknesses
 - W1: In addition to Q-error, P-error should be also evaluated, which is becoming a standard metric.

- W2: As shown in Table 3, H1 demonstrates the highest performance, so a structure of H1 -> PostgreSQL seems optimal, making the multiple hierarchy setup (in Equation 15) unnecessary. The authors should clarify the benefit of using multiple hierarchy levels. 

- W3: Although the proposal adopts a workload-driven approach, recent trends favor data-driven or hybrid approaches. Notably, data-driven approaches have the advantage of robustness for unknown queries. Combining a workload-driven approach with data-driven methods could enhance accuracy in cases where prediction errors are large. While a workload-driven approach has the advantage of faster inference time, it is not obvious workload-driven approach alone is useful. 

- W4: In Section 2.5, the statement "All graphs whose templates are isomorphic share the same model" is based on graph isomorphism as defined in Definition 1, relying on edge information only. The templatizer, H1, thus does not use graph attribute information. However, Section 3.1 states, "Hence, query graphs found in the same H1 template differ only by the constant values," which appears contradictory.

- W5: Section 3.3 includes a calculation for the hash size, such as s(#T1), but according to Equation 6, the hash length is fixed at h, so the case distinction in Equation 10 does not seem valid.

- W6: Although Cardbench is used as the evaluation benchmark, it is proposed in an arXiv paper and is not yet a standard benchmark. It would be better to use the widely accepted join order benchmark or explain the strong justification for using Cardbench.

### Questions
- It is unclear how the plan tree is constructed. For example, is it correct to interpret that (A ? B) ? C and A ? (B ? C) are non-isomorphic plans?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a supervised cardinality estimation method that enhances accuracy for workloads with repetitive queries (i.e., queries repeated in templates with only the constant parameters changed) by leveraging hierarchical, online localized models. This approach transforms each SQL query into a Directed Acyclic Graph (DAG) representation, groups isomorphic DAGs into the same partition, and trains an online model for each partition as queries are executed. Grouping is conducted hierarchically at multiple levels of granularity, ranging from fine-grained (i.e., queries varying only in constant terms are placed in the same partition) to coarse-grained (e.g., queries varying only in constants, operator types, and column names are placed in the same partition). During runtime, given a query, the method begins with the fine-grained model and moves to coarser-grained models until it finds a confident model for the query. If no suitable model exists, it defaults to a learned or traditional model. Using the CardBench benchmark, the authors demonstrate that this method yields more accurate cardinality estimates compared to competitors such as PostgreSQL and MSCN.

### Strengths
S1. The authors tackle an important issue in analytical databases: cardinality estimation for repetitive queries.

S2. The authors propose a cardinality estimator, which leverages hierarchical localized models that are trained online.

### Weaknesses
W1. The Experiments section needs to be improved.
- The authors should compare their method with state-of-the-art (SOTA) data-driven cardinality estimation methods such as [1]. Currently, the comparison is limited to MSCN, a query-driven method proposed in 2019 [2], and PostgreSQL, a traditional estimator. This comparison is insufficient to demonstrate the superiority of the proposed approach against current best practices in learned cardinality estimation. Specifically, the absence of a comparison against a data-driven method trained on a large dataset limits the impact of the experimental results.
- The “Imperfect Admission Experiments” in Section 4 seems unfair, as the q-error percentiles of each method are reported on different query subsets: PostgreSQL is evaluated on the entire query set, MSCN on a subset excluding disjunctions, while the proposed method seems to be evaluated on a subset of simple queries (e.g., repetitive queries varying only in constant terms). This inconsistent evaluation makes it difficult to draw meaningful conclusions about the relative performance of the methods.
- The authors should report end-to-end time (including both planning and query execution time), as shown in [1,3], along with its breakdown for further clarity. This is crucial for understanding the practical implications of the proposed method, as the overhead of online model training and inference could outweigh the benefits of improved accuracy. The breakdown should include time spent on feature extraction, model lookup, model training, and inference.
- Reporting training time and model size would provide further insights into the method’s practical feasibility. The training time, especially for the online models, is a critical factor in determining the applicability of the method in dynamic environments. Similarly, the model size will impact the memory footprint and the overall scalability of the approach.
- The authors should clarify why the q-error is higher in certain intervals with larger training sample sizes in Figure 4. This counter-intuitive behavior needs to be explained to ensure the validity of the experimental results. The lack of explanation raises concerns about the stability and reliability of the proposed method.
- The experimental setup requires a more thorough explanation, particularly regarding how query repetitiveness was generated and its extent. The authors should provide details on the workload generator, the distribution of query templates, and the number of constant variations used to generate the repetitive queries. Without these details, it is difficult to assess the generalizability of the results.

W2. Motivation is inadequate.
- The authors should explain why existing learned estimators struggle with repetitive workloads to highlight the necessity for their proposed method. It is not clear why existing methods, especially those that use neural networks, cannot adapt to repetitive query patterns. A detailed explanation of the limitations of existing methods in this specific context is needed.
- The authors should clarify why a hierarchical model structure is effective in improving the accuracy of cardinality estimation. The rationale behind using a hierarchy of models, ranging from fine-grained to coarse-grained, is not sufficiently explained. The authors should provide a theoretical or empirical justification for this design choice.

W3. The presentation needs to be improved.
- The process of generating a DAG from a query needs further explanation. If the DAG refers to a query plan, the authors should specify which query plan is used, as multiple plans can exist for a single query. The authors need to clarify whether they are using a logical or physical plan, and how the plan is generated. The impact of different query plans on the DAG structure should also be discussed.
- There are some undefined terms, such as d_{\psi} in Section 2. The lack of definition for this term makes it difficult to understand the feature extraction process.
- There are inconsistent notations throughout the paper. For instance, “query graph” and “query plan” are used interchangeably. This inconsistent terminology creates confusion and makes the paper harder to follow.
- Numerous typos appear throughout the paper, such as “geoping” and “hases” in Section 5. These typos detract from the overall quality of the paper and suggest a lack of careful proofreading.

W4. There are some misstatements regarding existing work
- The authors seem to overstate the limitations of existing methods. They claim that “NN-based estimators perform well if they are trained with large amounts of query samples,” which is true specifically for query-driven learned estimators, not all NN-based methods. This statement is too broad and does not accurately reflect the capabilities of all neural network-based cardinality estimators. The authors should be more precise in their claims.
- The authors state that “50% of the real world clusters have more than 90% queries repeated in templates (only changing the constant parameters),” citing [4]. However, according to [4], the correct value is 80%, not 90%. This misrepresentation of the cited work undermines the credibility of the authors' claims.

### Questions
Please refer to W1-W4.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the issue of repeated queries in cardinality estimation, this paper proposes an on-line cardinality estimation method. Unlike traditional cardinality estimation approaches that rely on a single model, this study introduces a hierarchical cardinality estimation framework. Queries are categorized into three levels, with different structural classifications applied at each level. For each level, distinct estimator models are trained based on various classification templates, and evaluations are conducted hierarchically. Additionally, these models utilize an extension of Merkle-Trees to hash directed acyclic graph (DAG) query plans. Finally, an ensemble learning method is used to statistically aggregate the results and produce the final cardinality estimates. Compared to traditional cardinality estimators and the query-based cost estimation method MSCN, this approach achieves superior results.

### Strengths
S1. Hierarchical cardinality estimation methods have significant advantages for cardinality estimation methods in the presence of a large number of repeated queries. They allow for the training of separate cardinality estimators for each query type, thereby saving training costs and improving the accuracy of cardinality estimation.
S2. The method presented in this paper demonstrates strong cardinality estimation performance, and it also exhibits good convergence stability through hierarchical training.
S3. Compared to traditional cardinality estimators, the method proposed in this paper achieves faster convergence speed with lower overhead, making it suitable for practical industrial applications.

### Weaknesses
W1. This paper employs only the Q-Error as an evaluation metric, which can assess the stability of the cardinality estimator but does not provide an intuitive measure of its accuracy. The addition of mean absolute error (MAE) and relative prediction error (RPE) would allow for a more comprehensive evaluation of the accuracy of different cardinality estimators.
W2. This paper compares only with two relatively outdated query-based cardinality estimation methods, MSCN and MSCN+. It should include a broader variety and greater number of baseline methods by introducing more advanced cardinality estimation approaches. Adding comparisons with data-driven cardinality estimation methods or experiments against paradigmatic methods like QueryFormer would enhance the analysis.
W3. The experimental workload in this paper lacks clarification regarding query redundancy. It should include comparative experiments under different workloads. Additionally, experiments on cardinality estimation with lower query redundancy should be added to provide a more comprehensive evaluation.

### Questions
Q1. The addition of mean absolute error (MAE) and relative prediction error (RPE) would allow for a more comprehensive evaluation of the accuracy of different cardinality estimators.
Q2. It should include a broader variety and greater number of baseline methods by introducing more advanced cardinality estimation approaches. Adding comparisons with data-driven cardinality estimation methods or experiments against paradigmatic methods like QueryFormer would enhance the analysis.
Q3. It should include comparative experiments under different workloads. Additionally, experiments on cardinality estimation with lower query redundancy should be added to provide a more comprehensive evaluation.
Q4. Could you clarify what specific models are used at each level of cardinality estimation in this paper? This detail is not adequately explained in the manuscript.

### Soundness
3

### Presentation
2

### Contribution
2
