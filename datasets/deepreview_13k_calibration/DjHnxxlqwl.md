# Solving Urban Network Security Games: Learning Platform, Benchmark, and Challenge for AI Research

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
After the great achievement of solving two-player zero-sum games, more and more AI researchers focus on solving multiplayer games. To facilitate the development of designing efficient learning algorithms for solving multiplayer games, we propose a multiplayer game platform for solving Urban Network Security Games (**UNSG**) that model real-world scenarios. That is,  
preventing criminal activity is a highly significant responsibility assigned to police officers in cities, and police officers have to allocate their limited security resources to interdict the escaping criminal when a crime takes place in a city. This interaction between multiple police officers and the escaping criminal can be modeled as a UNSG. The variants of UNSGs can model different real-world settings, e.g., whether real-time information is available or not, whether police officers can communicate or not.
The main challenges of solving this game include the large size of the game and the co-existence of cooperation and competition. 
While previous efforts have been made to tackle UNSGs, they have been hampered by performance and scalability issues. Therefore, we propose an open-source UNSG platform (**GraphChase**) for designing efficient learning algorithms for solving UNSGs.
Specifically, GraphChase offers a unified and flexible game environment for modeling various variants of UNSGs, supporting the development, testing, and benchmarking of algorithms. We believe that GraphChase    not only facilitates  the development of efficient algorithms for solving real-world problems but also paves the way for significant advancements in algorithmic development for solving general multiplayer games.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This is a benchmarks paper and the authors have chosen the correct primary area for this work. 
The work proposes an environment (or simulator) for urban security game, with various parameters that can be tuned for changing game parameters. This is a well-studied multi-player (>2) problem. The authors also evaluate many known algorithms in this environment.

### Strengths
1) The work is an important step towards benchmarking performance of the different algorithms and evaluating them on the same setup.
2) Benchmarking in multi-agent systems is lacking, so this is a timely piece of work.

### Weaknesses
1) There should a list/table of parameters that can be controlled. Right now, it is all in text and getting missed.
2) The paper mentioned NE many times, but the games seem stochastic form, and probably extensive form. There have Markov equilibrium and Subgame perfect equilibrium. It is not clear to the reviewer if the framework can handle all of these - as this is just a simulator, it is probably ok.
3) Any simulator must deal with question of realism. The authors acknowledge the abstract nature of the simulator model itself. But, then the important question is if the simulator is extendible easily to handle other aspects if some researcher wants to add extra nuances of the real world. How is this handled, please explain?
4) The comparison to other works in this area---in the design of environment and simulator---must be expanded. What extra does this work offer over SIMPE and Avalon?

### Questions
Please respond to questions in weakness. Note that while I am positive, my overall view is still dependent on the questions I raised, so please answer these in details.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers Urban Network Security Games (UNSGs), a game-theoretic model of a scenario in which pursuers seek to catch some evaders. The game takes place on a graph. Agents are positioned at certain nodes and can move to nodes in the neighbourhood by taking an action, and evaders can exit at a pre-specified set of nodes. The work implements a set of environments corresponding to variations in this family of games, as well as a set of algorithms that can be applied to them. Some benchmarks are shown that demonstrate that the proposed implementations are faster than those in the original papers.

### Strengths
S1. The basic idea behind the work (proposing a framework for developing learning algorithms for a class of multiplayer network games) is sensible and worthwhile.

S2. The work is technically sound.

### Weaknesses
W1. The presented benchmarks are very thin: the only aspect they demonstrate is that the authors' implementations are faster than the original codebases. In my opinion, this is a missed opportunity to showcase the type of experiments that are enabled by the existence of this framework. How do the different algorithms perform on the different game variants (e.g. pursuers able communicate versus not; the different observability of the locations as in cases i-iv described in Section 2.2; different types of graph topologies as you only consider grids). Without this type of analysis, the contribution of the paper is lacking. Including it would validate the argument that your framework would be helpful in carrying out algorithmic research.

W2. The paper reads more like an advertisement for the framework of the authors rather than objective scientific writing. The framework is self described as "advanced", "pivotal", etc. We also get sentences that seem to suggest the design is somehow highly innovative such as "[...] providing a seamless flow of information and actions across the system. This modular approach not only enhances the adaptability of the platform to different research demands and scenarios but also supports the integration of various algorithmic strategies". In my opinion, the design contains just about every component you would expect for a multiplayer game environment and is standard.

