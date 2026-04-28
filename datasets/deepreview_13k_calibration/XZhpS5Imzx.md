# CAN TRANSFORMERS IN-CONTEXT LEARN BEHAVIOR OF A LINEAR DYNAMICAL SYSTEM?

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 6, 3

## Abstract
\lipsum[1]

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies the capability of transformer-based models to implicitly learn the closed-form update equations of the Kalman filter. The paper lists an algorithm for implementing the Kalman filter equations using operations that can readily be implemented through appropriate weights of a transformer architecture. The claims are empirically investigated by comparing mean squared prediction difference between transformer’s in-context learning and Kalman filter vs SGD, ridge regression, and ordinary-least-squares.

### Strengths
The investigation of how modern deep learning architectures can learn complex behaviour such as Kalman filtering as an _in-context_ task is highly significant to ICLR. Whereas Goel et al. showed that transformers can implement Kalman filters up to a (small, bounded) additive error, when trained for a specific dynamical system, the present work aims to demonstrate that transformers can learn not just a _specific_ Kalman filter, but more generally the Kalman filter equations such that it can in-context learn any dynamical system whose parameters are provided in the context.

### Weaknesses
The paper does not provide a derivation of its theoretical claims; the paper simply asserts that Algorithm 1 provides a transformer-appropriate implementation of the Kalman update equations. Contrast this to e.g. Akyürek et al. (ICLR 2023; one of the key citations in this paper) who include a detailed derivation of their results in the appendix.

Regarding empirical evaluation, this paper also falls significantly short of the level set by previous investigations into the in-context learning capabilities of transformers. It considers only a proxy metric on a test set that is generated from the same distribution as the training set. In contrast, Garg et al. (NeurIPS 2022; again a key citation in this paper) investigate the out-of-distribution generalization as well as how performance depends on model capacity and problem dimensionality. Both of those would be just as important in the present study: demonstrating that the learned transformer performs as well out-of-distribution would be much stronger evidence for actually having learnt the Kalman filter than solely comparing the difference in prediction to a Kalman filter on dynamical systems from within the training distribution.



### Questions
Can you motivate your choices of setup, architecture, training schedule etc. (beginning of section 4)? Why did you choose specifically your Strategies 1 and 2 for generating $F$? 

Maximum marginal noise is 0.025: how much noise is this relative to the scale of dynamics (low-noise, high-noise, …)?

What does it mean that MSPD peaks when context length approximately equals state dimensionality? Does this hold for multiple state dimensions? If so, a discussion would be useful (and a visualization of the state dimension as a vertical line in Fig. 1).

## Clarity questions

1. line 136: what are the model parameters you are referring to?
2. line 151: what is the convergence criterion? It seems from the equation you simply run a fixed number of $N$ steps.
3. line 202: what do you mean by _causal_ linear estimator?
4. line 205: what are $\hat{x}_0^+$ and $\hat{P}_0^+$ (not introduced)?
5. line 230: in eq. (20), why do you provide $Q$, but not $R$ (also in eq. (28))? Corollary, in line 417 you discuss omitting $R$ and $Q$ from context, which would be at odds with $R$ never being in the context in the first place.
6. line 235: in eq. (21), what is $T_\theta$? (also in eq. (30))
7. lines 311–317: are $Q$, $R$ newly sampled for each example (like $x_0$, $H$)?
8. line 320: what is $\phi$, can you clarify what you are doing here?
9. lines 352–354: from step 50000 onwards, $\alpha=1$, does this mean the transformer’s loss no longer decreases for the second half of training?
10. line 367: is the initialization for the Kalman filter comparable to the initialization you use in the transformer model?

Please carefully check your references. For example, “What learning algorithm is in-context learning? Investigations with linear models” by Akyürek et al. has been published at ICLR 2023 (as is clear from the arXiv entry!), similarly for other citations only listed as arXiv preprints.

## Minor nits
- Eq. (1): should be $\operatorname{Softmax}$ instead of $Softmax$
- Section 2.2: Please use `\mathbb{R}` ($\mathbb{R}$) for the space of real numbers instead of just $R$ (which is ambiguous with your notation for covariance of measurement noise)
- Below eq. (5), I’m assuming you mean that $q_t$ and $r_t$ are Gaussian-distributed noise; please be explicit about $q_t \sim \mathrm{N}(0, Q)$, $r_t \sim \mathrm{N}(0, R)$: white noise is not necessarily Gaussian, only describes independence over $t$
- line 184: would be helpful to explain what is the _RAW_ operator, at the very least spell out that it stands for Read–Arithmetic–Write as described in Akyürek et al. (2023)
- Below eq. (21), it’d be useful to explicitly state you use 0-based indexing (arguably default in programming, but in mathematical notation I would expect 1-based indexing by default if not stated otherwise!)
- line 413: “eingenvalues” should be “eigenvalues”

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the ability of a Transformer to learn a Kalman filter for estimation of a linear dynamical system using a tailored context. The paper details the construction of such a context and provides detailed experiments to validate state and output estimates of the transformer against several classical estimation techniques.

