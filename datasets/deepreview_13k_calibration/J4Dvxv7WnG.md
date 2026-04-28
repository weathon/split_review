# Learning Dynamics of Deep Matrix Factorization Beyond the Edge of Stability

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Deep neural networks trained using gradient descent with a fixed learning rate $\eta$ often operate in the regime of ``edge of stability'' (EOS), where the largest eigenvalue of the Hessian equilibrates about the stability threshold $2/\eta$. 
Existing theoretical analyses of EOS focus on simple prototypes, such as scalar functions or second-order regression models, which limits our understanding of the phenomenon in deep networks. In this work, we present a fine-grained analysis of the learning dynamics of (deep) linear networks (DLN) within the deep matrix factorization loss beyond EOS. For DLNs, loss oscillations within EOS follow a period-doubling route to chaos. We theoretically analyze the regime of the 2-period orbit and show that the loss oscillations occur within a small subspace, with the dimension of the subspace precisely characterized by the learning rate. Our analysis contributes to explaining two key phenomena in deep networks: (i) shallow models and simple tasks do not always exhibit EOS and (ii) oscillations occur within top features. We present experiments to support our theory, along with examples demonstrating how these phenomena occur in nonlinear networks and how they differ from those in DLNs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the learning dynamics of deep linear networks trained using gradient descent at a fixed learning rate, especially beyond the edge of stability (EOS) regime.

Using the singular value stationary set and the strictly balancing assumptions (both can be validated in examples), the paper argues that within the EOS regime, periodic 2-period fixed orbit oscillations occur in a low-dimensional subspace, with the subspace dimension determined by the learning rate. This phenomenon explains the presence of oscillations within top features. Additionally, the paper compares the difference between deep linear networks and diagonal linear networks in the EOS regime, offering insights into how network structure impacts training dynamics. Experiments further reveal that fine-tuning with large learning rates in LoRA for low-rank adaptation of large language models induces "catapult dynamics," which can potentially improve generalization.

### Strengths
This work is both theoretically rigorous and experimentally thorough. The theoretical results are new to me, especially Theorem 1, and the proofs are rigorous and not difficult to follow. Additionally, the experiments are extensive and effectively validate the theoretical insights. Overall, the study contributes valuable advancements in understanding and optimizing the training dynamics of deep networks.

### Weaknesses
Although deep linear network shares some similarities with deep nonlinear networks, the claim that ``Our analysis explains two key phenomena in deep nonlinear networks" in abstract seems overstated and exaggerated. In the analysis, the initialization (eqn (3)) is very specific, and it is just a member in the singular vector stationary set. It is not clear if all statements work only based on the initialization (eqn (3)) or for any initialization in the singular vector stationary set. For example, will Lemma 1 and Lemma 2 work with general singular vector stationary initial data?

Why is the period of the fixed orbit is always 2? It seems that it comes from the two-step GD update. How about other periodicities? 

(15)-(16) on page 19-20 seem to have typos.  $\dot{W}_l(t)$ on the left side should be $\dot{U}_l(t)$?

### Questions
1. Why is the period of the fixed orbit is always 2? It seems that it comes from the two-step GD update. How about other periodicities? 

2. (15)-(16) on page 19-20 seem to have typos.  $\dot{W}_l(t)$ on the left side should be $\dot{U}_l(t)$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper analyzes learning dynamics of deep linear networks a.k.a. deep matrix factorization using Gradient Descent (GD) in the Edge-of-Stability (EOS) regime. The paper proves that, under a "strict balanced state" condition of singular values exactly matching across the weight matrices, the top singular values oscillate, leading to oscillations in training loss in the EOS regime. The paper also presents an experiment showing loss oscillations in Low-Rank-Adaptation (LoRA) finetuning on a language modeling task. Results in the paper help explain some observations in existing work.

### Strengths
The EOS oscillation theorems for deep linear networks are novel, and they directly map to simulations of training such networks using GD (Figs 2,3,6). The paper discusses oscillations in smaller subspaces first (Theorem 1), then extends the analysis to larger subspaces (Theorem 2). The theorems help theoretically ground observations seen in existing work, on loss oscillations in the EOS regime. It is curious that these oscillations can be somewhat explained by singular value oscillations in the top subspaces for deep linear networks.

### Weaknesses
There are 3 main weaknesses:

1. While it is useful to understand learning dynamics of deep linear networks from a theoretical perspective*, I'm not sure the results shed light on dynamics in deep nonlinear networks. In fact, the paper misinterprets the result of [1], which show that only for shallow networks are linear and nonlinear networks (2-layer bias-free ReLU networks) similar---for deep networks there is a strict separation in function approximation. [1] reports similarities between deep linear and nonlinear networks under very strong assumptions on data distribution and structure, which this manuscript does not consider. This submission misses this nuance (in abstract and lines 80-83), and overpromises results for deep nonlinear networks. In fact, the manuscript comments about the differences in loss landscapes in Line 511---nonlinear networks have highly irregular landscapes, and when trained with (minibatch) SGD could lead to catapults across regions not just in the vicinity. This is a major weakness in my view. The paper's analysis focuses on the Hessian's top singular values, which may not fully capture the complex dynamics of non-linear networks where the loss landscape is highly non-convex and contains many saddle points and local minima. The behavior of the top singular values in deep linear networks might not directly translate to the behavior of gradients and loss in non-linear networks, especially when considering the effects of non-linear activation functions and the presence of multiple minima.
2. The $\alpha$-scaled initialization scheme is not used in practice, especially for LoRA training where one of the matrix (A) is initialized at 0 and the other (B) with gaussian entries. The paper argues that the results work when initialization leads to convergence to the "singular vector stationary set" (line 148). Why is this not a strong and impractical assumption on how initialization is done in practice? Does random initialization satisfy this condition? The assumption that the network converges to a singular vector stationary set is a strong one, and it is not clear if this condition is met in practice with common initialization schemes. The paper should provide more justification for this assumption, or at least discuss the limitations of this assumption and how it might affect the results. The $\alpha$-scaled initialization, while useful for theoretical analysis, is not a standard practice in training deep neural networks, and it is not clear how the results would generalize to more common initialization schemes.
3. As highlighted in Section 5 by the authors, the assumptions on singular values' "strict balanced state" and initialization's "stationary set condition" are strong. It's not clear if and when they can be met.  The strict balanced state assumption, where singular values exactly match across weight matrices, is a very specific condition that might not hold in practice. The paper needs to provide more discussion on the practical implications of this assumption and how the results might be affected if this assumption is violated. The paper should also discuss how sensitive the results are to deviations from this strict balanced state.

*The authors need not motivate deep linear networks by (wrongly) arguing their similarity to deep nonlinear networks; linear networks have been studied in the ML optimization research for a while now.

# Experiments
Section 4.2 LoRA initialization does not match practice. In LoRA, one of the matrices is set to 0 and the other to random, so that $AB^T$ is 0 at finetuning initialization. This is different from the alpha-initialization, which is (1) not random and (2) not starting from 0. I don't think this experiment works well with the theoretical setting studied in this paper---the LoRA finetuning experiment seems ad-hoc when the rest of the paper is about deep linear networks.

Moreover, the "catapult" observation in LoRA experiments is on very shaky ground, since stochasticity affects the training loss and makes it oscillate. The paper mentions this in Line 431, so I'm not convinced that the oscillations are, in fact, "catapults".

A natural experiment to try: In Line 188, step size is suggested to be chosen based on the depth $L$ of the network (as $L$ is larger, smaller values of step size will lead to oscillcations). This is curious to verify.

# Writing
1. In the introduction, 3 observations are described from [2, 3], but it is not clear to me how or which ones the paper addresses. It is also not clear to me how sharpening and catapults from the two papers are related to each other.
2. Definition 2 is introduced abruptly without need or context. There is discussion in Lines 191-195, which can be better placed before/after Def. 2. 
3. The paper is missing a related work section. It is included as Appendix A.1, but I'd suggest cutting down on the main sections to include related work within 10 pages.

### Questions
# High-level questions
1. Theorem 1. Why is this called 1-d subspace oscillation?
2. Figure 2. There are 2 kinks in the EOS regime in the left plot but only 1 is visible in the right plot. Do the authors know why?
3. Section 4.2. The original LoRA paper [1] only applies adaptation to the attention weight matrices. Any reason the authors adapt all weights?
4. Line 450. Pearson correlation between what two quantities? If this is the metric from the STS-B task, then how would this kind of experiment extend to other tasks?
5. Line 474. Why do smooth, low-frequency images correspond to low task complexity? For the CIFAR dataset, number of samples $N$ is used as a proxy task complexity, why? Both datasets are image datasets. It seems to me that I can pick and choose any proxy/hyperparameter from the experiment setup to argue that sharpness does not rise to EOS regime in low complexity tasks.