### Questions
C1. Could you define more precisely in Section 2.1 what it means to for the pursuer to "catch" the evader, as it seems this is currently missing? Presumably, the evader is caught if both the pursuer and evader are located at the same node, and the node is not an exit node?

C2. L131: $E_{exit}$ or preferably $E_\text{exit}$? $\mathcal{N}(v)$ denotes either the *set of neighbours* or the *neighborhood*; L173: $\mathbb{R}$ instead of $R$?

C3. In Section 2.2 you say that NE is adopted as solution concept, but Section 6 mentions that a TMECom is computed in your framework. Section 2.2 should be updated with clarifications.

C4. For the "Game Module" component (3.1), you should specify what formats for graph data are supported e.g. graphml, xml, adjacency list, etc.

C5. Regarding the presented benchmarks, could you specify *why* your implementations perform faster? What is the core insight or optimization you did that enables this? This is not discussed.

C6. This is more of a preference, but I would suggest sticking to the "pursuer" and "evader" terminology throughout the paper. The work keeps intermittently referring to police officers and criminals, but this is a highly abstracted model, and while it is inspired by a real-world scenario, it is very far from capturing real-world complexity. Applying this terminology can also help to more clearly signal that the paper does not raise any ethical or fairness concerns (I don't think it does).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces GraphChase, a scalable, open-source platform tailored for Urban Network Security Games (UNSGs), where police agents coordinate to capture criminals in complex urban settings. UNSGs present computational challenges due to their large game spaces and the need for cooperation and competition among multiple players under imperfect information. Existing algorithms like CFR-MIX and PSRO have struggled with scalability and performance in these settings. GraphChase aims to provide a flexible environment for developing and benchmarking algorithms across diverse UNSG scenarios, supporting features including different numbers of players, types of underlying graphs, information levels, and the presence or absence of communication among police officers. Experimental results indicate that GraphChase improves algorithm efficiency compared to previous implementations but reveals ongoing challenges in scaling algorithms for larger urban networks​.

### Strengths
1. The paper addresses a challenging and practical problem—Urban Network Security Games (UNSGs)—that has direct applications in urban safety and law enforcement.
2. The paper aims to design an open-source, flexible, and modular platform that facilitates simulation, testing, and benchmarking of various algorithms in scalable settings. This makes it valuable for researchers aiming to develop efficient algorithms and compare them in a fair way. 
3. The paper implements multiple algorithms in its experiments, effectively identifying performance and scalability issues.

### Weaknesses
Considering that this is a submission for the datasets and benchmarks track, I have several concerns about the weakness of this paper.

1. Given that GraphChase is claimed as a comprehensive platform enabling various configurations, the experiments seem limited. Additional experiments and result analysis on different underlying graphs and varying information levels would better demonstrate the platform’s versatility and advantages. For example, the paper could explore the impact of different graph topologies (e.g., small-world, scale-free) on algorithm performance, and analyze how varying the level of information available to the pursuers (e.g., partial observability of the evader's location) affects the convergence and quality of the learned strategies. The current experiments primarily focus on grid-based graphs and do not fully explore the platform's capabilities in handling diverse scenarios.
2. It seems that the platform only considers algorithms for finding the optimal strategy for the pursuer, and directly computes the criminals' best responses as evaluation. However, the paper does not discuss the computational efficiencies of evaluation. Specifically, the paper lacks details on how the best response of the evader is computed. Is it through enumeration of all possible paths, or is there an approximation method? The computational cost of this evaluation process, especially in larger graphs, is not addressed, which is a critical aspect for a scalable platform. Furthermore, the paper does not explore the impact of different evaluation methods on the performance of the pursuer's strategy.
3. The paper elaborates related work on the pursuit-evation games and mentions their relationships to UNSGs. However, first, I found the literature comparison in this part is unclear. Second, the paper does not mention the relationships in detail nor does it illustrate using experiments. For example, does UNSG include other games beyond pursuit-evasion games? The paper should clarify the specific differences between UNSGs and other pursuit-evasion games, and explain why existing benchmarks for general pursuit-evasion games are not suitable for UNSGs. A more detailed analysis of the unique characteristics of UNSGs that necessitate a dedicated platform like GraphChase is needed.
4. The paper does not discuss the efficiency of using and interacting with the platform. The paper should include details on the ease of use for researchers, such as the API design, the learning curve for new users, and the availability of documentation and examples. This is crucial for a benchmark platform aimed at facilitating research in the field.
5. The experimental results are not presented in a clear way, as detailed in the "Questions" section below.

### Questions
1. In Line 347, how is the probability of being caught calculated? Specifically, I do not understand why the left side of Figure 5 has a probability of 0.5.
2. In Section 4.2, the authors aimed to show that their reproduced code performs better than the original. Could the authors further clarify this comparison? Is the improvement due to enhancements in code details, or does GraphChase offer systemic advantages that enable faster algorithm convergence?
3. In Table 1, the paper notes that even in relatively small settings, existing methods require extensive training times. Is this due to the complexity of environment interactions? Does this imply a lack of efficiency in the current platform, or is it simply a limitation of the algorithms themselves?
4. Around Line 410, the authors mention that current methods often make simplified assumptions about the criminal's strategy. Would it be possible to observe phenomena or convergence patterns if both the criminal and the police officer were modeled as learning algorithms?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes GraphChase, a Gymnasium-based platform that is aimed to solve urban network security games (e.g., policy trying to catch a criminal/terrorist in a densely populated urban environment where avoidance of collateral damages and civilian casualties is crucial). The platform has a modular structure allowing the user to define the environment (by entering a - potentially complex - graph), the strategies of the players and the learning algorithms among other parameters. The paper runs experiments in 7x7 grids with 4 police officers and 1 criminal and demonstrates that solution through GraphChase achieves generally faster solution times than naive implementation of the learning algorithms.

### Strengths
- *Quality and Clarity*: the paper is well-structured and cover many details of the proposed GraphChase platform. There is a discussion of related work, potential extensions to multi-agent settings and limitations of the current work which mainly stem from the (convergence) limitations (in complex environments) of state-art MARL algorithms. The exposition is generally clear, and I could follow the paper.

- *Originality and Significance*: the problem of urban network security games is important - entails optimisation of police strategies to arrest criminals which becomes particularly challenging in urban environments were casualties of co-existing civilians need to be avoided at any cost - and providing a platform to make their solution easier is an ambitious and well-received goal. There is a literature that studies this topic, and although I am not expert in this literature, the paper does a good job to present it for the general reader and motivate the current study.

-*Reproducibility*: The authors provide a link to a github repository with their code which I appreciated.

### Weaknesses
 - *Contribution and Novelty*: the main weakness in my opinion is that the paper does not provide convincing enough evidence that GraphChase is at the moment a significant step in solving UNSGs. The algorithmic results provide some evidence that it converges faster, but this is not surprising since the platform and the learning algorithms are integrated. I am not sure that I understand correctly the reasons of the claimed speed-up (so, please see my question below). Also, some of the simulations seem to terminate early or do not demonstrate significant improvements over the naive algorithm.

By weighting the strengths and weaknesses, my evaluation is that while I don't see methodological errors or bad exposition, the contribution of the current paper is simply not enough to merit publication at its current stage at ICLR. The paper should provide more substantial experiments in more complex environments and more systematic comparisons to the existing literature. While I understand that such environments can grow very complex very quickly demanding unrealistic computational power to be solved on researchers' computers, I still believe that the current contribution is not sufficient.

### Questions
- Can the authors clearly explain how is the speed-up achieved in the simulations that they show? In other words, what are the exact reasons/mechanisms that make the solution through GraphChase faster than the "naive" solution. Also how does the "original code" (or naive) implementation solve the games? Can the authors provide a detailed breakdown of computational time for different components of their algorithm compared to the baseline approaches?
- Why do some simulations seem to terminate early (especially the red lines) and some others to terminate before convergence (e.g., first panels of Fig 7 and 8). Can you please explain the termination criteria in detail, and provide convergence plots that show the full trajectory of the algorithms until a well-defined convergence point is reached?
- Can the authors provide specific additional experiments in already existing environments from the literature (with references) and  comparisons that would provide more convincing evidence of GraphChase's significance?

### Soundness
3

### Presentation
3

### Contribution
2
