# Learning to Permute with Discrete Diffusion

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8, 8

## Abstract
The group of permutations $S_n$, also known as the finite symmetric groups, are essential in fields such as combinatorics, physics, and chemistry. However, learning a probability distribution over $S_n$ poses significant challenges due to its intractable size and discrete nature. In this paper, we introduce *SymmetricDiffusers*, a novel discrete diffusion model that simplifies the task of learning a complicated distribution over $S_n$ by decomposing it into learning simpler transitions of the reverse diffusion using deep neural networks. We identify the riffle shuffle as an effective forward transition and provide empirical guidelines for selecting the diffusion length based on the theory of random walks on finite groups. Additionally, we propose a generalized Plackett-Luce (PL) distribution for the reverse transition, which is provably more expressive than the PL distribution. We further introduce a theoretically grounded "denoising schedule" to improve sampling and learning efficiency. Extensive experiments show that our model achieves state-of-the-art or comparable performances on solving tasks including sorting 4-digit MNIST images, jigsaw puzzles, and traveling salesman problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents SymmetricDiffusers, a novel discrete diffusion model for learning distributions over permutations within symmetric groups. This model addresses the complexity of directly modeling the vast and discrete state space of permutations by decomposing the task into simpler, more manageable transitions.

Key contributions include:
1) Forward Diffusion Process Using Card Shuffling Methods: Symmetric diffusers introduce noise to permutations using classical shuffling methods (riffle shuffles, random transpositions, and random insertions). These methods facilitate a gradual transformation toward a known noise distribution, simplifying the learning process.
2) Generalized Plackett-Luce (PL) Distribution for Reverse Diffusion: To return the noisy state to its original distribution, the model leverages a neural network-based generalized PL distribution, enhancing expressiveness and effectively reconstructing complex dependencies within permutations.
3) Theoretically Grounded Denoising Schedule: An optimized denoising schedule merges reverse steps to boost sampling efficiency and learning performance, reducing computational requirements without sacrificing accuracy.

The model demonstrates state-of-the-art or comparable results in tasks such as sorting, jigsaw puzzle assembly, and solving traveling salesman problems, validating its effectiveness in permutation-based applications.

### Strengths
Originality: This paper demonstrates notable originality by advancing discrete diffusion models to tackle the problem of learning distributions over permutations in symmetric groups. The task of modeling permutations is inherently challenging due to the factorial growth of the state space, and SymmetricDiffusers introduces an innovative solution by utilizing card shuffling techniques (riffle shuffle, random transpositions, and random insertions) as part of a structured forward diffusion process. Combining classic combinatorial methods with modern neural-based diffusion modeling is an inspired choice well-suited to the discrete and combinatorial nature of permutations. Compared to related works on discrete diffusion—such as Discrete Denoising Diffusion Probabilistic Models (D3PMs), which focus on multinomial categories—SymmetricDiffusers addresses a unique domain with a permutation-focused framework that current D3PMs do not target.

Furthermore, introducing a generalized Plackett-Luce (PL) distribution for the reverse process sets this work apart from other discrete diffusion models, such as score-based continuous-time discrete-state models, which operate on categorical data but lack this flexibility. The generalized PL distribution is well suited for structured dependencies in permutations, enabling greater expressiveness and more accurate learning over complex permutations.

Quality: The paper demonstrates high methodological rigor. Each component of SymmetricDiffusers—the forward process using card shuffling, the generalized PL distribution for reverse diffusion, and the denoising schedule—is technically well developed and grounded in established theories of random walks and Markov chains on finite groups. This adds a layer of mathematical credibility to the proposed model, particularly in the careful treatment of transition probabilities and mixing times associated with the shuffling methods.

Additionally, the experiments are comprehensive and well-chosen to validate the model across diverse tasks, such as sorting, jigsaw puzzle completion, and traveling salesman problems (TSPs). This diversity of functions effectively showcases the robustness and generalizability of SymmetricDiffusers, achieving state-of-the-art or comparable results in each case. Unlike other discrete diffusion models focused on simpler domains (e.g., categorical image data), SymmetricDiffusers’ application to more complex combinatorial problems uniquely highlights the model’s practical value and robustness.

