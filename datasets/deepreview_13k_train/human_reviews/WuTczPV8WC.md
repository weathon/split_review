# Optimal Non-Asymptotic Rates of Value Iteration for Average-Reward Markov Decision Processes

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
While there is an extensive body of research on the analysis of Value Iteration (VI) for discounted cumulative-reward MDPs, prior work on analyzing VI for (undiscounted) average-reward MDPs has been limited, and most prior results focus on asymptotic rates in terms of Bellman error. In this work, we conduct refined non-asymptotic analyses of average-reward MDPs, obtaining a collection of convergence results advancing our understanding of the setup. Among our new results, most notable are the $\mathcal{O}(1/k)$-rates of Anchored Value Iteration on the Bellman error under the multichain setup and the span-based complexity lower bound that matches the $\mathcal{O}(1/k)$ upper bound up to a constant factor of $8$ in the weakly communicating and unichain setups.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the convergence guarantees of the value iteration algorithm (VI) and some of its variants for average-reward MDPs. The following variants are considered: standard value iteration (Standard VI), Relaxed VI (Rx-VI), Anchored VI (Anc-VI). Further, the corresponding variants of the Relative VI algorithm are considered. The paper presents several results for these methods as well related lower bounds, all of which hold non-asymptotically. The lower bounds include a broad class of VI-type algorithms that satisfy a standard span-condition. Further, one lower bound is derived for the general class of multi-chain MDPs. In terms of upper bounds, it is established that a convergence rate of $O(1/k)$ is optimal as it matches the rate asserted by the lower bounds. They also apply to multi-chain MDPs.

### Strengths
The paper focuses on value iteration (and some of its variants) in the average-reward setting and presents several new results on their iteration complexities, substantially improving state-of-the-art, to my best knowledge. The presented upper bounds exhibit, in my view, some key strengths: they hold non-asymptotically; they cover multi-chain MDPs, which are quite general; and some of them are provably optimal. Further, the presented lower bounds that hold for a broad class of MDPs (multi-chain ones) are quite interesting. 

VI plays a key role in model-based reinforcement learning algorithms, and often appears there as a routine that must be run several times at each policy update. Hence, understanding iteration complexity of VI-style algorithms is important for the RL community.  

The paper does a great job in discussing and presenting VI (and the variants) in a systematic and precise way as fixed-point iterations. Although such connections are already known, most literature fail to provide precise pointers to relevant results on convergence of fixed-point iterations from communities beyond RL. 

The paper is well-written and well-organized, and the results and algorithmic ideas are presented very clearly. (I report below some typos and other relevant minor comments below.)

### Weaknesses
Comments about Literature
-
1- It was a good idea to provide pointer to works on average-reward RL. However, at least two key papers [1,2] appears missing. Further, (Zanette & Brunskill, 2019) must not have been cited as it deals with RL in episodic MDPs, and more importantly, it does not use any type of value iteration.

2- VI plays a key role in many algorithms designed for average-reward RL, beyond the tabular setting. For instance, it is used as a routine in algorithms developed for a wide range of settings including factored MDPs (e.g., [3]), robust MDPs [4], MDPs with reward machines [5], MDPs with options [6], etc. To further highlight the importance of VI, it might be necessary to enrich discussion in this part. I suggest the authors briefly expand the related work to address this. This makes the paper a better fit to the audience of ICLR.


Some Minor Comments
-
1. In Fact 2, you write $\pi_V$ to seemingly denote the greedy policy w.r.t. a value function $V$. However, it is not formally defined. 
2. In several places (e.g., Theorem 1), you use ‘/’ to denote set exclusion. Shouldn’t it be ‘\’ or ‘\setminus’ command in LaTeX? 
3. In line 317: In the second half of this rather long sentence (i.e., starting from “and in tabular setup”), you cite 4 papers, covering both discounted and undiscounted. But it is not fully clear that ‘respectively’ in the end maps which paper to which category.  
4. That you wrote 3.14 in lieu of the number $\pi$ to avoid overloading notation sounds rather strange. A fix could be to use text mode to write the number $\pi$.  
5. In line 456, did you mean Theorem 4 in the sentence “… improves the lower bound by constant factor of 2.”?
6. Line 394: Definition of “span” is missing. 


