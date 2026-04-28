# ATTENDING: Federated Learning with Personalized Attentive Pruning for Heterogeneous Clients

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Federated Learning (FL) emerges as a novel machine learning paradigm, enabling distributed clients to collaboratively train a global model while eliminating local data transmission.  Despite its advantages, FL faces challenges posed by system and data heterogeneity. System heterogeneity prevents low-end clients from participating in FL with uniform models, while data heterogeneity adversely impacts the learning performance of FL. In this paper, we propose the personalized ATTENtive pruning enabled federateD learnING (ATTENDING) to collectively address these heterogeneity challenges. Specifically, we first design an attention module incorporating spatial and channel attention to enhance the learning performance on heterogeneous data. Subsequently, we introduce the attentive pruning algorithm to generate personalized local models guided by attention scores, aiming to facilitate clients' participation in FL. Finally, we introduce a specific heterogeneous aggregation algorithm integrated with an attention matching mechanism to efficiently aggregate the pruned models. We implement ATTENDING with a real FL platform and the evaluation results show that ATTENDING significantly outperforms the baselines by up to 11.3\% and reduces the average model footprints by 32\%. Our code is available at: https://anonymous.4open.science/r/ATTENDING.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents ATTENDING (personalized ATTENtive pruning enabled federateD learnING), an approach to tackle the dual challenges of system and data heterogeneity in Federated Learning (FL). The authors propose an attention module that leverages spatial and channel attention to improve learning across diverse data distributions. They also introduce an attentive pruning method that produces personalized models based on attention scores, allowing broader client participation. Finally, a specialized heterogeneous aggregation algorithm, combined with attention matching, enables efficient model aggregation. Together, the paper claims these innovations improve FL’s adaptability and performance on heterogeneous systems and datasets.

### Strengths
+The paper is well represented, and easy to read. 

+The paper tries to address multiple challenges in FL: non-iid, heterogeneous client, resource constraints. All of them are interesting research directions in FL.

### Weaknesses
 - The paper mixes of three techniques: attention, personalized pruning, heterogeneous aggregation. All proposed methods are largely align with prior work. The paper fails to demonstrate the novelty, not even any incremental improvements.

- The paper fails to show the significance of integrating the three techniques together. Why does the paper put the three techniques together? How can they interplay? What are the challenges of integration? 

- The paper lacks theoratical analysis. 

-  The evalution is weak. Please see the specific questions. 

-  Related work is not sufficient. There are a lot of work in pruning, heterogieous devices for FL. The proposed method shall be compared with them.



### Questions
The paper is only compared with the methods for non-iid and model compression. How about the works in literature on heterogieous devices for FL and personazlied FL? Given that the proposed approach integrates three techniques, it would be more appropriate to compare it against existing works that also combine multiple techniques.

How are experiment settings determined? How are the model, dataset, pruning ratios,  α selected? 

How many clients are used for MNIST dataset in talbe 2 and table 3? How is the average performance cacluated? 

Why MNIST dataset is spllitted for 100 cleints, while cifar10 and cifar100 are splited for 10 clients? 

“FLOPs” can not be used to determine computation consumption. It is just a theoretial justification when sparsification is used. Please run the algorithm on-device and show the actual running time. Because the method is complex, the actual computation time on real device may be longer than other approaches. 

There is no result showing heterogeous devices. Since the method is propopsed for heterogeous devices. Please show such results on real device. 

The paper only shows results on image data. Please justify the applications of image data on heterogeous devices for FL. Or the paper shall include results with diversified datasets. 

The datasets used in evaluation are too simple, including MNIST, cifar10, and cifar100. Plus, they are not the dataset for heterogeneous FL, because the datasets have to be splitted artifically for the clients and non-iid. 

Minor issue: please carefully select the Primary Area when submitting the paper, instead of just using "other topics in machine learning (i.e., none of the above)". There must be a more appropriate Primary Area for the paper.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes an attention pruning method called ATTENDING for federated learning to address the data heterogeneity and system heterogeneity issues. Specifically, spatial and channel attention are designed to extract features from Non-IID data and assess model parameters' importance, respectively. Moreover, each client executes model pruning, and the server executes attention aggregation based on attention scores to shrink the footprint. ATTENDING is evaluated on three datasets and results show that ATTENDING can improve test accuracy and reduce model footprint.

