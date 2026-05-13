# Human-Producible Adversarial Examples

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Visual adversarial examples have so far been restricted to
pixel-level image manipulations in the digital world, or have
required sophisticated equipment such as 2D or 3D printers
to be produced in the physical real world. We present the first
ever method of generating human-producible adversarial examples
for the real world that requires nothing more complicated
than a marker pen. We call them \textbf{\textit{adversarial tags}}. First, building on top of differential rendering,
we demonstrate that it is possible to build potent adversarial examples with just lines. We find that by drawing just $4$ lines we can disrupt  a YOLO-based model in $54.8\%$ of cases; increasing this to $9$ lines disrupts $81.8\%$ of the cases tested. Next, we devise an improved method for line placement to be invariant to human drawing error. We evaluate our system thoroughly in both digital and analogue worlds and demonstrate that our tags can be applied by untrained humans. We demonstrate the effectiveness of our
method for producing real-world adversarial examples by
conducting a user study where participants were asked to
draw over printed images using digital equivalents
as guides. We further evaluate the effectiveness of both
targeted and untargeted attacks, and discuss various trade-offs
and method limitations, as well as the practical and ethical 
implications of our work. The source code will be released publicly.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a compelling approach, suggesting the use of line-based adversarial tags to deceive the predictions of YOLO-based models. Notably, the authors have taken an intriguing step by ensuring that these adversarial lines can be realistically produced by humans, adding a layer of practicality to their proposal.

### Strengths
1. This paper delves into a captivating avenue for generating adversarial perturbations. 
2. Moreover, the authors have thoughtfully crafted a robust loss function aimed at ensuring that the adversarial lines are feasibly replicable by humans.

### Weaknesses
 1. The "Method" section would benefit from additional granularity. Specifically, it remains unclear how overlapping of the randomly generated lines is addressed. Are there any constraints or specific guidelines governing the generation of these random lines? It is unclear if the lines are generated independently, potentially leading to redundant or ineffective perturbations, or if there's a mechanism to ensure diversity and coverage across the image or object of interest. The lack of detail on this aspect makes it difficult to assess the robustness and efficiency of the line generation process.
2. The decision to employ only four line-defining points warrants clarification. Is there a theoretical foundation or empirical rationale that supports this choice? The justification for using only two points to define the lines is not well-established, especially considering the potential for more complex curves or shapes to be used as adversarial perturbations. This choice may limit the expressiveness of the adversarial space and potentially miss more effective attack vectors. A discussion of the trade-offs between simplicity and effectiveness is needed.
3. There are noticeable writing inconsistencies. For instance, the abbreviation "NLL" is employed prior to its formal definition, which might be confusing for readers.

### Questions
This paper could be significantly enhanced by addressing the following queries:

1. What underlying principles or mechanisms allow simple lines to effectively execute adversarial attacks?
2. When considering both targeted and untargeted attacks on images of similar objects, what common traits or patterns emerge?
3. The motivation presented could be better articulated. What is the rationale behind necessitating human production of the adversarial line? Is there an inherent advantage or specific scenario where this becomes crucial?
4. In scenarios where the lines are confined solely within the object's area, does the efficacy of the proposed attack remain consistent?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Adversarial examples have shown to be effective against DNNs, but require special tools or equipment to apply in the physical world. The authors investigate an intuitive subset of adversarial attack, which are those easily drawn by human hands. The methodology is a hybrid of gradient-free and gradient-based computation. The authors gradually tune the 4-tuple parameter set for each line in a collection given the gradient of the model with respect to an adversarial loss. The adversarial loss takes into account the range of intrinsic human error when drawing lines. A fixed amount of lines are pruned each iteration, iterating until the final set of adversarial lines is achieved. The authors conduct a series of experiments to check the effectiveness of the adversarial lines. A user study wih four participants was conducted to check the variance between non-robust and robust adversarial losses among users, as well as the variance among users on the same image. An experiment also measures the practical use-case of the lines, where everything except the object in focus is allowed to be modified by black tape. The experiments show that fewer long lines are more efficient for perturbation than many short lines.

