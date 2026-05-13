# When Are Bias-Free ReLU Networks Effectively Linear Networks?

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
We investigate the expressivity and learning dynamics of bias-free ReLU networks. We firstly show that two-layer bias-free ReLU networks have limited expressivity: the only odd function two-layer bias-free ReLU networks can express is a linear one. We then show that, under symmetry conditions on the data, these networks have the same learning dynamics as linear networks. This allows us to give closed-form time-course solutions to certain two-layer bias-free ReLU networks, which has not been done for nonlinear networks outside the lazy learning regime. While deep bias-free ReLU networks are more expressive than their two-layer counterparts, they still share a number of similarities with deep linear networks. These similarities enable us to leverage insights from linear networks, leading to a novel understanding of bias-free ReLU networks. Overall, our results show that some properties established for bias-free ReLU networks arise due to equivalence to linear networks, and suggest that including bias or considering asymmetric data are avenues to engage with nonlinear behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies what functions bias-free ReLU and leaky ReLU networks can represent and what the training dynamics are. A difference between two-layer networks and deeper networks is established. Specifically, it is observed that such bias-free networks that are limited to two layers cannot express any odd function except linear ones. However, the exists non-linear odd functions that can be expressed if the network has at least three layers. It is also established that under certain assumptions on the training data, the training dynamics of bias-free two-layer (leaky) ReLU networks is essentially the same as that of linear networks.

### Strengths
The paper is predominantly theoretical and full proofs are provided. The experimental parts complement the paper well and illustrate the theoretical findings.

The presentation is very good and polished and the main claims in the paper are clearly presented.

Understanding the expressiveness and training dynamics of different network architectures is important. The impact of removing bias from the architecture is also an interesting topic to study, in particular, as the authors point out, because in analytical studies of networks, bias terms are sometimes omitted for simplicity. The results on expressiveness of bias-free networks are mostly relatively simple observations. Understanding the training dynamics is much more involved.

Formally studying training dynamics is important, interesting, and challenging. This paper makes some welcome contributions. I found Section 5 as well as the discussion on "perturbed symmetric datasets" particularly intriguing.

### Weaknesses
The main limitation of the results on training dynamics is that the results are limited to the case that the target model is odd (in addition to some more mild assumptions). Specifically, it is shown that in this case, two-layer bias-free (leaky) ReLU networks essentially behave like a linear network. There is evidence that even slight violations of this property of the target model, make the network behave in a non-linear way in later phases of training. I appreciate that it is challenging, but deriving training dynamics for more different types of datasets would of course benefit the work.

In the writeup, I think it would be helpful to reemphasize the core assumption made on the target model more explicitly in places where the results are summarized or discussed. For example, in Section 6, in the sentence "Theorem 7 shows that under symmetry conditions on the dataset, two-layer bias-free (leaky) ReLU networks have the same time evolution as a linear network (modulo scale factors)", the phrase "symmetry conditions" does a lot of heavy lifting and it may be helpful to be more explicit about what Condition 3 says.

The authors could clarify that Assumption 5 is only for the initialization.

### Questions
Is there any possibility of deriving the empirical results in Section 5 analytically? In terms of results, this is possibly the most interesting part of the paper. What are the main difficulties in doing so?

It would also be interesting to somehow quantify the observed lack of robustness when a two-layer bias-free network is trained on a dataset that nearly satisfies Condition 3. Although, once again, I appreciate this may be a very challenging task.

### Soundness
4

### Presentation
4

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
The paper studies the bias-free ReLU and leaky-ReLU networks, both two-layer networks and deep ones. The authors show that bias-free two-layer ReLU and leaky ReLU networks have limited expressivity, and cannot express non-linear odd functions. Showing that deep bias-free ReLU networks can express non-linear odd functions, the paper establishes a separation between bias-free deep and shallow networks. Additionally, the authors analyze the dynamics of training bias-free shallow networks under some distributional assumptions, showing theoretically and experimentally that their dynamics follows the dynamics of linear networks. Additionally, the authors provide some insights on the dynamics of deep bias-free ReLU networks.

