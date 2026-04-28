# Faster Gradient Descent in Deep Linear Networks: The Advantage of Depth

- Decision: Reject
- Avg Score: 2.33
- Scores: 3, 1, 3

## Abstract
Gradient descent dynamics in deep linear networks has been studied under a wide range of settings. These studies have reported some negative results on the role of depth, in that, gradient descent in  deep linear networks: (i) can take exponential number of iterations to converge, (ii) can exhibit sigmoidal learning, i.e., almost no learning in initial phase followed by rapid learning, (iii) can delay convergence with increase in depth. Some of these results are also under stronger assumptions such as whitened data and balanced initialisation. These messages from prior works suggest that depth hurts the speed of convergence.

In this paper, we argue that the negative role of depth in the prior works is due to certain pitfalls which can be carefully avoided. We give a positive message on the role of depth, i.e., seen as an additional resource, depth can always be used to speed up convergence. For this purpose, we consider scalar regression with quadratic loss. In this setting, we propose a novel aligned gradient descent (AGD) algorithm for which we show that (i) linear convergence is always possible (ii) depth accelerates the speed of convergence. In AGD, feature alignment happens in first layer and the deeper layers accelerate by learning the right scale. We show acceleration in AGD happens in finite time for unwhitened data. We provide insights into the {acceleration} mechanism and also show that acceleration happens in phases. We also demonstrate the acceleration due to AGD on synthetic and benchmark datasets. Our main message is not propose AGD as a new algorithm in itself, but to demonstrate that depth is an advantage in linear networks thereby dispelling some of the past negative results on the role of depth.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies optimization in deep linear networks, in particular the effect of depth on convergence.
It proposes a novel algorithm, aligned gradient descent (AGD), that solves the issue of slow convergence of linear networks.

### Strengths
The results seem correct.

### Weaknesses
This work considers a very narrow problem that, in my opinion, is of very little interest.
First of all, the problem of deep linear networks is very narrow.
However, even worse than that, the authors motivate their work from trivial observations.
Section 3.1 describes a trivial situation in which the neural network is initialized at a very special value of the parameters, that is known to converge to a saddle point. Any initialization that is sufficiently far from that special case would not suffer from the limitations described by the authors. Also, depth plays no role in this section, contrary to what seems to be the main motivation of the authors.
Similarly, section 3.2 describes another trivial situation where the neural network is initialized very near the saddle point. Again, any initialization that is far away enough from that special initialization would not suffer from the problems described.
In section 3.3, the authors desribe problems in the case of p-norm loss, but that is also a narrow case of very little interest.
The novel algorithm, AGD, is quite complicated and is limited to deep linear networks.
It remains unclear why that algoroithm may be useful or interesting in any other (non-linear) case.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper tackles the optimization issues induced by higher depth.

The authors show that in the case of 1) width 1, 2) a very precisel and unrealistic initialization where all the layers but one are initialized at 1 and the others at 0, a version of GD converges exponentially as the standard OLS.

The authors conclude that this implies that some negative optimization results attributed to the depth are not actually attributable to the depth.

### Strengths
The paper is clearly written and well organized. The problem is well introduced.

### Weaknesses
The paper tackles the optimization issues induced by higher depth.

The authors show that in the case of 1) width 1, 2) a very precisel and unrealistic initialization where all the layers but one are initialized at 1 and the others at 0, a version of GD converges exponentially as the standard OLS.

The authors conclude that this implies that some negative optimization results attributed to the depth are not actually attributable to the depth.

### soundness:
 1

### presentation:
 2

### contribution:
 1

### strengths:
 The paper is clearly written and well organized. The problem is well introduced.

### weaknesses:
 The paper does not meet the ICLR standards for theoretical novelty or practical relevance. The issues with unrealistic assumptions, limited scope of the investigation, and lack of empirical support are significant enough that a strong reject recommendation is given.
The paper has a huge number of problems, but those are not even the point. It completely fails in its objective. The conclusions drawn are misleading and not supported by the computations on the toy models provided.

