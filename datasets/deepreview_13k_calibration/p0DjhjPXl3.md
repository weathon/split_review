# Stealthy Shield Defense: A Conditional Mutual Information-Based Approach against Black-Box Model Inversion Attacks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Model inversion attacks (MIA) aim to uncover private training data by accessing public models, raising  increasing concerns about privacy breaches. Black-box MIA, where attackers can generate inputs and obtain the model's outputs arbitrarily, has gained more attention due to its closer alignment with real-world scenarios and greater potential threats. Existing defenses primarily focus on white-box attacks, with a lack of specialized defenses to address the latest black-box attacks. To fill this technological gap, we propose a post-processing defense algorithm based on conditional mutual information (CMI). We have theoretically proven that our CMI framework serves as a special information bottleneck, making outputs less dependent on inputs and more dependent on true labels. To further reduce the modifications to outputs, we introduce an adaptive rate-distortion framework and optimize it by water-filling method. Experimental results show that our approach outperforms existing defenses, in terms of both MIA robustness and model utility, across various attack algorithms, training datasets, and model architectures. In particular, on CelebA dataset, our defense lowers the attack accuracy of LOKT to 0\% while other defenses remain 50-75\%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a post-process black-box MI defense Stealthy Shield Defense (SSD) based on conditional mutual information (CMI). By leveraging CMI, SSD aims to reduce the model's output dependence on its input. The experiments demonstrate SSD's effectiveness against four state-of-the-art black-box MI attacks on two datasets.

### Strengths
* This work focuses on defending against black-box MI attacks which have not been addressed in the existing defense.

* As a post-processing defense, SSD can be easily integrated with most pre-trained models for defending against black-box attacks.

* Empirical results demonstrate SSD's success in reducing the attack performance of four state-of-the-art black-box MI attacks.

### Weaknesses
 * Practical Limitations: Although the idea of post-processing defense is interesting, the proposed method raises concerns about its applicability in real-world scenarios. To modify the model's prediction output, **SSD requires a dataset $D_{valid}$**, which I believe should be real data (either the training dataset or its validation set). This means the user must store raw training data or predictions on the training data to perform predictions, potentially increasing the risk of data leakage. Furthermore, the method's reliance on a per-class validation set, especially when some classes may have very few samples, raises concerns about the robustness of the estimated conditional mutual information. The use of a single sample per class, as suggested by the authors' description of their validation set, is particularly concerning, as it does not allow for a reliable estimation of the average prediction, which is a core component of the method.

* SSD's prediction process involves an optimization step for each image, leading to significantly increased computational costs and slower inference times compared to other models. This per-sample optimization is a significant drawback, making the method impractical for real-time applications or large-scale deployments. The computational overhead is not just a matter of time but also of energy consumption, which is a critical factor in many practical scenarios.

* The experiments were conducted on low-resolution 64x64 images, limiting the generalizability of the findings high-resolution scenarios. The performance of MI attacks and defenses can vary significantly with image resolution, and it is unclear whether the reported results would hold for higher resolution images, which are more common in real-world applications. The lack of experiments on high-resolution images makes it difficult to assess the practical relevance of the proposed method.

* [r1] was omitted in the paper while it is also a state-of-the-art black-box attack.

* The paper suffers from some typos and grammatical errors. For examples, lines 41, 107.

### Questions
* [r1] was omitted in the paper. I suggest the author should add [r1] in the experiments

* Can the author evaluate the proposed method's performance on high-resolution images? Additionally, please provide more details on how high-resolution MI attacks like MIRROR are adapted to low-resolution scenarios.

* Algorithm 1 references $D_{valid}$ without a clear definition. Please provide an explicit expression for $D_{valid}$. Furthermore, it would be interesting to understand the impact of $D_{valid}$’s size on the final output. Were all training images used as $D_{valid}$?

* For the LOKT experiments, please clarify whether the authors retrained their TACGAN and other surrogate models or used pre-trained models. Note that LOKT requires training target models with GANs and surrogate models,  which in this case SSD needs to be performed on every samples.

*  Please specify the number of identities used for attacks and the quantity of reconstructed images generated per identity.

