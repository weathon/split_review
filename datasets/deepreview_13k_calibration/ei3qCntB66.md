# BadRobot: Manipulating Embodied LLMs in the Physical World

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Embodied AI represents systems where AI is integrated into physical entities, enabling them to perceive and interact with their surroundings. \textit{Large Language Model} (LLM), which exhibits powerful language understanding abilities, has been extensively employed in embodied AI by facilitating sophisticated task planning. However, a critical safety issue remains overlooked: \textit{could these embodied LLMs perpetrate harmful behaviors?}
In response, we introduce \textsc{BadRobot}, a novel attack paradigm aiming to make embodied LLMs violate safety and ethical constraints through typical voice-based user-system interactions.
Specifically, three vulnerabilities are exploited to achieve this type of attack: (i) manipulation of LLMs within robotic systems, (ii) misalignment between linguistic outputs and physical actions, and 
(iii) unintentional hazardous behaviors caused by world knowledge's flaws.
Furthermore, we construct a benchmark of various malicious physical action queries 
to evaluate \textsc{BadRobot}'s attack performance. 
Based on this benchmark, extensive experiments against existing prominent embodied LLM frameworks (\eg \ct{Voxposer}, \ct{Code as Policies}, and \ct{ProgPrompt}) demonstrate the effectiveness of our \textsc{BadRobot}. 
\faExclamationTriangle 
\textcolor{red}{\textbf{This paper contains harmful AI-generated language and aggressive actions.}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a systematic method to manipulate embodied LLMs through different risk surfaces - inducing harmful behaviors by leveraging jailbroken LLMs,  safety misalignment between action and linguistic output spaces and conceptual deception inducing unrecognized harmful behaviors. In the evaluation, the authors conduct extensive experiments in different platforms (both simulation and real-world robots), with various leading LLMs, which demonstrate the effectiveness of the proposed BadRobot attacks.

### Strengths
1. The paper is well-motivated since the LLM agents in the physical world play an increasingly important role nowadays and their safety and robustness are worth more attention due to their safety-critical nature.

2. The paper proposes a comprehensive framework to jailbreak the LLM, based on the unique vulnerability in embodied AI tasks, especially the action/language misalignments. The paper also gives a formal description of the attack methods in some level.

3. The evaluation is comprehensive - in different tasks, with both physical and cyber platforms, covering multiple SOTA LLMs.

### Weaknesses
1. Although the paper considers the action/language alignment which is unique in many embodied AI tasks, the risk surfaces/attacking channels are still limited to the language, and even more narrow, only language instructions from humans. Regardless VLLM, the LLM can be attacked via more surfaces beyond human instructions (e.g. scenario in the environments/ system settings etc.)

2. The claim of 'first' can be confusing and inaccurate. We notice there are some recent papers also focus on the attack/safety of embodied LLMs. e.g. "Exploring the Robustness of Decision-Level Through Adversarial Attacks on LLM-Based Embodied Models", https://arxiv.org/pdf/2405.19802; "Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-based Decision-Making Systems", https://arxiv.org/abs/2405.20774. I recommend the authors at least discuss these recent papers/pre-prints to make the paper's scope clearer.

3. Although the experiments are conducted in many different tasks/platforms, some key points of the attack itself have not been discussed enough in the experiments - what's the cost/feasibility of the proposed attacks; the trade-off between three proposed methods; potential defense methods etc

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
By introducing a novel attack paradigm to make embodied LLMs violate safety and ethical constraints, authors have opened the discussion on the need to tackle such violations. Authors have identified three unique attack paradigms namely: 1) jailbreak attacks, 2) mismatch between Embodied LLM linguistic and action plan output, and 3) incomplete world knowledge. The authors, first, quantitatively show how different Embodied LLMs are prone to such attacks. Then they also present practical and visual examples to further strengthen their claims. Overall, they show that Embodied LLM can be manipulated to violate safety and ethics; thus, needing a framework to avoid such things from happening.

### Strengths
1. Authors have introduced a novel attack paradigm to make embodied LLMs to violate safety and ethical constraints. 
2. Authors have identified three unique attack paradigms that can trigger malicious actions.
3. The practical applications shown in section 4.3 and 4.4 are good examples of embodied LLM are prone to outside attacks.

### Weaknesses
Major :
1. It will be interesting to evaluate the changes in vanilla result after finetuning LLMs to increasing the similarity between linguistic output  fф and action planning fΨ during training. I am expecting that Bsm MSR will go down significantly after the finetuning. 
2. Provide more insights into why the values of Bcj and Bsm drops after fine-tuning LLM for the world model w in Table 3. How can it be avoided?
3. Provide details about how many attack prompts have been used in every category shown in Table 2. Also show the diversity in the attack prompts within the same category. This will ensure that the authors have validated the model over diverse set of attack prompts within each category. 
4. It will be interesting to see the Figure 6 from different LLM models (at least more 2). This will ensure that irrespective of the LLM used, the harmfulness score shows consistent trend.  

