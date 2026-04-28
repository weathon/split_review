# Visual Perception in Text Strings

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Understanding visual semantics embedded in consecutive characters is a crucial capability for both large language models (LLMs) and multi-modal large language models (MLLMs). This type of artifact possesses the unique characteristic that identical information can be readily formulated in both texts and images, making them a significant proxy for analyzing modern LLMs' and MLLMs' capabilities in modality-agnostic vision understanding. 
In this work, we select ASCII art as a representative artifact, where the lines and brightness used to depict each concept are rendered by characters, and we frame the problem as an ASCII art recognition task. We benchmark model performance on this task by constructing an evaluation dataset with an elaborate categorization tree and also collect a training set to elicit the models' visual perception ability. Through a comprehensive analysis of dozens of models, results reveal that although humans can achieve nearly 100\% accuracy, the state-of-the-art LLMs and MLLMs lag far behind. 
Models are capable of recognizing concepts depicted in the ASCII arts given only text inputs indicated by over 60\% accuracy for some concepts, 
but most of them achieves merely around 30\% accuracy when averaged across all categories. 
When provided with images as inputs, GPT-4o gets 82.68\%, outperforming the strongest open-source MLLM by 21.95\%. 
Although models favor different kinds of ASCII art depending on the modality provided, none of the MLLMs successfully benefit when both modalities are supplied simultaneously. Moreover, supervised fine-tuning helps improve models' accuracy especially when provided with the image modality, but also highlights the need for better training techniques to enhance the information fusion among modalities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the use of ASCII art as a tool to evaluate the visual perception capabilities of large language models (LLMs) and multimodal large language models (MLLMs). It introduces two datasets, ASCIIEVAL and ASCIITUNE, which contain 3,526 and 11,836 samples respectively, aimed at assessing and fine-tuning these models. The study conducts extensive testing on a variety of LLMs and MLLMs using the ASCIIEVAL dataset, providing detailed analysis and insights into their performance.

### Strengths
1. The paper attempts to use ASCII art to evaluate the visual understanding capabilities of LLMs and MLLMs, offering a new perspective for assessing these models.

2. The authors manually constructed the ASCIIEVAL and ASCIITUNE datasets, containing 3,526 and 11,836 samples respectively, which can be used for evaluating and fine-tuning LLM/MLLM models on ASCII arts understanding.

3. A wide range of different LLMs and MLLMs were tested on ASCIIEVAL, with detailed analysis and discussion of the results provided, contributing to a deeper understanding of model performance.

### Weaknesses
1. My main concern is that ASCII art may not effectively represent modality-agnostic visual perception due to the inherent differences in information representation between text and image modalities.

    In text form, LLMs process token sequences derived from a tokenizer, independent of the visual shapes of ASCII characters. In contrast, as images, semantic information is conveyed through pixel rendering, influenced by factors unrelated to the characters themselves, such as font and size. Specifically, the tokenization process transforms the raw ASCII characters into a sequence of tokens, which are then represented by embeddings. This process loses the direct spatial relationships inherent in the visual representation of the ASCII art. The model then operates on these token embeddings, which are fundamentally different from pixel-based representations.

    As a result, using ASCII art might lead to misleading conclusions about a model's visual perception abilities, as performance can vary significantly between text and image inputs due to the inherent different nature of information representation.

2. Since most real-world images are not represented by ASCII arts, the potential application scenario is also limited.

### Questions
1. How does the tokenization process affect the model's ability to understand visual semantics in ASCII art when processed as text?

2. From the perspective of AGI, why enhancing the model's performance on understanding ASCII arts is important?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study introduces an ASCII art recognition task to assess the visual information perception abilities of multimodal large language models (MLLMs). Using data from various public sources, the authors built two datasets, ASCIITune for training and ASCIIEval for evaluation, following thorough normalization and filtering processes. Evaluation of numerous existing LLM and MLLM models with these datasets revealed that most models struggle with recognizing textual ASCII art. Additionally, it was observed that, for most MLLMs, performance in recognizing rendered ASCII art is significantly better than textual ASCII art. Finally, even after fine-tuning, performance improvements for textual ASCII art were minimal compared to the more substantial gains seen for rendered ASCII art.

### Strengths
Introduction of a new task: ASCII Art Recognition
- Although many image-text paired datasets exist for MLLM training, ensuring that the images and text in these datasets have precisely the same semantics is often challenging. Evaluating the alignment between vision and text modalities in MLLMs requires a strictly controlled setting, traditionally achieved using document data. This is typically done by pairing rendered images with OCR-ed text. However, this approach is quite limited to character recognition tasks. The ASCII art recognition task introduces a more suitable approach for expanding the field of multimodal representation learning.

Data release: ASCIITune (for training) and ASCIIEval (for evaluation)
- This work utilized various public data sources, constructed multiple-choice questions for more straightforward quantitative evaluation, avoided duplication between training and evaluation datasets, and appropriately excluded potentially sensitive categories. I appreciate releasing such carefully selected data and believe it will benefit the community.

Identification of areas where current LLMs and MLLMs have limitations
- One of the crucial implications of this study is that many current LLMs and MLLMs, both commercial and open-source, have difficulty recognizing textual ASCII art. This might be because these models haven’t been exposed to much of this type of data (ASCII art) during pretraining or due to structural limitations within each model. Similar issues have also come up in vision tasks (e.g., challenges with recognizing analog clocks). However, the inability to recognize information that can be fully represented in text is a noteworthy finding.

### Weaknesses
Section 5.1 shows that "current LLMs do not fully understand textual ASCII art." Additionally, Section 5.2 shows that "most MLLMs recognize rendered ASCII art more effectively than textual ASCII art." The lower recognition performance for textual ASCII art seems to stem from LLMs' limitations, as further confirmed in Section 5.3.1. Therefore, it is important to explore why LLMs struggle with the proposed task and consider offering potential solutions. While this study attempts to address this through SFT (supervised fine-tuning), it appears insufficient.

Typical MLLM training generally involves two main stages: (1) a vision-text alignment stage utilizing image-caption data and (2) an instruction tuning stage using image-text QA data. However, representation learning for the text modality itself usually occurs in the LLM's pretraining phase. Therefore, the SFT approach used in this study may not be ideal for enhancing ASCII art recognition in pretrained MLLMs. Additionally, since SFT uses class labels for supervision (e.g., "A: bird"), it may not be suitable in cases where recognition capability is limited, and there may also be insufficient data and training FLOPs.

Here are a few methods worth attempting to address this issue. I believe these efforts and analyses could provide more valuable insights for readers:
1. Further pretraining (M)LLMs on the "textual ASCII art" as a text corpus.
- This step could allow the model to learn patterns specific to textual ASCII art directly.
2. Fine-tuning MLLMs to input rendered ASCII art and output "textual ASCII art" (unfreezing both the vision encoder and LLM).
- This approach may enable the model to learn both image comprehension and the process of generating textual ASCII art.

### Questions
1. In Section 3.2 on Data Filtering, is plain edit distance sufficient? Standard edit distance is known to be sensitive to temporal scaling (e.g., "ABBC" vs. "AAABBBBBBCCC"). It may be worth considering methods like Dynamic Time Warping as well.

2. For Figure 4, does Figure 4(a) operate in text-only mode and Figure 4(b) in image-only mode?

3. ASCIITune is likely to be more diverse and noisier than ASCIIEval. I am curious about its quality. It might be helpful to sample a portion of the data and measure human performance as a quality check.

4. While the character count of textual ASCII art is essential, providing the token length after tokenization could also be valuable. Additionally, I would like to know if the ASCII art data used in experiments respects the context length limitations of each model tested.

### Soundness
2

### Presentation
3

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
The authors propose a novel benchmark to test the ability of multimodal large language models to understand ASCII art. Their experiments show that most multimodal large language models suffer at this task, performing as poorly as random. On the other hand, humans can perform near perfectly at this task. However this changes when we provide an LLM an image of the given ASCII art. The authors benchmark a wide variety of LMMS and report their results.

### Strengths
1. The authors propose a novel problem, the idea of this benchmark is quite new.
2. The benchmark proposed is new and large, giving the community a new limitation of Multimodal Models to discover and analyze.

### Weaknesses
1. I am not entirely convinced by the motivation of the paper, I don't really understand why it impacts security. The authors should be more clear while describing why is this important for MLLMs to learn.
2. I tried pasting some of the ASCII art text as shown in FIG 1, and was not able to reproduce it in python. The closest I could get was with the dog, this gives me some doubts about the evaluation. The other two ASCII art were not reproducible at least when I pasted it in python.
3. Additionally, I feel some art can have multiple interpretations; for example, certain depictions of cats might resemble rats or raccoons. Since this is art, it naturally lends itself to varied perspectives.
4. Missed reference to an important paper: Can Large Language Models Understand Symbolic Graphics Programs?

### Questions
1. It seems like ASCII art is very sensitive to minor character changes, did the authors ablate this? Like a small character being missed can lead to the ASCII art not making any sense.
2. In the human evaluation, were there some images that had multiple interpretations? 
3. Could you improve the motivation and introduction? Currently, it feels a bit confusing, covering many points without clearly explaining why LLMs and MLLMs need this capability. While it's an interesting idea, I’m not fully convinced of its practical significance. This isn’t necessarily a criticism of the paper, but adding clarity would be helpful.

### Soundness
3

### Presentation
2

### Contribution
3
