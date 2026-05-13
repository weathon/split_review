# Unveiling Linear Mode Connectivity of Re-basin from Neuron Distribution Perspective

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
In deep learning, stochastic gradient descent (SGD) finds many minima that are functionally similar but divergent in parameter space, and connecting the two SGD solutions will depict a loss landscape called linear mode connectivity (LMC), where barriers usually exist. 
Improving LMC plays an important role in model ensemble, model fusion, and federated learning. Previous works of re-basin map different solutions into the same basin to reduce the barriers in LMC, using permutation symmetry. It is found that the re-basin methods work poorly in early training and emerge to improve LMC after several epochs. Also, the performances of re-basins are usually suboptimal that they can find permutations to reduce the barrier but cannot eliminate it (or the reduction is marginal). However, there is no unified theory on when and why re-basins will improve LMC above chance, and unveiling the behind mechanism is fundamental to improving re-basin approaches and further understanding the loss landscape and training dynamics of deep learning. Therefore, in this paper, we propose a theory from the neuron distribution perspective to demystify the mechanism behind the LMC of re-basin. In our theory, we use Shannon entropy to depict the uniformity of neuron distributions and derive that non-uniformity (entropy decrease) will result in better LMC after re-basin. In accordance with our theory, we present the following observations, all of which can be aptly explained by our theory. i) The LMC of re-basin changes in various non-uniform initializations. ii) The re-basin's LMC improvement emerges after training due to the neuron distribution change. iii) The LMC of re-basin changes when pruning with different pruning ratios. 
Building upon these findings, we further showcase how to apply our theory to refine the performances of other neuron alignment methods beyond re-basin, e.g., OTFusion and FedMA.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a conjecture that behavior of loss barrier in Linear Mode Connectivity (LMC) of Deep Neural Networks can be explained through entropy (non-uniformity) of distribution imposed on the neurons of the network. The authors show that for multi layered perceptron the loss barrier between two networks are upper bounded by O(polynomial(number of neurons in hidden layers) x exponential(entropy of neuron distributions)). The paper goes on the explain that pruning results in reduction in entropy and hence loss barrier of LMC for pruned networks are better, resulting in higher accuracy of fused model. The experiments in the paper are two fold (a) to show empirically that entropy and LMC are connected (b) apply pruning to various existing methods for better fusion of deep networks.

### Strengths
The ideas presented in the paper are interesting and could have potential applications in understanding of LMC, as well as in improving accuracy of model fusion methods. 

a) The connection between loss barrier of LMC and entropy is novel and should be explored further. 

b) The application of pruning in model fusion seems to be a positive direction in improving the accuracy of fused model.

### Weaknesses
Paper is hard to follow and there are many questions that arise upon reading it.

The first question that is aimed to answer is about hardness of LMC at initialization as in Ainsworth et al. The answer that paper gives is that it depends on the entropy of the initialization, but there is no correspondence to the initial question in a sense of considering same experiments as in Ainsworth et al. and changing initialization to less entropy one. Moreover, already at Ainsworth et al. it is mentioned that in a concurrent work it was shown that mapping found after training improves LMC at initialization. How can entropy explain this? In Entezari et al. it was proven that for wide networks LMC is possible at initialization. How does this result connects to the entropy?

The authors use definition of the barrier introduced in Entezari et al. Nevertheless, it is not quite clear to me how \alpha is selected there (and later in the paper Entezari et al. just use 1/2, thus returning to the classical definition of Frankle et al.). I wonder how the authors use this definition. Moreover, in the theorem 3.1 instead of bounding barrier, some other value is bounded - supremum over difference between network output for interpolated weights and interpolation of network outputs. This already does not correspond to any of the definitions. I can assume that they still can be linked, but this linking is not given in the paper.

Proof of theorem 3.1 does not require permutations per se - it is introduced in the very end to shrink the barrier. So overall, it should mean that entropy of neuron distribution can bound the difference between output of interpolated model and interpolation of the models? Moreover, result in lemma 3.2 requires 0 mean of the distribution of the neuron weights - I think it does not have to be the case in a trained network. Finally, the proof of theorem 3.3 is absent. While it is connecting theorem 3.1 and lemma 3.2 it requires some polynomial properties of the network, which are not explained.

The experiment in section 4.2 uses a network with sigmoid activation. Such activation is known to bin into two corner cases with training (see discussion about experiments in the work on information bottleneck of N.Tishby). Therefore the demonstrated peaks in the values of the weights does not necessarily mean the desired result.

The argument for why pruning by itself does not result in decrease of the barrier value is not convincing for me. The value of the barrier is normalized by the losses of the two initial models, therefore it should not mean that the barrier will be high if models do not perform well. And fine-tuning after matching is known to always improve LMC, so once again this experiment does not show the desired result.

Minor:

- currently, pruning does not smoothly integrate in the paper: in the introduction it is formulated as "we observe that pruning can improve LMC, but what is the mechanism", while in the paper itself pruning is directly proposed as a method to decrease entropy.

- the Figure 1 is very sloppy - why the shadow areas are exactly where solutions would be? How is it justified?

- the formulation "making neuron distribution gather around minima" is unclear to me

- in the introduction it is controversially claimed that the proposed method makes re-basin easier, while it is not the case

- neuron entropy and neural entropy are used in parallel in the paper, while neuron entropy is the term introduced

- lemma 3.2 is called theorem 3.2 in the text

- using assumptions from another paper (Mei et al.) without explaining them (at least in appendix) makes the paper not self-contained

### Questions
Q1) Could you provide the comparison between the relative order of magnitudes of various constants in the presented Theorem 3.1? It seems crucial to understand the same to understand the impact of entropy in that equation.

Q2) Consider two untrained VGG network on MNIST dataset vs two trained VGG network. As seen in Figure 4, the trained networks have non-trivial loss barrier. But the non-trained networks would have closer to zero loss barrier because they already are at a high point in the loss landscape. There can be different ways in which this can be made to happen. However the entropy of trained networks are lower, but it does not explain the different in loss barrier? This seems contradictory to the result in the paper.

Q3) I don't seem to get grasp on how bias could be added to weight matrix through small adjustment as mentioned just before section 2.2. Please elaborate the same in the light of if equation 3 still holds. 

Q4) In experiment 4.1, why are the curves later fit to the observation vs plotting the entropy exp(.) function.

Q5) Are bias terms = 0 in all the networks considered in experiments? If not how is OTFusion extended for the same.

Q6) Could you please why LTH does not lead to good fused networks? Different matching algorithms should be able to combine two models generated by LTH.

Q7) What does '/' mean in Table 2? Please also include base model accuracy for fusion. Why are models fine tuned till epoch 30? 

Typos:

a) Please fix VGG11 vs VGG16 in Table 2 and section 5. They seem to be interchangeably used.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors aim at their research to explain the linear mode connectivity, i.e., the ability of neural networks to be connected by a low loss line, through the properties of the weights values distribution. In particular they are using discrete Shannon entropy of the weights distribution as a characteristic that should be low in order to allow for low barrier between models. They provide a theoretical result for the upper bound on the difference of network outputs that depends on the entropy of the weights distribution. Further they evaluate empirically the values of the barrier and entropy for the newly initialized models, after training and after pruning. It is proposed to use pruning as a method for enhancement of the linear connectivity via empirical results with some state-of-the-art vision models and fusion methods.

### Strengths
Paper aims at having a theoretically justified result about effect of entropy on the barrier between two models. Additionally, this result is used to propose an applicational enhancement for permutation based matching between networks in order to fuse them (as a fusion ensemble or federated learning).

### Weaknesses
Paper is hard to follow and there are many questions that arise upon reading it.

The first question that is aimed to answer is about hardness of LMC at initialization as in Ainsworth et al. The answer that paper gives is that it depends on the entropy of the initialization, but there is no correspondence to the initial question in a sense of considering same experiments as in Ainsworth et al. and changing initialization to less entropy one. Moreover, already at Ainsworth et al. it is mentioned that in a concurrent work it was shown that mapping found after training improves LMC at initialization. How can entropy explain this? In Entezari et al. it was proven that for wide networks LMC is possible at initialization. How does this result connects to the entropy?

The authors use definition of the barrier introduced in Entezari et al. Nevertheless, it is not quite clear to me how \alpha is selected there (and later in the paper Entezari et al. just use 1/2, thus returning to the classical definition of Frankle et al.). I wonder how the authors use this definition. Moreover, in the theorem 3.1 instead of bounding barrier, some other value is bounded - supremum over difference between network output for interpolated weights and interpolation of network outputs. This already does not correspond to any of the definitions. I can assume that they still can be linked, but this linking is not given in the paper.

Proof of theorem 3.1 does not require permutations per se - it is introduced in the very end to shrink the barrier. So overall, it should mean that entropy of neuron distribution can bound the difference between output of interpolated model and interpolation of the models? Moreover, result in lemma 3.2 requires 0 mean of the distribution of the neuron weights - I think it does not have to be the case in a trained network. Finally, the proof of theorem 3.3 is absent. While it is connecting theorem 3.1 and lemma 3.2 it requires some polynomial properties of the network, which are not explained.

The experiment in section 4.2 uses a network with sigmoid activation. Such activation is known to bin into two corner cases with training (see discussion about experiments in the work on information bottleneck of N.Tishby). Therefore the demonstrated peaks in the values of the weights does not necessarily mean the desired result.

