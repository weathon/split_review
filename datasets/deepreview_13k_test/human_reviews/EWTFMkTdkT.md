# Invariance-based Learning of Latent Dynamics

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
We propose a new model class aimed at predicting dynamical trajectories from high-dimensional empirical data. This is done by combining variational autoencoders and (spatio-)temporal transformers within a  framework designed to enforce certain scientifically-motivated invariances. The models allow inference of system behavior at any continuous time and generalization well beyond the data distributions seen during training. Furthermore, the models do not require an explicit neural ODE formulation, making them efficient and highly scalable in practice. We study  behavior through simple theoretical analyses and  extensive empirical experiments. The latter investigate  the ability to predict the trajectories of complicated  systems based on finite data and show that the proposed approaches can outperform existing neural-dynamical models. We study also more general inductive bias in the context of transfer to data obtained under entirely novel system interventions. Overall, our results provide a new framework for efficiently learning complicated dynamics in a data-driven manner, with potential applications in a wide range of fields including physics, biology, and engineering.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript introduces a novel deep trajectory inference model, referred to as LaDID. This model designed to predict dynamical trajectories by disentangling invariant and variant dynamical factors. LaDID employs a convolutional autoencoder unit for dimension reduction and a transformer unit for learning temporal structure, eliminating the need for ODE formulations and enabling efficient long trajectory prediction without added computational costs.

In the study, the authors evaluated LaDID's performance using six simulated datasets. They conducted a comprehensive comparison of LaDID with four ODE-based models, namely ODE-RNN, ODE2VAE, NDP, and MSVI. The results demonstrated LaDID's superiority in all experiments, including challenging few-shot learning tasks.

I appreciate the problem tackled by the author and find the concept of invariant-latent representation learning in dynamical systems intriguing. The paper appears to have a solid metric in place. Nevertheless, there are certain crucial aspects that need to be improved. I am open to potentially revising my assessment following the author's rebuttal.

### Strengths
- The manuscript tackles an intriguing and challenging problem related to trajectory inference in dynamical systems. The proposed approach involves effectively decomposing the latent factors into variant and invariant components, which is fairly innovative.

- The authors conducted a comprehensive performance evaluation across six complex dynamical systems. 

- The proposed model consistently outperforms its related counterparts across a wide range of tasks. 

- The proposed model showcases capabilities in handling long trajectories, even when provided with limited training samples. This adaptability to data constraints is a significant strength, as it opens up opportunities for more efficient and practical application in dynamical system modeling.

### Weaknesses
**Major comment:**

My prominent concern in the paper pertains to the insufficient explanation for why their model outperforms others. The main contribution of the paper lacks clear description and justification. As pointed out by the authors, both LaDID and MSVI (Iakovlev et al., 2023) share several similarities, such as using CNN encoders/decoders and the same transformer. The primary distinction between these models lies in replacing neural ODE with MLPs to learn $f_{\phi_{dyn}}$ and introducing a smoothness loss to discourage abrupt transitions between latent subpatches. It remains unclear how these modifications enhance the process of learning latent dynamics in comparison to ODE-based methods.

**Minor Points:**

- Figure 1 could benefit from a more comprehensive overview of their framework. Clarifying how each process in the top row corresponds to each step in the bottom row would enhance understanding.
- The paper's writing can be improved, and some content from the Appendix may be integrated into the main text.
- The descriptions of the experiments are somewhat confusing and could benefit from increased clarity and explanation.

### Questions
- If I understand correctly, the paper addresses only the initial state as the specific (variant) trajectory factor, right? What about other sources of variability, like measurement noise?

- In section 4.1, Model, the main text says *"To obtain a latent trajectory,  ... we choose as a set of different sine and cosine waves with different wave length."* Could you explain it? 

- Could you please explain the choice of using MSE/RMSE for evaluation? It seems that capturing the overall structure of dynamics (direction, shape, etc.) might be more crucial than the absolute amount of misprediction.

- Can LaDID effectively handle time-variant dynamical systems? If yes, how?

- In the graphical model (Figure A1), $\psi^r$ is out of the box "$N$". Then, how is $\psi^r$ a function of "$n$" in Eq. 3 and Eq. 9?

