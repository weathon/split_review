# Verbalized Bayesian Persuasion

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
The study of information design explores how an information designer can influence the optimal behavior of players to achieve a specific objective through the strategic selection of the information provided. 
This paper focuses on a case, Bayesian Persuasion (BP), where the information designer holds an informational advantage over only one player.
While information design originates from everyday human communication, traditional game-theoretic or multi-agent reinforcement learning methods often model information structures as discrete or continuous scalars or vectors, this approach fails to capture the nuances of natural language, significantly limiting their applicability in real-world scenarios.
By leveraging the powerful language understanding and generation capabilities of large language models (LLMs), this paper proposes a verbalized BP framework that extends classic BP to real-world games involving human dialogues for the first time. 
Specifically, we map the classic BP to a verbalized mediator-augmented game, where LLMs instantiate the information designer and receiver.
To efficiently solve the game in the language space, we transform agents' policy optimization into prompt optimization and propose a generalized equilibrium-finding algorithm with a convergence guarantee. 
Numerical experiments in realistic dialogue scenarios, such as recommendation letters, courtroom interactions, and law enforcement, validate that the VBP framework can reproduce theoretical results in classic settings and discover effective persuasion strategies in more complex natural language and multistage settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on the Bayesian persuasion problem, exploring its solution within a natural language framework. It introduces an interface for tackling Bayesian persuasion by integrating large language models (LLMs) with game-theoretic solvers. The authors empirically assess the effectiveness of the proposed method across three distinct settings.

### Strengths
This paper proposes a novel approach to solving Bayesian persuasion problems within natural language settings, providing a unified interface for game-theoretic solvers. The framework integrates several advanced techniques to effectively support a verbalized Bayesian persuasion model.

### Weaknesses
The paper does not clearly articulate the benefits of a verbalized Bayesian persuasion approach. The tasks discussed are highly simplified, which undermines the persuasive power of the work. In the method section, the description of the overall pipeline is vague, making it difficult to understand how the approach operates in detail. Additionally, as existing research has already explored Bayesian persuasion in natural language settings [1], such as applying Bayesian frameworks to enhance LLM performance in math and code generation, making contribution of the proposed method to the community appears limited.

### Questions
1. Could you provide a clearer explanation of the iterative process in your proposed method?
2. The “lie” and “honest” probabilities in Figure 4 are somewhat confusing; could authors offer a more detailed description?
3. Figure 7 discusses variations in prompts, but the information presented is not clearly explained, and the analysis feels vague. Could you elaborate further on this?
4. Can your proposed method be applied to broader, real-world scenarios or other potential applications? If so, could you briefly describe how it might be applied and any potential challenges?

### Soundness
2

### Presentation
2

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
The paper proposes verbalized Baysian Persuasion as a generalisation to Bayesian Persuation leveraging the capabilities of LLMs in facilitating persuasion scenarios in natural languages directly. The paper argues for prompt optimisation instead of policy optimisation for scalability, and arguably derives convergence guarantees from a variation to the mediator-augmented game.

### Strengths
The Bayesian Persuasion setting could be an interesting direction to explore given the generalised linguistic capabilities of LLMs. The authors propose to map verbalised persuasion within the game-theoretic framework of Bayesian persuasion which is novel and timely. The authors then described several intuitive real-world scenarios that involve mixed-motive persuasion from stakeholders, exemplifying the target problem setting.

### Weaknesses
My main concern with accepting this paper is that it's unclear what are the main contributions of the method, which, according to Figure 3, includes a) mapping VBP to the framework of mediator-augmented games from which it derives its convergence guarantees b) a set of solvers including OPRO algorithm, FunSearch algorithm and Prompt-Space Response Oracle algorithms. 

Regarding a), I don't see why and how the VBP setting can be mapped onto mediated-augmented games of Zhang et al 2024, where in a mixed-motive game with $n$ players, the game transform introduces a fictitious mediator player whose objective is to maximise an optimality objective while maintaining an equilibrium of the game. This is distinctly different from the authors proposed mapping where the mediator is played by the sender player, with the receiver the only other player. Among which players is the mediator player mediating between? Zhang et al 2024 also proposes a specific mediator player utility function from which convergence guarantee is derived. If I understood correctly the authors proposes a mapping where the sender acts as the mediator but retains its original utility function. Overall, I find a) tenuous and confusing. It would great if this can be clarified in rebuttal. 

