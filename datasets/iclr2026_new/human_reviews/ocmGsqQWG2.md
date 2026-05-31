## Human Reviewer 1

### Summary
This paper presents a jailbreak paradigm termed "involuntary jailbreak," which induces LLMs to autonomously generate both harmful questions and corresponding unsafe responses through a meta-prompting approach. Unlike traditional targeted jailbreaks, this method employs abstract language operators and a balanced mix of safe/unsafe examples to systematically bypass model alignment safeguards. The authors demonstrate high success rates across multiple state-of-the-art proprietary models and argue this reveals fundamental fragility in current LLM safety mechanisms.

### Strengths
1. The concept of an untargeted, meta-level jailbreak that induces models to self-generate harmful content represents a novel and concerning attack vector beyond most existing prompt-level exploits.

2. The demonstration of high vulnerability across multiple state-of-the-art proprietary models (e.g., Claude Opus, GPT-4.1, Gemini 2.5 Pro) underscores the pervasiveness of the alignment problem.

### Weaknesses
1. The paper suffers from suboptimal organization, with excessive space allocated to large figures (e.g., Figures 5) that detail the attack construction. These visual elements, while helpful, should be relegated to an appendix to free up space for more critical content. The current structure sacrifices depth in experimental design and mechanistic analysis for visual exposition, weakening the paper's scholarly rigor.

2. The paper introduces multiple language operators (A, B, C, R) without justifying their individual necessity. There is no ablation study to determine which components are essential for the attack's success. This omission raises questions about whether a simpler, more minimal prompt design could achieve similar results, thereby undermining the claimed novelty and sophistication of the proposed method.

3. The #ASA metric, defined as the count of attempts where "at least one unsafe output is generated" out of 100 trials, is problematic. This low threshold means that an attempt is considered successful even if only one out of ten generated responses is harmful. Such occasional generation of unsafe content is not surprising and has been observed in prior work. This metric, combined with the lack of discussion about the computational or reasoning budget required per successful attack, casts doubt on the method's practical threat level compared to existing jailbreak techniques. 

4. The discussion of defenses in Section 5 is cursory and lacks practical utility. While noting that blocking the specific prompt is straightforward, the paper provides no systematic evaluation of how existing defense mechanisms (e.g., constitutional AI, inference-time monitoring, or adversarial training) would fare against variations of this attack. This limits the paper's contribution to the broader security landscape

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces involuntary jailbreak. This method is not specific to a malicious question but lets the victim model generate content in the format specified by the instructions, and then there will be unsafe content in the generated response. The attack only uses a universal template to trigger the response containing unsafe content, and there are different operators (rules) in the template to instruct the generation. Experiment results show that this method can lead state-of-the-art LLMs to generate unsafe responses.

### Strengths
1. This method uses a single universal template, which is easy to implement.
2. It can lead the SOTA LLMs to generate unsafe content with a relatively high portion in the whole response.

### Weaknesses
**1. Extremely exaggerated novelty:**

The author incorporates numerous requirements into the template and defines intricate logical rules. The template is inherently a meticulously engineered template. Therefore, LLMs are not “involuntarily” jailbroken. Instead, they are just meticulously following the user's design of extremely complex instructions, whose purpose is to overwhelm the security barriers. What's more, the techniques used in the template are also not new, such as prohibiting the generation of certain words and rewriting logic; the template seems to be a combination of existing jailbreak thoughts. In summary, I believe this is nothing more than a sophisticated instruction-following attack, fundamentally identical to the principles underlying DAN [1].

**2. Extremely exaggerated attack effects and impacts:**

This method is a non-directional attack, yet it nearly only induces the model to generate random ‘dangerous content’ on two specific topics, Topic 2 (non-violent crimes) and Topic 9 (indiscriminate weapons), which itself has very limited effect. What's more, how can targeted attacks (e.g., those aimed at achieving specific malicious goals) be made to “seem less necessary”?

**3. Limited utility:**

