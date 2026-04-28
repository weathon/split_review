# InnateCoder: Learning Programmatic Options with Foundation Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Outside of transfer learning settings, reinforcement learning agents start their learning process from a clean slate. As a result, such agents have to go through a slow process to learn even the most obvious skills required to solve a problem. In this paper, we present InnateCoder, a system that leverages human knowledge encoded in foundation models to provide programmatic policies that encode "innate skills" in the form of temporally extended actions, or options. In contrast to existing approaches to learning options, InnateCoder learns them from the general human knowledge encoded in foundation models in a zero-shot setting, and not from the knowledge the agent gains by interacting with the environment. Then, InnateCoder searches for a programmatic policy by combining the programs encoding these options into a larger and more complex program. We hypothesized that InnateCoder's scheme of learning and using options could improve the sampling efficiency of current methods for synthesizing programmatic policies. We evaluated our hypothesis in MicroRTS and Karel the Robot, two challenging domains. Empirical results support our hypothesis, since they show that InnateCoder is more sample efficient than versions of the system that do not use options or learn the options from experience. The policies InnateCoder learns are competitive and often outperform current state-of-the-art agents in both domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
InnateCoder uses foundations models to generate domain-specific language candidates (options), and then use stochastic hill-climbing in the induced syntax / semantics space to find a best-performing agent.

### Strengths
- Writing overall is fine, although I have some small complaints which I'll mention in the weakness section.
- I believe this method is novel to my knowledge.
- InnateCoder was evaluated in two domains used in previous methods, showing nontrivial improvement over baselines in a number of tasks while matching performances in the rest. 
- I appreciate the authors' effort to eliminate data leakage as a factor during evaluation.

### Weaknesses
 - I find the presentation of this paper to be a little confusing for someone not familiar with the prior work. For example, in section 2, the authors start to talk about the pros and cons of DSL before giving an introduction or even a definition of DSL. I also think using the actual language (or a simplified version) in one of the tested domains, instead of the generic "if b then c" or "c1" "c2" as the example could be more helpful.
- Could the authors specify what are the exact differences between InnateCoder and LISS? Is the option source the only difference?
- I have concerns that application of this method could be limited. The DSL-dependency demands all discrete actions with a hand-crafted grammar. This requires significant domain expertise to design a DSL that is both expressive enough to solve the task and also amenable to the stochastic hill-climbing search. The assumption that all tasks can be solved within a hand-crafted DSL is a strong one and may not hold in many real-world scenarios.
- I would suggest showing some examples of the foundation model / final policy (can put those in the appendix).

Minor issues:

- Figure 1 is after Figure 2.
- 3.2.1 is the only subsection under 3.2.
- L208 "starting at the non-terminal __ the node represents".
- L230 "that is is".

### Questions
- The policies produced by InnateCoder seem to be deterministic. Is this the case for other baselines? How are the numbers in Table 1 produced? Are they calculated (by enumerating through all initial positions) or simulated (for a certain number of games and taking the average)? If the latter, how many games did you run to get the numbers?
- Why is there a clear difference between agents with $\leq 1400$ options and with $\geq 5000$ options? Agents with $\geq 5000$ options have sharp performance increases in the early stage of learning while agents with $\leq 1400$ options don't and can even have performance drops. Despite having such a distinction between the two groups, the curves within the two groups look similar. What factors contribute to this cut-off?
- L210 "$\mathcal{E}$ is an approximation of ..., ${\hat{V}^n(s_0)}$". What is the difference between $\mathcal{E}$ and ${\hat{V}^n}$?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors introduce a new way to learn programmatic options.  The set of options is built by first sampling a set of programs from a foundation model that is given a description of the MDP and the domain-specific language (DSL).  Then the set of programs is improved by searching through sets of modified programs to find ones with high reward.  Results show that this approach outperforms (i) other programmatic search algorithms that do not use foundation models and (ii) Deep RL approaches in the games MicroRTS and Karel the Robot.

