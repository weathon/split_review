# CODA: Temporal Domain Generalization via Concept Drift Simulator

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
In real-world applications, machine learning models are often notoriously blamed for performance degradation due to data distribution shifts. Temporal domain generalization aims to learn models that can adapt to ``concept drift" over time and perform well in the near future.
To the best of our knowledge, existing works rely on model extrapolation enhancement or models with dynamic parameters to achieve temporal generalization. 
However, these model-centric training strategies involve the \textit{unnecessarily comprehensive} interaction between data and model to train the model for distribution shift, accordingly.\footnote{The fundamental cause in concept drift arises \textit{only} from data perspective.}
To this end, we aim to tackle the concept drift problem from a data-centric perspective and naturally bypass the cumbersome interaction between data and model.
Developing the data-centric framework involves two challenges: (i) existing generative models struggle to generate future data with natural evolution, and (ii) directly capturing the temporal trends of data with high precision is daunting \footnote{Directly predicting a whole dataset requires data distribution estimation, leading to prohibitive computational costs. (Please see Section~\ref{sec:prelim_exp} for more details.)}.
To tackle these challenges, we propose the \Algnameunderline{} (\Algnameabbr{}) framework incorporating a predicted feature correlation matrix to simulate future data for model training.
Specifically, the feature correlations matrix serves as a delegation to represent data characteristics at each time point and the trigger for future data generation. 
Experimental results demonstrate that using \Algnameabbr{}-generated data as training input effectively achieves temporal domain generalization across different model architectures with great transferability.
Our source code is available at: \href{https://anonymous.4open.science/r/coda-D648}{\texttt{https://anonymous.4open.science/r/coda-D648}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a generative approach to mimic the dynamic behavior of instances in temporal domain generalization (TDG). In particular, by modeling the correlation matrices, the proposed simulator can *predict* the data in the future domain to help TDG. The effectiveness of the proposed method is justified by empirical results.

### Strengths
1. Overall, the paper is well presented and easy to follow (though some points are still not clear, please see my comments below).
2. This work studies a challenging but still under-studied problem in the literature.
3. The proposed method demonstrates superior performance over several state-of-the-art methods across multiple datasets.

### Weaknesses
1. I have concerns about the motivation of this paper. In particular, the authors have emphasized that existing TDG methods are model-centric, which are *unnecessarily comprehensive*, and therefore, TDG should be addressed via a data-centric approach. I doubt this point, as generating samples, in principle, is more challenging than discriminating them. With that said, I am not against the approach itself, but the paper presents it in a way that the data-centric itself is superior to model-centric, which I cannot agree with.   
2. In addition, generating the instances itself is challenging, but not necessary -- one may generate the feature samples in the representation space. After all, the ultimate goal is to train a predictor that generalizes well on the future domain rather than to generate the instances themselves. 
3. TDG has been studied recently. However, the authors only review two of them (DRAIN and GI), missing a few related works in the literature (e.g., [1, 2]). In fact, I think [2] also adopted a generative approach that *predicts* the feature domain. The authors should clarify the contributions and novelties given these works.
4. Why modeling the correlation between two consecutive domains is not clear to me. After all, it only captures the second-order information of data.
5. The form of the simulator $\mathcal{G}$ is not clearly defined in the paper. In particular, from Sec. 3.3, it is still not clear to me how the synthetic dataset $\hat{\mathcal{D}}_{T+1}$ is generated from Eq (4). In Appendix B.1 it only says that $\mathcal{G}$ is a generative model, but how the estimated correlation matrix and $\mathcal{D}_T$ are incorporated in the generation process is not clear to me.
6. The empirical analysis is weak. In addition to the baseline algorithms mentioned above. Several commonly used benchmark data sets are also missing, including both synthetic (e.g., Circle, Sine) and real (e.g., RMNIST, Portraits, Ocular, Caltran, WILDS) data sets.

### Questions
1. The definition of correlation matrices is not clear to me. Do they include the label information? If yes, how? If not, how to incorporate the label information to generate discriminative features? Also, what is the dimension of the matrices? If it is high, how to guarantee the consistency of the estimation?
2. In Eq (3), how the cross entropy between two matrices is defined? Why both $\ell_1$ and $\ell_2$ norm regularizations are imposed?
3. Are stage one (Sec. 3.2) and stage two (Sec. 3.3) trained individually or interactively? 
4. I am a little confused with Eq (5): why does the reconstruction loss is defined over two different domains $T+1$ ($\hat{\mathcal{D}}_{T+1}$) and $T$ ($\mathcal{D}_T$)? 
5. I cannot see the connection between Theorem 1 and the proposed method (e.g., Eq (5)). From my understanding, Theorem 1 states that for two random vectors, if they are bounded and their distributions are close, then the difference between their correlation matrices are also bounded. But how this is related to the algorithm? In Eq (5), the distance is already constrained by the regularization term.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on a data-centric approach to tackle the issue, presenting the CODA framework. CODA uses a predicted feature correlation matrix to simulate future data for training, leveraging feature correlations to depict data specifics at particular times. This sidesteps massive computational demands, and experiments show that CODA-enhanced data improves temporal generalization across multiple model designs.

### Strengths
1. The motivation is quite interesting, and it's meaningful to decompose the concept drift into the data component and model component. 
2. The proposed generative method is sound, and the theoretical analysis is also valid.
3. The experiments are well aligned with the three raised research questions.

### Weaknesses
The overall paper suggests a novel way to generate out-of-domain temporal data via generative methods. Even though the motivation is great, the major claim of the paper is to solve the temporal domain generalization, and I am not sure how generating new temporal data can help solve the domain generalization. The provided solution still goes back to train a model to get familiar with the data, and leveraging the generated data to fine-tune existing model-centric methods might have a better result.

### Questions
1. According to the authors, the generated data would still be utilized as the training data for prediction models. Would it still go back to model-centric strategies?
2. The generated data is then used to train models, would it be unfair for comparison methods? Should the comparison methods also use the same generated data to fine-tune?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a data-centric framework named COncept Drift simulAtor (CODA); it aims to address concept drift in temporal domain generalization by predicting feature correlation matrices. The authors start by analyzing the limitations of directly using RNNs for future data generation and propose a two-stage approach: first predicting feature correlations, then generating data based on these correlations. This approach not only captures temporal changes in data distributions more effectively but also generates more accurate future data, improving model generalization.

### Strengths
S1.	Great approach in combining feature correlation prediction with data generation.

S2.	Effective experimental design demonstrating CODA's strengths in certain datasets.

S3.	Clear explanations and logical presentation of the methodology.

### Weaknesses
W1. Limited dynamic network adaptability compared to some existing methods.

W2. Constrained application in model-agnostic learning scenarios.

W3. Potential performance decline in handling high-dimensional data sets.

W4. Exploration of CODA's effectiveness in diverse concept drift scenarios is insufficient.

### Questions
Q1.	In the context of high-dimensional data, how does CODA maintain performance efficiency? Is there an analysis within the study that discusses the computational complexity implications as the number of features increases?

Q2.	Regarding the applicability of CODA, does this methodology account for various natures of concept drift, such as abrupt or cyclical changes?

### Soundness
3 good

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
This paper addresses the problem of performance degradation in machine learning models caused by shifts in data distribution over time, known as "concept drift." Existing solutions primarily rely on model-centric strategies, such as model extrapolation or dynamic parameters. This work proposes a data-centric framework called the COncept Drift simulAtor (CODA). CODA leverages a predicted feature correlation matrix to simulate future data for model training. This matrix represents data characteristics at each time point and serves as a trigger for generating future data. The propose method achieves state-of-the-art (SOTA) accuracy on some classification and regression problem. Further, it is shown that using CODA-generated data for training enables effective temporal domain generalization across various model architectures, demonstrating high transferability.

### Strengths
- The paper achieves the state-of-the-art results in temporal domain generalization and beats DRAIN (which is the current SOTA method).
- I appreciate the author's great effort to provide implementation details and ablation studies.
- The paper introduces a theorem about the usage of the prior knowlege in the proposed formulation and prove it.
- The paper is well-written and well-organized in overall.

### Weaknesses
## Major concerns
- The proposed algorithm's applicability seems limited to low-dimensional data, as also acknowledged by the authors. The computational cost of learning the correlation matrix becomes prohibitive with high-dimensional data, potentially explaining the exclusion of datasets like rotating MNIST. Specifically, the correlation matrix computation scales quadratically with the number of features, making it intractable for datasets with a large number of features. This limitation significantly restricts the method's practical applicability in many real-world scenarios where high-dimensional data is common.
- While the proposed method achieves state-of-the-art accuracy, the multi-step nature of the approach raises concerns about its overall efficiency and intuitiveness. The method involves (1) learning the correlation matrix, (2) learning the data simulator, (3) tuning the data simulator, and (4) learning the final classifier/regressor. This contrasts with the end-to-end learning paradigm often preferred in deep learning, where joint optimization often leads to better performance. The computational overhead of these multiple stages, particularly the correlation matrix computation, needs further investigation and comparison against existing methods.
- An alternative approach for future data simulation could involve training a conditional data generator that utilizes the time index as a condition. This is conceptually similar to how diffusion models incorporate time information. Encoding the time index with techniques like Position Embedding could provide a more direct way to model temporal dependencies in the data generation process, potentially simplifying the overall pipeline.

## Minor concerns
- The explanation regarding the tuning of the data simulator based on the classification/regression models lacks clarity. It is unclear how this tuning process is performed, whether it involves a separate optimization step, and how it impacts the overall training procedure. A more detailed description of this step is necessary to fully understand the proposed method.
- The current formulation, as shown in Eq. (5), only considers the last domain for data simulation and does not incorporate information from all previous domains. This raises questions about the method's ability to capture long-range temporal dependencies and whether incorporating a broader historical context could improve performance.

### Questions
I explained them above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
