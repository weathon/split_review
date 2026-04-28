# Task-Oriented Multi-View Representation Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6, 3, 5

## Abstract
Multi-view representation learning aims to learn a high-quality unified representation for an entity from its multiple observable views to facilitate the performance of downstream tasks. A typical multi-view representation learning framework consists of four main components: View-specific encoding, Single-view learning (SVL), Multi-view learning (MVL), and Fusion. Recent studies achieve promising performance by carefully designing SVL and MVL constraints, but almost all of them ignore the basic fact that \textit{effective representations are different for different tasks, even for the same entity}. To bridge this gap, this work proposes a \textbf{T}ask-\textbf{O}riented \textbf{M}ulti-\textbf{V}iew \textbf{R}epresentation \textbf{L}earning (TOMRL) method, where the key idea is to modulate features in the View-specific encoding and Fusion modules according to the task guidance. To this end, we first design a gradient-based embedding strategy to flexibly represent multi-view tasks. After that, a meta-learner is trained to map the task embedding into a set of view-specific parameters and a view-shared parameter for modulation in the Encoding and Fusion modules, respectively. This whole process is formalized as a nested optimization problem and ultimately solved by a bi-level optimization scheme. Extensive experiments on four multi-view datasets validate that our TOMRL consistently improves the performance of most existing multi-view representation learning approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a task-oriented multi-view representation learning method. Specifically, it adopts the meta-learning paradigm to minimize the distribution differences in representations across various tasks. However, the overall technical soundness of this paper appears to be lacking, and the experimental evidence presented is not sufficiently convincing.

### Strengths
1. For multi-view representation learning, different tasks have distinct requirements for the distribution of representations. This paper highlights this issue.

2. The proposed method integrates meta-learning and multi-view learning through a nested bi-level optimization approach.

### Weaknesses
1. For ‘representations from multiple views can better serve the task’ in the contribution 1. In fact, it explores the relationship amongst various tasks, from the perspective of multi-task learning, which is not enough as an innovation point. The core idea of leveraging task relationships to modulate feature extraction and fusion, while beneficial, does not fundamentally depart from existing multi-task learning paradigms. The novelty is incremental rather than transformative, particularly when considering the extensive literature on multi-task learning with shared or task-specific parameters.

2. In the section 3, the authors mentioned that the fusion process of features may also be inconsistent. The proposed method focuses on Fusion modules, how does the author align the features of similar instances in different tasks? Specifically, if the fusion process is inconsistent, it implies that the same instance might have different fused representations across tasks. The paper does not adequately address how these potentially disparate representations are handled to ensure consistent learning, particularly when the task embeddings are used to modulate the fusion process.

3. The authors should discuss the insight of this paper with the lifelong multi-view learning or multi-view multi-task learning. The absence of a discussion regarding the connection to lifelong learning is a significant oversight. Specifically, how does this method handle the introduction of new tasks over time without catastrophic forgetting, and how does it compare to existing lifelong learning methods in a multi-view context?

4.  In term of the loss function, the author does not introduce the concept of weight. For multiple tasks, the data distribution and importance of different tasks are different. How does the author solve this problem? The lack of task-specific weighting in the loss function is a major concern. Different tasks may have varying levels of importance or data quality, and treating them equally during training can lead to suboptimal performance. The paper fails to address how the method accounts for these differences, potentially leading to a bias toward tasks with larger datasets or more easily learned patterns.

5. The current manuscript need to be carefully polished, such as, in the section 2, 〖R〗^(d_H ) not R_(d_H ), in table 2, line 4, the font thickness should be consistent； the notations in equation (1)

### Questions
1. Due to the limited sample size in the dataset, avoiding overfitting poses a central challenge in few-shot learning. However, the paper lacks an in-depth discussion on this issue and does not introduce method-level strategies to alleviate the problem.

2. The authors should consider validating their method on the dataset with a significantly larger domain difference.

3. The introduction of multi-view seems to be optional. Additionally, there is no information exchange between the multi-view sub-networks.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a multi-view representation learning method, where the key idea is to modulate features in the View-specific encoding and Fusion modules according to the task guidance. The authors design a gradient-based embedding strategy to represent multi-view tasks. In addition, a meta-learner is trained to map the task embedding into a set of view-specific parameters and a view-shared parameter. This whole process is formalized as a nested optimization problem and ultimately solved by a bi-level optimization scheme.

### Strengths
1. The paper proposes a task-oriented multi-view representation Learning method from a meta-learning perspective. The performance of classification and clustering tasks is improved significantly.
2. The proposed method defines an unsupervised multi-view task in an episode fashion, and designs a meta-learner for modulating the view-specific features and unified entity representations with the task guidance.
3. The proposed method models meta-learning and multi-view learning as a nested bi-level optimization.

