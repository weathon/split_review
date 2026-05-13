# Bridging Lottery Ticket and Grokking: Understanding Grokking from Inner Structure of Networks

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Grokking is the intriguing phenomenon of delayed generalization: networks ini-
tially memorize training data with perfect accuracy but poor generalization, then
transition to a generalizing solution with continued training. While reasons for this
delayed generalization, such as weight norms and sparsity, have been discussed,
the influence of network structure, particularly the role of subnetworks, remains
underexplored. In this work, we link the grokking phenomenon to the lottery ticket
hypothesis to investigate the impact of inner network structures. We demonstrate
that using lottery tickets obtained at the generalizing phase (termed ‘grokking
tickets’) significantly reduces delayed generalization on various tasks, including
multiple modular arithmetic, polynomial regression, sparse parity, and MNIST.
Through a series of controlled experiments, our findings reveal that neither small
weight norms nor sparsity alone account for the reduction of delayed generalization;
instead, the presence of a good subnetwork structure is crucial. Analyzing the
transition from memorization to generalization, we observe that rapid changes
in subnetwork structures, measured by the Jaccard distance, correlate strongly
with improvements in test accuracy. We further show that pruning techniques
can accelerate the grokking process, transforming a memorizing network into a
generalizing one without updating the weights. Finally, we confirm the emergence
of periodic inner-structures, indicating that the model discovers internally good
structures (generalizing structures) suited for the task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper examines the phenomenon of "grokking," in which neural networks first achieve high training accuracy but poor generalization, then later switch to a generalization solution with more training. Earlier explanations explaining grokking along the lines of reducing weight norm are challenged, and it is argued that the identification of the "grokking tickets" specific subnetworks aligned with the lottery ticket hypothesis-play a key role in enabling generalization.

The authors provide empirical evidence that (1) grokking tickets can be used to overcome the phenomenon of delayed generalization observed in dense networks; (2) similar weight norms fail to overcome the need for long training if the subnetwork proper is missing, and finally, structure optimization alone--without weight updating--can transform memorization solutions into generalization solutions. These suggest that good sub-network search is more important to grokking than weight norm reduction, but it does offer a different perspective in regards to how generalization within neural networks happens.

### Strengths
Originality is demonstrated because the author tries to bridge two concepts that were seen independently before: the lottery ticket hypothesis and grokking. To put it in words, this can be shown through the proposition that the primary driving force behind grokking is not weight norm reduction but identification of a special subnetwork of "grokking tickets". Fresh angle of attack, challenging explanations of the form: what's really critical here is not just the simplicity of the model but the actual discovery of the subnetworks. One might expect this to have the effect of making a contribution that is more novel in its theoretical framing and prompts further exploration into the roles of sparsity and subnetwork structure more generally in generalization.

Quality-wise, the paper is sound because the experimental setup is robust, and careful comparisons across various models, including MLPs and transformers as well as tasks like modular arithmetic and MNIST, assure to critically analyze the idea. The methodology of the experiment controls very well, isolating the effects of subnetworks from confounding factors like weight norm. Indeed, that work can be labeled as comprehensive because it shows the use of multiple pruning techniques, establishment of a critical pruning ratio, and the use of experiments with edge-popup. All these conclusions strengthen the final conclusion drawn by the paper and reflect what should have been the actual efforts of the authors in being extremely cautious while testing their hypothesis.

The paper is clearly written in general. Authors described and explained the main concepts, including grokking tickets and their corresponding different pruning techniques used to find those subnetworks. Different experimental results of figures and graphs added clarity between grokking, weight norms, and subnetworks. Some parts of the theoretical sections, especially on the aspects that involve metrics, such as Jaccard similarity and frequency entropy, are highly supported by visual aids that enlighten the sub-network relationships and generalization.

The paper carries great value in terms of possibilities for reshaping discussions regarding delayed generalization and generalization mechanisms for neural networks. Treating the subnetworks as the focal point for grokking thus opens up avenues for research into model efficiency and interpretability, and maybe even efficiency in pruning. Moreover, if validated further, this approach is bound to have a considerable impact on thinking about training over-parameterized networks among practitioners and researchers and especially in identifying the optimal subnetwork. This approach for grokking could then be applied further to the realms of reinforcement learning and others, all pointing towards a wide-ranging impact of the discovery.

### Weaknesses
While extremely compelling and a new perspective on grokking, there are still some weaknesses of the paper, especially regarding theoretical justification, experimental scope, and clarity of interpretation.

One weakness lies in the theoretical motivation for why subnetworks (grokking tickets) are enough to explain grokking. Although experimentally subnetworks are shown to generalize faster than their dense counterparts, why it is that the subnetwork is generalizing and not in cases where weight norm fails remains slightly implicit. A discussion of some of the theoretical underpinnings of why some subnetworks well-perform, perhaps leveraging the insights from some recent sparsity studies on neural networks (e.g., Varma et al., 2023; Merrill et al., 2023) would significantly strengthen the conceptual framework and move it closer in line with prior work. Making such results more explicitly connectable to theoretical explanations of neural network generalization, such as in terms of double descent or simplicity bias, would go a long way in contextualizing the findings within a broader landscape of generalization theory.

The experimental setup is comprehensive but could be further extended to strengthen the generality of the results. For example, the main experiments are with simple modular arithmetic tasks and MNIST, which are suitable but quite simplistic and not necessarily representative of more complex distributions or task structures, as in natural language processing or computer vision. Further experiments would expand the complexity of the datasets and architectures used-for instance, BERT on NLP tasks or ResNet on CIFAR-10, which might be even leading towards more inference on whether the grokking tickets are consistently beneficial across a wide range of tasks and architectures. In this sense, an expanded effort would go to show how solid the results are and could further generalize their applicability.

Finally, even though the authors do account for the role of structural similarity in terms of Jaccard similarity in their grokking explanation, one might further explore what the implications of such a metric would be. Indeed, this could again relate to how variations in structural similarity over training align with the grokking process or consider how it would relate to properties of generalization. The other aspect where there is room for improvement includes the fact that the significance of subnetwork structures can be further ascertained through the use of other metrics for measuring the similarity of networks, based on weight sparsity patterns or neuron activations. Lastly, the paper could do much better in establishing the connection between experimental findings and practical implications.

For example, even though the study proves that a subnetwork can be learned without weight decay, it may be more helpful to know how this might impact the practices in the real world in terms of training or pruning neural networks. It would also provide more concrete recommendations or at least some hint on possible applications of grokking tickets to better connect the theoretical insights to practice. This will not only make the contribution much more vivid, but also emphasize how important the findings are for the more general community of practitioners of machine learning. In other words, the paper does provide a good foundation, yet it could further be improved with a more detailed theoretical justification, broader experimental validation across complex tasks, a deeper exploration of structural metrics, and clearer practical implications. Such refinements would make the work more comprehensive and more impactful in advancing our understanding of grokking and neural network generalization.

### Questions
1. It would be great if you provide more theoretical insight into why it is enough for generalization to have the presence of certain subnetworks (grokking tickets)? It would be interesting to know if there is an undercurrent mechanism, besides the empirical evidence, that could be given to support the idea that it was really the subnetworks that drive the transition from memorization to generalization and not the weight norm. Lastly, would it be possible to learn other relevant theories on generalization, for example, simplicity bias or double descent, which could place these findings into a wider context?

2. Although the paper does very nicely on modular arithmetic and MNIST, how would grokking tickets generalize to a few domains, perhaps such as NLP, like using a model such as BERT? Or image recognition, such as applying a CNN to CIFAR-10? This would help in generalizing the results. Can the authors comment on whether grokking tickets applies to other forms of tasks or known limitations for those other domains?

3. Since the results show generalization with the appropriate subnetworks instead of depending on weight decay, do the authors have any insights on practical takeaways? For instance, how do these grokking tickets that were discovered alter regimes of training, pruning of models, and the choice of architecture? Including more specific recommendations on how to leverage grokking tickets in practice better opens up findings for practitioners to put into action.

4. The paper introduces Jaccard similarity to measure structural similarity between subnetworks, yet does not delve enough into the implications of this metric. Could the authors go into additional detail about which variations in structural similarity correlate with stages of grokking? Specifically, does some degree of Jaccard similarity correspond to a "critical" sub-network structure predictive of successful generalization? Further research on the nature of structural similarity resulting from training might shed further light on grokking tickets.

