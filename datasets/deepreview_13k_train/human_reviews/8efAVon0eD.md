# OOD-Chameleon: Is Algorithm Selection for OOD Generalization Learnable?

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Out-of-distribution (OOD) generalization is challenging because distribution shifts come in many forms.
    A multitude of learning algorithms exist and each can improve performance in \emph{specific} OOD situations.
    We posit that much of the challenge of OOD generalization lies in \emph{choosing the right algorithm for the right dataset}. 
    However, such algorithm selection is often elusive under complex real-world shifts.
    In this work, we formalize the task of \emph{algorithm selection for OOD generalization} and investigate whether it could be approached by learning.

    We propose a solution, dubbed \alg that treats the task as a supervised classification over candidate algorithms.
    We construct a \emph{dataset of datasets} to learn from, which represents diverse types, magnitudes and combinations of shifts (covariate shift, label shift, spurious correlations).
    We train the model to predict the relative performance of algorithms given a dataset's characteristics.
    This enables \emph{a priori} selection of the best learning strategy,
    i.e.\ without training various models as needed with traditional model selection.

    Our experiments show that the adaptive selection outperforms any individual algorithm
    and simple selection heuristics,
    on unseen datasets of controllable and realistic image data.
    Inspecting the model shows that it learns non-trivial data/algorithms interactions,
    and reveals the conditions for any one algorithm to surpass another. 
    This opens new avenues for (1)~enhancing OOD generalization with existing algorithms instead of designing new ones, and (2)~gaining insights into the applicability of existing algorithms with respect to datasets' properties.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors formulate a new problem setting of predicting the performances of multiple algorithms on a given dataset without training models. They propose a framework called OOD-CHAMELEON to address this setting.

### Strengths
The problem setting is novel.

### Weaknesses
1. The practice of predicting performance with only some simple characteristics of the dataset and an algorithm represented by a one-hot vector does not really make sense to me. Given a learning algorithm and a dataset, there are too many other factors that could largely influence the final trained model, including hyperparameters. However, all other factors are ignored in this setting. The concern about hyperparameters is particularly significant. While the authors propose a novel problem setting, the exclusion of hyperparameter tuning in the prediction process raises questions about the practical applicability of the framework. Different hyperparameter settings can drastically alter the performance of an algorithm on a given dataset. Without considering this aspect, the predictions may not accurately reflect real-world scenarios.
2. Experiments are not sufficient enough to support the claims made in the paper.
   - Only five algorithms are selected as candidates while there are various OOD algorithms besides them. I believe at least several SOTA or influential algorithms could be added. Specifically, the inclusion of more recent and widely recognized OOD algorithms would strengthen the experimental validation. The current selection appears limited and may not fully represent the diversity of approaches in the field.
   - Only two real-world datasets are included. Expanding the dataset variety would provide a more comprehensive evaluation of the proposed framework. The current datasets, while relevant, might not capture the full spectrum of challenges encountered in OOD generalization.

3. The writing seems poor. 
   - The writing seems awkward in some places. 
     - In Line 018 "treats the task as a supervised classification"
     - In Line 025 "on unseen datasets of controllable and realistic image data". 
     - In Line 110, "It consists in predicting the best strategy to obtain a robust model given a statistical descriptor of the dataset." Here "consist in". 
   - The writing seems imprecise/ambiguous in some places. 
     - In Line 052 "A well-known study by Gulrajani & Lopez-Paz (2020) showed that none of these methods surpasses an ERM baseline across a collection of datasets." If here "these methods" refer to the upper line, then "the more complex ones" in Line 051 are not included since there are many new algorithms proposed in recent three years that are not included in the paper of DomainBed. 
     - In Line 075 "We posit that OOD generalization can be improved if we knew which algorithm to apply in each situation" why use "knew" instead of "know" here?  
     - In Line 105, "our findings call for improving OOD generalization by learning to better apply existing algorithms, instead of designing new ones." Here "instead of designing new ones" might be interpreted as designing new algorithms is less useful than learning to apply existing algorithms. 
   - The notations are not clear enough and some are abused. 
     - There are multiple confusions of variables and sets. For example, in Section 2.1, $X$ seems to be a random variable, however in $x\in X$, it seems to be the support set of the input variable. In Section 2.2, $\mathcal{A}(\cdot):D^{tr}\rightarrow h_{\theta}$, when defining a function mapping, it should be between two sets. However, here $D^{tr}$ is a dataset instead of the data space and $h_{\theta}$ is a detailed hypothesis instead of a hypothesis space. 
     - In Line 130, is $X_c$ a subset of variables of the input? This should be clarified. 
     - In Line 206, $|\mathcal{G}\_i|=n_{te}/i$. I suppose here $i$ is a wrong notation, which should be replaced by the number of groups.

