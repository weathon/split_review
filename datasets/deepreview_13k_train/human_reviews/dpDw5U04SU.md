# Minimum width for universal approximation using ReLU networks on compact domain

- Decision: Accept
- Scores: 5, 8, 8

## Abstract
\noindent
It has been shown that deep neural networks of a large enough width are universal approximators but they are not if the width is too small.
There were several attempts to characterize the minimum width $w_{\min}$ enabling the universal approximation property; however, only a few of them found the exact values.
In this work, we show that the minimum width for %
$L^p$ approximation of $L^p$ functions from $[0,1]^{d_x}$ to $\mathbb R^{d_y}$ is exactly $\max\{d_x,d_y,2\}$ if an activation function is $\relul$ (e.g., $\relu$, $\gelu$,  $\softplus$).
Compared to the known result for $\relu$ networks, $w_{\min}=\max\{d_x+1,d_y\}$ when the domain is $\smash{\mathbb R^{d_x}}$, our result first shows that approximation on a compact domain requires smaller width than on $\smash{\mathbb R^{d_x}}$.
We next prove a lower bound on $w_{\min}$ for uniform approximation using general activation functions including $\relu$: $w_{\min}\ge d_y+1$ if $d_x<d_y\le2d_x$. Together with our first result, this shows a dichotomy between $L^p$ and uniform approximations for general activation functions and input/output dimensions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the universal approximation problem of deep neural networks with unlimited depth. The main contribution of this paper is to derive that when the input domain and output domain are $[0,1]^{d_x}$ and $\mathbb R^{d_y}$ respectively, the minimum width of the universal approximation of neural networks for $L^p$ functions is equal to $\max(d_x,d_y,2)$, when the activation function is similar to RELU (e.g., RELU, GELU, SOFTPLUS). The authors also show that if the activation function is a continuous function that can be uniformly approximated by a sequence of continuous one-to-one functions, then the minimum width of the universal approximation of neural networks for continuous functions is at least $d_y+1$ if $d_x<d_y \leq 2d_x$.

### Strengths
Originality: The related works are adequately cited. The main results in this paper will certainly help us have a better understanding of the universal approximation property of deep neural networks from a theoretical way. I have checked the technique parts and found that the proofs are solid. One of the main results, which shows that there is a dichotomy between $L^p$ and uniform approximations for general activation functions and input/output dimensions, is a non-trivial extension of previous results in this field.

Quality: This paper is technically sound.

Clarity: This paper is clearly written and well organized. I find it easy to follow.

Significance: I think the results in this paper are not very significant, as explained below.

### Weaknesses
However, I have several concerns about the contribution of this paper. Firstly, the paper (Cai, 2023) already proved that the minimum width of the universal approximation of neural networks for $L^p$ functions is equal to $\max(d_x,d_y,2)$, when the activation function is Leaky-RELU. This paper only generalizes Leaky-RELU to RELU-LIKE activations (e.g., RELU, GELU, SOFTPLUS), and derives the same result. I think this makes the contribution of this paper incremental. Also, It would be more interesting if the authors could study the exact minimum width for more architectures used in practice. Furthermore, the technical part is not very deep and mostly based on the technical results from previous papers such as (Cai, 2023). In summary, I think this paper is a decent paper with some good results, but may not be suitable for the top conferences such as ICLR.

### Questions
As explained above, It would be more interesting if the authors could study the exact minimum width for more architectures used in practice.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors, in a sense, improve on the available results quantifying the minimal widths required for a class of deep but narrow MLPs to be universal in $C([0,1]^{d_X},\mathbb{R}^{d_Y})$.    The result is very interesting, and of a technical nature; namely, they show that minimal width can (but surprisingly and not shockingly) be improved when only considering approximation of functions on the cube and not the entire domain $\mathbb{R}^{d_X}$.

### Strengths
The results are interesting, especially for those studying the fundamental limits of MLPs and their approximation theory. The presentation is clear and the proofs are mathematically correct.  

Though one may foreseeable argue that the contribution is of a technical nature, these results answer fundamental questions at the core of the validity of practical MLP implementations. 

In short, I think these results should definitely be published :)

### Weaknesses
 The paper is rigorous and I do not see any weaknesses; with one exception:

- Can the authors please add more details and rigor in the construction in Lemma 6's proof.  I know a lot of it is drawn from another paper's lemmata but it would be better to have it explicit and self contained.  Right now it is not even a proof but a proof sketch/recipe.

### Questions
** 1) Impact of metric entropy on minimal width?**

Fix a compact subset $X$ of $\mathbb{R}^{d_X}$, non-empty.  Suppose that we are looking for universal approximators in $C(X,\mathbb{R}^{d_Y})$  implementable by MLPs with ReLU-Like activation function and of bounded widths.  How do you expect that the metric entropy/capacity of $X$ will impact the minimum width?


