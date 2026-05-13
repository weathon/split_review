# LayoutNUWA: Revealing the Hidden Layout Expertise of Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
\vspace{-4mm}
Graphic layout generation, a growing research field, plays a significant role in user engagement and information perception. 
Existing methods primarily treat layout generation as a numerical optimization task, focusing on quantitative aspects while overlooking the semantic information of layout, such as the relationship between each layout element. 
In this paper, we propose LayoutNUWA, the first model that treats layout generation as a code generation task to enhance semantic information and harnesses the hidden layout expertise of large language models~(LLMs). 
More concretely, we develop a Code Instruct Tuning (CIT) approach comprising three interconnected modules: 1) the Code Initialization (CI) module quantifies the numerical conditions and initializes them as HTML code with strategically placed masks; 2) the Code Completion (CC) module employs the formatting knowledge of LLMs to fill in the masked portions within the HTML code; 3) the Code Rendering (CR) module transforms the completed code into the final layout output, ensuring a highly interpretable and transparent layout generation procedure that directly maps code to a visualized layout. 
We attain significant state-of-the-art performance (even over 50\% improvements) on multiple datasets, showcasing the strong capabilities of LayoutNUWA.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method to instruction-tune LLMs for layout generation task. Utilizing pre-trained LLMs and formulated as a code-generation task, the proposed method can build upon the semantic knowledge about geometries and code in the LLMs and achieve SoTA performance for conditional layout generation tasks. This paper further explores both domain-specific and domain-agnostic settings, demonstrating that a single LLM instruction-tuned in multiple domains can achieve SoTA performance in multiple domains.

### Strengths
- Achieved SoTA in Layout Generation tasks in multiple domains with a single LLM. 
- Extensive experimentation with multiple baselines, model variants, tasks and datasets.
- Enabled LLMs to generate layouts, which opens up possible research avenues for complex language-based interactions in the layout generation space.

### Weaknesses
- *Limited Architectural Novelty from Fine-tuning LLMs*
- *Constrained Tasks and Conditions*: While the evaluated tasks are established and important for fairly comparing against existing work, I believe the paper can be significantly improved by exploring more complex, language-based interactions, given that LLMs are used to perform the layout generation task for the first time. It would significantly improve the contribution if the author(s) can explore (could be preliminary) whether LLMs can fuse its natural language / common task knowledge with layout generation, such as having a conversation with users about their layout generation constraints, or specifying the use-cases of the layouts.
- *Potential limited diversity and overfitting*: The qualitative generation results appear very similar to the real design, and it is unclear whether the model can generate diverse layouts given a single condition, or if the model has overfitted to a certain specific layout. I suggest the author(s) to include the most similar training example to the generation (by DocSim) in a figure in the appendix. Please also see questions below for addressing my concerns.

Because of these concerns, I am currently on the fence about accepting this paper, but I am willing to raise my score if these concerns are addressed adequately in the rebuttals.

### Questions
- Regarding the potential diversity and overfitting, I wonder if the author(s) can show whether the model can generate diverse layouts during the sampling process, given the same input conditions. Moreover, I wonder if the 'real design' in the Figures (e.g., Fig 5) are taken from the training or validation set? It could indicate overfitting given the high similarity between real designs and the generated designs in LayoutNUWA, especially given the LLMs  are significantly larger in size over prior work.

- Have the author(s) also explored unconditional generation? It would be good to understand the capability of the models to generate diverse layouts unconditionally, following the point above.

- While the domain-agnostic model is impressive, I wonder if the author(s) have observed domain confusion? Such as the model generating a magazine layout (when prompted to generate a mobile layout (from RICO).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles the task of graphic layout generation. Previous works usually treat this task as a numerical optimization problem, whereas this paper proposes to leverage the knowledge of LLMs for layout generation. Specifically, the authors propose a Code Instruct Tuning framework with three components: Code Initialization, Code Completion, and Code Rendering. The proposed method achieves strong performance compared with current SOTAs on three datasets, RICO, PubLayNet, and Magazine.

### Strengths
- The paper is well organized and easy to read.

- Utilizing LLMs for layout generation seems a good way to tackle this graphic layout generation task. The code template also supports three different variants for code completion task.

- The paper provides strong results compared with baseline models, as well as several ablation studies including LLaMA2/CodeLLaMA, Domain-Specific/Domain-Agnostic settings, and code/numerical output formats.

### Weaknesses
- This paper focus on graphic layout generation. Even though LLMs are not used for this specific task, layout generation via LLMs seems not novel [1,2,3]. Therefore, the novelty of this paper is not very strong. 



[1] Cho, Jaemin, Abhay Zala, and Mohit Bansal. "Visual Programming for Text-to-Image Generation and Evaluation." arXiv preprint arXiv:2305.15328 (2023)

[2] Feng, Weixi, et al. "LayoutGPT: Compositional Visual Planning and Generation with Large Language Models." arXiv preprint arXiv:2305.15393 (2023)

[3] Lian, Long, et al. "LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with Large Language Models." arXiv preprint arXiv:2305.13655 (2023).

### Questions
The authors mention that LayoutNUWA suffers from the error propagation problem. Some visualizations/examples might be useful to illustrate this point.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a new approach for the layout generation task. The proposed method treats layout design as an HTML code formulation and harnesses the power of a large language model to fill in the masked attributes. The proposed method operates in three primary phases: it begins by transforming the given conditions into an initialized HTML code. Subsequently, the language model is deployed to predict the final output including the masked attributes. Finally, this output is translated back into a layout design. The experiments on three datasets, (RICO, PubLay, and Magazine) show the improvement over the state-of-the-art methods in different settings.

### Strengths
The paper presents is easy to follow. The proposed approach to utilizing the capabilities of LLMs for layout design, particularly through the formulation of HTML codes, is novel to the best of my knowledge. Moreover, the proposed technique surpasses current state-of-the-art methods, especially when tested on the Magazine dataset.

### Weaknesses
A significant limitations that in my view is its inability to incorporate non-categorical data, such as image embeddings. This constraint considerably narrows the method's applicability in real-world situations, especially when users input attributes that aren't readily translatable for language models.

The presentation could benefit from further refinement. Specific implementation details are missing, including the number of training iterations, batch size, learning rate, etc. Furthermore, Figure 3's organization makes it challenging to visually compare the proposed method against both the original design and LayoutDM as the state-of-the-art method.

Given that prior techniques were optimized for domain-specific settings, the enhancements seen in the "LayoutNUWA-*-DS" variants don't come across as particularly robust, as evidenced by metrics like the FID in the RICO dataset. This limitation, coupled with the inherently slower processing speed of LLMs compared to other methods, may limit the method's broader application.

### Questions
As I understand, the authors also pass the layout size as the initialization part. However, this is not given in for example LayoutDM to the best of my knowledge and can be a strong signal to the model. Can you clarify on this part?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles conditional layout generation by formulating it as code generation and leveraging the prior knowledge of large language models (LLMs) to improve the performance of layout generation.

The main technical contribution is a code instruct tuning (CIT) method specialized in conditional layout generation, which consists of three components: 1) a code initialization module to convert input conditions into a masked HTML code; 2) a code completion module to predict the masked values using LLM; 3) a code rendering module to render the completed code into the final layout.

### Strengths
1. The idea of leveraging LLMs for conditions layout generation is very interesting, which has not been explored previously. The attempt of this paper on bridging LLMs and layout generation is inspiring, which provides a new perspective to layout modeling.

2. The performance improvement on the Magazine dataset is impressive.

### Weaknesses
1. The amount of technical contribution is limited. While the paper claims that a novel CTI approach is contributed, the technical innovation of the CTI is not significant since it only involves a simple solution to converting layout data to a LLMs-readable format (template generation), and some small modifications to adapt LLMs to layout generation (such as element order permutation and multi-task modeling). Therefore, the technical contribution that the paper can make to the ICLR community may not be significant. 

2. The experiment setup is questionable. First, the proposed method, in theory, can support both conditional and unconditional layout generation (e.g., by setting the task instruction in Sec. 3.2.1 properly and tuning the LLM to generate the entire code instead of just the masked values). However, only the experiments on conditional generation are presented now, and there is no evaluation on unconditional generation that most of the previous works primarily aim for. Thus, a (potentially) key capability of the proposed method (also a problem interesting to the layout modeling community) is ignored in the paper. Second, LayoutGAN++ is only trained for the “C -> S + P” task. It is unclear how it is adapted to solve the other two conditional generation tasks in the experiments. Third, LayoutDM is only trained for unconditional generation, which is then adapted to conditional generation without any fine-tuning or re-training. In contrast, the proposed method is especially fine-tuned for various conditional generation tasks. As a result, direct comparison between LayoutDM and the proposed method under such a setting is unfair.

3. The performance on RICO and PubLayNet is unsatisfactory. As shown in Table 2, the advantage of the proposed method over SOTA methods is marginal on average. This is somewhat below expectation given the fact that the proposed method is based on large pre-trained models and has a chance to observe more training data (under the DA setting).

### Questions
1. In Eq.(3), what does M_j^t denote? What is the definition of L on the right hand side of the equation?

2. From the results in Table 1 and 2, the performance improvement on RICO and PubLayNet is not as significant as on the Magazine dataset. What are possible reasons behind this?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
3 good