* I would like to see a comparison of the prediction time between SSD and baseline methods like NoDef or other defenses.

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
4

### Summary
This paper proposes a post-processing defense SSD based on conditional mutual information (CMI) especially for defending against black-box model inversion attacks. It theoretically proves that CMI is effective and further reduce modifications to outputs by proposing adaptive rate-distortion framework. Experiment results indicate that SSD achieves SOTA better utility-privacy trade-off.

### Strengths
-	This paper considers defense against model inversion attack from a new perspective by proposing CMI, which provides new insights into this field.
-	It provides thorough theoretical analysis to support the effectiveness of the SSD defense, with a clear and rigorous logical structure.
-	The paper achieves state-of-the-art performance in terms of utility-privacy trade-off and defense against advanced black-box attacks, qualitatively demonstrating its effectiveness.

### Weaknesses
- Key concepts, such as the water-filling method, lack adequate coverage in the main body. While relegated to the appendix, the water-filling method is central to the proposed adaptive rate-distortion framework. Its omission from the main text hinders a comprehensive understanding of the core methodology. Specifically, the paper should elaborate on the rationale behind the choice of water-filling, its algorithmic implementation within the SSD framework, and its impact on the optimization process. 
- The experimental setup omits certain critical information, raising concerns about reproducibility. For instance, the dataset used for GAN prior training is not specified. Different datasets could lead to varying GAN performance, thus impacting the effectiveness of the defense. Additionally, the specifics for Figure 1, such as the exact hyperparameters used for the target model and the defense mechanism, are not provided. Without these details, it is difficult to replicate the results and validate the claims made in the paper.
- The study exclusively benchmarks against state-of-the-art white-box defenses but omits comparisons with black-box defenses. This is a significant oversight, given that the paper focuses on defending against black-box model inversion attacks. Comparing SSD's performance to other black-box defenses would provide a more relevant and accurate assessment of its effectiveness within the intended threat model. For example, the paper could compare against methods that perturb the model's output probabilities or modify the confidence scores to mislead the attacker. The lack of such comparisons weakens the paper's claim of achieving state-of-the-art performance in the black-box setting.

Minor remarks:

- There are also minor errors, such as duplicated words (line 107), inconsistent notation (duplicate use of $p$ at line 215) and typo at line 314.
- The notation is unconventional, such as using non-bold font for vector inputs like $\mathbf{x}$, which reduces consistency with standard notation practices.

### Questions
-	How does SSD perform when the distribution of the public dataset differs significantly from the private dataset (e.g., public dataset = FFHQ, private dataset = CelebA)? Clarification on this point would help to understand SSD’s adaptability under various deployment conditions.
-	The paper states that SSD shows exceptional performance in reducing attack accuracy for LOKT and BREP methods. Could the authors elaborate on why SSD is particularly effective against these specific methods?
-	Could the authors provide additional details on the GAN prior training and any specific hyperparameters used for Figure 1?

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
This paper proposes a post-processing based defense to protect against black-box model inversion attack. The key insight of the paper is to transform the output of the model to reduce conditional mutual information (CMI). This is done to reduce the dependence between the output and the input while preserving the dependence on the true labels. The authors develop a mechanism to transform the model’s prediction to reduce CMI by framing it as an optimization problem. The experimental results on multiple image classification datasets show that their proposed SSD defense provides a better privacy-utility tradeoff compared to prior defenses.

### Strengths
1. The paper is well-written and easy to follow.
2. The idea behind the proposed defense is intuitive and presented well.
3. Experiments seem comprehensive and the defense shows better utility-privacy tradeoff compared to prior defenses in both soft and hard label settings
4. The defense is post-processing based, making it easy to adopt.

### Weaknesses
1. The proposed defense could be susceptible to an adaptive attack. An adversary could query the same input multiple times to obtain multiple predictions from the model. Since the defense produces outputs by perturbing the original prediction, the adversary could compute an average over multiple outputs to get a better estimate of the model’s true output. Such an adaptive attack is not discussed by the paper. Specifically, the defense mechanism relies on adding noise to the model's output, and averaging multiple noisy outputs could effectively cancel out the noise, revealing the underlying prediction. This is a significant vulnerability that needs to be addressed.
2. The defense requires a validation dataset to implement, which could limit its adoption. The requirement of a separate validation set for tuning the defense parameters introduces a practical constraint. In scenarios where such a dataset is not readily available, the applicability of the defense might be limited. This dependence on a validation set makes the defense less flexible and potentially harder to deploy in real-world settings.

