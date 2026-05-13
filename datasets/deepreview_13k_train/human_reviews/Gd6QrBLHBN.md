# Altared Environments: The Role of Normative Infrastructure in AI Alignment

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Cooperation is central to human societies, which they achieve by constantly tack-
ling the alignment problem of ensuring self-interested individuals act in ways that
benefit the groups in which they live. As AI agents become pervasive in shared
environments, it will be similarly crucial for them to align with the cooperative
goals of human groups. Current AI alignment research largely focuses on em-
bedding specified or learned norms into agents to achieve this cooperation. While
valuable, this approach overlooks the role that institutions play in aligning human
behavior to achieve cooperative gains and thus overlooks a potential alignment
technique for AI agents. We address this gap by proposing Altared Games, a
novel formal extension of Markov games that incorporates an altar—a classification institution providing explicit normative guidance to agents. Our approach focuses on a challenging setting where norms are dynamic, thereby requiring agents
to adapt to the evolving norm content represented by the altar. Using multi-agent
reinforcement learning (MARL) as a computational model of AI agents, we con-
duct experiments in two mixed-motive environments: Commons Harvest, which
models resource sustainability, and Allelopathic Harvest, which involves coordination under conflicting incentives. Our results demonstrate that the altar enables
agents to adapt effectively to dynamic norms, engage in accurate sanctioning, and
achieve higher social welfare compared to systems without a classification institution. These findings highlight the importance of normative institutions in fostering
cooperative, adaptable AI agents operating in complex real-world settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper describes the importance of cooperation to reach socially beneficial equilibriums in mixed motive environments, which often present a variety of cooperation challenges. Specifically, this paper mentions the tragedy of commons, alignment, and the free-rider problem. They use the Allelopathic Harvest and Commons Harvest environments, making modifications as needed.
For the purposes of this study the agents used to explore these concepts use multi-agent reinforcement learning, specifically using PPO in self-play. However, this is not the focus of the study, and the specific learning method is not the primary focus and should be viewed as such. They claim to be agnostic to the learning method and have further claims that similar performance with and without GRU units. 

This is due to the authors want the study to not focus on additions to the model of the agent, but rather on changing the environment to affect the norms. They wish to understand institutions and describe multiple formulations of institutions in the work.

The authors show they are wanting to study the effect of introducing “altars” or institutions into the environment (which can act similarly to the formulations they have described, ie be dynamic, fixed, etc…) to show that this can help solve the alignment problem. They do this by explicitly adding altars to the map, which are zones which prescribe the colour of the resource that should be used. 

Many variants of the game are described, however the variants of the games which are most applicable are those in which the agents can use some method to tag/sanction their fellow agents to encourage desired social norms. These tagging abilities have different rewards based on a hidden rule or the altar colour in the environment. In some versions distraction institutions are added and the agents are still capable of learning.

The presence of the altar is shown to have a direct effect of increasing the total reward (adjusted for hidden rewards) of the agents even as compared to the hidden reward, which are both capable of suggesting the same norm for the behaviour.

### Strengths
The work is well presented, and easy to follow.

The experiments do show that the introduction of an altar does reduce the cognitive burden on agents while addressing cooperation challenges and promote normative social order. And that performance is increased compared to simply having a hidden rule/norm built into the reward of the sanctioning actions.

The experiments are solid and show the improvement achieved by the introduction of altars.

### Weaknesses
These institutions/altars have to know the environment rules to dynamically change. I am not convinced we always have that knowledge available, especially when it is environment dependent (like when it has to do with the relative scarcity of the apples/berries in different zones).

It would also have to have some sense of the possible norms before it can be introduced and then we're simply choosing one for it to represent. 

That brings in the introduction of an altar with dynamic rules, which has to match the reward structure of the tagging. Is this not something we have to know before hand? Or is that seen as dictated by the environment. If it is, how do we enforce the altar to follow those rules? We won't always know them like we do in these situations. Is there a possibility of them having to learn how to change to fit the environments rules? (How will its observations work then?)

