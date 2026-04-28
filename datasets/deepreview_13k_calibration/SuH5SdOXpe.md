# Robustness Reprogramming for Representation Learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
This work tackles an intriguing and fundamental open challenge in representation learning: Given a well-trained deep learning model, can it be reprogrammed to enhance its robustness against adversarial or noisy input perturbations without altering its parameters?
To explore this, we revisit the core feature transformation mechanism in representation learning and propose a novel non-linear robust pattern matching technique as a robust alternative. Furthermore, we introduce three model reprogramming paradigms to offer flexible control of robustness under different efficiency requirements. Comprehensive experiments and ablation studies across diverse learning models ranging from basic linear model and MLPs to shallow and modern deep ConvNets demonstrate the effectiveness 
of our approaches.
This work not only opens a promising and orthogonal direction for improving adversarial defenses in deep learning beyond existing methods but also provides new insights into designing more resilient AI systems with robust statistics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a "reprogramming" approach to improve the robustness of neural networks with minimal or no alteration of the model parameters. The reprogramming approach is executed by incorporating additional set of parameters (one per input dimension) in each layer to reweight the importance of features at inference time. The approach is motivated from a perspective of looking at the function of each unit as a linear feature pattern matching that is proposed to be replaced by a nonlinear version. The final implementation of the approach combines the activity of both linear and nonlinear feature pattern matching methods.

### Strengths
1. Proposed idea of reprogramming is interesting as it would allow reusing the learned features by the original model. May be an important approach to explore in large models. 
2. Empirical results consider multiple datasets of various sizes and different perturbations

### Weaknesses
1. The approach is based on eq 1 and the precursor to this for what is named as "linear feature pattern matching". The first equation (unnumbered equation before eq 1) formulates the OLS solution as the minimum of \mathcal{L}=\sum_{d=1}^{D}{(\frac{y}{D}-a_d.x_d)^2}. However, this formulation of the solution assumes that the prediction error is distributed uniformly across all dimensions which is not generally true and may indeed be very constraining in certain situations. Despite this possible issue, I didn't see any mention of this anywhere in the paper which in my opinion is a big weakness. The formulation appears to be minimizing the error between a uniform distribution of the target variable across dimensions and a linear combination of the input features, which is not a standard OLS objective. This discrepancy needs to be addressed with a clear justification for why this specific error formulation is appropriate for the task of feature reweighting.

2. Some of the key implementation details of the approach were unclear. What data is used to optimize the $w_i$ parameters? Are they optimized over the full training set of each dataset? Alg 1 contains a loop of K iterations for each $x_d$. Does this mean that the approach finds independent $w_d$ for each sample independently? In what order are different parameters/hyperparameters optimized? A step by step description of the approach or a pseudo-code would be helpful if not necessary. The lack of clarity on how the $w_i$ parameters are computed and updated makes it difficult to assess the practical feasibility and computational cost of the proposed method. The paper needs to specify whether these parameters are learned or computed directly, and if learned, what optimization procedure is used.

3. The approach requires computing additional activations for every layer that may be costly but no comparison of runtime, computation cost etc is provided. The additional computation required by the nonlinear reprogramming method needs to be quantified and compared against the computational cost of the original model. Without this comparison, it is difficult to evaluate the practical trade-offs between robustness and efficiency.

4. Details of Adv-train baseline is missing. Was this the result of adversarial training from scratch or fine-tuning? The paper should clearly state whether the adversarial training baselines were trained from scratch or fine-tuned from a pre-trained model. This is important for ensuring a fair comparison between the proposed method and existing adversarial training techniques.

5. In Table5, the AA accuracy is substantially higher than that of PGD (64.60 vs. 57.23). This to me looks like a big red flag. AA is an ensemble attack made of 4 separate attacks including two effective variations of PGD. Because of this, AA accuracy is always lower than that of PGD. I'm doubtful of the validity of empirical evaluations.

### Questions
1. Related to weakness #1 above, on line 167 it is stated that by replacing the loss function with the proposed one the impact of outliers will be reduced, referring to Huber and Ronchetti's book Robust Statistics. The connection is unclear to me and I think deserves a more detailed explanation. Can you expand? 

