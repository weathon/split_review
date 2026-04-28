# Correlated dense associative memories

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 3, 3

## Abstract
Associative memory networks store memory patterns by forming dynamic attractors around chosen states of neurons. These attractors do not, however, need to be fixed points or single memory patterns. By correlating attractors, we may represent temporally or spatially related sequences or groups of stimuli. By further modulating these correlations using inhibitory (anti-Hebbian) learning rules, we show how such sequences and groups may be hierarchically-segmented at multiple scales. In combination with the dramatically-increased storage capacity of dense associative memory networks (also known as modern Hopfield networks) and their connection to Transformers, our results have implications for both machine learning and neurobiology. We demonstrate this by applying our networks, dubbed *Correlated Dense Associative Memory (CDAM)*, to model multi-scale representations of community structures in graphs, oriented recall in a symmetric connection regime, and temporal sequences with distractors in an asymmetric connection regime.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes "Correlated Dense Associative Memories" using an iterative update defined by the linear combination of an auto-associative signal and a hetero-associative signal. We can weight this linear combination strongly in favor of the hetero-associative signal to retrieve distinct and meaningful signals.

### Strengths
## Experiments clearly show method effectiveness on small data

- (++) The problem in the paper is clearly introduced and defended, and the simulated experiments justify the mathematical design proposed in Eq. (2) on simulated data. 
- (+) The experiments an interpretation of Dense Associative Memory that can be used for temporal sequence modeling, a problem where Transformer architectures are currently king.

**Originality**: This paper is novel to my knowledge and tackles the problem of hetero-associative memory when you are constrained to undirected graphs.

**Quality and Clarity**: This paper is well written and clear.

**Significance**: The contributions in this paper are primarily on simulated, small data, but touches an important problem in the field at large.

### Weaknesses
## Minimal experiments on real data; experiments primarily analyze effect of $b$

1. (- -) The paper does not include experiments on real temporal data. It is thus unclear how such a system could be applied to real problems. The experiments provided are limited to synthetic data, which does not fully capture the complexities of real-world temporal sequences. The absence of real-world validation makes it difficult to assess the practical utility of the proposed method.
2. (- -) The paper is missing analysis of the hetero-association dynamics as $t \rightarrow \infty$ at different values of $b$ (i.e., why did you choose to display results only at $t=10$?). Will the state blow up or converge to meaningful values? The lack of analysis on long-term behavior raises concerns about the stability and convergence properties of the proposed iterative update rule. It is crucial to understand whether the system reaches a stable state or if the state values diverge over time, especially with different values of $b$.
3. (-) Experiments only show correlations, not the actual state itself. I feel that the hidden state $S^{(t)}$ is blowing up in value and cannot be run at low values of $b$ for too long. The paper should include visualizations of the actual state values over time to provide a more complete picture of the system's behavior. The current focus on correlations alone is insufficient to understand the dynamics of the hidden state, and it is important to investigate if the state values are indeed diverging.
4. (-) Missing experiments that would consider alternative formulations of anti-hebbian modulation. Why should anti-hebbian modulation also amplify the signal from hetero-association? See Question 1. The paper's choice of anti-hebbian modulation is not sufficiently justified, and it would be beneficial to explore alternative formulations to understand the impact on the system's performance. The current approach may not be the most effective way to achieve the desired behavior, and alternative methods should be considered.

### Questions
1. Eq. (2) presents the linear combination between auto- and hetero-associative memory using the hyperparameter $b$ and $(1-b)$. But this notation hints at convex combination $b \in [0, 1]$, where $b=0$ implies only hetero-associative memory and $b=1$ implies only auto-associative memory. **Why do we need a full linear combination** instead of the more intuitive convex combination? Many results require $b<<0$ (which is what the authors call "anti-hebbian" modulation) to achieve meaningful results, which both inverts the signal from auto-associative recall and amplifies the signal from hetero-associative recall. Can the authors please clarify why we need such negative values for $b$? Could the same effect be obtained by using $b=0$ and running dynamics for more steps?

2. The Zachary Karate club example hints that this is a possible method for unsupervised clustering of data. Could the authors clarify how this method could be useful for generating clusters from data, if at all?


Typos:
- Sec 3.1 paragraph 1: "As we increase b" -> "As we decrease b"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a generalization of recently studied static and sequential Dense Associative Memories to settings where the sequences of memories live on a graph with connectivity matrix H, instead of living on a one dimensional line. The proposed update rule is also related to hetero-associative memory settings, which is a valid perspective.

### Strengths
1. The paper proposes to use graph connectivity to encode transitions between memories in a Dense Associative Memory model, which includes asymmetric weights. 

2. Sequential associative memories are connected to hetero-associative models. 

3. Structured graphs are used to embed memories into the CDAM model (this is done for the first time to my knowledge) and a successful recall is demonstrated.

