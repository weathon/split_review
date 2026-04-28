# Identifying neural dynamics using interventional state space models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Neural circuits produce signals that are complex and nonlinear. To facilitate the understanding of neural dynamics, a popular approach is to fit state space models (SSM) to data and analyze the dynamics of the low-dimensional latent variables. Despite the power of SSM in explaining neural circuit dynamics, it has been shown that these models merely capture statistical associations in the data and cannot be causally interpreted. Therefore, an important research problem is to build models that can predict neural dynamics under causal manipulations. Here, we propose interventional state space models (iSSM), a class of causal models that can predict neural responses to novel perturbations. We draw on recent advances in causal dynamical systems and present theoretical results for the identifiability of iSSM. In simulations of the motor cortex, we show that iSSM can recover the true latents and the underlying dynamics. In addition, we illustrate two applications of iSSM in biological datasets. First, we apply iSSM to a dataset of calcium recordings from ALM neurons in mice during photostimulation and uncover dynamical mechanisms underlying short-term memory. Second, we apply iSSM to a dataset of electrophysiological recordings from macaque dlPFC recordings during micro-stimulation and show that it successfully predicts responses to unseen perturbations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of modeling neural dynamics under causal perturbations, an important open problem in computational neuroscience. The authors propose an extension to PfLDS — an established and expressive state space model for neural data with linear dynamics and nonlinear emissions — that accounts for causal interventions on the latent state of the model, in both the generative model and  inference approach. Furthermore, they provide a proof, under specific assumptions, of identifiability of the unperturbed model dynamics when using causal interventions. The authors apply the proposed approach to simulation of two established hypotheses of neural dynamics underlying motor activity generation, showing they are able to recover the latent trajectories and reconstruct observations under the model. They also apply the approach to two neural datasets involving causal perturbations, showing their approach can be used to gain insight when modeling real neural data.

### Strengths
Overall, this is a good paper with a simple and elegant approach to making progress on an important open problem, despite some limitations.

* The paper addresses an extremely important and under-explored open problem in computational neuroscience — modeling neural dynamics under causal perturbation — and as such has potential for large impact in the field. Applying causal perturbations is a critical experimental approach to gaining insight into neural mechanisms that continues to develop with relatively little support on the modeling side. State space models (SSM) are an important and widely used neural modeling approach, and so an important entry point into this problem. Furthermore, the authors attempt to formally address identifiability of the model under causal perturbations, an important open theoretical problem that complicates the practical use of state space modeling in neuroscience.

* Discussion of the scientific background and problem, relevant literature on interventional models and non-identifiability issues is generally excellent.   

* The overall approach is clever and well executed. The paper uses a well established, simple but highly expressive SSM model (fLDS), to make progress on this important problem. It suggests a simple and elegant extension to the model to consider causal interventions. There are important and noteworthy limitations of this approach which are not addressed in the paper (see weaknesses), but it is nonetheless an important contribution.

* Inclusion of the interventional structure by reuse of the generative interventional effect parameters B, in the inference process, is a nice idea that aligns with, but stops short of fully structured VAE (eg SVAE) inference approaches. 

* The proof of identifiability presented is rigorous and instructive and builds on recent theoretical results across the machine learning field — although the assumptions the proof relies on may be problematic, adding to the unaddressed limitations of this work (see weaknesses). 

* Simulations of two dynamical regimes inspired by established motor cortical dynamics hypotheses are well motivated by the literature.

* The paper uses two interesting and relevant neural datasets with causal perturbations, spanning calcium imaging and electrophysiology in mice and monkeys, showing the approach can be applied successfully to data and provide scientific insight.

### Weaknesses
While an important contribution, the paper has important weaknesses which should be addressed - and which could justify raising the score for the paper.

**Modeling interventions at the latent level seems to limit interpretability, and raises questions re. assumptions of the identifiability proof.**

A key, unaddressed limitation of the work is the assumption that interventions at the neuron level affect the latent dynamics directly. This is a reasonable approach for making progress on this open problem using SSMs, and it remains an important contribution despite these limitations, but the paper would benefit from explicit consideration of the limitations of this assumption and its implications for the model, the provided proof, and data analysis, which seem to me to be meaningful. 

