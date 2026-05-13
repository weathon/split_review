# TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models

- Decision: Accept
- Scores: 5, 6, 8, 6, 8

## Abstract
How humans can effectively and efficiently acquire images has always been a perennial question. A classic solution is *text-to-image retrieval* from an existing database; however, the limited database typically lacks creativity. By contrast, recent breakthroughs in *text-to-image generation* have made it possible to produce attractive and counterfactual visual content, but it faces challenges in synthesizing knowledge-intensive images. In this work, we rethink the relationship between text-to-image generation and retrieval, proposing a *unified* framework for both tasks with one single Large Multimodal Model (LMM). Specifically, we first explore the intrinsic discriminative abilities of LMMs and introduce an efficient generative retrieval method for text-to-image retrieval in a training-free manner. Subsequently, we unify generation and retrieval autoregressively and propose an autonomous decision mechanism to choose the best-matched one between generated and retrieved images as the response to the text prompt. To standardize the evaluation of unified text-to-image generation and retrieval, we construct TIGeR-Bench, a benchmark spanning both creative and knowledge-intensive domains. Extensive experiments on TIGeR-Bench and two retrieval benchmarks, *i.e.*, Flickr30K and MS-COCO, demonstrate the superiority of our proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an approach to address the limitations of current text-to-image generation (T2I-G) and retrieval (T2I-R) systems. Particularly, it propose to unify generation and retrieval auto-regressively, and use a decision making model to decide whether to use generated or retrieved image as the response to a text prompt.

### Strengths
- Unification of Generation and Retrieval: The core contribution of unifying T2I-G and T2I-R within a single framework centered with LMMs. This framework leverages the strengths of both paradigms, mitigating the limitations of relying on either alone for offering visual content per user query. In an ideal world, the users can obtain a factual image generation when its query is centered at knowledge-intensive factual entity, and see a creative image when queried for imaginary scene.

- New benchmark: This paper creates a dedicated benchmark, TIGER-Bench, which accesses image generation in both creative and knowledge-intensive domains, and offers a more comprehensive evaluation platform.

### Weaknesses
- Lots of details related to presentation needs improvement: 

1. Figure  1 is referring to many things that has not be introduced before, it is hard for people to understand forward beam-search & reverse re-ranking at the first glimpse. Many terms are not really explained in caption, or the introduction and people needs to leap to methodology section to really understand the meaning. 

2. Section 3.2 is not very clear to me, I couldn't find a connection one why those three metrics are used, and also why the metric it has to be training-free. Meanwhile, I also think that comparing to those proposed proxy metrics, a more straightforward way is to directly ask the LMM a visual question, i.e. "<image> Is the presented image is aligned with the following caption? <caption>. Answer yes or no.", and then measure the likelihood on yes and no. 

3. Given that the authors also agree that "It is inefficient due to |G| times of forward propagation" for computing the proposed cross-modal similarity, why not considering leveraging a contrastively trained text-to-image similarity function? The forward beam search + reverse re-ranking seems unnecessarily complicated.

- Lack of simple baseline method: It would make a lot sense to compare a simple zero-shot / fine-tuned LMM that makes a decision between whether to use the SDXL's generated image or CLIP model's retrieved image, according to a user's input query. IMO, this method would be very competitive to the proposed approach.

- The core experimental result is based on author's proposed benchmark, which is not very convincing given that it is really hard to judge the quality and validity of this newly introduced benchmark. It appears to me that the authors are being the player and judge at the same time, which is quite tricky to assess the significance of this work. 

- Missing relevant works: 

The following works have discussed how to leverage image retrieval for image generation and should be discussed and cited. 

1. Re-Imagen: Retrieval-Augmented Text-to-Image Generator
2. KITTEN: A Knowledge-Intensive Evaluation of Image Generation on Visual Entities

### Questions
Please see weakness for my questions

--- Post-rebuttal comments:

I improved my scores based on authors' response.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies how to effectively combine the T2I generation and retrieval into a combined framework. For this task, this paper makes two folds of contribution: 1) This paper proposes a new T2I generation and retrieval pipeline, where the generation and retrieval branches run in parallel, followed by a final image ranking/selection process to decide the final output. 2) This paper proposes a benchmark to evaluate the joint T2I generation and retrieval. The benchmark contains half creative and half knowledge based image-text pairs.

### Strengths
- The overall presentation of this paper is good. This paper contains a lot of content which is hard to make the presentation organized and easy to follow. The authors did a good job in my opinion.
- Joint T2I generation and retrieval is a important task. The proposed benchmark set is key to make different methods devoted for the task comparable.
- The experimental results show that the proposed method has good performance than other generation or retrieval-based methods.

### Weaknesses
- In my opinion, the biggest drawback of this paper is that it lacks technical novelty. This work looks more like a prototype of an application than a research paper. All modules used by this paper has been used by previous papers and the combination of them contributes very limited new knowledge or insight. I understand that this work belongs to a type of papers that is more engineer than research. I put this point inside the weakness section but I am open to any discussion about the fit of this paper to iclr with authors, other reviewers, and AC if possible.
- I am confused about the comparison results in Table 2. What is the difference between the SEED-LLaMA vs Ours (SEED-LLaMA)? Does the latter one used both retrieval and generation? If so, this comparison seems to be somewhat unfair. If not, what is the components of the proposed method that lead to the performance improvement over the baseline. More discussion is welcomed.

### Questions
Please see the weakness section

### Soundness
2

