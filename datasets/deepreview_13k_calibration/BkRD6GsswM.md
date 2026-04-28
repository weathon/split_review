# CLA-RA: COLLABORATIVE ACTIVE LEARNING AMIDST RELABELING AMBIGUITY

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Obtaining diverse and high-quality labeled data for training efficient classifiers remains a practical challenge. Crowdsourcing, which involves employing multiple weak labelers, is a popular approach to address this issue. However, crowd labelers often introduce noise, inaccuracies, and possess limited domain knowledge. In this paper, we propose a novel framework CLA-RA to optimize the labeling process by determining what to label next and assigning tasks to the most suitable annotators. Our technique aims to optimize classifier efficiency by utilizing the collective wisdom of various annotators while limiting the influence of error-prone annotations. The key contributions of our work include an annotator disagreement based instance selection mechanism which identifies the noise present in annotations of the instances and an instance-dependent annotator confidence model, which identifies the annotator with the highest confidence to correctly label an instance.These methods, combined with a similarity based annotator inference method, result in improved classifier accuracy while reducing annotation efforts. Experimental results over 13 datasets demonstrate significant improvements over state-of-the-art multi-annotator active learning methods, highlighting the effectiveness of our approach in obtaining high-quality labeled data for training classifiers with minimal labeling costs and errors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present the CLA-RA framework, an active learning approach to selecting instances to be labeled and the annotators who will label them in a crowd-source setting. The goal of this framework is to best use a annotation budget to achieve the highest accuracy for a classifier. To achieve this the framework has two main components, and instance selection process and an annotator selection process.  The authors evaluate over 13 datasets (11 of which have simulated multiple annotator labels, and two that have legitimate multiple ratings). The authors show how their active learning framework out performs other similar approaches across many of the datasets (10 out of the 13).

### Strengths
The approach taken by the authors is sensible, splitting the components of selecting an instance to be labeled and then selecting whom should do the labeling. The paper provides thorough citations.

### Weaknesses
I have concerns about the results. There are thirteen datasets, but often the authors only show eight datasets when presenting their results. It also isn't clear if the improvements are statistically significant. The authors have no description of how they simulated the multiple ratings, the make passing reference to another paper. Given the importance of this detail the authors should explain how they simulated the ratings AND reference the paper. Most of the figures have a Y-axis that DOES NOT start at 0, thus inflating their improvements. In the two non-simulated datasets the proposed framework barely surpasses past approaches. For figure five and seven the authors show no baseline. How would random selection of instances and annotators performed in this case? They hand-wave that their approach works best when raters are more error prone.

### Questions
- Why does the approach not work as well as CEAL for Mushroom and Vehicle?
- Would this approach work in high-dimension domains, thus making the similarity function more of an issue?
- The Annotator Model makes a big assumption that the majority will be correct, can this work in cases where the majority isn't correct?

### Soundness
1 poor

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the CLA-RA framework, a novel approach designed for optimized data labeling in machine learning, specifically addressing noise and inaccuracies from crowd labelers. Key innovations of CLA-RA include an 'Annotator Disagreement-Based Instance Selection Mechanism' for better noise detection, an 'Instance-Dependent Annotator Confidence Model' to streamline annotation, and the 'Annotator Inference Method' to build annotator-specific knowledge repositories based on consensus. Empirical tests across 13 datasets indicate a marked improvement in classifier accuracy with CLA-RA, underscoring its potential to enhance data labeling efficiency and quality in active machine learning.

### Strengths
To address the issue of active learning with multiple annotators, the paper proposes a suite of intricate mechanisms, including a knowledge repository, instance-related selection mechanisms, and annotator selection strategies, which are highly advantageous for the implementation of crowdsourced learning in practical settings.

### Weaknesses
The experimental section of the article appears overly concise, with the most critical deficiency being the absence of ablation studies for relevant components, which leaves unclear which step plays a pivotal role. Specifically, the contribution of the 'Annotator Disagreement-Based Instance Selection Mechanism', the 'Instance-Dependent Annotator Confidence Model', and the 'Annotator Inference Method' are not independently evaluated. This makes it difficult to ascertain the necessity of each component and their individual impact on the overall performance. Additionally, the section lacks essential parameter analyses, such as those for the exploration threshold \epsilon, the confidence threshold \eta, and others, which are crucial for understanding the robustness and generalizability of the proposed approach. The absence of these analyses makes it difficult to determine the sensitivity of the method to different parameter settings and limits the practical applicability of the framework. Furthermore, the experimental setup does not include comparisons against strong baselines that utilize similar active learning strategies with multiple annotators, which would provide a more robust evaluation of the proposed method's effectiveness.

### Questions
Q1: The authors claim in the experimental section that Figures 6 and 5 demonstrate the efficiency of their example selection strategy for labeling and re-labeling; however, no comparative analysis is presented within these figures. In my opinion, a comparison with alternative selection strategies, such as random annotator selection, should be included. The efficacy of the sample selection strategy would be more convincingly demonstrated if the same level of accuracy could be achieved with fewer queries.

Q2: In the method proposed by the article, a weighted majority scheme is employed to compute the confidence among different annotators. Numerous extant methods exist to calculate confidence, such as utilizing the L1 norm of predictions. My question concerns the decision to employ the weighted majority algorithm—a relatively conventional approach—over more recent methodologies. What was the rationale behind this choice?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a framework CLA-RA to solve the problems of active learning strategy in crowdsourcing. The proposed method consists of an instance selection approach, an annotator confidence model, and an inference model. The proposed method compares with several baselines on 13 datasets. A comprehensive insight into each component is also applied.

