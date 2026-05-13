# Predictive Coding beyond Correlations

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Recently, there has been extensive research on the capabilities of biologically plausible algorithms. In this work, we show how one of such algorithms, called predictive coding, is able to perform causal inference tasks. First, we show how a simple change in the inference process of predictive coding enables to compute interventions without the need to mutilate or redefine a causal graph. Then, we explore applications in cases where the graph is unknown, and has to be inferred from observational data. Empirically, we show how such findings can be used to improve the performance of predictive coding in image classification tasks, and conclude that such models are able to perform simple end-to-end causal inference tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the introduction of the predictive coding for causal inference and discovery. They claim that a few simple changes in the standard PC process enable these both these tasks.

### Strengths
- Original exploration of PC concepts in this context

### Weaknesses
- Paper is very informally written and theorems / definitions are not up to standards of a statistics community. Eg Theorem 1 has no assumptions stated, what are the spaces allowed of the variables involved etc.
- **I don't see actual methodological novelty wrt to causal inference and/or discovery except "interpretations" of existing techniques in the parlance of predictive coding.** If the interpretation is the only contribution, can you clarify what is the value here? The paper purports to introduce predictive coding for causal inference and discovery, but the presented methodology seems to largely reframe existing techniques. For instance, the adaptation of the method by Zhang et al. (2018) for structure discovery raises questions about the specific novel contributions of predictive coding in this context. Is predictive coding being used to propose a fundamentally different approach, or is it primarily providing a new lens through which to view established methods?
- Theorem 1 is irrelevant and not new or a contribution, I am not sure why it is there. The statement "This approach obviates the need for explicit adjustment formulas and back-door criteria in causal inference." preceding Theorem 1 appears to overstate the contribution. While technically correct, it seems to be a direct consequence of the "truncated factorization" as defined in Pearl 2009 (Eq 1.37) when there are no unobserved confounders. In such a scenario, back-door adjustments are not needed even under standard causal inference frameworks. The theorem, in its current form, does not seem to add substantial value or novelty to the existing body of knowledge.
- Same for Sec 2. Causal graph is defined wrongly or incomplete at least; the Markov factorization is not what makes an CBN, since it applies to standard BNs. See definitions of CBN in eg [Pearl, 2009, Definition 1.3.1] , it's about all interventional distributions having the Markov fact. and other constraints.
- What are the assumptions in the part before 2.1  "Posterior distribution" ? The method is presented in the intro/abstract as very general but here we seem to require Gaussian assumptions, unit variances, mean field approximations .. all these in text and not presented properly mathematically (see comment above too). Is the setting the same as Peters et al (see below reference) ? Specifically, the reliance on Gaussian assumptions, unit variances, and mean-field approximations should be clearly stated and justified. The current presentation lacks the mathematical rigor expected in a statistical context, leaving ambiguity about the precise conditions under which the proposed method is applicable. A more formal mathematical exposition, including a clear statement of the optimization problem with argmins, would significantly enhance the clarity and credibility of the approach.
- At start of 2.1 you say you will use SGD for optimizing ( I guess F from Eq 2) - why SGD ? This is a simple least squares objective to optimize and simpler (faster) alternatives exist. Unless I'm missing something but again not very formally presented, there is no clear optimization problem stated with argmins etc. The choice of Stochastic Gradient Descent (SGD) for optimizing the objective function (presumably F from Eq. 2) seems suboptimal given the nature of the problem. The objective appears to be a least squares problem, for which more efficient and direct optimization methods exist. The absence of a clearly stated optimization problem, complete with argmins and a precise definition of the variables involved, further compounds this issue.
- For discovery you use the method of Zhang et al (2018) - again where is the novelty here ? Is PC used to propose a different method or not ?


References
- Peters, J. and Bühlmann, P., 2014. Identifiability of Gaussian structural equation models with equal error variances. Biometrika, 101(1), pp.219-228.

### Questions
Explained in the weaknesses section

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors show that it is possible to use predictive coding on graphs to answer causal and counterfactual queries as well as learn the causal structure. For causal queries, this is done by mimicking interventions (fixing certain nodes to a value) during the inference phase of PC. For counterfactual queries the process is similar - the usual operations of abductions, action and prediction are shown to be do-able with PC inference. Structure learning can also be done using PC on the adjacency matrix of the graph.

### Strengths
- The paper provides another way of answering causal queries from the conventional methods, which is interesting in itself

