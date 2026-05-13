# Unmasking Trees for Tabular Data

- Decision: Reject
- Scores: 8, 3, 3, 6

## Abstract
Despite much work on advanced deep learning and generative modeling techniques for tabular data generation and imputation, traditional methods have continued to win on imputation benchmarks. 
We herein present UnmaskingTrees, a simple method for tabular imputation (and generation) employing gradient-boosted decision trees which are used to incrementally unmask individual features. 
This approach offers state-of-the-art performance on imputation, and on generation given training data with missingness; and it has competitive performance on vanilla generation.
To solve the conditional generation subproblem, we propose a tabular probabilistic prediction method, BaltoBot, which fits a \emph{bal}anced \emph{t}ree \emph{o}f \emph{bo}osted \emph{t}ree classifiers. 
Unlike older methods, it requires no parametric assumption on the conditional distribution, accommodating features with multimodal distributions; unlike newer diffusion methods, it offers fast sampling, closed-form density estimation, and flexible handling of discrete variables.
We finally consider our two approaches as meta-algorithms, demonstrating in-context learning-based generative modeling with TabPFN.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose leveraging the autoregressive framework of [1] for generative modeling of tabular data, replacing Transformers with XGBoost.

Because this requires learning conditional distributions over numerical variables, and XGBoost regression models only provide point estimates, the authors propose a second contribution in the form of a non-parametric conditional density estimator which they call BaltoBot. 

The authors also explore replacing XGBoost with TabPFN which, despite not achieving comparable results to XGBoost, shows the overall flexibility of the framework where any classification model can be used as an autoregressive model to generate tabular data.


