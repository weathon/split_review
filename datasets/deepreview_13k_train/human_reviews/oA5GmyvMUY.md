# Robust Federated Learning Frameworks Guarding Against Data Flipping Threats for Autonomous Vehicles

- Decision: Reject
- Scores: 3, 5, 3, 3, 1, 3, 3

## Abstract
Federated Learning (FL) has become an established technique to facilitate privacy-preserving collaborative training across a multitude of clients. The ability to achieve collaborative learning from multiple parties containing an extensive volume of data while providing the essence of data privacy made it an attractive solution to address numerous challenges in sensitive data-driven fields such as autonomous vehicles (AVs). However, its decentralized nature exposes it to security threats, such as evasion and data poisoning attacks, where malicious participants can compromise training data. This paper addresses the challenge of defending federated learning systems against data poisoning attacks specifically focusing on data-flipping techniques in AVs by proposing a novel defense mechanism that combines anomaly detection with robust aggregation techniques. Our approach employs statistical outlier detection and model-based consistency checks to filter out compromised updates before they affect the global model. Experiments on benchmark datasets show that our method significantly enhances robustness by preventing nearly 15\% of accuracy drop for our global model when confronted with a malicious participant and reduction the the attack success rate even when dealing with 20\% of poisoning level. These findings provide a comprehensive solution to strengthen FL systems against adversarial threats.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes new defense method on against data poisoning attacks in federated learning, especially for image classification models in autonomous vehicles. The method uses Principal Component Analysis (PCA) and Multi-class Support Vector Machine (SVM) classifiers together to offer a strong way to defend against label flipping attacks in federated learning. Experiments show the performance.

### Strengths
1. Again data poisoning attack in FL and Autonomous Vehicle is important.
2. The proposed method (PCA+SVM) can be used for detecting outliers.
3. Experiments are provided.

### Weaknesses
1. PCA+SVM has been well studied and has been extended to FL settings. The contribution of the paper is unclear.
2. Experiments do not have comparison methods.
3. It does not have experiments on simulated autonomous vehicles.

### Questions
typos:
1. Page 2, line 87 "labels.,Furthermore,", "the robustness,of the", line 90 "high classification performance..."

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a novel defense strategy that combines PCA and SVM to detect and mitigate these attacks. This approach aims to filter out malicious updates by identifying statistical anomalies in model updates before they impact the global model. Their experiments, conducted using various datasets, demonstrate that this defense mechanism successfully maintains model accuracy and integrity, even with significant data poisoning levels.

### Strengths
By focusing on label-flipping in AVs, this paper addresses a specific and underexplored threat in FL. The experimental design is robust, testing on multiple datasets and using meaningful metrics to demonstrate the effectiveness of the defense. Clear explanations of PCA and SVM integration, along with structured result presentation and well-contextualized related work, enhance the paper’s readability and situate its contributions within the broader FL literature.

### Weaknesses
The contributions of the paper are not solid enough, and the challenges are not adequately highlighted. It appears that the authors merely combine existing technologies into different scenarios.

On one hand, while the authors use a label-flipping attack to implement targeted data poisoning in federated learning (FL), they do not clarify how this attack differs from existing ones or specify the challenges it poses in the FL context. Specifically, the paper lacks a discussion on how the non-IID nature of federated data impacts the effectiveness of label-flipping attacks compared to attacks in centralized settings. The authors should elaborate on how the distribution of poisoned data across different clients affects the global model convergence and the overall attack success rate. Furthermore, the paper does not explore the potential for adaptive attacks that could exploit the federated learning process itself, such as adjusting the attack strategy based on the observed model updates.

On the other hand, in their proposed defense mechanism, they set a detection agent in each autonomous vehicle (AV) to filter out attacking data. However, this defense mechanism is independent of the federated learning setting, meaning that existing defense strategies could be directly applied here for protection. The paper does not discuss the specific challenges of applying anomaly detection and robust aggregation in the FL context, such as the need for decentralized anomaly detection or the impact of communication constraints on the aggregation process. The authors should also address the computational overhead of running PCA and SVM on each device, especially in resource-constrained AVs, and how this overhead scales with the number of clients.

