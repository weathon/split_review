# Advantage Alignment Algorithms

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Artificially intelligent agents are increasingly being integrated into human decision-making: from large language model (LLM) assistants to autonomous vehicles. These systems often optimize their individual objective, leading to conflicts, particularly in general-sum games where naive reinforcement learning agents empirically converge to Pareto-suboptimal Nash equilibria. To address this issue, opponent shaping has emerged as a paradigm for finding socially beneficial equilibria in general-sum games. In this work, we introduce Advantage Alignment, a family of algorithms derived from first principles that perform opponent shaping efficiently and intuitively. We achieve this by aligning the advantages of interacting agents, increasing the probability of mutually beneficial actions when their interaction has been positive. We prove that existing opponent shaping methods implicitly perform Advantage Alignment. Compared to these methods, Advantage Alignment simplifies the mathematical formulation of opponent shaping, reduces the computational burden and extends to continuous action domains. We demonstrate the effectiveness of our algorithms across a range of social dilemmas, achieving state-of-the-art cooperation and robustness against exploitation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work aims to encourage cooperation in normal form games through opponent shaping. This is done by proposing Advantage Alignment, where the product of the advantages of the player's value-network and the opponent's value-network are used to update the policy. This means that, when advantages are aligned (i.e., they have the same sign), the log probabilities increase or decrease accordingly. The authors show theoretically that LOLA and LOQA, 2 other opponent shaping algorithms, also follow the advantage alignment principles. They then experimentally validate advantage alignment on Coin Game, Negotiation Game, and the high-dimensional Commons Harvest Open environment.

### Strengths
Strengths:
- This paper follows a long line of work on opponent shaping (LOLA, POLA, COLA, LOQA) and builds on LOQA to propose a new opponent shaping algorithm. While it feels a bit incremental, I find the work very well motivated, and theoretically justified. Extensive experiments on different domains and with relevant baselines confirm its practical performance.

### Weaknesses
Concerns:
- Having access to the opponent's value function results in a specific setting where all the player's preferences are public. The negotiation game completely changes if we know the preferences of the opponent, and we could devise a simple strategy that maximizes the average utility of both players. Since the utilities in this experiment are orthogonal to each other, there does not seem to be any real dilemma. For these reasons, I believe the insights gained from the Negotiation Game experiments to be limited. Specifically, the negotiation game setup, where agents have full knowledge of each other's value functions, reduces the problem to a simple optimization task, rather than a true test of emergent cooperation. The fact that the utilities are orthogonal further simplifies the problem, as there is no inherent conflict of interest that would necessitate complex negotiation strategies. The experiment, therefore, does not adequately demonstrate the algorithm's ability to foster cooperation in more realistic scenarios where preferences are private and conflicts are present.
- Advantage Alignment uses the product of advantages to align the policy. When there are more than 2 players involved (as in Commons Harvest Open), does the alignment depend on the product of the advantages of all players? If so, if a single agent does not cooperate, the whole alignment product fails. This would limit the scaling of Advantage Alignment to $n$ players. The concern here is that the method's reliance on a product of advantages across all agents could lead to instability and fragility in multi-agent settings. If the advantage of even one agent is negative, it could disproportionately affect the overall alignment, potentially hindering the emergence of cooperation. This raises questions about the method's robustness and scalability to environments with a larger number of agents.

### Questions
Additional clarification questions:
- Fig6 seems to indicate that Advantage Alignment is not really stable (increasingly noisy rewards, partial collapse towards the end of training against AC and AD). Is it sensible to hyperparameters? Or is there another reason for this behavior?
- Fig4 selects the best agent out of 10 seeds. Given the variance observed for the Negotiation Game in Fig6 (which granted is not the same game as Fig4), how representative are the results in Fig4?
- I am curious how Advantage Alignment can play against AD or AC if it can't change its policy (AD and AC are fixed policies). Doesn't this break Assumption 1?