For instance, if $X=\{x_0\}$ is a singleton and $d_Y=1$, then clearly the width $\min\{d_X,d_Y,2\}$ is suboptimal since the class since the class
$$
\{ x\mapsto a\operatorname{ReLU}(1\cdot (x+b)):\, a\in \mathbb{R} ,\, b:= -x_0 + 1\}
$$
is universal in $C(X,\mathbb{R})$.  So I guess there is room for improvement for general $X$.  (The same question applies to the case where $d_X=0$ and $d_Y=1$, in which case the minimum width is
$$
1 < \max\{d_X,d_Y,2\}=\max\{0,1,2\}=2.
$$


----

What's your intuition on how the metric entropy of $X$ appears into the estimate?  


I thought about the case where $X=\{-1,1\}$ but minimal width seems to apply there also.  What am I missing?



----

** 2) Why not note more general implications?**

Perhaps I missed it, but it could be worth noting that your results also imply the minimal widths for universality/density in $C(\mathbb{R}^{d_X},\mathbb{R}^{d_Y})$ in the topology of uniform convergence on compact sets.  This is because of the extension and normalization arguments as in the proof of Proposition 3.10 [1] or in the proof of Proposition 53 [2], which allows one reduce the problem of universality in $C([0,1]^{d_X},\mathbb{R}^{d_Y})$.  I.e. using either of the Tiezte or McShane extension theorems


** 3) Improving Minimal Width Estimates for general nonlinearities**

In [5], the authors just recently showed that most MLPs with standard and continuous activation functions can approximately implement and MLP with ReLU activation function using roughly the same depth, width, and number of parameters.  I was wondering, unless I am missing something, why not use their results to sharpen your statement for general continuous activation functions?

- References -

[1] Acciaio, Beatrice, Anastasis Kratsios, and Gudmund Pammer. "Designing universal causal deep learning models: The geometric (Hyper) transformer." Mathematical Finance (2023).

[2] Kratsios, Anastasis, and Léonie Papon. "Universal approximation theorems for differentiable geometric deep learning." The Journal of Machine Learning Research 23, no. 1 (2022): 8896-8968.

[3] Arenas, Francisco García, and María Luz Puertas. "Tietze's extension theorem." Divulgaciones Matemáticas 10, no. 1 (2002): 63-78.

[4] Beer, Gerald. "McShane’s extension theorem revisited." Vietnam Journal of Mathematics 48, no. 2 (2020): 237-246.

[5] Zhang, Shijun, Jianfeng Lu, and Hongkai Zhao. "Deep Network Approximation: Beyond ReLU to Diverse Activation Functions." arXiv preprint arXiv:2307.06555 (2023).

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work studies the minimum width required for universal approximation ability of neural networks, under general settings with varying norm, input/output dimensions and activation functions. In particular, this work generalizes the result of Cai 2023, showing that the minimum width is exactly $\max(d_x,d_y,2)$ for neural networks with ReLU-class activations to approximate $L^p$ functions from a compact set of $\mathbb{R}^{d_x}$ to $\mathbb{R}^{d_y}$. Then it's shown that when uniform approximation is considered, the minimum width is at least $d_y+1$ when $d_x\le d_y\le 2d_x$, implying a dichotomy between $L^p$ and uniform approximation.

### Strengths
**Solid results:** the theoretical results make a solid contribution to the understanding of the universal approximation ability of neural networks.

**Wide coverage:** Theorem 2 holds for a wide class of ReLU-like activations, while previous works mostly consider only the most representative ReLU. Though such result is well expected due to the similarity between these activations, and indeed the proof is based on a simple reduction, it is non-trivial and such generality is valuable.

**Tight bounds:** since the initial work of Lu et al 2017 which achieves the $d_x+4$ bound in the particular setting with $L_1$ norm, $d_y=1$ and ReLU activation, there has been a line of works on sharpening the bound itself, and generalizing the setting to other norms and activations. This work finally presents an exact characterization of the minimum width for general $L^p$ norm and a wide class of ReLU-like activations.

### Weaknesses
 **Questionable significance:** though this work makes a solid contribution to a tight characterization of the minimum width for universal approximation which is certainly valuable for our theoretical understanding, in my opinion, the mission itself to improve upon previous results is not so significant. The gap between known upper and lower bounds is merely an additive constant, and a similar tight result was achieved in Cai 2023 for the special case of Leaky-ReLU. While the generalization to a wider class of ReLU-like activations is appreciated, the core techniques appear to be incremental, building upon existing proof strategies. The improvement over the Leaky-ReLU case, while technically sound, does not introduce a fundamentally new approach or concept in the field of neural network approximation theory. The practical implications of this tight bound, especially given the small constant difference, remain unclear, and it's not immediately obvious how this result will lead to new algorithms or architectures. The focus on achieving the absolute tightest bound, while mathematically interesting, might not be the most impactful direction for the field at this time.


### Questions
As a side note, the separation between the whole Euclidean space and compact subset (equivalently, $L^p$ versus uniform) was noticed even before Wang and Qu 2022. In a technical report of Lu [1], it's shown that any two-layer ReLU network must incur $\int_{\mathbb{R}^d}|f|$ error to approximate an integrable function $f$, a sharp contrast to the case when the integral is deployed on a compact set. Their argument is very simple and may be potentially helpful for explaining the intuition of such separation results.

[1], A note on the representation power of ghhs, Zhou Lu, arXiv preprint 2101.11286

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
