# To Grok or not to Grok: Disentangling Generalization and Memorization on Corrupted Algorithmic Datasets

- Decision: Accept
- Scores: 5, 8, 5

## Abstract
Robust generalization is a major challenge in deep learning, particularly when the number of trainable parameters is very large. In general, it is very difficult to know if the network has memorized a particular set of examples or understood the underlying rule (or both). Motivated by this challenge, we study an interpretable model where generalizing representations are understood analytically, and are easily distinguishable from the memorizing ones. Namely, we consider multi-layer perceptron (MLP) and Transformer architectures trained on modular arithmetic tasks, where ($\xi \cdot 100\%$) of labels are corrupted (\emph{i.e.} some results of the modular operations in the training set are incorrect). We show that (i) it is possible for the network to memorize the corrupted labels \emph{and} achieve $100\%$ generalization at the same time; (ii) the memorizing neurons can be identified and pruned, lowering the accuracy on corrupted data and improving the accuracy on uncorrupted data; (iii) regularization methods such as weight decay, dropout and BatchNorm force the network to ignore the corrupted data during optimization, and achieve $100\%$ accuracy on the uncorrupted dataset; and (iv) the effect of these regularization methods is (``mechanistically'') interpretable: weight decay and dropout force all the neurons to learn generalizing representations, while BatchNorm de-amplifies the output of memorizing neurons and amplifies the output of the generalizing ones. Finally, we show that in the presence of regularization, the training dynamics involves two consecutive stages: first, the network undergoes \emph{grokking} dynamics reaching high train \emph{and} test accuracy; second, it unlearns the memorizing representations, where the train accuracy suddenly jumps from $100\%$ to $100 (1-\xi)\%$.git}}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the grokking phenomenon on algorithmic datasets with label corruptions.  In particular, a two-layer MLP is fitted to a modular arithmetic dataset with varying degrees of label corruptions, weight decay, and dropout rates. As a measure of generalization, the authors propose to use the inverse participation ratio, which quantifies the periodicity in the parameters. Experiments show that (i) the model can perfectly memorize the mislabeled examples while achieving near-perfect test accuracy, (ii) the model learns to "correct" some or all mislabeled examples depending on the level of regularization, (iii) the memorizing/generalizing neurons are identifiable.

### Strengths
The paper is written clearly and the results are discussed well. The specific idea of training under label corruption is interesting, which seems to allow for studying memorization on the neuron level. I find some results important (e.g. simultaneous memorization and generalization and sub-network identification) while some are not as significant (e.g. the impact of weight decay).

### Weaknesses
Recently, there have been a series of papers on grokking, most of which rely on empirical analysis of training dynamics or final networks. Although such findings could be thought-provoking, they often come with the risk that findings/questions may apply to the particular setting considered in the work. I'm not sure whether the analysis and findings in this work can be extrapolated to other setups, e.g., different architectures or datasets. This is why I'm closer to a rejection but would be happy to discuss it with the authors and other reviewers.

- The paper analyzes the learning under label corruptions in the same vein as previous works. As shown in Nanda et al. (2023), the algorithm implemented by the algorithm after the grokking phase, roughly speaking, boils down to a handful of periodic functions, which is further confirmed by Gromov (2023) in terms of an analytical solution. Based on this observation, the authors propose to use IPR as a measure of "how periodic a neural representation is", which serves as a proxy for whether a neuron generalizes or memorizes. Then, the effect of pruning individual neurons is investigated in the same spirit as Nanda et al. (2023). All in all, on the procedural side, the only novelties seem to be the use of IPR and label corruption.

- I find the finding that there are separate generalizing/memorizing sub-networks (or rather collections of neurons) interesting. Yet, the identification of these sub-networks is demonstrated on this toy algorithmic problem whose solution is known to be periodic. Consequently, I'm not sure if this finding translates into more general problems with non-periodic subnetworks that generalize.

- I do not understand the main takeaway of sections 3.1 and 3.2. Is there any new finding or just a confirmation of well-known results?

### Questions
- Interestingly, even in the case of full inversion without batch normalization, low IPR neurons do not disappear. Why does this occur? 
- Likewise, batch normalization seems to downweight the low IPR activations but does not zero them out, meaning that memorization still occurs. How do the authors interpret this?
- Multi-modality in Figure 4 alone does not imply low/high IPR neurons memorizing/generalizing as there is no evidence that low IPR neurons are indeed connected to memorization. I think this becomes clear only in the second to the last paragraph of section 2.
- _In trained networks, a larger population of high-IPR neurons leads to better generalization_ requires citation or explanation.
- _Choosing quadratic activation function ... makes the problem analytically solvable._ requires citation.
- _It’s role ..._ <--- typo
- _In the previous Section_ <--- S should be small

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Grokking is a recent empirical phenomenon where training achieves zero error long before neural network models generalize. People have identified this phenomenon to explore memorization vs. generalization and acquire mechanistic understanding of training dynamics of neural networks.

