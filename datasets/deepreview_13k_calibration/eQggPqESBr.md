# Simplicity Bias and Optimization Threshold in Two-Layer Networks

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Understanding generalization of overparametrized neural networks remains a fundamental challenge in machine learning. 
Most of the literature mostly studies generalization from an interpolation point of view, taking convergence of parameters towards a global minimum of the training loss for granted. While overparametrized architectures indeed interpolated the data for typical classification tasks, this interpolation paradigm does not seem valid anymore for more complex tasks such as in-context learning or diffusion. Instead for such tasks, it has been empirically observed that the trained models goes from global minima to spurious local minima of the training loss as the number of training samples becomes larger than some level we call \textit{optimization threshold}. While the former yields a poor generalization to the true population loss, the latter was observed to actually correspond to the minimiser of this true loss.
This paper explores theoretically this phenomenon in the context of two-layer ReLU networks. We demonstrate that, despite overparametrization, networks often converge toward simpler solutions rather than interpolating the training data, which can lead to a drastic improvement on the test loss with respect to interpolating solutions. %This absence of interpolation appears when the number of training samples grows larger than some \textit{optimization threshold}. 
Our analysis relies on the so called early alignment phase, during which neurons align towards specific directions. This directional alignment, which occurs in the early stage of training, leads to a simplicity bias, wherein the network approximates the ground truth model without converging to the global minimum of the training loss. Our results suggest that this bias, resulting in an optimization threshold from which interpolation is not reached anymore, is beneficial and enhances the generalization of trained models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This is a theoretical paper seeking to explain the phenomenon that in some situations overparameterized models, once the number of noisy training samples is large, fail to interpolate the training data and instead converge to a solution that minimizes the test loss.  This was observed with in-context learning and with diffusion models.  In this paper, the architecture is overparameterized two-layer ReLU networks, and the focus is on training them from a small initialization by gradient flow on noisy data which is labelled by a linear teacher and which satisfies some further simplifying assumptions.  The main result confirms the motivating phenomenon, and its proof provides further insights, pinpointing an early-phase alignment of neurons as the principal cause.  Another contribution are concentration bounds for the extremal vectors that drive the alignment process, and the assumptions here are less restrictive than in the main result.  The paper also reports and discusses numerical experiments in setups related to but extending the setting of the main theoretical result.

### Strengths
The paper is well written and the main result is accompanied by a detailed discussion.

The theoretical results are non-trivial, and their proofs are provided in the appendix.

The concentration bounds result may indeed be useful for future work.

The experimental results are interesting, and their discussion is informative.

### Weaknesses
The gap between the theoretical setting in this work and the empirically observed phenomenon with in-context learning and diffusion modes is large, and it is not clear whether and how the properties of the training dynamics identified here are related to what actually happens in those practical situations.  (E.g. it might be that case that the stability issues studied by Qiao et al. in NeurIPS 2024 are at play there to a greater extent than the neuron alignment in early training.)

As far as I can see, equation (8) is actually an assumption in Theorem 2, however that is not stated in Theorem 2, and moreover equation (8) is presented in the middle of a paragraph which starts with an example.  It would be clearer to have equation (8) as Assumption 2.

More minor points:
- The notation B(0, 1) is not defined, and presumably the 0 there should be bold because it is a vector.
- It seems to me you wanted to say that the data points are the columns of X, given how you multiply X and Y in Theorem 2.
- Perhaps stick to either transpose or angular parenthesis as the notation for inner products.
- In the Experiments section, it could be informative to state what m was.
- In the References, check whether papers cited as on arXiv have been published, and consider providing a clickable link for each item.

### Questions
Can you say more about your conjecture of order n effective width at the end of training in the orthogonal training data setting?  As far as I understand, Boursier et al. in NeurIPS 2022 showed that this width would be only 2, one group of aligned neurons for the positive labels, and another for the negative labels?

How essential is the ReLU activation for the main result?

How much compute was needed for the experiments?

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
2

### Summary
The paper proves results for a 2-layer ReLU network trained with gradient descent, and its convergence with respect to sample complexity. First, it proves that neuron weights cluster around a few extremal vectors as data size increases. Then, it shows that for a linear problem, the same network converges to the ordinary least squares estimator as data size goes beyond a threshold. This shows that contrary to common wisdom that neural networks interpolate between training data points, neural networks in this setting converge to simpler solutions with sufficient data.

