# Sounding the Alarm: Backdooring Acoustic Foundation Models for Physically Realizable Triggers

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Although foundation models help increase performance on many downstream tasks while reducing the amount of labeled data needed, 
their proliferation has raised a natural question: To what extent can a model downloaded from the Internet be trusted?  We tackle this question for acoustic foundation models (AFMs) and propose the $\textbf F$oundation $\textbf A$coustic model $\textbf B$ackdoor (FAB) attack against AFMs, showing that state-of-the-art models are susceptible to a new attack vector. Despite preserving model performance on benign data, AFM induces backdoors that survive fine-tuning, and, when activated, lead to a significant performance drop on various downstream tasks.  Notably, backdoors created by FAB can be activated in a ${physically\ realizable}$ manner by ${inconspicuous}$, ${input}$-${agnostic}$ triggers that ${do\ not\ require\ syncing}$ with the acoustic input (e.g., by playing a siren sound in the background). Crucially, FAB also assumes a weaker threat model than past work, where the adversary has no knowledge of the pre-training data and certain architectural details.  We tested FAB with two leading AFMs, on nine tasks, with four triggers, against two defenses, as well as in the digital and physical domains, and found the attack highly successful in all scenarios.  Overall, our work highlights the risks facing AFMs and calls for advanced defences to mitigate them.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the Foundation Acoustic model Backdoor (FAB) attack, a method for inserting backdoors in acoustic foundation models (AFMs) using physically realizable, input-agnostic audio triggers, such as sirens or barks. FAB attacks maintain model performance on benign data but degrade it significantly when activated, impacting various downstream tasks. Unlike prior work, FAB assumes a weak threat model, with attackers having limited knowledge of training data and model parameters. Experiments across multiple AFMs, tasks, triggers, and defenses show FAB's effectiveness in both digital and physical settings, even against standard defenses like fine-pruning and input filtering. This study highlights security risks in AFMs and the need for stronger defenses against backdoor attacks.

### Strengths
- Task-Agnostic and Physically Realizable Backdoor Attack: The proposed FAB is task-agnostic and physically realizable. Unlike prior work, FAB uses simple, inconspicuous sounds like sirens or dog barks as triggers without needing synchronization, making it adaptable to real-world settings.

- Comprehensive Evaluation: Extensive experiments demonstrate FAB's effectiveness across various tasks and AFMs. The paper also tests FAB against defenses like fine-pruning and input filtration, showing its resilience. This thorough evaluation highlights the attack’s robustness and underscores the need for stronger defenses in model security.

### Weaknesses
 - Limited Novelty: While the FAB attack presents an interesting application, fine-tuning-based backdoor injection is not new, and FAB still requires auxiliary data with a distribution similar to the target AFM. This reliance on auxiliary data limits its originality and does not fully address existing challenges in realistic backdoor attacks.

- Unrealistic Threat Model: The threat model lacks practical relevance, as it assumes the model provider itself would inject backdoors that degrade performance significantly. Major AFM providers, like OpenAI, are unlikely to introduce such vulnerabilities into their own models, limiting the real-world applicability of this attack.

- Limited Evaluation Scope: The study focuses primarily on AFMs like HuBERT and WavLM, without assessing generalizability to a broader range of models. Testing additional AFM architectures, such as wav2vec 2.0 from Google and Data2Vec from Meta.

- Lack of Audio Quality Evaluation: The study does not assess the audio quality of samples embedded with backdoor triggers compared to the original, unmodified samples. Metrics like ViSQOL could provide insights into whether the trigger significantly affects perceived audio quality. This evaluation is essential to ensure that the trigger remains inconspicuous to users, as noticeable quality degradation could alert users to the presence of an anomaly, undermining the stealth of the attack.

### Questions
- Could you elaborate on the need for auxiliary data with a similar distribution to the target AFM? Are there any approaches under consideration to remove this requirement? Clarifying this could help address concerns regarding FAB's novelty and broader applicability.

- Given that major AFM providers like OpenAI are unlikely to risk their model’s reputation by embedding backdoors, who do you envision as the realistic adversary for FAB? Additional clarification on feasible attacker scenarios could strengthen the practical relevance of the proposed method.

- The study’s evaluation primarily focuses on HuBERT and WavLM. Have you considered expanding your experiments to include other prominent AFMs, such as wav2vec 2.0 or Data2Vec? 

- To better understand the stealth of the embedded trigger, could you provide an audio quality evaluation using metrics like ViSQOL?

### Soundness
3

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
Foundation models enhance performance across various downstream tasks and minimize the need for labeled data. This paper's authors revealed that acoustic foundation models are vulnerable to backdoor attacks, and extensive experiments confirmed the effectiveness of these attacks.

### Strengths
Exploring the security issues in acoustic foundation models is both an important and intriguing topic.

### Weaknesses
1) The paper is poorly written.
2) The threat model lacks clarity.
3) Baseline attacks are not included.

### Questions
Thank you to the authors for this interesting paper. I have a few comments regarding the current work:

1) Overall, the paper is not well-written. In Section 4, instead of just stating that FAB minimizes a compound loss function, the authors should provide the mathematical details of  L_back and L_benign. Without this, it becomes difficult for readers to follow the explanation.
2) Typically, foundation models and downstream tasks use different encoders. However, the threat model does not clearly specify whether the attacker is aware of the encoders used in the downstream tasks.
3) In recent years, numerous papers have targeted foundation models to mislead downstream tasks, such as [A] and [B]. The main distinction in this paper seems to be its focus on the security of acoustic foundation models. Aside from this, the technical challenges appear similar. The authors should clarify in the related work section the key differences between this research and existing literature. Why not simply apply previous attack techniques to acoustic foundation models? What are the unique challenges in attacking acoustic foundation models?
4) The current paper does not seem to compare the proposed attacks with existing ones. It should not be difficult to apply the attacks described in [A] and [B] to the scenario outlined in this paper.
5) A potential defense against the proposed attack could be for the downstream task to use a conditional diffusion model to denoise the audio.