### Strengths
The paper studies a relevant and interesting connection between control/estimation theory and deep learning, which fits well in the contemporary research focus. The paper is overall well-written and the mathematical derivations are correct. It sufficiently extends existing literature on the transformer’s ability to represent various algorithms, e.g. SGD, via in-context learning.

### Weaknesses
However, the paper has several weaknesses that render the paper reading like a draft to an interesting and promising paper.

First, the paper only contains few references and does not accurately position itself in existing literature.  The paper lacks a sufficient discussion on recent works connecting the transformer architecture to linear state space models, see e.g. [1,2]. The paper also ignores work on learning the Kalman filter not related to transformers, see e.g. [3,4]. These works should at least be referenced as related work and ideally be discussed and compared against. Additionally, there are missing references for the GPT2 model [5] and the Adam optimization algorithm [6].

Second, the mathematical and experimental presentation is not sufficient. Regarding mathematical derivations, almost all details are not presented, which would significantly improve the paper and would allow the reader to more easily follow the arguments. For example, there should be more background on the RAW operator (11 -12), which can be given in the appendix to make the paper self-contained.  The index matrices I_{B1}, …, I_B{8}, I_F, etc. should be stated in the appendix. Currently, these matrices are assumed to be inferred by the reader, which severely hampers the readability. Additionally, the derivation of the contexts (20), (28) should be derived or the derivation at least be discussed in more detail. The same goes for Algorithm 1 (and Algorithm 2 in the appendix); there is no derivation or explanation to how these are obtained. The statement that eigenvalues on the unit circle are unstable is false according to standard definitions of stability. These eigenvalues are marginally stable, since the state does neither converge nor diverge in this case. Observability and Detectability of the linear system is not discussed at all. However, these two notions are important in this setting (F, H are randomly generated), since the ability to observe or detect the state from the specific F, H is important for the resulting performance of the Kalman filter and ultimately the transformer. Regarding this point, the presentation of the results is insufficient. Currently, only the relative performance (i.e. transformer compared to Kalman filter etc.) is stated, but the results would be much stronger if the actual ground truth (which is available) is reported, i.e., state the ground truth state/output and then the error of Kalman filter, transformer, and the other estimation algorithms w.r.t. the ground truth. Additionally, the plots (e.g. Figure 1) should not be clipped, but maybe split in two: one plot showing the full plot (e.g. on a logarithmic scale) highlighting the performance difference and a second plot showing the detailed differences between the better performing algorithms. Finally, the used codebase (Garg, 2022) should be hyperlinked and all the experimental details should be provided; currently this is insufficient.

Third, in my opinion the title is misleading. The title insinuates that the behavior, i.e., the dynamical representation of a linear system, is learned. However, the transformer actually learns to estimate the hidden state or output of a linear system. These two things are not equivalent. Additionally, the appendix is only used to give an extension of the method to dual Kalman filters instead of providing additional details of the main method.

Lastly, there are several typos in the equations and grammar mistakes (mainly prepositions), some of which are listed below. However, the authors should make an effort to carefully check the full paper beyond the following list.

- In (9) and (10), the inverse should be a pseudoinverse, since in general these inverses do not exist.
- In (4) the matrix F is time-varying, but later on all derivations are done for time-invariant F. Since it is assumed that F is time-invariant, why not state (4) for time-invariant F? Additionally, mention why Q, R are not time-varying here; in general they are time-varying.
- Line 259: \mathcal{A}_append should be \mathcal{A}_prepend
- Line 177: comprising of examples
- Line 201: assume a time-invariant; For simplicity of presentation (no “the”)
- Line 202: we consider scalar measurements at first.
- Lines 217-218: the computationally intensive matrix inversion in (15) simplifies to a simple scalar division
- Line 226: how closely a transformer can mimic

### Questions
-	Does the in-context learning also work for time-varying F? I assume the derivations would only differ slightly, so this is more of an experimental question. Also did you consider time-varying Q, R?
-	Regarding the performance gap between Strategies 1 and 2: Is the reason for this gap the stability of the system or is it the specific sampling of F? You could check this be removing alpha=1 in Strategy 1 (see below).
-	Related to the question above, why do you include alpha = 1 in Strategy 1? You could just vary alpha in [0,1).
-	Have you considered other learning rates for SGD? Your results suggest that by tuning the learning rate the performance of the SGD estimation could be close to Kalman filtering.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper demonstrates that ICL in a transformer can mimic a Kalman filter. Theoretical results show a hand-coded transformer can emulate the internal calculations of the KF algorithm. Experiments training a transformer to predict a linear-Gaussian SSM show its behavior is close to the optimal KF predictions.

### Strengths
This is an advance on the recent literature showing how transformers can implement incremental learning algorithms in their forward pass, extending this work to the KF.

The robustness to missing hyperparams is impressive and suggests the trained transformer is doing something more than the theoretical hand-coded one. This merits further investigation, especially since filtering with unknown hyperparams is still an active area of research.

