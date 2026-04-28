# Bidirectional Generative Retrieval with Multi-Modal LLMs for Text-Video Retrieval

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 8, 5, 3, 3

## Abstract
In recent years, multi-modal large language models (MLLMs) have shown outstanding advancement in various multi-modal understanding tasks by leveraging the powerful knowledge of large language models (LLMs). Extending MLLMs to text-video retrieval enables handling more complex queries with multiple modalities beyond simple uni-modal queries for traditional search engines. It also provides a new opportunity to incorporate search into a unified conversational system, but MLLM-based text-video retrieval has been less explored in the literature. To this end, we investigate MLLMs' capabilities in text-video retrieval as a generation task, namely, generative retrieval, in two directions. An intuitive direction is $\textit{content generation}$ that directly generates the content given a query. Another direction is $\textit{query generation}$, which generates the query given the content. Interestingly, we observe that in both text-to-video and video-to-text retrieval tasks, query-generation less suffers from the bias and significantly outperforms content-generation. In this paper, we propose a novel framework, Bidirectional Text-Video Generative Retrieval (BGR), that handles both text-to-video and video-to-text retrieval tasks by measuring the relevance using two generation directions. Our framework trains MLLMs by simultaneously optimizing two objectives, $\textit{i.e.}$, video-grounded text generation (VTG) and text-grounded video feature generation (TVG). At inference, our framework ensembles predictions by both generation directions. We also introduce a Prior Normalization, a simple plug-and-play module, to further alleviate the $\textit{prior bias}$ induced by the likelihood of uni-modal content data that often overwhelms the relevance between query and content. Our extensive experiments on multi-modal benchmarks demonstrate that BGR and Prior Normalization are effective in alleviating the prior bias, especially the text prior bias from LLMs' pretrained knowledge in MLLMs, achieving state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework, Bidirectional Text-Video Generative Retrieval (BGR), to address the challenge of text-video retrieval using MLLMs. BGR leverages two generation directions: text-to-video (VTG) and video-to-text (TVG). By combining the strengths of both directions and employing a Prior Normalization technique, BGR mitigates the bias towards uni-modal content and improves retrieval performance.

### Strengths
1. The proposed method is straightforward and intuitive.
2. The paper is easy to follow.
3. Some empirical results are strong.

### Weaknesses
1. The overall contribution is rather limited. The key idea of adding content generation loss is implemented as contrastive losses, which are not fundamentally different from widely-used formulations in video language modeling. The reviewer would expect further exploration on how content generation is uniquely modeled if the main claim is on formulating retrieval as a generative task.

2. More in-depth analysis are needed in the prior normalization technique. It is still unclear why this is needed mathematically. From the current manuscript, it is not well analyzed and explained why it is necessary.

3. It is important to understand how the proposed decoding process affects the inference speed.

### Questions
Please check weakness for details.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses text-video retrieval using Multi-Modal Large Language Models (MLLMs), focusing on mitigating prior biases such as text bias in video-to-text (V2T) and video bias in text-to-video (T2V). The key contribution is a Bidirectional Generative Retrieval (BGR) framework that integrates content generation (e.g., generating text from video) and query generation (e.g., generating video features from text) within a unified training framework. This bidirectional approach inherently addresses modality-specific biases by leveraging complementary strengths of both directions.

The authors introduce Prior Normalization as a core component to further balance contributions from text and video, enhancing robustness and retrieval accuracy. The framework achieves state-of-the-art results on standard benchmarks (e.g., DiDeMo, ActivityNet, MSRVTT), significantly outperforming contrastive and hybrid methods. By combining bidirectional generation with effective bias mitigation, the paper presents a novel and impactful paradigm for multi-modal retrieval.

### Strengths
1. **Innovative Framework**: The integration of content and query generation into a single bidirectional retrieval framework is novel and effective.
2. **Bias Mitigation**: The use of Prior Normalization directly addresses modality-specific biases, improving robustness and accuracy.
3. **State-of-the-Art Results**: The method achieves strong performance across multiple benchmarks, demonstrating its practical effectiveness.