In this paper, the authors present randomization experiments where a fraction of labels are corrupted, i.e., replaced by random labels. A simple arithmetic task, namely modular addition, is used to train a small 2-MLP network. According to levels of memorization and generalization, the trained neural networks are categorized into several regimes: (1) memorization (2) coexistence (3) partial inversion (4) full inversion (5) forgetting. Each regime corresponds to an explanation of the inner mechanism.

### Strengths
Overall, I find this paper very clear and interesting. The authors focus on a recent phenomenon, and by experimenting under idealized data and networks, phase transitions are identified, each with meaningful interpretations.

Some of the key contributions include:
1. Randomization experiments reminiscent of [1], which helps understand generalization of neural nets in the presence of label noise.
2. A clear phase transition phenomenon and separates different data generating regimes into interpretable regions. This may be helpful for understanding the inner workings of neural networks and training dynamics.
3. Clear measurements that quantify the behavior of the trained network.
4. Some insights into regularization techniques such as batchNorm and weight decay.

[1] Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. Understanding deep learning requires rethinking generalization. In International Conference on Learning Rep- resentations, 2017.

### Weaknesses
This paper follows a line of papers that study grokking, and provides a refined analysis of the phenomenon instead of proposing more general principles. 

1. I feel that compared with the initial phenomenon identified in earlier papers, this paper is in a way less innovative.
2. The scope of the analysis is limited, as toy datasets and toy neural nets are studied. It is unclear whether these analyses can generalize to practical settings.
3. This paper does not contain a detailed study of the training dynamics, how the weights behave, or some theoretical analyses. It is unclear whether this paper has impact on the theory community.

### Questions
See the above sections.

In addition, is there any scenario where we believe Partial Inversion or Full Inversion may be observed in practice?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the interplay between memorization and generalization in a controlled setting of synthetic task, where analytical solution exists and can be found by neural network optimizers. It demonstrates interesting behavior where generalization and memorization co-exists, and identified subnetworks that are responsible for each behavior. It further studies how popular regularization techniques impact the interplay between memorization and generalization.

### Strengths
This paper presented a simple synthetic machine learning setting where memorization and generalization can be studied in a very controlled manner. It further demonstrate that memorization and generalization could co-exist, and when it happens, there are clear distinction of subnetworks (at neuron level) that are responsible for each aspect. Moreover, by using the inverse participation ration (IPR), those neurons can be easily identified. This allows the authors to conduct further analysis on how different regularization techniques impact generalization and memorization from the perspective of memorization neurons. For example, it is shown that batch normalization operates in a very different manner from dropout and weight decay. Although the task of study is completely synthetic, it is still valuable to have such a controlled task that demonstrate interesting neural network behaviors such as grokking and memorization/generalization.

### Weaknesses
While some of the results are interesting, this paper is not strong in novelty and depth.

1. The main synthetic task studied in this paper is from previous papers, including the construction of the analytical solution and the matching neural network architecture that could realize such solutions. The main technique to distinguish memorization and generalization neurons, the inverse participation ration (IPR), is also from previous literature. While this paper does has some interesting observations when analyzing the memorization-generalization behaviors, I think it could benefit significantly from more novel analytical or algorithmic contributions.

2. The title and motivation put a lot of emphasis on grokking, yet there are no in-depth analysis of the grokking behaviors presented in the paper. I think the paper could be improved if it could show that the analytical tools used in this paper could bring new insights to our understanding of the grokking behaviors.

3. The experiments could be improved by more in-depth analysis. See below for a few examples.

    1. The paper shows regularizers help improve the generalization and demonstrated the "inversion" behaviors. However, given the emphasis on "grok" from the motivations, I would expect more in-depth analysis and insights to how those regularizers impact the *learning dynamics* that lead to the end result of "inversion" or "coexistence". Specifically, the paper lacks a detailed analysis of how the weight updates and gradient flow change over time with different regularization techniques, and how these changes correlate with the observed generalization performance.

    2. In the case of co-existence, are there any consistent patterns on which neurons would become memorization and which would become generalization? Are they mostly in the lower layer or the upper layer? Do they have different learning dynamics? The paper does not provide sufficient analysis on the location of these neurons within the network architecture, nor does it explore the differences in their learning trajectories, such as the magnitude and direction of weight updates during training. A more detailed investigation into these aspects could reveal crucial insights into the mechanisms of memorization and generalization.

    3. The paper studies the two-layer neural networks with quadratic activation function because analytical solution could be admitted with this architecture. However, most of the empirical studies (e.g. the phase diagrams) does not rely on this property. I think it is very helpful to see experiments with more realistic deep neural networks and diverse neural network architectures to see if they demonstrate consistent behaviors, and if not, to analyze what contribute to the different behaviors. There are some experiments in the appendix but only with small variations of the activation function or the width, and without in-depth analysis.

### Questions
1. The paper uses p=97. Why such a value is chosen? Does the behavior critically depend on the actual value of p (odd, even, prime, very small, very large, etc.)?

2. In Fig.6, the test accuracy remains almost perfect even after 60% of the neurons being pruned. How does the ratio (60%) depend on various aspects of the underlying task? Does it remain constant when the network size changes?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
