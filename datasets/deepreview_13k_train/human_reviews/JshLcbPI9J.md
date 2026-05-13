# Deep Backtracking Counterfactuals for Causally Compliant Explanations

- Decision: Reject
- Scores: 5, 5, 3, 6, 6

## Abstract
Counterfactuals answer questions of what would have been observed under altered circumstances and can therefore offer valuable insights. Whereas the classical interventional interpretation of counterfactuals has been studied extensively, \emph{backtracking} constitutes a less studied alternative where all causal laws are kept intact. In the present work, we introduce a practical method called \textit{deep backtracking counterfactuals} (DeepBC) for computing backtracking counterfactuals in structural causal models that consist of deep generative components. We propose two distinct versions of our method—one utilizing Langevin Monte Carlo sampling and the other employing constrained optimization—to generate counterfactuals for high-dimensional data. As a special case, our formulation reduces to methods in the field of counterfactual explanations. Compared to these, our approach represents a causally compliant, versatile and modular  alternative. We demonstrate these properties experimentally on a modified version of MNIST and CelebA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper implements backtracking counterfactuals [1] in the framework of deep SCMs [2] and points to connections with counterfactual explanations for deep learning models. The paper performs experiments similar to the MorphoMNIST experiments in [2] as well as showing the differences of interventional and backtracking counterfactuals on CelebA.

[1] Von Kügelgen, Julius, Abdirisak Mohamed, and Sander Beckers. "Backtracking counterfactuals." Conference on Causal Learning and Reasoning. PMLR, 2023.
[2 ]Pawlowski, Nick, Daniel Coelho de Castro, and Ben Glocker. "Deep structural causal models for tractable counterfactual inference." Advances in Neural Information Processing Systems 33 (2020): 857-869.

### Strengths
The paper is well written and easy to follow. It combines the idea of backtracking counterfactuals with the deep SCM framework to tackle the problem of counterfactual estimation. The paper is sound and shows convincing results of the differences between interventional and backtracking counterfactuals in high-dimensional settings.

### Weaknesses
The paper is a relatively simple combination of [1] and [2] and it is unclear how important the linearisation of the optimisation procedure is for the performance of the counterfactuals: How well would simple SGD perform? Is the optimisation over u* converging or simply stopped after 30 iterations?
From my understanding, the DeepBC algorithm is limited to handle continuous variables and it is unclear how the choice of distance metric would influence the resulting counterfactuals in case of u's with different dimensionalities along the backtracking trace. Additional ablations comparing the different design choices would strengthen the paper.
Additionally, I would encourage the authors to consider adding quantitative evaluations such as proposed by [3].

Generally, it feels like this paper tries to introduce DeepBC as a combination of [1] and [2], while being a counterfactual explanation paper. I am not sure which of the two it really ends up being. Furthermore, the use of the DSCM framework could be highlighted more.

### Questions
- I saw in the code that the autoencoders use a simple MSE loss without properly modelling the observational noise. Why is this choice made?
- In eq 7 you use an L2 penalty for the distance in latent space. This is very restrictive and would only sensibly work for continuous noise variables.:
  - What's the impact on that if the variables have different noise dimensions?
  - How would this generalise to discrete variables?
  - This does not use any scaling between the variables. In footnote 2, it is mentioned that this isn't necessary because they all assume the same base distribution. I believe this point should be elevated beyond a footnote as it might be lost to readers otherwise.
- You mention that you approximate $F_s$ at $\bar{u}$. Is this correct? What is $\bar{u}$ in this case?
- Why do you use the linearisation? Is this faster than SGD? Did you compare the two?
- Why do we want to enforce sparse changes in $u$? Is this sparse in the dimensions of all u or sparse in the different variables?
- You mention that interventional CF can generate samples in low-density regions and mention it as a weakness. Why is that? Isn't that actually one of the strengths in terms of disentanglement and generalisation?
- You mention that you're using standardized logits for modelling. How do you compute them? What's the impact of using this over discrete variables?
- You mention the composability / modularity as a strength of your work. However, this is generally possible within any causal generative framework, particularly the DSCM framework. What's special about this work in this regard?
- You mention you're using "an image regressor, together with an unconditional AE ...". Can you elaborate how this baseline works?
- You mention that DeepBC does not properly sample from the counterfactual distribution and it didn't yield satisfactory results. Why is that? What were the results?
- As for CF explanations, how does this compare to explaining anti-causal predictions by using causal generative models (e.g. see [4]).

[4] Zhang, Cheng, Kun Zhang, and Yingzhen Li. "A causal view on robustness of neural networks." Advances in Neural Information Processing Systems 33 (2020): 289-301.

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
The paper proposes a particular instantiation of backtracking counterfactuals introduced by von Kugelgen et al. by formalising the counterfactual generation as a tractable constrained optimisation problem in the latent space of a causal model.

### Strengths
- The proposed method draws interesting connections between counterfactuals in explainability literature and causal literature and shows how backtracking counterfactuals can be seen as a generalised form of other.
- The paper is very well written easy to follow the framework introduced 
- Nice illustrative examples on the Morpho-MNIST dataset

### Weaknesses
 - The proposed approach solves an optimisation problem for every counterfactual query, very similar to [1, 2]. Unlike referred papers, the authors here aim to generate faithful counterfactuals respecting the given causal graph; it is unclear how the faithfulness of generated counterfactuals is maintained. (based on results, in the case of celebA it seems like the causal graph is not respected).