The method cannot even work on smaller models.

**4. Lack of testing under any state-of-the-art defensive mechanism:**

If an attack can be easily mitigated by known defensive measures, then it cannot be considered groundbreaking.

**5. Lack of sufficient ablations:**

The paper did not conduct any ablation experiments on the individual elements in its complex template.

**6. Lack of any useful interpretation of the proposed jailbreak method:**

The author merely states that LLMs focus on implementing complex operators while neglecting security rules. If this is the explanation, then this method certainly cannot be said to reveal an entirely new vulnerability; it is merely another manifestation or combination of existing vulnerabilities (long context [2], complex logic [3], instruction compliance [1], etc.).

**7. It only proved its own effectiveness without comparing it to any baseline in any aspect.**


[1] DAN (Do Anything Now).

[2] Many-shot jailbreaking

[3] GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher

### Questions
See the weakness above.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper propose a new jailbreak prompt towards LLMs.

### Strengths
+ The topic is interesting

### Weaknesses
- This main contribution of paper is positioned by the authors themselves as a single universal prompt. While there are already tons of prompt-based jailbreak attack in this domain, this paper even does not introduce any new pipeline or framework, which makes the contribution even more limited. As to the prompt itself, it is also not new. For example, it seems just a combination of few-shot jailbreak [Jailbreak and Guard Aligned Language Models
with Only Few In-Context Demonstrations] attack and answer the benign response first and then the desired harmful response. For the latter, I cannot even list the citation as it was just a strategy discovered in 2023 (see GPTFuzz's collected jailbreak template).

- No baseline is compared

- Some experimental details are missing, for example, where did you obtain the harmful and harmless questions? How did you set the temperature during sampling, what is the top_k? Is there repeated runs?

### Questions
See the weakness above

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper identifies involuntary jailbreak, which is a vulnerability across major LLMs, especially instruction-followed ones. Involuntary jailbreak shows that a structured prompt using abstract operators can reliably bypass the safety mechanisms in an LLM. Experiments show that it achieves high attack performance across many frontier LLMs, revealing its effectiveness.

### Strengths
- Novel concept
- Comprehensive coverage of 2025 LLM families
- Prompt design innovation

### Weaknesses
- Lack of targetability
- Lack of answer validation
- Figure presentation and clarity need to be improved
- Lack of baselines

### Questions
- Although it is effective, it lacks target specificity. As such, attackers cannot easily obtain desired responses to specific queries, limiting their practical exploitability. Take an attacker with a specific harmful purpose, for example. They need to first query the LLMs multiple times and obtain a set of harmful question-answer pairs. Then, they need to find the question they are interested in. This raises concerns that the QA set does not contain the specific question.

- Additionally, there is no validation for the correctness of the answer. In the experiments, the authors only focus on whether the generated pairs are harmful or not, ignoring the correctness of the answer. Measuring the correctness of the answer[1][2] would contribute to the effectiveness of this method.

- Figure 1-4 occupies a lot of space but adds limited analytical value. Considering moving some of them into the appendix may help improve readability and allocate space for deeper discussion.

- There is also a lack of explanation on these figures (the authors only mention them briefly in the introduction), preventing the audience from understanding the content. For example, what do "X(input)" and "Y(X(input))" present?

- Further, there is also a lack of baselines. Given the questions obtained, I would like to know whether these questions are easier for targeted jailbreak attacks such as AutoDAN[3] or LAA[4].

- Statements such as "the entire guardrail structure collapses" or "GPT-5 need not be tested" are overgeneralized. The experiments only demonstrate behavioral vulnerabilities under a specific prompt, not systemic or architectural guardrail failure.

[1] HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal. Mazeika et al. 2024.

[2] JADES: A Universal Framework for Jailbreak Assessment via Decompositional Scoring. Chu et al. 2025.

[3] AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models. Liu et al. 2023.

[4] Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks. Andriushchenko et al. 2024.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
2

### Confidence
3