### Weaknesses
1. **Low Coverage in V2T**: Generated text queries may oversimplify video content, reducing detail and diversity in retrieval results. This simplification could lead to a loss of nuanced information present in the video, effectively making the retrieval process less sensitive to subtle differences between videos. The generated text might focus on the most salient actions or objects, neglecting other relevant aspects that could be crucial for a more comprehensive retrieval.
2. **Superficial Signals in T2V**: The approach may overfit to visually striking but semantically irrelevant features in videos. This could manifest as the model prioritizing visually prominent elements (e.g., bright colors, rapid motion) over the actual semantic content of the video, leading to retrieval results that are visually similar but semantically mismatched. The model might latch onto superficial visual patterns that are not indicative of the video's true meaning.
3. **Limited Discussion of Trade-Offs**: The paper does not analyze the computational complexity or scalability of the bidirectional inference framework. Not critical but should cover. Specifically, the paper lacks a detailed analysis of the memory and time requirements for both training and inference, especially when dealing with large-scale datasets. This is important for practical applications.
4. **Omitted Baseline Comparisons**: The evaluation misses DiffusionRet (ICCV 2023) and GLSCL (CVPR 2023), which are relevant recent works but likely not critical given the strong baselines included.

### Questions
I generally liked the idea of combining bidirectional generative retrieval with prior normalization—it reminds me of cycle training, though your method doesn’t fully address the problem of ensuring mutual semantic consistency across directions.

I'd like the authors to address a more philosophical question: the information content in videos and queries are vastly different, in terms of diversity, richness etc. i.e. a picture is worth a thousand words and videos (saving for academic talks) will have much more. It wont' be a good idea if we cannot identify "man walking" if that is indeed what the user is asking, instead of some specific aspects. This asymmetric problem exists in both direction, but with different aspects. Trained in this framework, we might "overfit" to the queries in the training data.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the Bidirectional Text-Video Generative Retrieval (BGR) framework to enhance text-video retrieval tasks by mitigating prior biases in MLLMs through a dual-generation approach (VTG and TVG) and a plug-and-play Prior Normalization module. Extensive experiments on benchmark datasets demonstrate that BGR significantly outperforms traditional methods, showcasing improved performance in text-to-video and video-to-text retrieval.

### Strengths
1. Authors provide a baseline model using MLLM.
2. Authors provide solutions for generative retrieval by text video feature generation and video text generation.
3. Authors present a solution for reducing the bias in MLLM.

### Weaknesses
1. Lack of discussion and comparison on image-text generative retrieval. For example, comparing with them showing some special design for video (as this is the only difference between video/image text generative retrieval.)
3. Writing is not clear. 
	1. Lack of explanation of lots of mathematical  formulations. For example, what is v_1, v_2, t_1, t_2 in Figure 3? What is the difference between them and tilde{t}^1 and tilde{t}^2 . The introduction of these mathematical notations should be before Figure 2.
	2. In figure 3, how to get t_2, t_3, v_2, v_3 from tilde t _ 1. v_1?
	3. The definition of P(t) in Line 187 is not clear. How to calculate that?
	4. The details of several models should be put in the main paper not the appendix.


### Questions
First see weakness.
Q1: So in 3.1, the MMLM baseline is a single tower model? The complexity during training and inferences is O(mn) assuming m is the number of video and n is number of text? This is way higher that dual tower model.
Q2: How to calculate P(t) in Eq. 10?

### Soundness
3

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
The authors propose a method that addresses the challenge of text-video retrieval using multi-modal large language models. The proposed method leverages the generative capabilities of MLLMs in two directions: content generation (generating the content given a query) and query generation (generating the query given the content). The authors also introduce a simple plug-and-play module called Prior Normalization, which is a training-free score calibration method to further reduce the prior bias at retrieval inference.

### Strengths
* The proposed BGR framework, when combined with Prior Normalization, outperforms existing methods on text-video retrieval tasks across various benchmark datasets.
* The idea of using multi-modal large language models for text-video retrieval is interesting.

