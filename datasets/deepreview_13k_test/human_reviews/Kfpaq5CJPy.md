# Leveraging image representations for bounded adversarial attacks and robustness

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Both classical and learned image transformations such as the discrete wavelet transforms (DWTs) and flow-based generative models provide semantically meaningful representations of images. In this paper, we propose a general method for robustness exploiting the expressiveness of image representations by targeting substantially low-dimensional subspaces inside the $L^\infty$ box. Experiments with DCT, DWTs and Glow produce adversarial examples that are significantly more similar to the original than those found considering the full  $L^\infty$ box. Further, through adversarial training we show that robustness under the introduced constraints transfers better to robustness against a broad class of common image perturbations compared to the standard  $L^\infty$ box, without a major sacrifice of natural accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel white box adversarial attack method by creating perturbations in a transformed image representation space while constraining the maximum pixel perturbation. To this end, the image in transformed space is split into two vectors and one of them is perturbed. This problem is then converted to a linear programming problem and the barrier method is used to find the optimal value (the adversarial example). Three different image representations - DCT, DWT and glow (2 linear and 1 learner based) are used to demonstrate the effectiveness of attack on CIFAR dataset. The attack method is then used in adversarial training (TRADES used here) to show its effectiveness in training robust models. Experiments are presented to test the robustness against various kinds of corruptions.

### Strengths
The idea presented in the paper is very interesting and novel. Converting the adversarial attack problem into a linear programming problem and using adequate tools to solve it is a good catch. The authors have explained well the problems encountered during making such a conversion and strategies used to overcome it. E.g. using barrier method to remove need for projection, using first-order update rule instead of the usual minimization, dealing with discontinuity of $L^{\infty}$ norm. Overall the problem is well formulated and explained.

The flow of the paper is clear and easy to understand. In terms of significance, this reformulation of adversarial attack is interesting and might be for the useful for the community to look at.

### Weaknesses
The idea presented is novel but the experiments do not back it up well. 

1. The method finds examples that are less perturbed than other methods compared but the attack success rate is not upto par with other methods. In fact it is very low in some of the image representations used. The presented the trade-off between distance from original image and success rate does not show it to be very effective attack method. You can't really visually tell the difference between the adversarial images generated from this attack and PGD.
2. The attack methods are only compared on CIFAR - Imagenet would be a good addition as datapoint to the experiments.
3. No mention of the cost of attack, number of steps to reach the adv example and time taken by barrier method optimization.
4. For adversarial training, comparison has only been made with PGD. I believe other methods should be used in the comparison. 
5. Again ImageNet not used for adversarial training, would be a good experiment to add.

Overall the experiments do not showcase the effectiveness of method as adversarial attack or for training robust models compared to other state of the art methods. 

Typo:

Eqn 2 : $R^n$ -> $R^q$ ?

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to conduct adversarial attacks in a meaningful subspace of a transformed image representation while obeying the Linf box at the same time. Since the perturbation space is more complex, PGD cannot be directly applied, and the authors proposed to use the barrier method from nonlinear programming to compute perturbations without a projection. Experiments show that the proposed method can generate adversarial images that are more similar to original images, in the Linf adversarial attack setting. Experiments also show that when the proposed method is used in adversarial training, it can improve robustness against corruptions.

### Strengths
* This work proposed a new threat model which considers perturbations in a meaningful subspace of a transformed image representation.
* This work designed an attack for the proposed threat model, using a barrier method.  
* Experiments show that adversarial training with the proposed threat model can improve robustness against corruptions.

### Weaknesses
* Comparison with baseline attacks using Linf boxes is not fair. The proposed method has smaller perturbations but also lower success rates. It is possible that the perturbation size of the baseline attacks may be reduced at the cost of the success rates. The proposed method and the baseline methods need to be compared by controlling for the success rate or the perturbation size. 
* The introduction says "In this paper we offer progress in the quest for corruption robustness by present- ing a powerful novel adversarial attack and associated adversarial training". Thus, it sounds like improving the robustness against corruption is the main purpose of this paper. However, the experiments do not compare with any baseline specifically for robustness against corruption.
* The proposed adversarial training has improvement on Blur and Noise, but not really on Digital and Weather. Thus, the significance of the empirical improvement is limited.
* The concept of subspace adversarial training has earlier appeared in Li et al., 2022, which is missed in this work, although the techniques are not the same.

Li, T., Wu, Y., Chen, S., Fang, K., & Huang, X. (2022). Subspace adversarial training. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 13409-13418).

----------------

**Updates after rebuttal**:

>We are approaching the problem of robustness from an adversarial training perspective unlike state-of-the-art corruption robust methods that are mainly based on data augmentation. We have discussed this in Section 4, the Limitations and discussion paragraph.

The problem and the goal is still the same, and thus a comparison is necessary. 

>Not correct. From Table 2: under the Digital category, we have improved in Elastic from 85.04 to 88.42, in JPEG from 81.07 to 98.44, and in Pixelization from 79.23 to 92.09. In the Weather category, the improvement is in Snow from 84.33 to 88.89, in Fog from 89.15 to 90.81, and in Spatter from 87.99 to 89.78.

The improvement is unstable and inconsistent. E.g., for the Digital category, while JPEG is improved from 81.07 to 89.44, Contrast is significantly degraded from 83.01 to 67.28. Same issue for the Weather category. 

Therefore, most of the weaknesses I originally mentioned persist. I'll keep my score.

### Questions
See the weakness points.

### Soundness
3 good

### Presentation
2 fair

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
The paper proposes to find adversarial examples by perturbing the image in the representation space and then convert it back to the original image space. Empirical experiments show that this method can produce adversarial examples with more natural adversarial examples and smaller Lipschitz distance.

