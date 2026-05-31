## Human Reviewer 1

### Summary
This paper implements both Critic-Guided Decision Transformers (CGDT) and Online Decision Transformers (ODT) into the Gym-$\mu$-RTS domain, and also explores the combination of the two methods. The authors build a dataset from games from two previous competition bots  (CoacAI, Mayari), and use this data to train their models, which matches the performance Implicit Q-Learning (IQL).

### Strengths
- This paper re-implements two different methods, and combines them together, then applies them to the Gym-$\mu$-RTS domain. Given that the project has been open-sourced, this work may be useful to others.
- The presented algorithm runs on a desktop PC, in a much smaller amount of walltime than many other RL projects. This accessibility and sustainability is something that I believe is often under-valued.

### Weaknesses
- Sadly, this paper does not resemble something I would expect to see at a top-tier conference such as ICLR. The writing is quite poor, containing a strangely large number of very short sentences, making it unnatural to read. Furthermore, all of the Figures in this paper are significantly below the typical quality of this venue. I recommend that the authors spend some time reading over previously accepted work and more closely adopting their style.

- The paper only appears to test the proposed algorithm on a single task, with a single set of settings. While $\mu$-RTS is a challenging environment, using a single environment is generally a notable weakness. Testing on different map sizes or settings would have improved the paper.

- The paper has rather limited novelty - it mostly just combines two existing ideas together and adapting them to a new task. While the combination and re-implementation of algorithms can be very useful and sometimes worthy of acceptance, I don’t believe the provided results are groundbreaking enough to justify this.

- The agent’s training data is taken from CoacAI and Mayari, and then also evaluated against these same agents. It is generally poor practice to train and evaluate on the same data/agent.

- The paper does not appear to have a limitations section, which are quite a standard and important section in most papers.

- In Table 1, while I think the ablations were quite interesting, the use of A-G make it quite difficult to read. Please consider using something like OCGDT + Online, and OCGDT + Double Tuning, etc. The caption could still keep the detailed description, but this would make the results easier to digest.

### Questions
- In a single paragraph, could you concisely summarize what the novelty of this paper is?
- Can this algorithm be applied to other environments? Could it improve performance?
- Given that this method appears to be very computationally light, perhaps a walltime vs performance graph against prior methods would be a nice way to demonstrate the utility of your method?

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper explores an approach to playing real-time strategy games based on decision transformers, and therefore offline RL. The paper leverages two ideas to make DTs more amenable to an RTS setting, which are online DT and critic guided DT. It then combines these approaches to form OCGDT, or online critic guided decision transformers.

The paper converts the RTS setting into an offline RL problem with online fine-tuning by using $\mu$RTS and the associated Gymnasium framework. It collects data using two state-of-the-art, rulebased frameworks for playing RTS games, and both learns from such data and competes with said baselines. The paper also includes an implementation of IQL as an alternative offline RL baseline and compares its contributions with this well-established baseline.

### Strengths
The paper is well-written in terms of prose, level of details, and most importantly the clear description of technical details. This is the case throughout, but an example is the description of the architecture; e.g. section 3 does well to describe how the approach "works" and is complimented nicely with figure 1. Several other examples show up in the paper as well.

The idea is clever and the setting is quite interesting given that most offline RL papers are applied to the same benchmarks. There is some technical innovation in converting the problem and getting both the DT-based algorithms and IQL to fit within the $\mu$RTS setup.

### Weaknesses
The contribution of OCGDT needs to be made more clear. Is this novel? Non-trivial? The re-implementation of ODT and CGDT on $\mu$RTS problems is interesting in its own right, but again it is unclear if this is the contribution or if it is the creation of a new architecture / algorithm.

In general it is unclear if this approach actually worked. This is perhaps fine given that this is a new foray into this setting from offline RL. But the paper itself mentions that recently ML-based approaches have achieved competitive results in RTS settings. Why, then, is the proposed approach not competitive?

