# A new framework for evaluating model out-of-distribution generalisation for the biochemical domain

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Quantifying model generalization to out-of-distribution data has been a longstanding challenge in machine learning. Addressing this issue is crucial for leveraging machine learning in scientific discovery, where models must generalize to new molecules or materials. Current methods typically split data into train and test sets using various criteria — temporal, sequence identity, scaffold, or random cross-validation — before evaluating model performance. However, with so many splitting criteria available, existing approaches offer limited guidance on selecting the most appropriate one, and they do not provide mechanisms for incorporating prior knowledge about the target deployment distribution(s).

To tackle this problem, we have developed a novel metric, AU-GOOD, which quantifies expected model performance under conditions of increasing dissimilarity between train and test sets, while also accounting for prior knowledge about the target deployment distribution(s), when available. This metric is broadly applicable to biochemical entities, including proteins, small molecules, nucleic acids, or cells; as long as a relevant similarity function is defined for them. Recognizing the wide range of similarity functions used in biochemistry, we propose criteria to guide the selection of the most appropriate metric for partitioning. We also introduce a new partitioning algorithm that generates more challenging test sets, and we propose statistical methods for comparing models based on AU-GOOD.

Finally, we demonstrate the insights that can be gained from this framework by applying it to two different use cases: developing predictors for pharmaceutical properties of small molecules, and using protein language models as embeddings to build biophysical property predictors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed an interesting framework for evaluating the model generalization to the out-of-distribution data (OOD) specifically with-in the biochemical domain. The author first proposed a metric that measures the model generalization based on existing similarity measures. A dataset partitioning algorithm and non-parametric statistical testing methods are proposed to complete the framework for model generalization comparisons.

### Strengths
1. This paper presents a comprehensive framework that not only measures generalization capabilities but also provides a statistical method for comparing different models based on the new AU-GOOD metric​

2. In the experimental section and the Appendix, the authors present a detailed and systematic analysis of selecting the similarity function, including its crucial relationship with the robustness of the GOOD metric in predicting the OOD data. 

3. The paper includes extensive experiments on multiple use cases to demonstrate the framework's effectiveness. Including selecting the model with more generalization abilities in case 1: predicting pharmaceutical properties of small molecules and case 2: predicting protein sequence properties. 

4. The open source code repo is clean and well-organized.

### Weaknesses
1. I am a bit confused by the formulation process in section 2.1 and found the formulation process is somewhat misleading. Here is a simple example, given four data points with features x1, x2, x3, x4. Assume the similarity score is: s(x1, x2) = 0.2. s(x1, x3) = 0.3, s(x1, x4) = 0.5, s(x2, x3) = 0.7, s(x2, x4) = 0.8, s(x3, x4) = 0.9. Assume the maximal value of similarity \lambda between the training and testing elements is 0.85. In this case, \lambda_{s}=0.85 only restricts x3 and x4 to be both in either the training set or the test set. Therefore, \lambda_{s}=0.85 results in different partitions of these four data points. E.g (x1, x3, x4) for training (x2) for testing or (x3, x4) for training and (x1, x2) for testing, etc. I am wondering if it is proper to formulate eq.3 from eq.2 by eliminating the \phi, since \lambda_{s} can only  be considered as a partition constraint rather than partition method.

2. In addition, assuming \phi is not omitted in equation 5, and empirical risk R is rewrite as (say) a function of \phi. This indicates that, under the same threshold, the AU_GOOD value is not only dependent on the target distribution, but also the partition algorithms. It’s better to discuss different partition algorithms, and how it impacts the AU_GOOD, or, justify that the proposed CCPart can successfully partition the Out-of-distribution sets. The current justification relies on a qualitative visualization, which is not sufficient to demonstrate the effectiveness of the partitioning algorithm in creating true OOD splits. A more rigorous analysis, perhaps using quantitative measures of distribution shift, would be beneficial.

---

Minor concerns

3. For equation 2, \mathcal{T} denotes the training subset, and the empirical risk is calculated among the test set \mathcal{E}, the subscript of x should not be i. 

4. It’s better to enlarge the captions, x-labs and y-labs in Figure 1.

5. Another minor shortcoming of this paper is that it lacks a ‘ground truth label’ for model generalization comparison. In use case 1, Figure 5 shows that the Random Forest is significantly better than the rest models in OOD generalization. However, this conclusion cannot be further verified. It is better to know exactly which model does better in handling the actual OOD data. (Though it is well recognized that RF and lightgbm is good at handling the outliers)

### Questions
My questions are listed in the weakness part.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes AU-GOOD, a metric for assessing machine learning model generalization to out-of-distribution biochemical data. AU-GOOD quantifies expected performance under increasing train-test set dissimilarity, integrating prior target distribution knowledge. A novel partitioning algorithm, CCPart, generates challenging test sets by prioritizing dissimilar data points. Statistical methods for model comparison based on AU-GOOD are also provided. The accompanying open-source code includes implementations of various similarity functions, partitioning algorithms, and AU-GOOD calculation, applied to two use cases: small molecule property prediction and protein language model embedding evaluation.

