# Unlearning Mapping Attack: Exposing Hidden Vulnerabilities in Machine Unlearning

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 6, 5, 5

## Abstract
As machine learning becomes increasingly data-dependent, concerns over privacy and content regulation among data owners have intensified. Machine Unlearning has emerged as a promising solution, allowing for the removal of specific data from pre-trained systems to protect user privacy and regulate information. Existing research on Machine Unlearning has shown considerable success in eliminating the influence of certain data while preserving model performance. However, the resilience of Machine Unlearning to malicious attacks has not been thoroughly examined. In this paper, we investigate the hidden vulnerabilities within current Machine Unlearning techniques. We propose a novel adversarial attack, the Unlearning Mapping Attack (UMA), capable of undermining the unlearning process without altering its procedures. Through experiments on both generative and discriminative tasks, we demonstrate the susceptibility of existing unlearning techniques to UMA. These findings highlight the need to reassess unlearning objectives across various tasks, prompting the introduction of a Robust Unlearning standard that prioritizes protection against adversarial threats. Our extensive studies show the successful adaptation of current unlearning methods to this robust framework. The Python implementation will be made publicly available upon acceptance of the paper.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel adversarial attack, the Unlearning Mapping Attack (UMA), which exposes vulnerabilities in current machine unlearning techniques. Machine unlearning aims to remove specific data from trained models to ensure privacy and compliance with regulations. However, UMA demonstrates that even when data is supposedly "forgotten," it can be reconstructed by leveraging information from the model before and after unlearning. The study evaluates UMA on both generative and discriminative tasks, showing that existing unlearning methods are vulnerable to such attacks without any alteration to the unlearning process itself. The authors propose a need for "Robust Unlearning," which strengthens models against adversarial reconstruction. Experimental results highlight UMA's effectiveness in recovering forgotten data, underscoring the importance of reassessing current unlearning techniques to prioritize resistance against sophisticated attacks.

### Strengths
The paper’s strengths lie in its introduction of the Unlearning Mapping Attack (UMA), a novel strategy that uncovers vulnerabilities in current machine unlearning methods without altering the unlearning process. Through comprehensive testing on both generative and discriminative tasks, UMA demonstrates broad applicability and highlights the critical need for “Robust Unlearning” standards to defend against adversarial attacks. By assuming realistic attack conditions, the study provides valuable insights into practical security implications, contributing to the advancement of secure and resilient unlearning techniques.

### Weaknesses
Weakness 1: This method does not assess the resistance of existing defenses against poisoning samples.
Weakness 2: The format discrepancy between the attack output and input may allow service providers to plausibly deny the relationship between them. Simple metrics, such as L1 distance, could easily indicate that the input and output are not the same. 
Weakness 3: The relationship between the poisoning rate and the amount of data reconstructed remains unexplored.

### Questions
1 .Can sample-based defenses effectively mitigate the attack?
2. What is the relationship between the poisoning rate and data reconstruction after unlearning?
3. What is the L1 norm difference between the input and output?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an attack strategy in the context of machine unlearning. The attack involves introducing a minimal perturbation to a sample that has been unlearned, during inference. This perturbation is designed to make the model's prediction on the perturbed, unlearned sample closely resemble the prediction it would have made prior to the unlearning process. The paper first presents several propositions regarding the attack, followed by an optimization step to obtain such malicious perturbations. Several experiments are conducted on both discriminative and generative models.

### Strengths
1. The paper is clear and easy to follow. 

2. The paper utilizes several popular unlearning methods to demonstrate the efficacy of the proposed attack method.

### Weaknesses
1. This paper's contribution is somewhat limited. The type of attack that aims to recover unlearned information after the unlearning phase has been recently explored in both large language models (LLMs) and the field of generative models. This paper proposes such unlearning attacks on discriminative classification tasks and generative tasks. However, for discriminative classification tasks, the attack is relatively straightforward. Moreover, the paper does not discuss related work or provide comparisons with existing post-unlearning attacks on generative models, such as diffusion models.

2. The definition of unlearning requires clarification. The statement "a discriminative model must no longer recognize the unlearned samples" along with equations (1) and (2) seems to be weird. Most existing definitions of machine unlearning involve the retrained model (though there is some debate over this), which does not imply that the unlearned model must no longer recognize the unlearned samples.

