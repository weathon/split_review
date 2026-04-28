# Emergent properties with repeated examples

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
{We study the performance of transformers as a function of the number of repetitions of training examples with algorithmically generated datasets. On three problems of mathematics: the greatest common divisor, modular multiplication, and matrix eigenvalues, we show that for a fixed number of training steps,
models trained on smaller sets of repeated examples outperform models trained on larger sets of single-use examples. We also demonstrate that {\em two-set training} - repeated use of a small random subset of examples, along normal sampling on the rest of the training set - provides for faster learning and better performance.
This highlights that the benefits of repetition can outweigh those of data diversity. 
These datasets and problems provide a controlled setting to shed light on the still poorly understood interplay between generalization and memorization in deep learning. }

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper empirically shows that the repetition of training data can be beneficial in certain setups. The authors conduct experiments on three algorithmically generated datasets, and show that model trained with small data budgets outperforms model trained on larger data budgets. The authors also identify a two-phase training algorithm that gives faster training and better performance.

### Strengths
1. The experiments are conducted on three algorithmically generated datasets of math tasks, which is an ideal setup of controlled experiments. The experiment setups are clearly described, and the results are well presented and explained. 

2. The empirical findings of the beneficial of repeated examples have decent practical meanings. The success of two set training is interesting and novel to me.

### Weaknesses
1. My major concern is that the experiments are only conducted on algorithmically generated synthetic data, instead of real world datasets. This makes me not fully convinced that the experimental findings are universal and can be transferred to more realistic setups. 
Specifically, I am wondering whether the main findings, especially the success of two set training, also applies to real language datasets. Do you have empirical results to support that? Besides, the three dataset are all math problems. Do you think that this specific type of training data might have a positive influence on the performance of repeated data? 

2. Does the emergent property in the title mean that the observed phenomena only happens for training at scale? Do you have found any criteria that can indicate under what circumstance can repeated data or two-set training be beneficial?

### Questions
See weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The present paper deals with the essential question of the role of repetition in the training data of machine learning models. More specifically, the work delves into the effect of introducing repeated examples when training transformers on three mathematical problems: finding the greatest common divisor between two numbers, performing modular multiplication, and computing the eigenvalues of (small) matrices. Through extensive numerical experiments, the authors show that repetition during training is very valuable for transformers to perform well on these tasks, and that might be necessary for learning to emerge in the case of modular multiplication. In light of these results, they propose a two-set training procedure, in which training examples may be drawn from either a large set of examples that will be seen only a handful of times or from a much smaller set of examples repeated many times during training. Consistent with their initial experiments, they find that this procedure improves the performance of trained networks for given data budgets, and in some cases enables learning. The authors finally consider variations of this procedure, notably the natural idea of curating the repeated set to further improve performance. Surprisingly, they find that curating does not provide further gains, or may be detrimental.

### Strengths
Overall, this paper explores an important aspect of machine learning—understanding why algorithms are usually expected to suffer from repetitions whereas human and animal learning appear to be highly dependent on them for learning—and could therefore be a significant contribution to this puzzle as it provides counter-examples that deserve to be better understood. By relying on the transformer architecture, which has become ubiquitous in many practical implementations, the authors also maximize the chance that their findings, and the training protocol they propose, may be taken advantage of in practical settings. The study of mathematical tasks provides a well-controlled environment where memorization can be identified, while properly learning an algorithm is necessary to achieve good generalization. The paper is well-written, and the author’s conclusions are clearly stated.

### Weaknesses
I believe the main limitation of this work lies in the limited number of tasks it considers, undermining the generality of its conclusions. In particular, the authors repeatedly make statements such as ‘models trained on smaller sets of repeated examples outperform models trained on larger sets of single-use examples’ (abstract); ‘smaller data budgets and more frequent repetition allow for faster learning, but also for much better performance’ (p. 5); ‘learning emerges through repetition’ (p. 5) etc. Based on the presented results however, it appears that these claims should be slightly tempered: there is a tradeoff between the repetition and the diversity that is necessary to avoid overfitting, as clearly illustrated in Fig. 2. While the authors show that repetitions at a given data budget may be beneficial, this relation is strongly non-monotonous, and in the greatest common divisor task one notably still requires a large number of unique samples to perform correctly (and as apparent in Fig. 4 the balance between repetition and diversity is hard to strike in this problem!). Clarifying this point and emphasizing that it is a tradeoff would make the paper more convincing, and would add to the relevance of the two-set procedure which precisely tries to provide the ideal tradeoff. 

