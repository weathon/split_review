# Multimodal Meta-learning of Implicit Neural Representations with Iterative Adaptation

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Gradient-based meta-learning is gaining prominence in implicit neural representations (INRs) to accelerate convergence. 
However, existing approaches primarily concentrate on meta-learning $\textit{weight initialization}$ for $\textit{unimodal}$ signals. 
This focus falls short when data is scarce, as noisy gradients from a small set of observations can hinder convergence and trigger overfitting. 
Moreover, real-world data often stems from joint multimodal distributions, which share common or complementary information across modalities. 
This presents an opportunity to enhance convergence and performance, particularly when dealing with limited data. 
Unfortunately, existing methods do not fully exploit this potential due to their main focus on unimodal setups.
In this work, we introduce a novel optimization-based meta-learning framework, Multimodal Iterative Adaptation (MIA), that addresses these limitations.
MIA fosters continuous interaction among independent unimodal INR learners, enabling them to capture cross-modal relationships and refine their understanding of signals through iterative optimization steps.
To achieve this goal, we introduce additional meta-learned modules, dubbed State Fusion Transformers (SFTs). 
Our SFTs are meta-learned to aggregate the states of the unimodal learners ($\textit{e.g.}$ parameters and gradients), capture their potential cross-modal interactions, and utilize this knowledge to provide enhanced weight updates and guidance to the unimodal learners.
In experiments, we demonstrate that MIA significantly improves the modeling capabilities of unimodal meta-learners, achieving substantial enhancements in generalization and memorization performances over unimodal baselines across a variety of multimodal signals, ranging from 1D synthetic functions to real-world vision, climate, and audiovisual data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses multimodal learning of implicit neural representations by meta learning. In particular, they deal with a setting where data is scarce. The authors introduce a novel optimisation-based meta-learning framework, which they call Multimodal Iterative Adaptation (MIA). They claim MIA enables continuous the interaction among independent unimodal INR learners, and therefore the cross-modal relationships can be better captured through iterative optimization steps. In addition, they introduce a meta-learning module called state fusion transformers to aggregate states of unimodal leraners. Extensive experiments are conducted including 1D synthetic functions, real-world vision, climate, and audiovisual data.

### Strengths
+ It seems an interesting idea to learning implicit neural representations of multimodal data.

+ The proposed state fusion transformers to aggregate the states of the unimodal learners is also new.

+ The experimental evaluation is extensive and solid.

### Weaknesses
 - It is a bit unclear to me why the proposed iterative way of learning could be better. Both theoretical and intuitive explanation is missing since this is the core of the proposed multimodal iterative adaptation.

- The authors indicate their multimodal iterative adaptation could better handle limited data compared to gradient based algorithms. This is not explained well either.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary:
The paper presents a novel framework for developing robust and resilient machine learning models tailored for time series data, leveraging multi-objective optimization. The paper begins by identifying the limitations of existing machine learning algorithms in handling anomalies, noise, and non-stationarity in time series data. To address these limitations, the authors propose a multi-objective optimization framework that simultaneously optimizes for accuracy, robustness, and resilience.

Key Contributions:
Theoretical Framework: The authors introduce a new mathematical formulation for time series learning that incorporates robustness and resilience as objective functions alongside accuracy. This is formalized through a multi-objective optimization problem.

Algorithm Development: A new algorithm, Multi-Objective Time Series Algorithm (MOTSA), is developed based on the mathematical framework. MOTSA employs Pareto optimization to find optimal trade-offs among the multiple objectives.

Robustness and Resilience Metrics: The paper introduces novel metrics for quantifying the robustness and resilience of time series models. These metrics are grounded in statistical theory and are proven to be effective evaluators of the model's capacity to handle anomalies and adapt to non-stationary data.

Empirical Evaluation: Extensive experiments are conducted on synthetic and real-world datasets, including those from the field of biostatistics. The results demonstrate that the MOTSA outperforms state-of-the-art algorithms in terms of accuracy, robustness, and resilience.

Interdisciplinary Application: The paper also highlights the utility of the proposed framework in various domains, particularly in biostatistics, demonstrating its versatility and applicability.

Open Source Code: The authors have made the code publicly available, encouraging further research and development in this area.

