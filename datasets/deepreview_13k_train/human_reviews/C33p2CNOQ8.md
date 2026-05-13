# Training the Untrainable: Introducing Inductive Bias via Representational Alignment

- Decision: Reject
- Scores: 3, 8, 5, 8

## Abstract
We demonstrate that architectures which traditionally are considered to be ill-suited for a task can be trained using inductive biases from another architecture.  Networks are considered untrainable when they overfit, underfit, or converge to poor results even when tuning their hyperparameters. For example, plain fully connected networks overfit on object recognition while deep convolutional networks without residual connections underfit. The traditional answer is to change the architecture to impose some inductive bias, although what that bias is remains unknown. We introduce guidance, where a guide network guides a target network using a neural distance function. The target is optimized to perform well and to match its internal representations, layer-by-layer, to those of the guide; the guide is unchanged. If the guide is trained, this transfers over part of the architectural prior and knowledge of the guide to the target. If the guide is untrained, this transfers over only part of the architectural prior of the guide. In this manner, we can investigate what kinds of priors different architectures place on untrainable networks such as fully connected networks. We demonstrate that this method overcomes the immediate overfitting of fully connected networks on vision tasks, makes plain CNNs competitive to ResNets, closes much of the gap between plain vanilla RNNs and Transformers, and can even help Transformers learn tasks which RNNs can perform more easily. We also discover evidence that better initializations of fully connected networks likely exist to avoid overfitting. Our method provides a mathematical tool to investigate priors and architectures, and in the long term, may demystify the dark art of architecture creation, even perhaps turning architectures into a continuous optimizable parameter of the network.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes guidance, a method where a well-performing guide network directs the layer-wise representations of a target network, transferring inductive biases without modifying the architecture. The technique aims to improve training for architectures traditionally prone to issues like overfitting or underfitting, such as fully connected networks and plain CNNs. Initial results suggest that guidance can improve performance in various settings, but further validation across tasks and more rigorous testing would clarify its robustness and broader applicability.

### Strengths
- The observations are interesting and to some degree novel. 
- A wide range of tasks from several domains are tested empirically. 
-  The paper is well written and methods are explained comprehensively.

### Weaknesses
1. The main observation of the paper is that the performance of suboptimal architectures can be improved if their intermediate representations are matched to a more optimal guide models. This is an interesting observation but somewhat a natural outcome of what we already know.  

	Functionally, representation matching to a guide network allows deeper layers of the target networks to receive useful gradients for learning that they normally do not receive from the task loss. We know that in deep networks w/o skip connections, auxiliary loss functions applied on intermediate layers help with learning [1]. These losses were proposed to mediate the very same issue examined here, that deep CNNs suffer from the vanishing gradient. Relatedly, models with skip connections like ResNets can also be viewed as ensemble of shallow networks as skip connections allow gradient to pass through the deep layers [2]. Suggesting that what skip connections in one way do is to allow many parallel pathways inside the model for letting the gradients flow throughout. I don't see how what is proposed here is fundamentally different from what was show in the prior literature. One way to make this claim more grounded is to show that representation matching outdoes auxiliary losses applied on earlier layers. In general, distillation is a critical missing baseline in all the results. 

	[1] Szegedy, Christian, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, and Andrew Rabinovich. "Going deeper with convolutions." In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1-9. 2015.

	[2] Veit, Andreas, Michael J. Wilber, and Serge Belongie. "Residual networks behave like ensembles of relatively shallow networks." Advances in neural information processing systems 29 (2016).


