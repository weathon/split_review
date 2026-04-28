# Enhancing Certified Robustness via Block Reflector Orthogonal Layers

- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 6, 6, 3, 6

## Abstract
Lipschitz neural networks are well-known for providing certified robustness in deep learning. In this paper, we present a novel efficient Block Reflector Orthogonal layer that enables the construction of simple yet effective Lipschitz neural networks. 
In addition, by theoretically analyzing the nature of Lipschitz neural networks, we introduce a new loss function that employs an annealing mechanism to improve margin for most data points.
This enables Lipschitz models to provide better certified robustness.
By employing our BRO layer and loss function, we design BRONet, which provides state-of-the-art certified robustness.	
Extensive experiments and empirical analysis on CIFAR-10, CIFAR-100, and Tiny-ImageNet validate that our method outperforms existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose a new orthogonal parametrization, Block Reflector Orthogonal layer (BRO), that can be used in the context of Lipschitz neural networks and provide certified robustness against adversarial attacks. The authors state that the BRO method to construct orthogonal layers using low-rank parameterization is both time and memory efficient, while also being stable during training as it does need 
an iterative approximation algorithms. The authors also propose a theoretical analysis and develop a novel loss function, Logit Annealing loss, to increase certified accuracy. The authors perform an extensive set of experiments to demonstrate their finds.

### Strengths
- The paper is well written. The motivation is clear and the contribution BRO is well stated. 
- The BRO method leverage FFT for convolution in a similar fashion as the Caley approach
- The authors have performed an extensive set of experiments to demonstrate their results (comparaison and ablation study)

### Weaknesses
 - BRO is not compared to the Cayley approach in Figure 2. Does BRO offer better memory and runtime against Cayley? can Cayley orthogonal layers appear in Figure 2?
- For the comparison on certified accuracy, there are a lot of moving parts in the experimental section and this tends to become confusing, I would suggest the authors to simplify the experiments and focus on the comparison with the state of the art, which is LiResNet (Hu et al. 2024).
- It seems that the authors did not take the results of the latest version of Hu et al. 2024 (which came out in June 2024) as there seems to be a huge gap in the reported results. Can the authors comment on this?
- Table 1 reports the first results of SLL, but there was an erratum in the latest version and the results have been revised (see Table 7 in the arxiv version of the paper).
- It seems that BRO does not perform very well at large radius, is this due to the parameterization of the loss?
- Hu et al. 2024 have shown that their approach scales to ImageNet, can the authors provide certified results for ImagNet?

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work presents a novel BRO layer for constructing Lipschitz neural networks that leverages low-rank parameterization, avoiding iterative approximations to enhance both memory and computational efficiency. The introduction of the Logit Annealing loss function addresses the complexity limitations of Lipschitz networks, contributing to improved learning of margin properties. This work promises good advancements in robust and efficient Lipschitz neural networks design.

### Strengths
1. The proposed method is supported by good theoretical analysis.

2. The BRO improves both efficiency and stability compared with previous work.

3. The proposed Annealing Loss could serve as a scalable method to enhance the training for the Lipschitz neural network.

### Weaknesses
1.  **The scalability to other large models**: The proposed BRO layer is currently designed to function within specific neural network architectures, such as the BRONet Architecture, maybe with constrained parameters and fixed configurations. This limitation raises concerns about its practical applicability to large-scale foundation models. Ensuring the Lipschitz condition for these more complex and expansive models could be challenging. Specifically, the reliance on low-rank parameterization within the BRO layer might not effectively capture the intricate dependencies present in high-dimensional data processed by foundation models. The fixed rank could impose a bottleneck, limiting the model's ability to learn complex features. Furthermore, the computational overhead of maintaining the Lipschitz constant in such large models needs to be addressed. The impact of this work would be significantly enhanced if the authors could empirically demonstrate that BRO effectively improves the robustness of more complex and diverse neural networks.

2. According to lines 276-279, the BRO layer is not a universal approximation for orthogonal layers and the author empirically demonstrates BRO is competitive with that of LOT and SOC. A more detailed analysis would be beneficial to illustrate that the error introduced by this non-universal approximation is minimal. It is unclear how the non-universal approximation affects the expressiveness of the model, especially in scenarios where the underlying data distribution requires a more complex orthogonal transformation. A quantitative analysis of the approximation error, perhaps using metrics like the Frobenius norm between the learned BRO matrix and the ideal orthogonal matrix, would be beneficial. Furthermore, the authors should explore the effect of the rank parameter on the approximation quality and the overall performance of the network.

3. I am curious about whether the choice of activation function affects the Lipschitz constant.

### Questions
See weakness.

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
3

