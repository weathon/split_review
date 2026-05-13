# Efficient Dynamics Modeling in Interactive Environments with Koopman Theory

- Decision: Accept
- Scores: 3, 6, 5, 8

## Abstract
The accurate modeling of dynamics in interactive environments is critical for successful long-range prediction. Such a capability could advance Reinforcement Learning (RL) and Planning algorithms, but achieving it is challenging. Inaccuracies in model estimates can compound, resulting in increased errors over long horizons.
We approach this problem from the lens of Koopman theory, where the nonlinear dynamics of the environment can be linearized in a high-dimensional latent space. This allows us to efficiently parallelize the sequential problem of long-range prediction using convolution while accounting for the agent's action at every time step.
Our approach also enables stability analysis and better control over gradients through time. Taken together, these advantages result in significant improvement over the existing approaches, both in the efficiency and the accuracy of modeling dynamics over extended horizons. We also show that this model can be easily incorporated into dynamics modeling for model-based planning and model-free RL and report promising experimental results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an approach based on Koopman theory, which linearizes the nonlinear dynamics of the environment in a high-dimensional latent space for long term prediction. This allows for efficient parallelization of the sequential problem of long-range prediction using convolution, while considering the agent's actions at each time step. The approach also enables stability analysis and better control over gradients through time, resulting in significant improvements in efficiency and accuracy of modeling dynamics over extended horizons.

### Strengths
The strengths are as follows:
1) They provide extensive experimental results verifying the claims made in the better and showing better long term prediction accuracy that other recent non-Koopman NN based methods.

2) They provide numerical simulations that they Koopman based approach does not lead of instability. In other words, they show that their long term predictions do not blow up.

### Weaknesses
The weakness of the paper are as follows:

1) I've had the opportunity to delve into Koopman operator theory in my past research. It's noted that control-affine systems transform to a bilinear control Koopman based system in the lifted space under particular conditions, as exemplified by Theorem II.1 in the paper titled "Advantages of Bilinear Koopman Realizations for the Modeling and Control of Systems with Unknown Dynamics". It's also worth mentioning that these bilinear forms may not be universally applicable to all nonlinear systems, especially those that do not adopt the control affine form. Some recent works on Koopman operator theory have also showcased how a control-affine nonlinear system can be transitioned to a more generalized input-separable Koopman system, with bilinear and linear forms being special instances of these separable Koopman formats.

2) There are alternative NN methods, such as Neural ODE, that have consistently demonstrated promising results for long horizon predictions, in my experience. It might be valuable to consider or reference them in the context of this paper.

3) The problem of long horizon prediction for both controlled and non-controlled dynamical systems using Koopman operator has been explored before, please see the Nature publication titled "Deep learning for universal linear embeddings of nonlinear dynamics", and in subsequent studies.  I am aware that you already cited this reference but “twice” (please check)

4) While controlled systems are a primary focus in this paper, an additional section dedicated to control design could potentially improve the paper further.

5) On the topic of stability in Koopman-based learned matrices, there are several contributions, such as "Learning Stable Koopman Embeddings", and its subsequent related studies. It might be advantageous to discuss or incorporate the stability guarantees they present in the context of this paper.

6) Considering the above, a more comprehensive literature review on the Koopman operator for controlled/non-controlled dynamical systems might enhance the paper's breadth.

7) For the purpose of replication and validation, making the code available as open-source (while preserving the authors' anonymity) could be beneficial for the broader community.

### Questions
1) It would be interesting to see the results with NeuralODE

2) Please do a more thorough literature review on Koopman operator theory for control and modelling.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a diagonal Koopman-operator approach that helps to efficiently learn and quickly plan with dynamic models. The standard encoder used in Koopman-operator-based approaches is modified to output the complex eigenvectors of the latent linear model, whose estimation is then reduced to learning a diagonal matrix (together with the encoder/decoder weights). By careful initialization of the complex eigenvalues of the Koopman-matrix the authors can also protect against vanishing/exploding gradients. The diagonalization helps quite significantly to reduce the computation time needed for planning over long horizons, as the authors show in several dynamics-estimation and RL based tasks. The method also works competitively with several state-of-the-art approaches in dynamics modeling and RL applications.