It also remains unclear whether the two-set procedure is relevant in settings where the transformer must not necessarily learn a clear-cut algorithm. For instance, could such a procedure be effective in image classification and more generally vision-related tasks? It seems plausible that the need for repetition is related to the hardness of the task at hand, which is not discussed in the paper. In that respect, the difference in hardness of the three tasks exposed is not straightforward to understand: the authors notably state that the computation of eigenvalues is the hardest task they consider, yet the smallest model (in number of parameters) is used to tackle it. Therefore, it is not evident how the eigenvalue problem contributes to the clarity of the paper and its conclusion, also considering the relatively poor results that the authors find (4/30 as the maximum trained model success rate if I understand correctly) and the lack of clear plots dedicated to this third problem, despite it being expected to be the most difficult to tackle.

From a more technical standpoint, the accuracy metric chosen by the authors is not easy to interpret, notably in Fig. 2. While Appendix A provides some explanation as to how the chosen accuracy may stay fixed while the test loss explodes, the fact that it is on the eigenvalue computation and not the GCD problem for clear interpretation of Fig. 2 makes it still unsatisfactory. Besides, Fig. 6 does show some examples where the accuracy decreases as the model overfits.

Finally, the conclusion of the authors that the transformers should somehow be able to distinguish between already seen and unseen examples is puzzling. Could the role of repetition not be simply explained by the fact that there needs to be some form of symmetry breaking in the direction of the loss to follow and that repeating examples allows for a clear direction in the loss landscape to emerge? In that respect, I point the authors towards the papers: 
Dandi, Y., Troiani, E., Arnaboldi, L., Pesce, L., Zdeborová, L., & Krzakala, F. (2024). The benefits of reusing batches for gradient descent in two-layer networks: Breaking the curse of information and leap exponents. arXiv preprint arXiv:2402.03220. 
Arnaboldi, L., Dandi, Y., Krzakala, F., Pesce, L., & Stephan, L. (2024). Repetita iuvant: Data repetition allows sgd to learn high-dimensional multi-index functions. arXiv preprint arXiv:2405.15459

### Questions
List of questions (including some repetitions of the above):
- Do the authors believe that their findings hold in tasks that do not require learning an algorithm? For example in vision-related tasks where memorization could be more useful (and sufficient in some cases)?
- Do they know of an example where repetition or the two-step procedure is not beneficial? One could notably think of tasks where curriculum learning is decisively effective, then shouldn’t random repetitions at least fare worse than curated ones? In other words, can the two-step procedure work well when curriculum learning works well?
- Can the two-step procedure be performed by showing only the repeated samples in a first learning phase, and then moving on to the more diverse samples in a second phase? i.e. focus first on discovering some ‘rules’, before generalizing these rules? I believe that finding good results in such a procedure would go in the direction of a loss-landscape-based interpretation of the phenomenon, in the sense of the Dandi et al. paper mentioned above. This would also further clarify the difference between what the authors observe and grokking (in addition to the different timescales and sample sizes they mention in Sec. 2).
- Can the authors clarify how accuracy is never affected by overfitting in the GCD task? How general do they expect this behavior to be?
- Can the authors clarify what they mean by a transformer being able to identify deja vu and jamais vu examples? Why should the architecture ‘care’?

**AFTER DISCUSSION**

The authors have addressed the main concerns I presented and included different explorations that I believe clarify and strengthen their message.  I will raise my score to a 6, for the moment.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work investigates the effect of training with repeated examples (like training over the training data over multiple epochs) compared to training on very large datasets only once. The authors run experiments on three large-scale math problems, to compute GCD, modular multiplication, and computing eigenvalues using varying sizes of transformers and varying data and training budgets. The authors also propose a two-set training method in which they repeat one small subset of data throughout training and otherwise train on new data continually.

### Strengths
The paper is written clearly and is easy to follow and understand. The problem posed is important and if answered can be helpful in guiding training methods, fine-tuning and data gathering for complex problems. The results for the two-set training method bring up interesting questions about the role of memorization that would be interesting for future research.  All experiments are very thorough, showing good evidence for their claims on the datasets chosen.

### Weaknesses
From my point of view, this is not a particularly new idea. Training over many epochs over the training data is standard in most applications. This is perhaps not common in new applications such as in NLP as the authors cite for large language models. Given this, it would have been more interesting to see applications within NLP instead. The problems considered (algebraic problems) are very different, and the connection to other applications like NLP is not well-motivated.