### Strengths
The paper gives novel insights on both expressivity and optimization of bias-free networks. As these networks have been studied often in prior theoretical works, discussing their limitations sheds new light on the conclusions from past theoretical works. Additionally, while ReLU networks often are trained with bias in practice, in certain situations bias-free networks have been used in practice, and thus understanding their behavior and limitation is important. The insights on the dynamics of these networks, drawing the connection to linear networks which are much better understood theoretically, helps advance our theoretical understanding of the dynamics and solutions found by ReLU networks.

### Weaknesses
- Previous work by Basri et al. (cited by the authors) shows that two-layer bias free networks cannot express non-linear odd functions when the inputs are uniformly distributed. The authors claim that the result in the paper is stronger, but it's not clear to me that this is the case. My understanding is that the authors show: for any non-linear odd function $f$, for any bias-free (leaky) ReLU network $h$, there exists some input $x$ such that $f(x) \neq h(x)$. My understanding is that Basri et al. shows a stronger result: for $x$ sampled from the uniform distribution, $f(x) \neq h(x)$ (with high probability?). It is possible that I am misunderstanding either the Basri et al. result or the result shown in the paper, so I would appreciate it if the authors clarify this point. In any case, I believe that writing the result in the paper more formally with the right order of quantifiers will help clarify things.
- The fact that bias-free ReLU networks are very limited is already evident from the somewhat trivial (and previously observed) fact that bias-free ReLU networks can only express positively homogenous functions. While the results shown in the paper are indeed stronger, showing that the networks cannot express a larger family of functions, it is worth emphasizing that the fact that bias-free ReLU networks are very restricted is not a novel contribution of this work.
- The introduction of Assumption 5 feels a little bit without context and missing some details. Is this an assumption on the initialization? Throughout the network training? What is the vector $r$ - is this satisfied for some $r$? It would be helpful to write this more formally, and clarify these points.
- The bottom-line result/message of Section 5 is not clear. If the main point is stating a conjecture, it is worthwhile to state more precisely what the conjecture is, and how it is supported by the experiments.

### Questions
- The main result on the dynamics of bias-free networks (Theorem 7) is shown for infinite data (training on the distribution) and with gradient flow. How would these results change for finite data and/or training with GD/SGD?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper compares the gradient descent dynamics of ReLU networks with no bias to linear networks. First, the authors show that two-layer bias-free networks have limited expressivity. Next, the main result (Theorem 7) is that for "symmetric datasets" (Condition 3) and under a specific initialization (Assumption 5), the gradient flow trajectories of a two-layer ReLU network and a linear network are the same, up to weight and time-rescaling. The authors also consider extensions to other data distributions (such as orthogonal or XOR), and ReLU networks with depth > 2.

### Strengths
- Prior theoretical work considers networks with no bias, and thus it is an interesting question to understand the expressivity and learning dynamics of such networks.
- The proofs appear to the best of my knowledge to be sound, and the paper is well-written and easy to follow.

### Weaknesses
- My main concern with the paper is that I find the contribution to be rather incremental, which limits the significance/impact of the work. For example, Theorem 7 requires both symmetry on the data and for the first layer to be initialized as rank 1 ($W_1 = W_2^Tr^T$). While the latter assumption is justified as a consequence of training from infinitesimal initialization, I still find these to be rather strong assumptions, and I do not think such equivalence between linear networks and ReLU networks holds beyond this limited case.
- I find that the currently paper does not have much additional novelty, compared to the prior work Lyu et al. (2021). Lyu et al. (2021) shows that for a two-layer ReLU network trained on symmetric data 1) starting from infinitesimal initialization, the weight $W_1$ becomes rank 1 and 2) as training continues, this rank 1 component converges in the direction of the max-margin linear classifier. This second stage is exactly the same as the dynamics of a linear neural network (Ji & Telgarsky, 2019; Soudry et al., 2018). While the current paper does consider a slightly more general target which is not necessarily linearly separable, to me it seems as that the linear separability assumption in Lyu et al. (2021) was so that they could show convergence to max-margin, and thus I find the generalization to be rather minor
- In the setting of section 4.2 (orthogonal or XOR data), the derivation in Appendix D relies on initializing the network so that the neurons $W_1$ are perfectly aligned with the directions of the data points. This also seems like a rather strong assumptions, and to me the important part of understanding these dynamics is showing that the neurons will align in the direction of the data points. Proving this for the setting of XOR data has been the goal of prior works [1, 2], and is quite challenging.

