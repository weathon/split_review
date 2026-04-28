# MQFL-FHE: Multimodal Quantum Federated Learning Framework with Fully Homomorphic Encryption

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 3, 3, 5, 3

## Abstract
The integration of fully homomorphic encryption (FHE) in federated learning (FL) has led to significant advances in data privacy. However, during the aggregation phase, it often results in performance degradation of the aggregated model, hindering the development of robust representational generalization. In this work, we propose a novel multimodal quantum federated learning framework that utilizes quantum computing to counteract the performance drop resulting from FHE. For the first time in FL, our framework combines a multimodal quantum mixture of experts (MQMoE) model with FHE, incorporating multimodal datasets for enriched representation and task-specific learning. Our MQMoE framework enhances performance on multimodal datasets and combined genomics and brain MRI scans, especially for underrepresented categories. Our results also demonstrate that the quantum-enhanced approach mitigates the performance degradation associated with FHE and improves classification accuracy across diverse datasets, validating the potential of quantum interventions in enhancing privacy in FL.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work combines a multimodal quantum mixture of experts (MQMoE) with fully homomorphic encryption (FHE). Integrating FHE with federated learning (FL) is advantageous in data privacy, but results in performance degradation of the aggregated model. This work takes a stab at addressing this issue utilizing quantum computing.

### Strengths
The manuscript is well written in general. The integration of quantum federated learning to address performance degradation of FHE scheme is interesting. Experiments, although not detailed enough, seem to support the claim.

### Weaknesses
- I do not have any experience with fully homomorphic encryption nor quantum federated learning. However, to me, this work is understood as a proof of concept, with many non-trivial tasks abstracted away. Please refer to the Questions section for more detailed comments.
- Given that all quantum experiments are carried out with Pennylane, it is hard to conclude that the proposed method indeed is beneficial; on the other hand, this work seems to assume client as well as server in FL has access to quantum computer, which seems very farfetched.
- It’s a bit hard to follow without any equation numbers, for instance third point in the questions.

### Questions
- Quantum computers are inherently more noisy due to its probabilistic nature. Why would utilizing QC “reduce” noise accumulation in conjunction with FHE? I could not find any intuition or explanation.
- It seems that each client is also assumed to have access to a quantum computer, based on Eq. in line 199. Encoding classical data to a quantum state, especially if the data is multi-modal, sounds quite non-trivial. Can you comment on how this can be achieved?
- Continuing on the above point, multimodal dataset preparation is just “abstracted” in Algorithm 1 with $\mathcal{D}_k \leftarrow \text{PrepareMultimodalDataset(k)}$. But this is highly non-trivial, e.g., how would you encode text and image dataset into a quantum state? I’m quite confused how the local model update for client $k$ is done in line 273 when the local data is already encoded into a quantum state (line 199).
- Is the experimental result in Table 3 without the FHE scheme?
- Given that pennylane is used for quantum experiments, are processes outlined in Figure 3 utilized at all for experiments? If yes, these should be explained in detail. If not, I’m not sure how to interpret the experimental results in conjunction with what is claimed in the main text.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a multimodal quantum federated learning framework (MQFL-FHE) that utilizes quantum computing to improve the performance of fully homomorphic encryption (FHE) in federated learning (FL). The authors specifically focus on federated learning from multimodal data. The authors show that by using quantum NN layer, the performance degradation of using FHE in federated learning can be alleviated.

The experiments are performed on 4 dataset of different modality and the proposed approach is compared against centralized training, federation training and federated training with FHE.

### Strengths
- The paper is easy to follow and I commend the authors for showing results on different types of datasets. 
- The results are intriguing
   - Even though quantum layers perform worse than classical training in centralized setting and is only on par in federated setup quantum layers + FHE outperforms federated training in some cases.

### Weaknesses
 - While the empirical results with QC+FHE+FL are better, the motivation for using QC unclear. What is the main intuition? It is further not clear why QC works in some cases and doesn't work in other cases. Authors should investigate this more.
- The experimental setup is quite vague. It is unclear what is the distribution of and size of the training datasets for each client. One of the key issues in FL is heterogenous setups, that is, different clients may have different distribution and different sizes of training dataset. Authors should evaluate the approach in heterogenous settings.
- The baselines are trivial or ablation of the main method. It is unclear how the proposed method QC+FHE perform, compared to other more advanced methods, say CreamFL + FHE? It would be nice to see some more relevant baselines.