Some Typos
-
- l. 188: There exist line ==> … exists a line  
- l. 211: an near-optimal ==> a near-optimal
- l. 218: … of the Appendix ==> of Appendix OR of the appendix  ---- In some places (e.g., l. 280) you correctly used the latter form)
- l. 221: Table A.5 and A.6 ==> Tables A.5 and A.6  ---- It appeared elsewhere, e.g., l. 218, 370,…  
- Corollary 2: a a general ==> remove extra ‘a’
- l. 306: … MDPs satisfies ==> … satisfy
- Theorem 4: such that such that ==> such that

### Questions
See above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes value iteration methods for average-reward MDPs, focusing on the case of general/multichain MDPs. The algorithms studied are based off of Halpern and Kransnosel’skii-Mann iterations, as well as relative versions (which prevent divergence of iterates). New nonasymptotic upper bounds are established for the multichain setting, and lower bounds are also provided.

### Strengths
Since multichain MDPs are the most general setting and yet they have received relatively little attention compared to weakly-communicating settings, I think the nonasymptotic results on multichain MDPs are of good significance. 

It is nice to have lower bounds, and I think it is interesting that the standard VI is optimal in terms of the normalized iterates.

The paper is thorough in its presentation of related work, which I think will benefit the community.

### Weaknesses
It doesn't seem like there is a large amount of technical novelty/insight used to establish the upper bounds for multichain MDPs. I think the paper would be stronger if the authors could discuss any interesting technical novelties. It would also be nice if the main body of the paper could include some proof ideas.

Related to the above point, the proofs are not very easy to follow and could benefit from some discussion about the steps beyond just the statements of the lemmas. In particular, it would be nice for there to be discussion particularly about how the analysis differs from standard analyses for KM/Halpern iterations. The current presentation makes it difficult to understand the core ideas behind the analysis, and how the multichain setting necessitates different techniques.

The upper bounds for general MDPs do not match the lower bounds. This is another area which would benefit from some more technical discussion in the main body of the paper. It is unclear whether the gap is due to looseness in the upper bound, or the lower bound, and this should be clarified.

It seems unclear what the normalized iterate performance measure is actually useful for/why should we care about it (contrasting the Bellman error, which at least under some conditions is related to actual policy performance). The paper should provide more context on why this is an important metric to analyze, and what practical implications it has.

Typos:
The tables in Appendix A say "muAlti MDP"

### Questions
Are there any interesting technical novelties within the analysis of algorithms for multichain MDPs? Because value iteration is such a widely used algorithmic template in RL, I think it is easier to overlook the seemingly lower level of technical novelty of the paper if there are any simple but novel insights which might be applicable more broadly.

(Related) How does the analysis differ from standard analyses for KM/Halpern iterations?

Do you think it is possible to improve the Bellman error rate for general MDPs to match the lower bound? What are some challenges in doing so?

What is the normalized iterate performance measure useful for?

Is there a reason why it seems to be easier to get good performance for the normalized iterate performance measure rather than the Bellman error? (In the sense that standard VI works well.)

Typos:
The tables in Appendix A say "muAlti MDP"

### Soundness
3

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
3

### Summary
The paper investigates non-asymptotic convergence rates for value iteration algorithms in average-reward Markov decision processes (MDPs). The analysis convergence rates of O(1/k) for Anchored Value Iteration and O(1/sqrt(k)) for Relaxed Value Iteration under specific conditions, leading to a better understanding of these algorithms in multichain settings. Additionally, they establish matching lower bounds that indicate the optimality of their results for weakly communicating and unichain MDPs. While the theoretical contributions are notable, the paper could benefit from clearer explanations and empirical validation to support the theoretical findings.

### Strengths
1. The paper provides a detailed analysis of non-asymptotic convergence rates for value iteration in average-reward MDPs, addressing a gap in existing literature.