# Low-level questions
1. Figure 1. What is the pearson correlation in the last plot? A pointer to the relevant section would help.
2. Line 71. What is "sharpening"? First time this term is mentioned.
3. Lines 249-254. Lost here, what are $f_{\Delta_i}$, $x$, and the line? I think more text is needed to explain how the analysis is done for $r$-dimensional oscillations. A figure would really help the reader.

[1] Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., ... & Chen, W. (2021). Lora: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685.


*************
**Update after author response:** I am increasing my review score from 3 to 6 since the authors addressed my [concerns](https://openreview.net/forum?id=J4Dvxv7WnG&noteId=9ZRUV9lccn). The manuscript has been updated significantly, but not to the extent that I do not understand the central claims. Hence, I'm keeping my original confidence score at 3. Thank you to the authors for a good discussion.
*************

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper rigorously analyzes gradient descent dynamics of deep linear networks for deep matrix factorization at the Edge of Stability. Assuming initialization within the singular vector stationary set and strictly balanced weights, the authors characterize a 2-period oscillation within top subspaces. The main insight is that, under these assumptions, the loss can be rewritten as a function of singular values, decoupling the effect of singular vectors. The authors also provide empirical support for the strict balancing assumption, showing that singular values become increasingly balanced during gradient descent dynamics, with numerical experiments aligning well with the theoretical findings.

### Strengths
This paper makes a solid contribution to the theoretical understanding of the Edge of Stability by analyzing gradient descent dynamics in deep matrix factorization. It extends previous studies on deep scalar linear networks [Kreisler et al., 2023], offering a rigorous proof that oscillations in the EoS regime are confined to top subspaces, as empirically observed in prior work [Zhu et al., 2024]. Additionally, the exact characterization of Hessian eigenvalues at convergence under strict balancing provides a valuable technical contribution to deep matrix factorization problem.

---

**References**

[Kreisler et al., 2023] Gradient Descent Monotonically Decreases the Sharpness of Gradient Flow Solutions in Scalar Networks and Beyond, ICML 2023.

[Zhu et al., 2024] Catapults in SGD: spikes in the training loss and their impact on generalization through feature learning, ICML 2024.

### Weaknesses
1. **My main concern is that Lemma 2 does not ensure convergence to strict balancing.** While Lemma 2 shows that the balancing gap decreases with each step, it does not guarantee that this gap converges to zero. The authors suggest that Lemma 2 justifies the strictly balanced assumption, but this needs further clarification. Although Figure 4 empirically shows the gap converging to zero, Lemma 2 alone does not rigorously establish this phenomenon. Specifically, the proof only demonstrates that the balancing gap is non-increasing, i.e., $b(t+1) \leq b(t)$, but it does not show that $b(t+1) \leq c \cdot b(t)$ for some $0 < c < 1$, which is necessary for convergence to zero. This distinction is crucial because a non-increasing sequence can converge to a non-zero value. The authors need to provide a stronger argument to ensure that the balancing gap truly vanishes over time, especially given that the balancing gap is not zero at initialization.

2. **The model fails to capture (non-monotonic) decreasing training loss in the Edge of Stability.** A key characteristic of the Edge of Stability is that training loss oscillates but decreases over time, reflecting unstable convergence (e.g., [Cohen et al., 2021], [Ahn et al., 2022]). In this study’s setup, weights oscillate in a 2-period orbit, causing the loss to oscillate indefinitely without decreasing. This limits the model’s applicability to realistic settings. The model's inability to capture the non-monotonic decrease in training loss, which is a hallmark of the Edge of Stability, is a significant limitation. The authors should address why their model does not exhibit this behavior, and how this impacts the relevance of their findings to practical scenarios.

3. **The claims on LoRA dynamics in Section 4.2 lack sufficient evidence.** The authors claim that using large learning rates in LoRA dynamics leads to oscillations and catapults, enhancing generalization by increasing Pearson correlation. However, Figures 7 and 8 do not clearly show catapult behavior, as oscillations occur even at lower learning rates (e.g., $\eta = 10^{-5}, 10^{-6}$), making it difficult to conclude that catapults are unique to $\eta=10^{-4}$. Additionally, empirical evidence linking catapults to better generalization is insufficient. The claims here seem overstated and less relavant to the main theory. I recommend moving this section to the appendix and avoid making strong claims.


Minor comments
- (Section 3, Page 4, Line 169) Typo: unbold subscript $k$ in $W_k$.
- (Appendix A, Page 14, Line 723) Wrong citation: "Ahn et al. (2022) established the phenomenon in two-layer networks..." is citing the paper [Ahn et al., 2022], but it should be citing another paper [Ahn et al., 2023].
- (Reference, Page 13) Duplicate entries for Zhu et al. (2024) in the reference (Line 692 and Line 696).

### Questions
1. Could the authors please include the following references in the related works section? Prior to [Cohen et al., 2021], [Jastrzebski et al., 2019] and [Jastrzebski et al., 2020] demonstrated that step size influences sharpness along optimization trajectories. Additionally, [Ahn et al., 2023], [Song et al., 2023], and [Karla et al., 2023] provide rigorous analyses of learning dynamics at the Edge of Stability in simplified settings, such as two-layer linear networks. [Zhu et al., 2024] and [Chen et al., 2024] study gradient descent dynamics for quadratic models in large learning rate regimes where catapults occur.

2. When initialization is outside the singular vector invariant set, how do loss and sharpness behave at the Edge of Stability? Specifically, does the weight converge to a period-2 orbit, or does the loss oscillate while decreasing non-monotonically? Similarly, if oscillations begin before strict balance is achieved, how are the loss trajectory and learning dynamics affected? It would be insightful if the authors could provide additional experimental results exploring these scenarios.

---

**References**

[Jastrzebski et al., 2019] On the Relation Between the Sharpest Directions of DNN Loss and the SGD Step Length, ICLR 2019.

[Jastrzebski et al., 2020] The Break-Even Point on Optimization Trajectories of Deep Neural Networks, ICLR 2020.

[Cohen et al., 2021] Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability, ICLR 2021.

[Ahn et al., 2023] Learning threshold neurons via the “edge of stability”, NeurIPS 2023.

[Song et al., 2023] Trajectory Alignment: Understanding the Edge of Stability Phenomenon via Bifurcation Theory, NeurIPS 2023.

[Karla et al., 2023] Universal Sharpness Dynamics in Neural Network Training: Fixed Point Analysis, Edge of Stability, and Route to Chaos, arXiv 2023.

[Zhu et al., 2024] Quadratic models for understanding neural network dynamics, ICLR 2024.

[Chen et al., 2024] From Stability to Chaos: Analyzing Gradient Descent Dynamics in Quadratic Regression, TMLR 2024.

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
This paper analyzes the catapult behaviors of DLNs (Deep Linear Networks) and explains many unexplained observations regarding EOS (Edge of Stability) phenomenon: (i) periodic subspace oscillations (especially in the top subspace that corresponds with more prominent features), (ii) mild (or no) sharpening for simple dataset with low complexity (when the eigenvalue for the strongest feature is too small), (iii) difference between DLNs and DiagLNs (i.e., the architecture matters), and (iii) catapult in LoRA.

### Strengths
- The paper explains many unexplained observations regarding EOS phenomenon.

### Weaknesses
 - Lemma 2 does **not** tell us that the singular values become balanced as $t\rightarrow \infty$ (L191-193). The strictly decreasing balancing gap and the difference being lower bounded by zero does **not** lead to the convergence to zero (L307-309). Think about the sequence $0.5+\frac{1}{t}$. Can you provide a proof to show the convergence to zero?

- "When the learning rate is large enough to induce catapults, we observe that the training loss decreases rapidly ..." 
The statement does not seem right. Large lr may lead to fast decreasing of the training loss because of its large stepsize not because of the catapults. Same for the statement "when the learning rate is small, convergence takes much longer, as the model seems to bounce around within the same local basin before reaching a low training loss". Can you provide an experiment to show that "the catapult implies faster optimization"?

- It is hard to say "in DLNs, self-stabilization does not occur". Actually, also in the original EOS paper, the sharpness oscillates **above** $2/\eta$ (they say "it hovers above $2/\eta$"). It is true that DLNs do not satisfy the condition of the proposition in the self-stabilization paper, but self-stabilization is a broader concept and the threshold may not be necessarily $2/\eta$. The statement should be written carefully.

- In Thm 1, what is $\rho_i(t)$ exactly? It only says that $\rho_i(t)\in \{\rho_1,\rho_2\}$. Does $i$ depend on $t$? As it says that the matrix oscillates, it is likely that $\rho_i(t)$ changes with $t$. Is it $\rho_i(t)=\rho_1$ if $t$ is odd (even) and $\rho_i(t)=\rho_2$ if $t$ is even (odd)? If the readers have to guess the meaning, then it is not well-written.

- What do you mean by that "To show oscillations in two or more subspace, we can easily extend Theorem 1"? Why do we need to set $\lambda_2\geq K>\lambda_3$? I don't think this is a trivial result from Thm 1. Can you elaborate more on the paragraph L241-248? My understanding is that $\rho_i(t)$ in the first term of $W_\ell(t)$ in Thm 1 corresponds to the oscillation, is it right? I didn't fully understand the $r$-subspace oscillation part.

- For the second term $\sum_j \sigma_{\ast,i}u_{\ast,j}v^\top_{\ast,j}$, isn't it $\sigma_{\ast,j}$ with $j$, not $\sigma_{\ast,i}$ with $i$?

- Is there any reason that we can view the adaptations as individual low-rank matrix factorization problems? Can you elaborate more on this? I hope some "math" may help the reader to understand this.

- "Notably, for ranks $r=4$ and $r=8$, there are catapults ... do not occur for $r=1$ or $r=2$". What catapults are you talking about? In Fig 7, it is hard to see the catapult (or loss oscillation) and compare it with other ranks ($r=1,2$). I don't fully understand Section 4.2.
 
- Can you somehow compute or estimate the $\sigma_{\ast,1}$ for Fig 10 (a) and for each image in Fig 10 (b)? It would be better to have a quantitative understanding of the "low-complexity learning".

- L 29-30 (spacing): ... 2020).The -> ... 2020). The
- L415: give a ... -> given a ...

