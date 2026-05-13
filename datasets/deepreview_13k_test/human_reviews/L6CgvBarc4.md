# Bag of Tricks to Boost Adversarial Transferability

- Decision: Reject
- Scores: 6, 8, 5, 6

## Abstract
Deep neural networks are widely known to be vulnerable to adversarial examples. However, vanilla adversarial examples generated under the white-box setting often exhibit low transferability across different models. Since adversarial transferability poses more severe threats to practical applications, various approaches have been proposed for better transferability, including gradient-based, input transformation-based, and model-related attacks, \etc. In this work, we find that several tiny changes in the existing adversarial attacks can significantly affect the attack performance, \eg, the number of iterations and step size. Based on careful studies of existing adversarial attacks, we propose a bag of tricks to enhance adversarial transferability, including momentum initialization, scheduled step size, dual example, spectral-based input transformation, and several ensemble strategies. Extensive experiments on the ImageNet dataset validate the high effectiveness of our proposed tricks and show that combining them can further boost adversarial transferability. Our work provides practical insights and techniques to enhance adversarial transferability, and offers guidance to improve the attack performance on the real-world application through simple adjustments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates transfer-based adversarial attacks and proposes a series of simple yet effective tricks to enhance the adversarial transferability of different category of attack methods. The authors conduct extensive experiments to demonstrate how individual trick can help crafting adversarial example and combining them together can significantly improve the attack performance on various defense models and Google vision API.

### Strengths
It is good empirical study work with detailed experiments.

### Weaknesses
- Although the tricks are simple and the technical novelty is limited, the authors do provide many insights into the limitations of existing methods. The limitations and corresponding solutions are well explained and hence easy to understand and follow.

- The experiments are thorough and well conducted overall, and a lot of statistical details are well presented regarding the comparison studies.

- In section 3.1 hyper-parameters study, the authors choose seven FGSM based approaches for the comparison study, however for tricks described in section 3.2, 3.3 & 3.4, only five methods are selected as shown in Table 1, 2, & 3. Why not keep in consistent in all the comparison study for gradient based attacks?

- For ensemble based attack, a recent study [1] is not compared. I am wondering if any of the tricks applies as well.

- For input transformation methods in related works, previous study [2] is not properly discussed as well.

### References
[1] Chen, H., Zhang, Y., Dong, Y., & Zhu, J. (2023). Rethinking Model Ensemble in Transfer-based Adversarial Attacks. arXiv preprint arXiv:2303.09105

[2] Dong, Y., Pang, T., Su, H., & Zhu, J. (2019). Evading defenses to transferable adversarial examples by translation-invariant attacks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4312-4321)

### Questions
See weakness above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a comprehensive set of tricks to boost the adversarial transferability of existing transfer-based black-box attack methods. These tricks are tailored to different categories of attacks, including iterative gradient-based attacks (e.g., global momentum initialization,
scheduled step size, and dual example), input transformation-based attacks (e.g., spectral-based input transformation), and model-related ensemble attacks (e.g., gradient alignment, asynchronous input transformation, and model shuffle). An extensive study on tweaking the
fundamental but seemingly trivial hyper-parameters, such as the number of iterations, step size, and momentum coefficient, is also carried out. The proposed bag of tricks provides valuable insights into influencing factors of adversarial transferability and techniques for enhancing it.
Relevant research directions, such as developing novel and more robust defense methods for DNNs, could be inspired by this paper’s findings.

### Strengths
1. [Originality]:
• This is a valuable work that integrates and analyzes multiple factors contributing to adversarial transferability.
2. [Quality]:
• Experiments are extensive for validating the effectiveness and generality of their proposed tricks; for example, multiple surrogate models are used, including VGG-16, ResNet-18, DenseNet-121, and ViT.
• The tricks are proposed with a decent logical flow: the former trick’s weaknesses become the later trick’s motivation and hypothesis to verify.
3. [Clarity]:
• Detailed experiment settings and algorithm descriptions are provided in the Appendix.
• At the end of each subsection of an empirical study, there’s a “Takeaways” section that summarizes the authors’ observations and insights.
• At the end of each subsection of a proposed trick, there’s a “Results” section that analyzes the attack success rate (ASR) results, concludes the functionality and mechanism of the specific trick, and validates the author’s hypothesis if there’s one. Important key sentences are also highlighted in italic fonts.
• At the outset of each subsection of a proposed trick, the motivation and reasoning behind the proposal, as well as the authors’ hypothesis, are provided.
• Abundant plots, charts, and tables are provided to display the results across multiple methods and tricks, which is convenient and easy for readers to compare.
• Ablation study of various combinations of tricks is provided.
4. [Significance]:
• According to Table 5, the authors’ combined tricks yield the highest ASR across multiple defense methods and even 100% ASR on Google Vision API. Particularly, comparing their approach to the runner-up method, there’s a remarkable 18.1% improvement against the most powerful defense method – Random Smoothing (RS). This simulates a new line of research regarding effective defense design against attacks with high adversarial transferability.

