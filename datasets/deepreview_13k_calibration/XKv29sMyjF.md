# Query-based Knowledge Transfer for Heterogeneous Learning Environments

- Decision: Accept
- Avg Score: 5.60
- Scores: 5, 6, 5, 6, 6

## Abstract
Decentralized collaborative learning under data heterogeneity and privacy constraints has rapidly advanced. However, existing solutions like federated learning,  ensembles, and transfer learning,  often fail to adequately serve the unique needs of clients, especially when local data representation is limited.  
To address this issue, we propose a novel framework called Query-based Knowledge Transfer (QKT) that enables tailored knowledge acquisition to fulfill specific client needs without direct data exchange. 
It employs a data-free masking strategy to facilitate the communication-efficient query-focused knowledge transformation while refining task-specific parameters to mitigate knowledge interference and forgetting. Our experiments, conducted on both standard and clinical benchmarks, show that QKT significantly outperforms existing collaborative learning methods by an average of 20.91% points in single-class query settings and an average of 14.32% points in multi-class query scenarios.
Further analysis and ablation studies reveal that QKT effectively balances the learning of new and existing knowledge, showing strong potential for its application in decentralized learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose the Query-based Knowledge Transfer (QKT) method where the learning process consists of two stages: 1) the feature extractor enhancement stage, where the model is optimized to approximate the prediction of the teacher model regarding the query classes, and 2) the classification head refinement stage, where the initialized classification head is reused and trained to maintain the accuracy of the original tasks. The method is empirically shown to be effective regarding the query-class accuracy gain and the local-class forgetting.

### Strengths
Originality: Although knowledge distillation is well-known, the authors additionally propose a masking strategy for query-oriented learning, and add a second stage in which they reuse the classification head to maintain performance.

Significance: The method is empirically shown to be effective both in improving the query-class performance and maintaining the local-class performance.

Strengths:
1. The masking strategy is innovative and motivated based on the observation made by (Guo et al 2017).
2. The experiments are comprehensive with multiple popular benchmarks included. Experimental results show strong improvement across datasets, even with the light version of QKT.
3. The effects of various factors are presented.

### Weaknesses
1. It is unclear what Figure 2 is showing. The background color is inconsistent. Besides, it is not obvious that the QKT improves the boundaries.
2. As the losses in both stages are both equation 4, it is not clear why the second stage helps to maintain the performance. Could the author provide some intuitions behind the strategy?
3. While the performances of different methods are reported, the time of convergence and the computational costs in communication are missing. It would be beneficial for authors to show the speed and computational costs of QKT compared to the baselines. The convergence can be slow due to the synthetic dataset generation and query-class identification of dynamic models. The datasets shown are mostly small toy datasets. It is unclear whether the method scales.
4. There is no experiment showing how the performance changes during stages 1 and 2. It could be insightful for the authors to show the dynamic performance within the stages.
5. The performance is evaluated with 10 clients. Could the author show how the baselines and the QKT method perform with an increasing amount of clients?

### Questions
As listed in the weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a challenge where the models are learned from heterogeneous environments. In specific, different clients can train their models with their local data. To this end, the authors introduce QKT to enhance the local model (a.k.a. student model) by distilling the knowledge from other pretrained models (a.k.a. teacher models). The solution consists of two phases: Feature Extractor Enhancement and Classification Head Refinement. The first phase filters out the irrelevant teacher models and uses them to facilitate the performance of the student model, and the second phase takes a further step to train the classifier. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper proposes a new decentralized collaborative learning approach to enhance the performance of a client. 
2. This work is well-motivated by identifying the limitations of knowledge distillation. 
3. The work is verified on various datasets and demonstrates superior performance over other baselines.

### Weaknesses
1. The authors should discuss the recent development of ensemble learning rather than (personalized) federated learning. The proposed QKT relies on a number of pretrained teacher models and looks pretty similar to ensemble learning settings. 
2. The proposed work requires pretraining for numerous teacher models. I cannot find the pretraining details in the paper. The authors should discuss this issue. Moreover, since these models store on a client, it leads to a significant storage burden if the client does not have sufficient storage/computation resources. Furthermore, the paper does not address the computational burden of loading multiple teacher models on a single client, especially during the distillation process where logits from multiple teachers are required. The client's limited resources (e.g., GPU memory) may not support simultaneous loading of all these models. 
3. The justification for using Equation (2) to filter teacher models is not sufficiently clear. The authors claim that a well-trained teacher model will have a higher probability on its trained classes when the input is Gaussian noise. However, if a teacher model is trained on a single class, it is expected to output a high probability for that class only when the input resembles that class. For Gaussian noise, the output should be random, as the model has never seen such data. The paper needs to provide a more robust explanation of why this filtering mechanism works and why the selected teachers enhance the student model's performance.
4. I saw a very related work, FedBoost [1], that is neither discussed in the paper nor mentioned in the rebuttal. I also noticed that the authors have not addressed other reviewers' comments.

### Questions
See **Weaknesses**.

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
3

### Summary
The paper introduces a framework that addresses the challenges arising from knowledge interference and catastrophic forgetting in FL due to the collaboration mechanisms that transfer knowledge between clients through weights. This is achieved by a data-free masking strategy that masks "irrelevant" knowledge from peer clients and a two-phase training process to balance knowledge transfer and retention.

