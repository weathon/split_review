# Accelerated training through iterative gradient propagation along the residual path

- Decision: Accept
- Scores: 6, 6, 8, 8, 8

## Abstract
Despite being the cornerstone of deep learning, backpropagation is criticized for its inherent sequentiality, which can limit the scalability of very deep models.
Such models faced convergence issues due to vanishing gradient, later resolved using residual connections. Variants of these are now widely used in modern architectures.
However, the computational cost of backpropagation remains a major burden, accounting for most of the training time.
Taking advantage of residual-like architectural designs, we introduce Highway backpropagation, a parallelizable iterative algorithm that approximates backpropagation, by alternatively i) accumulating the gradient estimates along the residual path, and ii) backpropagating them through every layer in parallel. This algorithm is naturally derived from a decomposition of the gradient as the sum of gradients flowing through all paths, and is adaptable to a diverse set of common architectures, ranging from ResNets and Transformers to recurrent neural networks.
Through an extensive empirical study on a large selection of tasks and models, we evaluate Highway-BP and show that major speedups can be achieved with minimal performance degradation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method to accelerate the backward pass of backpropagation through parallelization of the gradient calculation in deep neural networks with residual-like architecture. This is done by decomposing the gradient into a sum of terms, where the k-th term is the sum of all gradients passing through at most k blocks which are not a residual (i.e. skip-like) connection. By parallelizing this computation, an acceleration is achieved as long as the maximal k we compute is not too large (i.e., we need to drop values of k above some threshold). It is shown empirically that k=5 is approximately enough for good accuracy on several (small) benchmarks, while still achieving significant acceleration.

### Strengths
1. The problem of accelerating Backprop is important.

2. The idea is novel, original, and quite interesting.

3. The empirical results are promising.

4. The presentation is mostly clear.

### Weaknesses
1. The main issue is the scale of the experiments, which is rather small (e.g., no ImageNet). It is not clear to me that a small k would be enough to get both high accuracy and acceleration on more complicated problems than those shown in this paper. The experiments are limited to relatively small datasets (CIFAR-10, CIFAR-100, and Wikitext103), and the models used are not as complex as those commonly used in state-of-the-art research. The lack of experiments on large-scale datasets like ImageNet makes it difficult to assess the practical applicability of the proposed method in real-world scenarios.  It is also unclear whether the observed performance gains would generalize to more complex architectures and tasks.

2. The acceleration is only relevant for the backward pass, which is roughly a third of the total time of Backprop (which includes the forward pass, backward pass, and parameter gradient) and so this limits the overall benefit of this method. While the authors focus on accelerating the backward pass, the forward pass and the parameter update also contribute significantly to the total training time. The reported speedups might not translate to substantial overall training time reductions if the backward pass is not the dominant bottleneck in more complex models or hardware settings. The method's impact on the overall training time is therefore limited by its focus on only one of the three stages.

### Questions
3. I think there are some small mistakes in the math. For example, in eq. 8: 

$\quad$ a) The transition to eq. 8 from eq. 6 is not clear. Specifically, why did $w_{i}^{0}$ disappear?

$\quad$ b) The right side of eq. 8 seems different from the middle part of the equation, since $v_{i}^{k+1}$ is multiplied by $K_{i+1}$ in the middle part of the equation, but not in the right side of the equation.

Can the authors please check these?

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
4

### Summary
The paper introduces Highway backpropagation (Highway-BP), an algorithm that speeds up training of deep neural networks by approximating traditional backpropagation using parallelizable iterative methods. It leverages residual connections to propagate gradients efficiently and is adaptable to various architectures like ResNets and Transformers. Empirical studies show that Highway-BP achieves significant speedups with minimal performance loss, making it a promising method for accelerating deep learning model training.

### Strengths
Parallelization: The algorithm is designed to be parallelizable, which can significantly reduce training time, especially for very deep models or large-scale problems.
Architecture Flexibility: Highway-BP is adaptable to a variety of common neural network architectures, making it a versatile tool for different applications.
Theoretical Foundation: The paper is grounded in mathematical theorems that provide a theoretical foundation for the proposed method.

