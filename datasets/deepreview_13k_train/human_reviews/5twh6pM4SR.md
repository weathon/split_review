# Automating Continual Learning

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
General-purpose learning systems should improve themselves in open-ended fashion in ever-changing environments. Conventional learning algorithms for neural networks, however, suffer from catastrophic forgetting (CF)---previously acquired skills are forgotten when a new task is learned. Instead of hand-crafting new algorithms for avoiding CF, we propose Automated Continual Learning (ACL) to train self-referential neural networks to meta-learn their own in-context continual \mbox{(meta-)learning} algorithms. ACL encodes all desiderata---good performance on both old and new tasks---into its meta-learning objectives.
Our experiments demonstrate that
ACL effectively solves ``in-context catastrophic forgetting''; our ACL-learned algorithms outperform hand-crafted ones, e.g., on the Split-MNIST benchmark in the replay-free setting, 
and enables continual learning of diverse tasks consisting of multiple few-shot and standard image classification datasets

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a continual learning method based on self-referential weight matrices. By posing the continual learning problem as a meta-learning task, it is possible to formulate the standard continual learning desiderata (low forgetting, high forward and backward transfers) simply as terms of the meta-learning objective. Authors show that their approach is promising through experiments on MNIST, Omniglot, and Mini-ImageNet.

### Strengths
Originality is the main strength of the proposed approach. To my knowledge, the application of SRWM to continual learning is a novel idea. Automating the discovery of continual learning algorithms by including the desired requirements as loss terms of the meta-learner is an exciting approach and it would be great to explore it in a bit more details. The paper is well written and properly structured. The figures are of high quality and help in quickly grasping the main ideas.

### Weaknesses
The main weakness of the paper is the experimental evaluation. Despite presenting their approach as a continual learning method, the authors don't use any of the standard benchmarks (e.g. Split MNIST, Split Mini-ImageNet), nor do they compare to any previous work (regularization, replay, or parameter isolation methods). The meta-learning formulation is also a major limitation, as the number of loss terms grows rapidly with the number of tasks and it is not clear whether the method is practical for e.g. 10 tasks (which is still a small number compared to the requirements of real-world lifelong learning). It would also be great to include a figure that illustrates the architecture of your model in more detail.

### Questions
How do the data requirements of your method grow with the number of tasks?

How is the training sequence constructed? Do you use a single sequence? If not, doesn't it mean you're effectively performing joint training?

Could you elaborate what do you mean by "certain real-world data may naturally give rise to an ACL-like objective"?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new way to think about, and potentially solve, the continual learning problem (in particular, the supervised task incremental learning variation of CL). 
This new approach views CL as a sequence learning problem. Each sub-sequence consists of input/target examples corresponding to one task to be learned. These sub-sequences can then form longer sequences, for multiple tasks, by concatenating multiple sub-sequences.
Once formulated as such a sequence-learning task, a gradient descent search for CL learning algorithms can look for the desired CL behavior by constructing loss functions that avoid catastrophic forgetting and aim to achieve goals such as forward transfer.

### Strengths
On the positive side, the approach of viewing the CL problem in the context of sequence learning seems interesting -- and it gives a fresh perspective to an area (CL) that is becoming increasingly incremental.

### Weaknesses
I have some major concerns about whether this method is actually doing CL (versus multitask learning).

Another major concern is whether ACL can be used in a practical context in which many tasks will be learned over time (as opposed to just a handful).

Please see comments below.

On Page 6, the paper states: “Unless otherwise indicated, we concatenate 15 examples for each class for each task in the context during both training and evaluation (resulting in sequences of length 75 for each task).” 
Having a temporally structured input during evaluation is not a valid approach in the context of CL. Such temporally structured inputs makes discrimination between classes of different tasks trivial. For example, if you give someone 75 Omniglot examples and 75 Imagenet examples and ask them to classify an input x during testing, I can easily determine whether x is from Omniglot or Imagenet without learning (just by computing some statistics of pixel values). Letters would, of course, look different than natural images. Then, predictions become much easier.

On Page 6, the paper states: “The order of appearance of two tasks within training sequences is alternated for every batch.” This sounds like both datasets are available at the same time. If that is true, what the paper is actually doing multitask learning, not CL.

Looking at the loss function (Equation 4), the first term requires access to old model weights W_A (linear growth in memory requirement as they see more tasks), the second term is okay in terms of CL, but the third term requires access to a previous test dataset, which violates CL. It may be that these are some form of “replay” examples, but the paper does not mention that.

I see that the method is significantly different from other continual learning methods, still I would expect the authors to benchmark against some existing methods. After all, the claim is that instead of hand-crafting CL algorithms, we can learn how to sequentially learn. Does ACL perform better than handcrafted tricks? The method is computation intensive, and it does not seem easily scalable to more tasks. So, I would at least want to see the paper outperform some existing methods in the two-task scenario to argue that learning how to continual learn is a promising direction to pursue.

If you examine Equation 5 on the last page, you'll notice that in order to learn a third task, they need to add three terms to the loss function. In continual learning, a five-task setting is considered small. To learn SplitMNIST, for example, they would actually need 1 + 2 + 3 + 4 + 5 (15) terms in the loss function. As a result, their method becomes quadratically more expensive in terms of computation (i.e., for Task n, you require backpropagation through (n)(n-1)/2 terms). This is clearly not practical.

