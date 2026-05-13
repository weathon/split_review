# Grokking in Linear Estimators -- A Solvable Model that Groks without Understanding

- Decision: Accept
- Scores: 6, 5, 8, 3

## Abstract
Grokking is the intriguing phenomenon where a model learns to generalize long after it has fit the training data. 
    We show both analytically and numerically that grokking can surprisingly occur in linear networks performing linear tasks in a simple teacher-student setup with Gaussian inputs. 
    In this setting, the full training dynamics is derived in terms of the training and generalization data covariance matrix. 
    We present exact predictions on how the grokking time depends on input and output dimensionality, train sample size, regularization, and network initialization.
    We demonstrate that the sharp increase in generalization accuracy may not imply a transition from "memorization" to "understanding", but can simply be an artifact of the accuracy measure. We provide empirical verification for our calculations, along with preliminary results indicating that some predictions also hold for deeper networks, with non-linear activations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies delayed generalization in a linear student-teacher setup with diagonal-covariance Gaussian inputs. The authors also offer some extensions to non-linear 2-layer networks (still in the Gaussian setting). Extensive analytical derivations in the gradient flow regime are shown to match numerical simulations closely.

### Strengths
- The paper is very well-written and easy to follow.
- Corroborates prior observations on the effect of dataset size on Grokking and distills the delayed generalization behavior down to a very simple toy setup.
- Theoretically and empirically, the toy setting is well explained and studied thoroughly, from a simple 1-D linear setup to various extensions, including a non-linear 2-layer setting.

### Weaknesses
 - My biggest worry about the paper is that it does not deviate from the toy setting proposed. While the results are good, and the match between analytical results and empirical behavior is close, the entire investigation leaves out realistic applications and the original setting in which the phenomenon was first observed. Furthermore, it seems like the theory does not cover some phenomena associated with Grokking, and it might just be too far from the original setting to yield practical results. Specifically, the model's monotonic loss behavior during generalization is a concern, as Grokking often involves an initial increase in generalization loss before a sharp decrease. This discrepancy suggests the model might be capturing a different phenomenon than what is typically understood as Grokking. The submission would be substantially stronger with more connections to realistic settings or insights that can transfer across, e.g., tasks, datasets, models, etc.

- The effect of label noise does not seem to be completely captured by the theory. I have seen scenarios where the label noise is “corrected” at Grokking time, still reaching 100% accuracy. Specifically, one can take a *Grokking on modular addition* setup and assign random labels at a certain rate. Generalization accuracy can still reach 100% eventually. Do you have any idea why that’s the case? Is there a way for the toy model to accommodate such "self-correcting" behavior?

### Questions
- Delayed generalization in many settings can occur after the generalization loss **increases**, whereas the toy setting presented seems to imply monotonic behavior. Could this mean that the phenomenon studied here is qualitatively different from Grokking in the original setting? There is no fixed and precise definition of Grokking, so this is not a big issue, but I think a distinction might be helpful in understanding feature learning dynamics.
- The effect of label noise does not seem to be completely captured by the theory. I have seen scenarios where the label noise is “corrected” at Grokking time, still reaching 100% accuracy. Specifically, one can take a *Grokking on modular addition* setup and assign random labels at a certain rate. Generalization accuracy can still reach 100% eventually. Do you have any idea why that’s the case? Is there a way for the toy model to accommodate such "self-correcting" behavior?

**Nit:**
The figures are nice but can be difficult to parse. In particular, I think it would be easier to understand figures where the theoretical predictions are differentiated for the training and generalization curves (e.g., dashed lines for train, solid for generalization with empirical data shown as points with different markers for train/gen).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a toy model for grokking, a phenomenon where training accuracy rises much before test accuracy. The proposed model is a linear target function on Gaussian data distribution. A student model attempts to estimate parameters with a matching linear model. The authors use random matrix theory (specifically the eigenvalue distribution of the Wishart ensemble) to derive the dynamics of training and test losses under gradient flow. While both train and test losses decrease smoothly in terms of MSE, when plotting a hard classification accuracy, this toy model exhibits a separation of timescales between training accuracy saturation and test accuracy saturation. The authors illustrate that this is entirely due to the difference between the feature covariance matrix on the training distribution and on the test distribution. These results, taken together provide a possible deflationary explanation for grokking, which can occur merely as an artifact of the choice of metric in very simple models, rather than due to a deeper reason related to learning generalizing features at late training time. The authors show that their results can be extended to weight decay, multiple outputs, training a linear neural network with multiple layers, and training deep nonlinear networks in the lazy/kernel regime.

