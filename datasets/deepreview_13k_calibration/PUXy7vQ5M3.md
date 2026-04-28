# Benchmarking the Fidelity and Utility of Synthetic Relational Data

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Synthesizing relational data has started to receive more attention from researchers, practitioners, and industry. The task is more difficult than synthesizing a single table due to the added complexity of relationships between tables. For the same reason, benchmarking methods for synthesizing relational data introduces new challenges. Our work is motivated by a lack of an empirical evaluation of state-of-the-art methods and by gaps in the understanding of how such an evaluation should be done. We review related work on relational data synthesis, common benchmarking datasets, and approaches to measuring the fidelity and utility of synthetic data. We combine the best practices and a novel robust detection approach into a benchmarking tool and use it to compare six methods, including two commercial tools. While some methods are better than others, no method is able to synthesize a dataset that is indistinguishable from original data. For utility, we typically observe moderate correlation between real and synthetic data for both model predictive performance and feature importance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a benchmark for evaluating synthetic data generation techniques specifically designed for relational data. Notably, it introduces a method to assess synthetic data generation based on fidelity metrics and reports benchmark evaluation results on existing relational data generation techniques.

### Strengths
Establishing benchmarks for synthetic relational data generation is an interesting contribution, particularly with a focus on fidelity and utility as critical evaluation metrics.

### Weaknesses
 - W1: While the focus on benchmarking is indeed valuable, the evaluation experiments on the proposed benchmark and existing techniques appear insufficient. Specifically, in Table 1, the comparison between statistical cardinality and the proposed approach is discussed only briefly in Section 4.3, with only around four lines of explanation, leaving the analysis of the proposed method’s advantages underdeveloped. I suggest the authors redesign the whole experiment section to have a new question, such as "Q1: Is the proposed benchmark more effective than SOTAs?". The current discussion lacks a rigorous analysis of why the proposed benchmark is superior, especially given that the core idea of using a classifier to distinguish between real and synthetic data is not entirely novel. The authors should provide a more in-depth analysis of the specific advantages of their approach over existing methods, potentially by including more diverse datasets or by conducting a more thorough ablation study.

- W2: Although the primary purpose of the paper, as stated in Chapter 1, is **privacy protection**, it does not assess some major approaches in this field, such as relational data generation using differential privacy. I would suggest the authors either 1) to add several existing data generation techniques based on differential privacy, or 2) to explain why you exclude these techniques in spite of claiming privacy protection is the benefit of synthetic data generation. Some SOTAs based on differential privacy are as follows:
  - J. Yang, P. Wu, G. Cong, T. Zhang, and X. He. “SAM: Database generation from query workloads with supervised autoregressive models.” In SIGMOD, 2022.
  - K. Cai, X. Xiao, and G. Cormode. “Privlava: Synthesizing relational data with foreign keys under differential privacy.” SIGMOD, 1(2), 2023.
 The absence of differential privacy methods is a significant oversight, given the stated importance of privacy. The authors should clarify whether the focus of the benchmark is solely on fidelity, or if privacy is also a consideration. If privacy is a goal, the benchmark should include methods that explicitly address it, and the evaluation should include metrics relevant to privacy, such as differential privacy guarantees or membership inference attack success rates.


- W3: The paper places a heavy emphasis on fidelity, with only limited evaluation of utility, creating an imbalance. Since the tile and abstract claim that fidelity and utility have the same importance in benchmarking synthetic data generation, the experiment of benchmarking should also have similar importance over fidelity and utility. For instance, granularity (single-column, single-table, multi-table) is extensively examined with regard to fidelity, taking up considerable space in the experiments, while utility is assessed only for single-table input, with a relatively small space devoted to these experiments. I would suggest adding more experiments for utility evaluation: 1) using regression/classification for estimating different attribute values, and/or 2) joining different numbers of tables and using them as input to train the models. The current utility evaluation is not comprehensive enough to justify the claim that the benchmark equally considers fidelity and utility. The authors should expand the utility experiments to include more complex tasks that involve multi-table data, such as predictive modeling on joined tables or tasks that require understanding relationships between tables.

- W4: The proposed method in Section 3 appears relatively simple, so its novelty is not clear. In detail, Algorithm 1 simply trains the model to discriminate the original data and (derived) synthetic data using the Binominal test, which is just a standard technique. Also, the extension to multi-table in Section 3.2 is quite simple, in that it utilizes simple aggregation from child tables. The method, while functional, lacks significant innovation. The core idea of using a classifier to distinguish between real and synthetic data is not new, and the extension to multi-table data using simple aggregations is not particularly sophisticated. The authors should clarify the novelty of their approach, perhaps by highlighting specific aspects of their implementation or by demonstrating how their method overcomes limitations of existing approaches.
- W5: Issues with readability and consistency:
  - Several graphs in the experimental section lack descriptions on the X and Y axes.
  - In Figure 2, the description “Most methods model the parent table (store) better since the tests find more differences for the child table (historical)” applies to (b) but not to (a).
  - Inconsistencies exist between Section 4.5 (first and third most important features) and Figure 5 (1st and 4th most important features).

