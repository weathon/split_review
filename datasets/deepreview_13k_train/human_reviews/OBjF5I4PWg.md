# Erasing Concept Combination from Text-to-Image Diffusion Model

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Advancements in the text-to-image diffusion model have raised security concerns due to their potential to generate images with inappropriate themes such as societal biases and copyright infringements. Current studies make a great process to prevent the model from generating images containing specific high-risk visual concepts. However, these methods neglect the issue that inappropriate themes may also arise from the combination of benign visual concepts. Considering that the same image theme might be represented via multiple different visual concept combinations, and the model's generation performance of the corresponding individual visual concepts is distorted easily while processing the visual concept combination, effectively erasing such visual concept combinations from the diffusion model remains a formidable challenge. To this end, we formulate such challenge as the Concept Combination Erasing (CCE) problem and propose a Concept Graph-based high-level Feature Decoupling framework (CoGFD) to address CCE. CoGFD identifies and decomposes visual concept combinations with a consistent image theme from an LLM-induced concept logic graph, and erases these combinations through decoupling oc-occurrent high-level features. These techniques enable CoGFD to erase visual concept combinations of image content while enjoying a much less negative effect, compared to SOTA baselines, on the generative fidelity of related individual concepts. Extensive experiments on diverse visual concept combination scenarios verify the effectiveness of CoGFD.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses a new problem in concept erasing, specifically targeting the erasure of harmful concept combinations while preserving the integrity of individual concepts. To tackle this issue, the paper proposes a two-step solution: it first constructs a concept logic graph using large language models (LLMs) to generate potential concept combinations from an initial seed. Next, it introduces a loss function designed to erase the harmful combinations in the high-level feature space while retaining individual concepts.

### Strengths
1. The paper introduces an important and practical problem in concept erasing by focusing on harmful combinations of otherwise harmless individual concepts. This approach is relevant to real-world applications, where harmful meanings can arise from specific combinations, even if the individual elements (e.g., “child” and “wine”) are harmless alone.

2. The proposed pipeline is well-targeted and reasonable for the problem, effectively combining concept generation through LLMs and a loss function tailored to erase only the harmful combinations.

### Weaknesses
1. The Reviewer agent's functionality may be limited. According to Appendix A.1, the Reviewer only checks the correctness of the Generator’s output without providing revision suggestions, contrary to what is stated in Section 3.2.1. This limitation could reduce the effectiveness of the concept logic graph generation. It would be helpful to include details of the generation process for each round in the Appendix to validate the roles of both the Generator and Reviewer in the pipeline.

2. The loss function does not directly enforce a reduction in P(c1,..,c_k). Instead, it relies on manipulating the similarity between high-level features. Without directly controlling P(c1,..,c_k) with a direction, the model may not achieve the desired reduction in joint probability, as it might simply adjust similarity in feature space without a concrete probabilistic effect on P(c1,..,c_k).  Alternative loss formulations may be more effective, such as ESD [1], which guides generation away from the target concept, or AC [2], which steers towards an anchor concept different from the target.

### Questions
1. Is there a distinction in disentanglement between erasing style combinations versus object combinations? Since different concepts may occupy different levels of feature representation, could they be disentangled at different stages of the denoising process?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper firstly formally formulates the Concept Combination Erasing (CCE) problem, which is overlooked by previous concept erasure works. This task aims to erase the model’s ability to generate images of specific concept combinations (e.g., kids drink wine) while preserving the generative quality of related concepts within the concept combinations (e.g., kids and wine). To solve this problem, the authors propose a Concept Graph-based high-level Feature Decoupling framework (COGFD), consisting of an LLM-based concept logic graph generation module and a gradient-based high-level feature decoupling module.

### Strengths
1. This work focuses on the CCE problem, which has generally been overlooked in previous concept erasure baselines. This problem is valuable and brings novel insights to this community.
2. This work proposes a baseline, termed COGFD, to solve CCE problem.
3. This work proposes HarmfulCmb Dataset, involving 10 harmful concept combination themes.