### Weaknesses
Generalization to All Models: Although Highway-BP is adaptable to many architectures, there may be specific models or scenarios where it does not perform as well as traditional backpropagation or other optimization methods. For example, experiments on Graph neural network, spiking neural network and mamba.
Hyperparameter Tuning: The algorithm introduces a new hyperparameter (the number of iterations, k), which requires tuning and may lead to different optimal values depending on the model and task. This can add complexity to the training process. A ablation on how to tune the parameter should be included.
Missing baselines: The paper compares Highway-BP with backpropagation and fixed-point iteration but may not fully address how it stacks up against other state-of-the-art optimization techniques. Here are some papers authors should include in their baseline:
Huang, Kai, et al. "Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation." arXiv preprint arXiv:2309.13192 (2023).
Wang, Ziteng, Jianfei Chen, and Jun Zhu. "Efficient Backpropagation with Variance-Controlled Adaptive Sampling." arXiv preprint arXiv:2402.17227 (2024).
Yang, Yuedong, et al. "Efficient low-rank backpropagation for vision transformer adaptation." Advances in Neural Information Processing Systems 36 (2024).
Scalability to Distributed Settings: The paper mentions the potential for distributed training but does not provide empirical results or a detailed discussion on how Highway-BP would perform in a distributed setting.

### Questions
How does Highway-BP compare with other advanced optimization techniques, especially in terms of convergence speed and final model accuracy?
What are the performance implications of Highway-BP when scaling to models with billions of parameters, and how does it handle memory and computational constraints?
Can the authors provide more theoretical analysis or proofs regarding the convergence properties of Highway-BP compared to traditional backpropagation? For example, give a lower bound for the improvement.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers gradient computation in network architectures with multiple residual connections. The authors propose the Highway-BP method to improve the efficiency of gradient computation/estimation by decoupling and rearranging multiple computational paths in vanilla BP. The proposed algorithm leverages the fact that computational burdens differ between the two paths within each block and iteratively approximates the gradient from easier to more challenging paths, allowing trade-offs between accuracy and efficiency through adjustable iteration steps. Numerical results indicate that the approximate gradient, with a certain number of iterations, achieves comparable results to the true gradient, demonstrating its potential applicability.

### Strengths
The authors present an interesting idea for improving the sequential computation in BP, utilizing the shared structural characteristics of mainstream models, which may facilitate further refined explorations in the future. The experimental results in the paper are comprehensive, demonstrating potential advantages in terms of efficiency.

### Weaknesses
My main concern is that unrolling the recursive computation in vanilla BP requires storing a significant number of additional variables, thereby increasing the algorithm’s storage demands. The authors do not appear to provide test results for memory consumption, which is an important consideration when developing algorithms for large-scale models. From the perspective of memory usage, the proposed method introduces additional tensors to store intermediate results for the iterative approximation, which could be a significant overhead, especially when dealing with deep networks or high-resolution inputs. The authors should provide a detailed analysis of the memory footprint of their method, including the size of these additional tensors and how they scale with network depth and input size.

The efficiency of the proposed algorithm lacks theoretical guarantees, and the experimental results have minor flaws. Please see the question part for details. The comparison includes only the fixed-point iteration algorithm. Algorithms mentioned in the literature and other approximation-based acceleration methods for BP are not included. Furthermore, the time overhead observed in Table 3, where the proposed algorithm approaches the time consumption of vanilla BP with only 20 iterations, suggests that the additional read/write operations and the computation of the CumSumProd operation may introduce a non-negligible overhead, potentially negating the benefits of the approximation, especially for larger models or more complex architectures. This needs further investigation and more detailed analysis.

