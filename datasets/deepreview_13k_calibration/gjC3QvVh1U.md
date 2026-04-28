# AlphaZero Neural Scaling and Zipf's Law: a Tale of Board Games and Power Laws

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Neural scaling laws are observed in a range of domains, to date with no clear understanding of why they occur. Recent theories suggest that loss power laws arise from Zipf's law, a power law observed in domains like natural language. One theory suggests that language scaling laws emerge when Zipf-distributed task quanta are learned in descending order of frequency. In this paper we examine power-law scaling in AlphaZero, a reinforcement learning algorithm, using a theory of language-model scaling. We find that game states in training and inference data scale with Zipf's law, which is known to arise from the tree structure of the environment, and examine the correlation between scaling-law  and Zipf's-law exponents. In agreement with quanta scaling theory, we find that agents optimize state loss in descending order of frequency, even though this order scales inversely with modelling complexity. We also find that inverse scaling, the failure of models to improve with size, is correlated with unusual Zipf curves where end-game states are among the most frequent states. We show evidence that larger models shift their focus to these less-important states, sacrificing their understanding of important early-game states.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The current paper explores scaling laws in an RL setting---specifically, in board games. The main goal (at least as I understand) is to borrow prior theory on explaining LLM scaling laws to investigate scaling laws in an RL setting. To this end, the authors first show that the assumptions of prior theory (zipfian distribution of tasks) is met in this setting (since board games have a tree-like data-generating process). The authors' investigations also leads to the demonstration of an inverse scaling effect, which they argue is explained by larger models memorizing relatively endgame states, which are relatively less important, at the cost of reducing loss on earlier game states, which are important for developing solid opening strategies. Overall, this is a good model system work, wherein a synthetic abstraction (a model system) is used to study some phenomenon of interest (scaling laws), but my apprehension lies in lack of a coherent question-driven narrative.

### Strengths
Though scaling laws have been explored in RL before (see Jones 2021), the current paper is broader in its scope. It often centers itself in a prior theoretical framework by Michaud et al. (2023), with several experiments primarily verifying the validity of that framework. I'm a big fan of such synthetic studies, and hence really like the experiments in the paper. For example, these experiments allow authors to develop a concrete demonstration of inverse scaling. The paper is also well written (though there are certain parts that can be made more precise, e.g., simply specifying what a "state" means).

### Weaknesses
 - **Unsure what the point of the paper is.** My biggest apprehension with the paper is that I am unsure what the guiding question is. I currently see the paper as replication of scaling laws in RL / board games (which we know is possible because of Jones 2021) and a validation of Michaud et al. (2023)'s theory of how scaling laws arise. Given the latter paper never makes an assumption about modality, but merely relies on the existence of a multi-task setting with a Zipfian prior, any setting that satisfies these conditions should yield a power law scaling with increase in model / data size. I note that it's certainly good to confirm theories in different settings, but I'm apprehensive of accepting a paper for merely that reason. Overall, then, I argue results in the paper are either known or relatively expected corollaries of prior results. If I'm missing something, please let me know what questions the paper's contributions help address, and I'd be happy to reevaluate my opinions accordingly.

- **How does the proposed inverse scaling hypothesis connect with prior explanations of the concept?** A possibly novel result may be the exploration of inverse scaling in this work, but I first need to clarify how the proposed hypothesis is different from prior work on the topic. For example, in the original inverse scaling paper by McKenzie et al., the main connecting thread between several tasks is that there are multiple viable ways of responding to a query, but the model starts to prefer using an undesired way (e.g., by relying on some distractor features) as it is scaled. This leads to a reduction in performance as size is scaled. Is the proposed hypothesis by authors, i.e., inverse scaling is driven by memorization of a set of endgame states (which will lead to faster loss reduction), inline with prior distractor features hypothesis? If not, how is the proposed hypothesis different? 

