# BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Large multi-modal models inevitably decay over time as facts change and previously learned information becomes outdated. Traditional approaches such as fine-tuning are often impractical for updating these models due to their size and complexity. Instead, direct knowledge editing within the models presents a more viable solution. Current model editing techniques, however, typically overlook the unique influence ranges of different facts, leading to compromised model performance in terms of both generality and locality. To address this issue, we introduce the concept of the generality-locality trade-off in multi-modal model editing. We develop a new model editing dataset named OKEDIT, specifically designed to effectively evaluate this trade-off. Building on this foundation, we propose \textbf{BalancEdit}, a novel method for balanced model editing that dynamically achieves an optimal balance between generality and locality. BalancEdit utilizes a unique mechanism that generates both positive and negative samples for each fact to accurately determine its influence scope and incorporates these insights into the model's latent space using a discrete, localized codebook of edits, without modifying the underlying model weights. To our knowledge, this is the first approach explicitly addressing the generality-locality trade-off in multi-modal model editing. Our comprehensive results confirm the effectiveness of BalancEdit, demonstrating minimal trade-offs while maintaining robust editing capabilities. Our code and dataset will be available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Existing knowledge editing methods often overlook the influence scope of a knowledge edit, leading to limited generality and locality about samples similar to the edited ones. This paper proposes a novel method, BalancEdit, to optimize the trade-off between generality and locality. To assess this trade-off, this paper constructed a new dataset, OKEDIT. Experimental results demonstrate that BalancEdit outperforms existing methods in both single and sequential editing settings.

### Strengths
The issues addressed in this paper are of considerable significance. Existing editing methods affect the performance of the edited model on samples related to the edited ones. This paper proposed a new method to adjust the influence radius dynamically. The innovative approach of using positive and negative samples to estimate the influence radius of each knowledge edit is particularly commendable. Additionally, the paper clearly articulates the above issues and presents corresponding solutions.

### Weaknesses
1. The proposed method builds upon Grace [1], with the key differences being using positive and negative samples to estimate the influence radius and the fine-tuning of the transformation layer. However, the paper does not include an ablation study to evaluate the contributions of these two modules.
2. The proposed dataset OKEDIT employs GPT-4 and a diffusion model to generate rephrased images for assessing image generality. However, previous studies have noted that generated images may shift in content, leading to inconsistencies with the original images [2]. 
3. The use of the harmonic mean (HM) is questionable, as the presence of a minimum can result in a lower harmonic mean. In Table 3, the FT method applied to BLIP2-OPT shows a performance of less than 1% on the locality.

[1] Aging with GRACE: Lifelong Model Editing with Discrete Key-Value Adaptors
[2] VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark

### Questions
1.Why is the accuracy for the Base model in Table 3 not 0? In my humble opinion, the Acc and Loc should be 0 and 100 respectively, similar to the results presented in [1]. 
2. Why were sequential editing experiments conducted on OKVQA instead of MMEdit and OKEDIT, as proposed in this paper?
3. Previous studies have indicated that the MEND method can produce NaN values [2] during sequential editing; however, this issue does not appear in Table 4. Are there differences in the sequential editing settings between this study and [2]?
4. IMHO, if the weights in the language module are edited, it is essential to measure text locality and compare it with other methods.
5. The paper states that black images are used as negative samples across various visual recognition tasks. It would be beneficial to include citations to support this approach.
6. Some proprietary terms, such as MiniGPT-4 and BLIP-2 OPT, are used inconsistently throughout the text.

[1] Can We Edit Multimodal Large Language Models？
[2] VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
BalancEdit introduces a new model editing approach, addressing the limitations of traditional model editing techniques. Unlike existing methods, which often ignore the distinct influence of different facts, BalancEdit strikes an optimal balance between generality and locality. By using a codebook of localized edits and generating both positive and negative samples, it accurately assesses each fact's impact without altering the model's core structure. Tested on the newly developed OKEDIT dataset, BalancEdit demonstrates robust editing performance with minimal trade-offs, marking a significant advance in multi-modal model editing.

### Strengths
The motivation is good, particularly the attention to balancing generality and locality in model edits. 
The approach for setting the influence radius is straightforward, requiring no additional training, which enhances usability. 
Additionally, the model demonstrates good efficiency in terms of both time and data requirements.

### Weaknesses
The method’s visual reasoning goal is limited, offering little differentiation from MMEdit, especially as the test data format remains similar and is based on question answering. 

Using a black image as a negative sample is simplistic and may fall short in defining an "optimal balance between generality and locality." Consequently, the hyperparameter alpha is fixed, potentially limiting flexibility.

Images in the generality and locality tests are generated by a diffusion model, which offers limited advancement over MMEdit due to inconsistent image quality.

The study uses Blip2-OPT and MiniGPT-4 as baseline models, which are somewhat outdated and limited. Architectures like LLaVA and related models may yield different results.

Writing issue:
There is a major issue on page 10, lines 489-514, where two paragraphs convey the same information, likely due to an unintentional oversight.
Typo: Line 723: “labelis”
Line 862: missing reference
Table 3: some bold texts are not best results
The example in figure 4 is confusing, because the first image and the rest two has significant difference, and the main subject is two people rather than a church.

### Questions
As those mentioned in weakness:

Does the visual reasoning goal in this approach offer substantial differentiation from MMEdit, given the test data's similarity in the form of QA? 

Could a more sophisticated method replace black images as negative samples to better define the balance between generality and locality?

How significant is the impact of using diffusion model-generated images for testing generality and locality, considering their variable quality? Do you verify the image quality by any means (especially human verification), check if the generated images could be used for test?

Would using more recent model architectures, like those in the LLaVA series, yield different results in these experiments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
BalancEdit presents a new solution for updating large multi-modal models by achieving a balance between generality and locality in model edits. By introducing the OKEDIT dataset, this approach evaluates and addresses the generality-locality trade-off, a challenge overlooked by other methods. BalancEdit showcases minimal compromise in model performance, offering a robust and efficient approach to knowledge editing without altering the model's core weights.

### Strengths
The motivation of balancing generality and specificity in model editing is good. 

The method for determining the influence radius is simple and requires no extra training, which improves usability. 

Moreover, the model shows good efficiency in terms of both time and data usage.

Introducing more generality test for each editing case is beneficial.

### Weaknesses
Using a black or white image as a negative sample is straightforward but may not achieve an optimal balance between generality and locality.

The editing method involves finetuning a layer, which may be simplistic. Additionally, the experimental results lack comparison with the SERAC method.

About image quality, I have some doubts on diffusion generated images, which are used as tests. From fig 4, the second image is totally different from the first image. From fig 6, the first and third examples of generality test are entirely different from the editing sample, making the test results questionable.

The experiments involve Blip2-OPT and MiniGPT-4. However, considering the fast development of MLLMs, the newer models like LLaVA series, which are widely recognized, should be tested.

### Questions
As those mentioned in weakness.

Additions:

How many locality test image for each editing case? If only one image, this can be imbalanced because generality test has 10 images for each.

Do you verify the quality of generated images? How do you verify them?

Why don’t you present the results of SERAC method?

Writing issue:

Table 3: Misuse bold texts, some are not best results.

A critical issue exists on lines 489-514, where two paragraphs redundantly convey the same information. This appears to be a significant oversight of the content.

Missing reference in ine 862

### Soundness
2

### Presentation
1

### Contribution
2