- The text mentions *" ... mean-aggregation, which can be changed based on the task at hand."* Could you elaborate on the role and task-dependent nature of mean-aggregation?

- In Eq. 9, within the representation prior term, none of the variables appear to be a function of "$n$." Can you clarify this discrepancy?

- What does "$D$" represent in Figure A1?

- The authors stated that *"our models are specifically designed to exploit certain invariances that are important in classical scientific models."* Could you provide more detail on these "certain invariances"?

- Beyond classical scientific examples, can LaDID effectively learn developmental trajectories involving bifurcations and other complex phenomena?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a general framework for predicting dynamical trajectories based from data. The model architecture specificially aims at extracting realization-invariant and realization-specific information from different observations of underlying dynamical processes, iterated e.g. from different initial states or with different model parameters. To this end they employ a sophisticated encoder architecture, based on CNNs, temporal self-attention and a multi-shooting augmentation to obtain a condensed representation that can be used as a conditioning for a dynamics forecast. The learned latent dynamics model can be queried at irregular times, and the predicted dynamics decoded via a CNN-based decoder model and compared with the data. The model shows SOTA performance on 6 complicated and high-dimensional observations of dynamical processes, such as fluid flows. The author also investigate transfer learning between different parameter settings of the same underlying systems via few-shot learning.

### Strengths
The presentation, including the figures and writing, is high quality. I also appreciate the detailed appendix. While I have seen many of the components employed in similar settings, such as sequential variational autoencoders or Latent-ODEs, the proposed architecture looks like an interesting new combination of all of them. The idea of transfer learning and generalization for dynamics models is an important field of study. I like the approach of using an expressive encoder to inform the dynamics model about the specifics of the observed time series by encoding it in the initial state, and the fact that the obtained model is continuous in time.

### Weaknesses
General problem setting:

What is meant by invariant? To my understanding the term “invariant” in this paper mostly refers to the flow of the underlying system (i.e. the equations given in Appendix 1), while the realization-specific components are different initial conditions from which different observations start. This is also the situation primarily studied in the experimental section. The authors claim to show "generalization well beyond the data distributions seen during training".
However, the setting they mostly investigate is just the standard setting in dynamical systems reconstruction, where underlying dynamical processes/flow fields are inferred from multiple or even single observations. I don't think this constitutes generalization beyond the data distribution in the usual sense.

More interesting to my mind is the question of transfer learning e.g. between different dynamical regimes (as studied out in 6.2.) with different parameter settings of the underlying system, or even between different but in some way related systems. Relating this to a more formal language common in dynamical systems theory might be helpful, since for dynamical systems the concept of invariants, such as topological invariants, fixed points, periodic orbits, Lyapunov spectra, invariant measures etc. is well studied. While the abstract mentions the motivation to “ enforce certain scientifically-motivated invariances” these invariances are not really made explicit in the related work or in the analysis of the obtained results and remained somewhat elusive to me.
Further, while you mention that your approach “is in principle not specific to physical ODE-like models”, these are the only systems you actually study in the experiments, which naturally suggests are framing in these terms.

Transfer learning setting (6.2.)

Your framework is aimed at transfer learning from “potentially highly heterogeneous parameters and data”, which as mentioned seems the more novel application of your framework. Most of the empirical section however focuses on multiple instantionations of the same underlying system. The results from 6.2., where transfer learning between different model parameters is learned, however indicate that the transfer effect is relatively weka, with advantages over learning from scratch remaining within the error bars, and comparative performance requiring a significant portion of the new training set (if I understood it correctly corresponding to hundreds of tractories from the altered system).

Interventions/nonstationarities in parameters for dynamical systems can also be viewed through the lense of bifurcations. Increasing the Reynolds number can e.g. induce turbulence, as you rightly point out. From your description it is not altogether clear what changes in the dynamics your parameter changes in this section induce, and whether they lead to qualitative differences.
Since to my understanding this transfer is the primary motivation for introducing your framework, I found this section to be a little too short and and not in-depth enough.
I also wasn't 100% sure if you indeed jointly trained on different Reynolds numbers for the flow around a blunt body (Re = 100, 250, 500), which would be an interesting extension of your study in 6.2.

