# Hiding in Plain Sight: Disguising Data Stealing Attacks in Federated Learning

- Decision: Accept
- Scores: 6, 6, 6, 8, 5

## Abstract
Malicious server (MS) attacks have enabled the scaling of data stealing in federated learning to large batch sizes and secure aggregation, settings previously considered private. However, many concerns regarding the client-side detectability of MS attacks were raised, questioning their practicality. In this work, for the first time, we thoroughly study client-side detectability. We first demonstrate that all prior MS attacks are detectable by principled checks, and formulate a necessary set of requirements that a practical MS attack must satisfy. Next, we propose \tool{}, a novel attack framework that satisfies these requirements. The key insight of \tool{} is the use of a secret decoder, jointly trained with the shared model. We show that \tool{} can steal user data from gradients of realistic networks, even for large batch sizes of up to 512 and under secure aggregation. Our work is a promising step towards assessing the true vulnerability of federated learning in real-world settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper found that existing malicious server attacks in FL are detectable on the client side using a metric, D-SNR. The authors then propose a new attack called SEER which can bypass the detection by co-optimizing the disaggregator and reconstructor.

### Strengths
1. D-SNR is a useful metric to detect disaggregation by malicious server
2. SEER is an attack that can efficiently extract information and bypass D-SNR detection.

### Weaknesses
1. The performance of SEER will depend on the task and dataset. For some dataset, SEER might lose effect since it's not always possible to disaggregate a value from the mean. Specifically, the disaggregation process relies on the server's ability to manipulate the global model weights to induce specific gradient patterns in the clients. If the client-side gradients are inherently resistant to such manipulation due to the nature of the data or the model architecture, SEER's effectiveness could be significantly reduced. For instance, if the gradients are highly sparse or if the relationship between the model weights and the gradients is non-linear and complex, the attack might struggle to extract meaningful information.
2. The evaluation is on CIFAR10/100. It'd better to demonstrate the effectiveness of SEER on more tasks closer to real-world applications. The current evaluation lacks diversity in terms of data modalities and task complexity. The CIFAR datasets are relatively small and well-structured, which might not accurately reflect the challenges and nuances of real-world federated learning scenarios. For example, tasks involving natural language processing, time-series data, or medical imaging could present different challenges for the SEER attack, potentially revealing limitations not apparent in the current evaluation.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies data-stealing attacks in federated learning with malicious servers. The authors first demonstrate the client-side detectability of existing attacks by introducing a simple vulnerability metric called D-SNR, and then reveal the limitation of their attack design which is their dependence on the underlying honest attack. Based on this analysis, the authors further propose a new attack framework SEER using a server-side decoder that is jointly optimized with the shared model to reduce the chances of being detected. Experiments on three image datasets show that the proposed attack can successfully extract user data of large batch sizes (up to 512) even under secure aggregation.

### Strengths
- The paper is in general well-written and self-contained and provides a good summarization of prior studies in this field.

- The proposed method addresses several limitations of existing attacks including client-side detectability and the assumptions on BN statistics and labels.

- The idea of jointly learning a disaggregator and a reconstructor with the shared model is novel.

- The empirical results are in favor of the proposed method in terms of stealthiness and reconstruction quality.

### Weaknesses
 - The work lacks a more nuanced discussion on the threat model. Despite having relaxed some of the assumptions of previous work, the proposed attack is still somewhat restrictive in the sense that it requires multiple steps of offline training and an auxiliary dataset of sufficient size, and it is not very clear how to deploy such an attack during the federated learning process in practice. In particular, the joint optimization of the shared model seems to ignore the classification loss of the federated task, which might be leveraged to detect the attack in a retrospective way (e.g., a client may evaluate the local training loss before and after each update and choose to opt out of training if the loss is not reduced after several rounds). One reasonable strategy is to deploy the attack in the first round of training, i.e., substitute the random initialization with the optimized model weights, but this may still raise the alarm if it’s beyond normal weight distributions. It would be better to add corresponding discussions and limitations.

