# Training Large Neural Networks With Low-Dimensional Error Feedback

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 3, 8, 5

## Abstract
Training deep neural networks typically relies on backpropagating high-dimensional error signals—a computationally intensive process with little evidence supporting its implementation in the brain. However, since most tasks involve low-dimensional outputs, we propose that low-dimensional error signals may suffice for effective learning. To test this hypothesis, we introduce a novel local learning rule based on Feedback Alignment that leverages indirect, low-dimensional error feedback to train large networks. Our method decouples the backward pass from the forward pass, enabling precise control over error signal dimensionality while maintaining high-dimensional representations. We begin with a detailed theoretical derivation for linear networks, which forms the foundation of our learning framework, and extend our approach to nonlinear and convolutional architectures. Remarkably, we demonstrate that even minimal error dimensionality—on the order of the task dimensionality—can achieve performance matching that of traditional backpropagation. Furthermore, our rule enables efficient training of convolutional networks, which have previously been resistant to Feedback Alignment methods, with minimal error. This breakthrough not only paves the way towards more biologically accurate models of learning but also challenges the conventional reliance on high-dimensional gradient signals in neural network training. Our findings suggest that low-dimensional error signals can be as effective as high-dimensional ones, prompting a reevaluation of gradient-based learning in high-dimensional systems. Ultimately, our work offers a fresh perspective on neural network optimization and contributes to understanding learning mechanisms in both artificial and biological systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript focuses on developing a feedback alignment method that uses low-rank gradient approximation matrix, B, in order, to show that low-dimensionality error is sufficient for learning.

### Strengths
- Theoretical extensions of the Kolen-Pollack algorithm are very clear and easy to follow. Theoretical contributions were validated well on simulations in linear models.
- Experiments on CIFAR-10 with different numbers of classes seem interesting given the dimensionality match between the number of classes and the rank of the matrix B.
- The experiments on the receptive fields show an interesting relationship between features learned by the model and the rank of the gradient.

### Weaknesses
 - Given the difficulty of FA to match higher class datasets (as shown by Lillicrap et al), the paper would benefit by doing experiments in ImageNet as in Akrout et al, 2019. Similarly to the CIFAR100 experiments, the rank of the B follows the number of categories in ImageNet. Would it do it on other datasets such as SVHN?
- Novelty of low-rank gradients. There has been extensive work on the implicit regularizarion literature (see examples below), that show that gradient descent is regularized to change the weights of the model in a low dimensional space:
   - Ma, C., & Ying, L. (2021). On linear stability of sgd and input-smoothness of neural networks. Advances in Neural Information Processing Systems, 34, 16805-16817.
   - Feng, Y., & Tu, Y. (2021). The inverse variance–flatness relation in stochastic gradient descent is critical for finding flat minima. Proceedings of the National Academy of Sciences, 118(9), e2015617118.

### Questions
Question:

- Can you elaborate here and in the manuscript about the relationship between the Lindsay et al 2019 results and yours. In the manuscript you indicate “We hypothesize that these effects are due to constraints on the error signal reaching the retina, rather than the feedforward bottlenecks themselves.”. However, the bottleneck in the feedforward network can impose a lower rank in the feedback due to the different structure of W. There has been some work on the relationship of these properties in the implicit regularization literature, specially relating SGD with convolutional kernel learning. It would be good for them to be included in the discussion of these results because it seems like architecture and gradient structure are highly correlated. 
   - Gunasekar, S., Lee, J. D., Soudry, D., & Srebro, N. (2018). Implicit bias of gradient descent on linear convolutional networks. Advances in neural information processing systems, 31.
   - Ortega Caro, J., Ju, Y., Pyle, R., Dey, S., Brendel, W., Anselmi, F., & Patel, A. B. Translational Symmetry in Convolutions with Localized Kernels Causes an Implicit Bias towards High Frequency Adversarial Examples. Frontiers in Computational Neuroscience, 18, 1387077.

Suggestions:

- Given the references above, It would be good to include these references because there are indications that SGD already works in a low dimensional space. In addition,  change the paragraph in the discussion about rethinking of gradient descent dynamics due to these references.

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
This paper introduces Restricted Adaptive Feedback (RAF), a learning method inspired by Feedback Alignment (FA) using low-dimensional error feedback to train neural networks. 
By adopting a factorized version of Feedback Alignment with low-rank matrices, the need for high-dimensional error signals is challenged.
RAF achieves performance comparable to backpropagation in some settings, offering a low-dimensional biologically plausible training principle.

### Strengths
1. The subject of biological alternatives to back-propagation (BP) is a really interesting topic.

