# Mitigating Backdoor Attacks in Federated Learning through Noise-Guided Aggregation

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Backdoor attack in federated learning (FL) has attracted much attention in the literature due to its destructive power. Advanced backdoor defense methods mainly involve modifying the server's aggregation rule to filter out malicious models through some pre-defined metrics. However, calculating these metrics involves malicious models, leading to biased metrics and defense failure. Therefore, a straightforward approach is to design a metric not tainted by malicious models. For instance, if the server has private data to evaluate model performance, then model performance would be an effective metric for backdoor defense. However, directly introducing data-related information may cause privacy issues, we thus propose $\textit{n}$oise-gu$\textit{i}$ded $\textit{r}$obust $\textit{a}$ggregation, Nira, which trains and evaluates models using pure noise. Specifically, Nira constructs a noise dataset and shares it across the server and clients, enabling clients to train their models over the shared noise and local data. To ensure the generalizability of models trained on noise, Nira encourages clients to align their local data to shared noise in the representation space. Consequently, Nira can filter out models prior to aggregation according to the model performance, e.g., prediction accuracy on noise. We conduct extensive experiments to verify the effectiveness of Nira against backdoor attacks, demonstrating the superiority over previous works by a substantial margin.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a novel approach utilizing generated (surrogate) dataset for mitigating the backdoor attacks in federated learning.  Domain adaption is performed to align the distribution between the surrogate and original dataset. Experimental results demonstrate the effectiveness of the approach under various settings.

### Strengths
1. The proposed approach is technically novel and sound.
2. The paper is well-written and easy to follow in general.
3. Experimental evaluations are comprehensive, covering a broad aspect of factors and baseline methods.

### Weaknesses
1. The proposed approach is based on strong assumptions that the malicious attackers follow the proposed protocol, i.e. training both surrogate and local dataset with the proposed objectives exactly or adaptively (in Adaptive Attack Scenario). However, the introduction of surrogate data may easily prompt the malicious attackers to inject backdoor triggers and objectives to the surrogate dataset as well. Have the author considered these scenarios?

2. The paper claims that "We point out that metrics used for backdoor defense can be tainted by malicious models, leading to the failure of existing approaches." as its contribution, however, it is not convincing that the proposed method adequately addressed this problem since 1) the metric that server used for filtering out malicious attackers appear to use a distance outliner (eq.6) and thresholds, which may be also tainted if the majority are attackers. 2) experimental results are limited to small ratio of clients (12/50) and poisons (20%).

3. Missing Details. The design of the filtering thresholds is crucial to the proposed method but is not explained well. Why they vary with time in experiments? Are there any insights on how to adjust them systematically? In 3.3, what does "features of the model" mean and how to determine the value of b? In Table 1, the definition of "Acc" , "Atk Rate" and "Main Acc" are not explicitly explained and therefore confusing. 

4. The experiments are conducted on relatively limited settings, i.e., only one triggered-based backdoor attack is considered, and small dataset.

### Questions
1. What is the ratio of the number of surrogate data and real data for each clients? How will this ratio affect the performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method to defend against backdoor attacks in federated learning. A surrogate dataset is generated based on Gaussian noise to help detect malicious clients. The surrogate dataset will be shared to clients and the clients will train models based on both local data and the surrogate data to get models that perform well on both local data and the surrogate data. Malicious clients are detected based on measuring accuracy and feature distances of local models on the surrogate data. Experiments on vision data show that the proposed method performs well under certain scenarios.

### Strengths
Strengths:

- The proposed method does not need the assumption that the majority of the clients are benign. It also does not need access to an auxiliary dataset which some previous methods require.

- Experiments show that the proposed method performs well on three vision datasets.

- The paper is clearly written with several graphs illustrating the idea and framework.

- Backdoor attack is an important security issue in the field of federated learning.

### Weaknesses
Weaknesses:

- The paper claims that it is not majority-based defense. Based on the description, it seems right. However, why not evaluate the claim with experiments? There are 50 clients in the experiment, and the number of attackers ranges from 0 to 12, which corresponds to 0% to 24% of malicious clients, not exceeding 50%. It would be more convincing to show the method's robustness with a higher proportion of malicious clients, such as 60% or 70%, to truly demonstrate its non-reliance on a majority of benign clients.

- The thresholds of filtering clients seem to be important hyper-parameters. In the experimental part, it is explained that the accuracy threshold increases as the training rounds progress and the distance threshold decreases. The specific thresholds in different rounds are also given. However, details of threshold selection are not included in the main paper. In the appendix, it says that "train a few rounds on a small number of identified benign clients". If the thresholds are selected this way, knowing some identified benign clients is an important assumption of the method that should be mentioned in the main paper. This reliance on pre-identified benign clients for threshold tuning introduces a potential vulnerability if these clients are compromised or misidentified.

