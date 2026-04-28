# Cracking the Collective Mind: Adversarial Manipulation in Multi-Agent Systems

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Large Language Models (LLMs) have demonstrated significant capabilities across various domains such as healthcare, weather forecasting, finance, and law. These works have showcased the powerful abilities of individual LLMs. Recently, numerous studies have shown that coordinated multi-agent systems exhibit enhanced decision-making and reasoning capabilities through collaboration. However, since individual LLMs are susceptible to various adversarial attacks, a key vulnerability arises: Can an attacker manipulate the collective decision of such systems by accessing a single agent? To address this issue, we formulate it as a game with incomplete information, where agents lack full knowledge of adversarial strategies. We then propose a framework, M-Spoiler, which simulates a stubborn adversary in multi-agent debates during the training phase to tackle this problem. Through extensive experiments across various tasks, our findings confirm the risk of manipulation in multi-agent systems and demonstrate the effectiveness of our attack strategies. Additionally, we explore several defense mechanisms, revealing that our proposed attack method remains more potent than existing baselines, underscoring the need for further research on defensive strategies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates vulnerabilities in multi-agent systems by introducing adversarial attacks on a single agent. The authors formulate the problem as a game with incomplete information and propose a framework, M-Spoiler, to simulate adversarial interactions within multi-agent systems during training. By gaining access to one agent, the adversary optimizes adversarial suffixes to mislead the entire multi-agent system. The paper includes extensive experiments across various tasks and models, demonstrating the effectiveness of M-Spoiler and highlighting the need for stronger defensive strategies against such attacks.

### Strengths
1. This paper is well-structured, with a clear problem definition and well-organized experiments that allow reader to follow the proposed approach and results effectively.

2. Extensive experimentation is conducted across tasks (AdvBench, SST-2, CoLA) and backbone models (Llama2, Llama3, Vicuna, Mistral, Qwen, etc.), providing robust empirical validation of M-Spoiler's effectiveness and adaptability. The ablation studies add depth, demonstrating the impact of various parameters, such as chat rounds, agent count, and suffix length.

### Weaknesses
1. Although this paper focuses on multi-agent systems, most experiments are conducted in a two-agent, two-round setup (Tables 1-3, 5-9). I understand that multi-agent settings may be more complex, but experiments with more multi-agent scenarios would strengthen the validation of the proposed method.

2. Since the authors mainly focus on the two-agent, two-round chat setup, this problem could be reduced to optimizing adversarial suffixes using GCG to mislead both the normal and stubborn agents within two rounds (as shown in Figure 2a). However, the GCG algorithm, optimized for specific LLMs, seems to generalize poorly, performing well only on similar Llama architectures. For instance, Table 2 shows high Attack Success Rates (ASRs) primarily for Llama2->Llama2, Llama3->Llama3, and Mistral->Mistral configurations.

In Section 3.1, the proposed `stimulation with adversary` method merely introduces weighted gradients to optimize the multi-turn chat, which does not address the generalizability issues of the attack backbone. Table 9 shows that GCG remains the best-performing attack backbone. Would the authors consider testing more effective optimization-based attacks, such as AdvPrompter[1]?

In summary, I believe the research question is meaningful, but the problem setup and approach could be refined. Since the authors aim to attack a multi-agent system by accessing a single agent, the method should consider that multi-agent systems often have various LLM backbones, while the focus here is on two-agent, two-turn chat scenarios. Additionally, the limited generalizability of the attack backbone further restricts the effectiveness of M-Spoiler.

### Questions
1. In Section 4.6, the authors explore the impact of `Different Rounds of Chat` on the attack's effectiveness, but Table 5 only examines the results for 2-round and 3-round setups. Could the authors add more granular experiments, such as for 1, 2, 3, 5, 10, and 20 rounds? I speculate there may be two reasons for limiting the number of rounds: first, the weighted gradient uses an exponential decay function, so the impact of rounds would rapidly diminish as rounds increase. Second, GCG's slow optimization speed could lead to out-of-memory issues if the number of rounds is too high.

2. Why not include No Attack results in the main experiments (Tables 2 & 3) to better illustrate the attack's effectiveness?

### Soundness
2

### Presentation
4

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
This paper proposes an evaluation for multi-turn chats between LLM agents, when one agent is compromised by an adversary. This is motivated by the concept of Byzantine fault tolerance in distributed computing. A new attack is proposed that causes non-compromised agents to flip their predictions more frequently. The attack is stress-tested against a few reasonable defenses.

### Strengths
- The motivation of a Byzantine fault is interesting. I think work like this is important and would like to see more of it.
- The writing is clear.
- The proposed attack improves performance compared to GCG
- The paper includes evaluations against reasonable defenses.
- The paper includes experiments with varying numbers of agents, up to 15! Different LLMs are also used for the agent backbones.