2. Line 105, by "robust training" do you mean "adversarial training"? 

3. Line 244: "One naive approach is to simply replace the vanilla linear pattern matching (LPM) with NRPM. However, this naive approach does not work well in practice". Why doesn't this approach work? 

4. Line 231: according to the text, $x_o$ is not the perturbation but the initial input. Is that correct? 

5. In table1 and others, what are the numbers at the top of each column? Are they the epsilon values used for test? What attack was used? 

6. Adaptation of the approach to CNNs needs more explanation. Were separate $w_i$ parameters considered per filter or per activation? 

7. Fig 5: likelihood in the bar plots doesn't look like proper probability density functions. What is being shown? 

8. Fig 5 caption: 1 and 2 correspond to (a) and (b) in the figure?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Many methods have been proposed to improve the adversarial robustness of neural networks, including adversarial training, purification, and regularization. However, these approaches don't take advantage of the learned parameters of models that were not robustly trained. This paper proposed robust reprogramming, which uses those learned parameters to construct a new model that is robust to adversarial perturbations by design. The authors identify linear transformations to essentially be linear pattern matching (LPM), with the pattern being specified by the parameters of the transformation which are capable of matching related features in the input. They further note that linear feature pattern matching is the optimal closed-form solution to the Optimized Least Squares problem, which is particularly sensitive to outliers due to its quadratic penalty. To reduce this sensitivity, this work introduces a new feature pattern matching term based on Least Absolute Deviation estimation, which is called Nonlinear Robust Pattern Matching (NRPM). Theoretical results show that adopting NRPM mitigates the influence of any datapoint on downstream predictions. Three paradigms of robust reprogramming are then introduced: one which only involves implementing the NRPM architecture, one which involves NRPM and fine-tuning hyperparameters, and one which involves NRPM and finetuning all parameters in the model. Experimental results show that these paradigms (and especially paradigm 3) can provide significant improvements over existing robustness techniques. For example, in ResNets trained on CIFAR10, paradigm 3 results in significantly higher robustness than state of the art adversarial training techniques, with only a modest drop in clean accuracy.

### Strengths
* There is a great deal of novelty in this approach. Many defenses against adversarial examples atttempt to learn weights that are more robust, or to detect/purify adversarial inputs to a network. I am not aware of any prior work that modifies the model of computation to increase robustness in this way.
* Code and model weights have been provided for replication purposes. 
* The experimental results are impressive. In particular, in certain cases the third paradigm can increase both robustness and clean accuracy.

### Weaknesses
 * Theorem 3.2 is presented in a confusing manner. You refer to $x_0$ as the perturbation, but isn't it instead the location of a possible perturbation?
* The theoretical justification for the robustness of NRPM largely relies on the influence functions that are derived for NRPM and LPM. However, there's no explicit connection that's made between influence functions and adversarial robustness. It's not immediately clear to me that the influence function on its own would immediately imply adversarial robustness. I think additional justification for this relationship would be necessary in the final version of this paper (or references to related works which establish this relationship).
* On a similar note, there are settings that have been studied in the literature in which an adversary is capable of making unbounded changes to the input (i.e. [1,2]). It seems that the influence function would be less informative about the robustness of the model to adversaries that are unbounded in $\ell_p$ space. I think it should be made more explicit if you are only envisioning this as a defense against $\ell_p$ bounded adversaries.
* The table and figure captions could use more information about the experimental setups. For example, its unclear which attacks/norms mentioned in section 5.1 are used in which table.

### Questions
* What is the difference in inference efficiency between a standard MLP and a reprogrammed MLP (in terms of memory usage/inference time)?
* Similarly, how does execution time scale with the depth/width of the network?
* Are there any adaptive attacks that could improve over AutoAttack against robust reprogramming? Does this approach just reduce to gradient masking?
* Is the NRPM approach suitable for training from scratch? If so, do you think that would that further improve over the performance of paradigm 3?
* Would an adversary with knowledge of the robust reprogramming scheme be able to design an adaptive attack to counteract these defenses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed nonlinear robust pattern matching algorithm (NRPM) that can improves the robustness without modifying its parameters while maintaining the feature pattern matching by reprogramming a pretrained model. Especially, this paper theoretically analyzed linear pattern matching and Newton-iterative reweighted least squares algorithm, and introduced robustness reprogramming paradigms under three different situations: parameter-free tuning, lightweight fine-tuning and full fine-tuning. The experimental results support its theoretical analysis and demonstrate the effectiveness of proposed method.

