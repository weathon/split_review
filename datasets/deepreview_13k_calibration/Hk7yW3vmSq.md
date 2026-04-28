# Conceptual Graph Counterfactuals

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Conceptual counterfactuals refer to hypothetical scenarios involving changes in a
high-level conceptual representation. In the realm of XAI, conceptual Counterfac
tual Explanations (CEs) allow for more meaningful and interpretable modifications.
For instance, instead of explaining image predictions through superficial pixel-level
changes, the focus shifts to alterations in the underlying semantics. In this work,
we propose representing input data as semantic graphs to achieve more descriptive,
accurate, and human-aligned explanations. Furthermore, we introduce a model-
agnostic GNN-powered method to efficiently compute counterfactuals. We begin
by representing images as scene graphs and obtain appropriate representations
through GNNs to bypass solving the NP-hard graph similarity problem for all input
pairs, an integral part of the CE computation process. We apply our method to
widely-used datasets and compare our CEs with previous state-of-the-art explana
tion models based on semantics, including both white and black-box approaches.
We outperform both approaches quantitatively and qualitatively, as validated by
human subjects, specifically when the graphs contain numerous edges, highlighting
the significance of capturing intricate relationships. Given the model-agnostic
nature of our approach and the generalizability of the graph representation, this
method is successfully extended to diverse modalities and classifiers, including
non-neural models. Additionally, it is proven consistent across generated anno
tations, at least in the case of scene graph generation. Our approach is, to our
knowledge, the first to emphasize semantic graphs as a vehicle for CEs, allowing
the transition from low-level features to concepts. It uniquely leverages graph
matching GNNs as a XAI tool achieving efficient approximation and significant
acceleration in comparison to the exact Graph Edit Distance (GED) algorithm. It is
widely applicable and easily extensible, producing actionable explanations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work analyzes scene graphs built on semantic attributes of the data. In particular given a scene graph, this work proposes a method to identify the closest scene graph -- in terms of graph edit distance --- with a different label. Solving this problem is NP-hard and hence, this work adopts an approximate solution that uses a GNN. The GNN computes an embedding for each graph such that the distance between the embeddings of two graphs approximates the graph edit distance. The authors evaluate this method on a variety of datasets.

### Strengths
This works designs a novel solution to compute the closest scene graph with a different label. The work uses an simple and elegant solution to the problem that is similar to multi-dimensional scaling (MDS). 

The experiments highlight that their work empirically outperforms prior works like CVE and SC. Their proposed method finds graphs with smaller edit distance across different benchmarks. The human evaluators also prefer CEs and find them significantly easier to use them distinguish classes. The author also show that their method is significantly more efficient compared to computing the underlying GED.

### Weaknesses
 **Understanding the significance of this work: aren't counterfactual explanations used to understand model predictions?**
I am not an expert in this area so I am unable to accurately evaluate the significance of this work. I am unable to understand how these counterfactual explanations will be used. What kinds of insights can they provide and in what scenarios can they be used?

The counterfactual explanations in this work are model-agnostic which means that they cannot be used to understand  how models make predictions. However, I am only familiar with counterfactual explanations (see [1]) that help us understand why models have arrived at a particular decision. Can model-agnostic counterfactual explanations be used for other tasks?

**How do you generate the scene graph for each data point if it isn't available?**
Each data points requires a scene graph which may not be readily available. For example, CUB does not have a ground-truth scene graph and the authors are forced to construct one. As a result, the counterfactual explanations will change depending on how the graph is constructed. If this is the case, how should the graph be constructed in order to get the "right" counterfactual explanation? In this case, is modelling the scene graph the right thing to do?

Also, why is the graph edit distance a reliable way to measure the distance? Perhaps, editing should be assigned less weight compared to deletion when computing the distance.

**Quality of the model is limited by the quality of the labelled data.**
The labelled data uses an approximate algorithm to find the edit distance. As a result, the neural network will also approximate the sub-optimal solution and not predict the optimal answer. Are there ways to get around this hurdle?

**Why use cosine distance in Eqn 4, and why not use euclidean distance instead?**
Since the training objective is also based on the euclidean distance, wouldn't be a better distance measure to compute the nearest scene graph?