### Strengths
This paper has a nice analytically solvable theory of training dynamics which reproduces grokking-like learning curves. The paper uses a basic result in random matrix theory, namely the limiting spectral density of the Marcheko Pastur law to derive the train and test loss dynamics. Due to the model’s simplicity the authors can derive nice asymptotic expressions for the loss at late time and use these to derive a grokking timescale. They show that their theory is predictive in experiments on reasonably large features and datasets sizes.

### Weaknesses
While this paper provides an interesting and exactly solvable toy model of grokking, it has some major defects which must be addressed before I can support acceptance. 

First, the paper lacks a proper comparison to literature on gradient flow dynamics in linear models (see below). In addition the citations are often incorrect or correspond to nonexistent papers. We outline these issues below in section titled Related Work Issues.  

Next, the comparison of the grokking observed in this model and grokking observed in real networks is still unclear. Do the authors think that the proposed statistical effect is the phenomenon at play in grokking in real networks? Below I list some observed phenomena associated with grokking that this theory does not quite capture

1.  Many works on grokking report development of specialized weight structures in deep networks temporally coincident with the improved generalization error. I suspect this form of grokking would correspond to deviation from a linear model which would be outside the scope of explanation in this work. If the authors are not claiming this is a theory of grokking as it is observed in its original settings (like modular arithmetic in transformers), in what sense is this an explanation of grokking? 
2. Another example of a difference between observed dynamics and the present study is that weight decay does not induce more extreme grokking which was reported in Liu et al 2023. 
3. Sometimes in grokking experiments with deep networks, the test loss (MSE) even increases before later decreasing to its final value like in Davies et al 2023 Figure 1. It is unclear if this can happen in the linear model where the errors in each non-null eigendirections decrease exponentially.  

On the other hand, it could be that the primary point of the paper is motivating the need for more careful research on grokking in the future. For example, what artifacts due to choice metric should experimenters be wary of? How should we distinguish “improvement in understanding” vs mere statistical noise? Commenting further on this distinction and comparison to phenomena observed in prior works on grokking would greatly improve the paper. 

**Issues with Related Work**