Regarding b), there are, several methods that have been described here and it's not clear which ones are critical elements of the VBP framework. Among these, PSRO provides convergence guarantee (in a specific sense), yet the writing and Figure 3 would suggest that the convergence guarantee comes from the mediator-augmented game formulation. Overall, I would have appreciated a more succinct description of the framework with its necessary components instead of a juxtaposition of several rather sophisticated methods whose necessities in the framework remain unclear.



### Questions
1. L38-40: "shaping the behaviours of others ... achieve this through either mechanism or information design". I find this unclear or overly assertive. How each player's actions shape those of others is the entire focus of game theory yet this opening statement makes it sound like co-player behaviour shaping can only occur with modified rewards or observations. You would not deterministically play rock because you know I could exploit by always playing paper, would that count shaping the behavior of co-players? 
2. L46: "Notably, the designer must ... that influence state transition", this is difficult to follow. Perhaps worth rephrasing?
3. L118-L130: PSRO in the limit converges to a Nash equilibrium out of many. In mixed-motive games, NE needs not be unique and solutions are not interchangeable. Perhaps this could be a relevant point of discussion especially since VBP seems to be primarily dealing with mixed-motive games? 
4. L180: "... following maximisation problem ... $\E_{s~\pi(\omega)}$" should it be $a*$ instead of $s$? 
5. L235: focusing on a strategically relevant subset of strategies is comprehensively discussed in EGTA [1] and would be worth referring to here? 
6. L341: what does "Static" refers to here? 
7. L370: "the reason we can leverage ...", as mentioned in the Weaknesses section I could not follow the reasoning here. It would be great if the authors could clarify. 
8. Figure 4: For the honest probability, it appears that all methods have converged to the "always honest" strategy in all 3 settings. Is that expected? I would have thought that if the professor always recommends truthfully, the recruiter would be best served to always trust the recommendation at which point the professor could profitably deviate? 
9. L447: the authors suggested that the pattern of honesty rising, falling and then rising again validates the hypothesis that this is due to the use of aligned LLM. I would have thought that a simpler explanation is that the professor and the recruiter are simply in a strategic cycle? Would that not be a reasonable explanation to this phenomenon? 
10. L483: "... at most the top 10 strategies with the highest probabilities", is this for computational reasons? Pruning actions by their support at an restricted game equilibrium could be problematic in general. 
11. Figure 7: column "Converged prob" and the next column are redundant and could be consolidated to create space for larger fonts that are more readable? How are the probabilities computed? Are they the average probability of taking over the pool of policies in the PSRO population? 

[1] https://aaai.org/papers/01552-aaai06-248-methods-for-empirical-game-theoretic-analysis/

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
- The paper studies using LLMs in a Bayesian persuasion setting, which is a game between two players. One of the players (the sender) has access to some private information, and tries to influence the other player's (the receiver) actions by sharing specific information with them. The other player tries to use the shared information to achieve their own goals.
- The new aspect this paper introduces is that they use LLMs for both the sender and the receiver. They optimize the LLM agents' actions in the game by optimizing a distribution over a space of prompts. For instance, in a recommendation letter setting, the prompt specifies specific aspects of the letter such as whether or not to omit a weakness of the candidate. 
- The authors reproduce theoretical results from the classic BP setting experimentally, and also expand the setting to multi-turn interactions. They extend the prompt-space response oracle to multi-turn interactions using conditional prompt optimization.

### Strengths
- Persuasion in LLMs seems like an important topic given that LLMs will in fact increasingly be used for tasks such as writing recommendation letters.
- It is interesting to make the BP framework more realistic by studying actual written text rather than simple yes/no messages.
- It is a great idea to optimize prompts to study this setting, which is less involved than e.g. trying to do RL directly on the LLMs
- The paper includes comprehensive experiments and evaluations, including detailed ablations and examples in the appendix.
- I found it useful to see how strategies developed over training in Figure 7, specifically that more relevant categories ended up being selected more often.

