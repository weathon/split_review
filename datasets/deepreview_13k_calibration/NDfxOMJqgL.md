# CAST: Cluster-Aware Self-Training for Tabular Data

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 5, 3, 5, 6

## Abstract
Tabular data is one of the most widely used data modalities, encompassing numerous datasets with substantial amounts of unlabeled data.
Despite this prevalence, there is a notable lack of simple and versatile methods for utilizing unlabeled data in the tabular domain, where both gradient-boosting decision trees and neural networks are employed.
In this context, self-training has gained attraction due to its simplicity and versatility, yet it is vulnerable to noisy pseudo-labels caused by erroneous confidence.
Several solutions have been proposed to handle this problem, but they often compromise the inherent advantages of self-training, resulting in limited applicability in the tabular domain.
To address this issue, we explore a novel direction of \emph{reliable confidence in self-training contexts} and conclude that \emph{self-training can be improved by making that the confidence, which represents the value of the pseudo-label, aligns with the cluster assumption.}
In this regard, we propose \textbf{C}luster-\textbf{A}ware \textbf{S}elf-\textbf{T}raining (CAST) for tabular data, which enhances existing self-training algorithms at a negligible cost while maintaining simplicity and versatility. 
Concretely, CAST calibrates confidence by regularizing the classifier's confidence based on local density for each class in the labeled training data, resulting in lower confidence for pseudo-labels in low-density regions.
Extensive empirical evaluations on up to 21 real-world datasets confirm not only the superior performance of CAST but also its robustness in various setups in self-training contexts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This pager proposes a simple way to generate reliable pseudo-labels by assigning high confidence to pseudo-labels in high-density regions and low confidence to those in low-density regions. The proposed method could be plugged into current self-training algorithms and tabular models, and extensive experiments validate the effectiveness of this method. However, there lacks detailed analysis (empirical or theoretical) or insights on why it works, and the reliable pseudo-labels are not adequately verified in real scenarios.

### Strengths
This work proposes a simple but effective way to generate reliable pseudo-labels, which multiples the original pseudo labels with a density score. The method is simple and could be incorporated with various existing algorithms, and extensive experiments validate the effectiveness of it.

### Weaknesses
After reading this paper carefully, I have some concerns:
1. There lacks detailed analysis on why this method works. And I wonder whether it has some relationship with label smoothing techniques. And I would recommend the authors to give more in-depth analysis, either empirical or theoretical. Also, the 'cluster assumption' or the reliable pseudo-labels should be checked or verified in real datasets. For example, why they are reliable and can we explain it?
2. I believe there are many many semi-supervised learning methods, but there are only 5 baselines, which I think is not enough and representative for SSL. 
3. Some of the datasets are not open-sources, e.g., 6M mortality.

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to use self-training to handle the tabular data learning without altering the self-training algorithm or model architecture.

### Strengths
- This paper delves into the confidences of pseudo-labels in self-training from the perspective of cluster assumption, providing a new view for the field of self-training. In addition, the proposed CAST is easy to follow.

### Weaknesses
 - From the Introduction, I cannot get the significant relationship between tabular data and the proposed self-training method. The motivation and organization of this paper should be further clarified. Specifically, the introduction does not adequately explain why existing self-training methods are insufficient for tabular data. The paper should articulate the unique challenges that tabular data presents for self-training, beyond simply stating that GBDT is suitable. The connection between the proposed method and the specific characteristics of tabular data is not clear.
- In addition, the difficulties brought by tabular data over the general unstructured data (e.g., images, texts) in machine learning have not been discussed. In detail, they only stated that the GBDT is suitable for tabular data, while they do not explain why other methods are not suitable. The paper needs to elaborate on why methods successful in image or text domains might not translate well to tabular data. For instance, the paper should discuss the impact of feature heterogeneity, varying scales, and the lack of spatial or sequential structure in tabular data, and how these factors affect the performance of self-training.
- In my view, CAST is not a tabular data-specific method. Its idea is to adjust the prediction confidence based on the cluster assumption, which is also available for other data types. I think that this discussion should be included and the corresponding experiments are needed. The paper should acknowledge that the core idea of CAST, which involves adjusting prediction confidence based on cluster assumptions, is not inherently limited to tabular data. The authors should discuss the applicability of their method to other data types and provide a rationale for why they chose to focus solely on tabular data. Furthermore, the paper should include experiments on other data types to demonstrate the generalizability of the method or, conversely, to justify its limitation to tabular data.

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
2 fair

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
In the paper "CAST: Cluster-Aware Self-Training for Tabular Data" the authors propose an approach to self-training for tabular data. The basic idea of the approach is to take into account how densely populated the dataset is around candidate data points for generating pseudo labels. More specifically, the density is used for regularizing class confidences discounting confidences in less densely populated realms of the space.

### Strengths
- The proposed method is relatively simple and thus relatively easy to implement.
- The related work is nicely surveyed.

### Weaknesses
 - The paper is not self-contained, i.e., there are gaps in the proposed methodology. For example, in Eq. 2 the authors state that prior knowledge is encoded in terms of a vector $\gamma$ and $\gamma$ is assigned the output of some function TD(). However, the function is not clearly described. Only "prior knowledge which is derived from the labeled training data distribution TD"  is mentioned in the text. Probably TD is on purpose quite vague. However, there is not even a single mention of what this could be. It is also confusing that it seems to be the labeled training data distribution, however, this distribution should at maximum be implicitly given by the data sample.