### Strengths
Authors presented a detailed analysis of AU-GOOD, and presented a CCPart for splitting sets based on pairwise similarities. CCPart can be applied to any dataset that has useful pairwise similarity metrics in the data, which means it can be applied to other datasets outside of biochemical applications. The authors perform a wide variety of tests on various datasets, and also study various protein language model embeddings, and their performances on OOD. The authors take care to use statistical tests to confirm statistical significance.

### Weaknesses
The font in the figures are extremely small. Please enlarge to improve readability. Especially the plots in the SI, ie. SI fig 1. 

The use of pairwise similarity measures heavily restricts the size of the dataset that can be split. As such, most datasets the authors look at are on the smaller end. This also means that the models studied are usually traditional ML methods (KNN, SVM, RF, etc.).

Various works have already tried structure-only fingerprints-based splitting methods. This includes work done by the MOOD paper from Tossou et al. (2024), DeepChem from Ramsundar et al. (2019), and Dionysus from Tom et al. (2023). In particular, CCPart is quite similar to Butina or scaffold splitting (from DeepChem), which gathers clusters of fingerprints or scaffolds and sets a cutoff threshold for Tanimoto similarity. 

Overall, the AUGOOD metric, and the GOOD curve, is not convincing to me as a reliable measure of OOD performance. Looking at the curves in SI Fig 2, the variations in the GOOD curve are not as well behaved as those in the main text, such as Fig 1, or Fig 5. Fitting a linear line to the GOOD curve to attain a "slope" also seems strange considering the huge variations in the performance metric. The curves also dramatically change as the performance metric is changed (ie. between Matthew vs Spearman vs Pearson coefficients). The error bars are very large on the performance metrics, but the authors seem to use the metrics of model performance interchangeably.

Additionally, the choice of AU the GOOD curve is confusing to me. Take for example, Fig 1A, where the authors conclude that Model A is less generalizable than B, because B performes similarily across the different similarity thresholds. However, the area under the curve would actually be quite similar for model A and B. While this is an example to illustrate the GOOD curve, it is also an example that shows how AUGOOD may not be a useful metric. The authors may defer to the slope of a linear fit, but as seen in Fig 2 of SI, the GOOD curve is rarely linear, or even monotonic.

### Questions
Are there any plans to extend the work to larger datasets and deep learning models? Often, datasets for virtual screening are much larger, on the order of millions, and GNN and GCN models start to exhibit state-of-the-art performance. 

What motivates the use of various performance metrics? Why, for example, Spearman for Caco2, Halflife and LD509, but Matthew for Ames, DILI, and PAMPA? It seems that the behaviour of the GOOD curve is heavily dependent on this choice. Would the conclusions change for different metrics? And how might that affect the interpretation of AU-GOOD, if the metric can so quickly fluctuate and change?

How does CCPart compare with other splitting methods that are already available, such as Butina splits, scaffold splits, cluster splits etc.? 

Table 1, I think the ranking should be 2,4,1,4 for the models read left to right?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a formalized approach for creating training and test splits that assesses the generalization performance of a machine learning algorithm on biological data as a function of a (chosen) similarity metric between data points.

### Strengths
* The paper is generally well written.
* It is broadly applicable to a wide range of biological domains given the generality of the similarity metric based approach.

### Weaknesses
 * The paper is written in an overly formalized manner. Sections 2.1 and 2.2 say very little that’s non-obvious. It can be described in 1-2 paragraphs of plain English. The over-formalization of very simple concepts seem largely intended to make the matter seem more complex than it actually is. Similarly for sec 2.3, which introduces more novel methods and is not strictly a pedagogical section, but the description is far too long and unnecessarily mathematical.
* While the basic concepts are overly formalized, concepts that could actually use more formal precision, e.g., the behavior of different GOOD curves, are instead described using phrases like “visually incoherent GOOD curves” without actually specifying what “visually incoherent” means. The lack of a quantitative definition makes it difficult to reproduce or compare results. For example, what specific characteristics of the curves are considered incoherent? Is it the presence of multiple local maxima, a lack of monotonicity, or some other feature? This ambiguity undermines the rigor of the analysis.
* In most biological domains, data points are evolutionarily related (e.g. proteins, species, etc), and so the assumption that there will be disconnected subgraphs is not really correct, at least not for stringent levels of generalization. I.e., it might be possible to find a threshold by which the graph does become disconnected, but that threshold would only segregate highly similar data points and would result in a very easy test. The method's reliance on disconnected subgraphs may not be appropriate for datasets where data points form a highly connected graph.
* In many biological domains, data points are noisy, and it’s quite possible that the type of disconnected subgraphs found in the proposed algorithm would basically correspond to pathological outliers. Thus I would caution against naive application of this approach as it may result in test sets comprising largely unrepresentative data points. The algorithm might inadvertently create test sets that are not representative of the overall data distribution, leading to misleading performance evaluations.
* Ultimately there’s little utility / novelty here. The approach does not introduce anything substantially different from the existing literature, and in the places where it does differ, it is hard to judge whether this approach will actually work in practice. The experiments performed are not compared to any other than baseline and the discussion about the resulting GOOD curves is largely informal and speculative.

### Questions
* I would ask the authors to think of ways to demonstrate that their approach outperforms other existing methods.

### Soundness
2

### Presentation
2

### Contribution
1