### Questions
On Page 6, the paper states: “Unless otherwise indicated, we concatenate 15 examples for each class for each task in the context during both training and evaluation (resulting in sequences of length 75 for each task).” 
Having a temporally structured input during evaluation is not a valid approach in the context of CL (although I am aware that some meta-learning papers unfortunately do that -- but that does not mean that their approach can be accepted without question because it has been previously published). Such temporally structured inputs makes discrimination between classes of different tasks trivial. For example, if you give someone 75 Omniglot examples and 75 Imagenet examples and ask them to classify an input x during testing, I can easily determine whether x is from Omniglot or Imagenet without learning (just by computing some statistics of pixel values). Letters would, of course, look different than natural images. Then, predictions become much easier.

On Page 6, the paper states: “The order of appearance of two tasks within training sequences is alternated for every batch.” This sounds like both datasets are available at the same time. If that is true, what the paper is actually doing multitask learning, not CL.

Looking at the loss function (Equation 4), the first term requires access to old model weights W_A (linear growth in memory requirement as they see more tasks), the second term is okay in terms of CL, but the third term requires access to a previous test dataset, which violates CL. It may be that these are some form of “replay” examples, but the paper does not mention that.

I see that the method is significantly different from other continual learning methods, still I would expect the authors to benchmark against some existing methods. After all, the claim is that instead of hand-crafting CL algorithms, we can learn how to sequentially learn. Does ACL perform better than handcrafted tricks? The method is computation intensive, and it does not seem easily scalable to more tasks. So, I would at least want to see the paper outperform some existing methods in the two-task scenario to argue that learning how to continual learn is a promising direction to pursue.

If you examine Equation 5 on the last page, you'll notice that in order to learn a third task, they need to add three terms to the loss function. In continual learning, a five-task setting is considered small. To learn SplitMNIST, for example, they would actually need 1 + 2 + 3 + 4 + 5 (15) terms in the loss function. As a result, their method becomes quadratically more expensive in terms of computation (i.e., for Task n, you require backpropagation through (n)(n-1)/2 terms). This is clearly not practical.

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes to formulate continual learning as a sequence learning problem and applies self-referential weight matrices (SRWM), which can be considered a sequence model, as the key mechanism for continual learning.
SRWM is a linear layer that produces self-modification as an auxiliary output.

### Strengths
I agree with the general direction of this paper that formulates continual learning as a sequence learning problem.
This idea of formulating a learning process as sequence learning has been used in the meta-learning literature, especially for few-shot settings, but has not been utilized in the continual learning domain.
I believe this direction requires further investigation.

### Weaknesses
### Missing Related Works in Meta-Continual Learning

According to my understanding, this work should be classified as a meta-continual learning (MCL) approach, which is also referred to as *learning to continually learn*. 
It is a direct extension of meta-learning that replaces each learning episode with a continual learning episode, which also aligns with the authors' description in section 2.2.
There are several important prior works in this domain [1, 2, 3] that were not mentioned in the paper. These works explore various meta-learning techniques for continual learning, such as learning initializations or optimization algorithms, and should be compared as baselines. Specifically, the paper lacks a comparison to methods that learn to optimize learning algorithms for CL, which is a crucial aspect of MCL.

### Confusing Description About the Experimental Settings

Since MCL is a branch of meta-learning that aims to optimize a learning algorithm, it is crucial to separate meta-training and meta-test sets. Also, there should be no overlap in the constituent tasks between them. Otherwise, the model can achieve a high score simply by memorizing the tasks in the meta-training set without learning new knowledge during the meta-test phase. The paper does not clearly describe how meta-training and meta-test sets are constructed, making it difficult to assess the validity of the experimental results. The use of standard meta-learning splits for Omniglot and Mini-ImageNet should be explicitly stated, and the terminology should be consistent with the existing meta-learning or MCL literature. Furthermore, the paper should clarify whether the meta-test set contains tasks from the same distribution as the meta-training set or from a different distribution, as this significantly impacts the interpretation of the results.

### Weak Experimental Results

The proposed method is tested only on two-task and three-task CL scenarios, which is an unreasonably tiny scale compared to previous works on MCL [1, 2, 3]. These prior works often evaluate on dozens or even hundreds of tasks, providing a much more comprehensive assessment of the method's capabilities. Such a small number of tasks does not provide sufficient evidence that the proposed method can handle the complexities of continual learning. The lack of experiments on more challenging and diverse task sequences makes it difficult to assess the practical applicability of the proposed approach.

### Reproducibility

It seems hard to reproduce the experimental results solely from the provided text. To verify and reproduce experimental results, I believe that including code with the submission should be the standard practice. The absence of code makes it difficult to verify the implementation details and reproduce the reported results, which is essential for the scientific community to build upon this work.

### Questions
- Experiments with much longer training sequences, as in [1, 2, 3], seem necessary.
- Since each convolution filter is just a linear layer applied to a local patch, shouldn't it be possible to construct a CNN version of ACL?
- I have doubts about the representational capability of SRWM since the complex learning dynamics in non-stationary streams depend solely on the initial parameters. Is it really sufficient to manipulate the initial parameters? Can SRWM really handle long sequences?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
