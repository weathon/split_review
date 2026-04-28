# LCA-on-the-Line: Benchmarking Out-of-Distribution Generalization with Class Taxonomies

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 5, 3

## Abstract
We tackle the challenge of predicting models' Out-of-Distribution (OOD) performance using in-distribution (ID) measurements without requiring OOD data. Existing evaluations with ``Effective Robustness'', which use ID accuracy as an indicator of OOD accuracy, encounter limitations when models are trained with diverse supervision and distributions, such as class labels (\textit{Vision Models, VMs, on ImageNet}) and textual descriptions (\textit{Visual-Language Models, VLMs, on LAION}). VLMs often generalize better to OOD data than VMs despite having similar or lower ID performance. To improve the prediction of models' OOD performance from ID measurements, we introduce the \emph{Lowest Common Ancestor (LCA)-on-the-Line} framework. This approach revisits the established concept of LCA distance, which measures the hierarchical distance between labels and predictions within a predefined class hierarchy, such as WordNet. We assess 75 models using ImageNet as the ID dataset and five significantly shifted OOD variants, uncovering a strong linear correlation between ID LCA distance and OOD top-1 accuracy. Our method provides a compelling alternative for understanding why VLMs tend to generalize better. Additionally, we propose a technique to construct a taxonomic hierarchy on any dataset using $K$-means clustering, demonstrating that LCA distance is robust to the constructed taxonomic hierarchy. Moreover, we demonstrate that aligning model predictions with class taxonomies, through soft labels or prompt engineering, can enhance model generalization. Open source code in our \href{https://elvishelvis.io/papers/lca/}{Project Page}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on evaluating the Out-of-Distribution (OOD) generalization by using Least Common Ancestor (LCA) distance based on the WordNet hierarchy. LCA measures the taxonomic distance between labels and predictions, and the paper shows that LCA is a better measure of OOD generalization than top-1 accuracy (when both LCA and top-1 accuracy are computed on in-domain data). Intuitively, LCA is able to better evaluate how well a model has learned semantic knowledge of the classes (since lower LCA indicates that the model’s wrong predictions are semantically closer to the true class). This enables LCA to be a better measure of OOD performance compared to top-1 accuracy which only considers whether the prediction is correct or not. Specifically, they test 75 different models (including both vision models and vision-language models) and find a linear correlation between ImageNet LCA and OOD accuracy across 4 standard ImageNet-OOD datasets. They also use the pairwise LCA between classes as soft labels for linear probing over pretrained models, and find that OOD performance can be improved at the cost of in-domain performance.

### Strengths
* The idea of using LCA for evaluating OOD generalization is simple, intuitive, well-motivated, and effective.

* The paper is fairly well-written (except some typos which can be fixed).

* The experimental analyses are quite extensive. The contributions of this work will likely be quite significant for industry applications where predicting OOD performance ahead of deployment tends to be important.

### Weaknesses
 * Explanation of LCA is complicated
    * A visual illustration of LCA computation with a small part of the WordNet hierarchy and 2-3 example pairs of classes would help readers to quickly and better understand the LCA distance measure. For instance, showing a small tree with 'dog', 'cat', 'wolf', 'husky', and 'siamese cat' nodes, and then highlighting the LCA for pairs like ('dog', 'cat') and ('husky', 'siamese cat') would be beneficial. The current description relies heavily on the reader's prior knowledge of WordNet and hierarchical structures, which may not be universally true.
    * Maybe a figure in the main paper like Fig. 3 (in Suppl.) but with some actual classes and example LCA values for a few pairs of classes.

* Fig. 1 is very difficult to read and understand
    * The legend is too small. It would be better to show only top-1 here (first row) with larger font sizes (match caption size, roughly) and show the full figure in supplementary. The current figure crams too much information into a small space, making it hard to discern the trends and relationships being presented. Focusing on a single metric in the main text would improve clarity.

* Implementation of inferred class taxonomy is difficult to understand
    * It is unclear what "establishing the cluster level where both classes share the same cluster as the height of LCA" means. Please clarify and try to simplify it. The description lacks sufficient detail on how the clustering is performed and how the hierarchical structure is derived from the clustering results. Specifically, what distance metric is used for clustering, and how the number of clusters at each level is determined should be clarified.
    * A figure illustrating the method would be ideal to help readers understand it better. A diagram showing a few classes at the bottom, then how they are grouped into clusters at different levels, and finally how the LCA is determined based on the cluster hierarchy would be very helpful.

### Questions
* Please see the weaknesses section.

* Minor comments
    * Abstract (second paragraph) has a typo: “Beside” → “Besides”.
    * Introduction (second paragraph): “effective robustness(Taori et al., 2020)” space needed between robustness and the citation.
    * Above the contributions list, typo: “in measure model’s semantic awareness” → “in measuring a model’s semantic awareness”.
    * Sec. 2 (second paragraph): extra or less brackets in three equations in this paragraph.
    * In many places in the paper, quotes are used incorrectly in LaTeX. Please use ` ' in LaTeX (i.e. backtick and quote instead of both quotes).
    * Paragraph below Table 3 has a typo: “As illustrated in Table3” → “As illustrated in Table 3”, i.e. add space.
    * Sec. 3.3 (last paragraph) has a typo: “natural image(ImageNet)” → “natural image (ImageNet)”, i.e. add space.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the Least Common Ancestor (LCA) distance via the WordNet hierarchy is employed to measure the taxonomic distance between labels and predictions, utilizing it as a benchmark for model generalization. Extensive experiments are performed on model evaluation, including vision-only and vision-language models on natural distribution shift datasets. A strong linear correlation is observed between in-domain ImageNet LCA scores and out-of-domain (OOD) Top1 performance across many variants of ImageNet.

### Strengths
A thorough experimental analysis of the relationship between Out-of-Distribution (OOD) detection performance and Least Common Ancestor (LCA) distance for image classifiers is provided in this paper. The following are key strengths of the work:

(1) Experiments are conducted on a diverse set of neural network architectures, including ResNet, VGG, EfficientNet, Vision Transformer (ViT), and Vision-Language Models (VLMs), enabling conclusions that potentially generalize across problem domains. The rigor and comprehensiveness of the methodology are underscored by the scale of experiments, involving up to 75 network variants.

(2) A major point about this submission is the analysis that demonstrates a correlation between OOD detection performance and LCA distances in the classifier. For instance, it is quantitatively shown how images from OOD datasets with more distant LCA relationships to the training data tend to be easier to detect as anomalies. The intuitive justification provided is that greater separation between the semantics of the origin dataset and OOD dataset in the hierarchical LCA structure leads to more separable distributions.

### Weaknesses
Major:

(1) The paper does not evaluate multiple OOD scoring methods like energy scores[1], ODIN[2], Mahalanobis distance[3], and ReAct[4], which would have provided insights into the validity of the key conclusions across different anomaly scoring approaches. The interaction between the choice of scoring method and LCA distance remains unclear. Understanding how these scoring methods affect OOD performance from the perspective of the LCA distance is important. It should be noted that the calculation of this LCA distance is limited to variants of ImageNet considering the WordNet hierarchy used.

(2) The claim is made that the findings offer "invaluable insights and actionable techniques" to enhance robustness and generalization. However, no concrete solutions leveraging the LCA distance are proposed or analyzed. Further theoretical or empirical analysis that establishes a connection between these insights and improved generalization would be beneficial.


Minor:

“Given two classes, y (the ground truth class) and y′, we define the LCA distance according to (Bertinetto et al., 2020) as lcad(y′, y) := f(y) − f(lca(y, y′), where f(y) ≥ f(lca(y, y′) and
lca((y′, y) denotes…” All formulations lose the right brackets.

“As highlighted in Fig 1 (indicated in red), when adhering to ’accuracy on the line’,” Wrong quotes.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on addressing the challenge of assessing model generalization under out-of-distribution conditions. They reintroduce the Least Common Ancestor (LCA) distance. Particularly, they utilize the LCA to measure the taxonomic distance between labels and predictions, presenting it as a benchmark for model generalization. In the experiments, the proposed method is evaluated on multiple datasets.

### Strengths
It is interesting to address the challenge of assessing model generalization under out-of-distribution conditions.

### Weaknesses
1. The Introduction Section is not clear. The authors indicate that most methods involve modeling correlations with in-domain accuracy or agreement. And many studies evaluate generalization on OOD datasets that feature limited visual shifts. These interpretations are very unclear. I am not clear the concrete meaning. I recommend the authors modify their paper carefully.

2. The authors indicate that to address the analyzed issues, they introduce a method to benchmark model generalization, i.e., using the taxonomy loss. Firstly, the authors do not interpret whether the research is meaningful clearly. Secondly, the authors do not sufficiently introduce the advantages of the taxonomy loss. I recommend the authors draw a figure to clearly describe the motivation.

3. In Table 1, the evaluated methods are somewhat old. The authors should verify the effectiveness of the proposed method on more state-of-the-art methods, e.g., the works from CVPR 2023, ICLR 2023. Meanwhile, the experiments are somewhat unclear. The authors only evaluate the classification performance. I recommend the authors evaluate the proposed method on other tasks, e.g., object detection and semantic segmentation. Finally, for Fig. 1, the authors should give more interpretations.

### Questions
See Weakness.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