We won't always be able to alter an environment to include an altar, how do we address such situations?

Do these altars not have to have the reward structures with regards to tagging hard programmed into them to follow the rules to show agents the correct representation colour?

### Questions
Please see the strengths/weaknesses.

However, see below, I am open to debate on these and willing to be persuaded to adjust my score, I just have to be convinced after the following questions:

1. Does the introduction of the altar not add a new observation data point into the input? Or is this just directly learned over time and from passing it in earlier states? I am assuming the latter?

2. Do these altars not have to have the reward structures with regards to tagging hard programmed into them to follow the rules to show agents the correct representation colour? (is there a possibility of them having to learn how to change to fit the environments rules?)

3. With the introduction of an altar with dynamic rules, which has to match the reward structure of the tagging. Is this not something we have to know before hand? Or is that seen as dictated by the environment. If it is, how do we enforce the altar to follow those rules? We won't always know them like we do in these situations. Is there a possibility of the altar having to learn how to change to fit the environments rules? (How will its observations work then?)

4. We won't always be able to alter an environment to include an altar, how do we address such situations? Or is this simply not applicable then?

5. How do we get a sense of the available norms before being able to add the altars?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work tackles the problem of collaboration in mixed-motive multi-agent reinforcement learning. The authors suggest introducing an addition to the agents' observations, the altar, that indicates certain institutional rules that the agents should follow to maximize social welfare. This is in contrast to previous work in which these institutional rules are hidden. Empirical results over two grid-based domains show that agents trained with altared versions of the environment achieve higher rewards and are resilient to changes in these institutional rules.

### Strengths
- The idea is novel and deals with an interesting problem in multi-agent AI research.
- Results show that indeed altared environments promote collaboration and resilience in agents.

### Weaknesses
 - Poorly written and difficult to read:
	- There are many grammatical errors that lead to ambiguity and ruin the flow of the text. It is  recommended to use automated grammar checking tools as this is present throughout the entire text.
	- Paragraphs are long and packed with multiple ideas making them hard to read. Each paragraph should capture one main idea.
	- There are many run-on sentences which are difficult to follow. Shorter, more concise sentences will be easier to follow.
	- There are broken links to appendices, unreferenced figures, and overall messy presentation of results. 
