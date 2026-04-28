# Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
Vision and language model (VLM) decoders are currently the best-performing architectures on multimodal tasks. Next to answers, they are able to produce natural language explanations, either in post-hoc or CoT settings. However, it is not clear to what extent they are using the input vision and text modalities when generating answers or explanations.
In this work, we investigate if VLMs rely on their input modalities differently when they produce explanations as opposed to answers.
We also evaluate the self-consistency of VLM decoders in both post-hoc and CoT explanation settings, by extending existing unimodal tests and measures to VLM decoders. We find that most tested VLMs are less self-consistent than LLMs. Text contributions in all tested VL decoders are more important than image contributions in all examined tasks. However, when comparing explanation generation to answer generation, the contributions of images are significantly stronger for generating explanations compared to answers. This difference is even larger in CoT compared to post-hoc explanations.
Lastly, we provide an up-to-date benchmarking of state-of-the-art VL decoders on the VALSE benchmark, which before was restricted to VL encoders. We find that the tested VL decoders still struggle with most phenomena tested by VALSE

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates how VLMs balance text and image data when generating answers and explanations, evaluating whether their reliance on each modality shifts depending on the task. Additionally, the authors measure the self-consistency of VLMs by comparing answers and explanations generated in both post-hoc and Chain-of-Thought settings. The results show that VLMs are less consistent than LLMs, with visual information playing a more significant role in explanations than in answer generation.

### Strengths
- This paper is well-motivated and shows interesting findings of VLM. I believe that the result is welcome and beneficial to the community.
- The paper is overall well-written.
- The experimental results are extensive, including various datasets (VQA, GQA, Foi1It, MSCOCO, VALSE) in a wide range of tasks.

### Weaknesses
 - The main technical contribution is limited since the proposed method is heavily based on MM-SHAP and CC-SHAP but applies to VL decoders instead of encoders.
- Only evaluated on LLaVA-based models, missing baselines such as CogVLM.

### Questions
- Please refer to the weakness.

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
3

### Summary
This paper conducts a study on how the inputs to an autoregressive vision-language model (VLM) influence the outputs. Mainly the paper compares the influence of textual and visual input tokens on the output answer and explanation, evaluates the faithfulness of explanations using controlled modifications of the input. The paper studies three open-weight models: BakLLaVA, LLaVA-Mistral, and LLaVA-Vicuna. The methods of the analyses are adapted from prior work on interpreting LMs and encoder VLMs. The results show, among other things, that textual inputs influence the answer more than visual inputs, but that the influence of visual inputs increases when looking at influence on generated explanations.

### Strengths
- Interesting findings regarding interpretability of VLM decoders. These are the main qualitative findings: text input is more influential than visual input for answer prediction, visual input is more influential for explanation generation than for answer prediction, the contributions from each modality are different in answer prediction and explanation generation
- Evaluated on 3 models and 3+ datasets

### Weaknesses
 - Methods are essentially the same as those from prior work
- The argument that the edit-based tests do not provide consistent/meaningful results has dubious value given that flaws in these tests have already been exposed in the context of LMs. The paper does not give examples of prior work claiming that these tests are useful for VLMs.
- The paper does not explain how CC-Shap works (page 4) -- how are the values computed?

### Questions
- Lines 357-358 say: "The large difference between overall higher accr and lower acc results suggests that VL decoders rely on linguistic priors to solve VALSE" - isn't this also because acc is a harder metric? How do you tease those two issues apart?
- What do you view as the main takeaway(s) from the edit-based tests?

### Soundness
3

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
2

### Summary
This paper investigates how Vision-Language Models use image and text modalities in generating predictions and explanations. It studies whether VLMs rely more on visual or textual inputs, and also studies to what extent these models are self-consistent when providing explanations. The paper found that generally, LLM is more reliable than VLMs and text contributes more in VL decoders compared to image. And the effect is even larger with CoT explanations included. The paper also provided the first  benchmarking of state-of-the-art VL decoders on the VALSE benchmark.

