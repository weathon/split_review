# Equivariant Graph Neural Operator for Modeling 3D Dynamics

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
\looseness=-1
Modeling the complex three-dimensional (3D) dynamics of relational systems is an important problem in the natural sciences, with applications ranging from molecular simulations to particle mechanics. Machine learning methods have achieved good success by learning graph neural networks to model spatial interactions. However, these approaches do not faithfully capture temporal correlations since they only model next-step predictions. In this work, we propose Equivariant Graph Neural Operator (\method), a novel and principled method that directly models dynamics as trajectories instead of just next-step prediction. Different from existing methods, \method explicitly learns the temporal evolution of 3D dynamics where we formulate the dynamics as a function over time and learn neural operators to approximate it. To capture the temporal correlations while keeping the intrinsic SE(3)-equivariance, we develop equivariant temporal convolutions parameterized in the Fourier space and build \method by stacking the Fourier layers over equivariant networks. \method is the first operator learning framework that is capable of modeling solution dynamics functions over time while retaining 3D equivariance. Comprehensive experiments in multiple domains, including particle simulations, human motion capture, and molecular dynamics, demonstrate the significantly superior performance of \method against existing methods, thanks to the equivariant temporal modeling.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to learn SE(3) equivariant discretization invariant dynamics on graphs. To do this, the authors learn a Fourier neural operator (FNO) to predict future states from the current state. Differently from previous approaches, here, future states are determined by a time window (making it a function space), rather than a fixed dt. To constrain the dynamics to be equivariant to SE(3) transformations, the authors use a modified version of the FNO layer.

### Strengths
*Originality:* The work appears original. 
- The literature review appears comprehensive
- The work seems to address a gap in the literature

*Quality:* The work is of good quality. 
- The claims are validated either theoretically or empirically. 
- In the many experiments presented, the proposed work outperforms baselines
- The ablation studies show the utility of each component of the approach
- The empirical analysis studies the effect of varying I and P and finds results consistent with expectations

*Clarity:* 
- The work is clearly written and organized.

*Significance:* The work appears significant. 
- As far as I know this work is the first to consider temporal windows as function spaces on which to apply neural operators.

### Weaknesses
While the paper presents a novel approach, there are a few areas that could benefit from further clarification. Specifically, the definition and implementation of $M_\theta$ as a complex tensor warrants a more detailed discussion. The paper mentions that $M_\theta$ is a complex tensor. However, it does not elaborate on how this is represented and handled in the actual implementation. A clearer explanation of the computational implications of using a complex tensor would be beneficial. For instance, how does the use of complex numbers affect the computational performance compared to using real-valued tensors? Are there any specific optimizations or considerations that need to be taken into account when working with complex tensors in this context?

### Questions
In the paper, $M_\theta$ is defined as a complex tensor, is this reflected in the implementation? How does that impact computational performance?

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
The proposed method addresses the limitations of autoregressive models for dynamical systems particularly in settings where graph representations are well motivated with Fourier neural operators. In this setting, roto-translational equivariance is typically incorporated in the graph neural network-based models. This work introduces a temporal convolutional filter that computes the Discrete Fourier transformation while maintaining equivariance to the roto-translational group. This enables the model to combine the strengths of the equivariance graph neural networks and the Fourier neural operators approaches. 

The delivered neural operators can produce the evolution of the dynamics of the system (in contrast to the next time step) and they can operate independently of the temporal discretization. 

The authors claim that training over temporal dynamics rather than one-step prediction also allows them to achieve superior performance with respect to the MSE on the predictions as well as improvement with respect to the amount of training data required to train the model.

### Strengths
The idea of extending equivariant graph neural networks for dynamical systems with neural operators is well-motivated and has clear value. 

Theoretically, the paper is well presented. The empirical analysis is very well designed with enough breadth and the results support the proposed claims.

### Weaknesses
I have one aspect of the paper that I cannot fully understand and I think the presentation can be improved to benefit a broader set of audience.

The implementation of the method includes the following steps:
- The graph G(t) is repeated P times
- Followed by time embedding of the various length \delta t
- Then a discrete Fourier transformation follows this.

I think the paper can benefit from a more detailed motivation of these steps. 

I follow up with specific questions bellow.

1. What is the role of multiplying the state G(t) of the system?
2. I am not sure how the model does the DFT on a single time set from the input sequence. Can you please explain this?
3. Is this model also able to operate on an input sequence rather than only on one-time step G(t)?
4. Why is there a need to embed the \delta t and how is this implemented in the model?

