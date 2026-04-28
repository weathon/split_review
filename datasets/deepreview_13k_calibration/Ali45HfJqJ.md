# Observer Uncertainty of Learning in Games from a Covariance Perspective

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
We investigate the accuracy of prediction in deterministic learning dynamics of zero-sum games with random initializations, specifically focusing on observer uncertainty and its relationship to the evolution of covariances. Zero-sum games are a prominent field of interest in machine learning due to their various applications, such as Generative Adversarial Networks. Concurrently, the accuracy of observation in dynamical systems from mechanics has long been a classic subject of investigation since the discovery of the Heisenberg Uncertainty Principle. This principle employs covariance and standard deviation of particle states to measure observation accuracy. In this study, we bring these two approaches together to analyze the follow-the-regularized-leader (FTRL) algorithm in two-player zero-sum games. We provide growth rates of covariance information for continuous-time FTRL, as well as its two canonical discretization methods (Euler and symplectic). Our analysis and experiments shows that employing symplectic discretization enhances the accuracy of prediction in learning dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigate the evolution of observer uncertainty in the Follow-the-Regularized-Leader dynamics for learning to solve zero-sum games. The authors prove concrete rates of covariance evolution for different discretization schemes. The proofs rely on the techniques from symplectic geometry for analysing the evolution of uncertainty.

### Strengths
The authors provide rigorous, theoretical analysis for the uncertainty in the Follow-the-Regularized-Leader dynamics for learning to solve zero-sum games. The proofs are given in detail. The paper is well written.

### Weaknesses
I would say this paper is not well-motivated. I appreciate the mathematical rigour of the theory, but can hardly see how it is useful for machine learning. The authors are needed to clarify why we need to study this problem, and how the results would contribute to the community in the context of machine learning (such as understanding algorithms or designing new algorithms?)

I am also concerned about the novelty. The first 5 pages do not include new theory. Section 4 seems directly from Cheung et al. (2022). The proofs for Section 5 heavily rely on existing results - a very large proportion of the "proofs" are actually quoting existing papers, and the new part seems actually combining existing lemmas/propositions, or simple matrix calculations. Please clarify.

I was excited to see the abstract talks about Heisenberg Uncertainty Principle, but later found little theory is really relevant - please consider removing "Heisenberg Uncertainty Principle" or giving more discussion.

### Questions
Please address the above.

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
The authors study the observer uncertainty in deterministic learning dynamics of zero-sum games with random initializations. They explore the follow-the-regularized-leader (FTRL) algorithm in two-player zero-sum games and analyze its continuous-time as well as Euler and symplectic discretization dynamics. They give bounds on the growth rate of the covariance variables (cumulative payoff and cumulative strategy) during evolution for CT, Euler and symplectic cases for L2 and negentropy regularizations. They also establish a Heisenberg-type uncertainty inequality for variances of variables under CT, Euler and symplectic dynamics under general regularizers. Furthermore, they demonstrate by analysis and numerical experiments that symplectic discretization improves the accuracy of prediction in learning dynamics.

### Strengths
The uncertainty inequality for general regularizers and its connection to Hamiltonian systems seem interesting and original. Motivation, objevtives and results are stated clearly.. Theoretical results are also easy to follow.

### Weaknesses
related works can be discussed more comprehensively.  the limitations of the results and assumptions can be eloborated more to make it easier to follow.

### Questions
I don't have any questions to authors.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the evolution of uncertainty or observation accuracy in game dynamics by characterizing the growth rate of a certain covariance information. In particular, they focus on two-player zero-sum games and the continuous-time FTRL with different regularizers, as well as two discretization methods, namely Euler and sympletic. The theoretical results reveal that the symplectic discretization improves the accuracy of prediction in game dynamics, which is also confirmed experimentally.

### Strengths
The paper provides a novel characterization of continuous-time FTRL and discretizations thereof in two-player zero-sum games. The new results are also connected to earlier works (such as Cheung and Piliouras (2020) and Cheung (2022)). The separation in the behavior of  Euler versus sympletic discretization is also conceptually interesting. Furthermore, the results are non-trivial from a technical standpoint, combing tools from different areas. It is possible that such techniques could be of independent interest for future work in this area. The results appear to be sound; I did not find any notable issue.

In terms of the presentation, the writing overall is clear, and the key ideas are carefully explained. It was generally easy to follow the paper.

### Weaknesses
The main issue I have is with regards to the motivation and the significance of the results. Although the authors already attempt to discuss about the motivation in quite length in the introduction, I still cannot see any concrete motivation or applications for those results. Overall, the paper provides throughout several facts about the game dynamics but without explaining the significance of the characterization. Can the authors provide some actual applications where the new results can be relevant? Otherwise the results appear to some extent artificial.