### Strengths
1. The paper identifies and addresses a gap of previous works. Previous works only studies encoder while this work provides a study of the decoder on their multi-modal degree and the consistency in their self-explanation.
2. The paper found that VLMs use text more than image, and the gap is larger with CoT included.
3. The paper provides an benchmarking of state-of-the-art VL decoders on VALSE, which has previously only focused on encoders.

### Weaknesses
1. The paper primarily uses existing techniques (e.g., MM-SHAP and CC-SHAP) and the main contribution is applying these metrics to VLM decoders. This adaptation is incremental. The application of MM-SHAP and CC-SHAP to the decoder, while novel in its specific context, largely reuses the existing methodology. The core mathematical formulations and computational steps of these methods remain unchanged. The paper does not introduce any modifications or extensions to the algorithms themselves, which limits the methodological contribution.
2. The writing is unclear and needs to be improved. It would be useful to provide more details on the Shapley values and the computation. The paper lacks a clear, step-by-step explanation of how Shapley values are calculated in the context of VLMs. The description of how MM-SHAP and CC-SHAP are adapted for the decoder is not sufficiently detailed, making it difficult to reproduce the results or understand the nuances of the implementation. The paper should include a more thorough explanation of the specific input features used in the Shapley value calculation, and how these features are derived from the image and text modalities.

### Questions
1. The results show that text is more significantly used compared to image for answer generation. Is it possible that this is a result of dataset biases or limitations in the MM-SHAP metric’s rather than image/text contributions?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work aims to answer an important research question - Do VLM-generated responses (and self-explanations) rely more on images or text?"

By extending methods from VL and LLM research, the authors propose MM-SHAP to measure the contribution of individual tokens to model predictions in order to explore the multimodal degree of autoregressive VLM under different tasks. Their findings are quite interesting and inspiring for future VLM works.

### Strengths
- This work aims to explore an important research question that is well-motivated. The three findings presented are all very interesting. 
- The approach is clearly presented and reasonable. 
- Comprehensively experiments and analysis.

### Weaknesses
 - This work claims the scope as “all decoder VLMs,” yet all experiments are based on llava-based models. I agree with the statement in line 108 that these models (e.g. llava, miniGPT-4, blip2, Otter, etc) share similar high-level ideas; however, do their subtle differences in design lead to changes in the results/conclusions?
- The discussion section lacks in-depth analysis and exploration of the root causes of the observation. In particular, each paragraph in Section 4.4 reveals some interesting phenomena (for example, for CoT ability, VLM is clearly worse than that of LLM in self-consistency) but lacks a deeper discussion of the underlying reason. That being said, this is still a good finding paper.

### Questions
As mentioned in the Weaknesses section, do you think/have found your conclusions can be applied to all decoder VLMs?

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
The paper studies the degree to which VLMs use image or text modalities more in different contexts. The paper does a good job in extending established measures like MM-SHAP to decoder models and evaluating self-consistency of decoders in post-hoc and CoT with CC-SHAP. The authors do an extensive evaluation across 12 datasets with multiple answer formats. 

The papers main contribution include:
1) Benchmarks VLMs on VALSE.
2) VL decoders are more text-centric compared to VL encoders.
3) VLMs are less self-consistent than LLMs.

### Strengths
1) Extending proven measures for VL Encoders to Decoders. 
2) Provides robust evidence about how VLMs rely on different modalities unequally, by evaluating extensively across 12 datasets.

### Weaknesses
1) The paper evaluates only on LLaVA based open-source models. Could the authors evaluate on mPLUG-Owl2 or CogVLM or other non-LLaVA based VLMs as it would be ideal to see the approach work on a different architecture and with different pre-training data? [RESOLVED]

### Questions
Please refer to the weakness section to answer questions about the paper.

### Soundness
3

### Presentation
4

### Contribution
4
