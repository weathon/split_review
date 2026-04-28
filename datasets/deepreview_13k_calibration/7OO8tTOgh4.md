# Non-targeted Adversarial Attacks on Vision-Language Models via Maximizing Information Entropy

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Adversarial examples pose significant security concerns in deep neural networks and play a crucial role in assessing the robustness of models. Nevertheless, existing research has primarily focused on classification tasks, while the evaluation of adversarial examples is urgently needed for more complex tasks. In this paper, we investigate the adversarial robustness of large vision-language models (VLMs). We propose a non-targeted white-box attack method that maximizes information entropy (MIE) to induce the victim model to generate misleading image descriptions deviating from reality. Our method is thoroughly analyzed experimentally, with validation conducted on the ImageNet dataset. The comprehensive and quantifiable experimental results demonstrate a significant success rate achieved by our method in adversarial attacks. Given the consistent architecture of the language decoder, our proposed method can serve as a benchmark for evaluating the robustness of diverse vision-language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes  adversarial attacks on Visual Language Models (VLMs), as illustrated in Figure 1. A clean image is perturbed slightly so that a VLM generates a wrong description of the image. In this paper, the attacks are "non-targeted" in that the goal is to cause the description to change to anything, and not something specific. 

A concern with the paper is that prior work, e.g., (Carlini 2023), which is cited in the paper, also solves a pretty similar problem, but the contribution over that work  is not clearly stated. For instance, see page 20 of (Carlini 2023) in which the image of Mona Lisa was adversarially perturbed to cause a completely incorrect description to be output. Why couldn't the same techniques be used here and what precisely is the contribution over (Carlini 2023) or similar work? I would have liked to see the difference with the closest works highlighted in the Intro. 

In the Related Work section, it seems that the main difference claimed is that prior adversarial attacks on VLMs are targeted, whereas authors propose an untargeted attack (as an aside, if this is the crucial contribution -- I think that should have been stated in the Intro clearly). But, even accepting the author's premise that untargeted attacks weren't addressed by prior work, why (1) is an untargeted attack important; (2) not a special case of a targeted attack where a target is picked at random from the desired domain, thus turning an untargeted attack into a targeted attack and using a prior solution.

### Strengths
The specific algorithm for doing an untargeted attack seems to be different from prior work in VLMs. The authors propose injecting adversarial noise that maximizes the entropy  -- thus effectively causing the resulting image to produce essentially a random caption. They propose three different ways of maximizing entropy and use a weighted combination of the three methods as the objective function (as shown in Algorithm 1).  They find that the first method (equation 2) dominates overall (weight ended up as 0.8). An ablation study would  have been nice to show how each way (equation 2, 3, or 4) would have performed by itself versus the  weighted combination of the three.

### Weaknesses
 A concern with the paper is that prior work, e.g., (Carlini 2023), which is cited in the paper, also solves a pretty similar problem, but the contribution over that work  is not clearly stated. For instance, see page 20 of (Carlini 2023) in which the image of Mona Lisa was adversarially perturbed to cause a completely incorrect description to be output. Why couldn't the same techniques be used here and what precisely is the contribution over (Carlini 2023) or similar work? I would have liked to see the difference with the closest works highlighted in the Intro.

In the Related Work section, it seems that the main difference claimed is that prior adversarial attacks on VLMs are targeted, whereas authors propose an untargeted attack (as an aside, if this is the crucial contribution -- I think that should have been stated in the Intro clearly). But, even accepting the author's premise that untargeted attacks weren't addressed by prior work, why (1) is an untargeted attack important; (2) not a special case of a targeted attack where a target is picked at random from the desired domain, thus turning an untargeted attack into a targeted attack and using a prior solution.

 An alternate way would be to simply feed some random image that is clearly maximum entropy to the VLM, get a few words of text from it (essentially a random phrase) and then use a targeted attack on the VLM to generate that particular or similar text. I would have liked to see a comparison with such an approach in the paper.

As an example, couldn't "a pair of flip flops sitting on a pile of garbage" in Appendix A.1 first row  be set as the target caption in Carlini 2023 and then a perturbation found that achieves that? Or any other random caption for that matter?

Wouldn't the captions just become random sequence of words as the attack progresses? The figures in Appendix A should probably illustrate that, if that is the case. And if that is the case, is such an attack considered successful? Or should the caption generally make sense to a human?

