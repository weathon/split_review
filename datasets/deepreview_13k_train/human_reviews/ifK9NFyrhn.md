# Disconnecting The Dots: Creating Leakage-Free Protein Datasets by Removal of Densely Connected Data Points

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Biological systems arise through evolutionary processes that effectively render all biological data, at scales ranging from biomolecules to organisms, to be evolutionarily related. This poses a challenge to assessments of model generalization, as naive random splits do not safeguard against data leakage; all data points are in some sense related, and their degree of relatedness lies on a continuum. To address this challenge, various similarity metrics are typically used to cluster data prior to splitting to ensure dissimilarity of resulting partitions. However, as we show in this study, similarity thresholds that lead to well-behaved splits (large numbers of homogeneously sized clusters) must invariably be too permissive, thus only permitting assessment of weak generalization. Conversely, stringent thresholds that could in principle enable assessment of strong generalization typically fail to produce well-separated clusters, yielding one or a handful of very large clusters that span the entire dataset. Here, we propose a new data splitting methodology that optimally balances these competing considerations by relaxing the assumption that all data points must be retained. Instead, through a principled and judicious removal of highly central data points, our approach yields well-behaved data splits that enable assessment of extreme generalization regimes. We demonstrate its utility by investigating the impact of diverse proteins representations on protein function prediction. Our experiments confirm the robustness of our new methodology and provide insights into the utility and behavior of protein representations  under previously untested regimes of sequence and structure generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper is about splitting the data into training, validation, and test sets when a data set is not IID. The paper focuses on protein sequence data sets, where all existing sequences are sampled through evolution and related to each other. The paper acknowledges that this problem has been known in bioinformatics and that a typical way to address it is by creating validation/test sets such that their examples are not similar (using specific similarity thresholds) to examples in training data. The claim is that existing data splitting approaches in the protein domain do not find a good tradeoff between ability to evaluate model generalization and having enough representative data left for training. To address it, the paper proposes a new splitting method that identifies communities of proteins and removes proteins that are connectors between those communities. The new approach is evaluated on several representative protein prediction tasks.

### Strengths
+ The main strength of the paper is in a new way to split protein data sets aided by identifying communities of proteins. One the communities are identified and central proteins linking those communities are removed from data, it is possible to generate cleaner training-test splits that results in more diverse sets of training proteins. The proposed approach is well justified and sound.
+ The experimental evaluation is quite extensive, providing insights into the benefits of the proposed approach compared to the state of the art

### Weaknesses
 - The main weakness of this paper is that this is a relatively niche area for the ICLR community. While the contribution might be of practical interest to the bioinformatics research community, the methodological contribution (finding communities and removing central proteins prior to data split) is relatively minor for the machine learning community.
- A weakness related to the community finding approach is that it does not scale well (what is the computational cost, is it cubic in the number of examples?). As a results, the paper only evaluates the proposed splitting approach on relatively small data set (up to 30,000 proteins), although protein sequence data sets often go into millions.
- The paper does not provide convincing experimental results that the proposed split makes a large practical difference. The arguments provided are mostly of the qualitative nature.
- The paper claimed that the approach is "agnostic to the splitting strategy is the choice of similarity metric". This is an issue because the similarity metric is a key choice that can greatly impact splitting model training and evaluation. It would be good to see the evaluation using at least two different types of similarity metrics.
- The paper aims to improve on deepFRI partitioning, which does not remove central proteins after clustering (finding communities). But, deepFRI is only one of the existing splitting approaches, and one of the rare ones that results in leakage between training and test data. There are many other splitting methods that do not result in leakage.
- The concept of leakage is never clearly defined in the paper. It would be very useful to see what it means mathematically early in the paper.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

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
The paper addresses the issue of random splitting data in the context of cross validation for predictive tasks. The paper described the problem as data leakage and inflating reported generalization performance. The paper suggested the strategy as clustering data and then splitting among clusters. The paper described the root cause of the issue being biological data are generated by a universal evolutionary process that connects all known life on Earth and aims to improve fidelity of model assessment.

