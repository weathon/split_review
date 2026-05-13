# Stabilized Neural Prediction of Potential Outcomes in Continuous Time

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Patient trajectories from electronic health records are widely used to predict potential outcomes of treatments over time, which then allows to personalize care. Yet, existing neural methods for this purpose have a key limitation: while some adjust for time-varying confounding, these methods assume that the time series are recorded in \emph{discrete time}. In other words, they are constrained to settings where measurements and treatments are conducted at fixed time steps, even though this is unrealistic in medical practice. In this work, we aim to predict potential outcomes in \emph{continuous time}. The latter is of direct practical relevance because it allows for modeling patient trajectories where measurements and treatments take place at arbitrary, irregular timestamps. We thus propose a new method called \emph{\methodlong}~(\method). For this, we further derive stabilized inverse propensity weights for robust prediction of the potential outcomes. To the best of our knowledge, our \method is the first neural method that performs \emph{proper adjustments for time-varying confounding in continuous time}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Models that can predict patient outcomes over time from EHR and insurance claims trajectories are increasingly important. This problem is technically non-trivial since patient events take place at irregular times and often have burst-like patterns around a major event. The key here is to model outcomes in continuous time and account for confounding that varies in time. The paper considers methods for adjusting time-varying confounding in continuous time, and proposes a new framework that permits doing so i.e. for irregular measurements. The presentation is heavy in formalism, but quite well-written. However, despite the formalism, the method by itself is fairly simple, at least in principle. The main problem as mentioned earlier is to predict patient outcome with interventions on both the treatment propensity and the treatment frequency given the history of the patient. The authors first write a separable interventional distribution (involving a geometric product integral) and clarify how the process also ensures identifiability. The general formulation for patient outcomes involves inverse propensity scoring, which is non-trivial to work with for various reasons, including computational tractability and instability. The paper first proposes a simple method to make the objective tractable and then formulate a scaling factor to weigh inverse propensity weights to improve stability. The architecture description looks quite complicated at first, but under the formalism is quite straightforward (although I do have concerns about how easy it is to train). The architecture is an encoder-decoder type network that involves learning the unstabilized inverse propensity measures with another network to obtain scaling weights, all of which are implemented using neural controlled differential equations. The experiments are rather brief, but in my opinion, sufficient to illustrate the efficacy of the method. 

Overall, I thought the paper was innovative and I enjoyed reading it.

### Strengths
-- The paper is generally well-written and rigorous. It is also well-motivated and provides a solution of a problem of quite some importance not just in healthcare (the focus of this paper), but also applicable to other areas such as banking (where customer interactions are modeled in a similar manner irregularly, where interactions can also happen in bursts i.e. such as around a fraudulent transaction).
-- The contribution, to the best of my knowledge is novel and interesting.

### Weaknesses
 -- The paper obviously needs a lot of formalism, which is fine, but on the surface it seems like the network construction is essentially quite simple. But still, it is not clear how easy it is to train. It would be great to include more details on training details and difficulties, if any, in the appendix. On looking at the paper, one might think that the approach is complicated.


### Questions
See the above filed under "weakness": I am curious about how easy is it to train the proposed model compared to the competition. I understand that the approach intends to improve stability, but the actual training exercise could possibly be quite involved given multiple moving parts.

### Soundness
3

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
This work proposed the inverse propensity weight adjustment and stabilized inverse propensity weight adjustment to the training of continuous time modeling of counterfactual outcomes using neural controlled differential equations. The weights and stabilized weights are learned by separate neural networks, and used to adjust the target of outcome model, yielding a weighted MSE loss. The approach was evaluated on synthetic dataset based on tumor growth model and semi-synthetic dataset based on MIMIC-III, on showed noticeable improvement to compared prior work.

### Strengths
1. To the best of my knowledge, the use of inverse propensity weight to adjust the neural estimation of conditional average potential outcome in continuous time has not been proposed, so there is some non-trivial novel contribution in this work.

2. The paper is well-written and easy to follow. It is quite notation-heavy but I'm not sure if there is much room for improvement.

3. Good experimental results are shown on MIMIC-III and one-day ahead prediction of the tumor growth model.

### Weaknesses
1. Corresponding to Strengths 1., although the use of inverse propensity weight to adjust the neural estimation of conditional average potential outcome in continuous time has not been proposed, I do not see it as a significant contribution. It is a combination of TE-CDE and the line of work by Lok, Roysland and Rytgaard, i.e. A+B style contribution. Therefore, I think a score in the acceptance range is warranted, but not high acceptance.

2. There are quite a few statements in this paper that I think are either inaccurate or in lack of evidence. In their statement of contributions (L100-107), they claim that balancing is a heuristic approach to adjust for time-varying confounding and was originally proposed for variance reduction, however, it is in fact first proposed in [1] for counterfactual inference. [2] was cited to state that balancing may increase bias, however, bias adjustment in [2] is for marginal parameter (averaging over covariates) and I don't think it is related to the conditional estimation in the scope of this work. Overall, I don't see any real argument or evidence that balancing is more biased than the proposed method and hence, I definitely don't think it is appropriate to say that it does not "properly" adjust for time-varying confounding. Besides, the parameter of interest is the conditional average potential outcome instead of potential outcome, and it should be stated correctly in Proposition 1 and the title.