### Strengths
1. The paper is well-written, and the idea is easy to follow.

2. There are figures to help understand the methods.

### Weaknesses
1. Authors claim that one main advantage of ATTENDING compared with other methods is reducing communicating, computational, and storage overhead. However, there is limited theoretical analysis regarding these perspectives. One example of computation (lines 193-196) is insufficient. The analysis should include a formal treatment of the computational complexity of the attention mechanism and the pruning process, as well as a comparison with the complexity of other pruning methods. The current discussion lacks a detailed breakdown of the FLOPs involved in both the training and inference phases, making it difficult to assess the true computational savings.

2. The authors also claim that their method does not need binary mask matrices compared with other pruning methods. However, the disadvantages of using matrices and the advantages of ATTENDING are not well analyzed and compared theoretically and experimentally. The paper should provide a more rigorous analysis of the overhead associated with maintaining and transmitting binary mask matrices, including the memory footprint and the computational cost of applying these masks during training and inference. A theoretical comparison of the computational cost of applying binary masks versus the attention-based pruning should be included.

3. The experiment part mainly focuses on accuracy, also lacks communication and storage results. How many computation and communication resources do ATTENDING and baselines require? Some results tables or figures should be included to illustrate such comparisons. This can help support what the authors claim. The paper needs to quantify the communication cost in terms of the number of bits transmitted per round and the storage cost in terms of the memory footprint of the models. The experiments should also include a breakdown of the computational cost, such as the wall-clock time or FLOPs, for both training and inference.

4. MNIST is used in two of the three Envs, but this dataset is too simple, and more complicated datasets are suggested to replace it. The use of MNIST, while common, does not adequately represent the complexities of real-world federated learning scenarios. More complex datasets with higher dimensionality and more diverse features, such as those found in image recognition or natural language processing tasks, should be included to better evaluate the robustness and scalability of ATTENDING.

5. ATTENDING is designed to address the data heterogeneity and system heterogeneity issues, as claimed by the authors. However, related experimental settings are not so detailed and heterogenous. Experiments should include more different alpha values regarding data heterogeneity and more different client configurations regarding system heterogeneity issues. The experiments should explore a wider range of alpha values to assess the method's sensitivity to varying degrees of data heterogeneity. Additionally, the system heterogeneity experiments should include variations in client computational resources, network bandwidth, and data availability, to better reflect real-world scenarios.

6. Figure 1 only compares ATTENDING with FedAvg; other baselines aiming for the data heterogeneity issue should also be included, and I believe such a comparison is more valuable and fair. The comparison should include other state-of-the-art federated learning algorithms that are specifically designed to address data heterogeneity, such as FedProx, FedMA, or SCAFFOLD. This would provide a more comprehensive evaluation of the proposed method's performance relative to existing approaches.

7. The limitations of ATTENDING should also be discussed in the paper, except for the advantages.

### Questions
What is the intuition to calculate the threshold in the current way, i.e., equation (7)?

How many computation and communication resources do ATTENDING and baselines require?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an attention-based pruning scheme to address the heterogeneity problems in FL. The attention scheme includes both channel attention and spatial attention to calculate a per-channel score for pruning, instead of using mask, which according to the authors, provides better robustness to performance permutation and reduced computation cost. The algorithm is implemented in FedML and compared with several SoTA methods showing reasonable benefits in terms of accuracy and cost.

### Strengths
The idea is somewhat novel in the sense that there aren't many pruning works in FL setups that employ attention-based scores, mostly would, like the authors mentioned, used masks. 
The writing and description are in general clear and easy to follow. 
The algorithm seems reasonable to function, as proved by the evaluation, which is quite sufficient. 
Some details are well explained, e.g., the effect of pruning ratios on different layers in Appendix H.

