# TabGraphs: A Benchmark and Strong Baselines for Learning on Graphs with Tabular Node Features

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Tabular machine learning is an important field for industry and science. In this field, table rows are usually treated as independent data samples, but additional information about relations between them is sometimes available and can be used to improve predictive performance. Such information can be naturally modeled with a graph, thus tabular machine learning may benefit from graph machine learning methods. However, graph machine learning models are typically evaluated on datasets with homogeneous node features, which have little in common with heterogeneous mixtures of numerical and categorical features present in tabular datasets. Thus, there is a critical difference between the data used in tabular and graph machine learning studies, which does not allow one to understand how successfully graph models can be transferred to tabular data. To bridge this gap, we propose a new benchmark of diverse graphs with heterogeneous tabular node features and realistic prediction tasks. We use this benchmark to evaluate a vast set of models, including simple methods previously overlooked in the literature. Our experiments show that graph neural networks (GNNs) can indeed often bring gains in predictive performance for tabular data, but standard tabular models also can be adapted to work with graph data by using simple feature preprocessing, which sometimes enables them to compete with and even outperform GNNs. Based on our empirical study, we provide insights for researchers and practitioners in both tabular and graph machine learning fields.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, the authors aim to study the usefulness of introducing graphs while working with ML for tabular data. To bridge the gap between graph based ML (E.g. techniques such as GNNs, Deepwalk, etc.) and tabular ML methods (e.g. GBDT) - the authors propose to create a benchmark of graph datasets with heterogenous tabular node features across domains such as fraud detection, road networks, etc - with varying number of nodes, edges and other commonly studied graph based statistics. The authors then use the created benchmark to evaluate different ML methods and their combinations.

### Strengths
1. The authors propose multiple datasets which combine graph structure with tabular data -- specifically with heterogenous node data.
2. The authors compare a wide range of methods on the constructed benchmarks

### Weaknesses
1. The authors appear to ignore the graph based tabular datasets and tasks given presented concisely in the survey --  https://arxiv.org/abs/2401.02143 which survey prior works which have employed GNNs for tabular data.
2. While the authors state "If it is possible to define meaningful relations between data samples, it is worth trying to convert the given data to a graph and experiment with ML methods that are capable of processing graph information, as it can lead to significant performance gains" - and given its largely a benchmark paper - they do not propose a standardized mechanism or methodology to augment any table with graphs - largely limiting the novelty of the contributions. 
4. The analysis accompanying the results presented on the benchmarks also feel handwavy - "it is important to experiment
with different design choices" - seems to suggest - it is prudent for the downstream users to try every possible method and architecture, and therefore not providing a way to prune the search space of methods or architectures for a given dataset/ problem
5. As the paper notes, the graph methods proposed here are not novel and have been employed by works such as https://arxiv.org/abs/2004.05718 and others -- even for heterogenous node data - and therefore the paper lacks novelty from the method perspective as well.

### Questions
Please address the weaknesses section as applicable

### Soundness
2

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
5

### Summary
The paper introduces a benchmark to evaluate graph ML methods on tabular data with heterogeneous features. The paper hopes to bridge the gap between tabular and graph machine learning studies. It finds that while GNNs can enhance predictive performance, simple adaptations of standard tabular models could also work well.

### Strengths
- The experimental results are comprehensive. I appreciate the efforts from the authors to conduct experiments over 10+ baselines and 10+ datasets
- The paper cited a large number of related works, which helped the readers to know more about the field.

### Weaknesses
 - The problem setting is flawed. I do not agree that graphs with tabular node features are different from relational databases and can be redeemed as a new type of ML problem to work with. Indeed, the authors mentioned that "In contrast, our work is focused on single-table data with a single type of relationships between entities in the same table", and led the readers to Appendix C. But even after carefully reading the Appendix C, the paper still does not explain why the setting is different from a relational database with 2 tables (1 for the original table, the other for the additional relational information within the table). In that case, my understanding is that this paper is only a benchmark for relational databases with 2 tables, and only serves as a special case from the existing relational database benchmarks.
