# On the expressiveness and spectral bias of KANs

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
Kolmogorov-Arnold Networks (KAN) \cite{liu2024kan} were very recently proposed as a potential alternative to the prevalent architectural backbone of many deep learning models, the multi-layer perceptron (MLP). KANs have seen success in various tasks of AI for science, with their empirical efficiency and accuracy demonstrated in function regression, PDE solving, and many more scientific problems.
 
In this article, we revisit the comparison of KANs and MLPs, with emphasis on a theoretical perspective. On the one hand, we compare the representation and approximation capabilities of KANs and MLPs. We establish that MLPs can be represented using KANs of a comparable size. This shows that the approximation and representation capabilities of KANs are at least as good as MLPs. Conversely, we show that KANs can be represented using MLPs, but that in this representation the number of parameters increases by a factor of the KAN grid size. This suggests that KANs with a large grid size may be more efficient than MLPs at approximating certain functions. On the other hand, from the perspective of learning and optimization, we study the spectral bias of KANs compared with MLPs. We demonstrate that KANs are less biased toward low frequencies than MLPs. We highlight that the multi-level learning feature specific to KANs, i.e. grid extension of splines, improves the learning process for high-frequency components.  Detailed comparisons with different choices of depth, width, and grid sizes of KANs are made, shedding some light on how to choose the hyperparameters in practice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the theoretical and empirical properties of Kolmogorov-Arnold Networks (KANs), particularly focusing on their approximation capabilities and spectral bias. Given the growing interest in alternative neural network architectures for function approximation, the study of KANs is relevant to the broader machine learning and scientific computing community. However, while the comparison with MLPs is insightful, the direct impact and importance of KANs over existing methods are not convincingly demonstrated.

### Strengths
1.Theoretical Comparison of Expressiveness: The authors establish that KANs are at least as expressive as MLPs. Specifically, they show that any MLP can be reparameterized as a KAN with degree k splines which is only slightly larger. Conversely, they demonstrate that KANs can also be represented by MLPs, but the number of parameters increases significantly with the grid size of the KAN. This implies that KANs with large grid sizes may be more efficient in approximating certain classes of functions.
2. The exploration of KANs’ spectral bias and their comparison with MLPs provides a novel perspective. The use of B-splines and the grid extension method offer unique contributions. However, much of the theoretical groundwork relies heavily on established techniques.

### Weaknesses
1. The parameter count in KANs and MLPs are not directly comparable, and the authors have blurred the distinction between these concepts. Additionally, the depth of KANs differs from that of MLPs, and the authors should not directly compare them, as this leads to a conceptual confusion. 
We acknowledge that the conceptual confusion arises from the discussion in Section 3, particularly in Theorem 3.1- 3.4, where we compare the parameter count and depth between KANs and MLPs. This issue is also present in the experimental results in Sec4.1 and 4.2, where parameter comparisons are made across different models. 

2. Theorem 4.1 lacks clarity regarding its implications for KAN's performance on high-frequency data. The authors should explicitly state whether the theorem suggests that KANs outperform other models in handling high-frequency data. Additionally, it would be beneficial to provide a brief discussion or corollary connecting the theorem to spectral bias or high-frequency performance to clarify its practical significance.

3.The theoretical analysis provided in the paper is limited to shallow KANs, which restricts the generalizability of the conclusions regarding spectral bias. To enhance the practical relevance, the authors should discuss the limitations of their current analysis and suggest potential methods for extending the theoretical framework to deeper KANs. This would provide a more comprehensive understanding of the spectral bias in real-world applications.

4.While the experiments cover diverse applications, they lack rigorous statistical validation to substantiate the claimed advantages of KANs. The authors should include specific statistical tests or validation methods to strengthen their results. Furthermore, more detailed comparisons with state-of-the-art baseline methods would help provide a stronger foundation for the claimed benefits of KANs, especially in practical applications like PDE solving and Gaussian random field fitting.

5.Incomplete Problem Contextualization: The paper does not clearly establish the practical significance of overcoming spectral bias in real-world tasks, nor does it compare KANs against state-of-the-art methods beyond MLPs.

6.Limited Discussion on Limitations: The potential downsides of KANs, such as computational cost, overfitting, and practical implementation challenges, are not thoroughly addressed.

### Questions
1.Theoretical Expansion: How does the depth of Kolmogorov-Arnold Networks (KANs) influence their spectral bias and approximation capabilities? Could a deeper theoretical analysis be provided to explore this relationship?

2.Enhanced Experimental Design:Could the authors include more rigorous statistical analysis and comparative experiments with a broader set of baseline models, particularly state-of-the-art neural architectures used in scientific computing?

3.Real-World Applications: How could the practicality of KANs be demonstrated in more diverse and realistic scenarios? Are there plans to showcase examples that highlight their advantages and limitations?