Clarity: The paper is generally well-organized and easy to follow, with a clear introduction to the challenges and requirements of permutation modeling. Complex ideas are supported by notations, figures, and a well-structured flow that gradually builds the reader’s understanding from the background on symmetric groups to the technical construction of SymmetricDiffusers. Visualizing the forward and reverse processes in figure form is particularly helpful, illustrating the model’s approach to diffusion over permutations.
However, compared to some other papers on discrete diffusion (e.g., D3PMs), certain sections—particularly those explaining the forward and reverse processes in detailed mathematical terms—might benefit from additional simplification for readers less familiar with random walks on finite groups. Nevertheless, the overall clarity and structure make the contributions accessible and understandable.

Significance: SymmetricDiffusers addresses an important area in machine learning by advancing the state of permutation modeling within discrete diffusion frameworks. Distributions over permutations are critical in domains like ranking, combinatorial optimization, and sequence alignment, and current models struggle with the computational complexity posed by large discrete spaces. This work opens up new possibilities for generative modeling within these areas, especially with its robust performance in tasks requiring complex combinatorial reasoning (e.g., TSP).

Compared to recent discrete diffusion works on more general categorical or sequential data, this paper contributes uniquely to discrete generative modeling by directly addressing permutation structures. This is significant because it establishes a pathway for diffusion models to utilize high-complexity tasks beyond traditional applications effectively. By providing an effective means of modeling permutations, SymmetricDiffusers could substantially impact practical applications and inspire future research in discrete-state diffusion for structured data.

The paper’s strengths lie in its original approach, which combines structured combinatorial methods with diffusion modeling. It also has high-quality methodological rigor, clearly presents complex concepts, and significantly contributes to modeling distributions over large permutation spaces, positioning it as a valuable advancement in discrete diffusion research.

### Weaknesses
Limited Comparative Analysis with Other Discrete Diffusion Models: While SymmetricDiffusers clearly advances permutation modeling, the paper could benefit from a more detailed comparison with other discrete diffusion models, particularly those handling high-dimensional categorical or sequential data, such as Discrete Denoising Diffusion Probabilistic Models (D3PMs). The current related work section mentions other models briefly but does not delve into how SymmetricDiffusers directly compares in terms of handling large discrete spaces. Including more detailed experiments or ablation studies to demonstrate SymmetricDiffusers’ advantages over such models regarding efficiency or performance on simpler permutation tasks could clarify its relative strengths and limitations. Specifically, the paper lacks a direct comparison showing how the proposed shuffling-based diffusion compares against standard categorical diffusion approaches when applied to permutation data, even if those approaches are not designed for permutations. This comparison is crucial to understand the practical benefits of the proposed approach over existing methods, even if those methods are not perfectly suited for the task.

Lack of Exploration on Scalability to Larger: The factorial growth of permutations means that scaling to larger sizes can become computationally intensive. The paper currently demonstrates its model on small-to-moderate values (e.g., tasks like 4-digit MNIST sorting). However, it does not provide clear insights into the scalability limits or potential strategies for scaling SymmetricDiffusers to larger values, where the computational load may become a bottleneck. Future work should consider including benchmarks on larger values or discussing ways to optimize the model’s performance, such as using sparse transition matrices or adopting modular architectures. The paper needs to address the practical limitations of the proposed method when applied to larger permutation spaces, including the computational cost of the forward and reverse processes, and the memory requirements for storing the model parameters and intermediate states.

Clarity in the Forward and Reverse Processes: While the paper is generally well-structured, some sections—particularly those detailing the forward and reverse diffusion processes—are highly technical and may be challenging for readers less familiar with symmetric groups and permutation modeling. Additional clarifications or simplified explanations could improve accessibility. Specifically, breaking down the mathematical formulations for each shuffling method and reverse diffusion process with more illustrative examples would make these sections easier to understand. Clearer definitions of key terms, such as “stationary distribution” and “mixing time” in the context of random walks, could also make the content more accessible to a broader audience. The paper should provide more intuitive explanations of how the shuffling methods induce a Markov chain on the symmetric group and how the generalized Plackett-Luce distribution is used to model the reverse transitions, including a discussion of the limitations of the standard Plackett-Luce distribution in this context.

Efficiency of the Denoising Schedule: The paper introduces a theoretically grounded denoising schedule to merge reverse steps and improve efficiency, but it lacks concrete benchmarks or ablation studies to assess its impact. Comparing SymmetricDiffusers with and without the denoising schedule in terms of computational time and performance would provide readers with a clearer understanding of its practical benefits. Additionally, exploring alternative denoising schedules or adaptive strategies that adjust based on task complexity could further optimize the model’s performance. The paper should also explore the sensitivity of the model to the choice of denoising schedule, and provide guidelines for selecting appropriate schedules for different tasks.