### Questions
1. **Why do we need a neural network? Why can't we just compute the ground-truth?** Isn't it possible to compute the ground-truth graph edit distance between all pairs of graphs instead of training a neural network to make these predictions. Since we need to create a lot of training data, why can't we compute graph edit distances for the entire data by throwing lots of compute at the problem? 
2. **What is error from ground-truth?** How different are the predictions of the network when compared to the ground-truth? Do the feature vectors accurately reconstruct the MDS or are they only correlated? While, the proposed method outperforms other methods, how far away is it from ground-truth?
3. **What are the benefit of being model-agnostic?** What kind of problems can these counterfactual explanations be used to tackle?
4. **What should we do if the scene graph is not readily available for a problem?** How should we construct such a scene graph from semantic attributes?
5. **Why is the counterfactual explanation given by the minimum graph edit distance useful?** Should we count the edit of two different attributes to be equivalent (say stripe pattern and color) or does it make more sense to count them differently.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a novel counterfactual approach that focuses on semantics shifts instead of explaining models' decisions via pixel-level changes. The authors represent images as semantic graphs derived from semantically annotated datasets. Subsequently, the counterfactuals for a given query image are defined as the closest graph (measured by graph edit distance) from another class. To enhance computational efficiency, the authors propose training a GNN to approximate the GED computation. Experimental results on widely-used datasets demonstrate superior performance compared to previous methods.

### Strengths
1. The authors employ graph similarity between a query and a target image, which is the first attempt in this direction. The authors have evaluate the method's performance across various datasets spanning different modalities, including CUB (an image classification dataset) and COVID-19 (an audio classification dataset), demonstrating the model-agnostic nature.
2. The authors provide code for reproducibility check.
3. The paper is well-written and easy to follow.

### Weaknesses
[Major]

1. **Method & motivation:** A primary objective of counterfactual explanation is to discover why and how the deep model (system) decision changes when specific regions within the given query image are modified. However, the semantics constructed in this paper rely on annotations from the dataset rather than capturing from the target model. Consequently, this raises concerns regarding the fidelity of the explanations generated by the proposed conceptual graph counterfactual method to the deep model's decision-making process. For instance, in the context of adversarial attacks [1-2], imperceptible image modifications to humans can significantly impact the model's output, a phenomenon unaddressed by the proposed method. The core issue is that the semantic graph representation is derived from human annotations, which may not align with the features the model uses for classification. This discrepancy could lead to counterfactuals that are semantically plausible to humans but do not accurately reflect the model's internal decision boundaries. The method does not account for the possibility that a model might rely on subtle texture or color variations, which are not captured by semantic graphs.


[Minor]

1. The font size in the figures is excessively small, making them particularly challenging to decipher when printed. Furthermore, it is advisable for the authors to employ vector graphics to enhance the quality of the illustrations.
2. As the authors pointed out in Appendix H, the method relies on massive annotation. At present, large vision (multi-modal) models [3-5] have the capacity to produce annotations with rich descriptions. It is advisable to evaluate the proposed method in conjunction with these large models. The current approach uses a fixed set of semantic concepts derived from the training data annotations. This limits the method's ability to generalize to novel concepts or out-of-distribution examples. The method should explore how to incorporate more flexible and adaptive semantic representations.

### Questions
My questions are listed in "Weaknesses" section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article presents an approach for providing more interpretable Counterfactual Explanations using concept graphs. Assuming instances to be represented as scene graphs and given a target "counterfactual" class, finding a counterfactual explanation is formulated as retrieving the instance of that class with minimum Graph Edit Distance (GED) from the current input. To avoid the costly process of explicitly computing GED for each pair of instances in the dataset, the method proposes to learn to embed scene graphs in such a way that their distance in the embedding space is similar to the GED of their graphs. This objective is supervised by computing GED on a subset of the dataset and experiments show that it generalizes even when fractions of the original dataset are provided. Comparisons with other semantically interpretable counterfactual XAI methods show that the approach retrieves counterfactual images with lower/more coherent GED distance w.r.t. to the ground-truth one.

### Strengths
1. Using distances among scene graphs to define counterfactuals is sound and of practical interest: as scene graphs ground the input to semantically interpretable concepts, the distance, and edits are inherently interpretable by humans, as also confirmed via the user studies Table 3 and Table 4.
2. The introduction clearly motivates the proposed approach and provides an extensive overview of Counterfactual Explanation methods and their interpretability issues, motivating the targeted scenario and the employed solution. 
3. The approach is flexible as it can be applied to any input representable via graphs, as shown in the audio experiments of Table 7.
4. As graphs are grounded to input instances, the edits are all actionable, a fundamental property for counterfactual explanations.