### Strengths
1. The proposed method is technically sound.
2. The framework is clear and easy to follow.
3. The comprehensive insights for each component of the proposed method are interesting.

### Weaknesses
1. Notations are not defined clearly. Also, the usage of notations is really confusing. This is the most important thing that hinders understanding. Here are some examples. The notations for features of an instance are very similar to the notation of the instance itself. And, the last $x$ in the first paragraph of Section 3.1 is misused; The condition in the second paragraph of Section 3.5 is ambiguous. An indicator (j) cannot be equal to a vector (z). Specifically, the lack of clear distinction between an instance $x$ and its feature representation, often also denoted as $x$ or $x_i$, makes it difficult to follow the mathematical formulations. The use of $x$ in section 3.1 where it appears to be an index rather than an instance is also a major source of confusion. The condition in section 3.5 where an index $j$ is compared to a vector $z$ is mathematically incorrect, suggesting a lack of rigor in the formalization.
2. The selection of the datasets is not very reasonable. The characteristics of all datasets are not clear. This is my main concern about the effectiveness of the experiment. Detailed traits of each dataset should be exhibited. The number of annotators is too small. This condition is really beneficial to the proposed method which drops the convincing of the experiment. The paper does not provide sufficient detail on the datasets used, making it hard to assess the generalizability of the results. The lack of information about the class distributions, feature types, and the number of instances in each dataset makes it difficult to understand the experimental setup. The use of a small number of annotators, which may not reflect real-world scenarios, is a critical limitation that could artificially inflate the performance of the proposed method, especially since the method relies on modeling annotator behavior.
3. Hyper-parameters are too much. The experiment part lacks an explanation for the specific values of these hyper-parameters. Due to the core component being the annotator model, a well-work $ f_{\theta} $ is really important to the proposed method. However, there is no mechanism to guarantee the training result of that $ f_{\theta} $ is ‘good’. The paper introduces several hyper-parameters without providing a clear rationale for their specific values. The absence of a principled approach to hyper-parameter selection, such as a validation set or cross-validation, raises concerns about the robustness of the results. The reliance on the annotator model $f_{\theta}$ without any mechanism to ensure its quality is a significant weakness. The paper does not address the potential for the annotator model to converge to a suboptimal solution, especially given the limited training data and the potential for bias in annotator responses.

### Questions
1. How were the hyper-parameters, i.e. ratio of training data, annotation budget, exploration threshold, confidence threshold, and similarity threshold, selected in the experiment? 
2. How about the time complexity of the proposed method compared with other methods? When the number of workers becomes greater, due to the training phase, the proposed method will 
3. How to guarantee that the annotator model works well? If the training data is unbalanced or responses from annotators have great bias, the annotator model will fail. Also, too small a quantity of training datasets cannot overcome the random prediction brought by the random initialization of the neural network.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a new scheme for active learning based (re-)labeling of ML datasets that leads to improved classification accuracy of the classifiers resulting from training on the (re-)labeled datasets. The key idea of the paper is to combine crowd-sourced annotation from annotators who are not necessarily experts and thus potentially unreliable (at least to some extent) with confidence estimations for individual annotators — combined these two ideas evidently lead to substantially improved classifiers, as evaluated on a range of standard UCI ML datasets.

### Strengths
This is a very solid paper that makes an important contribution to the active learning community. I applaud the authors for a clear, technically sound presentation of a clever idea that evidently (as shown by the experimental evaluation) leads to improvements in classification accuracy for classifiers that are trained through active learning. While the related work part is a bit short, it covers relevant concepts and previous work in the field. The technical approach is nice: combining crowdsourcing with active learning, thereby taking into account that crowd annotators are not necessarily experts and then turning this around by assigning assumed confidence values to individual annotators through the majority voting on multiply labels samples and looking at consistency amongst individual annotators and their performance (with regard to the majority votes) is clever. Combining this with the budget constraint that is often used in active learning scenarios evidently leads to an effective active learning scheme. The experimental evaluation is solid. The authors did a good job in experimenting over a range of datasets (even though some more details on these should have been given, e.g., in an appendix, to make the paper more comprehensive). As usual in the field, alas, no statistical significance analysis has been performed — yet the numerical gains are large enough such that this reviewer (who has experience with those datasets) believes that the gains actually are significant (see weaknesses and questions). The presentation of the approach is solid and the paper is easy to follow.

### Weaknesses
There are a few issues with the paper that should be considered: Extend the related work a bit (there should be space); add an actual statistical significance analysis; justify why accuracy is used as evaluation measure (and not macro F1 as it would be more appropriate for at least some of the rather imbalanced datasets; add an appendix where more details are given, e.g., on the datasets and on the classification pipeline.

My biggest concerns with this paper, however, are scope and potential impact. ICLR is, as per its own definition, a venue that focuses on representation learning / deep learning. This paper is essentially a core machine learning paper, yet it does not actually cover representation learning nor deep learning. As such, I see this paper in its current form slightly out of scope for ICLR. The second concern (impact) comes from the fact that active learning has been around for quite a while (even including the crowd sourcing component as identified by the authors), and the field is somewhat saturated. The presented approach is clever and effective for a range of standard classification tasks but I wonder whether this would actually be of substantial enough interest for the ICLR audience. If the authors would link their work closer to recent applications / problems in the deep learning / representation learning field it probably would gain more attention / impact.

### Questions
See my comments above with suggestions / questions that could be addressed in an appendix etc.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair
