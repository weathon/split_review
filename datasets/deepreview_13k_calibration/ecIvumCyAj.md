# Filtered not Mixed: Filtering-Based Online Gating for Mixture of Large Language Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 3, 6

## Abstract
We propose \textbf{\colorwblk{MoE-F}} -- a formalised mechanism for combining \bm{$N$} pre-trained expert Large Language Models (LLMs) in online time-series prediction tasks by adaptively forecasting the best weighting of LLM predictions at every time step. Our mechanism leverages the conditional information in each expert's running performance to forecast the best combination of LLMs for predicting the time series in its next step. Diverging from static (learned) Mixture of Experts (MoE) methods, MoE-F employs time-adaptive stochastic filtering techniques to combine experts. By framing the expert selection problem as a finite state-space, continuous-time \textit{Hidden Markov model} (HMM), we can leverage the \textit{\colorwblk{Wohman-Shiryaev}} filter. Our approach first constructs $N$ parallel filters corresponding to each of the $N$ individual LLMs. Each filter proposes its best combination of LLMs, given the information that they have access to. Subsequently, the $N$ filter outputs are aggregated to optimize a lower bound for the loss of the aggregated LLMs, which can be optimized in closed-form, thus generating our ensemble predictor. Our contributions here are: \textbf{(I)} the MoE-F algorithm -- deployable as a plug-and-play filtering harness, \textbf{(II)} theoretical optimality guarantees of the proposed filtering-based gating algorithm, and \textbf{(III)} empirical evaluation and ablative results using state of the art foundational and MoE LLMs on a real-world \textit{Financial Market Movement} task where MoE-F attains a remarkable \emph{17\%} absolute and {48.5\%} relative F1 measure improvement over the next best performing individual LLM expert.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents an online algorithm, called MoE-F, to adapt a mixture of pretrained large language models (LLMs) for time-series prediction tasks. A filter is used for each LLM, and the learning algorithm will learn those filters from data. The authors then provide an analysis about their method to reveal some nice properties of the solution. Finally, an extensive experiment has been done to evaluate their proposed method, using many big pretrained models, e.g., Llama-2, Llama-3, Mixtral, DBRX, ... Two types of problems are used in their evaluation, classification of financial market movement, and time-series forcasting. The results suggest that the new method can perform significantly better than the baselines for the first classification task. For time-series forcasting, their method also exhibits competitive performance.

### Strengths
**Originality:**
The proposed method seems novel and work well with time-series forcasting in an online fashion. 

**Quality:** 
The performance of their proposed method seems good, compatitive with the recent baselines. Their method is supported by some theoretical analysis.

**Clarity:**
The writing is readable with soem efforts for new readers.

**Significance:**
Please refer to other reviewers for this aspect, as I am not familiar with the topic of this paper.

### Weaknesses
The experimental results pose a concern about their way of evaluation or measurement. This concern comes from the strange behavior of F1 score in Table 2 and Table 3. In some columns (e.g., most columns in table 3), the value of F1 is smaller than both Precision and Recall. This is really strange. In my understanding, F1 is a hamonic mean of Precision and Recall, and hence it can not be less than both Precision and Recall.

### Questions
Can the authors explain about the concern before? Does it only a writing mistake?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a filtering algorithm to combine predictions from several experts in sequential decision making problems. At each time-step each of the experts provide their prediction and their reliability based on their local estimates. Then based on the historical losses of the expert the algorithm comes up with mixture weights to combine the experts at time t and the process continues. The paper provides optimality guarantees for their method under a hidden markov model process environment. Then they show two applications: (i) combining LLM experts for the task of market direction prediction based on evolving text market data (ii) combining time-series experts for forecasting. They show remarkable gains in both applications.

### Strengths
1. The problem is interesting. The dynamic filtering method is easily implementable. 

2. Both the applications are well selected and real world. The method shows a remarkable 17% gain over individual experts for the financial market direction task. This is pretty significant for a noisy problem.

### Weaknesses
 1. The writing can be improved in some sections, specifically the implications of theorem 1 and 2 need to be explained better.

2. In the TSF application it is unclear at what granularity of time-steps is the filtering applied. For instance if the horizon is 720, do the individual experts predict every 60 time-steps and then their 60 step look-ahead predictions are combined and then we move to the task of predicting the next 60 time-steps. Or do they predict one step at a time for 720 time-steps?

### Questions
Asked in the weakness section

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes to combine the predictions of multiple (large language) models in order to predict univariate time series. To optimise the weightings associated with each model based on past performances, the authors employ a continuous-time finite-state hidden Markov model (and an associated filtering algorithm).

### Strengths
**Novelty:** To my knowledge, this methodology is novel.

**Significance/contribution.** Making use of multiple (large language) models and using a filtering algorithm to decide in an online manner how to weight the predictions from each of these seems like a sensible idea.

### Weaknesses
 **Major comments:**