2. A second primary observation in the paper is that even when the representation is matched to that of an untrained guide network it leads to substantial improvements in the performance of the target network. While this is an interesting observation, specially in cases where this scenario surpasses the matching of the trained network, the portrayal of the results are inaccurate. The main issue lies in considering the untrained model as incapable of performing the task better than chance. In Table 2, the accuracy of the untrained models are reported as being consistently around chance, which is expected if none of the parameters are trained. However, in the context of this paper which uses network representations as guide, the informative measure would be the accuracy of a linear classifier trained on the penultimate layer features. This value is typically much higher than chance and I expect it to be so here as well which attests to the usefulness of the features at their initial state. 
Apart from this, there are more things to be done in order to at least attempt to offer a plausible explanation of this phenomenon. For example, what are the geometrical differences as a result of matching to the untrained and trained networks? Presumably, since the trained model is better able to distinguish between imagenet classes, matching its representations, if successful, should have been more useful for the target network. But somehow that's not true. 

3. The observed higher utility of the untrained guide network becomes more interesting specially when considering the fact that the matching loss term is included throughout the training. One possible explanation could be that the untrained network geometry is simpler to replicate for the target network while the fully trained model could have a much more clustered representation that is too difficult for the target to learn from. This could be tested by using various guide networks at different stages of training and tracking performance when matching to each, then examining any relationship between geometrical properties of the latent space and performance of the target network.

4. Figure 4 results are interesting in showing that even limited training on the matching loss is still helpful. Would the target network its full accuracy in Table 1 if training is done in two phase where the first phase will fully train the network on the untrained guide representations (weight initialization), and phase 2 would do the task training? I think this experiment is important for supporting the claim about finding a good initial weight in these models using the representation matching idea. 

5. At parts, the writing is very verbose. 6.5 pages of the paper is dedicated to the intro, background, and a methods section that contains only modest novelty. Sections 1 and 2 should be written much more concisely to make room for additional experiments. Some of the details of the experiments could also be moved to the appendix. 

6. There are a few papers that are conceptually very similar to the proposed ideas in this paper but were not cited 

https://arxiv.org/abs/1412.6550

https://arxiv.org/abs/1808.01405

7. The last paragraph of introduction talks about the limitations, would fit better at the end of the paper (e.g. in the discussion)

8. Line 116: "To that end, we also did not optimize networks to convergence," this sounds like a serious limitation that could be avoided. If the networks are not trained optimally some of the conclusions may turn out being incorrect. E.g. the observed differences between matching the trained and untrained models. 

9. Line 257: "We describe the task settings": remove 

Overall, this paper showcases very interesting observations but falls short at providing concrete insights. The paper in its current format reads premature. The methods are not novel, the observations are interesting but no real insight is offered. This is study has many potentials but they are not met yet and so I don't think it is ready for publication.

### Questions
1. Figure 3 shows the pattern of error consistency, is this any different from what would be obtained from distillation? 

2. Related to fig. 3, are the intermediate representations of these two guide models also similar? A similar plot could be made for the intermediate representational similarities which would be very informative.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel distillation technique called guiding which distils the inductive priors of the 'guide' network into the target network. The paper shows that by using a known task strong network as the guide, a target network which is known to be weak at the specific task can be significantly improved in terms of performance. The paper then proposes that the guiding network can be disconnected from the process at a very early stage so that it simply acts as a initialisation technique for the network.

### Strengths
- Paper is very well written and even enjoyable to read.
- Technique is novel and proposes a new direction in which the field of distillation can go. 
- Technique could revitalise 'dead' neural architectures which failed to take off due to weak performance.
- Experimentation on multiple modalities.

### Weaknesses
 - I would have liked to see results on smaller datasets. I feel that this could have resulted in a higher number of ablations to determine different configurations of the network e.g. should we be connecting multiple layers to a single layer in the target? Should guide network have the same number of layers as the target? Do all layers in the target need connections to the guide?
- I would have liked to see more in depth discussion of the ViT to CNN/MLP experiments which are hinted at in figure 3.

