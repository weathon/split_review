# Leveraging Optimization for Adaptive Attacks on Image Watermarks

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Untrustworthy users can misuse image generators to synthesize high-quality deepfakes and engage in unethical activities.  
Watermarking deters misuse by marking generated content with a hidden message, enabling its detection using a secret watermarking key.
A core security property of watermarking is robustness, which states that an attacker can only evade detection by substantially degrading image quality. 
Assessing robustness requires designing an adaptive attack for the specific watermarking algorithm.  
When evaluating watermarking algorithms and their (adaptive) attacks, it is challenging to determine whether an adaptive attack is optimal, i.e., the best possible attack.
We solve this problem by defining an objective function and then approach adaptive attacks as an optimization problem.
The core idea of our adaptive attacks is to replicate secret watermarking keys locally by creating \emph{surrogate keys} that are differentiable and can be used to optimize the attack's parameters. 
We demonstrate for Stable Diffusion models that such an attacker can break all five surveyed watermarking methods at \revised{no visible degradation} in image quality.
\revised{Optimizing our attacks is efficient and requires less than 1 GPU hour to reduce the detection accuracy to 6.3\% or less. }
Our findings emphasize the need for more rigorous robustness testing against adaptive, learnable attackers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Untrustworthy users can misuse image generators to synthesize high-quality deep-
fakes and engage in online spam or disinformation campaigns. Watermarking de-
ters misuse by marking generated content with a hidden message, enabling its
detection using a secret watermarking key. A core security property of water-
marking is robustness, which states that an attacker can only evade detection by
substantially degrading image quality. Assessing robustness requires designing
an adaptive attack for the specific watermarking algorithm. A challenge when
evaluating watermarking algorithms and their (adaptive) attacks is to determine
whether an adaptive attack is optimal, i.e., it is the best possible attack. We solve
this problem by defining an objective function and then approach adaptive attacks
as an optimization problem. The core idea of our adaptive attacks is to replicate
secret watermarking keys locally by creating surrogate keys that are differentiable
and can be used to optimize the attack’s parameters. The authors demonstrate for Stable
Diffusion models that such an attacker can break all five surveyed watermarking
methods at negligible degradation in image quality. These findings emphasize the
need for more rigorous robustness testing against adaptive, learnable attackers.

### Strengths
Paper is well formatted

Topic is interesting

Good balance of theory and experiments

### Weaknesses
Please improve readability

Please number all equations

Please discuss figures, tables and algorithms clearly in the text

Please add a security analysis to known attacks in this domain

### Questions
Why is this topic important?

What are the future work directions of this work?

Why is the comparative analysis limited

What is the complexity of the algorithms?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors emphasize the significance of watermarking in countering misuse by marking generated content with hidden messages. The core security property of watermarking, robustness, is investigated in this paper. The authors assert that evaluating robustness involves creating adaptive attacks tailored to specific watermarking algorithms. To this end, one of the paper's contributions is the proposed approach to assess the optimality of adaptive attacks by framing them as an optimization problem and defining an objective function. The paper presents evidence that such attackers can effectively break all five surveyed watermarking methods with negligible degradation in image quality.

### Strengths
First, on the aspect of the paper’s organization, this manuscript is well-organized and easy to follow. Second, on the aspect of clarity, the proposed method is clearly defined using schematics and pseudo-code descriptions. Third, this paper provides an approach to evaluating adaptive attacks and the demonstration of their effectiveness provide a fresh perspective on the challenges faced in countering image manipulation.

### Weaknesses
The motivation and importance of the proposed method are not clear enough, e.g., what problems did the previous works exist? Besides, the experiments comparison and discussion are weak. Experiment section should expand the scope of discussion, compare with more advanced methods, and provide in-depth discussions.

