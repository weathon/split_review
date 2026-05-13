# Catapults in SGD: spikes in the training loss and their impact on generalization through feature learning

- Decision: Reject
- Scores: 6, 6, 8, 5

## Abstract
In this paper, we first present an explanation regarding the common occurrence of spikes in the training loss when neural networks are trained with stochastic gradient descent (SGD). We provide evidence that the spikes in the training loss of  SGD are ``catapults'',  an optimization phenomenon originally observed in GD with large learning rates in~\cite{lewkowycz2020large}. We empirically show that these catapults  occur in a low-dimensional subspace spanned by the top eigenvectors of the tangent kernel, for both GD and SGD. Second, we posit an explanation for how catapults lead to better generalization by demonstrating that catapults promote feature learning by increasing alignment with the Average Gradient Outer Product (AGOP) of the true predictor.  Furthermore, we demonstrate that a smaller batch size in SGD induces a larger number of catapults, thereby improving \AGOP alignment and test performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides an empirical verification of the claim that catapults in SGD occur in the top eigenspace of the NTK, where the catapults correspond to the "spikes" of the neural network training. Moreover, by leveraging the AGOP alignment, the paper also claims that more catapults induce better test accuracies. These claims are connected with some of the neural network training hyperparameters, most notably the batch size, and are corroborated with extensive experiments.

### Strengths
1. The paper is well-motivated and well-written
2. The experiments generally support the claims regarding catapults and generalization
3. The paper has some theoretical discussions.

### Weaknesses
1. The paper never answers *why* the catapults occur. The observations that the catapults happen in the top eigenspace of NTK and that it leads to a decrease in the spectral norm of NTK are not the actual mechanisms behind why catapults occur. Rather, they are direct conclusions of catapults occurring. The paper lacks a mechanistic explanation for the emergence of these 'spikes' in training, which limits its explanatory power. For instance, it would be valuable to explore how specific network architectures or activation functions might influence the propensity for catapults. A deeper investigation into the underlying causes, perhaps through a more detailed analysis of the loss landscape or the dynamics of weight updates, is needed.
2. The authors discuss in detail that the number of catapults correlates strongly with AGOP, which is known to be correlated strongly with test accuracy. But to me, these are still just correlations not explicit inner workings of catapults and their effects on generalization. The paper does not establish a causal link between catapults and improved generalization, and it remains unclear whether the observed correlation is merely a byproduct of other underlying factors. It would be beneficial to investigate whether manipulating the occurrence of catapults directly leads to predictable changes in generalization performance, or if other factors are also at play.

### Questions
1. Any results on (stochastic) gradient descent with momentum?
2. Although the authors did provide sufficient motivation for considering AGOP, I'm still curious about the relations to other "generalization measures" such as flatness (max eigenvalue of Hessian), tail-index of the trajectory/weight matrix [2,3]...etc.
3. Any connection to recently uncovered saddle-to-saddle hopping dynamics [3,4]? Can the hoppings be equated to catapults?


[1] https://proceedings.neurips.cc/paper/2020/hash/37693cfc748049e45d87b8c7d8b9aacd-Abstract.html
[2] https://jmlr.org/papers/v22/20-410.html
[3] https://arxiv.org/abs/2304.00488
[4] https://arxiv.org/abs/2106.15933

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discusses spikes in training loss dynamics when neural networks are trained with SGD, attributing them to "catapults" - an optimization phenomenon noted in GD with large learning rates in one previous work. They demonstrate that these catapults exist in a subspace defined by top eigenvectors of the tangent kernel for both GD and SGD. They also suggest that catapults enhance generalization by promoting feature learning and alignment with the AGOP of the true predictor. Additionally, they show that a smaller SGD batch size results in more catapults, thus boosting AGOP alignment and test results.

### Strengths
It's important to know why there are spikes in the training loss of modern NNs. This paper offers a clear and organized explanation. I think this will be very helpful for the community. The article is well-written and structured.