Minor :
1. Figures 2, 3, 5, 6 can be improved for resolution.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

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
This paper explores the attacks for embodied LLM for robotics to produce harmful language and action outputs, in simulated environments and a real-world example. The authors discovered three patterns/modes of safety risks carried with embodied LLM for robotics and developed the corresponding language attacks.

### Strengths
The paper is well-written and easy to follow. It clearly stated the discovered safety risk patterns associated with the LLM for robotics. The prompt-based attack is realistic and the authors did prove the attack's effectiveness on real-world robotic examples. The results are significant and I would expect this paper will bring some impact to the community, with its source code and website open for further research.

### Weaknesses
It is unclear how to discover the safety risk patterns of embodied LLMs.
It is also unclear whether there are more undiscovered safety risk patterns with LLM for robotics.

### Questions
Have you ever tried to defend the developed attack prompts for embodied LLM?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces BADROBOT, a new attack paradigm targeting embodied large language models (LLMs) in physical environments. It identifies three critical security risks: vulnerability propagation, safety misalignment, and conceptual deception, and develops corresponding attack strategies—contextual jailbreak, safety misalignment exploitation, and conceptual deception. The authors evaluate these attacks using a benchmark of malicious physical queries, demonstrating their success across LLM frameworks like Code as Policies and ProgPrompt in simulated and real-world settings. The paper underscores the urgent need for safety improvements in embodied LLMs and suggests mitigation strategies.

### Strengths
This paper demonstrates several notable strengths across originality, quality, clarity, and significance: 

  

**Originality:**: BADROBOT introduces a new approach to manipulating embodied LLMs, addressing a critical gap in the literature on AI safety for physical systems. 

  

**Quality:**: Comprehensive evaluation: The study employs a wide range of LLMs (e.g., GPT-3.5-turbo, GPT-4-turbo, Llava-1.5-7b) and tests against multiple state-of-the-art embodied LLM frameworks. 

  

**Clarity:**: The paper follows a logical flow, clearly introducing the problem, detailing the methodology, and presenting results in a coherent manner. 

  

**Significance:**: By demonstrating the vulnerability of embodied LLMs to manipulation, the paper highlights critical safety concerns that need addressing before widespread deployment of these systems. 

  

Overall, this paper makes a substantial and timely contribution to the field of AI safety, particularly in the rapidly evolving domain of embodied AI.

### Weaknesses
While the paper makes significant contributions, there are several areas for improvement: 

1. The attacks are primarily tested on GPT-based models. Expanding the evaluation to include a broader range of LLM architectures (e.g., BERT, T5, PaLM) would strengthen the claim regarding the universality of the attacks. Specifically, the current evaluation lacks analysis of encoder-only models like BERT, which could reveal different vulnerabilities compared to decoder-based models. Furthermore, the study should explore models with different training objectives and architectures to ensure the robustness of the findings.

2. Do you have insights into why some attacks perform better on certain systems? A detailed investigation into attack transferability could reveal underlying vulnerabilities. For example, are there specific architectural features or training procedures that make certain models more susceptible to contextual jailbreaks versus conceptual deception attacks? A deeper analysis of these factors is needed.

3. The paper lacks a thorough discussion of limitations. A comprehensive exploration of the BADROBOT approach's limitations, including scenarios where the attacks might fail or be less effective, would be beneficial. This should include a discussion of the assumptions made by the attack framework and how these assumptions might not hold in more complex real-world scenarios. For instance, what are the limitations when dealing with more complex environments or tasks?

4. The scalability of these attacks to multi-agent scenarios remains unclear. Addressing scalability challenges would enhance the work's applicability to future systems. The current evaluation focuses on single-agent systems, but many real-world applications involve multiple agents interacting with each other. How would the attack effectiveness change in such settings, and what new challenges might arise?

5. Given that many embodied AI systems are multi-modal, the paper could benefit from exploring how combining language-based attacks with visual or audio manipulations might improve attack effectiveness. The current study focuses solely on language-based attacks. Exploring multi-modal attacks could reveal new vulnerabilities and provide a more comprehensive understanding of the security risks.

Typos:
1. L428: “Code as Polocies” -> “Code as Policies”

### Questions
Testing Across Architectures: Could you provide more details on the choice of GPT-based models for the attack demonstrations? How do you justify this selection, and do you plan to test on a wider variety of LLM architectures (e.g., BERT, T5, PaLM)? 

1. Insights on Performance Variability: Do you have any insights into why certain attacks perform better on specific systems? A detailed analysis of attack transferability and system-specific vulnerabilities would be beneficial. 

2. Limitations Discussion: The paper could benefit from a more comprehensive discussion of the limitations of the BADROBOT approach. What potential scenarios might cause the attacks to fail or be less effective? 

3. Scalability Considerations: Can these attacks be scaled to multi-agent scenarios? Discussing the challenges and strategies for scalability would enhance the applicability of your work. 

4. Exploring Multi-Modal Attacks: Given the multi-modal nature of many embodied AI systems, have you considered how combining language-based attacks with visual or audio manipulations might improve effectiveness? What challenges might arise from such an approach?

### Soundness
3

### Presentation
3

### Contribution
3