### Strengths
- Authors do a nice job of explaining the algorithm.
- Authors also did a nice job of providing the DSL for each environment and the exact prompts used.

### Weaknesses
The main weakness here is that the contribution seems to be small.  It seems likely that the better use of a LLM is to learn a policy that outputs short programs conditioned on the history of the game that has occurred.  This way the foundation model can adjust its output as it gets more information on how the game works.  The reasoning provided for not testing this is that this would be expensive.  But if you were to apply this algorithm from scratch to a new environment, it would already be costly to come up with a sufficiently expressive DSL.

It is also unclear to me why machine learning is needing for settings like these.  The hand-engineered action space of (non-terminals, terminals, etc.) is already small, so regular software engineering should often be able to learn the sequence of these actions.  

In addition, although it was helpful to see the exact prompts, the authors could be more transparent of how much prompt engineering was needed.  The exact "Program writing guidelines" and the "list of tasks" provided make it seem like there may have been quite a bit of prompt tuning was needed.

### Questions
1.  Can you discuss the types of prompt engineering that was required?
2.  Can you provide some examples of what the final programs look like in these domains?  It is difficult to know how complex these domains are.
3.  Is there any results on what type of search is more important between syntax and semantic search?

I am willing to increase my score if I can get a better sense of the value add of using machine learning here vs. just hand-crafting policies.

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
This work introduces a new approach for learning policies for reinforcement learning tasks, by using the knowledge from pretrained LLMs. Instead of learning a NN policy, as is common in regular DRL, InnateCoder generates a number of options, each represented as a program in a custom DSL. These are then combined into a policy, with the exact combination being obtained via stochastic hill climbing during the training process.

### Strengths
This paper works on a very interesting direction of using pretrained LLMs to synthesize agent policies in RL tasks. This is important, as we still lack any meaningful foundation models for agents (here understood as action-taking systems), and this seems to be one good way of using the "general knowledge machines" for some agentic behavior. 

The results obtained with this approach seem very good, and claim SOTA - I'm not sufficiently familiar with this specific domain to evaluate this claim, but it seems reasonable as it's compared to winners from public competitions.

### Weaknesses
My only main concern is about the fairness of comparison in the MicroRTS evaluation, possibly due to not understanding this part of the paper. In Figure 3, you plot the winrate. The winrate is defined on line 341 (somewhat confusingly under "Other specifications") as "The winning rate of a policy is computed for a set of opponent policies [...]" - what policies? Is it equally sampled between COAC, Mayari and RAISocketAI?

More importantly, over the course of the training in Figure 3 (the one that goes up to 1e5 games), is each method exclusively trained on self-play, and then checkpoints are "separately" evaluated against reference opponent policies (COAC, Mayari, RAISocketAI presumably)? Or do they interact with those policies throughout the training process?

Generally speaking, the writing is at times difficult to follow, possibly because I'm not that familiar with this specific subfield. For example, in line 283, "2L" is introduced as the algorithm used to train the policies, without much further elaboration or expanding the acronym. There is, of course, a reference to the paper that introduced it, but seeing as it's not a widely known algorithm, it might be useful to include some outline of how it works.

As a half-nitpick: the pixelated aesthetic of Figure 4 makes it rather difficult to tell what's going on. Consider for example FourCorners, where I can see something happening early on in the training, but mostly it's just straight converged lines. Or OneStroke, where it's just the straight converged lines. I understand it's difficult to present so much information in a finite amount of space, but perhaps there's some other way to make it work?

Furthermore, I'd be curious to see how well regular DRL algorithms would perform on Karel as a baseline - it does not seem to be an overwhelmingly difficult task, though I have not used it personally.

### Questions
Can you elaborate on the exact training procedure? Specifically - when training e.g. IC-Llama, what exactly is the workflow of the policy being improved, the round-robin tournament between 30 seeds, what data is used to improve the policy, and how/when it's evaluated? 

