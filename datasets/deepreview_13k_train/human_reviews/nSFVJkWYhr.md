# AutoCATE: End-to-End, Automated Treatment Effect Estimation

- Decision: Reject
- Scores: 3, 8, 8, 5, 1

## Abstract
Accurate estimation of heterogeneous treatment effects is critical in domains such as healthcare, economics, and education. While machine learning (ML) has led to significant advances in estimating conditional average treatment effects (CATE), real-world adoption of these methods remains limited due to the complexity of implementing, tuning, and validating them. To this end, we advocate for a more holistic view on the development of ML pipelines for CATE estimation through automated, end-to-end protocols. We formalize the search for an optimal pipeline as a counterfactual Combined Algorithm Selection and Hyperparameter optimization (CASH) problem. We introduce \texttt{AutoCATE}, the first automated solution tailored for CATE estimation that addresses this problem based on protocols for evaluation, estimation, and ensembling. Our experiments show how AutoCATE allows for comparing different protocols, with the final configuration outperforming common strategies. We provide AutoCATE as an open-source software package to help practitioners and researchers develop ML pipelines for CATE estimation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an end-to-end pipeline for CATE estimations and conducts a comprehensive comparison with existing methods.

### Strengths
I think the paper has comprehensive experiments and reproducible code.

### Weaknesses
Novelty and significance of the paper:
The methods in each stage of the autoCATE pipeline are not new and the pipeline itself is not novel either. The paper does conduct a comprehensive experiments, but again most of the similar comparisons are already covered in the existing papers. The author claims the stacking is novel, but from my knowledge, it has been proposed by multiple authors. Using proxy outcome to do model selection is not novel either.

Writing: 
I think the paper lacks a lot of the details, for example, what exactly is the novel stacking algorithm, what is the definition of AllMeta and what meta learners are included in this 'allmeta' definition. The value of the paper comes from the experiments and without very specific details it is hard to evaluate the quality.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a pipeline for automating the several design choices required for CATE estimation; from preprocessing datasets to different risk measures for model selection. The pipeline is divided into three stages corresponding to the following three questions; what risk measure should be used for model selection, what CATE estimators should be trained, and finally how should be select over the trained CATE estimators and combine them for better generalization. The authors conduct experiments on widely used benchmarks and present interesting insights regarding the numerous design choices in CATE estimation.

### Strengths
- The authors have done a really good job at covering nearly all the design choices involved in CATE estimation. Specifically, analyzing the role of preprocessing datasets and dataset splits for training/evaluation has not been done in prior works. Further, the authors experiment with novel strategies for model selection with multiple risk measures and ensembling of CATE estimators.

- The scale of the empirical study is quite comprehensive; experiments involve a variety of meta-learners, base-learners, and risk measures. This makes their findings interesting and significant for practitioners and future work, and their software package should also make it easy for practitioners to adopt the proposed pipeline.

- The paper overall is well written and organized which makes it easy to follow and understand main results. The experiment results are clearly presented with good discussion around them. I especially like their comparisons with the findings from prior benchmarking studies for CATE model selection.

