# Generalization Guarantees for Representation Learning via Data-Dependent Gaussian Mixture Priors

- Decision: Accept
- Avg Score: 7.20
- Scores: 8, 6, 8, 6, 8

## Abstract
We establish in-expectation and tail bounds on the generalization error of representation learning type algorithms. The bounds are in terms of the relative entropy between the distribution of the representations extracted from the training and "test'' datasets and a data-dependent symmetric prior, i.e., the Minimum Description Length (MDL) of the latent variables for the training and test datasets. Our bounds are shown to reflect the "structure'' and "simplicity'' of the encoder and significantly improve upon the few existing ones for the studied model. We then use our in-expectation bound to devise a suitable data-dependent regularizer; and we investigate thoroughly the important question of the selection of the prior. We propose a systematic approach to simultaneously learning a date-dependent Gaussian mixture prior and using it as a regularizer. Interestingly, we show that a weighted attention mechanism emerges naturally in this procedure. Our experiments show that our approach outperforms the now popular Variational Information Bottleneck (VIB) method as well as the recent Category-Dependent VIB (CDVIB).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the setting of representation learning, where the task is to jointly learn a good representation and a good predictor. PAC-like generalization bounds are provided, which crucially depend on the complexity of the latent representation. Based on these theoretical insights, the authors then suggest a new regularizer term, which shows promising results in some applications.

### Strengths
- Novel generalization bounds for representation learning: The paper derives generalization guarantees for representation learning. To my knowledge, this setting has not been studied in depth previously. I found the remarks about these bounds interesting, particularly the fact that they do not depend on the encoder component.
- Novel regularization term based on the theoretical analysis: As is often the case with generalization bounds, they can directly inspire regularization terms or other modifications to the learning pipeline. The authors propose a new regularization term for representation learning. In experiments with image classification datasets, the introduced method is shown to compete favorably with other recently introduced methods for this task.

### Weaknesses
In general, I found the presentation of some results in the paper to be a bit lacking, while the discussion of related work seems somewhat insufficient. The authors discuss prior work in the introduction, but the discussion is high-level and mainly directed at 'experts' in the field. An additional (perhaps small) section covering related work would have served this paper well. Additionally, the main results of the paper (Theorem 1 and Theorem 2) are presented without much (if any) discussion on the techniques used in their proofs. For instance, it would be beneficial to elaborate on how the shuffling argument is applied in the context of representation learning, and how it differs from standard applications of such techniques. Another example is in line 305, where the authors mention and emphasize the 'geometrical compression phenomenon' but do not describe it further. It is unclear what specific properties of the latent space are being exploited and how this compression relates to the generalization bounds derived. In various places, the manuscript would benefit from additional polishing.

### Questions
I have some concrete questions:
- What is the "joint" (line 1188, Appendix C.3) learning procedure that you followed in the experiments? Can you provide more details on the loss used, etc?
- How do the proof techniques compare to the ones used by SZK23?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides generalization guarantees for representation learning algorithms by deriving in-expectation and tail bounds on generalization error. The authors develop these bounds based on the MDL principle, using a data-dependent Gaussian mixture prior as a regularizer. By establishing bounds related to the relative entropy between representations from training and test datasets, the method aims to leverage the simplicity and structure of the encoder for improved generalization.

### Strengths
1. The paper provides non-vacuous generalization bounds for representation learning.

2. The proposed regularizer has been validated in many image datasets.

3. Theoretical results have been rigorously presented and supported.

### Weaknesses
1. The Gaussian mixture prior introduces additional computational overhead, especially during training, which may make the approach less practical for very large datasets. The computational cost stems from the need to estimate the parameters of the Gaussian mixture, which involves calculating and storing the means and covariances for each component. This overhead is not just a one-time cost but is incurred at each training step, potentially slowing down the convergence, especially when the number of mixture components is large or the latent space has high dimensionality. This is a significant concern for large-scale applications where training time is a critical factor.

2. Although the emergence of a weighted attention mechanism is highlighted, the paper could benefit from a more detailed analysis of this component and its role in generalization. The current analysis lacks a clear explanation of how the attention weights are derived and how they contribute to the overall generalization performance. Specifically, it is unclear if the attention mechanism is directly influenced by the Gaussian mixture prior or if it arises as a byproduct of the optimization process. A more in-depth investigation into the attention weights, perhaps through visualizations or ablation studies, would be beneficial.

3. The empirical validation is limited to standard classification datasets. Testing on real-world tasks beyond classification (e.g., transfer learning, semi-supervised learning) would strengthen the claims of generalization benefits. The current experiments do not fully demonstrate the versatility of the proposed method. For example, it is not clear how the learned representations would perform in a transfer learning setting where the model is trained on one dataset and then applied to another. Similarly, the method's performance in semi-supervised learning, where only a fraction of the data is labeled, remains unexplored. These are important aspects to consider when assessing the real-world applicability of the method.

### Questions
1. What might be the potential limitations of the current method? What could be the future work?

2. Are there any constraints on the applicability in real-world scenarios introduced by relying on a Gaussian mixture prior?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the generalization error of representation learning, in which we have the encoder-decoder model. The authors establish a new generalization bound based on the minimum description length (MDL) of a symmetric prior and the induced representation distribution of the encoder. The paper explains how to choose the prior using a mixture of Gaussians, and connects the generalization bound to the regularizer of the optimization problem, in which the prior and the representation distribution are learned jointly. The authors examine their method in simple datasets and model architectures, and in both lossy and lossless scenarios.

### Strengths
The paper is well-written and the motivation is clear. The authors improved the generalization bound of the encoder-decoder representation learning from $\sqrt{\text{MDL}(Q)/n}$ to $\text{MDL}(Q)/n$. The proposed symmetric prior using mixtures of Gaussians is relatively practical and easy to implement. The idea of adding the generalization bound as a regularizer and learning the prior and the induced distribution of the encoder together is interesting.

### Weaknesses
While the authors have improved on the previous generalization bound, the technical work and the idea of regularization are heavily based on [1]. However, I think the mixture of Gussians is a nice addition.

The lossy generalization bound in Section 3.3 seems a bit incomplete to me. While the authors explain what lossy means, I could not follow how it results in Eq 14 and 15. I also checked the appendix, but could not find anything related to this section. I would appreciate it if the authors could elaborate on this section more, or add a theorem and the proof either in the main text or the appendix. Specifically, the connection between the distortion introduced by the quantization and the resulting bound is not clear. The current explanation lacks the necessary detail to understand how the lossy compression directly translates into the stated generalization bound. It would be beneficial to see a more explicit derivation that shows how the quantization error affects the MDL term and the overall bound.

I also think there are some parts that the author can improve the writing or the intuition of their work (see questions).

### Questions
1. In section 3.3, the bound in Eq 14 seems to be similar to [1] with $\sqrt{\text{MDL}(Q)/n}$ rather than $\text{MDL}(Q)/n$. Do the authors have any intuition/proof on why this change happens in the lossy setting?

2. Is there any intuition behind $h_C$ in Eq 6?

3. In section 4.1, M denotes the number of mixtures. Do the authors suggest any systematic way of choosing M? Or is it a hyperparameter that needs to be tuned?

Some typos also can be addressed:
- Line 342, an addition | in KL
- Eq. 17, the index of X should be batch size and not beta

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the generalization performance of representation learning algorithms (where the models consist of an encoder and a decoder) is considered. Specifically, bounds based on the compressibility of the latent variables of the models are derived. On the basis of these bounds, regularizers using priors with a Gaussian mixture model are devised. These regularizers are numerically shown to provide improved performance compared to prior work for some tasks.

### Strengths
The general problem under consideration is interesting, and the twin goals of explaining generalization and finding ways to improve it are valuable. Interesting connections are drawn between, e.g., the presented bounds and classical compressibility, and between the form of the prior updates and attention. The way in which the regularizer is constructed is, as far as I am aware, new and yields promising results. The numerical experiments compare to several prior alternatives from the literature.