### Strengths
* The writing quality is high and only a few minor typos are noticeable. 
* The investigated problem is interesting and well-separated from existing literature. The plausible implementation of adversarial distortion by humans is still an under-studied area. The submission may offer some impact to the literature. 
* The paper is well organized and flows easily from section to section. 
* Experiments are intuitive and investigate key aspects of the methodology. The authors attempted a user study which gives some promising results.  The technique itself can reliably flip labels with up to 94% success. 
* It was interesting to see the tradeoff between quantity and size of lines. Intuitively, more lines leads to more adversarial success, but in fact fewer long lines is more beneficial from a human factors standpoint. Likewise, more lines leads to more error when scanning the photos. 
* The details of incorporating human error into the adversarial loss are useful to understand the potential attack surfaces of the model from a human-in-the-loop. 
* The submission is headed in a good direction, but requires some more work before meeting the bar for publication (see Weaknesses).

### Weaknesses
 * The user study consisted of only four participants, and does not investigate the effects of artistic ability. The sample size seems too low to draw any broad conclusions. It wasn't mentioned if the participants had a limited time budget to replicate the lines, which might be an important consideration in replication. 
* The evaluation only considers a single YoloV8 classifier, rather than checking on multiple architectures and robustness levels, which are valid in the author's threat model. I was expecting experiments on robustified models [1,2] or some experimental results in trying to use adversarial lines for adversarial training. It would be interesting to see if the data generated by adversarial lines is too noisy, potentially degrading the benign accuracy when used for AT. This could provide useful information for the broader community.
* Only the white-box implementation is investigated, so the transferability of lines is unknown. It seems unlikely that a human with only a marker can also backprop through a service provider's model. I was expecting an experiment where the adversary tries to transfer adversarial lines from an owned model to an unseen model, potentially of a different architecture. The authors primarily pitch the contribution as an easily accessible technique for non-experts, so it seemed contradictory that they would also require access to weight-level knowledge of the defender's model. In the same spirit, the computational complexity seems too high for a non-expert to perform these attacks, since it requires a 4-GPU workstation to run. 
* Only 500 images from 1000-class ImageNet were investigated (i.e., only half of classes are represented), and in that regard, the authors have only performed experiments on ImageNet. It isn't clear if the proposed methodology is applicable to other datasets, or how the attack behaves across different object classes. I suspect some object classes and camera angles are more difficult to attack under this threat model. This would change the overall feasability of the attack. 
* The physical realization of attacks still seems unlikely, since most experiments allow adversarial lines to occupy any portion of the image, even the background. Previous work have successfully launched similar attacks by only perturbing the spatial region of a relevant object (e.g., clothing patch or fashion attacks). 
* It is difficult to gauge the significance of the submission without comparisons to baseline techniques. For example, it seems feasible that existing white-box attacks could be used for a similar style attack by limiting their influence to the regions with adversarial lines, and limiting the fidelity of perturbation. Likewise, it isn't clear how adversarial lines perform compared to techniques such as adversarial clothing or sunglasses.

### Questions
* It isn't clear why the adversary could only perturb the background of an image, rather than the object. This seems to go counter to previous work. Can the authors comment on the attack feasability from only perturbing the object's spatial region? 
* Can the authors comment on the attack transferability? Is it feasible that adversarial lines would transfer to an unseen model? 
* In the human study, how much time were participants given to replicate the lines? 
* How does the proposed attack compare to existing physical attacks? 
* What is the time complexity of running the attack on a single image? Does it scale well with the number of lines?
* How well do robust models fare against the adversarial lines? Can adversarial lines be used for adversarial training? 
* Do the authors normalize the size of the lines for the size of the object? A black marker will cover more of a plastic cup, but not so much of a soccer ball.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new type of adversarial attacks, named adversarial tags. This attack can be accomplished in real world with only one marker pen. The authors propose generate-and-prune method to achieve this goal.

### Strengths
- The paper's central concept—developing adversarial examples that can be created with something as simple as a single marker pen—is intriguing. This raises significant security concerns, particularly the possibility of attackers drawing lines on the ground to mislead autonomous driving systems.
- The authors suggest employing Jitter and Erasing as augmentation techniques during the optimization process of adversarial examples. These methods could potentially enhance the robustness of adversarial examples when faced with real-world conditions.

### Weaknesses
 - The most significant shortcoming of this paper is the extremely insufficient evaluations. Attacks like the ones proposed are designed to be executed in real-world scenarios, which are typically "black-box" in nature. To only assess such attacks in "white-box" settings is not adequate; after all, any attack designed to maximize the loss function might perform well against known classifiers in such a setting. The paper lacks any evaluation of the transferability of these adversarial tags to different model architectures or even different training instances of the same architecture. This is a critical omission, as the practical utility of the attack hinges on its ability to generalize beyond the specific model used for its generation.