### Questions
The following questions may be related to the weaknesses as the paper may have some unclear points:
- In Thm 1, what is $\rho_i(t)$ exactly? It only says that $\rho_i(t)\in \\{\rho_1,\rho_2\\}$. Does $i$ depend on $t$? As it says that the matrix oscillates, it is likely that $\rho_i(t)$ changes with $t$. Is it $\rho_i(t)=\rho_1$ if $t$ is odd (even) and $\rho_i(t)=\rho_2$ if $t$ is even (odd)? If the readers have to guess the meaning, then it is not well-written.

- What do you mean by that "To show oscillations in two or more subspace, we can easily extend Theorem 1"? Why do we need to set $\lambda_2\geq K>\lambda_3$? I don't think this is a trivial result from Thm 1. Can you elaborate more on the paragraph L241-248? My understanding is that $\rho_i(t)$ in the first term of $W_\ell(t)$ in Thm 1 corresponds to the oscillation, is it right? I didn't fully understand the $r$-subspace oscillation part.

- For the second term $\sum_j \sigma_{\ast,i}u_{\ast,j}v^\top_{\ast,j}$, isn't it $\sigma_{\ast,j}$ with $j$, not $\sigma_{\ast,i}$ with $i$?

- Is there any reason that we can view the adaptations as individual low-rank matrix factorization problems? Can you elaborate more on this? I hope some "math" may help the reader to understand this.

- "Notably, for ranks $r=4$ and $r=8$, there are catapults ... do not occur for $r=1$ or $r=2$". What catapults are you talking about? In Fig 7, it is hard to see the catapult (or loss oscillation) and compare it with other ranks ($r=1,2$). I don't fully understand Section 4.2.
 
- Can you somehow compute or estimate the $\sigma_{\ast,1}$ for Fig 10 (a) and for each image in Fig 10 (b)? It would be better to have a quantitative understanding of the "low-complexity learning".

- L 29-30 (spacing): ... 2020).The -> ... 2020). The
- L415: give a ... -> given a ...
-

### Soundness
3

### Presentation
2

### Contribution
3
