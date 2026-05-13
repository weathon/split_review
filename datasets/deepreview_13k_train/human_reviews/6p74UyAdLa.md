# Dynamic Negative Guidance of Diffusion Models

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Negative Prompting (NP) is widely utilized in diffusion models, particularly in text-to-image applications, to prevent the generation of undesired features. In this paper, we show that conventional NP is limited by the assumption of a constant guidance scale, which may lead to highly suboptimal results, or even complete failure, due to the non-stationarity and state-dependence of the reverse process. Based on this analysis, we derive a principled technique called \textit{\textbf{D}ynamic \textbf{N}egative \textbf{G}uidance}, which relies on a near-optimal time and state dependent modulation of the guidance without requiring additional training. Unlike NP, negative guidance requires estimating the posterior class probability during the denoising process, which is achieved with limited additional computational overhead by tracking the discrete Markov Chain during the generative process. We evaluate the performance of DNG class-removal on MNIST and CIFAR10, where we show that DNG leads to higher safety, preservation of class balance and image quality when compared with baseline methods. Furthermore, we show that it is possible to use DNG with Stable Diffusion to obtain more accurate and less invasive guidance than NP.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, a new concept called Dynamic Negative Guidance (DNG) is proposed, which is an improvement on the existing Negative Prompting (NP) method in diffusion models.

### Strengths
1. By dynamically adjusting the intensity of negative prompts, DNG solves the problem that the traditional NP method may encounter suboptimal results or complete failures in the generation process.
2. The structure of the paper is clear and the content is well organized.
3. DNG combines the needs of diffusion model (DMs) and condition generation, and estimates the posterior probability by tracking discrete Markov chains in the generation process. This method is an innovative extension of the existing technology.

### Weaknesses
1. Although the paper has been experimentally verified on MNIST and CIFAR10 datasets, the performance of DNG for more complex tasks (Text to image) has not been fully verified. Specifically, the paper lacks a rigorous evaluation of DNG's performance on datasets with high semantic variability and complexity, such as ImageNet. The current experiments are limited to relatively simple datasets, which may not fully reveal the potential limitations of DNG in more challenging scenarios. The absence of a thorough analysis on diverse image semantics and complexity raises concerns about the generalizability of the proposed method.
2. DNG is compared with NP and SLD methods in this paper, but the comparison of each method may lack in-depth analysis, especially the performance comparison under different parameter settings. The paper does not explore the sensitivity of each method to various hyperparameter configurations. For instance, the guidance scale in NP and the threshold parameter in SLD could significantly impact their performance, and a detailed analysis of how these parameters interact with the performance of each method is missing. This lack of a comprehensive parameter study makes it difficult to draw definitive conclusions about the superiority of DNG over existing methods.

### Questions
1. You have demonstrated the effectiveness of DNG on the MNIST and CIFAR10 datasets. How does DNG perform on more complex and diverse data sets, such as ImageNet, especially on different image semantics and complexity?
2. The paper contains some visualizations, but can you provide more detailed visualizations to show the progressive impact of DNG in the image generation process, especially how it dynamically adjusts in the denoising step?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors argue that conventional negative prompting methods are constrained by the assumption of a constant guidance scale. To address this limitation, they propose a novel dynamic negative guidance technique that adapts the guidance scale based on both time and state, aiming for near-optimal modulation. Notably, this approach does not require additional training. The authors evaluate their method on MNIST and CIFAR10, comparing it against various baselines, and demonstrate its effectiveness. They also show that the technique integrates well with Stable Diffusion, offering improved accuracy in defining negative prompts.

### Strengths
• The proposed method demonstrates promising results on MNIST and CIFAR10, outperforming standard negative prompting techniques and safe latent diffusion methods. This improvement suggests that the dynamic guidance approach offers a meaningful advantage in generating more accurate outputs for image datasets with complex features.

• Preliminary results with Stable Diffusion also appear promising, indicating that the method may effectively enhance prompt accuracy within more sophisticated generative models. However, additional evaluation would further substantiate these findings and provide more insight.

• Though a minor detail, the use of color highlights in algorithms and formulas is a thoughtful touch that enhances readability.

### Weaknesses
• There is a lot of research happening in the field of negative prompting, yet this paper lacks a comprehensive comparison with many  leading methods. An in-depth comparison would have more clearly illustrated the strengths and limitations of this approach relative to existing techniques, helping to clarify its unique contributions.

• Overall, the evaluation of the proposed method lacks depth. A more thorough and systematic assessment across various scenarios and metrics would strengthen the validity of the results and give a clearer picture of the method’s real-world applicability and robustness. Specifically, the evaluation should include a more diverse range of negative prompts, including those that are semantically related to the positive prompt, to assess the method's ability to handle complex scenarios. Furthermore, the current evaluation primarily focuses on class-conditional generation, while the method's applicability to more complex text-to-image generation scenarios is not sufficiently explored.