### Questions
- Q-error is a standard measure for evaluating record count accuracy in query results, but this paper does not adopt Q-error. What is the reason for this?
- Although the paper asserts the importance of machine learning utility, machine learning models typically only handle single-table structured data as input. Conversely, the paper emphasizes the importance of multi-table data generation, creating a potential inconsistency in its argument. How does the paper propose to input multi-table data into machine learning models? Additionally, how is the input data prepared from multiple tables for Section 4.6?
- The phrase “generating child rows conditionally on parent rows” implies a propagation of information to the parent side. However, the paper associates this with “propagating errors down the hierarchy,” referring to propagation to the child side, which seems inconsistent.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
As pointed out by the authors, the use of synthetic relational data is
attractive as it can help to preserve the privacy of the original
data, and it can help to alleviate the scarcity of data. Of course, to
help with these problems and be useful, the synthetic data has to
preserve some properties of the original data. This is an old problem
that has been studied in the database area; in particular, in this
context, the type of properties one would like to preserve in the
synthetic data are related to the complexity of evaluating certain
classes of queries in the real and synthetic scenarios. However, what
is new in the scenario presented in this paper is that an ML model is
going to be trained on the synthetic data to later make predictions on
the real data. Hence, the synthetic data has to preserve the structure
of the real data that allows the ML model to make accurate
predictions on the real data.

The main aspects used to measure the quality of synthetic relational
data are fidelity and utility. The former refers to how close the
synthetic data is to the real data, while the latter refers to how
well an ML model would perform on a prediction task over the real data
if the real data is replaced by the synthetic data. In this paper, the
authors propose a synthetic relational data benchmark, which combines
known techniques to measure fidelity and utility with a new general
approach to measure fidelity for relational data. Moreover, the
authors use this approach to compare known methods for synthesizing
relational data.

### Strengths
S1) The authors present a fairly general framework to compare methods
for synthesizing relational data.

S2) The paper presents an experimental evaluation where the proposed
framework is used to compare known methods for synthesizing relational
data. This evaluation provides useful information about these methods.

### Weaknesses
W1) The general approach to measure fidelity with discriminative
detection can be understood. However, the notion of relational data
used in the paper is not properly formalized.



### Questions
The notion of relational data used in the paper is not properly formalized.

- The authors mention that the datasets used in the paper are
  organized based on the structure of their relational schema. For
  example, they mention that AirBnB uses only linear relationships,
  which means one parent and one child table. But they do not indicate
  how the parent-child relationship is defined between tables. Is this
  relationship defined considering the foreign keys in the tables?

- A foreign key for the table T_i is defined p_{T_j}, T_i ~ T_j. I
  assumed this foreign key is defined with respect to the primary key
  of the table T_j, since this foreign key is defined for T_i. But
  which attributes of T_i participate in this dependency? The notation
  has to include this information.

- A row of a table is defined as a set of values. Since a set is not
  ordered, how do you know what is the value of an attribute of the
  table in this row?

- The authors indicate that if {a_1^{T_i}, ..., a_l^{T_i}} are the
  attributes of a table T_i, then a row of this table is a set of
  values {v_{p_{T_i}}, v_{k_1}, ..., v_{k_o}, v_{a_1^{T_i}}, ...,
  v_{a_l^{T_i}}}. I assume that v_{a_j^{T_i}} is the value of
  attribute a_j^{T_i}. But then I do not understand what the other
  values are, as they do not correspond with the attributes of the
  table.

### Soundness
3

### Presentation
3

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
Experimental study that benchmarks various tools for generating synthetic relational data for a given source database. Uses standard approaches for single-table quality assessment (with straightforward but important modifications) and proposes a new approach for multi-table quality assessment. The main takeaway for me is that even single-table assessment fails with current data generation methods.

### Strengths
S1. Independent assessment and comparison of various synthetic data generation tools is a valuable contribution.

S2. The proposed "discriminative detection" for single-table assessment is a common, useful baseline approach.