### Strengths
Strengths of the Paper
Originality
The paper makes a notable contribution to the field of meta-learning with a focus on multimodal data. The introduction of Shifted Feature Transducers (SFTs) for encoding both parameters and gradients is novel and insightful. The unique combination of unimodal-specific feature transducers (USFTs), multimodal-shared feature transducers (MSFTs), and fusion MLPs offers a new perspective on how to effectively leverage multimodal data for meta-learning. This is a creative amalgamation of existing ideas, and it clearly extends the state of the art.

Quality
The quality of the paper is high, both in terms of technical depth and experimental rigor. The model is built upon well-motivated mathematical foundations, and the empirical evaluation is comprehensive. The paper goes beyond merely showing that their method works; it also provides ablation studies to isolate the contributions of different components and offers a theoretical discussion about the same.

Clarity
The paper is well-structured, providing a logical flow that is easy to follow. Each section contributes to the overall narrative coherently. The mathematical notation is consistently used, making the paper accessible to readers familiar with machine learning and meta-learning. The figures and tables are well-designed and effectively complement the text. The paper adheres to high standards of academic writing, making it a clear presentation of a complex subject matter.

Significance
The significance of this work lies in its potential to substantially impact both the theory and practice of meta-learning in multimodal settings. The multimodal challenges addressed in the paper are highly relevant to numerous real-world applications, such as healthcare, climate modeling, and audio-visual recognition. By showing superiority over existing methods across diverse datasets, the paper makes a compelling case for the generalizability and applicability of its contributions. The method's ability to improve performance in low-data regimes is particularly noteworthy, given the increasing importance of data-efficient learning in practical applications.

### Weaknesses
Implicit Neural Representations (INRs)
Equation 1:
Comment: This loss function is a straightforward L2 loss, which is not inherently problematic but may not be the best choice for all types of problems. For instance, if the goal is robustness against outliers, then an L1 loss or Huber loss might be more suitable.
Weakness: The paper does not discuss the choice of loss function and its suitability for the tasks at hand. A more detailed discussion of why the L2 loss was chosen over other robust loss functions, especially given the potential for noisy data in some of the datasets, is needed. The authors should justify this choice or at least acknowledge the potential limitations.
Meta-Learning Approach
Equation 2:
Comment: This equation extends Equation 1 by adding context parameters ϕ. However, the paper does not provide a mathematical justification for the choice of this extension.
Weakness: The addition of context parameters ϕ increases the model complexity without a detailed explanation or justification. This can be an issue if the goal is to keep the model as simple as possible for interpretability or computational efficiency. The paper should provide a more rigorous explanation of why this specific extension is necessary and how it improves the meta-learning process, especially in the context of multimodal data. A comparison to simpler meta-learning approaches would also be valuable.
Equation 3 and 4: Meta-objective and update rule for ϕ.

Comment: The meta-objective is a standard formulation. However, the paper does not discuss the potential issues that could arise from a bi-level optimization problem, such as saddle points or local minima.
Weakness: The paper lacks a rigorous mathematical analysis of the optimization landscape, which is crucial for understanding the method's efficiency and effectiveness. The authors should include a discussion of the challenges associated with bi-level optimization and how they are addressed in their method. This could include an analysis of the convergence properties or the use of techniques to avoid poor local optima.
Approach
Multimodal Iterative Adaptation (MIA)
Equation 5 to 11: These equations describe the MIA approach.
Comment: These equations introduce an elaborate framework that involves several novel components, like State Fusion Transformers (SFTs). However, it's not clear how these equations were derived or why they are theoretically sound.
Weakness: The paper introduces several novel ideas but does not provide a theoretical justification for them. This lack of theoretical grounding makes it difficult to assess the quality and applicability of the proposed method. The authors should provide a more detailed explanation of the motivation behind the SFTs and their specific design choices, including a theoretical analysis of why this architecture is suitable for the problem.
Figures, Tables, and Diagrams
Figure 2: Schematic illustration of MIA.

Comment: While visually appealing, the figure does not offer a quantitative evaluation of the proposed method's performance.
Weakness: The lack of quantitative metrics in the figure makes it less informative. The figure should include some quantitative metrics, such as convergence rates or error reduction, to better illustrate the performance of the proposed method.
Table 1 and 2: Quantitative comparisons.

