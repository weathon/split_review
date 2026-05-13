# What Makes a Good Prune? Maximal Unstructured Pruning for Maximal Cosine Similarity

- Decision: Accept
- Scores: 5, 8, 1, 6

## Abstract
Pruning is an effective method to reduce the size of deep neural network models, maintain accuracy, and, in some cases, improve the network's overall performance. However, the mechanisms underpinning pruning remain unclear. Why can different methods prune by different percentages yet achieve similar performance? Why can we not prune at the start of training? Why are some models more amenable to being pruned than others? Given a model, what is the maximum amount it can be pruned before significantly affecting the performance? This paper explores and answers these questions from the global unstructured magnitude pruning perspective with one epoch of fine-tuning. We develop the idea that cosine similarity is an effective proxy measure for functional similarity between the parent and the pruned network. We prove that the L1 pruning method is optimal when pruning by cosine similarity. We show that the higher the kurtosis of a model's parameter distribution, the more it can be pruned while maintaining performance. Finally, we present a simple method to determine the optimal amount by which a network can be L1-pruned based on its parameter distribution. The code demonstrating the method is available at https://github.com/gmw99/what_makes_a_good_prune

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors explore the use of cosine similarity for quantifying the sparseness-accuracy tradeoff when performing unstructured global pruning of a pretrained neural network. The authors hypothesize that larger values of cosine similarity of the trained weights and the trained weights after unstructured sparsification indicate that the sparsified weights are more amenable to fine-tuning to regain accuracy lost due to pruning. To study this hypothesis, they perform an empirical study using 3 architectures of varying complexity on a single dataset and analyze the cosine similarity of two pruning strategies (random and L1). Research into this problem is motivated by the desire to better understand the complexities of model pruning (e.g., why some pruning strategies and architectures can produce sparse models with higher accuracy).

### Strengths
**Findings of cosine similarity on fine-tunability of pruned models:** Figures 3, 4, and 5 are interesting and summative of findings. Particularly, high cosine similarity of pruned weights to original weights enables 1 fine-tuning step to converge to point in loss landscape close to original optimum (i.e., regaining accuracy lost due to unstructured pruning).

### Weaknesses
 **Limited evaluation:** Experiments only utilize 3 architectures, 2 pruning strategies, and 1 dataset (CIFAR10). I would expect an empirical paper at ICLR to consider at least one additional dataset (ImageNet) and some additional unstructured pruning strategies (e.g., lottery ticket rewinding) would increase impact of findings.

### Questions
1. At the top of p. 7 you state “It is still unclear whether, given more fine-tuning steps, these models can return to the low-loss region from their current position.” Did you consider exploring this more? I think it would be an interesting and worthwhile to empirically explore this direction by increasing the number of fine-tuning steps to see if the pruned models with lower cosine similarity can regain accuracy lost due to pruning.

2. While I find the premise and findings to be interesting, I think the evaluation is limited in that it is only performed on a single dataset. I think the addition of empirical results at least a larger scale dataset, like ImageNet, and additional unstructured pruning strategies would better support the generalizability of the takeaways.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the underlying mechanisms of neural network pruning. It aims to answer questions about why different methods yield similar performance, why pruning cannot be done at the start of training, and how much a model can be pruned without affecting performance. The paper introduces the concept of cosine similarity as an effective measure for functional similarity between the parent and pruned networks. It proves that L1 magnitude pruning is optimal for maintaining maximal cosine similarity and shows that higher kurtosis in a model's parameter distribution allows for more pruning without performance loss. The paper also presents a method to determine the optimal amount of L1-pruning based on a network's parameter distribution.

### Strengths
1. The paper delves into the intricate mechanisms of neural network pruning, providing a understanding of why and how pruning works. This adds a layer of conceptual depth to the existing literature.

2. The paper employs rigorous mathematical proofs to substantiate its claims for the optimality of L1 pruning for maximal cosine similarity. This lends credibility to the research.

3. The paper conducts experiments on multiple architectures like LeNet Small, ResNet18, and VGG11, providing a relatively broad empirical basis for its findings.

### Weaknesses
1.The observation mainly made from the results on the Cifar-10 dataset, whether the observation and conclusion is extendable to other large-scale datasets remain unclear.

2. The paper focuses on specific architectures (LeNet_Small, ResNet18, and VGG11) and does not provide insights into how the findings might generalize to other types of neural networks like Transformers, or other tasks like text understanding. This contradicts the third question, which targets different models.

3. The analysis section, which comprises a significant portion of the paper, lacks logical structure and clarity.

4. Certain observations, such as the point at 80% pruned (Sect. 5.1) in Figures 1c-1d, are confusing, why 80%?

### Questions
See questions in weaknesses above. Additionally,

It looks to me you're computing cosine similarity of a vectorized weight vector and its pruned version, the former containing ALL weights in the network and its size would be humongous, how do you deal with that? Also, that weight vector contains weights of different DNN layers which're segregated by nonlinear activations in the network, why grouping them into one huge vector would work at all? More insights or analytical explanations are needed here.

