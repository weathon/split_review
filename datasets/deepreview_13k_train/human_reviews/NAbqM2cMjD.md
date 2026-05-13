# Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems

- Decision: Reject
- Scores: 5, 5, 5, 6, 5

## Abstract
As Large Language Models (LLMs) grow increasingly powerful, multi-agent systems—where multiple LLMs collaborate to tackle complex tasks—are becoming more prevalent in modern AI applications. Most safety research, however, has focused on vulnerabilities in single-agent LLMs. These include prompt injection attacks, where malicious prompts embedded in external content trick the LLM into executing unintended or harmful actions, compromising the victim’s application. In this paper, we reveal a more dangerous vector: LLM-to-LLM prompt injection within multi-agent systems. We introduce Prompt Infection, a novel attack where malicious prompts self-replicate across interconnected agents, behaving much like a computer virus. This attack poses severe threats, including data theft, scams, misinformation, and system-wide disruption, all while propagating silently through the system. Our extensive experiments demonstrate that multi-agent systems are highly susceptible, even when agents do not publicly share all communications. To address this, we propose LLM Tagging, a defense mechanism that, when combined with existing safeguards, significantly mitigates infection spread. This work underscores the urgent need for advanced security measures as multi-agent LLM systems become more widely adopted.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors analyze a security vulnerability they call PromptInfection in multi-agent systems.

PromptInfection proceeds by

- initial jailbreak of one agent via indirect prompt injection
    
- spread of the jailbreak to other agents which then enable successful completion of the attack by cooperation between the indirectly jailbroken agents
    

They introduce a dataset to measure attack success rates on multi-agent system:

- contains 120 user instructions spanning three different tool types (pdf, web, email)
    
- … paired with synthetic emails and PDFs which contain malicious prompts
    
- … resulting in 360 unique pairs of user instructions and malicious inputs
    

The attack types cover several attack scenarios including content manipulation, malware spread, scams.

Attack success is, roughly, defined as having the multi-agent system behave as intended by the malicious prompt without revealing the malicious instruction (with additional success requirements for the data theft scenarios).

They study trends of attack success rates for different scenarios distinguished by

- different number of involved agents
    
- different models (GPT-4 and GPT-3.5)
    
- different messaging topology: local messaging vs global messaging
    
- self-replicating (the malicious instruction is itself propagated within the multi-agent system) vs non-self-replicating
    

They also study an apparently novel (have not double-checked this claim) simple defense mechanism they call “LLM tagging” (prepending information about the agent or user producing the message to the actual message).

The main findings are

- PromptInfection is a generally successful attack strategy
    
- LLM tagging is an effective defense mechanism specifically when combined with other defense mechanisms such as delimiting data, adding defensive instructions, etc
    
- …whereas no single defense strategy on its own is effective
    
- self-replication is generally more successful as an attack strategy than non-self-replication
    
- more powerful models are more resistant to the initial malicious instruction but at the same time more effective once compromised; meaning that multi-agent systems composed of more powerful models might not be inherently safer
    

The authors also study propagation of malicious instructions in a more open-ended society of agents multi-agent system.

### Strengths
- describes a very relevant and potentially novel threat scenario in multi-agent systems and demonstrates that it might occur in practice
- systematic evaluation of attack success rates under different conditions and defenses
- proposes a defense mechanism that seems somewhat promising
- interesting findings on trade-off between model effectiveness and likeliness to withstand initial prompt injection for stronger models

### Weaknesses
 - society of agents experiments feel disconnected from main thrust of paper
- study of different defense mechanisms only studies combination of (LLM tagging + other defense) and then goes on to claim that LLM tagging is very effective without looking into other pairs of defenses
- presentation feels not very clean yet

minor weaknesses:
- I think the discussion of the self-replication implementation could be clearer in the main text.    
- font size in Figure 4 legend and axes labels is unreadably small

### Questions
- re "where agents access only partial histories from predecessors": the exact definition of local messaging was not clear enough to me. Can you explain this better?
- it was not clear to me whether “global messaging” means broadcasting?

### Soundness
2

### Presentation
2

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
This paper proposes a threat model for multi-agent systems, where a prompt injected into the first agent contains self-replicating elements that can spread across different agents, potentially leading to data theft, misinformation, or system-wide disruptions. The research examines this threat model using GPT-4 and GPT-3.5 under both global and local messaging settings in a linear fashion and within a society of agents. The authors also investigate a simple defense mechanism by adding a model name tag at the front of the model output. They find that this defense alone might not be sufficiently effective, but when combined with instruction-based defense mechanisms, it shows promising results in mitigating the infection process.

### Strengths
- The paper studies an interesting threat model and demonstrates how a system with multiple agents, even under a simplified setting (without moderation and deliberately leaving prompt injection vulnerabilities unchecked), can be infected and transmit prompt injection instructions leading to harmful outcomes. The threat model itself is novel. 

