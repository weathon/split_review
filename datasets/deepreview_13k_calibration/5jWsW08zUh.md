# Some Fundamental Aspects about Lipschitz Continuity of Neural Networks

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
Lipschitz continuity is a crucial functional property of any predictive model, that naturally governs its robustness, generalisation, as well as adversarial vulnerability. Contrary to other works that focus on obtaining tighter bounds and developing different practical strategies to enforce certain Lipschitz properties, we aim to thoroughly examine and characterise the Lipschitz behaviour of Neural Networks. Thus, we carry out an empirical investigation in a range of different settings (namely, architectures, datasets, label noise, and more) by exhausting the limits of the simplest and the most general lower and upper bounds. As a highlight of this investigation, we showcase a remarkable \emph{fidelity of the lower Lipschitz bound}, identify a striking \textit{Double Descent trend in both upper and lower bounds to the Lipschitz} and explain the intriguing \textit{effects of label noise on function smoothness and generalisation}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focus on the Lipschitz constant of Neural Networks, and in particular focus on different aspect: 1) how and what do we learn from different Lipschitz bounds from the literature and in particular the gap between lower and upper bounds and its evolution during training, 2) the impact of over-parametrisation on the Lispchitz constant and 3) the impact of noisy labels the network lipschitzness. 
The author focus on an intense experimental protocol in order to shade some lights on many claims about the Lipschitz constant of neural networks.

### Strengths
The paper is very nice to read (if the appendix had been printed aside), it covers the topic pretty well and its relationship with related works is well described.

It is mostly an experimental study and it seems to me that the methodology is correct. A lot of experiments in various regime with many different real life instances are quite convincing to me. All experiments lead to a reasonable or theoretically supported interpretation.  
I quite appreciate that many experiences are real life: with trained network of descent size on well known datasets.

### Weaknesses
The article covers many subject and proposes many illustrations of their finding. However a limitation of this work relies in the lack of theoretical insights on the different findings that are discussed (which is an easy weakness to raise for any experimental paper, I admit).

Reading this article is a constant back-and-forth between the main article and its appendix. It often feel that the main article is a glossary to the appendix. As such it often feels like the article should be 'vectorized' and would be better put into a journal format.  
For this reason I find difficult to correctly judge the adequacy of this (paper+appendix) to a conference like ICLR and I am open to this discussion with my fellow reviewers and AC.

Bibliography:

- many references are incomplete: they point at arXiv versions rather than their peer-reviewed publications.
- Some references are doubled such as 'On lazy training in differentiable programming' by Chizat et al.
- Are you certain that the reference to (Gomez et al. 2020) ('Lipschitz constant estimation of Neural network via sparse polynomial optimization') shouldn't be (Latorre et al.) as I do not see the name 'Gomez' in the original paper.

Definition 2.2 is more of a proposition following Definition 2.1.

Section 3.2: How do you compute the convex combinations of the domain samples? Does it actually makes a lot of difference with looking at random points around the samples (say a gaussian centered at a specific sample)? Intuitively it is where one could find the steepest parts of the neural networks rather than convex combinations.

Figure 8: does the practical variance follow the theoretical bound

More generally and in the actual context of the field, it would be very interesting to add experiments with Transformers (with constraint inputs to make it Lipschitz).

**Appendix:**

S4, Intermediate-points based analysis:  
I am not sure about how to go from 2nd line to 3d line of the list of inequalities. It seems to me that $C^{discrete}$ is not the correct constant to consider and in order for the inequality to be correct, the supremum should be considered on all $\theta$. It however doesn't seem to be critical to the result about the growth of the Lipschitz constant through training. Could you confirm or dismiss this comment?

S3.17: I am very surprised with this and I agree with the comment made there, do you have any explanation to propose for such a marginal difference?

S3.18: Have you try to apply the same methods as in S4.1 but for Adam (or maybe RMSprop as it might be easier) optimizer? With maybe minimum assumptions it could shade some lights on this difference of behaviour.

## Typos:

Section 5: 'emprical'

Appendix S3.1: 'btheta' missing '' in tex file probably

### Questions
Definition 2.2 is more of a proposition following Definition 2.1.

Section 3.2: How do you compute the convex combinations of the domain samples? Does it actually makes a lot of difference with looking at random points around the samples (say a gaussian centered at a specific sample)? Intuitively it is where one could find the steepest parts of the neural networks rather than convex combinations.

Figure 8: does the practical variance follow the theoretical bound

More generally and in the actual context of the field, it would be very interesting to add experiments with Transformers (with constraint inputs to make it Lipschitz).

**Appendix:**

S4, Intermediate-points based analysis:  
I am not sure about how to go from 2nd line to 3d line of the list of inequalities. It seems to me that $C^{discrete}$ is not the correct constant to consider and in order for the inequality to be correct, the supremum should be considered on all $\theta$. It however doesn't seem to be critical to the result about the growth of the Lipschitz constant through training. Could you confirm or dismiss this comment?

S3.17: I am very surprised with this and I agree with the comment made there, do you have any explanation to propose for such a marginal difference?

S3.18: Have you try to apply the same methods as in S4.1 but for Adam (or maybe RMSprop as it might be easier) optimizer? With maybe minimum assumptions it could shade some lights on this difference of behaviour.

## Typos:

Section 5: 'emprical'

Appendix S3.1: 'btheta' missing '' in tex file probably

## Overall

