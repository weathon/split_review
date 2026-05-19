# Does SGD really happen in tiny subspaces?

- Decision: Accept
- Scores: 6, 3, 8, 6

## Abstract
Understanding the training dynamics of deep neural networks is challenging due to their high-dimensional nature and intricate loss landscapes.
Recent studies have revealed that, along the training trajectory, the gradient approximately aligns with a low-rank top eigenspace of the training loss Hessian, referred to as the dominant subspace.
Given this alignment, this paper explores whether neural networks can be trained within the dominant subspace, which, if feasible, could lead to more efficient training methods.
Our primary observation is that when the SGD update is projected onto the dominant subspace, the training loss does not decrease further.
This suggests that the observed alignment between the gradient and the dominant subspace is spurious.
Surprisingly, projecting out the dominant subspace proves to be just as effective as the original update, despite removing the majority of the original update component.
Similar observations are made for the large learning rate regime (also known as Edge of Stability) and Sharpness-Aware Minimization.
We discuss the main causes and implications of this spurious alignment, shedding light on the intricate dynamics of neural network training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates whether neural networks can be effectively trained by focusing only on the "dominant subspace", which is the top eigenspace of the Hessian of the loss, where the gradient seems to align with. The authors projects SGD updates onto this dominant subspace and find that cannot reduce the training loss further. In contrast, removing the dominant subspace from the updates proves equally effective for training, even though it projects out most of the original gradient component. The authors suggest that the alignment between the gradient and the dominant hessian subspace is "spurious". This "spurious" alignment appears consistently across various practical settings, such as the Edge of Stability, Sharpness-Aware Minimization, and when using momentum or adaptive optimizers. The authors also discuss the possible main causes of the phenomenon, and propose some toy models to understand it.

### Strengths
This paper systematically investigates the phenomenon of gradient-Hessian alignment in various optimization algorithms, including SGD, GD in the Edge of Stability (EoS) regime, and the Sharpness-Aware Minimization (SAM) algorithm, with a particular emphasis on the analysis of SGD. Previous studies have primarily focused on understanding full-batch algorithms like GD or Adaptive GD without stochasticity. 

Moreover, this work takes an initial step toward understanding the 'spurious' alignment where the actual useful component of the gradient is the non-dominant part. They also claim that batch noise is the cause of this alignment by introducing a toy model to provide theoretical intuition. Though it is not very precise to say the mechanism is totally different between GD and SGD (see weakness), I believe the **"ill-conditioned-valley" view of loss landscape** captures why dom-GD doesn't decrease the loss but bulk-GD does.

### Weaknesses
First, the so-called 'spurious alignment' is long observed in EoS literature in my opinion. For example, Damian et al. [2] showed that in the EoS regime, (1) the gradient alignment happens (2) the loss decrement in the EoS regime depends on the constrained trajectory **by projecting out the top eigenspace**. It is exactly the finding listed in section 5.1 of this paper that bulk-GD is as effective as GD. I believe the authors should discuss those related works.

The author may argue that "The mechanisms behind gradient alignment differ between GD with large learning rates and SGD with small learning rates." so their findings are novel. But that is also my primary concern of the paper's conclusion "Stochastic noise is the cause of spurious alignment". I agree that "stochastic noise is part of the cause of spurious alignment", but I don't think the alignment mechanism is intrinsically different between GD and SGD.

In section 4. The authors define the "small LR regime" and "large LR regime" of SGD and claim they are different by setting the threshold of $2/\lambda_1$ of the learning rate. This threshold is for the GD descent lemma to hold. Then the authors claim in the small LR regime, the cause of the spurious alignment is the gradient noise. They 'verify' their findings by switching SGD to GD, and observe that the alignment disappears. However, [1] found that SGD begins to oscillate within the top eigenspace smaller than $2/\lambda_1$. An intuitive explanation for this is **injected gradient noise increases the second order term of the Taylor expansion**, making the loss begin to oscillate **when the learning rate is below $2/\lambda_1$** as the descent lemma predicted. In this case, GD is still stable and descent lemma holds, quickly converging back to the "bottom of the valley". That is why the alignment disappears after switching to GD, since after it's in the "bottom of the valley" the gradient component in the top eigenspace will be very small. 

Therefore, my argument is that stochastic noise indeed reduces the threshold of learning rate for oscillation and makes it easier to have spurious alignment. But the mechanism is the same: the self-stabilization effect induced by the gradient(+noise) within the top Hessian subspace. **To test this argument, the author should also calculate the full gradient when "spurious alignment" happens and see if the full gradient aligns with the top eigenspace. Also, the experiments should include various batch sizes to test different levels of gradient noise.** If my conjecture holds, I think this work can be seen as a generalized empirical validation of self-stabilization [2] for SGD, which somehow limits the novelty of this paper. I might also be wrong, so if the conjecture is not correct, I will raise my score.