### Questions
1.	ABSTRACT: The text should include more details to the proposed methodology, numerical results achieved, and comparison with other methods
2.	Could you tell me the limitations of the proposed method? How will you solve them? Please add this part to the manuscript.
3.	The abbreviations must appear at the very first place that the terminology is introduced and the way of introducing the terms must be consistent throughout the manuscript from abstract to conclusion.
4.	The conclusions should be improved such that the authors add some analytical terms.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method for performing adaptive attacks against image watermarking methods, allowing for more accurate evaluations of the robustness of watermarking methods against motivated attackers. To enable standard adversarial optimization attacks against known but non-differentiable watermarking methods, the authors propose to train surrogate (differentiable) watermark detection networks. Experiments show that adaptive attacks crafted with the proposed method significantly degrade the effectiveness of all evaluated watermarking methods and outperform non-adaptive attacks while preserving the overall perceptual quality of attacked images.

### Strengths
The issue of watermarking the outputs of generative models is timely and interesting.

The idea of training differentiable surrogates for arbitrary watermarking methods is an interesting threat model.

The selection of baseline watermarking methods is reasonable and includes both "post-hoc" (low-perturbation) and "semantic" (high-perturbation) methods.

The autoencoder/compression-based attack is interesting and seems to effectively remove watermarks while retaining high perceptual quality.

### Weaknesses
I think there is a terminology issue in the paper that could be confusing for readers. It appears the watermark "key" referenced in the paper more closely matches the concept of a watermark "detector" algorithm in methods such as RivaGAN and Tree-Rings; many methods often use "key" and "message" interchangeably to refer to the hidden signal. If this is true, the authors' proposed training of differentiable surrogate "keys" can be understood as training differentiable surrogate detector networks that predict the key/message concealed in a watermarked image --  allowing for gradient-based optimization attacks on non-differentiable detectors. The pseudocode in Algorithm 1 strongly suggests this. If this is the case, I urge the authors to revise their terminology to make this more clear.  
  
- - - -

It should be clarified that in the general no-box watermarking scenario, the second step $\mathrm{EMBED}$ need not modify the parameters of the generator model, just endow it with watermarking capabilities (e.g. by applying a post-hoc watermarking algorithm to its outputs). As far as I can tell, none of the methods evaluated in the paper modify the generator parameters directly. Overall, the no-box watermarking steps and their instantiations for each of the evaluated watermarking methods are not clearly explained.
  
- - - -