An assumption of the SSM framework is that high dimensional activity can be well described, or summarized, by dynamics in a low dimensional latent space, and the generative model treats observations as emissions from the latent state, ie the causal graph of the model flows from latents to observations and not the other way around. This is a meaningful issue in using SSMs to model experimental causal perturbations performed at the neuron level. 

In section 3.1, the authors explain their modeling choice in a slightly confusing / misleading way:
“whenever a neuron is perturbed, its activity is dissociated from all its upstream neurons. This assumption is easy to incorporate in a linear model, which is achieved by ignoring the columns in the dynamics matrix corresponding to the perturbed neuron”

The issue is that the perturbed neuron is not directly represented in the latent dynamics matrix $A$, but rather is “mixed in” by the emission function $f$. In a system with linear emissions, this emission function is directly invertible; in the nonlinear case considered here, it generally is not. In either case of SSM, neurons are not privately represented in specific dimensions of the latent space by design.

The switching mechanism proposed by the authors $1 \lbrace Bu=0 \rbrace$ applies interventions to dimensions of the latent space rather than to individual neurons. Notably, there is no mechanism to encourage the latent dynamics to isolate perturbed neurons in private dimensions of the latent space, and it’s anyway not clear that this would be desirable from the perspective of modeling the spontaneous population dynamics — this is a feature and not a bug of SSMs. 

Indeed, the results in eg Figures 3,4 suggest that the learned model does not isolate dimensions of the latents, and instead learns interventional effects across both latent dimensions for every intervention. 

From this perspective, the model can really be seen as a fully switching linear dynamics model, with the switch gated by the existence of interventional inputs across all dimensions, and the interventional regime (given by input-driven dynamics Bu) ignoring the current latent state. 

Concretely, this choice and its limitations should be made more clear in the presentation of the approach. 

From the perspective of modeling usefulness and interpretability -- 

-There is no way to bake in known elements of the stimulation, eg in the mice data case where specific neurons are targeted based on their response selectivity.  
-Can this framework be used to analyze or make claims about the circuit mechanism involved in interventions, ie how individual neurons affect other neurons in the circuit? Can the framework be used to reproduce or further understand the local neuron level effects of stimulation?

**Assumptions of the proof**

Assumption 3.4 in section 3.3: “(do-interventions on each latent node). There is at least one do-intervention (i.e. non-random $u_t$) being performed on each latent dimension of $x_t$.”

In the current wording it’s not immediately clear that these interventions are required to be *separate* ie that the interventions happen on each latent dimension in isolation. My understanding is that this is in fact the case, and that the proof proceeds by considering interventions $1 \lbrace (B u_{t,j} ) = 0 \rbrace = 0$ performed on individual dimensions of $x$, which uncouple $x_{t+1,j}$ from $x_t$, and then arguing that if some dimension $\hat{x_j}$ is also uncoupled by the isolated intervention, than it must be an affine transformation of $x{_j}$. 

Does the proof therefore require the ability to intervene separately in individual dimensions of the latent space? That is, if every intervention involves $1 \lbrace Bu_{t,j} = 0 \rbrace = 0 \quad \forall j$, does the proof still work? Presumably this makes it such that all interventions will impact all latent dimensions?

This question relates to the main weakness discussed above - if neuron level interventions are modeled as direct interventions in the latent space that span the latent dimensions and are not isolated, these interventions will not allow isolation of individual latent dimensions in the model, and will be inconsistent with the identifiability proof.

If this is in fact the case, I believe the proof is still instructive and the method is still valuable, but it is a major limitation of the approach when applied to neural data and should be discussed in this light.

**Lack of comparison to non-interventional PfLDS model**

Another important but easy to fix limitation of the paper is the lack of comparisons - how much does the interventional framework improve the ability of the PfLDS model to recover the system parameters, latents, reconstruct observations under novel perturbations etc? An easy win for the paper would be to provide an example in which the interventional data, in both simulation and neural data, is fit using the standard PfLDS model. This would provide a baseline against which to judge the benefits of this approach.

**Showing that generative dynamics are consistent with inferred latents**

