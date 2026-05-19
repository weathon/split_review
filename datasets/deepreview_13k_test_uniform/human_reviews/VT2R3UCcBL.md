# Efficient Privacy-Preserving Federated Learning With Selective Parameter Encryption

- Decision: Reject
- Scores: 8, 8, 6, 5

## Abstract
Federated learning trains machine learning models on distributed devices by aggregating local model updates instead of local data. However, privacy concerns arise as aggregating local model updates on the server may reveal sensitive personal information by inversion attacks. Privacy-preserving methods, such as homomorphic encryption (HE), then become necessary for FL training. Despite HE's privacy advantages, its applications suffer from impractical overheads, especially for foundation models. In this paper, we present the first practical privacy-preserving federated learning work with efficient HE-based secure model aggregation. Our approach proposes to selectively encrypt sensitive parameters, significantly reducing both computation and communication overheads during training while providing quantifiable privacy guarantee. Our optimization shows considerable overhead reduction, particularly for large foundation models (e.g. 
100x reduction for GPT-2), demonstrating the potential for scalable HE-based FL deployment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper tackles the significant computational and communication overhead associated with using Homomorphic Encryption (HE) to protect personal privacy in federated learning, an issue that has become even more critical with the rise of foundational models. To address this, the authors propose a method that selectively encrypts sensitive parameters, thereby markedly reducing computation and communication costs during training while providing quantifiable privacy guarantees. The paper is presented clearly and concisely, with comprehensive experiments that thoroughly evaluate the proposed method, making it a strong and valuable contribution to the field.

### Strengths
1. The paper is written with notable clarity and conciseness, with figures and tables placed effectively to enhance readability and comprehension.
2. The theoretical proofs and experiments are comprehensive, addressing privacy through quantifiable discussions on selective parameter encryption, demonstrating gains in computational and communication efficiency, and validating model effectiveness.
3. The content is well-structured, effectively conveying the authors’ intended contributions and addressing most anticipated questions or concerns a reader might have.

### Weaknesses
The chosen base model, GPT-2, is relatively small, which may limit the generalizability of the results to larger foundational models. Since the paper aims to demonstrate the feasibility of implementing privacy-preserving techniques in foundational models, GPT-2 may not be sufficiently representative of these larger-scale models. I suggest testing the proposed method on a more current, widely used model such as the latest LLaMA 3.2, to provide stronger evidence of its scalability and applicability to modern foundational models.

### Questions
Have the authors considered testing the proposed method on larger foundational models? Given that GPT-2 is relatively small, it would be helpful to understand whether the method’s efficiency and computational and communication cost reductions hold at scale with more recent models, such as LLaMA 3.2 or similar. Expanding the experiments to include such models could strengthen the paper’s claims about feasibility for broader foundational model applications.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a privacy-preserving federated learning framework that leverages selective parameter encryption to address the computational and communication overhead associated with large-scale models. By encrypting only a subset of parameters, the proposed method aims to achieve a balance between privacy preservation and efficiency. The authors provide evidence that their approach significantly reduces computational and communication costs while maintaining privacy guarantees. The empirical results further support the efficacy of the method across models of varying scales, with especially pronounced benefits observed for large models.

### Strengths
The paper effectively integrates theoretical analysis with empirical validation, which strengthens the credibility of the proposed approach and enhances the robustness of the findings.

The proposed method demonstrates substantial reductions in encryption and communication overhead, a particularly advantageous outcome for the scalability of large models.

### Weaknesses
Limited Comparative Analysis: The manuscript lacks sufficient depth in referencing and comparing existing selective parameter encryption techniques. While some methods are briefly addressed in Table 9, a more thorough and nuanced comparative analysis is necessary to clearly establish the novelty and advantages of the proposed approach.

Lack of Analysis on Parameter Selection Overhead: The introduction of a parameter selection step in the encryption process is not accompanied by a detailed evaluation of the associated overhead. This omission leaves the cost-effectiveness assessment incomplete, particularly regarding practical implementation.

### Questions
Comparison with Existing Methods: The manuscript would benefit from a more exhaustive comparative analysis of existing selective parameter encryption approaches. This analysis should elucidate the specific advantages of the proposed method, particularly with respect to scalability and efficiency in practical deployment scenarios. For example, some methods simultaneously employ homomorphic encryption for certain parameters while using differential privacy for others, thereby enhancing privacy protection. A detailed comparison of these hybrid approaches, including their respective advantages and trade-offs, would strengthen the overall contribution.

Parameter Selection Overhead: It is crucial to quantify the overhead introduced by the parameter selection mechanism. A detailed examination of this overhead would provide a more comprehensive understanding of the practical trade-offs and facilitate a balanced evaluation of the approach's feasibility.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an efficient privacy-protecting federated learning framework that protects machine learning models trained on distributed devices with selective parameter encryption to prevent the disclosure of sensitive personal information through inversion attacks when servers are aggregated.

### Strengths
1. A selective parameter encryption method is proposed via encrypting only the most privacy-sensitive parameters, which can reduce the costs of HE-based Federated Learning.
2. A theoretical framework and sufficient experiments are proposed to support their conclusion.

