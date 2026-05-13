# Learning Randomized Algorithms with Transformers

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Randomization is a powerful tool that endows algorithms with remarkable properties. For instance, randomized algorithms excel in adversarial settings, often surpassing the worst-case performance of deterministic algorithms with large margins. Furthermore, their success probability can be amplified by simple strategies such as repetition and majority voting.
In this paper, we enhance deep neural networks, in particular transformer models, with randomization. We demonstrate for the first time that randomized algorithms can be instilled in transformers through learning, in a purely data- and objective-driven manner.
First, we analyze known adversarial objectives for which randomized algorithms offer a distinct advantage over deterministic ones. We then show that common optimization techniques, such as gradient descent or evolutionary strategies, can effectively learn transformer parameters that make use of the randomness provided to the model.
To illustrate the broad applicability of randomization in empowering neural networks, we study three conceptual tasks: associative recall, graph coloring, and agents that explore grid worlds. In addition to demonstrating increased robustness against oblivious adversaries through learned randomization, our experiments reveal remarkable performance improvements due to the inherently random nature of the neural networks' computation and predictions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Randomized algorithms can offer better worst-case performance than deterministic ones.  
Can transformers learn randomized algorithms?   
The authors study conditions for randomized algorithms to yield possible advantages and they offer a training methodology to emerge them in transformer networks. Namely design choices to emerge randomized algorithms involve around: a. the model; it needs to have limited capacity and receive random signal at its input, b. the loss function; it needs to be a surrogate for worst-input risk instead of expected risk.
They demonstrate application in three conceptual tasks: associative recall, graph coloring, agent exploring a grid-world
And they claim that randomized algorithms achieve increased robustness against adversaries.

### Strengths
Very well-written paper, easy to follow, with extensive examples and related work material both in the main paper and in the appendix.
Well-motivated and executed study for the possibility to learn randomized algorithms.

1. Convincing results of superior worst-case performance in the considered tasks when compared to training alternatives, ablating some aspect of the loss, the multi-seed version trained on the relaxed adversarial loss is the best.
2. Experiments cover well important hyperparameters for the training setting. namely the relaxation hyperparameter which interpolates between ERM and worst-case risk, $q$, and the number of seeds per input, $m$.
3. Experiments cover variety of architectural constraints, such as linear attention (sec 3.2), structured local attention masks that are GNN-like (sec 3.3), and autoregressive settings (sec 3.4). As well as a variety of tasks and optimization techniques.

The paper finds the reader with a clear impression about the possibility of randomized algorithms for improving worst-case performance, as evidence by 95th percentile results in Figs 2,3,5 and 7. As well as inference-time strategies on improving them with majority voting.

### Weaknesses
 1.a. I would personally have enjoyed seeing experiments with actual adversarial robustness training, using a threat model on human preference alignment data, applied at generative LLMs.  

1.b. Lines 216-218 mention that adversarial robustness training is difficult, however recent literature has provided with framework for that [1]. While it does not decrease the contributions of this paper, comparing with the methodology mentioned in the paper would have been great!

2. Section 2.1 “Excessive Model Capacity Will not Enforce Randomness” the argument is not very convincing to me. In the face of a multi-seed worst-case objective like one described later, does the argument still hold? Proposition 1 also seems to go against the impossibility eluded by this section. Experiments on finetuning medium-sized (~1B) models on toy tasks could have provided some extra evidence for that.

3. On grid-world experiments: While the first episode demonstrates randomness in ways to explore for the target, why doesn’t the randomness follow as well in the second “exploitation” episode? There are multiple equivalent in length ways to reach the target. I would expect that in Figure 6.C. those would vary across different seeds.

4. Instead of using input randomness, it would have been very interesting to understand the ability or limitations on using output sample randomness which is fed back to the input in an autoreregressive case, as a drive to learn randomized algorithms. The authors avoid this explicitly in Section 3.4, however I do not understand the reason.

### Questions
1. The transition to use the q-norm relaxed loss in L195-200 is not motivated sufficiently at that point in text. Can you elaborate on it a bit more?

