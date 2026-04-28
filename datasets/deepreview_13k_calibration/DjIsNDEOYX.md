# Scalable Monotonic Neural Networks

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 5, 8

## Abstract
In this research, we focus on the problem of learning monotonic neural networks, as preserving the monotonicity of a model with respect to a subset of inputs is crucial for practical applications across various domains. Although several methods have recently been proposed to address this problem, they have limitations such as not guaranteeing monotonicity in certain cases, requiring additional inference time, lacking scalability with increasing network size and number of monotonic inputs, and manipulating network weights during training. To overcome these limitations, we introduce a simple but novel architecture of the partially connected network which incorporates a 'scalable monotonic hidden layer' comprising three units: the exponentiated unit, ReLU unit, and confluence unit. This allows for the repetitive integration of the scalable monotonic hidden layers without other structural constraints. Consequently, our method offers ease of implementation and rapid training through the conventional error-backpropagation algorithm. We accordingly term this method as Scalable Monotonic Neural Networks (SMNN). Numerical experiments demonstrated that our method achieved comparable prediction accuracy to the state-of-the-art approaches while effectively addressing the aforementioned weaknesses.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes Scalable Monotonic Neural Network (SMNN) to learn neural networks that preserve monotonicity of a model w.r.t. a subset of inputs. Existing works require additional overhead in terms of inference cost, weight constraints during training, scalability issues w.r.t. network size and number of monotonic inputs, etc. This work bakes in the monotonic properties directly into the network architecture by designing hidden layers with three different units ( exponential unit, ReLU unit and confluence unit ). Exponential unit preserves the monotonic nature of its input and are explicitly tied to the monotonic inputs. Remaining inputs go through the confluence and the ReLU unit, while the output of the confluence unit also goes through addition with the input for the next exponential unit (see Figure 1). Thus, monotonic inputs pass through a unique path in the network that preserves their monotonic nature. Empirical evaluation demonstrates that this method achieves comparable performance to the existing state-of-the-art and helps eliminate many issues arising in those works.

### Strengths
- Interaction of the monotonic inputs is segregated from the other inputs through a dedicated path in the neural network. This ensures the monotonic nature as these inputs pass through exponential units in the hidden layers 
- Empirical experiments show the viability of such a simple approach to enforcing monotonicity

### Weaknesses
 - Only performs on-par as the existing methods for enforcing monotonicity in neural networks 
- Its unclear if there's any computational advantage (in terms of training/inference cost) compared to existing baselines
- Limited discuss on extensions to other activations or expressivity of the network

### Questions
- Does restricting interaction between monotonic and non-monotonic inputs hurt expressivity of this network?
- How does one incorporate other activations/non-linear operators in this architecture?
- How do you select the parameter n in ReLU-n activation?
- Do you have any comparison on train/test time for the baselines with the SMNN architecture? Does it take longer to converge compared to existing methods?
- Why are parameters missing for XGBoost and Isotonic methods in Table 2?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an architecture for a neural net that guarantees the monotonicity of the output wrt a subset of predefined inputs, and still allows interactions between features derived from all inputs.

### Strengths
Originality
--------------
The method is related to several existing pieces of work, but the design of the specific architecture, enabling the integration of information from the non-monotonous inputs in a principled way, at every level, is original to my knowledge.
The architecture is generic enough that it should be applicable in a wide variety of settings.

Quality
----------
Experiments are well designed and match well with the (implicit) research questions, demonstrate well the behaviours of the algorithm, in particular:
1. when scaling up the number of parameters
2. when scaling up the number of monotonic features
3. when increasing the noise (compared to less-constrained or regular MLPs)

Experiments on real datasets show that this method is at least competitive with state-of-the-art methods.

Clarity
---------
The paper is clearly written, does not pose any notable challenge for comprehension. The method is defined clearly enough to be reimplemented from the paper, even without the provided source code.

Significance
-----------------
A scalable, end-to-end learning method guaranteeing the monotonicity wrt some inputs would have an impact for ML application where interpretability, trust, or predictability are necessary.

