# The Cyclical Chaos And Its Equilibrium

- Decision: Reject
- Scores: 3, 3, 3, 5, 3

## Abstract
Finding a Nash Equilibrium (NE) in noncooperative games is a fundamental challenge in game theory and artificial intelligence, but existing methods can be computationally demanding to address the cyclical strategy problem. Existing methods like Policy Space Response Oracles (PSRO) allow agents to learn a best response (BR) policy against all prior policies. Once the learned policy converges, it is added to the sequence until an NE is identified. While the learning against all prior policies prevents agents' strategy interactions from descending into a cyclical chaos, this approach increases computational demands due to the expanding population of opponents. Our research offers a new perspective. We argue that cyclical strategies are not chaotic anomalies to be avoided; instead, they are orderly sequences integral to an equilibrium. We establish the theoretical equivalency between a complete set of cyclical strategies and the support set of a Mixed Strategy NE (MSNE). Our proof intuitively demonstrates that the cyclical strategies must form a circular counter, implying that a complete set is necessary to support an MSNE due to the intrinsic counterbalancing dynamic. This enables a novel graph search learning representation of self-play that finds an NE as a graph search. Our empirical results show improved self-play efficiency in discovering both a Pure Strategy NE (PSNE) and a MSNE in noncooperative games such as Connect4 and Naruto Mobile.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Empirical game theory methods such as Policy Space Response Oracle (PSRO) aim to compute a Nash equilibrium in normal-form games by iteratively solving for the equilibrium of a consistently growing game. Such algorithms often exhibit cycling behavior over a set of action profiles. The authors show that the action profiles over which these algorithms cycle form the support of the set of mixed Nash equilibria. This results enables a novel graph search learning representation of self-play that finds an NE as a graph search. The authors demonstrate in experiment that their method is efficient in discovering Nash equilibria in normal-form games such as Connect4 and Naruto Mobile.

### Strengths
The authors provide insights into the behavior of a large class of empirical game theoretic algorithms, and use the insights to provide improvement on the state of the art.

### Weaknesses
The paper is highly inaccessible. Many concepts lack technical definitions (e.g., cycles). There also seems to be formatting issues (there are two proofs under theorem 3.1? Unclear which one to refer to).



### Questions
What is the purpose of the experiments? The takeaway is not clear.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The core contribution of the paper is the identification of behavioral regularities (BR-wise dynamics) in normal form games, manifesting as cycles. Main claim is that these cycles are not arbitrary but are fundamentally related to the structure of the game itself, specifically the support strategies of Mixed Nash Equilibria (MSNE). In essence, the study finds that Path-Response Strategy Oscillations (PRSO) inherently orbit around MSNEs, suggesting a deeper, systematic relationship between dynamic strategy adjustments and equilibrium concepts in game theory

### Strengths
The strength of the result in the manuscript is indeed noteworthy as it provides a contemporary interpretation and formalization of long-observed phenomena in game theory. Drawing a line from the early observations of cyclic patterns in strategies, such as those seen in Shapley's polygons, through to the formal predictions of the Poincaré recurrence theorem, the paper successfully situates its findings within a historical context of strategic analysis. The assertion that the detection of cycling within Path-Response Strategy Oscillations (PRSO) dynamics is tantamount to discovering the support strategies of a Mixed Nash Equilibrium (MSNE) is a significant one. This claim underscores the potential of cycle detection not only as a diagnostic tool for understanding strategic behaviors in games but also as a means to unearth the foundational structures that underpin MSNEs. The result, therefore, is not just a reflection of dynamic behavior in games but also a powerful statement about the nature of equilibrium within the strategic play.

### Weaknesses
1) Computational Complexity: The manuscript suggests that detecting cycles within PRSO dynamics is computationally feasible, which implies a method for identifying Nash Equilibria by constraining the game to the faces of a simplex formed by these cycles. However, this raises a significant question about the computational tractability of Nash Equilibrium. The paper should address why cycle detection is presented as an easy task and not as evidence that finding a Nash Equilibrium is tractable. It would be beneficial for the authors to delineate the aspects of their cycle detection methodology that may incur exponential time, which would then align with the conventional complexity understanding of Nash Equilibria.

