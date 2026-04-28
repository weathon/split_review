# On the Cycle Consistency of Image-Text Mappings

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 3, 3, 5

## Abstract
The increasing exchange of image and text in large multimodal models leads us to ask: to what degree are mappings from text to image, and back, cycle-consistent? First, we find that current image-to-text models paired with text-to-image models do achieve a degree of perceptual cycle consistency, even when these models are not trained to have this effect. However, these mappings are far from perfect, motivating us to analyze in what ways they fail. First, we observe a strong correlation between cycle consistency and downstream performance in both image captioning and text-to-image generation. Next, we investigate how divergent are text-to-image mappings as a function of the number of objects described by the text, and how it affects achieving cycle consistency. Surprisingly, we find that more descriptive text leads to a a broader distribution of generated images, but also results in overall better reconstructions. Finally, we show possible challenges of training cycle consistent models due to the sensitivity of text-to-image models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper analyzes the cycle consistency of image-to-text and text-to-image models. The study shows that while current models exhibit a level of cycle consistency, there is room for improvement, especially T2I models are sensitive to slight changes in prompts.

### Strengths
1. The paper focuses on interesting topics about the cycle consistency of by analyzing the cycle consistency of T2I and I2T models.
2. It provides a comprehensive analysis of cycle consistency in image-to-text and text-to-image mappings, highlighting the correlation between cycle consistency and downstream performance in tasks such as image captioning and text-to-image generation.

### Weaknesses
1. Although the paper presents that T2I models are more sensitive to small changes in input prompts, it lacks an in-depth analysis of why different combinations of T2I and I2T models yield varying performance. For example, how does the training dataset affect the cycle consistency? How does the pre-trained model in T2I or I2T affect the cycle consistency?
2. The paper does not sufficiently analyze why specific combinations of I2T and T2I models perform differently in terms of image and text cycle consistency. For example, BLIP2 underperforms compared to LLaVA1.6 in image cycle consistency while surpassing it in text cycle consistency.
3. The analysis in the paper highlights that text-to-image models are highly sensitive to slight changes in prompt structure (word choice, order, and length), which can lead to inconsistencies. However, the paper stops short of proposing concrete solutions or mitigation strategies for this issue.
4. The evaluation conducted solely on 1k MS COCO data is limited, especially since MS COCO captions often lack detailed descriptions of the images

### Questions
1. Recent research shows the hallucination problems in Multimodal LLM and compositional problems in T2I. How can the proposed method avoid this issue? For example, an input prompt could result in the generation of an incorrect image, which might then lead to an MLLM producing captions that are incorrect but resemble the original prompt. In this case, the cycle consistency might be high, but the actual performance should be low.
2. What is the cycle consistency on long captions?

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
3

### Summary
This paper analyzes the cycle consistency of current image/text generative models, which represents how well the original input is preserved when it consecutively passes through two generative models. To quantify the cycle consistency of images and text, the authors use metrics that measure perceptual similarity and present results for various combinations of image and text generative models. Using several benchmarks, the authors suggest that cycle consistency alone can imply the performance of models on downstream tasks by showing a high correlation between the two, thereby eliminating the need for creating additional test sets.

### Strengths
- The paper presents various quantitative analysis results on the proposed claim while also visualizing various qualitative results.
- The authors analyze a less explored aspect of generative models and provide insights into its significance.

### Weaknesses
 - There is little analysis on the differences between the models used to measure cycle consistency. The paper simply mentions that recent models perform better, without analyzing whether the differences stem from their training data, objective functions, specific architectures, etc. Authors could have provided a table summarizing these differences and discussed how these factors may contribute to the observed performance differences in cycle consistency.
- In sections 4 and 5, it is unclear what message the authors are trying to convey. It is ambiguous how these sections relate to the cycle consistency discussed in sections 2 and 3. Authors could have better linked these sections to the overall narrative, such as explicitly stating how the divergence in text-to-image mappings (Section 4) and sensitivity in image-to-text mappings (Section 5) impact or relate to cycle consistency.

### Questions
- When calculating cycle consistency for each modality, one of two generative models is fixed. (SDXL Turbo for image cycle consistency / LLaVA 1.5-13b for text cycle consistency) Would results show the same trend if the fixed models were changed?
- If richer and more detailed data improves cycle consistency, can we say that recent models show better performance because they use quality data? It could lead to valuable insights if authors examined the training data characteristics of the better-performing models to see if there's a correlation with data quality, and discussed how this relates to cycle consistency performance.

### Soundness
2

### Presentation
2

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
This paper presents several intriguing phenomena regarding the cycle consistency of image-text mappings with text-to-image models and image-to-text ones. It demonstrates (1) that more advanced models achieve better cycle consistency; (2) a strong correlation between cycle consistency and tasks such as image captioning and text-to-image generation; (3) that the number of objects described by the text affects text-to-image mappings; and (4) that text-to-image models are sensitive to prompt variations.

### Strengths
- The paper is well presented and easy to read.
- The paper demonstrates extensive experiments incorporating multiple combinations of T2I and I2T models.

### Weaknesses
Major issues:
- Regarding Table 1 and 2, the analysis of why image-to-text models have greater impact than text-to-image models is hand-wavy. There should be more discussion on this. Specifically, the paper lacks a detailed analysis of the architectural differences between the models that might lead to this discrepancy. For instance, are the vision encoders in the image-to-text models inherently better at preserving information during the encoding process, or is it related to the language model's ability to generate more consistent text? The paper needs to explore these factors more rigorously.
- Causality Direction: While the paper demonstrates correlation between cycle consistency and model performance (captioning/generation), it fails to address the causality direction. The improved cycle consistency is likely a consequence of better model capabilities rather than a contributing factor, which diminishes the practical utility of cycle consistency as a metric. The paper does not provide any evidence that improving cycle consistency directly leads to better performance in downstream tasks. It's crucial to investigate whether cycle consistency is a cause or an effect of model improvement.
- The claim that "more descriptive text leads to a a broader distribution of generated images" is not convincing. The experiments does not properly control the caption length. Figure 6 shows a case where the 1-tag caption exceeds the 5-tag caption in length. This makes it difficult to isolate the effect of descriptiveness from the effect of caption length. The experiment needs to be redesigned to control for caption length and focus on the information density of the text.
- The abstract makes several claims that aren't supported by the paper's content:
  - "analyze in what ways they (cycle consistency) fail": there are no such discussions in the paper. The paper lacks a detailed error analysis of the cycle consistency failures. It should include specific examples of failure modes and discuss the underlying reasons for these failures.
  - "how it affects achieving cycle consistency": there are no such discussions in the paper. The paper does not explore how different factors, such as model architecture or training data, affect the ability to achieve cycle consistency. This is a crucial aspect that needs to be addressed.
  - "we show possible challenges of training cycle consistent models due to the sensitivity of text-to-image models": there are no explorations of training cycle-consistent models in the paper. The paper does not provide any insights into the challenges of training models to be cycle-consistent. This claim is not supported by any experimental evidence.

Minor issues:
- "more descriptive text leads to a a broader distribution of generated images" has double "a".
- On the 4th line in page 4, the sentence "Therefore, examine how a text-to-image mapping can diverge from one fixed text prompt into many different images." is incomplete.
- At the end of page 8, "Table 5" should be "Table 6".

### Questions
- Is image-text cycle consistency a meaningful metric for model development? Should improving cycle consistency be a priority for model designers? What are the concrete applications or benefits of enhanced cycle consistency?

### Soundness
2

### Presentation
3

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
In this work, the authors explored about the multi-modal cycle consistency of current text-to-image(T2I) and image-to-text(I2T) generation models. 

They paired various off-the-shelf T2I and I2T models to build a cycle model and measured the input-output difference.  They found that current state-of-the-art models possess a certain level of perceptual cycle consistency, even when they're not explicitly trained with cycle consistency objectives.
Then, they argued that as the performance of the individual T2I/I2T module increases, the cycle consistency improves.

To further analyze and find possible factors that can affect to achievement of cycle consistency, the authors suggested the concept of 'divergence' in T2I mappings. And they claimed that more detailed and informed text prompts showed more divergent output space, yet improved cycle consistency.
Finally, the authors demonstrated that a slight perturbation of text input sometimes results in higher variation in the T2I model output, which could be a challenge to achieve better cycle consistency.

### Strengths
-Considering the current generative models become more challenging to inject cycle consistency because of their iterative sampling process, their behavior on cycle consistency is an interesting question.

-The script is well-written and clearly presents its claim.

### Weaknesses
 -Some experiments are not well-designed, which makes the corresponding findings seem to lack contributions or doubtful.

1. Section 3 stated to demonstrate "more cycle-consistent models have better T2I/I2T downstream performance",  but its content only shows that "better T2I/I2T models are more cycle-consistent", which are not the same.
It seems too natural that combining better T2I&I2T models improves cycle-consistency of the pair, since they provide high-quality data that contains major information of the input. On the other hand, it's still questionable that satisfying cycle consistency guarantees better T2I&I2T performance.
(e.g. A perfect Image->Text->Image reconstruction can be achieved if the I2T model writes down all pixel values in one long string. A perfect Text->Image->Text reconstruction can be achieved if the T2I model produces the image that contains the entire input text visually.)

2. In Figure 6, synthesized input captions with fewer tags don't seem to actually contain less information. In the first row, the input caption for 1 Tag is very long and specific, more detailed than 2~5 Tag captions. In the second row, the 1 Tag caption already contains the info of the second tag "reflects". This could be the reason that the divergence decreased with fewer tags, since better cycle consistency (more tags) coming with more divergence seems counter-intuitive.

### Questions
-In Table 1\~2, the presented values alone are not enough to tell if each I2T+T2I model pair has a good cycle consistency since there's no baseline performance or threshold was suggested. Although the authors showed several cases in Figure 2\~3, could the authors provide any kind of baseline scenario for comparison?

-Since the sampling process image-to-text models can be also stochastic, could you also provide the analysis on the divergence of I2T models?

-What does the analysis of the divergence and sensitivity of I2T models suggest for creating more cycle-consistent models? It would be better if there's a clearer statement about how the results on divergence and sensitivity imply about cycle consistency.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper (Cycle Consistency of Image-Text Mappings) investigates the degree to which the image-text mappings have a cyclical consistency. Although existing models do not train for this consistency explicitly, for a subset of models this cyclic consistency is enforced. In terms of application, the authors find that the measure of cycle-consistency correlates relatively well with downstream accuracy — which can help perform quick tests on the capabilities of the model without requiring a curated benchmark.  Overall, I believe that the paper is insightful, but lacks a strong application using those insights except for an approximate performance check for downstream tasks.

### Strengths
Below I state the strengths and weaknesses of the model: 

Strengths:

- The paper is a thorough empirical study on the cycle-consistency of image-text representations across most of the popular T2I and I2I models. The results though not super surprising (as they are often trained / fine-tuned on the similar training sets) are well documented and can be crucial for the community. 
- The observation regarding the correlation between image-text cyclical consistency and downstream task accuracy can be useful to quickly check the effectiveness of the model.  One question regarding this: In Fig. 4, SDXL-Turbo is used as a decoder for the image reconstruction case and LLaVa-1.5-13B for text generation. How does this design choice affect the correlation between cycle consistency and downstream performance? The authors should ideally provide some ablation on this design choice.

### Weaknesses
Weaknesses:
- The application of using cycle-consistency as an approximate measure for downstream task accuracy is an interesting use-case; However, I believe they are proxy for only two tasks (Image captioning and T2I generation performance). To be useful in practice, I suggest the authors to add in more tasks concerning these models (e.g., VQA amongst others) and check if cycle-consistency can still be an approximate measure of task accuracy. 
- I find the Sec.(5) to be intriguing, but the authors should highlight how some of the takeaways be used towards training / fine-tuning models with better downstream capabilities. 
- The authors select CIDEr score for captioning performance measurement; Have the authors considered using a strong MLLM for measuring captioning performance and using it to measure the correlation with?
- (This is not a weakness - but a discussion point) — Based on the insights, what do the authors think about building unified image-to-text and text-to-image models while enforcing cyclical consistency? Will it lead to better downstream performance than training these models independently.

### Questions
Overall, this paper is a nice empirical study on cyclical consistency of image-text mappings, but I would urge the authors to respond to the Weaknesses during the rebuttal. I am open to improving the score based on the rebuttal discussion. Looking forward to the discussion. 

See Weaknesses for additional questions.

### Soundness
3

### Presentation
2

### Contribution
2