[1] Sgd finds then tunes features in two-layer neural networks with near-optimal sample complexity: A case study in the xor problem. Margalit Glasgow. ICLR 2024.
[2] Random Feature Amplification: Feature Learning and Generalization in Neural Networks. Spencer Frei, Niladri S. Chatterji, Peter L. Bartlett. JMLR 2024.

### Questions
- I would appreciate if the authors could comment on my concerns re novelty and significance stated above.
- Line 438 states that the second layer weights $W_2$ are nonnegative. Why is this true?

Minor comments:
- It might be helpful to add a plot of the depth separation function in Section 3.2.
- line 1329 "sumed"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies various cases where bias-free ReLU networks are equivalent to linear networks. This requires assumptions on the data (e.g., symmetry or linear target) and on the initialization (e.g., rank-one and balanced). These assumptions allow to show conservation laws, which imply that the network remains equivalent to a linear network throughout the dynamics.

### Strengths
The paper is very clearly written. It tackles the crucial question of understanding training dynamics of deep neural networks. I appreciate that the authors find settings simple enough for elementary analysis and exposition. An interesting and important contribution of the paper is to warn people wanting to study (bias-free) ReLU networks that their assumptions might make them inadvertently fall back to the linear case.

### Weaknesses
My main concern regards the soundness and importance of the contribution. Most results rely on conservation laws, which show that, under a specific initialization and a particular family of data distributions, the network is equivalent to a (sum of independent) linear network throughout training. However, deviations from these conversation laws are not studied in a thorough manner, which would be crucial in order to substantiate the claim that “the bias terms in the network and the structures in the data play an essential role in learning nonlinear tasks with ReLU networks” (line 59). For instance, the results of Figure 2b strongly rely on a very small-scale initialization (and perhaps a small learning rate), and this is not clearly discussed. Furthermore, for several cases studied in the paper, preexisting works already gave similar results and additionally rigorously control some of the deviation terms to this ideal initialization scenario.

More precisely, the results of Section 4.1 are close to the ones of Lyu et al. While the current paper lifts the assumption of linear separability, it considers the ideal case of a rank-one and balanced initialization. On the contrary, in Lyu et al., the deviation terms from this perfect scenario are carefully controlled, showing that the network still converges to a (global-max-margin) linear solution. This makes the latter analysis more nuanced, challenging the assertion in the present paper that they “incorporate as special case” the latter (l. 48). The claim that "we are able to give exact time-course solutions to certain two-layer ReLU networks in closed form, which has never been done for nonlinear networks outside the lazy learning regime” is therefore misleading, because Lyu et al provide a richer, though not closed-form, description, since they control additional error terms.

The situation is similar in Section 4.2: the decoupled dynamics from Appendix D is a simplification from the study of Boursier et al., which does not assume that the weight matrices are aligned with the data at initialization, but rather control the deviation from alignment.

I encourage authors to:
- clarify that they study idealized cases both in terms of data and initialization, and that these idealized cases lead to conservation laws which entail equivalence with linear networks.
- study more thoroughly deviations from this scenario, both in terms of data assumption and initialization assumptions (what happens for a Gaussian initialization depending on scale? Learning rate?).

Minor remarks:
- A relevant reference for rank-one structure in deep linear networks for regression (to complement references of lines 400) is Marion and Chizat, Deep linear networks for regression are implicitly regularized towards flat minima, NeurIPS 2024. Also, the rank-one structure is only approximate for a non-vanishingly small initialization, whereas authors seem to indicate the contrary on line 400.
- A study of the rank of matrices in deep ReLU networks was done in Timor et al., Implicit Regularization Towards Rank Minimization in ReLU Networks, ALT 2023.

### Questions
In Appendix C.5, the fact that the equivalence with a linear map holds even with large-scale initialization is very interesting, and could be further investigated. Does this equivalence also hold for larger learning rates?

### Soundness
4

### Presentation
4

### Contribution
2