### Strengths
Originality: the paper has a similar setting and results as some previous works (Boursier & Flammarion, Tsoy & Konstantinov) but generalizes to more datasets (e.g. beyond XOR) with unbounded sample complexity (e.g. theorem 2).

Quality: I cannot speak too much to the proofs, but they appear to follow from the established methods of Boursier & Flammarion. Despite being theoretically motivated, the paper has some nice experimental supporting evidence, e.g. appendix A.2 which shows the large gradient steps are not sufficient to explain simplicity bias.

Clarity: the discussions and experiments are straightforward to follow.

Significance: the immediate impact of this work is to build on analyses of 2-layer networks and regression settings to strengthen the case for the simplicity bias of neural network optimization. There is potential to explain the good generalization of in-context learning and diffusion models, but much work remains to extend the results to these applications.

### Weaknesses
My main concern is that the sample complexity bounds appear loose relative to empirical evidence, even in the regression setting presented in this work. The paper's structure could also be improved.

As discussed by the authors in "Limitations", there is a large (more than cubed) dependence of sample complexity on the input dimensionality, which makes it hard to relate this work to practical tasks, where dimensionality tends to grow more than sample complexity. It would be nice to see the experiment in figure 1 repeated for at least 2 more values of $d$ other than 5 to see if $n^\star$ evolves with respect to dimensionality at a different rate in practice. The current analysis does not provide sufficient insight into the scaling of sample complexity with dimensionality, which is a critical factor for practical relevance.

Overall the sections are somewhat disjointed due to the way discussions are interleaved with results: it would be easier to follow if every result was presented in a consistent manner (e.g. in order of the idea/intuition, context/prior work, the actual mathematical statement, the implications of the statement). In particular, section 2 can be hard to follow, especially regarding extremal vectors, which are introduced with little explanation or supporting intuition - some of the discussion and context for these concepts occurs after proposition 1. Although space is limited, explaining more details of the notation and key proof concepts would help make the work stand on its own instead of requiring unfamiliar readers to refer to prior work (e.g. intuition for the set $\mathfrak{D}$, reasoning for the domination property of initialization).

Since theorem 2 states neurons should cluster into one of two states, figure 1 could use include some information about the distance between neuron weights and the true OLS data model. For example, the mean cosine similarity after training could be plotted.

### Questions
Prior work (Boursier & Flammarion) discusses early phases of training where directional alignment occurs. Could the authors empirically or theoretically discuss if sample complexity influences when this early training phase occurs?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proves a simplicity bias of gradient flow on two-layer ReLU networks
which prevents them from converging to the training loss's global minimum when
the training set is large enough. Instead, the network's neurons align with a
small number of critical directions in the early phase of training, which guides
gradient flow towards the minimum of the population loss, therefore improving
generalization.

### Strengths
- **S1 Motivation:** The paper derives a theoretical explanation for the
  empirically well-documented phenomenon that overparameterized nets generalize
  well despite their capability to fit the training data. The simulation data
  seems to be in agreement with the presented theory. This provides solid
  insights into a general phenomenon.

### Weaknesses
 - **W1 Gap to practical setting:** To achieve tractability, the paper introduces
  assumptions, e.g. that gradient flow governs the training dynamics, and that
  the net uses ReLU activations. In the introduction, it argues that the
  discussed phenomenon is found in a wide class of models (diffusion, language
  models), though. These models usually contain other activation functions, are
  trained with finite step-size SGD, or even other optimizers like Adam(W). The
  paper acknowledges some of these limitations, but does not probe these
  directions empirically. I think it would be very insightful to report the
  behaviour with a different activation function (say GeLU, popular in LLMs), or
  when using a different training algorithm (say AdamW), or when initializing
  the weights with the default scheme. The reliance on gradient flow, while mathematically convenient, is a significant simplification that may not accurately reflect the dynamics of SGD with mini-batches and finite learning rates, which are standard in practical deep learning. Furthermore, the assumption of ReLU activations is quite restrictive, given the wide variety of activation functions used in modern architectures. The paper should also investigate how the observed phenomena are affected by different initialization schemes, as the initial parameter distribution can significantly influence the training trajectory.

