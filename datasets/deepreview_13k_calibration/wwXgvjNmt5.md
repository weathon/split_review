# MAC: A Multimodal Benchmark for Understanding and Generating Academic Journal Covers

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
We introduce the Multimodal Academic Cover (MAC) benchmark to address the challenges of Large Multimodal Models (LMMs) in understanding and generating academic journal covers. While LMMs have demonstrated significant progress in creative arts and everyday applications, their capabilities in comprehending complex academic visuals and narratives remain underexplored. MAC comprises
a collection of 5,872 cover images, accompanying cover stories, and associated articles from 40 prominent academic journals, providing a rich dataset for evaluation. We design bidirectional generative tasks—Image2Text and Text2Imag to assess authenticity and creativity in generating cover images and stories. Current LMMs, including DALL·E 3, GPT-4V, Gemini, CogView-3, GLM-4V, LLaVA, LLaMA-adapter, and MiniGPT4, are evaluated on this benchmark. Furthermore, we propose Multimodal Agent Linkage (MAL), a novel method to enhance conceptual comprehension within a long-context window. In-context learning techniques, such as few-shot learning, are also explored to improve the effectiveness of LMMs. All benchmarks, prompts, and codes will be released publicly.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents MAC, a benchmark for journal cover generation and understanding. After constructing the benchmark, the authors conduct extensive experiments with many LMMs like GPT-4V and LLaVA. The authors also propose a new method to improve long-context understanding.

### Strengths
- The proposed benchmark is useful for specific fields like journal and advertisement industry.
- Many popular models are tested, which is good.

### Weaknesses
 - The benchmark only includes 5K images, which is pretty small. Besides, I am not sure how much impact would this benchmark have in a broader aspect. It seems the journal cover is only useful for some specific business.
- It is a task of image generation and understanding with LLMs, so methods that advance both should be discussed such as Emu, GILL, DreamLLM, SEED, and VILA-U.
- I think LMM is not a common expression. I suggest authors to use MLLM instead (multimodal LLM).

### Questions
n/a

### Soundness
3

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
3

### Summary
This paper proposes the Multimodal Academic Cover (MAC) benchmark, a new multimodal evaluation framework to assess the ability of Large Multimodal Models (LMMs) in both understanding and generating academic journal covers. MAC includes two core tasks:
1) Image2Text: Generating cover stories from given journal cover images and articles, assessing how well LMMs understand and articulate the scientific concepts depicted. 2) Text2Image: Generating academic journal cover images from cover stories and articles, which tests the models' capability to visualize complex scientific concepts in a visually compelling and contextually accurate manner. Additionally, the paper introduces Multimodal Agent Linkage (MAL), a technique that combines LLMs (e.g., ChatGPT) with LMMs to improve their performance in handling long-context, academic content. MAL enhances LMMs by leveraging LLMs’ strengths in processing complex scientific texts, translating them into prompts or descriptions that are suitable for image generation.

### Strengths
1. This paper’s structure is clear.
2. This paper is well-written.

### Weaknesses
1. There are too few MLLMS for comparison, and some typical MLLMS are not included, such as Emu2, Flamingo, etc.
2. Research on related work is inadequate. Some other work that included both human-involved and Large Model-involved evaluations is not compared in the related work. 
3. The data set is too small. With only 5872 journal issues covered, it seems likely that the model will be trained on this basis to overfit, and diversity seems difficult to guarantee.
4. The distribution of the data set appears to be very imbalanced. There is also a lack of more detailed analysis. As Table 4 shows, for example, biology has many times the number of issues.

### Questions
Please refer to the weaknesses.

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
This paper propose The Multimodal Academic Cover (MAC) benchmark to evaluate Large Multimodal Models (LMMs) in generating and understanding academic journal covers. MAC uses Image2Text and Text2Image tasks to assess current LMMs. Additionally, it introduces Multimodal Agent Linkage (MAL) to enhance conceptual comprehension within a long-context window.

### Strengths
This paper firstly introduces an benchmark for evaluating the LLM's ability on (1) generating cover for scientific journals and (2) understanding the cover of scientific journals

### Weaknesses
1. Benchmark lacks scalability and practicality. Can MAC extended to other types of covers?
2. Benchmark design details are relatively poor.
3. The proposed method Multimodal Agent Linkage (MAL) lacks innovation.
See questions below.

### Questions
1. I have doubts about the scalability and practicality of the MAC. Although the authors proposed a benchmark for the understanding and generation of scientific journal covers, I did not see the distinction between scientific journals and other types of documents in the context of this article's topic. For example, the generation and understanding of covers by LLMs for magazines, textbooks, etc., are almost identical to those of scientific journals, with no significant differences. From this perspective, why is the theme of the Benchmark limited to scientific journals? Or can MAC be extended to other types of covers?
2. The scoring mechanism of the MAC is too vague and lacks refinement. For instance, in the prompt of the appendix, only a few aspects such as color and relevance are mentioned. A more reasonable approach for LLMs would be to evaluate the model using different fine-grained metrics, then combine these scores using weighting methods to derive a final score.
3. I have concerns regarding the human-expert evaluation. For instance, in the I-T task, the reference stories provided should be highly specialized, requiring strong domain-specific knowledge to understand. The paper does not adequately consider or explain whether the human experts meet this criterion. LLMs might generate stories that contain similar terms and themes but could be logically incorrect or entirely wrong due to hallucination. Has this possibility been considered?
4. Why is the performance of GLM-4V worse than MiniGPT-4 in Table 3?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a benchmark dataset for the evaluation of text-to-image and image-to-text tasks. The dataset consists of close to 6000 cover images of scientific journals. The paper reported human-evaluation results of a number of well-known image-to-text and text-to-image models like DALLE3, GPT-4V, etc on this benchmark dataset.

### Strengths
The main contribution if the benchmark dataset. As far as I know, this is the first benchmark dataset on scientific journal cover image understanding/generation.

### Weaknesses
The main weakness is that the scope of the dataset is too narrow. It is limited to the cover images of three scientific journals (cell, science, nature). Conclusions drawn for the cover images in these journals may not be valid for many academic journals in other science and engineering disciplines.

 Since those journals are all well-known journals. The cover images may have been used by many of the models as training data. It is difficult to come up with new test images which have not been seen by the models.

Another problem is that there is no quantitative measure on what makes a good cover image. Some scientific journals have their cover pages simply listing the titles of all the papers or the titles of a few selected feature articles. Are those cover images considered good or bad?

### Questions
Is there any way to know if a model has already included the benchmark images into their training data?

Given an "imaginary" journal name, and an arbitrary article (with text and diagrams), there are many ways to come up with a "reasonable" cover image. Is there a quantitative way to measure the "quality" of the images?

How can the benchmark dataset be extended to other journals which may not show feature articles in their cover images?

### Soundness
3

### Presentation
3

### Contribution
2