### Weaknesses
1. The formulation of CCE problem is not comprehensive. As the major contribution of this paper, the authors just define this task itself in Definition 3.1 without delving into other relevant aspects, such as taxonomy, problem scenarios, implications, and practical significance. For example, given the 4 cases in Fig. 1 (a), only the two cases "Kids drink wine" and "Muslim and pork" should be taken into consideration as CCE problem. Indeed, the case "A male wears blue tights and red cape" may involve the problem of copyrighted issues. This could be solved by current concept erasure method, which should not be categorized into CCE problem. As for the last case "Polar bear chases penguin", from my perspective, it would not invoke safety issues regarding offensive or copyrights, which should not be included in CCF or concept erasure.
2. Building upon the first point, it seems that the authors are unclear about the specific application scenarios of CCF. For example, in Fig. 4, there are cases about "Cat and Woman", "Car and Tree", "Child and Flower". These common concept combinations seem unrelated to security issues. Is it necessary for us to conduct disentanglement on these concept combinations?
3. It appears that the CONCEPT LOGIC GRAPH GENERATION WITH LLMS process requires manual annotations from the reviewer, which limits the flexibility and scalability of the method. Is there an automated annotation solution available?
4. Building upon the 3rd point, how many prompts were used during training, and what were they like? Additionally, what were the annotation costs and training overhead during training?
5. This work seems to overlook the issue of prior protection in concept erasure, which has been widely studied in existing research. As a security defense mechanism, the fine-tuned model needs to generate normal concepts; significant degradation of priors would render this technique ineffective.
6. How effective is this method in continually erasing multiple concept combinations, and does it suffer from catastrophic forgetting?
7. The proposed HarmfulCmb Dataset contains only 10 topics, most of which are related to children, smoking, and drinking. This dataset is too limited in both scale and the variety of topics it covers.
8. It seems that the CCE problem could be addressed using existing concept erasure methods. Intuitively, we could treat the composite concept as the target for erasure, with individual concepts as priors to be protected. Have you tried this approach, based on methods like ConAbl [1], MACE [2], or SPM [3]

### Questions
See the weaknesses.

### Soundness
2

### Presentation
1

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
This paper addresses the generation of inappropriate images by text-to-image diffusion models, which can arise from benign visual combinations. Introducing the Concept Combination Erasing (CCE) problem, the study proposes the Concept Graph-based high-level Feature Decoupling (CoGFD) framework. Using an LLM-induced concept logic graph, CoGFD identifies and erases problematic combinations, like children drinking wine, minimizing impact on image quality. Experiments show its effectiveness over standard methods.

### Strengths
The paper studies a new problem of concept combination and introduces a novel framework for addressing the challenge of erasing inappropriate concept combinations in image generation models, which involves Concept Graph-based high-level Feature Decoupling (CoGFD). Experimental results show the effectiveness of the proposed approach.

### Weaknesses
Although the proposed problem is interesting and practical, there are two major issues.

(1) The proposed solution may be overly complex. Current standard methods for preventing the generation of inappropriate concepts typically employ safety alignment techniques. A more straightforward approach could involve using a Large Language Model (LLM) to manage safety alignment. For instance, querying GPT-4 or Gemini about the appropriateness of a concept combination could yield direct feedback. An LLM can promptly identify and indicate whether a combination poses any issues for generation, as illustrated below.

----
**Example 1: Generate images about kids drink wine**

**Reply from GPT-4**: The prompt "Generate an image about kids drink wine" is inappropriate and problematic for several reasons:

Legal Concerns: It involves children in a context with alcohol, which is illegal and promotes underage drinking, a subject that is both illegal and ethically troubling in many jurisdictions around the world.

Safety and Ethics: It portrays minors in a harmful scenario, which could promote or normalize dangerous behavior to vulnerable audiences.

Platform Policies: Most content generation platforms, including text-to-image models, explicitly forbid the creation of content that involves unsafe or harmful activities, especially with children.

----

**Example 2: Generate images about Muslim and pork**
**Reply from GPT-4**: The prompt "Generate an image about Muslim and pork" is potentially sensitive and could be seen as disrespectful or offensive due to religious considerations. In Islam, pork is considered haram (forbidden), and depicting Muslims with pork could be seen as culturally insensitive or mocking religious practices.

It's important to handle religious themes with respect and sensitivity, avoiding content that might be seen as disrespectful or inflammatory towards any religious group. If you're aiming to discuss or depict religious dietary laws or cultural practices, it's advisable to do so in an educational or respectful manner that provides accurate information and context.


----

As such, it is suggested to discuss tradeoffs between using LLMs for filtering vs. directly modifying the diffusion model, such as inference time, robustness to adversarial prompts, or ability to handle edge cases.



(2) Some of the demonstrated examples may not reflect realistic scenarios, such as cats depicted in a sketch style. It is recommended to use more practical prompts that address real-world issues and demonstrate results with specific styles for specific objects. For instance, an example could involve the use of a distinct art style, such as Disney's animated character design, applied to generic animal figures. This would help assess the model's handling of potential copyright issues when a distinctive artistic style, known for its association with copyrighted material, is applied to common subjects. To this end, it is suggested to include experiments with specific real-world scenarios that demonstrate the method's effectiveness on issues like copyright infringement or cultural sensitivity, in addition to the current examples.

