# Adversarial Perturbations Cannot Reliably Protect Artists From Generative AI

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Artists are increasingly concerned about advancements in image generation models that can closely replicate their unique artistic styles.
In response, several protection tools against style mimicry have been developed that incorporate small adversarial perturbations into artworks published online.
In this work, we evaluate the effectiveness of popular protections---with millions of downloads---and show they only provide a false sense of security.
We find that low-effort and ``off-the-shelf'' techniques, such as image upscaling, are sufficient to create {robust mimicry methods} that significantly degrade existing protections.
Through a user study, we demonstrate that \emph{all existing protections can be easily bypassed}, leaving artists vulnerable to style mimicry. 
We caution that tools based on adversarial perturbations cannot reliably protect artists from the misuse of generative AI, and urge the development of alternative protective solutions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors critically revisit the current efforts towards protecting artists' work from diffusion model mimicry. The author proposes that most protection nowadays cannot really protect artists, since the protection can by easily bypassed using some tricks of purifications e.g. Gaussian Noising, Diff-Pure and Up-scalers. Extensive experiments are done to support the claim in this paper. Overall, the paper is well-written, easy to follow and the proposed method is simple but effective.

### Strengths
- The paper is well-written and easy to follow.
- It works on an important problem and provides critical insights: all protection methods today cannot protect artworks from diffusion-based mimicry. Though works like Glaze have been widely accepted by artists, they actually perform bad.
- The proposed robust mimicry methods are simple but effective.
- The authors did extensive experiments to support the claims.

### Weaknesses
Clarification:
- The title of this paper is 'ADVERSARIAL PERTURBATIONS CANNOT RELIABLY PROTECT ARTISTS FROM GENERATIVE AI', while style-based mimicry is one part of diffusion-based mimicry, there are more basic mimicry e.g. inpainting, style-transfer by diffusion model, which are also tested in previous papers of protection e.g. Mist. Fine-tuning a diffusion model seems to have a more complicated mechanism compared with image-to-image applications of diffusion models. 
- I wonder does the proposed method also work for inpainting/image-to-image SDEdit, if it works, the proposed method becomes more general.

Methods:
- I noticed that the perturbation used in this paper is quite small, if the noise is scaled up, will the purification be worse
- While Glaze and Mist are popular, there are many other protection methods that can be studied to get a safer conclusion. e.g. MetaCloak [3] and SDS [4].

Related Papers:
[1, 2] are highly related to this paper, [1] also find that the current attacks are vulnerable to purifications, [2] proposed that latent diffusion models can be easily purified by pixel-space diffusion models. 

[1] Can Protective Perturbation Safeguard Personal Data from Being Exploited by Stable Diffusion?

[2] Pixel is a Barrier: Diffusion Models Are More Adversarially Robust Than We Think.

[3] MetaCloak: Preventing Unauthorized Subject-driven Text-to-image Diffusion-based Synthesis via Meta-learning

[4] Toward effective protection against diffusion-based mimicry through score distillation

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper examines the effectiveness of existing style protection methods (such as Glaze, Mist, and Anti-DreamBooth) against both black-box and white-box attacks. The authors demonstrate that these protections can be easily circumvented using simple techniques like DiffPure, upscaling, and adding Gaussian noise, as well as more sophisticated methods like IMPRESS. The findings are supported by an MTurk study, where participants were asked to distinguish between images generated using style mimicry on unprotected vs protected artworks. The paper highlights the inherent asymmetry between attackers (style mimickers) and defenders (artists), cautioning against relying on adversarial perturbations for style protection due to the potential false sense of security they may provide.

### Strengths
1.  While it was anticipated that prominent style protection techniques like Glaze might have weaknesses, the extent of their fragility is striking. The paper demonstrates that these methods fail even against rudimentary attacks, with Glaze unable to withstand a mere change in the fine-tuning script. This revelation underscores a concerning lack of “security mindset” within the style protection research community, which is particularly alarming given the recognition Glaze has received, including multiple awards from USENIX Security.

2. The MTurk study is well constructed and the authors have taken pains to ensure that their work adheres to commonly accepted ethical standards.

### Weaknesses
1. The work has limited novelty since it was predictable that style protection would be vulnerable to DiffPure-like purification methods. It would be good if the purification methods evaluated in the paper could be packaged into a standard baseline, say on the lines of AutoAttack.

2. In my opinion, the paper overstates the general case against style protection techniques based on adversarial perturbation. The presented argument makes an assumption that artists have the choice to release their artworks on the internet, and they may choose to withhold their artworks if they believe that AI models may be trained on their artworks. However, digital artists are extremely dependent on the internet to grow their customer pool and advertise their works, so this is likely not a feasible option. The appropriate counterfactual to artists using Glaze-like methods would be not using any protections at all. Also, since these methods seem to be improving against simple attacks at least, it may be enough to use them as a deterrent rather than as fool-rpoof security.