- The authors claim to have published their code for reproducibility, but following the link provided in the abstract leads to an empty repository (https://anonymous.4open.science/r/normarl-public-804C/README.md).
- The authors make claims and mentions models that are not explained nor cited. A glaring example from the introduction is in line 45: "literature in multi-agent systems (MAS) has grappled with...". This is present several other places as well. Another example is the lack of citation for definition of models in the background, e.g., Markov game (line 107). The authors should either cite, prove, or give an intuitive explanation to every claim in the paper.
- The authors define many decision-making frameworks in section 2 and sections 3.1, 3.2, but these are not revisited in the main parts of the paper which makes them confusing and redundant.
- The contribution of this work is can be boiled down to adding manually programmed indications of social rules explicitly into the agents' observations. This is done with no theoretical justification and relatively weak intuition. You should either mathematically prove that using the altar modification encourages correct sanctioning, or at least give a stronger intuition as to why this effect might occur.
- Figure 1, is not clear at all and does not help demonstrate the differences between the  versions of Markov games. Also, it appears at the top of page 2 with an uninformative caption, but is first referenced on page 4. Figures should be near where they are first referenced because otherwise the reader is forced to constantly scroll and break concentration.
- Figure 2 is not referenced anywhere in the text.
- Environment description in main paper is insufficient. e.g., It is mentioned in line 315 out of the blue that the agents can eat the berries.
- showcases only harvest domains. There are other social dilemma domains like cleanup, economist, prisoners dilemma, etc. Every social dilemma environment presents its own challenges that can be potentially be solved by smart sanctioning. Testing in these environments could make a stronger case for using altars or might provide insights into the limitations of altars.
- There is inconsistent plot coloring and labeling of plots, making it difficult to follow the results.

### Questions
- why is POMG mentioned? are the environments partially observable? if so, this is not clear from the text.
- Why is I-SMG defined? it seems redundant. Isn't it enough to define an altar and explain that it induces institutional rules? what is the difference between an altar and an I-SMG institution?
- In figure 6 the authors show 6 plots. why does figure 7, which is essentially the same kind of results but for a different environment, present only 3?

### Soundness
2

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
4

### Summary
This paper proposes tackling the alignment challenge in multi-agent systems using normative classification institutions. They consider two socially challenging multi-agent reinforcement learning environments augmented with normative infrastructure, which they call “altars”. These altars are features of the environment associated with functions that determine whether agent sanctioning actions are “right” or “wrong” in Sanction-Augmented Markov Games. They investigate the effect of such infrastructure on the learning dynamics and alignment of agents in their environments.

### Strengths
1. Cooperative alignment in multi-agent systems, the problem this paper aims to tackle, is highly relevant and important.
2. The idea is good. Classification institutions for normative alignment make intuitive sense and are well-grounded in social science and anthropology.
3. The introduction is very well written.

### Weaknesses
1. To me, Figure 1 is not very informative. This figure should provide a clear and unambiguous overview of your approach for the busy reader. The caption is just “Overview of the Altared Framework”. What are the three subfigures? What actually is your framework and how is it depicted here? What is “history”? I feel like this could be made clearer.

2. Section 3 does not flow well and feels confused. There is very low information density per word here. I feel there are enough issues to warrant a full section-by-section breakdown:
    
    3.1. introduces the problem and how you fix it. This is great.
    
    3.2 defines I-SMG. Is this the framework you propose? Figure 1, the central figure of the paper, mentions an “altared framework” but this is not defined anywhere. I would expect a description of your core proposal here.
     
    3.2.1 “salient features of an institution”. I am not sure what this adds. The “Prescriptive” sub-sub-sub-section seems to be additional explanation of I-SMG. This is helpful but out-of-place and presented confusingly. The “Dynamic” points range from vague (what is avg_behaviour? what is an “annual policy update function” and why would we apply the same transformation every year?) to outright confusing:

    - 1. What do tax policies and insurance regulations have to do with social norms? You explicitly mention that the institutional prescription does not modify rewards, but it seems to me that taxation would.

    - 2. How do we go from \tau(I_t, s_t) to averaging over the past k states? The only explanation we get is “where h adjusts the institution based on recent agent behaviors”. This is very vague and I suspect violates the Markov property of the I-SMG.

    3.3 this section finally introduces the word “altar” again, but honestly I have no idea what it adds. Everything in here is just a repeat of things that have already been said, and there is no reference to I-SMG to tie it all together.
    
    3.3.1 and 3.3.2 - environment descriptions. These are long sub-sub-sections of the proposed method section and do not flow well from it. Why are they not in “4.1 Environments”? Importantly, I do not like that these sections do not give a self-contained description of the environments but instead point the reader to the appendix. When reading a paper, the first thing I personally want to do is check results; to do this, I should be able to quickly get a nice concise explanation of the test environments and then move on - not scroll down to the appendix for such crucial information. Finally, we go back to an explanation of why/how your method works at the bottom of 3.2.2 - this again feels out of place and does not flow well (in what way is this specific to the Allelopathic harvest environment?).

3. Section 4 is similarly poorly written. A non-exhaustive list of comments:
    1. "4.1 Environments" is just one short uninformative paragraph. Is this half written? It says “we describe the variations here” but does not do so. This seems a good place for the environment descriptions above…
    2. "4.2 Baselines and Agent Architecture” and then "4.2.1 Agent Architecture” and no other sub-sub-sections. Was this proofread?
    3. Why are environment descriptions, needed to understand your results, in the appendix but agent architecture in the main paper?
    4. Are the plots just WandB screenshots? I would expect much neater plots with axis labels and much longer, descriptive figure captions from a paper submitted to ICLR. Why are some lines truncated earlier than others? Font size is a bit small too.
4. Weak results. This is my primary concern and biggest reason I’m going to recommend rejection. These results are far from convincing. It looks to me like there is no difference at all in mean episode reward for allelopathic harvest, and three seeds is not enough for a rigorous evaluation on Commons Harvest. I have worked with the meltingpot environments myself in the past and have seen firsthand just how stochastic these are. Even more concerningly, the error bands seem to abruptly shrink twice on your Commons Harvest mean episode reward plot, with no variance at all at the end; this looks a lot like the three seeds ran were not all run to termination. Unless you can explain these two sharp decreases in variance, it seems to me one of the core plots supporting your approach is presenting misleading information.
5. No ethics section? Who gets to decide the norms that the institution classifies as “right”?
6. (very minor) latex comments:
    1. some of the notation in definitions is unnecessarily verbose - I personally prefer \bigtimes for long cartesian products.
    2. Sanction function being called Sigma is ambiguous given this is summation notation, e.g. ambiguity in SMG reward function definition.

### Questions
Please address the questions raised above - especially those concerning the experimental results.

### Soundness
1

### Presentation
1

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
This paper incorporates 'altars', institutions within selected cooperative multi-agent environments by DeepMind (Melting Pot), that provide agents with observable guidelines on how to punish each other's actions to enhance collective welfare. Authors claim to validate their hypothesis by running 3 experiments, 1. "vanilla" trained using PPO 2. hidden-rule based and 3. altars as environment features

### Strengths
1. Well-written paper, reads naturally (flow, language)
2. Introduction and Preliminaries set the stage very well and explain the broader interest in the problems touched.

### Weaknesses
## Main concern:
1. Experiments and their results do not support the claims made by unfair comparison. For example, we compare mean rewards while one of the baselines has a clear disadvantage in earning rewards.
2. Code is not accessible to reproduce or investigate the work further
3. No description on how the altar "dynamic" attribute works
4. No mention of the results of the original authors of the Melting Pot environment suite

## Sub-issues:
1. The abstract is very ambiguous, assuming specific knowledge of the environments, which can confuse readers who are not knowledgeable.
2. I appreciate the anonymization of the repository, however it renders empty, this leads to missing code, to reproduce the work and experiment videos cannot be accessed.
3. Minor spelling mistakes such as in line 128, 515
4. Line 320 - link to reference is missing
5. Figure 1 is an important figure however, it is not / hard to understand
6. Figure captions are insufficient for most / all figures in the main body of the paper.

### Questions
## Questions:
1. It is not clear to the reader how the altar is set up, i.e. How are punishment policies chosen? Is this hard-coded? This is what is being revealed: "Finally, as the institutional content is dynamic," but there is no indication of how this works.
2. The same goes for the hidden-rules setup. How are hidden rules decided, and what are they exactly? This might become clear when investigating the environment suite; however, it should be made clear in the main body of this paper.
3. The baselines are not supporting. The results reported by the original authors of the Melting Pot environment suite are not mentioned, and I believe this work should be compared against what the original work reported.
4. The experiment results show how the altar and/or hidden-rule-based setups surpass the "vanilla" setup when looking at Mean Episode Reward. However, the chosen environment scenarios are not about mean episode rewards. What they care about is, for example, the depletion rate.
5. Your Vanilla baseline mentions that zapping results only in negative rewards, no positive rewards, while the other setups yield positive rewards. That means we do not have an apples-for-apples comparison of results.
6. Finally, my biggest question is: What if the agent's reward function is modified, such as the altars policies are set? Adding the altar as an observable sanctioning feature appears to be a complicated dynamic reward that is not given by the environment directly but rather potentially by other agents catching others doing the wrong thing. This would mean that if a negative reward for bad behaviour is always given, we should even see better performance, but this could be achieved by reward-shaping or adding a reward structure already only. In conclusion, the partially observable rules that help agents police each other's actions, when observed, seem not worth the effort.

### Soundness
2

### Presentation
1

### Contribution
2
