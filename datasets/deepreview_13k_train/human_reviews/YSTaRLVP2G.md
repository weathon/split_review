# The Power of Linear Combinations: Learning with Random Convolutions

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Following the traditional paradigm of convolutional neural networks (CNNs), modern CNNs manage to keep pace with more recent, for example transformer-based, models by not only increasing model depth and width but also the kernel size. This results in large amounts of learnable model parameters that need to be handled during training. While following the convolutional paradigm with the according spatial inductive bias, we question the significance of \emph{learned} convolution filters. In fact, our findings demonstrate that many contemporary CNN architectures can achieve high test accuracies without ever updating randomly initialized (spatial) convolution filters. Instead, simple linear combinations (implemented through efficient $1\times 1$ convolutions) suffice to effectively recombine even random filters into expressive network operators. Furthermore, these combinations of random filters can implicitly regularize the resulting operations, mitigating overfitting and enhancing overall performance and robustness. Conversely, retaining the ability to learn filter updates can impair network performance. Lastly, although we only observe relatively small gains from learning $3\times 3$ convolutions, the learning gains increase proportionally with kernel size, owing to the non-idealities of the independent and identically distributed (\textit{i.i.d.}) nature of default initialization techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the power of using random convolutions in different neural architectures. The authors find that linear combinations suffice to effectively recombine random conv filters into expressive network operations (by means of 1x1 convs). The authors also emphasize on the fact that the difference between learnable and random kernels becomes larger as the size of the kernels is increased.

### Strengths
The presentation of the paper is very good. All the findings are provided in a digestible and organized way, making the paper an interesting, intriguing and enjoyable read. The study is carried out in a systematic way, shedding light into the modus operandi of CNNs. 

Altogether I believe this is a very strong submission with a little flaw in its evaluation.

### Weaknesses
The only weakness I see is that the experiments in Section 5.2 are not conclusive. Specifically, the results on ImageNet, where the authors state "we were not able to outperform the baseline, but we attribute this to the granularity of the tested expansion rates and the fluctuations in the measurements of a single run", are not sufficiently convincing. This leaves the reader with the impression that the method's effectiveness on larger, more complex datasets is not fully established, weakening the overall analysis of the paper –which is very strong up to this point.

### Questions
Do you have any insights wrt modus operandi of long convolutional models and how it differs from that of conventional (small kernel) architectures?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to investigate the impact of learned spatial filters v.s. random spatial filters in a deep Convolutional Neural Network (CNN) that uses 1x1 filters, the hypothesis being that the linear combinations (of the spatial filters) learned by 1x1 filters, are powerful enough themselves with random spatial filters alone to learn visual representations and attain good generalization on tasks such as image classification. The authors empirically investigate this hypothesis using existing CNN architectures with appropriate 1x1 filters, and furthermore by adding 1x1 filters to ensure that spatial filters are followed by a linear combination, to create "LC" blocks. The authors demonstrate that by drastically increasing the width of these LC blocks (i.e. both the spatial filters and 1x1), using only uniform randomly sampled spatial filters with learned 1x1 linear combinations, CNNs can match the generalization performance of using learned spatial filters on ResNet-based models with ImageNet, CIFAR-100, CIRAR-10, SVHN and Fashion-MNIST. The authors do also show however, a degradation in robustness performance when not using learned spatial filters that warrants further study.

### Strengths
* The paper is well-written overall, with a good background on both the recent developments in convolutional kernel sizes, and usage of 1x1 convolutions.
* The experimental setup is overall quite good overall (with some exceptions listed below), with the appropriate models and datasets used to demonstrate convincing empirical evidence on the author's hypothesis.
* The robustness results in the paper are perhaps the most novel/insightful part of the paper, and would benefit from more analysis/further study.

### Weaknesses
 * The hypothesis and results are not surprising at all given how many linear combinations the authors learn in replacement of learned spatial filters. We already know that we can learn to reconstruct anything in a space by learning a linear combination of orthogonal basis vectors. While the basis vectors in this case are not designed to be orthogonal, they are sampled randomly sampled from a high-dimensional space (e.g. the kernel space of e.g. 3x3xC, where C is often very large). Randomly sampled vectors in high dimensional spaces are extremely likely to be orthogonal. Furthermore, we don't need to reconstruct perfectly any possible vector in filter space – the filters learned by CNNs likely represent a low-dimensional manifold within filter space, and approximating these filters rather than exact reconstruction is sufficient. The authors do not provide any analysis to demonstrate that the random spatial filters are not approximately orthogonal, and therefore this hypothesis is not sufficiently motivated.
* Given the fact the hypothesis/results should not be surprising, this paper cannot just be considered an analysis paper pointing out a novel/surprising result to the research community, which is in itself a perfectly valid thing to do. The paper should be motivated outside of the fact that they hypothesis is true - i.e. is it useful to train a CNN in this manner over learning spatial filters? It's obvious that, as explained by the authors in the paper, using frozen LC models that match learned LC generalization performance are much more expensive in terms of compute and perhaps more importantly working memory (i.e. GPU VRAM), so this appears to not be the case at all. The authors do not provide any analysis of the compute and memory requirements of the proposed approach, and therefore do not sufficiently motivate the utility of the proposed approach.
* Many of the empirical results compare models with drastically different numbers of trainable parameters, while using the same training hyperparameters. However, we know that models with different numbers of trainable parameters usually need different hyperparameters and training setups. For example, models with more trainable parameters typically need longer to converge and require different learning rates, etc. Given this, it's not completely convincing that the model's generalization being compared between frozen lc and learned lc is fair. The authors do not provide any evidence that the training hyperparameters used are appropriate for the different models being compared, and therefore the results are not sufficiently convincing.
* No explicit comparison of the compute and VRAM requirements for training models that are compared, in many cases there is quite a drastic difference it would seem. This is especially stark in section 5.1 where models with exponential increasing compute/param are compared with a fixed baseline model, i.e. ResNet-20-16. The lack of compute and VRAM analysis makes it difficult to assess the practical implications of the proposed method.
* While I like the robustness analysis and think it warrants further attention, this is yet another reason why even when frozen LC models match generalization, they are poorly motivated.

