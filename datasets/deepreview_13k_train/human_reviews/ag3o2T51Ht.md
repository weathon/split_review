# Circumventing Concept Erasure Methods For Text-To-Image Generative Models

- Decision: Accept
- Scores: 6, 5, 8, 6, 8

## Abstract
Text-to-image generative models can produce photo-realistic images for an extremely broad range of concepts, and their usage has proliferated widely among the general public. Yet, these models have numerous drawbacks, including their potential to generate images featuring sexually explicit content, mirror artistic styles without permission, or even hallucinate (or deepfake) the likenesses of celebrities. Consequently, various methods have been proposed in order to ``erase'' sensitive concepts from text-to-image models. In this work, we examine seven recently proposed concept erasure methods, and show that targeted concepts are not fully excised from any of these methods. Specifically, we devise an algorithm to learn special input word embeddings that can retrieve ``erased'' concepts from the sanitized models with no alterations to their weights. Our results highlight the brittleness of post hoc concept erasure methods, and call into question their use in the algorithmic toolkit for AI safety.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines seven concept erasure methods in text-to-image models, and show that the targeted concepts that are supposedly erased from the models can be retrieved using an algorithm which learns special input word embeddings. In this way, this paper shows more thoughts and efforts are needed when coming up with concept erasure methods in text-to-image models.

### Strengths
The paper addresses an important problem that is often not looked upon in text-to-image generation models. 

Visual illustrations are presented well. It is also good that both quantitative and qualitative results are shown. 

Detailed appendix is also helpful.

### Weaknesses
Only 1 version of Stable Diffusion (version 1.4) is presented. Is there any reason to choose this? Will the results be similar in later versions of Stable Diffusion?

Though the paper exposes that the seven recently proposed concept erasure methods can be broken, the paper does not address in detail how these can be fixed. A detailed discussion section on this will be useful and make the paper stronger.

### Questions
None.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper reveals that seven recent concept erasure methods in text-to-image models are ineffective, as erased concepts can be regenerated with specialized prompts. It demonstrates the methods' vulnerability and the need for stronger evaluation approaches to truly sanitize models from sensitive content.

### Strengths
1. The paper is clear and well-structured.
2. Experiments are well-executed.
3. The authors have provided the accompanying code.

### Weaknesses
1. The paper evaluates black-box methods using a white-box approach. For example, Kumari et al. [1] already acknowledged their limitation in the white-box setting.

2. Clarification is needed regarding the attack scenarios presented. Specifically, it is unclear why an adversary with white-box access would seek to bypass a black-box model.

3. Assumption 5 in section 3 appears inconsistent with a white-box setting, particularly when considering Assumption 4, which grants the adversary computational resources. It raises the question of why an adversary could not alter the weights of the "erased" model under these conditions.

4. Regarding the practicality of the proposed attack method, it is important to note that widely-used public services such as Stability AI and DALL-E 3 do not currently accept text-embedding inputs to my knowledge. This may render the evaluation less critical, especially considering that existing methods effectively erase explicitly mentioned words.

### Questions
Please refer weakness part.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a comprehensive analysis of concept erasure techniques in the context of text-to-image diffusion models. The authors investigate the effectiveness of seven existing methods, which encompass both fine-tuning-based and inference-guiding-based approaches. Through their proposed concept inversion technique, the authors demonstrate that these current methods fall short in completely removing target concepts.

### Strengths
1. The motivation and storyline are reasonable and novel. The organization and most of the writing are clear, ensuring easy comprehension. The inclusion of preliminary experiments on Text Inversion is appreciated, as it demonstrates that the text inversion is not able to introduce additional knowledge to the model.

2. The authors conduct extensive experiments on the existing 7 works of erasure methods. The paper presents both qualitative and quantitative results, further enhancing its robustness.

### Weaknesses
1. While the concept inversion attack in this paper assumes full access to the diffusion model and erasure method, which may be seen as a relatively strong assumption, the reviewer acknowledges that the current setting still represents a significant advancement towards enhancing the safety of text-to-image (T2I) models. Therefore, this limitation can be considered a minor weakness rather than a significant drawback.

2. In Section 4.4, there are several points of misunderstanding that arise, pls see questions.



### Questions
1. There is curiosity about the behavior of the learned concept placeholder embedding in comparison to the embedding of the original concept name. This comparison could provide valuable insights into the effectiveness of the proposed approach.