Moreover, only LeNet, ResNet18 and VGG11 are experimented. I would be interested in seeing edge networks like MobileNet to see how "brittle" they are, and whether these edge nets are already tight for further pruning.

As mentioned, can the findings be extended to other types of neural networks, such as recurrent neural networks or Transformers?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proves that the L1 pruning method is optimal when pruning by cosine similarity. Also it presents a simple method to determine the optimal amount by which a network can be L1-pruned based on its parameter distribution.

### Strengths
* It described the research questions that they would answer clearly early on, and then summarized them again in the conclusion.

### Weaknesses
 * It lacks a justification on why the consine similarity needs to be maximized. The (sub-)structure of the pruned network is different from the original network, which means their (combination of) parameters are not necessarily similar. It would have been nicer if the authors described why it should be consine-similar.

* The paper showed that maximizing cosine similarity is to L1-prune. However, that does not tell if the L1-pruned one is anyway the optimally/best pruned network. That is because, again, similar (combination of) parameters of parent and pruned networks do not necessarily mean that the pruned network is the optimally pruned network.

* Basically, a pruning is supposed to be retrained a lot, repeatedly. It’s unclear how valuable to show that maximizing cosine similarity is the same as removing the least magnitudes (L1 pruning), because the parameters will be retrained (fine-tuned) – then the maintained similarity will be disturbed as well. The theorem holds only when there is no retraining/fine-tuning on L1 pruning.

* Also, the approach does 1-epoch fine-tuning. Is it just for the pruned network? Then what’s the similarity after a 1-epoch fine-tuning? Or if it does not care about cosine similarity after fine-tuning, why does it fine-tune only for 1 epoch, but not multiple times as the SOTA pruning approaches do?

* This work lacks necessary comparisons with SOTA pruning approaches, such as Weight rewinding [1], Learning rate rewinding [2], and Gradual magnitude pruning [3][4][5]. Please consider comparing it with them. Comparing with Random pruning does not provide extremely interesting information.

* It could be overlooked as a minor issue, but because all the results were shown with only one dataset (CIFAR10), they are not convincing. The work is encouraged to be shown with at least 3 benchmark datasets.

* Minor typo: in page 8: in “VGG11 network can be pruned more that the LeNet Small network,”, “that” needs to be “than”.

### Questions
* Basically, a pruning is supposed to be retrained a lot, repeatedly. It’s unclear how valuable to show that maximizing cosine similarity is the same as removing the least magnitudes (L1 pruning), because the parameters will be retrained (fine-tuned) – then the maintained similarity will be disturbed as well. The theorem holds only when there is no retraining/fine-tuning on L1 pruning.

* The approach does 1-epoch fine-tuning. Is it just for the pruned network? Then what’s the similarity after a 1-epoch fine-tuning? Or if it does not care about cosine similarity after fine-tuning, why does it fine-tune only for 1 epoch, but not multiple times as the SOTA pruning approaches do?

* Can this work be compared with other SOTA pruning approaches?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents empirical and some theoretical arguments for making maximal cosine similarity between the parent network and pruning network a more reliable target metric to focus on for optimal pruning and argues for that in a one-shot pruning regime. 

The paper also presents that the longer the tail of the parameter weight distribution it is easier to prune more.

The brevity of the review doesn't stand for the quality of the review or of the paper. The paper was easy to follow and had a precise goal with only a few comments and questions from my side.

### Strengths
1) Motivating problem and setup
2) Precise investigation of what is important.
3) The proposal of cosine similarity as a proxy is simple, intuitive, and just works
4) The experiments help us understand that changing proxy metrics for pruning results in a more reliable way to determine better accuracy of pruned networks. 
5) The empirical investigation is on CIFAR across 3 networks. 
6) Furthermore investigation into loss landscapes and transformation of function space provide interesting insights into a very well-studied problem. 
7) The experimentation and analysis to find the optimal cosine similarity are very interesting and further using it for pruning of neural nets to have minimal loss in accuracy.

### Weaknesses
1) The cosine similarity argument while intuitive and powerful is obvious from the magnitude pruning perspective -- however, what makes it interesting is the generality of it over the course of multiple 1% pruning steps.
2) I understand for every dataset network pair one can find the closest point to utopia, however, this is not sustainable, how to make this scale up across various dataset network pairs at scale?
3) My major concern is that pruning results on CIFAR-10 often are too easy and need more investigation at Tiny ImageNet and ImageNet scale to verify if the empirical insights translate. I would be very happy to increase my score and advocate for acceptance with the presence of ImageNet results on one or two networks (see Blalock et al., 2020 for best practices)

On similar lines, the networks used for CIFAR-10 are often way too overparameterized and that would be handled by experiments on ImageNet.

### Questions
see above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