I struggled to decide whether to rate this paper as borderline accept or clear accept due to the stated weaknesses. Ultimately, I decided to rate this paper as clear accept as the argument may indeed be persuasive to a small minority of artists who may decide to not publish any of their works if there is no secure style protection mechanism.

### Questions
1. It would be interesting to see the results on Glaze 2.1 (the newest version) for completeness’s sake. Does this induce greater quality degradation compared to its previous versions?

2. The “Best-of-4” method is not really a practical method since it depends on the human ratings and the same human ratings are used to evaluate the method. For fair comparison, the raters need to be split into validation and test raters, and the method selection should utilize only the validation raters and be evaluated by the test raters, with averaging across splits via cross-validation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a user study evaluating pre-processing techniques against current adversarial perturbations, finding that such methods can significantly reduce their effectiveness.

### Strengths
1. The writing is clear and easy to follow.
2. The topic is interesting and important.

### Weaknesses
The main weakness is the unreliable evaluation and whether the experimental results reflect real-world cases.

1. The study heavily relies on MTurk workers, who may not be suitable for this task. They might lack the expertise to classify artistic styles or assess whether artwork quality has been degraded. Artists themselves, such as those mentioned in [1], should be included in the main evaluation. Additionally, these workers may not represent potential consumers of artists' works, contrary to what the authors propose (L 338). A more thorough study should report the workers' relevance to the art domain (e.g., how often they purchase art or visit museums).
2. The effectiveness of the fine-tuning procedure is unclear. As shown in Fig. 3 (especially the bottom row) and Fig. 5, the generated images, even without protection, do not closely resemble the style of the training images. In contrast, previous work like Glaze [1] uses a fine-tuning setting with much stronger resemblance between generated images and training data (see Fig. 2 in [1]). The focus should be on whether adversarial perturbations effectively defend against mimicry once it has been successfully achieved. Even in Appendix K, where the limitations of using MTurk for evaluation are acknowledged, fewer than 50% of cases were rated as better or equal to “successful” mimicry.
    
    In an extreme case, if fine-tuning involved only one step, adversarial perturbations would likely fail to defend against mimicry. The core issue seems to be underestimating how closely the model need to fit training images, including adversarial perturbations,  to learn the style, which may result in an underestimation of their impact.
    
3. Even if the above weaknesses are overlooked, the paper provides no new insights on solving the problem of mimicry. Both pre-processing and adversarial perturbations degrade image quality, raising the question of whether removing adversarial perturbations is worth the cost, given that pre-processing might degrade the image quality in ways that hinder style recognition.
4. The paper overlooks broader ethical implications, such as the removal of adversarial perturbations used as a watermark. Similar to traditional watermarks (such as a simple icon on the corner) that can be removed but are illegal to do so in many countries, stronger watermarks complicate removal and leave evidence. A discussion on these ethical issues would contribute more meaningfully to the community.
5. The proposed methods lack novelty, largely offering improved hyper-parameter tuning of existing approaches.

[1] Shan S, Cryan J, Wenger E, et al. Glaze: Protecting artists from style mimicry by {Text-to-Image} models[C]//32nd USENIX Security Symposium (USENIX Security 23). 2023: 2187-2204.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the practicality of "using adversarial perturbations to protect art works from mimicry". The paper argues that, existing research works which uses adversarial noise for art copyright protection -- although published in top ML/Security conferences -- do not robustly achieve their claimed goals. Simple technical means are enough to bypass these existing protections. The work argues that researchers and practitioners should rethink the solution for art mimicry problem and develop alternative protections.

### Strengths
+ S1: The motivation is clear and compelling, effectively serving the paper's purpose: to caution researchers about the limitations of using adversarial perturbations for protection against art mimicry.

+ S2: The paper is well-organized and easy to follow. The experiments conducted are solid.

+ S3: The conclusions drawn from this work are potentially significant for the community and could reshape the landscape of this research field. Researchers are encouraged to reconsider the current paradigms of artwork / copyright data protection in light of their practical effectiveness.

### Weaknesses
+ Typos
    1. Line 219, fare -> fail?
    2. Figure 11, 13, 14, 15 seem to have the wrong label - now they are all labelled as "gaussian noising"

### Questions
Overall, the technical details in the paper are clearly described, so I have no questions about the technical aspects. However, I do have some open questions for the authors that I would like to discuss:

+ Q1: Practical and scalable evaluations? The core claim of this paper is to demonstrate the ineffectiveness of existing art mimicry protection methods. For this purpose, using a user study as an evaluation method is sufficient. However, for future papers proposing alternative protective solutions, what could be a scalable way to evaluate their effectiveness?

+ Q2: Is it technically possible to protect artists from mimicry? The conclusions drawn from this work appear to be somewhat pessimistic. Given that generative AI has a strong capability to fit any content, it seems that the potential for mimicry might be inevitable. What could be potential solutions to mitigate this issue?

### Soundness
3

### Presentation
3

### Contribution
3