2. L207-208: Are the same random input seeds reused for all inputs? Why? What would happen if fresh seeds are sampled for every input $x_i$?  

3. Batching strategy when finetuning for the emergence of a randomized algorithm is not clear at the text. I assume that $B \times N$ samples are processed independently at once. $B$ is the number of input data, $N$ is the number of random seeds. Is this correct?

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
The paper explores the incorporation of randomized algorithms into transformer models through learning, in order to enhance robustness and performance in adversarial environments. By training transformers on expected and adversarial losso, single and multiple seeds, the study demonstrates that their proposed approach can outperform their deterministic counterparts, particularly when faced with adversarial challenges. The authors focus on three main tasks: associative recall, graph coloring and exploration in grid worlds, to evaluate the impact of randomized strategies on model performance. The results indicate that, by employing randomness, transformers achieve higher robustness and adaptability (implementing simple strategies repetition or majority voting) over predictions with different random seeds.

### Strengths
1) Innovative integration of randomization: Altough randomization was a concept that has been used with Transformers during the years and at different levels (e.g. positional encodings, attention weights) the paper introduces an original concept of definining randomized algorithms within neural networks through learning: by simple epmloying repetitions and strategies such as majority voting this approach outperforms deterministic approach

2) Comprehensive experimental design: The paper provides a solid experimental framework across varied tasks, such as associative recall, graph coloring, and grid world exploration. Each task is carefully selected to illustrate different advantages of randomization, such as memory management, combinatorial problem-solving, and exploration.

3) Theoretical justifications and adversarially driven objective : The authors define a description of theoretical considerations about randomized algorithms that bring to the definition of an adversarially driven objective: it is an interesting addition that supports the study's claims on robustness. The use of a relaxed adversarial loss and exploration of different adversarial strengths adds depth and completeness to the analysis of transformer behavior in challenging environments.

4) Empirical results on robustness: The empirical results are thorough and show randomized transformers advantages, eespecially in scenarios with worst-case inputs. The paper's analysis highlights how majority voting and the number of seeds influence performance, enhancing the robustness of the findings. Moreover tha authors discuss about their results and the major limitations of their approach.

5) Appendix: Further information on the training modality and parameters is appreciated.

### Weaknesses
1) Scalability challenges: The most important corcern about the proposed methodology is the computationally cost, particularly with the reliance on multiple seeds and adversarial loss training. The authors acknowledge this in the "Summary and Limitations" paragraph, noting that scaling the approach to larger settings may require significant computational resources, which limits the practicality and broader applicability of the approach. I consider that such a problem should have been addressed in a more in-depth manner and not relegated to a second analysis, as it is a very important measure for judging the entire methodology. Specifically, the paper lacks a detailed analysis of the computational complexity as a function of the number of seeds (m), the number of repetitions (q), and the size of the input. A theoretical analysis, or at least an empirical study on the scaling of training time and memory consumption with respect to these parameters, would be crucial to assess the feasibility of the approach for larger problems. The absence of such an analysis makes it difficult to understand the practical limitations of the proposed method.

2) Limited practical applications discussed: While the theoretical foundation is strong, the paper could benefit from discussing more real-world applications where randomized transformers might be beneficial. The current discussion is limited to the three tasks presented, which are somewhat abstract. The paper would be strengthened by exploring potential applications in areas such as robotics, where exploration and robustness are crucial, or in financial modeling, where dealing with noisy and adversarial data is a common challenge. Without these concrete examples, the practical relevance of the proposed approach remains unclear.

3) Dependency on the choice of q and m hyperparameters: The model's performance and randomization effectiveness heavily depend on hyperparameters, particularly q and m. The authors could delve further into automated ways to tune these values or provide guidelines for choosing optimal parameters for various tasks. High-computation hardware needed to perfom analysis about the hyperparameters can be prohibitive. The paper does not provide sufficient guidance on how to select these parameters, and the sensitivity analysis is limited. A more thorough investigation into the impact of these parameters on the final performance, including a discussion of the trade-offs between performance and computational cost, is needed. Furthermore, the lack of a clear methodology for choosing these parameters makes it difficult to reproduce the results and apply the method to new problems.

