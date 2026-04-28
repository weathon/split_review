# Leveraging Generative Models for Unsupervised Alignment of Neural Time Series Data

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Large scale inference models are widely used in neuroscience to extract latent representations from high-dimensional neural recordings. Due to the statistical heterogeneities between sessions and animals, a new model is trained from scratch to infer the underlying dynamics for each new dataset. This is computationally expensive and does not fully leverage all the available data. Moreover, as these models get more complex, they can be challenging to train. In parallel, it is becoming common to use pre-trained models in the machine learning community for few shot and transfer learning. One major hurdle that prevents the re-use of generative models in neuroscience is the complex spatio-temporal structure of neural dynamics within and across animals. Interestingly, the underlying dynamics identified from different datasets on the same task are qualitatively similar. In this work, we exploit this observation and propose a source-free and unsupervised alignment approach that utilizes the learnt dynamics and enables the re-use of trained generative models. We validate our approach on simulations and show the efficacy of the alignment on neural recordings from the motor cortex obtained during a reaching task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Stable and Effective inference models are crucial for decoding neural recordings, yet the need to train new models for each dataset due to variability is computationally demanding and inefficient. This is thus an interesting scientific question. This study introduces a novel alignment method that applies learned dynamics to new data, enabling the reuse of pre-trained models and facilitating the sharing of generative models across different distribution settings. The method's effectiveness is demonstrated by using a seqVAE trained on monkey behavior datasets, underscoring the significance of low-dimensional neural representations and offering a new perspective on handling the neural variability between sessions.

### Strengths
1. The paper focuses on an insightful and scientific research question: alignment of neural recordings. Since the generalization ability of models is a great concern.
2. The paper's words and figures are well-written and easy to follow.
3. The proposed method is analytically tractable and is with good theoretical guarantees.

### Weaknesses
1. The baselines in the experimental part is too few, just the recently proposed SOTA method ERDiff [1]. There are many classical methods like [2] and [3]. Specifically, methods like Procrustes alignment, which directly aligns latent spaces, and other established techniques for cross-session alignment, such as those based on canonical correlation analysis or adversarial training, should be included for a comprehensive comparison. The current lack of these baselines makes it difficult to assess the true novelty and effectiveness of the proposed method.
2. The spatio and temporal structure has already been noticed by the SOTA method ERDiff, and ERDiff also employs a generative model (score-based model) for alignment. Thus what's the new motivations and insights of your work? The paper needs to more clearly articulate what specific limitations of ERDiff it addresses and what novel aspects it introduces beyond the existing framework of using generative models for alignment. The current explanation is insufficient to justify the need for a new method.
3. There should be more experiments and empirical results to support your method. The current set of experiments is limited in scope and does not sufficiently demonstrate the robustness and generalizability of the proposed method. The paper would benefit from experiments on more diverse datasets, including those with varying levels of noise and complexity, and across different neural recording modalities (e.g., LFP, calcium imaging).

### Questions
Please consider the things listed in the “Weaknesses” section.
Also please consider providing information regarding any potential future improvements.

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
The authors present a novel algorithm for leveraging pre-trained seqVAEs for fitting neural recordings. This algorithm builds on the assumption that the neural data in question share the same neural dynamics as the ones used to train the pre-trained model. The two key components to this algorithms are: (1) learn a new observation model from latents to observations and (2) _implicitly_ learn an alignment function from the new observations to the old observations. The authors validated their algorithm on both synthetic data and a monkey reaching dataset.

### Strengths
- originality
    To the best of my knowledge this is a new approach for leveraging pre-trained generative models for fitting new data.
- quality & clarity
    - The paper is well-motivated and clearly written, notwithstanding some typos here and there (e.g., missing "In contrast, [our method] does not require..." in last sentence of section 2.)
    - The experiments are relevant and convincing.

### Weaknesses
 * I am not sure I follow why Proposition 1 implies good alignment? If the space of alignment function that the authors are trying to learn is linear (i.e., $g_\theta(w) = \theta w$), isn't it always the case that any $\theta_\star$ will be some linear offset away from the optimal alignment? Is this offset $B$ supposed to be small somehow? The proposition, as stated, does not seem to provide a strong guarantee about the quality of the learned alignment, especially if the noise characteristics of the new data differ significantly from the pre-training data. The relationship between the learned alignment and the optimal alignment needs further clarification and justification.
* The choice of alignment function $g_\theta$ appears crucial to this paper, but there is very little discussion/evaluation about different choices. Specifically, if $g_\theta$ is a point-wise nonlinear function approximator $g_\theta(w_t)$ the authors are implicitly assuming that the latent dynamics are not just qualitatively similar, but **identifcal** between the new and old observations. This assumption is quite strong and may not hold in many real-world scenarios. Furthermore, if we make $g_\theta$ too flexible (e.g., another full bi-directional RNN), then we are effectively re-learning the encoder, which defeats the purpose of using a pre-trained model. The paper should explore the trade-offs between the expressiveness of $g_\theta$ and the benefits of leveraging the pre-trained model more thoroughly. The authors should also provide a more detailed analysis of how the choice of $g_\theta$ impacts the alignment quality and the overall performance of the method.

