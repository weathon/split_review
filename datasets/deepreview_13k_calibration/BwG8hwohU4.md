# StableSSM: Alleviating the Curse of Memory in State-space Models through Stable Reparameterization

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
In this paper, we investigate the long-term memory learning capabilities of state-space models (SSMs) from the perspective of parameterization. 
    We prove that state-space models without any reparameterization exhibit a memory limitation similar to that of traditional RNNs: the target relationships that can be stably approximated by state-space models must have an exponential decaying memory. 
    Our analysis identifies this ``curse of memory'' as a result of the recurrent weights converging to a stability boundary, suggesting that a reparameterization technique can be effective. 
    To this end, we introduce a class of reparameterization techniques for SSMs that effectively lift its memory limitations. 
    Besides improving approximation capabilities, we further illustrate that a principled choice of reparameterization scheme can also enhance optimization stability. 
    We validate our findings using synthetic datasets, language models and image classifications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes how SSM-based models approximate target sequences. It proposes a simple criterion based on gradient norm scales to improve the implicit parametrization for the eigenvalue of real-valued SSM, first on a synthetic approximation task, then on a gated-convolution model.

### Strengths
* Choosing an appropriate implicit parametrization for SSMs is quite important in practice, and this paper provides a criterion to rank them.
* I found some of the theoretical connections quite interesting e.g., how the authors use Volterra series to express these models.

### Weaknesses
My main concern with this paper is the disconnect between theory and experimental results: the authors train few small-scale Hyena-SSM model on wikitext, and then attempt to explain how the ranking in training loss corresponds to a ranking with the proposed gradient-norm scale. There are no attempts to perform multiple runs, try in different applications, or verify whether this hypothesis holds with different hyperparameters. In fact, Appendix D shows the rankings change completely by tweaking the learning rate.

Eq (2) does not correspond to practical instantiation of SSM-based models, which have linear readout ($c^T h_t$), then a pointwise shallow MLP (either with gating or without).

### Questions
* The experiments rely on exploring different options for the implicit parametrization $f(w)$ of the eigenvalues of a real-valued SSM. Have you considered using small hypernetworks, or alternative parametrizations? Why parametrize only the poles of the SSM implicitly, and not also the residues? 
* Have you considered the effect of the entire architecture block, composed of gating and the SSM, on the choice of parametrization? Could that inform a better metric that better correlated with performance in practice?
* Can you provide some downstream evaluation of the language model, or at the very least validation loss?


Some nitpicks:
* Eq (2) does not correspond to practical instantiation of SSM-based models, which have linear readout ($c^T h_t$), then a pointwise shallow MLP (either with gating or without).

*UPDATE*: The authors have provided some clarifications and additional numerical experiments. While I do not think the experiments are conclusive, the paper puts forward a compelling theoretical argument that could produce improvements to the parametrization of SSM layers. I have raised my score.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work proposed a class of reparameterization techniques that lifts the memory limitations in SSM. The authors provide both theoretical analysis and empirical evaluation on the proposed approach.

### Strengths
The paper is well organized with detailed theoretical analysis and empirical evaluation. The overall workflow is pretty easy to follow. 

The authors demonstrate that the model structure of state-space models does not address the curse of memory phenomenon, and proposed the stable reparameterization to tackle the issue, While the reviewer didn't checked every detail, the derivation looks to be concrete.

### Weaknesses
The empirical evaluation on the synthetic dataset and language model seems are mostly on training behavior, e.g. decrease on training loss, improvement on stability of the training curve etc. Could the proposed approach concretely improve the testing performance? More evaluation on model performance on testing data is needed.

The author mentioned in multiple places that the theorems are established for the shallow case. Better to make a clarification on how shallow it is and why the same don't establish for deeper cases.

In introduction, further illustration and demonstration on the disadvantage of exponential decay in memory is needed, as it is the main problem tackled in the work.

### Questions
Could the proposed approach concretely improve the testing performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is about alleviating the "curse of memeory" in sequence modeling. Authors treat the training of a state-space model (SSM or linear RNN) as an estimation of regularized linear functional $\mathbf{H}$, and proves that the normal SSM with stable approximation shows exponential decay and thus cannot estimate functions with non-exponential decay. Then, it is proved that using reparameterization such as softplus can alleviate this problem, and also suggest optimal reparameterization operator for the given task.

### Strengths
The main theorems about the curse of memory and the necessity of reparameterization is thoroughly supported with assumptions and resulting proofs.

### Weaknesses
1. The analysis on the curse of memeory is limited to the simple state space model approximating linear decay. Reparameterization technique may not be applicable for sequential models with more complex structures. Specifically, the theoretical results are derived for linear time-invariant (LTI) systems, which may not directly translate to more complex non-linear or time-varying models. The paper does not adequately address how the proposed reparameterization would interact with non-linear activation functions commonly used in deep RNNs, or how it would handle the complexities introduced by multi-layered architectures.

2. It is not clear that why the "best" reparameterization should satisfy that the gradient is Lipshitz to the weight. While the paper suggests this property is related to optimization stability, it lacks a rigorous justification for why Lipschitz continuity of the gradient with respect to the weights is a necessary or sufficient condition for stable training. The connection between this property and the convergence of gradient-based optimization algorithms is not clearly established, and the paper does not provide a clear explanation of how this Lipschitz condition translates to improved generalization performance.

### Questions
1. As the numerical examples mainly show the results on gradient to weight ratio, how can you justify that this quantity is related with better training?

2. Can this analysis be extended to more complex models such as multi-layer RNN or transformer-based RNN?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
