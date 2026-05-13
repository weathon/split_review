# PROSE: Predicting Operators and Symbolic Expressions using Multimodal Transformers

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Approximating nonlinear differential equations using a neural network provides a robust and efficient tool for various scientific computing tasks, including real-time predictions, inverse problems, optimal controls, and surrogate modeling. Previous works have focused on embedding dynamical systems into networks through two approaches: learning a single solution operator (i.e., the mapping from input parametrized functions to solutions) or learning the governing system of equations (i.e., the constitutive model relative to the state variables). Both of these approaches yield different representations for the same underlying data or function. 
Additionally, observing that families of differential equations often share key characteristics, we seek one network representation across a wide range of equations. Our method, called \textbf{Pr}edicting \textbf{O}perators and \textbf{S}ymbolic \textbf{E}xpressions (PROSE), learns maps from multimodal inputs to multimodal outputs, capable of generating both numerical predictions and mathematical equations. By using a transformer structure and a feature fusion approach, our network can simultaneously embed sets of solution operators for various parametric differential equations using a single trained network. Detailed experiments demonstrate that the network benefits from its multimodal nature, resulting in improved prediction accuracy and better generalization. The network is shown to be able to handle noise in the data and errors in the symbolic representation, including noisy numerical values, model misspecification, and erroneous addition or deletion of terms.
PROSE provides a new neural network framework for differential equations which allows for more flexibility and generality in learning operators and governing equations from data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a bimodal transformer-based model to predict solutions of (partly) known ordinary differential systems from a few initial points in their trajectories. 

The initial points on the trajectories to be predicted are encoded by a two-layer transformer. The system equations, which be fully known, known up to their pre-factors or known up to a few random terms, are represented as trees, enumerated in Polish notation, and encoded by a 4-layer transformer. The output of both encoders are then mixed together by a 8-layer transformer.

Two decoders (both 8-layer transformers) operate on the encoded inputs: one to predict future values of the trajectories from their time coordinates, and one (auto-regressive) to predict the system equation. 

Experiments on 15 dynamical systems, with parameters sampled in a small range around a value of interest, show that the model can indeed predict trajectories and actual model parameters with good accuracy, and that the model can extrapolate away from the equation parameters seen at train time.

### Strengths
Using bimodal numeric/symbolic models is a promising approach, and the architecture proposed makes a lot of sense. The initial results are interesting and promising.

### Weaknesses
The methodology must be better justified. The overall architecture is fairly complex, and many technical choices and not justified, or validated by ablation studies. Some important information, like the training loss, is missing.

The training and test sets are too small and not diverse enough. All train and test examples are generated from only 15 systems, with a very small number of free parameters (4/15 have 1 free parameter, 3/15 have 2 and 4/15 have 3). Those parameters are  sampled in a small interval (0.9,1.1) around their value of interest, to generate a training sample of 512k examples -- i.e. 34,000 examples per system. There is a large risk that the training and test equations will significantly overlap, or at least be very similar. What guarantees do you have that your results are not due to train/test contamination?

The experiments are the weak part of the paper. Appendix B states that the model was run for 80 epochs of 2000 optimisation steps, on batches of 2*256=512 examples. Overall, this means 81.9 million training examples, or 160 passes on the 512k training set. Given the size of the model (several hundred million parameters), and the lack of diversity in the train set (34k examples per system on average), there is a large risk that the model memorize its training data. This might account for some of the results. 

