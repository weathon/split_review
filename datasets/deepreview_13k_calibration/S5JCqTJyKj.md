# Deferred Backdoor Functionality Attacks on Deep Learning Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5

## Abstract
Deep learning models are vulnerable to backdoor attacks, where adversaries inject malicious functionality during training that activates on trigger inputs at inference time. Extensive research has focused on developing stealthy backdoor attacks to evade detection and defense mechanisms. 
However, these approaches still have limitations that leave the door open for detection and mitigation due to their inherent design to cause malicious behavior in the presence of a trigger.
To address this limitation, we introduce Deferred Activated Backdoor Functionality (DABF), a new paradigm in backdoor attacks. Unlike conventional attacks, DABF initially conceals its backdoor, producing benign outputs even when triggered. This stealthy behavior allows DABF to bypass multiple detection and defense methods, remaining undetected during initial inspections.
The backdoor functionality is strategically activated only after the model undergoes subsequent updates, such as retraining on benign data. DABF attacks exploit the common practice in the life cycle of machine learning models to perform model updates and fine-tuning after initial deployment. To implement DABF attacks, we approach the problem by making the unlearning of the backdoor fragile, allowing it to be easily cancelled and subsequently reactivate the backdoor functionality. To achieve this, we propose a novel two-stage training scheme, called $\texttt{DeferBad}$. Our extensive experiments across various fine-tuning scenarios, backdoor attack types, datasets, and model architectures demonstrate the effectiveness and stealthiness of $\texttt{DeferBad}$.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The authors propose a novel backdoor attack method called Defferred Activated Backdoor Functionality (DABF), which enhances the stealthiness and detection difficulty of the attack by deferring the backdoor trigger. This attack method comprises two main stages: the Backdoor Dormancy Stage and the Backdoor Activation Stage. In the Backdoor Dormancy Stage, the model is initially trained with a poisoned dataset labeled with the target label. Then, it is updated using a poisoned dataset with correct labels (i.e., "unlearning dataset") to partially modify model parameters and thus conceal the backdoor. The Backdoor Deferred Activation Stage involves fine-tuning the model with a normal dataset, thereby reactivating the backdoor.

### Strengths
* The topic of deferred activation of backdoor attack is highly relevant and timely.
* The paper is clearly written and well organized.
* The approach is clear and easy to follow.

### Weaknesses
 * Weak threat model: The authors’ threat model assumes a scenario where a user obtains a pre-trained model with a hidden backdoor from a third party, and this backdoor is activated after fine-tuning with a normal dataset. In this model, it is assumed that the user would only conduct backdoor detection on the pre-trained model they obtained. However, in practice, users are only responsible for conducting backdoor detection on the final model they use after fine-tuning; inspection of the pre-trained model itself is not necessary and holds no practical value. Even if backdoor detection were performed on both the pre-trained and the fine-tuned models, the additional cost would not be significant. Therefore, the threat model proposed in this paper is too weak and does not align with real-world application scenarios.
* Insufficient Experimental Design: Firstly, in practice, the most common scenario involves fine-tuning a pre-trained model on a dataset for a similar task, where the distribution of this dataset is often significantly different from that of the pre-trained model’s original training data. However, in this experiment, whether by removing some data or using adversarial data, the fine-tuning dataset only exhibits a slight distribution shift from the pre-training dataset. This makes it difficult to demonstrate the real-world effectiveness of the proposed attack method. Secondly, the backdoor detection and mitigation techniques used in this paper are outdated (published over five years ago) and do not include all representative detection approaches (such as model behavior-based detection methods). Therefore, it is challenging to validate that the proposed method can effectively evade current defense techniques.