2. The authors provide good theoretical foundation of their method.

3. The study shows that error dimensionality shapes receptive fields which is interesting and provides insights on the emergence of representations in both artificial and biological systems.

4. The empirical study shows competitive performance with reduced error signal dimensionality, which could reduce computational costs without sacrificing accuracy.

5. The link between task dimensionality and the minimal rank is interesting and promising.

### Weaknesses
1. The paper is not very well-written in multiple aspect. The use of figurative language and lack of precision makes it somewhat ambiguous and less rigorous and I would consider rephrasing to focus on the main concept in a more direct way.
This can be seen in the first paragraph of the introduction for example. The paper is sometimes very redundant, making the read feel repetitive and unnecessarily lengthy. The notations are repeated (eg. numerous mentions of $\mathbf{x}$ being the input vector).
A thorough proofreading is needed (example Figure 5 in the Appendix, the caption is "Enter Caption").

2. The study is extensive on easy/non practical settings (linear/shallow cases) which leaves limited room for presenting interesting and novel results in more complex scenarios.

3. Several references are lacking, which is very detrimental as some previous experimental results not presented have adapted FA/DFA to a wide range of architectures. For example (Akrout et al., 2019) is merely cited but they present adaptations of FA that match back-propagation on more complex architecture (ResNet-50) and on more complex data (Image-Net) than the presented results. Furthermore, (Sanfiz and Akrout, 2021) which benchmarked FA, DFA and other biologically plausible alternatives to BP with open-sourced code is not cited.
Another work by (Launay et al., 2020), scaling to some degree DFA to even more complex architectures such as Transformer is not mentioned either.
Altogether, this makes the experimental part very shallow, which is unfortunate because the undelying idea has a really good potential and the consequence of the main difference with the other adaptations (sparser feedback matrices -> lower memory constraints) is not studied.

### Questions
1. You mention the use of batchnorm in your convolutional network (Table 1 in the Appendix). How could it be interpreted biologically? How do you train the parameters of the batchnorm in your model? Do you use RAF? Do you set the affine to false?
 How could maxpooling be biologically interpreted? Same question with dropout as you use a probability of 0.4.

2. Could your findings be linked to the fact that you only tested with image data? Could the dimensionality reduction be transposable to natural language processing (NLP)? Would the task dimensionality determine the minimal rank ? How could it then be adapted to learn in a self-supervised manner?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper aims at approximating backpropagation by using a low-rank projection of the forward matrix (and hence an approximation of the true gradient). The backward pass in each layer is done via two layers that together form a low-rank approximation of the forward weights. These weights are aligned to the forward weights through a combination of Hebbian and Oja’s rules.

### Strengths
1. The proposed method performs well and also provides a good approximation to backprop.
2. Sec. 5 results are interesting, as they suggest the same type of phenomena can be due to either forward or backward architectural choices (but see below).
3. Overall, this result shows that error signals have to at least match the task dimensionality for efficient learning, which provides useful intuition for bioplausible learning search.

### Weaknesses
1. Small improvement compared to [Akrout 2019]

The proposed approach doesn’t add much to the discussion in [Akrout 2019], at least in my opinion. [Akrout 2019] (using Eq. 10 (top) for $P=I$ in the definitions of this paper) showed that the Kolen-Pollack rule is good enough to achieve backprop-level performance on ImageNet. The proposed approach introduces one more feedback layer per forward layer, which is arguably even less biologically plausible than the feedback alignment-style feedback network. The core contribution, the low-rank approximation, seems to be a minor extension of the existing framework, and the performance gains are not substantial enough to warrant the added complexity. The paper should more clearly articulate the specific problem that low-rank feedback addresses that is not already covered by existing feedback alignment methods.

2. Oja’s rule issue

As presented in the paper, the learning rule for $P$ is not local – it requires weight transport, exactly the issue the authors are solving for backprop. This is because the matrix version of Oja’s rule uses a $(P\delta)(P\delta)^T P$ term: $P\delta$ is the output of the layer receiving $\delta$, so, like in backprop, $(P\delta)(P\delta)^T P$ requires the output activations to be multiplied by the transpose of the weights to find $(P\delta)^T P$. It might be that you can still do PCA with some modifications of Oja’s rule that make it local, but that should be clearly articulated in the paper. (What’s usually considered local is the 1d version of Oja’s rule, since it doesn’t have matrix multiplication. But that can only find the top principal component.) The non-locality of the Oja's rule implementation undermines the biological plausibility claims, and the paper needs to address this limitation more thoroughly.

3. No baselines for Sec. 5

