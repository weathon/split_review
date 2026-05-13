# Separating common from salient patterns with Contrastive Representation Learning

- Decision: Accept
- Scores: 8, 8, 8, 5, 8

## Abstract
Contrastive Analysis is a sub-field of Representation Learning that aims at separating common factors of variation between two datasets, a background (i.e., healthy subjects) and a target (i.e., diseased subjects), from the salient factors of variation, only present in the target dataset.
Despite their relevance, current models based on Variational Auto-Encoders have shown poor performance in learning semantically-expressive representations. On the other hand, Contrastive Representation Learning has shown tremendous performance leaps in various applications (classification, clustering, etc.). In this work, we propose to leverage the ability of Contrastive Learning to learn semantically expressive representations %when performing 
well adapted for Contrastive Analysis. We reformulate it under the lens of the InfoMax Principle and identify two Mutual Information terms to maximize and one to minimize. We decompose the first two terms into an Alignment and a Uniformity term, as commonly done in Contrastive Learning. Then, we motivate a novel Mutual Information minimization strategy to prevent information leakage between common and salient distributions. We validate our method, called SepCLR, on three visual datasets and three medical datasets, specifically conceived to assess the pattern separation capability in Contrastive Analysis

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a novel concept of contrastive learning for separating common and silent patterns. The approach utilizes two encoders, one responsible for learning silent representation and one for common. The authors propose the criterion to train the model that is based on the InfoMax principle. Due to the fact the direct optimization of the criterion for the problem is difficult and general for the problem, they propose a set of assumptions that allow to training of the model directly using a gradient-based approach. The approach is evaluated using big number of use cases.

### Strengths
- The presentation of the paper is good, and the work is clear and well-written. 
- The proposed method is very interesting and sounds good technically. The flow of the proposed solution seems to be accurate. The authors clearly formulate the problem and general criterion given by eq. 1. Further, they decompose each component and propose a well-justified form of the component for given encoders. 
- The experiments are well-motivated, and the results seem to confirm the hypothesis stated in this work. It is very beneficial that datasets are from a variety of domains, going beyond standard benchmarks.

### Weaknesses
- The model is designed only to model $p(c|\cdot)$ and $p(s|\cdot )$. It would be nice to see some approximation of the distribution over data $p(\cdot|s,c)$. I think that the proposed architecture can be enriched with the decoder that models this probability. 
- I am not quite sure if setting the same architecture for the proposed and reference methods is a good approach. In my opinion, the best architecture for each individual method should be used in experiments. 
- Only VAE-based methods are used as reference approaches. VAEs are doing the additional jobs, they have decoders and serve as generative models, while SEPCLR is only learning the common and silent representation. It would be nice to see the comparison with the models from similar groups, either SEPCLR as VAE, or reference methods that do not preserve autoencoding properties.

### Questions
I would like to ask the authors to respond to the weaknesses section. I will also would like to ask about selecting KDE as a model for this case. Can KDE be replaced with the normalizing flow instead?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a theoretically grounded approach based on contrastive learning, SepCLR, to separate salient features from common features given a weak supervision in the form of a target dataset that contains both salient and common features and a background dataset that contains only common features. A series of mutual information based objective functions and regularization terms are presented along with clear motivation and background behind each of the terms, and the approximate loss functions are derived to achieve these objectives. Experimental results on multiple vision and medical benchmarks demonstrate that a good separation of latents is achieved and the method out-performs prior work. Visualizations of retrievals support their experiments.

### Strengths
This paper is well-organized and well-written. It covers the necessary background on contrastive analysis, provides the theoretical and intuitive motivations on their various objective functions and puts them in context with prior literature, provide the derivations, and also discuss their limitations well.

The main novelty lies in their information-theoritic formulation of the various objectives and more importantly, exploiting contrastive learning and other prior literature to make the various objectives tractable. Another novelty is that they proposed joint entropy maximization to prevent information leakage between the common and salient latents as opposed to mutual information minimization, as the latter strategy can lose information.

Results in Table 1 and 2 show good latent separation on synthetic vision tasks, and that the proposed approach outperforms prior approaches. In addition, they also reveal that the proposed joint entropy maximization is better than other strategies to prevent information leakage. Table 3, 4, and 5 show similar results on the medical domain and the retrieval visualizations support their findings.

### Weaknesses
This paper presents several objectives, but it's unclear which objectives are important and how they work together. This makes it unclear for a practitioner to transfer the results to a different problem. So, I encourage the authors to ablate the different objectives. 

Another weakness is that in Table .4, which is perhaps an important real-world application of the proposed approach, the improvements over prior work is not much. This is in contrast with other experiments i.e. Table 1, 2, 3, 5. The reasoning for this is unclear and also not provided.  

Nit: MMD abbreviates to maximum mean discrepancy and is referred in the paper as moment matching distance [1]. 

[1]: A Kernel Two-Sample Test https://jmlr.csail.mit.edu/papers/v13/gretton12a.html

### Questions
1. Could you provide an ablation study on the various objectives and their impact?
2. In Table 1, 2, what is the performance on the background dataset? Is the salient latent non-informative as it is supposed to be? Is the common term informative?
3. Is the task switch from classification to regression affecting the proposed approach's effectiveness in Table 4?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a technique called SepCLR that uses contrastive learning in order to learn representations that separate common elements from salient ones for the downstream task at hand. The authors examine the performance of their method in creating separate representations for these two elements, and demonstrate improvements over previous work on the same subject.

### Strengths
- The method proposed by the authors is novel, as far as I am aware. Limiting the shared information between the common and the salient space explicitly is an interesting way to ensure that the two encoders model different aspects of the data, leading to less overlap in the information between the two encoders.

- The authors have performed extensive experiments on a variety of datasets, and have also examined several different variations of their proposed method, as can be seen in Table 1. I also appreciate the fact that the datasets used are not only standard ones like MNIST or CIFAR-10, but also come from the medical domain (although I would also appreciate results involving more complicated datasets like CIFAR-100 or ImageNet, which have more object classes available).

- I also appreciate the detailed analysis that the authors provide for the datasets used in the appendix.

### Weaknesses
- As far as I understand, there is an inherent limitation for the method in that knowing the labels for the target dataset is required during training. This limits the applicability of SepCLR in the unsupervised setting, which is also the one most commonly examined by contrastive learning works.

- I believe that there are some issues with the proposed method, that I would be grateful if the authors could elaborate on:

  - The authors make some decisions when designing the loss that go against what is commonly done in related contrastive learning papers. In particular, the loss they propose has the formulation of $L_{unif}$ as found in Wang & Isola [A], but the most commonly used formulation is that of InfoNCE, which differs in that the resulting loss is a sum of Log-Sum-Exp functions, instead of a single Log-Sum-Exp. Similarly, in the alignment term they use a formulation closer to $L_{out}$ from Supervised Contrastive Learning [B], but the same paper notes that another formulation that simply sums the inner products, named $L_{in}$, is better experimentally (the authors examine this in the appendix, but do not explain why they chose $L_{out}$). I would be grateful if the authors could elaborate on these design decisions.

  - Related to the above, it seems that the alignment terms in the common space and in the salient space are different (and similar to $L_{out}$ and $L_{in}$ respectively). I would be glad if the authors could explain why this is the case.

  - In Equation (7), the first term in the sums essentially forces the representations of the salient encoder to be far from the constant vector $s’$. It’s not immediately clear to me why this term is there - it doesn’t seem to arise from optimizing $\hat{H}(S)$, and the informationless hypothesis only comes into play in Equation (8). I think the authors need to explain this part a bit more.

  - Finally, the zero mutual information constraint is somewhat misleading - I understand the point the authors make that minimizing $I(c;s)$ is not the best thing to do, but at the same time, the proposed method does not directly force $I(c; s) = 0$. There is no guarantee that maximizing $H(c,s)$ does not affect the maximization of $H(c) + H(s)$, nor that the final solution will have $H(c,s) = H(c) + H(s)$. I believe that the authors should be clearer about this point.

- I also believe that some points regarding the presentation of the paper can be improved:

  - Tables 1 and 2 contain several variants of SepCLR, but it is not clear what each of them signify. The authors should better explain the variants of SepCLR in this table.

  - Section 4 seems out of place, as it does not come up later in the main paper, and is in fact extremely similar to Section E in the Appendix. I believe that this part should be moved away from the main paper, as currently it throws the reader off (despite the paper having good structure overall).

- Finally, I believe that it would be good to include the baseline of simply training the model using the entirety of the dataset via e.g. SimCLR. While I’m fairly sure that this will not perform as well, it’s still something good to include to get a sense of why the two different encoders are necessary.