- Moreover, the authors did mention "Very recently, two benchmarks of large-scale relational databases have been proposed: RelBench (Fey et al., 2023) and 4DBInfer (Wang et al., 2024)." in the appendix. Given the high correlation with the proposed domain, they should be highlighted in the main paper and be thoroughly discussed, instead of hiding it within 1 sentence in the appendix. I'm not sure able the reason why the relevant discussions should not be mentioned in the main paper.
- The writing is a bit verbose. For example, the motivation in the introduction is weak. The first 2 paragraphs only introduce why we need tabular learning and graph learning, which is not relevant to the research problem in this paper.
- The paper makes little to none algorithmic contributions. Overall, I think this paper has not met the publication bar for ICLR.

### Questions
- Why does this paper not emphasize the high relevance of ML for relational databases? Why should relevant discussions go into the Appendix? The "Machine learning for graphs" paragraph in the related work took almost a page, but it is less relevant to ML for relational databases for this topic since the setting is essentially just a relational database with 2 tables.
- Why working with homogenous graphs a benefit, rather than a limitation? Extending homogeneous GNNs to heterogeneous GNNs only takes a few lines of code in PyG, and it makes the GNN model more expressive. I don't find homogeneous GNNs present benefits with heterogeneous GNNs.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper explores enhancing predictive accuracy in tabular machine learning by incorporating graph structures, proposing benchmarks to bridge the gap between heterogeneous tabular and homogeneous graph data features. Results indicate that graph neural networks boost the accuracy of tabular predictions, and simple graph-based enhancements can enable traditional models to effectively compete. Valuable insights are provided for both tabular and graph machine learning practitioners.

### Strengths
- **Research Topic.** The studied problem is interesting and practically important for tabular machine learning.

- **Experiments.** Experiments are carried out on 10 datasets with 18 baseline methods, which is quite solid. And there are also enough discussion.

### Weaknesses
 - **Lack of Novelty.** The concept of constructing graph datasets from tabular data is not novel and has been previously suggested in multiple studies.

- **Writing.** The initial paragraph in the 'Machine Learning for Graphs' section of the related works is excessively lengthy, potentially hindering readability. Besides, The main text should provide more details about how tabular data is represented as graph data. The absence of these details in the main text may lead to confusion among readers.


### Questions
- More discussion is needed on the differences between this paper and the previous paper on this topic.

- Why there are models that suffer from performance drop after utilizing PLR?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a benchmark for graph learning on single-table tasks(1 type of node and 1 type of edge), with heterogenous features. 
It constructs 11 tasks from 8 different datasets and ran experiments with GBDTs as well as GNNs on the tasks. 
The results show that GNNs outperforms GBDTs on the tasks authors proposed.

### Strengths
Overall the writing is good and the presentation is clear. 
The experiments the authors provide are extensive, including different types of models, tabular dl models, GBDTs, GNNs, etc.

### Weaknesses
The novel contribution is limited in this paper.

On page 2, the authors claimed that GNNs are typically evaluated on homogeneous features, but tabular learning typically has heterogenous features. I think they omit the work of PyTorch Frame (Hu, Weihua, et al. "PyTorch Frame: A Modular Framework for Multi-Modal Tabular Learning." arXiv preprint arXiv:2404.00776 (2024). ), which supports encoding heterogenous tabular data through deep encoders and can be used with PyG on downstream GNN tasks. It is good to include comparison to PyTorch Frame + PyG in your paper as it also fits into graph + heterogenous tabular data. 

The authors claim on page 4. "In contrast, our work is focused on single-table data with a single type of relationships
between entities in the same table.". However, it seems to me all the graph structure constructed by the authors can be represented by the graph structure in Relbench as well.

I also think the task type is too limited. Currently it only supports node classification and node regression. The authors did not mention link prediction tasks. Link prediction is a common tasks solved by GNNs and is offered by Relbench. It is unfair to say node level task is "the most common setting in modern graph machine learning".

### Questions
In the experiment section, the authors only compared the performance scores. I think it's also good to compare the runtime of the methods, as GBDTs can be much slower on larger datasets as compared to GNNs and tabular models.

The authors propose two types of tasks, node regression and classification. I'd like to see some other task types being covered, for example, multi-label classification, or link prediction. For example, in the hnm dataset, can you add a task to predict new items that will be co-purchases?

The authors should make proper comparisons to existing relational learning benchmarks RelBench and 4DBInfer.

Happy to raise the score if the authors can address all the three comments above.

### Soundness
3

### Presentation
3

### Contribution
2
