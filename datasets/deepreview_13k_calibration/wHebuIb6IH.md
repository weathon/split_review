# VLMaterial: Procedural Material Generation with Large Vision-Language Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Procedural materials, represented as functional node graphs, are ubiquitous in computer graphics for photorealistic material appearance design. They allow users to perform intuitive and precise editing to achieve desired visual appearances. However, creating a procedural material given an input image requires professional knowledge and significant effort. In this work, we leverage the ability to convert procedural materials into standard Python programs and fine-tune a large pre-trained vision-language model (VLM) to generate such programs from input images. To enable effective fine-tuning, we also contribute an open-source procedural material dataset and propose to perform program-level augmentation by prompting another VLM. Through extensive evaluation, we show that our method outperforms previous methods on both synthetic and real-world examples.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a framework for finetuning a VLM for generating procedural materials that matches an input image. A new procedural material dataset collected and curated from various sources, and then augmented with an LLM based approach. Output generated from the finetuned VLM also undergoes a MCMC-based gradient free optimization step to bring it closer to the input image. The results are impressive both qualitative and quantitatively, and with better generalzation capacities.

### Strengths
- Personally, I always enjoy seeing papers that show "foundation models work on X". Even if there is minimal contribution architecture and algorithm wise, it still provide me with insight about what kind of tasks can benefit from large models. This paper adds even more evidence about the viability of applying LLM/VLMs to procedural generation (and graphics in general), and I find this message important.
- Beyond the rather straightforward application of LLM + finetuning, considerable works as also being done here for creating the finetuning data. There are valuable insights on how data is cleaned and augmented, and the LLM based approach for creating new samples from two examples seem generally applicable for anything that involve visual programs. The dataset itself can also be immensely useful, especially when the alternative is not publicly/easily accessible.
- Solid insights on how to work with procedural material graphs that a not differentiable. The MCMC based approach is reasonable, appears to be working from the ablations and examples. It is also nice (and a bit nolstalgic) to add some exposure to a classic set of optimization methods and show that they are very viable in certain cases.
- The results look good. I do have a good amount of issues with some results but overall, it does appear to be that there are cases where the proposed method works clearly better than alternatives. Ablation is also solid and effective.

### Weaknesses
 - Also I do appreciate the message that "VLM works for procedural materials", arguably the novelty is limited. This is one of the lower hanging fruits, and a good amount of work is engineering-centric, making the impact of this work potentially limited. It probably also makes this paper less suitable for a venue like ICLR, since there isn't too much contribution learning-wise. I would definitely love to see this at a graphics venue a bit more.
- Following the previous point - even for paper that's mostly "apply VLM to X", the amount of insights in the paper is still on the relatively low end. Most of the discussion is around the data. They are important, and I do consider the data portion a strength. However, I feel that there's missed opporunities here in further invesgitating how to best apply VLMs to this problem, especially since the supervision is entirely token level, without visual feedback (comparing the generated material to the input). E.g. there are many known limitations with VLM/LLMs that make them not perfectly suitable for directly outputing complex visual programs with lots of parameters that are non-trivial to interpret on a purely language level. How to design something that alleviate such issues? Does fine tuning take care of most of it or do we need to more carefully design/modify the language and the prompts? What part of the output do the model struggle the most with? Is there a more intuitive explanation of why failure cases like those in Figure 7 happen, and what part of the output contribute the most to the discrepancy between the output material and the image (e.g. it does appear that many BSDFs are quite off?)? Discussions along these lines would be very helpful both for people who want to use this approach, or for future researchers that might build upon this.
- My standard on quality of results is definitely higher on this one, due to the rather limited amount of technical insights. And while the results look good overall, they are still quite far from matching the input image, even among the few qualitative examples provided and after the post-processing step.

### Questions
I am overall positive on this one. Despite the rather limited novelty and lack of deeper exploration, there is still solid data contribution, a good amount of insights, and solid results. I won't champion this paper in its current state, but more "insights" (see weakness section above) will most likely move me towards a more positive stance on this paper.

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
5

### Summary
VLMATERIAL generates a procedural node based material pipeline from a given input image. The authors create a dataset (will be open sourced) of pairs of material images and their corresponding graphs by doing clever data augmentation for paramters and node structure. The material graphs are also obtained as Python programs. A VLM is fine tuned on this data to generate a python program to create a material graph from an input image. The method is evaluated on in-distribution (Blender) as well as out-of-distribution data(Adobe substance + real images) and an ablation is performed.

### Strengths
* The paper is well-written and motivated. All things are explained clearly. 
* The work aims to address a significant issue of directly generating a material graph from an input image as this is highly desriable in CG pipelines. Compared to existing work such as MatFormer and Conditional MatFormer, the results are superior. This is also proven quantitaively in Table 1 against baselines.
* The method creates a large datasset by performing augmentation using an LLM which picks 2 sample programs and then creates a distinct program. 
* The VLM in the loop to generate a dataset and also synthesize programs after fine tuning is simple but novel in material generation. 
* The ablation results are strong. A test for program correctness is also included.

### Weaknesses
 * The method is 90% accurate in terms of program correctness compared to other methods which have guaranteed correctness. Have the authors explored methods to reduce LLM hallucination to improve correctness?
* It would good to have a reference for the compution time for different methods

### Questions
It would be interesting to see how the complexity of the node setup (number of shader nodes, edges, etc) correlate with the quality of the results and program correctness

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackle the problem of procedural material generation with LLM. The authors first generate Python code conditioned on the input image with LLM, then execute the code in Blender, which can match the input image exactly. This method also facilitates the downstream editing and manual creation.

### Strengths
+ This paper proposes a straightforward pipeline for procedural material generation. It trains a domain-specific Vision-Language Model (VLM) through meticulous data collection, processing, and fine-tuning, followed by effective post-processing techniques to address the problem.
+ Both data augmentation and MCMC-based post-processing are validated through qualitative and quantitative results. 
+ Using VLM to tackle graphics problems is a promising and intriguing area for exploration, with potential applications across a wide range of domains. 
+ The results appear robust, surpassing all baselines, including MatFormer and LLM-based approaches, in both quantitative and qualitative evaluations.

### Weaknesses
 + Adapting VLM as a tool for material code generation may not be entirely reasonable, as LLaVa primarily addresses natural images rather than focusing on code generation. It is important for the network design to account for these biases.

+ Additionally, could you provide a detailed user study for artist? Is it possible for this AI tool to substitute certain steps in the artistic creation process?

### Questions
+ The paper addresses the challenge of limited material data (~2k) in fine-tuning LLMs through data augmentation. The first question is: what specific techniques were employed in the data augmentation process? Could you summarize these techniques and provide a clearer description?

+ Additionally, the reviewer believes it is quite meaningful to apply LLMs (VLMs) to a broader range of applications, particularly in domains with limited data. Could you provide more evidence regarding the **training/val process** about role of data augmentation?

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
The paper presents a novel approach to procedural material generation from input images using a large, fine-tuned vision-language model (VLM). This method transforms material generation into a text-to-program problem, converting material graphs to Python code for Blender's API. The paper introduces an open-source procedural material dataset and proposes a two-tier data augmentation strategy to enhance training, achieving a substantial improvement in program accuracy and visual quality over existing methods.

Several contributions:
1. VLM Fine-Tuning for Procedural Materials: The authors fine-tune a VLM to generate procedural material node graphs in Python code format based on input images, addressing the limitation that existing VLMs lack training data specific to procedural materials.

2. Open-Source Dataset for Procedural Materials: The authors compile an open-source dataset of 550,000 procedural material samples for training and evaluation, combining real artist-created Blender materials with augmented data.

3. Post-Optimization Algorithm: A gradient-free, Markov Chain Monte Carlo (MCMC) approach refines the generated material node graphs to better match the visual appearance of the input image.

### Strengths
1. Recasting procedural material generation as a vision-language task, effectively combining visual perception with the generation of structured, editable material programs.
2. Fine-tuning a VLM specifically for procedural material generation, a domain that was previously not widely explored in the vision-language field.
3. Introducing a dataset of 550,000 procedural material samples, which includes not only real-world data but also creatively synthesized samples generated via program-level and parameter-level augmentations. This contribution provides a foundational dataset for further research in this area.
4. Evaluation on both synthetic and real-world images shows that VLMaterial outperforms baselines like BlenderAlchemy and Conditional MatFormer in metrics such as style loss, SWD, and program correctness, demonstrating improvements in visual fidelity and program accuracy.

### Weaknesses
1. Limited Novelty in Augmentation Techniques: While the paper presents a large dataset with program-level and parameter-level augmentation, the augmentation techniques themselves rely on GPT-based models and parameter variations, which may not fully capture the variety found in real-world material designs. Specifically, the program-level augmentations, while generating new graph structures, might not introduce fundamentally different material properties or visual characteristics beyond what can be achieved through simpler parameter adjustments. This reliance on LLMs for graph generation could lead to a bias towards structures that are easily generated by these models, potentially limiting the diversity of the dataset and the generalizability of the trained model.
2. Despite its strong performance, the model struggles with highly intricate textures, where certain details are either lost or inaccurately represented, as shown in Figure 7. Furthermore, in Table 3, this method underperforms compared to other approaches on out-of-distribution datasets (Substance and real images) when operating under a more constrained sample budget. This limitation may affect its applicability in scenarios that demand high precision. The underperformance on out-of-distribution data, particularly with limited samples, suggests a potential overfitting to the training distribution or a lack of robustness in the learned representations. The model's inability to capture intricate details also points to a limitation in its capacity to handle high-frequency information present in complex textures.
3. The paper’s evaluation relies heavily on quantitative metrics and in-distribution and out-of-distribution tests. However, given the subjective and artistic nature of material design, the paper would benefit from user studies or feedback from professional material artists. Expert insights could help assess aspects like the usability, editability, and practical value of the generated materials in real production workflows. The current evaluation does not adequately address the practical utility of the generated materials from a user perspective, focusing primarily on visual similarity and program correctness.

### Questions
Question 1: In Figure 7, it seems the model has difficulty reproducing certain intricate textures. Are there particular features (e.g., high-frequency details, irregular patterns) that consistently pose challenges? Could you expand on why these features are difficult to capture with your model? It may help to provide an analysis of failure cases or challenging texture types, as well as insights into potential model improvements or data augmentation strategies to better handle intricate textures. This could guide future work and inspire researchers to address these limitations.

Question 2: In Table 3, your model underperforms on out-of-distribution datasets (Substance and real images) with a limited sample budget. Could you elaborate on how the model’s architecture or training process might contribute to this limitation? It might be helpful to explore or discuss possible adjustments, such as adaptive fine-tuning or feature-specific augmentations, to improve generalization on out-of-distribution data under constrained conditions. Additionally, explaining the trade-offs involved in this limitation and suggesting potential remedies would provide a more comprehensive understanding of the model’s practical applicability.

### Soundness
3

### Presentation
3

### Contribution
3
