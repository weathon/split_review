# AdvBDGen: Adversarially Fortified Prompt-Specific Fuzzy Backdoor Generator Against LLM Alignment

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 5, 3, 3

## Abstract
With the growing adoption of reinforcement learning with human feedback (RLHF) for aligning large language models (LLMs), the risk of backdoor installation during alignment has increased, leading to unintended and harmful behaviors. Existing backdoor triggers are typically limited to fixed word patterns, making them detectable during data cleaning and easily removable post-poisoning. In this work, we explore the use of prompt-specific paraphrases as backdoor triggers, enhancing their stealth  and resistance to removal during LLM alignment. We propose AdvBDGen, an adversarially fortified generative fine-tuning framework that automatically generates prompt-specific backdoors that are effective, stealthy, and transferable across models. AdvBDGen employs a generator-discriminator pair, fortified by an adversary, to ensure the installability and stealthiness of backdoors. It enables the crafting and successful installation of complex triggers using as little as 3\% of the fine-tuning data. Once installed, these backdoors can jailbreak LLMs during inference, demonstrate improved stability against perturbations compared to traditional constant triggers, and are more challenging to remove. These findings underscore an urgent need for the research community to develop more robust defenses against adversarial backdoor threats in LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents AdvBDGen, a generative framework designed to create adaptive and stealthy backdoor triggers in LLMs by leveraging an adversarially fortified training setup. AdvBDGen improves the stealth and resilience of backdoor triggers compared to traditional fixed-pattern approaches by generating prompt-specific, paraphrased triggers. These backdoors are crafted through an adversarial setting involving a generator and two discriminators—a strong and a weak one—that work together to ensure the backdoors remain both effective and undetectable by less sophisticated defenses. The primary contributions of the paper are:

- AdvBDGen introduces a new backdoor generation framework that generates prompt-specific, adaptive triggers for LLMs.

- The backdoor triggers are shown to be effective across different LLM architectures, enhancing their generalizability.

- Highlights the challenge of defense against fuzzy backdoors.

### Strengths
- Originality

This paper proposes a novel approach for generating adaptive, prompt-specific backdoor triggers that are context-aware and resistant to traditional defense mechanisms. By using adversarial training with dual discriminators (weak and strong), the framework encourages the generation of subtle, complex triggers that evade detection more effectively than fixed-pattern backdoors.


- Quality

The paper presents rigorous experiments, evaluating the generated backdoors’ effectiveness and resilience. AdvBDGen is benchmarked against standard trigger models, demonstrating its robustness across different poisoning percentages and showing that the generated backdoors are transferable across models.

- Clarity

The paper is well-organized and provides clear explanations of its methodology.

- Significance

The framework addresses an emerging threat in the alignment of LLMs. Given the increasing reliance on preference alignment to ensure safe and aligned AI behavior, the work highlights significant vulnerabilities. By presenting a robust approach to backdoor generation, the paper calls attention to the need for improved defense mechanisms, making it a valuable contribution to AI safety research.

### Weaknesses
 - Stylistic [1] and Syntactic [2] backdoor triggers can serve as a competing baseline method.

### Questions
- Two related works [1,2] are not discussed in this paper. A more detailed discussion on the differences would help readers understand the unique contributions and contextualize this approach within the existing literature.

- Since the generator aims at creating more sophisticated triggers that are subtle enough to bypass the weaker discriminator while still identifiable by the stronger one, should we expect an increase in the prediction error of the weaker discriminator in Figure 2?


[1] Jiahao Yu et al. GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts.

[2] Jiongxiao Wang et al. RLHFPoison: Reward Poisoning Attack for Reinforcement Learning with Human Feedback in Large Language Models

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores vulnerabilities in aligning LLMs using RLHF, specifically focusing on backdoor poisoning attacks. Traditional backdoor triggers are often fixed and detectable, making them less effective. To address these limitations, the authors propose AdvBDGen, an adversarially fortified generative framework that creates prompt-specific, adaptable, and stealthy backdoor triggers resistant to common defensive measures. This system comprises a generator and two discriminators (strong and weak), which collaborate to optimize the generation of stealthy, effective triggers while maintaining semantic integrity and resisting detection.

