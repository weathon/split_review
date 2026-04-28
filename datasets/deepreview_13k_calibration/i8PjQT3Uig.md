# Locality Sensitive Sparse Encoding for Learning World Models Online

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
\new{Acquiring an accurate world model \textit{online} for model-based reinforcement learning (MBRL) is challenging due to data nonstationarity, which typically causes catastrophic forgetting for neural networks (NNs). From the online learning perspective, a Follow-The-Leader (FTL) world model is desirable, which optimally fits all previous experiences at each round. Unfortunately, NN-based models need re-training on all accumulated data at every interaction step to achieve FTL, which is computationally expensive for lifelong agents. In this paper, we revisit models that can achieve FTL with incremental updates. Specifically, our world model is a linear regression model supported by nonlinear random features. The linear part ensures efficient FTL update while the nonlinear random feature empowers the fitting of complex environments. To best trade off model capacity and computation efficiency, we introduce a locality sensitive sparse encoding, which allows us to conduct efficient sparse updates even with very high dimensional nonlinear features. We validate the representation power of our encoding and verify that it allows efficient online learning under data covariate shift. We also show, in the Dyna MBRL setting, that our world models learned online using a \textit{single pass} of trajectory data either surpass or match the performance of deep world models trained with replay and other continual learning methods.
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a model-based reinforcement learning approach that utilizes a sparse representation-to-representation model. The use of sparse representation aims to address the challenge of catastrophic forgetting in a reinforcement learning (RL) setting, where data generation constantly shifts. The architecture employed for model-based reinforcement learning is Dyna. The proposed method involves learning nonlinear sparse features and building a model based on this sparse representation. To enhance computational efficiency, a method for updating model weights using sparse representation is presented. Empirical experiments are included to demonstrate the effectiveness of this approach.

### Strengths
1. The paper targets an important topic of learning a model in RL 

2. I do not see many related works of building sparse representation-based models.

### Weaknesses
I will list below main weaknesses for improvements, centred around the main contribution of the paper.

1. Is there any reason for why the particular sparse representation learning method is chosen? Furthermore, in the experiments part, FTA should also be compared as a baseline. It is unclear why you compare it in a supervised learning setting but omit in a RL setting. The performance on a SL setting does not invlidate/validate another. As an empirical paper, I think a rigorous comparison is necessary.

2. Could you clarify do you update both your model and representation every environment time step?

3. There is a critical weakness in the paper: the paper claims to develop a sparse representation-based approach for model learning, but it is not justified the reported benefits come from the use of the sparse representation for policy learning or for model learning. Note that the former has been extensive studied. in general, a full replay method should be the best in mitigating catastrophic forgetting, but the empirical results reported that the proposed algorithm can sometimes even outperform full replay. That raises a natural question that the benefit mainly comes from the policy learning part by using sparse representation, rather than the proposed model learning part.

4. other issues.

Alg 1. it is better to be specific, use the title Dyna architecture, rather than MBRL, as there are numerous MBRL algorithms and not everyone is as Alg 1 described.

Alg 2, line 4 & 5: shouldn’t it be outer product? Please specify the dimension of the matrices capital Phi and letter phi. This is nontrivial as it affects the understanding of the algorithm.

The term “world model” might intrigue the readers to see much more challenging tasks than the paper presented, this can be seen by other papers using such terms. It is better to rephrase it to be more precise.

### Questions
see above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for the online learning of a world model for model-based reinforcement learning (MBRL). To obtain efficient updates to the world model, the world model is expressed as a linear combination of a set of spare features. This efficiency allows online learning at a constant computational cost.

### Strengths
The work is well motivated in the introduction and a sufficient and clear background is provided for non-expert readers in the preliminaries section. The algorithms, definitions, etc. are mathematically rigorously presented. 

A comprehensive set of experiments has been conducted demonstrating the efficacy of Losse-FTL

### Weaknesses
Significant discussion around catastrophic forgetting was mentioned in the introduction but little discussion is presented in the main text and left in the appendix.

“Example 3.1” could be a regular paragraph. Formatting this as an Example does not improve readability and is, in fact, the only Example in the entire paper.

In figure (1): d(s_(t+1), f(st, at)) and \delta were not defined in the caption or anywhere obvious in the main text.

In eq (3), does || . ||^2_F denote the Frobenius matrix norm? It is only stated so after eq (5). It helps to have the notation introduced earlier here. Especially since “F” is the dimension of the feature space

### Questions
In figure (1): d(s_(t+1), f(st, at)) and \delta were not defined in the caption or anywhere obvious in the main text.

In eq (3), does || . ||^2_F denote the Frobenius matrix norm? It is only stated so after eq (5). It helps to have the notation introduced earlier here. Especially since “F” is the dimension of the feature space

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a world model for model-based reinforcement learning (RL) which can be learned online and does not
require full retraining on all previous data.
The authors highlight that training world models is subject to issues arising in continual learning.
That is, each sequential data set can be interpreted as coming from a new task and thus the world model needs to be retrained
after each agent-environment interaction.
This is because the data collected via agent-environment interaction is non-stationary.
They propose a world model based on a linear regression model which uses high-dimensional nonlinear features.
Importantly, the linear model can be updated given new data whilst retaining good predictive performance on old data.
They compare their feature encoding method to other feature encoding techniques in an image denoising task on MNIST.
They then evaluate their method's ability to handle training data covariate shift in an artificial online learning experiment.
Finally, they evaluate their method's ability to combat non-stationary data in model-based RL.

### Strengths
This paper addresses an important problem in model-based RL, which is likely a problem that must be solved for developing lifelong agents.
The method for updating the linear model online is simple but appears to be effective.
This is also the first time I have seen a non-trainable encoder used for world models.
It is very common to see world models with NN encoders and NN transition models operating in the encoder's latent space.
Typically the dynamic model operates on a latent state which is lower dimensional than the high-dimensional observations.
Perhaps I am not aware of the relevant literature, but this seems like an interesting and original idea.

### Weaknesses
This paper has two main weaknesses.
Firstly, there is no comparison to state-of-the-art MBRL strategies that use world models, e.g. Dreamer/TD-MPC. As such, there is no experiment highlighting the main issue that the paper is trying to address:
that NN-based world models suffer from catastrophic interference due to non-stationary data. The experiments do not isolate the issue of non-stationary data for world model training. The limited performance of the Full-replay baseline is likely due to primacy bias and not the non-stationary data. Training until the validation loss stops decreasing will almost certainly lead to the NN overfitting early in training. A simple solution is to add one extra baseline. A modification of the Full replay experiment where the NN is reset at each episode. Whilst I know this is not practical for a lifelong agent, it should be feasible for the simple environments reported in the paper. This would remove issues with primacy bias and allow the baseline to act as a sort of upper bound on model-based performance.
Second, all of the RL experiments are in simple RL environments. From the current results, it is impossible to know how practically useful this world model is. There is no discussion about its limitations nor is there a comparison to other model-based RL algorithms that use world models. Sure the proposed method works on some simple RL environments but can it scale to difficult environments like humanoid and can it handle image-based observations?
It is OK if the method cannot do this but it should be addressed in the text. Moreover, it should be made clear what benefit it does have over other world model methods (like Dreamer).
For example, I'd like to see a state-of-the-art world model method (like Dreamer) performing poorly/failing because it cannot handle non-stationary data.

I also have questions regarding the training of the NNs in the experiments.
Did the full-replay experiment involve resetting the neural network's weights? If so, what initialization was used?
When was the NN training stopped? Was the data split into train/validation sets and used to stop training when the
validation loss stopped improving?
The paper needs more details to explain exactly how this was implemented. In my experience, these steps are important to ensure the NNs don't overfit on early data sets.

I am also unsure why the full-replay strategy (which is model-based), does not appear to have better sample
efficiency than the model-free experiment. Am I missing something here?
Perhaps this is an interesting point for discussion. Do the high-dimensional features sacrifice sample efficiency
in favour of formulating a linear model which can handle the non-stationary data?
I'm not sure if this is correct.
My main point here is that the paper has not answered all of my questions about the method.

The experiments tell the first part of a nice story.
Table 1 compares to other encoding methods and Fig. 3 clearly shows how the method handles covariate shift better than NNs.
Fig. 4 also acts as a nice ablation for comparing the method to other CL strategies within the same set-up.
However, the experiments section lacks a comparison to other MBRL strategies which use world models.
In particular, there is no experiment highlighting the main issue the paper is trying to address.
That is, there is no MBRL experiment failing due to the non-stationarity of the training data.

Minor comments and corrections:
- The abstract is very long. I would recommend shortening it.
- Sections shouldn't lead straight into subsections (Section 4/4.1, 5/5.1, B/B.1, C/C.1). There should be text explaining what the reader can expect to read in the section.
- In the first paragraph of Section 2.2, the reward function is defined as $R(\mathbf{s}, \mathbf{a}, \mathbf{s}')$ but then in the optimal policy equation you use $R(\mathbf{s}, \mathbf{a})$.
- Fourth line of Section 2.2 the initial state distribution is $\rho$ but earlier it is $\rho_0$.
- Third paragraph of Section 2.2 - "We firstly formulate" should be "We first formulate".
- Section 2.1 - "When the input is a convex set $\mathcal{S}$, the prediction a vector $\mathbf{w}_{t} \in \mathcal{S}$". This sentence doesn't read properly.
- $\rho$ is used to denote the initial state distribution and to denote the dimension of the grids in Section 3.2.
- What is the value of $\delta$ in Fig. 1?
- What are $\pi_0$, $\pi_t$ and $\pi_{t'}$?
- The first sentence of the abstract says model-based RL has better sample efficiency. Better than what? It's model-free counterparts?
- It is unusual to end the paper with a section titled "Summary". I recommend changing this to "Conclusion".

### Questions
- What are the limitations of the proposed method? Can it handle image observations? Can it scale to difficult environments like Humanoid?
- Why haven't you compared to any other world model algorithms? E.g. Dreamer, TD-MPC.
- How was the NN full-replay experiment implemented? Did the full-replay experiment involve resetting the neural network's weights? If so, what initialization was used? When was the NN training stopped? Was the data split into train/validation sets and used to stop training when the validation loss stopped improving?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
