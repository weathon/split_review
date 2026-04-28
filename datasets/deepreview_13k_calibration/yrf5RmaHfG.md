# JuxtAlign:  A Foundational Analysis on Alignment of Certified Reinforcement Learning

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Sequential decision making in highly complex MDPs with high-dimensional observations and state dynamics became possible with the progress achieved in deep reinforcement learning research. At the same time, deep neural policies have been observed to be highly unstable with respect to the minor sensitivities in their state space induced by non-robust directions. To alleviate these volatilities a line of work suggested techniques to cope with this problem via explicitly regularizing the temporal difference loss for the worst-case sensitivity. 
In this paper we provide theoretical foundations on the failure instances of the approaches proposed to overcome instabilities of the deep neural policy manifolds. Our comprehensive analysis reveals that certified reinforcement learning learns misaligned values. Our empirical analysis in the Arcade Learning Environment further demonstrates that the state-of-the-art certified policies learn inconsistent and overestimated value functions compared to standard training techniques. In connection to this analysis, we highlight the intrinsic gap between how natural intelligence understands and interacts with an environment in contrast to policies learnt via certified training. This intrinsic gap between natural intelligence and the restrictions induced by certified training on the capabilities of artificial intelligence further demonstrates the need to rethink the approach in establishing reliable and aligned deep reinforcement learning policies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors provide a theoretical and experimental of analysis of certified robust training of Q-values for reinforcement learning. Certified robost training is a method for adversarially training neural networks such that they are robust to small perturbations in the input values. In the case of reinforcement learning in particular, this is implemented as a regularizer added to the standard temporal difference loss, where the regularizer penalizes Q functions for which a perturbation in the state $s$ can result in a change in the action that produces the _maximum_ Q-value. The authors provide an existence proof that this style of training can produce misalignment amongst the sub-optimal Q-values, which they claim is a departure from natural intelligence which is able to properly order counterfactual actions. They demonstrate this phenomenon experimentally in several games in the Arcade learning environment, by showing that the performance drop incurred when selected the second best action some percentage of the time, instead of the optimal action, is much higher for adversarially trained RL than for vanilla RL. Additionally, they show that selecting the worst action some percentage of the time leads to a larger performance drop for vanilla RL than adversarial RL, again indicating that vanilla RL produces a better ordering over sub-optimal Q-values.

### Strengths
- The paper is fairly clear - the existence proof is very detailed and easy to follow. Certain areas like Figure captions need some improvement
- The authors provide an original contribution - the misalignment of sub-optimal Q-values in adversarial training has not been observed before
- Experiments are convincing, at least of the existence of mis-aligned Q-values with adversarial training. The construction of the experiments (i.e. using the second best action or worst action) is intuitive and well-explained/motivated

### Weaknesses
Major Issues:
- Overall, the main claim of the paper could be better motivated with a better argument for why it matters if sub-optimal Q-values are misaligned, particularly for a method that is specifically designed to be robust to changes in the _optimal_ Q-values. The authors mainly motivate the importance of this by the divergence from natural intelligence however (a) it is not entirely clear why a departure from natural intelligence is necessarily a bad thing and (2) the claims that this is a departure from natural intelligence don't seem to be fully supported (see next point). The author's suggest that misaligned sub-optimal Q-values present a vulnerability which could perhaps be a good motivation - could you provide specific examples of how misaligned sub-optimal Q-values could be problematic or exploited in practical scenarios? For instance, in a multi-agent setting, could an adversary exploit the misaligned Q-values of a robustly trained agent by forcing it into a state where the second-best action is actually detrimental, or could this lead to a failure in generalization when the agent encounters a novel state where the optimal action is unavailable?