5. The authors introduce a critical pruning ratio, such as 0.81, needed to achieve generalization without weight decay. Would the authors comment upon how that ratio could vary by architectures and datasets? A more in-depth examination of how the result is sensitive to this pruning rate and others can help to explain how reliably grokking tickets can be identified across different setups.

6. While the authors have employed Jaccard similarity and frequency entropy to compute quality metrics of subnetworks, do they also explore other metrics for validation of soundness of their results? For example, capturing the degree of similarity in activation of neurons or any such sparsity-based metrics might prove the significance of certain structures of subnetworks as well. This will likely reiterate that in fact subnetworks are prime essentials for generalization.

7. The authors show that typical pruning-at-initialization methods, such as SNIP and Synflow, cannot efficiently produce grokking tickets. Are the authors willing to provide more analysis into why such classical PaI methods do not elicit generalization? For example, is something inherently different between the identified subnetworks by the former methods compared to grokking tickets? This comparison would help clarify the unique properties of grokking tickets and guide future improvements in these techniques.

8. The experimental results seem to suggest that the structures of subnetworks change over time. Can the authors provide some illustrations-for example, weight heatmaps or connectivity graphs of subnetworks-probing the evolution through multiple training phases? Such illustrations would make the process more intelligible, where grokking tickets form and generalize, and serve to additionally demonstrate their role in delayed generalization.

9. The paper records that grokking tickets facilitate the generalisation when compared with dense networks. Is it possible for the authors to probe for a predictable point during the training regime where these sub-networks first arise? Investigating whether there is some measurable "onset" of generalization with grokking tickets, maybe utilising Jaccard similarity or other measures, might reveal important transition points in the training regime.

10. Some phenomena of generalization, like the double descent phenomenon, have been studied to some large extent. Would it be interesting if the authors were able to delineate how grokking tickets might relate to these other phenomena? For example, is an appearance of grokking tickets associated with first descent in a curve describing a situation of double descent? If one is able to draw these relations, it may give grokking tickets a context of being part of a bigger picture of generalization dynamics of neural networks.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work explores the phenomenon of grokking in neural networks, where models initially memorize training data without generalizing well, but after extended training, they suddenly begin to generalize effectively. Specifically, it investigates the relationship between grokking and the lottery ticket hypothesis---within a large neural network, there exist smaller, trainable subnetworks (or "winning tickets") that can achieve comparable performance to the original network. The authors introduce the concept of "grokking tickets", which are subnetworks identified during the generalization phase of training. They further show that the change of inner structure (subnetworks obtained by the magnitude pruning) highly correlates with the change in test accuracy.

### Strengths
The authors establish an innovative link between two significant phenomena in deep learning: grokking and the lottery ticket hypothesis, which provides new insights into understanding the generalization of neural networks. The experiments span multiple tasks, and the authors have also conducted thorough ablation studies to verify their hypothesis.

### Weaknesses
While this work presents an interesting investigation connecting grokking with the lottery ticket hypothesis, it is still unclear how the finding can be of practical usage, and some claims in this work still need more justifications (e.g., "the acquired good structure is linked to good representations") In particular, although the authors introduce Fourier Entropy to quantify the periodicity in the learned representations, it is still unclear how specific/different "periodicity" can be regarded as good representations. Also, the paper mainly explores grokking within fully connected networks and lacks a broad examination across various network architectures. For example, adding experiments across a wider range of architectures (e.g., Transformers) would increase the generalizability and appeal of the findings.