### Weaknesses
1. Why two modulation processes are useful in this task was unclear.  Also, the benefit of the TOMRL on different dataset domain is also not discussed or analyzed in the paper. I think the paper should at least study at least one scenario , e.g., NoisyFashion to Caltech 101-7, to verify the effectiveness of TMORL as this is considered as one of the main contribution of the paper. It shall also be helpful to analyze why TOMRL is helpful in learning a high-quality unified representation, perhaps from the perspective of gradient analysis.

2. The display of experimental results in this paper is not uniform. For example, bold results in some tables indicate the best results, while others denote the results of TOMRL. Please unify the form in the full text. Alternatively, give clear comments in each table title.

### Questions
Please check the comments above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a gradient-based embedding strategy to flexibly represent multi-view tasks. The authors propose a meta-learning-based solution and learns task-oriented multi-view representations, where meta-learning and multi-view learning are ultimately formalized as a nested optimization problem and solved via a bi-level optimization paradigm.

### Strengths
1. Results on four datasets are presented on multi-view tasks.
2. Empirical study shows that the method consistently improves the performance of downstream tasks for both few-shot and routine tasks.

### Weaknesses
1.	The motivation is not clear. For example, there are many methods could learn task-oriented representation and multi-view representation, however, the authors only provide some examples which are not applicable for out-of-sample data or only learning the uniform representation for entities. It is not convincible. 

2.	“A typical multi-view representation learning framework consists of four main components: View-specific encoding, Single-view learning (SVL), Multi-view learning (MVL), and Fusion.”  It is a very strong claim or assumption. The authors should provide a comprehensive study and moreover a formulation to unify these models is necessary. 

3.	“how representations from multiple views can better serve the task” I think this is a very natural requirement in many models. So, I do not find any necessity or novelty for this claim. 

4.	The writing and organization are not clear. It is difficult to understand the motivation and why the proposed model is good.

### Questions
Regarding the cross task experiment in Table 3, the proposed TOMRL brings a decrease in NMI indicators of NoisyFashion to EdgeFashion. With the significant growth MORL has brought under other conditions, why did this particular decline occur?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a model to learn task-oriented multi-view representation. Based on the observation that almost all of current models ignore the basic fact that effective representations are different for different tasks, even for the same entity, they propose a Task-Oriented Multi-View Representation Learning (TOMRL) method.

### Strengths
Learning task-oriented multiview representation is important.

### Weaknesses
1. The paper artificially defines downstream tasks for multi-view representation learning, but typically representation learning aims to acquire a general representation that can be fine-tuned for different specific tasks. Is it unfair to directly consider downstream tasks in the representation learning, and can the representations learned in this paper still perform well for new tasks that are not considered in the paper?

2. The paper is not very clear in explaining how the meta-learning paradigm generates task-specific biases and whether it can explain why using task bias generated by the meta-learning paradigm can improve the model's performance.

3. The experimental evaluations are not comprehensive enough in several aspects. The dataset used in this paper is not sufficiently diverse. For example, commonly used datasets in this field, such as NoisyMNIST, EdgeMNIST, Caltech20, and PatchedMNIST, were not tested. Additionally, the paper only integrates the method into three approaches, all from the same source paper. It is hoped that the authors can validate their method by integrating it into a wider range of methods to enhance its credibility.

### Questions
The claim that there are four components is questionable, so the authors should provide more clear and strict evidence or analysis. 

There are no theoretical results.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper argues that the semantic features required for different tasks may vary when using the same representation. Therefore, it proposes a task-oriented multi-view representation learning method. The paper adopts a meta-learning paradigm, defines multi-view tasks, and retains both task-specific information for each view and unified information across views. Additionally, it introduces task bias for different tasks. This method can be integrated into existing multi-view representation learning methods and has shown performance improvements.

### Strengths
1. The motivation and idea presented in this paper are reasonable. The introduction of the paper effectively highlights that multi-view representations should focus on both the unified representation and the unique information of each view, and should adapt to different representations for different tasks.

2. This paper leverages a meta-learning paradigm to generate task bias and integrates it into existing multi-view representation learning methods, resulting in performance improvements.

### Weaknesses
1. The paper artificially defines downstream tasks for multi-view representation learning, but typically representation learning aims to acquire a general representation that can be fine-tuned for different specific tasks. Is it unfair to directly consider downstream tasks in the representation learning, and can the representations learned in this paper still perform well for new tasks that are not considered in the paper?

2. The paper is not very clear in explaining how the meta-learning paradigm generates task-specific biases and whether it can explain why using task bias generated by the meta-learning paradigm can improve the model's performance.

3. The experimental evaluations are not comprehensive enough in several aspects. The dataset used in this paper is not sufficiently diverse. For example, commonly used datasets in this field, such as NoisyMNIST, EdgeMNIST, Caltech20, and PatchedMNIST, were not tested. Additionally, the paper only integrates the method into three approaches, all from the same source paper. It is hoped that the authors can validate their method by integrating it into a wider range of methods to enhance its credibility.

### Questions
For major concerns including the problem/experimental setting, unclear description, and experimental evaluation, please see weaknesses for details.

There appears to be a minor error in the pseudocode. Should line 20 be placed after line 21?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