### Presentation
3

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
This paper introduces a unified framework for text-to-image generation and retrieval using LMM. It proposes an efficient method leveraging LMMs' discriminative abilities. It also presents an autonomous decision mechanism for selecting between generated and retrieved images. The authors also developed TIGeR-Bench to evaluate generation and retrieval abilities across creative and knowledge-intensive domains simultaneously.

### Strengths
- This paper is well-written and easy to follow. 
- Efficient retrieval and accurate decision-making are crucial in unifying generation and retrieval, balancing creativity and knowledge. The proposed TIGER-One solves these two problems within one LMM is elegant.
- The proposed TIGER-One seems effective and shows superior generation results in experiments.

### Weaknesses
- A  preliminary introduction of beam search is recommended to add.
- The authors indicate that the similarity score is calculated by one of the three proxies. More details and discussion of the proxies chosen in decision-making are recommended. 
- With the help of TIGER-One, the LMM demonstrates improved results (Tab. 2).  It’s interesting to explore the addition of dream images based on knowledge (RAG) as a third option alongside generation and retrieval in future work

### Questions
see the weakness part

### Soundness
4

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
2

### Summary
1. Explore the retrieval capabilities of Large Language Models (LMMs) to enable text-to-image (T2I) generation retrieval.
2. Unify generation and retrieval in an autoregressive manner.
3. Propose an autonomous decision mechanism to select the best-matched image from generated and retrieved images.
4. To standardize the evaluation of unified text-to-image generation and retrieval, we construct TIGeR-Bench, a benchmark spanning both 5. creative and knowledge-intensive domains.
6. Conduct extensive experiments on TIGeR-Bench and two retrieval benchmarks, namely Flickr30K and MS-COCO.

### Strengths
1. Propose a unified framework for text-to-image generation and retrieval.
2. Propose an autonomous decision mechanism to automatically select the most suitable image from the retrieved images.
3. To validate the capability of unified generation and retrieval, introduce a new benchmark, TIGeR-Bench.
4. Extensive experiments on TIGeR-Bench and two retrieval benchmarks, i.e., Flickr30K and MS-COCO, demonstrate the pipeline's capabilities.
5. The article is well-written, with clear and precise explanations.

### Weaknesses
1. The challenges faced by generation models in knowledge-intensive tasks are mentioned, but the proposed approach’s effectiveness in consistently addressing these challenges without hallucination remains unclear. Explicit quantitative analysis on knowledge domains might be helpful.
2. Can TIGeR-ONE adapt to user-specific preferences in the decision-making process, especially in creative tasks? If not, how could this be incorporated to enhance user experience?
3. I noticed the multi-round generation in Figure 7. Could you please explain how this process maintains consistency with the user-provided image?

### Questions
As shown in Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper rethinks the relationship between text-to-image generation and retrieval, presenting a novel and pragmatic task, i.e., TIGeR, to meet the challenging information need of humans in real-world scenarios. The authors identify limitations in traditional retrieval methods, which rely on existing image databases, and in generation approaches that struggle with knowledge-intensive content. Motivated by these limitations, the authors proposed a novel unified framework called TIGeR-ONE that combines both tasks using a single LMM. To endow LMMs with the retrieval abilities, they introduce a training-free generative retrieval method that leverages LMM's discriminative abilities, allowing for efficient text-to-image retrieval. Additionally, an autonomous decision mechanism selects either generated or retrieved images as the most suitable response to a given text prompt. The authors develop TIGeR-Bench, a benchmark covering creative and knowledge-intensive image domains, to standardize evaluation. Their approach demonstrates superior performance on the unified benchmark, text-to-image and chat-to-image retrieval and generation benchmarks.

### Strengths
1.	The authors introduce an innovative task that combines retrieval and generation, addressing a gap in traditional approaches that often consider these processes separately. This integrated task is highly practical, as it reflects real-world information needs where users may require either a retrieved image from a database or a newly generated one, depending on the context.
2.	The authors propose a novel unified framework that unifies text-to-image generation and retrieval within a single LMM, streamlining both tasks into a cohesive process. By using a single LMM, the authors simplify the model architecture, allowing the system to handle both retrieval of existing images and generation of new ones without additional model switching or training steps.
3.	The authors introduce a training-free generative retrieval method that enhances both the effectiveness and efficiency of text-to-image retrieval. The proposed method leverages the pre-existing discriminative abilities of Large Multimodal Models (LMMs) to perform retrieval without the need for extensive training on large datasets. 
4.	They build a unified benchmark, i.e., TIGeR-Bench, to standardize evaluation across creative and knowledge-intensive tasks, serving as a strong foundation to attract more researchers to explore complex multimodal information acquisition.

### Weaknesses
1.	Considering there has been prior work (i.e., GILL) addressing text-to-image retrieval and generation, the difference and advantages of the proposed method over GILL should be further highlighted clearly.  
2.	The paper lacks analysis on how the unified model’s performance varies with prompts that have similar intentions but are expressed differently. In practical use, different users may convey the same idea with varied wording, prompts, and questions. How sensitive is the proposed method to these variations? 
3.	Given that the distribution over creative domains and knowledge domains may not be uniform in real-world scenarios, an analysis of the model’s performance and decision-making behavior under unbalanced distribution conditions would be beneficial.

### Questions
1.	Is there any experiment demonstrating the decision behavior of the proposed model? 
2.	Compared to dense retrieval methods, such as CLIP, what advantages do MLLMs and the proposed generative retrieval framework offer?

The authors have solved my concerns.
I stand by my positive score, after reading other reviewers' comments.

### Soundness
4

### Presentation
3

### Contribution
4