- This method seems to be limited to vision data. Federated learning can also be applied to other types of data, such as NLP, graph. How could the method generalize to other types of data? The paper does not discuss how the surrogate dataset generation and the feature distance calculation would be adapted for non-image data. The reliance on pixel-based feature distances may not be directly applicable to sequence data or graph-structured data, which require different notions of feature representation and similarity.

### Questions
See previous part.

### Soundness
3 good

### Presentation
3 good

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
This paper proposes Nira, a backdoor defense for federated learning based on the idea of noise-guided robust aggregation.

### Strengths
* The proposed noise-guided defense is novel among the defense literature.

* Unlike many existing defenses, the method does not require a surrogate dataset (but only noise) in filtering out the poisoned model from the aggregation phase.

* The benign accuracy is increased due to alignment with noise, while for most existing defenses, the accuracy is suffered.

### Weaknesses
 * The reason for the effectiveness of noise alignment and filtering lacks clarity. It remains uncertain why attackers struggle to align their data with noise. It is advisable for the authors to conduct a toy experiment to illustrate this point. For instance, in a scenario involving two clients, we could fix the benign data of both clients to be the same while introducing additional poisoned samples to the first client. Performing one epoch of noise alignment with these two clients and comparing their accuracy on noise samples would shed light on this issue. 


* The provided rationale for Nira's ability to defend against adaptive attacks is not clear too. The authors shows that Nira is robust to hte adaptive attack where attackers split their poisoned dataset into poisoned and benign segments, aligning only the surrogate samples with the data within the benign segments. The reasons given are that 1) "scale-up operation on the model weights has its impact" and 2) poisoned samples in the cross-entropy loss lead to poor alignment. It is suggested that the authors i) disable the scale-up operation, and ii) in the absence of the scale-up operation, substantiate the second reason with experimental results. This is important because it might not be reasonable to assume that attackers cannot produce an over-parameterized model that can simultaneously minimize the alignment loss and the backdoor cross-entropy loss, as these objectives are not inherently contradictory.

* The statement that "calculating these metrics involves malicious models, leading to biased metrics and defense failure" suggests that involving malicious models in metric calculation introduces bias and can result in defense failure. However, this statement needs further clarification, and it might be beneficial for the authors to elaborate on the specific reasons why using malicious models for metric calculation could lead to biased results and ultimately undermine the defense. Additionally, it's worth addressing why Nira's use of malicious models in a similar context does not result in failure.

In Table 2, the impact of poisoning ratio on benign accuracy appears significant, which is not a usual case for backdoor attack. To better understand this phenomenon, it would be helpful to see the results for scenarios with only one attacker (attacker number = 1) and no attackers (attacker number = 0) under different poisoning ratios for both FedAvg and Nira. This would provide a clearer picture of the algorithm's performance under varying conditions.

It is suggested to provide experimental results when full client participation is employed, without client selection. The randomness associated with client selection could indeed influence training results, particularly affecting the ASR. Demonstrating how the approach performs under full participation conditions would offer insights into its stability.

Clarification on the scale factor in replacement attacks is necessary. It would also be valuable to determine whether Nira remains effective when the scaling-up operation is disabled. Note that the scaling-up operation may not be essential for conducting backdoor attacks.

### Questions
The statement that "calculating these metrics involves malicious models, leading to biased metrics and defense failure" suggests that involving malicious models in metric calculation introduces bias and can result in defense failure. However, this statement needs further clarification, and it might be beneficial for the authors to elaborate on the specific reasons why using malicious models for metric calculation could lead to biased results and ultimately undermine the defense. Additionally, it's worth addressing why Nira's use of malicious models in a similar context does not result in failure.

In Table 2, the impact of poisoning ratio on benign accuracy appears significant, which is not a usual case for backdoor attack. To better understand this phenomenon, it would be helpful to see the results for scenarios with only one attacker (attacker number = 1) and no attackers (attacker number = 0) under different poisoning ratios for both FedAvg and Nira. This would provide a clearer picture of the algorithm's performance under varying conditions.

It is suggested to provide experimental results when full client participation is employed, without client selection. The randomness associated with client selection could indeed influence training results, particularly affecting the ASR. Demonstrating how the approach performs under full participation conditions would offer insights into its stability.

Clarification on the scale factor in replacement attacks is necessary. It would also be valuable to determine whether Nira remains effective when the scaling-up operation is disabled. Note that the scaling-up operation may not be essential for conducting backdoor attacks.

I would consider adjusting my score based on the authors rebuttal, and will actively participate in it.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