3. The propositions presented in the paper are not formally stated. For instance, Proposition 2 suggests that a universal perturbation $\delta$ applies to all unlearned samples, which does not seem to be the case according to the paper.

4. Figure 1 is somewhat ambiguous. At first glance, it might be misunderstood that the perturbation is added before the training phase, rather than after the unlearning phase.

5. The paper lacks ablation studies, and none of the experiments report standard deviations.

### Questions
1. Please explain why the definitions of unlearning attacks for discriminative and generative models differ in terms of $\delta$ and $x+\delta$.

2. Black-box transfer experiments would be interesting to demonstrate the efficacy of the proposed attack.

3. Which Membership Inference Attack (MIA) method do you choose for the experiments?

4. In your experiments, do you employ data augmentation?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the Unlearning Mapping Attack (UMA), a novel post-unlearning adversarial attack designed to expose vulnerabilities in existing machine unlearning (MUL) methods. The authors demonstrate that UMA can undermine current MUL techniques without altering the unlearning procedure itself, reintroducing forgotten information. The study highlights the insufficiencies of existing unlearning strategies in safeguarding models against such attacks, especially when adversaries have access to both pre- and post-unlearning models. Experiments on both generative and discriminative tasks reveal how UMA can retrieve forgotten data, emphasizing the need for a more robust definition of machine unlearning.

### Strengths
1. Novel Attack Strategy: The introduction of UMA fills a gap in machine unlearning research by focusing on post-unlearning attacks that expose hidden vulnerabilities. Unlike previous work that manipulates the unlearning process or data, UMA operates post-hoc, revealing a new class of threats.

2. Comprehensive Evaluation: The experiments span multiple datasets (CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1k) and tasks (discriminative and generative). This comprehensive evaluation strengthens the generality of the findings.

3. Focus on Robustness: The authors highlight the need for a new standard of Robust Unlearning, which ensures that models remain secure against adversarial inputs post-unlearning. This is a valuable contribution to both academia and industry, as it pushes for higher standards of security in privacy-preserving ML.

### Weaknesses
1. Limited Practical Mitigation Discussion: While the paper demonstrates the UMA vulnerability well, the section on mitigating this attack could be further expanded. Though adversarial training is explored, the feasibility of integrating robust unlearning techniques into various MUL methods needs more discussion, especially for large-scale systems. The paper lacks a detailed analysis of the computational costs associated with adversarial training, such as the number of iterations required for convergence and the memory footprint of storing adversarial examples. Furthermore, the discussion should include the impact of these costs on the overall scalability of the proposed unlearning framework, especially when dealing with high-dimensional data and complex models.

2. Assumptions on Attacker's Knowledge: The UMA attack assumes that the adversary has full knowledge of both the pre- and post-unlearning models, which may not always be realistic. Clarifying how the attack would function under more limited access (e.g., black-box settings) would enhance the paper’s practical relevance. The paper should explore scenarios where the adversary has access to only the output of the models, or where the adversary has access to a surrogate model trained on similar data. This would provide a more realistic evaluation of the attack's practical impact and help to identify potential defenses in real-world scenarios.

3. Focus on Specific Unlearning Methods: The study tests UMA primarily on select MUL methods like fine-tuning and retraining. It would be beneficial to see more experiments on emerging unlearning methods, especially in federated learning or distributed systems, where unlearning is more complex. The paper should include a discussion on how UMA could be adapted to attack unlearning methods in federated learning, where the model is distributed across multiple devices and the unlearning process involves communication between these devices. This would highlight the potential vulnerabilities of these systems and provide insights into the development of more robust unlearning techniques.

### Questions
1. How does the UMA attack perform in black-box scenarios where the adversary has only partial knowledge of the model pre- and post-unlearning? Could the attack still be successful with limited model access?

2. What are the computational overheads of incorporating robust unlearning into existing systems? How does this affect the scalability of machine unlearning in real-world applications?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the vulnerability of machine unlearning (MUL) to malicious attacks that attempt to recover forgotten information. To address this question, this paper introduces the concept of robust unlearning. This paper also develops the unlearning mapping attack (UMA), a malicious attack against MUL that can retrieve forgotten information.

