# FedNovel: Federated Novel Class Learning

- Decision: Reject
- Scores: 8, 6, 3, 5

## Abstract
In a privacy-focused era, Federated Learning (FL) has emerged as a promising machine learning technique. However, most existing FL studies assume that the data distribution remains nearly fixed over time, while real-world scenarios often involve dynamic and continual changes. To equip FL systems with continual model evolution capabilities, enabling them to discover and incorporate unseen novel classes, we focus on an important problem called \emph{\underline{Fed}erated \underline{C}ontinual \underline{N}ovel Class Learning} (\FedNovel{}) in this work. The biggest challenge in \FedNovel{} is to merge and align novel classes that are discovered and learned by different clients without compromising privacy. To address this, we propose a \emph{Global Alignment Learning} (\GAL{}) framework that can accurately estimate the global novel class number and provide effective guidance for local training from a global perspective, all while maintaining privacy protection. Specifically, \GAL{} first locates high-density regions in the representation space through a bi-level clustering mechanism to estimate the novel class number, with which the global prototypes corresponding to novel classes can be constructed. Then, \GAL{} uses a novel semantic weighted loss to capture all possible correlations between these prototypes and the training data for mitigating the impact of pseudo-label noise and data heterogeneity. Extensive experiments on various datasets demonstrate \GAL{}'s superior performance over state-of-the-art novel class discovery methods. In particular, \GAL{} achieves significant improvements in novel-class performance, increasing the accuracy by 5.1\% to 10.6\% in the case of one novel class learning stage and by 7.8\% to 17.9\% in the case of two novel class learning stages, without sacrificing known-class performance. Moreover, 
\GAL{} is shown to be effective in equipping a variety of different mainstream FL algorithms with novel class discovery and learning capability, highlighting its potential for many real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel method to learn novel classes in federated learning with emerging unknown classes.

### Strengths
1. (Originality) The proposed method is novel by known-class representation learning and adaptive class merging without access to clients' data.
2. (Clarity) The paper is clear in techniques. Methods are well formulated and motivated. Sufficient details are provided for the experiments.
3. (Significance) The proposed method is sufficiently evaluated in multiple datasets, models including small-scale sets (like Cifar10, or Cifar100) and large-scale sets (ImageNet). In all of these experiments, the proposed methods outperform the baselines in both known class and novel class evaluations.
4. (Quality) Extensive experiments evaluate the method in multiple dimensions. Importantly, multiple federated learning is demonstrated to be integrable with the proposed method.

### Weaknesses
1. The authors claim their contribution as a federated novel-class learning without compromising privacy. However, it is unclear how the existing federated novel-class learning methods compromise privacy. Importantly, the definition of private information is vague. It seems that the number of novel classes is thought to be private, which however is not necessarily true. Without specification on the privacy definition, there also lacks sufficient justification for how the proposed method will protect privacy. Though I appreciate the empirical results of privacy evaluation, the authors should clarify the meaning of privacy and adjust the claim of privacy.

### Questions
* What is the definition of private information in the paper?

### Soundness
3 good

### Presentation
2 fair

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
This paper considers a novel FL scenario, where the data distribution involves dynamic and continual changes. Instead of naively integrating FL and conventional novel class discovery methods,  the authors propose a Global Alignment Learning (GAL) framework to estimate the number of novel classes and optimize the local training process in a semantic similarity-empowered reweighting manner. Extensive experiments have been conducted to demonstrate the efficiency of the proposed method.

### Strengths
[+] The whole paper is easy to understand, and well-written.

[+] The problem statement is very nice and clean. It also has some applications in practice.

[+] There is enough empirical evidence to support the main claims of the paper.

### Weaknesses
[-] It seems that open-world semi-supervised learning [1][2] also considers classifying both seen and unseen classes during the testing phase. Please compare it in related work.

[1] Open-world semisupervised learning. In International Conference on Learning Representations, 2022.

[2] Robust semi-supervised learning when not all classes have labels. In Advances in Neural Information Processing Systems, 2022.

[-] In section 4, the baselines on federated self-supervised learning methods are insufficient. It is suggested to add more FedSSL methods in the experimental part.

[3] Semifl: Semi-supervised federated learning for unlabeled clients with alternate training. Advances in Neural Information Processing Systems, 35:17871–17884, 2022.

[-] It is unclear why the value of $n_{size}$ is set as 2. A more detailed explanation should be added.

