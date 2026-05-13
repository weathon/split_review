# A Demon at Work: Leveraging Neuron Death for Efficient Neural Network Pruning

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
When training deep neural networks, the phenomenon of "dying neurons" —units that become inactive and output zero throughout training—has traditionally been viewed as undesirable, linked with optimization challenges, and contributing to plasticity loss, particularly in continual learning scenarios. In this paper, we reassess this phenomenon through the lens of network sparsity and pruning. By systematically exploring the influence of various hyperparameter configurations on the occurrence of dying neurons, we unveil their potential to facilitate simple yet effective structured pruning algorithms. We introduce "Demon's Pruning" (DemP), a method that controls the proliferation of dead neurons, dynamically sparsifying neural networks as training progresses. Remarkably, our approach, characterized by its simplicity and broad applicability,  outperforms existing structured pruning techniques, while achieving results comparable to prevalent unstructured pruning methods. These findings pave the way for leveraging dying neurons as a valuable resource for efficient model compression and optimization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript provides mathematical and empirical support for the authors' argument that neuronal death is governed by settings of common hyperparameters (batch size, regularization strength, etc.). They leverage this observation by choosing hyperparameter settings that prompt neuron death, allowing them to prune such neurons to obtain training speedups. The results improve on those of other structured pruning algorithms on ResNet18, VGG16, and ResNet50.

### Strengths
Relative to other structured pruning algorithms, the proposed pruning approach (DemP) is more accurate and providing of stronger speedups. 

The idea to prune dead neurons for efficient training is, as far as I know, original. If it can be shown to be helpful in more contexts (see "Questions" below), this method's simplicity and intuitive justification will make it impactful. 

The manuscript provides a mathematical analysis in Section 3.2 that provides further intuition for the neuron death problem and its relationship to training hyperparameters, which is generally helpful. 

The experiments (those analyzing neuron death and those analyzing DemP) are well designed and clear -- e.g., baseline structured pruning methods that are compared to DemP are thoughtfully chosen.

### Weaknesses
The experiments left unclear the practical relevance of DemP. As discussed more thoroughly below (see "Questions"), training in a wider variety of contexts and using more competitive training setups as baselines will help clarify whether DemP provides speedups that are relevant to readers' work/research.

The experiments on CIFAR10 with ResNet18 achieve lower accuracy than typically reported, and the manuscript should clarify if this is due to the regularization approach used to encourage sparsity. If the decreased accuracy is an inherent limitation of the method, it should be clearly stated. The comparison to unstructured pruning methods is also not ideal, as the baselines are not well-tuned, making it difficult to assess the true performance of DemP relative to unstructured approaches. The manuscript should also provide more details on the unstructured algorithms to provide needed context for their performances. The benefit of DemP relative to unstructured pruning should be framed around its ability to provide speedups, rather than matching weakly-tuned unstructured pruning algorithms on accuracy. Furthermore, the ImageNet results lack detail on the accuracy-efficiency frontier created by DemP, and the baselines should be trained by the authors to ensure a fair comparison.

Figures should be closer to where they are discussed. E.g., Figure 4 is two pages away from where it's explained.

The second paragraph of Section 3.1 should be made clearer -- where are the 3904 neurons that are referenced coming from?
The Maxwell's demon analogy in the intuition section is slightly unclear, perhaps clean this up a bit to avoid confusion. 
At the top of page 5, a simplified version of Equation 4 is referenced, I think "3" is meant.
In equation 5, is eta in the denominator or numerator of the exponent? I think it's the latter but the typesetting leaves this unclear.
The last sentence of the third to last paragraph on page 5 is unclear, I think an "=0" is missing.
Figure 7 has an incorrect caption.
On page 8, you reference Table 5, I think you mean Table 1.

### Questions
Score-affecting:

1. More results on speedups from DemP would be great to see. For instance, using your method, can you improve on the Mosaic ML ResNet50 ImageNet training time result? (See https://docs.mosaicml.com/projects/composer/en/stable/tutorials/train_resnet50_on_aws.html.) 
2. ResNet18 typically gets ~95% accuracy on CIFAR10 but does not in your experiments. Could you please explain the hyperparameter choices causing the gap? 
   - If the decrease in accuracy is caused by the regularization approach you use to encourage sparsity, that is seemingly a limitation of the proposed method that should be stated clearly. 
3. In the main text, please make clear that the baseline methods compared to (e.g., EarlyCroP) are not using the (potentially suboptimal) regularization schedule required by DemP. I believe they are not based on my reading of Sections F.1 and F.3, but please correct me if I am wrong.
4. Is DemP effective on more modern architectures like ViTs or language models? Exploring transformer models need not require a significant increase in compute (e.g. results on GPT-2 Small would be interesting and that model is not too much larger than ResNet50).
5. The fact that unstructured pruning baselines aren't well tuned, which is noted in the manuscript, should coincide with more cautious claims about performance relative to unstructured pruning. 
   - A well tuned magnitude pruning algorithm on ResNet-18 using CIFAR10 data actually improves baseline accuracy (95% accurate) at 95% sparsity (96% accurate); see Figure 1 of Diffenderfer et al. (2021).
   - Consider complementing Figure 6 with more details (in the main text) on the unstructured algorithms to provide needed context for their performances. 
   - Relative to unstructured pruning, the benefit of DemP to emphasize is probably its ability to provide speedups (as opposed to its ability to match weakly-tuned unstructured pruning algorithms on accuracy).
6. It would be great to see ImageNet accuracy at a few different DemP sparsity levels in a figure that supplements Table 1 (i.e., show the accuracy-efficiency frontier created by DemP). 
7. In Table 1, train your own baselines (at least for the dense model). 
   - Right now, it's unclear what to attribute the gap between Dense and DemP to (training code differences or DemP's effect).


Important:
1. Figures should be closer to where they are discussed. E.g., Figure 4 is two pages away from where it's explained. 

Minor:

1. The second paragraph of Section 3.1 should be made clearer -- where are the 3904 neurons that are referenced coming from?
2. The Maxwell's demon analogy in the intuition section is slightly unclear, perhaps clean this up a bit to avoid confusion. 
   - If I understand correctly, the demon in that thought experiment is needed because there's otherwise a lack of a mechanism for entropy decreasing. When it comes to a neuron's transition to death/life, however, there are actual mechanisms (e.g., learning rate size) that govern transitions; no hypothetical demon is needed. Perhaps the function of the analogy is to clarify that, before the present manuscript, neuron death transition was treated too much like a black box (or demon). In any case, I suggest revising the "Intuition" paragraph that discusses this analogy. 
3. At the top of page 5, a simplified version of Equation 4 is referenced, I think "3" is meant.
4. In equation 5, is eta in the denominator or numerator of the exponent? I think it's the latter but the typesetting leaves this unclear. 
5. The last sentence of the third to last paragraph on page 5 is unclear, I think an "=0" is missing. 
6. Figure 7 has an incorrect caption.
7. On page 8, you reference Table 5, I think you mean Table 1.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the dying neurons phenomenon in network pruning. By employing the random walk model for network parameters, it reveals that neurons that become inactive during training may be challenging to recover. The study also explores how different hyperparameter configurations impact the occurrence of dying neurons. The authors thus introduce the "Demon’s Pruning" (DemP) to remove dead neurons in real time as they arise. This method dynamically prunes networks during training and outperforms some existing structured pruning techniques as shown in the experiments.

### Strengths
- Offers some insights into mechanisms of neuron mortality through the lens of network sparsity and pruning and provides analysis into the influence of gradient noise/learning rate/regularization. Experimental results support its findings to some extent.
- The proposed pruning method seems simple, computationally efficient, and straightforward to implement.

### Weaknesses
 - The concept of pruning neural networks by eliminating inactive neurons based on their activation doesn't appear very novel. Several prior papers have explored the notion of dead neurons in sparse neural networks or proposed activation-based pruning methods [1,2,3]. Specifically, the idea of identifying and removing neurons that consistently output zero activations has been explored in various contexts, and the contribution of this paper in this regard is not immediately clear. It's important to differentiate this work from existing methods that use similar criteria for pruning, such as those that target neurons with low activation frequencies or magnitudes.