Overall, I recommend for acceptance, for the strengths listed above (theoretically sound, well motivated, experimentally justified).

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper focuses on opponent shaping.  They propose an opponent shaping formulation that aligns the advantages of interacting agents, thereby simplifying the mathematical formulation of opponent shaping and reducing the associated computational complexity. In this formulation, the probability of future mutually beneficial actions is increased when their interaction has been positive. They demonstrate their methodologies' effectiveness on several social dilemmas and connect opponent shaping's past successes with this new advantage alignment formulation.

### Strengths
This paper is very well-written, and I appreciated how the authors helped the reader build intuition and understanding of the significance of their technique in section 4. The experiments served to reiterate the strength of their algorithm's performance, and the authors gave solid context for why each environment was selected.

### Weaknesses
The main concern I have with the paper is its individuality from the LOQA work, which concerns a similar technique, applied on similar problems, that achieves similar results. Both the more complex experiments (negociation and and harvest open) and the attached proofs in the appendix helped differentiate some of the beneficial aspects of Advantage Alignment in terms of scalability. However, the core mechanism of modifying advantages based on past interactions appears quite similar, and a more thorough comparison, perhaps with a controlled ablation study, would be beneficial to clearly delineate the novel contributions of this work. Specifically, it would be helpful to see a direct comparison of the performance of Advantage Alignment against LOQA on the more complex environments, to better understand the practical advantages of the proposed approach beyond the theoretical scalability arguments. The current experiments, while demonstrating the effectiveness of the algorithm, do not fully address the question of whether the performance gains are solely due to the use of PPO as a base optimizer, or if the advantage alignment formulation itself provides a significant improvement.

### Questions
- For the coin game, in the always defect case, LOQA receives slightly higher return than Advantage Alignment. Do you have any ideas for why this is?
-  In figure 3, there is mention of green values to show cooperation, but I do not see the green values in the figure.
- In Appendix 6, you mention that equation 59 uses the sum of past advantages of the agent up to the current time step and the advantage of the opponent at the current time step. Did you experiment with much tuning for number of terms to include in the sum of past advantages or number of future terms?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigated a long-standing research problem in multi-agent systems and game theory, named social dilemma. To address this problem, this paper stood on the side of opponent shaping and proposed a method that attempted to align advantages of various agents, to achieve a compromise between social welfare and self-interests. The main assumption lies in the connection between the opponent's policy gradient and the agent's policy parameters. Building on this, this paper proposed a paradigm called Advantage Alignment, and a corresponding RL algorithm based on PPO. This paper also unified other approaches of opponent shaping, such as LOLA and LOQA, in the paradigm of Advantage Alignment. The experimental results on various tasks showed the effectiveness of the proposed Advantage Alignment.

### Strengths
1. This paper proposed an original idea that derives the advantage alignment to implement the policy gradient with respect to the opponent (the opponent shaping term), which can reduce the computational complexity. This paradigm has been shown to have connections to previous opponent shaping approaches, which is a progress in this research direction.
2. The general quality of this paper is good. Although there are some technical points that I require some furtehr clarifications, most of proofs are correct to my best knowledge. The theorem proofs are actually dependent on assumptions raised in this paper, and assumptions are provided with explanations. The experiments were conducted on sufficient banchmarks, in comparison with multiple baselines. Furthermore, the results not only include the numeric results, but also involve some demonstrations of test case, which make the paper more comprehensive. 
3. This paper is well written. It has a clear motivation in Introduction and a thorough introduction of social delimma and opponent shaping. For those people who are not doing research in this direction, it is still friendly enough for them to catch up. 
4. As for the significance of the research problem, social delimma, it is surely a significant problem. The main reason from my own perspective is that it can simulate a class of social problems. About the opponent shaping direction, the significance to me is sceptical, since the requirement of opponent's knowledge seems like a bit strong assumption. However, I do not deny that this is a necessary step towards the weaker and more realistic assumptions. As a result, this paper is significant within the resesrch community of opponent shaping.