### Questions
* If you believe this is not explained simply as learning from an orthogonal basis, as explained above, how many of the randomly sampled spatial filters are not orthogonal? You could perform an analysis to understand the representational ability of the random basis used.
* If you do believe this explanation, what does your paper contribute that is not simply empirical validation of this understanding? i.e. things that are specific to the DNN context, and other findings that are not trivially a result of being able to learn from an orthogonal basis.
* Why is it useful to train a frozen LC model v.s. a learned spatial model that achieve the same generalization? What is the tradeoff in compute and working memory (i.e. GPU VRAM) utilization for achieving this with frozen LC models v.s. a baseline learned spatial model for the same generalization performance? 
* Did you do any hyperparameter turning for frozen LC v.s. learnable LC models you compared to ensure using the same hyperparameters/training setup is appropriate?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigate whether it is necessary to learn spatial convolutional filter weights in CNNs at all, to achieve good performance on data-specific tasks. Their approach is to fix the spatial convolutional kernel at initialization, only allowing learning linear combinations of these random spatial kernels during training. Authors argue that this approach has a regularising effect, as it prevents overfitting of the spatial kernels to specific spatial patterns occurring in the training data, also showing that learnable spatial convolutions in combination with a high rate of linear combinations actually decreases validation accuracy. Authors show that the benefits of learning linear combinations of random spatial kernels are mostly present at small kernel sizes, as for larger kernel sizes performance of the standard learnable spatial kernel and random spatial kernel starts to diverge. Authors conclude by giving a number of possible research extensions of their work, e.g. modifying the standard random i.i.d. initialization to reflect spatial distributions found in trained spatial kernels could be a very interesting next step.

### Strengths
Authors are very thorough in positioning their work and contrasting it with previous methods. I appreciate the thorough literature review, as it contributes to a clear context for the current work. The main research question that the authors investigate; the possibility of training a CNN without modifying the original spatial convolution weights, is well addressed theoretically and empirically, at least in the setting of image classification. The authors perform a number of relevant ablations over the hyperparameters of their method (i.e. kernel size, expansion rate) and provide extensive analysis of their results. Furthermore, where the method underperforms (larger kernel sizes), the authors give a qualitative analysis through visualisation of the distribution of learned kernels and provide pointers for possible ways of addressing this problem.

### Weaknesses
 - My main objection with respect to this manuscript is the clarity of practical impact of this approach. It seems like in most settings, the proposed approach slightly underperforms traditional CNN architectures. For larger expansion rates, the model may outperform the baseline, but to me the trade-off in computational complexity is unclear. Although the author’s findings are interesting in their own right - it is certainly somewhat suprising that a factorization this drastic is still able to perform this impressively - I think the manuscript would greatly benefit from more clear indication of where potential benefits of frozen spatial convolution weights may lie, as the current version of the manuscript doesn’t sufficiently address this in my opinion.
- Second, the theoretical analysis of their approach seems somewhat limited. Although the authors list as one of their contributions the theoretical explanation for the impressive performance of their factorization, I'm not sure where in the paper this happens. On the one hand the authors say a large enough basis of random spatial filters provides enough expressivity to represent any other fully learnable spatial kernel (lemma 4.1), on the other hand they indicate that their approach has a clear regularizing effect, improving robustness. Are these not two contrasting observations?
- Third, the experiments conducted by the authors in the main body of the paper are quite limited in scope, in that they are all classification problems. Given that the authors themselves indicate that linear combinations of random weights have a hard time forming sharp spatial patterns, I think more attention should also be given to e.g. fine-grained segmentation (I’ve seen the results in the appendix but the authors might consider moving them to the main body and providing a more detailed experimental setup).

### Questions
- For the experiments in 5.1, how do the modified models and their baseline counterparts compare in terms of computational requirements? I.e. as you increase the expansion factor it increases computational complexity right? How do the different expansion factors and the original model compare, for example in terms of flops?
- In 5.3 the role of kernel size, you indicate that you investigate the spatial distribution for kernels for different kernel sizes. I assume the visualisations of the kernels shown for the frozen model are obtained after training? You indicate that there is a very clear spatial pattern in trained non-frozen kernels that isn’t present in the frozen model, and you indicate this as the main reason for trailing performance. This seems like a reasonable hypothesis (although somewhat in contrast to Fig 2), but would this mean your model is unable to perform more fine-grained tasks such as segmentation? Why not?
- Could you clarify what you see as the main practical impact of this approach? (see above)
- Could you clarify what you list as theoretical analysis for the performance of your approach? (see above)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper questions the significance of learned convolution filters, while following the convolutional paradigm with according spatial inductive bias. Contemporary CNN architectures can achieve high test accuracies without updating the randomly initialized filters. It further shows that romdom filters mitigates overfitting and enhances overall performance and robustness. Learning gains increase proportionally with kernel size.

### Strengths
- CNNs can be trained to high validation accuracies on computer vision tasks without ever updating weights of randomly intialized spatial convolutions.
- training with random filters can outperform the accuracy and robustness of fully learnable convolutions due to implicit regularization in the weight space. 
- The paper is well written.

### Weaknesses
 - The idea is trivial and well-known.
- the experiments are done on toy models and datasets, which are not convincing.

### Questions
- Experiments on state-of-the-art models

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