### Strengths
1. The problem defined in the paper is interesting and the problems of knowledge interference and catastrophic forgetting make sense.
2. The paper is easy to understand.

### Weaknesses
1. Some of the claims like "QKT performs knowledge transfer in a single round, which is significantly more efficient than traditional centralized and peer-to-peer FL approaches that involve multiple communication rounds.", do not seem well justified since the goal of FL is joint collaborative training vs goal of this work is to distill knowledge from well trained peers.
2. The algorithmic details are not well presented - for example, how the teacher models' are trained and how their predictions are sent to the student model to obtain loss in Eq 4 are missing. 
3. Some algorithmic details like how communication rounds = 100 were set for other approaches and what synthetic datasets were used are also missing.

### Questions
1. How would the methods compare in more homogeneous data settings? And how does the quality of the teacher model impact the performance? Is there a criterion to eliminate teacher models apart from the class based criterion. 
2. Can you elaborate on what practical use case would this method be helpful in? And how does this work compare with body of work in knowledge distillation from multiple teachers in centralized settings?

### Soundness
2

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
3

### Summary
The paper introduces Query-based Knowledge Transfer (QKT) to learn query class in a collaborative learning setting while preventing interference from irrelevant information and mitigating catastrophic forgetting. It achieves this by implementing a two-phase distillation process that involves query-focused learning and classification head refinement. 
Experimental results demonstrate that QKT outperforms traditional federated learning and other collaborative methods in single- and multi-class query tasks.

### Strengths
- The variant QKT Light can reduce communication overhead by requiring only one communication round, making it well-suited for communication-limited settings.
- The authors demonstrate the adaptability of the proposed method across diverse datasets and tasks, including medical and standard image classification benchmarks.

### Weaknesses
 - The practical applications or user cases motivating this approach for query-based knowledge transfer are not clearly defined, especially given that personalized federated learning can also handle similar scenarios.
- The novelty of the paper's contributions is somewhat limited, as knowledge distillation and classification head refinement are established methods in personalized FL​  [1,2,3,4]
- Table 2 lacks comparisons with advanced personalized FL baselines after 2022 such as those in [5,6].
- Table 1 also lacks a baseline of standalone local fine-tuning on the query class, which is the simplest way to learn the query class without any communication. How effective is this baseline?
- QKT's performance is highly sensitive to the hyperparameters (e.g., $\lambda$ in the mask shown in Table 4), which could be challenging to optimize in real-world scenarios.


- It is unclear why learning irrelevant classes is inherently problematic, as shown in Figure 1; incorporating such classes could potentially enhance the model’s ability to handle out-of-distribution data in test time [5].
- In Phase 1 (lines 219-221), it seems to be assumed that clients are aware of the irrelevant classes for defining the threshold $\tau$. Does it mean that each client knows the complete set of available classes [C]? This might raise questions about the method's applicability in real-world decentralized settings where it could be hard to know what other clients’ classes are.

### Questions
- It is unclear why learning irrelevant classes is inherently problematic, as shown in Figure 1; incorporating such classes could potentially enhance the model’s ability to handle out-of-distribution data in test time [5].
- In Phase 1 (lines 219-221), it seems to be assumed that clients are aware of the irrelevant classes for defining the threshold $\tau$. Does it mean that each client knows the complete set of available classes [C]? This might raise questions about the method's applicability in real-world decentralized settings where it could be hard to know what other clients’ classes are.


post-rebuttal: Thanks to the authors for addressing my concerns about motivation and baselines. I raised the score accordingly.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a framework called Query-based Knowledge Transfer (QKT). This framework uses a data-free masking strategy that facilitates more effective knowledge distillation, addressing statistically heterogeneous environments in Federated Learning.

### Strengths
-The paper is well-motivated. Figures 1 and 2 makes it easy to understand the strong motivations of this paper. The writing is also clear.
- The idea of using noise to identify expert models is interesting, as it avoids dodgy reliances of "public data" or "synthetic data" in federated learning context, where such data may be scarce.

### Weaknesses
 -While the framework proposed seems general, it is not clear why only image-related tasks are considered.
- The accuracies on simple datasets in Table 2 seem surprisingly low, for the baseline approaches.
- The authors seem to have chosen some relatively general baselines to compare against, neglecting several Federated learning + knowledge distillation papers; such as Zhu, Z., Hong, J., & Zhou, J. (2021, July). Data-free knowledge distillation for heterogeneous federated learning. In International conference on machine learning (pp. 12878-12889). PMLR.
- the entire idea seems overly reliant on the overconfidence concept (Guo et al., 2017). This implies that a careful tuning of \lambda in (3) is needed. The experiments seem to not mention what happens when a client may be an expert in multiple classes at once, or when multiple clients are experts in a single class

### Questions
-how will the framework extend to other modalities?
- the authors claim that QKT completes learning in a single round. Is there convergence guarantees for this?
- using noise to check what expert a model is could also reveal the client's data distribution, which is itself a privacy intrusion

### Soundness
2

### Presentation
3

### Contribution
2
