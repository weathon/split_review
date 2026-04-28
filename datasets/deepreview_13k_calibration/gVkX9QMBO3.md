# Efficient Biological Data Acquisition through Inference Set Design

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
In drug discovery, highly automated high-throughput laboratories are used to screen a large number of compounds in search of effective drugs. These experiments are expensive, so one might hope to reduce their cost by experimenting on a subset of the compounds, and predicting the outcomes of the remaining experiments. In this work, we model this scenario as a sequential subset selection problem: we aim to select the smallest set of candidates in order to achieve some desired level of accuracy for the system as a whole. Our key observation is that, if there is heterogeneity in the difficulty of the prediction problem across the input space, selectively obtaining the labels for the hardest examples in the acquisition pool will leave only the relatively easy examples to remain in the inference set, leading to better overall system performance. We call this mechanism \textit{inference set design}, and propose the use of an confidence-based active learning solution to prune out these challenging examples. Our algorithm includes an explicit stopping criterion that stops running the experiments when it is sufficiently confident that the system has reached the target performance. Our empirical studies on image and molecular datasets, as well as a real-world large-scale biological assay, show that active learning for inference set design leads to significant reduction in experimental cost while retaining high system performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper describes the application of active learning for Inference Set Design, a problem where the goal is to label a predefined finite set of instances. To this end, a hybrid screen is proposed where experiment carried out on a subset of the instances (the observation set) and the label on the rest of instances (inference set) is approximated by the prediction of a model trained on the observation set. The paper shows that in this setup the inference set design aspects dominate the better model generalization aspects of active learning.

### Strengths
The described problem is very close to industrial application, and as such quite relevant.  The paper is clearly written and quite easy to follow. The experiments are quite detailed.

### Weaknesses
The machine learning novelty is limited, it describes classical active learning evaluated with a non traditional performance metric. (This metric is however quite well motivated). The argument by the authors, that the benefit of active learning should be interpreted more broadly if the goal is to label the dataset is valid. Using similar argument, however, most of the time the final goal is to maximize (target) or minimize (off-target, tox.) the outcome of the experiment (at least find multiple diverse extrema), the problem become a Bayesian optimization problem, with already existing literature and efficient methods. In the light of this, can you point out a few practical scenarios where ISD is still relevant?

The paper describes the goal as getting the labels cheaper, so if all measurement would be available Accuracy would be 100%. This assumption of no measurement error (zero aleatoric uncertainty) is not reasonable in practical biological assays. At first glance reformulating the problem with measurement noise is not trivial. For example, sometimes it may be beneficial to spend the budget on a repeat if the model flags it as “suspicious” (model based on other data consistently predict different value than the measured one)

**On page limit**
The manuscript is over the page limit though not by much, as on page 5 a page break is left in. Please fix this.
also 392-393 line break should be removed

Minor:

Line 402 “We have shown that inference set design that inference set design”

L568-569 “With inference set design, the active agent is again able to outperform thebaselines (see Figure 10). ” <- this should be Figure 9 right?

Define $KL(\hat{\mu}_t, a)$ in eq 5

### Questions
1) Can you point out a few practical scenarios where ISD is relevant while Bayesian Optimisation not? (see Weaknesses)
2) How can the method handle measurement error?
3) Were you able to see any meaningful pattern in the hard to predict examples in the public dataset chemical problems? (HOMO-LUMO gap and energy prediction)
4) Pleas fix page limit, and the minor issues.

### Soundness
4

### Presentation
4

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
The paper presents an active learning method for hybrid screening, for the setting where there is a finite library and the goal is performance on this library (and not generalization). The idea is to use an active learning approach to include the difficult examples in the training set and stop when the performance is beyond some threshold. The paper discusses two reasonable acquisition functions for this purpose. In each round, a batch of difficult observations are labelled, and the performance on this batch is used to lower bound the performance on the remaining data in the inference set. The method is demonstrated on several relevant benchmark data sets.

### Strengths
The paper is generally well written and easy to follow.

The main idea is clear, useful and effective.

Good experiments to demonstrate the benefits of the approach.

