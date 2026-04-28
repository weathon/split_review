# SAN: Inducing Metrizability of GAN with Discriminative Normalized Linear Layer

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6

## Abstract
Generative adversarial networks (GANs) learn a target probability distribution by optimizing a generator and a discriminator with minimax objectives. This paper addresses the question of whether such optimization actually provides the generator with gradients that make its distribution close to the target distribution. We derive \yuhta{\textit{metrizable conditions}}, sufficient conditions for the discriminator to serve as the distance between the distributions, by connecting the GAN formulation with the concept of sliced optimal transport. Furthermore, by leveraging these theoretical results, we propose a novel GAN training scheme called the Slicing Adversarial Network (SAN). With only simple modifications, \yuhta{a broad class of existing GANs can be converted to SANs}. Experiments on synthetic and image datasets support our theoretical results and the effectiveness of SAN as compared to the usual GANs. \yuhta{We also apply SAN to StyleGAN-XL, which leads to a state-of-the-art FID score amongst GANs for class conditional generation on CIFAR10 and ImageNet 256$\times$256.} Our implementation is available on the project page \url{https://ytakida.io/san/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors focus on evaluating the metrizability of discriminators in Generative Adversarial Networks (GANs) training by determining if the discriminator's measure can constitute a metric, defined by properties such as directionality, separability, and injectivity. Initially, they establish a connection between the Wasserstein distance and the Functional Mean Divergence (FM*). Then the Separability is proposed to link FM* to the maximum Average Sliced Wasserstein (max-ASW) distance. Subsequently, they introduce the injectivity for the design of effective discriminators. They examine commonly used GAN frameworks, including Wasserstein GAN and other losses GANs, and find that most GAN architectures, including those using Hinge-loss, Saturating, and Non-Saturating loss functions, typically do not fulfill the criterion of directional optimality. In response to this, the authors propose a straightforward modification to enhance this property within these GANs. To substantiate their theoretical claims, they conduct experiments that demonstrate the significance of these three properties. They also apply their modifications to contemporary models such as DCGAN, BigGAN, and StyleGAN-XL. The results affirm that their simple yet effective alterations lead to improvements over the baseline performance, thereby confirming the practical value of their theoretical insights.

### Strengths
1. The authors present a theoretically grounded analysis that yields a straightforward method for enhancing GAN discriminators.

2. Their theoretical contributions are insightful and offer practical guidance for discriminator design. 

3. The experiments conducted are well-aligned with the theory, and the clarity of the writing effectively conveys the study's findings and implications.

### Weaknesses
1. While the study shows experimental progress, the improvement in FID (Frechet Inception Distance) is modest.

2. The authors are encouraged to conduct experiments on CIFAR-100 using BigGAN and FFHQ using StyleGAN2 to further verify the effectiveness of the proposed method.

3. To enhance accessibility, the authors should consider simplifying the mathematical notation to cater to a wider audience.

### Questions
1. Could the authors cite studies or evidence that show how regularizing the gradient of the discriminator or switching from ReLU to LeakyReLU might enhance injectivity?

2.  In Table 4, are the results shown for BigGAN the ones obtained after replacing ReLU with LeakyReLU?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article introduces a novel theoretical perspective to shed light on the optimization process, which determines whether the generator receives gradients that bring its distribution closer to the target distribution. The article introduces three metrizable conditions: direction optimality (evaluating the gradient between two distributions), separability (examining the distinctness between two distributions), and injectivity (measuring the metric as a distance). These conditions aim to provide clarity on the underlying motivation. Furthermore, the article includes a theoretical proof and introduces a new loss function and a normalized linear layer. These enhancements are designed to boost the discriminative capability of the discriminator and enable the generation of diverse, high-fidelity samples from the generator.

### Strengths
This article introduces a novel theoretical perspective aimed at addressing whether the optimization process truly provides the generator with gradients that lead its distribution closer to the target distribution. The article proposes three metrizable conditions, namely direction optimality (evaluating the gradient between two distributions), separability (evaluating disjointedness), and injectivity (measuring the metric as a distance).

Additionally, the article provides both theoretical and empirical evidence to demonstrate that only Wasserstein GANs fulfill these conditions. To enhance the discriminative capability of the discriminator and facilitate the generation of diverse, high-fidelity samples from the generator, the authors introduce a new loss function and a normalized linear layer. This normalized linear layer serves as a plug-in component that can be seamlessly incorporated into various GAN models.

In experimental evaluations, the SAN model achieves the best FID score when compared to numerous GAN baseline models.

### Weaknesses
The article's motivation, which revolves around the examination of whether trained discriminators effectively supply gradient information to optimize generators for reducing dissimilarities, appears to have been explored in prior articles [1-5]. However, the article falls short in providing a clear connection between the theoretical results and their practical implications. Specifically, while the authors introduce three metrizable conditions, direction optimality, separability, and injectivity, the paper does not sufficiently explain how these conditions translate into concrete improvements in GAN training. The theoretical framework, while novel, lacks a detailed explanation of how it addresses the limitations of existing GAN training methods. Moreover, the significance of the theoretical findings might benefit from more detailed explanation. For instance, the practical implications of satisfying these conditions, beyond the Wasserstein GAN, are not clearly articulated. The paper would benefit from a more thorough discussion of how the proposed conditions lead to better convergence properties or improved sample quality in practice. The connection between the theoretical framework and the empirical results needs to be strengthened, particularly in explaining why the proposed loss function and normalized linear layer are effective in light of the theoretical conditions.


1.Variational inference via Wasserstein gradient flows

2.Variational Wasserstein gradient flow

3.Deep Generative Learning via Variational Gradient Flow

4.A Framework of Composite Functional Gradient
Methods for Generative Adversarial Models

5.Gradient Layer: Enhancing the Convergence of Adversarial Training for Generative Models

### Questions
I have read the paper carefully, so i want the author to clarify the questions as follows:

If the author can clarify the following questions well, I'd like to raise my rating score.

1. If I understand correctly, "direction optimality" implies that a negative gradient of the metric between the generated distribution and the target distribution , which guides the generated distribution toward the target. "Separability" pertains to two disjointed distributions, and "injectivity" suggests that the metric between the generated and target distributions is a distance. Is this interpretation accurate?

2. Could you clarify the symbol "$*$" in Table 1?


3. I recommend that when the article first mentions metrizable conditions, namely, direction optimality, separability, and injectivity, it would be more reader-friendly to provide an intuitive understanding of these terms and indicate which paragraphs explain these definitions. This would help readers quickly grasp the key concepts before delving into the detailed explanations.

4. I have a question about the statement as follows:
most existing GANs besides Wasserstein GAN do not satisfy direction optimality with the maximizer $w$ of $\mathcal{V}$. Although most existing GANs do not  satisfy direction optimality proposed in the article, but the discriminator of these gans actually provides the generator with gradients that make its distribution close to the target distribution which has been discussed in other articles[1-5]. What do you think about this question?



5. There might be an error in the symbol  $g\# $     $=\sigma(g^{-1}(B))$. 

The function $g$ is defined as $g: Z \rightarrow X$, so the inverse function $g^{-1}$ should be $g^{-1}: X \rightarrow Z$. The term $\sigma(\cdot) \in \mathcal{P}(Z)$. However, $g\#$ 

is meant to represent the generator $g: Z \rightarrow X$. Thus, there appears to be a discrepancy.


6. I recommend that the author provide a clear explanation of why Equation (16) satisfies Theorem 5.3. I find it somewhat confusing and would appreciate a more comprehensible clarification.

7. I have reviewed the code in the supplementary materials. There is a discrepancy between the code provided in Listing 2 (SAN discriminator) and lines 92-96 in the file "STYLESAN-XL/pg_modules/san_mondules.py/SANConv2d." To ensure accuracy, please verify which version is the correct one.
8. Should the SAN be trained from scratch, or can it be fine-tuned, especially in the last layer, using the Eq.16 loss function?

9. I find it quite confusing to understand the importance of the three conditions in your theorem 5.3. In my opinion, direction optimality should be the most important condition, while the separability and injectivity conditions may not carry the same weight. This is because metrics used in GANs, such as f-divergences or IPM functions, inherently satisfy the distance property. Maintaining the separability condition becomes increasingly challenging as GAN training progresses and the generated distribution approaches the real data distribution.
Therefore, I recommend that the author clearly outline the relationships and significance of all three conditions to provide a better understanding.


1.Variational inference via Wasserstein gradient flows

2.Variational Wasserstein gradient flow

3.Deep Generative Learning via Variational Gradient Flow

4.A Framework of Composite Functional Gradient
Methods for Generative Adversarial Models

5.Gradient Layer: Enhancing the Convergence of Adversarial Training for Generative Models

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