### Questions
1. In this paper, distribution shifts are categorized into three categories. However, any distribution shift can be decomposed into covariate shift and concept shift. Why is label shift required when shift on $P(X)$ and $P(Y|X)$ both exist? 
2. In Line 132, "A shift of spurious correlations implies a variation of an attribute/label co-occurrences, which means a shift on $P(Y|A)$ but not $P(Y|X_c)$." Previously the spurious correlation is stated as shift of $P(Y|X)$. However, if $X_c$ is a subset of variables of $X$, and if there is no shift on $P(Y|X_c)$, there should not be shift on $P(Y|X)$ since $P(Y|X)=P(Y|X_c)$. 
3. In Equation 2, why is the positive correlation between $y$ and $a$ considered as spurious correlation, while the negative correlation is not considered? In other words, when $d_{sc}$ is close to 1 or close to 0, both circumstances could imply strong spurious correlations.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose an approach to algorithm selection for OOD generalization by treating it as a supervised classification problem over candidate algorithms. They introduce OOD-CHAMELEON, a system that constructs a dataset of datasets representing various distribution shifts and trains a model to predict the relative performance of algorithms based on dataset characteristics. The experiments demonstrate that OOD-CHAMELEON can outperform individual algorithms and simple selection heuristics on unseen datasets with controlled and realistic image data. The paper also inspects the model to reveal non-trivial data/algorithm interactions and conditions under which one algorithm might surpass another, offering insights into the applicability of existing algorithms.

### Strengths
Characterizing different OOD generalization tasks as distinct objectives and then selecting different methods to address those objectives is a reasonable approach. This strategy could have implications for the practical application of machine learning algorithms.

### Weaknesses
1. The contributions of this paper seem insufficient to me. The three proposed methods are all based on existing simple techniques and don't provide genuinely new insights into algorithm selection for different OOD problems.
2. While using a learning-based approach for method selection is a promising idea, this paper doesn't delve into a crucial aspect: why this problem is learnable in the first place. There's no discussion about the differentiability or continuity of the problem of selecting the optimal algorithm for different datasets. To me, it's a good direction, but the solution likely isn't straightforward. It might require some specialized design and deeper insights to properly address the inherent challenges of learning algorithm selection.
3. Although the paper is complete in content, the layout of some parts is slightly compact, especially the algorithm description and experimental parts, which lack a clear modular structure. Some paragraphs are too long and the reading experience is poor. If the algorithm description, experimental design, and result analysis are divided into clearer sub-modules, the reading fluency may be improved.

### Questions
1. How efficient is OOD-CHAMELEON in processing large-scale data sets? 
2. Are there any further optimization solutions to improve its efficiency in practical applications?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work focuses on the development of a method for selecting algorithms, specifically with the goal of OOD generalization. Optimal selection of algorithms may depend on the type of shift which has occurred and what the algorithm is tailored to handle.


The proposed selection method, named OOD-chameleon, is a learnable method which aims to solve a classification task over a set of candidate algorithms.

The supervision of this task is proposed to be based on a meta-dataset which contains many datasets with different types of shifts and the candidate algorithms performances on these. The datasets are represented by dataset descriptors which contain measures of the distribution shift and data complexity.

These datasets are then constructed by sampling from synthetic distributions or from real-world datasets in the empirical evaluation of the method. The evaluation shows that the method selection performs better than just selecting the best performing model overall. Further, the authors show that leaving some dataset descriptors out of the meta dataset description can severely hamper the performance of the selected algorithm. This implies that certain information is more valuable when making a selection, depending on the algorithm characteristics.

### Strengths
- The possibility of learning how to select algorithms based on dataset characteristics is very interesting

- The motivation for the work is clear

- The performance of the method is good and makes the case for using properties of the data to select different algorithms on a per dataset  basis