### Questions
1. What is the role of multiplying the state G(t) of the system?
2. I am not sure how the model does the DFT on a single time set from the input sequence. Can you please explain this?
3. Is this model also able to operate on an input sequence rather than only on one-time step G(t)?
4. Why is there a need to embed the \delta t and how is this implemented in the model?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes equivariant temporal convolutions in the Fourier space to capture temporal correlations, which can be observed in complex three-dimensional dynamics. The experimental results show that the method outperforms other equivariant models, such as Tensor Field Networks [Thomas+ 2018], SE(3)-Transformers [Fuchs+ 202], and E(n)-GNN [Satorras+ 2021].

### Strengths
* The paper incorporates E(n)-equivariance into Fourier transformation, which is a solid mathematical tool to express temporal dynamics.
* The method is general enough to be compatible with an arbitrary E(n)-equivariant graph neural network.
* The experimental results show that the proposed approach has a significant advantage over other models in tasks of various fields, such as an n-body system, motion capture, and molecular dynamics.
* The paper is well-written enough to understand the methodology and background of the work easily.

### Weaknesses
 * The method seems to have a strong relation with the temporal bundling proposed in [Brandstetter+, ICLR 2022] in terms of predicting several time steps with one forward computation. Therefore, the reviewer strongly recommends the authors implement the temporal bundling and compare it with the proposed Fourier-based approach to show the superiority. Specifically, a direct comparison is needed to quantify the performance differences, in terms of both accuracy and computational cost, between the proposed method and a temporal bundling approach. This comparison should be performed across the same set of datasets and experimental conditions to ensure a fair evaluation.
* The ablation study indicates that two modes are sufficient to perform well on the n-body and mocap-run datasets. However, the advantage of Fourier transformation could be to capture complex temporal dynamics. Therefore, the reviewer suspects that the datasets are too simple to demonstrate the superiority of the method. It is unclear if the datasets used truly require the power of a Fourier-based approach, which could be better suited to more complex systems with a wider range of frequencies. A more detailed analysis of the frequency content of the datasets and how well the proposed method captures these frequencies is needed. The current results do not sufficiently justify the use of the Fourier transform over simpler temporal modeling methods.

Minor points:
* By comparing values, the reviewer guesses Table 3 corresponds to |Train| = 3000 case, but this should be clarified in the caption.

### Questions
* The paper states that the authors use fast Fourier transformation (FFT). In my understanding, the length of the time series should be 2^n (n: positive integer) to use FFT, while Table 3 says that they tested time series 2, 5, and 10. How is it possible?
* The experimental conditions are not described in detail enough. P and I are hyperparameters, but the reviewer could not determine the values used for each experiment. Sometimes, one of two parameters is specified, but not two. Thus, could authors clarify these parameters?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method called Equivariant Graph Neural Operator (EGNO) to directly model dynamics as trajectories instead of just as next-step prediction. To capture the temporal correlations while keeping the intrinsic SE(3)-equivariance, they develop equivariant temporal convolutions parameterized in the Fourier space. Empirical experimental results in multiple domains are provided to support the effectiveness of EGNO.

### Strengths
* The paper proposes an effective strategy to capture the temporal correlation along the dynamic trajectory, which results in better prediction accuracy.
* The operator formulation enables efficient parallel decoding of future states within a time window with just one model inference.
* The paper is well-organized and easy to follow.

### Weaknesses
 * EGNO can be regarded as an extension or application of Fourier operator learning in modeling 3D dynamics. This fact may limit the technical novelty of the paper. Can the authors elaborate on the specific contributions of EGNO beyond the established works in these two fields?
* Some recent related works on N-body simulation tasks, such as GCPNet [1] and ClofNet [2], have not been mentioned or used as baselines in this paper. It would be beneficial to address these works and their relevance to the current research.

### Questions
* When it comes to modeling dynamics as a trajectory, another viable approach is to employ neural ODEs as a surrogate for modeling the gradient field between two states. This method can also capture temporal correlation by explicitly reparameterizing an ODE. I noticed that ClofNet utilizes this paradigm to investigate the interpolation and extrapolation capacity of equivariant networks in predicting dynamic trajectories. How does this strategy compare to Fourier operator learning?
* The metrics used for motion capture and molecular dynamics tasks have not been clearly explained. Please provide additional clarification to ensure a better understanding of these aspects.
* The technical details of time embedding have not been thoroughly clarified. It would be helpful to provide more comprehensive explanations.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