### Weaknesses
The technical novelty is limited, as it is mostly an application of existing methods.

The paper would benefit from including comparisons with other heuristics that capture the "difficulty" of observations. For molecules, one could think of many ways to heuristically score their complexity, and use this to train on most complex examples first. I think this would be of practical interest to know how much the proposed method can improve over such baselines.

The paper appears to have formatting issues, with a mostly blank page and a full page of text exceeding the page limit.

What are key differences to existing uncertainty based active learning methods? It appears to me, that the main difference is that the evaluation criterion is performance on the library and not generalization.

In what practical sense does the stopping criterion provide theoretical guarantees? The paper argues that there is a lower bound on target accuracy, assuming the model is weakly calibrated (i.e., the order of uncertainty is correct). However, how reliably does this assumption hold in practice?

For the committee approach, why do you focus on the voting entropy, rather than e.g. entropy of the mean predictive distribution?

I did not find a description in the main text of the ML models used in the experiments.

If I understand correctly, on Molecules3D you include a comparison with data ordered by molecule size, smallest first. Does this not go against the idea of training on difficult examples first? Would it not be more interesting to compare with data ordered by decreasing molecule size? 

Notation:

In eq. 3 Nb is not defined, and the notation is not clear. The left hand side has no index i inside the brackets, and the right hand side evaluates to a single value, not a set. Same goes for eq. 4.

Minor comments:

This sentence is unclear to me: "Because of this, we can treat performance on X_inf^t as though they were IID samples from X_inf^t, and construct a (conservative) lower bound on the accuracy on X_inf."

I am not sure why the method is called "inference set design" - it does not explicitly design the inference set, but is rather a fairly standard active learning scheme with a particular focus on optimizing system performance by including difficult examples in the observation set.

### Questions
What are key differences to existing uncertainty based active learning methods? It appears to me, that the main difference is that the evaluation criterion is performance on the library and not generalization.

In what practical sense does the stopping criterion provide theoretical guarantees? The paper argues that there is a lower bound on target accuracy, assuming the model is weakly calibrated (i.e., the order of uncertainty is correct). However, how reliably does this assumption hold in practice?

For the committee approach, why do you focus on the voting entropy, rather than e.g. entropy of the mean predictive distribution?

I did not find a description in the main text of the ML models used in the experiments.

If I understand correctly, on Molecules3D you include a comparison with data ordered by molecule size, smallest first. Does this not go against the idea of training on difficult examples first? Would it not be more interesting to compare with data ordered by decreasing molecule size? 

Notation:

In eq. 3 Nb is not defined, and the notation is not clear. The left hand side has no index i inside the brackets, and the right hand side evaluates to a single value, not a set. Same goes for eq. 4.

Minor comments:

This sentence is unclear to me: "Because of this, we can treat performance on X_inf^t as though they were IID samples from X_inf^t, and construct a (conservative) lower bound on the accuracy on X_inf.

I am not sure why the method is called "inference set design" - it does not explicitly design the inference set, but is rather a fairly standard active learning scheme with a particular focus on optimizing system performance by including difficult examples in the observation set.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles the challenge of reducing experimental costs in high-throughput biological screening, with a focus on real-world applications such as drug discovery and cell microscopy. To achieve this, the authors formulate it as a sequential subset selection problem, which seeks to identify the smallest possible subset of compounds for experimental testing, whose outcomes can ensure a desired level of accuracy for the entire system. In other words, the authors propose a mechanism that aims to actively identify and experimentally test the most challenging compounds, leaving the relatively easier-to-predict compounds for the inference set. To strategically label only the most challenging compound samples, the authors propose to employ an uncertainty-based active learning approach that selects samples for which the model shows the lowest predicted probabilities or where ensemble models exhibit the highest disagreement.

### Strengths
The strength of this paper is derived from addressing an interesting real-world challenge in biological screening, where experimental costs are one of the most significant bottleneck. The proposed inference set design method shows somewhat promising potential for these applications by enabling a strategically targeted selection of samples based on model uncertainty. Another strength is the use of diverse real-world datasets, ranging from molecular property prediction (QM9 and Molecules3D) to cell microscopy experiments (RXRX3 dataset with 17,063 CRISPR knockouts and 1,674 FDA-approved compounds).