### Weaknesses
1. Most of the quantitative metrics are based on graph distances. For instance, Table 1, and Table 5 report the performance as the average number of graph edits between the retrieved instance by the proposed framework and the competitors. Similarly, Table 2 compares the ranking of the retrieved instance vs the "gold-standard" ranking provided by the ground-truth minimum GED. Given that the main contribution of the work is using GED over scene graphs as a way to provide counterfactuals and that the model is supervised with ground-truth GEDs over scene graphs (while the competitors are not), these results are not completely fair as the metric is biased toward the proposed model. Finding more method-agnostic metrics (as done in Tables 3 and 4) would make the claims stronger. Specifically, the reliance on GED as the primary metric, especially when the model is trained to minimize GED, raises concerns about whether the reported improvements are truly reflective of superior counterfactual explanations or simply an artifact of the evaluation setup. A more robust evaluation would include metrics that assess the quality of the counterfactuals from a different perspective, such as the change in classifier confidence or the semantic plausibility of the edits, independent of graph edit distance.
2. Despite being biased on the metrics, it seems that the competitor SC can still retrieve samples with low edits (Table 5, Section 4.2) achieving either superior or comparable results with the proposed method. Section 4.2 claims the contrary (i.e. superiority of the proposed approach) but the quantitative evidence is not clear. This statement should be refined and the reason for these comparable results expanded. The analysis should delve deeper into the specific scenarios where SC performs well and where the proposed method excels, providing a more nuanced understanding of the strengths and weaknesses of both approaches. The current analysis lacks a detailed breakdown of the types of graph edits that are being made and how they relate to the semantic changes in the images.
3. The SC approach (Dervakos et al., 2023) also uses GED but over knowledge graphs. From the text (and Section 2), it is unclear whether the contribution w.r.t. SC is mostly on the type of input graphs rather than on the selection criterion per se. Note that this would also impact the contribution in Section 1, as the article would not be the first to employ graphs for visual counterfactuals (but GNN for fast computation of GED). The distinction between using scene graphs versus knowledge graphs needs to be more clearly articulated, highlighting the specific advantages of scene graphs in the context of counterfactual explanations. The paper should also discuss the limitations of knowledge graphs in capturing the fine-grained details of visual scenes, which scene graphs are designed to address. The novelty of using GNNs for fast GED computation is not sufficiently emphasized as a key contribution.
4. Tables present inconsistent sets of baselines as Tab. 3 does not report the CVE baseline, and Table 4 misses the SC one. This makes it hard to assess whether the proposed approach is superior to all competitors in all user studies. The lack of consistent baselines across different experiments makes it difficult to draw definitive conclusions about the overall performance of the proposed method. A more comprehensive evaluation would include all baselines in each experiment, allowing for a direct comparison of their strengths and weaknesses. The absence of SC in Table 4 is particularly concerning, as it prevents a complete assessment of how the proposed method compares to the most similar approach in terms of human perception.
5. While using GED over scene graphs it is an interesting direction, it has two potential drawbacks. The first is that concepts of interest should be included in the pretrained scene-graph extractor. The article does not describe at the moment how the performance of the approach varies w.r.t. the scene graph extractor and Sections 4.1 and 4.2 assume graphs to be available (either via automatic extraction from labels or the dataset itself). The dependence on the scene graph extractor is a significant limitation that needs to be addressed. The paper should include an analysis of how the quality of the extracted scene graphs affects the performance of the counterfactual explanation method. This analysis should consider different scene graph extractors and their impact on the final results. The current assumption of readily available graphs is not realistic in many practical scenarios.
6. The second point is that GED may not correlate with distance in the classifier space but rather in the graph-based input representation. This is taken into account methodologically when the retrieved sample is conditioned on the classifier scores ranking (last part of Section 3). Nevertheless, It would be helpful to add a discussion on how the two relate to each other, and even quantitative analyses  (e.g. on L2 distances in the feature space) to check whether distances in the feature/classifier space correlate with GED. The lack of correlation between GED and classifier space distances is a critical concern that needs further investigation. The paper should include a quantitative analysis of how these two distances relate to each other, providing insights into the limitations of using GED as a proxy for classifier-relevant changes. The current approach of conditioning on classifier scores is not sufficient to address this issue. A more thorough analysis is needed to understand the relationship between graph edits and changes in the classifier's decision.
7. For the analyses on Visual Genome, the approach is using a model pretrained on Places365 as a classifier. However, as the examples in Fig. 4 show, the images may depict a single foreground object rather than a scene. The choice of Places365 as a pretraining classifier rather than other choices (e.g. ImageNet) is not motivated in the text. The choice of Places365 as the pretraining dataset for the classifier is questionable, especially given that the Visual Genome dataset contains both scenes and objects. The paper should provide a clear justification for this choice, explaining why Places365 is more suitable than other alternatives, such as ImageNet. The current lack of motivation raises concerns about the validity of the results on Visual Genome.