The author present a very interesting experimental approach to many Lipschitz claims about neural network and are convincing at exploring, discussing and interpreting their finding. As such I think it is a good paper. My main limitation for a conference is the fact that the paper is mostly located within its own appendix.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the importance of Lipschitz continuity in neural network models, which influences their robustness, generalization, and susceptibility to adversarial attacks. In contrast to previous research that aims to tighten Lipschitz bounds and enforce specific properties, this study delves into characterizing the Lipschitz behavior of Neural Networks. It conducts empirical experiments across various scenarios, including different architectures, datasets, label noise levels, and more, exploring the limits of lower and upper Lipschitz bounds. 

Notably, the paper highlights the strong adherence to the lower Lipschitz bound, identifies a noteworthy Double Descent trend in both upper and lower bounds for Lipschitz continuity, and offers insights into how label noise affects function smoothness and generalization.

### Strengths
- This paper conducted extensive experiments to showcase its findings and offers a comprehensive exploration of experimental details and discussions.
- The paper raised intriguing facets of Lipschitz continuity within neural network models, which are likely to attract substantial interest from the deep learning community aiming to develop theory and practical algorithms based on these observations.

### Weaknesses
 - While the paper provides thorough experiments and in-depth discussions, its novelty might be subject to question. As also mentioned in the paper, there is concurrent research with a similar focus that has also highlighted the connection between the Lipschitz constant and Double Descent, although they tracked only an estimate of the Lipschitz constant. I appreciate the authors’ efforts in sharing more empirical observations and discussions. But I am not very confident that the paper is completely novel.

- From the optimizer's perspective, this paper may have some shortcomings as it does not delve into the discussion of weight decay and dropout, which are widely employed regularization techniques in neural network training. It is noted in the paper that the intention is not to focus on regularization techniques, but there are a few concerns to address. The term "weight decay" is mentioned only once in S2.6.9 (Page 22) with non-zero values. This implies that all other experiments either employ zero weight decay or the paper lacks sufficient implementation details. Similarly, the term "dropout" appears only once in S2.6.7 (Page), and the paper does not provide any insights or discussions regarding the impact of dropout.

### Questions
- As highlighted in the weaknesses section, my primary concern revolves around understanding how commonly-used and seemingly simple regularization techniques like "weight decay" and "dropout" influence the Lipschitz constants. The paper would benefit from thorough discussions in this regard, rather than solely focusing on scenarios without regularization.

- In the context of classification problems, it would be advantageous for the paper to display C_lower values separately for mis-classified samples and correctly-classified samples.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses Lipschitz continuity of neural networks in the following aspects. Firstly, they show the fidelity of the local Lipschitz-based lower bound, by providing several experiments on different models and datasets (section 3.2, also in appendix), and provide their intuition based on a toy example (section 3.3). With that, they investigate the trend of the Lipschitz constant, from initialization and during the course of training. Secondly, they discuss the (implicit) Lipschitz regularisation and double descent behavior, mainly in the context of over parameterization setup of the deep models and a bias variance trade off argument is provided. Thirdly, they discuss about the Lipschitz constant in the presence of the label noise, with the main focus of the network capacities vs the noise strengths. A hypothesis is provided: “while the network is able to fit the noise, Lipschitz constant should increase”, beyond which the network will reach a memorization threshold, and collapse to a smoother function with a smaller Lipschitz constant. In all the 3 aspects discussed, empirical evidence is provided based on several models and datasets.

### Strengths
Extensive experiment to show the different aspects in the discussion, as well as to provide evidence for their intuition and hypothesis.

### Weaknesses
Less theoretical explanation of the different aspects discussed.

### Questions
1. Is it possible to provide theoretical explanation of the different aspects found?
2. Is it possible to extend some of the experiment in any of the language models?

### Soundness
3 good

### Presentation
3 good

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
This paper presents some empirical studies on the Lipschitz constant of neural networks. The studies reveal three major results:
1. the evolution of Lipschitz constant during training; 2. the double descent of Lipschitz constant of neural networks; 3. The Lipchitz contant variation with respect to random labels. The study also shows the fidelity of lower Lipschitz bound.

### Strengths
The perspective and results are interesting: the Lipschitz constant of a function is an intrinsic property of neural networks, and it has connections with many learning theoretical properties. For example, the double descent of phenomenon of neural networks is known and understanding this phenomenon from the Lipschitz constant evolution can be an interesting persepctive.

### Weaknesses
1. Overall this paper lacks coherence. Though this paper studies the Lipschitz constant of neural networks, each question studied in the paper is quite independent. Also these questions are important and each deserves an in-depth study. The empirical result is interesting yet insufficient to understand the phenomenon per se.

2. The paper is also not rigorous. For example, in the intro, the paper stated that "to put it more accurately, it is the maximum absolute change in the function per unit norm change in the input". This statement is only true when the function is scaling invariant. Also because of each question is not studied thourouly, many of the aspects are not rigorously studied. for example, the paper studies effective Lipschitz constant but in reality distributional shift may occur and how the effective Lipschitz constant may change is not known. The scope of this paper is too big and each of the questions requires an in-depth analysis.

3. The paper is also not well-organized. This comes from that the paper lacks coherence. Even though each point is explained, it is still unclear about the message of this paper.

### Questions
The layerwise upper bound is known a loose measurement, and indeed there is a giant gap between the upper and lower bounds in the experiments. Is it possible to strengthen the measurement to have a more precise characterization of the Lipschitz constant?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
