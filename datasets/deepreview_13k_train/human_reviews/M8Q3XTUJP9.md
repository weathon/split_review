# How does overparametrization affect features?

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Overparametrization, the condition where models have more parameters than necessary to fit their training loss, is a crucial factor for the success of deep learning. However, the characteristics of the features learned by overparametrized networks are not well understood. In this work, we explore this question by comparing models with the same architecture but different widths. We first examine the expressivity of the features of these models, and show that the feature space of overparametrized networks cannot be spanned by concatenating many underparametrized features, and vice versa. This reveals that both overparametrized and underparametrized networks acquire some distinctive features. We then evaluate the performance of these models, and find that overparametrized networks outperform underparametrized networks, even when many of the latter are concatenated. We corroborate these findings using a VGG-16 and ResNet18 on CIFAR-10 and a Transformer on the MNLI classification dataset. Finally, we propose a toy setting to explain how overparametrized networks can learn some important features that the underparamaterized networks cannot learn.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
They study the neural representations of thin and wide deep neural networks. Their main finding is that concatenating the latent representations of multiple thin networks does not result in representations that are as useful as a single wide neural network. Their primary experiments involve seeing how well the activations of a wide network can be reconstructed from the concatenated activations of thin networks using a linear layer and vice versa.

### Strengths
- I think that the approach is mostly novel and clever. I think the results make a very clear case for their conclusions. This seems like a valuable piece of evidence related to understanding neural representations. I’m glad this work was done.
- The paper is very well-written.

### Weaknesses
1. I think this paper is well-done but lags somewhat behind its time. I think this area of research was much more popular and cutting-edge a few years ago. In that sense, I think this paper can be a good one but probably is not groundbreaking enough to be great. This criticism will not factor into my overall rating.
2. The experiments did not scale past the CIFAR and MNLI scale.
3. I think there are some related works that should have been discussed. I recommend considering adding the ones below.
    - https://arxiv.org/abs/2212.11005
    - https://arxiv.org/abs/2106.07682
    - https://arxiv.org/abs/2110.14633
    - https://arxiv.org/abs/2010.02323
    - https://arxiv.org/abs/1912.04783