### Weaknesses
 - The main weakness of the work is the presentation, in that it is very hard to parse the information. A lot of the details are in the Appendix but there are not enough pointers to the Appendix in the main text (e.g. Appendix D is never referenced).
	- Where are the results comparing the causal queries with VACA, CAREFL, etc? It's not stated in the main text.
	- Results in section 3.2. For which experiment are these results of? It seems its only for counterfactual queries.
	- Figures like fig 4, fig 5, and fig 6 have too much information from too many results. These results can also be presented in much cleaner formats. For example, in structure learning the mean squared error of the learned and actual adjacency averaged over multiple runs would be much more informative than simply showing the adjacency for two graphs.
	- Figures 15- 20: Its unclear for what tasks and under which data generation regime these results are for.
	- Figures 8 -14: I can't see these referenced anywhere and so it is entirely unclear what these are showing.


- Another main weakness is that while it is interesting that it is possible to perform causal queries with PC, what is the obvious advantage? For causal queries, contradictory to the claims made in the paper, its not obvious that the PC approach is more efficient. Specifically, the method states that "To avoid this and perform an intervention, we set the value of e2 to zero throughout the inference phase". This implies that the inference has to be rerun for a different error to be set to zero (and hence a different query). It is unclear if the parameters of the variational approximation also have to be retrained for each intervention. For structure learning, why would PC perform better than other maximum likelihood methods? A more thorough discussion of what is exciting about the fact that PC can be used to answer causal queries would benefit the reader.

 - It should be made more clear that the method assumes that the observed variables are Gaussian distributed (eq 1). This assumption, that each conditional is Gaussian distributed, is quite restrictive in terms of what can be modeled. While the variables themselves do not have to be Gaussian, the assumption on the conditionals limits the applicability of the method.
- Intervention query: Am I correct in assuming that for each intervention query, a new PC graph has to be trained from scratch? I believe this is the case as a different error has to be zeroed out. If so, is this not very inefficient? This is not the case if interventional queries are found by doing graph mutilations.  
- Classification task: A lot more detail is needed for this to be clear. It is simply stated that "we perform an intervention on the input" but its not clear what this means. An intervention in a causal sense means, putting in another input which will change the label as well. If you mean zeroing out the errors of the input nodes, this needs to be made clear. "Intervention" has a very specific meaning in causal literature. The Appendix has insufficient details. 
- Structure learning: Has the data been normalised? If not, this should be mentioned and compared against standardised data in line with [1]

Minor points:
- X_unk is never formally defined
- Appendix is a bit messy.
	- Took a while to find where the non-linear data generation was as Appendix D is never referred to in any of the text.
	- Final line in discussion in page 20: This seems slightly misleading, the data in all cases is generated with additive Gaussian noise, whereas the methods discussed are specifically designed to deal with Non-Gaussian distributions.

- How does predictive coding handle a single dataset? All the theory in the paper assumes access to a single datapoint.
- Section 3, Interventional query: "...perform an intervention", what variable the intervention on? It's not clear here
- Section 2.1: What is time step t refering to? It has not been defined.
- Given that each x_i is a node in the (causal) graph, how is it possible to use deeper neural networks (eq 1) to learn the relationship between observed variables? The current formulation seems to limit the relationship between variables to 1 layer NNs.
- If generated from non linear data, the counterfactual queries are not identifiable, how does the method handle this?

### Questions
- It should be made more clear that the method assumes that the observed variables are Gaussian distributed (eq 1).
- Intervention query: Am I correct in assuming that for each intervention query, a new PC graph has to be trained from scratch? I believe this is the case as a different error has to be zeroed out. If so, is this not very inefficient? This is not the case if interventional queries are found by doing graph mutilations.  
- Classification task: A lot more detail is needed for this to be clear. It is simply stated that "we perform an intervention on the input" but its not clear what this means. An intervention in a causal sense means, putting in another input which will change the label as well. If you mean zeroing out the errors of the input nodes, this needs to be made clear. "Intervention" has a very specific meaning in causal literature. The Appendix has insufficient details. 
- Structure learning: Has the data been normalised? If not, this should be mentioned and compared against standardised data in line with [1]

Minor points:
- X_unk is never formally defined
- Appendix is a bit messy.
	- Took a while to find where the non-linear data generation was as Appendix D is never referred to in any of the text.
	- Final line in discussion in page 20: This seems slightly misleading, the data in all cases is generated with additive Gaussian noise, whereas the methods discussed are specifically designed to deal with Non-Gaussian distributions.