- It is not quite clear how to utilize the batch normalization statistics to design the local selection strategy of the property.

- The proposed attack algorithm appears to be quite computationally expensive (~14 GPU days to train for ResImageNet). It also implicitly assumes knowledge of the private data distribution as is for all learning-based attack approaches that rely on a large auxiliary dataset.

### Questions
1. Could you provide some further explanation on how SEER utilizes batch normalization to choose the local property? In cases where this is not feasible (e.g., secure aggregation or no batch norm layer), would it be possible for the attacker to simply run a linear search to find the optimal property for each batch?

2. Would it be possible to replace the learned disaggregating mapping with some hand-crafted criteria such as simply recovering the image with the largest loss within the batch?

3. Does the design of the local properties take into account the potential non-IIDness of the data? What’s the success rate if the clients’ data are locally correlated?

4. Could you share some insights on designing potential defense and mitigation strategies for the proposed attack besides standard options like DP and HE?

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
1. The paper focuses on the issue of client-side detectability of malicious server (MS) attacks in federated learning. It discusses prior work on gradient leakage attacks in federated learning, including honest server attacks, malicious server attacks, and the limitations of existing attacks.

2. To ensure reproducibility, the authors provide the source code of SEER in the supplementary material and detail how to install the code prerequisites and reproduce the experiments presented in the paper.

3. Overall, the paper contributes a novel attack strategy that avoids detection in federated learning, highlights the importance of attack detectability, provides insights into reconstructing data from securely aggregated gradient updates, and addresses the ethical implications of their attack.

### Strengths
1. The authors propose a novel attack strategy called SEER that avoids detection while effectively stealing data despite aggregation. They demonstrate that all prior attacks are detectable in a principled way and highlight the importance of studying attack detectability.

2. SEER is designed to reconstruct data from securely aggregated gradient updates. The authors describe in detail how they combine local and global distribution information about the client data to achieve this reconstruction.

3. The paper also discusses the ethical implications of their attack and acknowledges the potential disparate impact and privacy risks. However, they argue that their investigation of detection and emphasis on realistic scenarios have a positive impact by enabling further studies of defenses and helping practitioners better estimate privacy risks.

### Weaknesses
1. Would the author have some initial idea for defensing the proposed attacks？

### Questions
See weakness part

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the disaggregation signal-to-noise ratio (D-SNR) metric, designed to detect the vulnerability of local clients to malicious attacks (MS). Subsequently, the authors outline a set of requirements for future realistic MS attacks. They then present a novel attack framework, SEER, which operates by disaggregating the gradients in a hidden space. Specifically, the SEER framework encompasses a shared model dispersed among clients for encoding gradients, a server-side disaggregator to nullify the contributions of images not satisfying the pre-defined property and a server-side reconstructor to reconstruct images that comply with the said property. The framework facilitates end-to-end training and presents a challenge for detection using D-SNR, in contrast to previous MS methods. Experiments also show the effectiveness of the proposed method.

The main contributions of this work include a pioneering study of client-side detectability, the introduction of a novel detection metric, highlighting potential concerns for future MS, and the unveiling of a groundbreaking realistic MS approach.

### Strengths
- The paper is well-written and easy to follow, making for an enjoyable read.
- The motivation is clear and the study problem is significant.
- The proposed detection metric and attack framework are innovative and intriguing, offering a fresh viewpoint on the privacy issue in FL.

### Weaknesses
The main concern is about the auxiliary data used to train the SEER framework. The key point is that the pre-defined property could separate examples.
The paper details experiments where CIFAR10 serves as the auxiliary data for other client datasets (CIFAR10.1v6, CIFAR10.2, and TinyImageNet). While the results affirm its robustness to distributional disparities between the auxiliary and client data, there may be scenarios where this approach is less effective. For instance, when the clients possess specialized data such as medical records, the server have no prior knowledge about the data and use generic dataset like CIFAR10 as the auxiliary data, the framework might encounter challenges, because the pre-defined property might significantly differ across such diverse datasets.

