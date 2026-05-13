# General-Purpose In-Context Learning by Meta-Learning Transformers

- Decision: Reject
- Scores: 6, 1, 5, 3

## Abstract
Modern machine learning requires system designers to specify aspects of the learning pipeline, such as losses, architectures, and optimizers.
Meta-learning, or learning-to-learn, instead aims to \emph{learn} those aspects, and promises to unlock greater capabilities with less manual effort.
One particularly ambitious goal of meta-learning is to train general-purpose in-context learning algorithms from scratch, using only black-box models with \emph{minimal inductive bias}.
Such a model takes in training data, and produces test-set predictions across a wide range of problems, without any explicit definition of an inference model, training loss, or optimization algorithm.
In this paper we show that Transformers and other black-box models can be meta-trained to act as general-purpose in-context learners.
We characterize transitions between algorithms that generalize, algorithms that memorize, and algorithms that fail to meta-train at all, induced by changes in model size, number of tasks, and meta-optimization.
We further show that the capabilities of meta-trained algorithms are bottlenecked by the accessible state size (memory) determining the next prediction, unlike standard models which are thought to be bottlenecked by parameter count.
Finally, we propose practical interventions such as biasing the training distribution that improve the meta-training and meta-generalization of general-purpose in-context learning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper demonstrated that transformers can be meta-trained to act as general-purpose in-context learners. This paper also characterizes transitions between algorithms that generalize, algorithms that memorize, and algorithms that fail to meta-train at all, induced by changes in model size, number of tasks, and meta-optimization. This paper proposes practical interventions such as biasing the training distribution to improve the meta-training.

### Strengths
1. This paper performed experiments on image classification datasets to demonstrate that transformers can be meta-trained to perform in-context learning. 
2. Figure 2 gives convincing evidence of a transition from memorization and generalization induced by model capacity and sample size. 
3. This paper provides practical interventions to improve meta-training.

### Weaknesses
1. The writing is not completely clear. For example, "general-purpose in-context learning" is a vague term without a rigorous mathematical definition. This makes the paper a bit hard to read. 
2. The memory or state in Section 4.2 is quite heuristic without a concrete math definition. Beyond LSTM and transformers, it is not clear how the state is defined. The insight that "Large state is more crucial than parameter count" is thus not fully grounded.

### Questions
Could the authors address the comments on the weakness?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This submission is a resubmission from another machine learning venue, and the paper has undergone 0 modifications since its previous rejection. While it is permissible to resubmit the work, in this case, the authors have not addressed the points raised in the earlier review process. I believe these points are crucial for the paper's improvement, and it would be counterproductive to overlook the feedback provided in the previous reviews.

If the Area Chair still deems it appropriate to consider this submission, I recommend using all reviews so far.

### Strengths
N/A

### Weaknesses
This submission is a resubmission from another machine learning venue, and the paper has undergone 0 modifications since its previous rejection. While it is permissible to resubmit the work, in this case, the authors have not addressed the points raised in the earlier review process. I believe these points are crucial for the paper's improvement, and it would be counterproductive to overlook the feedback provided in the previous reviews. The lack of revisions suggests a disregard for the peer-review process and raises concerns about the authors' commitment to improving their work. The paper, in its current state, does not meet the standards of this venue.

### Questions
N/A

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates how transformer-based models can meta-learn general-purpose in-context learning algorithms (that take in training data and produce test-set predictions without any explicit definition of an inference model, training loss, or optimization algorithm) with minimal inductive bias. The authors propose using black-box sequence models like LSTMs and Transformers as meta-learners, since they can learn concepts from demonstrations without an explicit definition of the learning algorithm. 

Authors go to great lengths to introduce and classify different in-context learning algorithms and introduce a Transformer-based model (GPICL) and associated meta-training task distribution. They discuss how they generate different tasks for the meta algorithm to learn by taking existing supervised datasets and randomly projecting the inputs and permuting classes to generate many datasets from a small seed. Based on that they define the General-Purpose In-Context Learner (GPICL) - a transformer model that is fed sequences of input-output data and asked to predict next output based on previous input. During training of GPICL, each iteration uses Adam to optimize the loss on a random batch of training data sampled from a random task. 
Authors run many ablation studies analysing meta-learning with transformers. Among others, they show results that indicate the transformer starts to learn rather than memorize with enough memory used for training, and that simple data augmentations during meta-training lead to the emergence of learning-to-learn behaviors.

### Strengths
- Presents a simple baseline model (GPICL) for meta-learning general purpose learners with minimal inductive bias. Shows competitive performance compared to models with stronger inductive biases.

- Provides interesting insights into the transitions from memorization to task identification to general learning as model size and number of tasks increase during meta-training. Identifies the accessible state/memory size as a key bottleneck for meta-learning capabilities, rather than just model parameter count.
- Identifies the accessible state/memory size as a key bottleneck for meta-learning capabilities, rather than just model parameter count.
- Well-written and easy to follow presentation of methods and results.

### Weaknesses
 - Authors use CIFAR10, MNIST, FashionMNIST and SVHN as their datasets. Those are rather simple datasets and it would be good to see if the findings generalizes well to harder and larger datasets. Most importantly it would be interesting to show that the method is performing well due to its inherent ability to learn rather than the datasets being easy.
- The authors do not make it explicitly clear what elements of their new setup is their contribution and which is already present in other papers. I understand the random projection strategy and the coding for the transformer are the main modeling novelties while the ablation studies have significant impact on the understanding of the field. Still, the presentation would be improved with a clear contributions section that highlights this.
- Authors claim that the performance of the model improves not with the number of parameters but with the state size. I am wondering if this is the case because the datasets considered such as MNIST are simple enough that having more parameters is no longer helpful rather than showing a general trend.

### Questions
Authors claim that the performance of the model improves not with the number of parameters but with the state size. I am wondering if this is the case because the datasets considered such as MNIST are simple enough that having more parameters is no longer helpful rather than showing a general trend.

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
The paper describes a "General Purpose In Context Learning" algorithm. It is basically transformed that is trained to predict the label of a specific sample given a context (the train dataset). The authors do experiments in some datasets such as MNIST and SVHN, and compare to some baselines to demonstrate that their method achieves some degree of generalization.

### Strengths
- The paper adresses a very important problem in the community: learning-to-learn, in order to leverage information from previous tasks. 
- The authors invest some effort in demonstrating that the model generalizes.

### Weaknesses
 - Lack of related work discussion: there is a tremendous amount of related work aiming to perform meta-learning or adapting transformers for in-context learning. However, the authors do not discuss any of them. For instance Meta-Transformer [1], OptFormer [2], or PFNs [3]. 

 - The contribution is limited: the authors propose a very similar approach as to previous work [2][3], while only introducing a data augmentation step.

 - The data augmentation step is not well-founded. By performing random projections, it is likely to introduce noise. According to the authors, it allows to achieve generalization, but they do not perform any ablation to test this.

 - Experiments are poor in demonstrating the validity and superiority method. They do not use strong baselines or relevant datasets (they limit most of the experiments to MNIST).

### Questions
- Are the authors planing to release the code?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
