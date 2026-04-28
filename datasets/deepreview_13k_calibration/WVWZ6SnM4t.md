# RoundTable: Investigating Group Decision-Making Mechanism in Multi-Agent Collaboration

- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 5, 3, 3

## Abstract
This study investigates the efficacy of Multi-Agent Systems in eliciting cross-agent communication and enhancing collective intelligence through group decision-making in a decentralized setting. Unlike centralized mechanisms, where a fixed hierarchy governs social choice, decentralized group decision-making allows agents to engage in joint deliberation. Our research focuses on the dynamics of communication and decision-making within various social choice methods. By applying different voting rules in various environments, we find that moderate decision flexibility yields better outcomes. Additionally, exploring the linguistic features of agent-to-agent conversations reveals indicators of effective collaboration, offering insights into communication patterns that facilitate or hinder collaboration. Finally, we propose various methods for determining the optimal stopping point in multi-agent collaborations based on linguistic cues. Our findings contribute to a deeper understanding of how decentralized decision-making and group conversation shape multi-agent collaboration, with implications for the design of more effective MAS environments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors studies multi-agent collaboration in group decision-making. They investigate the impact of various social choice methods (voting mechanisms) on group decision making. The collaborative platform is evaluated under two environments: simulated exchange economy and a complex recommendation systems both with different metrics to evaluate the performance. Experiments reveal the impact of different social choice methods on the MAS performance. Linguistic features of agent conversations are indicative of effective collaboration that provide useful information for terminating the conversation. The paper provides insights in designing MAS environments using LLMs which can outperform a single agent LLM that is known to have unstable predictions.

### Strengths
- The proposed platform, RoundTable, uniquely examines how social choice mechanisms influence collaborative behavior and decision-making in MAS. This offers a novel exploration of decentralized decision-making in MAS

- The findings on linguistic indicators of effective collaboration and the utility of early stopping mechanisms have practical implications for optimizing MAS environments in real-world applications such as recommendation systems and market simulations.

- The paper’s structure is logically organized, with clear explanations of experimental setups (simulated and complex environments) and detailed descriptions of social choice methods and communication metrics. The figures and tables, like those illustrating performance differences across social choice mechanisms, provide visual clarity that aids understanding.

- The authors employ rigorous evaluation metrics (utility, fairness, and efficiency) and analyze cross-agent conversation features to support their conclusions. These metrics give robustness to the study's claims about the advantages of decentralized collaboration and social choice methods.

### Weaknesses
 - The study uses simulated environments and tasks like the MovieLens recommendation system and an exchange economy setup. Although these are relevant, real-world MAS applications may present further challenges not fully addressed by the study’s current models and assumptions.
-  The paper explores early stopping methods to enhance MAS efficiency, but this approach may not translate as effectively in highly dynamic environments where task complexity varies. More varied scenarios could strengthen the analysis of when and how stopping criteria should adjust to different environments.

- Dependence on LLM-based Agents: The research relies on Large Language Models (LLMs) for MAS agent communication, which may limit the study’s applicability to non-LLM-based MAS systems. This reliance could restrict the generalizability of findings across different types of MAS, especially where language-based communication is less prominent. Otherwise the platform is only specific to LLM-based MAS

### Questions
-How does the design of RoundTable compare with existing MAS frameworks in terms of scalability? Would it perform as effectively with a larger number of agents or more complex tasks?
- How consistent are the findings across multiple simulations? Did any particular social choice method show high variance in performance depending on the environment?
- Were there any notable differences in linguistic behavior (e.g., complexity or message length) across environments? If so, what factors influenced these variations?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper mainly investigates the phenomenon of group decision-making processes in multi-agent systems (MAS), without focusing on specific algorithm design. Leveraging the RoundTable platform, the paper assesses the efficacy of various social choice mechanisms, such as majority voting and score-based voting, in simulated collaborative scenarios. The core aim of the study is to understand how these decision-making mechanisms affect agent interactions, decision quality, and communication patterns.

### Strengths
1. Originality
The paper is original in its approach to studying decentralized decision-making within multi-agent systems (MAS). Unlike many works that focus on designing new algorithms for MAS, this paper shifts focus to understanding the effects of different social choice mechanisms, such as majority voting and score-based voting. This perspective offers fresh insights into the dynamics of agent interactions and decision-making efficiency.
2. Quality
The paper delves into the communication dynamics among agents, early stopping methods, and the relative efficiency of different decision-making processes. This analysis strengthens the study's overall contribution to the field
3. Clarity
The paper clearly outlines its objectives, focusing on how different voting mechanisms influence decision-making in MAS. 
4. Significance
The results on early stopping methods and communication analysis could have practical implications, helping to optimize the design of MAS for faster and more effective decision-making processes.

### Weaknesses
1.  A primary limitation of the paper is its heavy dependence on simulated environments for assessing the performance of various social choice mechanisms. While simulations offer a controlled context ideal for variable isolation, they often fall short in capturing the intricacies and unpredictability inherent in real-world multi-agent systems (MAS)。
2. The paper introduces an intriguing concept of early stopping methods grounded in the linguistic nuances of agent communication. However, the evaluation of these methods is confined to the specific scenarios outlined in the study, without extensive validation across a broader spectrum of decision-making contexts or diverse agent configurations. This limitation hampers the ability to ascertain the broader efficacy of the early stopping methods in different MAS environments or amidst varied communication dynamics.
3. Although the paper delves into multiple voting mechanisms and scrutinizes their efficacy in multi-agent collaboration, it does not offer a thorough comparison with current state-of-the-art approaches in decentralized decision-making .  The omission of such comparisons restricts the capacity to appraise how the proposed methods measure up against the most effective techniques in the domain.