4. My biggest reservation about the paper is that there are multiple ways of comparing the similarity of neural representations. This paper introduces the FSE and FSG, but I do not see why prior methods were not considered. At a minimum, these deserve discussion. Section V.G of [Rauker et al. (2022)](https://arxiv.org/abs/2207.13243) discusses single neuron alignment, vector space alignment, CCA, singular vector CCA, CKA, deconfounded representation similarity, layer reconstruction, model stitching, representational similarity analysis, and probing. I do not think that the paper does a good job of overviewing related work and comparing their measures against baselines.
5. Why use a linear layer to define the FSE? Why not allow yourself to use a nonlinear layer? Other works from the model stitching literature have done this, e.g. [Bansal et al. (2021)](https://arxiv.org/abs/2106.07682). I would not be shocked if the main result from 3.2 didn’t hold much for a nonlinear version of FSE.
6 I see no error bars in some of the figures. Were these results based on one trial? Or are the error bars too small to see?

### Questions
5. Why use a linear layer to define the FSE? Why not allow yourself to use a nonlinear layer? Other works from the model stitching literature have done this, e.g. [Bansal et al. (2021)](https://arxiv.org/abs/2106.07682). I would not be shocked if the main result from 3.2 didn’t hold much for a nonlinear version of FSE.
6 I see no error bars in some of the figures. Were these results based on one trial? Or are the error bars too small to see?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the overparametrization of neural networks from the perspective of their expressive power. Specifically, the paper compares a wide network with an ensemble of shallow network that has the same width of the wide network. The paper uses a ridge regression between features to measure their expressive power. The paper demonstrates that even after concatenating many models, underparameterized features cannot cover the span nor retrieve the performance of overparameterized features. At last, the paper uses one specific case to show the difference of small and large network and what leads to the difference.

### Strengths
1. The paper studies an important problem of overparametrization, and show that ensemble of small models cannot recover the expressive power of overparameterized models.

2. The paper proposes FSE, which arises from ridge regression, to measure the  expressive power.

### Weaknesses
1. The paper does not justify why the ridge regression is an appropriate method to measure the expressive power. As it is known to all, the network is a very complicated non-linear models. The true expressive power should be analyzed in terms of the function classes of these two kinds of networks. Specifically, the paper uses ridge regression to measure the capacity of the learned features, but it is unclear if the linear approximation is sufficient to capture the expressive power of the non-linear features. The paper should provide more justification on why the linear approximation is a good measure of expressive power in this context. 

2. The paper does not justify why comparing overparameterized models with an ensemble of shallow models is important or meaningful. As an ensemble of small networks has fewer parameters than the large network, why is this a fair comparison? The paper should clarify the motivation behind comparing a single wide network with an ensemble of shallow networks, especially when the parameter counts are not directly comparable. It is not clear what specific insight this comparison is intended to provide about overparameterization.

3. The paper only provides empirical observations and lacks of theoretical analysis. The paper would be significantly strengthened by theoretical analysis that supports the empirical findings. Without theoretical grounding, it is difficult to generalize the conclusions beyond the specific experiments conducted.

4. The mathematical symbols of the paper is a little bits complicated, which makes the paper hard to read.

5. Although the case analysis in section 4 is interesting, the result is only applicable to one very specific data distribution. Can the authors connect the data distribution to more general cases?

Minor

1. Missing section number of "RELATED WORK"

2. Why do the authors use ridge regression to measure the expressive power instead of plain linear regression without regularziation? The use of ridge regression introduces a regularization term, which might affect the measurement of the expressive power. The paper should justify why this regularization is necessary and how it impacts the results.

### Questions
See "Weakness" section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work tries to investigate the difference in learned features between overparametrized and underparametrized networks. The authors explore this point by comparing regular networks (e.g. VGG-16, ResNet18) with corresponding thinner networks (e.g. ResNet18 with half channels in each layer). By using a feature cross-prediction (linear) method, the authors show the feature difference between regular networks and thinner networks. Then this work further compares the feature difference between regular networks and the concatenation of many narrower networks. Finally, the authors conclude these investigations as "overparametrized network learns more expressive than the underparameterized one".

### Strengths
- writing is clear and easy-to-understand. 
- the idea of investigating the feature difference between over-parameterized and under-parameterized networks is interesting.

### Weaknesses
 - The most basic requirement to verify this paper's point,  "Do the features of overparameterized networks exhibit greater expressivity than the features of low-width networks, given that they tend to perform better?", is to have **a close training performance of overparameterized network and low-width networks**. So that both networks are well-learned. Otherwise, the feature difference can come from well-learned / poorly-learned networks instead of overparameterized / underparameterized networks. 
- Table 1 and Table 2 tell me the feature difference actually comes from well-learned / poorly-learned networks.  Table 1 (b) shows the FSE feature difference starts to increase at $\alpha=1/8$. meanwhile, table 2 shows the training accuracy starts to decrease at the same time ($\alpha=1/8$). Please note that when $\alpha < 1/8$,  Table 2 shows a very similar training accuracy (99.81 - 99.99) but different validation accuracy (92.72 -95.29). Table 1 ($\alpha < 1/8$) doesn't reflect feature differences.
- The proposed FSE score (Definition 2.2.) is a common metric. [1] shows (almost) the same feature score. [3] computes a linear regression between two sets of features. Canonical Correlation Analysis [2] also shares a close idea. 

- The feature concatenation of independently learned networks was tested in [3]. But they get a very different conclusion about feature concatenation. Probably because they allow models to be well-learned. So that they avoid the well-learned / poorly-learned network problem.

### Questions
- I suggest the author choose a regular network (e.g. resnet18) as a low-width network and use a much wider (more channels) version as the base network (overparameterized). So that you can avoid the well-learned /poorly-learned network problem.
- It is not called "shallow" in Section 4 title " HOW DO WIDE MODELS CAPTURE FEATURES THAT SHALLOW ONES CANNOT?". In general, "shallow" indicates less layers. I suggest "thin".

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the influence on the number of parameters (over- vs. underparameterization) on the learned features. In particular, the work investigates whether a concatentation of independently trained underparameterized networks (with similar parameter count) retrieves the expressive power and performance of an overparameterized network. To scale networks, the work employs scaling of network widths, while keeping other network hyperparameters, such as depth, fixed (Sec. 2.1 & 2.3). To analyze feature similarity, they introduce some metrics: feature span error (Sec. 2.2), feature span gap (based on FSE; Sec. 3.2), and feature performance (Sec. 2.4). They find that underparameterized networks cannot fully capture the features of overparameterized networks, and vice versa (Sec. 3.2). Thus, they conclude that the networks seem to learn distinct features. Further, the features from the overparameterized have higher predictive prowess (Sec. 3.3). Finally, the work provides a toy example to show that some features can only be learned by overparameterized networks (Sec. 4).

### Strengths
* All metrics are intuitive and sound.

* The analyses are interesting.

* The toy example is interesting and sound.

* Code is provided in the supplementary results.

### Weaknesses
 * The research question has significant flaws. That is, independently trained underparameterized networks are likely to converge to similar feature representations, as each of them tries to minimize the target loss and, thus, only the features with the largest effect on the target loss are learned (given the more restrictive capacity constraint from the width scaling). On the other hand, overparameterized networks do not suffer from such an issue and can use their larger capacity during training to learn more (and other) features to further reduce the target loss. Consequently, this raises substantial concerns about the empirical findings.

* The paper is hard to follow. For example, the varying notation makes it hard to read without keeping track of notation and resolving ambiguities. E.g., why is $\beta$ needed if $\alpha$ suffices and seems to also be used interchangeably by the authors, e.g.:
   * Eq. 2.1
   * vs. “linear combination of the features $\{ m_{\beta}(x_k)[s]\}^{\beta n_L}_{s=1}$” (p. 3)
   * vs. $\{ m_{\beta}(x_k)[s]\}^{\alpha n_L}_{s=1}$ (p. 4)?

* Besides the above, the paper seems partially unordered. E.g., why are the proposed metrics interleaved with the setup on how the networks are scaled?

* The introduced metric “feature performance” is only a linear probe and not an original contribution of the work.

* The feature residual analysis has contradictory results (Fig. 4a vs. 4b and Fig. 10). For the transformer setting, it is quite clear that the residual features help in predictive performance. However, for the ResNet setting this is not clear, as for $\alpha=1/8$ and $\alpha=1/16$ the difference is negligible. There is no discussion on this.

* Sec. 4 seems to reiterate the lottery ticket hypothesis (the initial weights are particularly effective or ineffective for training). It is unclear how this relates to the empirical findings of the present work.

### Questions
* Do the authors ensure the same random initialization between the overparameterized and the underparameterized networks (assuming that layer widths are integer multiples of $\alpha$)?

* How do the underparameterized networks perform on the target task compared to the overparameterized network?

* Seemingly, the underparameterized CIFAR-10 models improve their predictive performance for $\alpha=1/2$ in Fig. 3. Is there any explanation by the authors for why?

* How are the feature residual experiments conducted? I.e., how are these features “appended”? Is a new linear mapping $W^{(L+1)}$ learned for the additional features?

* How is the MLP scaled in Sec. 4?

## Suggestions

* As mentioned above, the paper would be easier to follow by substantially improving the presentation. For example, instead of $\beta$ and $\gamma$ in Def. 2.2, it would be easier if the authors would just use $\alpha_1$ and $\alpha_2$ instead.

* Table 1 should be within the page size limits.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