If this is not the case, how did we avoid PPAD-hardness of the result?

2) 

Novelty of the Result: The paper's results, while compelling, do not seem novel in the light of existing research. The concept of cycling and instability of Nash equilibria has been addressed in several key papers, such as "Nash, Conley, and Computation: Impossibility and Incompleteness in Game Dynamics" by Milionis et al., 2022, and "No-regret learning and mixed Nash equilibria: They do not mix" by Vlatakis-Gkaragkounis et al., 2020. Furthermore, "Cycles in adversarial regularized learning" by Mertikopoulos et al., 2018, touches upon similar themes within FTRL dynamics, which are akin to BR-dynamics with a strong convex regularizer.
For a discrete example see section 4.5 of Vlatakis-Gkaragkounis et al., 2020. The authors cite also books where preliminary results are already known in the literature for simpler dynamics.
Vaguely speaking, current literature actually is far ahead from proving simply cycles by giving understanding also the econometric impact of them: Papers like "On the Interplay between Social Welfare and Tractability of Equilibria" by Anagnostides and Sandholm discuss the outcomes of non-converging gradient descent methods, which  form a cycle and explain the impact of cycle in PoA  results.

Moreover, going to the core of the problem, Milionis et al, their predecessors and follow-up  works such as "The Replicator Dynamic, Chain Components and the Response Graph" by Biggar and Shames, and E. Akin's "Domination or Equilibrium" (1980), have already discussed the elements of strongly connected component (aka a  ``generic'' cycle) of best response dynamics includes the support of a Mixed  Nash state.

It is essential for the review committee to consider the depth of related literature on this topic, potentially uncovering more foundational results which covers also exactly PRSO dynamics. Although the age of a result does not undermine its relevance, it does affect the suitability of the work for a conference setting, as opposed to a journal that might better accommodate such ``slight'' rediscoveries.

Given these considerations, I recommend that the paper be accepted on the condition of a significant expansion of the related work section. This expansion should not only acknowledge the depth of existing research but also elucidate the specific differences in the dynamics studied by the paper that add to its merit. A more in-depth comparison with the broader body of literature will greatly enhance the paper's contribution and ensure a thorough understanding of where it stands in the context of existing knowledge.

### Questions
Please answer to weaknesses section issues.

I am very eager to the response of AC and authors about the novelty of Theorem 3.1, willing to change my score to 10

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper examines the connection between best response trajectories and the support of mixed Nash equilibria in games and makes some statement that connect the too. Although, I generally find the the subject study to be of interest the paper is rather poorly written with not well justified terminology and notation, which makes pursing the paper a cumbersome exercise.

Examples of this: 

1.The word chaos plays a prominent role in the title and abstract but it seems to have no connection to anything explored in the paper. The authors never for example try to even hint at whether they mean Li-Yorke chaos, Lyapunov chaos, Devaney Chaos, etc. In fact the paper seems to be about best-response dynamics.

2. Reading through the intro and even up to and including the main theorem statement I still do not know what the paper has actually showed.