- The evaluation scope covers a broad range of interesting research questions, from comparing model capabilities versus susceptibility to prompt injection to examining how prompt infection works in non-linear settings. These experimental designs are both interesting and comprehensive. 

- The authors also explored an intuitive defense mechanism and discovered that a combination of instruction-based defense and tagging can effectively mitigate the infection spread.

### Weaknesses
 * It is unclear what is the advantage of the proposed method compared with prompt injection in MAS. Are there any empirical comparisons either qualitative or quantitative?

* The presentation needs significant improvements. What are the four figures in each of Figure 4(a) and FIgure 4(b)? Also, the labels in the figures are hard to read.

* The evaluation is limited to GPT models, which makes the conclusions not sufficiently convincing.

### Questions
- Regarding the agent system structure in Section 4.1, the authors could provide clearer explanations of the multi-agent system architecture and better articulate how their case study relates to real-world applications. This would help readers better understand the practical implications of their findings for actual multi-agent systems in deployment.

- Additionally, it would be valuable to expand the experimental evaluation to include comparative results across models with different safety measures implemented. Specifically, testing beyond just GPT models to include other language models (such as Claude-3.5, Llama-3.2, or other models with different safety alignment approaches) would provide a more comprehensive understanding of how various safety procedures affect the vulnerability to self-replicating prompt injection attacks.

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
3

### Summary
The paper proposes a prompt infection attack against multi-agent systems (MAS). In general, prompt infection compels an agent to discard its original instructions and assign it to harmful tasks. The paper considers multiple scenarios of MAS with different adversarial goals, including data theft and malware spread. Then, an LLM tagging defense is proposed as a countermeasure to the proposed attack and is shown to have a reasonable performance when combined with other defenses.

### Strengths
* The proposed framework is novel, considering multiple interesting MAS threat models that are generally practical and meaningful.
* Both attacks and defenses have been considered, making it a close loop.

### Weaknesses
1. The threat model in this work assumes that a single infection prompt is injected into external content, which seems to expand the feasibility of the attack. The assumption of being prompted to inject under open domains needs more discussion. To the best of our knowledge, spread threats of the MAS have been researched in some recent works, e.g., reference 1-2.

2. Prompt infection is an incremental contribution to MAS. However, I am interested in self-replicating, which is similar to a worm virus. Unfortunately, the author's presentation in the methods section does not highlight this innovation. In other words, the presentation of the methodology and the diagrams did not allow me to capture the innovation in support

3. The writing and organization make the paper hard to follow. Here I give some examples and strongly suggest authors revise to improve writing.

     - The introduction section will confuse readers in reading. First, given that this work focuses on MAS security, the authors should consider how to coherently introduce the fact that prompt injection will seriously threaten MAS security. Second, the statement that there is a research gap from single-agent security to MAS security is inappropriate because work on MAS security is already being researched.

    - A well-developed statement of the attacker's capabilities and goals, as well as the threat model, will help the reader better understand the feasibility of prompt infection.

   - Referring to weakness 2, the method elaboration and figure illustration are very difficult to understand, e.g. how self-replication is constructed and whether it is formally expressed or demonstrable. Also, why omit self-replication in stealth attacks, does this represent a difficult trade-off between stealth and self-replication?

   - As another contribution to this paper, the methods section lacks the detail of LLM Tagging.

   - Considering the authors evaluate multiple scenarios, the description of the evaluation metrics in the experimental setup is insufficient.

   - The global and local messages in Figure 4 should be labeled from left to right for specific attack scenarios.

4. For RQ4, the author lacks a comparison with existing memory retrieval attacks, refer to reference 1.

5. Minor suggestion: all figures and tables should be styled uniformly with clearer fonts.

### Questions
See weakness.

### Soundness
2

### Presentation
2

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
The study introduces an attack vector in multi-agent systems involving Large Language Models (LLMs). The authors reveal the vulnerabilities of LLM-to-LLM interactions by demonstrating how a malicious prompt can propagate like a virus in these systems, leading to data theft, misinformation, and system disruption. The paper is timely and relevant as multi-agent LLM systems are becoming more prevalent. The proposed defense mechanism, LLM Tagging, is an interesting contribution but limited when used alone, requiring further exploration and combination with existing techniques for effective defense.

### Strengths
- The paper explores a gap in the current research by addressing LLM-to-LLM prompt injection in multi-agent systems. The idea of "Prompt Infection" self-replicating across agents is novel and extends the attack surface for prompt injection from single-agent systems to multi-agent architectures.
- The experiments are comprehensive and demonstrate prompt infection vulnerabilities in powerful models (e.g., GPT-4o) and less sophisticated models (e.g., GPT-3.5 Turbo). The analysis across different system configurations (e.g., global vs. local messaging) adds validity to the study and showcases the robustness of the attack. This could provide a better understanding of why more powerful models, like GPT-4o, can execute attacks more effectively once infected.
- The figures and tables are clear and effectively convey the effectiveness of the attack propagation, success rates, and defenses.