Comparisons and Experimental Evaluation
 
All datasets studied in the comparison methods are based on solutions to synthetic ODE systems, and include several PDEs. The claim that you provided evaluation on real-world datasets I find a little misleading, since none of the benchmarks are based on experimental/real world data, while of course being inspired by real systems.

Selecting comparisons is always a debatable point, but since all benchmark systems chosen are relatively simple/polynomial form, other classes of comparisons could be valuable: approaches by Brunton et al. based on SINDy and its variants are also frequently studies similar fluid flows. Neural Fourier Operators, which you also mention in the related work have been particularly successful for PDEs, so they might be a better choice here.
 
Algorithms like ODE-RNN are tailored towards irregularly sampled, but not necessarily spatially extended data. ODE-RNN in general has very poor performance everywhere in the paper (see all figures including ODE-RNN, e.g. Fig 4 or Fig. J6 b), where they seem to have learned nothing meaningful at all, which indicates that there either is a bug in the training, or the method is not well suited as a comparison.

Overall, since I think the general setting studied here is important and the presentation is good, if my concerns can be adressed I am also willing to adjust my final score.

### Questions
Model parameters:

How parameter intense is your approach? Would it struggle to infer meaningful dynamics from only single or few trajectories, compared to approaches with a stronger inductive bias, such as SINDy (Brunton et al., 2015), or experimental settings, where there are often only single or few observed trajectories. The models in Table H2 have between 1 and 10 million parameters, and are trained on observations with 400 initial states each used for training, which hints at a data and parameter intese regime given some of the relatively simple underlying dynamical processes. How does your model behave for sparser data? Figure 6 indicates that for comparable performance on the pendulum data, comparable performance requires hundreds of observed trajectories?

Related Work: 

I understand that it's hard to provide an exhaustive overview over related methods, and I appreciate the extended related work. I however want to point out that there are many RNN based approaches specifically designed for inferring complex dynamics and leveraging inferred models for long-term time series forecasting (Reservoir Computing, see Pathak et al. 2018), LSTMs (Vlachas et al., 2018) or RNNs (see e.g. Hess et al., ICML 2023), and could be mentioned here as well.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider an encoder decoder model for predicting the trajectory of time series from high dimensional observations. A key difference of the model is that the authors do not impose a particular type of known structure on the dynamics such that the dynamics must follow this structure. The authors then introduce a probabilistic multiple shooting method such that the method can be trained. The authors illustrate the proposed method on a number of different datasets to validate its performance. The main question in the performance evaluation is how well the method works on unseen conditions, i.e. changing the parameters of the true underlying dynamical system.

### Strengths
The premise of the paper is very well founded. In general, most time series approaches with latent dynamics consider some model from the applied mathematics literature (e.g. SDEs, ODEs) and then parameterize it according to a neural network. However, the authors consider a more general framework where they split the dynamics according to realization-specific components and invariant components. This induces a new algebra that should somehow be given by the parameterization of the model. The empirical results are also very good and suggest that the model outperforms the baseline methods.

### Weaknesses
While the motivation of the paper is nice, there exist a number of limitations in the implementation and in the model itself. For one, there is no guarantee that the model will converge to something that has these separable parameter sets within the motivation of the work. The loss function seems rather standard in the sense that it is the standard loss when one parameterizes a latent variable time series model. It would have been nice to show under what assumptions does the model decompose into the disjoint parameter sets -- the invariant ones and the instance-specific ones. 

While this is a small weakness, the paper seems to claim a bit too much (though I may have also misunderstood). For example, the authors mention they make no assumptions on the structure of the model in the sense of an ODE type of factorization, but still the fact that the first $K$ steps of the time series are used for conditioning does induce a particular structure. In some sense, the ODE interpretation is amenable since one can use the known properties of ODEs to probe the model.