### Weaknesses
 * The writing of this paper needs significant improvement:

  * First, this paper defines cross-modal similarity as a conditional probability but does not clearly explain how to calculate it. Is the conditional probability $P_{vtg}(t|v)$ a combination of the LLM's output probabilities for each token, just the probability of the last token, or is it based on the cosine similarity of the LLM output tokens? Similarly, how is $P_{tvg}(v|t)$ calculated? The paper should provide a clear mathematical definition of how these probabilities are derived from the model's outputs.
  * Second, the paper uses many similar abbreviations, like vtg and tvg, which make it hard to follow. It would be beneficial to provide a table of abbreviations and their meanings.
  * Third, the explanation of the hyper-parameter settings is unclear. For example, $\alpha$ is a key parameter in Prior Normalization that affects the model’s performance, but it’s not clear how its value is chosen. Is $\alpha$ a fixed value, or is it adjusted for each dataset? A more detailed explanation of the hyperparameter tuning process is needed.

* The proposed method isn’t specific to video, so it’s not ideal to limit experiments to only text-video retrieval. Adding text-image retrieval tests would better verify its effectiveness. Specifically, evaluating the method on datasets like Flickr30k and COCO would provide a more comprehensive understanding of its capabilities.
* There are some typos in the equations, like missing "( )" in Eq. 1. I strongly recommend checking each equation carefully.
* The proposed method requires traversing all candidate videos to calculate the conditional probability, and Prior Normalization also needs to process each candidate video. This approach is computationally intensive for multi-modal large language models. The paper should provide a detailed analysis of the computational complexity and inference time of the proposed method.
* The proposed method uses significantly more parameters and pre-training data than the other methods in Tab. 3. To ensure a fair comparison, I suggest using the same vision encoder (such as BLIP 2 and UMT) as VideoChat2 for the other methods in Tab. 3. This would help to isolate the performance gains due to the proposed BGR framework and Prior Normalization.

### Questions
* How is the value of $\alpha$ chosen?
* What is the inference time for the proposed method on ActivityNet?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
We investigated the ability of MLLMs to approach text-video retrieval as a generation task from two perspectives: 
1. Content Generation: Generating content directly from a given query； 
2. Query Generation: Generating a query from provided content；
We observed that in T2V and V2T tasks, using query generation outperformed content generation, showing better performance and reduced bias. Our framework optimizes from both perspectives: generating VTG (video-to-text generation) for a given video and generating TVG (text-to-video generation) from a given text’s video features. We also integrated a plug-and-play Prior Normalization module to mitigate biases within unimodal data."

### Strengths
1. This work provides a comprehensive background on the video-text retrieval task and includes a detailed summary of relevant datasets and evaluation benchmarks for this task in the supplementary materials.

2. The author first applies Prior Normalized Decoding to multimodal scene understanding tasks, offering a solid mathematical foundation and notable improvements in generalization performance.

3. Centered on Prior Normalization, the authors provide extensive ablation studies to substantiate the effectiveness of the module.

### Weaknesses
1. The authors' writing logic presents certain issues. I recommend restructuring the entire paper with Prior Normalization as the central focus. From an overall readability perspective, the connection between Prior Normalization and Generative Retrieval appears weak, suggesting that Prior Normalization functions more effectively as a plug-and-play multimodal optimization tool.

2. The authors' definition of the query-generation task is quite confusing. The primary goal of a retrieval task is to retrieve unknown content based on a given query. However, does query-generation entail generating a query in reverse from the content? This approach does not align with the fundamental objective of retrieval tasks.

3. Figure~1 needs modification. Figure 1(a) Text-video retrieval should depict a representation learning model performing matches within the database. Figure 1(c) is also overly confusingly illustrated.

### Questions
Why does the simple regularization of Prior Normalization yield performance improvements? The authors need to include relevant references and mathematical analysis on Prior Normalization. I believe this concept is not the authors' original discovery, as it has likely appeared in other fields previously[1].

[1]. Prior normalization for certified likelihood-informed subspace detection of Bayesian inverse problems

### Soundness
3

### Presentation
2

### Contribution
2