### Questions
I am interested in discussion on both of the weaknesses that I have proposed. Overall I am positive on this paper, but I feel that if the above weaknesses were addressed, it would improve the paper.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents a simple method for training neural networks that are typically considered untrainable. The approach, similar to the teacher-student methodology, involves training a "target" network with the assistance of a "guide" network, which can be either trained or untrained and may have a completely different architecture from the target. The objective is to align the target network's internal representations as closely as possible with the guide ones in terms of CKA similarity.

### Strengths
* The paper studies an interesting problem trying to solve the problem of untrainable networks
* The authors analyzed multiple scenarios with different tasks and architectures
* The authors provide the supplementary materials with demo notebooks

### Weaknesses
 **Writing and Presentation**: The paper could benefit from improved clarity and readability. Some suggestions to consider: 

* The paper includes expressions that may introduce ambiguity or complexity (e.g. lines 30,42) potentially making it harder for readers to grasp the authors' points fully. Rephrasing these expressions with clearer language would better convey the challenges discussed and enhance accessibility.

* The tables are somewhat difficult to interpret, and it’s unclear if certain entries serve as baselines. For example, Table 2 could be restructured to distinguish between guide and target, rather than using the "experiment" column, and highlight when training is performed without teacher guidance. Making tables and feature descriptions more self-contained and better explained would enhance clarity.

* The Method section could be more clearly organized and written. It is challenging to follow, and restructuring or rephrasing certain parts would likely improve reader comprehension.

* In the Related Work section, the "representation similarity" literature is missing (e.g. 2,4-8). Adding this section could support several claims, such as the one on line 145. 

**Novelty**: The paper’s novelty is limited, as it overlooks relevant related work that addresses similar challenges. For example:

* A similar work exists, such as [1], where authors leveraged relative representations [2] in a teacher-student framework, training the student network to mirror the teacher network’s latent representations.

* The authors’ claim in the conclusion regarding the absence of known methods for improved network initialization is not entirely accurate. For instance, [3] proposed a method for initializing smaller models by selecting subsets of weights from a larger, pretrained model, thereby transferring knowledge from the larger model to smaller architectures.

* Additionally, the experiments lack a comparison with the classic teacher-student setting, which would provide a useful benchmark.

**Contribution**: While the results show some improvement, they also highlight ongoing challenges in making these networks fully trainable. For example:

* In Table 2, the results show an accuracy improvement from 7.5 to 13.10. However, no standard deviation is provided, which limits the interpretation of these results. Moreover, an accuracy of 13.10 is not competitive on this dataset for the image classification task.

* The choice of the networks raises questions, as they do not represent state-of-the-art (SOTA) architectures. It would be interesting to explore whether using a pre-trained network to guide another competitive network could yield further improvements. 

### Questions
* Are the trained guide networks pretrained models that are then fine-tuned during the guidance process?
* Are the untrained guide networks trained in parallel to the target network, or are they frozen during training? If they are not frozen, what is the advantage of training both networks simultaneously rather than focusing solely on training the guide network?
* In Figure 1, when mapping different layers of the guide network to the same layer of the target, it may be important to consider the similarity between these different guide layers.
* How might the results differ if an alternative metric is used to calculate the similarity?
* What impact would guiding only the final layers of the target network have on the results?
* In Table 3, the RNN achieves 100% accuracy and is used as a guide network. What does this imply? Given that the work aims to train untrainable networks using well-performing networks, why use a network that appears to be overfitting as a guide for training the target network?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose an approach for aligning representations across two different deep learning architectures. One architecture serves as the "teacher" (providing guidance) to the "student" (target network). For example, one architecture could a convolution whereas the other could be a transformer. 

Specifically the authors propose training the target network with an additional loss term penalizing the dissimilarity between the target and fixed guidance network. The authors measure the layer-wise dissimilarity using the complement of linear CKA similarity. 

The authors study four tasks (across vision, language, and arithmetic) to illustrate how their approach can improve performance by guiding an ill-suited architecture for the task with a more suitable architecture for the task using their alignment approach.