[[1]](https://arxiv.org/abs/2312.06089) Manbir S. Gulati and Paul F. Roysdon. TabMT: Generating Tabular data with Masked Transformers. In NeurIPS 2023.

### Strengths
- The main idea is simple and sensible.
- The algorithm proposed for conditional density estimation over numerical variables, despite not being the main focus of the paper, shows promising results. 
I will note that while this algorithm might seem expensive, requiring training multiple binary classification models for predicting a single variable, it is in fact not so dissimilar to how a naive treatment as a multi-class categorical variable would be handled in XGBoost, requiring training one tree per categorical value.
If one were to quantize a numerical variable into an equivalent $2^\Delta$ bins and fit a multi-class XGBoost model, it would also require fitting $2^\Delta$ trees at each boosting round, therefore leading to a similar "duplication" of models. Furthermore, as noted by the authors, training a BaltoBot model actually seems advantageous in this instance as each XGBoost model not at base level only sees a fraction of the training examples.
- As an autoregressive model, the method proposed here allows for density evaluation which is an advantage that is somewhat understated. This would enable interesting use cases that other generative methods can't do such as out of distribution detection.
It would also allow one to compute likelihoods under the model which would be a golden standard for evaluation of a generative model.
- Source code is provided.

### Weaknesses
In my opinion this is a good paper with good ideas but certain aspects could be improved (roughly in order of importance):

- The biggest downside of the proposed method would seem to be the need for duplicating the training set K*D times which could make it impratical for large datasets (and require selecting a lower K least the training set wouldn't fit in memory). 
The paper doesn't explore this regime and the trade-offs that would have to be made to scale to datasets with more examples and/or more features since it relies on a benchmark composed only of relatively small datasets. Specifically, the memory footprint of the method grows linearly with both the number of features and the number of splits K, making it unsuitable for high-dimensional tabular data or when a large number of splits is required for accurate density estimation. The authors should provide a more detailed analysis of the computational and memory requirements of their approach, including a discussion of how these scale with dataset size and dimensionality.

- The benchmark proposed by [1] also does not carry out any hyperparameter tuning as far as I understand. It could be more relevant to a practitioner who would tune the hyperparameters of their chosen generative model to know the performance that each method can achieve with some reasonable hyperparameter tuning protocol. However, I do sympathize with the authors that there are too many degrees of freedom to such an analysis and it is not fun.

- The BaltoBot evaluation could be further developed. As a non-parametric conditional estimation method for numerical variables it could have wider applicability as it seems competitive to other proposed methods for uncertainty estimation.
However, evaluation on more than one real-world scenario would be required to draw meaningful conclusions. The current evaluation is limited to a single task within the context of the proposed generative model. A more thorough evaluation of BaltoBot's performance on diverse datasets and against other established conditional density estimation techniques would be beneficial to assess its general applicability.

- Please consider providing the full table of results and standard errors for every metric in an appendix. This would allow an interested reader to assess the magnitude of the differences in a metric of interest between different methods.

- The explanation of BaltoBot could be improved. Namely, it could be clearer that the input space to every node is partitioned into two with the splitting point determined by KDI.

- Fix missing $K$ in line 092:
(...), we repeat this process times with $K$ different random permutations -> (...), we repeat this process $K$ times with $K$ different random permutations

**Other interesting analyses**

The following are not really weaknesses of the paper but rather analyses that I would be interested in but I don't think should be expected of the paper.

- The density estimation aspect could be explored further. Namely, comparing with [2] as an example of another tree-based model for density estimation on NLL directly.

- Since errors in auto-regressive generation could accumulate faster given certain feature permutations than others it could be interesting to explore doing multiple rounds of imputation with different random permutations.
This could be an easy way to improve results at the cost of more computation.

### Questions
- Would similar strategies to ForestDiffusion using a data iterator to avoid materializing the entire duplicated training set in memory be a viable strategy?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces UnmaskingTrees, an approach for tabular data imputation and generation using gradient-boosted decision trees with an autoregressive unmasking objective. The authors also present BaltoBot, a tree-based probabilistic prediction method. Their method is more computationally efficient than diffusion-based approaches and offers practical advantages like closed-form density estimation.

### Strengths
- **Problem relevance**: There is a clear gap in the literature for methods that can handle tabular data imputations effectively, especially given that traditional methods like MissForest outperform newer deep learning approaches.

- **Computational efficiency**: The method offers faster training and inference compared to diffusion-based approaches, which is valuable for practical applications.

- **Novel combination**: While the individual components aren't new, combining gradient-boosted trees with autoregressive unmasking for tabular data is an interesting direction.

- **Numerous baseline models** : The authors compare their method with several baseline models, including MissForest, MICE, and GAIN, which provide a comprehensive evaluation.

- **Existing implementation**: The authors provide the source code implementation that promotes reproducibility and practical adoption. Although the code for the case studies and their proposed method was available, the code for the experiments on the 27 datasets was missing.

### Weaknesses
- **Incomplete technical analysis**: The paper fails to properly analyze how the method performs under different missingness mechanisms (MAR, MCAR, MNAR). Specifically, while the experiments are conducted under MCAR, there is no theoretical discussion or empirical evaluation of the method's behavior and guarantees under MAR and MNAR conditions. This is a critical oversight for a paper focused on missing data, as the performance and applicability of imputation methods can vary significantly depending on the underlying missingness mechanism.

- **Superficial approach**: Although the method is a novel combination of existing techniques, it also lacks substantial theoretical innovation or justification. The paper does not provide a deep theoretical analysis of why combining gradient-boosted trees with autoregressive unmasking is particularly suitable for tabular data imputation or generation. The rationale behind using an autoregressive approach with decision trees, as opposed to other sequence models, is not thoroughly explained.

- **Oversold and unjustified claims**: The method is presented as a general solution, but its limitations and assumptions are not adequately discussed. For instance, the paper lacks a clear discussion of how the method handles discrete variables and different data types. While softmax-based classification with cross-entropy loss is mentioned for categorical features, the implications and potential limitations of this approach are not fully explored. The impact of different masking orders and the justification for using a random order are also not sufficiently addressed.

- **Poor presentation of the methodology**: The method is poorly formalized and difficult to follow. The description needs more rigorous mathematical formulation and clear algorithmic steps. For instance, the process of constructing the meta-tree and the criteria for splitting nodes could be better defined. The interaction between the autoregressive unmasking and the tree-based structure could also benefit from a more formal treatment, including a clear definition of how the unmasking order is determined and how it affects the learning process.

- **Writing issues**: There are some editorial issues (e.g., line 91 has a missing variable definition somewhere in between "process" and "times," or in line 112, it is unclear what $\Delta$ in depth-$\Delta$ refers to). These issues make the technical part of the paper especially hard to follow.

- **Datasets assumptions**: Even though there are 27 datasets, [1] carried out pre-processing steps, such as encoding the categorical features as one-hot vectors, that have implications for the experimental results. The use of one-hot encoding can significantly increase the dimensionality of the data, potentially affecting the performance and scalability of the method. Therefore, an overview of the datasets in the appendix with this information would have been helpful.

- **Poor abstract**: The abstract fails to clearly communicate the paper's contributions and methodology. It does not provide a concise summary of the proposed method, its advantages, and its limitations. A reader should be able to quickly grasp the main ideas and contributions of the paper from the abstract, which is currently not the case.

### Questions
- How does the method specifically handle MAR, MCAR, and MNAR cases? What are the theoretical guarantees for each case?
- What are the method's limitations when dealing with discrete variables? The same question applies to mixed data types.
- How does the choice of masking order affect the results? Is there any theoretical justification for random ordering?
- What are the computational complexity implications for high-dimensional data?
- Was the experiment code (for the 27 datasets) available, or did I miss something? Additionally, here are some minor remarks on the code: (1) there were no unit tests, so `pytest` in your `README.md` is unnecessary, and (2) I advise the authors to add `ForestDiffusion` to the `requirements.txt` required for `iris-demo.ipynb`.

### Soundness
2

### Presentation
1

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
This paper proposes to generate tabular data using discriminative models by posing the generation as a sampling from regressors/classificators one feature at a time, using multiple permutations to allow features to be conditioned on different sets of other features.


EDIT: I have read the authors response, and stay with my score. Thanks for pointing out the baselines that I missed and for pointing out that simplicity really is not a downside, which I fully agree with. What I wanted to say is that the proposed method is not very novel and to my understanding the thing that people already do when generating data with discriminatory models. The tree for regression models of course is novel, but I would believe that models that do not work discriminatory will win this in the medium-long run.

### Strengths
- Simple to understand

### Weaknesses
 - Unclear how the proposed hierarchical handling of regression sampling is better than a simple discretized approach with well chosen bins
- The idea is very simple and low-effort in terms of putting it to work
EDIT: I want to take the above weakness back.
- The results are not great. The tables feel a little to designed: boldening non-standard things in the table, i.e. the winner of a subset of the methods or the 2 best methods.


I think if one wants to make a scientific contribution at ICLR level it would be the right thing to train a model that generates data for filling in in one forward pass, instead of relying on traditional discriminative models only. Maybe this is worse, but then it would be an important ablation.

### Questions
How is your approach to regression sampling different from using a well-chosen discretization in combination with a single classification model?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces **UnmaskingTrees**, a novel method for tabular data imputation and generation, leveraging gradient-boosted decision trees. The approach focuses on sequentially “unmasking” individual features using tree models, enabling state-of-the-art imputation performance and competitive generation results. The paper includes experimental results on 27 datasets, showcasing the superior performance of UnmaskingTrees in imputation tasks compared to established methods like MissForest and ForestDiffusion. Additionally, the paper explores the potential of **TabPFN** as a base learner within the UnmaskingTrees framework, demonstrating its flexibility for probabilistic prediction and generative modeling.

### Strengths
1. UnmaskingTrees achieves superior imputation performance, outperforming several popular benchmarks such as MissForest and ForestDiffusion on various metrics.

2. The autoregressive unmasking approach is innovative and avoids the pitfalls of traditional diffusion models for tabular data, including the usage of TabPFN for regression.


3. The proposed model reduces training and inference time by only requiring predictions along a single path in the meta-tree, compared to multiple models in diffusion-based approaches.

4. Extensive benchmarks across 27 datasets with multiple metrics validate the model’s effectiveness across various imputation and generation tasks. And the authors provide code for experiments.

### Weaknesses
1. The training and inference procedure is not clear in writing. Can the authors show a more precise algorithm?
2. The paper do limited ablation to show how the hyperparameters effect the results, like tree depth or duplication factor, especially for large datasets.
3. The results for each dataset in tabular data generation should be shown in the appendix. 
4. For tabular datasets the results are close to each other in value, so the comparison with mean rank of different methods can show the results more clear.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