### Questions
- The authors should provide a more detailed experimental setup in the paper. In Figure 2, the final performance of vanilla BP appears to differ significantly from its usual training outcomes. Might this be due to insufficient training? As observed in Figure 3, the effectiveness of Highway-BP's approximation seems limited to the relatively easy early stages of training, suggesting that the accuracy results in Figure 2 may need to be presented at multiple time points.

- The paper includes empirical tests of the algorithm, but could the authors provide a theoretical analysis of how the approximation error varies with $k$? Alternatively, could a more rigorous boundary be identified for the types of network structures where this approximation applies? Additionally, conducting a comprehensive analysis of the time and space complexity of Highway-BP is also worthwhile and important.

- Since the paper aims to alleviate the sequentiality in BP, which is a challenge that typically arises in large models, could the authors evaluate whether the complex computation of Highway-BP might hinder the application of other crucial techniques in this area, such as data parallelism or distributed training? Furthermore, how might these structural changes to gradient computation impact communication and read/write overhead?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Summary: This paper proposes Highway Backpropagation, an algorithm for accelerating the training of neural nets with residual connections (such as ResNets, RNNs, and Transformers) by skipping some of the expensive backpropagation steps. In a nutshell, backpropagating a gradient through a layer consisting of a weight matrix plus a residual connection consists of a ‘cheap’ part (the residual) and an expensive part (the weight matrix), and the total gradient can be represented as the sum of all combinations of going through either. By omitting some of the terms of that summation - specifically those that have more than $k$ ‘expensive’ components, the gradient calculation can be sped up. The authors address the practical concerns of the implementation and provide experimental results validating their setup.

### Strengths
This paper tackles a crucially important problem, which is the enormous cumulative expense of training machine learning models, especially in the world of transformers. The idea seems to be quite original, and makes a great deal of intuitive sense. It is also straightforward to implement.

Overall, the main body of the paper is generally well-written and lays out its argument in a logical and even exciting way. The mathematical argument is very clearly presented. Further, the practical considerations of creating an implementation with real-world speedups are addressed.

The training dynamics section is nicely presented and interesting.

### Weaknesses
### Main weaknesses:

The main weakness of the paper is the experimental section. While the method is clever, the real value of the idea is in whether it is actually useful, and unfortunately the experimental section does not sufficiently cover this point. Of course, we cannot expect a finely optimized implementation in a research work. However, this reviewer doesn’t see a reason that a basic, workable implementation couldn’t have been built for standard architectures (e.g., ResNets) or something much closer to them. Because of the authors’ use of these nonstandard implementations, at least some of the actual numerical results are very far below what could be expected.

For instance, for CIFAR100, a standard ResNet50 architecture would have an accuracy of over 85%; the 50-layer architecture used in the paper (albeit with about a quarter of the total parameters of a RN50)  has an accuracy of 40%. A ResNet20, which has far fewer parameters, should still be able to get something like 70-75%. The authors do not address or justify this gap.

Likewise, real-world speedup numbers are not presented. Again, the point regarding the practical difficulty of creating a CUDA-optimal distributed setup is well taken, but the question remains unanswered. Perhaps it may have been possible to create a less-optimized standard implementation of backpropagation (e.g., on CPU) and compare this to the proposed one.

Finally, there is no guidance for selecting the right $k$ for a new task. This omission makes it difficult to use Highway Backpropagation in practice, even if an efficient implementation is available. 

### Smaller issues:

The writing style of the introduction/related work sections is often vague or confusing.
* Like 36: what is meant by “transformers only defer the problem”?
* Line 41: What is meant by “often involve trade-offs between speed and task performance”? Aren’t these tradeoffs always involved?
* Line 42: What is meant by “leverage the recent layers”?
* Line 45: What is meant by “significantly improves optimization”? Can vague statements like this be made more precise?
* Line 51: What is meant by “derived from an original derivation”?
* Line 75: “where gradients can either diminish or grow uncontrollably” is completely redundant with line 73.
* Line 92: “While this seems attractive, the reality differs” - can this be made more clear and precise?
* Line 93: “computing the Jacobian matrix of all layers”: this is misleading, since the proposed Highway-BP algorithm also requires this computation.