The claims of non-detrimental effects of depth are based on a single, highly contrived example where all layers but one are essentially bypassed by setting their weights to 1, reducing the model to a standard linear regression. This approach does not reflect the complexities or realities of deploying deep networks in practice. The authors provide precisely one of those few cases (of measure zero) in which depth is not detrimental for the optimization and they claim that thus depth may not be detrimental. 

This does not imply that deeper networks may be trainable. They are actually cooking up an example in which they kill the effect of depth to say that depth there has no effect. Not only this cooked up example is very far from practice, but everywhere else in the parameter space, depth has an effect.

It is also misleading to suggest that the computational increase is limited to 5L, which results solely from choosing a network width of one—a characteristic of the architecture, not the algorithm itself. Computational demands typically scale with network width.

Moreover, even in this overly simplistic case they show that GD is unstable and that is the reason why they change algorithms. In practice they are telling us that even on this instance of deep network in which all the layers are the identity except one, GD would not behave well as the depth scales.

Additionally, the terminology used to describe shallow networks as standard linear regressions contradicts the literature referenced, where shallow networks are generally recognized as having a single hidden layer.

Overall, this paper does little to enhance our understanding of the phenomena it intends to explore and fails to address its central thesis effectively.

A minor point of critique is the redundancy in the text; the last paragraph of page 1 is essentially repeated with identical wording at line 168 and again in section 5. This redundancy could have been avoided to streamline the content and enhance clarity.

### Questions
Am I wrong about my assessment? I really do not see how this analysis can lead to prove your claims but happy to discuss it with the authors.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Whether the depth provides an advantage in training deep networks has been a key question discussed in prior research. In response to this, the present study constructs a gradient method (along with the initialization strategy) that achieves fast convergence even as the number of layers increases, positively answering this question. The distinct feature compared to previous studies is that un-whitened data is allowed, as well as the use of the standard L2 loss function.

### Strengths
- The authors constructed a concrete and solvable example where a specific gradient method achieves fast convergence in a deep linear network. Notably, this work demonstrates that depth can be an advantage in optimization even in the general case with un-whitened data.

- The intuition behind the speed-up of convergence is well explained, including examples from previous works on acceleration.

### Weaknesses
 **Limitation on the Width**  
As far as I understand, the analysis is limited to a width of 1 for hidden layers, and it is not obvious whether it can be extended to networks with general widths. If this is true, it is a very restricted scenario. The restriction to a width of 1 significantly limits the practical relevance of the results, as modern deep networks are typically over-parameterized and have much larger widths. This narrow width constraint raises concerns about the applicability of the proposed method to real-world scenarios, where wider networks are the norm. The analysis should address how the convergence properties change as the width increases, and whether the observed speed-up is maintained in more realistic settings.

**Necessity of AGD**  
While it is clear that AGD contributes to the acceleration of convergence, the necessity of using AGD specifically is unclear. For instance, why wouldn’t Adam or Newton’s method work? It is not clear why the specific adaptive learning rate scaling of AGD is crucial for the observed convergence speedup. A more thorough analysis comparing AGD with other optimization methods, such as Adam or Newton's method, is needed to justify the choice of AGD. The paper should provide a more detailed explanation of why AGD is essential and whether other optimization methods could achieve similar results, possibly with different parameter tunings.

### Questions
**Limitation on the Width**  
- Why do the authors not generalize the results to networks with general widths? A width of 1 is very restrictive. The authors mention some prior work as being limited due to the assumption of whitened data, but to me, restricting the width to 1 seems more idealized and far removed from modern *over-parameterized* deep networks.  
- What is the width used in the experiments on datasets in Section 4.5?

**Necessity of AGD**  
AGD has an adaptive learning rate scaled by $(\Theta_t^{(2:L)})^2$.  Is it necessary to use the square, or can this be generalized to $(\Theta_t^{(2:L)})^p$ ($p>0$)?

### Soundness
3

### Presentation
3

### Contribution
2
