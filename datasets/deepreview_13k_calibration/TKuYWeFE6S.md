# PolyNet: Learning Diverse Solution Strategies for Neural Combinatorial Optimization

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Reinforcement learning-based methods for constructing solutions to combinatorial optimization problems are rapidly approaching the performance of human-designed algorithms. To further narrow the gap, learning-based approaches must efficiently explore the solution space during the search process. Recent approaches artificially increase exploration by enforcing diverse solution generation through handcrafted rules, however, these rules can impair solution quality and are difficult to design for more complex problems.  In this paper, we introduce PolyNet, an approach for improving exploration of the solution space by learning complementary solution strategies. In contrast to other works, PolyNet uses only a single-decoder and a training schema that does not enforce diverse solution generation through handcrafted rules. We evaluate PolyNet on four combinatorial optimization problems and observe that the implicit diversity mechanism allows PolyNet to find better solutions than approaches the explicitly enforce diverse solution generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
PolyNet introduces a novel approach to enhancing exploration in neural combinatorial optimization (CO). Unlike traditional methods that enforce diversity via handcrafted rules, PolyNet employs a single-decoder model that inherently learns multiple strategies, facilitating more effective search and solution quality. The paper demonstrates PolyNet's superior performance across several benchmark CO problems, such as TSP, CVRP, and CVRPTW, outperforming state-of-the-art methods both in speed and solution quality.

### Strengths
- The use of a single-decoder model that can learn multiple strategies simplifies the training pipeline and reduces computational overhead compared to multi-decoder systems.

- The model's training schema, which emphasizes inherent diversity, makes it adaptable to various CO problems beyond simple routing tasks.

- The authors provide useful insights into the impact of their design choices, such as the effectiveness of not forcing diverse first moves.

### Weaknesses
 - While starting from pre-trained models boosts training efficiency, this reliance could limit applicability in cases where such pre-training is not feasible or available.

- While PolyNet demonstrates strong results in routing tasks, its effectiveness in other CO problem domains (e.g., scheduling or knapsack) has not been deeply explored.

- The paper does not discuss how PolyNet handles instances where input data is noisy or incomplete, a common occurrence in practical applications.

- The impact of different hyperparameter settings on model performance is not fully analyzed, which could be critical for real-world applications requiring fine-tuning.

### Questions
1. How would PolyNet perform when extended to non-routing CO problems, such as job scheduling or knapsack problems?

2. Can you elaborate on the potential methods for improving PolyNet’s scalability to handle larger problem instances?

3. What are the specific limitations of PolyNet’s inherent diversity mechanism when applied to problem instances with different statistical properties?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
To facilitate learning complementary solution strategies, this paper avoids forcing the initial action step. Instead, it enhances exploration by embedding it into the decoder as a bit vector. While experiments demonstrate performance improvements, the approach lacks novelty.

### Strengths
1. The paper is well-structured, presenting its content in a clear manner.
2. A wide range of experiments are conducted to assess solution diversity.

### Weaknesses
1. The method of inserting additional vectors in the decoder is very similar to the idea of COMPASS [1], lacking sufficient innovation to significantly advance the field.
2. The description of bit vectors is minimal, and there is no detailed analysis of how varying vector representations might impact performance. Specifically, the paper does not explore the impact of different bit vector lengths or encoding schemes on the learned solution strategies. The choice of a binary representation over other discrete encodings, such as one-hot encoding, is not justified with empirical evidence or theoretical analysis.
3. The fairness of comparing COMPASS with PolyNet+EAS in an experimental context is questionable. The paper does not adequately address the inherent differences in the search mechanisms of these methods, making a direct comparison problematic. The computational resources and optimization strategies employed by COMPASS, which uses CMA-ES, are fundamentally different from those used by PolyNet+EAS, which relies on a simpler parameter update.
4. In [1], there is a big difference between COMPASS and EAS runtimes, but in this paper, PolyNet+EAS time is similar to COMPASS, please specify the reason.

### Questions
1. The advantages of using bit vectors as supplementary vectors for insertion should be thoroughly analyzed, particularly in comparison to previous continuous potential vectors.
2. In the experimental section, a more comprehensive explanation and analysis of performance concerning runtime are necessary.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study, grounded in the POMO framework, introduces a straightforward yet impactful component: PolyNet. The component takes as input the concatenation of a set of binary vectors and the output from the decoder's multi-head attention layers. After processing through a series of linear layers and activation functions, the output is directly added to the output of the decoder's multi-head attention layers, thereby directly influencing the probability distribution of node selection. Analysis from the paper indicates that the newly added module helps to enhance solution diversity without the need for mandatory starting point selection as in POMO. Additionally, the authors assert that PolyNet can be integrated with EAS, and significant performance improvements can be achieved by updating only the newly added modules.