### Questions
What were the reasons that pushed the authors not to present analyses (even theoretical) regarding the computational cost preferring to insert more general information such as section E of the appendix?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores how transformers can learn and implement randomized algorithms, which are advantageous in certain adversarial and game-theoretical contexts. Randomized algorithms typically perform well in adversarial environments and exhibit robustness against worst-case scenarios. The authors propose a novel objective function for training transformers that optimizes their performance in these settings by introducing randomization via an input "seed."

### Strengths
- The authors provide a strong theoretical foundation for why randomization is advantageous in certain adversarial contexts, referencing game theory and established concepts like Yao’s Minimax Principle.
- The study highlights that randomization can increase resilience against adversarial attacks.

### Weaknesses
 - While the paper presents conceptual tasks to validate the approach, it does not provide empirical results on large-scale or real-world datasets. This limitation raises questions about how well the method would scale and perform in more complex, realistic environments.
- The approach requires sampling multiple seeds during training (controlled by the hyperparameter mm), which can increase computational overhead significantly. The authors note that this limitation affects memory, training time, and inference time, making the method potentially impractical for large-scale applications.
- The paper’s theoretical sections are rigorous but may be dense for readers without a background in adversarial training or randomized algorithms.
- The study assumes relatively static environments for tasks like grid world exploration and graph coloring. However, it does not address how the transformer’s randomized strategies would perform in dynamic, non-stationary settings where environmental conditions change over time.

### Questions
- What are the computational and memory challenges of scaling the proposed randomization method to larger, more complex datasets or real-world tasks? Are there specific optimizations that could make the approach more efficient?
- The study introduces hyperparameters qq and mm in the training objective. How sensitive are the final model’s performance and robustness to variations in these hyperparameters?
- Could the proposed randomization approach be adapted for more complex reinforcement learning environments, such as those with continuous action spaces or requiring long-term strategy?
- How does this approach compare with other randomization techniques, such as dropout (at inference)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the integration of randomization into transformer models, traditionally used in deterministic settings, to enhance their performance, especially in adversarial contexts. The authors demonstrate that randomized algorithms can be instilled in transformers through learning, in a purely data- and objective-driven manner. Though an analysis of known adversarial objectives for which randomized algorithms offer a distinct advantage over deterministic ones, they show that common optimization techniques, such as gradient descent or evolutionary strategies can effectively learn transformer parameters that make use of the randomness provided to the model. To illustrate the broad applicability of randomization in empowering neural networks, we study three conceptual tasks: associative recall, graph coloring, and agents that explore grid worlds.

### Strengths
- The paper is very well written, clear, with a good motivation. They first introduce the setting by presenting an example with associative recall, which is a variant of the classical paging problem in computer science for which randomized solutions exist. This problem is also a well-studied problem for transformers with the goal of evaluating recall capabilities. The paper continues with a theoretical analysis in which the authors study when randomization can be beneficial and when it is not. From there, the authors propose a training objective. 
Finally, the authors experiment with 3 use cases: associative recall, graph coloring, and agents exploring lattice worlds.
- The contribution is, to the best of my knowledge, novel and could lead to improvements in how transformers can solve certain tasks.

### Weaknesses
 - The experiments are performed on three different small tasks, the proposed approach should increase the computational complexity, which is already high with transformers, can the authors comment on this in terms of training and inference? 
- I am a bit puzzled by the paragraph on adversarial robustness (small input perturbations) in the related work, first, the cited paper (Rakin et al. (2018)) shows an approach to increase robustness with randomization, but now such approaches have been mostly disproved (see Gnecco et al. 2023). Furthermore, the randomized smoothing approach uses randomization _only in the training phase_, the approach is inherently a training procedure for a smooth function. The inference _is_ deterministic. Overall, I find this discussion could be made clearer.

### Questions
See first Weakness

### Soundness
3

### Presentation
4

### Contribution
3
