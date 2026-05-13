# The Phase Transition Phenomenon of Shuffled Regression

- Decision: Reject
- Scores: 3, 8, 6, 3

## Abstract
vspace{0.2in}
\noindent We study the phase transition
phenomenon inherent in the shuffled (permuted) regression problem, which has found numerous applications in databases, privacy, data analysis, etc. For the permuted regression task: $\bY = \bPi^{\natural}\bX\bB^{\natural}$, the goal is to recover the permutation matrix $\bPi^{\natural}$ as well as the coefficient matrix $\bB^{\natural}$. It has been empirically observed in prior studies that when recovering $\bPi^{\natural}$, there exists a phase transition phenomenon: the error rate drops to zero rapidly once the parameters reach certain thresholds. In this study, we aim to precisely identify the locations of the phase transition points by leveraging techniques from {\em message passing} (MP).

\vspace{0.15in}

\noindent In our analysis, we first transform the permutation recovery problem into a probabilistic graphical model. We then leverage the analytical tools rooted in the message passing (MP) algorithm and derive an equation to track the convergence of the MP algorithm. By linking this equation to the branching random walk process, we are able to characterize the impact of the \emph{signal-to-noise-ratio} ($\snr$) on the permutation recovery.  Depending on whether the signal is given or not, we separately investigate the oracle case and the non-oracle case. The bottleneck in identifying the phase transition regimes lies in deriving closed-form formulas for the corresponding critical points, but only in rare scenarios can one obtain such precise expressions. To tackle this technical challenge, this study proposes the Gaussian approximation method, which  allows us to obtain the closed-form formulas in almost all scenarios.
In the oracle case, our method can fairly accurately predict the phase transition $\snr$. In the non-oracle case, our  algorithm can predict the maximum allowed number of permuted rows and uncover its dependency on the sample number.

\vspace{0.15in}

\noindent Our numerical experiments reveal that the observed phase transition  points are well aligned with our theoretical predictions. It is anticipated that our study will motivate exploiting MP algorithms (and the related techniques) as an effective tool for solving the  permuted regression problems, which have found many applications in machine learning, privacy, databases, etc.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper studies the shuffled multi-observation linear regression in two regimes: when the signal matrix is known and when it is unknown. The authors investigate the SNR at the phase transition.

### Strengths
The paper studies the general version of the problem that was studied in several prior works. The authors claim that they solve an open problem from a prior work [Lufkin et al., 2024]. While I'm not sure about this statement (see below), I think their result might be anyway helpful to investigate the regime that [Lufkin et al., 2024] were interested in.

### Weaknesses
Your assumption 1 seems to be unrealistic. You justify it by some numerical experiments, but it is not the usual way how assumptions in learning theory work. You have to assume some nice properties of B (or other paramerers of the problem), and then rigorously derive some result. Currently it is unclear to me whether there is any non-trivial matrix B that satisfies this assumption. Is it the case that you used this assumption in your formal proofs? Also, is it correct that your result formally answers the question from [Lufkin et al., 2024] only under this assumption?

In addition, your proofs seem to contain only equalities (or approximate equalities up to $o(1)$ terms). While this complaint might sound weird, it indicates that the approach may not be very sophisticated. You basically just do equivalent transformations of formulas. While potentially sometimes it might be non-trivial, practically almost always it is not the case. So far it seems to me that your assumption 1 is needed exactly for these equivalent transformations to work, and with any mathematically correct assumption the analysis has to become significantly more challenging.

Given these two observations, I recommend rejecting the paper.

### Questions
(see Weaknesses above)

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
The paper studies the phase transition phenomenon in the shuffled regression problem. The authors transform the permutation recovery problem into a probabilistic graphical model and use message passing (MP) algorithms to derive equations tracking convergence. To address the challenge of deriving closed-form formulas for critical points, they propose a Gaussian approximation method, which provides accurate predictions of phase transition thresholds in multiple scenarios. Experiments are provided and suggest that the proposed algorithm is able to recover the structure.

### Strengths
- The problem being studied seems novel. I'm more familiar with phase transitions in the context of network models, and in the context of permuted LR the problem seems new.
- The authors propose a new method which leverages the MP algorithms by relating the combinatorial structure in the shuffled regression problem to a graphical model. This seems novel. 
- Detailed proofs for the phase transition points are included. Specifically the Gaussian approximation analysis can be interesting when tackling more general scenarios.
- Synthetic experiments are provided, and the phase transition points from the results match the prediction from the theorem.

### Weaknesses
I am not familiar with this line of literature and I wouldn't be the best to provide an assessment. That being said, I think the organization of the paper can be improved. While I understand the paper is highly theoretical and statistical, it would be easier for readers to follow if the authors can provide more high level motivations or concrete examples. Specifically, the connection between the practical shuffled regression problem and the graphical model formulation could be made more explicit. The current presentation jumps into the mathematical formulation without sufficient motivation for why a probabilistic graphical model is the right approach. Furthermore, the paper could benefit from a more intuitive explanation of the message-passing algorithm's role in solving the permutation recovery problem. The current description is quite dense, and a high-level overview of how the messages relate to the underlying permutation would be helpful. The Gaussian approximation method, while mathematically sound, also lacks a clear, intuitive explanation of why it works and what assumptions are being made about the underlying data distribution to justify this approximation.

