# In-Context Learning for Games

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3

## Abstract
Most literature in algorithmic game theory focuses on equilibrium finding, particularly Nash Equilibrium (NE). However, computing NE typically involves repeated computations of best responses (e.g., policy space response oracle (PSRO)), which can be computationally intensive. Moreover, NE strategies may not be ideal in games with more than two players or when facing irrational opponents. Consequently, NE strategies often require further adaptions to effectively address various types of opponents, impeding practical deployments.  In contrast, In-Context Learning (ICL), i.e., learning from context examples, plays the core role in the generalizability of large language models (LLMs) to novel tasks without changing parameters. While ICL has been applied to decision-making tasks, e.g., algorithm distillation (AD), existing research primarily focuses on single-agent scenarios, and the ICL for games is largely unexplored.
To facilitate the game solving and the practical deployment, the research question investigated in this work is: *Can we leverage ICL to learn a model to i) play as **any player** of the game, ii) exploit **any opponent** to maximize the utility, and iii) be used to compute NE, **without changing the parameters**?* In this work, we propose **In-Context Exploiter** (**ICE**) to address this question: i) **ICE** generates the diverse opponents with different capability levels for each player of the game to generate the training datasets, ii) **ICE** combines the curriculum learning and the ICL for single-agent scenarios (e.g., AD), to train the single model for all players of games, and iii) **ICE** leverages the pre-trained single model to play as each player of the game against different opponents and integrate with the equilibrium finding framework, e.g., PSRO, to compute NE. Extensive experiments on Kuhn poker, Leduc poker, and Goofspiel demonstrate that **ICE** can efficiently exploit different opponents as different players of the games and can be seamlessly integrated with PSRO to compute NE without changing the parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of this work is to leverage in-context learning through the use of a transformer agent for multi-agent systems such that this single model can adjust to playing as any player and exploiting any type of opponent entirely through the context within its input and not through parameter fine-tuning.

### Strengths
- I think the approach and the framework is interesting, and the notion of in-context learning as a method of fast adaptation to any player strategy is interesting in the field of game solving.
- I think the paper is well-written and generally well-explained.
- The empirical results, whilst maybe lacking in terms of complexity of game explored, are encouraging for the proposed framework

### Weaknesses
 - In terms of opponent strategies generation, I think it is missing some nuance. In particular, I am not sure that either the random generation or the learning-based generation necessarily produce a meaningful & diverse dataset of opponent strategies. Whilst random generation can guarantee a form randomness, I am not sure that it would produce relevant behaviour to actually *learn* against (i.e. if we consider from the perspective that this approach should help with dealing with a wide set of opponents, it is unlikely that a real-world opponent would perform entirely at random). Furthermore, vanilla PSRO has been demonstrated in many papers to not generate a population of diverse agents and that is why there is a long line of literature looking at this exact problem: e.g. see those that cite 1) Open-Ended Learning in Symmetric Zero-Sum Games (Balduzzi et al. 2019) or 2) Modelling Behavioural Diversity for Learning in Open-Ended Games (Perez-Nieves et al. 2021). Therefore, can the authors demonstrate the diversity of the data that is collected?
- For the learning-based generated opponent strategies, it would also be good for the authors to discuss / demonstrate why they have called the final strategies added to the population as the most difficult task? I would be more inclined to say that the NE distribution over the *final* population is the most difficult task, but not the final strategy itself (e.g. it may only constitute a small part of the true NE support). Could the authors maybe present a stronger argument for why the order of teh curriculum they proposed is good for this framework?
- To me personally, it feels counterproductive to the learning process to include the random strategies to the curriculum process at all (they will most likely be such poor strategies that they could interrupt the curriculum as they are possibly so different - the authors also mention the catastrophic forgetting problem and I think the influence of these random strategies could emphasise this).
- My general concern with the framework is that, whilst the results do suggest that in-context learning can allow the model to perform well in comparison to other training approaches, is it truly beneficial if we still need to do the pre-training phase (which requires e.g. generation of PSRO trajectories and therefore a large amount of e.g. RL training anyway)? I think the authors should spend more time discussing why this is an approach that could be ultimately be better even with the potentially large amounts of pre-training required?
- I think RQ5 could use a small ablation in terms of which part of the CL is used (e.g. CL with PSRO generated strategies only, random only, both etc...)

