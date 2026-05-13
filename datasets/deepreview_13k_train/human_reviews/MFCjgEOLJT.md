# Learning interpretable control inputs and dynamics underlying animal locomotion

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
A central objective in neuroscience is to understand how the brain orchestrates movement. Recent advances in automated tracking technologies have made it possible to document behavior with unprecedented temporal resolution and scale, generating rich datasets which can be exploited to gain insights into the neural control of movement. One common approach is to identify stereotypical motor primitives using cluster analysis. However, this categorical description can limit our ability to model the effect of more continuous control schemes. Here we take a control theoretic approach to behavioral modeling and argue that movements can be understood as the output of a controlled dynamical system. Previously, models of movement dynamics, trained solely on behavioral data, have been effective in reproducing observed features of neural activity. These models addressed specific scenarios where animals were trained to execute particular movements upon receiving a prompt. In this study, we extend this approach to analyze the full natural locomotor repertoire of an animal: the zebrafish larva. Our findings demonstrate that this repertoire can be effectively generated through a sparse control signal driving a latent Recurrent Neural Network (RNN). Our model's learned latent space preserves key kinematic features and disentangles different categories of movements. To further interpret the latent dynamics, we used balanced model reduction to yield a simplified model. Collectively, our methods serve as a case study for interpretable system identification, and offer a novel framework for understanding neural activity in relation to movement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper uses an unsupervised method of discovering latent control signals from behavioural sequences, to discover behavioural motifs. The main methodological contribution is using a model reduction technique to gain interpretability insights into the inferred models. Overall I think this is a good paper.

### Strengths
This paper analyses various behavioural sequences and infers intuitive behavioural motifs.

While the core method is not new, the interpretability aspect is, and the insights are interesting.

The paper is well written, and clearly presented.

### Weaknesses
The paper could do with a proper model comparison, i.e. vs moseq. Specifically, the authors should quantitatively compare the performance of their method against MoSeq in terms of segmentation accuracy and the ability to reconstruct behavioral sequences. A direct comparison of the latent control signals and their interpretability would also strengthen the paper's claims.

The Balanced truncation bit needs to be better explained with some intuition. While the mathematical formulation is presented, the paper lacks a clear explanation of how the Hankel singular values relate to the system's dynamics and how their magnitude informs the model reduction process. Providing a more intuitive understanding of how balancing transformations are derived and how they relate to observability and controllability would significantly improve the paper's accessibility.

Eqn 5 should have $ \tilde{W}_o = \tilde{W}_c = \dots$. This is a crucial detail for the correctness of the balanced truncation method.

Fig 1 A: what does blue and orange correspond to? Different sequences? Different input/output channels? This needs to be clarified in the caption for better understanding.

Some of the Figures seem to be mis-referenced, e.g., “As shown in Figure 3B, the MGU could reconstruct bouts using a sparser control compared to the LDS. " This specific example should be carefully checked, and the authors should ensure all figure references are accurate throughout the manuscript.

All the figures could do with more explanations in their captions. For instance, providing details on the specific parameters used for each model in the figures, the meaning of different colors or line styles, and a brief interpretation of the results shown would make the figures much more informative.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a framework to identify the latent control signals and the underlying dynamics that make up the natural behavior of zebrafish. It utilizes iLQR-VAE for learning the parameters and inferring the control signals. The paper trained recurrent neural network (RNN) models and linear dynamical systems (LDS) to reproduce the postural sequence with sparse control signals. The underlying dynamics of those models are explored and how they relate to the behaviors is studied. The paper further demonstrates the model order reduction on the LDS model and relates the reduced mode to the observed behaviors.

### Strengths
The paper looks at a new approach for studying naturalistic behaviors, and defines the problem in a clear way.

The model reduction on the LDS model gives new insights into modeling behavior.

### Weaknesses
The paper utilizes iLQR-VAE for learning the parameters and inferring the control signals. It would be helpful if the authors stated clearly in the text what is the difference between the proposed model and the previous model. It seems like the differences are minimal if any, in which case, this is a good application paper, however, it doesn't introduce many novel elements from a modeling perspective. While the model reduction technique for linear models is not usually applied to this field of behavioral modeling, it is a very well-known concept and does not offer novelty from a methodological perspective. There are interesting takeaways from a neuroscience perspective, but these would have to be validated more thoroughly and may be more suitable for a different venue.

The kinematics of the zebrafish are somewhat simple; however, the naturalistic behaviors of other animals (mice and monkeys, for example) are much more complex. Will the model still be able to capture these dynamics? One real-world dataset may not be able to provide enough insight about the generalizability of the model for this question.

There is no comparison with other models presented.


Minor:
1. Section 4.1, mismatched figure labels. Figure 1C->Figure 1B; Figure 1D -> Figure 1C
2. Figure 3 Caption: missing space: ‘udriving’ -> ‘u driving’
3. More explanations on Figure 3D in the main text.
4. Page 15: ‘all states withing the LDS’ -> ‘all states within the LDS’
5. Page 15: ‘cannot be reach via observations’ -> ‘cannot be reached via observations’
6. Page 16: ‘Therefore, we can the compute the’ -> ‘Therefore, we can compute the’

### Questions
Please see above weaknesses.

### Soundness
3 good