### Questions
* I assume $q_\phi(x_t, x_{t-1}|y_{1:T}) = q_\phi(x_t|y_{1:T}) q_\phi(x_{t-1}|y_{1:T})$ in equation 3? Might be worth clarifying.
* Is the equation supposed to have $p_\theta(x_t|x_{t-1:t-k})$ instead of $p_\theta(x_t|x_{t-1})$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Here, the authors consider the problem posed by the existence of multiple data sets of neural time series from the same or similar tasks, asking whether it is possible to transfer learned latent dynamics from one to the other. They propose a model in which a sequential VAE is first trained on a large data set to establish a latent space ${x}_{1:T}$ (assuming a linear decoder). On a new data set, these dynamics are frozen, a new (linear) decoder is retrained, and the encoder is reused by learning a nonlinear mapping $g(w)$ from the new observations $w$ to the space of the training observations $y$. This requires only the trained encoder and does not require labeled examples. This method is compared with several other alignment proposals, where it produces both quantitative and qualitative improvements.

### Strengths
- The problem of aligning multiple data sets across animals and experimental sessions is a major one in neuroscience. An ability to reuse or amortize model training across these would be of significant benefit.
- The method is theoretically well-motivated and fairly flexible. It doesn't appear to require a particular architecture (apart from the linear decoder, which is a limitation of data availability as much as anything).
- The approach appears to produce real qualitative improvements in the learned embedding (Figures 3 and 4).

### Weaknesses
 - The approach uses a fairly strong assumption that the latent dynamics really are shared across data sets, which all but implies a shared task setup. That is, it doesn't appear to be the case that a sufficiently large task-free data set in one mouse would facilitate embedding of mice performing a task-based behavior. It would be surprising if true, but this weakness should be acknowledged, since this limits the range of applicability.
- Given the large literature on data alignment/domain adaptation both within and without neuroscience, it's a bit surprising that there are only two approaches compared in Table 1.

### Questions
- How flexible is this setup to the specific architecture chosen? It's mentioned that using an ELBO that measures log predictive probability several steps ahead is important to achive a good embedding, but it's not entirely clear to me why.
- How complex are the learned dynamics in cases that work versus don't work? The monkey reach data typically have rotational dynamics. Do you see anything more complicated in other data?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an unsupervised alignment approach that can apply a pre-trained model on other neural recordings to the new dataset. They mathematically prove their approach is optimal up to scaler in a simplified case. They validate their methods on a simulation and a real dataset.

### Strengths
The authors propose a new unsupervised method to solve the transfer learning problem in neuroscience by re-using the temporal dynamics structure. They also have mathematical proof of the optimality of their method in a simplified case.

### Weaknesses
The experiment results are limited. The paper only shows results on 1 real dataset. There are some unclear parts in the paper, which I listed in the Questions section below.

1. how do you model the latent dynamics pθ(xt|xt−1)? Do you add any smooth constraints? In figure 2b, it seems that the results of the proposed approach are much smoother than ERDiff. 
2. what is FA + LDS method that you compare to in figure 2? Can you list a bit more details on how it's implemented? 
3. figure 2e, why does the mean k-step r^2 for Re-training decrease as the number of training samples increases? Intuitively the r^2 should increase as there are more training samples.
4. what are the results showing in table 1? Are they results for the real neural dataset? I found the r^2 number in table 1 doesn't match the number in figure 4.
5. in table 1, why the k-step MSE standard deviation is smaller than the stddev of MSE for ERDiff and the proposed method? 
6. in figure 4, why the proposed method performs better than ERDiff for poisson observations but not for the smoothed observations, especially Figure 4b (Top, left)?
7. The proposed method assumes that prior dynamics p(xt | xt-1) is fixed, and the encoder q(x | y_embed) is fixed. I wonder if the authors have checked these two assumptions? For example, if you jointly train a model on two datasets and learn the latent dynamics and encoder, will they be similar to the results of training separate models on each dataset?

### Questions
1. how do you model the latent dynamics pθ(xt|xt−1)? Do you add any smooth constraints? In figure 2b, it seems that the results of the proposed approach are much smoother than ERDiff. 
2. what is FA + LDS method that you compare to in figure 2? Can you list a bit more details on how it's implemented? 
3. figure 2e, why does the mean k-step r^2 for Re-training decrease as the number of training samples increases? Intuitively the r^2 should increase as there are more training samples.
4. what are the results showing in table 1? Are they results for the real neural dataset? I found the r^2 number in table 1 doesn't match the number in figure 4.
5. in table 1, why the k-step MSE standard deviation is smaller than the stddev of MSE for ERDiff and the proposed method? 
6. in figure 4, why the proposed method performs better than ERDiff for poisson observations but not for the smoothed observations, especially Figure 4b (Top, left)?
7. The proposed method assumes that prior dynamics p(xt | xt-1) is fixed, and the encoder q(x | y_embed) is fixed. I wonder if the authors have checked these two assumptions? For example, if you jointly train a model on two datasets and learn the latent dynamics and encoder, will they be similar to the results of training separate models on each dataset?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
