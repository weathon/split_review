# Unlocking the Potential of Model Calibration in Federated Learning

- Decision: Accept
- Scores: 8, 5, 5, 6

## Abstract
Over the past several years, various federated learning (FL) methodologies have been developed to improve model accuracy, a primary performance metric in machine learning. However, to utilize FL in practical decision-making scenarios, beyond considering accuracy, the trained     model  must also have a reliable confidence in each of its predictions, an aspect that has been largely overlooked in existing FL research. Motivated by this gap, we propose Non-Uniform Calibration for Federated Learning (\texttt{NUCFL}), a generic framework that integrates FL with the concept of \textit{model calibration}. The inherent data heterogeneity in FL environments makes model calibration particularly difficult, as it must ensure reliability across diverse data distributions and client conditions.  Our \texttt{NUCFL} addresses this challenge by dynamically adjusting the model calibration objectives based on statistical relationships between each client's local model and the global model in FL.  In particular, \texttt{NUCFL} assesses the similarity between local and global model relationships, and controls the penalty term for the calibration loss during client-side local training.  By doing so, \texttt{NUCFL} effectively aligns calibration needs for the global model in  heterogeneous FL settings while not sacrificing accuracy. Extensive experiments show that \texttt{NUCFL} offers flexibility and effectiveness across various FL algorithms, enhancing accuracy  as well as model calibration.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the issue of model calibration in federated learning (FL), with a specific focus on heterogeneous scenarios, characterized by distribution shifts across clients. The paper argues that most works have focused on improving the accuracy of the proposed methods so far, but almost no attention has been given to the model's confidence in its predictions. This highlights a gap in the current literature: FL models should hava reliable confidence in their predictions to be deployed in real-world use cases. To fill this gap, this work introduces Non-Uniform Calibration for Federated Learning (NUCFL), a novel method to integrate FL with model calibration, that can be easily combined with existing approaches.

The work discusses the various benefits of NUCFL, studying its application with several calibration approaches and FL methods, showing its effectiveness in improving the model's confidence in its predictions, according to multiple metrics.

### Strengths
- The paper underlines a gap in the current FL research and proposes an effective method to address it
-  NUCFL can be easily added on top of existing methods
- The paper extensively shows the efficacy of NUCFL across various settings, model architectures and methods
- NUCFL is extensively studied through in-depth and well-carried analyses
- NUCFL does not increase communication costs

### Weaknesses
 - Difficulties in proving NUCFL's convergence and theoretical properties, as also pointed out by the authors
- The paper argues that works like Zhang et al. [2022] and Luo et al. [2021] misuse the term "calibration" and do not further analyze the comparison with those methods. However, I believe it would still be relevant to the FL community to understand how NUCFL compares to them. 
- The application of NUCFL seems limited to supervised scenarios

### Questions
- Could the authors provide a comparison between NUCFL and Zhang et al. [2022] and Luo et al. [2021], according to the introduced metrics?
- Does NUCFL increase computational costs on the client-side?
- How could NUCFL be adapted to unsupervised/semi-supervised settings?
- How sensible if NUCFL to the hyperparam $\beta$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a model calibration method for federated learning, which adaptively adjusts penalties based on the relationship between local and global models.

### Strengths
The motivation makes sense.

The paper is well-written and easy to follow.

### Weaknesses
The contribution of this paper is limited. The proposed method seems a simple incremental work of the existing FL model calibration method.

Although I understand the author's motivation, I need the author to explain why the proposed metric is more important than accuracy. The proposed metrics are not intuitive enough. Typically, accuracy and the proposed metric are positively correlated. The author should add some detailed experiments to validate its motivation.

The experimental results show that The proposed method is only slightly optimized for federated learning. In addition, the proposed method may cause a decrease in accuracy in some scenarios.

Lake of comparison with SOTA FL optimization methods [1-5]. These methods achieve better model performance by guiding the model to optimize towards the flat region. I think these methods can still reduce the measures proposed by the author. I wonder if the author can compare these methods or integrate the proposed method into them.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper aims to ensure the reliability of FL in real-world applications. It proposes Non-Uniform Calibration for Federated Learning (NUCFL) that integrates FL with model calibration to achieve the goal. NUCFL dynamically adjusts the model calibration objectives by measuring the relationships between the local and the global model. Experiments show the superiority of NUCFL compared with existing FL methods.

### Strengths
[1] The paper takes an important step to explore FL from the perspective of model calibration, which is important to various decision-making scenarios. 

[2] Extensive experiments are carried out to show that NUCFL can seamlessly integrate with existing FL methods and improve the original performance of those methods.

### Weaknesses
[1] It is unclear whether there is a trade-off between accuracy and reliability. If so, please give a detailed illustration of this aspect. If not, the advantage of not sacrificing accuracy seems an irrelevant contribution. 

[2] The relation between model calibration and enhancing the confidence of FL outputs is weak. It requires further demonstration and analysis of why model calibration can realize that. 

[3] It is better to provide a further investigation into how existing centralized calibration methods can adapt to the FL setting, for example, simply combining them with FedAvg framework. Empirical studies can also involve this part.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper contributes to a well-established line of research that adapts standard machine learning (ML) techniques for federated settings by leveraging the similarity between global and local models to weight client contributions. Here, the ML technique under adaptation is model calibration, achieved through an auxiliary loss function. The paper’s primary contribution is a proposal to weight this auxiliary calibration loss based on a customizable similarity metric between global and local models, such as cosine similarity or other advanced measures. In this context, the “local” model refers to the locally trained replica of the global model. The authors provide an extensive empirical evaluation on standard federated learning datasets for computer vision, using LDA to generate non-IID partitions for IID datasets and some naturally heterogeneous datasets as well (FEMNIST). Their results indicate improved performance over baseline methods across all datasets, models, and levels of data heterogeneity.

### Strengths
- Comprehensive Evaluation: Experiments are extensive and demonstrate consistent improvements across datasets, models, and non-IID settings.
- Writing and Presentation: The paper is well-written, with clear diagrams and formatting that aid readability.
- Practical Relevance: The method holds strong practical implications, bringing effective calibration methods to FL.

### Weaknesses
I must mention that I am much more familiar with FL than model calibration and thus focus on this side of the work.

- Limited Novelty in Core Insight: Although the similarity-based weighting approach is practical, it is not particularly novel, e.g.,[1,2,3]. The authors do acknowledge the influence of prior FL works that leverage model similarity metrics. 
- Potential Sensitivity to Hyperparameters: The method might be sensitive to local training hyperparameters like learning rate and epoch count, which could impact the similarity measure’s effectiveness. In cases closer to FedSGD with only one or a few steps performed, data heterogeneity may minimally impact the model replica, potentially diminishing the relevance of the similarity function. Similarly, scenarios involving extensive local training or very high learning rates may affect the similarity measure’s utility as all models may diverge very far from the global model regardless of the degree of local data heterogeneity. 
- No Exploration of Alternative Similarity References: Using only the client’s local model replica as the similarity reference could limit the applicability; other approaches (e.g., auxiliary persistent local models or specific personalized layers) might better capture client-specific characteristics.

### Questions
1. Can the authors provide any insight on how would the proposed approach perform under different local training conditions? For example with minimal local training (≤ 1 epoch or with very low learning rates) or extensive local training (e.g., training the local model to convergence or near convergence every round).
2. Have the authors considered the use of auxiliary local models or personalized layers, to compute similarity? 
3. Why did the authors decide to use raw similarity/relevance values rather than a softmaxed version with a normalization factor constructed based on the entire distribution of client similarities?

### Soundness
3

### Presentation
3

### Contribution
2