### Weaknesses
In the present form the paper demonstrates the possibility to write pre-defined patterns with a given graph connectivity H to CDAM and read the patterns from it. While this is of course a non-trivial capability of the model, and a first step in studying this model, it would be great to illustrate the utility of the proposed framework for some useful downstream applications that a graph community might be interested in. Specifically, the paper lacks a clear demonstration of how this model could be used in practical graph-related tasks. The current experiments only show that the model can store and recall sequences on a graph, but it does not show how this capability can be leveraged for tasks such as node classification, link prediction, or graph clustering. The paper would benefit from showing how the proposed model can be integrated with existing graph learning frameworks or how it can be adapted to solve real-world problems. The experiments are limited to demonstrating the recall of pre-defined patterns, which, while important, does not fully justify the practical relevance of the proposed model for the graph community. The paper would be strengthened by showcasing its potential in more complex scenarios, such as noisy environments or when dealing with incomplete graph information. Additionally, the paper does not explore the scalability of the proposed approach, which is a crucial factor for practical applications in graph-related tasks.

### Questions
1. Could the authors imagine this network being helpful for some graph-related tasks that ML or graph community might be interested in? 

2. I am not sure I understand how the model uses the "transition" term (with the matrix H in equation 2) in situations when one node on the graph is connected to 2 other nodes. How does the model decide which of the two connected nodes it should give more weight and transition to? 

3. I am a little skeptical about using the model with negative $\beta$. In that case the softmax in equation 2 will pick the pattern with the smallest overlap with the current state $S$. Why would this setting be useful?  

4. Do the authors see any interesting phenomena for $b$ in the range [0,1]? When $b$ is less than 0, as in most case studies presented, the model needs not only jump to the next pattern (on the graph), but also unlearn the current pattern. Technically, there is nothing wrong with this, but keeping $b$ in the range [0,1] would be more natural.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a new associative memory model, which they name Correlated Dense Associative Memories (CDAM). Much of the prior work on associative memory models focus on the case of auto-associative memory, in which networks learn to recover memory patterns given parts of those same memory patterns. The authors instead explore hetero-associative memory retrieval, in which the recovered memory patterns differ from the given patterns. Using random and partially-random data, the authors analyze the properties of CDAM networks. They further study different network topologies and their impact on the embedded associative memory structures, and show that it can be used to model multi-scale representations of community structures in graphs, oriented recall in a symmetric connection regime, and temporal sequences with distractors.

### Strengths
- The introduction provides a good overview of the field. It gives a crisp summary of the intuition behind associative memory networks, and delineates the field’s current progress and some open problems.

### Weaknesses
 - The introduction barely discusses the contributions of this work; the contributions are relegated to single-sentences at the end with few details. It’s hard to interpret the results or impact of this work from the intro-- much of it reads like a background.
- The results section is hard to parse; it’s unclear to me what research questions the authors are trying to answer with their results section. I suggest adding an overview section and explicitly stating the goals of your experiments.
- Experimental design is poorly discussed. It's difficult to find basic information about the experiments, such as what dataset is used, or what refutable hypotheses each experiment is testing. The authors mention that they used both random and partially-random memory patterns; in the partially-random case they "use some real-world data." Where does this real-world data come from and what are its structural properties?
- There is insufficient discussion of the potential applications or usefulness of CDAM. The authors state that “our results have implications for both machine learning and neurobiology” but do not convincingly back up this claim. They discuss some connections to transformers in the future work section, but it is purely speculative.
- Frankly, this work seems very rushed and premature. It's less than 8 pages, with nearly half of the content occupied by figures. Brevity itself is certainly not bad, but when there are so many components of the paper inadequately discussed or simply missing, a short submission reflects poorly on the authors. Submitting incomplete work unfairly appropriates reviewer resources from complete submissions. I strongly discourage the authors from doing so again in the future, lest they risk tarnishing their academic reputation.

### Questions
- The novelty claim of this work is not immediately clear to me. Can you explain how CDAM qualitatively differs from the method and capabilities of hetero-associative MCHNs discussed by Millidge et al. (2022) which you cite?
- The experiments are mostly run on randomly generated data. This makes its impact on real-world problems hard to judge. How does CDAM perform on real-world data, or how do you expect it to perform?
- On what types of real-world problems should I use CDAM, and why? You claim that your results show that CDAM can be used to model multi-scale representations of community structures in graphs, oriented recall in a symmetric connection regime, and temporal sequences with distractors. In which domains do these problems appear, and how does CDAM compare to current approaches?
- Could you explain what anti-Hebbian learning rule you applied and why?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a model for heteroassociative memory that extends previously-proposed sequence memory models to store more general heteroassociations.