### Weaknesses
Some minor typos:
• On page 3, at the beginning of Section 3, you stated: “We use eight surrogate/victim models, comprising...”. There should be seven only: 5 CNNs – VGG-16, ResNet-18, ResNet-101, DenseNet-121, and MobileNet; 2 transformers – ViT and Swin.
• On page 7, on the second last line of the Hyper-parameter study section, “achieves” should be “achieved”.
2. You provided explanations and insights or viewpoints for most of the observations you made from the experimental results but not each. Although some might be obvious, it’s still better that you provide a sentence or two explaining each observation. Specifically, for example:

• In Fig. 2(a), why GIMI-FGSM peak at T=5, which differs greatly from other gradient- based attack methods?
• In Fig. 2(b), why excessively large step sizes can harm attack performance?
• In Fig. 2(c), why does the performance degradation occur when the momentum decay factor is less than one, indicating momentum increase?
3. It would be better if results on speech applications could also be provided.
4. It would be better if recommended future defense directions could be provided.

### Questions
1. In Fig. 1, which tricks exactly are being used for the integrated tricks (the orange bar)?
2. You mentioned: “we choose 10,000 images from the ImageNet-1K dataset as our evaluation set.” How the 10,000 images were chosen? You also didn’t mention which
dataset you used to generate adversarial examples. Is it also ImageNet-1K?
3. For ensemble strategies, was there a specific reason why you used MI-FGSM attack to create adversarial perturbations? Would it be better if you provided more results with other attack methods to even strongly validate the effectiveness of ensemble strategies?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a bag of tricks to boost the transferability of adversarial examples, including techniques for gradient-based attacks, input transformation-based attacks, and ensemble attacks. The proposed tricks are evaluated extensively on ImageNet, against defense methods and Google Cloud Vision. Combining tricks boosts success rates, highlighting their complementary nature.

### Strengths
The paper tackles an important problem - improving adversarial transferability. The bag of tricks enhances attacks without architectural changes. The tricks are intuitive and easy to implement, requiring only minor modifications to existing methods.

### Weaknesses
1. For each model and attack, the ideal hyperparameters, including the iteration count and the scheduled step size, require fine-tuning, and the study lacks of theoretical direction for this.
2. While the tricks enhance transferability, the computational overhead and training time increase from additional steps like random initializations.
3. Effects of tricks diminish with certified defenses. More analysis is needed on certified robustness.

### Questions
See the above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work investigates the potential tricks to improve the adversarial transferability of existing works. Specifically, the authors study number of iterations, scale factor, momentum decay factor, momentum initialization, step size scheduling, dual example, input transformation, and ensemble. The evaluation covers various baselines with their variants on ImageNet.

### Strengths
1. The paper is well-organized and easy to follow.
2. The evaluation is extensive, including both CNNs and ViTs, and covers several important aspects that could influence adversarial transferability.
3. The results could benefit the adversarial transferability community.

### Weaknesses
1. Lack of in-depth analysis. Although the authors provide extensive evaluation of various techniques, it is difficult to see the in-depth analysis to provide more insights. For example, the authors discuss the hyper-parameters study in Section 3.1. Given different patterns, how these patterns inspire new research and why these patterns exist deserve more discussion instead of simple optimal hyper-parameters takeaways.
2. Since the authors discuss various aspects that could influence adversarial transferability, it is important to discuss the orthogonality and the effectiveness of different combinations. Although part of the results is shown in Table C2, there are no comprehensive results as well as valuable analysis.
3. The covered baselines are mainly before 2022. However, there exist many recent works on adversarial transferability, such as [a, b, c, d].

[a]. Transferable Adversarial Attack for Both Vision Transformers and Convolutional Networks via Momentum Integrated Gradients. ICCV 2023.

[b]. Transferable Adversarial Attacks on Vision Transformers with Token Gradient Regularization. CVPR 2023.

[c]. Improving Adversarial Transferability via Neuron Attribution-based Attacks. CVPR 2022.

[d]. Boosting the transferability of adversarial attacks with reverse adversarial perturbation. NeurIPS 2022.

### Questions
1. Please provide more in-depth analysis to clarify the contribution.
2. Please provide more evaluation and analysis of orthogonality and the effectiveness of different combinations.
3. Please involve more comparison and discussion with recent work.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