### Questions
1. In line 228, the authors state that “the objective function is too complex for the convex optimizer to solve.” and use this as the motivation to minimize a simplified objective $KL(p||q^y)$ instead (by sampling $y\in\mathbb{Y}$). Why is this the original objective too complex? Wouldn’t you be able to use gradient descent to solve for $p$? Would this lead to a better solution?
2. How was the temperature $T$ picked in Algorithm 1?
3. What was the value of $\epsilon$ for the proposed defense in the experiments?
4. Why is the Acc@1 for IR-152 lower for “no defense” compared to prior defenses? This suggests that adding prior defense improves the attack success rate, which is very strange.
5. Can you address the adaptive attack discussed in Weakness#1?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the critical issue of protecting machine learning models from black-box model inversion attacks (MIAs). Specifically, the attacker’s objective is to reconstruct private training data by only accessing the model's outputs.The authors therefore propose a novel defense mechanism named Stealthy Shield Defense (SSD) to post-process the model’s output such that the information revealed by the model’s output about the private data is minimized under constrain. This method leverages Conditional Mutual Information (CMI) to reduce the dependency between the model's output and private data. In addition, they also propose an adaptive rate-distortion framework using water-filling method to preserve the utility while minimizing the CMI.

### Strengths
1. The authors propose SSD, a post-processing defense mechanism that doesn’t require retraining the model, making it practical for real  deployment. 

2. The authors theoretically prove that minimizing CMI serves as a special information bottleneck, therefore minimizing CMI can effectively balance data privacy and utility. By iterating the CMI through all possible labels, the whole dataset can thus be. 

3. The paper introduces an adaptive rate-distortion mechanism optimized using the water-filling method. This approach efficiently calibrates the probability distributions output by the model. 

4. The authors validate their method across various attack algorithms (BREP, Mirror, C2F, LOKT), datasets (FaceScrub, CelebA), and model architectures (VGG-16, IR-152). The results demonstrate that SSD outperforms existing defenses in terms of defense scheme robustness and effectiveness on preservation of model utility.

### Weaknesses
1. Even though the authors claim that the computational overhead is negligible due to the efficient optimization on GPU, a more detailed analysis or benchmarking of the computational cost would greatly support this claim. 

2. Using MI/CMI in deep learning is gaining increasing attention. However, its introduction in related work lacks both depth and breadth, which makes it hard to find the role of this work into the relevant community. 

3. The authors should use a deeper model architecture and higher-dimensional input data for training and prove the effectiveness of the proposed method. When the input data is in high dimensionality, it usually contains a significant amount of irrelevant information. Even worse, since the model depth is also high, the final output, Y ̂, may only contain a small amount of MI with the input, X. I am wondering if optimizing I(X;Y ̂ ∣ Y) will be challenging in this case. 

4. Even though this is a robust scheme against model inversion attack, the authors should discuss about the potential possibility of adaptive attacks. If the adaptive attack is unlikely to happen for now, the authors should also state the reason why.

### Questions
1. The proposed scheme requires iterating over all possible labels to perform the defense. What happens if there are a large number of possible labels? For example, a large company or region may train a face recognition model that includes thousands or millions of faces. Will this scale slow down the defense and become a bottleneck? I suggest some detailed computational analysis.

2. As the authors pointed out in the paper, X→Z→Y ̂ is a Markov chain. It is possible that when input data has large dimensionality, or the model has very deep layers. Under this circumstance, it is likely that Y ̂ shares very little information with X. The derived MI I(X;Y ̂ ∣ Y) will have such a small value that could be hardly optimized. Does the proposed scheme still hold effective in this scenario? The authors should provide more empirical/theoretical analysis to justify this. 

3. Are there any manifest adaptive attack schemes that can target at this defense? How difficult is it to design/launch such attacks?

### Soundness
4

### Presentation
3

### Contribution
3
