# Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Neuromorphic computing with spiking neural networks is promising for energy-efficient artificial intelligence (AI) applications. However, different from humans who continually learn different tasks in a lifetime, neural network models suffer from catastrophic forgetting. How could neuronal operations solve this problem is an important question for AI and neuroscience. Many previous studies draw inspiration from observed neuroscience phenomena and propose episodic replay or synaptic metaplasticity, but they are not guaranteed to explicitly preserve knowledge for neuron populations. Other works focus on machine learning methods with more mathematical grounding, e.g., orthogonal projection on high dimensional spaces, but there is no neural correspondence for neuromorphic computing. In this work, we develop a new method with neuronal operations based on lateral connections and Hebbian learning, which can protect knowledge by projecting activity traces of neurons into an orthogonal subspace so that synaptic weight update will not interfere with old tasks. We show that Hebbian and anti-Hebbian learning on recurrent lateral connections can effectively extract the principal subspace of neural activities and enable orthogonal projection. This provides new insights into how neural circuits and Hebbian learning can help continual learning, and also how the concept of orthogonal projection can be realized in neuronal systems. Our method is also flexible to utilize arbitrary training methods based on presynaptic activities/traces. Experiments show that our method consistently solves forgetting for spiking neural networks with nearly zero forgetting under various supervised training methods with different error propagation approaches, and outperforms previous approaches under various settings. Our method can pave a solid path for building continual neuromorphic computing systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Unlike biological intelligence, current deep learning suffers from catastrophic forgetting— upon learning new tasks, networks often lose the ability to solve previously learned tasks. 
One set of methods to solve catastrophic forgetting is orthogonal gradient projection, in which the learning gradient for new tasks are projected to a subspace that is approximately orthogonal to the subspace of the gradient of the network w.r.t. the weights for old tasks.
However, they are not applicable to Spiking Neural Networks (SNNs), which is the predominant architecture for neuromorphic learning.
This paper proposes Hebbian Learning based Orthogonal Projection, or HLOP, an orthogonal gradient projection method that extracts principal subspaces of neuronal activities using Hebbian learning.
HLOP is compatible with SNNs, and outperforms other continuous learning methods on several computer vision datasets.
Thus, it may be a promising new direction for continual neuromorphic learning.

### Strengths
- The authors introduce a novel combination of Hebbian learning with orthogonal projection to solve catastrophic forgetting for SNNs. While using Hebbian learning to find principal subspaces is not a new technique, its application to this problem is both novel and elegant.
- HLOP achieves strong empirical performance, surpassing all other continual learning methods that the authors benchmarked against.

### Weaknesses
- The final paragraph of the intro that discusses your contributions is a bit dense. I suggest breaking it up, and allocating more intro space to discuss your contributions, as it’s the most important part of your intro. In particular, I think you should have a separate paragraph to discuss the experimental setup and results, and include some performance numbers to quantify the strength of your method; currently its strength is hard to judge from the intro.

- The background on SNNs provided in Section 3.1 is a word-for-word replica of Section 3.1 in Xiao et al. (2022).
It’s fine to reuse definitions from previous work, but a direct replica like this should be explicitly attributed to avoid plagiarism concerns (even if it’s your own work).

- There is almost no discussion on the current limitations/challenges of HLOP and the experimental design, making it hard to judge the tradeoffs between using HLOP versus other approaches.
I’d like to see the authors also include a discussion on the potential downsides of HLOP and limitations of the evaluation process.

- Minor issue, but the sentence in Section 5.2 explaining the weight transport problem of backprop is very long and hard to parse.
I suggest either rewriting it and breaking it down to smaller chunks, or removing it entirely as it’s not central to your work; just stating that FA and SS are more biologically-plausible and more amenable to neuromorphic hardware is enough.

### Questions
- At the end of Section 3.2, you mention that previous methods “cannot be implemented by neuronal operations for neuromorphic computing,” but do not provide further explanation. 
To me, this is important because it provides critical motivation for your method; it highlights why your novel approach using Hebbian learning is required.
I understand that these methods cannot be directly implemented on SNNs out-of-the-box, but can you elaborate on why it is difficult or infeasible to adapt them for SNNs?

- The performance of HLOP is close to the upper bound (specified by Multitask performance) for each dataset except miniImageNet, where there is a large gap. Can you provide reasoning or intuition for why this is the case?

- Your results show that HLOP outperforms several other continual learning methods. Can I assume that the results achieved with HLOP are state-of-the-art on these datasets? Or are there other methods that you did not compare against?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a task-incremental continual learning (CL) method for spiking neural networks.
It can be categorized as a CL approach based on orthogonal gradient projection.
In orthogonal gradient projection approaches, the update $\Delta \mathbf W^P$ of each layer is projected to a subspace to minimize changes to the outputs for previous tasks.
This is achieved by performing PCA on the input data for each layer and projecting the gradient to the subspace orthogonal to the principal subspace of the input data.

The main technical novelty of this work is the application of a Hebbian learning rule to perform PCA.
This rule is claimed to be more suitable for neuromorphic hardware.