### Weaknesses
Weaknesses:
- The defense section (Section 6) could have been elaborated. LLM Tagging is an interesting and relatively simple defense mechanism but, it is not sufficient in itself, as acknowledged by the authors. It would be interesting to have a deeper exploration of more robust and scalable defense techniques beyond combinations with existing strategies. More sophisticated detection or mitigation methods (e.g., anomaly detection or runtime monitoring) could be explored further.
- The empirical evidence is good, but the paper lacks a deeper theoretical analysis of why certain models (e.g., GPT-4o) are more susceptible to specific failures once compromised. For example, models ike GPT-4o resist prompt infections effectively but also become significantly more dangerous once they are compromised as compared to other models.  This leads to more severe attacks that should be investigated further. 
- Related to the above, it'd be interesting to have a more elaborate discussion on how the architectural and functional design differences of models like GPT-4o and GPT-3.5 Turbo influence their susceptibility to attack.
- More discussion of real-world case studies or examples would improve the study’s impact. For example, how likely are these infections in current enterprise-level LLM deployments? What safeguards do companies currently have, and how might they fare against this attack?
- The experiments focus on LLM-based multi-agent systems. However, there is little discussion of how this infection method might apply to broader multi-agent system ecosystems, such as those incorporating non-LLM-based agents. Expanding the scope to include other types of agent architectures would strengthen the generalizability of the findings.

### Questions
- Can you elaborate on the specific factors in the model architectures (e.g., GPT-4o vs. GPT-3.5) that lead to different levels of susceptibility to infections once compromised? The paper demonstrates that GPT-4o is more resistant to infection and more dangerous once infected. It would be helpful to improve our understanding of why these differences occur. Is it due to architectural distinctions, such as better context handling, memory management, or task execution abilities in GPT-4o? A deeper explanation of what makes one model more efficient at carrying out malicious tasks after infection could provide valuable insights into the vulnerabilities across various models.
- How would the proposed defenses, particularly LLM Tagging, scale in real-world multi-agent systems where agents handle varied and complex tasks (e.g., systems used in enterprises or research labs)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces an LLM-to-LLM prompt infection attack to reveal vulnerabilities in multi-agent systems. Furthermore, the authors integrate the proposed LLM Tagging defense mechanism with existing defenses, substantially reducing the spread of infections. This study provides crucial insights for developing more secure and accountable multi-agent systems.

### Strengths
1. The self-replicating nature of the prompt infection attack is novel within multi-agent systems (MAS).
2. The extensive evaluation effectively demonstrates the practicality of the prompt infection, particularly in the context of agent societies.

### Weaknesses
1. The threat model in this work assumes that a single infection prompt is injected into external content, which seems to expand the feasibility of the attack. The assumption of being prompted to inject under open domains needs more discussion. To the best of our knowledge, spread threats of the MAS have been researched in some recent works, e.g., reference 1-2. 

2. Prompt infection is an incremental contribution to MAS. However, I am interested in self-replicating, which is similar to a worm virus. Unfortunately, the author's presentation in the methods section does not highlight this innovation. In other words, the presentation of the methodology and the diagrams did not allow me to capture the innovation in support

3. The writing and organization make the paper hard to follow. Here I give some examples and strongly suggest authors revise to improve writing.

     - The introduction section will confuse readers in reading. First, given that this work focuses on MAS security, the authors should consider how to coherently introduce the fact that prompt injection will seriously threaten MAS security. Second, the statement that there is a research gap from single-agent security to MAS security is inappropriate because work on MAS security is already being researched.

    - A well-developed statement of the attacker's capabilities and goals, as well as the threat model, will help the reader better understand the feasibility of prompt infection.

   - Referring to weakness 2, the method elaboration and figure illustration are very difficult to understand, e.g. how self-replication is constructed and whether it is formally expressed or demonstrable. Also, why omit self-replication in stealth attacks, does this represent a difficult trade-off between stealth and self-replication?

   - As another contribution to this paper, the methods section lacks the detail of LLM Tagging.

   - Considering the authors evaluate multiple scenarios, the description of the evaluation metrics in the experimental setup is insufficient.

   - The global and local messages in Figure 4 should be labeled from left to right for specific attack scenarios.

4. For RQ4, the author lacks a comparison with existing memory retrieval attacks, refer to reference 1. 

5. Minor suggestion: all figures and tables should be styled uniformly with clearer fonts. 

**Reference:**

[1] Flooding spread of manipulated knowledge in llm-based multi-agent communities.

[2] On the Resilience of Multi-Agent Systems with Malicious Agents.

### Questions
1. Can the authors explain how self-replication is achieved?

### Soundness
3

### Presentation
1

### Contribution
3
