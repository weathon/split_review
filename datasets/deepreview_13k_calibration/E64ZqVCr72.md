# Active Domain Adaptation Of Medical Images Using Feature Disentanglement

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
State-of-the-art deep learning models often fail to generalize in the presence of distribution shifts between training (source) data and test (target) data. Domain adaptation techniques have been developed to address this challenge, leveraging either labeled data (supervised domain adaptation) or unlabeled data (unsupervised domain adaptation). The careful selection of target domain samples can significantly enhance model performance and robustness, while also reducing the overall data requirements. Active learning, a strategy for intelligently choosing informative samples with minimal annotation effort, offers a means to maximize performance. In this paper, we introduce an innovative method for active learning in the presence of domain shifts. We propose a novel feature disentanglement approach to decompose image features into domain-specific and task-specific components. Thereafter we define multiple novel cost functions that identify informative samples under domain shift. We test our proposed method for medical image classification using one histopathology dataset and two chest x-ray datasets. Experiments show our proposed approach achieves state-of-the-art performance when compared to both domain adaptation methods and other active domain adaptation techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method that uses feature disentanglement for active learning. The method is demonstrated under domain shift, i.e. actively selecting examples for further training so as to adapt to a shifted target domain. Results are given on multi-centre histopathology and chest x-ray datasets.

