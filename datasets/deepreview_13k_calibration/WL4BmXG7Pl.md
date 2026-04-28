# Crafting Heavy-Tails in Weight Matrix Spectrum without Gradient Noise

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 6, 3

## Abstract
Training strategies for modern deep neural networks (NNs) tend to induce a heavy-tailed (HT) empirical spectral density (ESD) in the layer weights. While previous efforts have shown that the HT phenomenon correlates with good generalization in large NNs, a theoretical explanation of its occurrence is still lacking. Especially, understanding the conditions which lead to this phenomenon can shed light on the interplay between generalization and weight spectra. Our work aims to bridge this gap by presenting a simple, rich setting to model the emergence of HT ESD. In particular, we present a theory-informed analysis for `crafting' heavy tails in the ESD of two-layer NNs without any gradient noise. This is the first work to analyze a noise-free setting and incorporate optimizer (\texttt{GD/Adam}) dependent (large) learning rates into the HT ESD analysis. Our results highlight the role of optimizer-dependent learning rates on the Bulk+Spike and HT shape of the ESDs in the early phase of training, which can facilitate generalization in the two-layer NN. These observations shed light on the behavior of large-scale NNs, albeit in a much simpler setting. Last but not least, we present a novel perspective on the ESD evolution dynamics by analyzing the singular vectors of weight matrices and optimizer updates.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the heavy tail phenomenon of the spectrum of weight matrices and its impact on generalization.  The paper presents a theorem for single step of Adam which shows an emergence of "Bulk + spike" spectrum. It futher empirical evaluates how this spectrum evolves into a heavy tail.

### Strengths
a) The paper extends the single step analysis of GD Ba et. al. for Adam.   
b) The observation that bulk + spike evolves into a heavy tail is interesting.

### Weaknesses
a) The paper lacks sufficient motivation for the problem setting and the relevance of the chosen algorithm, leaving it unclear why this is an important quantity to study. Notably, both the heavy-tail mechanism and strong generalization stem from learning the single-index direction, making it uncertain whether the heavy tail is simply a byproduct of good generalization or its cause. Consequently, it is challenging to assess whether this problem setting and analysis truly captures the influence of the heavy-tail spectrum on generalization.

b) The empirical analysis is restricted to single-index teachers and two-layer networks, which limits the study's scope and makes it insufficient to determine whether any findings are broadly applicable.

c) The theoritical analysis does not capture how "BULK + spike" transition into a heavy tail phenomenon. Hence the paper falls short of theoritically understanding the emergence of HT-ESD - the theoritical analysis is only captures the BULK + spike shape of spectrum after a single step of Adam.

Minor :
- Make a consistent notation of $\beta^{*}$ through out the paper.
- The inline math can be formatted better to ensure better readbility.

### Questions
discussed above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper aims to investigate the relationship between heavy tails in the weight spectrum distribution of neural networks and the ability of the network to generalize over unseen samples. The authors set up a teacher-student setting where a two-layer neural network learns a single-index model. First, the paper shows that for a sufficiently large step size, the full-batch Adam can align with the teacher's direction in just one step, corresponding to a spike in the ESD emerging from the initial mass. The analysis continues by empirically showing that the dynamics of the ESD evolves from the bulk to a heavy tail distribution. Finally, the paper shows the connection between the ESD heavy tails and the orientation of the singular vector of weight updates.

### Strengths
- To my knowledge, this paper is the first to study the HT-generalization correspondence in the single-index teacher-student setting. Altough not bringing any revolutionizing idea, the paper establishes an important first step towards understating this phenomenon within the community.
- The analysis is comprehensive and precise, also taking into account techniques used in practice such as weight normalization and learning rate schedulers.

### Weaknesses
 - The paper is showing mostly empirical result. In this theoretical setting one might expect to have more theoretical support of the claims.

 - In line 241, shouldn't we divide the similarity by the norm of $u_1$? Otherwise it can grow even if $u_1$ and $\beta$ are not getting more aligned

 - In line 308 you talk about a sweet for $\eta$, but I can't see it in the figure, can you clarify?

Minor:
- Line 297: $\eta=0.1$, but the figures says $\eta=1.$

### Questions
- In line 241, shouldn't we divide the similarity by the norm of $u_1$? Otherwise it can grow even if $u_1$ and $\beta$ are not getting more aligned
- In line 308 you talk about a sweet for $\eta$, but I can't see it in the figure, can you clarify?

Minor:
- Line 297: $\eta=0.1$, but the figures says $\eta=1.$

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is interested in understanding the evolution of the empirical spectral distribution for the first-layer weight matrix in a two-layer neural network during training. The paper considers a student teacher (single index model) with Gaussian. It shows that early-stage feature learning occurs for a much smaller step size for Adam compared to GD. 

The paper also empirically studies the spectrum's evolution during further training and claims the existence of the initial spike is needed to transition to the heavy-tailed phase. Finally, the paper looks at various kernel alignment metrics, their evolution, and correlation with generalization.

**Justification for Score**

I think overall the paper presents intersting insights for a different optimizer. Hence I think it is worth accepting. However, the paper doesn't always position itselves in the most informative way compared to prior work and I have concerns about the significance of the spike that has been seen. Hence I do not give it a higher score.

### Strengths
**Novelty:** As far as I know, the theoretical works on the early-stage emergence of spikes have been primarily limited to gradient descent. No theoretical work I know of analyzes Adam. Hence I think this is a novel contribution of the paper. Additionally, the insight that Adam requires a smaller step size than gradient descent to see the spike is important. 


**Clarity:** The paper is mostly well-written. My one concern is that when people talk about the spiked structure (Ba et al, Moniri et al). they mean for the features $F = \sigma(WX)$ and not for the weight matrix $W$. This was confusing at first.

### Weaknesses
 **Originality:** In terms of originality, the paper should do a better job of positioning itself with respect to Martin and Mahoney,  Ba et al., and Moniri et al. I think this is important. 


**Significance:** I think the result on smaller step size results in spikes is significant. If this were a result as presented in Moniri et al. However, as a result is currently presented, I am not sure the theory result says enough. Specifically, 

1. The paragraph after the corollary is clear to me. The step size scales are different for the spectral norm and the Frobenius norm. How do we rationalize this to show that there is a spike?

2. Spikes in $W$ do not necessarily correspond to spikes in $F$. Especially if you have Gaussian Data. See [1] (flipping the role of $W$ and $X$).

### Questions
1. Generalization with Heavy-Tailed models. Do the authors know of any works that theoretically characterize the generalization error of models with heavy tails? Even in the regression setting I know of [2]. Also, do the authors know about papers that consider generalization error for models with spiked covariance (besides the Ba et al. 2023 paper), again including regression. 

[2] Wang, Yutong, Rishi Sonthalia, and Wei Hu. "Near-interpolators: Rapid norm growth and the trade-off between interpolation and generalization." International Conference on Artificial Intelligence and Statistics. PMLR, 2024.

2. Emergence of heavy tails. For $\eta=0.1$, the experiment needed $t \sim 10^4$. However, the authors claim $t \sim 10^4$ was not enough for $\eta = 0.01$. I imagine we need more steps, maybe even something like $t \sim 10^7$.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The submission studies an interesting problem. When does HT-ESD happen? Why does it lead to good generalization?

The key results are below:

1. Using a toy model,  ADAM after one step can provably induce a spike in spetrum. (thm 4.1)

2. With experiments, the authors show that bulk decay happens (Fig 4), and that spike + decay leads to heavy tail.

3. With experiments, the authors show that successful feature learning happens when the spectrum has the right tail exponent. (fig 5)

##Strength:##

I like the experiment part of this work.  In particular, comparing ADAM vs GD in Fig2 Fig3, and demonstrating the decay in Fig 4. 

I think the perspective is novel. The spectrum distribution not only results from the minibatch noise but also from full batch updates.

##Weakness:##

Although I enjoy reading the work, I am not confident that the authors successfully answer the questions asked.

1. The spike after one large update is trivial. Given the backprop structure of neural net, one step update to the weight is rank one. When the step is large, one gets a rank-one spike.

2. The paper demonstrates that decay happens without explaining why. More specifically, does the decay happen just correctly such the spectrum is heavy tailed?

3. The paper demonstrates that the tail index should be in the correct range for the features to be learned. However, no explanation is given. Further, the experiments for this result are synthetic and toy.

I am happy to update my review if the authors could address the above concern.


##Minors:##

What is u in line 241?

### Strengths
See summary

### Weaknesses
Although I enjoy reading the work, I am not confident that the authors successfully answer the questions asked.

1. The spike after one large update is trivial. Given the backprop structure of neural net, one step update to the weight is rank one. When the step is large, one gets a rank-one spike. This is particularly true when considering the update as a function of the outer product of the input and the activation, which is inherently rank one. The authors need to clarify how the specific structure of the neural network and the optimization algorithm interact to produce this spike, and why it is not simply a consequence of the rank-one update.

2. The paper demonstrates that decay happens without explaining why. More specifically, does the decay happen just correctly such the spectrum is heavy tailed? The authors show the decay, but the mechanism that leads to the specific heavy-tailed shape remains unclear. It is not sufficient to show that decay occurs; the paper needs to explain why the decay follows a power-law distribution, and what conditions are necessary for this specific type of decay to emerge. The connection between the decay and the heavy-tailed spectrum is not rigorously established.

3. The paper demonstrates that the tail index should be in the correct range for the features to be learned. However, no explanation is given. Further, the experiments for this result are synthetic and toy. The paper needs to provide a theoretical justification for why a specific range of tail indices is optimal for feature learning. The current experiments, being synthetic, do not provide sufficient evidence that this phenomenon generalizes to real-world datasets and more complex architectures. The authors should provide a mechanistic explanation for why the tail index affects feature learning, and why a specific range is optimal.

### Questions
See summary

### Soundness
3

### Presentation
3

### Contribution
2