The relevance to AVs is not clear. It is difficult to find the connection between the proposals and AVs, despite the authors providing Figure 1 to illustrate the FL for label-flipping attacks on AVs. The paper does not detail the specific types of data used in the AV context (e.g., sensor data, camera images) and how label-flipping attacks would manifest in these data types. For example, how would flipping labels in sensor data impact the AV's perception and decision-making? The paper needs to provide a more concrete explanation of how the proposed attack and defense mechanisms are tailored to the unique challenges of AVs.

Additionally, no comparisons are provided. A comparison of attacks and defenses should be included to strengthen the contributions. Without this, it is challenging to assess the effectiveness of the proposed attack and defense mechanisms. The paper should include a comparison with other state-of-the-art poisoning attacks and defense mechanisms in the federated learning setting. This comparison should include metrics such as attack success rate, defense accuracy, and computational cost. Without such comparisons, it is difficult to evaluate the novelty and effectiveness of the proposed approach.

Finally, there are too many unexpected grammar issues and typos that make the current version far from acceptable.

### Questions
1) Have you considered methods to reduce the computational burden of PCA-SVM for a larger number of participants? Could dimensionality reduction or distributed processing techniques make scaling feasible?

2) How do you anticipate that the PCA-SVM method would perform against other common attacks in FL, such as backdoor or gradient leakage attacks?

3) How does the PCA-SVM mechanism perform when faced with non-IID data, which is common in real federated learning applications?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to resist data poisoning attacks (in particular data-flipping) faced by autonomous vehicles (AVs) in the federated learning (FL) setting. The authors propose a novel defense mechanism that combines anomaly detection with robust aggregation techniques. They employ statistical outlier detection and model-based consistency checks to filter out compromised updates before they affect the global model.

### Strengths
1. Interesting to explore the poisoning attacks in the FL setting, for ensuring the security of AVs.
2. The logic of the proposal is easy to follow, although there are a lots of grammar issues and typos.
3. Experiment results to some extent support their conclusion.

### Weaknesses
 - Techniques: 
 1. Label Flippinp: Label flipping is the easiest data poisoning, there are many poisoning attacks like backdoor or model poisoning attack, this threat seems to be quite weak as of now. The paper does not discuss the limitations of focusing solely on label flipping attacks, particularly in the context of autonomous vehicles where more sophisticated attacks could be deployed. For example, adversarial attacks that manipulate sensor data to cause misclassification, or model poisoning attacks that directly corrupt the global model, pose significant threats and should be considered.
 2. No Baselines for a comparative study
 3. Insufficient experiments
No ablation studies and more settings like Non-IID.

- Writing: 
 1. The writing needs thorough revision, and the current form read more like an experimental report.  
 2. Please split the experiment and proposed framework.
 3. Don't introduce too much basic knowledge in your proposed method.
 4. Please give a formalized/mathematical description on your method, it is unlikely to understand the proposed method in detail from pure text descriptions.
 5. Some statements are unclear. What is the k in 191?

### Questions
1. What challenges arise in applying this label-flipping attack and its corresponding defense in the federated learning setting?
2. What advantages do the proposed attack and defense offer over existing methods?

### Soundness
2

### Presentation
1

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
This paper proposes a defense for Federated Learning (FL) against data poisoning attacks, especially in autonomous vehicles. The authors use PCA and SVM to detect label flipping attacks and try to build a robust FL framework.

### Strengths
+ The problem worths detailed investigation. 

+ The structure of the draft is good.

### Weaknesses
The paper has many typos.

Both label-flipping attacks and outlier detection methods have been well-studied in federated learning. See, for example, "Defending against the Label-flipping Attack in Federated Learning" by Najeeb Moharram Jebreel et al. The paper does not seem to propose anything new.

The FL setting and the threat model are poorly described and involve multiple unreasonable assumptions. What do you mean by training FL models without the adversarial settings? How can you ensure that there is no adversarial device during training? Also, what is the testing dataset D_test? Where does it come from, and why is it disjoint from the participants' datasets? In FL, the data is typically provided by participants.