### Questions
1. How are grokking tickets fundamentally different from typical winning tickets found in lottery ticket hypothesis studies? Are there specific characteristics or properties that distinguish grokking tickets, or could they potentially overlap?
2. Do the authors have insights into the specific structures of the subnetworks (grokking tickets) that facilitate the transition from memorization to generalization? For example, do different types of tasks have different structures in their grokking tickets?
3. How does the finding generalize to other neural network structures (e.g., Transformer) and language-based tasks?
4. How does pruning affect the abilities of pretrained models in terms of grokking?
5. Why does periodicity in representations correlate with good performance?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the grokking phenomena of the subnetworks identified by the pruning methods in the Lottery Ticket Hypothesis. The findings of the paper are mainly three-fold. First, they show that, compared with the whole network, the subnetworks exhibits a shorter "grokking period", leading to a better generalization result faster. Second, they provide evidence to support that neither the weight norm nor the sparsity of the subnetwork is the crucial factor for the shorter "grokking period". Lastly, they show that the difference between the pruned subnetworks is related to the test accuracy at the point they are pruned, and that the subnetworks learns better representations from data.

### Strengths
1. The paper has a clear presentation of the experimental setup, which follows the previous works on grokking. This experimental design choice increases the effectiveness of their results.

2. In Section 3, the paper presented an interesting relationship between the pruning ratio and the duration of the grokking period.

3. In Section 5, the paper explored the connection between the test accuracy during training and the change of the masks.

### Weaknesses
1. The paper does not have a clear and unified argument. It seems that, instead of using the LTH as a tool to understand the grokking behavior of neural network training, the paper focus more on the grokking behavior of the pruned subnetworks. From this perspective, though they consist of interesting findings, the results of the paper lacks practical implications: we are not sure how the grokking behavior of the subnetworks is going to shed light on the grokking behavior of neural network in general from an "inner structure" perspective.

2. The paper does not decouple the behavior of "shorter grokking period" from the "easier training" property of the winning tickets. It was observed in the line of the LTH works that subnetworks that are winning tickets are easier to train, which include the behavior of achieving a better generalization result from a smaller number of epochs. It is not sure what is the de-facto distinction between this "easy-to-training" behavior and the result in this paper.

3. Some experimental design in Section 4 is weird. In particular, in Section 4.1 when constructing the neural network with the same weight norm as the pruned network, the paper directly shrinks each weight by a factor. There is no evidence that this method of reducing the weight norm will preserve the network performance or lead to better generalization performance, as is the case in the weight-decay training. Therefore, the paper could be comparing the lottery tickets with some arbitrarily bad neural network. Moreover, in Section 4.2, the paper compared the lottery tickets with PAI method, but it is known that PAI method usually sacrifices performance for better computation efficiency. Based on these experimental design, what Section 4 is doing is simply comparing lottery tickets with not-as-good neural network that has the same weight norms or sparsity, which makes the argument that the paper is trying to make trivial.

4. In Section 5.3, the paper tries to argue that the subnetworks has shorter grokking period because they learn better representations. Given that grokking is determined by generalization performance, it seems that, for the specific task design, the only way for the neural network to achieve good generalization is to learn the good representation (in other words, no benign overfitting is possible). This may not be the case for more complicated tasks.

### Questions
Which figure is line 486 trying to refer to? Right now it seems that there is a missing reference.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper found that given an appropriate lottery ticket of a specific task, the model generalizes much faster than the base model. They also found that the structure of the subnetwork changes rapidly during phase transition and pruning during training can accelerate generalization.

### Strengths
- The paper is well-written and easy to follow. It studies the hidden mechanism of grokking, which is an important question. 

- The idea that a small proportion of generalized network is sufficiently for neural networks to generalize much faster and accelerate grokking is interesting.

### Weaknesses
 - The hyperparameters (e.g. learning rate and weight decay) are not tuned. For example, I think for the modular addition task, the base model can generalize much faster than 25k steps given proper learning rate and weight decay. It is thus not fair to say the lottery ticket can accelerate 65 times in modular addition. Also the results in Table 1 would be more convincing if the hyperparameters are tuned.

- Why the network structure can be measured by Jaccard distance? It seems intuitive that when the model undergoes a phase transition (from memorization to generalization), its weight norm will change rapidly, causing the Jaccard distance to also increase rapidly.

### Questions
- Why the Jaccard distance can be used as a progress measure? The dynamics of Jaccard distance and that of test accuracy change show similar trend.

- Is it possible to obtain a good lottery ticket during memorization phase? It would be great if a mask can be found before the phase transition, so that it can be applied to the model and accelerates grokking.

### Soundness
2

### Presentation
3

### Contribution
2
