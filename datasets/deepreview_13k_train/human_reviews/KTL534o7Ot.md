# Programmable Synthetic Data Generation

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Large amounts of tabular data remain underutilized due to privacy, data quality, and data sharing limitations. While generating synthetic data resembling the original distribution addresses some of these issues, most applications would benefit from additional customization on the generated data. However, existing synthetic data generation approaches are limited to particular constraints, e.g., differential privacy (DP) or fairness. In this work, we introduce ProgSyn, the first programmable and flexible synthetic tabular data generation framework. Customization is achieved via programmatically declared statistical and logical expressions, supporting a wide range of requirements (e.g., DP or fairness, among others). To ensure high synthetic data quality in the presence of custom specifications, ProgSyn pre-trains a generative model on the original dataset and fine-tunes it on a differentiable loss automatically derived from the provided specifications using novel relaxations. We conduct an extensive experimental evaluation of ProgSyn over four datasets and on numerous custom specifications, where we outperform state-of-the-art specialized approaches on several tasks, while being more general. For instance, at the same fairness level we achieve 2.3% higher downstream accuracy than the state-of-the-art in fair synthetic data generation on the Adult dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors tackle the interesting problem of adding constraints to the synthetic data generation. They provide a framework where they consider both statistical and logical constraints arising from privacy, fairness and the domain. Experiments are conducted on real-datasets to showcase the benefits of their approach.

### Strengths
Overall:

The paper is well-written and easy to digest. The approach is simple and the experiments are convincing but the novelty factor is a bit missing. 

Pros:

(a) The problem setup is very timely and relevant to the literature and the community. The framework solves a real issue of generating high-quality synthetic data with constraints.
(b) The experiments are extensive and showcase the framework in a wide variety of constraints while contrasting with the current state of the art approaches.

### Weaknesses
Cons:

(i) The main approach of fine tuning and adding differentiable constraints is relatively straightforward. 
(ii) The approach is not adaptive to changing the constraint set and is not even discussed in the paper.

### Questions
1. How would you generate a variety of synthetic datasets with varying constraint specifications without retuning your model?


* On the Constrained Time-Series Generation Problem  https://openreview.net/forum?id=KTZttLZekHa

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article introduces the ProgSyn framework, which is the first framework designed for programmable table data generation.  The overall architecture of this framework is based on a two-stage process, starting with pre-training of the generated model using sampling and decoder structures, and then fine-tuning specific downstream tasks and adapting to their requirements.  At the same time, in the process of concrete implementation, ProgSyn uses the relaxed version of differential privacy, descriptive requirements and specification to achieve the programmability of the whole process.  The structure of this paper is reasonable and the content is clear, which provides a good model for the research of controlled table data generation.  In subsequent experiments and appendices, the authors also intelligently present their contributions and ideas by using selected datasets.

### Strengths
1.	The paper maintains a clear and focused main theme, presenting novel research in the realm of programmable generation for table data. The proposed ProgSyn framework, utilizing a pretraining and fine-tuning architecture, effectively caters to the requirements of downstream tasks in practical scenarios.
2.	In terms of methodology, the authors employ three approaches: differential privacy constraints, logical constraints, and statistical formulations. These strategies support the programmable nature of ProgSyn and demonstrate careful consideration for its differentiability, thereby enhancing its practical implement ability.
3.	Within this paper, the proposed differential computation for binary masks addresses the challenge of non-differentiable hard logical constraints and counts. This method provides an effective means for controlling the content generated by the model during the generation process.
4.	The supporting materials provided in this paper exhibit well code writing standardization and good applicability. The code content aligns well with the paper's core ideas, making it an excellent resource for readers seeking a deeper understanding of the author's concepts.