Broader Applicability and Practical Implications: Although SymmetricDiffusers demonstrates promising results in permutation-specific tasks (sorting, TSP, jigsaw puzzles), the paper could better communicate its broader applicability and potential limitations. For example, could the model be applied to non-permutation-based tasks with discrete structures, such as certain types of graph-based tasks? A brief discussion of the boundaries of SymmetricDiffusers’ applicability and how it might adapt to related yet distinct discrete structures would clarify its versatility and limitations.

### Questions
Comparative Analysis with Other Discrete Diffusion Models:
Question: Could you provide additional comparisons between symmetric diffusers and other discrete diffusion models, such as discrete denoising diffusion probabilistic models (D3PMs), particularly regarding tasks that involve smaller permutation spaces?
Suggestion: Including benchmarks with other models for more straightforward tasks could help clarify SymmetricDiffusers' unique benefits in terms of accuracy, expressiveness, and computational efficiency. If it outperforms or scales better than current discrete diffusion models, it would provide valuable evidence of its novelty.

Scalability for Larger :
Question: How do symmetric diffusers handle scalability as increases, and what strategies do you envision for managing the factorial growth in the state space for large permutations?
Suggestion: An empirical analysis or theoretical discussion on the scalability limits and potential optimizations (e.g., sparse transition matrices or modular architectures) would provide greater insight into the model’s practicality for large-scale tasks.

Denoising Schedule Efficiency:
Question: How significant is the denoising schedule's impact on computational efficiency and model performance? Have you considered alternative denoising schedules that might further improve efficiency?
Suggestion: An ablation study on the denoising schedule’s impact on performance and efficiency would be beneficial. Exploring adaptive denoising strategies or alternative merging techniques might also enhance the model’s flexibility and efficiency.

Forward and Reverse Diffusion Process Clarifications:
Question: Could you clarify certain technical details of the forward and reverse diffusion processes, especially for readers unfamiliar with symmetric groups? Specifically, could you break down the mathematical formulations for each shuffling method?
Suggestion: To make these sections more accessible to readers, illustrative examples for the shuffling and reverse diffusion steps or a more detailed explanation of terms such as “stationary distribution” and “mixing time” could be added.

Broader Applicability and Adaptation to Other Discrete Structures:
Question: Can symmetric diffusers be adapted for other structured discrete data beyond permutations, such as specific types of graph structures or other combinatorial tasks?
Suggestion: A brief discussion of the model’s applicability to other structured discrete data or potential adaptations would help clarify its versatility. For instance, could SymmetricDiffusers’ approach be generalized to data with hierarchical or relational structures?

Generalized Plackett-Luce Distribution Benefits:
Question: Could you provide more insights or experiments to demonstrate the practical benefits of using the generalized Plackett-Luce (PL) distribution over the standard PL model? In which cases does the generalized PL significantly enhance performance?
Suggestion: Examples or comparisons that highlight the generalized PL distribution’s expressiveness—especially in complex permutation tasks—would illustrate its value over standard PL models.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a discrete diffusion model for learning a distribution over permutations ($S_n$). They present several choices of forward noising process, including transpositions, insertions, and the rifle shuffle. For the reverse noising process, they define inverse processes corresponding to each of the three proposed forward processes, as well as a generalization of the Plackett-Luce Distribution that is more expressive than the original (e.g. it can represent a delta distribution). They train their diffusion models via a variational lower bound, estimated via Monte Carlo samples since they cannot obtain an analytic form. They derive a noise schedule, based on merging adjacent diffusion steps for certain inverse distributions, and run experiments comparing different versions of their diffusion model to differentiable sorting methods and test tasks including sorting MNIST digits and solving traveling salesman instances.

### Strengths
This is the first work to define a diffusion model over $S_n$. Their enumeration, and mathematical treatment, of possible forward and reverse noising processes is thorough, as are the experiments and ablations. The presentation is quite clear in general. The application of a diffusion model to problems that require outputting a permutation in a differentiable matter — even if a distribution over $S_n$ is not strictly required — seems to be creative and novel. The experimental results are generally good, particularly at increased sequence lengths.