- Is identity preservation enforced in the inference optimisation iteration? (as observed in celebA dataset, changing baldness is also affecting gender, facial hair, and age)
- The main difference between the counterfactual explanations and deepBC is that explainability approaches do not use the auxiliary causal variables to generate counterfactual images (at least to the best of my knowledge, I haven't seen any papers using them); using deepBC for generating explanations will severally limit the applicability on datasets with meta information on auxiliary variables and the data generating graph. 
- From an explainability point of view, the metrics like faithfulness, reliability, and robustness of the generated counterfactuals would be interesting to discuss, celebA results suggest that these metrics would be affected 
- It would be useful to have auxiliary models evaluating the identity preservation and faithfulness of the generated counterfactuals and have a comparison against interventional counterfactuals.

### Questions
Please refer to weakness section

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new method to compute the backtracking counterfactuals in structural causal models with deep generative components. The problem is transformed into a tractable optimization in the structured latent space. Through experiments on the data sets MINST and CelebA, the paper also demonstrates that the proposed method has good properties such as being versatile and modular.

### Strengths
A good addition to the existing literature.

### Weaknesses
1. The importance of the problem under consideration is not well-articulated.
2. The performance evaluations lack a quantitative measure to demonstrate the validity of the method. In other words, how do we know if the generated counterfactuals are good or bad?

### Questions
1. Why is it important to generate backtracking counterfactuals?

2. Can the authors provide an important application of their proposed method and demonstrate that the proposed deep backtracking counterfactuals approach provide great solutions for this application?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author proposed a scheme for computing backtracking counterfactuals in SCM.

### Strengths
1. The paper is well-written and is easy to follow.

2. The backtracking counterfactual is an interesting concept to explore.

### Weaknesses
1. First of all, there should be a related work section in the main paper.  I checked the one in the appendix, and it is still not sufficient. If the contribution of this paper is to introduce a new computation scheme for backtracking counterfactuals, you should at least include how existing work computes it. Also, there is a lack of proper citation in the introduction when you compare your work to the existing methods. 

2. My main concern is how significant the proposed method is. It seems like the author optimizes it in the latent space rather than the feature space. Basically, all deep models are learning representations in the latent space, it looks like the proposed algorithm is just an implementation. The paper needs to clarify how the proposed method differs from standard latent space optimization techniques and what specific constraints or modifications are introduced to achieve backtracking counterfactuals. The current explanation is not sufficient to distinguish the proposed method from existing deep learning practices.

3. In the experiment section, the author compares backtracking intervention and conventional intervention, it is more like an introductory article that introduces backtracking intervention.

### Questions
See weakness, and also

How does deepBC perform against other algorithms that also conduct backtracking counterfactual reasoning?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on *backtracking* counterfactuals as opposed to *interventional* counterfactuals that are most frequently considered. It formulates backtracking counterfactuals as constrained optimization using bijective deep structural causal models. Furthermore, it highlights connections to causally compliant counterfactual explanations.

### Strengths
The writing is super clear. I want to thank the authors for such clarity.
I also liked the connection made between backtracking counterfactuals and causally compliant counterfactual explanations.

### Weaknesses
The authors make a very big assumption that they only gently brush in section 2.2:
> We assume that all f_i are given as deep generative models.

This assumption is central, and key to feasibility of their formulation. However, structural causal equations are unknown, and often impossible to figure out solely based on data [1]. Specifically, the assumption of having access to deep generative models for each structural equation is quite strong. While the paper focuses on bijective models, even in simpler cases, identifiability from observational data can be a significant challenge. For instance, even with a known causal graph, without further assumptions, the true structural equations might not be recoverable. This raises concerns about the practical applicability of the proposed method in real-world scenarios where such deep generative models are not readily available. My question to authors regarding this: `How can we get access to structural causal equations underlying our data? How do we ensure identifiability of such equations given observed data?` I will reconsider my score if authors provide a convincing answer.

Some thoughts regarding this matter: Although authors assume access to underlying generation mechanisms, my guess is that this assumption might not be necessary. identifiability of backtracking counterfactuals seems easier than identifiability of interventional counterfactuals, and we might not need access to generation mechanisms for them. For example, if the causal graph is known and certain constraints are placed on the functional form of the equations or the distribution of exogenous variables, it might be possible to identify backtracking counterfactuals without fully specifying the generative models. This is just my intuition, and not rigorous.

### Questions
1. How is  *Deep Invertible Structural Causal Models* defined in section 2.2 or structural causal models with invertible reduced form mentioned in the last sentence of Appendix. D different from BGMs [2]? If they are similar, perhaps you can use some of their identifiability results?
2. In the third line of section 2.3., It took me a while to understand the quoted question. I enclosing $x^*$ with parentheses will help the reader.
3. Why does the title of section 3 contain the word `Deep`? I think your formulation as a constrained optimization is not limited to deep neural networks.
4. In the first line of section 3, why do you use the word `example`? I thought counterfactual explanations explained in the former section are just an application of backtracking counterfactuals. If that is the case, I don't think you should use them when explaining your general formulation.
5. I beleive F should be changed to $F^{-1}$ in the end of equation (4).
6. What is $Y$ in the footnote of page 4? I don't think it's mentioned anywhere else in the text.
7. How computationally expensive is calculating the Jacobian esp. for high-dimensional generation mechanisms such as those of images? Can you provide some numbers? I think this is important esp. for practitioners as you may need many Jacobian calculations for your method to converge.
8. How many iterations does it take for Algorithm 1 to converge? Can you provide some ballparks?
9. How did you choose $\lambda=10^4$? How should we choose it for a new domain? What are the implications of large or small $\lambda$s?


[2] [Counterfactual Identifiability of Bijective Causal Models](https://arxiv.org/abs/2302.02228)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
