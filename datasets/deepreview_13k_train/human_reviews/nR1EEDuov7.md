# Securing Deep Generative Models with Universal Adversarial Signature

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Recent advances in deep generative models have led to the development of methods capable of synthesizing high-quality, realistic images.  These models pose threats to society due to their potential misuse. Prior research attempted to mitigate these threats by detecting generated images, but the varying traces left by different generative models make it challenging to create a universal detector capable of generalizing to new, unseen generative models. In this paper, we propose to inject a universal adversarial signature into an arbitrary pre-trained generative model, 
in order to make its generated contents more detectable and traceable. First, the imperceptible optimal signature for each image can be found by a signature injector through adversarial training. Subsequently, the signature can be incorporated into an arbitrary generator by fine-tuning it with the images processed by the signature injector. In this way, the detector corresponding to the signature can be reused for any fine-tuned generator for tracking the generator identity. The proposed method is validated on the FFHQ and ImageNet datasets with various state-of-the-art generative models, consistently showing a promising detection rate.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Injecting a universal adversarial signature into an arbitrary pre-trained generative model, in order to make its generated contents more detectable and traceable.

### Strengths
The motivation is explained clearly. 
The paper is well-written.

### Weaknesses
The performance with or without the adversarial signature should be presented.
The term universal in used incorrectly since the signature depends on each image.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a simple idea of finetuning image generator models to embed an adversarial noise signature into the generated images, so that the resulting images can be easily detected by a classifier. This has been achieved in two steps: first learning a signature injector W together with the detector F, and then finetuning the generator G to produce these signatures. Experiments have shown that the inserted signatures are easily detectable by the detector F.

### Strengths
1) The papers deals with an important problem regarding the safety of generative models and proposes an innovative solution.
2) The proposed solution intuitively makes sense and is also feasible in practice. 
2) The paper is well-written and easy to follow.

### Weaknesses
There are five main concerns about the proposed solution.

1) Firstly, the model F has been primarily described as a binary classifier whose goal is to distinguish between real images and "signed" synthetic images. What happens when the classifier F is fed with an "unsigned" synthetic image (i.e., an image generated from the original generator instead of the finetuned generator)? Shouldn't it be trained in such a way to detect "unsigned" synthetic images to the best possible extent along with "signed" synthetic images. Otherwise, why is a deep model such as ResNet-34 required to detect such "signed" images (a much smaller network should be enough to perform this relatively simpler task)?

2) The proposition 3.3 on persistency against image restoration attacks does not appear to be logical. Why would an attacker try to add noise e to the original image and learn a model M such that M(W(x+e)) = x. Instead the goal of the attacker would be to find e such that W(x)+e = x. In fact, even this image restoration task would not be required if the goal of the attacker is to simply bypass the detector F. The attacker has to just mount a simple adversarial attack to fool the detector F, i.e., add noise to W(x) such that F(W(x)) = real.

3) In terms of experiments, it is surprising that there is no comparison with a simple post-hoc watermarking approach (just add a unique generator-specific watermark to the generated image and categorize images with the watermark as synthetic), though this idea has been discussed in the introduction. It is true that the watermark will be decoupled from the generator, but it would still achieve the stated goals (imperceptibility, persistence, provenance of the generator, etc.). Also, the main paper does not talk about the ability to the detector to work under various image transformations. Only the appendix talks briefly about JPEG compression and cropping. How will the proposed detector work under various image transformations such as different levels of lossy compression, affine transformations, resolution and image format changes, etc.

4) Finally, there has to be more clarity on the threat model for the proposed solution. Specifically, who owns the generator and who will own the detector and what are their motivations? For instance, if the owner of the generator model is not honest (they want to hide their identity), why would they insert the signature in the first place? If a third-party is finetuning the generator, why would the users trust the finetuned model released by the third-party in place of the original model released by the owner. Similarly, who will own the detector and what happens when the owner of the detector is not honest? The proposed solution envisages that both the signature detector and detector are learned jointly. How will this be possible if the owners are different? Who will enforce the rule that every generated image must be signed? If there is no enforcer, the problem again boils down to detecting unsigned synthetic images where generalization is the core issue.

5) How is the proposed approach different from model poisoning attacks? The goal is to insert an "imperceptible" trigger pattern into the generated images such that the machine learning model will be easily triggered by these patterns and output  a specific decision (in this case, the synthetic class). One could potentially take any real vs. synthetic classification model and poison it to achieve this goal. Then, one has to just add the trigger to the generated images.

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the detection methods for images generated by generative models and proposes to track the generated images by using adversarial signatures to make them more easily recognized by the designed detectors. Specifically, this paper constructs a signature injector W for learning to generate adversarial signatures and a classifier F for learning how to detect the images generated by W. Then, W and F are jointly trained. After that, the samples generated by W are then applied to finetune the original generative model G to obtain G'. The author elaborately designed the loss function as well as the binary code, and it has been shown through extensive experiments that the method can achieve good results.

### Strengths
(1)	This paper introduces adversarial examples into the detection of images generated by generative models, combined with joint training and watermark fine-tuning, which is novelty;
(2)	For the generation model, this paper investigates the latest diffusion-based generation model, which is of good practical significance under the common use of AIGC nowadays;
(3)	This paper is well-structured and logical. The author reviews the effectiveness and limitations of the proposed method from multiple perspectives. It points out the existing challenges, and gives possible solutions.

### Weaknesses
 (1) The two SOTA detection methods compared in the experiment are against the CNN-based and GAN-based generative model, whether there is any relevant paper for the watermarking of the diffusion model at present, if so, please supplement;