2. Typo: inconsistency in the caption of Figure 7, which does not align with the order of the figure.

3. confusion regarding Section 4.4 

* How to understand ‘remapping the concept in token space’? Since the original text encoder and the embedding of the original text tokens are not updated, right?

* how the authors conducted experiments to demonstrate the editability, as the left figure of Figure 7 does not appear to clearly showcase this aspect?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Text-to-image generative models, widely adopted by the general public, present significant risks. These models can be exploited to generate sexually explicit content, mirror artistic styles without authorization, or even fabricate celebrity likenesses. A variety of methods have been proposed to "erase" sensitive concepts from these text-to-image models, some of which claim to "permanently remove targeted concepts from the weights." Empirical evidence across multiple test instances and use-cases like object removal and artistic style forgetting seem to support the efficacy of these erasure methods. However, the authors demonstrate that such post hoc concept erasure techniques are flawed and can be circumvented. They argue that these techniques essentially perform a form of input filtering, rendering them vulnerable to some more sophisticated text prompts. The authors introduce the "Concept Inversion" attack technique to recover erased concepts, effectively defeating seven recently announced hoc concept erasure methods across multiple use-cases. Their study calls into question the effectiveness of existing erasure methods and introduces a strong new evaluation methodology for future concept erasure research.

### Strengths
1. The authors offer a comprehensive introduction to the background, maintaining clear logic throughout the paper. Through diverse and reasonable experimental settings and evaluation methods that cover four different attack scenarios, the overall experiments are highly convincing, backed not only by objective numerical data but also by subjective evaluations from volunteers.

2. The experimental section of the article is detailed. The authors clearly expound on the principles behind the latest seven post hoc concept erasure methods and introduce adaptive concept inversion methods tailored for each. Each attack scenario is deeply analyzed, with proposed attack methods that are both clear and logical.

3. The authors' concept inversion method is effective, successfully circumventing most of the advanced Post hoc concept erasure methods. Even in instances where they could not break the SLD-Max method, as depicted in Appendix Figure 9, they provide a reasonable explanation in Appendix B.5.

### Weaknesses
1. The authors propose their attack methods under relatively lenient conditions, as evidenced by assumptions (1) and (2) in the PRELIMINARIES section. These assumptions are closer to a white-box setting. Specifically, the assumption that the attacker can add new tokens to the model's dictionary is unrealistic for most real-world scenarios, particularly those involving Machine Learning as a Service (MLaaS) platforms. In such platforms, the internal workings of the model, including the token dictionary, are typically inaccessible to the user. This significantly limits the practical applicability of the proposed Concept Inversion (CI) attacks. The TRANSFERABILITY method outlined by the authors in Appendix 4.4 also suffers from this limitation, as it relies on the ability to modify the model's internal dictionary, which is not feasible in a black-box setting. Therefore, the current CI attacks, while effective under the stated assumptions, appear to have limited effectiveness in more realistic black-box deployment scenarios, where the attacker has no access to the model's internal parameters or tokenization scheme.


### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes that the existing erasure methods do not fully excise concepts from the generative models. Special prompts can be used as attack procedures to regenerate the unsafe outputs.

### Strengths
1. The target issues of the paper are meaningful and worth exploring. This submission gives a valuable implementation of such an idea and presents good results. Existing work rarely explores the failure cases of concept erasure methods, while it is valuable.
2. The paper is generally well-written, clearly structured, and quite easy to follow.
3. Many experiments are conducted to verify the viewpoints.

### Weaknesses
1. The CI attack method is straightforward. Basically, this paper uses the existing methods, such as Textual Inversion (Gal et al., 2023), for the Concept Inversion Method. The CI methods lack insightful and novel design. The application of Textual Inversion, while effective, does not introduce a novel approach to circumventing the erasure methods; it primarily leverages an existing technique. The core contribution of the attack method seems to be in its application rather than in algorithmic innovation. A more sophisticated attack method, perhaps involving adversarial training or a more nuanced manipulation of the latent space, would have strengthened the paper's contribution.
2. It seems that this paper only shows a number of image cases. The experiments conducted on large-scale datasets are favored. The limited number of image examples makes it difficult to assess the generalizability of the proposed attack. The absence of quantitative metrics and large-scale evaluations makes it hard to determine the practical significance of the findings. A more rigorous evaluation on a diverse set of images and potentially other modalities would provide a more robust assessment of the proposed method.

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