3. The definition of cyclical best response strategies which appears in theorem 1, while being undefined, is still not properly defined. The definition that follows the theorem is referring to an optimal strategy of the opponents (-i). Optimal to what? Is this meant to apply to a zero-sum games? If not, to which strategy of the agent i is this to meant to an optimal response. Also, pease do not use notation of the form \sigma^{i}_{*'}. Those indices are very hard to read.

4. Does theorem 1 refers to two players games or n-player games? Is it about zero-sum games as many of the examples suggest but in the  game theory basics we have definition for n player games.

I believe that the could be some interesting statement made here, but this paper needs some thorough work before it is ready to published.

### Strengths
The paper studies an interesting subject matter, related to PSRO/double oracle techniques which are used widely in multi-agent RL.

### Weaknesses
The paper purports to examine the connection between best response trajectories and the support of mixed Nash equilibria, but the presentation is severely hampered by poorly defined terminology and notation, making it difficult to ascertain the core contributions. 

Several examples highlight these issues:

1. The term "chaos" is prominently featured in the title and abstract, yet its meaning and relevance remain entirely opaque. The authors fail to specify the type of chaos (Li-Yorke, Lyapunov, Devaney, etc.) they are referring to, and there is no discernible connection to the actual content, which appears to be centered on best-response dynamics.

2. The main theorem statement, even after reading through the introduction, lacks clarity. It is unclear what the paper has actually demonstrated.

3. The definition of "cyclical best response strategies" in Theorem 1 is not properly defined. The subsequent definition refers to an "optimal strategy of the opponents (-i)" without specifying optimality criteria. It is unclear whether this applies only to zero-sum games or, if not, to which strategy of agent *i* this is supposed to be an optimal response. The notation  \sigma^{i}_{*'} is also unnecessarily difficult to read.

4. It is ambiguous whether Theorem 1 pertains to two-player or n-player games. The examples suggest a focus on zero-sum games, yet the background section defines n-player games. This lack of clarity undermines the general applicability of the theorem.

Overall, while the subject matter holds potential interest, the paper requires substantial revisions to improve clarity and rigor.

### Questions
Can you provide a formal unambiguous statement of your main theorem? E.g. what is the class of games that this theorems applies to? What is a formal definition of cyclical strategies and of complete cyclical strategies?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new graph search learning representation of self-play that finds a Nash equilibrium of non-cooperative games. One of the problems of self-play is that it may fall into a cyclical strategy, where population based frameworks that aim to remedy this then have the problem of maintaining a large pool of strategies that need to be trained against. This paper proposes a framework to try alleviate both of these problems.

### Strengths
- In general, the problem that the paper is trying to solve is very important. Self-play is a difficult to utilise framework in games that not strictly transitive and population frameworks such as PSRO can grow to having a very large population of strategies which become increasingly hard to find an approximate best-response to. Therefore, being able to minimise the amount of necessary strategies needed to train against is important for the literature.
- The empirical results suggest that GraphNES is able to outperform population methods (in this case NeuPL) whilst maintaining a small opponent population size (which makes approximate best-response training easier)

### Weaknesses
- At times I found the paper difficult to follow. In particular, it would be useful if the authors were able to provide a visual representation of the algorithm similar to what they do for self-play and PSRO. Specifically, a diagram illustrating the graph construction and search process, highlighting the differences from standard self-play and population-based methods, would significantly improve the clarity of the proposed GraphNES algorithm.
- The experimental choice seems a little strange for the baselines that the authors are comparing to. For example, PSRO frameworks have generally been evaluated on card games (e.g. those from the OpenSpiel repository), matrix games or environments in the MeltingPot library. Whilst I am not expecting the authors to add results from these environments during the rebuttal phase, it would be useful if the authors could discuss their criteria when selecting the environments that they did and why they did not select more common ones. Specifically, the rationale behind choosing Connect4 and a Street Fighter-like game (Naruto Mobile) is not immediately clear. A justification for selecting these environments, particularly in the context of demonstrating the ability to handle cyclical strategies and maintain a small opponent population, would strengthen the experimental design.
- In line with the environment selection, I think it would be good if the authors could have a more representative example that helps understand what the algorithm is doing. For example, a simple matrix game comparison of which strategies are being found etc... Providing a step-by-step walkthrough of GraphNES on a small, illustrative matrix game (e.g., a 2x2 or 3x3 game) would greatly enhance the reader's understanding of the core mechanics. This example should demonstrate how the algorithm constructs the graph, identifies best responses, and converges to a Nash equilibrium (or approximates it) in a simplified setting.

### Questions
It would be great if the authors could address the points that I mentioned in the weaknesses section. Primarily:

1) Is it possible to provide a visual representation of the algorithm similar to those provided for self-play and PSRO?

2) Why were these environments selected over other more common baselines for these style of algorithms?