My only real doubt is regarding the fairness of training IC against fixed versions of opponent policies. Also, fairness of the evaluations - how do the winrates differ against different reference policies? (for example, it could be the case that IC does really well against weaker opponents, but still mostly loses to the strongest policy, but all of this gets averaged to a high winrate on the graph - I don't claim that this is happening, but I'm not confident that it's not happening given the data in the paper)

I'm looking forward to seeing this cleared up during the discussion, and if by the end of it I'm fully convinced that this method actually outperforms all other known alternatives on these benchmarks (mainly MicroRTS, but also Karel - although in the latter I suppose SOTA isn't as difficult as in a competitive game), I'd be happy to increase my rating.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel framework called InnateCoder which leverages foundation models (FM) and stochastic hill-climbing (SHC) to search programmatic policies to solve various RL problems. InnateCoder encode general human knowledge from foundation models in a zero-shot setting to formulate programmactic policies, while these policies interact with RL environment using options as "innate skills". The framework works as follows: given the environment description and its corresponding domain specific language (DSL), a prompt can be built to query the foundation models to generate programmatic policies. Although the generated programs are unlikely to solve the problem directly, they provide important corpus of options. By tweaking the syntax and semantics of these options, new options and programs are obtained for the framework to evaluate and search via SHC. The search stops when run out of budgets or the optimal solution is found.

### Strengths
- Presents a novel method called InnateCoder which leverages foundation models to provide corpus of knowledge instead of trying to solve the problem directly. Authors claim that the generated programmatic policies can be used as the starting point of option and program searching, and InnateCoder should extend the searching by extending to and visiting neighborhood programs. This method leverages the foundation models' great ability on higher-level abstraction and left the lower-level operations to options. The overall method is simple and very intuitive.
- Performes extensive evaluations on different benchmarks. The baselines are properly selected. The proposed framework is highly competitive in nearly all evaluated benchmarks.
- Related disccusion is extensive and informative. The discussion is helful and meaningful for researchers in related community.

### Weaknesses
 - The main text does not provide a single complete example programmatic policies or an option for a single environment, it could be helpful to add at least one for better readability. 
- The discussion on $\epsilon$ in SHC is lacking. In Sec. 4.1 line 371, it says the results shows the semantic space can be less conducive to search than the syntax space, depinding on the quality of the options used to induce it. If so, modifying the $\epsilon$ may improve the results.
- This is minor. The Sec. 3.1 introduces the definition of options. I think it might be better to introduce this concept informally before the formal definition.
- In Sec. 4.2, why the results of Llama 3.1 + GPT-40 in Mayari is worse than the results of Llama 3.1 or GPT-4o alone?
- I understand how does the filtering options work in  Sec. 3.2.1 in general. However, could you demonstrate some specific numbers if possible?  For example, people would like to see the percentage of adopted options for each environment.
- The SHC looks very nice in many domains. Could you briefly summarize how does it work, e.g., how does SHC accquire the inital programmatic component? By enumeration of the DSL?
- I did not read the prompt line by line, so sorry if I miss anything. When you use prompts to query the programmatic policies, do you provide any multi-modal information other than plain text, such as images or animations? If not, do you think it is possible to improve the quality of the generated programs and options?

### Questions
- In Sec. 4.2, why the results of Llama 3.1 + GPT-40 in Mayari is worse than the results of Llama 3.1 or GPT-4o alone?
- I understand how does the filtering options work in  Sec. 3.2.1 in general. However, could you demonstrate some specific numbers if possible?  For example, people would like to see the percentage of adopted options for each environment.
- The SHC looks very nice in many domains. Could you briefly summarize how does it work, e.g., how does SHC accquire the inital programmatic component? By enumeration of the DSL?
- I did not read the prompt line by line, so sorry if I miss anything. When you use prompts to query the programmatic policies, do you provide any multi-modal information other than plain text, such as images or animations? If not, do you think it is possible to improve the quality of the generated programs and options?

### Soundness
3

### Presentation
3

### Contribution
3