The evaluation considers a very small setting with three devices and iid data distribution. The results are far from being convincing.

### Questions
Please check the weakness part.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper evaluates a label-flipping attack in federated learning and proposes a simple outlier detection approach using PCA and SVM to filter out compromised updates.

### Strengths
I cannot identify any strength of the paper.

### Weaknesses
Weaknesses:
- The novelty of this paper needs to be further improved.
- The experimental results of this paper are not convincing.
- More poisoning attack baselines and advanced defenses need to be included.
- The writing quality of this paper needs another round of polishing.

### Questions
Please see the discussion on weaknesses above.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a defense against label flipping attacks in federated learning in the context of applications for autonomous vehicles. The defense combines anomaly detection and robust aggregation to mitigate the effect of potential attacks by filtering out malicious model updates. The experimental evaluation against label flipping attacks in benchmark datasets show that the method is capable of mitigating the effect of the attack.

### Strengths
+ The paper proposes a defense against label flipping attacks in the context of applications for autonomous vehicles, which is a relevant challenge for the security and robustness of distributed learning techniques such as federated learning. 
+ The authors present a novel defense integrating PCA and MCSVM for detecting malicious label flipping attacks in federated learning, which effectively enhances the robustness of the algorithm during training against this type of attack.

### Weaknesses
+ The novelty and the contribution of the method compared to existing defenses in the research literature is unclear. Many defenses are already capable of defending against the type of attacks explored in the paper. In this sense, the authors did not discuss these aspects in the paper and did not compare against any other competing method in the experiments. 
+ The settings for the experiments are relatively trivial. The authors just tested in an environment with IID data partitions and with a very reduced number of participants (just 3). As mentioned before, there is no comparison with other existing methods in the research literature. 
+ Although the paper aims to focus on autonomous vehicle applications, the paper really restricts to computer vision applications. It would be interesting to analyze more applications typical for autonomous vehicles (e.g., LiDAR, sensing, etc.). The way the paper is presented differs little from the majority of the papers in this area, which often consider similar computer vision benchmarks (e.g., CIFAR) for their experiments.

### Questions
+ What is the threat model assumed by the authors for the paper? What are the capabilities that the adversary has to compromise the system? 
+ How this paper advances the state of the art compared to other competing methods in the research literature on robust federated learning?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 7

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a defense mechanism for FL against data poisoning attacks, specifically focusing on data-flipping attacks in AVs. The approach combines anomaly detection with robust aggregation techniques, using statistical outlier detection and model consistency checks to filter out compromised updates. Experimental results on benchmark datasets show that the method effectively improves FL robustness, preventing nearly a 15% accuracy drop in the global model and reducing the attack success rate, even at a 20% poisoning level. This solution enhances FL system security against adversarial threats in sensitive data-driven fields.

### Strengths
Strengths:
+ This work offers a defense mechanism for FL against data poisoning attacks, specifically focusing on data-flipping attacks in AVs.

### Weaknesses
Weaknesses:
- The novelty of this paper needs to be further improved.
- The experimental results of this paper are not convincing.
- More poisoning attack baselines and advanced defenses need to be included.
- The writing quality of this paper needs another round of polishing.

### Questions
Comments:

- The novelty of this paper needs to be further strengthened. Currently, it appears to combine existing techniques—namely anomaly detection and robust aggregation—without a clear distinction from prior work. The authors should further elaborate on the differences and connections between their approach and existing methods to better demonstrate its unique contributions.

- The paper should include more advanced poisoning attack baselines. The experimental results do not compare against any state-of-the-art poisoning attack baselines, which limits the ability to highlight the superiority of the proposed defense mechanism.

- The paper also requires more advanced defense mechanism comparisons. To comprehensively evaluate performance, the proposed defense should be fairly compared with existing advanced defenses. Additionally, the authors should explain why their approach demonstrates superior performance relative to other defenses.

- Finally, the paper should incorporate more extensive experimental evaluations. The authors currently present only one set of experiments, which is insufficient for a convincing analysis. To provide a thorough evaluation, additional experiments are recommended.

### Soundness
1

### Presentation
1

### Contribution
2