- Additionally, the experimentation is conducted exclusively on the YOLOv8 model. To ensure a thorough understanding of the attack's efficacy, it's crucial to extend the evaluations to include a broader range of models. The absence of experiments on other object detection models, such as Faster R-CNN or SSD, makes it difficult to ascertain whether the observed adversarial effects are specific to YOLOv8's architecture or a more general phenomenon. Furthermore, the evaluation should consider models trained on different datasets to assess the robustness of the attack across varying training distributions.
- In real-life conditions, adversarial implementations may face various distortions due to camera angles or environmental interferences like weather. However, the paper's evaluation seems too idealistic. The authors have chosen an optimal camera angle, and there is a noticeable absence of corruption in the adversarial tags. This approach doesn't fully simulate the real-world conditions where such adversarial techniques would be applied. The lack of consideration for perspective distortions, partial occlusions, and varying lighting conditions significantly limits the practical relevance of the presented results.

### Questions
To convincingly demonstrate the practical viability of the proposed attack, I recommend conducting more comprehensive evaluations. For instance, transitioning from white-box to black-box settings would better reflect real-world operational conditions. Additionally, incorporating transformations or Gaussian noise could simulate the kind of corruptions one might encounter in actual scenarios, thereby providing a more robust validation of the attack's effectiveness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper argues that existing manipulations for creating physical adversarial examples are hard to be reproduced by humans (without access to an electronic device). Therefore, they propose to generate human-producible adversarial examples, which are achieved by hand drawing. Specifically, in the digital space, the adversarial examples are optimized based on gradients and genetic search within a parameter space of line-based adversarial tags. Then, humans are asked to reproduce the adversarial lines given the (printed) digital image as the reference.

### Strengths
- The concept of “human-producible adversarial examples” was previously not well studied.
- The presentation of the paper is good, including sufficient example visualizations and clearly described technical details.
- Real-world experiments with human studies are conducted, involving both the tests with drawing and pasting tapes.

### Weaknesses
 - Lack of motivation. The reviewer is not convinced about why “human-producible adversarial examples” are desired in the first place, given that electronic devices, e.g., printers and scanners, are quite easy to get nowadays. More importantly, printed adversarial examples have been shown to be very robust in the literature and the proposed  “human-producible adversarial examples”  have not saved any computational cost at all. 
From the perspective of the budget of the attacker vs. defender, it seems not reasonable to constrain the attacker to use only pens since the defender has the ability to use a model/camera/scanner. 
More specifically, in this paper, the authors indeed printed out those adversarial images with lines and let humans reproduce them. In this case, why don’t the authors directly use printed images as the final adversarial examples? By the way, these printed adversarial images should be compared as a baseline (non-human-producible) attack.

- Lack of discussion about potential countermeasures. A clear drawback of using a simple adversarial manipulation is the lack of stealthiness. In the case of line-based adversarial tags, it seems very easy to filter out them, e.g., based on edge detection or simply prototype matching. The authors should better test these potential countermeasures because attack stealthiness is important.

- As can be seen from the visualizations, the robust loss leads to lines quite close to the cup but the non-robust loss leads to lines further away. Why does it happen? If this really the case about why the robust loss works better, is it possible to just constrain the modification space to be surrounding the cup to make the attack robust? 

- The detailed image design was not introduced until Section 3.5 “To test this real-world scenario, we conducted an experiment whereby we took photographs of a common household object – a cup – and produced an adversarial tag for them. We constrained the search area to a rectangular bounding box to limit the lines to a specific area of the image to avoid the cup itself.” However, without this introduction, it is very hard to understand the specific design depicted in Figure 2. The reviewer initially thought there was a sub-figure showing a cup pasted in the main figure showing the wall. So the suggestion is, for Figure 2, to detail those two factors independently but leave out the messages about the image design. By the way, why doesn’t the black area occupy the whole image?

- The use of “real world”/“physical world”. In the experiments, the authors consider drawing lines and pasting tapes. It is better to separate these two settings using more specific terms beyond the “real world”/ “physical world”.

### Questions
See the above weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