### Weaknesses
To me, the main piece missing from this paper is a motivation of why machine learning applications require generative models over permutations in the first place, rather than just outputting a single permutation, which is what the tested datasets seem to satisfy. Is this related to differentiability? The introduction is well-written, but would improve from being more concrete and grounded in the machine learning literature. To be specific, the claim on line 35 that “Therefore, studying probabilistic models over $S_n$ through the lens of modern machine learning is both natural and beneficial” feels a bit unjustified. Differentiable sorting is mentioned in the related works, but a discussion of why “such methods often focus on finding the optimal permutation instead of learning a distribution over the finite symmetric group” and what the tradeoffs are would be helpful. 

The experiments also show stronger performance for longer sequence lengths, but the quadratic scaling with longer sequence lengths remains an open direction of improvement.

### Questions
1. As discussed in the Weaknesses section, what exactly is the motivation of using diffusion model for these problems, if ultimately only a single learned permutation is required per input? This is my primary question. 
2. For the right choice of parameters, can the reverse processes actually represent the exactly correct distributions induced by the corresponding forward diffusion process?
3. One minor point of confusion was that the abstract claims to learn a distribution over $S_n$, but the concrete objects that are dealt with are ordered sets of objects (stored in an $n$ by $d$ matrix). Would it be accurate to refer to this method as *conditional* diffusion? If not, how could the architectures best be modified to output a distribution over raw permutation matrices? 
4. As noted on line 154, $\mathcal{S}$ does not change across steps — why enforce this for diffusion models? Does this make something easier? Is it potentially restrictive in terms of what distributions can be represented after a given number of steps?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper explores a novel problem: learning probability distributions over finite symmetric groups. As an example, the problem can be thought of as learning to sort, with important differences:

- instead of finding just the most optimal permutation, the focus is on learning a *distribution* over all possible rankings, so that rankings "closer" to the optimal permutation are more likely to be generated.
- the problem formulation is general enough to cover rankings over any finite group of elements and not just a set of $n$ integers as long as one trains the algorithm using appropriate data (for instance, pictures of numbers instead of just numbers). 

The authors propose *SymmetricDiffusers*, a discrete diffusion model (with a transformer-based architecture in this case) trained to recover the target permutation in several steps after the original (target permutation) is converted into noise over a number of steps. This decomposition of the recovery process eases the otherwise very difficult problem of learning to directly come up with the optimal permutation out of $n!$ possible states.

With this context, the authors' study reveals several insights into potentially best practices with regard to the training process, *e.g.,* choice of the forward shuffling method (riffle shuffle because of its fast mixing time), and when it might be feasible to merge steps during the denoising process. The authors validate their findings via state-of-the-art results on three benchmarks: MNIST sorting, jigsaw puzzles, and the Travelling Salesman Problem.

### Strengths
1. The style of writing is extremely clear and structured. 
2. The paper makes a wealth of interesting contributions: introducing a novel perspective on an important problem that is currently underexplored in the ML community; proposing a method to solve said problem; revealing insights that will help further research; and finally, validating their method on three benchmarks. The authors also share their code. The general nature of the problem means that the findings here can potentially open up a whole new set of possibilities.

### Weaknesses
I don't see obvious weaknesses. But, as the authors also acknowledge (in the conclusion and Appendix G), there is potential for improving scalability (w.r.t. $n$) and possibly extending the method to finite groups beyond $S_n$.

**(Nit: typos)**
- Abstract (line 009): groups --> group?
- line 472: performances --> performance?

### Questions
1. Have the authors considered evaluating OOD performance (e.g., feeding colored, or otherwise font-shifted MNIST into a model that was trained on grayscale images) ? Do they anticipate a drop in performance in that setting?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the important question of sampling from the finite symmetric group $S_n$ via diffusion models. This is structurally different from prior works on diffusion models which concentrate on sampling from product spaces (i.e, sampling without replacement). The authors clearly introduce various noising Markov chains for sampling a uniform distribution over $S_n$ and show how to parametrize the forward and reverse processes. This is the main technical contribution of the paper. The training loss is then based the variational lower bound of D3PM (Austin et al). The paper achieves strong performance in solving jigsaw puzzles of MNIST and CIFAR 10, sorting numbers from MNIST and solving TSP problems.

### Strengths
The paper is clearly written and the Markov chains used to obtain uniformly random permutations are clearly surveyed. The construction of the parameterization of the reverse process and the loss function is nice and the algorithm outperforms existing methods in the empirical tasks.