### Weaknesses
1. The article does not fully address the risks posed by malicious clients during the negotiation of homomorphic encryption (HE) keys. While the authors propose using a threshold version to mitigate collusion risks, there remains a significant motivation for colluding clients to target a specific client, particularly in scenarios with a small number of clients.
2. The method for generating mask maps may lead to inconsistencies in a heterogeneous environment. If clients use the same mask map, it could compromise privacy, especially when sensitive parameters differ across clients.
3. The use of the Hessian matrix to define privacy sensitivity lacks clarity. The correlation between gradient changes and privacy leakage is not sufficiently supported, particularly regarding the behavior of gradients at different training stages.
4. There is a notable lack of empirical evidence supporting the fitting of the log-normal mixture distribution model to various parameter models.

### Questions
1. How to mitigate the risk of colluded clients stealing a targeted client’s parameters, especially since this is a common issue faced by existing HE-based federated learning solutions?
2. Are mask maps unified across clients after aggregation? If they are, how do you handle differences in sensitive parameters? If not, what happens to the other parameters post-aggregation?
3. How do gradient changes relate to privacy risk? Could you provide evidence that gradient changes decrease as the model converges, affecting privacy risk?
4. What additional evidence can you provide to support the fitting of the log-normal mixture distribution model to different parameter models?

### Soundness
3

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
The paper addresses the challenge of high overheads associated with using homomorphic encryption (HE) in federated learning (FL) to protect against privacy attacks such as gradient inversion. Traditional HE methods, while providing strong privacy guarantees, are computationally intensive and not scalable for large models like GPT-2.

To tackle this issue, the authors propose an privacy-preserving FL framework called Selective Parameter Encryption. The key idea is to encrypt only the most privacy-sensitive parameters of local models rather than encrypting the entire model.

### Strengths
The originality of this work lies in its combination of selective encryption with homomorphic encryption in the context of federated learning.

### Weaknesses
Although the paper proposes an method to reduce overhead in privacy-preserving federated learning through Selective Parameter Encryption, it needs to deepen its theoretical analysis and experimental validation. Specifically, it should provide a detailed explanation of how the assumption that model parameters follow a log-normal mixture distribution is utilized in the privacy quantification framework. Additionally, offering mathematical comparisons with differential privacy would substantiate claims of superiority. The paper should include simulations of privacy attacks, such as gradient inversion attacks, to empirically demonstrate the method's effectiveness. Moreover, an in-depth discussion of potential vulnerabilities introduced by partial encryption is necessary, along with a formal security analysis to ensure the method's robustness against sophisticated attacks.

### Questions
1. The theoretical framework used for privatization has not been fully developed in the paper. The author mentioned that most existing models follow the mixed distribution of normal state, but did not explain in detail how this assumptions were integrated into their privacy analysis.

2. The thesis asserted that the method is largely better than differential privacy. However, there is no comparison of mathematics or empirical to verify this statement. It is necessary to comprehensively analyze the privacy-effective balance of two methods.

3. In order to prove the effectiveness of the method in defense privacy attacks, the author should include experiments to simulate the opponent's attempt to rebuild the training data from the model update. The lack of such experiments has weakened the claim to enhance privacy.

4. Reducing the parameters of encryption may expose the unblocked parameter to the new type of attack. The author shall discuss the potential vulnerabilities that selective encryption may be introduced and propose to ease the strategy.

5. The paper should provide formal security analysis to ensure that only the encrypted parameters will not weaken the overall security of the model aggregation process. Without this analysis, it is difficult to evaluate the steadyness of the method mentioned to fight complex attacks.

6. In Section 3.2, the description of the threat model is relatively simple. It should be more detailed to explain the attacker's ability, possible attack vector, and why you choose specific security assumptions.

7. Although the use of Palisade and Tenseal libraries is mentioned, there is no explanation of specific versions and configurations, and why Palisade is selected as the main evaluation object.

8. Although selective encryption can effectively defend anti -discrimination attacks, it lacks a detailed description of attack experiments. For example, the attacker's ability assumptions, the details of the attack method, and the statistical verification of the defense effect.

9. It may not be comprehensive enough by reducing attack scores to evaluate privacy protection. Based on the theoretical framework of differential privacy to discuss the possibility and risks of privacy leakage.

10. It is necessary to clarify whether the attacker's knowledge and ability, and whether the defense effect of selective encryption is still effective under a stronger attack model.

11. In "A.11 Proof of Base Full Encryption Protocol", the author mentioned that the privacy of the basic agreement was mentioned, but the proof provided was too brief. Lack of detailed steps and logical derivation, it is difficult to persuade readers.

12. In "A.12 Quantifying Negligible Privacy Value in Full Encryption", the author tries to quantify the privacy budget under the condition of quantification, but the derivation process is not clear enough. It is necessary to provide more detailed calculation steps and explain the basis of the selection of each parameter.

### Soundness
2

### Presentation
3

### Contribution
2