### Questions
- How does the proposed SEER MS fare when differential privacy mechanisms are implemented?
- How does SEER perform in non-iid settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out that malicious attacks for data stealing of FL clients are easily detectable, and propose a novel data stealing attack named SEER that can evade defenses and achieve good data reconstruction performance.

### Strengths
Propose to design defense-aware data stealing attacks, making the attacks potentially stealthier.

### Weaknesses
1.  Threat model is missing. For example, it is until the description of the SEER attack that the authors mention the availability of auxiliary data at the server, which is not always required by other attacks and can be a strong assumption. Furthermore, the threat model does not specify the capabilities of the adversary, such as whether they can modify the client-side code or only the server-side parameters. This lack of clarity makes it difficult to assess the practical relevance of the proposed attack.
2.  Lack of details: it is not clear what are the exact client-side checks the malicious server needs to evade; it is also not clear what do the authors mean by “handcrafted modifications”. Why is SEER’s mode not handcrafted? The descriptions of the necessary conditions at the end of section 3 are too vague, not to mention providing any theoretical or experimental proofs for those. It is important to specify which client-side defenses are considered, such as gradient clipping or differential privacy, and how SEER evades them. The term "handcrafted modifications" needs a precise definition to distinguish it from the optimization-based approach of SEER.
3.  It is not clear how SEER exactly breaks through secure aggregation. The paper does not explain the specific mechanisms that allow SEER to bypass the cryptographic protections of secure aggregation. A detailed explanation of how SEER manipulates the aggregated gradients to extract individual client data is required.
4.  Quality and quantity of auxiliary data are key to the performance of SEER. More discussions and ablation studies are needed on auxiliary data. The paper should explore how the size and diversity of the auxiliary dataset affect the reconstruction quality. This includes evaluating the attack's performance with varying amounts of auxiliary data and different levels of distribution shift between auxiliary and client datasets.
5.  Complexity issue. Algorithm 1 needs to be repeated for each sample in the batch (i.e., retrain a set of models for each property). This incurs high computational complexity, and should be evaluated carefully and compared with baselines. The computational cost of retraining a model for each sample needs to be quantified and compared to the computational overhead of other attacks. Additionally, the paper should discuss the scalability of SEER to larger batch sizes and more complex models.
6.  No evaluations of SEER and baselines under defenses, which is supposed to be the main motivation of the paper. The core claim of the paper is that SEER can evade defenses, but there is a lack of experimental validation of this claim. The paper should include a comprehensive evaluation of SEER under various defense mechanisms, such as differential privacy, gradient clipping, and secure aggregation with added noise.
7.  The results in Table 3 are quite counter-intuitive and curious. This needs more exploration and explanation. The paper should provide a more in-depth analysis of the results in Table 3, explaining why certain properties lead to better reconstruction quality than others and why the performance varies across different datasets. The lack of explanation weakens the credibility of the results.
8.  Only comparison with one baseline in Table 4, which is insufficient. The reviewer would like to see more evaluations and comparisons with the malicious server attacks mentioned in the "gradient leakage attacks" subsection in introduction, and "malicious server attacks" sub-section in related work. Specifically, comparisons with the following recent attacks are needed:

1) Joshua C. Zhao, Atul Sharma, Ahmed Roushdy Elkordy, Yahya H. Ezzeldin, Salman Avestimehr, and Saurabh Bagchi. Secure aggregation in federated learning is not private: Leaking user data at large scale through model modification. arXiv, 2023. (Just accepted to S&P 2024 with the title "LOKI: Large-scale Data Reconstruction Attack against Federated Learning through Model Manipulation").

2) Shuaishuai Zhang, Jie Huang, Zeping Zhang, and Chunyang Qi. Compromise privacy in large-batch federated learning via malicious model parameters. In ICA3PP, 2023.

### Questions
1.	Does a distinguishing property for each sample in a batch always exist? What if it does not exist? How does it affect the performance of SEER?
2.	Are all the experiments under any kinds of defenses or nor? How do the experiment results show that SEER is undetectable?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