1. The authors miss several important works on gradient flow with linear models. Advani & Saxe 2020 (https://www.sciencedirect.com/science/article/pii/S0893608020303117) derive the training and test errors dynamics for the model considered in this paper. Omitting this citation does not do justice to their relevant contribution. In addition, Saxe et al 2013 (https://arxiv.org/abs/1312.6120) derive learning curves for deep linear networks with fixed dataset. 
2. Several other papers which derive asymptotic performance of linear models trained with Gaussian data in the proportional regime with gradient flow.  
   (a) Mignacco et al 2022 (https://proceedings.neurips.cc/paper/2020/hash/6c81c83c4bd0b58850495f603ab45a93-Abstract.html), Mignacco et al 2022 (https://iopscience.iop.org/article/10.1088/1742-5468/ac841d/meta), 
   (b) Paquette et al 2022 (https://arxiv.org/abs/2205.07069)
3. The authors also miss the work of Gromov (https://arxiv.org/abs/2301.02679) on the dynamics of grokking in modular arithmetic without regularization. 
4. Several cited papers do not even seem to exist! These include [2] E. Bodin and N. Macris. Dynamics of generalization in learning with gradient descent for piecewise linear neural networks [4] A. Crisanti and H. Sompolinsky. Dynamics of learning in deep linear neural networks: A mean-field approach   [7] S. Goldt, M. M’ezard, F. Krzakala, and L. Zdeborov’a. Modelling the infinite width limit of neural networks with mean field theory

### Questions
**Questions/Comments**

1. Figure 5 Bottom row: Is the reason that the dynamics for the tanh networks are well approximated by linear two layer dynamics because the activation function is linearizable around $\phi(h) \sim h$? What if you used a different activation function, for instance, increasing the “gain” of the tanh nonlinearity like $\tanh(g * h)$ for $g > 1$? For large enough $g$, would we expect the correspondence to the linearized dynamics to break? 
2. Equation 7 is using approximation signs instead of equality. However, I suspect that if one considered the average case error over random teachers where $T \sim \mathcal N(0,I)$ then the equation given is exact. Is there any reason to not focus on averaging over random teachers since the data is isotropic?
3. The authors claim that deep networks in the kernel regime can be described by the same equations except redefinition of the kernel. I believe that the kernel would not only change the eigenvalue spectrum but would also make the train and test dynamics dependent on the decomposition of the teacher T in the eigenbasis of the kernel. This would therefore make the result much less trivial than what is provided here since the test error is not merely a functional of the spectral density.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uncovers a surprising fact that linear models can manifest the 'grokking' phenomenon within a teacher-student framework. The author qualitatively predicts the precise dependencies of grokking time on input/output dimensions, sample size, regularization (weight decay), and initialization. Remarkably, these predictions hold true for more intricate models in specific settings. The paper also includes a comprehensive set of empirical validations to support the theoretical analysis.

### Strengths
The paper is notably well-structured and written. Its strengths can be summarized as follows:

- The paper offers a substantial novelty value, as it explores the grokking phenomenon through a theoretical lens, an area with limited prior analysis. The surprising discovery of grokking in certain linear model scenarios (even without weight decay) adds a unique perspective to the literature. This novel approach contributes significantly to our understanding of grokking from the first principle.
- The authors provide comprehensive theoretical predictions for their proposed linear model. They not only establish the asymptotic order of grokking time but also consider various related factors. Also, the paper extends its analysis to two-layer networks, both with and without nonlinearity. To further strengthen their claims, the authors conduct an array of extensive experiments that effectively illustrate and validate the theoretical findings.

### Weaknesses
Though the paper is of good quality, I believe the paper would improve in the following aspects:
- The notations are quite dense even for the simplest model at first glance. The paper would benefit from having some explicit definition or intro to the model and all the notations. For example, the use of $d_{in}$, $d_{out}$, $N_{training}$ and their relationship with the linear model parameters (e.g., weight matrix) could be more clearly defined early on. A concrete example of the linear model setup, perhaps with a small numerical example, would greatly aid understanding before diving into the theoretical analysis.
-  The derivation of this paper is concrete. However, all the calculations are in the asymptotic manner. It would be better to see the results be displayed as some rigorous theorem in some limiting case. For instance, while the paper provides scaling laws for grokking time, it would be beneficial to see a formal theorem stating the precise conditions under which these scaling laws hold, including specific assumptions on the data distribution and model parameters. This would increase the rigor of the analysis.

### Questions
In this linear model, the grokking phenomenon is due to the gap of convergence speed between training and generalization loss. Can it also imply the difference in two-layer networks settings (or in NTK regime), or they have a different mechanism?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript studies a linear teacher-student model trained with Gradient flow and MSE loss. The authors solve the dynamical training equation which yields to an exponential decay of the initial error with a spectrum of exponents related to the training data covariance matrix. When the input dimension is larger than the number of data-points, this matrix has zero eigenvalues and hence target modes that cannot be learned. Moreover, using Gaussian iid data, this matrix is Wishart, thereby allowing the authors to estimate where the bulk of non-zero spectral modes resides. Following this they find that the asymptotic dependence of the training loss is roughly exponential with a time scale depending on the lower bulk spectrum of the Wishard matrix. In this asymptotic regime, the test loss behaves as the train loss up to a multiplicative factor larger than 1. Hence the time at which the training loss drops below some small threshold (t_{*,train}) is smaller than the time it takes the test loss to do so (t_{*,test}). This delay between t_{*,test} and t_{*,train} is then viewed as a form of Grokking. The authors proceed with extending their results to several other scenarios. Such as networks with vector outputs, weight decay, and two-layer network in the linear/NTK regime.

### Strengths
The authors study a timely topic. 

They lay bare some issues with how Grokking is perceived.  

The manuscript is clearly written and easy to follow.

### Weaknesses
I feel there are two main issues with the current work.

1. Is this Grokking?

Grokking is a somewhat ill-defined phenomenon. However, like many grey area situations, the fact that it is difficult to draw one sharp reason doesn't mean there cannot be a sharp feeling that something does fit. Let me then rationalize several reasons for why I don't think this is grokking: 
A. It is too simple. If this model Groks, everything Groks.   
B. There aren't any feature learning effects (see for instance Gromov (2023) or Misra (2022)) or beyond NTK effects. 
C. There is only one time scale here, which is (1-\sqrt{\Lambda})^{-2}, governing both test and train loss. Hence, looking at the train and validation loss, a practitioner would not be encouraged to do any early stopping here. In contrast, in various Grokking models, there is an over-fitting regime prior to Grokking which can mislead practitioners.  

2. Technical aspects seem quite close to previous results in the literature.

The training dynamic the authors find is closely related to the e^{-\Theta t} \Delta obtained in the NTK work. In fact, up to a standard shift of the inner and outer indices, their data covariance matrix is Theta here. In particular, both have the same non-zero spectrum. I'm sure there are much earlier works which solve this for a linear network. 

Similar factors relating train and test performances, however at infinite time, were also found in Adlahm and Pennington 2020 and https://arxiv.org/abs/2006.09796. Given the expected exponential decay of the discrepancy in linear models, the fact this ratio holds also in the asymptotic dynamics seems expected. At any rate, It'll be good to compare and disentangle the factors the authors find from those.

### Questions
The work is clearly written. I don't have any questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