### Strengths
- This paper provides comprehensive and detailed theoretical analysis and explanations.
- This paper is well written to follow.

### Weaknesses
 - This paper leveraged old baselines for ResNet18 backbone while recent baselines (e.g., [1], [2]) are missing and evaluation against stronger attack (e.g., LGV, SPSA, DeepFool) could be beneficial.
   - [1] Consistency regularization for adversarial robustness
   - [2] Dynamic Label Adversarial Training for Deep Learning Robustness Against Adversarial Attacks
- This paper utilizes backbones that are too small and tasks that are too easy. For example, main table (Table 1, 2) used MLPs and MNIST. It would be beneficial to provide experimental results on CIFAR-100 and Tiny-ImageNet at least with backbone of ResNet18 and WideResNet28-10. 
- Under same computing resource, it would be better to directly compare the required resources (e.g., FLOPs) or training time (e.g., GPU Hours) between the proposed method (e.g., paradigm 3, full-tuning) and existing methods for ResNet18 backbone.

### Questions
- In table 5, robust accuracy against AutoAttack seems to be high, and it would be better to check whether the model suffers from obfuscated gradient or not. For example, following scenarios could be provided: 1) evaluation against adaptive attacks, 2) checking for gradient masking, or 3) evaluation against PGD attacks with extremely large attack strength where robust accuracy should be almost zero while PGD attacks using same strength but different step sizes and steps (e.g., 2 times smaller step size but 2 times larger attack steps) should achieve similar robust accuracy from original attack setting. 
- For the proposed three different paradigms, it would be better to explain when it is more effective to use which paradigm to achieve robustness efficiently based on the differences between three scenarios.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes an adversarial robustness scheme that doesn't necessarily require altering the pretrained parameters. They propose a "reprogramming" scheme to adapt the representations learned by a pretrained network in order to enhance the network's robustness. The proposed approach is extensively evaluated on multiple datasets and simpler model architectures and is shown to enhance empirical performance.

### Strengths
- The approach is thoroughly evaluated on multiple datasets and simpler models.
- It empirically performs well under increasing attack strength/various attack types.

### Weaknesses
1) The readability of the paper is not good in its current form. The paper doesn't provide sufficient background/cite references to understand the terminology used or where ideas are derived from. Overall, I find it very hard to understand the ideas/contributions of this work, even though the results look promising.

2) The notation is inconsistent, and several terms are used without introduction. For example,

      a) What is X in the indicator function of F in line 212?

      b) What is y in Line 223? Such missing details make it very hard to follow the ideas introduced in the paper.

      c) What is the difference between {\lambda} and \lambda? Guessing from Table 1, the weights are learned/assigned per layer? The notation does not convey this correctly (it should either be a vector or otherwise properly subscripted in the notation).

      d) What is N in algorithm 2?

3) The figures lack sufficient description to understand what's happening. How are the visualizations of hidden embeddings created in Figure 5? What is meant by the "size of the budget" in Figure 3? (my intuitive guess is that refers to the attack budget, but under what norm? Which attack? The language needs to be a lot clearer and the captions/descriptions are too succinct and vague in the current draft).

4) Please include an analysis of how exactly is this better than adversarial training. How do the training time and number of parameters compare for the two approaches?

5) I also find it hard to appreciate the need for the 3 separate training paradigms. A discussion of when and how exactly would each of these be more applicable and suitable is lacking.

6) What is the cost of scaling this approach to more practical models/datasets (e.g. ImageNet with ResNet50 or so)? This goes back to -4- as to if/how this is better than AT, besides the empirical gains.

### Questions
Refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