- **W2 (minor) notation:** I think the notation could at some points be improved
  to make the paper easier to follow, for instance by introducing bold symbols
  for vectors, explicitly specifying the types of some objects (e.g. the
  elements of the set in L153) or operations (e.g. if L143 is an element-wise
  vector multiplication). I also sometimes found the notation a bit confusing,
  e.g. in L177, where $\theta$ contains $w$, so $\theta=0$ should imply $w=0$,
  but $w$ is a separate argument!? Some symbols are undefined, e.g. the
  distribution $B(0,1)$ in L314, and the norm on the LHS in L299. To some
  extent, this limited my understanding of the results, and how they go beyond
  existing works. The lack of clarity in notation, particularly regarding the distinction between $w$ as a general vector and $w_i(t)$ as a time-dependent parameter, makes it difficult to follow the mathematical arguments. The definition of $\mathfrak{D}_n$ as a function of two separate arguments, $(w, \theta)$, where $w$ is also part of $\theta$, is confusing and requires further clarification. The paper should explicitly define the distribution $B(0,1)$ and the norm used in the analysis, as these are not standard notations.

### Questions
- Q1: Could you elaborate on the optimization threshold's dependency on the
  network's width $m$, and provide an additional experiment similar to Figure 1,
  but using a second value for $m$ (similar to the larger value of $d$ in the
  appendix)? Also, what is $m$ in the network used to generate Figure 1?

- Q2: Definition 1 is not self-contained as it misses the object that possesses
  an extremal vector. This object should be $G_n$. Can you make the connection
  between $G_n$ and $D$ more explicit? Is it possible to visualize the concept
  of an extremal vector in a low-dimensional example?

- L325: In the parenthesis, it should be $S_-$.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies two-layer ReLU networks trained on a noisy linear regression task. By analyzing the training dynamics, the authors show that the two-layer ReLU network learns a nearly linear estimator. The authors use this analysis to illustrate an optimization threshold phenomenon that was observed and attracted interest in practical settings.

### Strengths
- The optimization threshold occurring in two-layer ReLU networks trained on a linear task is an interesting and somewhat surprising result. There is not yet much theoretical work on optimization threshold. So theoretical insight on this topic is new. 
- The main result is laid out with explicit assumptions and detailed discussions of its implications and limitations.

### Weaknesses
 - It seems to be a well-known opinion [1-3] that the early alignment, learning sparse features, or simplicity bias is a double-edged sword and sometimes leads to overfitting [1] instead of good generalization. This paper says the simplicity bias is beneficial, at least in this case. So I wonder how this paper fits into previous results with the different claim. I am especially interested in the authors' comparison with [1,2] because they are also theoretical works on two-layer ReLU networks.
- The dataset this paper studies seems quite similar to [4], which also assumed symmetric input distribution and a linear target. So I am wondering if this paper addresses a more challenging setup and in what ways the technical contribution goes beyond [4].
- The flow of the paper may benefit from a clearer structure. I felt I had to jump back and forth because the main theorem is immediately followed by discussions and then its proof sketch. Also, there is no related work section, though there are scattered discussions of related work throughout the paper.
- The authors motivate their problem by introducing the optimization threshold phenomenon in transformers and diffusion models. Although these models contain fully-connected ReLU layers, the mechanism in a two-layer ReLU network doesn't necessarily explain phenomena in transformers and diffusion models. For instance, one plausible possibility is that the attention layers in transformers play a key role in inducing this phenomenon rather than the ReLU layers. So I am not convinced that the ReLU network problem is well motivated by a phenomenon observed in transformers and diffusion models, despite the possibility of other valid motivations that weren't stated.

- In line 124, does this paper consider stochastic gradient descent or just gradient descent/flow? I imagine if SGD instead of GD is used, the data samples in each minibatch won't always satisfy Assumption 1?
- In line 135, what distribution are $(\tilde a_j,\tilde w_j)$ drawn i.i.d. from?
- In line 153, the definition of $\mathfrak D_n(w,\theta)$ doesn't look right. There are two left curly brackets but only one right curly bracket.
- In Figure 1, it was hard to spot $\sigma^2$ in both plots. Perhaps it's more visible if $\sigma^2$ is a tick on the y axis.

### Questions
- In line 124, does this paper consider stochastic gradient descent or just gradient descent/flow? I imagine if SGD instead of GD is used, the data samples in each minibatch won't always satisfy Assumption 1?
- In line 135, what distribution are $(\tilde a_j,\tilde w_j)$ drawn i.i.d. from?
- In line 153, the definition of $\mathfrak D_n(w,\theta)$ doesn't look right. There are two left curly brackets but only one right curly bracket.
- In Figure 1, it was hard to spot $\sigma^2$ in both plots. Perhaps it's more visible if $\sigma^2$ is a tick on the y axis.

I'd be happy to raise score if the questions are properly addressed.

### Soundness
3

### Presentation
2

### Contribution
2
