# Sketch2Diagram: Generating Vector Diagrams from Hand-Drawn Sketches

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
We address the challenge of automatically generating high-quality vector diagrams from hand-drawn sketches. 
Vector diagrams are essential for communicating complex ideas across various fields, offering flexibility and scalability. 
While recent research has progressed in generating diagrams from text descriptions, converting hand-drawn sketches into vector diagrams remains largely unexplored, primarily due to the lack of suitable datasets. 
To address this, we introduce SketikZ, a dataset containing 3,231 pairs of hand-drawn sketches, reference diagrams, and corresponding TikZ codes. 
Our evaluations highlight current limitations of state-of-the-art vision and language models (VLMs), establishing SketikZ as a key benchmark for future research in sketch-to-diagram conversion.
Along with SketikZ, we present ImgTikZ, an image-to-TikZ model that integrates a 6.7B parameter code-specialized open-source large language model (LLM) with a pre-trained vision encoder. 
Despite its modest size, ImgTikZ demonstrates performance comparable to more extensive models such as GPT-4o.
The model's success is largely driven by using our two data augmentation techniques and a multi-candidate inference strategy,
significantly improving its performance.
These findings provide promising avenues for future research in sketch-to-diagram conversion and may have broader implications for image-to-code generation tasks. SketikZ is publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a system for generating high-quality vector diagrams from hand-drawn sketches based on the new SKETIkZ dataset. SKETIkZ has pairs of hand-drawn sketches and TikZ codes. The system uses data augmentation and a multi-candidate inference strategy to significantly improve output quality.

### Strengths
- This paper proposes a novel important dataset. SKETIkZ fills a critical gap in publicly available data for sketch-to-diagram conversion, supporting future research.
- IMGTIkZ shows comparable performance to larger models like GPT-4o, highlighting efficient architecture and training strategies.
- Data augmentation and multi-candidate inference enhances performance.
- This paper contributes SKETIkZ for evaluating vision-language models' capabilities in diagram generation from sketches.
- Human evaluation is adopted to evaluate the generation results.

### Weaknesses
 - No attempt was made to train with other open-source multimodal large models.
- No performance comparison was made with other open-source multimodal large models.
- Other input should be considered, such as a hand-drawn diagram with corresponding descriptions, where descriptions can be generated using a captioning model.

### Questions
Would it be better to add text descriptions as input along with the hand-drawn diagram for image input?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper generates TikZ code and render them as images from input hand-drawn sketch and a textual prompt (predefined instruction). The proposed VLM, ImgTikZ, combines three components: an open-source LLM from DeepSeek coder, a vision encoder from SigLIP, a trainable adapter network (i.e., a linear layer) added to a pre-trained SigLIP vision encoder which is trained using contrastive learning, and a LoRA appended to the language model. The resulting method is trained in two-stages: in stage-1, the adapter network weights are updated, whereas, in stage-2, both the adapter and LoRA are updated. Along with the ImgTikZ method, the authors proposed SkeTikZ, a new dataset comprising of 3,231 pairs of hand-drawn sketches and corresponding TikZ codes. The authors further augment this dataset such as synthesising notebook backgrounds, adding Gaussian noise, varying brightness and contrast, and introducing distortion. The proposed method and the impact of the dataset is measured using four automatic evaluation: compilation success rate, image similarity, code similarity, and character similarity.

### Strengths
[+] I really want to appreciate the authors for highlighting concurrent works (Belouadi et al, 2024). This is something that should be celebrated more broadly, as it really helps readers understand the overall literature.

[+] The proposed method is simple and intuitive, without unnecessary forced contributions.

[+] The SkeTikZ dataset will hugely help the community in <query>-to-technical diagram generation.

### Weaknesses
[-] While the proposed method is simple and clear, the paper, however, is difficult to follow. For example, when describing "model structure" in Sec.4.1 or in "Datasets used in stage 1 training" the authors could describe the simple adapter network. I could not find the architecture of this linear layer until I went to Page-15 in supplementary. The same is for LoRA, where the authors have to wait till Page-15 in Tab.7 to know lora_r and lora_alpha. If space is the limitation, the authors could add the following in Sec.4.1 -- "for more details on <xxx> architecture/designs, please refer to Tab.7".

[-] The dataset creation process has a caveat: images are rendered using pdflatex, after which a human annotator draws a sketch based on the rendered image. However, human sketching is inherently a lossy process, meaning that certain details may be ommitted or subtly altered. Consequently, when a VLM uses this dataset to perform sketch-to-image generation, there is a high risk of hallucination where the model might introduce small details into the generated image that were not present in the original sketch. Hallucinations may not always be a bad thing, but for generating code or technical diagrams, this can be detrimental.

[-] How is the proposed method different from Gervais et al., 2024 and others, which generate LaTeX code from screenshots of mathematical formulas or handwritten images? Can they be applied to this same problem with minimal modifications?

Minor: 

[-] Typo I presume? re: CSR_ave in Tab.2 whereas CSR_avg in Tab.3

[-] All the tables look too big and consumes a lot of unnecessary space. I would suggest the authors to make the table font smaller and use the space to add details on adapter network, LoRA, and some training details.

### Questions
See weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work investigates the problem of sketch-to-diagram generation, which converts hand-drawn sketches into diagrams formatted as TikZ codes. As drawing sketches is a visual tool that is more intuitive and user-friendly for ideation, the authors think tackling the problem of sketch-to-diagram generation is meaningful but underexplored so far, compared to its text-to-diagram generation counterpart. The authors proposed using a vision language model to handle the interesting problem. A new dataset of paired sketch images, TikZ codes and reference images is also proposed.

### Strengths
- The proposed dataset contains 3,231 sketch images associated with the TikZ codes, and the rendered images are valuable for sketch-to-diagram generation.
- It is interesting and reasonable that a vision language model is utilised to tackle the problem of sketch-to-diagram generation. This work expands the usage of VLM into a new domain.
- Extensive experiments are conducted, which is helpful in understanding the effectiveness and the limitations of the proposed method and other VLM models in the context of image-to-TikZ generation.

### Weaknesses
 - The authors claim that the task of sketch-to-diagram has not been explored before. However, there are some existing works [a][b][c][d]. It would be nice if the authors discuss how this work differs from or improves upon these existing works, particularly in the context of TikZ code generation from sketches. This would help clarify the novelty and contributions of this work.
- The authors could further improve the dataset section. For example, the authors could demonstrate all the types of diagrams this work focuses on and provide statistics about the data (e.g., how many for each category, etc).
- The contribution of using data augmentation and multi-candidate inference tricks is minor.

### Questions
- Could the authors provide a detailed analysis of why the proposed method requires generating multiple candidates for the TikZ code and selecting the best one? Does this stem from the limitation of the vision encoder or the LLM-based code generator?
- Follow-up question: It seems the output of the CodeLLM is somehow random, i.e., sometimes it works and sometimes not, so it requires generating until a satisfactory result is given (both the iterative and the multi-candidate generation falls in this case). Is there any strategy to improve the consistency and accuracy of the code generation process?
- It is confusing to know the difference between CSR_avg and CSR_cum. How could N_gen be different from N_test? The authors might want to provide a concrete example that illustrates how these two metrics are calculated and why they might differ. This could help readers better understand and interpret the results.
- Regarding all the competitors, did all of them fine-tune using the SkeTikZ dataset as well?

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
4

### Summary
This article provides a solution for the task of generating high-quality vector graphics from hand-drawn sketches, a convenient method for conveying complex concepts across various fields. However, the problem of converting hand-drawn sketches to vector graphics remains inadequately addressed due to the lack of datasets. To address this issue, the article constructs a dataset called SKETIkZ, which contains 3,231 pairs of hand-drawn sketches, reference images, and corresponding TikZ code. The authors also commit to making the SKETIkZ dataset fully publicly available. Leveraging the SKETIkZ dataset, the article proposes a modest-sized method called IMGTIkZ that can compete with the performance of GPT-4o.

### Strengths
1. This article is written in a clear and concise manner, introducing the proposed method very clearly and discussing in detail some issues of concern to readers in the results section.
2. The article has open-sourced a dataset for converting hand-drawn sketches to vector graphics, contributing usable foundational data for subsequent research on the same task.

### Weaknesses
1. The method proposed in this article for converting hand-drawn sketches to vector graphics relies more on the combination of existing technical solutions and does not introduce particularly innovative technical approaches.
2. This article carries out extensive data augmentation and supplementation when using the SKETIkZ dataset, which raises curiosity about whether the SKETIkZ dataset itself could play a significant role in future research endeavors.

### Questions
1. I find the SKETIkZ dataset contributed by this article to be quite beneficial, which is why I am more concerned about this dataset. Although I have noticed that the article discusses how the use of the SKETIkZ dataset alone can enhance model performance, I am somewhat concerned about whether the SKETIkZ dataset will universally bring performance improvements in future research work.

2. Regarding the vector graphics generated from hand-drawn sketches, if there are minor errors in the output, I wonder if there are any simple methods available for correction.

### Soundness
3

### Presentation
3

### Contribution
3