In terms of related work, it may be interesting to investigate the connection to continual learning and catastrophic forgetting. This is more geared towards learning new tasks, and not about revisiting old examples from the same distribution. However, some of the work done here may provide valuable insight and would be nice to have some discussion comparing the methods in this area with yours.

Moreover, your idea of two-set learning sounds similar to spaced repetition in human learning -- being shown old instances right before you are about to forget them. There is not much work in this direction for ML training applications, although I did find this paper [1] which seems to have similar ideas to yours, proposing an order and frequency to the examples being trained on.


[1] Repeat before Forgetting: Spaced Repetition for Efficient and Effective Training of Neural Networks, Hadi Amiri, Timothy A. Miller, Guergana Savova.

### Questions
1. Why did you choose these experiments? I understand it is easier to control the data and the distribution of repeated examples. However, it is hard to see why conclusions drawn on algebraic problems should extend to other more natural data and NLP problems. 

2. Can you try your ideas and run the experiments on non-synthetic datasets? It would be interesting to see if the two-set training works well for other data like CIFAR-10 or other natural datasets that you may find more appropriate.

3. Can you provide some discussion on continual learning etc. as I mentioned in the above section?

4. In Figure 5, the results are quite unstable as a function of your parameters, you need to be very careful in choosing the repeated set size etc. In practice, iterating over the possible set sizes and repeated set probability and training given each choice is very expensive. Do you have any intuition for how to choose these hyper-parameters in general? There does seem to be a general common "shape" where training works better.

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
Modern language models are typically trained with only one or at most a few epochs. This paper studies the potential benefit of training for more than a few epochs. With experiments on three synthetic problems (GCD, modular multiplication and matrix eigenvalues), the paper shows that for certain compute budget (or "training budget" as termed in the paper), repeating the same data many times can actually be better than using completely fresh data (i.e. 1 epoch or "online" training). Based on this intuition, this paper further proposed a "two-set training" paradigm where only a subset of training examples is repeated, to get the benefit of repeated training while also mitigating the potential overfitting issue.

### Strengths
The paper presented the idea clearly and conducted controlled experiments to study the question. It also proposed new training paradigms based on the observations that could potentially help improving model training.

### Weaknesses
1. This paper is making very big claims (e.g. of "emergent properties" or "emergent learning") based on very synthetic settings. While the models used are transformer models, they are tasked with specialized tokenizers for numbers and trained to perform a single synthetic task (e.g. given two numbers, output the greatest common divisor of the two numbers). In other words, those "language models" do not have any language capabilities. I think the paper could be better either (A) frame this as a general machine learning problem and have comparison studies covering many different neural network architectures, or (B) focus on LM but have additional experiments on more realistic settings. For example, in terms of relevancy to LMs, I think a study of fine-tuning with a proper LM would be more "transferable" to our understanding of how LM learning works than this synthetic pre-training setting.

2. There was the classical decomposition of test accuracy to training accuracy + generalization gap. It seems especially relevant when the paper talks about training with or without repetitions on difficult math / arithmetic tasks. Many of the observations might be more intuitively explained by undertraining --- i.e. the training accuracy itself is already quite bad as the model struggle to fit the problem (with small data repetitions). Adding studies from this angle could potentially make the paper more clear, but in the meantime, the observations would be less surprising if it is mostly explained by such classical decomposition.

3. The paper proposed two-set training algorithm, but there is no comparison to any previous curriculum learning baseline algorithms.

4. It is not clear if the experiments are comprehensive enough to support some of the big claims. For example, the paper talks about "emergence", *a task inaccessible to models trained with large or unlimited DB is learned with small DB*. The conclusion may change depending on the model architecture or even model sizes, and if may even be unclear if each setting allows to choose their own optimal hyperparameters. This paper is making those conclusions based on experiments with a single transformer model with fixed number of parameters and a fixed set of hyperparameters. For example, with repeated examples, later training steps would have potentially smaller updates because the gradients are smaller on seen examples. If this is benefiting the learning, could a similar effects be achieved by a better learning rate decaying scheme?

### Questions
Please see the "Weakness" section above.

---

**Post Rebuttal**: Thanks the authors for the response. I raised my rating, but I'm still not super convinced about the setting as well as concrete evidences in the experiments of this paper excluding the undertraining as a potential confounding factor.

### Soundness
2

### Presentation
3

### Contribution
1
