# Image Hijacks: Adversarial Images can Control Generative Models at Runtime

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Are foundation models secure against malicious actors? In this work, we focus on the image input to a vision-language model (VLM). We discover \vocab{image hijacks}, adversarial images that control the behaviour of VLMs at inference time, and introduce the general Behaviour Matching algorithm for training image hijacks. From this, we derive the Prompt Matching method, allowing us to train hijacks matching the behaviour of an \emph{arbitrary user-defined text prompt} (e.g.~`the Eiffel Tower is now located in Rome') using a generic, off-the-shelf dataset \emph{unrelated to our choice of prompt}. We use Behaviour Matching to craft hijacks for four types of attack, forcing VLMs to generate outputs of the adversary's choice, leak information from their context window, override their safety training, and believe false statements. 
We study these attacks against LLaVA, a state-of-the-art VLM based on CLIP and LLaMA-2, and find that all attack types achieve a success rate of over 80\%. Moreover, our attacks are automated and require only small image perturbations. 
\blfootnote{*Denotes equal contribution.
Project page at \hyperlink{https://image-hijacks.io}{https://image-hijacks.io}.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is well-organized and easy to follow. This idea is simple yet effective.
The authors introduce the concept of image hijacks – adversarial images that manipulate the behavior of VLMs during inference time. They propose a behavior matching algorithm to train these models in a more robust manner against user input. The authors have developed three types of image hijacks: specific string attacks, jailbreak attacks, and leak-context attacks. The optimized perturbation is both imperceptible and effective. 
The experiments are comprehensive, and the overall ASR is high, demonstrating the effectiveness of these methods.

### Strengths
+ The paper presents a rather interesting approach. Utilizing an image to replace the prompt templates of jailbreak attacks seems reasonable. As large multi-modal models continue to develop, such attack methods introduce a new area of adversarial attacks that can be better optimized using computer vision gradient information. I found the idea and the overall paper to be quite enjoyable.

### Weaknesses
- This paper is well-organized and easy to follow, but there is one important baseline missing: "Visual Adversarial Examples Jailbreak Aligned Large Language Models." This paper demonstrates that by using a preset adversarial sample image, a safely aligned LLM can be successfully jailbroken during subsequent model risk assessments, leading the LLM to generate harmful content. The primary attack method involves optimizing the adversarial sample image to create a specific mapping relationship between the image and malicious text.

- I suggest further research on using a single image to match a series of jailbreak attack prompt templates, such as the "Do Anything Now" (DAN) series.

- In my opinion, the patch-level attack or l-p norm attack may not be particularly meaningful. They are simply different methods for generating adversarial examples. What truly matters is the effectiveness of the mapping between adversarial examples and various hijack risks, such as specific string attacks, jailbreak attacks, and leak-context attacks.

### Questions
Refer to weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper delves into the security aspects of vision-language models (VLMs) and their susceptibility to adversarial attacks via the image channel. It introduces "image hijacks," adversarial images that can manipulate generative models in real time. Using a method called Behavior Matching, the authors showcase three attack types: specific string attacks, leak context attacks, and jailbreak attacks. In their evaluation, these attacks have a success rate exceeding 90% on leading VLMs, with the attacks being automated and necessitating only minor image alterations. They underscore the security vulnerabilities of foundational models, hinting that countering image hijacks might be as formidable as defending against adversarial examples in image categorization.

### Strengths
1. Problem Motivation: The paper studies a highly pertinent and timely issue, highlighting the security vulnerabilities of VLMs, which are increasingly being used in various applications.

2. Methodology: The behavior-matching method for creating image hijacks is sound and intuitive. The three types of attacks presented provide a wide understanding of the potential threats.

3. Evaluating the Evaluation: The evaluation is highlighted with alarming results, with all attack types achieving a success rate above 90% against LLaVA. This supports the paper's claims about the vulnerabilities of open-sourced VLMs.

### Weaknesses
1. Technical Contribution: Limited novelty due to similarities with prior works (e.g., Qi et al., Carlini et al.).
    
2. Problem Formulation: Restricted impact concerning closed-sourced VLMs or those not directly interfacing the image channel with the hidden space.
    
3. Transferability of Attacks: Insufficient discussion on attack applicability to unknown VLMs accessible only via APIs (balckbox attacks, which can be a great contribution to set the difference to existing efforts).
    
4. Lack of Defense Discussion: No mention of potential defenses or mitigation strategies against the proposed attacks.

### Questions
- Technical Contribution and Novelty: While your paper introduces the specific string attack and leak context attack, which were not covered by Qi et al. and Carlini et al., the attack process appears to be highly similar to these prior works. Could you elaborate on the distinct technical innovations that differentiate your methods from these existing studies? Additionally, are there areas where you foresee further improvements or refinements to enhance the technical novelty of your approach?

- Problem Formulation: Considering the limited applicability of your problem formulation to closed-sourced VLMs or those VLMs that do not directly interface the image channel with the hidden space, how do you envision the broader relevance of your proposed attacks? Are there specific scenarios or VLM architectures where your attacks would be particularly effective?

- Transferability of Attacks: Could you expand on the transferability of your attacks to unknown VLMs, especially those only accessible via APIs, such as GPT-4V? Given that GPT-4V's technical report has already highlighted potential risks associated with the image channel and proposed baseline defenses, how do you anticipate your attacks would perform in such contexts?

- Lack of Defense Discussion: Why was there an omission of defenses or potential mitigation strategies against the proposed attacks in your paper? A discussion on potential countermeasures would enhance the paper's depth and practical relevance. Do you have insights or preliminary findings on how one might defend against the attacks you've introduced?

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
This paper studies the security problems of Vision-Language Models (VLMs), and propose to add unnoticeable perturbations onto the image inputs, to mislead the model have various types of adversarial behaviors.

### Strengths
The proposed attacks absolutely make sense, and demonstrate the weakness, the security risks of the VLMs.

### Weaknesses
The greatest concern is that the paper does not study the transferability behavior of the proposed attacks to close-source VLMs. Although the authors mention that the jailbreak attack in [Zou 2023] did similar experiments to transfer the attacks from open-source LLMs to close-source LLMs, it can not ensure the VLM attacks can also have the ability to transfer. If this part of experiment is not provided, it would dramatically limit the significant of the contribution of this paper. 

Beyond the study of transferability, I found the methodology is not significantly novel, compared to existing attack methods such as Jailbreak attacks in LLMs and image adversarial examples. Therefore, without the transferability study, this work seems solely a white-box attack paper without significant novelty, because people already know that the DNN models are vulnerable to adversarial attacks.

### Questions
Plz see the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies adversarial images (referred to as image hijacks) in the context of attacking large vision-language models (VLMs). Specifically, the authors explore three types of attacks, i.e., specific string attack, leak context attack, and jailbreak attack, which target three different undesirable behaviours of VLMs. Three different image constraints are considered: Lp norm, stationary patch, and moving patch.

### Strengths
- "Adversarial images on VLMs" is an interesting and promising topic. 
- The paper is well written, including sufficient example visualizations and clearly described technical details.
- Real-world experiments with human studies are conducted, involving both the tests with drawing and pasting tapes.

### Weaknesses
 - The experimental studies in this paper are limited. Only the ideal, white-box setting is considered. The authors should follow recent attempts (e.g., the GCG paper) to explore more realistic attack settings, such as query-based and transfer-based attacks. Moreover, although the authors envision three different undesired behaviors, the implemented three attacks are indeed following the same attack goal which is to output a pre-defined text.  More diverse attack goals should be explored.

- Considering this paper studies a really hot topic, it should highlight its specific contributions, especially in terms of technical novelty, compared to other (concurrent) similar studies. In the current version, only the differences in attack settings are briefly mentioned in Section 5.

- The reviewer does not get the idea of splitting the dataset into train, val, and test sets. Is the perturbation vector universal, i.e., it is trained over a lot of original images and once trained can be directly applied to any testing images? If this is the case, it should be explicitly mentioned in the paper. Otherwise, it is confusing that creating adversarial images requires image (or model) training. In addition, why didn’t the authors explore the common setting of image-specific attacks?

- Since the baseline GCG attack was also designed to achieve “exact match”, it is reasonable to compare with it also on the rest two types of attacks: specific string and leak context.

- Figure 4 takes an unreasonably large space (i.e., one page) given the fact those three considered types of constraints are well-known in the literature.

### Questions
See the above weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