### Questions
- Can the authors provide some motivation behind eq. (3)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the shuffled regression problem, in which unknown permutation matrix is multiplied to a linear model, with a focus on predicting phase transition. The authors leverage the message passing algorithm to find phase transition point in the limit of some parameters. In the analysis of phase transition, they categorize oracle and non-oracle cases, where the signal matrix is known and unknown respectively.

### Strengths
The derivation of the phase transition point using message passing and LAP is clearly presented and technically sound. This work distinguishes the difference from the recent papers having similar problem and settings, which in fact shows technical contribution over the  recent papers.

### Weaknesses
Some motivations and intuition in the derivation part are missing. For instance, eq(3), eq (10) and assumption 1 are given without motivation. Specifically, the probabilistic interpretation of the permutation matrix in eq(3) is not well-motivated, and it's unclear why this specific distribution is chosen. The use of a Gaussian approximation in eq(10) lacks justification, particularly regarding the conditions under which this approximation is valid and the potential impact on the accuracy of the phase transition prediction. Furthermore, the assumption of weak correlations in Assumption 1, while common in message passing analysis, requires more discussion in the context of this specific problem, including why it is expected to hold and what the consequences might be if it does not. Analysis of the approximation error (such as Gaussian approximation in eq (10) or the use of the lower bound for $\theta^*$) is not provided. As oracle case is rare in practice, I think comparison of non-oracle case with oracle case is needed at least in empirically, but it is missing in the paper.

### Questions
1) Is eq (3) necessary for the problem of shuffled regression? How much does prediction error arise if the prior distribution on the permutation matrix is not following eq(3)?
2) As I wrote in the weaknesses part, what are the motivation or reasoning behind using eq(3), eq(10), and assumption 1?
3) With the similar setting of Table 2, what are the predicted phase transition points by the algorithm for non-oracle case? Are they similar with the prediction of oracle case? 
4) How to read the upper panel in figure 2? Is the fluctuated point of $\tau_h$ the phase transition point w.r.t. $\tau_h$? If yes, why it is?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies high-dimensional shuffled linear regression, which is the following problem.
We are given a design matrix $X$ and a set of observations $Y$, drawn according to the following model:

$Y = Pi \cdot X \cdot B + \sigma W$

Here, $B$ is a "signal" matrix and $Pi$ is an unknown permutation matrix.
$\sigma > 0$ is a parameter and $W$ is a noise matrix with iid Gaussian entries.
In some variants of the problem, we may also be given $B$.
The goal is to recover $Pi$, and, if it is not given to us, $B$.

The paper offers a method to predict the signal-to-noise ratio above which a certain "message passing" algorithm, derived from statistical physics, can recover $Pi$ or $Pi,B$.
(The message passing algorithm is also derived in the paper.)
From what I can tell, the method is heuristic, making "physics-style" approximations along the way.
The authors corroborate their findings with some numerical experiments to show that the predictions they make are not too far numerically from the observed signal-to-noise threshold at which message passing stops working.

The problem of shuffled linear regression is a natural one, and well within the scope of ICLR.
However, I do not feel that the paper clears the bar for acceptance.

The main (major) issue is that the presentation of results is not at all clear.
The results are scattered throughout the 10 page, there is inadequate context for all of them.
For instance, I think proposition 1 is supposed to be one of the main results.
But I cannot tell how to interpret it as a mathematical proposition -- is it meant to be a rigorously-proven equation?

There are lots of heuristic physics-style "derivations" of phase transitions for message passing algorithms for high-dimensional learning problems now in the literature.
What is novel about this derivation?
If it is just a matter of turning the crank on existing technology, then even with clarified presentation I think it should go to a more specialized conference.
If there is something really novel about the way the derivation works here that I am missing, then perhaps it could be of interest to a broad ICLR audience.

### Strengths
see above

### Weaknesses
The paper studies high-dimensional shuffled linear regression, a natural problem for ICLR, but the presentation and novelty are not sufficiently clear for acceptance. The core issue is the lack of clarity in presenting results. The results are scattered throughout the 10 pages, and there's insufficient context. For example, Proposition 1, which seems central, lacks clear interpretation. Is it a rigorously proven equation, or an approximation? The paper uses a message-passing (MP) algorithm derived from statistical physics to predict the signal-to-noise ratio (SNR) threshold for recovering the permutation matrix $Pi$ and/or the signal matrix $B$. However, the derivation of this threshold relies on heuristic, physics-style approximations. It's unclear what is novel about this derivation, given the existing literature on phase transitions for MP algorithms in high-dimensional learning. If it's a standard application of existing techniques, the paper might be better suited for a more specialized conference. The lack of clear mathematical statements and the heuristic nature of the derivations make it difficult to assess the true contribution of this work. The numerical experiments, while corroborating the predictions, do not fully compensate for the lack of clarity in the theoretical results. The paper needs to clearly articulate the assumptions under which the results hold, and provide more precise mathematical statements.

### Questions
see above

### Soundness
2

### Presentation
2

### Contribution
2