### Weaknesses
1. The paper's claim on the weakness of existing mask-based pruning approaches only apply to some of the existing works. Those with different approaches, e.g., using sign supermask instead of binary supermask, or, conduct pruning in the server instead in the clients [1], do not have the mentioned weakness yet seem to be overlooked in the work. 
2. The attention module seems quite similar, if not identical, to the classical CBAM [2], please clarify the innovation there.
3. In 3.3, the attention-matching mechanism rearranges the channels based on attention scores before aggregation. I might have misunderstood this, but wouldn't this operation cause chaos since the sequence of channels is now changed and thus channels learning different features are aggregated, e.g., those learing "edge" aggregated with those learning "texture"?

### Questions
As mentioned in the weakness, 
1. What's the advantage of this work over those pruning works using sign-supermask server-side pruning, e.g., [1]?
2. What's the innovation/difference between this attention module and CBAM's [2]?
3. Wouldn't the attention-matching mechanism cause chaos since the sequence of channels is now changed and thus channels learning different features are aggregated?

[1] HideNseek: Federated Lottery Ticket via Server-side Pruning and Sign Supermask, arXiv:2206.04385

[2] CBAM: Convolutional Block Attention Module, ECCV 2018

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To address challenges from system and data heterogeneity in FL, the paper proposes ATTENDING, a personalized attentive pruning-enabled federated learning approach. ATTENDING enhances learning performance using an attention module and generates personalized local models through attentive pruning. Evaluation results demonstrate that ATTENDING outperforms baselines by up to 11.3% and reduces average model footprints by 32%.

### Strengths
1. The paper introduces the attention mechanism,  incorporating spatial and channel attention to effectively addresses both heterogeneity in FL.
2. The paper clearly illustrate the proposed method, including the attention module design, the pruning algorithm, and the aggregation mechanism.
3. The paper conducts extensive experiments across various datasets and settings, demonstrating the robustness and scalability of ATTENDING.

### Weaknesses
1. To obtain the pruned client models, it is necessary for all client models to initially possess sufficient resources to run the original models. This requirement appears to contradict the system heterogeneity challenge that ATTENDING aims to address. Specifically, the initial full model requirement places a significant burden on resource-constrained clients, which is precisely the problem the paper seeks to solve. The paper does not adequately address how this initial overhead is mitigated or justified in the context of heterogeneous client capabilities.

2. In line 125, could the authors please clarify that what is the permutation invariance problem in Federated Learning (FL)? It is not immediately clear how this property affects the aggregation of local models in the context of the proposed method.

3. The proposed attention module is designed for each client individually; however, these attention modules do not seem to have any alignments. How can it be ensured that the attention module "is a key component to capture features on heterogeneous data," as stated in line 127? It seems that the attenion module can only extract features from the local dataset, rather than from the heterogeneous data in the FL training system. The paper lacks a clear explanation of how these independently trained attention modules contribute to a global understanding of heterogeneous data distributions.

4. In Figure 3, it appears that the channels are aggregated based on the scores rather than their original positions in each layer. Could this have any impact, considering that channel weights from different positions may extract different features from the images? The paper does not discuss the potential consequences of this reordering on feature representation and model performance, particularly if spatial relationships between channels are important.

5. In line 321, does this imply that only the first round involves pruning the client models? How can it be ensured that the initial model with the attention module can extract appropriate attentions when the model weights are initialized randomly? Additionally, what would be the results if the channels with the highest scores were pruned, or if pruning were done randomly? The paper does not provide a rationale for using only the first round for pruning, nor does it explore the impact of different pruning strategies.

6. It would be beneficial to include additional results that why ATTENDING performs better , such as the distribution of attention values for different channels and the effect of different attention scores. The paper lacks a detailed analysis of the attention mechanism's behavior and its contribution to performance gains.

7. Could ATTENDING be applied in Transformers? If so, what modifications would be necessary to adapt the approach for use with Transformers? The paper does not discuss the applicability of the proposed method to other architectures beyond CNNs, which limits the generalizability of the approach.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