### Summary
This paper introduces a novel approach called Block Reflector Orthogonal (BRO) layer for constructing Lipschitz neural networks with certified robustness guarantees against adversarial attacks. The key innovation is a new parameterization scheme that creates orthogonal layers without requiring iterative approximation algorithms, making it both computationally efficient and numerically stable compared to existing methods like SOC and LOT. The authors use BRO to develop BRONet, which achieves state-of-the-art certified robustness on CIFAR-10, CIFAR-100, and Tiny-ImageNet datasets. Additionally, they provide theoretical analysis showing that Lipschitz networks have inherent limitations in margin maximization due to limited model complexity, leading them to propose a new Logit Annealing (LA) loss function that employs an annealing mechanism to help models learn appropriate margins for most data points rather than overfitting to maximize margins for specific examples. Through extensive experiments, they demonstrate that their combined approach (BRO layer + LA loss) outperforms existing methods while requiring fewer parameters and computational resources.

### Strengths
- Strong theoretical foundations with clear mathematical proofs for their proposed methods
- Significant computational efficiency gains compared to existing approaches (SOC, LOT)
- Comprehensive experiments across multiple datasets and architectures
- Novel loss function with clear theoretical motivation and empirical benefits
- State-of-the-art certified robustness with fewer parameters
- Thorough ablation studies demonstrating impact of each component

### Weaknesses
 - BRO layer is not a universal orthogonal parameterization (acknowledged by authors)
- Limited experiments on larger datasets beyond Tiny-ImageNet
- No comparison with empirical defenses or other certified robustness approaches beyond Lipschitz methods
- Lack of investigation into potential failure cases or limitations of the LA loss
- Some hyper-parameters (rank selection, LA loss parameters) require manual tuning

### Questions
- Have you tested BRO's performance on larger datasets like ImageNet?
- How sensitive is the method to the choice of rank in BRO and how should practitioners select it?
- How does the LA loss perform compared to other margin-based losses beyond CE+CR?
- What are the main failure cases or limitations of your approach?
- Have you considered comparing against other certified defense methods beyond Lipschitz approaches?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel 1-Lipschitz layer based on Block-reflector matrices (BRO convolution), which are orthogonal. Additionally, authors propose a Logit Annealing (LA) loss to optimize during training in order to favor certified accuracy. Their proposed recipe consistently improves certified accuracy in CIFAR10/100 and TinyImageNet and is shown to be more efficient than previously proposed orthogonal layers.

### Strengths
The strengths of this work are mainly on the experimental side. Assuming the theoretical results hold:

- More efficient and scalable models than the previous art due to exact 1-Lipschitz layers without the need of iterative approximations.
- Improved certified accuracy. Authors demonstrate that both their BRO convolutional layer and LA loss help improving the certified accuracy.

### Weaknesses
The weaknesses of the paper appear on the theoretical and implementation sides. In general, the paper is very hard to read and has many errors in key parts of the paper. This questions the validity of their 1-Lipschitz claims for the BRO convolution.

- **Many typos and unclear notation:**
	- Everywhere: Please use $c_{\text{in}}$ and not $c_{in}$ when subscripting or upperscripting with words.
	- Algorithm 1, line 1: I assume $c_{\text{in}}$ and $c_{\text{in}}’$ are the number of input channels for the current and next layers respectively. Then, why do you need $c_{\text{out}}$? It is very confusing. I would just remove $c_{\text{in}}’$ and use $c_{\text{out}}$ instead.
	- Algorithm 1, line 4: $\tilde{V}:= \text{FFT}(V)$ should be $\tilde{V}:= \text{FFT}(V^{\text{pad}})$.
	- Lines 205 and 214: Is $\circledast$ the convolution operator? 
	- Proposition 2: If $J \in \mathbb{C}^{m \times m}$, then $J^* \in \mathbb{C}^{m \times m}$ as well. How can you even perform $J\tilde{V}J^{*}$ if $\tilde{V} \in \mathbb{C}^{m\times n}$? Does it have to be that $m=n$?
	- Proposition 2, equation 14: If assuming $n=m$, the proof is right, but equation 14 should be: $(\tilde{V}^* \tilde{V})^{-1} = J(J\tilde{V}^*\tilde{V}J^*)^{-1}J^*$

- **Unclear if BRO convolutions are orthogonal:**

From Proposition 1, it’s clear that in the dense case, the BRO layer is orthogonal. However, in the convolutional case there are many unclear aspects.

In lines 205 and 214, authors state that they construct their BRO convolution based on constructing the kernel:
	$$
		W_{\text{Conv}} = I - 2V \circledast (V^{\top} \circledast V)^{-1} \circledast V^{\top}
	$$