### Questions
Can the Intro be revised to identify the closest work to the paper and identify the key contribution over that work (or minor variants of prior work)? 

Why can't untargeted attacks use a method for targeted attacks as a subroutine to achieve an untargeted attack? Note that there is precedence for this in adversarial ML. In the OPT method for blackbox adversarial attacks, the fundamental method is for a targeted attack. The OPT paper discusses how to do an untargeted attack by wrapping a small amount of code around a targeted attack. An example strategy would be to choose a random target and then attempt a targeted attack.

Why are untargeted attacks on VLMs particularly interesting, given that we already know that targeted attacks are possible and how to do them?

Can an ablation study be presented to show how each entropy method performs on its own (e.g., lambda_1 = 1, others 0, etc.), versus the chosen setting for lambdas of (0.8, 0.1., 0.1).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new attack on VLM. They utilize the PGD optimization algorithm to maximize the entropy of the predicted token entropy, attention weights, and normalized hidden layers values. They show empirically that their attack is effective in attacking sevral open-source VLMs.

### Strengths
- The topic of robustness of VLMs is relevant. 
- The experimental results show the effectiveness of the attack.

### Weaknesses
 - The technical contribution is on the moderate side. However, to the best of my knowledge using maximum entropy to adversarial attack is novel.   
- the paper lacks comparison to related work. There are several attacks on image captioning in the literature. The paper lacks a comparison against them (see for example, [1] and [2]). The authors mention [2] in the related work but did not empirically compare against it, they justify it as this method uses the original caption. This, however, is a minor requirement as it can be mitigated by treating the caption on the clean image as the ground-truth caption.   

### Questions
- There are hyper-parameters for the attacks $\lambda_1,\lambda_2,\lambda_3$. Are these selected based on the same validation set?  If so I believe the experiment might lack statistical integrity.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study achieves non-targeted attacks on VLMs by maximizing the entropy of network output, attention, and features.

### Strengths
* The content of the paper is very easy to understand.

### Weaknesses
 * Lack of comparative methods. Many methods have already been proposed for attacking VLMs[1], but the authors did not compare with these methods during the experimental phase, choosing only simple Gaussian noise for comparison.

* The approach in the paper is somewhat ad-hoc. There are various ways to disrupt the expressions in network layers, such as maximizing the norm of mid-layer features. Why did the authors choose to maximize entropy for the attack? The rationale behind this was not clarified in the paper.

* Absence of ablation studies. The final attack method in the paper is composed of three losses, but the authors did not discuss the impact of different loss coefficients on the results within the article.

* There is a typo below Equation (5), where the second instance of $\lambda_1$ should be $\lambda_3$.

### Questions
Please see weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a novel untargeted attack on large visual-language models. To achieve this, the paper attempts to perturb the input image in order to maximize the entropy of the logits, attention, and the intermediate embeddings. Subsequently, the semantic meaning of the output texts is disrupted. The experiments demonstrate the effectiveness of this method and show that visual-language models can be attacked from the vision side.

### Strengths
- This paper explores an important problem. Currently, a lot of work on adversarial examples has been done on vision models, while less attention has been paid to large VLMs. With the increasing application of large VLMs, I believe that the exploration of the robustness of large VLMs is a valuable and important step.
- This paper presents the first untargeted attack against large VLMs. The untargeted goal is realized by maximizing the entropy of the intermediate or output values of the LLM.
- This paper is well-written and well-presented. I enjoyed reading this paper.

### Weaknesses
 - While I like the idea of this paper, the technical contributions concern me. Since this paper is not the first attack against large VLMs, I believe the main contribution of this paper is the design of an untargeted attack that explores information entropy. If this is the case, I think the contributions, in their current state, lack depth. I believe this paper can improve in the following directions.
    - For example, we now have three methods of MIE, but which one is better? What are their strength and weaknesses? Can we have an analysis and an in-depth discussion?
    - What factors can influence the performance of this method?
    - Is this attack robust against simple defensive methods like robust training?
    - Comprehensive evaluation on parameter different settings. For now the evaluation is limited, e.g., only one attack strength is evaluated.

### Questions
I generally appreciate the direction and idea of this paper. However, the current state of this paper can only be considered a simple proof of concept and lacks depth. I would consider accepting this paper if the authors provide a comprehensive study of this method.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