Line 192 typo provie -> provide

Line 231 typo $K$ -> $k$

### Questions
* Why is the CIFAR-10 and CIFAR-100 model accuracy so low for the chosen architectures, or, conversely, why were architectures with such low accuracy chosen?

* Especially for image classification, why was this method not tested in the most standard setups, for instance Imagenet-1K on a standard ResNet50? Admittedly, in a standard RN50 architecture, the residual layer spans several weight matrices, but this seems like a straightforward extension of the proposed method. For the architectures chosen, why is the number of parameters much lower than that of the standard models (for instance, a traditional ResNet30 would have about 25M parameters, versus this paper’s 4.1M)? What is meant in line 317 by “standard ResNet”?

* In line 367, what is meant by “very reasonable performances”? 

* Is there an advantage to varying $k$ during the training process?

* Why are the intermediate losses necessary for the theoretical framework to be effective?   Likewise, why is the proposed algorithm restricted to generative and classification tasks (liNE 153)?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new algorithm for approximating backpropagation in deep sequential neural network models: Highway Backpropagation (Highway-BP)

Motivation: Backprop is computationally expensive, and has sequential dependence in depth making it hard to parallelize.
Key idea: Highway-BP leverages residual connections in modern architectures to decompose the gradient into paths of different lengths. It then iteratively computes an approximation of the gradient. Pruning some of the gradient paths enables Highway-BP to compute the approximate backprop in parallel. Doing this iteratively allows the approximate gradient to approach the true gradient over iterations.




I really like this paper. In my head I'm drawing a parallel with the "Residual Networks Behave Like Ensembles of Relatively Shallow Networks" paper. In Figure 1 from that paper, they "unravel" the residual connection of an N=3 block network.
When I read your paper, I immediately drew a parallel with that paper where, a view of your method, is that you only take backprop thru the right diagonal portion of the "unraveled" representation of Figure 1(b) of the "Residual Networks Behave Like Ensembles of Relatively Shallow Networks" paper.
Its brilliant!
(I am not an author of that paper :) )

### Strengths
(1) Flexibility: Can be applied to various architectures like ResNets, Transformers, and RNNs. 

(1.5) Experiments: Tested on image classification (CIFAR10/100) and language modeling (Wikitext103) tasks. Compared against standard backpropagation and fixed-point iteration (for RNNs). Achieved comparable performance to backpropagation with fewer iterations (k ≤ 5 in most cases). Showed consistent speedups (2x-4x) over standard backpropagation.

(2) Paper presents a tradeoff frontier: Number of iterations (k) controls the trade-off between speed and accuracy

Edit:
(3) The parallelism unlocked by this method can greatly accelerate training speeds producing more efficient and faster training setups. The fact that it generalizes to a lot of settings makes this paper :chefs-kiss:
(see Appendix C for potential speedup wins (but this could be better presented in the main body))

### Weaknesses
This proposes a way to accelerate training at the cost of model performance
The true cost of AI is inference NOT training. I'd pay more for training if it produced a better model (and therefore made TCO cheaper)...

The results obviously show that the using the method produces worse models


I'll be the echo chamber (somebody has gotta do it): I want to see this applied to large scale autoregressive LLMs. Show me LLaMa training or I don't care! 
\s

### Questions
The results obviously show that the using the method produces worse models.
Have you looked at methods for recovering performance?
Have you tried increasing k over training?
In figure 3, I can see a schedule in which, for the first 500 steps, you use k=1, then for the next 500 steps, you use k=2, then for the next 1000 steps, you use k=5, then eventually you use backprop a the end of training to fully recover performance.


Edit:
Can Figure 3 be redone but with training time on the x-axis (instead of time)? Appendix C shows that your method will look more favorable when this is done.

### Soundness
3

### Presentation
3

### Contribution
4
