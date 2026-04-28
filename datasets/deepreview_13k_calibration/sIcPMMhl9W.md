# The Phase Transition Phenomenon of Shuffled Regression

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 5, 5, 5, 8

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
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper's primary focus is the analysis of phase transition thresholds within the context of recovering the permutation matrix in shuffled regression, as described by the model $Y = \Pi X B + \sigma W$. To achieve this, the paper employs techniques derived from message passing algorithms. The central goal in the paper is to establish phase transition thresholds by assessing the signal-to-noise ratio ($\text{snr}$) in two distinct scenarios. In the oracle case, the matrix $B$ is assumed to be known, while in the non-oracle case, $B$ is considered unknown. The derived thresholds serve as critical points where the error rates for permutation matrix recovery sharply drop to zero when the signal to noise ratio exceeds a certain threshold. Numerical results confirms the accuracy and reliability of the theoretically derived phase transition points in both the oracle and non-oracle cases.

### Strengths
The paper showcases notable strengths, particularly in terms of its technical contributions. It is the first work that leverages the framework of message passing algorithms to derive phase transition thresholds for shuffled regression. 
Furthermore, the section dedicated to related work is thoughtfully presented and offers a clear and comprehensive overview of the existing literature.

### Weaknesses
 - The paper's motivation could benefit from a more explicit and clear description. While the challenges of the problem are well-defined, a paragraph highlighting the practical applications of shuffled regression would greatly enhance the paper's appeal. Providing real-world scenarios where this problem arises would place it within a broader context of applicability and increase its relevance.

- Additionally, I would suggest reorganizing the notation-heavy equations, starting with equation (4) and its subsequent equations regarding message flows right until message passing update equation. Improved organization and perhaps some explanatory text would enhance the overall readability of the paper.

- The paper could benefit from a clearer explanation of the relationship between the permutation recovery problem and the linear assignment problem as defined in Equation (2). Providing more context on how the linear assignment problem is connected to the ML estimator for permutation recovery would be beneficial. The sudden introduction of the linear assignment problem might be confusing to readers initially. Additionally, it would be helpful to include a note regarding the operational significance of the matrix $E$ and why it plays a crucial role in this context.

- The derivation of the lower bound for $\log \mathbb{E}e^{-\theta\Xi}$ on page 6 is not clearly explained. Providing a more detailed and comprehensible explanation of how this lower bound is derived would greatly enhance the paper's clarity.

- Given the significance of the Gaussian approximation in obtaining closed-form expressions for $\text{snr}$, it would be valuable to provide an intuitive explanation of why this approximation is effective. 

-  The paper imposes a condition on the ratio of the singular values for matrix $B$ when computing $\text{snr}_{\text{non-oracle}}$. An explanation for the rationale behind this condition would be beneficial.

### Questions
- The paper could benefit from a clearer explanation of the relationship between the permutation recovery problem and the linear assignment problem as defined in Equation (2). Providing more context on how the linear assignment problem is connected to the ML estimator for permutation recovery would be beneficial. The sudden introduction of the linear assignment problem might be confusing to readers initially. Additionally, it would be helpful to include a note regarding the operational significance of the matrix $E$ and why it plays a crucial role in this context.

- The derivation of the lower bound for $\log \mathbb{E}e^{-\theta\Xi}$ on page 6 is not clearly explained. Providing a more detailed and comprehensible explanation of how this lower bound is derived would greatly enhance the paper's clarity.

- Given the significance of the Gaussian approximation in obtaining closed-form expressions for $\text{snr}$, it would be valuable to provide an intuitive explanation of why this approximation is effective. 

-  The paper imposes a condition on the ratio of the singular values for matrix $B$ when computing $\text{snr}_{\text{non-oracle}}$. An explanation for the rationale behind this condition would be beneficial.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into identifying the precise location of phase transition thresholds in permuted linear regressions. While prior work could ascertain this for the oracle case where the signal matrix $B^*$ is given, this study innovates by extending the analysis to non-oracle scenarios, employing techniques from quadratic assignment problems. Through mathematical formulations, the paper showcases a phase transition phenomenon that is consistent with the oracle case. Validation is presented using numerical experiments, demonstrating the model's ability to reconstruct permutation matrices in the noiseless context. The paper concludes by emphasizing its novel approach to pinpointing phase transition thresholds in the non-oracle realm, thus marking a significant advancement in understanding permuted linear regressions.

### Strengths
- **Originality:** Introduces a novel approach by tackling non-oracle scenarios in phase transition thresholds of permuted linear regressions, uniquely combining techniques from quadratic assignment problems.
  
- **Quality:** Demonstrates strong mathematical rigor, with theorems well-supported by numerical experiments, ensuring both theoretical and practical robustness.

- **Significance:** Offers deeper insights into phase transition thresholds in permuted linear regressions, bridging gaps between oracle and non-oracle scenarios, with potential for broader applications.

### Weaknesses
 - **Notation Issues:** The notation throughout the paper can be perplexing, especially for those not familiar with Mezard & Montanari (2009). Consistent and universally recognized notation would improve readability and understanding.

- **Specific Errors:** The representation in equation (3) on page 3 seems incorrect. A direct comparison to the original definition from Mezard & Montanari (2009) indicates a mistake. Specifically, the equation should be \(1 = \sum_j \Pi_{i,j}\) or \(1 \leq \sum_j \Pi_{i,j}\) instead of \(1 - \sum_j \Pi_{i,j}\). Such inaccuracies can mislead readers and detract from the paper's overall quality.

- **Assumed Prior Knowledge:** The paper heavily relies on readers having read Mezard & Montanari (2009). For wider appeal and comprehension, summarizing or introducing key concepts from the referenced work would be beneficial.

- **Constructive Feedback:** A deeper review of the paper's mathematical foundations, specifically in terms of its equations and their derivations, is necessary. This will ensure the elimination of such errors in future revisions.

### Questions
- In the methodology section, there seems to be a gap between the presented model and its practical application. Could you elaborate on how the proposed model can be applied to real-world scenarios?

 - How do the findings of this paper differ or expand upon the conclusions drawn in Mezard & Montanari (2009)? A comparative analysis would be useful for readers familiar with the referenced work.

 - Were there any limitations or constraints in the datasets or simulations used in the experiments? Understanding the scope and boundary conditions would be beneficial.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors characterize the phase transition threshold (in the signal-to-noise ratio, SNR) in the permuted linear regression problem. By leveraging the tool of message passing and connections to branching random walk process, closed-form formulas for the critical points, as well as the phase transition SNR are given, for both oracle (with known signal) and non-oracle (with unknown signal) settings.

Some numerical results are provided to support the proposed theoretical characterizations.

### Strengths
This paper focuses on the important problem of the statistical characterization of the phase transition behavior of the fundamental permuted linear regression problem.

There are many interesting (in fact shining!) ideas in the derivation of the phase transition SNR. And the numerical results seem to support the derived results.

### Weaknesses
The theoretical results in this paper are presented in a somewhat vague fashion.
If I understand correctly, some steps in the derivation are mathematically rigorous, while others are approximations and/or intuitions without strong theoretical evidence. 
It remains unclear, at least to me, which part of the results can be confidently called for future use, and which part cannot.

My major concern is that (it seems to me) the following approximations/heuristics are used to derive the phase transition threshold:
* approximation $\log( \mathbb{E}[e^{-\theta \Xi}] )$ by its lower bound;
* Gaussian approximation of the random variable $\Xi$.
It would be great if some further theoretical arguments and/or discussions can be provided to support these approximation. Otherwise, I do see why the derived phase transition is a reasonable approximate solution to the original problem, and the main results in this paper should be stated as "conjectures".

Some additional comments:
1. is Proposition 1 proven somewhere?
2. "We defer the technical details to Appendix": please refer to the specific section in the appendix.

### Questions
My major concern is that (it seems to me) the following approximations/heuristics are used to derive the phase transition threshold:
* approximation $\log( \mathbb{E}[e^{-\theta \Xi}] )$ by its lower bound;
* Gaussian approximation of the random variable $\Xi$.
It would be great if some further theoretical arguments and/or discussions can be provided to support these approximation. Otherwise, I do see why the derived phase transition is a reasonable approximate solution to the original problem, and the main results in this paper should be stated as "conjectures".

Some additional comments:
1. is Proposition 1 proven somewhere?
2. "We defer the technical details to Appendix": please refer to the specific section in the appendix.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the shuffled linear regression problem: linear measurements of a signal are perturbed via an additive noise and a permutation of the measured observables. The objective is then to recover the signal and the permutation (or only the permutation in the oracle version of the problem in which the signal is also observed). The manuscript relies on a previous study of the planted matching problem to propose expressions of phase transition points, as well as Gaussian approximations.

### Strengths
The shuffled linear regression problem is an interesting one, and it is a desirable objective to understand the phase transition it undergoes. In this respect the connection to the planted matching problem appears original and promising.

### Weaknesses
The clarity and pedagogy of the presentation of the paper seems rather insufficient to me. Section 2 is a review of the message-passing approach to the linear assignment problem, but the relation to the present problem is not motivated beforehand. Moreover the relation between the purely random and the planted version is not clear, and I don't think it is possible to understand the reasoning in Sec. 2.3 that leads to theorem 1, on which the rest of the results of the paper relies, without reading the original paper [Semerjian et al (2020)]. The Appendix A which seems to be aimed at clarifying this derivation remains quite obscure.

