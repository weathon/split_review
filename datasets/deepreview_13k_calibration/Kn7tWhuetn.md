# On the Markov Property of Neural Algorithmic Reasoning: Analyses and Methods

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 6, 8, 8, 6

## Abstract
Neural algorithmic reasoning is an emerging research direction that endows neural networks with the ability to mimic algorithmic executions step-by-step. A common paradigm in existing designs involves the use of historical embeddings in predicting the results of future execution steps. Our observation in this work is that such historical dependence intrinsically contradicts the Markov nature of algorithmic reasoning tasks. Based on this motivation, we present our ForgetNet, which does not use historical embeddings and thus is consistent with the Markov nature of the tasks. To address challenges in training ForgetNet at early stages, we further introduce G-ForgetNet, which uses a gating mechanism to allow for the selective integration of historical embeddings. Such an enhanced capability provides valuable computational pathways during the model's early training phase. Our extensive experiments, based on the CLRS-30 algorithmic reasoning benchmark, demonstrate that both ForgetNet and G-ForgetNet achieve better generalization capability than existing methods. Furthermore, we investigate the behavior of the gating mechanism, highlighting its degree of alignment with our intuitions and its effectiveness for robust performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the Markov property of neural algorithmic reasoning. More specifically, neural networks that learn to imitate algorithmic execution have thus far used as additional inputs data from the algorithmic traces at previous execution steps, not just the current step. The paper emphasises that, as the studied algorithms are Markovian, a better alignment between the neural network and the task should mean not using data from previous execution steps, which are named historical embeddings in the paper. This work uses an established architecture as the baseline, and with the removal of the historical embeddings proposes ForgetNet. Further, G-ForgetNet is obtained by using a gating mechanism to learn how much to use the historical embeddings within the baseline. The proposed changes outperform the studied baselines, and a simple ablation study on the gating mechanism shows the importance of using historical embeddings early on in training, when accumulating errors can be more harmful for final performance.

### Strengths
The paper is well motivated and clear. The proposed changes are supported by the empirical evaluation on the CLRS-30, outperforming the baseline in most algorithms.

### Weaknesses
The initial hypothesis — that better alignment with the markovian property should result in better performance — is strong. However, there are trainability issues (e.g. accumulating errors early in training) that can be addressed in different ways. The paper proposes one solution, gating, but some questions remain — why is gating better than the NN more generally learning how to combine historical and current embeddings, as in the baseline? Moreover, what are other solutions, possibly not involving learning?

Lastly, the TripletGMPNN includes a gating layer in the single-task setup. A discussion on how this differs from the gating in G-ForgetNet should be included.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes ForgetNet, a GNN that enforces Markov structure across algorithmic reasoning steps.
- Motivation: algorithmic tasks (e.g. sorting) can be modeled by transitioning through states which is Markov in nature, whereas existing methods use the history.
- Solution: ForgetNet enforces such Markov structure by updating the representation at each step usingfeatures at the current step only.
    - i.e. the hidden states at time $t$ is updated as $\{h_i^{(t)}\} = f_{\text{GNN}}(\{x_i^{(t)}\}, \{e_{ij}^{t}\}, g^{(t)})$, for node features $x$, edge features $e$, and global feature $g$.
- Further challenge: empirical results suggest that such Markov structure may cause training instability issues at early stage of training, likely because the intermediate steps are too unconstrained (note that supervision is provided only on the final state).
- Solution: G-ForgetNet, which selectively and adaptively keeps some history using a gating mechanism.

### Strengths
Another way to state the results is that
1. for better generalization, the authors proposed to restrict the function class by excluding non-Markov solutions, leading to the proposed ForgetNet.
2. the restricted function class raises optimization challenges. To address these challenges, the author incorporates a gating mechanism that selectively incorporate the history.

Both these changes are natural/simple yet effective: the proposed G-ForgetNet outperforms baselines in most tasks in the CLRS-30 benchmark.

### Weaknesses
 - The discussion about the motivation could be improved.
- About the motivation that "algorithmic reasoning tasks are Markov": it should be clarified that this work is about algorithmic reasoning tasks that can be modeled by finite-state automata. In general, whether the process is Markov or not depends the definition of the state space. The paper should explicitly define the state space for the algorithms considered and justify why the Markov property holds under that definition. For example, in sorting, is the state space the partially sorted list, or some other representation? How is the state space represented in the GNN?
- Even though the Markov observation motivates to remove history information, history information proves to be important for stabilizing training (hence the proposal of G-ForgetNet). This is similar to the effect of residual links, which can be discussed more in the paper. The paper should discuss in more detail why the Markov property is helpful for generalization, and why the history is needed for optimization, and how the gating mechanism addresses this trade-off.