### Strengths
The motivation was very attractive, to address potentially inflated reported model generalization. And the paper attempted to solve the problem in generic way, ie. not specific to a given predictive task, or not specific to a type of data.
The proposed technique of detecting communities by removing highest degree of nodes is neat and well-motivated.

### Weaknesses
I found the motivation lacking evidence, how reported model generalization has been inflated. The paper tried to address a very challenging problem, ie. improve fidelity evaluation methods for generic predictive tasks. I expect the paper to provide more rigorous design how to quantify that the proposed scheme can make evaluation more trustworthy, or model performance generalizes better. Some notion of defining and quantifying model generalization performance would be useful to support the value of the proposed method.

In addition, I think the paper would be stronger if the paper can clarify, why being generated from evolutionary processes can be a problem when we split the data randomly – one suggestion would be to motivate from the specific tasks, for example, when a researcher needs high fidelity prediction of protein functions and has various tools in hand – how reported model performance can help the researcher.

Line 085: it is not clear why the temporal split is a problem for actual applications.

Line 161: missing reference and format errors

Line 193: some clarification would be useful to justify the assumption of an appropriate similarity metric exists; especially, such information used to calculate such similarity metric needs to not introduce data leakage as well for predictive tasks.

Line 235: format error

Line 366, Line 370, Line 519, I didn’t quite follow what results/metrics are relevant to support the claim that the proposed dataset construction pipeline provides an ideal framework for protein representation.

### Questions
Line 085: it is not clear why the temporal split is a problem for actual applications.

Line 161: missing reference and format errors

Line 193: some clarification would be useful to justify the assumption of an appropriate similarity metric exists; especially, such information used to calculate such similarity metric needs to not introduce data leakage as well for predictive tasks.

Line 235: format error

Line 366, Line 370, Line 519, I didn’t quite follow what results/metrics are relevant to support the claim that the proposed dataset construction pipeline provides an ideal framework for protein representation.

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
Note added on December 4: I appreciate the authors' careful replies to the reviews. However, the replies do not change my evaluation of the work.

Some of the replies highlight that the contribution to machine learning in general is limited. These include the assertion that discussing classification with a reject option is out of scope, the absence of a big-O analysis, and the fact that Algorithm 2 is due to previous research.

=============

All living things are related via evolution, so all biological objects such as proteins are related. Hence, it is impossible to create training/test data splits where test objects are unrelated to training objects. This submission proposes a new heuristic algorithm to create clusters that are reasonably unrelated to each other. Training and test sets can then be based on clusters.

### Strengths
This paper is written well and is understandable and sensible. Originality is fair relative to previous work, which is cited comprehensively AFAIK. Quality is good, with no obvious mistakes; so is clarity.

### Weaknesses
Originality, quality, and clarity are adequate. Significance is limited. First, there is no claim of significance outside computational biology, so the importance for machine learning and ICLR is weak. Second, the algorithm is heuristic and not very surprising. Third, within computational biology, the method does not lead to any actually more successful predictive method. Rather, it confirms two facts that are  well-known already: "structure-based splits present a significantly more challenging test than sequence-based splits and ... protein function prediction remains an unsolved task."

Overall, this paper should be published in a specialized computational biology venue, perhaps an ICLR workshop.

### Questions
054: There is an opportunity to make this research deeper and broader: formulate these three desiderata as axioms in the style of Arrow or Shapley. Then derive something like Arrow's impossibility theorem, or Shapley values.