2. It establishes both upper and lower bounds for convergence rates, contributing to a clearer understanding of the performance of value iteration algorithms.

3. The theoretical results are presented with comprehensive proofs, demonstrating rigorous mathematical foundations.

4. The work includes novel findings on the complexity lower bounds for average-reward MDPs, which may inform future research directions in this area.

### Weaknesses
1. The paper lacks empirical validation of its theoretical results, making it difficult to assess the practical applicability of the proposed methods in real-world scenarios. Additionally, there is a limited discussion on how these theoretical findings might translate into practical implementations or inform algorithm design. Specifically, the paper does not explore the performance of Anchored Value Iteration (Anc-VI) and Relaxed Value Iteration (Rx-VI) on benchmark MDPs, nor does it provide any guidance on parameter tuning for these algorithms in practice. The absence of such experiments makes it hard to gauge the actual benefits of the proposed methods over standard value iteration in realistic settings.

2. The presentation is highly technical and may pose challenges for ML community researchers who are not deeply familiar with the underlying mathematical concepts, potentially limiting the accessibility of the research and further algorithm design. The authors should consider enhancing the understanding by providing more intuitive explanations, intermediate remarks and some visual/diagrammatic aids to complement their analysis. The current presentation relies heavily on dense mathematical notation and lacks sufficient explanation of the core ideas, making it difficult for a broader audience to grasp the significance of the results. For example, the paper could benefit from a clearer explanation of the span seminorm and its relevance to the convergence analysis.

3. There is no discussion of the computational complexity or scalability, nor any exploration of sensitivity analyses for key parameters. This omission raises questions about how well the characterized bounds hold for larger or more complex MDP settings. The paper should include a discussion on the computational cost per iteration for Anc-VI and Rx-VI, and how this compares to standard value iteration. Furthermore, the sensitivity of the convergence rates to the choice of the relaxation parameter λ needs to be analyzed, as this could greatly impact the practical performance of these algorithms.

### Questions
In addition to the mentioned weaknesses, I request authors to provide further clarifications on the following points :

1. How sensitive are the convergence rates of Relaxed Value Iteration (Rx-VI) and Anchored Value Iteration (Anc-VI) to the choice of the relaxation parameter ? Are there optimal choices that might specifically apply for different MDP classes?

2. The presented results show improved convergence rates for Anc-VI compared to Rx-VI. Are there scenarios where Rx-VI might be preferable, or is Anc-VI generally superior?

3. The paper establishes optimal complexity for standard VI and Anc-VI in certain MDP classes. Are there other value iteration variants or MDP classes not covered in this work? If so, it might be worth having a discussion on whether similar optimality is anticipated for those settings.

4. Are results presented applicable only for stationary MDPs ? It will be worth investigating how resilient these bounds are when the MDP is non-stationary i.e., unknown drifts/distribution shifts occur across time.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper consider the problem of learning average reward MDPs given the underlying dynamics. The major contribution is to  propose a simple but efficient iteration method (Anchored Value Iteration)  to learn a near-optimal policy. In comparison, the naive Bellman iteration method could only approximate the optimal value function, instead of a near optimal policy.

### Strengths
Overall I appreciate the technical effort to improve the order of $k$ by designing a proper learning rate sequence $\\{\lambda_k\\}_{k\geq 1}$.

### Weaknesses
The major concern is about the significance of the result. The condition number $\epsilon$ might be a problem in the worst case. In particular, I do not understand how  a $\delta-$sub-optimal state-action pair ($\delta\to 0$) forces a larger iteration number. Is there any lower bounds related to the condition number $\epsilon$?

I also wonder whether  the same problem exists in the case of discounted MDP.

Another concern is about the motivation. This work assumes access to the Bellman operator oracle, which is relatively strong in related fields. 

Minor point: Line 1556 and possible other places: the index in $\Pi$ should be $\Pi_{\ell=i}^{k-1}$, not $\Pi_{\ell=k-1}^{i}$.

### Questions
Please see the comments above.

### Soundness
2

### Presentation
3

### Contribution
2