### Strengths
1. The authors have clearly articulated the framework and implementation of the method, with smooth writing.
2. The tables and figures are presented clearly, and the experiments are comprehensive.
3. Testing PolyNet on various combinatorial optimization problems (TSP, CVRP, CVRPTW, FFSP) demonstrates the good generality of the method.
4. (As claimed by the authors) their method performs exceptionally well on instances of scale 100, 200, and 300 (Tables 1-3).

### Weaknesses
PolyNet can enhance the diversity and optimality of solution sets, but the authors seem to lack an in-depth discussion on the principles behind the additional layers of PolyNet. This leaves me somewhat puzzled. The training process described in the paper adopts a method similar to Poppy, and the added linear layers, activation functions, and residual connections are common components in the Transformer architecture. The motivation for significant improvements by merely concatenating an additional binary array is not very clear. Specifically, the paper does not provide a clear explanation of how the binary vector interacts with the decoder's attention outputs through the linear layers and activation functions to achieve the observed diversity and optimality gains. The lack of ablation studies on the specific architecture of the added layers further compounds this issue. It is unclear if the number of layers, the specific activation functions, or the dimensionality of the hidden layers are critical to the performance of PolyNet, or if they were chosen arbitrarily. Furthermore, the paper does not explore the sensitivity of the method to the size of the binary vector, which could be a critical hyperparameter.

### Questions
1. What is the design motivation behind the additional concatenated binary array $v$? Why can it significantly enhance diversity and optimality? If it were replaced with a column of random numbers, or if random perturbations were directly added to the input of the "added layer," would the same effect be achieved?

2. In Appendix Figure 6, a comparison is made between "PolyNet w/o Added Layers" and "POMO with Added Layers." It would be better if a "POMO" without additional additions could be included for comparison. My question is, why does "PolyNet w/o Added Layers" perform significantly better than "POMO with Added Layers"? Is it due to differences in training methods? If so, it would be best to compare POMO with the new training method.

3. Which contributes more significantly, the training method or the new structure?

4. In combinatorial optimization, there is a class of problems specifically focused on diversity optimization, where multiple solutions need to be found simultaneously. Relevant papers include “Computing Diverse Shortest Paths Efficiently: A Theoretical and Experimental Study” and “A Niching Memetic Algorithm for Multi-Solution Traveling Salesman Problem.” The work presented in this paper seems particularly suited for such scenarios, and I hope to see more discussion on this topic.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes PolyNet, which aims to reinforce the exploration training and testing of Nueral CO methods. In particular, a representive NCO method POMO is used as the playground in this paper. The idea behind this paper is quite simple: adding a neural network module which contains MLP layers besides the  main structure of POMO, termed PolyNet layer. PolyNet layer  provide exploration ability by letting its input as the node embeddings and a binary context coding. Using different binary context codings, the output of PolyNet layer add different information to the output of POMO hidden layers. By training on moderate instances, PolyNet show state-of-the-art performance on several CO problems (#nodes < 300). Besides, the authors demonstrate the exploration ability of PolyNet during the training and testing is different from the common practice in existing works: forcing diverse first action selection.

### Strengths
The idea behind PolyNet is simple yet effective. The methodology part is easy-to-follow. The experimental results for performance comparison on different CO problems are solid and convincing. The ablation studies that explain the solution diversity in PolyNet are with good demonstration.

### Weaknesses
There are two major weaknesses:

a) Related works are not well-organized. As a important part to let readers aware the background, the motivation and the priority of this paper, Neural CO methods should be organized in a way that these points are clearly outlined. The current organization merely lists existing methods without providing a critical analysis of their limitations or how this work addresses them. The reader is left to infer the gaps in the literature, rather than having them explicitly stated and justified. This makes it difficult to understand the specific niche that PolyNet is attempting to fill and why it is a necessary contribution.

b) Fow now, the scale of the CO problems PolyNet could address is no more than 300, which makes me curious about the performance of PolyNet on larger instances (#nodes > > 300). From my angle, the exploration ability is especially needed in large scale problems. The lack of scalability to larger problem instances significantly limits the practical applicability of the proposed method. While the performance on smaller instances is promising, many real-world combinatorial optimization problems involve significantly larger problem sizes, and it is unclear how PolyNet would perform in such scenarios. The paper does not address the computational complexity of the method, which is a crucial factor when dealing with larger instances.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
