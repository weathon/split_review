# OvercookedV2: Rethinking Overcooked for Zero-Shot Coordination

- Decision: Accept
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
AI agents hold the potential to transform everyday life by helping humans achieve their goals.
To do this successfully, agents need to be able to coordinate with novel partners without prior interaction, a setting known as zero-shot coordination (ZSC).
Overcooked has become one of the most popular benchmarks for evaluating coordination capabilities of AI agents and learning algorithms.
In this work, we investigate the origins of ZSC challenges in Overcooked.
We introduce a state augmentation mechanism which mixes states that might be encountered when paired with unknown partners into the training distribution, reducing the out-of-distribution challenge associated with ZSC.
We show that independently trained agents under this algorithm coordinate successfully in Overcooked.
Our results suggest that ZSC failure can largely be attributed to poor state coverage under self-play rather than more sophisticated coordination challenges. The Overcooked environment is therefore not suitable as a ZSC benchmark.
To address these shortcomings, we introduce OvercookedV2, a new version of the benchmark, which includes asymmetric information and stochasticity, facilitating the creation of interesting ZSC scenarios.
To validate OvercookedV2, we conduct experiments demonstrating that mere exhaustive state coverage is insufficient to coordinate well. Finally, we use OvercookedV2 to build a new range of coordination challenges, including ones that require test time protocol formation, and we demonstrate the need for new coordination algorithms that can adapt online.
We hope that OvercookedV2 will help benchmark the next generation of ZSC algorithms and advance collaboration between AI agents and humans.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A key challenge in zero-shot coordination (ZSC) is how to communicate with an agent that has never been seen before. Typical algorithms such as self-play settle on arbitrary communication protocols, which no longer work when playing with a never-before-seen agent that doesn’t have the same communication protocol. Instead, agents would ideally learn grounded communication protocols.

So far, ZSC algorithms have been tested primarily in Hanabi and Overcooked. However, in Overcooked, there is no need for grounded communication – indeed, many failures in Overcooked can be eliminated by simply increasing the diversity of states encountered during training – so it does not serve as a good test of the grounded communication aspect of ZSC.

To address this, the authors extend Overcooked to add features that induce partial observability, stochasticity, and asymmetric information across agents, and use these features to design six new handcrafted coordination challenges, which require grounded communication to perform well in the ZSC setting. Experiments demonstrate that the environment is challenging for existing algorithms, making it a good benchmark to hill climb on.

### Strengths
* As the paper notes, grounded communication for ZSC is an interesting area of research, and there is only one benchmark for it currently (Hanabi). Evaluating solely on Hanabi runs the risk of overfitting to the environment.
* The authors don’t note this, but I especially like that OvercookedV2 requires that grounded communication be done alongside other skills such as low-level motion planning (unlike Hanabi which is almost purely a communication challenge).
* I _think_ at least the simple versions of the handcrafted coordination challenges make sense as tests of different types of grounded communication, though I found it hard to evaluate due to missing details in the paper.

### Weaknesses
## State robustness is a part of ZSC