### Questions
I believe semantic graphs are a useful tool for providing interpretable and semantically grounded Counterfactual Explanations. At the same time, I have concerns regarding the experimental evaluation and the methodology that I hope the rebuttal could address. Specifically:
1. Is considering GED as ground truth for the rankings fair?
2. What are the main differences (in terms of contribution) w.r.t. SC? And why the performance differences with SC is limited for the Visual Genome experiments?
3. Why the user studies focused on different type of baselines?
4. How do performance/explanations vary w.r.t.the underlying scene graph extractor? E.g. applying SGG to extract graphs Visual Genome and CUB would impact the performance of the model?
5. Do distances on scene graphs correlate with distances on the classifier space?
6. What is the reason behind the choice of Places365 as the pretraining dataset for the results on Visual Genome?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to use semantic graphs as a vehicle for Counterfactual Explanations. Since handling distance over graph could be computationally too expensive the paper proposes a novel method based on GNNs to efficiently compute counterfactuals retrieved from a given database. The proposed method is validated both quantitatively and qualitatively on diverse modalities.

### Strengths
1. The idea of applying GNNs over scene graphs to compute an approximate graph edit distance for Counterfactual Explanations is novel and interesting. 
2. The proposed method is evaluated both against previous SoTA methods and with human annotations.

### Weaknesses
1. The main contribution of the paper is rather empirical, to the best of my knowledge none of the proposed techniques is novel, however their joint application to solve the problem statement is interesting. As such, the impact of the work on the community could be increased by providing a more comprehensive evaluation of a broader set of modalities/domains (the current version of the manuscript mostly covers images and very briefly audio signals). The evaluation, while including human studies, lacks a thorough exploration of the method's performance across diverse data types. The limited scope of modalities tested raises concerns about the generalizability of the findings and the practical applicability of the proposed approach in real-world scenarios beyond the specific image and audio datasets used.
2. The current version of manuscript works under the assumption that the "retrieval database" (of scene graphs) is “dense enough”. Such an assumption is key, especially when using Counterfactual Explanations for explaining specific failure modes of trained models. However, this assumption might not easily hold in practice. Can the authors comment more on this problem and how their new framework is expected to behave in realistic scenarios? It is not difficult to see that, as the scene graphs increase in dimension, all possible graph insertion/deletion/substitution lead to a combinatorial explosion of possible compatible scene graphs that might be hard to cover with a finite amount of data. The paper does not adequately address the potential for the method to fail when the database lacks sufficient coverage of relevant graph structures, particularly in complex scenarios with high-dimensional scene graphs. This limitation is crucial for the practical applicability of the method.
3. Results in Table 5 are quite close, however authors claim that their method exhibits superior performance over the baseline, can the authors put the number into perspective? In absolute terms it appears that both models perform quite similarly (as it is highlighted in the qualitative Figure 4 as well). The reported differences in Table 5, while statistically significant, are not substantial enough to convincingly demonstrate a clear advantage over the baseline. The qualitative examples, while illustrative, do not provide a strong enough justification for the claimed superiority, especially considering the small numerical differences in the quantitative results.

### Questions
Why “computing the GED for only N/2 pairs to contract the training set is adequate for achieving high quality representations? Has it only been validated experimentally or it can be formalized more precisely? Can the authors make this point clearer in the manuscript? 


Minor: 
- Editorial suggestions:
    - Please define acronyms before use, e.g. in the abstract.  
    - The abstract could be summarized without loss of information. 
- What is actionability mentioned in the introduction?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