### Weaknesses
This paper lacks proof. It proposes a potential reason for spikes in neural network training loss but doesn't provide any rigorous theoretical analysis. Can we do this theory in a simpler setting? Furthermore, the authors seem to assume a linearized dynamics between spikes, but I'm not sure if this holds true in real-world situations. I don't think this is true in real-word situations, and I don't know whether this is true in simpler cases. For instance, in a basic setup using a 2-layer network, does this apply? While I understand the main idea (that with a higher learning rate, GD moves towards flatter regions to ensure the stability condition, which causes spikes, and with SGD's randomness, spikes might occur more often because the stability condition is changing), I'm not convinced about the linearized approximation between two spikes. Can you clarify this? If this is addressed, I'd rate the paper higher to 8.

### Questions
No.

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
The paper analyses the spikes in the learning curve of SGD in DNNs. They provide empirical evidence that:
- These spikes in the loss correspond to an increase in the error along the top eigenvalues of the NTK.
- The spikes happen when the learning rate becomes larger than the critical learning rate (which can depend on the batch).
- The number of spikes (which depends on the learning rate, batch-size and training algorithm) is well corelated with the test error and the AGOP alignement.

### Strengths
We are still lacking a good understanding of why these spikes appear during training, and even more why they improve performences. The paper proposes three simple (but to my knowledge new) postulates and checks them on a variety of tasks and architectures. These ideas form together a pretty complete picture.

### Weaknesses
The paper provides evidence that the spikes help generalization, but not so much in terms of what happens after the spikes that improve generalization.

For example, though the paper shows that the NTK decreases in size after each spike, it does not describe how it is changing, one could expect the NTK to decrease more along its top eigenvalues for example, since these eigenvalues are highly related to the spikes.

The only explanation that is proposed is that the AGOP alignement increases, but it is not explained why these spikes should increase AGOP alignement. Also while the paper presents the AGOP alignement as `the mechanism throught which NN learn features', I personnaly think that while the AGOP is an interesting measure of feature learning, but it is unlikely that it fully captures feature learning.

The authors could have considered other measures of feature learning, such as the alignement between the NTK and the task (there are multiple possible alignement measures). This could have been especially interesting since the first part of the argument suggest that the NTK spectrum plays an important role in the spikes.

### Questions
I would prefer if you did not present the AGOP as `the mechanism throught which NN learn features'. I think that there is clearly not enough evidence today to make this claim, when multiple other mechanisms for feature learning have been proposed (for example Information Bottleneck, NTK/kernel alignement). While the AGOP alignement seems well suited to low-index tasks (since the `index' can be recovered from the AGOP), it seems ill suited to measure feature learning when the learned features depend nonlinearly on the inputs, such as in (https://arxiv.org/abs/2305.19008).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the catapult phenomenon of (S)GD, which happens when we use a large enough step size that results in a spike in the training loss. This is mainly an empirical work, and they focus on various models under the MSE loss. Through extensive experiments, they show empirically that whenever catapults occur, the loss also spikes in the top eigenspace of the neural tangent kernel (NTK) matrix. Furthermore, they show that more catapults corresponds to an increased alignment between the trained model and the groundtruth model. This alignment is measured in terms of the AGOP of the respective models, where AGOP stands for the average gradient outer product, a matrix known to capture learned features. From this observation, they claim that catapults lead to better generalization.

### Strengths
The catapult phenomenon studied is interesting and deserves attention in the ICLR community. Although it has been observed and studied in the past, this paper provides new insights into how catapults are decomposed in the eigenspace of the NTK, and how they correlate with better generalization. These are novel directions to study this problem. The connection between catapults and AGOP alignment metric is also original and interesting.

### Weaknesses
Although the experiments are quite extensive and the observations are interesting, the paper in its current state is somewhat weak in both impact and presentation. In summary, I'm concerned about how much of the results can carry over to a realistic deep learning setting, where the cross entropy loss is most often used for classification, whereas in this work only the MSE loss is considered. There are many observations, but there lacks a coherent message. The language used in this paper can be inaccurate and handwavy, and I'm afraid the experiment details provided is insufficient for easy reproducibility. The presentation also needs some improvement.


### Major concerns

- Although I'm aware that Lewkowycz et al. (2020) also studied catapults only for the squared loss, it's still concerning that this work also does this same. Given that the logistic/cross-entropy loss is so often used in deep learning, at least some of the experiments should involve this setting. Especially since many of the tasks in this work is on classification, it's unrealistic to use the squared loss as it's extremely rare to train a classification model this way. This makes me wonder whether one can observe or induce catapults at all when using the logistic or cross-entropy loss, and whether the observations and claims in this paper can be carried in this more realistic setting. 

- The authors repeatedly emphasize that they show "catapults mainly occur in the subspace spanned by the top eigenvectors of the tangent kernel". After reading the entire paper, I'm still confused about this observation. Yes, the experiments show that this indeed seems to happen. But the question is: so what? Should I be surprised about it? The top eigenspace of the NTK corresponds to the examples in the training set that matter the most in terms of prediction, so they are likely the "support vectors". So if catapults were to occur, it's not surprising that the projection of the residual also spikes for these examples. I think more elaboration about this observation is needed. Why is it significant, and why should we care about the NTK matrix when it comes to catapults? This part of the paper also seems to be somewhat disconnected from the latter part - it's unclear how "catapults show up in the top eigenspace of the NTK" is related to the AGOP alignment. In fact, upon first reading of this observation, it's not immediately clear what it means or what it implies. Further elaboration of this point is need to strengthen the paper, otherwise it just seems like a standalone observation that may or may not be significant. 

- The paper claims to connect three phenomena in deep learning, the third one being "small batch SGD leads to better generalization" (paraphrased third point at the bottom of page 1). As far as I'm aware, the paper by Geiping et al., 2022 [Stochastic Training is Not Necessary for Generalization](https://arxiv.org/abs/2109.14119) says that's not always the case if you tune well. It seems like in Figure 7, 18-20, only one step size is given for each task (page 22), so I'm assuming they are the same across batch sizes as well. It's unclear how these step sizes are selected and why they are the same for all batch sizes. I'm a bit skeptical about this setup, especially given the results in Geiping et al., 2022. 

- Claim 2 is about changes in the (projected) batch loss, but the experiments on SGD all show the full loss. Is Claim 2 really significant if what we truly care about is the full loss? 

- Page 2: "This explains why the loss drops quickly to pre-spike levels from the peak of the spike". First, I don't see how catapult in the eigenspace explains this. Second, I find this entire sentence vague and handwavy. It's unclear what the authors mean by pre-spike levels. Is it the loss level at the iteration right before the spike occurs, or 50 iterations before the spike occurs? What drop rate is considered quick? Quick compared to what?

- More experiment details should be given and in a clear manner, rather than having them scattered around throughout the main text and the appendix. 
	- For instance, the paper mentions that the NTK parameterization is used in many places, but what exactly is this parameterization is unclear, especially to readers who may not be familiar with it. I recommend that the authors explicitly describe what the model architecture is, what the initializations are (crucial to the NTK parameterization), etc. More importantly, why is the NTK parameterization used? Is it crucial that you must use this to produce the results?  
	- Another one is the step size used for Figure 3: yes, we can sort of read off the step size from the LR figure, but the exact numbers are not given. How did you choose those numbers? It's said in the next page that it starts small $\eta<\eta_{\mathrm{crit}}\approx\eta/\lambda_{\max}(K)$ and increases to $\eta>\eta_{\mathrm{crit}}$, but how exactly is it achieved? What is $\approx$? Is the step size increased by a multiplicative factor? I don't think this information is explicitly provided in the paper, and I apologize in advance if I had missed it somewhere. 

- The related work section needs more work, in the sense that it currently presents a laundry list of related works, but how they are related to each other and to the current work is inadequately discussed. Specifically, at the end of the **Catapult phase** paragraph, instead of explaining what catapult is, which was already done in the intro, here the authors should elaborate more on what these works have found, what setup was different, how their results relate to the results of the current work, and so on. Similar improvements can be made to the **EoS paragraph.


### questions:
 - Why does the critical step size only depend on the initialization and not varying throughout training?
- Paragraph under Claim 1: shouldn't it be $\mathcal{P}\mathcal{L}_n$ instead of  $\mathcal{P}\mathcal{L}_5$ that corresponds to the the spike in the training loss? Is $\mathcal{P}\mathcal{L}_5$ even plotted somewhere that I missed?
- **Choice of top eigenspace dimension $s$**: 
	- The first sentence after this  - I'm confused by what this sentence is trying to convey, especially the second part. What linear dynamics? 
	- So you expect to need a larger $s$, and turns out a small $s$ is sufficient to produce the catapults in the top-$s$ eigenspace. Do you have an explanation to why this contradicts to what you expect? My guess is that $s$ corresponds to the support vectors in some sense, but I'm also uncertain. Is there a way to verify this?  
- Eq (6): $\mathbf{f}(X_{\mathrm{batch}})$ has the same length as the number of examples in the batch. But the projection operator acts on prediction vectors of length $n$. Is something off here or am I misunderstanding? 
- Do you need to recompute $\eta_{\mathrm{crit}}(X_{\mathrm{batch}})$ for each batch? How does it work? 
- I think more motivation for "AGOP alignment is a good measure for generalization" can be given. As a simple example, one can consider the classic low-rank matrix sensing problem 
$$
L(U) = \frac{1}{2n}\sum_{i=1}^n ( \langle A_i,UU^\top \rangle - y_i )^2
$$
where the labels are generated via $y_i= \langle A_i, X^* \rangle$ for some positive semidefinite low-rank groundtruth $X^*$. Since $G$ and $G^*$ can be derived in closed form, does high AGOP alignment imply high generalization in terms of $\Vert UU^\top - X^*\Vert_F$?


### Minor suggestions
- Latin words such  as *a priori* should be italicized 
- Figure 1 caption: training loss "of" SGD -> training loss "when optimized using" SGD 
- Table 2: please use $0.01$ or $10^{-2}$ instead of 1e-2 to present hyperparameters used.
- Page 2: sentence starting with "Namely, we project the residual..."
	- Up to this point, the paper has not mentioned that it only looks at the MSE loss, so readers who expect the authors to also study the logistic/cross-entropy loss may be confused why you are projecting the residual.
- The experimental details section (E) can be improved in terms of writing: there are many dangling paragraphs with only one or two sentences, which break the flow of the writing and reads more like bullet points that don't belong together. 
- Section E, 3rd paragraph: "the test error refers to the classification error" -> "the test error refers to the classification error on the test split"
- I may be overly fussy about this or have interpreted something incorrectly, but in the related work section, the authors say that "In Cohen et al. (2020)", it was conjectured that at EoS, there are numerous catapults". To me it's more like Cohen et al. "observed" numerous catapults at EoS, but conjectured that EoS and catapults have the same underlying cause.
- Page 4 second paragraph: 
	- "the tangent kernel $K=$... and $H_{\mathcal{L}}=$..." -> "the tangent kernel is given by $K=$... and the Hessian is $H_{\mathcal{L}}=$..."
	- "As wide networks are close to their linear approximations" -> "As wide networks are close to their linear approximations when in the NTK regime"
- When defining the AGOP alignment in page 4, the "true model" $f^*$ should be defined more rigorously. Since $w$ is the set of parameters for any given model throughout the paper, one could say something along the lines of "let $w$ be the parameters for the trained model, and $w^*$ be the parameters minimizing the population objective or a reference model that achieves SoTA accuracy on a test set". At this point, the reader can be confused to what exactly is the true model, as with an arbitrary dataset and model architecture, you don't always have access to the data-generating model.
- First sentence in Section 3.1: "eigenvalues" -> "eigenvectors" 
- It's better to move Definition 2 to the beginning of Section 4, where AGOP alignment first show up in experiments and discussion.

### Questions
- Why does the critical step size only depend on the initialization and not varying throughout training?
- Paragraph under Claim 1: shouldn't it be $\mathcal{P}\mathcal{L}_n$ instead of  $\mathcal{P}\mathcal{L}_5$ that corresponds to the the spike in the training loss? Is $\mathcal{P}\mathcal{L}_5$ even plotted somewhere that I missed?
- **Choice of top eigenspace dimension $s$**: 
	- The first sentence after this  - I'm confused by what this sentence is trying to convey, especially the second part. What linear dynamics? 
	- So you expect to need a larger $s$, and turns out a small $s$ is sufficient to produce the catapults in the top-$s$ eigenspace. Do you have an explanation to why this contradicts to what you expect? My guess is that $s$ corresponds to the support vectors in some sense, but I'm also uncertain. Is there a way to verify this?  
- Eq (6): $\mathbf{f}(X_{\mathrm{batch}})$ has the same length as the number of examples in the batch. But the projection operator acts on prediction vectors of length $n$. Is something off here or am I misunderstanding? 
- Do you need to recompute $\eta_{\mathrm{crit}}(X_{\mathrm{batch}})$ for each batch? How does it work? 
- I think more motivation for "AGOP alignment is a good measure for generalization" can be given. As a simple example, one can consider the classic low-rank matrix sensing problem 
$$
L(U) = \frac{1}{2n}\sum_{i=1}^n ( \langle A_i,UU^\top \rangle - y_i )^2
$$
where the labels are generated via $y_i= \langle A_i, X^* \rangle$ for some positive semidefinite low-rank groundtruth $X^*$. Since $G$ and $G^*$ can be derived in closed form, does high AGOP alignment imply high generalization in terms of $\Vert UU^\top - X^*\Vert_F$? 


### Minor suggestions
- Latin words such  as *a priori* should be italicized 
- Figure 1 caption: training loss "of" SGD -> training loss "when optimized using" SGD 
- Table 2: please use $0.01$ or $10^{-2}$ instead of 1e-2 to present hyperparameters used.
- Page 2: sentence starting with "Namely, we project the residual..."
	- Up to this point, the paper has not mentioned that it only looks at the MSE loss, so readers who expect the authors to also study the logistic/cross-entropy loss may be confused why you are projecting the residual.
- The experimental details section (E) can be improved in terms of writing: there are many dangling paragraphs with only one or two sentences, which break the flow of the writing and reads more like bullet points that don't belong together. 
- Section E, 3rd paragraph: "the test error refers to the classification error" -> "the test error refers to the classification error on the test split"
- I may be overly fussy about this or have interpreted something incorrectly, but in the related work section, the authors say that "In Cohen et al. (2020)", it was conjectured that at EoS, there are numerous catapults". To me it's more like Cohen et al. "observed" numerous catapults at EoS, but conjectured that EoS and catapults have the same underlying cause.
- Page 4 second paragraph: 
	- "the tangent kernel $K=$... and $H_{\mathcal{L}}=$..." -> "the tangent kernel is given by $K=$... and the Hessian is $H_{\mathcal{L}}=$..."
	- "As wide networks are close to their linear approximations" -> "As wide networks are close to their linear approximations when in the NTK regime"
- When defining the AGOP alignment in page 4, the "true model" $f^*$ should be defined more rigorously. Since $w$ is the set of parameters for any given model throughout the paper, one could say something along the lines of "let $w$ be the parameters for the trained model, and $w^*$ be the parameters minimizing the population objective or a reference model that achieves SoTA accuracy on a test set". At this point, the reader can be confused to what exactly is the true model, as with an arbitrary dataset and model architecture, you don't always have access to the data-generating model.
- First sentence in Section 3.1: "eigenvalues" -> "eigenvectors" 
- It's better to move Definition 2 to the beginning of Section 4, where AGOP alignment first show up in experiments and discussion.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
