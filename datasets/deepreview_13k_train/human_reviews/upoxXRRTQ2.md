# The impact of allocation strategies in subset learning on the expressive power of neural networks

- Decision: Accept
- Scores: 3, 3, 6, 8

## Abstract
In traditional machine learning, models are defined by a set of parameters, which are optimized to perform specific tasks. In neural networks, these parameters correspond to the synaptic weights. However, in reality, it is often infeasible to control or update all weights. This challenge is not limited to artificial networks but extends to biological networks, such as the brain, where the extent of distributed synaptic weight modification during learning remains unclear. Motivated by these insights, we theoretically investigate how different allocations of a fixed number of learnable weights influence the capacity of neural networks. Using a teacher-student setup, we introduce a benchmark to quantify the expressivity associated with each allocation. We establish conditions under which allocations have \`maximal' or \`minimal' expressive power in linear recurrent neural networks and linear multi-layer feedforward networks. For suboptimal allocations, we propose heuristic principles to estimate their expressivity. These principles extend to shallow ReLU networks as well. Finally, we validate our theoretical findings with empirical experiments. Our results emphasize the critical role of strategically distributing learnable weights across the network, showing that a more widespread allocation generally enhances the network’s expressive power.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the conditions under which 'allocations' have maximal or minimal expressive power in linear RNN and linear MLPs.

### Strengths
Originality: I think allocation is an interesting concept though it seems to significantly overlap with the concept of subnetwork in lottery ticket hypothesis. 

Clarity: The paper is clearly written.

### Weaknesses
Quality: Studying expressivity of RNNs/MLPs from the perspective of linear solvable equations require strong assumptions such as 'the distribution $\mathcal X$ is such that any drawn square matrix is invertible' (l197) and I'm having trouble extracting insights from the theorems. The assumption about the invertibility of drawn square matrices is particularly concerning, as it is not generally true for arbitrary distributions and significantly limits the applicability of the theoretical results. Furthermore, the paper does not adequately address the implications of this assumption on the practical relevance of the findings. The theorems, while mathematically rigorous, lack clear connections to real-world scenarios, making it difficult to understand their practical significance. The paper would benefit from a more detailed discussion of how these theoretical results translate to actual neural network training and performance.

Significance: Increasing the percentage of learnable weights leads to more expressivity seems trivial to me (maybe there are insights I'm not seeing from the paper?) so I'm not quite sure what we can learn from the submission. The core idea of exploring the impact of weight allocation on expressivity, while interesting, seems to lack novelty. The paper does not sufficiently differentiate itself from existing work on network pruning and resource allocation. The connection to the lottery ticket hypothesis is not adequately addressed, and the paper needs to clarify its unique contribution beyond simply varying the distribution of learnable weights. The lack of clear, non-trivial insights makes it difficult to assess the overall significance of the work.

### Questions
a. Could the authors comment on the practical implications of the theorems? 

b. L147 is joint not conditional? If so notation is confusing.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper develops a theoretical framework for analyzing the expressive power of neural networks when only allowing a subset of the network to learn. The authors focus on a student-teacher setup and defines expressivity as the likelihood that the student can replicate the teacher’s outputs. Using this metric, this work analyzed linear RNNs and deep linear feedforward networks, and evaluated the expressive power of different allocation strategies, then extended their analysis to one-layer ReLU feedforward networks.

### Strengths
The paper presents several theoretical results about the expressive power of linear networks when allowing a subset of the network to learn, and concludes that spreading the learnable weights in different parts of the network allows for stronger expressive power.

### Weaknesses
1.	There are many ways to evaluate allocation strategies, including generalization performance, capabilities of transfer learning and continual learning, etc. These are the interesting problems that the authors used to motivate their work. However, this paper particularly focuses on how allocation strategy affects the expressivity of a network, in a very specific setting, limiting the scope and potential insights that could be obtained from this work.
2.	The result of the work is restricted to a student-teacher framework in the sense that the central definition of the match probability is defined based on a student-teacher framework, where the student and the teacher have matching architectures, making it difficult to extend the results to real-world applications even heuristically. The numerical results shown in this paper is also limited to this synthetic task only.
3.	Various assumptions are dispersed and showed up in various places within the text, it would be better if the authors could explicitly list their assumptions when stating the theorems.
4.	I did not check all proofs carefully but multiple proofs in this paper is written in a very informal way, making it difficult to judge the validity of the proofs.

### Questions
1.	Both the student and the teacher weights are drawn from i.i.d. Gaussian, have you considered correlated weights in the teacher, or introducing structures into the teacher weights? 
2.	The central result that it is better to allocate the learnable weights throughout the network. Is this consistent with existing findings about learning in the brain?
3.	When stating that “the probability of finding at least one solution increases with the number of polynomials”, does the degree of the polynomials play a role?
4.	In the proof of theorem B1, do you assume that W is diagonalizable? The sentence “the eigenvector xxx is a space” does not make sense to me. Furthermore, I do not see why it is important to prevent the network from being degenerate, it is still a valid function of the input sequence, and it’s simply that the degree of freedom is less than the amount of effective linear weights.

### Soundness
2

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
4

### Summary
This paper provides a theoretical investigation into the distribution of learnable weights in neural networks, drawing inspiration from brain mechanisms. The study measures network expressivity as a function of these learnable weights, examining various network architectures and validating the theory through experiments.

### Strengths
Congratulations on your submission to ICLR! I commend the authors on producing this great piece of research. Below is my detailed review of the work:

**Originality**
This paper introduces a theoretical framework for analyzing network expressivity as a function of learnable weight allocation. Its originality lies in drawing parallels with brain mechanisms and adopting a fresh theoretical approach.

**Quality**
The paper demonstrates high quality with well-substantiated theoretical findings that are clearly explained and motivated. Key strengths include:
- Thorough and detailed theoretical results, effectively show that predictions from smaller models generalize well to non-linear, shallow ReLU architectures.
- Theoretical analysis is rigorously structured, adding robustness to the findings.
- The mathematical derivations appear accurate and sound.

**Clarity**
The paper is well-organized and accessible. 

- The use of a simplified linear network model as a toy example helps to build intuition, significantly enhancing readability. 
- The figures are clear, informative, and effectively support the main content.

**Significance**
This work is a valuable contribution to the machine learning research community, especially in deepening our understanding of model expressivity as a function of trainable weights in the context of increasing training costs. Additionally, the proposed theoretical framework may offer valuable insights for the neuroscience community.

### Weaknesses
 **Originality**
No notable weaknesses in originality.

**Quality:**
The paper is of high quality, yet there are areas where further clarity and detail could strengthen its impact:

- The paper would benefit from a more explicit discussion of its limitations. While valuable, the theoretical approach may not fully capture some empirical phenomena seen in practical neural networks. Highlighting these potential divergences between theory and real-world observations would add useful nuance.
- A clearer connection to applications in neuroscience would enhance the paper’s relevance to that field.

**Clarity**
The clarity of the paper is generally high but could be improved in specific areas:

- An introductory figure would be helpful, particularly for readers unfamiliar with the topic. For instance, a visual summary of the student-teacher setup could make the content more accessible.
- Including a discussion in the introduction on the growing computational demands—now requiring substantial resources—would add timely context to the study.
- Strengthening the link between neural networks and brain mechanisms would clarify the relevance of the approach.
- Developing Theorem 3.3 further, potentially in the appendix, would also improve clarity.

**Significance**
The significance of the study could be enhanced with a few adjustments:
- The benchmarks used primarily involve toy models, which may limit the generalizability of the findings. Extending the analysis to larger models could increase the impact and relevance of the results.

### Questions
-  Are there any constraints preventing from running the experiments with gradient descent? Is it correct to think that if you did you could have access to results with larger networks? 
- Do you have any intuition on how these insights might scale to more complex networks? Specifically, if larger models contain an increasing number of polynomials increases the probability to find a solution , does this imply that weight distribution becomes less significant, given that the transition would be so abrupt that the network would almost never (with a probability tending to zero) have no solution or expressivity zero ? 
- (This may be outside the intended scope, but I’m curious.) I understand that the approach abstracts away the specifics of the learning algorithm. However, I’m interested in how your findings might depend on the network’s initialization under a particular learning algorithm (e.g., the scale and relative scaling of layers). Given that different initializations can influence the learning rates of certain weights more than others—effectively controlling which parts of the network learn more actively—how does the network’s expressivity vary under these conditions?

I hope this review is helpful for the further development of the paper. I encourage the author to continue this research and incorporate the feedback provided.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors investigate the capacity of neural networks under constrained conditions where only a fixed number of weights are plastic and can be changed. The authors present theoretical work and then relate the theory to empirical simulations in simple networks. 
This work is quite interesting in that it forces us to think that not all weights are equal, that not all weights are needed, and that astute ways of choosing which weights to change can have a large impact in the capacity and efficacy of a neural network.

### Strengths
This work introduces an interesting question about the possibility to modify only certain weights in a network and ask how the choice of plastic weights impacts neural network capacity.
There has not been much work along these lines. Perhaps one related idea relates to continual learning. Upon learning new things, it may be useful to strategically decide which weights to change more. One instantiation of this is Kirkpatrick et al PNAS 2017 (the authors cite other work in this direction as well).
The work presents both theory and empirical simulations. 
The work introduces a benchmark that would be useful for the field to compare different potential mechanisms to allocate learnable parameters.

### Weaknesses
The abstract states that “biological systems like the brain where evidence suggests that only a subset of synaptic weights are modified during learning”. This is a grandiose claim that is not substantiated by any references. I strongly suggest that they remove this claim. Otherwise, the authors should provide compelling evidence about this statement. The introduction provides a better assessment: “the scale of this process in the brain is unclear”. 
The experiments presented are based on rather simple NNs. It is not clear how the conclusions extrapolate to more complex NNs. For instance, the networks used seem to be fully connected, and it is not clear how the results would translate to convolutional networks or other architectures with more structured connectivity. Furthermore, the datasets used are also quite simple. It would be useful to see how these results translate to more complex datasets. But this point does not distract from the beauty of the work presented here.

### Questions
The potential connections between the work presented here and weight protection strategies in continual learning is probably worth exploring further (though this is not a requirement by any means for the current work).

### Soundness
4

### Presentation
4

### Contribution
4
