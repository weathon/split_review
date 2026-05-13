# Modeling state-dependent communication between brain regions with switching nonlinear dynamical systems

- Decision: Accept
- Scores: 6, 6, 6, 6, 5

## Abstract
Understanding how multiple brain regions interact to produce behavior is a major challenge in systems neuroscience, with many regions causally implicated in common tasks such as sensory processing and decision making. A precise description of interactions between regions remains an open problem. Moreover, neural dynamics are nonlinear and non-stationary. Here, we propose MR-SDS, a multiregion, switching nonlinear state space model that decomposes global dynamics into local and cross-communication components in the latent space. MR-SDS includes directed interactions between brain regions, allowing for estimation of state-dependent communication signals, and accounts for sensory inputs effects. We show that our model accurately recovers latent trajectories, vector fields underlying switching nonlinear dynamics, and cross-region communication profiles in three simulations. We then apply our method to two large-scale, multi-region neural datasets involving mouse decision making. The first includes hundreds of neurons per region, recorded simultaneously at single-cell-resolution across 3 distant cortical regions. The second is a mesoscale widefield dataset of 8 adjacent cortical regions imaged across both hemispheres. On these multi-region datasets, our model outperforms existing piece-wise linear multi-region models and reveals multiple distinct dynamical states and a rich set of cross-region communication profiles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel approach, Multi-Region Switching Dynamical Systems (MR-SDS), for modeling neural interactions across multiple brain regions. The proposed method models low dimensional nonlinear neural dynamics. With transformer encoders inferring the states, the model provides a more precise representation compared to existing models such as rSLDS and RNNs. The model is validated by three simulations and is applied to two multi-region neural datasets.

### Strengths
The authors extend existing models to make them nonlinear, while keeping key aspects of modeling such as low dimensional dynamics in the neural space. Switching dynamics are able to describe neural activity in a variety of behaviors. The model is able to perform well on held-out and co-smoothing tests.

### Weaknesses
1. The authors state that RNNs have higher dimensionality while solving such problems, and thus, it is difficult to interpret the inferred dynamics. However, MR-SDS has a transformer included which may be even more difficult to interpret. Indeed, while the authors show a higher accuracy, they do not show the interpretability at all; it is not clear how interpretable this model is, more so since the communication between different brain regions cannot be accurately recovered (e.g., Fig. 2D).
2. In Figure 2, what is rho? Additionally, the reconstruction of states and the reconstruction of states’ communication are actually not good, thus, it is hard to say the model reconstructs the latent states successfully.
3. Could the authors detail the parameters, such as alpha, beta, and so on, in section 4.1.
4. In section 4.3, it would be better to link the paragraph to the figure with the corresponding result, referring to which figure the authors are talking about. Additionally, I assume that the figure is Figure 6, but how do the authors find that MR-SDS embeds a richer representation than PCA? And why is a richer representation better here? Since the resulting PCs are orthogonal, it is unfair to compare them with the richness of the data representation. 

Moreover, clarity is not as high as it should be. The authors would need to proofread the submission carefully and generate the figures professionally. Here are some examples that may need to be revised:
Section 4.1, last sentence: “MAKE SURE to say here that we also include in appendix A1 a result without the external input and show that we can still do inference but can’t generate” is not appropriate to show here.
Figure 2B needs a legend.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel state-space model for analyzing multi-region neural recordings. Briefly, the multi-region switching NLDS architecture assumes multiple, switching nonlinear latent dynamical systems per region, governed by a discrete state variable and continuous latent dynamics, whose transitions are all functions of the system input and previous states parameterized by neural nets. The emission model is likewise parameterized by an NN, while the latent state inference is performed by a Transformer that pools across regions (after local embeddings). Training is done via maximizing ELBO. The authors apply their method to 3 simulated systems, finding good performance compared to ground-truth latents and interpretable flow fields and inter-areal messages. Furthermore, the proposed method is benchmarked against a variety of previous single/multi-region switching/non-switching (non-)linear methods on two real datasets, with best performance on the co-smoothing metric. Lastly, they demonstrate how the method can be used to gain dataset-specific neuroscientific insights.

