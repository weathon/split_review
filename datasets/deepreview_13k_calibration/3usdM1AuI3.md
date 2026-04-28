# BRAID: Input-driven Nonlinear Dynamical Modeling of Neural-Behavioral Data

- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 8, 8, 6

## Abstract
Neural populations exhibit complex recurrent structures that drive behavior, while continuously receiving and integrating external inputs from sensory stimuli, upstream regions, and neurostimulation. However, neural populations are often modeled as autonomous dynamical systems, with little consideration given to the influence of external inputs that shape the population activity and behavioral outcomes. Here, we introduce BRAID, a deep learning framework that models nonlinear neural dynamics underlying behavior while explicitly incorporating any measured external inputs. Our method disentangles intrinsic recurrent neural population dynamics from the effects of inputs by including a forecasting objective within input-driven recurrent neural networks. BRAID further prioritizes the learning of intrinsic dynamics that are related to a behavior of interest by using a multi-stage optimization scheme. We validate BRAID with nonlinear simulations, showing that it can accurately learn the intrinsic dynamics shared between neural and behavioral modalities. We then apply BRAID to motor cortical activity recorded during a motor task and demonstrate that our method more accurately fits the neural-behavioral data by incorporating measured sensory stimuli into the model and improves the forecasting of neural-behavioral data compared with various baseline methods, whether input-driven or not.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
BRAID aims to distinguish the effect of measured inputs towards neural dynamics, while dissociating shared neural-behavioral dynamics, neural-only dynamics, and behavior-only dynamics. It does so by training a series of recurrent neural networks: (1) Stage 1 trains a shared recurrent neural network that outputs both neural activity and behavior for (a) 1-step ahead and (b) multi-step ahead prediction, (2) Stage 2 does similarly but for neural dynamics only, and (3) Stage 3 does so for behavioral dynamics only. The authors show better correlation coefficients with the neural and behavioral activity in validation datasets as compared to some baseline comparisons.

### Strengths
- The method dissociates neural-only, vs. behavior-only, vs. shared neural-behavioral spaces.
- BRAID has the ability to take in measured inputs. However, this is not providing any conceptual advance from existing methods, since they are simply fed into the RNNs with an additional input transformation in the form of K.

### Weaknesses
 - BRAID is very similar to DPAD (Sani et al., 2024), but with the addition of measured inputs, behavior-only dynamics, and an additional network that predicts m-steps ahead. None of these additions are conceptual advances, and are extremely straightforward additions to an existing method.
- The paper claims that "BRAID disentangles [input] dynamics from intrinsic dynamics", however the contribution of the inputs is not analyzed further at all - can one effectively disentangle input dynamics from intrinsic dynamics via this approach?
- The modeling strategy is multi-stage and quite involved, with multiple RNNs being trained without fully going into the utility of each one. The 'RNN_{fw}' models seem to be forecasting, but why is it necessary to have a separate RNN for forecasting when the 'RNN_1' model is a dynamical model that should be in theory capable of predicting m-steps forward in time?
- The R^2 should be reported throughout the paper instead of Pearson's; the R^2 is more standard in this field, and takes into account the predictability using the mean value of the signal.
- There is no attempt at interpretability of the underlying dynamics and the contribution from different sources as identified by this method.
- While the authors show that BRAID performs with higher behavior reconstructions than TNDM as shown in the Appendix, this is very much to be expected since TNDM does not optimize separately for behavior reconstruction, as BRAID does. Similarly, DPAD does not either (and does not take in inputs). However, these are very simple to add to both of these methods, and thus do not provide fair comparisons in their existing form.

### Questions
None noted / see above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new deep learning method to jointly model neural and behavioural data by explicitly modelling task inputs, in order to better model and disentangle input effects and intrinsic neural dynamics that are predictive of behaviour. The learning of the intrinsic dynamics is enabled by the use of a forecasting objective, i.e., $m$-step-ahead neural and behavioural prediction. The method involves 2 (or 3) RNN models, and optimisation is done in multiple stages: a pre-processing stage to filter out behaviours that are not relevant to recorded neural dynamics (used instead of actual behaviour for training), a stage to learn the neural dynamics predictive of behaviour, and a stage to learn any residual neural dynamics. The proposed method outperforms several baselines at predicting neural activity and decoding behaviour, and is also amenable to real-time predictions due to its causal formulation.

### Strengths
* The method is well-motivated given prior work, and the causal formulation makes it amenable to real-time inference, which is a strong asset.
* The figures are neat and the experiments are comprehensive. The writing is mostly clear, but I have some comments on explaining the method in a slightly clearer manner (see Weaknesses).
* The method performs well not only on synthetic tasks designed to show its efficacy over several baselines, but also on decoding real neural data.