### Weaknesses
Quality
----------
1. Regarding the theoretical aspect, and the proof of Theorem 1, an issue is that ReLU-n is not a differentiable function, contrary to the definitions in section 2. Its derivative is not defined at 0 or n. While the conclusion might still hold due to continuity and the existence of left and right derivatives, the proof and definition should be updated to explicitly address the non-differentiability at these points and ensure that the composition of ReLU-n with other functions still results in a monotonic function. The current proof implicitly assumes differentiability, which is not valid for ReLU-n.
2. The scaling of compute time wrt number of monotonic features cannot really be extrapolated from varying the dimensions from 1 to 20. It's likely that at this scale, the execution time is dominated by constant factors, and it's unclear how it would actually scale to "high-dimensional monotonic features", compared to Certified MNN or COMET for instance. Due to the architecture, it is likely that the scaling time _per training step_ would scale up as well as a regular MLP, however optimization issues could happen and slow down convergence, for instance. It would be more effective to demonstrate the scalability of this method by applying it on a problem too big for Certified MNN or COMET, showing a clear advantage in training time or model size. The current experiments do not show this.
3. In Tables 2 and 3, statistical ties should be bolded, and be assessed by a statistical test taking into account the variance of _both_ distributions. Assuming the ± numbers indicate 95% CIs, there should be many more ties, and the conclusions about SMNN outperforming all other methods on regression tasks to not really hold. For instance, on AutoMPG, 7.44±1.20 and 7.58±1.20 should clearly overlap. The authors should use a proper statistical test (e.g., t-test or Mann-Whitney U test) to determine statistical significance and highlight ties accordingly.
4. The COMPAS dataset is used despite ethical concerns, since these features were used by the original COMPAS system to produce a score that was unfair and biased. This work uses the dataset despite not explicitly aiming at producing unbiased decisions, or examining critically the trained system. This raises concerns about the potential for perpetuating biases, even if the method itself is not designed to be unfair.

Clarity
---------
1. In Table 1, maybe indicate which methods are categorized as "regularization", and which ones are "customized architectures". Or, if "customized architecture" is synonymous with "end-to-end learning", maybe indicate it in the caption. The current categorization is not clear and could be improved.
2. The circled "+" signs in Figure 1 is confusing if the operation is concatenation, not addition. Maybe it would be clearer to have both arrows point directly at the next "Exp unit"? (Idem for the fc layer). The current notation is ambiguous and could be misinterpreted.
3. Why are Table 2 and 3 separate? Both have a mix of regression and classification datasets, but they have a different set of methods, and those in Table 3 do not report parameter counts. This makes comparison difficult and the rationale for separation is unclear.
4. Not clear at first what "subjected to denoising" (S. 4.1) means. The term is vague and needs clarification.
5. Clarify what the "±" numbers in the table means: standard deviation, confidence interval? This is crucial for interpreting the results correctly.

Significance
-----------------
The small scale of experiments is a limitation. Given that the ambition of the algorithm is to be "scalable", I think it should try to demonstrate scaling where some other algorithms are limited. The current experiments do not show a clear advantage in terms of scalability, and the method should be tested on larger datasets and compared to methods that are known to have scalability limitations.

Minor points
-----------------
1. Datasets should have citations or footnotes when they are introduced in the main text, not only in the appendix. Maybe also refer to the appendix explicitly for which features were considered monotonic. This would improve the readability and reproducibility of the paper.

### Questions
1. To disentangle the effects of the connectivity pattern from the ones of monotonous parametrization, I'd be curious to see the performance of a network composed only of Exponential units (all fully connected), but where the non-monotonous inputs would be duplicated as [x_¬m, -x_¬m]. Is that something you tried?

Update after discussion
--------------------------------
Many points have been addressed, so I'm moving my score from 6 to 8.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper tackles the inductive bias of monotonicity in Neural Networks. The authors propose a module based on nonnegative weights with a ReLU-n activation to enforce monotonicity. The proposed architecture comprises three types of hidden layers to handle monotonic and non-monotonic inputs.

### Strengths
- The paper is very clear and easy to follow.
- The method itself is simple and easy to implement.
- Variety of experiments across several domain-specific datasets and toy problems.

### Weaknesses
 - It could be argued that the novelty of the approach is limited since Mikulincer & Reichman (2022) already describe a very similar architecture and prove the universality of 4-layer threshold networks with nonnegative weights in approximating monotonic datasets. ReLU-n is a continuous relaxation of the threshold function, so it is likely that universality holds here as well for the same reasons and might possibly offer better convergence properties, but this is not explored.
- There seems to be a big focus on scalability, but it’s unclear how this approach is better than current state-of-the-art models in this respect. The experiments do not compare against other models, and for good reason, I imagine; there is little difference in the scalability of the proposed method and existing works in the literature. So, this begs the question of why scalability is a central thesis in the paper.

Overall, this paper feels like yet another approach to the inductive bias of monotonicity in neural networks. It has no big flaws, but the advantages do not appear to be substantial compared to current methods. The approach is simple enough and is worth considering, but the paper is slightly below the acceptance threshold.