### Strengths
- The proposed idea is intuitively presented and I believe could serve as a useful tool for studying network initialization schemes as well as scientifically probing the role of architectural inductive biases.
- I appreciate the authors investigating how to bridge our understanding of the role of architecture by providing a principled mechanism for transferring (some) of the architectural biases of one network architecture to another. 
- Empirically the authors selected a diverse set of tasks with reasonable baselines and choice of target versus guide networks. I appreciate how thorough the authors are disclosing training details, hyperparameters, and the intent of the experiments. I also appreciate the error analysis conducted across architectures and the error bounds for experimental results. 
- Authors draw a distinction between typical distillation approaches and the proposed guidance approach that I find clear and well-motivated.

### Weaknesses
 - The field has mostly converged on the transformer architecture for most tasks. While this doesn't make the idea presented less interesting scientifically, I'd encourage the authors keep this in mind when motivating the approach as today, practitioners are not frequently choosing across many choices of architectures. I find initialization and the scientific value of understanding the role of architectural bias still valuable and would encourage the authors emphasize these angles instead.
- The gains for ImageNet are still quite small overall, suggesting we perhaps can't simply transfer over inductive biases or that much much more tuning is needed. Do the authors have any comments on this point? At a minimum, I'd recommend the authors acknowledge and discuss this in the results section. The reported 7.5% validation accuracy on ImageNet using a trained ResNet-18 to guide a Deep FCN is particularly low, raising questions about the practical utility of the approach in its current form. The authors should provide more analysis on why the gains are so limited, and what factors might be hindering the transfer of inductive biases.
- Inconsistent gains across trainable versus untrainable without clear intuition as to why this might be happening. I appreciate the author's attempt at clarifying this in the paragraph starting on line 373, but I still feel this section is missing crucial intuition to help readers make sense for the empirical findings across the tables. For example, why would an untrained ResNet-18 provide better guidance relative to a trained ResNet-18 to a Deep FCN as shown in Table 2. This is puzzling to me and am curious if the authors have additional experiments or intuition to better explain this in the context of the rest of the results. The authors should explore the representational differences between trained and untrained networks, perhaps by visualizing the feature spaces or analyzing the singular values of the layer activations to provide more concrete evidence for their claims.
- The authors make several claims about the revolutionary potential of the method that are not well-supported with evidence. While I'm also excited about the proposed method and potential future work that builds on it, I'd suggest the authors downtone what right now appear as spectulations in this draft. For example, lines 85-86 claim the proposed approach "expands the space of viable networks," a claim I believe is not well-supported by this work. Similar claims are made about potential future promises about guidance on lines 108-112 that are not well-supported by the experiments in the work.
	- Section 4 could be improved. You emphasize a distinction between untrained architectures (versus untrained tasks)—defining Untrainable Architectures as target networks difficult to train irrespective of task. In the experiments that follow however,  the focus is very much on whether a given target architecture is ill-suited for a specific task. The authors should clarify the distinction between an architecture being inherently difficult to train versus being ill-suited for a particular task, and ensure that the experiments align with the claims made in this section.

### Questions
- It's not crucial to the reception of the paper, but I'm curious if the authors explored the evolution of the CKA similarity across layers comparing early versus later layers throughout guidance akin to [https://proceedings.neurips.cc/paper_files/paper/2014/file/375c71349b295fbe2dcdca9206f20a06-Paper.pdf](https://proceedings.neurips.cc/paper_files/paper/2014/file/375c71349b295fbe2dcdca9206f20a06-Paper.pdf) 
- I'm also curious whether the authors explored any other similarity metrics besides linear CKA.
- Perhaps I missed it, but where are the experiments with guidance between architectures with a different number of layers described on lines 230-235?
- Did the authors consider weighing the two loss terms proposed in equation 1?  
- Not necessarily a weakness, but I'm curious whether the authors explored transferring equivariant architectures for tasks with known symmetries.

### Soundness
3

### Presentation
3

### Contribution
3