Authors argue that the circular convolution with this kernel is orthogonal, but do not provide any proofs. Then, given $\tilde{V} = \text{FFT}(V)$ authors conclude $\tilde{W} = \text{FFT}(W_{\text{Conv}}) = I - 2\tilde{V}(\tilde{V}^*\tilde{V})^{-1}\tilde{V}^*$. It’s unclear how authors arrive to this expression as it would need to assume that: (i) $n=m$ to be able to do element wise products (which authors do not mark with $\cdot$, leading to confusion) (ii) $\text{FFT}(I)=I$ (iii) $\text{FFT}((V^{\top} \circledast V)^{-1}) = \text{FFT}((V^{\top} \circledast V))^{-1}$, which are false in general. 

Moreover, it is not clear what Proposition 2 implies regarding orthogonality, or how the case when $m=n$ is handled (lines 237-241 are very vague). It would be nice to include an explicit proof that the norm of the output of algorithm 1 is the same as the input. Exactness of the 1-Lipschitz result is important for ensuring the experimental results about the certified accuracy are valid. So, I believe more rigour should be put into proving the results claimed in this paper.

- **Unclear motivation to use LA and differences with CR:**

Authors start motivating the need of their LA loss with a very convoluted argument about the minimal CR loss being constrained by the model complexity. Then, they simply present their loss without relating it with the theory they developed for the CR loss. I believe the analysis doesn’t add anything if it is not performed for the LA loss. While I see that LA is less strict I don’t see how LA solves the issue in Theorem 1. 

It would be more beneficial to fully state the CR loss and compare it with LA. Right now, only the reference is provided. I also think the results in Figure 8 and section C.2 are more interesting than the current write-up of the main paper.

All in all, I believe authors should be more careful about their theoretical derivations and be very clear about why Algorithm 1 results in orthogonal convolutions. Without this being clear, the results are meaningless and I cannot propose the paper for acceptance.

### Questions
Please see the weaknesses section for questions about the theory, notation and typos.

- Can authors implement the convolution without the FFT? Just creating $W_{\text{Conv}}$ and applying the standard Conv2D function from torch. Are the results the same as in Algorithm 1? Your outputs should be the same and its a good way to debug if anything is wrong.
- Did authors try LiResNet + BRO only for table 2? That is, only changing the backbone without changing the loss.
- The BRO layer is for sure orthogonal in the case of fully connected layers. Have authors tried comparing the different layers in the fully connected case? I.e. training fully connected classifiers in a small dataset (Cifar10 / MNIST). I don’t believe this experiment is super interesting but is the only case where orthogonality is clear at the moment.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents the block reflector orthogonal (BRO) layer, which enhances the construction of Lipschitz neural networks. By employing low-rank parameterization and circumventing iterative approximations, the proposed approach achieves notable gains in both memory and time efficiency. Comprehensive evaluations against existing orthogonal layers reveal its superior robustness, underscoring its potential in advancing neural network performance.

### Strengths
1. The BRO method effectively utilizes low-rank parameterization to construct orthogonal layers, resulting in significant improvements in both computational time and memory efficiency, which are critical for scaling neural networks.
2. The paper provides a thorough comparison with state-of-the-art techniques, presenting results that are well-structured and articulate, allowing readers to easily grasp the contributions and effectiveness of the proposed method.
3. The paper is well-structured and logically organized. The presentation of the results is clear and systematic.

### Weaknesses
1. The evaluation results in Table 1 indicate a degradation in the performance of the proposed BRONet with increasing perturbation budgets. A discussion on this inconsistency would enhance the paper's credibility and provide insight into the limitations of the model. Specifically, the trend of performance should be monotonic with respect to perturbation budget; the observed non-monotonic behavior suggests a potential flaw in the method's robustness guarantees or implementation. The paper should address why the certified accuracy at a perturbation budget of 72/255 is lower than at 36/255, which is counterintuitive for a robust model.
2. Results in Table 3 show only marginal improvements over existing methods, raising concerns about the significance of these gains. Including standard deviations or confidence intervals would clarify the statistical significance of the results and help determine whether observed improvements are due to random variance in training. The reported improvements, such as 0.2% or 0.4%, are within the typical range of random fluctuations in neural network training, and without statistical significance, it is difficult to assess the true impact of the proposed method.
3. The experiments are conducted solely on CIFAR and Tiny-ImageNet datasets, which, while widely used, may not fully demonstrate the method's robustness and scalability. Including additional datasets, particularly larger or more complex ones (e.g., ImageNet or real-world benchmarks), would provide a more comprehensive evaluation of the method's efficacy. The method's performance on larger datasets with more complex data distributions is crucial for assessing its practical applicability.

### Questions
1. What factors contribute to the inconsistent performance gains observed in the proposed BRONet as the perturbation budget increases?
2. Why were standard deviations or confidence intervals not included in the reported results? Given the marginal improvements, understanding the variability of the outcomes would be particularly valuable.
3. Has the BRO method been evaluated on more complex datasets, such as full ImageNet, or applied to tasks beyond classification, to assess its scalability and generalization?

### Soundness
2

### Presentation
3

### Contribution
2