- How does predictive coding handle a single dataset? All the theory in the paper assumes access to a single datapoint.
- Section 3, Interventional query: "...perform an intervention", what variable the intervention on? It's not clear here
- Section 2.1: What is time step t refering to? It has not been defined.
- Given that each x_i is a node in the (causal) graph, how is it possible to use deeper neural networks (eq 1) to learn the relationship between observed variables? The current formulation seems to limit the relationship between variables to 1 layer NNs.
- If generated from non linear data, the counterfactual queries are not identifiable, how does the method handle this?

[1] Reisach, Alexander, Christof Seiler, and Sebastian Weichwald. "Beware of the simulated dag! causal discovery benchmarks may be easy to game." Advances in Neural Information Processing Systems

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method for causal inference using predictive coding. The authors demonstrate that, given a known causal graph, the proposed method can perform both interventional and counterfactual inferences. In cases where the causal graph is unknown, a gradient-based approach is introduced to discern the causal structure. Through experiments with synthetic data, the authors illustrate that their method outperforms existing approaches.

### Strengths
- The paper is self-contained with a pretty novel approach for causal inference.
- The proposed method outperforms existing methods for structural learning, interventional, and counterfactual inferencing. 
- The authors claim that the proposed method is parameter efficient and does not require extensive hyperparameter tuning.

### Weaknesses
 - It is not very obvious how the proposed method compares with the existing frameworks. So, it is also not very clear how the proposed method would contribute to the research direction. An in-depth discussion comparing the PC graph with DAG might lend more weight to the paper's influence on the causality.
- It is not easy to see in principle how the proposed method is superior to the probabilistic method.
- While the comparison against baseline methods using synthetic data provides some insights, it would be more convincing to see the comparison of inferencing and structural learning with some real data.

### Questions
- In equation 1, is the variable $x$ sampled from the standard normal distribution or a parameter of the model?
- Is there any intuition of how the PC graph outperforms the existing method? Is it mainly because the proposed model better estimates the observational probabilities?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper demonstrates  the potentiality of predictive coding to handle causal related questions including causal inference and causal discovery. In the case of causal inference, the authors set the prediction error term to be 0 and show how this intervention helps the PC based models go beyond correlation. For the structure learning, causal relationships were derived from observational data using PC models. The proposed method is tested on a large number of benchmarks.

### Strengths
I think a leap from correlation to causation for predictive coding models could be interesting. This work consider a wide range of causal scenarios that PC models can be useful, including the causal effect estimation, different queries (associational, interventional, and counterfactual), structure learning, and classification. All scenarios are supported by empirical experiments and some are provided theoretical guarantees.

### Weaknesses
I think a leap from correlation to causation for predictive coding models could be interesting. This work consider a wide range of causal scenarios that PC models can be useful, including the causal effect estimation, different queries (associational, interventional, and counterfactual), structure learning, and classification. All scenarios are supported by empirical experiments and some are provided theoretical guarantees.

For the predictive coding go beyond correlation, I was expecting some formal assumptions and theorems to build a solid framework. This paper, however, use more intuitional and descriptive statements to demonstrate the methods. The figures look fancy but not illustrative, I also noticed that Fig. 7 mentioned  in page 5 causal inference section is missing. In addition, the structure is a little bit hard to follow, the important contents are scattered and not cohesive. See more detailed questions below.

1. page 3: it is noted that the way of removing impact of latent confounder is to do intervention on a randomly selected individual. Then with the intervened data, could we simply do the standard ATE calculation? What is the main advantage of PC model on causal inference compared with other methods?
2. page 4, Theorem 3.1: Any constraints on the horizon t? How is the asymptotic performance of the proposed estimator? Any sample size calculation for the PC related method?
3. page 6, classification: Could you further explained the relationship between classification and causal inference under the predictive coding model setting? What are the classes here? And how test accuracy is related to causal effect?
4. If the graph is unknown, could the PC model still do causal inference by using the structure learned by PC from observational data?

### Questions
1. page 3: it is noted that the way of removing impact of latent confounder is to do intervention on a randomly selected individual. Then with the intervened data, could we simply do the standard ATE calculation? What is the main advantage of PC model on causal inference compared with other methods?
2. page 4, Theorem 3.1: Any constraints on the horizon t? How is the asymptotic performance of the proposed estimator? Any sample size calculation for the PC related method?
3. page 6, classification: Could you further explained the relationship between classification and causal inference under the predictive coding model setting? What are the classes here? And how test accuracy is related to causal effect?
4. If the graph is unknown, could the PC model still do causal inference by using the structure learned by PC from observational data?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