A couple of minor stylistic issues:

1. Footnotes should come after punctuation marks
2. The references are not used appropriately; for example Go Silver et al. (2016) should instead be Go (Silver et al.)

### Questions
A couple of minor stylistic issues:

1. Footnotes should come after punctuation marks
2. The references are not used appropriately; for example Go Silver et al. (2016) should instead be Go (Silver et al.)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the evolution of observer uncertainty, mainly measured by covariances, in learning dynamics of two-player zero-sum games. The authors focus on the continuous-time FTRL algorithm and its two discretization schemes, Euler and symplectic discretization, which are equivalent to simultaneous and alternating GDA/MWU for certain regularizers. The authors show that for Euclidean regularizer, Euler discretization exponentially amplifies the covariance, while continuous-time FTRL and symplectic discretization amplify the covariance of cumulative strategies polynomially and keep that of cumulative payoffs bounded. As a comparison, the differential entropy of alternating MWU remains constant, which implies that covariance might be a better measurement of observer uncertainty. For general regularizers, the authors establish a Heisenberg-type inequality on variances to demonstrate the tradeoff between strategy spaces and payoff spaces.

### Strengths
The strengths of this paper mainly lie in its novelty.
1. The authors propose covariance to measure the observer uncertainty and provide evidence to show that it could be a better measurement than differential entropy.
2. The paper establishes the connection between Euler/symplectic discretization and simultaneous/alternating algorithms through the Hamiltonian system and provides a new perspective to analyze simultaneous and alternating GDA. Moreover, the results demonstrate that the alternating algorithm is more stable than the simultaneous one.
3. Although I do not check the details of the proofs, I believe they are correct.

### Weaknesses
I have some doubts about the significance of this paper and there is room for improvement in the presentation.
1. Although the authors claim that the 'input uncertainty' is well-motivated, I am still skeptical about this. For a convergent trajectory, measuring such an uncertainty could tell us (i) how fast we approach the solution; (ii) the initialization would not affect the convergence. However, for a non-convergent trajectory, measuring this uncertainty seems only to tell us whether the trajectory remains bounded or how fast it diverges. Although the results in this paper seem solid, I do not know what are the further implications for these cycling or divergent behaviors.

2. Some results related to cumulative strategies lack interpretation.
The adaptation of cumulative payoffs is easy to understand because we could map it into the strategy space through $\nabla h^*$. However, the adaptation of cumulative strategies seems just to facilitate the definition of the Hamiltonian system. Dividing it by $t$ yields a more intuitive meaning, i.e., the averaged strategies. Consequently, I think that the results in Theorem 5.1 could be transformed into those related to averaged strategies. Then the difference between the covariances of averaged strategies and cumulative payoffs can be better analyzed, because they represent the averaged-iterate and last-iterate behavior, respectively. In particular, I think it is also worth discussing the relationship between the results in Theorem 5.1 and the no-regret property of FTRL as well as the convergence of the averaged strategies. Finally, I do not understand the meaning of the covariance between cumulative strategies and payoffs.

3. The form of symplectic discretization may be not rigorous. If we adopt the symplectic Euler method in [1, Theorem VI.3.3], the update rule of $Y^t$ in symplectic discretization (Type I method) should be $Y^{t+1} = Y^{t} - \eta \nabla_X H( X^t, Y^{t+1} )$, while the authors use $Y^{t+1} = Y^{t} - \eta \nabla_X H( X^t, Y^{t} )$. Although for the Hamiltonian function defined in Proposition 3.1, the two versions are equivalent, I think adopting the latter one may be misleading and less rigorous.

4. The lower bound in Theorem 5.2 involves the covariance, while the amplification rates in Theorem 5.1 only hold for the Euclidean regularizer. For general regularizers, without the amplification rates of the covariance, the result in Theorem 5.2 itself is less meaningful.

Minor concerns
1. The authors could give more intuition on the definition of the Hamiltonian function.
2. The dependence of $\mu$ in Theorem 5.1 on the step size should be clarified.
3. To capture the exponential growth, one could change the y-axis to a log scale. Similarly, to capture quadratic (or more generally, polynomial) growth rate in figures, one could change both axes to log scales.

### Questions
1. The results about differential entropy in Section 4 are in terms of MWU and AltMWU, while covariance evolution results in Theorem 5.1 only hold for the Euclidean regularizer, i.e., GDA and AltGDA. They are not directly comparable. However, in the appendix, the authors say that the results in Section 4 hold for more general regularizers. Why not adopt the same regularizer in the main text or state a more general result in Section 4?

2. In Theorem 5.2, whether $AA^\top$ is singular has a significant influence on the rate. Could the authors give a more intuitive explanation of this phenomenon without resorting to the matrix

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