The author also did some small learning rate GD in Appendix D.1 to corroborate their argument. I wonder what is the learning rate of the "small learning rate"? In the original EoS paper, most of the figures will exhibit EoS due to progressive sharpening when the model is trained for a long time. Also, the authors use the cross-entropy loss, where EoS may not happen due to some margin-maximization effect. What if the authors switch to square loss? I believe when you enter the EoS regime (when trained with enough time),  the gradient alignment phenomenon will also appear.

The authors' toy examples constructed the two loss functions to introduce the gradient noise. However, I don't think this reflects the real-world gradient noise, since the 100xy term is artificially added to introduce gradient components in $x$-direction unless $y = 0$. But I think injecting some Gaussian noise biasing toward $x$-direction may also work for the toy case. It would be great to have some empirical evidence as to why the authors believe the gradient noise has a larger component in the top eigenspace.

[1] Lee, Sungyoon, and Cheongjae Jang. "A new characterization of the edge of stability based on a sharpness measure aware of batch gradient distribution." The Eleventh International Conference on Learning Representations. 2023.

[2] Damian, Alex, Eshaan Nichani, and Jason D. Lee. "Self-Stabilization: The Implicit Bias of Gradient Descent at the Edge of Stability."

### Questions
1. Can the authors calculate the full gradient when "spurious alignment" happens? Does that also align with the Hessian's top eigenspace? Or it has a very small similarity?
2. Can the authors experiment with some kind of Gaussian noise for the toy example? And can you empirically show why they believe the stochastic noise has a larger bias in the top-eigenspace?
3. For Appendix D.1, can the authors (1) report the learning rates (2) train with longer time s.t. EoS happens (3) add experiments with MSE loss?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper investigates that neural nets cannot be trained within the dominant subspace (i.e., along sharp directions).

### Strengths
Many recent papers (Blanc et al., 2022; Li et al., 2022) highlight that the dynamics in bulk subspace (i.e., along flat directions) are crucial for SGD/SAM to move to flat minima, thereby improving generalization.
In contrast, this paper emphasizes the significant role of the dynamics in bulk subspace (i.e., along flat directions) in relation to optimization.

### Weaknesses
My primary concern are (i) the paper does not sufficiently explain the main finding, i.e., why only the dynamics in the bulk subspace are crucial for optimization, and (ii) the novelty of many contexts:

- Section 4. This section focus on the alignment between the stochastic gradient and the sharp directions. However,

  - This section fails to adequately explain the main finding: why only the dynamics in the bulk subspace are crucial for optimization, expect for a very toy model.

  - Even regarding the alignment between stochatic gradient and the loss landscape, there are numerous previous works that address this point: $\mathbb{E}[g_tg_t^T]\approx 2 L(\theta)\nabla^2 L(\theta_t)$ (Wojtowytsch, 2021; Mori et al., 2022; Wu et al., 2022; Wang and Wu., 2023), implying that stochastic gradient concentrate more along sharp directions of the landscape (i.e., the bump directions). It appears that the authors have overlooked these works.

- Section 5. This section demonstrates that the gradient of GD aligns with the sharp directions in Edge of Stability (EoS), However, 

  - The authors do not explain the main finding: why only the dynamics in the bulk subspace are crucial for optimization.

  - Regarding the alignment between the gradient and sharp directions, this has beed well studied in (Arora et al., 2022; Lyu et al; 2022; Damian et al., 2023) that this occurs due to approximate power iterations). However, the authors do not provide new insights.

### Questions
- The experiments focus on the optimization comparsion between SGD, Bulk-SGD, and Dom-SGD. 
What are the generalization differences among these methods, particularly in the experiments conducted on MNIST and CIFAR, as shown in Figure 1?

- Could the authors provide sufficient theoretical explanation for the main finding?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper challenges existing assumptions about stochastic gradient descent (SGD) learning within a low-dimensional dominant subspace defined by the top eigenvectors of the Hessian of the loss. The authors find empirically that while gradients appear to align with this dominant subspace during training, projecting updates solely into this subspace (Dom-SGD) halts learning. Instead, projecting updates onto the orthogonal "bulk" subspace (Bulk-SGD) is as effective as standard SGD, suggesting that meaningful learning occurs outside the dominant subspace.