The main contributions include:
1. Introduction of AdvBDGen, which uses prompt-specific triggers with varied presentations to bypass conventional defenses.
Demonstration that these generated triggers are highly effective, transferable across models, and robust to semantic perturbations, unlike traditional fixed triggers.
2. Evidence that adversarially trained paraphrased triggers outperform naive paraphrases as reliable backdoors.
3. Highlighting the increased difficulty in detecting and removing these adaptable backdoor triggers, underlining the need for more advanced defense mechanisms in LLM alignment.

### Strengths
1. Unlike prior works that use fixed triggers, the paper leverages GAN-style training to explore context-adaptive and paraphrase-based backdoors that are harder to detect and neutralize.
2. The comparative analysis between naive LLM-generated paraphrases and those produced by AdvBDGen underscores the method's efficacy and robustness.
3. The work covers various dimensions of stealthiness and transferability, showcasing how the proposed backdoors withstand semantic perturbations and transfer across different models, enhancing the reliability of the results.
4. By demonstrating that minimal data can be leveraged to install potent and stealthy backdoors, the work underlines the potential real-world risks associated with LLM deployment and training, urging the research community to prioritize defensive measures.

### Weaknesses
1. The authors assert that constant triggers can be easily detected; however, they did not provide experimental evidence to support this claim. Notably, constant triggers have shown higher attack performance even at low poisoning rates, which are typically more challenging to detect. This raises the question of whether the proposed method, which involves complex backdoor generation steps, is truly necessary. I recommend providing additional experimental evidence to justify that the benefits of the proposed method outweigh the increased complexity. This will help strengthen the case for its practical advantages.
2. The generator and discriminator training process, which forms the core of your approach, lacks clarity. Specifically, as mentioned in line 237, the generator and discriminator are trained simultaneously. However, for training the discriminator effectively, original, "good," and "bad" prompts are needed, and these prompts are produced by the generator. At the initial stage of training, the generator is expected to create prompts that closely resemble the original, offering minimal informative cues for the discriminator to learn from. This setup implies that successful generator training hinges on the presence of a well-trained discriminator, creating a circular dependency between the two. While GANs face similar challenges, they begin with generators producing nonsensical images that can still be distinguished from real images by the discriminator. In your case, how does an untrained, "cold-start" discriminator differentiate between original and backdoored prompts? This raises concerns about potential model collapse, a known issue in GAN training. However, it appears that the authors did not report encountering this problem. 
    - Can you provide a detailed, step-by-step description of the initial stages of training, focusing on how they handle the cold-start problem for both the generator and discriminator.
    - Can you provide empirical evidence or metrics that demonstrate the stability of your training process over time.
    - Can you discuss any failed approaches or challenges you encountered during the development of this training process and how you overcame them.

3. The defense strategy examined in this work appears rather weak. Since the authors' goal was to train a LLM to produce helpful responses, a straightforward approach would involve using a classifier to detect and filter out misaligned (harmful) responses introduced through data poisoning. This method, which is already implemented on platforms such as OpenAPI, enables model developers to sanitize the training data and mitigate alignment issues effectively. In addition, one can paraphrase the prompt using paraphrasing models or round-trip translation models to neutralize the potential backdoor triggers [1,2]. I would like to see a discussion of the effectiveness of the proposed backdoor triggers against models protected by the defense methods above.
4. The novel is limited, as the use of GAN-style methods for generating backdoor triggers is well-established and has been extensively explored by the NLP and computer vision (CV) research communities [3, 4, 5].

### Questions
Typos:
1. In figure 1, semnatic-> semantic

### Soundness
3

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
4

### Summary
This paper presents a new approach AdvBDGen to generating adaptable, transferable, and stealthy backdoor triggers for large language models (LLMs). The proposed attacks can automatically generate backdoor triggers during the alignment stage of LLMs, and are robust to perturbations. Overall, this work underscores the potential risks associated with LLM alignment and the necessity for enhanced security measures to mitigate adversarial threats in this domain.

### Strengths
This paper focuses on an important research problem regarding the backdoor attacks in the LLMs alignment stage. From the attacker's perspective, the authors propose an attack approach named AdvBDGen that has been proven effective in the empirical experiments in the following aspects:
1. The injection of the triggers is easier with just 3% of the fine-tuning data.
2. The injected triggers are more stable compared to previous approaches.
3. The injected triggers are stealthy, making them hard to defend against. 

The research raises relevant security risks regarding the LLMs alignment data.

### Weaknesses
1. The overall writing and presentation of this paper should be largely improved. For the current version, it's hard to get an overall understanding of the proposed attack in the abstract and introduction (i.e., how and why the method can work, and the key motivation). The figure 1 doesn't provide too much useful information. Some concrete examples of poisoned samples can be better. 
2. The key motivation of this work and the novelty of the proposed approach are not very clear to me. To the best of my knowledge, semantic-based backdoor attacks are extensively proposed in previous research, including but not limited to the following work: [1,2,3]. However, this paper only mentions "constant triggers" during the motivation and development of the method. This makes the overall contribution and novelty very confusing.  Correspondingly, the relevant semantic-based backdoor attack methods are not considered and compared with in the experiments, making the results not solid enough. 
3. I appreciate the work done by the authors in Sec 4.4 that uses safety training to measure the strength of the proposed attack method. However, this evaluation is far from extensive. More evaluation beyond the simple discussion, including different defense methods and even human annotations should be conducted to measure the strength, stealth, and adaptability of the method.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work is motivated by the need to develop evasive triggers to avoid potential detection. The author proposes to increase backdoor evasiveness by developing input-tailored triggers. Therefore, this work introduces a GAN-based framework to produce text backdoors, where the generator is designed to fuse triggers into inputs, and the discriminator is responsible for identifying the presence of triggers. Through experiments, the authors demonstrate the partial effectiveness of the backdoor design.

### Strengths
1. This work stands on the need to study advanced attacks to reveal LLM vulnerabilities.
2. Design of the technique is clear.

### Weaknesses
 **1.** This work misuses or misunderstands many terms. (a) The "backdoor" attack is targeted. For untargeted attacks that generally degrade model performance, we typically name them as "poisoning." (b) "Fuzzing" is typically used for detection, standing on defender's side. When presenting an attack based on a generative technique, it is inappropriate to call it "fuzzing." Moreover, fuzzing involves specific pipeline, either mutation-based or generation-based, to produce variants of test cases (or seeds). However, the proposed technique does not align with the fuzzing pipeline. (c) The author mixes the concept "generator-discriminator" and "encoder-decoder." I understand that in this GAN-like architecture the generator functions like an encoder and the discriminator like a decoder, it would be better for the author to use consistent terminology throughout the paper.

**2.** The contribution is incremental, lacking novelty in both the problem definition and the technical solution. In terms of problem definition, evasive backdoors have been extensively studied, wherein novel approaches, such as "style backdoors"  treats semantic styles as backdoor triggers, has rigorous definitions. However, this work merely relies on a black-box model to produce trigger-embedded inputs, without providing intuitions about the nature of the backdoor. The technical solution is simply a combination of existing modules, without offering strong insights or a truly novel design.

**3.** Some terms are over complex, such as "ADVERSARIALLY FORTIFIED PROMPT-SPECIFIC FUZZY BACKDOOR."

**4.** Typo in Figure 1: "Semnatic"

**5.** Experiments are inadequate and degrading the credit of the proposed technique: (a) The paper only uses one dataset. (b) Only one naive baseline, without considering other evasive backdoor designs. (c) Defense is simple, while there are many advanced defensed such as RAP [1] that considers complex natures. (d) The attack effectiveness is limited (such as from table 1), and the author didn't explain how sacrifice effectiveness can benefit evasiveness.

### Questions
Please see the comments above.

### Soundness
2

### Presentation
2

### Contribution
1