### Weaknesses
 - My main concern is the need to know the attributes that are shifting a priori. Finding the proposed metrics for different real-world datasets is not something straightforward. It is furthermore unclear how we would get at these metrics in general if they are not given. Specifically, the paper does not adequately address the challenge of identifying and quantifying distribution shifts in real-world scenarios where the underlying causes of the shift are unknown. The reliance on pre-defined metrics, such as those based on known spurious attributes, limits the applicability of the method to situations where the shift is well-understood and easily measurable. This is a significant limitation, as many real-world OOD problems involve complex, multi-faceted shifts that are not easily captured by simple metrics. 

- The choice of attributes seem central for the approach to work at all. If the attributes used are not correlated to the shift it seems unlikely that the selection would be good for OOD generalization. The paper does not provide a clear methodology for determining which attributes are most relevant for a given dataset and algorithm. The selection process seems highly sensitive to the choice of attributes, and a poor choice could lead to suboptimal performance. Furthermore, the paper does not explore the impact of using noisy or irrelevant attributes, which could be a common occurrence in real-world datasets. This lack of robustness is a major concern.

- Unclear why other baselines like Öztürk et al. cannot be compared to, would the comparison be unfair?

Typos and other comments:
Maybe add a line defining the performance $P_j$ on page 3

line 428: outperform
line 905: we 9

### Questions
- How would you construct a meta-dataset in cases where the shift is not obvious or when the attribute is not labeled in the datasets? 

- Does the coverage of the distribution over shifts impact results? For example, if the types of shifts are not equally represented in the meta-dataset or only some magnitudes of spurious correlation are represented.

- Would the space required to store the meta-dataset not get out of hand if you consider that a tunable model could have several entries with different values of one or several hyperparameters? Is there a way to mitigate this?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work introduces OOD-CHAMELEON, a method for selecting the most suitable learning algorithm for out-of-distribution (OOD) generalization challenges. By treating algorithm selection as a supervised classification problem, the proposed solution learns from a dataset of diverse shifts to predict the relative performance of algorithms based on a dataset’s characteristics. This allows for the a priori selection of the best learning strategy. Experimental results demonstrate that the adaptive selection approach outperforms individual algorithms and simple heuristics on unseen datasets with controllable and realistic image data, revealing some interactions between data and algorithms.

### Strengths
1) The approach improves the ability to generalize in OOD scenarios by selecting the most appropriate algorithm for a given dataset’s characteristics.
2) OOD-CHAMELEON eliminates the need for training and evaluating multiple models for algorithm selection, leading to a more efficient use of computational resources.
3) The method provides interesting insights into the conditions under which different algorithms are more suitable.

### Weaknesses
1) The underlying concept of this article seems to require theoretical support. Selecting the most appropriate model based on data characteristics appears to be more challenging than learning a predictive model. To truly excel in this area, I believe a substantial number of datasets are needed for validation. However, in real-world scenarios, there may not be an abundance of datasets available. Therefore, further analysis and discussion are needed to determine the minimum number of datasets required to effectively choose the right model. Specifically, the paper lacks a discussion on how the dimensionality and diversity of the dataset feature space impacts the performance of the algorithm selector. It's unclear how the method would perform if the datasets used for training the selector have a significantly different feature space compared to the target dataset. This is a critical point because the effectiveness of the selector hinges on its ability to generalize across different feature spaces, not just different distributions within the same space.
2) The experimental section of this paper uses a few datasets and models, which is insufficient to fully validate the method proposed in this paper and the insights provided. The paper should include a more diverse set of datasets, including those with different modalities (e.g., text, audio) and different types of distribution shifts (e.g., covariate shift, label shift). Furthermore, the model selection should be tested on a wider range of algorithms, including more complex models and ensemble methods, to demonstrate the robustness and generalizability of the proposed approach. The current experimental setup is too limited to draw strong conclusions about the effectiveness of the method in real-world scenarios.
3) The performance of a model also depends on how well it is optimized on the dataset. Please provide specific details on the training process for each model, particularly whether the model’s parameters have been optimized to their best possible values. The paper should detail the hyperparameter tuning process for each algorithm, including the range of values explored and the criteria used for selection. Without this information, it's difficult to assess whether the observed performance differences are due to the algorithms themselves or to suboptimal hyperparameter settings. It's also important to discuss the computational cost associated with the hyperparameter tuning process, as this can be a significant factor in practical applications.

### Questions
Directly training multiple models and then aggregating their outputs might yield better results than the method proposed in this paper. In practical applications, what are the advantages of the method proposed in this paper compared to the ensemble model approach?

### Soundness
2

### Presentation
2

### Contribution
2