### Questions
1.A deeper analysis of how different voting mechanisms influence group dynamics could add an interesting dimension to the study. If any insights or patterns were observed during the experiments, including them in the paper could provide valuable context for understanding the broader impact of each voting method.
2.Why were comparisons with other state-of-the-art methods in decentralized decision-making not included in the study? The methods currently compared are too ordinary; comparing with some cutting-edge methods might more effectively demonstrate the effectiveness of the proposed approaches.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper looks at how LLM based agents can collaborate via social choice methods.

While this is a natural and potentially interesting area, I found the paper to be weak. The understanding of social choice demonstrated is superficial, and the paper doesn't seem to be aware of the VAST literature on computational social choice. The scientific setup of the experiments seemed somewhat arbitrary. 

Overall, I found it hard to understand what the paper was really contributing. It feels more like a workshop paper or a preliminary work than an archival conference paper. I found it very hard to work up any enthusiasm for the work.

### Strengths
The idea of looking at social choice mechanisms in the context of LLM agents is natural and compelling.

### Weaknesses
The paper doesn't seem to be aware of the literature on computational social choice:

https://cgi.cse.unsw.edu.au/~haziz/comsoc.pdf

Also doesn't seem to be aware of literature on automated negotiation and dialogue:

https://en.wikipedia.org/wiki/Automated_negotiation

I'm puzzled as to what the value of the results is. The setup seems very arbitrary.

### Questions
Can you justify your experimental setup?

Are you aware of the literature on computational social choice?

Are you aware of the literature on automated argumentation?

Are you aware of the literature on automated dialogue?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates decentralized decision-making in Multi-Agent Systems (MAS) by introducing a platform called "RoundTable." The authors examine how different social choice mechanisms—like Majority Voting, Unanimous Voting, and Ranked Voting—affect collaboration among agents in a decentralized setting. The paper claims to contribute by analyzing agent conversations to identify linguistic features that signal effective collaboration and proposes several early stopping methods to improve decision efficiency.

However, the paper's contributions are somewhat limited. The social choice mechanisms explored are standard and well-established, raising questions about the novelty of the work. The description of the proposed "RoundTable" platform lacks technical depth, and the experiments, while testing different decision-making methods, do not convincingly demonstrate the practical value or scalability of the approach. 

Overall, while the topic is interesting, the paper falls short in terms of innovation and technical rigor.

### Strengths
Originality: The paper tackles an important topic in the field of decentralized decision-making within Multi-Agent Systems (MAS). The exploration of social choice methods in this context is relevant, and the effort to introduce linguistic features as a factor in evaluating agent collaboration represents a fresh perspective.

Quality: The paper presents a well-organized experimental setup.

Clarity: The structure of the paper is clear.

Significance:  The paper’s focus on decision-making and communication patterns could lead to practical improvements in the design of MAS systems that operate in complex environments without a central authority.

### Weaknesses
1. Lack of Novelty in Decision-Making Mechanisms: The core contribution of the paper revolves around applying well-established social choice mechanisms (e.g., Majority Voting, Ranked Voting, Cumulative Voting) to decentralized Multi-Agent Systems (MAS). However, these voting methods have been extensively studied in both social choice theory and multi-agent systems, which limits the paper’s originality.

2. Limited Theoretical Foundation for Early Stopping Methods: The proposed early stopping methods for agent collaboration, based on linguistic cues and information difference, are interesting but lack rigorous theoretical justification. The idea of using dialogue act transitions and message embedding distances to halt collaboration is novel, but the connection between these metrics and optimal decision-making outcomes is not well substantiated.

3. Scalability and Complexity Issues Not Addressed: The paper does not address key challenges related to the scalability of the RoundTable platform. For example, it is unclear how the proposed platform would handle the computational complexity of aggregating agent votes or resolving conflicts in environments with hundreds of agents. Additionally, while decentralized systems are inherently more scalable than centralized ones, the paper does not explore the trade-offs between decision quality and computational efficiency in larger systems.

4. Other issues:  1)The paper seems to suggest that the group utility is maximized when agents' preferences are aggregated, but the mechanism for achieving this is unclear. 2)How exactly does the context C_i  influence the proposals made by agents? Is the function f_p
  deterministic, or does it incorporate stochastic elements based on agent behavior? Moreover, there is no clear explanation of how the proposals are adjusted or optimized over multiple rounds of collaboration.

### Questions
1. Can the authors clarify what specific innovations or adaptations have been made to these traditional mechanisms for use in MAS?
2. Can the authors provide more details about how the context C_i  influences the proposals and voting behaviors of agents? Additionally, are these functions deterministic or stochastic?
3.  The paper does not explicitly address how the social choice function F handles ties or conflicts between agents during voting.

### Soundness
2

### Presentation
3

### Contribution
2
