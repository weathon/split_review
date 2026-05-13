# Enhancing Adversarial Robustness on Categorical Data via Attribution Smoothing

- Decision: Reject
- Scores: 3, 5, 6, 5, 6, 6

## Abstract
Many efforts have been contributed to alleviate the adversarial risk of deep neural networks on continuous inputs.
Adversarial robustness on general categorical inputs, especially tabular categorical attributes, has received much less attention. To echo this challenge, our work aims to enhance the robustness of classification over categorical attributes against adversarial perturbations. We establish an information-theoretic upper bound on the expected adversarial risk. Based on it,
we propose an adversarially robust learning method, named Integrated Gradient-Smoothed Gradient (IGSG)-based regularization. It is designed to smooth the attributional sensitivity of each feature and the decision boundary of the classifier to achieve lower adversarial risk, i.e., desensitizing the categorical attributes in the classifier. We conduct an extensive empirical study over categorical datasets of various application domains. The experimental results confirm the effectiveness of IGSG, which surpasses the state-of-the-art robust training methods by a margin of approximately 0.4\% to 12.2\% on average in terms of adversarial accuracy, especially on high-dimension datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies how to strength the adversarial robustness of categorical data using attribution smoothing.

### Strengths
- There have been only a few works aiming to enhance the adversarial robustness of categorical data.

- The empirical results look quite convincing.

- The use of IG for discrete data is interesting.

### Weaknesses
 - The writing needs a significant boost and improvement.  The notions used in this paper are not good and easy to confuse such $b(x)_{i,j,k}$ sometimes $x_{i,j,k}$ for the element $jk$ of the categorical data point $x_i$.

- Theorem 1 has unsolid terms without a careful explanation
   -  $I(f;S^n)$ with the classifier $f$ and the training set $S^n$, how can you evaluate the mutual information between a classifier and a training set? It's unclear how this term is defined, given that mutual information is typically between random variables, not a function and a dataset. The training set $S^n$ is fixed, so it is not a random variable. Furthermore, the notation $f$ is also confusing, is it a random variable or a function?
   -  $I(x_{i,\omega_i}; f)$  with $\omega_i$ to be the selected feature, however, it is not clear  $x_{i,\omega_i}$ and how to compute $I(x_{i,\omega_i}; f)$ because it seems that $f(x_{i,\omega_i})$ is not valid.  It is unclear what $x_{i,\omega_i}$ represents. Does it represent a single feature, or a subset of features? If it's a subset, how is the mutual information computed between a subset of features and the classifier output? The notation $f(x_{i,\omega_i})$ is also problematic, as $f$ operates on the entire input $x_i$ and not a subset of it. Similar doubt for $I(x_{\bar{\omega}_i, y_i; f})$. The same issues apply to $I(x_{\bar{\omega}_i, y_i}; f)$. It is not clear how to compute the mutual information between a combination of features and the label with the classifier output.

-  The theories developed and the proposed approach are not really connected.

### Questions
I believe this paper has some interesting ideas. However, the presentation and writing need a significant boost, hence it is not ready to publish. 

For questions, please refer to the weaknesses and 
- Can you further explain more the intuition of the term $\ell_{TV}IG(x_i)$?

### Soundness
2 fair

### Presentation
1 poor

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
This paper studies adversarial robustness of classification over categorical attributes against adversarial perturbation. An information-theoretic upper bound on the expected adversarial risk has been established, together with an adversarial learning method with integrated gradient-smoothed gradient regularization. Experimental results demonstrate the effectiveness of the proposed training method and the superiority to the state-of-the-art robust training methods in terms of adversarial accuracy.

### Strengths
This paper is well-motivated and well-written. The adversarial robustness on categorical data is an interesting topic, and this paper takes a reasonable approach to tackle related challenges. Some interesting insights are also discussed, and they would be of interest to the community.

The definition of adversarial risk for categorical data is reasonable. It appears the information theoretic upper bound on the expected adversarial risk is new, and the remarks on the upper bound are sensible. The regularization terms inspired from the bound are reasonable.

There are some interesting experiments in the appendix, which are good to know.

### Weaknesses
It seems there is some gap between the information-theoretic upper bound and the regularization terms. They are weakly linked by some factors implied by the upper bound, but there does not seem there are any direct connection between them. That is, the factors are quite intuitive in such a way that the regularization terms can be designed without knowing the information-theoretic bounds. The mutual information terms just state some weak dependence between random variables, but there is no mention on how to compute/approximate them in the current context. It is unclear how tight the upper bound could be, and the evaluation of the dependence of the bounds against key parameters in practical models and datasets is also missing.

The proposed training method just puts two regularization term together with some hyper-parameters without explaining why they should be composed in that way. It is unclear how these regularization terms are connected to the mutual information terms in the upper bound. Specifically, the paper lacks a clear explanation of how minimizing the proposed regularization terms directly translates to minimizing the mutual information terms in the derived upper bound. The connection between the integrated gradient smoothing and the mutual information terms is not rigorously established, making it difficult to understand why this particular regularization approach is chosen over other alternatives. Furthermore, the paper does not provide any theoretical justification for the specific combination of the two regularization terms, leaving the reader to wonder if this is the optimal way to combine them or if other combinations might be more effective.

### Questions
1.	State clearly and explicitly how the information-theoretic upper bound is connected to the regularization terms.
2.	Evaluate the upper bound against the key parameters for practical models and datasets.

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
The authors address adversarial robustness in the context of categorical variables, a less-explored scenario in the literature. They highlight the key finding that different attack methods yield adversarial samples with varied distributions. Relying solely on PGD-generated adversarial samples for training leads to overfitting and inadequate defense against diverse attacks. Consequently, they opt to bolster robustness in categorical data training through a regularization-based approach.

