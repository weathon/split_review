# Towards Dynamic EHR Phenotyping: A Generative Clustering Model

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
In healthcare, identifying clinical phenotypes—subgroups defined by specific
clinical traits—is essential for optimizing patient care. The wealth of Electronic
Health Record (EHR) information has fueled data-driven approaches to tackle
this challenge. Unfortunately, the heterogeneity, multi-modality, and dynamic
nature of EHR data pose significant hurdles. We propose DeepGC, a novel
generative, clustering, outcome-sensitive end-to-end deep learning (DL) model for
uncovering dynamic phenotypes within temporal EHR data. DeepGC leverages
patient trajectories and outcomes to identify clinically meaningful phenotypes that
evolve over time. Our generative model employs a dynamic sequential approach
based on a Markovian Dirichlet distribution and Variational Auto-Encoders (VAEs),
which is capable of providing insights into the evolution of patient phenotypes
and health status. Preliminary evaluation indicates that DeepGC shows promise
in identifying distinct and interpretable phenotypes, and outperforming existing
benchmarks, particularly with regard to outcome sensitivity (3 % increase in F1).
We also showcase the model’s potential to yield valuable insights into the future
evolution of patients’ health status

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a deep generative model to model longitudinal EHR data as well as to identify clusters. Their model is implemented utilizing RNNs to model the latent state and variational inference is used to learn model parameters. The authors evaluate the utility of the approach on two separate datasets, where they evaluate both clustering and outcome prediction of the model against standard benchmarks.

### Strengths
1. I found the paper very easy to read and follow. 
2. The datasets and empirical evaluation seem reasonable albeit somewhat limited.

### Weaknesses
1. It's not clear to me what outcome prediction task was chosen by the authors. Also, one randomly chosen outcome prediction task seems like a somewhat incomplete evaluation. 
2. I am curious why the authors chose SVM, xgboost as standard outcome prediction methods instead of say more standard time series approaches like RNN and LSTM. It would be nice to see these benchmarks.
3. For both the clustering and the outcome prediction tasks, it is not at all clear from the results that DeepGC is better or significantly better than existing models. 
4. It would be nice to see some interpretation of the learned clusters in the paper to motivate why we need to cluster patients at all.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a generative model designed for patient subgrouping, namely DeepGC. This proposed method is rooted in variational inference to identify phenotypes within temporal clinical data. DeepGC accomplishes this by modeling the joint distribution among input, output, and cluster probabilities derived from observational data, leveraging this joint distribution to generate future data used for making clinical predictions. Experimental results based on two real clinical datasets (HAVEN and MIMIC-IV) demonstrate that DeepGC enhances patient subgrouping capabilities when compared to baseline models.

### Strengths
This paper targets EHR-based clinical risk prediction which is an important research area in machine learning for health.

### Weaknesses
- The paper's technical novelty appears somewhat limited. In particular, it fails to adequately address the unique challenges presented by modeling EHR data compared to other sequential data. It also does not sufficiently explain the novelty in terms of model design compared to existing sequential generative models. It's important to note that in the machine learning context, several VAE-based architectures have been proposed to handle various types of sequential data, such as images, audio, and videos [1, 2].

- The model's design lacks clear explanations or motivation. For instance, it is unclear why VAE was chosen over other generative models for modeling the EHR data distribution. Furthermore, the rationale behind modeling the cluster probability distribution using a Dirichlet distribution remains unexplained.

- Connected to the previous concerns, it's uncertain whether the improvement in prediction performance stems from modeling patient subgrouping or is merely a consequence of the neural network architecture's high capacity. In other words, it is unclear whether patient subgrouping is essential, and the paper does not explore the consequences of removing patient subgrouping from DeepGC. To clarify, why did the authors not use a VAE architecture to model the temporal data (i.e., $P(X,Y)$) directly, instead of modeling $P(X,Y,\pi)$?

- The concerns raised are somewhat substantiated by the results presented in Table 1. The model with strong patient subgrouping performance (TSKM) does not perform well on downstream prediction tasks. Additionally, DeepGC's performance falls within one standard deviation of the second-best baseline models. Consequently, the paper would benefit from statistical testing to establish the significance of the proposed method.

- Several important technical details are omitted, such as the evaluation of patient subgrouping in an unsupervised setting. Furthermore, the paper does not explain how clustering metrics like SIL, DBI, and VRI were calculated. Data statistics and processing steps are also missing, including information about which clinical features were employed and how missing values were handled.

- The paper lacks the provision of code and supplementary documentation, which would enhance clarity and reproducibility.

### Questions
Questions in the above section.

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
Motivation: EHR data lacks labeled phenotypic information, relies on unsupervised learning, hard to validate. Multi-dimensional nature also makes things harder. Previous work is limited to a time frame / not  outcome-sensitive / not end-to-end. 
The authors propose DeepGC combining VAE with dynamic clustering (Markovian Dirichlet distribution) to model physiological status over time. It also also enables generation of future observation data.
Evaluation performed on HAVEN and MIMIC demonstrates good performance over other baselines in all tasks, including clustering and outcome prediction.

