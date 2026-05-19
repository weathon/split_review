### Summary

This paper proposes using an evolutionary algorithm for conducting adversarial attacks on graph-based machine learning models. The authors argue that the evolutionary approach overcomes some of the limitations of gradient-based attacks, and they demonstrate the effectiveness of the proposed attack on several benchmark datasets.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

* The paper proposes a novel approach for adversarial attack on graph-based machine learning models. 
* The approach does not require gradients or a differentiable loss function, which could have significant implications for black-box attacks. 
* The authors demonstrate that the proposed attack can be effective on several benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

 * The paper is not well-written and could benefit from significant revision. The problem formulation and the description of the proposed method are unclear in several places, making it difficult to understand the technical details of the approach. For example, the encoding of the perturbations and the fitness function are not clearly explained.
* The experimental evaluation is limited and does not provide sufficient evidence to support the claims made in the paper. The authors only evaluate the proposed attack on a small number of benchmark datasets and do not compare it to any existing baselines. The lack of comparison to other attack methods, especially those that are black-box, makes it difficult to assess the true value of the proposed approach.
* The paper does not provide any theoretical analysis of the proposed method, such as convergence guarantees or bounds on the approximation error. This makes it difficult to understand the theoretical properties of the approach and its limitations. For instance, it is unclear how the evolutionary algorithm's parameters affect the quality of the solution and how the method scales with the size of the graph.

### Suggestions

The paper needs a significant overhaul to improve its clarity and technical depth. First, the authors should provide a more detailed explanation of the encoding scheme used for representing graph perturbations. It is crucial to clarify how the edges are represented, how the perturbations are applied, and how the method ensures that the perturbed graph remains valid. For instance, are the edges represented as a binary vector, or is there a more complex encoding? How does the method handle the removal of edges, and how does it ensure that the graph remains connected (if that is a requirement)? Furthermore, the fitness function needs to be clearly defined, including the specific loss function used and how it is calculated for a given perturbed graph. The authors should also clarify how the method handles the trade-off between attack effectiveness and perturbation magnitude. Providing concrete examples of how the encoding and fitness function work in practice would greatly enhance the reader's understanding.

Second, the experimental evaluation needs to be significantly expanded to provide more convincing evidence of the proposed method's effectiveness. The authors should compare their method against a wider range of existing adversarial attack methods, including both gradient-based and black-box approaches. It is important to evaluate the method on a more diverse set of datasets, including larger and more complex graphs. The evaluation should also include a thorough analysis of the method's performance under different attack budgets and different choices of evolutionary algorithm parameters. Furthermore, the authors should investigate the transferability of the proposed attack, i.e., whether perturbations generated for one model can also be effective against other models. This would provide a more comprehensive understanding of the method's strengths and weaknesses. The authors should also consider reporting the computational cost of the proposed method, as this is an important factor in practical applications.

Finally, the paper would benefit from a more in-depth discussion of the theoretical properties of the proposed method. While a full theoretical analysis may be challenging, the authors should provide some insights into the convergence behavior of the evolutionary algorithm and how its parameters affect the quality of the solution. It would be useful to discuss the method's limitations and potential failure cases. For example, under what conditions might the method fail to find effective perturbations? How does the method scale with the size of the graph, and what are the computational bottlenecks? Addressing these questions would provide a more complete picture of the proposed method and its applicability. The authors should also consider discussing the method's robustness to different types of defenses, such as adversarial training.

### Questions

1. Can the authors provide more details about the encoding scheme used for representing graph perturbations? How does this encoding ensure that the perturbed graph remains valid? 
2. How does the proposed method compare to existing black-box adversarial attack methods for graphs? 
3. What is the computational complexity of the proposed method, and how does it scale with the size of the graph? 
4. Can the authors provide any theoretical guarantees about the convergence or optimality of the proposed method? 
5. How does the proposed method handle the trade-off between attack effectiveness and perturbation magnitude?

### Rating

3

### Confidence

4

**********