- **Related work.** Related to both points above, I think authors did not properly situate their work with respect to existing work: are you trying to develop a new hypothesis for a given phenomenon, are you trying to identify a new phenomenon, or are you trying to simply verify existing theories? Generally, the relevant literature on all these questions should be cited and discussed, but especially if a new hypothesis is being proposed, at least a contrast should be made between the new and previous hypotheses to help clarify how the current one is different (e.g., prior work on inverse scaling should be cited https://proceedings.mlr.press/v238/ildiz24a/ildiz24a.pdf.

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper explores the relationship between neural scaling laws for the AlphaZero-type RL algorithms and Zipf's law, and the authors observe that the frequency of game states encountered by AlphaZero during training and testing adheres to Zipf's law. This pattern arises from the tree-like structure of board games, where certain states are more frequently visited than others.

### Strengths
The application of Zipf’s Law in RL contexts is innovative, and the paper has conducted substantial empirical analyses to support its core hypothesis: AlphaZero’s experience with game states follows Zipf’s distribution and correlates with neural scaling behavior. The paper also finds that inverse scaling, the failure of models to improve with size, is correlated with unusual Zipf curves where end-game states are among the most frequent states.

### Weaknesses
While the paper explores an intriguing connection between scaling laws and Zipf's law within the context of AlphaZero, a key concern is the practical utility of the discovered scaling law for advancing RL algorithms in meaningful ways --- the paper does not clarify how the observed relationship between state rank and frequency could directly inform the development of improved RL algorithms or strategies for board games or other RL tasks. For instance, if this relationship could guide the allocation of computational resources or suggest new exploration strategies, it would strengthen the practical relevance of the findings. 

Additionally, the work lacks sufficient intuitive explanations for the scaling law it reports. The authors could, for example, discuss why certain states might consistently follow Zipf’s law in terms of frequency and how this frequency pattern impacts AlphaZero’s learning efficiency. Some illustrative figures/plots would be helpful. Without these insights, it is challenging to interpret the implications of the scaling law or understand how it might generalize to other RL environments. Providing concrete examples or scenarios where this scaling law could impact AlphaZero's decision-making process or resource allocation would make the findings more actionable and relevant for the RL community.

### Questions
1. What's the practical usage of the discovered scaling law? Can the observed relationship between state rank and frequency improve the design of RL algorithms?
2. Can the discovered scaling law generalize to RL environments beyond board games, particularly those with continuous state and action spaces? If so, what would be the theoretical basis for this?
3. The inverse scaling phenomenon is an intriguing observation, but its causes are not fully explained. Could the authors elaborate on potential factors contributing to this behavior? 
4. What's the connection between the discovered RL scaling law for AlphaZero and LLMs?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies scaling laws for for AlphaZero, and RL algorithm, and aims to connect it to insights from a previous work, Michaud et al. '23, that proposes that the capabilities of a neural network are composed of discrete “quanta” that each help reduce loss on a subset of training examples, and that are learned in approximately decreasing order of frequency. If the quanta are present in a Zipfian (power-law) frequency distribution in the training data, and each quantum is approximately equally valuable in the examples where it’s present, such a theory would provide a mechanistic explanation for power law scaling of loss with respect to model and dataset size. This paper is empirical, and exhibits the Zipf-law (or approximations/variations of it) of game states for 4 games: Connect4, Pentago, Oware and Checkers. It shows that Zipf's law arises in self-play in AlphaZero style algorithms (which was already known in other settings/games). The paper then studies (empirically) the scaling laws that arise, the loss distribution over game states as a function of their rank/frequency. It also shows some inverse scaling for two of the games and relates it to anomalies in the Zipf distribution.

### Strengths
A novel contribution is the empirical observation that self-played games also lead to Zipf law distributed data, not just human games. Another nice insight is a loss-analysis as a function of state rank showing that loss increases for less frequent state. While this is neither surprising nor counterintuitive it is nice to see this clear picture.
The paper is very well written and contains a good number of experiments and empirical analyses. I like the deep dive into the reasons for inverse scaling, even though they seem to stem from idiosyncracies of certain games (and not all games). 
It has a genuine and immediate acknowledgement of limitations after each section. A good, critical and honest review of related work is given.

### Weaknesses
A crucial weakness of this paper is the lack of convincing connection to the quanta theory or even the necessaity to make this connection, not to mention the even more far fetched claimed connection to LLMs. The paper establishes that game states obey a Zipf law, and then invokes the quanta theory to say that this implies scaling laws and emergence. This seems to ignore the rather vast literature of other theory papers that derives scaling laws by starting from a power law distribution on the data. The simplest such example is the infinite-memory model of Hutter which starts with a power law on the data distribution as an assumption to derive scaling laws. But there are many other such papers (Cui et al, Cabannes et al'23, Maloney et al'22, the work of Pehlevan's group etc etc. Another poignant exposition on the role of the tails of the power-law distributed data can be found in Dohmatob et al ICML'24). All of these paper should be cited - and discussed).