### Strengths
The proposed method is a technical tour-de-force, and represents a generalization of many existing algorithms (e.g., MR-SLDS). The 3 simulation experiments are quite nice, and demonstrate the variety of systems for which this method may be applicable, even in the case of a mismatched model (i.e., the multiregion RNN model). The benchmark experiments against existing methods is also appreciated. The paper is clearly and concisely written for the most part, especially the introductory pages and explanation of the method, though one gets the feeling that the authors ran out of time (or space) for the results half of the paper, and there are some “rough edges” throughout. Overall, it seems like a promising and well-developed method with somewhat natural assumptions for modeling multi-region interactions in the brain.

### Weaknesses
I have two main concerns, which I will outline in brief here, with specific comments/questions in the next section:

First, the method is powerful by design, leveraging multiple nonlinear DS per region. However, the flexibility comes with a series of issues, most prominently the choice of hyperparameter values, such as the dimensionality of the system and, critically, the number of switching states. In the simulation experiments, if I understand correctly, the model was given the ground-truth number of states, but how would the inferred systems look like when starting with a different number (e.g., for the switching Lotka-Volterra system)? This is further an issue with the real neural data, where one does not have access to the ground-truth, and it’s arguable whether there is such a number. The lack of robustness to the number of switching states is a significant concern, as it could lead to drastically different interpretations of the underlying dynamics. For instance, if the model overfits by using too many states, it might capture noise instead of meaningful transitions. Conversely, if it underfits with too few states, it might miss crucial dynamic patterns, leading to an incomplete or inaccurate understanding of the system.

Second, is that the applications to real data is somewhat unconvincing for me, both in terms of the assumptions one makes regarding model architecture and hyperparameter values (related to above) and what actual insight was gained. Given the technical contribution in the method, I don’t think the authors should necessarily be penalized for attempting to apply it on real data. Nevertheless, I feel that the main claims regarding neuroscientific insight was not sufficiently evidenced. The interpretation of the inferred dynamics, especially in the real data, is unclear. The flow fields appear overly simplistic, and it's not evident how these relate to actual neural activity. The lack of clear, interpretable results from the real data undermines the practical utility of the method in a neuroscientific context. The claims of neuroscientific insight are not well-supported by the presented results, raising questions about the method's applicability beyond simulated scenarios.

### Questions
- a major question is whether the existing results are robust to different choices of the number of switching states, latent dims, etc., especially in the simulation experiments but using an incorrect number, as well as how do results change when applied to experimental data. I leave up to the authors to decide how best to demonstrate this, but in general, for a practicing neuroscientist using such a method, I would expect somewhat robust/consistent results independent of hyperparam choices.
- The inferred systems from the real data (Figures 3 & 4) don’t look that great, and I’m generally not sure what I’m suppose to get from them in general. First, in Figure 3B, the flow fields in state all look like linear 1D flows. Is this meaningful? Could this not have been combined with the first state? Or what happens if one uses a larger number of states, are all the ones after state 1 simple linear-ish flows? And how would one interpret this either way?
- In general, the figures could use a bit more explanation, e.g., what are the main occupied states? Why is the same trajectory plotted in both states but different portions are highlighted in blue in 3B? How exactly should someone interpret 3C / 4D? Various plots don’t have labeled axes (e.g., 3D, 4B/C), I guess that’s time in ms?
- one assumption the model makes is that communication across regions are in the form of the latent variable, while in the brain this happens concretely and literally via spikes, which is more akin to the observed signal in this model (though here it’s calcium signals). How is the original assumption valid given this?
- in practice, how does one decide on the various hyperparameter values, such as the number of latent dimensions, switching states, etc.?
- Some more discussion regarding whether there is an advantage to using multiple discrete nonlinear DS instead of one bigger / flexible one is warranted. In particular, is the switching timescale realistic considering neurobiology, and what would the switching states represent?
- I’m not sure what to make of the comparison to PCA in the high-D RNN experiment: the inferred flow field look quite similar, and if anything the PCA one looks cleaner. Maybe some further expansion on what we should be looking for would be helpful? (Also what are the markers?)
- some small typos and such: page 6 line 2, “Figure 2a” should be 2c; line directly above figure 2 is a runaway latex comment; page 8 section 4.6 “Figure 5 shows a macro…” should be Figure 3; Supplemental text refers to Figure AX while the numbers continue from the main figures; Figure 3D missing caption label, and what is the dark brown suppose to be? Fixing these (and the figure issues above) would lift the overall quality of the paper.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method for modeling interactions between brain regions in the context of a collection of nonlinear state space models. It aims to describe the neural dynamics both internal to a brain region and between regions. The authors provide plentiful comparisons to other similar methods, applied mostly to decision-making paradigms in neuroscience.

