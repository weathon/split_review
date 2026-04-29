## Human Reviewer 1

### Questions
There are some questions for the authors. 

* The authors show the importance of the multiplicative constants via numerical evaluations. Though the numerical studies proves the advantages of the UCBVI-bf method, it is not straightforward to show that the advantages come from the smaller constants. The reviewer believes the cumulative regret is not a good enough signal. 

* For researchers proving the lower bound, the reason we discard the constants is that we assume that it may take a large number of interactions before the algorithm converges, leading the importance of the convergence orders instead of the constants. 
However, in the numerical studies, it seems that $T$ is not large enough when the proposed method starts outperform the alternatives. Thus, it is not convincing enough that the multiplicative constants are truly crucial.

 * In addition, the authors considers the regret bound in bandit problems in section 3. However, the title of the manuscript is for Reinforcement Learning. The authors have not deliver a better algorithm (with lower constants) under real RL problems (stage-dependent). Thus, it is also convincing enough to claim the multiplicative constants are important for RL problem.

### Rating
3

### Confidence
3

---

## Human Reviewer 2

### Questions
Could you provide more examples where the loose constants in the regret bounds are detrimental to the empirical performance?

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Questions
- Would there be any potential downside in considering lower-order terms and constants when designing practical algorithms? Could the authors offer any insights on potential tradeoffs (*e.g.*, computational overhead)?
- Can similar refinements with constants be applied beyond the finite-horizon tabular RL (*e.g.*, to settings with function approximation or model-free RL)? Could the authors suggest any concrete future directions?

### Rating
5

### Confidence
3

---

## Human Reviewer 4

### Questions
This paper makes a valuable theoretical contribution by highlighting the importance of constants in regret minimization. However, its message is not as original as the paper claims, and is somewhat aggressively expressed at some points. 
Moreover, the authors did not seriously list all the articles sharing the same care for constants.
In a nutshell, this is a thought-provoking read for RL theorists and practitioners that would need some corrections and complements before publication.


The writing quality of this paper is clear and well-structured but has some readability issues due to its dense mathematical content and occasional awkward phrasing. 
In particular, the proofs in appendix are lengthy and it would be usefule to help the reader by providing a proof sketch or at least a structure in the proof


    "Ignoring multiplicative constants when evaluating whether an algorithm matches the problem’s lower bound may lead to disappointing results when using such an algorithm."
    "when using such an algorithm" is redundant and wordy.
    Suggestion: "Ignoring multiplicative constants when evaluating whether an algorithm matches the problem’s lower bound may lead to disappointing practical performance."


    "Starting from the well-known UCBVI algorithm, we improve  UPON the bonus terms and the corresponding regret analysis."


    "Constants matter in two key moments: (i) Algorithm design: the exploration strategy of the algorithm should be designed to enforce the minimal required exploration needed in order to achieve the desired regret performance."
    Issue: "the minimal required exploration needed" is redundant.
    
    
    
    "This reduction in over-exploration has significant empirical effects, as shown in the experiments in Section 4, where, as reported in Table 1, we achieve an improvement in the empirical regret of 1.87 times."
-> "This reduction in over-exploration has significant empirical effects, as shown in the experiments in Section 4, where we achieve a 1.87× reduction in empirical regret."

 Lemma C.1 : very classical better bound, see e.g. https://www.stat.cmu.edu/~larry/=sml/Concentration.pdf Lemma 7.37

### Rating
4

### Confidence
4