### Questions
1. Corresponding to Weaknesses 2., the authors should provide more robust argument or experimental evidence that balancing is biased and "not proper" compared to IPW adjustment, and change the column name "adjustment for time-varying covariates" in Table 1 to "propensity weight adjustment for time-varying covariates".

2. Other than balancing and IPW adjustment, the more recent temporal-difference learning approach [3] adjust for time-varying covariates by constructing targets with weighted average of neural pesudo-outcomes. Such method should be discussed in related work. 

[3] Shirakawa, Toru, et al. "Longitudinal Targeted Minimum Loss-based Estimation with Temporal-Difference Heterogeneous Transformer." International Conference on Machine Learning. PMLR, 2024.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study proposed SCIP-Net, a model designed to predict potential outcomes in continuous time. SCIP-Net adopts controlled differential equations (CDEs) as its architecture and primarily relies on inverse propensity weighting with stabilizing weights to estimate potential outcomes.

### Strengths
The paper's contributions are practically significant, as detailed in the introduction. 

The authors provide a thorough explanation of the problem formulation and model architecture. 

The paper is well-structured with (1) visual emphasis on key points and (2) a coherent organization of sections.

### Weaknesses
The numerical experiment section needs further details, particularly about the experiment setup (e.g., how the data are randomly sampled). I see that some of the details were referenced in the previous study (Vanderschueren et al.) and supplementary (perhaps most likely due to the page limit). However, considering different sampling strategies from Vanderschueren et al. and novelties compared to the previous studies that aimed to POs in discrete time, I believe it will be worthwhile to put more details about the experiment setup.

I believe the length of the forecast horizon (i.e., prediction window) affects the irregularity of the timestamps. Looking at the results when the forecast horizon is small (i.e., one-day prediction in tumor growth and 1 hour in MIMIC), SCIP and CIP did not show meaningful differences, which may be due to not significant irregularity of timestamps since the prediction horizon is small. Therefore, it will be very informative how irregular the timestamps (e.g., distributions of the length of the timestamps) are to analyze the performance and benefits of the proposed method. 

The ablation studies that compared CIP-Net and SCIP-Net are appropriate to show the benefits of using stabilized weights. Related to the comment above, it will be also informative if authors can show the performance of the proposed methods and baselines on regularly sampled timestamps.

### Questions
Figure 3 and Table 2 have low readability due to the small fonts and figure legends. The authors might consider improving the readability of them.

In Figure 3, the performance of TE-CDE is very different from the original publication since TE-CDE was outperformed by RMSN and CRN. It is different from the experiment on MIMIC data. Can authors provide reasonable guesses?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the modeling of EHR as continuous time series. In particular, it focuses on modeling the time-varying confounding as well. This paper proposes a stabilized target to fit and a neural network architecture, and validated the proposed method on two synthetic datasets.

### Strengths
The problem studied in this paper is important. Being able to perform "what if" analysis is critical in medical (and other) times series modeling tasks.

### Weaknesses
1. Experiment: Fundamentally I found it a bit difficult to conclude that the proposed method is effective. There are a lot of literature on similar topics (they may use the term "irregular time series" instead of "contiuous"). Although they do not model the confounding variables, in reality it is difficult to  know if such additional modeling helps or hurts. The paper now uses simulated data to show the point, but simulated data is fundamentally not reliable. One possible way to show that modeling confounding actually helps might be tweaking the distribution by oversampling certain interventions. If the proposed modeling actually helps, I'd imagine it not noly improves metrics measured on the original marginal distribution, but should also be better on the re-sampled distribution. 
	a. To be very clear, if the goal is to predict the effect of drug A on symptom B, and the proposed method actually models 1. when A will be applied, given EHR history x 2. result of A on B, then I'd expected that it might not always beat something that learns the marginal distribution B|x, but if we focus on only B|A=1 or B|A=0 (using real, unsimulated data), the covariate shift should have little to no impact on the proposed method but greatly hurts other baselines. 
	b. Please also include more literature in the "irregular time series" modeling space.

2. Presentation and writing bothers me a bit. While I appreciate the use of coloring to distinguish certain quantities, things like "=>Takeaway" in L509 makes the manuscript a bit too casual in my opinion. Minor issues on some of the expressions as well (such as "unconditional of" at L272). 
		a. Also related to 1, the experiment section is very unclear right now. The paper only says "RMSE" is the evaluation metric, but "RMSE of what"? This is particular problematic given that the dataset itself is synthetic. I'd suggest moving some details from the Appendix to the main paper and but very clear about the setup of the experiment (and the motivation behind it).

### Questions
1. How sensitive is SCIP-Net’s performance to the specific confounding strength? If confounding is minimal (and the data abundant), would SCIP-Net still provide benefits over simpler models? I saw that Figure 3 is related to this, but it's hard for me to make association between $\gamma$ and more realistic dataset. 

2. Can the authors elaborate how the baselines were chosen?

### Soundness
2

### Presentation
2

### Contribution
2