Separately, discuss explicitly what the goals are when creating training and test sets. Is the concept of IID (independent and identically distributed) relevant or not? Is there a conflict between *measuring* generalization and *achieving* it? (There is always at least some conflict, because the best generalization is presumably achieved by training on all available data, with no data left out for testing.

Most learning methods have hyperparameters which are chosen using a validation set. Discuss three-way splits: training, validation, test.

057: For relevance to machine learning in general, cite and discuss briefly the relationship to classification with a reject option. Also discuss how the need arises outside comp bio to make training and test sets genuinely separate. Note that there is a large literature on removing leakage from benchmarks for LLMs.

083: This paper does have citations older than a few years, but would be more scholarly and thoughtful with more. For example, the temporal approach to leakage prevention was used for decades by the CASP contests, and has been used for decades in finance.

213: Algorithm 1 mentions three concepts with different names: communities C, connected components K, and clusters (line 250). Algo. 2 line 12 reveals that clusters are actually a different name for K. Still, what is the conceptual difference between communities and clusters? Why doesn't Algorithm 1 merely return C with the top connector nodes v removed?

229: Provide a big-O complexity analysis.

270: Explain the need for Algorithm 2. Why must many different thresholds be used?

Nodes and edges are removed in five different places: Algo. 1 line 12 and Algo. 2 lines 10, 14, 17, 21. Why so complicated, especially given that the algorithm is heuristic without guarantees?

448: Figure 3 shows that the biological reality is one single large connected component. Conceptually, a learning algorithm should be able to learn and exploit this reality. The picture on the right is "fake news" that may be helpful for measuring generalization, but unhelpful for *achieving* generalization. Note that domains other than comp bio also have a reality with one main connected component and many tiny components, in particular social networks such as Facebook.

Figure 18: Spearman correlations are not appropriate for data that is so obviously nonlinear.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel approach for creating data splits in biological datasets, to avoid data leakage to support generalization testing. The paper introduces a data-splitting methodology that strategically removes highly connected/central data points to produce well-balanced, disconnected clusters, which should allow for strong generalization assessment. The authors evaluate the proposed method by examining how various protein representations influence protein function prediction.

### Strengths
- The paper introduces a novel data-splitting methodology that strategically removes highly central data points to achieve well-separated, leakage-free clusters. 
- The study rigorously tests the proposed method across different models. Although tests for other biological tasks are missing.
- Both sequence and structure based splits are considered

### Weaknesses
 - The authors mention that the new clustering approach results in a data loss of around 12.4% under structural similarity and 1.4% under sequence similarity. This level of data exclusion is significant, I feel like a more detailed section about this tradeoff is missing from the paper. Specifically, the paper lacks a discussion on how the removal of central nodes impacts the overall dataset's representativeness, particularly for smaller protein families or less-studied proteins. The authors should provide a more rigorous analysis of the potential biases introduced by this data removal strategy.
- The paper places significant reliance on community detection for constructing data splits. However, community detection, even with the Leiden algorithm, can still produce groupings that do not align with true biological relationships. This is especially concerning when the underlying network is not a perfect representation of biological interactions or similarities. The paper should include a more detailed justification for why community detection is the most appropriate method for this task, and perhaps consider alternative clustering approaches.
- The results are mainly focused on protein function prediction within specific ontologies, leaving it unclear how the method performs across other prediction tasks or with more diverse biological data. The paper should include results on other tasks such as protein-protein interaction prediction, or protein structure prediction to demonstrate the versatility of the proposed method.
- The authors emphasize the importance of choosing a similarity metric in the introduction but do not elaborate on the available similarity metrics (e.g., sequence identity, TM score). These metrics should be defined in the paper, including the specific parameters used (e.g., alignment algorithm for sequence identity, TM-score calculation method). The lack of detail makes it difficult to reproduce the results.
- A complexity and runtime analysis of the proposed method is missing. This is a crucial omission, as it is important to understand the computational cost of the method, especially when dealing with large datasets. The authors should provide a detailed analysis of the time and space complexity of their algorithm, and ideally, compare it to existing methods.

### Questions
- How did the authors ensure that the removed data points did not disproportionately affect the diversity or representativeness of the dataset, especially for small protein families?
- Have the authors tested the proposed method on additional biological tasks to assess its versatility and generalization across tasks?
- What is the total time complexity of the proposed method?

### Soundness
2

### Presentation
2

### Contribution
1