### Strengths
1. The paper proposes to generate adversarial examples with invertible image representations. This idea is novel and interesting, which is not known in existing literature as far as I know. 
2. Empirical experiments show that the proposed method can produce adversarial examples with significantly smaller Lp distances.

### Weaknesses
1. The attack success rate of the proposed method is much lower compared to baseline methods, which may also weakens the results with smaller perturbation radius. The author could report avg. Lp distance of the same top% of adversarial examples from the baseline method.
2. As the proposed method assume that the image representation function $\sigma$ is invertible, do the DCT and DWT implemented in the paper invertible? In my understanding they produce a compressed version of the original image and are not invertible.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel adversarial attack which relies on perturbing images in representation space such that, when this representation is inverted, we get an adversarial example in the pixel space. To this end, the authors create a framework where given an invertible transformation (DCT, DWT and GLOW are used in the paper), we can put an image through this transform and then separate out the most significant components of its representation. These important components are kept the same while the remaining components (presumed to be less important) are perturbed slightly. The space of these perturbations is such that when the perturbed representation is inverted, we get an adversarial example in pixel space (w.r.t the $\infty$ norm).

To actually produce the adversarial examples, the authors follow a method similar to PGD except that they replace the ‘projection’ step in PGD by placing a constraint in their optimization problem. This is just the standard barrier function method from constrained optimization which makes sure that the iterates of the optimization remain within the set of possible outcomes (within the set of allowed perturbations in this case).

This, the authors show, produces adversarial examples which are closer to the original image in terms of L2, LPIPS etc distance. Next, the authors use their attack for adversarial training which helps the model robustify against image corruptions (such as blue, weather etc) with small losses in clean accuracy. Since the adversarial attacks were not tuned w.r.t these image corruptions, the authors show that their attack introduces robustness which transfers over to other tasks (image corruptions in this case).

### Strengths
1. Significance of the problem: robustifying models against unseen threat models is an extremely important problem facing our community. The authors attempt to make a preliminary advance in pursuit of that goal.
2. The method introduced in the paper is novel to my knowledge and well motivated.
3. The paper is well written and easy to understand. Novel concepts introduced are explained well and their relation to past work is explained clearly.
4. The claims made by the authors in the introduction are clearly backed up via experiments.

### Weaknesses
My main concern about this paper revolves around the significance of the results.

I would break down the results into 3 parts:
1. First, the authors state that their attack produces adversarial examples which are closer to the original image than what we would get via PGD. This is measured via a number of distance metrics in pixel space (L2, LPIPS etc)
2. Second, they then show that when their attack is used for adversarial training, we get only a small drop in clean accuracy (only a few % points). This to me seems expected, because, the images produced are very similar to the original images so the model makes fewer mistakes (Point 1 above). 
3. Next, the authors show that adversarial training using their attack introduces robustness to threat models which were not trained against originally. This is a very significant problem and, from what I’ve seen, usually solved via some form of ensembling. However, the robustness introduced against image corruptions via this method falls short of what dedicated methods attain (this is a limitation pointed out by the authors to be fair and not to be held against them since they use a threat model agnostic method).

For Point 3 above, while the authors have shown that their method transfers better to image corruptions than vanilla PGD, there needs to be some control for the amount of image corruption added. As stated above, adversarial examples produced by the authors are closer to the original image. Hence, it might be possible that their method only performs better because the amount of corruption added to the image is too low and if more noise was added, vanilla PGD might become better.
Additionally, I would like to see the authors compare attacks with each other. If the claim is about the transferability of robustness, why not train the model with adversarial examples produced using their own attack and test them on adversarial examples produced via PGD? (And vice versa) Regardless of the outcome of this experiment, it would tell us something about the limits of transferability being claimed. 

I do think this paper contributes something meaningful methodologically (perturbing in representation space), however, it is unclear to me where or what this method is actually good at doing. This is the main reason behind my score below.

Minor:
1. There are several choices made throughout the paper which seem essential to making this technique work. It would be nice to have ablations over these choices to make the paper more rigorous experimentally. Some examples: choice of barrier function, size of ‘e’ in class conditional representations for GLOW etc.

Typos:
1. Page 1, Section “Introduction”, Subsection “Adversarial Robustness” - “attacks either by LEANING and embedding space using neural networks (Huang….)” should be “attacks either by LEARNING and embedding space using neural networks (Huang….)”
2. Page 2, Paragraph 2 - “Approaches include again suitable data augmentation” I presume should be “Approaches include using suitable data augmentation”
3. Page 5, Section 3, Subsection “DCT” - “collects the frequencies that are most SEVERALLY reduced” should be “collects the frequencies that are most SEVERELY reduced”
4. Page 5, Section 3, Subsection “DWT” - Capitalization “As for the DCT, and in JPEG2000, Similarly, we first perform” should presumably be something like “Similar to the case of DCT for JPEG2000, we first perform”. Note, this is just a suggestion and the authors might have been trying to communicate something else so feel free to use some other statement. The point of this was only to correct capitalization and grammar.
5.  I think the second argument for $\gamma$ in Eq 2 should be $R^{q}$ right? Because that is the domain of the ‘a’ values.

Formatting: 
1. Title of section 4 “Experimental Evaluation” is the last line of the page. Ideally, the title should have some following text so that the document flows better.

### Questions
1. The barrier function was chosen to be of the form $b(a^{*}) = -\frac{1}{g(a^{*})}$. What is the reason for this choice apart from it being continuous? Were other choices considered? 
2. Why is just the sign of the gradient taken in the SGD update instead of the value? Is there any reason beyond just that it works better in practice in this setting?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