### Weaknesses
The presentation is not always clear. For instance, one of the key concerns about the validity of the data-dependent prior, as far as I understood, is to guarantee that it is symmetric with respect to the training data and a ghost sample. However, the procedure seems to only depend on the training data, and it was unclear to me whether symmetry was preserved. Noise was added at some stages to “partially” preserve symmetry, and allusions were made to prior work which allows for conditions to be only partially fulfilled (e.g. differential privacy), but the results were discussed for exact symmetry.

The relation between prior literature and the presented generalization bounds and data-dependent priors could be discussed to a greater extent.

Minor:

— “date-dependent” in abstract

— Mix of numbering and words in some lists (“(1) First” in line 218, Lines 350-356)

### Questions
1. Can you clarify the data-dependence of the prior, and how this relates to the assumptions under which Theorem 1 is derived?

2. For Theorem 1, the prior to be symmetric (equivalent to the exchangeable priors of Audibert (“A better variance control for PAC-Bayesian classification”, 2004) and Catoni (“PAC-Bayesian Supervised Classification: The Thermodynamics of Statistical Learning”, 2007). In their work, it is often sufficient to consider “almost exchangeable priors”, where permutations are restricted to only swap the $i$th element of the training sample with the $i$th sample in the ghost sample. Would a similar weaker requirement work for your results?

3. Line 266: “when the empirical risk is set to 0.05” What does this mean exactly? Does it mean that you train until the empirical risk reaches 0.05 or below and then stops?

4. In Theorem 1, the bound is provided in terms of a scaled Jensen-Shannon divergence between two Bernoullis. This is reminiscent of the Maurer-Langford-Seeger (MLS) bound in PAC-Bayes, where the corresponding KL divergence is used in the LHS. There are results (Foong et al, “How Tight Can PAC-Bayes be in the Small Data Regime?”, Thm. 4, 2021) indicating that the MLS bound is the tightest possible bound (in some sense) up to the log term. What is the relation between Thm. 1 in the present paper and such preceding bounds? Is it possible to instead use the binary KL in the LHS? (Such bounds also have a fast-rate behavior for zero training loss). I understand that the present paper considers a slightly different setup.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper provides a new generalization bound for representation learning in multi-class classification tasks. The error bound incorporates the recent notion of minimum description length (MDL), which empirically has proven to be more useful than mutual information-based bounds. In particular, the in-expectation bound and tail bound only depend on the encoder part. This has implications that in order to achieve better generalization bound, one can propose a regularizer based on the MDL. This is further studied by approximations using a Gaussian mixture whose mean and variance are data-dependent, and an update scheme for the prior is provided. Several numerical experiments verify the theory.

### Strengths
1. The paper is clearly written and well-organized.

2. The derived bound is tighter than the best bound with MDL.

3. This work provides a quantitative explanation that the encoder plays the role of generalization, as reflected in the bounds in Theorem 1 and 2.

4. Based on the regularization using MDL, a practical and explicit optimization scheme for the prior is provided using Gaussian mixture models.

5. The theory is verified on a few datasets.

### Weaknesses
1. Typo in line 22 of the abstract, "date-dependent" should be "data-dependent".

2. In line 49, the author should make it clear what "MI" stands for before writing "MI-based".

3. In line 86, the author should cite earlier references about the universal approximation with Gaussian mixture, for example, some articles in JRSSB.

4. How do you determine the number of modes in the Gaussian mixture prior?

### Questions
1. Typo in line 22 of the abstract, "date-dependent" should be "data-dependent".

2. In line 49, the author should make it clear what "MI" stands for before writing "MI-based".

3. In line 86, the author should cite earlier references about the universal approximation with Gaussian mixture, for example, some articles in JRSSB.

4. How do you determine the number of modes in the Gaussian mixture prior?

### Soundness
3

### Presentation
3

### Contribution
3