1.  **Clarity needs to be drastically improved.** I believe Sections 1, 2 and 3 need to be substantially rewritten to improve clarity. I do not believe that this manuscript is ready for publication in ICLR based on the presentation alone. For instance:

    - There seems to be no clear structure/order to the explanation of the model/methodology in Sections 1--3.
    - Key aspects of the methodology (including some notation) are explained in a figure caption (of Figure 2) and this figure is then not even referenced until the following page.
    - Important parts of the model, e.g., the processes $W$, $w$ or $x$ are used for several pages, before being defined in the middle of a generic-seeming paragraph titled "Probability Theory" at the end of Section 2.
    - Section 2, in particular, is a collection of disjointed paragraphs lacking a clear structure.
    - Sections 1 and 2 switch between continuous time and discrete time without explanation. Indeed, a time-discretisation is briefly mentioned in Section 3 but without sufficient detail.
    - Enumerating a bunch of "helper functions" (Equations 2--4) at the reader without much intuition or context makes for a difficult read.

    I think these sections should start with a high-level explanation of the (Wonham-Shiryaev) filtering algorithm and the model that this filtering algorithm is targetting. The specification of the model should be consolidated in one place.


2.  **Undefined/poorly defined notation.** Related to the previous point, there is quite a bit of undefined or poorly defined notation (or notation that is only defined much later after it has already been extensively used). For instance:

    - In the caption of Figure 2 (and also in Line 9 of Algorithm 1), what are "$\pi_n$" and "$\pi^n$"? Is this the same as "$\pi_t^{(n)}$"?
    - In Line 178, what does "$Q_t^{n:i,j}$" mean?
    - In Line 5 of Algorithm 1, what is "$\ell$"? Page 2 defines a loss function $\ell$ but this has two arguments rather than one.
    - In Line 15 of Algorithm 1, what does "$P^{(n)}$" mean?
    - In Line 305, what does "$P_{w_{t+1}|w_{t-H:t}}$" mean?

3.  **Soundness.** The presentational issues outlined above have made it impossible for me to verify that the proposed algorithm is valid in any meaningful sense. Hence I have to give a low score here.



**Minor comments:**

* Abstract: "remarkable" does not seem very objective.

* Figures should not appear in the text before they have been referenced. For instance, Figure 1 seems not to be referenced at all; Figure 2 is only referenced a page after it is displayed.

* The legends/annotations in some of the figures (e.g. Figure 1) are too small.

* Avoid "forward" referencing of equations, i.e. referencing equations before they appear in the text (see, e.g., Lines 81, 88, 191).

* Switching between bold and non-bold symbols for some of the mathematical quantities in Section 2 is confusing.

* The sentence "Each $n$th expert additionally provides their best ranking $\pi_t^{(n)}$ of the reliability of each expert’s performance thus far" in Lines 83--84 is very ambiguous (but seems central to understanding the proposed methodology).

* L284: The last sentence (starting with "Furthermore, ...") does not seem to contain a statement.


**Typos:**

* Abstract: Wohman-Shiryaev -> Wonham-Shiryaev

* L81: "predictions" -> "prediction"

* Eq. 2: Presumably, the time subscript $s$ (rather than $t$) is a typo?

* L163: The name "transition matrix" is confusing since this would normally be understood to mean $\mathcal{P}_N$. Presumably, "transition-rate matrix" or "intensity matrix" or "$Q$-matrix" is meant here.

* L165: Shouldn't this be "sum to 0" instead of "sum to 1"?

* L173: "Eq. equation"

* L220: missing space

### Questions
1. Regarding the loss functions discussed in Lines 129--134, can you explain how the classification scenario works? This would require $Y_t$ to be in $[0, 1]$. But I don't see how this can be guaranteed with the Brownian motion component in Equation 1.

2. Can you explain why we have "$w_t$" rather than "$w_s$" in Equation 1 and Line 101?

3. Why does the model need to be specified in continuous time (thus complicating the methodology). For the applications considered in this work, wouldn't a discrete time model, i.e. a simple discrete-time hidden Markov model, suffice?

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MoE-F, a novel mechanism for adaptively combining multiple pre-trained Large Language Models (LLMs) for online time-series prediction tasks. The key innovation is framing expert selection as a finite state-space continuous-time Hidden Markov model and leveraging stochastic filtering techniques to dynamically weight expert predictions.

### Strengths
The paper demonstrates significant originality in its approach to combining LLMs through the lens of stochastic filtering theory. This represents a creative fusion of classical control theory with modern machine learning. The theoretical foundations are rigorous, with formal optimality guarantees derived for both the parallel filtering and robust aggregation phases.

### Weaknesses
While the theoretical analysis is strong, there are some limitations in the experimental validation. The financial market experiments focus primarily on a single dataset (NIFTY), and broader validation across different types of time series problems would strengthen the claims of generality. The ablation studies, while informative, could be expanded to provide deeper insights into the relative importance of different components of the MoE-F architecture. Specifically, the impact of varying the transition probabilities in the hidden Markov model, and the sensitivity of the results to the choice of initial state distribution, are not thoroughly explored. Furthermore, the paper does not investigate the robustness of the method to noisy or missing data, which is a crucial aspect in real-world time-series applications. The experimental setup also lacks a clear comparison with established time-series forecasting benchmarks, making it difficult to assess the practical significance of the reported improvements.

### Questions
How does the performance of MoE-F degrade with increasing number of experts, and what are the computational scaling implications?

What is the impact of different market regimes (high volatility vs. low volatility) on the filtering performance?

### Soundness
3

### Presentation
2

### Contribution
3