3) Is it possible to provide a simple matrix-game style example showing the learning process of the algorithm?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers iterative methods to determine Nash equilibria in finite, non-cooperative games. To avoid cycles of best responses, e.g., as is the case with myopic best response in Rock-Paper-Scissors, current state-of-the-art iterative methods like PSRO calculate best responses against all previous policies. This is effective in avoiding cycles, leading ultimately to learning a Nash equilibrium, however, it has a considerable (and often forbidding) increase in computational time by continuously increasing the opponent's self-play population of policies. 

With the aim to improve the self-play algorithm complexity, the paper proposes the idea that when such iterative algorithms enter a cycle, then this cycle must be the support of a mixed Nash equilibrium. It provides a rigorous proof that a complete cyclical set is necessary and sufficient to form the support of a Nash equilibrium. This implies that myopic algorithms, like AlphaZero, can in fact learn the support of a Nash equilibrium when they enter a cycle (or of course, learn a pure Nash equilibrium). Based on this intuition, the paper proposes a self-play algorithm, called GraphNES, that exploits the graph-search dynamics of the above formulation to either stop at a pure Nash equilibrium or to identify that it has entered a cycle. Empirical evaluations on Connect4 and Naruto Mobile suggest improved performance over baselines.

### Strengths
- The paper has a solid motivation: finding iterative self-play algorithms with low sample complexity is an interesting open problem. 
- The paper contains a rigorous result (Theorem 3.1) and interesting experiments in two games, Connect4 and Naruto Mobile.
- Some parts of the paper are clearly written, e.g., the introduction, and allow the reader to understand the context and claimed contributions of the paper.

### Weaknesses
 - The paper is generally not well-written. There are frequent typos (we shows, to illustrate the why, a MSNE union together, $(ps^1U, ..., ps^n)$, Theorem 3.1 ends without period), especially in the technical sections, and passages that seem out of place, e.g., the proof of Theorem 3.1 seems to end after the paragraph "Theorem Intuition" (bottom and middle of page 5 respectively). Also, some abrreviations are not defined, e.g., "is guaranteed by DO" and some definitions are not rigorous enough, e.g., "previous strategy" in a cyclical set or whether the paper only considers symmetric games (as indicated in some parts of the analysis).
- The finding of Theorem 3.1 is not surprising to me and it seems that it at least anecdotally known in the literature. Also, the paper seems to ignore a lot of papers on the average case performance of best response dynamics that have related results.
- The title does not seem representative of the context of the paper. Chaos does not seem to be relevant - and many recent studies on chaos are not referenced/acknowledged.
- Some claims seem to be poorly justified. E.g., why does "This allows us to represent the learning representation of an equilibrium point in noncooperative games as a directed graph search" (see Intro) or why "This aligns with Zermelo’s Theorem, providing theoretical validation." or "Hence, the learning representation of a noncooperative game as a graph provides a theoretical guarantee to
find a NE."
- Figure 2 is hard/impossible to parse due to the small font, but even then, I don't understand what do the numbers represent.
- The complexity of the proposed algorithm is not discussed and in particular, the problem of scaling this algorithm, is mentioned in the limitations of the paper. Thus, the paper provides only low-dimensional experiments. But this is precisely the problem that the algorithm was seeking to solve, to my understanding.

### Questions
I would appreciate the authors comments on the weaknesses mentioned above. However, based on my evaluation, I don't think that the paper is ready for publication. For this, it requires 1) a thorough improvement in its presentation, 2) more thorough experimental evaluation and 3) complexity analysis of its critical "Identify Cycle and Support Set" loop that indicates an improvement over current algorithms. Also, better placing the paper in the relevant literature on cyclical/chaotic dynamics in games would allow readers/reviewers to better evalulate the contribution of the theoretical result of the paper (stated in Theorem 3.1).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