### Questions
- I don't understand fully what is meant to by the third part of the desiderata 'used to compute the NE without changing the parameters' - especially in the context of the motivating example. The motivating example seems to suggest that we want an algorithm that is not *necessarily* searching for the NE given the behaviour of the opponent player. This seems counter-intuitive to the third desiderata, or I may be misinterpreting this point.
- In the card games, what does it mean for the framework to handle different players? Are the different players just defined by order of which of the players plays first?
- For the out-of-distribution testbed, where were the randomly sampled opponent strategies from? Were they just random strategies?
- In Fig. 10, what is the difference between the two subplots in (a) and (b)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the use of in-context learning for games. The goals are to train a transformer model such that it can in-context exploit any strategy by any player of a given game. This is then used as the best-response oracle in the population-based method PSRO to approximate a Nash equilibrium in a 2P0S (two-player, zero-sum) game. It builds off of the techniques for single-player setting techniques Algorithm Distillation (AD) and Decision Pretrained Transformer (DPT).

### Strengths
The research direction is solid. The three goals (play as any player, exploit any strategy, and find an approximate Nash) are reasonable, and the methodology and experiments do well in moving towards these goals.

The paper is written well, the experimental results are presented nicely, and most of the methods are clear.

### Weaknesses
My main critique of the paper is that the three goals and the research questions are good, but they are vague enough that it's unclear what the exact hypotheses are and therefore they aren't exactly falsifiable. I think the results on "RQ3: Can ICE be used to compute NE without changing the parameters" are mixed, not positive, but the paper does not mention it as a mixed or negative result.

This is important because I think that question is the most important and is in some sense the most unambiguous. The experiment measured performed PSRO and measured how exploitability changes as the algorithm progresses. The exploitability remains quite high even at the end of the experiment, yet the paper seems to deem this an affirmative answer to the question. For this question in particular, I think an affirmative answer to the question would involve a curve which converges to 0 exploitability, or at least something lower than the value that it got. It would also be helpful to compare the exploitability of ICE to some baseline, like PSRO with RL, or double-oracle with exact BRs, and maybe also to neural fictitious self-play (NFSP).

In my opinion, claiming that ICE affirmatively answers question RQ3 is overselling the results, and I would be more inclined to give a higher score if those results were more accurately contextualized. In my opinion, the overall framing of the paper, such as in the conclusion and perhaps the abstract, should also note that the experiments show positive first steps towards the goal of RQ3, but that there is still future work needed to achieve it.

Other minor critiques:
1. The experiments for RQ3 should also be performed on Leduc and Goofspiel. 
2. The setup of the Opponent Strategies Generation is ill-informed: "Intuitively, with the progress of the PSRO process, the generated opponent strategies will approach the NE strategy." That is *not* true: The opponent's *meta-strategy* will intuitively (but is also not guaranteed to) approach an NE strategy, but the best-response strategies $D_{li}$ will not. It's also not clear to me that $D_{l1}$ and $D_{lb}$ are respectively the easiest and hardest strategies to exploit. And $D_l$ is not really a diverse set of opponent strategies, since it may contain all "exploitative" (pure, or nearly pure) strategies. Because of that, they are likely all quite exploitable.
3. In the experimental results in 5.2, the BR (red line) is a fixed policy (not changing as the number of game iterations increases), right? Then it's probably clearer to take its value (either by taking its empirical value after many samples, or by simply computing its exact expected value) and plot it as a flat, horizontal line, than as a moving curve. Same with the NE (purple line).
4. It should be pointed out that ICE does not seem to converge to the BR in the OOD setting, which would presumable be a desiderata for this work.

### Questions
1. In Experimental Results, in RQ1 and RQ2, did you evaluate against just a single opponent per chart? Shouldn't the experiment be repeated several times, with a different opponent each time, and with error bars on the lines?
2. In RQ2: "The average returns of NE and BR strategies are not exactly zero. This deviation arises from using an approximate NE strategy as the opponent." -- Is it not expected that the average return of NE vs. NE in Kuhn poker is not 0? The Nash value is 1/18, right? [0]

[0]: https://en.wikipedia.org/wiki/Kuhn_poker

### Soundness
3

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
This paper proposes ICE, an in-context learning framework for multiagent games. Specifically the method consists of three stages, 1) collect interaction history from diverse opponents 2) optimise a transformer network to predict next action based on cross-episode interaction history with diverse opponents and 3) use the trained transformer policy network to act at inference time without further training. 

The key property of ICE is that the transformer network is no longer trained at inference time and only game interaction context is needed.

### Strengths
Leveraging transformer architecture for in-context learning in (single agent-) games has been a popular direction and the authors here extend this direction to multiplayer games and provided comprehensive experiments substantiating their claims that ICE is performant, does not require per-opponent re-training and can generalise across diverse opponents.

### Weaknesses
I'm unfortunately quite confused by the motivation for using transformer's in-context learning capabilities for the games that have been studied and I also find some of the experiments difficult to follow.