- In Algorithm 1 the $\gamma$ does not even occur. I assume it is somewhere hidden in the $\Phi$ which supposedly does the pseudo-labeling. However, $\Phi$ is nowhere given concretely. Not even in the appendix -- at least I could not find it there. Still, in the text, the authors write that Algorithm 1 is the complete algorithm but only a very basic self-training framework is given there -- nothing special about CAST as a standalone method. Also, the loop is terminating with respect to some unknown termination condition of $\Phi$ which is neither elaborated.
- While the experimental evaluation section covers most of the section, taking different perspectives and viewing angles, the breadth of the study is quite limited. In the main paper, the study comprises 4 real-world datasets with an additional 16 datasets in the appendix for a limited set of methods. Considering that there is no theoretical support for the claims, the underpinning of the claims made in the paper is quite weak. 
- Speaking about the empirical evaluation: While relative improvements over a baseline might be the primary goal, with which I agree, it is relatively hard to interpret the significance of the results. In particular, it impedes the application of a statistical test whether the results are significant. From the results, the differences are probably significant but still it is very hard to interpret and I would prefer plain results even though metrics might differ.

### Questions
- How is $\gamma$ computed? What are the requirements or desiderata for computing $\gamma$ to yield a sound approach?
- What is the termination criterion in relation to $\Phi$?
- How is the pseudo-labeling $\Phi$ done?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new calibration strategy for self-training on tabular data. The strategy is based on an algorithm outputting a confidence score for each input sample that linearly interpolates between the confidence score provided by the classifier and its scaled version. Specifically, the scaling factor incorporated the low-density assumption, thus being proportional to the data density. It is estimated either using a kernel density estimator or a Naive Bayes-like generative model. The overall calibration strategy can be easily plugged into existing self-training algorithms. Experiments are conducted on different toy and tabular datasets showcasing (i) the versatility of the approach for being easily applied to different self-training variants (fixed/adaptive threshold, noise filtering) and different classifiers (decision trees, MLPs) and (ii) the superiority against basic calibration strategies.

### Strengths
1. The idea is simple, yet novel (**Novelty**)
2. The paper is clear and easy to read (**Clarity**)
3. Code is provided. However, no additional check on replicability has been performed (**Reproducibility**)

### Weaknesses
 1. The scope of applicability of the proposed solution is quite narrow. Indeed, the proposed solution seems to be applicable to low dimensional datasets and it is not clear how well the solution scales and generalises to more realistic high-dimensional datasets (**Significance**)
2. The proposed solution requires a density estimation step and therefore it is more computationally demanding with respect to the considered baselines. Experiments should provide also this information (**Quality**)
3. The cluster assumption (or equivalently the low-density separation) can be cheaply incorporated by leveraging techniques based on entropy minimisation for semi-supervised learning. A discussion and possibly experimental comparison against such techniques is missing (**Quality**). For instance, see [1-3]
4. Limitations are not discussed (**Quality**)

### Questions
Please find below some questions related to the above mentioned weaknesses plus some more detailed ones about the experiments:
1. Can you please elaborate on the 4 above-mentioned weaknesses?
2. Regarding experiments on toy datasets, is there any reason why temperature scaling is not shown?
3. In almost all experiments there is a significant difference between the two proposed ways of estimating the density (CAST-D and CAST-L). Can you please discuss about this aspect? Is this issue related to an improper hyperparameter tuning?
4. In Figure 5, can you please explain why the performance decrease with a larger amount of labeled examples, as this seems a counterintuitive result?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a simple but effective self-training method for tabular data, which takes the cluster assumption to regularize confidence values. Experiments on four datasets demonstrate the superiority of the proposed method.

### Strengths
1. The proposed method is well motivated by the observations shown in Fig. 1, namely, pseudo-labels that lie in high-density regions are more reliable than those that lie in low-density regions.
2. The paper is well-written and organized in general. The simple modifications on the confidence value proved to be effective through experiments on four tabular datasets.

### Weaknesses
1. The density estimation plays an important role in the proposed method. However, the authors only spend a few words saying that the density is estimated using the prior knowledge derived from the labeled training data distribution. I am confused when reading this part of the method and hope the authors can provide more details on that. Specifically, it is unclear how the prior knowledge is extracted and used to estimate the density for unlabeled samples. What specific density estimation technique is employed (e.g., kernel density estimation, Gaussian mixture models)? How are the parameters of this density estimator determined from the labeled data? Furthermore, how is the 'prior knowledge' represented mathematically, and how does it translate into a density value for a given unlabeled sample?
2. Just as the authors have claimed, the only difference between CAST and the conventional self-training algorithm is the use of regularized confidence. In other words, it seems that the proposed method has no specific designs for tabular data. Thus, I wonder if it is possible to supply a bit more results on other forms of data to show the proposed method is a general solution in self-training. The lack of specific adaptations for tabular data raises concerns about its potential effectiveness compared to methods specifically designed for this data type. It would be beneficial to see a more thorough analysis of the method's performance on diverse datasets, including those with varying characteristics and complexities.
3. Are the best choices of the hyper-parameter $\alpha$ the same across different datasets? Would the optimal value be influenced by the number of samples in the dataset? It is crucial to understand the sensitivity of the method to this hyperparameter and how it should be tuned for different scenarios. The authors should provide a more detailed analysis of the impact of $\alpha$ on performance, including guidelines for selecting appropriate values based on dataset characteristics.
4. There are some related self-training enhanced clustering methods such as SCAN (ECCV 2020), SPICE (TIP 2022), and TCL (IJCV 2022), that the authors are encouraged to include in the related works.
5. The meaning of the abbreviation could be provided in the caption of Table 1 to improve readability.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
