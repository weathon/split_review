# Big Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Recent advances in foundation models reveal a promising direction for deep learning, with the roadmap steadily moving from big data to big models/neural-nets to the presented big learning.
Specifically, the big learning exhaustively exploits the information inherent in its large-scale \emph{complete/incomplete} training data, by simultaneously modeling many/all joint, conditional, and marginal data distributions across potentially diverse domains, with one universal foundation model. 
We reveal that the big learning principle 
($i$) underlies most foundation models, 
($ii$) is equipped with extraordinary flexibilities for complete/incomplete training data and various data generative tasks, 
($iii$) potentially delivers all joint, conditional, and marginal data sampling capabilities with one universal model,
and ($iv$) is a new dimension for upgrading conventional machine learning paradigms.
We leverage the big learning principle to upgrade the generative adversarial nets (in this paper), the expectation-maximization algorithm (in the supplementary), and the variational auto-encoders (in the supplementary) to their big-learning variants, with diverse experiments conducted to justify its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new learning paradigm called the Big Learning, where the learning algorithms can simultaneously model joint, conditional, and marginal distributions, by exploring incomplete training data. The authors show that many existing learning paradigms can be viewed as special cases of the proposed Big Learning paradigm, e.g., Masked LM.

After rebuttal: I have read the rebuttal and would like to keep my scores.

### Strengths
The authors introduce a new concept call the Big Learning, which unifies many existing learning paradigms such as Mask LM. Based on this new learning concept, the author proposes advanced versions of GAN and maximum likelihood learning. The authors also run experiments and show the efficacy of the proposed methods.

### Weaknesses
I have mixed feelings about this paper. While the authors propose a new learning paradigm Big Learning that can unify some existing learning paradigms, it seems to me that this new learning paradigm is just a slightly more "advanced" version of self-supervised learning. Can authors highlight the main differences?

Also, the description of experiments in Section 4 is not clear to me, e.g., what is the experiment setups for the ones shown in Fig 2, 3, 4? Specifically, the roles of $x_S$ and $x_T$ in the experiments are not well-defined. It's unclear how the input and output patches are selected and how these choices affect the results. The connection between the theoretical framework and the experimental setup needs further clarification. For instance, how do the different conditional distributions, which are central to the Big Learning framework, manifest in the experimental design?

### Questions
Please see comments above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a general problem called "Big Learning", which generalize various important problems e.g. masked/casual/autoregressive LM, supervised classification, generations,... They argue that big learning can be leveraged to deliver joint, conditional, and marginal data sampling capabilities with one universal foundation model. Then they study the generative adversarial net
(GAN) in the context of big-learning, where the variant is named the BigLearn-GAN. Experiments show the performance of BigLearn-GAN for MNIST/CelebA datasets and the GLUE benchmark.

### Strengths
This paper proposes to generalize a problem for masked/casual/autoregressive LM, supervised classification, generation, which could provide some structural perspective. The authors investigated the GAN network in this context and conduct experiments to test their method.

### Weaknesses
1. The presentation is poor, without the examples the definition of the big learning problem is unclear. The authors should define $x_T$ and $x_S$. Most of the examples only have one pair of $(T, S)$, not a collection.

2. This paper lacks of systematic quantitative comparisons between the proposed approach and existing methods on pretraining foundation models with large-scale data.

3. The claims are not sufficiently supported by the experiments: while the authors argue the potential of the learning framework, the quantitative experiments (table 2 only) is too small and cannot be representative for training FMs.

### Questions
It is important to compare the computational cost of the proposed approach with prior method. Can the authors discuss this?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the big learning that exhaustively exploits the available data information and potentially delivers all joint, conditional, and marginal sampling data capabilities. The authors claim that the big learning (i) comes with extraordinary training flexibilities for complete/incomplete data and for customizing training tasks, (ii) contains most objectives of foundation models as special cases, and (iii) is a new dimension for upgrading conventional machine learning paradigms; Specifically, this paper presents the upgraded BigLearn-GAN as a demonstration example and experiments justify the effectiveness of the presented big learning.

### Strengths
The authors try to propose a big learning framework, which contains most objectives of foundation models as special cases and potentially delivers all joint, conditional, and marginal sampling data capabilities.

### Weaknesses
Quality/Clarity: the paper is hard to follow. The title is too big and it is hard to know its contribution since it aggregates the existing approaches and wants to put everything under this framework. The core concept of 'big learning' remains vague; it's unclear what specific mathematical formulations or algorithmic innovations differentiate it from existing meta-learning or multi-task learning frameworks. The paper lacks a clear definition of what constitutes 'big learning,' making it difficult to assess its novelty and practical implications. Furthermore, if BigLearn-GAN is the contribution, then please compare it with the state of the art, providing quantitative metrics and ablation studies to demonstrate its superiority or unique capabilities. Without such comparisons, it's hard to gauge the practical value of this specific instantiation of the framework.

Originality/significance: the idea is ok, which wants to put all models under this big learning framework. However, it only aggregates the current approaches, and these approaches are known and did before. The paper does not introduce a novel theoretical framework or a new learning algorithm; instead, it seems to re-package existing methods under a new umbrella term. The claim of 'unifying' various models is not substantiated by concrete theoretical contributions or novel algorithmic developments. And if there were a big learning framework, can you guild the machine learning research in the future (for example, design a new model/architecture)? Also I did not see any novelty here. The paper needs to demonstrate how this framework leads to new insights or capabilities beyond what is already achievable with existing techniques.

### Questions
The authors try to unify everything under big learning framework, and if there is such framework, how does it guild our future research? for example, can we find something new (either theory or experimental level) from this framework?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a so-called ‘big learning’ framework that aims to unify the objective functions of most foundation models (such as masked or AR LM or MAEs), and that learns to sample from all conditional and marginal distributions of interest. The paper suggests a big-learning variant of GANs and demonstrate for example qualitatively its performance for versatile image completion. On a GLUE benchmark, it outperforms a naïve fine-tuning strategy.

### Strengths
It is interesting to see that different foundation models can be unified via the big learning framework. 

Learning flexible conditional/marginal generation with the suggested GAN model is new, as far as I am aware. The corresponding (non-naive) adversarial objective function is also well motivated, which I think can be seen as Kolmogorov consistency requirement.

The submission also includes qualitative results demonstrating the performance of the methods for different image competition data sets. 

The paper is largely well written.

### Weaknesses
I am not sure how novel the approach to deliver many/all joint/conditional/marginal sampling capabilities actually is. In particular, conditional [1] or latent [2] Neural Processes models appear to address the same issue. These frameworks also use self-attention [3] or transformer [4] models. It remains unclear if the considered multi-mode training objective considered in this submission are a better choice compared to these prior works. In particular, neural process models are often also quantitatively evaluated on image impainting tasks similarly to Sec. 4.1.

Any quantitative evaluation (and in relation to prior works, e.g. [5]) of the BigLearn-GAN model seems missing. The submission claims that BigLearn-GAN yields ‘generation/completion capabilities with learned adaptive generation diversity’. Since GANs often suffer from mode collapse, it is not clear to me how their approach avoids this issue to achieve diverse sample generation.  

Multimodal generative models (VAEs, etc.) have often been used to ‘unify classification and generation’ as in Sect. 4.3 and it remains unclear to me if the suggested approach improves such approaches (using common quantitative multi-modal evaluation measures).

### Questions
It would be interesting to see how the objective (6) with the 'communication' terms improve relative to the more naïve approach in (5).

Why does the objective for the cross-entropy loss assume that y given x is sampled from a categorical distribution? Why should this not work for more general $p_\theta(y|x)$?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