On the former, the in-context learning capability of transformer is typically studied in the context of transformer models that have been pre-trained on general domain datasets (e.g. Internet text corpus). By virtue of the generality of the training data and the effectiveness of the transformer architecture, one could leveraged such pre-trained models for in-context learning in domains where common sense knowledge is traditionally difficult to come by (e.g. SayCan [1] in robotics). If I understood correctly, the authors do not leverage pre-trained general-domain knowledge but generate domain-specific data that are used to train a specialist transformer model. From that perspective, "in-context learning" should be compared to meta-learning algorithms such as $RL^2$ [2] where the policy is conditioned on cross-episode interaction history. In multiplayer games, prior work at ICML such as $simplex-NeuPL$ [3] also showed that a policy network can adapt to diverse opponents, achieve near optimal returns (compared to BR policies) without inference time training. Neither of these works utilised the transformer architecture but I wouldn't find it surprising the a transformer architecture, with carefully constructed training dataset, would be able to achieve similar results.

On the latter, the authors did comprehensively study several experimental settings but I find the description of the experiments difficult to follow. For example, the authors compared ICE (AD) with PPO and found that PPO could not achieve optimal returns (compared to BR). However, it isn't clear what "assessed using the in-distribution testbed" would mean in this context. Is it a single opponent policy that's being played by the opponent? Or is it a distribution over opponent that's being sampled? For ICE (AD), are the "in-contexts" generated by one opponent policy or a distribution over them? As a reader I would appreciate if there's a clearly descried experiment even if it requires some of the less critical experiments need to be moved to the appendix (e.g. RQ6).

In short, I could imagine a project that studies in-context game play in games that demand common sense knowledge; with a more focused empirical section with one or two experiments that are clearly motivated and described.

### Questions
1. It would be great if the authors could address comments in the weaknesses section; 
2. L42-44: computing NE typically requires repeatedly computing best-responses: this is only true for Fictitious Play family of methods (e.g. PSRO) but there are many alternatives for which this is not required [1-2]. 
3. L45: NE is not ideal in games with more than two players: do you mean NE is difficult to compute? Could be useful if the authors could expand on this. 
4. Figure 1: it's not clear to me that this figure adds to the substance of the paper and I would suggest removing Figure 1 for more details on key experiments (e.g. RQ1). This figure could also mislead as it appears that one triangle feeds into another which I don't quite see why this would be the case. 
5. L74-75: AD, DPT are used for the first time (?) and yet to be defined. 
6. L76-L77: "... and be used to compute NE": what can be used to compute NE? The trained model or ICE the framework? Might be worth breaking into shorter sentences for clarity. 
7. L140-L150: Simplex-NeuPL [3] provides very similar motivations for not playing NE at times and could be a useful reference here as it tackles similar problem settings without using transformer or in-context learning in the LLM sense. Again Figure 2 could be removed for space or relegated to appendix. It would appear Figure 2 is stock imagery too which should be avoided? Providing a payoff table would suffice and would be more clear. 
8. L182: "consists of n ..." do you mean "consists of b"?
9. L186-187: "$D_{l1}$ and $D_{lb}$ are respectively the easiest and hardest ...". This isn't true in general. If you apply PSRO to rock-paper-scissors with {90% rock, 10% paper} the initial strategy, then your second (paper) and third strategy (scissors) would both be more exploitable than your initial strategy. The convergence is in terms of meta-game NE strategy, not in terms of individual ones. 
10: L196-199: "we can leverage the strategy learned via PPO...": this is not clear. Could you clarify what has been done? 
11: L211: "computing the gaps would be time consuming...": what gap? Do you mean the NashConv of strategies? If so, computing the NashConv should be quite easy in these games as you would only need to compare to the BR strategy? 
12: L215: It's not clear to me why you would want to mix in data random strategies at interval g. Would that lead to a jagged difficulty sequence with drops in difficulty every g steps?
13: L278: it might be clearer to avoid referring to self-play as an equilibrium finding algorithm when at L282 it's stated that "However, the self-play framework does not guarantee convergence". 
14: L312: "For the out-of-distribution testbed, we randomly sampled ..." from which distribution over policies did you sample these strategies? naively the space of policy is typically exponentially large and it's not obvious to me how to create a distribution over it that ensures diversity. 
15: L317: "we focus specifically on two-player games... as finding NEs in multi-player games [...] is challenging", could you clarify the NE results shown in the Kuhn-poker (3P) figure and how did you compute it? 
16: L346: what does the x-axis "game iterations" mean? 
17: when comparing ICE to PPO, I understood that ICE is conditioned on cross-episode trajectories that describe the interaction history. Is the PPO policy equally conditioned on cross-episode historic trajectories? If not, is each in-context episode conditionally independent from all other in-context episodes? 