Comment: These tables provide a valuable quantitative comparison of the proposed method against baselines. However, they lack statistical tests to prove the significance of the reported results.
Weakness: The absence of statistical tests makes it difficult to determine the reliability of the proposed method compared to the baselines. The authors should include statistical significance tests, such as t-tests or ANOVA, to support their claims of superior performance.

Section 5.2: Multimodal 2D CelebA Dataset
Novelty and Comparison to Baselines: The results appear to align well with the established literature, showing better performance for multimodal methods over unimodal ones. However, the manuscript could enhance its impact by discussing why ALFA performs better than multimodal methods when sufficient support sets are present. Is this a limitation of the proposed approach or an intrinsic property of the dataset?

Ambiguity in Setup: While the section describes the use of a pre-trained model for surface normals, it lacks explicit detail on how this could affect the generalizability and transferability of the learned features. Clarification and potential ablation studies could be beneficial.

Quality of Results: The manuscript does not delve into the qualitative implications of the MSE values reported. How do these numerical metrics translate into practical improvements? For instance, do lower MSEs correlate with visibly better reconstructions in real-world applications?

Section 5.3: Multimodal Climate Data
Lack of Theoretical Justification: The paper mentions that atmospheric variables are "relatively stable" but does not provide a theoretical or empirical justification for why ALFA performs so well in this scenario.

Statistical Significance: The manuscript would be improved by including statistical tests to determine the significance of the observed differences between the proposed method and baselines.

Domain-Specific Implications: Given the critical nature of climate data, an analysis of how errors in the model's predictions could propagate into real-world applications would be valuable.

Section 5.4: Multimodal Audio-Visual AVMNIST Dataset
Insufficient Rationale for Dataset Selection: The section does not sufficiently justify the choice of the AVMNIST dataset. Given its unique challenges, why was it selected over other multimodal datasets?

Lack of Depth in Failure Analysis: It's mentioned that MTNPs fail at approximating the audio signals properly. A deeper analysis into why this failure occurs could offer valuable insights into the limitations of existing methods, thereby contextualizing the contributions of the proposed method more effectively.

Ambiguity in Methodology: The manuscript mentions that the audio signals were trimmed. However, it does not explain how this preprocessing step might affect the meta-learning process.

Section 5.5: Analysis Study
Inadequate Ablation Studies: While the section provides a valuable ablation study to understand the impact of various modules, it is relatively shallow. For instance, it would be beneficial to understand how each of these modules contributes to reducing overfitting or improving convergence speed.

Non-Uniform Metric Analysis: The section uses relative error reduction as a metric but does not justify why this is an appropriate measure of performance. It might be valuable to consider other metrics like F1-score or ROC AUC, especially when comparing across multiple modalities.

Lack of Interpretability Discussion: Given the complex architecture involving USFTs, MSFTs, and Fusion MLPs, a discussion on model interpretability would be pertinent. This is essential for real-world applications where understanding model decisions is crucial.

General Remarks
Lack of Hyperparameter Sensitivity Analysis: Across all experiments, there is no discussion on how sensitive the model is to the choice of hyperparameters. This is a critical aspect to understand the robustness of the proposed methods.

Reproducibility Concerns: The manuscript could benefit from a clearer exposition of experimental details to ensure reproducibility.

Potential for Overfitting: Given the high complexity of the model, especially with the introduction of specialized modules like USFTs and MSFTs, there might be a risk of overfitting. An analysis or discussion on this would be beneficial.

### Questions
General
Reproducibility: Could you provide a clear list of hyperparameters used in your experiments? This information is crucial for reproducibility and for understanding the sensitivity of your model to hyperparameter changes.
Section 5.2: Multimodal 2D CelebA Dataset
Role of Pre-trained Models: Could you elaborate on the role of the pre-trained model used for obtaining surface normals? How would the absence of this pre-trained model affect the results?

ALFA's Performance: Your model underperforms compared to ALFA in certain scenarios. Could you discuss whether this is a limitation of your model or an intrinsic property of the dataset?

Section 5.3: Multimodal Climate Data
Statistical Significance: Could you provide statistical tests to back the significance of the results? This would solidify the comparative performance claims.

Theoretical Justification for ALFA's Performance: You mention that ALFA performs well because climate variables are "relatively stable." Could you provide empirical or theoretical evidence to support this claim?

Section 5.4: Multimodal Audio-Visual AVMNIST Dataset
Dataset Choice Justification: Could you explain the rationale behind choosing the AVMNIST dataset for your experiments?