4. Detailed Discussion: Could the authors provide a more detailed discussion on the computational cost, scalability, and limitations of KANs? What are the key factors that may affect their broader applicability?

5. The author should

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on two aspects of KAN and MLP. The first issue is the approximation and representation capacility to functions of both networks, and the second issue is the spectral bias of approximation. Both issues are very important and attractive.

### Strengths
This paper characterizes the representation capacility of approximation of KAN and MLP, with a considerably rigorous mathematical analysis.

### Weaknesses
On the expressiveness, it is merely a theoretical interest, and the proof of mathematical analysis is over simplified by assumpting extremely shallow KAN network, which violates the practical deep network situation, and can not be regarded as equalivent to general case or nonlinear effect.  

The experiments are not sufficient, and the paper is mainly of theoretical approach.

### Questions
I have following questions:

(1).  All the theorems 3.1, 3.2 and 3.3 are extremely mathematical, and their assumptions are not agreeable with practical cases. How can the authors explain the main differences?

(2). For the examples of PDE, the equation is very simplie, and the functions are of sufficient smoothness. If the functions concerned becomes chirp function and so on, how about the performance?

(3) In Fig. 4, the performance of approximation does not always tend to better. Can you explain the causes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper is both a theoretical and experimental study of KANs, a recently introduced architecture with parametrizable activation functions,
aiming at characterizing their expressivity and spectral biases in comparison to MLPs. Since KANs offer a lot of new potentialities, it is
a legitimate and relevant research subject to try to characterize these  in  relation to properties of the data, therefore expressivity and spectral biases constitute obviously a good angle of analysis. 

So the first theoretical result concerns expressivness: it tells that an arbitrary MLP (with activation function in C^k typically) can be exactly mapped onto a KAN (with B-splines of order k) with a depth multiplied by 2 and requiering a grid size of 2, so overall the number of parameters is multiplied by 4 (if I interpret well the result, this could be stated more explicitly actually) in this mapping. In reverse they find a mapping of a KAN to an MLP with an increase of parameters of G, the grid size of the original KAN. These constructions lead the authors to conclude qualitatively that KAN are more expressive than MLP. As acknowledged by the authors, this is not a sharp result as it is not excluded that a better construction of the mappings could be found leading to different conclusions, but these constructions are interesting on their own. A more concrete statement on expressivity is given by corollary 3.4, giving the speed of approximating of any function on a Sobolev space w.r.t the number of parameters of a KAN. Here, as a non specialist of this kind of result I become slightly confused. The statement  is seemingly based on generic results on MLP, and seems not to be specific to KAN but more to multi-layer models, as it exploit the  aforementioned mapping of the KAN to MLP, so that I wonder why MLP with relu-k would not lead to the same statement?
There is sentence discussing this at the end of the paragraph which is cryptic to me as it refers to some apparently non-standard MLP with relu-k.  As a result the overall take-home message of this part is unclear to me. Is there any advantage to be attributed to KAN wrt to comparable MLP under this measure of expressiveness? Maybe the statement 3.4 is a profound and central statement of the paper, but the discussion should make it clear, by first giving how standard MLP with relu-k compare and then also maybe what are the practical consequence of such statement if any?

The second theoretical point concerns spectral bias, and theorem 4.1 to me is a nice and non-trivial statement showing that a single layer of B-splines is well conditioned, especially when the grid size becomes large, by looking at the spectrum of the Hessian of the loss. This fully characterizes the conditioning of the problem with explicit dependency w.r.t. embedding dimension and grid size. The comparison is done with MLP with Relu using a result given in Hong et al. (2022) obtained with similar techniques (Courant Fisher theorem) showing  a much larger spectral bias for MLP. I wonder however if a  comparison with the spectral bias of MLP with relu-k (unfortunately not to given in Hong et al, but I presume that similar techniques would lead to the result) would not be more relevant as they are in the same class of regularity as KAN with B-splines of order k?

The experimental part focuses on the spectral bias question on diverse examples. A comparison is shown between KAN with kth order B-splines and MLP with relu, showing a clear advantage to KAN regarding spectral bias, but again I wonder why the comparison is not done with the spectral bias of MLP with relu-k, if this  would not be be more meaningful?

### Strengths
the questions addressed in the paper are interesting and some of the statements are quite strong, in particular th. 4.1 on the characterization of the spectral bias. Overall, my non-specialist viewpoint  on this paper is that it looks like a rather clear and solid paper, with interesting statements.