### Weaknesses
The theoretical result is a relatively straightforward corollary of Akyürek et al. (2022), just needing to show the KF can be reduced to operations of the form in (11)-(12).

The paper shows the KF can be composed from certain elemental operations and that a transformer can implement those operations, but these two facts need to be put together. It’s nontrivial to arrange multiple operations within the layers of one network. In particular, the required number of layers seems to grow linearly with the sequence length, since the calculations must proceed serially from t=1 to t=N. This contrasts with the transformer in the experiments which learns long contexts using a fixed depth.

The theoretical analysis makes no reference to positional embeddings, but (unless I'm wrong) these are essential to implementing the elemental operations on page 5, and for implementing KF calculations sequentially as noted above.

### Questions
Are there implications for ICL in other domains, including LLMs?

(1): shapes don’t agree. The correct expression reverses the order of the two main terms and swaps $W^Q$ and $W^K$.

Line 243: $n+1$ should be $n$ (thrice)

p 5: The four operations could be written more succinctly mathematically, e.g. $G^{l}[K]=G^{l-1}[I]G^{l-1}[J]$.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper investigates whether transformer models can learn the behavior of linear dynamical systems via in context learning. Their observations suggest that the transformer emulates the behavior of the Kalman filter which is a statistically optimal estimate of the state, assuming that the system is linear.  The authors explore whether transformers can predict hidden states and observations within state-space models where the system parameters and observations are provided as context. Interestingly, the model maintains robustness even when some parameters, like state transition and noise covariance matrices, are missing.

### Strengths
1. The authors provide a fresh perspective of predicting state linear time invariant dynamical systems with transformers and in context learning.
2. The method is well presented
3. The empirical results verify the claim.

### Weaknesses
1. While the formulation seems sound, I think it lacks justification as how the context is being setup.  Specifically, can authors present other viable options and have a discussion around these?
2. I prefer there be a short section on Kalman Filters in the background section.
3. How does the method presented extend to non-linear systems?
4. What is the computation requirement?
5. Can authors discuss some viable real life use case?
6. Can there be an ablation study on context length, model size?

### Questions
Please see above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors investigate the capability of transformer models to learn and mimic state estimation in linear dynamical systems (LDS). Building on Akyürek et al. (2022), who explored in-context learning for linear models, the authors demonstrate that transformers can effectively approximate the Kalman filter—the standard closed-form solution for linear dynamical systems. Through empirical analysis, they show that transformers successfully mimic Kalman filter behavior, providing accurate predictions for both latent states $(x_{1}, \dots, x_{n})$ and future observations $(y_{n+1})$. The study further explores how in-context learning (ICL) can replicate more challenging algorithms, like the Dual-Kalman filter.

### Strengths
The paper presents an interesting approach by evaluating the capability of transformer models to mimic the inference process in linear dynamical systems, typically addressed by the Kalman filter. Through empirical analysis, the authors demonstrate how closely the transformer model’s estimation aligns with that of the Kalman filter. The equations presented are logical and are a natural extension of Akyürek et al. (2022) to the Kalman filter algorithm.

### Weaknesses
While the paper explores an extension of Akyürek et al. (2022) to linear dynamical systems, it lacks clarity in its motivation, and the overall presentation could be significantly improved. Also, the extension seems logical but limited as Akyürek et al. (2022) has all the parts that is required to implement the model for any linear model. I have merged the weakness and question sections below:

1.	The paper does not explicitly address positional embeddings, which are critical in transformer architectures. Could the authors clarify how positional embeddings were managed in the experiments?
2.	In Figure 1 (among others), why is the error unexpectedly low at a context length of zero? What is the intuition here?
3.	Extending this study to non-linear dynamical systems would add depth and novelty, as demonstrating in-context learning for non-linear cases could yield valuable insights.
4.	As non-linear dynamical systems are considered, comparing the in-context learning performance with algorithms like EKF, UKF, and Gaussian Variational Inference would be beneficial.
5.	Scalability with larger datasets, e.g., up to $10^6$ data points, is an important question. Could low-rank or sparse matrix representations (e.g., in Eq. (20)) help in handling large-scale data efficiently?
6.	In line 481, 'sufficiently long context' is mentioned without specifics. Could the authors provide guidance on the required context length for different datasets or an analysis of its impact?
7.	In Eq. (1), why is normalization omitted?
8.	The presentation of Algorithm 1 is convoluted. Consider using pseudocode instead of describing the operations in prose for better readability.

Some minor suggestions/typos:

1.	Extra bracket in Eq. (1).
2.	L131: $R$ is used to denote both covariance and the real numbers $R^n$. 
3.	In Eq (21), $T_\theta$ is undefined.
4.	L248: consider replacing $j$ with $J$ in Div.
5.	Enhance readability by using bold symbols for matrices, $\mathbb{R}$ for real numbers, etc.

### Questions
Kindly check the weakness section above.

### Soundness
2

### Presentation
2

### Contribution
2