### Weaknesses
1. Experiments are very small scale, comprising of sorting 4 digit MNIST, solving 20 node TSPs and solving jigsaw puzzles of CIFAR-10 data. These tasks, while demonstrating the method's potential, do not fully explore the scalability of the proposed approach. The MNIST sorting task, for instance, only uses 4 digits, and the TSP is limited to 20 nodes, which are not particularly challenging instances for modern combinatorial optimization methods. The jigsaw puzzle experiments on CIFAR-10 also use a relatively small image size, limiting the complexity of the permutation space explored.

2. There is no substantive theoretical contribution other than introducing the parametrization for the reverse processes. While the parameterization is novel, the paper lacks deeper theoretical analysis of the proposed diffusion process. For example, convergence properties of the Markov chains, or the expressiveness of the reverse process parameterization, are not rigorously analyzed. The paper would benefit from a theoretical analysis of the proposed approach.

3. The reverse process for random transposition is not very expressive. Suppose the reverse transposition is $(1,2)$ with probability $0.5$ and $(2,3)$ with probability $0.5$. This simple distribution cannot be expressed using the model. This limitation raises concerns about the ability of the model to capture complex distributions over the symmetric group. The use of a limited set of transpositions may restrict the model's ability to learn arbitrary permutation distributions.

4. Note that $S_n \subseteq [n]^n$. If the input data comprises of only permutations, then the network should learn to sample from a distribution whose samples are permutations and the standard framework of diffusion models applies. This simple baseline has not been considered. The paper does not adequately justify why standard diffusion models, which operate on the product space $[n]^n$, cannot be adapted for permutation learning. It is unclear why the constraint of sampling permutations cannot be enforced within the standard framework, especially given that the output space is known to be the symmetric group. 

[Q related to 4] The authors also mention that representing a transition matrix over $S_n$ requires $n!\times n!$ sized matrix. However, the authors themselves give a succinct description/ representation of the forward transition matrix in the paper. The authors should elaborate why it is not possible to use this representation algorithmically.

**Minor:**
In proposition 1, should it be changed to "the GPL distribution can represent a delta distributions in the limit" instead of "exactly"?

### Questions
Address the points raised in the weaknesses section.

### Soundness
3

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
3

### Summary
This authors proposes a diffusion framework that learns a distribution over permutations.
They propose a set of different reverse and forward diffusion processes to realize this goal.
They validate their approach on various different experiments such as TSP, four-digit MNIST, CIFAR and noisy MNIST.

### Strengths
1. The paper presents an interesting approach with mostly clear writing
2. Several innovative reverse and forward processes are proposed

### Weaknesses
1. The claim of state-of-the-art performance on TSP-20 appears too bold given the limited scope. The experimental results on TSP-20 are not compelling enough to justify such a claim, especially considering that TSP-20 is a very small instance size and many specialized algorithms exist for solving TSPs optimally or near-optimally. The paper should provide a more thorough comparison against existing TSP solvers, and it should be made clear that this is not a method specifically designed for TSP, but rather a general permutation learning method.
2. Several experimental details lack sufficient clarity (see Questions). The description of the forward and reverse diffusion processes is somewhat abstract, and it is not immediately clear how these processes are implemented in practice. For example, the exact parameterization of the transition probabilities is not specified, and it is not clear how the neural network is used to parameterize the reverse process. The paper would benefit from a more detailed explanation of the implementation details, including the specific architectures and hyperparameters used in the experiments.

### Questions
1. How do the proposed reverse and forward processes compare to naive discrete denoising diffusion models?
What is the difference between your method and other differentiable sorting baselines in Tab. 1?

2. What is the sequence length $n$ in the four-digit MNIST dataset?

3. Why are experiments limited to TSP-20 instances rather than including larger TSP instances? TSP-20 is considered a very small problem size. This experiment is the most interesting to me and it would be interesting to see how this method performs on larger TSP instances. Can you provide an additional comparison on TSP-100?

4. Can your method be combined with the framework proposed in [1] to solve TSP using diffusion models without requiring data from classical solvers?



## References
[1] Sanokowski, Sebastian, Sepp Hochreiter, and Sebastian Lehner. "A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization." Forty-First International Conference on Machine Learning.

### Soundness
3

### Presentation
3

### Contribution
3