Using an LSTM for the recognition network allows for powerful inference, but given that the inference model learns an implicit model of the forward dynamics, it is important to show that generating sequences from the dynamics model {A,B} along with external inputs closely tracks inferred latents. 

**Figures could be improved**
* Figures are a bit hard to read and could be dramatically and easily improved, especially figures 1 and 2, 3 (eg axis ticks on panels C,D) and 4 to a lesser extent. Labels have a kind of “bleeding” bold font, text is too small, arrows are fuzzy, indices in the graphical model aren’t clear etc.
* In Figure 1, “spontaneous activity” may be a better label than “resting state” which has other connotations in the neuroscience literature, especially since the activity measured may typically involve the animal acting in an environment, processing experimental stimuli etc, although there is no neural intervention.
* Figures 2D,E are a bit hard to parse with the red black and blue dots and may have some mistakes in the legends? the text says:
(D,E) True (black) and inferred (red) latent (D) and observation (E) dynamics
But the titles are the other way around. Also I believe F represents the “behavior” output of the system, using the term emissions here is confusing since otherwise this term refers to the observations (neurons of the system). 

**No way to capture time varying interventional dynamics**

If optical or neural stimulation effects have a time course, this model will be forced to fit the average effect over that time course, unless the modeler decides to design the interventional input U as a time varying signal. This is fine but likely a meaningful limitation that should be noted.

### Questions
* See above weaknesses re questions on the interpretability implications of intervening on the latent state, as well as the proof assumptions 
* How does the amount of interventional data vs not interventional data differ in effecting reconstruction in simulation? Figure 2G shows for example that reconstruction of both latents and observations improves with the stimulation count, but it’s not clear whether that means the model is fit with more data in this case or not? Would be interesting to show how results are affected by additional observational vs interventional data. 
* Observations reconstruction seems to fall for the rotational dynamics case - any insight on why this may be?
* In the simulations, adding interventions improves recovery of latents and reconstructions, but its not clear that the interventions are actually necessary to disambiguate the two possible hypotheses on the motor flow fields? Would be nice to show this.

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
This manuscript introduces Interventional State Space Models (iSSM) to reveal latent neural dynamics under causal manipulations, addressing system identification problems in traditional state space models without interventions. The authors gave rigorous proof about the identification conditions and assumptions. They also showed that iSSM can recover true latent dynamics and predict responses to novel perturbations, using both simulated and real biological data from mouse and macaque experiments.

### Strengths
- Idea of intervention helps the identification problem is well justified 
- Detailed summary of the literature 
- Very clear presentation of the derivation process
- Promising results in recovering latent dynamics structures in simulations (i.e. Fig.2)

### Weaknesses
 - Model assumption 2 is too strong: From the equation on line 191. It looks like if there's a perturbation affects all latent dimensions, the internal dynamics (term A) at that time step would be totally ignored. This is certainly not a conventional way to model linear systems with input. Please give enough justifications on choosing this specific modeling equation. 
- This setup is essentially equivalent to system identification in a controlled system where controllability (thus identificabililty) is related to the structure of input matrix B. Could you comment on your assumptions on B? Or was B also inferred during the process?  
- Missing technical details in the inference procedure for readers unfamiliar with variational inference and reparameterization through recognition works. 
- For inference results, reconstruction correlation seems to be low. Could you include some baseline method correlation? Or how about using the non-intervened SSM for reconstruction.
- From the derivation in Session 3.3, it's unclear to me how the addition of input terms could help the identification problem. Could you emphasize the non-identifiability where B=0? 
- Assumption 3.2 assumes the observation function is piecewise linear but the ones used in simulation are not. Could you justify this? 
- Assumption 3.4 seems to be too strong by assuming there're perturbation cases at every latent dimension (and maybe for each time step as well?) Could you comment on how much this assumption applies to actual data? How much violation to this assumption could be tolerated?

### Questions
- From the derivation in Session 3.3, it's unclear to me how the addition of input terms could help the identification problem. Could you emphasize the non-identifiability where B=0? 
- Assumption 3.2 assumes the observation function is piecewise linear but the ones used in simulation are not. Could you justify this? 
- Assumption 3.4 seems to be too strong by assuming there're perturbation cases at every latent dimension (and maybe for each time step as well?) Could you comment on how much this assumption applies to actual data? How much violation to this assumption could be tolerated?