### Presentation
3 good

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
In this paper the authors propose a control framework for estimating movement dynamics from behavioural/postural observations. Movements are considered as generated by an unknown dynamical system controlled through sparse input signals.
They employ two alternative methods to fit the latent dynamics: 
- One that uses the iLQR-VAE from Schimel et al., 2022 that approximates the observed dynamical system through an RNN.
- And a linear model of “large dimensionality” that is consequently reduced to a lower dimensional model using balanced truncation.
They demonstrate their method on a toy example of a linearly approximated system comprising two pendulums, and on a behavioural dataset of zerbafish movements. 
They are able to further provide insights into the identified dynamics by dissecting the spectrum of the reduced linear model.

### Strengths
- Applying balanced model reduction together with dynamical and control inference is an interesting contribution to the existing system identification literature.
- The linear approximation through the model reduction allows for interesting insights into the approximated dynamics (like in Figure 4 for analysing the eigenmodes active during different movements), that would be otherwise more cumbersome to perform for an RNN.

### Weaknesses
 - The dissection of the identified dynamics through the reduced linear model requires the non-reduced linear system to already approximate accurately the observed system. I wonder whether the authors could provide a systematic analysis on the robustness of their framework when fit on the nonlinear toy model. Specifically, it's unclear how the accuracy of the reduced linear model's insights degrades as the non-linear dynamics deviate further from the initial linear approximation used to generate the data. A more rigorous approach would involve varying the parameters of the nonlinear system to explore the limits of the linear approximation and its impact on the reduced model's interpretability.
- As the authors already mention in their discussion, the framework they propose requires the fitting of two dynamical systems: an RNN that captures accurately the observed behavioural trajectories, and a linear system that provides interpretability. This dual-model approach introduces additional complexity and potential for error propagation. The dependence on an accurate initial RNN fit is a significant bottleneck, as any inaccuracies in the RNN will propagate to the subsequent linear approximation and model reduction steps. It would be beneficial to explore methods that allow for a more direct estimation of interpretable dynamics, rather than relying on this two-step process.

### Questions
- In the toy example with the pendulum, as I understand, the authors created observations by simulating the linear approximation of the system (assuming small angles). I wonder how  the proposed framework would perform if the authors created the observations for the same system parameters with the nonlinear dynamics, and for parameter sets that result in increasingly larger angles. I think in this toy example it is interesting to demonstrate the robustness of the linear-reduced order framework.

- In Figure 3 why does the classification accuracy decrease with time (observation time?)?

- In Figure 4C and associated main text, the authors mention that the reduced model added eigenmodes with larger timescales, while it neglected the small timescale modes of the the non-reduced system. While the second part of the previous sentence is expected, I am not sure how should I understand the first one. Can you provide some intuition. Also related to this, when I first looked at Figure 4C I thought that the large the large time scale values of the reduced and non-reduced model overlap, therefore the light grey ones are not visible. Can you probably make the circles of the reduced system non-opaque or non-filled to make the plot clearer?

- I think it would be helpful if the authors mention in the supplement how they fit the linear model of their framework, and provide a brief description of the iLQR-VAE framework that is a crucial component of the proposed approach.

- Model Selection C.1. section is missing from the supplement.

- There is a typo in the subscripts in Eq. 5.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript provides a framework for modeling the behavior of the larval zebrafish using a control theoretic and dynamical systems framework. They model the behavior of a system as arising from a dynamical system driven by sparse inputs with a students-t distributed prior. They assume behavior is generated from the dynamical system by either a linear or RNN model, and use iQLR-VAE to infer model parameters and the sparse inputs. In each case they use a model truncation approach to reduce the number of dimensions considered. They begin by validating the approach on a double pendulum oscillator system, showing they could reproduce the number and values of eigenvalues. Then they analyze a dataset of larval zebrafish behavior, which is organized into discrete bouts and thus a natural test case for this approach. They find they need high capacity models (120 latent dimensions, 10 control inputs) to fit the behavior. They show that the resulting representation is useful, in that the dynamical representations provides a more disentangled input that can be better decoded from the top 5 PCs compared to the postural representation or even the full time series in some cases. By using model reduction, they show the dynamics underlying behavior can be decomposed  into separate modes.

### Strengths
* The formulation is well described and I believe novel, and an addition to other methods fitting dynamical systems to neural and muscular systems, but here in the case of sparsely driven behavior. 

* The result about better disentangling of behavior is interesting, and the spatial decoding result as well. 

* The model reduction approach to achieve small models is interesting.

### Weaknesses
 * There is a lack of benchmarks comparisons to other techniques in the literature such as LFADs. Even though some suggest continuous inputs for their control scheme, could they be used to model the behavioral dynamics in Figure 3C for instance. 

* I found the applications a bit limited. It wasn’t obvious from this analysis that there were fundamentally new types of experiments that were enabled by this approach. 

* Overall, I think the lack of benchmarks combined with the lack of novel applications was a major sticking point for me and I view this manuscript as very borderline. I would be happy to reconsider the manuscript (which was very well written) if these were added or addressed. I see this as just 1 compelling figure short of a reasonable submission.

* There is no ground truth in behavior for the driving inputs and thus there is no way to validate that they are correct, however with an appropriate experiment (e.g. applying a perturbation or stimulus at a specific time) perhaps they could be useful. 

* Generally, more concretely linking any of the observations to real neural or behavioral variables would improve the manuscript's impact.

### Questions
* Does the number of control inputs match the number of bout types people have reported in the literature? 

* There is no ground truth in behavior for the driving inputs and thus there is no way to validate that they are correct, however with an appropriate experiment (e.g. applying a perturbation or stimulus at a specific time) perhaps they could be useful. 

* Generally, more concretely linking any of the observations to real neural or behavioral variables would improve the manuscript's impact.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