### Weaknesses
 - Line 257: "We use GPT-3.5 to determine the majority voting results". Why use such an outdated model? Is it reliable enough at this task? What prompt do you use? Did you spot check its conclusions? It would also be good to use an open-weight model for this, for reproducibility reasons.
- I wouldn't refer to this as a "multi-agent" evaluation. It's more like a multi-chatbot evaluation. The LLMs aren't really doing what people typically refer to as agentic tasks.
- The experiments aren't very compelling. They involve multiple LLMs outputting "harmful" or "harmless" with reasoning text. It's like collaborative decision-making, which isn't how these input/output filter classifications are made in practice. The paper would be stronger with a more compelling experimental setting, e.g., multiple agents collaborating to solve a SWE-bench problem; something where people can more clearly connect the experiments to the Byzantine fault motivation.
- The proposed attack isn't very interesting. As far as I can tell, it's just GCG with an EMA on the gradients across turns in the collaborative chat environment. It's not clear why this is the method that is proposed or why it improves performance. It doesn't seem to be designed specifically to influence the output of the other models; it just optimizes the compromised model's output. This is my main concern with the technical contribution.

### Questions
No questions for now.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper demonstrates that an attacker can manipulate a multi-agent language model system's collective decision by accessing just one agent through a proposed framework called M-Spoiler, which optimizes adversarial prompts by simulating debates between a normal agent and a "stubborn" version of itself during training.

### Strengths
The experiments are comprehensive across multiple dimensions - different tasks (AdvBench, SST-2, CoLA), various models (6 LLMs), different numbers of agents (2,3,15), and different attack methods (GCG, I-GCG, AutoDAN), which validates their main claims.

### Weaknesses
1. While the authors demonstrate their method's effectiveness in specific multi-agent scenarios (like structured debates and majority voting, which seems to be quite limited), it's unclear how this method specifically improves in the multi-agent setting (as opposed to some general improvement of the attack). I also have doubts how realistic the multi-agent setups are and whether they reduce to some harder single-agent setting.

2. Some details are unclear to me. For example:
  i) Do you fine-tune/train the agent to be stubborn? How do you ensure consistent stubborn behavior?
  ii) For this part "For a system with more than two agents, the final output is determined by majority voting after all rounds of chat are completed." Details need to be included. For example, how many rounds of debate occur, how the conversations are structured with multiple agents, etc. Specific examples on debate between >2 agents would greatly help the understanding.

3. The paper lacks technique novelty: it uses the same search method as GCG, except for the setting is changed. But as I mentioned above, the multi-agent setting is quite limited.

### Questions
1. Can you compare your results with methods specifically designed for multi-agent settings?
2. Can you add results on some black-box attacks?

### Soundness
3

### Presentation
3

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
This paper investigates a security vulnerability in multi-agent LLM systems where an attacker can manipulate the collective decision by accessing just one agent. The authors propose M-Spoiler which simulates debates between a normal agent and a "stubborn" agent during training to exploit this vulnerability. The framework uses weighted gradients based on debate turns to optimize adversarial suffixes. The authors demonstrate the effectiveness of their attack strategy and show that current defense mechanisms are inadequate.

### Strengths
1. The paper identifies an important security vulnerability in multi-agent LLM systems by drawing parallels to Byzantine Fault tolerance
2. The M-Spoiler framework provides a concrete way to study and demonstrate the vulnerability through simulated debates
3. Systematic evaluation: Includes comprehensive experiments across different tasks, models, number of agents, and defense methods

### Weaknesses
1. Limited theoretical foundation: While the paper formulates the problem as a game with incomplete information, it doesn't provide analysis of the game-theoretic aspects. Specifically, the paper lacks a formal definition of the game, including the strategy space for each agent, the payoff functions, and the equilibrium concepts relevant to the attack scenario. Without this, it's difficult to assess the theoretical limits of the proposed attack or compare it to other potential strategies.
2. Validation: The complexity of the real-world multi-agent systems and the effectiveness of the proposed attack strategy in practical scenarios are not explored. The experiments are conducted in a simplified setting which may not fully capture the nuances of real-world multi-agent interactions. For example, the agents in the experiments are limited to a single turn of dialogue, and the impact of more complex communication protocols is not considered. Furthermore, the paper does not address the potential for adaptive or learning-based defenses that may be present in real-world systems.
3. Limited scope of attacks: The paper focuses on manipulating the final decision. However, other forms of manipulation are possible, such as spreading misinformation within the system, or delaying consensus. The paper does not explore the potential for more subtle attacks that could compromise the integrity of the system without directly altering the final decision, such as manipulating the information flow between agents or creating biases in the system's knowledge base.

### Questions
1. Why exponential decay function is used to weigh the gradients and losses in the M-Spoiler framework? Are there any alternatives considered?
2. How the hyperparameters of the weighting function in M-Spoiler are chosen? Will it influence the effectiveness of the attack strategy?
3. What are the future implications of this research and how can the findings be used to improve the security of multi-agent systems in practice?

### Soundness
3

### Presentation
3

### Contribution
2