A major goal is to generalize the output on a new domains where some invariant properties are maintained, but the experiments only demonstrated this in the case of changing parameters. However, maybe it would be helpful to see the behavior under shifts in the observation distribution. For example, could the distribution of the observation space change in a trivial way (e.g. different color map for the wave equation example) and could the distribution still be predicted?

There are also some properties that the authors impose in their loss (e.g. smoothness of the latent space) but that assumption seems to violate some of the motivating ideas behind the paper. Smoothness almost implies a differential equation in the latent space.

### Questions
Is there anything in the loss that guarantees that the factorization in terms of the RI and RS components? If not how can one impose this on the latent representation?

Assumptions on the latent space being Gaussian seem a bit restrictive, is there a reason for making this assumption? Specifically am wondering how this affects the motivation that very little structure should be imposed on the latent distribution. Will the smoothness and Gaussian terms will force the learned dynamics to resemble something that satisfies an ODE?

### Soundness
2 fair

### Presentation
3 good

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
The paper introduces a novel framework called "Latent Dynamics via Invariant Decomposition" (LaDID) for predicting dynamical trajectories from high-dimensional empirical data. LaDID merges variational autoencoders with spatio-temporal attention, emphasizing scientifically-motivated invariances, allowing the model to predict system behavior at any continuous time and generalize beyond seen training data. Using a transformer-based architecture, it distinguishes between system-specific and universal dynamics, showing efficiency and scalability in experiments. The method is validated on various spatio-temporal systems, LaDID outperforms current neural-dynamical models.

### Strengths
1. The paper uniquely combines variational autoencoders with spatio-temporal attention

2. empirical tests on various spatio-temporal systems demonstrate that LaDID not only has practical utility but also massively outperforms existing neural-dynamical models

### Weaknesses
1.The definition of a system with realization-specific and realization-invariant properties is not clear. In chapter 3, I understand the authors try to explain its difference to the ode like systems and want to extend the ODE-like system setting to a more general settings with RS and RI properties, but I cannot find a specific example which is included in the RS-RI setting but excluded in the ODE setting. Can the author provide a useful example?

It seems like all the experiments in the paper can be treated as ODE-like dynamical system, so I was wondering what is the major difference here?

2.There is a missing literature review regarding invariant learning and its application in data-driven dynamical system learning, there are a few branches of related work worth mentioning and they are very close to the topic in this paper:
Physics/Conservation invariant:

"Hamiltonian neural networks." Advances in neural information processing systems 32 (2019).

Lagrangian Neural Networks. In ICLR 2020 Workshop on Integration of Deep Neural Models and Differential Equations.

ConCerNet: A Contrastive Learning Based Framework for Automated Conservation Law Discovery and Trustworthy Dynamical System Prediction. International Conference on Machine Learning 2023.

Symmetry invariant: Incorporating Symmetry into Deep Dynamics Models for Improved Generalization, ICLR 2021

Actually the Hamiltonian Neural network paper provides an image-based pendulum example which is similar to the experiment in this paper. 

3.Regarding the novelty of the model structure, I feel like it still belongs to the encoder-latent dynamics-decoder model class like many other prior works. Despite the author claimed the model decomposes the realization-specific (RS) and realization-invariant (RI) information, there is no evidence proving the claim both experimentally and theoretically.

4.Honestly I’m a bit skeptical regarding the massive improvement of the proposed method over the existing work, especially in figure 4 and 5 (see my questions)

### Questions
1. In the performance comparison figure 4, is the X axis the time axis? The results surprised me because the prediction from the first 3 models is bad starting from the beginning of the prediction, which means the error mostly comes from decoder reconstruction rather than dynamics prediction. Especially for ODE2VAE, VAE should be able to reconstruct the pendulum image fairly well.

2. In Figure 5, the MSE from the proposed method is 10-100 times smaller than the prior works. This is another surprise as such a difference usually happens between white box model and black box model. Could there be bugs in your code, or is there any unfair comparison? I’m not trying to be mean but it does not look reasonable for me unless formal claims/evidence is provided.

3. In the latent dynamics model (part v in figure 1), how does the query time t work? Does this model need to solve it iteratively like ODE-like solver to time t or the neural network directly takes t as input and outputs the latent state at time t.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