### Soundness
3

### Presentation
4

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
This paper proposed interventional state space models to causally predict neural responses to novel perturbations. The authors build a multiplication to the latent space to encode the interventional input. The model is tested on simulated data and is able to reconstruct the true latent and observations. The model is then tested on real data and is able to generalize to unseen interventional input.

### Strengths
The proposed iSSM jointly models the observational and interventional data, the model is applied to three different datasets and shows efficiency. The model can generalize to new interventions in the third dataset.

### Weaknesses
Lack of comparison: the authors mentioned that their contribution is to extend the model to the interventional regime, however, the authors did not show how this added interventional input affects the reconstruction or other aspects. Specifically, there is no ablation study to show the importance of the interventional component of the model. For instance, how does the reconstruction error change when the interventional input is not included? Also, it is unclear if the model is truly learning the interventional effects or simply fitting the data. The authors should also compare the performance of their model with other existing interventional models.



### Questions
1.	What do those blue dots mean in Figure 2 D and E?
2.	What do the inferred flow fields look like in Figure 2?
3.	How do you define input $u$? Also, in your simulation in section 4.1, are there any inputs?
4.	How do you choose your parameters? For example, dimension of latent. Did you try higher dimensions?
5.	In the first equation on page 4, does that mean when B$u_t$=0, 1 is multiplied to A$x_t$? Then what about B$u_t$ is not 0? You mentioned that the model decouples the intervened node from its parents, but the equation did not show this.
6.	Some equations are not labeled.

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
5

### Summary
The authors address the problem of constructing identifiable models of neural population activity by developing interventional state-space models. The idea is to utilize the theory of causal inference, which comes equipped with protocols and assumptions for model identification. The authors develop the model, prove identifiability under standard causal inference assumptions, and perform numerical investigations in three contexts with interventions: synthetic data, motor cortex Ca imaging, prefrontal cortex electrophysiology. 
Unfortunately, as outlined below, this paper has several limitations that prevent acceptance in its current form.

### Strengths
The theory is clear and well written, but is a straightforward combination of existing analytic approaches.

### Weaknesses
The theory is clear and well written, but is a straightforward combination of existing analytic approaches.

-Assumption 3.4 of causal inference is a very strong assumption, and it is not clear how to provide perturbation in systems neuroscience that adhere to it, and it is not discussed how to check this assumption in data. Indeed, it appears naively that the data displayed in Fig.3A,Fig.4A, in which the perturbation looks to affect most neurons, directly violates this assumption. This is a fatal flaw in the stated context of the manuscript, as the entire motivation for the paper and numerical validation are in the context of neuroscience.
-only low-d latent spaces are considered, but data could be high-d depending on task
-relatedly, selection of number of dimensions is not discussed
-compute time of algorithm not discussed? Useful in real-time?
-quantification: 
 –corr.coef is used, and the values look very low to me (e.g., Fig.3c,d, Fig.4I), so while there may be differences from 0, whether or not the model is meaningfully predictive is brought into doubt by the small effect size.
– samples sizes are not clear
    –statements about significance are vague (e.g., pg. 8 first paragraph)
-visuals are very small, hard to read, and poorly explained
-lots of plots, the relevance or results of which are poorly explained
	-there is no comparison to other methods whatsoever. Given the issues with 
Assumption 3.4 discussed above, this constitutes a fatal flaw in the current context, as the theory can not be used to justify the algorithm in the data to which it is applied, and as such other models/algorithms could perform comparably.
-no software availability as far as I could tell.
-no validation on non-interventional data (as far as i can tell) as another benchmark
-no numerical assessment of identifiability in the data. This could have been done in a number of ways, such as looking at the variance of the inferred variables in real data, or investigating how deviations from Assumption 3.4 are evidenced (e.g., systematic errors or magnitude of deviations across parameters) in the solutions.

### Questions
n/a

### Soundness
2

### Presentation
2

### Contribution
2