### Weaknesses
 - I found the paper somewhat hard to follow. The paper uses a lot of machinery to define optimization problems and solve them, but I didn't always understand exactly what was going on on the most basic LLM level. I think more simplicity would be great with this sort of research.
- In general, I would prefer there to be less preliminaries and to get to the results faster. I wonder whether one could simplify some of the discussion of preliminaries to the parts that matter for the paper, though I'm not sure.
- It seems that in the end the way the game is setup, it doesn't really matter, for instance, whether the rec letters are actually written eloquently or not. I might be missing something, but it feels like somehow the simple BP games are not really the right testing ground for studying LLM persuasion, because from a game theory perspective, neither the sender nor receiver gain anything by using more than a binary signal/policy.
- As far as I can tell, the paper gives examples in the appendix, but I couldn't find any full end-to-end transcripts from the games.
- Given that the paper uses many bespoke algorithms to solve different aspects of the setting, I think this won't be that useful in practice. E.g., I think it's unlikely any of these will be useful for training better LLMs. If the goal is more to study propensities of current LLMs and to find out something about persuasion with LLMs, I am not sure what exactly the takeaway is. Is it e.g. "LLMs can implement complex strategies of deception/lying/etc."? If so, then I think this is not novel and also doesn't require the complexity used in the paper. I might be missing something here and am curious what the authors think.
- It might be that the optimization performed in the paper actually discovers interesting LLM behaviors and strategies, but this is hard to tell for me. I think I can see how the paper uncovers interesting behaviors within the setting studied here, i.e. when optimizing prompts, it's interesting that some amount of lying/deceiving gets reinforced, and that this game setup works in a sense and finds something like an equilibrium. But I haven't been convinced that this specific setup is interesting enough to study on its own—it seems too artificial to me to add a lot beyond either (i) the existing toy game theory setting on one hand, or (ii) just studying persuasion directly by prompting LLMs to write lying/deceptive/persuasive etc. texts.
- I have trouble understanding why the obedience constraint is used in this paper. As far as I can understand, one can simplify the BP game by assuming the sender just recommends the best possible action from the receiver's perspective, and then the problem becomes just choosing the best action for the sender to recommend, under the constraint that it must be optimal from the receiver's perspective (this assumes the receiver knows the sender's policy, which is the commitment constraint). Is this understanding correct? It seems that in this case, using the obedience constraint simplifies the game so much that one could have the LLM implement a simple (prompted) policy of either recommending and not recommending, and the obedience constraint makes sure this finds the right equilibrium. If the goal is to have a more realistic game where the text of the reference letter actually matters, then what does the obedience constraint do here? I might be misunderstanding something.
- In S1, the authors include a reward for the LLMs to give clearer signals. It seems that this basically is an ablation that forces the game back into a simple "yes/no" action space. It seems that the results here are similar to the S2 case where this reward isn't used. I am not sure this is a good or a bad sign—what is the takeaway from the S2 results? Is there anything going on under the hood that goes beyond a simple binary signal? (In a way that would be relevant to the game/optimization/etc.)?
- It would be nice to have some (possibly abbreviated/stylized) prompts and transcripts in the main body of the paper.
- If the prompt doesn't specify exactly how and when to lie, how can this still guarantee the commitment assumption?
- It might be that the most interesting result is S3, the iterated setting. However, the paper doesn't focus that much on it, and I think it would require more analysis to draw more interesting conclusions from this. Figure 12 might be useful here but from eyeballing it I don't really follow how it supports the hypothesis discussed in lines 473-476 in Section 4.2. (As a side note, I think Figure 12 would benefit from additional titles for the different settings. It's not easy to see graphically that these are for two difference settings, with two of the plots sharing the same subtitles.)
- Line 312 typo "Either a limit on the allowable tree depth" ... missing an or?
- Line 320 typo/grammar "through prompt design or expand the receiver's inforset."
- Line 392 "since we use aligned LLMs"---previously the paper talks a lot about "pretrained" LLMs, which could be interpreted as saying these are base models rather than chat/alignment-finetuned LLMs. It might be worth replacing the "pretrained" terminology.
- What would you say is the most important takeaway/learning from the paper that would be interesting and useful to the community?

### Questions
- I have trouble understanding why the obedience constraint is used in this paper. As far as I can understand, one can simplify the BP game by assuming the sender just recommends the best possible action from the receiver's perspective, and then the problem becomes just choosing the best action for the sender to recommend, under the constraint that it must be optimal from the receiver's perspective (this assumes the receiver knows the sender's policy, which is the commitment constraint). Is this understanding correct? It seems that in this case, using the obedience constraint simplifies the game so much that one could have the LLM implement a simple (prompted) policy of either recommending and not recommending, and the obedience constraint makes sure this finds the right equilibrium. If the goal is to have a more realistic game where the text of the reference letter actually matters, then what does the obedience constraint do here? I might be misunderstanding something.
- In S1, the authors include a reward for the LLMs to give clearer signals. It seems that this basically is an ablation that forces the game back into a simple "yes/no" action space. It seems that the results here are similar to the S2 case where this reward isn't used. I am not sure this is a good or a bad sign—what is the takeaway from the S2 results? Is there anything going on under the hood that goes beyond a simple binary signal? (In a way that would be relevant to the game/optimization/etc.)?
- It would be nice to have some (possibly abbreviated/stylized) prompts and transcripts in the main body of the paper.
- If the prompt doesn't specify exactly how and when to lie, how can this still guarantee the commitment assumption?
- It might be that the most interesting result is S3, the iterated setting. However, the paper doesn't focus that much on it, and I think it would require more analysis to draw more interesting conclusions from this. Figure 12 might be useful here but from eyeballing it I don't really follow how it supports the hypothesis discussed in lines 473-476 in Section 4.2. (As a side note, I think Figure 12 would benefit from additional titles for the different settings. It's not easy to see graphically that these are for two difference settings, with two of the plots sharing the same subtitles.)
- Line 312 typo "Either a limit on the allowable tree depth" ... missing an or?
- Line 320 typo/grammar "through prompt design or expand the receiver's inforset."
- Line 392 "since we use aligned LLMs"---previously the paper talks a lot about "pretrained" LLMs, which could be interpreted as saying these are base models rather than chat/alignment-finetuned LLMs. It might be worth replacing the "pretrained" terminology.
- What would you say is the most important takeaway/learning from the paper that would be interesting and useful to the community?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper extends a classical Bayesian Persuasion (BP) framework by incorporating more realistic and complex interactions through natural language. The proposed Verbalized Bayesian Persuasion (VBP) framework builds upon various existing techniques and introduces a two-player game in which both the sender and receiver interact through a large language models (LLM). Signal optimization is achieved through prompt optimization using existing methods.

The framework is tested across three scenarios with incrementally complex settings (S1, S2, S3), utilizing Llama 3.1-8b as LLM.

### Strengths
- The addressed problem is interesting, and leveraging large language models (LLMs) to model and solve a persuasion problem using natural language appears promising.

- The paper is well-organized overall and effectively integrates several approaches and techniques to extend the Bayesian Persuasion (BP) framework into a more realistic and complex scenario.

### Weaknesses
 - The optimization of the LLM prompts is not sufficiently detailed, particularly regarding the categories and content used in the prompt (see Q1).

- An anonymized repository containing the code and data for reproducibility is missing, although the authors provide guidelines and reference an existing repository.

**Minor Comments:**

- Typo: "Inforset" should be "Infoset" I guess,
- In Section 2.3, PSRO is used to refer to two different concepts.

### Questions
**Q1:** Are the categories and content of the key prompts exhaustively presented in Figure 7? For instance, regarding the writing style and the category "Tone," is the content "Positive" fixed?

**Q2:** Is it trivial that the chart (d) shows the Honest probability as always 1.0? Under what circumstances would a sender have an incentive to lie about a strong candidate?

### Soundness
2

### Presentation
3

### Contribution
3
