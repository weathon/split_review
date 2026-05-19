### Summary

This paper considers a variant of the universal approximation problem for ReLU networks.  In the standard setting, one is given a continuous function $f^*$ defined on some compact domain, and a network architecture (e.g., number of hidden units, number of layers, etc.), and one wishes to find weights for the network that achieve a small error in some norm (typically $L^\infty$ or $L^2$).  Here, the authors consider a variant in which the weights of the network are not arbitrary, but instead are drawn from a fixed set of values, and only the *permutation* of those weights is allowed to change.  In particular, they focus on the case of a one-hidden-layer ReLU network, and consider two settings: (1) where the fixed weights are $\pm b_i$ for some fixed set of biases $\{b_i\}$, and (2) where the fixed weights are $\pm p_i$ for some uniform random set of biases $\{p_i\}$.  In both settings, they show that one can approximate any continuous function on the interval $[0,1]$ to arbitrary precision using a network with ReLU activations.  The key technical contribution is a construction that allows them to approximate step functions using a ReLU network with fixed weights.  The authors also provide some numerical simulations that demonstrate the effectiveness of their approach.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The main strength of the paper is that it considers an interesting variant of the universal approximation problem that, to my knowledge, has not been studied before.  The authors provide a simple and elegant construction that allows them to approximate step functions, which they then use to show that one can approximate any continuous function on the interval $[0,1]$ to arbitrary precision.  The paper is also well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is that the setting they consider is somewhat artificial and does not seem to have any practical applications.  In particular, it is not clear why one would want to restrict the weights of a neural network to a fixed set of values, and only allow the permutation of those weights to change.  This seems like a very restrictive constraint, and it is not clear if it is worth studying.  While the authors mention potential applications in hardware implementation, these seem quite far-fetched and not well-motivated.  The numerical simulations are also quite limited, and it is not clear if the results generalize to other settings.  Furthermore, the analysis is specific to ReLU activations, and it is not clear if the results hold for other activation functions.  The authors also do not address the question of how the width of the network scales with the desired approximation accuracy, which is a crucial aspect of universal approximation results.  Finally, the paper does not consider multi-layer networks, which are more commonly used in practice.

### Suggestions

The paper would be significantly strengthened by a more thorough discussion of the practical implications of the proposed approach. While the authors mention hardware implementations, they should provide more concrete examples and explain why permutation-based training is particularly well-suited for these applications. For instance, they could discuss specific hardware architectures where weight permutation is easier to implement than arbitrary weight updates, and provide a quantitative analysis of the potential benefits in terms of energy efficiency or computational speed. Furthermore, it would be beneficial to explore the limitations of the proposed approach in more detail. For example, how does the approximation error scale with the number of hidden units, and how does this compare to standard universal approximation results? It would also be useful to investigate the robustness of the approach to different choices of fixed weights and to explore whether there are any optimal strategies for selecting these weights. 

To address the limitation of the analysis being specific to ReLU activations, the authors should investigate whether their results can be extended to other commonly used activation functions, such as sigmoid or tanh. This would involve analyzing the approximation properties of ReLU networks with fixed weights and different activation functions, and potentially developing new techniques to handle the non-linearity of these functions. Furthermore, the authors should consider the implications of their approach for deeper networks. While their current analysis is limited to single-hidden-layer networks, it would be valuable to explore whether similar results can be obtained for multi-layer networks. This could involve developing new techniques for composing the approximation properties of individual layers, and potentially requiring more complex network architectures to achieve universal approximation. 

Finally, the authors should provide a more detailed analysis of the numerical simulations. While the current simulations demonstrate the effectiveness of their approach, they are quite limited in scope. It would be beneficial to explore a wider range of target functions, network architectures, and training parameters. In particular, the authors should investigate how the performance of their approach varies with the number of hidden units, the choice of fixed weights, and the training algorithm. They should also compare their results to standard training methods, such as backpropagation, to quantify the trade-offs between the two approaches. This would provide a more comprehensive understanding of the strengths and limitations of their approach and help to identify potential areas for future research.

### Questions

1. Do the results extend to multi-layer networks?  My guess is that they do, but that one would need to use more complicated networks and the analysis would be more involved.

2. What about other activation functions?  Can one obtain similar results for sigmoid or tanh activations?  I would guess that the analysis would be more difficult in this case, since one needs to use the particular homogeneity property of the ReLU activation.

3. How does the width of the network scale with the desired approximation accuracy?  This is a crucial aspect of universal approximation results, and it is not clear from the paper how this is addressed.

4. Can you provide more concrete examples of practical applications for your approach?  The hardware implementation examples seem quite far-fetched, and it would be helpful to have more realistic scenarios where permutation-based training is advantageous.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