### Weaknesses
 I found however a potential problem  of coherence concerning the comparison of KANs with MLPs: with relu-k at the beginning which is indeed legitimate,  and then basic relu starting from corollary 3.4. The theoretical expressivity result, specifically corollary 3.4, seems to rely on a mapping to MLPs, and the approximation rate achieved appears to be a general property of multi-layer models rather than something specific to KANs. The discussion does not sufficiently clarify why a standard MLP with ReLU-k would not achieve the same approximation rate. The authors mention a non-standard MLP with ReLU-k, but this is not clearly defined or compared to the standard case, making it difficult to assess the significance of the result for KANs. The spectral bias analysis in theorem 4.1 is strong, but the comparison to MLPs with ReLU is not fully convincing. A more relevant comparison would be with MLPs using ReLU-k activations, as they share the same class of regularity as KANs with B-splines of order k. The experimental section also suffers from this issue, comparing KANs with B-splines to MLPs with ReLU, rather than ReLU-k, which would provide a more meaningful comparison given the theoretical focus on the regularity of the activation functions. The instability observed in KAN learning during grid extension is not clearly explained. The reviewer is left wondering if the grid size is dynamically adjusted during learning, and if so, how this process affects the training dynamics. The presentation of experimental results could be improved. Figures 1 and 2 are very similar, and the information in Figures 3 and 4 could be synthesized into a more concise representation. The legends are too small to be legible in a printed version.

### Questions
- Is the comparison between KANs with kth order B-splines with MLP modified when considering relu-k instead of simple relu?
- In Figure 3 and 4 the learning of KANs display instabilities in contrary to MLP which are attributed to grid extension during the undersampled regime, I don't really understand what is meant by this, is it that the grid size of KAN is progressively extended during learning? 

Finally as a minor point:
I found that the way the experimental results are presented could be more concise and more informative. Figures 1 and 2 are almost identical, while all the plots given in figure 3 and 4 could be possibly synthetized to give the general behaviour w.r.t. to k, grid size, dimension and scale, and the legend should be magnified, I can't read anything on a printed version.

### Soundness
3

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
2

### Summary
The paper addresses the expressivity Kolmogorov-Arnold Networks (KAN) and the spectral bias.

A rigorous analysis of the representation power of the KAN vs MLP is welcome. 

I think the most important contribution of the paper is to show the relationship between MLP with ReLU^k activation function and KAN without bias. Th.3.2 and Th.3.3 bounds are not tight. A conclusion of the authors is that MLP scales with G^2 while KAN with G, the grid size. The additional contribution Cor3.4 is not well explained in relationship to MLP, but the authors highlight the potential advantage of KANs. 
 
The Analysis of the spectral bias seems a repetition of the analysis provided in [1], even if the authors analyze the Hessian matrix instead of the NTK matrix and show the elements of the Hessian. The authors are able to justify the reason why low frequency are not prioritized as in MLP, even if the connection with Th.4.1 is not clear.  

The analysis of PDE, seems to be the same are reported in [1], showing better performance of KAN-based models in the training loss. Not sure why the test loss is not reported. 


[1] 1. Wang, Y. et al. Kolmogorov Arnold Informed neural network: A physics-informed deep learning framework for solving forward and inverse problems based on Kolmogorov Arnold Networks. Preprint at https://doi.org/10.48550/arXiv.2406.11045 (2024).

### Strengths
As described above:

1. find the connection between two specific classes of MLP and KAN. 
2. interpretation of the spectral bias using the Hessian matrix
3. some experiments to visualize the spectral bias

### Weaknesses
The paper addresses the expressivity Kolmogorov-Arnold Networks (KAN) and the spectral bias.

A rigorous analysis of the representation power of the KAN vs MLP is welcome.

I think the most important contribution of the paper is to show the relationship between MLP with ReLU^k activation function and KAN without bias. Th.3.2 and Th.3.3 bounds are not tight. A conclusion of the authors is that MLP scales with G^2 while KAN with G, the grid size. The additional contribution Cor3.4 is not well explained in relationship to MLP, but the authors highlight the potential advantage of KANs. 

The Analysis of the spectral bias seems a repetition of the analysis provided in [1], even if the authors analyze the Hessian matrix instead of the NTK matrix and show the elements of the Hessian. The authors are able to justify the reason why low frequency are not prioritized as in MLP, even if the connection with Th.4.1 is not clear.  

The analysis of PDE, seems to be the same are reported in [1], showing better performance of KAN-based models in the training loss. Not sure why the test loss is not reported.

### Questions
1. could you expand on the consequences of Corollary 3.4
2. would be interesting to understand the consequence of thr.3.2 and th.3.3 for more "mainstream" architecture. For example, relu^k k=1 is probably the most common, while when gradients are needed SiLU SiLU-based activation functions are required, which is typical for scientific applications
3. would be nice to expand the Hessian analysis and connect with the NTK one
4. would be possible to perform the spectral analysis for section 4.4, instead of the error trend, if not, what is the test error?

### Soundness
3

### Presentation
2

### Contribution
2