Sec. 5 is an interesting approach, but it doesn’t have baselines. The authors should show that the baseline models (i.e. backprop, same architecture) with/without feedforward bottleneck produce different receptive fields. I understand that the architecture/training is the same or similar to [Lindsey 2019], but a reader shouldn’t have to look at another paper to find the baselines. (It is especially important since the results is purely qualitative) The lack of proper baselines makes it difficult to assess the significance of the results in this section, and the authors should include these baselines to support their claims.


4. Some parts of the literature are misrepresented

Lines 91-98 first introduce [Akrout 2019], and then state that it “struggles to match BP performance in complex architectures like CNNs”. Fig. 3 in [Akrout 2019] shows that their approach works exactly as well as backprop on ResNet50 trained on ImageNet. This misrepresentation undermines the credibility of the paper's literature review. Lines 416-420 mention that training CNNs with feedback alignment is hard, but that adaptive feedback “has made progress”. See above regarding [Akrout 2019], but even earlier work like [Liao 2016] (the sign-symmetry method) has achieved significant progress in that direction. Both should be cited in this paragraph. The paper should accurately represent the progress made by previous methods. Finally, line 491 says “our novel learning rule bears superficial similarity to previous Feedback Alignment (FA) schemes”. I don’t think it’s fair to call Eq. 10 only superficially similar to Kolen-Pollack, as it is pretty much the same rule with one extra step. The paper should acknowledge the strong connection to existing methods and avoid downplaying the similarities.

### Questions
1. Is there any way to quantify Sec. 5 results? The shift between center-surround and orientation selective is interesting, but presumably it is a function of how narrow the bottleneck is, and also of how wide the network is. Having a quantitative plot for these results would be a good addition to the paper. 
2. In Eq. 10 (left), shouldn’t $h_l$ be $h_{l-1}$?
3. Small issues: figures should have larger font sizes as they’re hard to read; Fig. 5 in the appendix has a placeholder caption; typo in "necessary" in line 215

-------------
Updated the score to 8; see the rebuttal discussion.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work explores the hypothesis that a low-dimensional error signal is sufficient to train neural networks, in particular an error signal of dimensionality equal to the neural network output, as opposed to the dimensionality of the gradient, which is equal to the number of parameters of the neural network. 
It proposes a new learning algorithm that allows manipulating the dimensionality of the error signal. 
The algorithm is based on feedback alignment, is local and therefore is supposed to be biologically plausible.
Training of feedback weights is not new, the novelty of the algorithm is using low-rank matrices for the feedback weights.
It studies the algorithm theoretically in a simple linear setting, it further tests it with MLP and a convnet on CIFAR10 and looks into receptive fields of neutrons.

### Strengths
The paper is well written and seems correct.
I find it interesting that the authors found a way to exploit the low-dimensionality of the error into a concrete algorithm, and that the algorithm can match the performance of gradient descent (backpropagation).

### Weaknesses
About biological plausibility, that’s a very controversial topic. 
I was working in computational neuroscience for 15 years, and what I learned is that there is absolutely no consensus on which model is biologically plausible which one is not.
The word “biologically plausible” is used by different people with vastly different meanings, so much so that those words are meaningless unless used in a very restricted context of a few “friends” who work on the same identical problems.
Therefore, in my opinion, the “biological plausibility” adds very little value to this paper.

About the machine learning side: the fact that the error signal should have dimensionality equal to the neural network output is trivial, and can be studied in any neural network, not just in the linear setting.
Using simple chain rule, it is easy to find that the gradient of the loss is equal to J^T err, where J is the Jacobian matrix of the neural network with respect to the parameters, and err is the vector of errors (the gradient of the loss with respect to the output).
The vector err has dimension d, where d is the dimensionality of the output, while the matrix J has dimension d x p, where p is the number of parameters.
Therefore, for any neural network, it is obvious that the gradient is a projection of a low dimensional (d) vector into a high dimensional space (p).

Trivial or not, I find it interesting that the authors found a way to exploit the low-dimensionality of the error into a concrete algorithm.
However, does this algorithm represents an advance for machine learning?
Feedback alignment is not new, training feedback weights is also not new, so the only novelty seems to be the low rank of the feedback weights.
That does not seem to be a significant contribution.

### Questions
I wonder whether the low-dimensionality of the error signal may be exploited to design an algorithm that is actually useful.
The proposed algorithm may perhaps save a little bit of compute during the reverse pass, due to the low-rank of the feedback weights, but it requires more memory, because it requires more weights than a standard neural network (feedback weights in addition to forward weights) and it still requires saving neural activations during the forward pass like standard models.

### Soundness
3

### Presentation
3

### Contribution
2