One of my main concerns is the use of theorem 1 in a setting where it does not apply: in [Semerjian et al (2020)] the weights on the edges of the graph are independent by construction, which allowed to write the recursive distributional equations (7). But here the weight matrix E=X B  has strong correlations in the edge weights, it is not clear why these should be neglected. The manuscript states on page 8 that in the "non-oracle case", "Unlike the oracle case, we notice the edge weights Eij are strongly correlated", but isn't it already the case that in the oracle case these are correlated ? The correlation structure in the oracle case, where $E = X B$, is not fully addressed, and the justification for neglecting these correlations is weak. Specifically, while the authors acknowledge correlations between $E_{\pi(i), \pi(i)}$ and $E_{\pi(j),\pi(j)}$ as well as $E_{i \pi(j)}$ and $E_{j \pi(i)}$, they do not provide a rigorous argument for why these correlations can be ignored in the message-passing analysis. The claim that these are only $O(n)$ out of $O(n^2)$ is insufficient, as the magnitude of these correlations is not considered, and their impact on the convergence of the message-passing algorithm could be significant.

There are also imprecisions in the use of the "phase transition" phrasing, since there is not a clear description of the qualitative differences between the two phases that the transition should separate, and since a study of the effect of the system size on the sharpness of the transition is not presented in the main part of the text.

- in the first line of equation (4) you express the m messages in terms of the hatted m messages, whereas the second line express the hatted m in terms of the hatted m, wouldn't it be more logical that the second line express the m hatted in terms of the m, or to suppress the first line since the second one is closed on one type of messages?

- in the upper panels of Fig. 2 the SNR axis extends to negative values, what is the meaning of the part of the curve at negative SNR?

- on page 6, "As a mitigation, we resort to approximating ... by its lower-bound", could you explain which inequality you use to derive this expression?

- on page 8 one can read that "this estimator can reach the statistical optimality in a broad range of parameters", could you give evidence for this statement? It is indeed quite surprising: from the beginning of the Section one understands that the "statistically optimal" estimator would involve solving a QAP, which is not doable efficiently, so how can one asserts that the LAP reaches statistical optimality if the latter is not known?

- on page 14, in the description of the numerical procedure, I'm not sure that it is the dichotomy search that should be expanded upon, but rather what corresponds to the line 5 and 6 of algorithm 1. What is meant by "run experiments", the resolution of the LAP? With an exact algorithm or via message passing? Could you also specify the definition of the error rate, is it the fraction of samples on which the inferred permutation fails to coincide with the planted one, or the average fraction of the permutation that is correctly inferred? This last question applies as well to the y axis on the lower panels of figure 2.

### Questions
- in the first line of equation (4) you express the m messages in terms of the hatted m messages, whereas the second line express the hatted m in terms of the hatted m, wouldn't it be more logical that the second line express the m hatted in terms of the m, or to suppress the first line since the second one is closed on one type of messages?

- in the upper panels of Fig. 2 the SNR axis extends to negative values, what is the meaning of the part of the curve at negative SNR?

- on page 6, "As a mitigation, we resort to approximating ... by its lower-bound", could you explain which inequality you use to derive this expression?

- on page 8 one can read that "this estimator can reach the statistical optimality in a broad range of parameters", could you give evidence for this statement? It is indeed quite surprising: from the beginning of the Section one understands that the "statistically optimal" estimator would involve solving a QAP, which is not doable efficiently, so how can one asserts that the LAP reaches statistical optimality if the latter is not known?

- on page 14, in the description of the numerical procedure, I'm not sure that it is the dichotomy search that should be expanded upon, but rather what corresponds to the line 5 and 6 of algorithm 1. What is meant by "run experiments", the resolution of the LAP? With an exact algorithm or via message passing? Could you also specify the definition of the error rate, is it the fraction of samples on which the inferred permutation fails to coincide with the planted one, or the average fraction of the permutation that is correctly inferred? This last question applies as well to the y axis on the lower panels of figure 2.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the phase transition phenomenon in the shuffled (permuted) regression problem: the error rate drops to zero rapidly once the parameters reach certain thresholds, which is empirically observed in previous works.

This paper aims to theoretically characterize and precisely identify the locations of phase transition thresholds using message passing techniques:
For the oracle case (regression coefficients known), the paper derives an analytical formula to predict the phase transition SNR;
For the non-oracle case (unknown coefficients), the paper proposes approximations to predict the maximum number of shuffled rows and its dependence on problem parameters.

Numerical experiments validate the theoretical predictions and show close alignment with the observed phase transitions.

Overall, the paper provides new theoretical understanding of phase transitions in shuffled regression

### Strengths
1. This paper is well written and the main stream easy to follow even though I am not quite familar with this area.

2. This paper gives the first theoretic result to identify the precise locations of phase transition thresholds associated with permuted linear regression, showing the precise positions of the phase transition points in the large-system limit.
The technical contribution seems to be significant.

1. Numerical experiments in this paper align well with theoretical predictions, even when problem sizes are not very large. This suggests the theory accurately captures the phase transition phenomenology.

### Weaknesses
1. The theoretic analysis in this paper uses a performing Gaussian approximation from statistical physics,
so the analysis here is not exactly rigorous.

2. The technical analysis and derivations in this paper are quite complex. This could make it difficult for a broad audience to digest the theory.
Although it is indeed a theory paper, a more gentle treatment on the mathematical details in the main text is still favorable.

### Questions
1. I would like the authors to discuss the connections to phase transitions studied in other problems, which could provide more insight on this phenomenon.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