[1] https://proceedings.mlr.press/v119/munos20a.html 
[2] https://arxiv.org/abs/2002.08456
[3] https://proceedings.mlr.press/v162/liu22h/liu22h.pdf

### Soundness
2

### Presentation
2

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
The authors introduce In-Context Exploiter (ICE), an algorithm addressing three questions: 1) Can in-context learning (ICL) enable a model to act as any player in a game? 2) Can it exploit opponents for maximum utility without updating parameters? 3) Can it compute the Nash Equilibrium (NE) with the same model? They use curriculum learning (CL) and reinforcement learning (RL) to train a highly adaptable Transformer model.

While this paper has limited novelty, rejection is still recommended for those listed in weaknesses.

### Strengths
1. Innovation: Combining NE and RL to generate diverse opponent data and proposing the ICE algorithm based on the ICL method, providing a complete framework from data collection and training to inference. But, it is common for ??? Therefore, the novelty is limited.

### Weaknesses
1. **Lack of Clarity in Algorithm 3 Evaluation**: It is unclear what specific advantages are demonstrated by PSRO with Opponent Exploitation in Algorithm 3. Is the primary goal to show that it can quickly approximate NE? The paper does not provide a clear comparison of computational costs or convergence rates with standard PSRO implementations, making it difficult to assess the practical benefits of this approach. Specifically, the evaluation lacks a direct comparison of the number of iterations or wall-clock time required to reach a similar level of approximation of the Nash Equilibrium, which is crucial for demonstrating the efficiency claims.
2. **Lack of Comparisons to Other Methods of Using ICL with RL**: There're a lot of existed ICL x RL methods, what's the main difference between yours and others? Given that ICL is applied to adapt to various opponent strategies, would directly integrating ICL into the RL training process yield better results? For instance, using historical **trajectories** to inform ICE in determining opponent strategies and providing this data to an RL model might enhance opponent exploitation. The paper does not explore how the proposed method compares to existing approaches that integrate ICL and RL, such as using ICL to guide policy learning or to improve exploration, which is a significant gap in the analysis.
3. **Unconvincing Experiments:** The experiments compare ICE (pretrained model) with PPO (Non-pretrained model), which is trivial that pretrained model can perform better at the previous time step. And in Figure 4, the performance drops afterwards. Results indicate that ICE performs slightly worse in OOD settings and is even surpassed by RL methods within 1000 iterations in some cases. The paper does not adequately address the performance drop of ICE after the initial time steps, nor does it provide a clear explanation for why ICE is outperformed by RL methods in certain OOD scenarios. This raises questions about the robustness and generalizability of the proposed method.
4. **Limited Ablation Study**: The study lacks ablation experiments on multiple factors, making it unclear whether ICE outperforms multi-task pre-training with fine-tuning frameworks in OOD  scenarios.  Moreover, the study does not clearly address the diversity or strength of opponent strategies, which raises questions about the method's potential for surpassing RL in broader applications. The ablation study should include a more detailed analysis of the impact of different context lengths, game types, and player positions on the performance of ICE, as well as a systematic evaluation of the diversity and strength of the opponent strategies used during training and testing. This is crucial for understanding the limitations and potential of the proposed method.
5. **Lack of Training Details**: The paper does not provide sufficient information on the amount of data, the number of training iterations required, or the specific model configurations.

### Questions
1. **Terminology Consistency and Figure Check**: In the paper, terminology is inconsistent; for instance, Section 4.2 refers to the "Curriculum Training Process," Algorithm 2 labels it as "Curriculum Training Framework," while in Section 5.2, it appears as "curriculum learning (CL) framework." If these refer to the same concept, a unified term should be used; if not, a clear distinction should be provided. Additionally, Figure 9 may contain an error, as the text states that the model "when combined with CL framework outperforms the version without CL," but the figure seems to indicate that w/ CL reward is lower.
2. **Provide Training Details and Data Requirements**: According to the results, the paper aims to demonstrate ICE's rapid adaptability across various opponents in specific game scenarios, which seems to benefit from pre-designed diverse opponent strategies. In contrast, RL methods may not require such pre-training. It would be helpful to further compare ICE's training requirements with RL methods (e.g., multi-task pre-training or representative NE methods within equilibrium finding), to substantiate ICE's claims of reduced training and application costs relative to RL or PSRO methods.
3. **Enhanced Ablation Studies**: The experiments currently only compare specific variables, but there is a lack of a comprehensive comparison across multiple factors. It is recommended to include tables for variable comparison or add parameter settings in the main text (some of which are found in B IMPLEMENTATION DETAILS). Ablation studies should compare different context lengths, game types (including player positions), and results for in-distribution vs. out-of-distribution players, to further illustrate ICE's early-stage training advantages over RL methods.

### Soundness
2

### Presentation
3

### Contribution
2