- While paper is easy to follow, certain parts of the paper are unclear or incoherent. See questions.

### Questions
- Is the MQMoE framework designed for paired data, Fig 3? That is does the model take (MRI,DNA) pair as the input in the multimodal experiments? 
   - If the dataset is paired, how do you handle missing data? Table 1 has different number of MRI & DNA data, so there may be some missing datasets?
- The test accuracy in multimodal setup is poorer than unimodal case in Table 1? So does this suggest that there is no benefit of having an additional modality?

- In sec 5.1, 
  - **Effects of FHE modifications** I can't find experiments corresponding to this ablation? It would be nice to include references to table or figures, if any 
  - Similar for **Efficacy of the MQMoE approach**, which experiments should I refer?


- Typo: Line 158-159, what is X? Did you intend to write $g_i(\theta, x_i)$
- What is Q, K, V on line 272? How is it computed?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose a multimodal quantum federated learning (FL) framework that incorporates quantum computing to mitigate the performance degradation in the aggregation phase caused by fully homomorphic encryption (FHE). The authors integrate the MQMoE model with FHE in FL to perform task-specific learning. They use the CKKS encryption scheme to encrypt local models and combine it with quantum federated learning to handle heterogeneous data modalities.

### Strengths
The authors introduce the research background of quantum computing, privacy protection, and multimodality in federated learning. They propose a framework that combines quantum federated learning and homomorphic encryption and apply it to multimodal quantum federated learning. Through ablation experiments, they demonstrate the specific role of each module.

### Weaknesses
1. The paper lacks an in-depth exploration of the integration between homomorphic encryption, quantum computing, and federated learning. There is insufficient discussion on how these technologies work together and how their respective advantages are reflected within the framework.
2. The argumentation regarding homomorphic encryption technology is insufficient. The paper employs the CKKS scheme but lacks a thorough discussion on security analysis and threat models, including potential attack methods and countermeasures, which may weaken the paper's discourse on privacy protection. For example, references such as "Remark on the Security of CKKS Scheme in Practice" by Jung Hee Cheon, Seungwan Hong, and Duhyeong Kim (2020) and "On the Security of Homomorphic Encryption on Approximate Numbers" by Li, B., Micciancio, D. (2021) should be considered.
3. In the experimental section, the paper lacks information on the parameter configuration of the CKKS scheme and its corresponding security levels, which may affect the reproducibility and practicality of the experimental results.
4. Additionally, the paper lacks technical innovation, merely combining homomorphic encryption and quantum computing for use in federated learning.
5. The layout of some figures in the paper could also be improved, as some images are too small to read comfortably.

### Questions
1. How do homomorphic encryption, quantum computing, and federated learning work together, and how are their respective advantages reflected within the framework?
2. Without security analysis and threat models, how can one ascertain the risks and limitations of the framework in specific application scenarios?
3. What are the specific security parameters of the CKKS scheme?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces MQFL-FHE, a Multimodal Quantum Federated Learning framework that incorporates Fully Homomorphic Encryption (FHE) to address data privacy concerns while utilizing quantum computing to mitigate performance degradation typically caused by encryption. The proposed framework uniquely integrates a Multimodal Quantum Mixture of Experts (MQMoE) model within the Federated Learning (FL) setup to enhance representational generalizability and classification accuracy, especially for underrepresented categories. Experimental validation is conducted using multimodal datasets, including genomics and brain MRI scans, demonstrating the framework's potential to improve privacy and performance.

### Strengths
The paper provides a novel integration of quantum computing and fully homomorphic encryption within the federated learning context, which is an innovative contribution to improving data privacy without sacrificing model performance.
﻿
The proposed MQMoE architecture effectively handles diverse multimodal data, achieving enhanced representation learning and mitigating the performance degradation associated with homomorphic encryption.
﻿
The work is well-supported by experimental results, which illustrate improvements in both data privacy and model accuracy across diverse datasets, particularly in sensitive areas like genomics and MRI scans.

### Weaknesses
The paper lacks sufficient detail on the practical implementation challenges associated with deploying the proposed quantum-enhanced federated learning framework.

The paper discusses the impact of homomorphic encryption on model accuracy in the introduction and related works. However, the discussion and citations related to this topic should be expanded to provide a more comprehensive context. Additionally, the experiments could better reflect this aspect by including different hyperparameters or model structures to illustrate the effects more thoroughly.