### Strengths
1.	This paper is clear and logically structured. 
2.	This paper raises an important and noteworthy issue, namely whether MUL needs to be robust in both discriminative and generative tasks.

### Weaknesses
1.	The rationale behind the definition of robust unlearning requires further elaboration.
2.	The concept of robust unlearning does not seem to align well with the Unlearning Mapping Attack, as the strict conditions defined for robust unlearning are inconsistent with the optimization framework used in the attack.
3.	The Unlearning Mapping Attack method requires further explanation.
4.	It would be beneficial to include additional experiments with various generative models, such as DDPM that used by some baselines.

### Questions
1.	The paper mentions that a hidden weakness of MUL is that “successfully unlearned knowledge can resurface through appropriate probes.” However, if the retrain model also exhibits this limitation, then MUL is merely preserving this limitation. How do you ensure this issue is inherent to MUL itself and not to the model or data used?
2.	The concept of robust unlearning does not seem to align well with the Unlearning Mapping Attack. As I understand it, Propositions 2 and 3 require consideration of cases where an input might violate Condition 1. Thus, the definition of robust unlearning is aimed at ensuring that **any**   $x \in \mathcal{D}_u$ satisfies both Conditions 1 and 2. In contrast, the Unlearning Mapping Attack provides an optimization problem that seeks an input. If the solution obtained from this optimization is not optimal, it seems inconsistent with the definition of robust unlearning because there may still exist a solution that yields a lower loss. Consequently, the results of this attack do not align well with the definition of robust unlearning.
3.	I hope this paper can include additional explanation on how to apply the UMA method. Is this attack approach designed to generate a malicious dataset and then evaluate different MUL methods on this dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies a new machine unlearning attack called unlearning mapping attacks. Specifically, an adversary given the full knowledge of the original and unlearning model, along with the unlearned data, can perturb the unlearned data as input to the unlearned model for reproducing the same output as the original model. The proposed attacks are achieved by adapting techniques from adversarial examples. Extensive experimental results validate the effectiveness of the proposed attacks. This paper studies a new machine unlearning attack called unlearning mapping attacks. Specifically, an adversary given the full knowledge of the original and unlearning model, along with the unlearned data, can perturb the unlearned data as input to the unlearned model for reproducing the same output as the original model. The proposed attacks are achieved by adapting techniques from adversarial examples. Extensive experimental results validate the effectiveness of the proposed attacks.

### Strengths
+ This paper proposes a new attack targeting machine unlearning. Specifically, an attacker can perturb the original unlearned data to make the unlearned model generate the same output as the data that has not been unlearned. This attack reveals the vulnerability of existing machine unlearning mechanisms.

+ The proposed attack is evaluated on several vision tasks across various datasets. The experimental results support the claims of the paper.

+ A defense mechanism is explored to mitigate the proposed attack and show somewhat effectiveness.

### Weaknesses
I have several concerns about this paper, which are listed below.

- Attack motivation. As listed in the introduction, the authors argue that "As a post-MUL attack, UMA only requires access to the model before and after the unlearning process, which practically makes the model provider or the MUL service provider an ideal candidate for carrying out such an attack." I do not understand why the server wants to launch the mapping attack. What is the benefit from the server's perspective?

- Threat model. The adversarial (i.e., the server) is given full access to the model before and after the unlearning process. In addition, specific samples that need to be unlearned are given to the attacker. In this case, for the attack goal, why did the server not directly plug backdoors into the unlearned model so a targeted attack could be achieved once the unlearned model is released? This could be an "active" attack, while under this assumption it seems more practical. In addition, as the authors describe, "here, we assume the attacker’s goal is to extract the forgotten information from the unlearned models," the attacker under this assumption already knows everything about the unlearned samples, why still need to perform such an attack?

- Experimental validation. In generative cases, is the model performing sample unlearning? Can the proposed attack work in retraining cases? In addition, the results are not that convincing. In Figure 2, the attacked output is more like removed masks of unlearned outputs, or inpainting from unlearned outputs.

### Questions
The questions are listed in the weakness part. I believe solving these concerns can help to improve the quality of this paper.

### Soundness
2

### Presentation
3

### Contribution
3