### Strengths
The paper addresses a question of significant interest in the ML community regarding SGD's effectiveness in low-dimensional subspaces. It helps address potential misconceptions arising from the well-cited work of Gur-Ari et al. (2018), which suggests that gradient descent would occur primarily within a tiny subspace.

A convincing quadratic toy model effectively reinforces the authors’ interpretation of the empirical results, lending credibility to their main conclusions.

The paper is well-structured, with a logical flow that makes the argument easy to follow and the findings readily accessible to readers.

Gur-Ari et al. (2018): https://arxiv.org/abs/1812.04754

### Weaknesses
Although the paper includes experiments on three datasets, training is restricted to small subsets (e.g., 5,000 of 50,000 samples of CIFAR10) and primarily uses mean squared error loss instead of cross-entropy, despite focusing on classification tasks. This may limit the generalizability of the findings and should be communicated more clearly.

The paper exclusively examines the effects on training loss, with no analysis of test accuracy under Dom-SGD and Bulk-SGD. Including at least one plot of test performance would offer valuable insights into the practical implications for readers.

### Questions
Why did the authors limit their experiments to a small subset of the datasets and can the authors share any insights for training with the full dataset?

Could the authors provide any test accuracy results for Dom-SGD and Bulk-SGD to offer some insight into their impact on model generalization? When Bulk-SGD performs similarly to SGD in terms of training loss, does this trend hold for test accuracy as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is built on recent studies that claim the gradients during neural network training live in a small subspace spanned by the top few eigenvectors of the Hessian. The authors decompose the gradients into the dominant component that lives in the dominant space and the bulk component that is orthogonal to the subspace. They find that dominant component of the gradient does not contribute to decreasing the training loss, while the bulk component, though only accounts for a small portion of the total gradient magnitude, is the main source driving the reduction in the loss. Through different experiments, the authors demonstrate that this observation holds for SGD, GD on the edge of stability, SAM, and adaptive optimizers. The authors also discuss potential explanations from a loss landscape perspective.

### Strengths
The paper is well written with a clear structure and compelling experimental results. The design of the experiments is sophisticated, covering both Dom-SGD and Bulk-SGD setups, along with more nuanced experiments like switching between SGD and GD during training. These additional experiments strongly support the paper’s claims, adding robustness to the argument. Additionally, the observations found in this paper is interesting and should contribute to a better understanding of the training dynamics of deep neural networks.

### Weaknesses
Major point:

1.	Generalization: The authors acknowledge in the limitation that this paper does not consider the generalization part. However, in modern deep learning, generalization error is usually more important than training loss. And it is widely believed that SGD has an implicit bias that benefits generalization (arxiv: 1611.03530, 2006.08680, 2306.04251, etc.). The absence of results or discussion on generalization weakens the paper. Including an analysis of generalization effects could significantly enhance the paper's impact.

2.	Bulk-SGD and noise: The results suggest that Bulk-SGD is less noisy than SGD (e. g. in Fig. 1) and Bulk-GD is less noisy than GD (Fig. 9). This reduction in noise may explain the speedup observed in Fig. 9 and 10. On the other hand, it is unclear how this will affect generalization. The authors have not adequately addressed this part in the paper, and I suggest including a more thorough discussion around that.

3.	Dom-SGD and loss increase: It appears that with cross-entropy loss or using a standard architecture (VGG-11) (Fig. 14 and 17), the loss increases if training with Dom-SGD. This is a surprising finding and I think the authors should discuss this phenomenon more explicitly in the main text. Additionally, the absence of training curves for Bulk-SGD in these figures raises questions. Is there a reason for not including the curves for Bulk-SGD? I am also wondering whether this increase in the training loss relates to findings in prior works: arxiv: 2107.11774, 2306.04251.


Minor point:

1.	For results shown in table 1, the authors calculate the effective learning rates over the first 1000 steps. However, the authors also show that the alignment usually happens after some warm-up steps (e. g. Fig. 3). I think it makes more sense to plot the effective learning rates as a function over time (if noise is a concern, then perhaps run some kind of EMA). 

2.	Although the toy quadratic model explains the observations well, the source of randomness seems a little contrived. I suggest incorporating the discussion of another model at least in the appendix, where the noise is Gaussian noise directly added on to the gradients, for a more natural comparison.

### Questions
Instead of computing the subspace based on the Hessian of the full loss, what if the subspace were computed based on the Hessian of the mini-batch loss. Would alignment still hold? Do the findings in the paper still hold?

### Soundness
3

### Presentation
4

### Contribution
2