### Weaknesses
W1. Technical novelty low. For single-table assessment, the proposed "discriminative detection" method is standard practice, as it amounts to training and evaluating a discriminator for real vs. synthetic examples. According to the authors, in the field of assessing synthetic relational data, prior work only used logistic regression as a discriminator. Although I find this hard to believe (e.g., some synthesis methods are GAN-based), I agree that that's took weak. For multi-table assessment, the proposed method is neither well-presented nor well-argued for. It computes/compares count and value statistics over joins, but it's not clear (i) why this is a good idea in the first place and (ii) which joins and which statistics should be used. For hierarchical data, it seems to modify the denormalization approach mainly by adding aggregation, but why/how does this actually lead to an improvement? Moreover, the approach seems to be basic and ignores the complex schemata of real relation data. As this is a benchmark paper, technical novelty is not a critical metric for assessment, but I include it here because the paper presents them as contributions.

W2. Insight low. I am not sure what I learned from this paper other than that even single-table assessment methods fail for the tested synthesizers. First, assuming that this wasn't known before already, the main reason must have been that a too weak model (logistic regression) was used as discriminator. That's a valuable insight, but it relevant to members of the subfield mainly, not the machine learning community as a whole (we know this). Second, given that single-table assessment already fails, doing multi-table assessment is not really helpful; it will also fail. In order to gauge the usefulness of the proposed aggregation method empirically, we want it to produce insights in cases where single-table assessment doesn't fail already. Third, the paper reports a large number of empirical results in tables and figures, but no further analysis, deeper discussion, or suggested next steps.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the challenge of relational data synthesis by introducing a general approach termed 'discriminative detection' to evaluate the fidelity of various relational data synthesis algorithms. The authors compare several recent solutions, including those utilizing Generative Adversarial Networks (GANs), and conduct an experimental study to assess the performance of these methods across different datasets.

### Strengths
The paper presents a good vision for establishing a benchmark that effectively evaluates both the fidelity and utility of synthesized relational data. Additionally, the initiative to define a generic metric is commendable, as it enhances the framework for assessing various synthesis methods.

### Weaknesses
The paper has several key weaknesses:

W1. Limited Identification of State-of-the-Art Methods: The authors only reference a few papers and overlook recent works exploring GANs and diffusion models for tabular data synthesis. For example, the VLDB Journal 2024 article below systematically analyzes the design space of tabular data synthesis using GANs, while studies like 'TableDiffusion' also utilize diffusion models. A comprehensive benchmark requires an up-to-date summary of SOTA methods.

- Tabular data synthesis with generative adversarial networks: design space and optimizations, VLDBJ 2024
- Diffusion Models for Tabular Data Imputation and Synthetic Data Generation (https://arxiv.org/pdf/2407.02549)

W2. Unclear Claims about Related Work: The statement regarding the lack of accessible APIs or source code for related studies is ambiguous. Notably, source code for significant works, such as the mentioned GAN paper and others that combine diffusion models, is publicly available. This oversight suggests that the authors may not have fully explored existing resources.

- https://github.com/ruc-datalab/Daisy for the above VLDBJ paper
- Tabsyn (https://github.com/amazon-science/tabsyn) that combines a diffusion model and a VAE, 
- CoDi (https://github.com/ChaejeongLee/CoDi) also uses diffusion models
- and there are many more papers with code using GANs and diffusion models

W3. Insufficient Dataset Variety: A robust benchmark necessitates a wide array of datasets, yet this paper includes only five. In contrast, other studies, like the one on diffusion models, utilize ten datasets for evaluation, indicating that the current work lacks adequate data diversity.

- Diffusion Models for Tabular Data Imputation and Synthetic Data Generation (https://arxiv.org/pdf/2407.02549)

W4. Neglect of Data Type Considerations: The paper does not address the critical distinction between numerical (or continuous) and categorical (or discrete) data in tabular synthesis. Different data types require tailored generation techniques, which is a significant oversight in the discussion.

W5. Generalization of Fidelity Metrics: The fidelity evaluation should be context-dependent; thus, the authors must justify how a single metric can effectively encompass diverse applications before proposing a general metric.

W6. Lack of a Consistent Conclusion: The paper fails to provide a clear and consistent conclusion that can effectively guide researchers and practitioners in applying the findings.

### Questions
Q1: How many relational data synthesis methods in each category should be considered sufficient to establish a robust benchmark? (Refer to Weaknesses W1 and W2)

Q2: What is the minimum number of datasets required to create an effective benchmark? (Refer to Weaknesses W3 and W4)

Q3: How can real-world applications be used to motivate or justify the choice of a generic metric, and what makes this metric suitable for various real-world applications? (Refer to Weakness W5)

### Soundness
1

### Presentation
2

### Contribution
1