[A] Badencoder: Backdoor attacks to pre-trained encoders in self-supervised learning.

[B] Adversarial Illusions in Multi-Modal Embeddings.

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
5

### Summary
This paper proposes a backdoor attack against the acoustic foundation model in self-supervised learning, which can degrade the performance of corresponding downstream tasks.

### Strengths
1. Language is mostly accessible, though with some minor issues
2. Experimental results verify the effectiveness of the proposed scheme.

### Weaknesses
The research motivation is not practical enough. Specifically, the choice of prominent sounds such as sirens, oboes, flutes, and barks as backdoor triggers raises concerns. The stated goal is to degrade the performance of downstream tasks, yet these triggers are easily identifiable and could be trivially filtered out or mitigated. If the attacker's objective is to actively trigger the backdoor, it is unclear why they would not opt for less conspicuous methods. For example, using noise-like triggers, such as white noise or ultrasound, would be more effective at impairing model performance without being easily detected. The selection of highly distinctive sounds seems counterintuitive if the goal is to maintain stealth, as these sounds are unlikely to blend into typical acoustic environments. The paper does not adequately justify why such easily detectable triggers are used, which undermines the practical relevance of the proposed attack.

The methods section (Section 4) writing is overly redundant and tedious, making an otherwise straightforward approach appear complicated. The description of the backdoor injection process and the training procedure could be significantly streamlined. The current presentation makes it difficult to grasp the core mechanics of the approach, and the excessive detail obscures the key ideas.

### Questions
1. key concern: The author chose prominent sounds such as sirens, oboes, flutes, and bark as backdoor triggers, aiming to degrade the performance of associated downstream tasks rather than inducing a specific target behaviour. Theoretically, readers might question why attackers do not directly utilize noise-like triggers to impair the model performance if the attacker was required to activate the trigger actively. Besides, considering stealthiness, selecting white noise or ultrasound could obviously be seen as more covert than distinctive sounds like sirens. Therefore, It seems that the article's motivation is not clearly explained.
2. The methods section (Section 4) writing is overly redundant and tedious, making an otherwise straightforward approach appear complicated. It is recommended that the author revise the methods section to present the information more logically and streamlined.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors assume that the backdoor attacker performs a type of ‘man-in-the-middle’ attack between the (benign) model provider and the victim user. Specifically, the attacker injects a backdoor into a pretrained Acoustic Foundation Model (AFM) obtained from the provider, and then releases it to the victim, who further fine-tunes it for a downstream task. According to their claim, the proposed backdoor is physically realizable, inconspicuous, input-agnostic, and sync-free (not requiring synchronization between the trigger sound and the sonic input).

### Strengths
# Advantage
The main contribution of this work is the method for injecting the backdoor in a realistic scenario where the attacker has limited capability: the attacker can only access the pretrained model, cannot access the provider's training dataset, and has no knowledge of the downstream task. To inject a backdoor, the attacker reduces the representation distance between poisoned samples (benign sample + trigger) and a ‘non-useful’ representation from intermediate layers, without affecting the model’s performance on benign tasks. During the downstream task, once the trigger is present in the input, the input is mapped to the ‘non-useful’ representation, leading to misclassification.

The main challenge is maintaining the model’s performance on benign tasks. According to the authors, the best approach is to retrain the pretrained model in the same way the provider did (but with an additional backdoor loss). However, since the attacker does not know the exact codewords and other parameters, the authors propose approximating the missing parameters and using pseudo-labeling.

### Weaknesses
 # Weakness

Several weaknesses can be identified:

1.	The authors assume that the user will use two fine-tuning paradigms: fine-tuning only the last layer or applying a weighted sum of all layers’ representations. However, to attach the trigger and the ‘non-useful’ representation, it seems necessary to freeze the feature extractor of the AFM. It is important to verify whether the backdoor remains robust after fine-tuning the entire AFM. Based on my experience, it is hard to ensure backdoor mapping without freezing. Specifically, the concern is that fine-tuning the entire model might cause the 'non-useful' representation to drift away from the intended target, thereby weakening or eliminating the backdoor effect. The authors should provide empirical evidence demonstrating the backdoor's persistence under full fine-tuning, including a detailed analysis of how the intermediate representations change during this process.

2.	The authors also assume that the attacker knows the same training procedure as the provider. How realistic is it for the model to publicly release the training algorithm? This assumption is particularly problematic because the training procedure often involves numerous hyperparameters and specific data augmentation techniques. Even if the general algorithm is known, subtle differences in these parameters could significantly impact the effectiveness of the backdoor injection. The authors need to justify this assumption or, alternatively, explore the robustness of their method under variations in the training procedure. For example, they could investigate how the backdoor's effectiveness changes when different optimizers, learning rates, or data augmentation strategies are used during the retraining phase.

3.	The two defenses are outdated and specifically don’t focus on backdoor detection in SSL. The authors should also consider more recent methods, such as:1.	Zheng, Mengxin, et al. "SSL-Cleanse: Trojan Detection and Mitigation in Self-Supervised Learning." ECCV 2024;2.	Feng, Shiwei, et al. "Detecting Backdoors in Pre-Trained Encoders." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023. The chosen defenses are not directly applicable to the self-supervised learning (SSL) context, and this limits the practical relevance of the evaluation. The authors should consider more recent methods that are specifically designed for backdoor detection in SSL, and also methods that are applicable to the audio domain. The lack of appropriate defenses makes it difficult to assess the true vulnerability of the proposed approach.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2