### Strengths
The approach as far as I can tell is sound, and as the summary above indicates, the authors show significant improvement in terms of computation time / backpropagation stability that results from the diagonalization and the careful initialization. The method is also tested in several benchmark problems (RL and dynamics modeling) and the ablation studies in the appendix look comprehensive to me.

### Weaknesses
Sometimes the discussions in the paper are not very clear, for instance

* "While the same dynamics model can also be used for (III) model-based RL, we leave that direction for future work."
> Do you mean you would improve the model K further? or g_theta perhaps?

* Can your approach fail even if eigenvalues are initialized well? After correct initialization, will the real part of the eigenvalues always stay negative? Are there any other failure scenarios?

* "we apply our dynamics model in model-free RL, "
> What does it mean to apply a model in the model-free setting? Please explain not just in the appendix but also in the main text briefly. In general much of the discussion in the Appendix could be streamlined with the text. Please organize the appendix and reduce its scope, code should be put in github and linked, no need for printing your code in the appendix. Instead you could mention more failure cases as part of the ablation studies perhaps.

* Would be nice to have figures or a section explaining *what* you're solving, rather than how, e.g. inputs are in the pixel space, encoder is an MLP and the TD-MPC tries to solve X ... So some part of Section E from the appendix could go to the main text.

* It is not clear to me which network architecture you used for the encoder g_{\theta}, is it another MLP?

### Questions
* This is not a problem only concerning this work but in general applies to all 'Koopman-operator-inspired-approaches': the connection to the theory is very very loose and hence these methods could instead be simply called linear latent-dynamics modelling. Do you agree? If not, please mention how the Koopman-operator theory guides you analytically and intuitively. 

* As a follow-up to the above: how does the encoder quality effect your results? How do you come up with the encoder structure? Can the theory guide you here?

* In the optimized Koopman matrix, are the eigenvalues sparse, or are they all nonzero/complex ? Can they be made sparse and is that interesting? 

* Please mention the limitation to deterministic environments in the introduction. Is this a limitation that all Koopman-operator approaches in the literature face?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new method for learning a Koopman embedding that gives decoupled linear dynamics in a latent space, opposed to nonlinear dynamics in the state space. This approach is also able to specify the eigenvalue spread of the resulting linear dynamics, stabilizing gradient evaluations through long chains.

### Strengths
1. There are many papers that propose using neural networks to find a Koopman embedding, this one is unique (to my knowledge) because it focuses on stabilizing the eigenvalues of the latent-space dynamics. 
2. The included JAX code is very helpful for comparing the implementation to algorithm for a better understanding of what's going on. 
3. The Koopman background section is clear and does a good job of defining all of the notation. 
4. The argument for why a Koopman model is easier to parallelize over RNN's like GRU and LSTM is a great addition to the algorithm.  
5. This approach was shown on a wide variety of robotics tasks from the DeepMind control suite (Ball in cup catch, cartpole, swingup, cheetah run, finger spin, and walker walk).

### Weaknesses
1. Figure 3 seems to undermine the utility of the presented Koopman approach, since the GRU is able to compete with it on all of the examples and metrics. Maybe some explanation in the figure caption explaining why this is expected would be appreciated. 
2. Longer/better figure captions would be nice. 
3. This seems like a marginal improvement over existing works cited. Some more comparisons between this approach and existing algorithms could better showcase the additions.

### Questions
N/A.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new state-space model for dynamical systems modelling based on the Koopman operator. The authors approximate the Koopman operator in such a way that they can leverage time convolution operators and compute multiple-step predictions without resorting to autoregressive filtering. This seems to reduce training time and improve learning algorithm stability. This is because the gradient growth can be directly controlled due to the structure of the proposed model. The authors also show that replacing a native model in some model-based algorithms with the proposed one improves the algorithm's performance.