### Strengths
- The paper is clearly written and easy to follow.
- The combination of spiking neural networks and continual learning seems interesting, although this is not the first work to address such problems.
- Code is provided in the supplementary material.

### Weaknesses
### Not Comparing Other Approximations of PCA

The essence of the proposed Hebbian approach is to perform PCA.
While there is a huge literature on more efficient approximate PCA with various forms of tradeoffs, the Hebbian approach is just one of such variants of PCA.

I think the authors need to justify why their Hebbian approach is particularly suitable for spiking neural networks.
They vaguely argue that the Hebbian rule only requires "neuronal operations," but the neuroscience-backed algorithm eventually boils down to some matrix-vector arithmetic, just like many other approximate PCA algorithms.
Currently, I do not see any reason that the Hebbian rule should be more suitable for spiking neural networks while others are not.

### Task-Incremental Settings

This paper exclusively focuses on the task-incremental settings.
Task-incremental CL is often considered the most naive and easiest form of CL.
Especially, providing task IDs even at test time is far from realistic and significantly reduces its practical utility.
I believe that relying solely on task-incremental experiments is insufficient to establish meaningful results.

### Questions
- Is the Hebbian rule a better fit for spiking neural networks compared to other approximate PCA approaches?
- If it is, what makes the Hebbian rule more suitable, and why aren't the other approaches as effective?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Hebbian learning based orthogonal projection (HLOP) as a novel method for implementing orthogonal projection using neuronal operations. Building upon the method of calculating projection matrices through SVD proposed by Saha et al. (2021), HLOP combines the properties of Hebbian learning to approximate orthogonal projection using learned weight matrices. This is the first approach that fully utilizes neuronal operations for implementing orthogonal projection. Furthermore, HLOP outperforms several baseline methods on multiple continual learning datasets, demonstrating the reliability of the proposed method through experimental results.

### Strengths
1.The paper introduces for the first time a method that fully utilizes neuronal operations to approximate orthogonal projection matrices, and achieves the best performance surpassing multiple baseline methods on various datasets in continual learning task.
2.The implementation based on Hebbian learning can seamlessly integrate with different training methods and aligns well with the parallel local learning approach of neuromorphic chips.
3.HLOP can be directly applied to SNNs, providing a new approach for continual learning in SNNs.

### Weaknesses
1.The method lacks sufficient detail in the methodology section. Providing complete formulas or a specific illustrative example would enhance understanding. 
2.The baselines compared in the study include EWC (Kirkpatrick et al., 2017), HAT (Serra et al., 2018), and GPM (Saha et al., 2021). It would be valuable to investigate if there are recent works that achieve better results than these methods.
3.Although the continual learning approach in this study relies solely on neuronal operations without directly utilizing past data, the increasing number of subspace neurons with each new task learned implies a form of data compression and storage to some extent.
4. Although the paper uses Hebbian learning to achieve a pure neuronal operation method, it seems that the newly added subspace neurons do not participate in the model's forward process. If this is the case, then despite being a pure neuronal operation approach, it is essentially just an estimation method for orthogonal projection matrices.
5. While the paper demonstrates the effectiveness of HLOP, it does not provide an explanation or analysis of why the weight matrices obtained through Hebbian learning can serve as a substitute for the orthogonal projection matrix.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper applies Oja's rule to implement gradient projection for continual learning. The method uses lateral circuits to avoid storing gradient explicitly, and works with spiking networks.

### Strengths
To the best of my knowledge, the method is novel. Orthogonalized gradients are known to perform well for continual learning, and Oja's rule is known to do PCA, but (as far as I know) they've never been combined like in this paper. The resulting method doesn't need to explicitly store gradients, and computes the projection matrix on the go with bio plausible operations (and not recursive least squares). This is an advantage over other projection-based methods. 

The method only uses Hebbian and anti-Hebbian plasticity, which makes it suitable for neuromorphic hardware and also biologically plausible. There's a caveat for biological networks though: the lateral circuits are only active during the backward pass, and don't interfere with the forward one. However, an exact biological implementation seems out of scope for this work.

Performance: on all (standard) benchmarks the method performs very well and usually outperforms other algorithms.

### Weaknesses
Some (not very critical) weaknesses:

1. The method needs to create new subspaces for each task, and then coordinate activity in a new subspace with the old ones. It's not clear if that can scale to many tasks (e.g. due to noise in PCA through Oja's rule) 
2. The lateral connectivity doesn't influence forward propagation (and it shouldn't due to projections), which might make it hard to implement with real neurons (not so sure about neuromorphic chips).
3. There are no evaluations on non-spiking networks, so it's not clear if the performance improvement over other methods is due to those being poorly suited for spikes or this method being better at continual learning.

### Questions
The proposed architecture looks like a model of memory, since neurons only update their weights if they haven't seen a specific input before. Can all task-specific lateral circuits be combined into a single associative memory module, like a Hopfield net, with each new memory being a new $y$ for the task?

Before Sec. 2:
>  Our results indicate that lateral circuits, which are long ignored by popular feedforward neural network

I’d say that lateral circuits are often present implicitly through normalization layers.

Tab. 2: boldface should be used for the best performing method in a column, not the author's method.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