### Weaknesses
 - I have concerns regarding the lack details for some key aspects of their empirical study. For experiment regarding risk measures in Section 5.2, how were the nuisance models associated with the risk measures selected? Also, what is the underlying set of trained CATE estimators over which authors are performing model selection via different risk measure? The caption inTable 1 state "Results for 50 evaluation trials and 50 estimation trials with a T -Learner and gradient boosting". Does this imply that model selection was done over only T Learners? That would be a serious issue as we want to select over a diverse set of CATE estimators to benchmark the different risk measures. For example, due to the congeniality bias (Curth & van der Schaar (2023), if the CATE estimators only involve T Learners, then T risk should do better than other risk measures. I would like the authors to clarify this point and provide clear details regarding this in the paper. The same issue is repeated with ensembling experiment in section 5.4, as the caption in Table 3 suggests the CATE estimators trained were only T Learners. 

 - Regarding experiment in section 5.5, the authors should follow the procedure of AutoML to tune S/T Learner (Mahajan et al. 20023) instead of manual grid search. This would ensure stronger baselines and a fair comparison with them. Similarly, the authors can construct meta-learners with nuisance model trained via AutoML (Mahajan et al. 20023), and that could serve an alternative set of CATE estimators for experiment in section 5.3 (Estimation) as well. For example, the BestBase estimator currently involves a manual search over a grid of different algorithms and hyperparameters, but this could be automated via AutoML.

 - I am not sure what are the main conclusions from the experiments with combined risk measures? The authors did not experiment with many combinations, and only considered combining T & DR risk and different T risk. So the experiments are not exhaustive which makes it hard to interpret what the main trend should be and what recommendations can be made. Similar comment for ensembling with multiple risk measures; I think the strategy of combining risk measures is the most novel aspect of the work, so analyzing it in depth would make the paper strong.

 - The experiments with ensembling in section 5.4 are good but they are missing the ensembling strategy of using softmax based on risk measures from Mahajan et al. 2023. I would recommend to have some discussion around the potential advantages/disadvantages of their proposed ensembling strategy over the softmax risk measure based ensembling. I understand experimenting with every possible ensembling strategy is not feasible by the rebuttal period, but I would encourage the authors to include it in their package for later. 

 - Finally, I find the counterfactual Combined Algorithm Selection and Hyperparameter optimization (CASH) formulation a bit misleading. The problem studied by the authors is essentially model selection for CATE estimation, as stated in prior works (Schuler et al. 2018,  Curth & van der Schaar (2023), Mahajan et al. 2023). I am not sure why the authors want to reformulate this? It makes the connection with the prior works weaker as it seems to give an impression that the authors are solving a different (and novel) problem.

### Questions
- How are the multiple risk measures combined? Do we take the average of risk measures, like average of T and DR risk in the experiments?

- How do the authors obtain the best meta-learner or best base-learner? Is it based on how well they fit the observational data? 

Minor comments

- In lines 109-110 authors state that prior works haven't explored AutoML for CATE estimation. This should be changed to account for the work by Mahajan et al. 2023, as acknowledged by the authors themselves ahead in line 144

- In line 258, the authors state that there are no prior works for ensembling CATE estimators, but they have acknowledged the work by Mahajan et al. in line 123 for ensemble selection. Please update the text to make it more consistent. 

- It will be good to add equations to explain the proposed ensembling strategy in section 4.3

- It would be nice to have statistics regarding the scale of the empirical study before section 5; like how many risk measures, how many meta-learners and base-learners for estimation, how many estimators are included for the model selection study, etc.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a software development framework: AutoCATE, which aims at automating the estimation of Conditional Average Treatment Effects (CATE) for real-world applications. It addresses the unique challenges in CATE estimation: the absence of ground truth for counterfactuals and the complexity of causal ML pipelines, by formalizing the pipeline search as a counterfactual Combined Algorithm Selection and Hyperparameter (CASH) optimization problem.

### Strengths
**Originality**: The paper proposes an innovative approach to address the specific complexities of CATE estimation with an automated solution tailored for non-expert practitioners. By implementing a counterfactual CASH optimization, it well addresses the gaps in the CATE literature.

**Quality**: The paper is well-structured, from its technical details to empirical evaluations. The effects of the proposed AutoCATE have been well-demonstrated through extensive comparisons with existing CATE estimation methods, supporting the validity of their claims.

**Clarity**: The overall writing of the paper is clear and easy to follow. Regarding its technical details, the problem formulation and the proposed three-stage solution are well-explained, making complex concepts easy to understand. The figures (e.g., pipeline flow and risk comparisons) and tables add clarity, effectively supporting the text.

**Significance**: AutoCATE is highly relevant for domains requiring accurate causal inference, as it democratizes access to CATE estimation methods by reducing the technical expertise needed. This can drive real-world adoption of CATE estimation in fields like healthcare, where accurate treatment effect estimation has significant implications.

### Weaknesses
 **Computation Complexity**: This is my major concern. How long would it take for AutoCATE to find an optimal ML pipeline given a dataset (e.g. the smallest and the biggest datasets you used in your experiments)? How would the size of the dataset impact the time of finding the optimal ML pipeline?

**Algorithm Coverage**: From the demonstration of the framework, only basic ML algorithms are covered in your software. I wonder are there more sophisticated ML algorithms that can be used for CATE estimation? If yes and if these algorithms are integrated into the entire framework, how will it impact the computation complexity?

### Questions
Please refer to weakness.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper develops an automated, end-to-end protocols for CATE estimation. It applies the techniques in AutoML to addresses complexities in real-world CATE estimation task by automating the process across evaluation, estimation, and ensembling stages. The authors use the experiments to compare the automated strategies in AutoCATE and benchmarking its performance with alternatives.

### Strengths
1. This paper presents an automated solution for CATE estimation, effectively consolidating various established methods into a single framework.
2. The AutoCATE code is simple, user-friendly, and accessible to practitioners with limited machine learning expertise.
3. The paper provides a comprehensive analysis of existing CATE methods, supported by extensive experimentation.

### Weaknesses
1. The contribution of AutoCATE could be more clearly communicated, possibly due to the writing style. For example:

     --Table 9 compares AutoCATE with alternative CATE estimation packages, highlighting similarities in functionality with EconML. The authors claim that AutoCATE provides "automated, end-to-end optimization," which EconML does not. This distinction could be elaborated more clearly in the main text, and Table 9 should be moved to the main sections to clarify AutoCATE's contribution.

     -- In lines 80-81, the authors state that their approach "addresses key aspects often overlooked in CATE estimation, such as preprocessing, feature selection, or ensembling." However, it’s not evident how these three aspects contribute to AutoCATE's performance throughout the paper. Explicitly demonstrating the impact of these components on performance would strengthen the narrative. For instance, the paper does not show a clear ablation study demonstrating the impact of feature selection or ensembling, making it difficult to assess their individual contributions.

2. The advantages of AutoCATE over existing methods are unclear. Benchmarking AutoCATE against common alternatives should be one of the central experiments, yet:

      -- Only two learners (S- and T-learners) are included. The table 8 presents results for additional benchmarks. I suggest including additional learners from Section B.1 (such as the DR-learner and R-learner). Also, due to similarity between AutoCATE and EconML, including the benchmarking between them may also be helpful. The current benchmarks do not provide a comprehensive comparison against state-of-the-art methods.

      -- The reason for AutoCATE's superior performance over these learners is not well-explained. I suggest providing a detailed explanation for why AutoCATE outperforms the S- and T-learner. It is unclear whether the performance gain is due to a better search strategy, a more comprehensive search space, or other factors.

3. To me, the main contribution of this paper is the development of a new package that facilitates benchmarking and selection of the best pipeline from existing CATE estimation methods, offering useful choices for users. However, similar benchmarking work was previously conducted by Curth & van der Schaar (2023), and this framework, while practical, does not introduce new algorithmic innovations or significantly advance CATE estimation methods to the level typically expected for ICLR. The paper does not adequately address why a practitioner could not simply use a package like EconML to run different models independently and select the best one, which raises questions about the necessity of the proposed framework.

### Questions
What does the number of evaluation and estimation trials mean? This is not clear to me while reading the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Accurate estimation of heterogeneous treatment effects is critical in domains such as healthcare, economics, and education. Real-world adoption of these methods in estimating conditional average treatment effects (CATE) remains limited due to the complexity of implementation, tuning, and validation. To address the challenges, the authors aim to develop ML pipelines for CATE estimation through automated, end-to-end protocols. The authors introduce a model termed AutoCATE, which is designed to find automated solutions tailored for CATE estimation based on protocols for evaluation, estimation, and ensembling. The automated solution is obtained after formalizing the potential problem as a counterfactual Combined Algorithm Selection and Hyperparameter optimization (CASH) problem. The authors also undergo comprehensive experiments and demonstrate that the results obtained by the proposed model outperform the results obtained by other common strategies.

### Strengths
As pointed out by the authors, this paper proposes a practical and comprehensive solution as the automated, end-to-end construction and validation of ML pipelines for CATE estimation.

### Weaknesses
It seems that the paper is simply a user manual for AutoCATE in Python. The authors do not provide any new models/methodologies to estimate CATE. All the methods in the paper are presented in previous papers. One can simply follow the algorithms given in existing literature and replicate the result. Typically, the paper does not contribute much to the related society.

Another clear drawback is poor writing. Many notational mistakes appear in the appendix. For example, see line 855. Furthermore, authors only outline the general procedure without providing a detailed description/explanation, which causes much confusion among readers. For instance, the authors state that, in the evaluation stage, the proposed model would combine different measures to make the evaluation more robust (see line 212).  Nevertheless, the authors do not explain how to combine different measures. The combination may simply concatenate different measures to form a vector or add all the measures together. Statements with unclear descriptions and explanations reduce the readability of the paper.

Confused notations: It is strange that minimization is taken over on $a$ and $h$, but the loss function does not contain $a$ and $h$. It is hard for readers to understand at the first glance. Should it be better to introduce a new notational system such that readers can understand directly? See other notations errors in Appendix B (X-learner), $f_x^1$ is not given, or it should be $f_X^1$.

Honestly, we can run different models independently and choose the best. What is the difference between applying the proposed model and choosing the best after running models independently? Please provide justifications. According to the replies, I also concerned if authors include ALL the methods of computing CATE. Missing any one method can make the result/conclusion unreliable.

I am still concerned with the contributions of this work since this is mainly a proof of concept paper, therefore I will keep my score.

### Questions
No technical questions. Please see the weakness above.

### Soundness
2

### Presentation
1

### Contribution
1