• As acknowledged by the authors, a significant limitation of this manuscript is the limited evaluation of text-to-image generation, which is the primary application area for this method. Without a comprehensive exploration of T2I use cases, the potential impact of this work is somewhat undermined, leaving much of its promise unexplored. The current T2I evaluation lacks a systematic approach, and it is unclear how the method performs with different types of prompts and across various image styles. A more thorough analysis is needed to demonstrate the method's effectiveness in real-world text-to-image generation scenarios.

• Additionally, the absence of quantitative metrics is a notable gap. Deferring these metrics to future work is a missed opportunity, as they would have added rigor to the analysis and allowed for a more objective assessment of the method's effectiveness. The lack of quantitative metrics makes it difficult to compare the proposed method with existing techniques and to assess its performance in a systematic manner. The authors should include metrics such as FID or CLIP score to provide a more objective evaluation of the method's performance.

### Questions
Given that you acknowledge these limitations in the manuscript, could you clarify why they were not addressed in the current version? Including these aspects seems essential to strengthen the manuscript's rigor and completeness.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In text-to-image generation, negative prompts are used to guide the generative model not to create something. This paper presents a method called dynamic negative guidance that aims to be safer, less invasive than regular negative prompting in guiding a T2I model to create desirable images while avoiding unwanted components. The dynamic negative guidance relies on a near-optimal time and state dependent modulation of the guidance without requiring additional training. The method has been tested in MNIST and CIFAR-10.

### Strengths
A strength of the proposed method, DNG, is to estimate the posterior by tracking the discrete Markov chain during the denoising process. The strength of the guidance is dynamically related to how close the negative prompt is related to the positive prompt. This seems to a strength of the method since it can adaptively determine whether the negative prompt is even relevant at all. To the contrary, existing negative prompting methods may not be able to ignore irrelevant negative prompts. The proposed method may overcome the weakness of existing NP methods that blankly try to invert the force field to move away from the positive prompts without precisely moving away from the negative prompts. This is reflected in the factor pt(c-|x)/(1−pt(c-|x)) in Eq 10.

### Weaknesses
Writing can be better and consistent. For example, the paper has both c_- and c-, it should be consistent.
The biggest weakness with the paper is the example images given at the end, starting from page 22. First, the pictures are so small, it is hard to appreciate the difference between NP results and DNG results. Second, I could be missing something, but it seems there is no big difference between the two types of results. In particular, it seems NP results are not bad or accidently include the undesirable features given in the negative prompts. 
Similar comment for Figure 6, as it does not seem that NP results in the presence of negative prompt "view of skyline" is incorrect.

### Questions
While the mathematical derivation of DNG looks reasonable, the generated image examples are hard to understand. 
Can authors point out the difference between NP results and DNG results in the example figures, such as Figure 6 and figures starting on page 22? 
The purpose of experiments of Section 4.1 and corresponding Figure 5 are not clear. I don't understand why the experiments need to remove one class in MNIST and one class in CIFAR-10. If the purpose of the method is to avoid generating undesirable features, shouldn't the model be trained on all classes and only in practical use of the method, one can prompt the model to not generate something, for example, not to generate number zero or an airplane. Or am I missing something here.
While Table 2 lists the positive prompts and related and unrelated negative prompts, can authors give examples on how exactly a full prompt was written up in English and fed to a T2I model? 
In Figure 10(b), as the authors explained, because SLD may have less invasiveness, it gave better FID than DNG, which is reasonable, but why from the figure it seems NP also had a lower FID than DNG as % of wrong images went up? Can authors elaborate on this?
From both Figure 10(a) and (b), it seems that NP had overall worse performance than SLD and DNG, but it also appears that NP performance in KL divergence and FID had a decreasing pattern while those of DNG appeared to pick up at higher % of wrong images, what could be the reason behind this observation? Can authors discuss about this?
Figure 11, for illogical prompts, the guidance scales were larger at later diffusion time than at early diffusion time, can authors provide intermediate generative results corresponding to this change of the guidance scale?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Dynamic Negative Guidance (DNG), a novel technique for improving Negative Prompting (NP) in diffusion models, specifically addressing limitations in text-to-image applications. Conventional NP assumes a fixed guidance scale to suppress undesired features, which can result in poor performance due to the non-stationary and state-dependent nature of the reverse process in diffusion models. DNG overcomes this by introducing an adaptive approach that adjusts the guidance dynamically based on time and state, thereby refining the model’s ability to avoid generating unwanted features.

### Strengths
1. the DNG method in novel and has strong practical significance
2. paper did a comprehensive evaluation on safety, class balance, and image quality on MNIST and CIFAR10.
3. the paper is straightforward and easy to follow

### Weaknesses
1. terms like Dynamic Negative Guidance and guidance scale could better deserve a brief contextual note, as not all readers may be familiar with their meaning in this context.
2. the paper needs to avoid jargon without explanation.
3. the paper needs to improve flow and conciseness.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3