n my opinion, there are several important things to add to the paper (e.g. a more robust IQL description), and hopefully in the main body. Therefore as an editorial suggestion, things like line 334-338, "Training is performed on a Windows 10 machine..." can then be moved to an appendix. These and other similar details are much appreciated and necessary but can likely be moved without degrading the quality of the paper.

### Questions
1. The results are somewhat puzzling. My understanding is that the offline data consists of games between CoacAI and Mayari. In the parlance of Offline RL, one might call these "expert" datasets. Why, then, do the methods not achieve parity with either of these baselines? In the case of IQL this is somewhat explanable as it is largely doing imitation learning, and CoacAI/Mayari may be doing things out of distribution at test time. (And if that is the case, is the buffer size appropriate? Should it be larger?) Then, for the online methods, i.e. those of this paper, why don't they perform better?

2. In Table 2, the most interesting thing to me is that CGDT appears to be essentially even wtih IQL (or IQL with sufficient resources). Both of these are offline and therefore, they are imitating each other. Does this suggest that the DT part of the architecture doesn't really matter, and that online finetuning and/or online experience is of first-order importance?

3. Line 423, "This suggests a larger and more diverse dataset...". I agree with this conclusion but I do not think the ablation was necessary to reach it. The fact that IQL has parity with the DT approaches, and that neither are competitive with the expert baselines, suggest that something is amiss with the dataset or perhaps that offline RL is not the correct approach. In standard offline RL datasets, the underlying distributions of the environments are stationary; in the case or RTS, the agent is actually playing a game with the environment, and it (the "environment", which is CoacAI or whatever) changes its distribution according to how OCGDT (or whatever) is behaving. It seems like offline RL will never work for such a case, although the exploration of different and better datasets is encouraged.

4. Line 284: "The actor, the critic, and the value function have separate parameters for state representation". Is this simply saying that there are 3 different neural networks? What is meant by "state representation? The paper could be improved by adding an architectural figure for IQL (probably in the appendix) and making the distinction between IQL details and the various DT details. These are very different things; for example, one doesn't do return-to-go conditioning in standard IQL. Furthermore, is there a transformer in the IQL set up? In other words, is IQL set up with the standard IQL loss functions, the set of neural networks, etc, but that the various neural networks also have transformers? How are they tokenized, and how is this different than DTs (which need return conditioning)? Section 3.3 is probably the least clear part of the paper, and IQL is not really described anyway (while the two variants of DT actually are explained, as well as their combination).

5. The setup to ensure a fair (or "reasonably" fair, or the most fair possible) comparison between IQL and OCGDT is much appreciated. To play devil's advocate, however, this might require a bit more justification. The argument here seems to be about getting an approximately equal number of "experiences" of the data and/or online interactions, and/or gradient steps. This is a solid foundation to start. But each (IQL and OCGDT) have their own hyperparameters at play. So just as a thought experiment, what if Approach A has 100K tunable parameters and Approach B has 100B. In this admittedly extreme example, is it really appropriate to say that having the same "experience" yields a "fair" comparison?

Again, in line 362, DT-based methods require an order of magnitude fewer updates, but are they parameter efficient with respect to IQL? The subsequent text appears to explain this somewhat (i.e. the text about training for wall-clock time and number of gradient steps).

6. Did the authors consider other notions or heuristics for calculating (estimating? Imitating?) the lower entropy bound for $\mu$RTS?

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This work re-implements two Decision Transformer variants, Online Decision Transformer (ODT) and Critic Guided Decision Transformer (CGDT), along with a widely used offline reinforcement learning method, Implicit Q-Learning (IQL). It further proposes a combined model named Online Critic Guided Decision Transformer (OCGDT) for the Gym-$\mu$RTS environment. Each method is first trained using datasets generated by rule-based $\mu$RTS competition winners, CoacAI and Mayari, and is then finetuned with online interaction. Among the RL approaches, OCGDT achieves the highest win rate against CoacAI, which empirically demonstrates that effective RL optimization in the $\mu$RTS remains a challenging task. Through a range of ablation studies, this paper explores which components of OCGDT are particularly difficult to optimize in the environment.

### Strengths
S1. (Clear and reproducible implementation details)
The paper provides detailed descriptions of the RL methods, including their architectures and training procedures.

S2. (Empirical performance of RL methods)
The results show that both DT-based methods and IQL exhibit low win rates when competing against rule-based winners. This finding highlights the difficulty of applying RL methods in the Gym-$\mu$RTS environment.

S3. (Ablation studies)
The ablation study varies several factors, such as buffer size, context window length, and the number of online steps in OCGDT. Through these experiments, it empirically reveals the challenges of online fine-tuning for OCGDT in the Gym-$\mu$RTS. It also emphasizes the importance of appropriately balancing offline data and online samples. However, one of the ablation results remains unclear, as discussed in Weakness W3.

### Weaknesses
W1. (Insufficient explanation of RL behaviors)
The paper lacks detailed analysis of how each RL method behaves in the $\mu$RTS. A more thorough explanation would help clarify how these models differ in decision-making.

W2. (Limited analysis of ablation results)
Despite multiple ablation studies (OCGDT A to G) results, their interpretations appear limited. In particular, the difficulties regarding online fine-tuning in OCGDT seem to require additional analysis and discussion.

W3. (Ambiguity in description)
The difference between OCGDT and OCGDT-E in Table 1 is not clearly explained. It would need to specify what distinguishes the two settings and affects their performances.

**Minor**

- typo at line 329; With -> with

### Questions
Could you provide further clarification regarding the weaknesses mentioned above, particularly the behavioral explanations of the RL methods and the interpretation of the ablation results?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper applies Critic-guided Online Decision Transformer to Gym-$\mu$RTS, a long-horizon, stochastic game environment with sparse rewards. OCGDT re-implements and combines ODT and CGDT, two standard return-conditioned sequence modeling methods, to enable offline critic learning, offline policy learning, and online fine-tuning. The authors evaluate against several rule-based bots and run ablations over buffer size, training step, and context length. Empirically, OCGDT matches or exceeds baselines like IQL, CGDT, and ODT.

### Strengths
- The paper well summarizes prior work it builds upon. 
- The paper includes enough experimental details for reproduction purposes.

### Weaknesses
- __The novelty and contribution of this paper are very limited.__ This paper is an application of existing methods to a new task. ODT and CGDT are well-known methods in the literature of RL sequence modelling. OCGDT is merely a combination of both up to some minor changes of the network architecture. And the motivation for combining them does not bring new insights either, as DT's inability of trajectory stitching and suboptimal behavior in the face of environment stochasticity are well-known and ongoing research questions nowadays. OCGDT does not add more algorithmic design for addressing these fundamental issues.

- __The methods involved in the paper are outdated.__ Compared with IQL, ReBRAC [1] is an acknowledged stronger offline RL baseline with the use of actor and critic. For the value-guided DT, QT [2] is one of the current SOTA DT variants. I believe the performance could be stronger when QT and ODT are properly merged.

- __The performance of OCGDT is not appealing.__ In Table 1, OCGDT performs on par with ODT alone for CoacAI, while it performs on par with CGDT and even worse than ODT for Mayari. So, the combination of the two algorithms benefits little. Moreover, IQL is not a proper baseline, since it is not strong enough and it lacks sequence modeling, which is important for this long-horizon, sparse-reward environment.

__References:__

[1] Revisiting the Minimalist Approach to Offline Reinforcement Learning

[2] Q-value Regularized Transformer for Offline Reinforcement Learning

### Questions
Please refer to the weaknesses. In addition, could the authors evaluate their method on canonical offline RL benchmarks, e.g., D4RL or Visual D4RL?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4