### Weaknesses
1.	Theoretical Framework: Although the research area explored in this paper holds promise for further investigation, the technical aspects in the paper appear somewhat dated, primarily covering foundational theories and methods. Considering the goal of ProgSyn is to generate sufficiently realistic simulated data with privacy protection properties, the authenticity aspect is addressed mainly in terms of experimental accuracy (given that XGBoost is a robust classifier), without validating its reliability from a statistical hypothesis testing perspective. This arrangement may lead to a somewhat one-sided argument in the paper. Specifically, the paper lacks a rigorous statistical analysis of the generated data's distribution compared to the original data, relying primarily on downstream task performance as a proxy for data quality. This approach overlooks potential discrepancies in higher-order statistical properties that might not be captured by a classifier. Furthermore, while differential privacy is mentioned, the paper does not delve deeply into the implications of the chosen privacy parameters on the utility of the generated data, nor does it offer a detailed analysis of the trade-off between privacy and accuracy in the context of complex tabular data.
2.	Writing Clarity: The content in the paper's introduction appears somewhat disorganized, as it combines background introduction with an overview of the framework's methodology. It is recommended to organize the sections logically as "introduction," "related work," and "formulation" to help readers better understand the core content of the paper. Additionally, there are instances of non-standard writing in the paper, such as lengthy formulas (page 6), pseudocode (page 5), page breaks (page 15, 20, 25), and inconsistencies in paper formatting (page 10-12). Also, it's important to address the improper use of color in tables.
3.	Code: To facilitate the research framework's wider adoption, it's advisable to update the code version requirements. Personally, I encountered issues with running the code on an NVIDIA GeForce RTX 4090 with CUDA capability sm_89, and it would be beneficial to address compatibility concerns to ensure broader accessibility and usability. The absence of clear instructions for environment setup and dependency management further complicates the process of reproducing the results.

### Questions
Regarding this study's research, I have the following queries:
1.	Typically, table data is more widespread and common than image data. Does the controllable generation method proposed in this paper aim to fill the missing distributions in real data, as opposed to directly applying conditional filtering within the table? Because it is cheaper to filter tabular data through simple rules than to generate data compared to other data structures.
2.	In the field of image generation, we can rely on our own visual judgment or specific discriminators or metrics, such as FID, for authenticity assessment. Apart from the loss function control methods mentioned in this paper, are there more reliable approaches for verifying the authenticity of the generated data?
3.	In practical scenarios involving table data, recommendation systems present a more realistic application. Since relying solely on a highly generalizable model like XGBoost might not provide strong model performance validation, can ProgSyn consider further methodological validation (e.g., using models from other domains like ONN, xDeepFM, or more general models like SVM, GBDT)?
4.	In the main text, I didn't come across rigorous proofs related to statistical control of table data generation. Could you provide some information on the formulation process for statistical control? This would greatly assist readers in understanding controllable generation.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a tabular data generation method called ProgSyn where one can vary fairness, privacy, and logical constraints. The three constraints are relaxed into differentiable loss terms and used to fine tune a generative model. Experiments show that it is possible to generate synthetic data that satisfies compound constraints while maintaining high downstream accuracy.

### Strengths
* This is a timely work that addresses the important problem of configurable tabular data generation satisfying multiple constraints.
* The presentation is straightforward to understand.
* Experiments show promising results on generating data satisfying multiple constraints.

### Weaknesses
 * The support for fairness seems limited. There are many fairness definitions in the literature beyond demographic parity including equalized odds, equal opportunity, predictive parity, equal error rates, individual fairness, and causal fairness, which seem to be ignored here. The proposed work would be much more interesting if it could also be configured for the other fairness measures as well. Supporting demographic parity only gives the impression that only the easiest fairness measure is supported, and there is no discussion on how to possibly extend the framework to other measures either.

* Emphasizing the programmability of ProgSyn sounds a bit exaggerated. For example, Figure 3 looks like a conventional config file instead of say a Python program. When using DP, a user always specify epsilon and delta, but this is not called programming.

* It is not clear why DP should be optimized together with fairness holistically. Why not generate a fair dataset using an existing technique or a fairness-only version of ProgSyn and then add random noise to satisfy DP? This two-step approach should be a baseline and compared with ProgSyn empirically.

* It would be more interesting to see the limitations of this method where the accuracy actually has to drop in order to satisfy various constraints. The current experiments only show success cases, but fairness and privacy are not necessary aligning, so there has to be a point where the accuracy cannot be maintained. In Table 3, there is almost no reduction of accuracy after applying DP, which suggests that the proposed method may have not been stressed tested enough. Hence, there should be more extensive experiments showing what happens in truly challenging scenarios.

### Questions
Please address the weak points.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