### Strengths
The intuition underlying the method is well described, and the math is clearly laid out. Quantifying the messages between regions in a nice addition beyond existing methods. 

The method does outperform other (very similar) methods in the datasets tested here.

### Weaknesses
Some clarifications of the use cases / benefits of the method would be helpful. For instance why is 'switching dynamics enables modeling the dynamics in low-dimensional space using more persistent discrete states' a benefit? A clearer description of the goal is needed.
Overall the discussion was weak and read as a series of unjustified statements. 

Some of the figures (e.g. Figure 5 B) were very low resolution, unlike other areas of the same figure. The caption would also be improved by defining terms ('accum' is different than 'accumulator'?, 'msgs'). Figure 5 has no C label. 
Figures don't appear to be consistently formatted and the text is often too small to read. (except Figure 1, which is well done and easily understood even without a caption).

The authors appear to have left in a note: 'MAKE SURE to say here that we also include in appendix A1 a result without the external input and show that we can still do inference but can’t generate'. (Why can't it generate?)

Could the authors comment on 'mr-rSLDS models required 10 latent dimensions per region (vs 3) to achieve comparable performance on the mesoscope dataset' and why more latent dimensions per region is a downside? Is it just about the computational load? Or is it important to model the latent dimensions with e.g. 3 dimensions because the brain itself 'uses' fewer than e.g. 10 dimensions? There is some trade off between summarization (fewer dimensions) and models that are structured more similarly to the higher-dimensional neural dynamics (more biological comparisons?). 

Would this method be able to discern the number of interacting brain regions? Rather than take the regions are proscribed (3 regions, 16/8 regions in the experimental datasets).

### Questions
The authors appear to have left in a note: 'MAKE SURE to say here that we also include in appendix A1 a result without the external input and show that we can still do inference but can’t generate'. (Why can't it generate?)

Could the authors comment on 'mr-rSLDS models required 10 latent dimensions per region (vs 3) to achieve comparable performance on the mesoscope dataset' and why more latent dimensions per region is a downside? Is it just about the computational load? Or is it important to model the latent dimensions with e.g. 3 dimensions because the brain itself 'uses' fewer than e.g. 10 dimensions? There is some trade off between summarization (fewer dimensions) and models that are structured more similarly to the higher-dimensional neural dynamics (more biological comparisons?). 

Would this method be able to discern the number of interacting brain regions? Rather than take the regions are proscribed (3 regions, 16/8 regions in the experimental datasets).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a switching nonlinear state space model to capture the nonlinear pattern in multi-region neural dynamics. The authors use a deep neural network-based approach, where they amortize the cost of inference by learning an inference neural network (Transformer in this paper), which predicts the mean and variance of the latent dynamics. In the experiments, they compare the proposed method with PCA and some widely used state space models in the neuroscience community by evaluating the prediction performances. They also apply the proposed method to multi-region calcium imaging data to explore the communication streams between regions.

### Strengths
Propose a switching nonlinear dynamics system by using the powerful expression of deep neural networks.

### Weaknesses
 * The experiment part needs clarification. Section 4.2 simulates a multi-region decision-making task, but there is no comparison of MR-SDS with other methods such as LDS, SLDS, and rSLDS. Besides, the author mentions their method, MR-SDS, is able to learn the nonlinear dynamics in this complex case, but there needs to be a figure to visualize such latent dynamics. Similarly, section 4.3 simulates a multi-region system with three interacting and high-dimensional RNNs, but there needs to be a figure to support their claim. The lack of visualizations makes it difficult to assess the claims about capturing complex dynamics.

* The comparisons with LDS, SLDS, and rSLDS are not enough. This paper only compares their prediction/reconstruction performance on calcium imaging data. It would be better to show the proposed method, MR-SDS, could capture more meaningful latent dynamics than other commonly used models, which may be more important than prediction performances in terms of neuroscience research. For example, could you provide some cases where MR-SDS captures some nonlinearity in the neural recordings while rSLDS cannot? The current comparisons do not sufficiently demonstrate the specific advantages of MR-SDS in uncovering underlying neural mechanisms.

* No standard deviation (variance) in Table 1. The absence of variance makes it hard to evaluate the robustness of the results and determine if the observed differences are statistically significant.

*  Many typos and wrong figure index/reference. E.g., in section 4.1 and the second line of page 6, it should be "Figure 2(c) shows ....". In section 4.1, there is no reference to Figure 2(d), etc. These errors detract from the paper's credibility and make it harder to follow the arguments.

### Questions
* Could SLDS / rSLDS give similar latent dynamics and message communications in Lokta-Voterra simulated data, mesoscope, and widefield calcium imaging data? Although SLDS is a linear model, it could capture the nonlinearity in latent space.

* Are there any insights as to why you choose Transformer instead of some simpler and faster deep neural networks like RNNs?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed the multi-region switching nonlinear state space model (MR-SDS) for learning state switching and nonlinear evolution of continuous latent with multi-region interactions setup. The inference algorithm uses the forward-backward algorithm to learn the latent state, and a transformer encoder as the variational distribution to infer the continuous latent. Experiments show that the proposed MR-SDS is able to learn the model parameter and then infer the nonlinear latent and predict future data. Besides, the volume of messages passing between different regions can be understood by such a model.

### Strengths
* The maths explaining the model is clear to me, with an intuitive schematic for the generative process.
* The model is able to capture the nonlinear evolution of the latent process $x_t$.

### Weaknesses
 * The -2th line of page 3, $f_z^{kk}$ should be $f_{kk}^z$
* Then main weaknesses is the mismatches between texts and figures:
    * We know Fig. 1 is a summary of the whole generative model, but it is informal to not mention it in the main text.
    * Page 6, 2nd line should be Figure 2(c).
    * Page 6, 3-5 lines and Figure 2. Where is the $R$ and $u$ in Figure 2.
    * Figure 2(b), what is true, what is the dashed curve? There is no clear legend.
    * Other mismatches in Figure 2, and etc.
* No "." in the last sentence of section 4.1.
* I think forward Euler is not appropriate for generating the data. Although I don't understand different curves in Figure 2(b), I can see the numerical error amplifies significantly because of forward Euler. The use of a simple forward Euler method for simulating the Lotka-Volterra system introduces significant numerical instability, especially with larger time steps. This is evident in the unrealistic trajectories shown in Figure 2(b), where the numerical error accumulates, leading to divergence from the true solution. This choice of integration method undermines the validity of the simulation results.
* Why only one state switch is allowed in experiment 4.1 and has to be within 40-60? This generating process is too simple and not complicated enough to validate the model. The restriction to a single state switch within a narrow time window (40-60) in experiment 4.1 significantly limits the complexity of the simulated data. This oversimplification does not adequately test the model's ability to handle more realistic scenarios with multiple switches and varying switch timings. The model's performance in this limited setting may not generalize to more complex datasets.
* Overall, too many errors in this paper. I cannot understand most of the experiments since wrong text-figure assignments, no legend, etc.

### Questions
* Why ‘posterior collapse’ is enclosed single quotes, and also others.
* What about other methods for section 4.1 and 4.2? Is that other methods in Table 1 not applicable to experiment 4.1 and 4.2? For, example, the generative model of the Lokta-Voterra model is nonlinear. Authors show that MR-SDS is able to capture the nonlinear evolution of the then latent process $x_t$. But for SLDS, for example, $x_{t+1} \sim \mathcal N(Ax_t,\Sigma)$. It seems like $Ax_t$ is a linear process, but there is a Gaussian distribution, so it is actually a nonlinear model. No matter how we define "linear/nonlinear", why not test whether SLDS can learn the Lokta-Voterra latent?
* Is Table 1 the held-out likelihood? Where is the variance? Are the likelihood of MR-SDS significantly better than others? Is it likelihood, or log-likelihood?
* I cannot see the significant benefits of the proposed model than others, in terms of both prediction on future data and latent estimation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