By establishing an upper bound on the theoretical risk gap and analyzing factors that mitigate adversarial risk, they propose IGSG—a regularization-based paradigm for robust training with categorical variables. Experimental results across multiple datasets affirm the method's superiority over baselines and traditional adversarial training techniques.

In summary, the authors introduce IGSG, a regularization-based robust training method, grounded in a theoretical analysis of factors reducing adversarial risk in dealing with categorical variables. Empirical evidence demonstrates its outperformance over baselines and competing adversarial training methods.

### Strengths
1、The authors address adversarial robustness in the context of categorical variables, an aspect that has received limited exploration in the literature.
2、The authors present a clear motivation for their work.
3、The authors substantiate their motivation through explicit theoretical and empirical experiments.

### Weaknesses
1、The expression contains ambiguities, such as the specific definition of $G^r" in equation (5), which needs clarification in the main text. On page six, the authors mention minimizing the "third and fourth terms" in the first line, but the subsequent explanations actually refer to optimizing the second and third terms. For the cross-validation of hyperparameters, it would be beneficial for the authors to elaborate on how they performed the training-validation set split using only the training data and specify the chosen values for the hyperparameters.
2、The experiments appear insufficient, and I suggest the authors supplement the following experiments to bolster support for their method:
1）While MLP and Transformer serve as baseline models, including more models would validate the generalizability of their method. Specifically, models that leverage different inductive biases, such as CNNs for local feature extraction or RNNs for sequential data, should be considered, where applicable, to demonstrate the robustness of the proposed approach across diverse architectures.
2）Despite utilizing cross-validation for hyperparameter selection, reporting performance with different hyperparameter choices is recommended to assess the sensitivity of their method. This should include a systematic exploration of the hyperparameter space, detailing how performance varies with different combinations of key parameters, rather than relying solely on a single cross-validated choice.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies adversarial robustness on tabular categorical attributes and establishes an information-theoretic upper bound on the expected adversarial risk.

### Strengths
- Provide some theoretical results.
- Easy to follow.

### Weaknesses
 - This work develops the theory over randomized learning algorithm $A(\cdot)$, however, the experiments are deployed on deterministic models. How can these empirical results support the theory?
- Given $S$, where does the randomness of $A(S)$ come from? Could authors provide a simple case of randomized algorithm that the theory can totally hold?
- I am familiar with PAC Bayes, which involves a posterior distribution of $A(S)$. Does a posterior distribution of $A(S)$ also exist here? If so, what assumptions are made about $A(S)$? If not, could authors provide the precise definition of $A(S)$?
- In $I(f,S)$, $f$ and $S$ are random variables, how to use $IG(x)$ with a given deterministic $f$ to influence $I(f,S)$ with a random $f$. We even have no idea with the assumption of random $f$. It is also confused which $f$ is random and which $f$ is deterministic, they are both represented as $f$.
- The adversarial robustness of tabular categorical attributes is only a minor extension of DNNs adversarial robustness, the contribution seems minor.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes IGSG, a theoretically motivated robust learning method for categorical inputs. It contains two parts: Integrated Gradient (IG) and Gradient Regularization. Experiments verify the effectiveness of the proposed method.

### Strengths
- The studied problem is interesting, adversarial attack/defense on caterical data is of interest to the community;
- The experimental results are strong to present the effectiveness of the proposed IGSG method.
- The paper is well-written and well formatted.

### Weaknesses
 - Minor issue:
     - Page 9, "”robust overfitting”"

### Questions
- I find some Adversarial Training baseline and Regularization baseline methods perform worse than undefended method. Could you please explain the reason?
- Could IGSG be used or modified to be used in continuous data?
- Could you please explain more about Figure 3? Why the summing of the attack frequency of IGSG features are lower than that of original features?
-  What is the meaning of the sign of $IG$? If the sign of insignificant, maybe using the absolute of $IG$ is better.
- According to Eq.3 and Factor 1, IGSG should base on the adversarial training. However, S is the original dataset used in Eq.5. Why not use the adversarial training as a base?
- I notice a recently ICML 2023 paper *Probabilistic Categorical Adversarial Attack and Adversarial Training* proposes a gradient-based attack. However, the attack methods you used (i.e. FSGS and OMPGS) are both search-based attack method. Therefore, the improvements against other methods your presented might come from the relatively weak attack, because the adversarial training employed gradient-based attack instead of search-based attack. Could you please show more results on defending the gradient-based attack methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a regularization method to enhance the robustness of classification over categorical attributes against adversarial perturbations. The paper establishes an information-theoretic upper bound on the expected adversarial risk and proposes an adversarially robust learning method, named Integrated Gradient-Smoothed Gradient (IGSG)-based regularization, which designed to smooth the attributional sensitivity of each feature and the decision boundary of the classifier to achieve lower adversarial risk, desensitizing the categorical attributes in the classifier. The paper conducts extensive empirical study over categorical datasets of various application domains to confirm the effectiveness of IGSG and achieve new start-of-arts.

### Strengths
This paper has good originality, high quality and clear expression. The paper proposes a new regularization method which outperforms adversarial training and generalize well.

### Weaknesses
Larger dataset is better to be verified to demonstrate the genelarization of the proposed method.

### Questions
1.This paper argues that the proposed method can smooth the decision boundary of the classifier, how about to visualize the decision boundary?
2.Is there exists obfuscated gradients in the proposed method?
3.Is the proposed method also works well under other attacks such as deepfool attack, C&W attack?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