### Questions
I would be grateful if the authors could clarify the points I made above regarding the design decisions made for the method and the details of its formulation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel theoretical framework for Contrastive Analysis based on the InfoMax principle, leveraging Contrastive Learning to estimate the common and salient terms, and suggests a strategy to reduce the information leakage between the common and salient spaces. Specifically, the framework consists of two InfoMax terms for the common space and the salient space, and k-JEM for preventing information leakage. In addition, the authors propose a Supervised InfoMax term to disentangle the salient factors. 

The key contributions are:

1) Reformulating Contrastive Analysis under the InfoMax principle with two Mutual Information terms to maximize - one for common factors and one for salient factors unique to the target dataset. 

2) Leveraging Contrastive Learning losses to estimate these Mutual Information terms - retrieving InfoNCE for the common factors and proposing a new background-contrasting loss for the salient factors.

3) Introducing a new strategy called k-JEM to maximize joint entropy for reducing information leakage between common and salient spaces.

4) Extending the framework with a Supervised InfoMax term to disentangle salient factors when attributes are available. 

The experimental results on 5 datasets show k-JEM outperforms other mutual information minimization techniques and significantly promotes separating salient factors and common factors.

Overall, the proposed SepCLR framework and k-JEM regularization demonstrate strong empirical results for contrastive analysis on both visual and medical datasets.

### Strengths
Here are some strengths of the paper:

1. The proposed theoretical framework provides new insights into Contrastive Analysis by formulating it under the InfoMax principle and identifying key mutual information terms to estimate. This enlightens future work on estimating these terms for contrastive analysis. 

2. The paper proposes a strategy to disentangle target-specific attributes within the salient space in a supervised manner when attributes are available. This extends the framework's capabilities.

3. The paper provides an extensive discussion and comparison of several mutual information variational upper bound methods (vCLUB, vUB, vL1out, TC) as well as the strategies of mutual information minimization and distribution matching for reducing information leakage.

4. The derivation of the InfoNCE loss and its alignment and uniformity terms from the InfoMax principle is clearly explained, connecting contrastive learning and information theory foundations.

### Weaknesses
1.  The choice of metrics could also be expanded and analyzed in more detail. For example, the reasoning behind expecting certain accuracy scores is not fully clear. Furthermore, it is not comparable between accuracy of 0% and 20% for (digits,C) on CIFAR-10. 

2. The evaluation is limited to a small set of datasets and tasks. A more comprehensive evaluation on a wider variety of datasets and downstream tasks could strengthen the results. There is limited discussion of hyperparameter sensitivity and scalability to larger datasets. Analyzing the impact of key hyperparameters and demonstrating scalability would be useful.

3. In the disentanglement experiment (Figure 2), some entanglement seems to remain between factors. Using quantitative metrics like MIG and DCI could help analyze this. The sprite changes in Figure 2(b) could also be explained. 

4. Some architectural and mathematical details are unclear:
- The encoder architectures and whether they are independent could be specified. 
- The notation for views v and number of samples Nx, Ny could be clarified.
- Formulas and descriptions could be expanded for readability.

### Questions
Here are some potential questions about the paper:

1. How does Equation 7 constrain `s'` to be information-less? This equation seems to promote the embeddings to be uniformly distributed rather than constraining s' specifically. Some clarification on how the information-less hypothesis is enforced would be helpful. 

2. The alignment terms in Equations 4 and 6 look different - one uses a log summation inside the log, while the other does not. What is the reason for this difference in formulations between the common space alignment (Eq 4) and salient space alignment (Eq 6)? Some explanation or intuition here could help the reader understand.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Ths paper discusses Contrastive Analysis, a sub-field of Representation Learning that aims to distinguish common and salient factors of variation between healthy and diseased datasets. 
Current models based on Variational Auto-Encoders have shown poor performance in learning semantically expressive representations. 
In contrast, Contrastive Representation Learning has shown significant advancements in various applications. 
The proposed method, called Sep-CLR, leverages Contrastive Learning to acquire semantically expressive representations suitable for Contrastive Analysis by utilizing the InfoMax Principle and optimizing Mutual Information terms.
The paper provides both theoretical and experimental analysis.

### Strengths
1. The theoretical analysis is reasonable and easy to follow.
2. The proposed method outperforms baselines by a significant margin on several datasets.

### Weaknesses
1. The submission format of the paper should change to ICLR 2024. It is ICLR 2023 now.
2. It will be better to give some qualitative results on not only the mnist dataset but also X-ray or other real-application data.

### Questions
1. It would be better if higher-resolution images could be provided in Figure 1.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