Last but not the least, there are two minor issues.
(1) One important paper in ICLR 2024 is not cited [A]. It is suggested to discuss the difference between this approach and the proposed approach.
[A] Yu-Lin Tsai et al., Ring-A-Bell! How Reliable are Concept Removal Methods For Diffusion Models?, International Conference on Learning Representations, 2024.
(2) This paper does not clearly specify the number of images used to evaluate the Fréchet Inception Distance (FID), which could lead to biased results. For a robust and statistically reliable evaluation, it is recommended to use a minimum of 10,000 images. Ensuring a sufficiently large dataset is crucial to avoid potential biases and provide more accurate assessments of the model's performance.

### Questions
A critical question remains: "What are the advantages of applying the proposed method over using a Large Language Model (LLM) for filtering unsafe prompts of concept combinations?" The motivation behind choosing an alternative to the established LLM-based safety alignment approach is not clearly articulated. It is essential to justify why the proposed method is preferable, including any benefits in accuracy, efficiency, or effectiveness in handling complex safety scenarios that LLM methods might miss. This justification will help clarify the necessity and value of the proposed approach within the field. For instance, could you show the rejection ratio when feeding the combined concepts used in this paper into the LLM, e.g., GTP-4/Gemini?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Concept Combination Erasing (CCE) problem, which addresses the challenge of preventing inappropriate concepts in images generated by combining benign visual concepts. They authors propose COGFD (Concept Graph-based high-level Feature Decoupling), a novel framework that identifies and decouples harmful visual concept combinations using a concept logic graph. Experimental results show that COGFD outperforms state-of-the-art methods in erasing inappropriate concept combinations while maintaining high image generation quality for related individual concepts.

### Strengths
1. The paper tackles a novel problem—the Concept Combination Erasing (CCE) problem—which addresses the issue of inappropriate image generation not from individual harmful concepts, but from combinations of benign concepts. This problem is meaning and practical in general, and is an original extension of concept erasing in diffusion models. The proposed COGFD framework is quite novel, particularly in its use of concept logic graphs generated by LLMs and the novel high-level feature decoupling method to preserve individual concepts while erasing harmful combinations. 

2. The authors conduct comprehensive experiments across diverse scenarios to demonstrate the effectiveness of proposed method. They also conduct experiments to explain why the use of logic graphs works. The analysis is also convincing.

3. The writing is clear to follow and the demonstration of figures are also good.

### Weaknesses
1. The paper tackles a novel problem—the Concept Combination Erasing (CCE) problem—which addresses the issue of inappropriate image generation not from individual harmful concepts, but from combinations of benign concepts. This problem is meaning and practical in general, and is an original extension of concept erasing in diffusion models. The proposed COGFD framework is quite novel, particularly in its use of concept logic graphs generated by LLMs and the novel high-level feature decoupling method to preserve individual concepts while erasing harmful combinations. 

2. The authors conduct comprehensive experiments across diverse scenarios to demonstrate the effectiveness of proposed method. They also conduct experiments to explain why the use of logic graphs works. The analysis is also convincing.

3. The writing is clear to follow and the demonstration of figures are also good.

1. The paper serves as a blue team tool to defend DMs against inappropriate contents. However, as far as I know, there have already been some quite strong red team tools for this topics, such as [1] and [2]. The paper doesn't show its performance against these red team tools.

2. The method relies on LLMs to construct the concept graph. But LLMs themselves can sometimes generate inconsistent or erroneous logic, for example, as indicated in recent research [3]. This might impact the quality of the concept graph and ultimately the performance of COGFD.

3. Although the paper highlights that COGFD preserves individual concepts, it falls short of providing an in-depth analysis of whether any degree of concept erosion still occurs for these harmless concepts. For example, does image quality deteriorate in certain combinations? Are there instances where the method unintentionally modifies the appearance or characteristics of harmless concepts (e.g., distorting "wine" when used alone after its combination with "kids" is erased)?

### Questions
See weakness. 

Still, my biggest concern is the method's performance against red team tools. These red team tools are black-box and easy  to implement, so they are indeed big threats to the blue team tools in real practice. I wonder how the proposed method behaves under the challenge of these red team tools.

### Soundness
3

### Presentation
4

### Contribution
3