### Weaknesses
The most significant weaknesses of this paper are both technical and presentational. First, this paper does not meet basic ICLR submission guidelines, as its length exceeds the 10-page limit, and this paper contains formatting issues, including a large blank space on page 5 and broken text formatting on lines 392-393 of page 8, which diminishes its professional presentation. Secondly, the experimental comparison is severely limited, with only a random agent used as a baseline method. Given the paper's relevance to active learning and sample selection, the absence of comparisons with reinforcement learning (RL) approaches or other active learning methods is a significant shortfall. Specifically, an RL agent with proper reward modeling could potentially offer competitive performance in sample subset selection. Furthermore, the lack of comparison to methods like Bayesian Active Learning by Disagreement (BALD) is a major oversight, as BALD [1] is explicitly designed to select samples that reduce uncertainty across the dataset, a goal directly relevant to this work. Lastly, the theoretical explanation of Lemma 1 lacks clarity. The notation $i \in\in\mathcal{X}^{t}_{\text{inf}}$ in the proof is unclear, and the claim that the inequality follows from weak calibration and least confidence selection is not rigorously justified, with logical gaps in the argument.

### Questions
1. What is $N_{\text{target}}$ on page 2? The notation appears without explanation, leaving its meaning unclear.
2. In Lemma 1, the inequality $P[\hat{Y} = Y \mid \hat{p} = p_1] > P[\hat{Y} = Y \mid \hat{p} = p_1]$ is used, but since both sides are identical, the inequality does not make logical sense.
3. In the proof of Lemma 1, the notation $i \in\in\mathcal{X}^{t}_{\text{inf}}$ is unclear. Additionally, the step claiming “the inequality follows from weak calibration and least confidence’s selection” does not seem justified, as it appears to have logical gaps and doesn't rigorously establish the claimed inequality. The overall proof structure needs a more detailed explanation to establish the claimed result.
4. On page 4, lines 212 to 213, this assertion seems to be logically circular, and the abbreviation 'IID' is used without definition. Although 'IID' is a common term, it should be defined in full upon its first appearance in the paper.
5. On page 6, the authors distinguish their approach from Bayesian methods but only compare it with a random agent. However, established Bayesian methods like Bayesian Active Learning by Disagreement (BALD) [1] can effectively select samples that are expected to reduce uncertainty across the dataset. The authors should explain why Bayesian active learning methods cannot be applied in this context and clarify their decision not to compare their approach with BALD or other active learning or reinforcement learning methods.
6. If the method's effectiveness is constrained by a 'low data regime and complex task' (as indicated by the RxRx3 dataset results), how can it be practically useful for real-world biological applications that commonly encounter these challenges?




[1] Houlsby, Neil, et al. "Bayesian active learning for classification and preference learning." arXiv preprint arXiv:1112.5745 (2011).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces and tries to tackle the problem of identifying a small subset of data on which to run costly measurements to train a machine learning model which infers the most probable measurements for the remainder of the data, with the theoretical guarantee that the model makes less of $\gamma$ percent of errors at inference time. The paper introduces a stopping criterion that would satisfy the correctness guarantee and applies their corresponding algorithm on several benchmark and real-life data sets.

### Strengths
- Originality: The submission tackles an interesting problem, where the goal is not to maximize model generalization but to ensure model correctness on a specific subset of data. This is a first step towards better theoretically-backed approaches in biology (compared for instance to what was done in the LINCS L1000 data set [1] for the regression of gene expression, where they only selected a fixed subset of genes to measure based on prior knowledge instead of difficulty in predicting gene expression).
       
- Quality: The experimental results look good, with appropriate baselines (random selection of new samples to measure, or adding a next batch to measure given the original order of samples). There is a good effort in applying the method to benchmark and real-life, biological data.
       
[1] Subramanian, Aravind, et al. "A next generation connectivity map: L1000 platform and the first 1,000,000 profiles." Cell 171.6 (2017): 1437-1452.