- The analysis section seems to oversimplify the problem. It remains a question whether this analysis, built on Brownian motion model of weights rather than some model of activation, can effectively explain the activation-based pruning method. The Brownian motion model, while useful for illustrating stochastic weight dynamics, may not fully capture the complex interactions and dependencies that govern neuron activations in deep networks. The model focuses on individual weight behavior, but the activation of a neuron is a function of all its weights and the input data, making the link between the Brownian motion of individual weights and the overall activation pattern not immediately obvious. Furthermore, the model's assumption of constant noise might not hold true in realistic training scenarios.
- The paper is generally easy to follow, but certain sections could benefit from additional details to make it more self-contained and less confusing. For instance, providing background information on Brownian motion, discussing implicit assumptions when using absorbing Brownian motion model, and offering a clear definition of 'dead neurons' in the context of convolutional neural networks would enhance clarity. Specifically, the paper should explain how a neuron's feature map is considered 'dead' if all its elements are zero, especially when dealing with batch processing and how this is different from a neuron with very low activation across a batch.

### Questions
- I'm curious about the definition of 'dead neurons' in convolutional neural networks and what specific structures DemP will remove.

- I'm also interested in understanding why a one-dimensional absorbing Brownian motion can effectively represent the weight dynamics of neural networks. Does the behavior of weights align with the assumptions of this model?

- The experiments employ a one-cycle scheduler for the regularization parameter. Is the comparison with other baseline methods also using the same regularization? It's important to consider that regularization may impact model performance.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposed a method “Demon’s Pruning” (DemP) for structured pruning, which removes dead neurons during training. The paper studied the phenomenon of dying neurons during training and how the choices of hyperparameter configurations impact how dying neurons occur in neural networks. Experiment results on CIFAR-10 and ImageNet show the advantages of the proposed method DemP.

### Strengths
1. The paper studied the setting of dying neurons during training, which is missing in existing structured pruning approaches.  
2. The perspective of learning a structured sparse network during training is interesting and promising.

### Weaknesses
1. No speedup evaluation is conducted. As a method for network pruning, it is expected to conduct real inference speedup evaluation over the original dense model.  
2. It seems that the method is essentially a structured version of existing sparse training methods, e.g. RigL. It is not clear to me the technical contribution of this work.  
3. The theory in section 3.2. seems not useful and redundant. It is not related to the method DemP itself.

### Questions
1. It is not clear to me why we should compare a structured pruning method with unstructured pruning methods, e.g. in Table 1. Since DemP is a structured pruning method, we should compare with possibly more structured pruning baselines?
2. Could the authors provide speedup evaluation of structured pruned models? 
3. Could the authors illustrate clearly the difference of the “dynamic pruning” procedure in the paper and existing sparse training methods, e.g. RiGL and iterative magnitude pruning? It looks to me they are essentially the same except DemP is removing neurons while sparse training methods remove individual weights.
4. Adjust the theory part in section 3.2 and explain how it is related to DemP. It seems right now they are just some fancy equations which is not helpful for understanding the paper.

### Soundness
4 excellent

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
This paper introduces "Demon's Pruning" (DemP), an innovative method that utilizes dying neurons for model optimization, and provides a comprehensive exploration of hyperparameters influencing neuron mortality. The authors demonstrate DemP's superior performance over existing structured pruning techniques and its competitive results with unstructured methods.

### Strengths
1. Insightful exploration of dying neurons, establishing their utility in structured pruning algorithms.
2. Introduction of the simple yet broadly applicable DemP, which outshines current structured pruning techniques.
3. Extensive empirical validation of DemP's effectiveness across multiple benchmarks, with comparative analysis against other pruning methods.

### Weaknesses
1. The paper's motivation is somewhat unconvincing. Encouraging neuron death during training may compromise the expressivity of neural networks, potentially leading to performance degradation. The authors, however, propose accelerating neuron death and subsequent pruning. What is the motivation to accelerate the neuron death? (I understand the authors' motivation, i.e., pruning, but why just have a "normal" speed of pruning as the neurons will die at the end of training with a high probability.) Besides, It's worth noting that several existing works already prune networks by removing small-weight "dead" neurons without the need for prompting [1, 2] in structured pruning and unstructured pruning, e.g., magnitude. 
2. the paper lacks direct evidence that dead neurons **remain inactive** during training, despite the existence of previous works validating this hypothesis, such as the overlap coefficient [3]. 
3. The experiments in Fig 2 suggest that noise may contribute to the accumulation of dead neurons, but its role appears to be more like an amplifier than a key driver. Moreover, the effect seems to depend on the noise type. The section seems more focused on expanding the word count which makes this paper inconsistent, and the experimental details on noisy updating are insufficient. Additionally,

Minor:
1. The unit of Dead Neurons Variation in Fig. 3 is unclear.

### Questions
see the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