### Questions
The authors demonstrate the framework's performance using DNA and MRI datasets, but the scalability to other types of multimodal data is unclear. Could the authors elaborate on how adaptable the proposed approach is to other types of data and any challenges they foresee?
﻿
The paper discusses the impact of homomorphic encryption on model accuracy. It would be beneficial to expand on this discussion with additional citations to similar works and provide more thorough experiments to investigate the impact. For example, testing different hyperparameters or model structures.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an approach to Federated Learning (FL) that incorporates fully homomorphic encryption (FHE) using the Cheon-Kim-Kim-Song (CKKS) encryption scheme, enabling secure parameter aggregation on encrypted data. The authors address a critical challenge in FHE-based federated learning: the introduction of noise during encrypted data aggregation, which affects model accuracy post-decryption. Their key contribution lies in demonstrating how quantum models can effectively mitigate this noise-induced performance degradation.
The authors propose three progressive implementations combining quantum computing with FL+FHE: (i) QFL+FHE: A basic integration of quantum models with FL+FHE, (ii) MQFL+FHE: An extension of QFL+FHE designed to handle multimodal input data, (iii) MQMoE-FL-FHE: An advanced architecture incorporating mixture of experts strategy within the QFL+FHE framework
The experimental validation compare the classical FL+FHE and centralized approaches across multiple datasets, including CIFAR-10, DNA sequences, MRI scans, and PCOS. For multimodal applications, the they evaluate their framework on combined DNA+MRI datasets.

### Strengths
The experimental results show that quantum neural networks (QNN) is more robust to be trained in in federated settings. Specifically, when comparing centralized versus federated learning with FHE, classical models show a larger drop in performance than quantum models.

### Weaknesses
1- In Algorithm 1, the decryption seems to happen on the server side, which is problematic. If the server has access to the secret key, it can decrypt each client's model parameters individually, making the encrypted aggregation redundant, so the purpose of the encryption should be clarified.
2- The simulation (dashboard_src/client.py) the implementation differs from Algorithm 1 and shows that only clients have access to the secret key. Clients send encrypted model updates to the server, where aggregation occurs on encrypted parameters, and the aggregate value is returned to each client for decryption. However, this scenario has a critical weakness: for the server to aggregate encrypted parameters, all clients must share the same secret key. The paper doesn't specify how clients share this key without server knowledge, particularly if all communication goes through the server. If secret sharing is used, there should be additional communication channels specified; otherwise, the purpose of FHE in this scenario is questionable.
3- The paper lacks theoretical proof demonstrating why quantum models should perform better under FL+FHE compared to classical approaches. Additionally, some simulation results appear inconsistent with theoretical expectations mentioning in point 5.
4- The application of QNN in this work lacks clarity. It appears disconnected from the FL logic and CKKS encryption mechanism, serving only as a comparison between implementing FL+FHE with classical models versus QNN+FL+FHE .
5- Under ideal conditions (perfect communication, infinite rounds), FL can at best match centralized learning's performance. It is unclear why QFL achieves higher accuracy compared to the centralized version (as shown in Tables 3 and 4 for DNA, MRI, PCOS, and multimodal datasets). Also, QFL+FHE outperforms both QFL and centralized quantum approaches in DNA and multimodal cases which is not compatible with FL concept.
6- The communication cost for FHE implementation is not addressed. The paper should explain both the communication and computation complexity of adding FHE to the FL process.

### Questions
1- Could you clarify whether the decryption and global model update process occurs on the server side or client side? The algorithm and implementation appear to show different approaches.
2- Does your implementation require clients to share the same secret key? If so, how is this key sharing accomplished securely without server access to this information?
3- If your system employs secret-sharing schemes for key distribution among clients, how do you handle client dropout scenarios? Have you investigated the impact of client unavailability on the secret-sharing mechanism?
4- The paper claims quantum computing helps mitigate FHE noise accumulation. Could you provide a detailed mathematical analysis demonstrating how quantum computing specifically counteracts this noise?
5- There appears to be an inconsistency between test loss and accuracy values in Tables 3 and 4. While accuracy increases, the loss also increases, which seems counterintuitive. Could you explain this apparent contradiction?
6- Your ablation study states that centralized systems outperform federated ones, yet the values in Tables 3 and 4 show the opposite trend. Could you clarify this discrepancy?

### Soundness
2

### Presentation
2

### Contribution
1