### Strengths
There is at present much interest in extensions of the classic Hopfield network, and the links between those extensions and the transformer architectures that are now ubiquitous in deep learning. This paper is therefore timely, and of potential interest to the community working on such memory models.

### Weaknesses
In the Abstract, the authors claim that "[their] results have implications for both machine learning and neurobiology." However, after reading the paper I was left wondering what precisely those implications were. In my **Questions** below, I detail several concerns regarding the presentation and substance of the results.

1. The overall motivation of the paper is, to me, rather unclear. Yes, the paper extends past work on sequence modeling using heteroassociative memories, but it is not made clear why this extension is of interest. This lack of clarity is accentuated by the fact that the simulations are not woven together into a coherent story. Rather, they read as independent vignettes, and it is not made clear why each is scientifically interesting.

2. In the list of contributions, the authors make an interesting claim regarding links between their model and studies of inhibitory plasticity in neuroscience. However, this link is never made concrete later in the paper. If there is a deeper link to neuroscience experiment, expanding on this point could help resolve my concerns regarding overall motivation, framing, and significance.

3. The weighted combination of autoassociative and heteroassociative terms in the update rule (2) resembles that used in previous works on discrete-state sequence models, c.f. the cited work of Kleinfeld & Sompolinsky (1988), work by Kanter & Sompolinsky (1986, Temporal Association in Asymmetric Neural Networks, not cited in the submitted manuscript), or eq. 13 of the cited work by Chaudhry et al. (2023). In those sequence models, tuning the relative weighting of the associative and heterassociative terms changes the dwell time of the system in a given state. Here, no clear motivation for the inclusion of the autoassociative term is given. The authors' empirical results (see for instance Figure 2) are consistent with the intuition that networks with small $b$ dwell near the initial state for longer, but they do not probe this carefully. Indeed, I think the authors' results on how varying $b$ determines which scales are "selected" are more precisely explained in terms of an increase in dwell time. This would be easy to probe by examining intermediate timesteps. In particular, they should examine how their model's dynamics relate to diffusion on the graph. This is also relevant to the question of what the overall objective of the proposed heteroassociative learning rule is. Finally, the parameterized weighting in (2), with $b$ and $1-b$, is a bit puzzling given that the authors proceed to consider $b = -100$; at this scale they are effectively considering $b$ and $-b$ as the weights. In short, more specific motivation for the combined update rule should be provided (including for why the authors are interested in continuous memories in this particular setting), and the resulting behavior probed more carefully.

4. In a similar vein to the above, the simulations do not probe some of the most basic properties of associative memories. How does the capacity of their model scale with the number of neurons? Related to point (3) above, how quickly does the model converge to each target state?

### Questions
1. The overall motivation of the paper is, to me, rather unclear. Yes, the paper extends past work on sequence modeling using heteroassociative memories, but it is not made clear why this extension is of interest. This lack of clarity is accentuated by the fact that the simulations are not woven together into a coherent story. Rather, they read as independent vignettes, and it is not made clear why each is scientifically interesting. 

2. In the list of contributions, the authors make an interesting claim regarding links between their model and studies of inhibitory plasticity in neuroscience. However, this link is never made concrete later in the paper. If there is a deeper link to neuroscience experiment, expanding on this point could help resolve my concerns regarding overall motivation, framing, and significance. 

3. The weighted combination of autoassociative and heteroassociative terms in the update rule (2) resembles that used in previous works on discrete-state sequence models, c.f. the cited work of Kleinfeld & Sompolinsky (1988), work by Kanter & Sompolinsky (1986, Temporal Association in Asymmetric Neural Networks, not cited in the submitted manuscript), or eq. 13 of the cited work by Chaudhry et al. (2023). In those sequence models, tuning the relative weighting of the associative and heterassociative terms changes the dwell time of the system in a given state. Here, no clear motivation for the inclusion of the autoassociative term is given. The authors' empirical results (see for instance Figure 2) are consistent with the intuition that networks with small $b$ dwell near the initial state for longer, but they do not probe this carefully. Indeed, I think the authors' results on how varying $b$ determines which scales are "selected" are more precisely explained in terms of an increase in dwell time. This would be easy to probe by examining intermediate timesteps. In particular, they should examine how their model's dynamics relate to diffusion on the graph. This is also relevant to the question of what the overall objective of the proposed heteroassociative learning rule is. Finally, the parameterized weighting in (2), with $b$ and $1-b$, is a bit puzzling given that the authors proceed to consider $b = -100$; at this scale they are effectively considering $b$ and $-b$ as the weights. In short, more specific motivation for the combined update rule should be provided (including for why the authors are interested in continuous memories in this particular setting), and the resulting behavior probed more carefully. 

4. In a similar vein to the above, the simulations do not probe some of the most basic properties of associative memories. How does the capacity of their model scale with the number of neurons? Related to point (3) above, how quickly does the model converge to each target state?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