### Questions
- Fig 4 (b): what are execution steps, and how are the labels acquired? Since there are labels to compute the per-step loss, can we also compare with per-step teacher forcing?
- Fig 5: for better comparison, could you also provide the norm of the residual branch in the baseline?
- I wonder if one can anneal the gating, i.e. gradually reducing the amount of the history (e.g. by controlling the gating value).
    - One motivation is that in Table 1, when G-ForgetNet is not better than the baseline, its performance is very close to the baseline. This suggests that G-ForgetNet falls back to the baseline in these cases, hence ensuring the history embeddings are actually not being used may help with performance.
    - Another reason is that according Fig 5, the gate value is ~0.38 even at the end of training. This means the history embeddings are still helpful, which weakens the claim that the task should be Markov, unless the history embeddings are effectively removed.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies a gap in the existing GNN literature -- while encoder-processor-decoder architectures typically have hidden states passed between calls to the processor, this work investigates the best way to handle those connections in the setting of algorithmic reasoning.

### Strengths
1. The work is original to my knowledge. In fact, I went through related work looking for experiments, claims, and ablation studies relevant to this paper. I expected to see some justification or discussion of the hidden states and the way they are used in other GNN architectures. I could not find a sufficient example and so I think question the architecture and showing that omitting hidden states all together or otherwise limiting the information flow through those connections is a valuable addition to the literature.  
2. The quality of the writing is good. I think the paper is well motivated and clearly written.
3. The conclusions are significant. The fact is that on a 30-problem benchmark suite, the two architectural changes proposed in this work generally improve performance.

### Weaknesses
1. The discussion of the Markov nature of algorithms could use some nuance. If it is the case that these algorithms, when processing entire graphs, therefore having some history in the 'state' are Markov, then the historical information in the hidden features shouldn't help. In fact, this work shows that a gated layer is better than no connection for passing information with the hidden states. Thus, I think the story arc is a bit confusing. It actually took me several readings to really piece together the fact that the treatment of the hidden state is under discussed in the literature and the two options presented in this paper are better than the existing approaches as a result of the confusing Markov narrative. This is perhaps a small point, and I'm only one reader -- if the Markov framework helps convey the story to others this is my weakness, and not the paper's but I though it was worth mentioning here.

### Questions
1. In most algorithms ForgetNet beats the baseline (Figure 3). Is there any intuition or hypothesis around which particular algorithms the baseline is better? For example, for Naive String Matcher the baseline looks considerably better. Why might that be?
2. I really like the visualization with bars in Figure 1, I think adding G-ForgetNet to that graphic or otherwise including a plot with the G-ForgetNet results would help. Can the authors provide such a visualization?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to reconsider the Markov property of neural algorithmic reasoning. While classical algorithms inherently possess the Markov property, existing neural algorithmic reasoning approaches learn to execute algorithms using historical embeddings, which contradicts this property. Building on this observation, this paper proposes ForgetNet, a method that eliminates the reliance on historical embeddings to reintroduce the Markov nature. Additionally, the paper introduces G-ForgetNet, which adaptively integrates historical embeddings.

### Strengths
1. This paper focuses on an emerging and interesting research topic: neural algorithmic reasoning.
2. This paper is well-written. Figures and formulas clearly illustrate the background and proposed method.
3. The motivation for aligning current algorithms with their Markov nature is well stated. Additionally, this paper complements a crucial concept in the context of neural algorithmic reasoning.
4. Experiments show that the proposed method can outperform baselines in most of the tasks (algorithms).

### Weaknesses
1. Although ForgetNet perfectly possesses the Markov property of algorithm execution, the newly proposed G-ForgetNet still utilizes historical embeddings but outperforms ForgetNet. Is there an inherent drawback of neural algorithmic reasoning in possessing the Markov property?
2. For certain tasks, G-ForgetNet performs worse than ForgetNet, or ForgetNet performs worse than the baseline. Some task-specific explanations regarding this should be discussed.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper points out that most algorithmic tasks should have Markov property and thus the optimal model should not rely on historical embeddings. The paper then proposes ForgeNet and GForgerNet which doesn't use or only limitedly use historical embeddings.

### Strengths
1. There is a novelty in observing the Markov property of many algorithmic tasks and proposing an architecture that aligns with this property.
2. The overall performance seems to be better than all compared baselines.
3. The paper is quite well-written and easy to follow.

### Weaknesses
The authors claimed that the gating value should decrease because  "As training progresses and the model starts predicting more reliable intermediate predictions". But if there are no regularisation terms on the gating variable, why should the gating value decrease if there is still useful information in the historical embeddings?  The authors do show a plot of the gating variable trajectory as training progresses, but the gating value only decreases slightly and never to 0. Are there any cases where the gating variable decreases to 0? If not, why is this the case since the model can just simply ignore the historical embedding after training stabilizes?

### Questions
See weakness,

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