### Questions
* Why assume that users do not perform backdoor defense on the fine-tuned model?
* Why is there no summary of the latest backdoor attacks and defense methods in the related work section?
* Is this method still effective for fine-tuning models using datasets different from the pre training dataset? For example, using CIFAR-10 to fine-tune a pre-trained model based on ImageNet.
* Why weren’t the latest defense methods (e.g., https://arxiv.org/abs/2305.18651) and model behavior-based defense methods (e.g., https://proceedings.neurips.cc/paper_files/paper/2022/file/db1d5c63576587fc1d40d33a75190c71-Paper-Conference.pdf) used in the experiments?
* The descriptions about parameter update and freeze in Lines 283 and 295 conflict with Lines 333 and 334.
* Is k the same parameter (i.e., has the same value) in backdoor concealment and backdoor activation? If yes, doesn’t this mean the attacker could control the fine-tuning? If not, please provide the value of k used in the backdoor concealment phase.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces DeferBad, a backdoor attack strategy that bypasses backdoor detection methods by initially concealing the backdoor. Unlike traditional backdoor attacks that activate upon deployment, DBFA maintains a dormant state, producing benign outputs even when triggered initially. The backdoor activates only after a model undergoes fine-tuning or retraining on clean data. It involves a two-stage training scheme consisting of an initial backdoor injection followed by partial model parameter updates for concealment. DeferBad proves to be effective across different models and datasets, demonstrating robustness and evading defenses.

### Strengths
+ The attacker does not need any involvement to activate the backdoor after deployment.
+ Extensive experiments using various datasets and neural network architectures.

### Weaknesses
 - The novelty of the paper is limited, as recent literature on camouflage backdoor attacks has already discussed approaches that operate on a similar principle to the proposed deferred backdoor functionality [1, 2, 3]. The related work section should include a more thorough comparison to these existing methods to better position the paper's contributions in the context of prior work.

- DeferBad has only been tested with two backdoor attacks, BadNets and ISSBA, making it hard to evaluate its effectiveness against newer, more sophisticated backdoor attacks like Bpp and WaNet. Consequently, it is difficult to draw a conclusion about the generalizability of DeferBad.

- The defenses evaluated in this paper are not state-of-the-art and primarily include methods dated back to 2019. More recent advancements in backdoor defenses have not been included in the paper [4]. Additionally, GradCAM is not classified as either a backdoor detection or mitigation approach.

- The paper states that DeferBad achieves backdoor concealment by selectively updating a subset of the model's layers, creating an unstable equilibrium that masks the backdoor. This concealed state remains dormant until disrupted by fine-tuning, which then reactivates the backdoor. However, the underlying rationale for why this method is effective is not extensively detailed. Providing theoretical justifications would strengthen the support for this claim.

- The paper claims that DeferBad remains effective even when the victim model undergoes full-layer fine-tuning. However, Figure 2 contradicts this claim, showing that DeferBad does not achieve a high attack success rate when the number of frozen layers is zero, implying full-layer fine-tuning. The attack success rate significantly increases only when minimal layers are fine-tuned.

- All the results presented in the paper must be evaluated across multiple runs to ensure the statistical significance of the reported values.

### Questions
- How does DeferBad compare against existing camouflage backdoor approaches in recent literature?
- Could you provide more theoretical insights into why selective layer updates create an "unstable equilibrium" that effectively masks the backdoor?
- Test DeferBad with newer and more sophisticated backdoor attacks such as Bpp and WaNet to assess its generalizability.
- Test DeferBad against more recent backdoor defense methods.
- Provide justifications for DeferBad's effectiveness when all model layers are fine-tuned.

### Soundness
3

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
The paper introduces a new backdoor attack strategy, which aims to make backdoors more stealthy by keeping them dormant during initial deployment and activating them during subsequent model fine-tuning. This approach targets a fundamental vulnerability in existing backdoor detection techniques, which often rely on observing immediate malicious behavior. To implement DBFA, the authors propose a two-stage training method called "DeferBad." This method first injects the backdoor and then strategically conceals it until model updates reactivate it. The paper demonstrates that DeferBad is highly effective across different fine-tuning scenarios, model architectures, and backdoor types, successfully evading state-of-the-art backdoor detection and mitigation methods.

### Strengths
This paper introduces a novel paradigm in backdoor attacks, significantly improving stealth by keeping the backdoor dormant during initial deployment and activating it only after fine-tuning.

### Weaknesses
This paper limits its generalizability only on vision domain.

While the paper demonstrates the effectiveness of DBFA through experiments, it lacks a rigorous theoretical explanation for why fine-tuning effectively reactivates the dormant backdoor.

The paper focuses on the effectiveness of the attack but does not discuss or propose potential defense mechanisms against DBFA.

The experimental results show variability in attack success rates based on the number of layers fine-tuned, but there is limited discussion on why these differences occur.

### Questions
See the weakness.

### Soundness
2

### Presentation
3

### Contribution
2