### Questions
It is unclear why the value of $n_{size}$ is set as 2. A more detailed explanation should be added.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a prototype-based class number estimation method for Federated Novel Class Discovery, where the model is required to merge and align novel classes that are discovered and learned by different clients under privacy constraint. Extensive experimental results demonstrate the effectiveness of proposed method.

### Strengths
1.	This paper is well-written, well-organized and easy to follow.
2.	The performance of the proposed method is impressive.
3.	Ablation studies are comprehensive and demonstrate the effectiveness of proposed method.

### Weaknesses
1. 	Lacks of crucial reference literatures [A][B]. Thus, Federated New Class Discovery/Learning is not a new research problem. In contribution, authors say,” we are the first to focus on this problem and propose an effective solution”. It might be somewhat overclaiming.
2.	Insufficient comparison and discussion. From my understanding, the proposed method is similar to commonly-used semi-supervised learning methods. 
3.	Limited novelty. From the perspective of NCD methods, prototype-based contrastive learning and low confidence sample rejection have explored in [C]. Why is the proposed method superior to [C]? From the perspective of semi-supervised federated learning methods, the federated prototype learning has been studied in [D][E]. What’s the novelty of the proposed methods compared with [D][E]?
4.	From my understanding, [A][B] can also be used in federated new class learning. It is better to discuss and compare the proposed method with [A][B].
5.	Lack of theoretical proof why the estimation method is better than other competitors.
6.	The reasonableness of the experiment setting still needs to be considered. As authors claimed in the paper, they use Dirichlet Distribution to control data heterogeneity. (1) It makes client labeled and unlabeled data highly-unbalanced. However, in [F], the labeled and unlabeled data are kept fixed partitioning. It is better to discuss the relationship between proposed method and data distribution. (2) It might lead clients to have some sharing categories or have non-overlapping categories. How does the proposed method solve both situations?

### Questions
Please see Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores novel class discovery and learning within the framework of federated learning, addressing the challenge of evolving data on local client devices. The study introduces a Global Alignment learning framework aimed at estimating the number of global novel classes and providing guidance for local training. Specifically, this framework initially estimates the number of novel classes by identifying high-density regions within the representation space. Then, it captures all potential correlations between prototypes and training data to alleviate issues related to data heterogeneity. The proposed approach demonstrates advanced performance across a range of benchmark datasets

### Strengths
1. The paper is well-written and easy to read. 

2. It introduces an effective approach for discovering novel classes with Global Alignment learning, specifically targeting the federated learning setting with dynamic change in data distribution.  

3. The authors conducted thorough experiments to validate the effectiveness of their proposed approach. Through empirical evidence, they support their claims and offer insights into the performance and advantages of novel class learning under the constraint of non-iid data, and privacy protection.

### Weaknesses
1. The method lacks sufficient elaboration and requires additional effort to comprehend the underlying technique. For instance, it encompasses multiple design elements, yet Figure 1 fails to offer adequate details to facilitate a clear understanding of the approach. And it is difficult to visualize the algorithm. It would be better if the paper provided an algorithm block. (Q1, Q2, Q4)

2. Some of the assertions made in the paper need additional justifications. (Q3)

### Questions
1. What is the training process? 

(a) In section 3.2, the known classes depend on Equation (2) to converge to model $m^L$. Then Section 3.3.1 includes a modified PCL to enhance training. Is the modified PCL included during the training for $m^L$ or after the global server achieved $m^L$?

(b) From Figure 1, the local prototypes are only uploaded once to the server, which contradicts my understanding of FL: the local models should communicate with the central server for several rounds until converge. And as the local model keeps updating, the local prototypes should also evolve, how does one-time uploading transmit every local information?

2. Section 3.2 mentions the unlabeled testing datasets "belongs to a unified novel label space", does it assume the number of classes of novel samples is fixed? If this number is not fixed, then how to decide the number of clusters? If this number is fixed, how does it apply to the setting where the novel data are continually emerging?

3. Section 3.3.2 chooses neuron weights as prototypes since the data from other clients is unavailable in the FL setting. However, there is still a lot of difference between weights and features. Any justification to support that using weights as prototypes is as effective as data/features?

4. The "anchor sample" first appears in Section 3.3.1. How are they selected, or what is their definition? 

5. In Section 3.3.2, there is a data memory storing filtered-out data. Are these data filtered out because they are known class data?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