### Strengths
- Motivation is clear, and grammar + style is quite fluent
- The work appears to be generally sound, with proofs, and performs well with respect to baselines
- A good number of baselines with respect to the task
- Datasets used to evaluate models are well-known in the field of ML for healthcare

### Weaknesses
 - Please use bolded vectors for variables that are not scalars, e.g. \bm{x} = \{x_1,x_2,...\}
- The figure is slightly pixilated, please use svg or pdf format. Additionally I found it confusing. The green solid line has no arrow, whereas the other lines do. Furthermore, the genreation of x' is not depicted. 
- Paper writing needs some edits. E.g. spaces after commas, X and $X$ both being used to refer to datasets, etc.
- Eqn 1 and the following paragraph has inconsistent $<$ and $\leq$
- Lack of discussion on interpretability, visualization of patient clusters. The paper does not explore how the learned latent space relates to clinically meaningful patient phenotypes. Visualizations, such as t-SNE plots or similar, would be beneficial to understand the structure of the learned representations and the separation of patient clusters.
- No ablations performed. The paper lacks a thorough ablation study to justify the design choices of the proposed model. For example, the contribution of the dynamic clustering component (Markovian Dirichlet distribution) is not isolated, and its impact on the overall performance is not clear. It is also not clear how different choices of the VAE architecture or the RNN would affect the results.

### Questions
- Is it possible to to run results from general tabular data generators, like TabDDPM (https://arxiv.org/abs/2209.15421) or PAR Synthsizer (https://docs.sdv.dev/sdv/sequential-data/modeling/parsynthesizer)?
- Can the authors include s quantitative evaluation of the different patient phenotypes discovered by the algorithm?
- Further analysis of the generated data / more ablations would be useful to see the full scope of the work. E.g. How different is the generated data from the original? Parameter tuning of the RNN? 
- Why does CAMELOT display a similar performance to DeepGC on one dataset and not the others?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present an innovative time-series clustering (phenotyping) approach designed to comprehensively capture both the "observational" and "outcome" dimensions of EHR time-series data. This proposed method incorporates the Dirichlet distribution under a Markovian assumption for cluster assignments and employs a VAE-like structure for forecasting future observations and predicting the outcome of interest, leveraging the cluster assignments and centroids. While distinct from prior works such as AC-TPC, T-Phenotype, and CAMELOT in temporal phenotyping, a comprehensive evaluation of the proposed method's enhancements and technical contributions (from both quantitative and qualitative perspectives) relative to existing approaches is not clear. The authors should provide a thorough exploration of the practical (clinical) validity of the experimental setup on why it is a valid scenario for the proposed method and not for the previous temporal phenotyping works. Moreover, the authors should sufficiently elucidate the implications of different components and design choices such as the number of clusters introduced in the model.

### Strengths
1.	The paper is generally well-written.
2.	The idea of incorporating both the outcome of interest and the observations into clustering is different from previous works.
3.	While utilizing the Dirichlet Process is not new in clustering (e.g., Dirichlet Process Gaussian Mixture Models), the authors effectively contextualize this well-known concept within the dynamic temporal phenotyping framework.

### Weaknesses
1.  The distinction of this work from AC-TPC and T-Phenotype is not clearly articulated in Section 2. These methods are all considered "dynamic temporal phenotyping" approaches, capable of incorporating any outcome of interest at each time step, implying that these method can also consider future (e.g., step-ahead) observations and/or the clinical outcome available at the end of the sequence as their “outcomes” at each time step.
2.  The impact of utilizing both future observations and clinical outcomes is not convincingly motivated nor adequately supported by the experimental results.
3.  The description of performance metrics should assist readers in comparing clustering performance across different methods. Additionally, it is unclear how similarity (distance) is measured to compute the Silhouette Index, Davies-Bouldin Index, and Variance Ratio Criterion. The use of Euclidean distance on time-series data with varying lengths is questionable.
4.  Experimental results on benchmarks and baselines appear incomplete. There is a notable absence of results on AC-TPC (as mentioned in Section 4.2) and T-Phenotype, both of which can incorporate either future observations or final outcomes of interest with a simple modification. Furthermore, results on the Normalized Mutual Information (NMI) are lacking. The discriminative power of the proposed method should be compared with the same network architecture without incorporating clustering, rather than relying solely on simple ML baselines, which may not be suitable for handling time-series data.
5.  The heterogeneity of time-series EHR data, especially its multiple modalities, which motivated this work, is not thoroughly explored. There is no architectural contribution to address this issue, and the modeling of future outcomes with a Gaussian distribution may not be suitable for binary/categorical observations, which are often prevalent in EHR data.

### Questions
1.	Regarding Weakness #2: What clusters were discovered in the experiments, and how do they differ from those in previous works? How do the discovered clusters vary when future outcomes are incorporated, and what happens if they are not?
2.	Regarding Weakness #3: What similarity (distance) metric is used to compute SIL, DBI, and VRI? Are the ground truth future observations taken into account?
3.	The discriminative power is relatively small, and it is not clearly stated how well the evaluated methods and the proposed method handle imbalanced labels. The authors should also provide performance at each class level and AUPRC, which would be more appropriate for assessing methods under imbalance.
4.	How was the number of clusters (K) determined? This is crucial for gauging the discriminative power of the discovered clusters.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