- The paper specifically makes the claim that adversarially trained Q-values are not well-aligned with natural intelligence compared to vanilla RL Q-values. However, this claim seems too strong for the results that are actually presented in the paper. The author’s argument for this claim seems to be that previous work in neuroscience i.e. Fig 1 demonstrate that humans _can_ assign correct ordering to counterfactual actions in a particular decision making task. But do humans _always_ assign correct ordering? Are there any limitations to this ability? The authors demonstrate theoretically and empirically that there exists cases where adversarial training produces misaligned Q-values. However, it seems like to make a claim about natural intelligence alignment, the authors would have to actually test natural intelligence on the same tasks, particularly since the proof is an existence proof. Admittedly, I am not too familiar with the neuroscience literature so if the authors could provide more comprehensive evidence from neuroscience literature to support their claim, this would be helpful. Alternatively, I do not necessarily think the claim about alignment with natural intelligence is necessary, so the language could be toned down a bit. It would be more convincing to focus on the practical implications of misaligned Q-values, such as their impact on generalization or robustness in complex environments, rather than relying on a comparison to human behavior.

- The captions of several figures are not very informative and need to be guessed at by the reader. For example, in Fig 2 there is no description of what the bar chart is displaying, there are images from Atari games with no description of what the reader should be paying attention to and the brain scan similarly has no context. For the bar graph, it would be helpful to provide the environment details, details of how the Q-values were estimated and the source of the natural intelligence data. Similarly, Fig 3 has no mention of what each of the three panels is - the caption says Adversarial and Vanilla, but the superscript on all the x-axis Q-values is "Adv". Please explain what each of the three figures represent and make sure the axes are correct. The placement of Fig 3 is also odd, since it isn't mentioned in the text until Section 4.3 - I would either move it to that section or mention it in the text earlier.

Minor issues:
- The axes and text in the plots are much too small. Fig 6 is particularly bad.
- It might be more intuitive to plot the performance drop as a negative value, so that the plots have the worse performing curve lower than the best performing curve
- In the first paragraph of 4.1, $\mathcal{P}_w$ is mentioned before it is defined
- Table 2 is never mentioned in the text

### Questions
- Is there some relation that can be drawn between this phenomenon and policy churn [1]? Perhaps this provides a different avenue to motivate this work.
- Do sections 4.1 and 4.2 make different points? They have different titles (randomized vs misaligned) but the claims seem the same?

[1] Schaul, Tom, et al. "The phenomenon of policy churn." Advances in Neural Information Processing Systems 35 (2022): 2537-2549.

### Soundness
3

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
3

### Summary
The paper approaches critically and formally recent advances in certified RL. It shows how these novel RL schemes aiming to learn robust policies, actually induce policies that are misaligned with natural intelligence. Moreover, they perform a rigorous theoretical analysis of such misalignment thus formally proving failure cases of such RL schemes.

### Strengths
CLARITY and QUALITY:
1. The paper is generally well-written, presents a clear problem, and clear derivations.
2. It help the reader to follow the main argument logic step by step and presents clear mathematical statements of the conclusions derived.

SIGNIFICANCE and ORIGINALITY:
1. The comparison with natural intelligence seems particularly interesting and likely novel.
2. The problem treated is important and has already received significant attention in other communities (e.g., computer vision), but arguably less in RL so far. Hence I believe it is an important direction of investigation. 
3. Regarding the significance of the derived results I have doubts expressed via the points/questions below. Especially points (1) and (3) regarding related works and formal implications.

### Weaknesses
CLARITY and QUALITY:
1. At points writing is not particularly sharp (e.g., the list of contributions could be significantly shorter and clearer). Often, diverse and not fully clear words are used to describe things (e.g., 'resilience' in line 137 - what does it formally mean?) or the terminology lacks cohesion (e.g., the word certified is not introduced in the introduction, where the related research line is introduced with alternative terminology).  
2. Example in pag. 4 might be hard to follow. I’d suggest to add a drawing with states/actions etc.
3. The paper does not seem cohesive in terms of storyline. In particular, it seems it has two themes: (1) showing the relationship between natural decision-making and RL with and without certified methods, and (2) showing formally the limits of certified methods. Although both are relevant topics, I fail to see clearly the connection between the two. Maybe the authors have a clear picture in mind connecting the two themes, but currently the alternation between them renders the paper not cohesive and feels like reading two papers forced into one via unclear motivations and connections. This is related with point (2) below.