### Weaknesses
 - Clarity: **(Major concern)** The full paper is not very well-written:

(1) The definition of $b$ (or $N_b$ in the pseudocode in appendix) is unclear and never defined. In Equation (5), it seems that $b=|X^t_\text{obs}|$ that is, the total number of points measured up at time $t$.

In Lemma 1, $b=|X^t_b|$, which is the total number of new points added to the observed set $X^{t-1}_{obs}$ at time $t$.

$N_b=|X^t_b|$ in the pseudocode in appendix.

In the proof of Lemma 1 in appendix, $b=|X^t_{inf}|$, that is, the number of points that are left to infer at time $t$ (there is no reason to assume that $b=|X^t_{inf}|=|X^t_b|$...). 

Moreover, it should be mentioned earlier than the appendix or the experimental section that a **constant** number of samples is added to the measured point set. 

(2) Perhaps a good thing would be to define all variables ($X^t_\text{obs}$, $X^t_b$, etc.) in a single paragraph just after the introduction. Please don’t remove the time-dependent indices ($X_\text{obs}$, $\hat{f}$…) and the hats ($f$ instead of $\hat{f}$ in the proof of Lemma 1), as it makes everything very confusing.

(3) Why mention the query-by-committee sampling, as there is no theoretical guarantee associated with it?

(4) It seems that $\hat{f}$ has a range in $[0,1]$ (or $\mathbb{N}$) whereas $\hat{p}$ has a range in $[0,1]$. Then writing $\hat{p}=\hat{f}(X)$ in the proof of Lemma 1 is extremely confusing.

(5) **(Minor suggestion)** I would put the related works section earlier in the manuscript, for instance, when the differences between active learning and inference set design is discussed, as I think it would make more sense.

(6) **(Minor suggestion)** A one-liner of the full structure of the Algorithm should be present at the end of the section 2 with a link to the pseudo-code in the appendix, so that the algorithmic contribution is clearly mentioned.
       
- Quality/Significance: **(Major concern)** As it is, the proof of Lemma 1 is wrong. What is $\hat{Y}$ ? the difference with $Y$? Is one the prediction made by the model $\hat{f}$ and the other the true measured label (and then $\hat{Y}= \hat{f}(X)$)? However, $y$ seems to be the probability given by the model in Equations (3) and (4). The proof displays the opposite sign of what is stated in Lemma 1 in the main text. Please rewrite properly the proof, including the use of Bayes’ theorem (?) in the second equality, the problem of the definition of the variables $b$, $\hat{f}$, $\hat{Y}$, $\hat{p}$, why “$P(\hat{p}=\hat{f}(X))$”=1 (assuming that here $\hat{f}(X)$ is the probability returned by the model: is it related to the model being accurate on every measured point?), and how the induction works (at least) from T-1 to T-2.

The result shown in Lemma 1 is not empirically tested (that is, at the stopping point of the Algorithm, with a prespecified probability $1-\delta$, the error is less than $\gamma$). The code producing the experiments is not shared, as such, the research is not reproducible.
       
- Significance: **(Minor concern)** The choice of accuracy measure is perhaps not very appropriate for the data: for instance, we expect more drugs to be labeled negatively (for instance, in drug discovery) than positively. Area Under the Curve is said to be slightly more appropriate on imbalanced data [2].

The proof of Lemma 1 being incorrect/badly-written is why I rated soundness to 1. The definitions of notation not being clear to the point of impairing the understanding of the paper is why I rated presentation to 1. The interesting question (mitigated by the perhaps incorrect Lemma 1) is why I rated contribution to 2. The main reason why I rated the paper 1 is because of the proof of Lemma 1.

### Questions
Typos:
- Is “weakly calibrated” (page 2) the same as “approximately calibrated” (Lemma 1)?
-  In Lemma 1, $P[\hat{Y} = Y \mid \hat{p} = p_1 ] > P [\hat{Y} = Y \mid \hat{p} = \underline{p_2} ]$ for $p_1 > p_2$
- In Equation (5), please mention that KL is the Kullback-Leibler divergence… also mention the name of the result (Corollary 10.4) instead of the page.