### Questions
- Could you clarify what this sentence means: “Nevertheless, it should be noted that an optimally trained network is not always guaranteed with respect to the Lipschitz constant λ, particularly for larger constants”?
- I am unsure why scalability is considered such a central point in the paper. Some of the other methods are clearly just as scalable, including LMNs and constrained monotonic networks. Am I missing something?

**********Nits:**********

- Missing slash for $\exp$ instead of $exp$ in the proof of theorem 1 on page 5.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a new method, Scalable Monotonic Neural Networks (SMNN), to learn monotonic neural networks. Monotonic features are propagated forward using exponentiated units, which guarantees monotonicity. Non-monotonic features are propagated forward through confluence units and ReLU units, where confluence units capture interactions between monotonic features and non-monotonic features, and ReLU units capture interactions among non-monotonic features. The authors provide a theoretical result to verify the monotonicity of SMNN and experimental results to demonstrate the performance of SMNN.

### Strengths
1. The investigated problem, learning monotonic neural networks, is important in many fields, where some features are believed to have a positive or negative impact on the concerned output.
2. To the best of my knowledge, the proposed SMNN is novel.
3. The proposed SMNN is succinct. It is easy to understand as it only consists of commonly used activation functions, exponentiated weights, and a two-group architecture. Thus, SMNN can be trained by traditional backpropagation algorithms. It is also intuitive that SMNN can guarantee monotonicity.

### Weaknesses
1. The authors review previous methods in detail in the introduction part but the introduction might be too long and Table 1 does not fully distinguish SMNN and other methods. In Table 1, LMN, constrained MNN and SMNN have the same characteristics. It would be better to summarize the difference between SMNN and other methods in Table 1, which helps readers grasp the advantage of SMNN without reading through the long introduction.
2. The authors provide many experiments but it seems that the proposed SMNN has a similar performance to LMN. There are 5 datasets. SMNN wins on 2 of them, loses on 2 of them, and is comparable on the last one.

### Questions
1. On page 2, the authors claim that the assurance of monotonicity is not always guaranteed as a regularization method. This is true but I think this should not be treated as the drawbacks of regularization methods. The monotonicity usually comes from experience and may not be the truth. When we prefer to believe the experience, we can use methods in the first group to guarantee monotonicity. But when the experience contradicts collected data, then regularization provides a chance to balance between past experience and new data. Thus, I think it is more suitable to say these two groups of methods have their applications in the real world rather than treating not guaranteed monotonicity as a drawback.
2. Authors provide two definitions for partial monotonicity, one using function values and one using partial derivatives. However, it seems that the definition using function values is not correct. I think the correct one should be "The function $f(\boldsymbol{x})$ is partially monotonically non-decreasing on $\boldsymbol{x}_m$ iff $\forall i, x_i \leqslant x_i' , \forall j \neq i , x_j = x_j' \Rightarrow f(\boldsymbol{x}) \leqslant f(\boldsymbol{x}')$. Take a 2-dimensional case as an example. Let the 1st coordinate be the monotonic feature, and the 2nd is not. Let $f(x_1 , x_2) = x_1 + x_2^2$. Then $f$ is partially monotonic according to the definition using partial derivatives but is not partially monotonic according to the definition using function values.
3. On page 4, the authors claim that "ReLU is commonly used as an activation function due to its advantages such as avoiding gradient vanishing". ReLU helps address the problem of gradient vanishing (compared with sigmoid) but it cannot "avoid" gradient vanishing. When the weight parameters are sufficiently small and the number of layers is large, ReLU also faces the problem of gradient vanishing, and other techniques are needed to help address the problem of gradient vanishing. Thus, it would be better to use the verb "alleviate" rather than "avoid".
4. In Eq. (5), $h_{con}$ should be $h_{conf}$.
5. In the current SMNN structure, both the exp unit and conf unit use the ReLU-n activation function for the purpose of universal approximation and aligning output magnitudes. But in the ReLU unit, ReLU is used rather than ReLU-n. I am wondering what will happen if all these three units use the ReLU-n activation function. I think a unified activation function makes the structure more succinct.
6. In theorem 1, $x$ belongs to $\boldsymbol{x}_m$. To my understanding, $\boldsymbol{x}_m$ is a vector rather than a set, which indicates that the belonging relation is not rigorously defined. I think $x$ is a coordinate of the vector $\boldsymbol{x}_m$. A suitable way is to define the subscript set of $\boldsymbol{x}_m$ as $M$, and then use $x_i$ with $i \in M$.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
