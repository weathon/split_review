# Moral Alignment for LLM Agents

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Decision-making agents based on pre-trained Large Language Models (LLMs) are increasingly being deployed across various domains of human activity. While their applications are currently rather specialized, several research efforts are under way to develop more generalist agents. As LLM-based systems become more agentic, their influence on human activity will grow and the transparency of this will decrease. Consequently, developing effective methods for aligning them to human values is vital. 

The prevailing practice in alignment often relies on human preference data (e.g., in RLHF or DPO), in which values are implicit and are essentially deduced from relative preferences over different model outputs. In this work, instead of relying on human feedback, we introduce the design of reward functions that explicitly encode core human values for Reinforcement Learning-based fine-tuning of foundation agent models. Specifically, we use \textit{intrinsic rewards} for the \textit{moral alignment} of LLM agents.  

We evaluate our approach using the traditional philosophical frameworks of \textit{Deontological Ethics} and \textit{Utilitarianism}, quantifying moral rewards for agents in terms of actions and consequences on the \textit{Iterated Prisoner's Dilemma (IPD)} environment. We also show how moral fine-tuning can be deployed to enable an agent to unlearn a previously developed selfish strategy. Finally, we find that certain moral strategies learned on the \textit{IPD} game generalize to several other matrix game environments. 
In summary, we demonstrate that fine-tuning with intrinsic rewards is a promising general solution for aligning LLM agents to human values, and it might represent a more transparent and cost-effective alternative to currently predominant alignment techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper points out a fundamental limitation of most current alignment approaches, which is that preference data is obtained from human participants that are highly noisy expressions of underlying values and end up in opaque models that are not interpretable.  The authors point out that a good alternative to this would be designing reward functions that explicitly encode values (or patterns of moral behavior) and use them for Reinforcement Learning-based fine-tuning of foundation agent models.  They validate their approach by constructing an iterated prisoner's dilemma environment and seeing how their fine-tuned models (tuned with various value-based policies) respond to tit-for-tat players or other LLM participants.

### Strengths
This is a fantastic paper!  It addresses a critical and highly understudied problem with a clever and interesting solution, the experiments are clear, simple, and well-executed and the writing is direct and easy to follow.

### Weaknesses
Though I love what the authors are doing here, a potential weakness of this approach, is encapsulated by this sentence in the introduction: "In
theory, our solution can be applied to any situation in which one can define a payoff matrix that captures the choices available to an agent that have moral implications."  But of course the trouble is that the world is very messy and complex place that often cannot be easily captured in a payoff matrix.  Now, the reason that economic games have gotten so much traction in the behavioral sciences is that they nicely capture the dynamics of the social world in neat packages that can be quantitatively studied in highly controlled environments -- and indeed the authors capitalize on that advantage.  Can they at least gesture at the challenges (and potential solutions?) to bridge their strategy with more open-world contexts?

I agree designing desired moral principles explicitly rather than using implicit preference comparisons is a good direction. There is work on this under the heading of constitutional AI or model specs. I worry that the approach taken in this paper is too simplistic, with hand-crafted rewards and no signs of nontrivial generalization, so that it doesn't really contribute relevantly to this important direction.

### Questions
Do the authors think that an interesting comparison to their system (fine-tuning via Reinforcement Learning with Intrinsic Rewards) would be simply prompting LLMs (eg GPT) do follow a natural language directive equivalent to the moral values they tested (eg, Deontological, Utilitarian)?  On the one hand, I could see this being an interesting baseline to beat.  On the other, there is much to be gained from the system that this paper describes beyond just the performance on these tasks, so I could see this comparison feeling a bit silly.  Curious what the authors think about this.  In general, it feels like having some baseline to compare performance to would be a good idea.


Small points:
Fig 3: label more prominently as depictions of the "unlearning" experiment.

### Soundness
4

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
4

### Summary
The paper introduces a new method for moral alignment of LLMs. Instead of using human preference comparisons, they suggest using intrinsic rewards to train an LLM for moral behavior. Specifically, they train on a dataset of games that are strategically equivalent to an iterated prisoner's dilemma, using two types of intrinstic reward: utilitarian and deontological. When trained with deontological rewards, models learn to cooperate against cooperators and defect against defectors, even when they were previously trained using game rewards and ended up always defecting. The paper investigates both training against a static opponent (tit for tat) and self-play. They test how the trained model generalizes to other general-sum bimatrix games and find that the models mostly continue to follow the moral framework they have been trained on.

### Strengths
- LLM moral alignment is an important topic, and especially the study of LLM agents in strategic interactions.
- I was able to follow along with the experimental methodology and results and they seem sound to me.
- Defining rewards intrinsic to games and training on these is an interesting idea that could help with alignment and avoid problems with inadequacies of human feedback. Moreover, game rewards might scale better than collecting human data.
- The authors do a great job visualizing the models' strategies graphically.
- The authors test generalization by using different tokens for the actions in the test games, to avoid simple token matching when generalizing.
- The authors compare extensively to relevant baselines, such as the base model, the game payoffs, and different ablations. They also perform both self-play and static opponent experiments. In general, I really appreciate all the thorough ablations.
- The authors use implicit ipd descriptions rather than specifically mentioning ipd/cooperate/defect, to avoid confounders from the model's preexisting knowledge about the ipd.

### Weaknesses
 - As far as I can tell, the deontological rewards are hand-designed. As such I don't currently see how this approach could be scaled to more games with more complex action spaces. Moreover, in the specific ipd setting, deontological rewards basically amount to specifically training the LLM to implement a tit-for-tat policy. The fact that the model can learn this policy when specifically trained on hand crafted rewards is not that interesting.
- When it comes to utilitarian rewards, these are not hand-designed, but I feel like training on utilitarian rewards is not interesting. The point of a strategic situation like the prisoner's dilemma is to model real-world conflict scenarios. Of course, if agents are all cooperative and care about each other, one can avoid conflict. But this is not feasible in the real world, where LLM agents need to act in the interest of the user. They should still be able to cooperate, but LLM agents that can be exploited and always try to appease other parties are not viable.
- The generalization results show that the model basically learns a static "cooperate/defect" policy and applies this to the different games. It would be much more interesting to see whether LLMs can adapt and behave differently depending on different payoff structures and strategic situations. The analysis of the Iterated Defective Coordination game does show that the utilitarian model fails to adapt, but this is not a very surprising result.
- Currently I do not see where the "LLM" really comes into play, other than being able to generalize to descriptions of other bimatrix games (though see my concerns about generalization above). My current impression from the results is that they don't really go beyond results one could have achieved with a simple parameterized conditional policy with 6 real-valued parameters. This is also supported by Section 8.9 in the appendix. Though I might have misunderstood something.
- Overall, studying training in games and using potential non-game rewards to incentivize cooperative equilibria is an interesting direction. However, I believe the experiments in the paper at hand are unable to make useful progress on this.

### Questions
- Do the models really understand the strategic situations they are in? One point of evidence in favor is that they seem to be able to find the equivalent "cooperate" and "defect" actions in other games, but it would be nice to have more evidence, such as asking the models follow-up questions about the games. Do you have any other evidence whether the models understand their strategic situation?
- I believe the background section is a bit too long. There is a lot of generic text that is not necessary to understand the core experiments with the ipd.
- Instead, I would be interested to see some examples of the games in the main text.
- From looking at Figure 6, I believe LLMs will be able to pattern match the payoffs to a prisoner's dilemma and thus infer that this is about prisoner's dilemmas. It would be interesting to use actual paraphrases of strategic situations which are ipd-like but don't have an explicit payoff matrix.
- I wouldn't use the term "unlearning" for the thing studied in this paper. Unlearning is a technical term used to describe removing knowledge from a model, not teaching the model a new strategy. The thing studied here is simply fine-tuning with a different initialization.
- I find the font in the plots for Figure 2 a bit small and hard to read.
- Is there a reason you use memory 1 policies? In principle, more than one iteration of the game would fit into an LLM's context window and would allow the LLM to make more sophisticated strategy judgments.
- Is it right that LLMs basically generalize by identifying the "cooperate" and "defect" options and then using the same policy as in the ipd? Have you tried permuting the two action labels and the columns/rows of the game descriptions? Have you observed cases where models change their actions in accordance with correct deontological judgments?
- Line 395+396 “static opponent” - is this still the tit for tat opponent?

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the possibility of aligning LLM agents by fine-tuning on intrinsic  moral rewards. Instead of implicitly representing human values during fine-tuning, as is done in methods like RLHF/DPO, the authors suggest directly specifying alignment goals by defining rewards based off moral philosophy frameworks. Namely, they fine-tune LLMs on the Iterated Prisoner’s Dilemma game using Deontological and Utilitarian rewards. They evaluate their approach using repeated social dilemma games in two settings: LLM vs another LLM, and LLM vs a tit-for-tat opponent. The authors then discuss how this can be generalized to other matrix games.

### Strengths
1. Aligning LLM agents to human values is a highly relevant and important research area.
2. The idea is interesting and I have no issues with any of the experiments. The authors do a good job of identifying the limitations of their method themselves, and other than those this is well-written research. Experimental results are thorough and comprehensive, and well cover key concerns I had as I read (e.g. anonymized names of action tokens, randomizing the action token order, etc). The paper is well-written and motivates their approach clearly.

### Weaknesses
As mentioned above, my main concerns here have been pointed out by the authors themselves already. Namely:

1. “A limitation of this approach
is that it requires the specification of rewards for a particular environment”, and
2. “An extension of this method to other environments would be of great interest, including fine-tuning agents with other payoff structures, more complex games or longer history lengths”

My primary concern is point 2; in my opinion, as-is this is a slightly weak paper and I would love to see this idea extended to more complex and interesting settings. Due to these limitations, I don’t believe this to be super impactful work - but I do think it is an interesting start. Hence, I would say it is marginally above the acceptance threshold.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
2