The argument for why pruning by itself does not result in decrease of the barrier value is not convincing for me. The value of the barrier is normalized by the losses of the two initial models, therefore it should not mean that the barrier will be high if models do not perform well. And fine-tuning after matching is known to always improve LMC, so once again this experiment does not show the desired result.

Minor:

- currently, pruning does not smoothly integrate in the paper: in the introduction it is formulated as "we observe that pruning can improve LMC, but what is the mechanism", while in the paper itself pruning is directly proposed as a method to decrease entropy.

- the Figure 1 is very sloppy - why the shadow areas are exactly where solutions would be? How is it justified?

- the formulation "making neuron distribution gather around minima" is unclear to me

- in the introduction it is controversially claimed that the proposed method makes re-basin easier, while it is not the case

- neuron entropy and neural entropy are used in parallel in the paper, while neuron entropy is the term introduced

- lemma 3.2 is called theorem 3.2 in the text

- using assumptions from another paper (Mei et al.) without explaining them (at least in appendix) makes the paper not self-contained

### Questions
Please see questions in the section "Weaknesses".

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the theory of re-basins, explores when and why re-basins improve linear mode connectivity, and examines the problem from a neuron distribution perspective. The authors conducted analytical experiments on neuron distributions with different initializations, comparisons before and after fine-tuning, pruning, and more. Notably, the pruning-then-fine-tuning experiments yield interesting findings. Finally, the authors demonstrate how to apply their theory to other methods, such as OTFusion and FedMA.

### Strengths
- This paper examines linear mode connectivity (LMC) after re-basin through changes in neuron distribution. 
- The authors provide both theoretical analysis as well as practical experiments. 
- The finding that pruning and then fine-tuning at a higher rate improves re-basin is an interesting discovery. 
- The writing is clear.

### Weaknesses
The analysis using entropy is rather trivial in hindsight; for instance, different initializations result in a higher entropy of the neuron distribution (Fig. 2), and training changes the neuron distribution from uniform to bi-modal (Fig. 3). Overall, the theoretical/analytical contribution may be somewhat thin.

### Questions
N/A

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper connects the theory of random matching problem and the weight matching method of Git Re-basin (Ainsworth et al). They give an upper bound over the loss barrier between two models and the bound is related to the distribution of model parameters (which could be formulated as discrete entropy). Also, they find pruning could potentially decrease the loss barrier between two models after re-basining.

### Strengths
- First of all, the authors identified an important problem that is why the permutation methods (including weight matching proposed in Ainsworth et al., 2022 and Entezari et al., 2021) could achieve LMC between two independently trained models and why they fail in some cases (e.g. early training). 
- A good point of this paper is to build the connection between random matching problem and loss barrier between two models. 
- Also, the phenomenon that pruning could potentially decrease the loss barrier after re-basining is interesting.

### Weaknesses
Theoretical side:
The theorem 3.1 tells a simple conclusion that is the loss barrier between models are bounded by the distance between their model parameters, which is intuitive and aligns with most literatures (I am not questioning on theorem 3.1). The theorem 3.2 gives an upper bound over the distance between two random model parameters. After that, theorem 3.3 just combines above two theorems. Therefore, I thought the core part of this paper is simply the theorem 3.2 (sometimes the author refers it as Lemma 3.2, which might be a typo...). 
- However, in a real case, the model parameters might not be "random" and the bound given by theorem 3.2 might be useless in practice. In that case, the relation between the loss barrier and the entropy could be overestimated.
- Also, the theorem 3.2 actually directly comes from the random Euclidean matching problems (as mentioned by the authors in Sec 3.)
Above all, the theoretical contribution of this paper is marginal.

Experimental side:
1. Sec 4.2, the experiments are quite "toy" (Polynomial Task, single output MLP and only first layer are tested). For both Sec 4.1 & 4.3, the experiments are conducted over standard image classification task and models, however, for Sec 4.2, the experiments are quite trivial. Harder datasets and models are needed for Sec 4.2.
2. Still 4.2, only the change of distribution of model parameters before training and after training cannot show a strong correlation between the loss barrier and entropy. More carefully designed experiments are needed.
3. Pruning experiments are interesting but the explanation of why Only Pruning and Lottery Ticket Hypothesis fail is not that clear. Actually, the failure cannot be predicted by their theoretical analysis.
4. From Figure 5, the loss does not always first decrease and then increase. For MLP and CIFAR-10, the loss first increases with pruning ratio actually. The phenomenon contradicts with the results of other dataset and models. Also, the loss curves of train dataset and test set are not always consistent.
5. The entropy before and after pruning should be presented for comparison.

Overall, the experimental contribution is not sound to me.

### Questions
1. For Sec 4.1, I wonder if all the models are all randomly initialized, how could loss barrier exist? Because in my mind, one randomly initialized model could be a "random guess" classifier, and therefore, if two "random guess" classifier are interpolated, the interpolated model should still random guess, then there couldn't exist any loss barrier.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