### Weaknesses
 * The model architecture and the learning stages are quite complicated, and the writing makes this hard to understand in some places. If I've understood this correctly, there are mainly two RNNs: one to predict the next timestep neural activity given current activity and observed inputs, and another to predict activity $m$ timesteps into the future using just observed inputs. Each of these RNNs' parameters are split into up to 3 subsets, which are optimised sequentially: one to learn behaviourally relevant neural dynamics, one to learn any residual dynamics, and another to learn behaviour that is not encoded in the neural dynamics. This is in addition to an RNN that preprocesses inputs.

  While this preprocessing RNN has been ablated for, can the authors comment on how one identifies in practice whether or not to use the second and third stages of training (RNN2 and RNN3), which were mentioned to be optional? Specifically, what criteria or diagnostics should a user employ to determine if the additional complexity of these stages is warranted for a given dataset? In general, some additional clarity in the writing here would be appreciated.

* It would be important to see how the method scales with the number of neurons – based on the details in the appendix, it seems like the maximum dimensionality explored here (in the neural data case) is around 45. Perhaps the authors could run an experiment comparing decoding performance and neural predicitivity for differing numbers of neurons from the same dataset to show this (and also comment on the time taken to train BRAID). It would be useful to see if the performance gains are maintained as the number of neurons increases, or if there are diminishing returns or even performance degradation due to the increased parameter space.

* From the experiments it seems that BRAID is mainly a single-session model. It is well-known that there can be a lot of variability in neural activity across sessions as animals learn to perform the task better or due to some representational drift. This does not seem to be addressed in the paper as far as I can see, but could the authors comment on how BRAID generalises to unseen sessions, and also specifically for the later parts of a session when training on the initial parts (one of the 5 folds)? It would be beneficial to see a quantitative analysis of how the model's performance degrades when tested on data from later portions of a session or entirely unseen sessions, and what steps could be taken to mitigate this.

* While the experiments are comprehensive and baselines have been compared against, I think comparisons with LFADS (and if possible, CEBRA) could be useful here – both these approaches seem slightly less involved in terms of training complexity, but would represent baselines when ablating for explicit input modelling (LFADS) or explicit dynamics modelling (CEBRA). The idea here is also that LFADS is designed to infer inputs to the dynamical system, so it might perform better than the extended TNDM baseline included currently. It would be important to understand how BRAID compares to these methods, especially in scenarios where the underlying dynamics are complex or the input signals are noisy.