### Strengths
1. The idea of creating a linear approximation of the nonlinear dynamical system through a Koopman framework is very interesting. This is because we can use a well-developed linear systems theory to derive scalable algorithms. 
1. The theoretical result on gradient growth is valuable for practitioners, who are not well acquainted with dynamical systems theory and stability theory
1. The authors demonstrate on some numerical examples, that the generative model is efficient for learning a planning controller as well as a policy.

### Weaknesses
1. Contributions are not well articulated in the introduction. It is not clear how this work is different from other Koopman operator-based RL methods. For example, I find the tools to compute long-term predictions quite interesting and a bit more detail on this in the introduction would strengthen the paper.
1. Ablation on sequence length for RL tasks is not provided, i.e., do we get an improvement from the model being able to predict several steps ahead? This is an important ablation since it was shown by Janner et al that using SAC as a policy learning algorithm does not benefit from rollouts longer than a one-time step. One potential reason for this is the algorithm itself that learns only from one-step-ahead predictions. Therefore, this raises the question of whether we actually need a model capable of long-term predictions. I do not see a discussion on this subject. 
1. Ablation with Hippo model as a backbone for offline RL is missing. The authors mention the relation to the Koopman framework and it would be interesting to see if the proposed model offers an improvement over HIPPO
1. The presentation needs to be sharpened a bit to highlight the main contribution - the effect of the novel Koopman model on RL in comparison to other generative models. I think the authors can pivot to argue that their Koopman model should be considered as the base model for most of the RL problems (offline RL, planning, model-based RL etc). But this a matter of choice.



### Questions
1. “In this work, we leverage techniques and perspectives from Koopman theory (Koopman, 1931; Koopman & Neumann, 1932; Brunton et al., 2021) to address this key problem in long-range dynamics modeling of interactive environments.” I feel that Mauroy et al 2020 would be a better reference for modern Koopman theory and recent developments 
1. “and thus an invariant subspace $G \subset F$ is often used, so that $Kg \in G$. $G$ is spanned by a finite set of observables $g_1$, . . . , $g_m$, where often we assume $m \gg n$.”\
This is slightly confusing. Finding an invariant subspace *is not a tractable problem*, while this phrasing implies that we can pick an invariant subspace. Please rephrase.  
1. Page 3. “one could show that the Koopman operator is bilinearized (Brunton et al., 2021)”
If I understood correctly Brunton et al bilinearization is possible only if there is a finite number of eingenfunctions (Theorem 6.1). I am not sure if this implies isomorphism to linear dynamics, but in any case, this is an important restriction worth mentioning 

1. “An alternate approach to simplifying the Koopman operator with a control signal assumes”. “Simplifying” is a confusing word in this context. I recommend using “approximating”, which would rule out equivalence of representations.

1. “Fig. 4 empirically verifies that our proposed Koopman dynamics model is around twice as fast as an MLP, GRU or Transformer based dynamics model in learning from longer trajectories” It is hard to verify this claim based on the figure, I suggest referencing Table 3 in the appendix and provide the number 1.7 instead of “around twice as fast”

1. There seems to be a small clash of notation, where $\overline \lambda_j$ is used to describe the entries of the diagonal Koopman matrix $\overline K$, and also the diagonal entries of the matrix $K$. 

References:
 
Janner, Michael, et al. "When to trust your model: Model-based policy optimization." Advances in neural information processing systems 32 (2019).

Fujimoto, Scott, and Shixiang Shane Gu. "A minimalist approach to offline reinforcement learning." Advances in neural information processing systems 34 (2021): 20132-20145.

Mauroy, Alexandre, Y. Susuki, and I. Mezić. Koopman operator in systems and control. Berlin: Springer International Publishing, 2020.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