Finally, a comparison with baseline results, notably prior work on symbolic regression(see for instance, https://arxiv.org/abs/2307.12617), would help assess put the results in perspective. In their current form, the benefits of this approach are difficult to evaluate.

### Questions
* related works: previous works on symbolic regression should be mentioned, notably Becker et al. (ICML 2023, https://arxiv.org/abs/2307.12617), and probably D'Ascoli et al., Biggio and Kamienny et al.
* Polish notation: in language models, it was introduced by Lample & Charton in 2019, but the technique is much older (logicians in the 1930s, and computer scientists in the 1950s)
* "there is a one-to-one correspondence between trees and mathematical expressions" this is incorrect: expressions like x-2.1 can be encoded as + x -2.1 or - x 2.1, and x+y+z as + +x y z or + x + y z. Besides, unless simplification is used when the data is prepared, many equivalent expressions result in different trees (2+x <=> x+2 <=> 1+x+1).
* the 3-token encoding for floating point numbers was introduced in Charton 2022. Lample et al. only use integer pre-factors.
* "our vocabulary is also of order $10^4$ words." What precision do you use? Charton 2022 uses 3 significant digits, for a vocabulary size of about 1100 words (901 mantissas, 200 exponents, 2 signs). D'Ascoli 2023 uses 4, for a vocabulary a little below $10^4$.
* Figure 2: the term self-attention layer used in the figure is misleading: these are self-attention+FFN layers, with most of the trainable parameters in the FFN. Maybe use transformer layer instead, or transformer encoder and transformer decoder to indicate the presence of the cross-attention mechanism.
* feature fusion: an 8-layer transformer seems like a very large model to learn to align the numeric and symbolic representations learned up-front. Have you tried smaller fusion networks (one or two layers, perhaps just self-attention and a single linear layer as the output?)
* since the symbolic output can have variable length, many authors propose to compress it as a single, high dimensional vector, using attention distillation (Santos 2016), or simpler techniques like max-pool. Have you tried such techniques?
* what is the training loss? how do you balance between the two decoders, are they trained simultaneously, or separately?
* could you provide results as a function of system dimension, and number of free parameters? 
* could other metrics be presented? (D'Ascoli uses $L^\infty$, Charton $L^1$)
* Table 4, seems to be on the Unknown 3D experiments, please add this to the caption.
* in table 2, a study of how error increases with the extrapolation interval would be interesting: from data sampled on (0,2) what is the error on (2,4), (4,6), (6,8)?

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposes PROSE (Predicting Operators and Symbolic Expressions), a novel approach to predict the evolution of a solution of a certain multi-dimensional ODE, given the first time-steps of the solution and symbolic information about the velocity field of the ODE. 

Alongside the numerical prediction of the ODE's solution at future time steps, the model also outputs a symbolic expression representing the velocity field of the underlying ODE. 

The method is based on fusing multi-modal input information in the form of numerical data (ODE's solution sampled up to a certain time step with noise perturbations) and a symbolic, potentially wrong or corrupted, representation of the velocity field. PROSE is entirely based on Transformers and the attention mechanism and draws inspiration from the pioneering line of work on operator learning for differential equations. 

The experiments, performed on 15 multi-dimensional ODE systems, show that the model efficiently leverages information from both the numerical and symbolic domains and predicts accurate solutions both at the numerical and the symbolic levels.

### Strengths
- The paper is generally well-written and background information is carefully provided.

- The topic of merging and combining numerical and symbolic information in Transformer models is very interesting and the paper takes a  relevant step in this direction.

- The experiments effectively show that the model is able to leverage symbolic information in the task of predicting the future time steps of the ODE's solution. This means that symbolic information is successfully combined with numerical information thanks to the modality fusion step.

### Weaknesses
 - My main concern is that the claims about the ability of PROSE to perform model discovery are not sufficiently backed by empirical evidence. The number of considered ODEs is limited to 15 and as such, I do not see the necessity of having a symbolic decoder predicting the full mathematical expression. Alternatively, one could have resorted to a simple classification network responsible for predicting one out of 15 classes corresponding to the underlying ODE. The coefficient of the predicted ODE could have then been optimized via, for example, BFGS. In other words, I feel that the hypothesis space considered in the paper is too small, as the number of possible expressions to be predicted is limited to 15.

- Another source of concern is that the model is trained on fixed grids, i.e. training solutions are provided up to 2 seconds. It would be interesting to see how the performance of the model changes as the size of the training window changes. 

- I think a more complete analysis should have been performed for the case when input symbolic information is wrong or corrupted by noise. Is the symbolic decoder able to correct the wrong information provided by the symbolic encoder?

- In terms of novelty, while I understand that fusing symbolic and numerical information can help in the prediction of the solution at future time steps, when symbolic information is not available (which is rather common), the model reduces to a relatively simple forecasting approach, whose novelty is quite limited. What would make the approach more novel is the symbolic decoder part, which in the considered setting of only 15 equations, cannot do much more than predicting one of the 15 examples seen at training time.

- Some relevant related works are not mentioned. In particular [1,2] also use Transformer to predict velocity fields at the symbolic level.

- The model is not compared with relevant baselines, e.g. SINDy or DeepOnet, or the aforementioned works.

### Questions
See weaknesses part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Predicting Operators and Symbolic Expressions (PROSE) to learn from multimodal inputs to generate numerical predictions and mathematical equations. Experiments using 15 differential equations show highly precise results.

### Strengths
1. The research on differential equations using machine learning methods is of significant research interests.
2. A multi-modal approach using transformer architecture is technically sound, and the novelty and technical contribution is reasonable.
3. Experiments results are impressive with high precision.

### Weaknesses
1. There is no comparison with existing methods, so it is hard to assess how the proposed approach comparing with SOTA.
2. The paper claims that high performance partially comes from multimodal learning, an ablation study will be interesting to verify this claim.

### Questions
1. Can you compare with existing methods to verify that the high performance is not because the differential equations used are too simple?
2. An ablation study with single inputs will be interesting to show the effectiveness of multimodal input.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