### Questions
* Could the authors attempt to make the writing clearer with regards to explaining the model and the various training stages? Perhaps a summary as a table might help.
* Is it possible to show results when ablating for the second and third (post-hoc) stages of training? Apologies if I've missed this. Also, could the authors comment on what happens when just training the model end-to-end?
* Could the authors consider experiments that show the scaling performance of the model vs number of neurons, and attempt to compare with LFADS (and CEBRA) if possible?
* Could the authors comment on multi-session models, generalisation to unseen sessions?
* Apart from neural predictivity and behaviour decoding, could the authors perhaps use a similarity metric to explicitly compare the learned and true dynamical systems (e.g. using [Dynamical Similarity Analysis](https://openreview.net/forum?id=7blSUMwe7R))? This should be fairly easy for the synthetic tasks, and should be possible in case of the neural data as well.
* It would be interesting to see the model's performance on a dataset involving multiple brain regions, but I understand that this would take more time to run and depend on the availability of a dataset.
* I spotted a potential typo on Line 073 ("prepossessing" -> "preprocessing"?), and another minor issue on Line 111 ("intrinsic representation of dynamic." -> "dynamics"?).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors tackle the problem of disentangling intrinsic from input-driven neural dynamics underlying behavioral measurements. They do so through a novel nonlinear model called BRAID. Their approach is to conceptualize the intrinsic as the generative (i.e. forward) dynamics, and the input-driven as the (posterior-) predictor dynamics. The authors model each of these components with nonlinear DNNs for flexibility, allowing each to be learned. Importantly, they devise a multi-stage training procedure that prioritizes learning behavior-relevant dynamics, with neural reconstruction placed second.  They show how this approach can help disentangle the neural dynamics directly relevant to behavior, in both synthetic experiments and monkey motor reaching neural activity.

### Strengths
- The work tackles a very relevant question in the field of statistical neuroscience of disentangling the relationships between behavior, neural activity and inputs, and shows originality in doing so with careful modeling. 
- The modeling is well-formulated in the main text, and made clear for the reader in the appendix and through provided code.
- The decomposition into multiple stages and sub-components to encourage learning behavior-relevant activity is interesting and novel (to my knowledge).
- The authors showcase their model on synthetic and real experimental data, showing strong performance in both. 
- The authors help support the significance of their results by (1) comparing them against many baselines and extensive ablations of their model, and (2) performing many runs, providing error bars for all numerical results. 
- The metrics are meaningful and bypass common non-identifiability problems (such as considering the eigenvalues of A)
- The figures are clean and easy to understand.

### Weaknesses
I am putting a score of 8 but I would be willing to increase it if the authors can help address my weaknesses/questions, and in particular the "major" ones below.

Major:
- I am not convinced by the claims of real-time inference in the discussion, and the lack of surrounding literature on the predictor components of the model. Variational inference approaches for sequential models similarly model the (sequential, i.e. filtering) posterior and optimize it jointly with the generative model in the ELBO. I believe the similarities could be actually quite exact, in which case a fairer depiction of the relationship with VI is necessary. On that note, Table 1 refers to your method as pure LL optimization, but perhaps it could be more easily interpreted through an ELBO objective.
- Most of the results are numerical, and the paper lacks a bit in alternate results such as posterior trajectories or visual reconstruction.  
- In line with the previous comment, the monkey experiment results are numerical and would benefit from some post-training analysis if the goal is to show the model as a modeling and analysis tool. 

Medium:
- Appendix should be for additional but not necessary details to understand the paper. One example of this is the simulations in section 4.1. The notation from L312 follows the appendix where you introduce $f_{C_z}$ and $\nu, \bar\nu$ -- I would make it consistent with eq. (1) or add eq (A.11) to the main text.
- Identifiability: the authors discuss behavioral- vs neural-relevant activity, but having nonlinear A, Cs are another type of inter-dependence, which could be discussed further.
- Monkey experiment: numerical performance results are good but sometimes lack transparency in their presentation. For instance, U-BRAID does do better on neural, but that is by construction and does not put BRAID in any lesser light. The corresponding paragraph (3 of section 4.2) however does not acknowledge this better performance. Similarly, the authors refer to mmPLRNN as having an "unfair advantage" (L451). I would remove this.
- The relationship with probabilistic formulations is skimmed but still alluded to with the ELBO/LL in Table 1. I would expand further on these ideas. 

Minor:
- Using $\cdot$ (\cdot) instead of $.$ (dot) is more standard for place-holder variables in functions (L191, L312, L1015)
- Dependency on x^1 on Stage 2 could be made more explicit in the text
- Table 2: bold entries per metric would be more representative

### Questions
Some of the following questions relate directly to the weaknesses raised above. 
- How does your predictor relate to sequential posterior in variational inference?
- Monkey experiment: What do x^1 and x^2 look like in this task? Is there any non-encoded activity x^3?
- Could you provide more details on the "automatic" selection (L313)? Is it simply picking the best performing?

### Soundness
4

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
4

### Summary
This paper introduced a novel framework, BRAID, modeling nonlinear neural and behavioral dynamics with external input. This model dissociates behaviorally relevant neural dynamics, neural specific and behavioral specific dynamics, and outperforms baselines.

### Strengths
BRAID considers input-driven neural and behavioral dynamics and dissociates them. The authors performed ablation studies to shown which parts of BRAID contributed to the neural and behavior forecasting.

### Weaknesses
1. Although the model has been shown to be highly efficient in modeling neural spiking data, it has not been tested on other modalities, such as widefield calcium imaging.
2. Although the authors mentioned that their model is not to infer unmeasured input, I still think this may be a weakness of this model, because (for example) the neural and behavioral dynamics can be encoded by unmeasured input.

### Questions
1.	In Figure 1, should there be a connection between stage 2 and behavior Z_k if you are learning C_z(2) in Stage 2 2b? If so, what is the difference between X_k(1) and X_k(2) since both are connected to neural activity via [C_y(1), C_y(2)] and to behavior via [C_z(1), C_z(2)]?
2.	In equation 1, the model can learn behavior dynamics that are predictable from the input but are not encoded in the recorded neural activity, but how do you make sure that the behavior prediction is not dominated by the input? In Figure 3a, there is a high correlation between your input target position and your behavior cursor position and velocity. If so, can the model learn any information encoded in neural activity?
3.	The model also has an input term in modeling neural activity y, what does this input mean? Because you have an input in latent space that encodes intrinsic contribution, then you also have the same input to encode input-driven contribution. 
4.	How do you define your initial states x0?
5.	I am curious, how do you ensure that the model learned all encoded information and the residual is the non-encoded information since the model is nonlinear with high flexibility? 
6.	Following Q5, you mentioned you trained the model until convergence, could you show your learning curve against epochs with zooming in the last epochs if necessary?

### Soundness
3

### Presentation
3

### Contribution
3