I thus view this paper mostly as a curious empirical paper, which in itself is not a weakness. But then several insights strongly depend on the idiosyncracies of each game (in particular the late turn difference between Oware/Checkers versus Connect4/Pentago). In my view, a theoretical analysis is lacking (which is fine if it wasn't for the prominent overpromising of explainability from the quantization method. Again: I do not see how this method is different from other methods that assume a Zipf law on the data and then prove a scaling law.)

To relate to the theory of quanta (if you must), another weakness is the identification of game states with quanta. Surely, there must be equivalence classes of games that could more closely match this notion. I also do not see how this paper "relates RL to language". That Zipf laws exists in states of game play was known (as the authors also point out).

Minor:
1) Line 99: what is the definition of \chi?
2) Figure 3B is not referenced anywhere in the text, it seems. To which paragraph does it belong?

### Questions
0) I am unclear on what exactly you call a game state when you establish the power law histograms. Is it a configuration of the game on the board, or would you call two configurations that look exactly the same *different*, if they have been reached through two distinct series of moves? I infer from the context that you probably refer to the latter (as is also done in the physics paper on chess), but please clarify directly when you define them.
1) I find the connection to LLMs (line 292 and following) way too speculative and unsubstantiated. Can you elaborate?
2) LIne 313: "The fact that the quantization model predicts this unintuitive behavior supports the claim that it could
explain AlphaZero scaling." - How so?
3) Why do large models overfit, lines 457 and following: Here is where you could have explained more, expecially if the quanta hypothesis would hold. The connection to distribution shift is not clear to me - do you have any evidence there?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The main goal of this paper is to demonstrate the connection between performance (ELO) scaling and Zipf's law (power-law distribution of states) in reinforcement learning (RL) agents for board games. The study examines how temperature in policy sampling affects scaling coefficients and also reports the inverse scaling phenomenon, where performance declines above a certain model size.

### Strengths
1. The paper clearly describes the procedures and results of the experiments.
2. The paper presents a clear demonstration of Zipf’s law in game states and examines how this is influenced by game rules and policy sampling temperature.
3. The paper establishes a link between Zipf's law in game states and performance (ELO) scaling.
4. The paper reports the interesting observation of inverse scaling in RL agents for board games and attempts to provide an explanation for this phenomenon.

### Weaknesses
1. The paper relies on a vague assumption that treats individual game states as "quanta" in a quantization model, but lacks verification or discussion of this assumption.
2. Related to point 1, the paper does not demonstrate that the model learns different game states orthogonally, raising questions about the validity of this assumption.
3. Also related to point 1, the paper does not show that the frequency of each game state is linked to performance gains from learning that state, further questioning the validity of the assumption.

### Questions
Could you address the weaknesses outlined above? For example, two types of analysis could provide a more rigorous justification for treating game states as quanta, which would strengthen the soundness of the paper. (1) Can you provide an analysis correlating state frequency with performance improvements? For instance, you could analyze how changes in value prediction accuracy or policy quality for specific states relate to their frequency in the training data. (2) Can you show how the loss of specific states decreases over training time and whether the learning of each state is independent of others? These would help to validate the concept of states as quanta.

### Soundness
3

### Presentation
3

### Contribution
3