(2) Missing a lot of experimental data on ImageNet, please add results comparing with SOTA on ImageNet;
(3) Some formatting issues: (1) Please cite the graphs in order; (2) Please distinguish between periods and semicolons within the algorithm; (3) Please give the value of lamda in Figure 7.
(4) The authors should indicate possible future directions in conclusion

### Questions
(1)	Fine-tuning an arbitrary G with samples generated by W to get G' is not unseen, in a sense it is inserting a backdoor that allows F to be better detected;
(2)	What is the difference between binary coding and multiclassification loss? What is the advantage of the binary coding?
(3)	I'm curious whether some of the latest adversarial defense methods can break this adversarial signature, such as diffusion-based purification. It would be great to add some experimental results in this scenario.
(4)	It mentioned in Sec5.2 that “The complexity of re-training a detector every time upon the release of a new generator is O(r^2)”, I wonder how to calculate this. For each new generator, the method of re-training a detector only needs to re-training once for the new generator.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the topic of adversarial signatures within the realm of generative models. At its core, the research introduces a method that involves the integration of a signature injector and a classifier. The ideal scenario is when the classifier can distinguish images that have been signed from the original, clean images based on subtle, almost imperceptible alterations made by the injector.

The research also explores the idea of securing generative models by embedding adversarial signatures directly into the model's parameters, potentially through a fine-tuning process. By doing so, the outputs from these secured generators inherently carry the adversarial signatures, making them detectable by the classifier.

The methodology involves processing training data with the signature injector to produce signed images. An existing generative model is then fine-tuned using these signed images, ensuring that the images it generates carry the adversarial signatures.

### Strengths
Originality:
Innovative Approach: The paper introduces a unique method centered around adversarial signatures within the realm of generative models. This approach, which involves the integration of a signature injector with a classifier, offers a fresh perspective in the domain of adversarial defenses.

Quality:
Comprehensive Methodology: The paper's methodology, which encompasses the processing of training data with a signature injector followed by the fine-tuning of an existing generative model, is thorough. This structured approach suggests a well-thought-out experimental setup.


Clarity:
Structured Presentation: The paper appears to be well-organized, with clear sections detailing the introduction of the signature injector and classifier, the methodology, and the broader context of adversarial signatures within generative models. This structured approach aids in understanding the paper's flow and main contributions.

Significance:
Addressing a Crucial Challenge: The paper's focus on adversarial signatures within generative models addresses a significant challenge in deep learning. Given the importance of adversarial defenses in various applications, the paper's contributions in this area are relevant.

### Weaknesses
Originality:
Delineation from Existing Methods: The paper could benefit from a clearer differentiation from existing methods in the domain of adversarial signatures or defenses. Without specific comparisons or benchmarks, it's challenging to gauge the unique contributions of the proposed method. It is unclear how this method compares to techniques that use watermarking or fingerprinting for generative models, especially in terms of robustness against removal or circumvention.

Quality:
Lack of Detailed Experimental Results: The paper's methodology is described, but without detailed experimental results or comparisons, it's difficult to assess the effectiveness and robustness of the proposed approach. Comprehensive experiments or evaluations against benchmark methods would enhance the paper's credibility. Specifically, the paper lacks quantitative metrics demonstrating the detection rate of the adversarial signatures under different conditions, such as varying levels of noise or image transformations. It also does not provide a clear comparison against baseline methods for detecting generated content.

Potential Overfitting: The approach of fine-tuning a generative model with signed images raises concerns about overfitting. If the model is too closely tailored to the signed images, its generalizability to unseen data or different adversarial attacks might be limited. The paper does not provide sufficient analysis to demonstrate that the fine-tuned model retains its original generative capabilities and does not simply memorize the injected signatures.

Clarity:
Need for Enhanced Technical Details: While the paper presents its concepts, more in-depth technical explanations or visual aids, such as diagrams or flowcharts, would help readers better understand the intricacies of the proposed method. For example, the exact mechanism of the signature injector and how it modifies the images is not clearly explained. The paper would benefit from a more detailed description of the classifier architecture and its training process.

Significance:
Unclear Practical Implications: The paper lacks a discussion on the practical implications or real-world applications of the proposed method. Understanding how this approach can be applied in real-world scenarios or its impact on existing systems would enhance its significance. It is not clear how this method would be used in practice to verify the authenticity of generated content or to track the source of a generative model.
Questions on Scalability and Generalizability: The paper's focus on a specific approach to adversarial signatures within generative models raises questions about the method's scalability to larger datasets or more complex models. Additionally, its generalizability to other types of adversarial attacks or different domains remains unexplored. It is unclear if the method would be effective on different types of generative models or if it would be robust against different types of manipulations of the generated images.

### Questions
Comparison with Existing Methods:
How does your approach to adversarial signatures differentiate from existing methods in the domain? Can you provide specific comparisons or benchmarks that highlight the advantages of your method?

Experimental Validation:
Could you provide more detailed results of your experiments, especially in comparison with state-of-the-art methods? How does your method perform in terms of robustness and effectiveness against various adversarial attacks?

Overfitting Concerns:
How do you address potential overfitting when fine-tuning the generative model with signed images? Have you conducted experiments to assess the model's generalizability to unseen data or different types of adversarial attacks?

Practical Implications:
What are the real-world applications of your proposed method? How does it impact existing systems or applications that utilize generative models?

Scalability and Generalizability:
How scalable is your method, especially when applied to larger datasets or more complex models? Have you tested its generalizability across different domains or types of adversarial attacks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