Failure of MTNPs: You mention that MTNPs fail to approximate the audio signals well. Could you delve deeper into the reasons for this failure?

Audio Signal Trimming: Could you explain how the trimming of audio signals might have affected the results and why this preprocessing was necessary?

Section 5.5: Analysis Study
Choice of Metrics: You use relative error reduction as a metric in your ablation studies. Could you justify why this is an appropriate metric?

Interpretability: Given the complexity of your model, how do you address the challenge of interpretability? Could you discuss any measures or future work planned to make the model's decisions interpretable?

Depth of Ablation Studies: The ablation study, while useful, seems relatively shallow. Could you comment on the potential for a more extensive ablation study to understand the impact of each module in greater depth?

Overfitting Concerns: With the high complexity of the model, how do you ensure that the model does not overfit? Could you provide any analysis or empirical evidence to support the model's robustness?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an optimization-based meta-learning framework for learning multimodal representations.

### Strengths
1. This paper proposes a meta-learning framework centered around the Multimodal Iterative Adaptation (MIA) paradigm, enhancing the capabilities of single-modal learners by learning from multimodal information.
2. Through several comparative experiments, this paper demonstrates the proposed method can improve the performance of single-modal learners.

### Weaknesses
1. Novelty:
- Previous research [1-4] has explored cross-modal relationships in multimodal data extensively. Some even utilize Transformer structures for multimodal meta-learning. 
- the paper mentions that existing methods focus on unimodal setups, but whether the information from other modalities is treated as noise or out-of-distribution data by specific-modal learners. Moreover, meta-learning itself is advantageous for few-shot learning, and there is substantial research addressing data scarcity, such as few-shot learning problems. I question the paper's research motivation and look forward to the authors' response.
[1] Vuorio, R., Sun, S. H., Hu, H., & Lim, J. J. (2019). Multimodal model-agnostic meta-learning via task-aware modulation. Advances in neural information processing systems, 32.
[2] Abdollahzadeh, M., Malekzadeh, T., & Cheung, N. M. M. (2021). Revisit multimodal meta-learning through the lens of multi-task learning. Advances in Neural Information Processing Systems, 34, 14632-14644.
[3] Vuorio, R., Sun, S. H., Hu, H., & Lim, J. J. (2018). Toward multimodal model-agnostic meta-learning. arXiv preprint arXiv:1812.07172.
[4] Sun, Y., Mai, S., & Hu, H. (2022). Learning to learn better unimodal representations via adaptive multimodal meta-learning. IEEE Transactions on Affective Computing.

2. Several conclusions in the paper lack supports, such as (i) why “slowing down convergence leads to overfitting” and (ii) claims without corresponding references, e.g., "arise in the gradient computation from a small set of observations (Zhang et al., 2019; Simon et al., 2020)." The claim about slowing convergence leading to overfitting is particularly concerning, as it is not a universally accepted principle and requires more justification. The paper needs to clarify the specific conditions under which this claim holds true within their framework.

3. The paper doesn't provide a clear explanation of how MIA guides single-modal learners' updates or the composition and structure of USFT, MSFT, etc. It's difficult to understand from Figure 2 how the "better guide the learners" with blue arrows is achieved. If the authors mean to find the optimal update direction using relationships between different modalities, did consider handle gradient conflicts between modalities? Moreover, the sequential process of multimodal fusion and subsequent meta-learning is not justified. The authors should provide an explanation. The lack of clarity regarding the specific mechanisms of the State Fusion Transformers (SFTs) makes it difficult to assess the method's effectiveness and potential limitations. The paper needs to provide a more detailed breakdown of the SFT architecture and its interaction with the single-modal learners.

4. Experimental Concerns: (i) Most of the datasets used in the experiments differ from those mentioned in the paper's motivation. The datasets use different features from a uniform data format, such as RGB images and sketches, rather than different modal features from distinct data forms, like images and text. (ii) In Table 5, the paper does not explain why MLPs were not used, especially when they achieved better results on Celeb. (iii) The claim of "facilitating rapid convergence" lacks corresponding experimental results. (iv) The proposed method introduces additional multi-modal information to compare whether the experiment is fair, (v) Is the performance improvement of the proposed method worth the extra computational effort?

### Questions
Please refer to Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