### Strengths
The method involves an informativeness score that combines measures of uncertainty, “domainness”, density, and novelty. There is some novelty in this.
Fairly extensive experiments are reported incorporating 6 methods from the literature on two medical applications using public datasets. Overall the performance seems promising.
Under “Ablation Studies” each of the free parameters in the loss and informativeness score (Eqns (10 and (11)) is set to zero in turn and the effect on performance measured. This is a useful experiment to show that each term has an effect (although in a few cases removal of L_1 or Q_unc seems to have helped, and that could be commented upon).

### Weaknesses
My main criticism is that the method has 4 free parameters in the loss function (Equation (1)) and another 4 in the informativeness score (Equation (11)). This is a high number of hyperparameters to set empirically and it needs to be clear that this has been done carefully and reproducibly. For the histopathology and CheXpert experiments, values are stated without any explanation of how these values were arrived at. This needs some comment, and in particular we need to know for certain that these values were determined without using test data in any way. For the NIH ChestXray experiment, subsection 4.4 describes a greedy hyperparameter search; again it needs to be clarified that test data were not used in this search (presumably). If test performance was used in this search then the results would be invalid. Hopefully this is not the case.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an innovative active learning method for domain adaptation. The problem at hand involves two data domains: the source and target domains, with a distribution shift between them. The algorithm comprises two key steps. In the first step, data (images) in both domains are transformed into a latent space using two separate autoencoders, and the feature representations in the latent space are disentangled into domain-specific and task-specific representations. It is assumed that the domain-specific representations account for the distribution shift. In the second step, criteria were designed to select informative unlabeled image samples in the target domain for labeling. The labeled image samples are then added to the labeled image samples from the source domain to update the classification model trained on the labeled data from the source domain. This process can be repeated multiple times. The proposed method was evaluated on two public image analysis datasets and outperformed several state-of-the-art active learning methods and a couple of domain adaptation algorithms.

### Strengths
1. Incorporating active learning, feature disentanglement, and domain adaptation all together seems to be an innovative idea.
2. The proposed metrics for identifying informative image samples based on disentangled feature representations appear to be effective.
3. The proposed algorithm was evaluated on two relatively large medical imaging datasets, and it achieved superb results.

### Weaknesses
1. The two medical image datasets are quite large. In the experimental setting, at least 10% of the unlabeled data samples in the target domain were selected for labeling and added to the source domain's labeled data to update the classifier. While 10% still represents a significant number, considering the constraints in the research setting—such as limited and expensive expertise in the medical field—it would be more valuable to evaluate the effectiveness of the proposed method with much fewer labeled samples from the target domain, for example, 0.1% or 1%. Unfortunately, this aspect is missing in the paper. The current evaluation does not adequately address the practical scenario where labeled data acquisition is extremely costly, and the proposed method's performance with very limited target domain labels remains unclear. Specifically, the paper lacks an analysis of how the performance degrades as the number of labeled target samples decreases below 10%, which is a critical aspect for real-world applicability.

2. The discussion section or the presentation of the paper could be improved. For instance, in the ablation study, each component of the loss function and the metrics for identifying informative data samples was thoroughly examined, and their contributions were reported in the tables. However, there is a lack of in-depth discussion and no clear claims have been made regarding which component contributes more. It is not readily apparent to readers which component has the most significant impact. The ablation study, while comprehensive in terms of the components examined, fails to provide a clear narrative on the relative importance of each component. The paper presents the results in tables but does not offer sufficient analysis to guide the reader on which component is most crucial for the method's performance. This lack of discussion makes it difficult to understand the core mechanisms driving the method's success.

### Questions
In the algorithm description, the authors initially state that feature disentangling was performed jointly using data samples from both the source and target domains. However, they later mention that the process was performed using data solely from the source domain. Which statement is correct?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a novel strategy for performing domain adaptation in an active learning scenario. 
The method is based on learning disentangled representations referred to domain and task, from which an informative score is computed on samples from the target domain. The most informative samples (below a certain available budget) are chosen and added to the training set.

### Strengths
- The proposed method is interesting and seems to provide good performance

- The problem tackled is very relevant in the medical field due to the cost of annotating data

### Weaknesses
 - The proposed method is not simple in terms of optimizations: 5 different losses are used, each with its own hyperparemeter. Also the informative score introduces many hyperparamers. Choosing many hyperparameters is not trivial, and authors report some arbitrary value for them. How were they chosen? It is not completely clear

- The tables are hard to read, best results are not highlighted. I also suggest author report a standard devation, especially in the higher p-value cases

- I think the experimental validation is somewhat lacking, as only two settings were explored (histology and cxr images). I suggest authors also include other modalities or tasks. For example brain MRI with the task of brain age regression (particularly relevant for domain shift), or image segmentation.

### Questions
See weaknesses.

Additional questions: 

- Could your framework be adapted to other tasks such as segmentation or regression (as mentioned in the weaknesses)?

- In your experimental protocol (Sec. 4.1) you select at each step 10% of the size of the training data from the target set. This means that the added samples will be in minority in the training set. Have you also tried reweighting them in the classification loss? Can this help in reducing the number of samples required for better AUC? 

- For improving the readability of this work, I think that the results could be presented in from of plots of AUC vs size rather then big tables

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method for combining active learning techniques with domain adaptation. They propose an algorithm for learning task-specific and task-shared features, along with several metrics which are supposed to quantify informativeness of samples for active learning. They evaluate their method on 2 datasets from the medical imaging domain, showing an improvement over the baselines.

### Strengths
- Authors performed ablation studies for all proposed modifications
- The proposed approach achieves (slightly) better results than baselines

### Weaknesses
1. The paper seems written in a rush and it’s difficult to read at times
2. Using features of a pre trained classifier for L_base does not need to identify the correct task-specific features. Nothing prohibits the model from a) extracting task-independent features and assigning them zero weights in the final classification layer and b) collapsing to the target variable already in the hidden layer (or the logit distribution)
3. The density estimation approach is incorrect. You cannot reason about probability densities by comparing cosine similarities of **arbitrarily distributed** vectors (e.g., imagine the case where several dimensions are strongly correlated).
4. In fact most of your objectives suffer from that same problem - the similarities can easily be inflated if multiple dimensions are not independent. Consider using a more probabilistically sound approach, e.g., by incorporating models such as normalizing flows

### Questions
1. “Given source and target domains S and T, an ideal domain independent feature’s classification accuracy on domain S is close to those obtained using the original images’ features.” - I do not understand this sentence
2. How did you select the hyperparameters (e.g., the percentiles for similarity cutoffs)? Actually looks like you just fitted the hyperparameters to the final results? Which is incorrect? How did you select hyperparameters for the baselines ?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor
