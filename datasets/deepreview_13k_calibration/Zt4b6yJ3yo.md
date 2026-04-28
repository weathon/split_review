# Denial-of-Service Poisoning Attacks against Large Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Recent studies have shown that LLMs are vulnerable to denial-of-service (DoS) attacks, where adversarial inputs like spelling errors or non-semantic prompts trigger endless outputs without generating an `[EOS]` token. These attacks can potentially cause high latency and make LLM services inaccessible to other users or tasks. However, when there are speech-to-text interfaces (e.g., voice commands to a robot), executing such DoS attacks becomes challenging, as it is difficult to introduce spelling errors or non-semantic prompts through speech. A simple DoS attack in these scenarios would be to instruct the model to *"Keep repeating Hello"*, but we observe that relying solely on natural instructions limits output length, which is bounded by the maximum length of the LLM’s supervised finetuning (SFT) data. To overcome this limitation, we propose **poisoning-based DoS (P-DoS)** attacks for LLMs, demonstrating that *injecting a single poisoned sample* designed for DoS purposes can break the output length limit. For example, a poisoned sample can successfully attack GPT-4o and GPT-4o mini (via OpenAI’s finetuning API) using less than \$1, causing repeated outputs up to the maximum inference length (16K tokens, compared to 0.5K before poisoning). Additionally, we perform comprehensive ablation studies on open-source LLMs and extend our method to LLM agents, where attackers can control both the finetuning dataset and algorithm. Our findings underscore the urgent need for defenses against P-DoS attacks to secure LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the problem of denial-of-service (DoS) attacks through finetuning. It shows that 1 example of direct instruction of repeating the same word N times with a corresponding answer in the finetuning dataset leads to the model performing this instruction during test time. Without finetuning, the model does not follow the instruction. The paper claims that this is due to bounded maximum length of the LLM's supervised finetuning data. Also, the paper claims that recent DoS attacks via adversarial inputs become challenging to execute when there are speech-to-text interfaces. Additionally, the paper demonstrates a backdoor attack by incorporating a trigger (e.g. "in 2025 year") with an adversarial goal of DoS attack (e.g. suppressing [EOS] token in open-source LLMs, generating "while (True)", "sleep 99999", "click[DoS]" in LLM-based agents). As a result, the authors "_strongly advocate for further research aimed at the defense of DoS threats in the custom finetuning of aligned LLMs_".

### Strengths
1. Highlighting a security issue of finetuning services and showcasing real-world examples of DoS attacks.

2. Experimental evaluation including ablation of most of the attack's design choices.

### Weaknesses
1. Novelty. The DoS attacks against LLMs were studied e.g. in Geiping et al. (2024) [1] as one of the objectives. The safety risks of finetuning were discussed in Qi et al. (2024) [2] in the context of harmful content generation. Although the DoS attacks might be an important security concern on their own, the paper lacks novelty in terms of the methodology.
2. The claims in the paper are not fully supported. 
    - Section 3 (which largely overlaps with Section 4.1 in terms of the methodology) studies the hypothesis that the reason of limited length of generated output is rooted in bounded length of inputs in supervised finetuning (SFT) data. However, it does not demonstrate the statistics of SFT data, and there is no clear evidence of output length dependence on SFT data (but not on pretraining data). More careful controlled experiments might be necessary to fully support this claim. 
    - The abstract and Figure 1 discuss the limitation of previous DoS attacks via adversarial inputs, namely, their instability under speech-to-text interfaces. However, I could not find experiments with speech-to-text interfaces in the paper. More recent "fluent" or low-perplexity adversarial attacks could potentially overcome this limitation, see e.g. Thompson et al. (2024) [3].

### Questions
Main concerns are in the weaknesses section.