Questions:
- What does “treat performance on $X^t_\text{inf}$ as though they were IID samples from $X^t_\text{inf}$” (Line 213) mean? Independence of the probabilities given by the model across data samples from $X^t_\text{inf}$?
- **(Score-changing question)** Please provide a proof for Lemma 1 that solves my concerns listed above.
- **(Score-changing question)** Is there a closed-form expression or at least an upper bound on the stopping time $\tau$ in Equation (6) (as the whole selection process is deterministic as long as the prediction model is deterministic)? If so, is the subsequent budget of measurements (that is, $|X^t_\text{obs}|$ where t is the final selection step of the algorithm) realistic with respect to the total number of items (for instance, we might want a number of measured elements sublinear in N for a reasonable value of $\gamma$, where N is the total number of items in the data set)?
- **(Minor question)** At each time t, the model $\hat{f}^t$ (or $\hat{f}^t_1, … \hat{f}^t_{Nmodels}$ for the query-by-committee) has to be retrained on the full $X^t_{obs}$ and evaluated on $X^t_{inf}$, and then take the arg max on $X^t_{inf}$ (least confidence sampling and query-by-committee). How expensive is it in practice? The budget of measurements ($|X^t_{obs}|$) is important but perhaps we would like also to minimize the number of selection rounds (that is, $t$) as training/evaluating/sampling might also be expensive. Minimizing $t$ might however be contradictory with the objective of minimizing $|X^t_{obs}|$ though, as if we measure a slight over-approximation of the minimal $X^t_{obs}$ in a single selection step, we optimize for the former objective but not the latter.
- **(Minor suggestion)** Why not a more adaptive approach where all points such that the maximal proba across class labels is no higher than 0.5 (and then the acquisition batch size is no longer a constant)? 
- **(Score-changing questions)** (1) There is a shadowed orange part on the plots in Figure 1, are the curves the average across all considered points (System performance: all points in MNIST training set = $|X_\text{target}|$, inference set $|X_\text{target}|-|X^t_\text{obs}|$ -that changes across the x-axis- acquired batch $1,000$, and test set = 50% of full data set) or the average across random seeds (=3 according to the appendix)?

(2) What the “saving” mentioned in Figure 1? The difference between the number of actually measured points and measuring all samples at a given point in time?

(3) What’s the threshold $\gamma$ used in the experiments for the stopping criterion? Can you check that the theoretical guarantee of Lemma 1 is empirically satisfied (by applying some calibration procedure on the trained model, if needed)?

I understand that not all score-changing questions can be answered, especially in the short time for rebuttal. I would be willing to increase the score whenever one of these can be answered (the most important being Lemma 1 and the ones related to the plots) / if the major concerns listed above are addressed.

Summary of the suggested modifications:
- Provide a clear and consistent definition of $b$ (or $N_b$) early in the paper, ideally in a dedicated notation section.
- Ensure that this definition is used consistently throughout the paper, including in equations, lemmas, proofs, and pseudocode.
- Explicitly state earlier in the paper that a constant number of samples is added to the measured point set in each iteration.
- Clearly define all variables used in the proof of Lemma 1, including $\hat{Y}$, $Y$, $\hat{f}$, and $\hat{p}$, and explain their relationships.
- Revise the proof to ensure consistency with the statement in Lemma 1, particularly regarding the inequality sign.
- Provide a step-by-step explanation of the proof, including justifications for each step (e.g., the use of Bayes' theorem).
- Clarify the induction process, especially the step from T-1 to T-2.
- Explain or justify any assumptions made in the proof of Lemma 1, such as "$P(\hat{p}=\hat{f}(X))$"=1.
- Include empirical tests of Lemma 1 in the experiments, specifically verifying that the error is indeed less than $\gamma$ with probability $1-\delta$ at the stopping point.
- Provide access to the code used for the experiments, either through a public repository or as supplementary material.
- Include more details about the experimental plots.

------------------------
**UPDATE**: I raised my score to 8 after reading the updated manuscript and exchanging with the authors.

### Soundness
1

### Presentation
1

### Contribution
2