The authors argue that OvercookedV1 is a poor fit for testing ZSC because a lot of the failures are due to poor state robustness. However, I would argue that state robustness *is* a key challenge in ZSC. When playing a collaborative game with a novel partner, the partner’s actions may move into novel, off-distribution states; to be good at ZSC an agent must be robust to this. Algorithms like self-play naturally fail to produce state robustness because they exploit a single collaborative strategy that only visits a narrow part of state space; this is why algorithms like [Fictitious Co-Play](https://arxiv.org/abs/2110.08176) improve results – by increasing the diversity of partners, we increase the diversity of states that the agent is trained on, making it better at ZSC.

Based on Section 4, it seems that the authors are interested only in “fundamentally incompatible conventions”, giving this the name a “true coordination challenge”. The intended solution seems to be to base conventions off of actions that are meaningfully grounded in the environment dynamics, which I would call “grounded communication”, following [Hu et al](https://proceedings.mlr.press/v139/hu21c.html). This is a fine focus, but it should not be confused with ZSC – it is a particular subskill that is required to do well at ZSC. The authors seem to be conflating the ability to generalize to new partners with the ability to establish new conventions at test time, which are distinct skills.

Relatedly, lines 141-152 discuss how “Partial observability and stochasticity are required for a problem to be truly multi-agent” because “there is an optimal joint policy where the only information required is the timestep and agent ID, which essentially boils down to a pre-determined sequence of actions”. While this is all technically accurate, this is irrelevant to the ZSC problem, where the whole point is that the agents do not get to coordinate ahead of time on an optimal joint policy. In fact, the [Overcooked video game](https://store.steampowered.com/app/448510/Overcooked/) that the benchmark is based on is itself (usually) fully observable, but nonetheless poses significant ZSC challenges, as anyone who has played it can attest. The authors' argument that fully observable environments are not truly multi-agent is not well-justified, and seems to stem from a misunderstanding of the ZSC problem.

I would recommend that the authors rewrite the paper to focus on the grounded communication problem, rather than ZSC more generally. The contributions of the paper make much more sense interpreted this way – indeed increased state robustness should not make much of a difference to grounded communication. Elsewhere in this review I have treated the paper as though it were discussing the problem of grounded communication rather than ZSC more broadly.

## Missing details

One of the key contributions of this work is the six new handcrafted coordination challenges, illustrated in Figure 5. However the paper provides fairly limited details about these layouts (including in the appendices, though perhaps I missed the details), making it very difficult to understand what the challenge in these environments is. I think I’ve inferred it based on the prose, but the paper should specify it directly (see also the subheading “Questions about the handcrafted layouts” under “Questions”). I would recommend that the authors put much more detail into Section 6.3, particularly discussing the intended solution to each of the layouts. The lack of detail makes it difficult to assess the validity of the proposed challenges.

## Why is OvercookedV2 difficult?

The authors argue that OvercookedV2 is a good benchmark to test grounded communication. In support of this, they show that state augmentation alone is insufficient to close the gap between self-play and cross-play in OvercookedV2.

Firstly, this isn’t quite as obvious as the paper suggests. According to Table 1, for original Overcooked on Cramped Room and Asymmetric Advantages, there is approximately no gap to begin with, on Coordination Ring and Counter Circuit, the gap is approximately halved, and on Forced Coordination the gap is mostly eliminated. So statements like “By employing a state augmentation algorithm during training, we nearly close the SP-XP gap across all layouts” (line 67) are overclaims. In OvercookedV2, state augmentation doesn’t change the gap on three environments, but does substantially reduce the gap on the other three environments. So while state augmentation is certainly less effective for OvercookedV2, it isn’t ineffective. The authors should be more precise about the extent to which state augmentation closes the gap in OvercookedV1 and V2.

However, the more important objection is that this doesn’t convince me that OvercookedV2 is limited by the ability to do grounded communication. OvercookedV2 adds significantly more complexity to the environment, resulting in a greatly expanded effective state space to be robust to. In particular, with partial observability, optimal policies now depend on _belief states_, which is an exponentially larger space than regular state space. It is plausible that state augmentation was enough to address state robustness in the relatively limited OvercookedV1 environments, but could not address state robustness in OvercookedV2. The authors need to provide more evidence that the performance gap in OvercookedV2 is due to a lack of grounded communication, rather than simply increased environmental complexity. The current evidence is not sufficient to support this claim.

To address this, the authors could conduct a qualitative analysis of the failures exhibited during cross-play in OvercookedV2. Do we see failures of grounded communication, or failures of robustness? Ideally the authors would extend the existing Overcooked demo linked in footnote 2 with their environments and policies, so readers could observe these failures themselves. This would provide more direct evidence of the challenges posed by the new environments.

The authors could also investigate how the effectiveness of the state augmentation method changes with complexity of the environment, to predict how much the OvercookedV2 environments “should” be helped by state augmentation if they didn’t have grounded communication challenges, and compare that with actual performance. However, this is probably more effort than it is worth.

## Baselines

I believe that the current state of the art algorithm for grounded communication is Off Belief Learning (OBL), from which the authors get their Button game. The experimental results on OvercookedV2 should include OBL as well – it seems quite plausible that OBL succeeds where State Augmentation and Other-Play did not, particularly since Overcooked is a poor fit for the “symmetry-breaking” approach employed by Other-Play. (Though if the primary challenge for OvercookedV2 is still state robustness, as would be my guess, then OBL probably wouldn’t make much of a difference.) The absence of a strong baseline like OBL makes it difficult to assess the true difficulty of the proposed environments.

Another relevant algorithm is [Fictitious Co-Play](https://arxiv.org/abs/2110.08176), though unlike OBL this is not targeted at grounded communication, and so is reasonable to exclude.

### Questions
## Questions on the general message

* Is it accurate to say that the focus of the paper is on grounded communication, rather than coordination more generally? (If not, why not?)
* Can you say more about the intended solutions for each of the handcrafted challenges?
* Do you think humans would solve these environments as intended, if they were given only the rules of the game and some time to familiarize themselves with the environment? (It would be interesting to do a human study to check.)

## Questions about the handcrafted layouts

Here are my current guesses about how the layouts work – are any of these incorrect?
* The white circle with red background is a recipe indicator block, the red circle is a button recipe indicator, and the green square is a delivery location. (Please add a legend to Figure 5 for future readers.)
* Agents are only provided a signal for successful delivery in the Test-Time Protocol Formation setups.
* The yellow (onion) and green (broccoli) ingredients are to be actually used in recipes, while the blue ingredient is available to enable arbitrary communication strategies.

What is the view radius for each of the environments? This matters to interpret the environments – for example, a view radius of 1 in Demo Cook would imply that the agents must communicate via counter placements or pot interactions, whereas a view radius of 2 or more would allow the agents to communicate via their movements as well.

(Incidentally, I would recommend the authors also consider communication through movement as a form of grounded communication – this has been studied under the term “legibility”, see e.g. [Dragan et al, 2013](https://www.ri.cmu.edu/pub_files/2013/3/legiilitypredictabilityIEEE.pdf).)

(Ideally the paper would also specify other hyperparameters such as the sizes of various positive and negative rewards, but they are not as crucial.)

## Other notes

* Please add some more clarification about the Button game somewhere (appendix is fine). I had to read the Colab to understand how it worked. (In particular, it is quite unintuitive that when Alice presses a button, it does not turn on a fixed light bulb, but rather which light bulb it turns on depends on whether the pet is a cat or a dog. Consider reskinning the environment to be more intuitive, e.g. maybe when Alice presses a button, it removes one of N screens on Bob’s side of the room, and behind the screen is a picture of the pet.)

## Overall take

I’ve recommended a Reject (3), but I want to note that I do like a lot of the work and think that it is reasonably close to a point where I’d want to accept it. Mostly what is needed is a significant rewrite, focusing more narrowly on grounded communication in particular, with less emphasis on state augmentation, and significantly more exposition of the handcrafted challenges. It will likely also require collecting some more evidence about the utility of the environment for grounded communication (most notably a qualitative analysis of failure modes, and having OBL as a baseline). This evidence may reveal issues with the handcrafted layouts, but if so I expect the authors will be able to design new layouts that fix the issues.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The study of Zero-shot Human-AI coordination is important within the MARL community. Prior work has focused on the benchmark Overcooked, and shown how naive methods such as self-play fail because they form arbitrary conventions that don't generalize. However, this work shows that by merely increasing the state coverage self-play agents are exposed to, they can close the SP-XP gap. As such, the authors conclude the original 5 layouts are not sufficient coordination challenges. They then introduce a new benchmark which extends Overcooked by introducing asymmetric information and stochasticity, and show that state coverage is insufficient to coordinate on this new setting.

### Strengths
This is a compelling idea and it was very nice to see how for self-play agents, state coverage on the original 5 layouts essentially solved the generalization gap. The authors did a nice job explaining how their new environment introduces novel challenges to the Overcooked literature through communication and partial observability, as well as limitations of self-play on these new layouts.

### Weaknesses
It would've been nice for all evaluations of the state-augmented agents on the default layouts to see how well they play with humans. If state coverage is really the key to removing the SP-XP gap, then we should see performance with humans be higher than conventional SP method playing with humans. Otherwise, it is not clear that state-coverage alone is getting at the ZSC capabilities methods like population-based training tries to learn. A similarly insightful analysis would be comparing how well the state-augmented agents on the default layouts play with other algorithms (SP, MEP, E3T, etc.) that are SOTA for ZSC on overcooked. If state-augmented agents can perform at SOTA levels or close to that, it would be more compelling evidence that the issue with generalization on the original problems was just state coverage.

For the new environments, it would be compelling to see baselines such as MEP or E3T, which are some of the most successful algorithms for ZSC in Overcooked (the former being population based, the latter being self-play based). MEP and other population-based methods in particular try to simulate strategy diversity (by generating diversity in trajectories of states visited), so if these methods fail on your new benchmark it would be especially compelling as a new challenge for the MARL community to try to tackle.

The "environment creation via ASCII text" was listed as a contribution. How does this differ from the same functionality the original JaxMARL codebase already included beyond the additional object predicates from your new layout? 

Similarly, you listed there was an interactive interface for humans to play on the new environment. JaxMARL included this for Overcooked as well, so how is your interface different? If it's easy to benchmark human-AI coordination would you be able to show preliminary results on the new benchmark?

### Questions
The "environment creation via ASCII text" was listed as a contribution. How does this differ from the same functionality the original JaxMARL codebase already included beyond the additional object predicates from your new layout? 

Similarly, you listed there was an interactive interface for humans to play on the new environment. JaxMARL included this for Overcooked as well, so how is your interface different? If it's easy to benchmark human-AI coordination would you be able to show preliminary results on the new benchmark?

### Soundness
3

### Presentation
3

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
This paper discusses limitations of the Overcooked benchmark, a widely adopted benchmark for zero shot coordination (ZSC), and proposes a new benchmark named OvercookedV2. The newly proposed benchmark better tests agents' coordinaiton skills and is less affected by the state coverage during agents' training (which significantly influences the test results on the Overcooked). In this way, OvercookedV2 mostly focuses on coordination between agents rather than generalization of the learned policy.

### Strengths
1. Zero shot coordination (ZSC) is an important topic

2. The Overcooked, the most popular benchmark for ZSC, is out-dated. It is even fair to say that challenges in this environment have already been solved. The proposed OvercookedV2 poses new challenges for studies on coordination (not only ZSC but also more general studies on agent coordination).

3. Thorough study on drawbacks of the Overcooked is given.

### Weaknesses
1. Insufficient evaluations of current ZSC methods on the new environment.

2. Some grammatical mistakes, e.g. 'where agents independently trained agents can adopt similar strategies but with arbitrary variations in execution'


### Questions
1. In the paper, you mentioned that in the Overcooked, ZSC failure can be attributed poor state coverage rather than more sophisticated coordination challenges. In this way, the Overcooked mainly evaluates policy generalization rather than coordination. So I wonder what is your definition of 'coordination'? Because I think generalizing to new partners is almost equal to ZSC.

2. Could you include more ZSC baselines in the paper. Other-play relies on pre-known symmetries in the environment so it may not work in the new environment. But there are also many ZSC methods that I believe are completely data-driven [1], [2], [3], [4].

[1] Strouse, D. J., et al. "Collaborating with humans without human data." Advances in Neural Information Processing Systems 34 (2021): 14502-14515.

[2] Zhao, Rui, et al. "Maximum entropy population-based training for zero-shot human-ai coordination." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 5. 2023.

[3] Lou, Xingzhou, et al. "Pecan: Leveraging policy ensemble for context-aware zero-shot human-ai coordination." arXiv preprint arXiv:2301.06387 (2023).

[4] Yan, Xue, et al. "An efficient end-to-end training approach for zero-shot human-AI coordination." Advances in Neural Information Processing Systems 36 (2024).

3. I wonder whether you plan to integrate human-AI coordination into OvercookedV2, since another important advantage of the Overcooked is its support for human-AI interaction.

### Soundness
3

### Presentation
4

### Contribution
3