Other minor questions:
1. In Figure 4, the DoS trigger is used with GPT model. However, I could not find such experiments. Could you please clarify this? Can GPT also be backdoored with a DoS trigger using the finetuning API?
2. It would be interesting to see and to analyze the generated outputs of LLMs under DoS attack with [EOS] suppression loss. Are there any patterns that could inspire other DoS attacks?
3. Could you discuss potential defenses against this attack in the paper?
4. The DoS attacks against LLMs discussed in this paper are manually crafted, and do not cover all possible attacks. Could you discuss ways to automatically find such vulnerabilities?

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
The paper proposes a poisoning-based DoS attack against (P-DoS) against LLMs and LLM agents. For P-DoS against LLMs, two threat models have been considered: attacker as the data contributor and attacker as the model publisher. For P-DoS against LLM agents, three types of agents have been considered.

### Strengths
* The attack is effective in general.
* The attack requires a low poisoning ratio.

### Weaknesses
 * The threat model is not realistic. For example, why do the model publishers attack their own model?
* The attacker's capability is too strong compared with the baselines. The baselines do not need access to the data. The comparison is unfair.
* Lack of novelty in the training loss. Can you justify the difference with backdoor attacks (which also include a loss for target and a loss for utility)?

### Questions
Please see the weakness.

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
This paper proposes a poisoning-based Denial-of-Service (DoS) attack. By fine-tuning an LLM on a small portion of poisoned data, an attacker can trigger the model to generate excessively long outputs, leading to high latency and costs. Across three different attack scenarios, this paper demonstrates the attack's effectiveness and stealthiness.

### Strengths
- This paper presents a powerful and stealthy poisoning-based DoS attack, highlighting the vulnerability of LLMs to such threats.
- This paper examines multiple attack scenarios, including data poisoning-only, fine-tuning, and agent-based attacks, further demonstrating the potential risks of this attack type.
- This attack demonstrates consistent high attack success rate through comprehensive evaluations with ablations across all three scenarios.

### Weaknesses
 - A discussion on potential defense methods against this type of attack would be helpful.
- Although the authors claim that speech-to-text interface is difficult to attack, there are adversarial examples [1] for speech recognition systems. Additionally, jailbreaking attacks using natural phrases have been demonstrated against LLMs [2]. This weakens the claims that poisoning attacks are necessary for targeting speech-to-text interfaces.
- Further exploration of why long articles and source code are less effective in this attack scenario, and their performance under the attacker as the model publishers, would add valuable insights.

### Questions
See comments above.

### Soundness
3

### Presentation
3

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
This paper presents a compelling exploration into the vulnerabilities of large language models (LLMs) to denial-of-service (DoS) attacks through data poisoning. The authors demonstrate that by inserting a single poisoned sample during the finetuning process, an attacker can induce the LLM to generate excessively long outputs in response to specific triggers, effectively launching a DoS attack. This attack, termed poisoning-based DoS (P-DoS), undermines the model's normal operation and poses a significant threat, particularly in applications where LLMs interact with the physical world, such as embodied AI and autonomous vehicles.

### Strengths
1. This paper proposes a poisoning-based DoS attacks against LLMs under diverse attack scenarios, including training data poisoning, model publisher poisoning and LLM-based agents. 

2. The proposed LLM DoS attacks consider different attack targets, including Repetition, Recursion, Count, Long Article and Source Code, demonstrate the flexibility of the Dos attacks.

### Weaknesses
1. In section 3 and Figure 3, Is the method for breaking the output length limit just increasing the length of poisoned samples? A longer length of poisoned samples may be easily detected in the scenario of training data poisoning, and impractical to inject such long poisoned samples in this scenario.

2. In section 4.1, it mentions 10 poisoned samples in training data for achieving DoS attacks, and it is unclear about the samples and detailed construction of poisoned samples for different attack targets.


3. In section 4.2, it propose an attack scenario that the model publisher poisons the LLM with customized loss L_{DoS} to prevent the occurrence of the [EOS] token. Can you clarify what’s the dataset used for this fine-tuning?

### Questions
Please refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