### Weaknesses
I have some technical concerns about this paper, which are specifically listed as follows:
1. In line 720, could you explain why the $\beta$ term is missing?
2. In line 739, could you give more details about how equation (16) is derived from equation (15)?
3. In line 755, could you give more details about how to transform from (19) to (8), step by step? Specifically, the transformation involves a double summation, and it is not immediately clear how the indices are manipulated to arrive at the final expression. A more detailed explanation of the index manipulation and the change in the order of summation would be beneficial.
4. In line 773, could you give more details about how equation (24) is derived from equation (23)?
5. In line 783, even with the assumption of orthonormal gradients, it is still not clear why equation (27) can be derived from equation (26). Could you please clarify this step by step? The orthonormality assumption implies that the dot product of gradients for different state-action pairs is zero, but it is not clear how this leads to the collapse of the sum to a single term. A more detailed explanation of how the orthonormality assumption is applied to simplify the summation would be helpful. It would also be beneficial to discuss the limitations of this assumption, and under what conditions it might not hold.
6. In line 792, is $A^{*}_{\text{LOLA}}$ equal to $V^{1}$?
7. In line 809, could you explain why $\alpha \nabla_{\theta_{2}} V^{2}(\theta_{1}, \theta_{2})$ is equal to $\Delta \theta_{2}$?
8. In line 1001, there is a typo: equation equation -> equation.

Additionally, I also have some concerns about the experimental analysis:

9. In the results shown in Figure 1b, could you give some intuitive interpretation on the asymmetry between the results of CD and DC? For example, is it related to your theoretical claims?

### Questions
See concerns in weaknesses. If the these concerns can be resolved, I will consider to raise the score. However, for the moment I can only give a reject due to those concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a novel method for opponent shaping based on the advantage functions of the interacting agents. The derivation unifies prior works through the lens of advantage alignment. Empirically, the proposed method is effective in learning complex coordination behaviors under various multi-agent environments.

### Strengths
- The proposed derivation is novel, and provides novel insight on opponent shaping methods
- The paper is theoretically grounded and well motivated.
- The resulting derivation unifies prior works nicely (Theorem 1 and 2).
- Broad suite of baselines and evaluation environments.

### Weaknesses
 - I wish Section 2 and 3 are more detailed, and cover more technical background on prior works. The additional information would allow the reader appreciate the contribution much better.
- The evaluation protocol is not provided. For readers that have little background in opponent shaping, it is not clear if the agent is trained prior to the evaluation or being trained (and thus adapted) during the evaluation episodes. Specifically, it is unclear whether the reported results are from a zero-shot evaluation against a fixed set of opponents, or if the agents are adapting during the evaluation phase. This distinction is crucial for understanding the robustness and generalization capabilities of the proposed method.
- It is not clear why increasing the log prob when both agents' advantages are negative is desirable (Eq. 8 and Fig. 1a). The intuition behind this design choice needs further clarification. For instance, what specific game-theoretic scenarios benefit from this behavior, and how does it prevent undesirable outcomes such as oscillations or instability?
- To my understanding, the proposed method does not outperform the baselines LOQA algorithm. The authors should discuss the differences and why it is desirable to use the proposed method over LOQA. A more detailed comparison, including specific scenarios where each method excels, would be beneficial.
- The paper claims that the proposed method is more efficient than the baseline but does not elaborate on this aspect. It would be helpful to quantify this efficiency gain, for example, in terms of training time or computational resources required.

Minor comments:
- The advantage function is not defined mathematically. This makes it difficult to follow the derivation and understand the precise meaning of the advantage terms.
- I believe Eq.2 is not the right expression, though I think this does not affect the main derivation of the paper. The equation appears to be missing a crucial component, and it is unclear how it relates to the standard definition of policy gradient.
- The connection between Eq.5 and Eq.6 is not explained. The transition between these two equations is not clear, and it is difficult to understand how the gradient of the squared policy is derived from the previous expression.

### Questions
- Could the authors explain how LOLA and LOQA and AdAlign are related? I see the derivation in Theorem 1 and 2 but do not understand the implication and how they differ in terms of their training objectives.
- It is not clear why increasing the log prob when both agents' advantages are negative is desirable (Eq. 8 and Fig. 1a). Can the authors elaborate on this?

### Soundness
3

### Presentation
2

### Contribution
3