The proposed method is similar to that of Jiang et al. [5] in that it adversarially parameterizes image transformations to remove watermarks. The authors claim that the method of Jiang et al. requires access to a watermarking "key;" however, Jiang et al. propose attacks under the explicit assumption that the attacker does not have access to the ground-truth key/message (which is either approximated via the detector model's predictions or sampled at random) -- from pp.6, "the attacker does not have access to the ground-truth watermark $w$".  On the other hand, if I am correct that the authors take "key" to mean "detector," this claim makes more sense in that Jiang et al. use full access (white-box) or query access (black-box) to the detector to craft attacks. 

The authors should clarify their statements about the prior work of Jiang et al. and the distinctions between their methods. And while additional experiments may not be feasible at this point for various reasons, I think the paper would be much stronger if it included comparisons between the proposed approach and either or both attack variants proposed by Jiang et al. This would also require modifying the proposed attack to evade two-tailed detection, as discussed by Jiang et al.

- - - -

If the attacker "does not need to invoke GKEYGEN" for TRW/WDM/RivaGAN, as stated in section 4.2, does this mean the attacker does not train a differentiable surrogate detector? In this case, doesn't the proposed approach just become a standard white-box attack, as in Jiang et al.?

- - - -

The authors do not provide any details of the architecture of the surrogate detector networks $\theta_D$ trained by the adversary. This seems like a crucial aspect of the proposed approach, so it is strange that it is not discussed.

- - - -

The related work section mixes references to image classifier watermarks [1][2] and watermarks for generative models [3], which are very different: the former aims to protect the intellectual property of a model developer, typically through query- or trigger-based verification, while the latter is embedded in all outputs of a generative model to distinguish real from fake content. This paper is concerned with the latter kind of watermark, so I'm confused by the emphasis on works in the former area. At the very least, these two different types of works should be clearly distinguished from one another in the related work section.

- - - -

As far as I can tell, the term "Adaptive Attack" comes from the adversarial example literature -- the authors should explain what distinguishes an adaptive attack from a non-adaptive attack and probably cite the original work [4].

- - - -

Figure 1 is missing step #8 (it skips from 7 to 9).

- - - -

This is a much smaller concern, but the substitution of the Stable Diffusion v1 generator for v2 does not seem like a very difficult obstacle for the attacker to overcome, given the general similarities in architecture and training. Attacks on post-hoc methods probably shouldn't be affected too much by the choice of surrogate generator, but Tree-Rings is deeply intertwined with the generator structure. Therefore, it would be interesting to see how attacks on TRW fare when there is a more substantial mismatch between the actual and surrogate generator.

- - - -

Overall, I think the central idea -- no-box watermark attacks with differentiable surrogates -- is very interesting, and the experimental results look very strong. However, I think the paper has many issues that still need to be addressed.


[1] Nils Lukas, Edward Jiang, Xinda Li, and Florian Kerschbaum. Sok: How robust is image classification deep neural network watermarking? In 2022 IEEE Symposium on Security and Privacy
(SP), pp. 787–804. IEEE, 2022.

[2] Arpit Bansal, Ping-yeh Chiang, Michael J Curry, Rajiv Jain, Curtis Wigington, Varun Manjunatha, John P Dickerson, and Tom Goldstein. Certified neural network watermarks with randomized smoothing. In International Conference on Machine Learning, pp. 1450–1465. PMLR, 2022.

[3] Yuxin Wen, John Kirchenbauer, Jonas Geiping, and Tom Goldstein. Tree-ring watermarks: Fingerprints for diffusion images that are invisible and robust. arXiv preprint arXiv:2305.20030, 2023.

[4] Nicholas Carlini and David Wagner. Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods. In AISec '17: Proceedings of the 10th ACM Workshop on Artificial Intelligence and Security, pp.3-14. 2017.

[5] Zhengyuan Jiang, Jinghuai Zhang, and Neil Zhenqiang Gong. Evading watermark based detection of ai-generated content. arXiv preprint arXiv:2305.03807, 2023.

### Questions
Did the authors train surrogate detectors for all the evaluated watermarking methods to create true no-box attacks?

Did the authors experiment with different degrees of attacker knowledge -- e.g., what if the attacker does not know the length of the watermark embedded by the actual generator? Would training on 32-bit messages cause attacks on a 64-bit message system to fail?

Rather than training surrogate detectors to reconstruct embedded messages, did the authors consider simply training a binary classifier on watermarked and un-watermarked images from the surrogate generator and then performing an adversarial attack on the binary classifier? This seems like the simplest no-box approach.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an objective function and approaches adaptive attacks as an optimization problem to evaluate the robustness of watermarking algorithms.  The core idea of the proposed adaptive attack is to replicate secret watermarking keys locally by creating surrogate keys that are differentiable and can be used to optimize the attack’s parameters. The experiments reveal that this type of attacker can successfully compromise all five surveyed watermarking methods with minimal degradation in image quality. These findings underscore the necessity for more comprehensive testing of the robustness of watermarking algorithms against adaptive, learnable adversaries.

### Strengths
This paper proposes a practical method of empirically testing the robustness of different watermarking methods. The proposed adaptive attack is shown to be effective against different watermarking methods.

### Weaknesses
1. The attack requires the knowledge of the watermarking algorithm. 
2 in the experiments the surrogate generator and the watermark generator exhibited a high degree of similarity, which may not be as practical in real-world scenarios.

### Questions
1 The paper shows that generates a single surrogate key and can evade watermark verification which indicates that the private key seems to have little impact. Is it possible that the less impact comes from the high similarity between the surrogate generator and the watermark generator?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