ORIGINALITY / SIGNIFICANCE / GENERAL:
1. Related works mention adversarial training schemes in general (not specific to RL), then present recent works specific for RL with positive results and finally some with negative non-theoretical results towards claiming that this work is the first showing formally the limitations of these RL schemes. What I am missing is the following: since these algorithmic ideas are far more general than RL as they boil down to regularized optimization schemes (that have been for instance explored vastly in computer vision, NNs etc.), aren’t there works showcasing their fundamental limitations (formally) in general that can therefore trivially hold also for RL, where NNs are used to represent the policy?
2. Even within the abstract the authors state ‘’This intrinsic gap between natural intelligence and the restrictions induced by certified training on the capabilities of artificial intelligence further demonstrates the need to rethink the approach…”. Why? Human/animals and machines clearly have different design spaces (i.e. have different limits and capabilities) so there is no reason to believe that machine intelligence has to be bound to schemes emerged in human/animal intelligence, which is arguably very limited and/or peculiar in terms of resources (e.g., sensors to minimize statistical complexity, and compute machinery). It seems to me that to evaluate (and compare) intelligence one should define measurable objectives rather than expecting certain specific behavior. 
3. I am having a hard time understanding the main message from Theorems 3.6 and 3.7. These seem portrayed as negative results as they show value function reordering for sub-optimal actions, but to the best of my understanding they seem also to claim that the value function properly identifies the optimal action, which seems to me what matters for achieving provably optimal policies in RL schemes (e.g., Q-learning). What am I missing (formally)?
4. What is the point of plotting the defined Performance Drop rather than a classic RL performance measure? I understand why the Performance Drop would show results aligned with your thesis, but, as mentioned in the previous point, it seems not aligned with classic RL schemes optimality measures.

### Questions
I have listed questions within the points above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
JuxtAlign studies alignment of certified RL using ideas of natural intelligence from neuroscience. The authors imply orthogonality of natural intelligence and adversarial training used often in robust RL.  The paper contains a theoretical and an experimental analysis of the phenomena

### Strengths
1. The paper contains a theoretical foundation for the analysis
2. The paper presents an experimental analysis of robustness and natural intelligence.

### Weaknesses
1. The presentation can be improved as it was hard for me to fully assess the results. Perhaps I missed something, but I didn't get the main message.
2. It’s well known that robustness, adversarial training are blunt tools in the sense that they try to avoid all possible outcomes as designed. For example, we can take a worst-case action within a ball of possible actions. If we re-design these training tools with a more constrained scope then the results will be different. Therefore, I don’t quite understand how we can make general conclusions on certified training vs natural intelligence from this study.
3. In extreme situations, robust training can result in trivial policies - do not do anything. Therefore, I don’t find it surprising that sometimes robust training is different from what we perceive as naturally intelligent. 
4. The theory seems to be based on the Danskin theorem, which can be applied only to C1 Q-functions. I believe this is a quite restrictive setting. In min-max problems it’s even more restrictive. 
5. Overestimation in Q-functions is a general problem in RL, not just in a robust setting. But I agree that in robust settings it will be more acute. However, using overestimation as a reason for misalignment in this context is not entirely correct and can be misleading.

### Questions
Minor comments 
1. Line 213 - typo
2. I am bit confused about the depiction of the brain and video games in Figure 2. Why are they there?
3. Def 4.2. The formulation is slightly confusing "For any $\tau >0$..." in the begining of the sentence typically implies that the condition must be valid for all $\tau > 0$ for the definition to hold. I think here the authors mean "for some $\tau >0$", which is better to place closer to the end of the sentence.

### Soundness
2

### Presentation
1

### Contribution
2
