# Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
While recent Large Vision-Language Models (LVLMs) have shown remarkable performance in multi-modal tasks, they are prone to generating hallucinatory text responses that do not align with the given visual input, which restricts their practical applicability in real-world scenarios. In this work, inspired by the observation that the text-to-image generation process is the inverse of image-conditioned response generation in LVLMs, we explore the potential of leveraging text-to-image generative models to assist in mitigating hallucinations in LVLMs. We discover that generative models can offer valuable self-feedback for mitigating hallucinations at both the response and token levels. Building on this insight, we introduce self-correcting Decoding with Generative Feedback (DeGF), a novel training-free algorithm that incorporates feedback from text-to-image generative models into the decoding process to effectively mitigate hallucinations in LVLMs. Specifically, DeGF generates an image from the initial response produced by LVLMs, which acts as an auxiliary visual reference and provides self-feedback to verify and correct the initial response through complementary or contrastive decoding. Extensive experimental results validate the effectiveness of our approach in mitigating diverse types of hallucinations, consistently surpassing state-of-the-art methods across six benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to mitigate hallucinations in LVLMs by introducing valuable feedback from text-to-image generative models. Then a training-free decoding algorithm is introduced to integrate information from the original images and feedback from text-to-image generative models. Experiments on five benchmarks and two LVLMs demonstrate the effectiveness of the proposed method.

### Strengths
1.	The idea of leveraging text-to-image generative models for LVLM hallucination mitigation is novel and interesting.
2.	The paper is well-written and easy to follow.
3.	Extensive experiments on multiple benchmarks demonstrate the effectiveness of the proposed method.

### Weaknesses
1.	The effectiveness of the proposed method is heavily influenced by the quality and realism of the generated images. So the authors should perform more experiments and analysis on the quality of the generated images (both quantitative and qualitative, especially for long captions and real images).
2.	Since the model relies on an addition diffusion model for inference, additional inference overhead should be discussed.
3.	Experiments are limited to two LVLMs, experiments on more recent LVLMs (e.g., QWenVL, MiniCPMV, etc.) should be conducted.
4.	It’s better to perform experiments on multiple object hallucination [1].
5.	The approach involves various hyperparameters that require careful tuning to achieve optimal performance, which could make practical implementation challenging.

[1] Chen X, Ma Z, Zhang X, et al. Multi-object hallucination in vision-language models[J]. arXiv preprint arXiv:2407.06192, 2024.

### Questions
Please see Weakness.

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
Recent large vision-language models (LVLMs) have demonstrated impressive performance in multi-modal tasks, but they are prone to generating hallucinated text responses that do not align with the given visual input. This work explores the potential of leveraging powerful text-to-image generative models to assist in mitigating these hallucinations. The authors discover that generative models can offer valuable self-feedback for correcting hallucinations at both the response and token levels. Building on this insight, they introduce a novel training-free decoding algorithm called "self-correcting Decoding with Generative Feedback (DeGF)" that incorporates feedback from text-to-image generative models to recursively enhance the accuracy of LVLM responses. Extensive experiments validate the effectiveness of DeGF in reducing diverse types of hallucinations, consistently outperforming state-of-the-art methods across multiple benchmarks.

### Strengths
1. Providing the generative feedback to mitigate hallucinations is straightforward and reasonable. Token-level refinement based on Jensen-Shannon divergence correctly utilize the generative feedback.
2. The proposed Self-Correcting Decoding with Generative Feedback (DeGF) also achieves pleasant results on POPE, CHAIR, MME, etc.
3. This paper is well-written and has clear figures. The experiments are extensive to some extent, and clearly organized.

### Weaknesses
1. The computation costs are unafforable for the LLM decoding strategy. Utilizing generative model like Stable Diffusion to provide generative feedback is unrealistic for practical deployment. Moreover, self-correcting decoding also consumes twice inference costs similar to contrastive decoding.
2. This approach utilizes extra pretrained network (i.e., Stable Diffusion). Baselines should contain methods that also employ extra analysis network like woodpecker [r1, r2], etc. Otherwise, it is unfair for other decoding methods.
[r] Woodpecker:Hallucinationcorrectionformultimodal largelanguage models. arXiv:2310.16045,2023.
[r2] HALC:Object hallucinationreductionviaadaptivefocal-contrastdecoding. In International Conferenceon MachineLearning, 2024.
3. No inference costs are listed and compared, which is important for LLM decoding strategies.
4. Experiments only comducted two LVLM backbones. More results like on QwenVL are better performed.

### Questions
1. How about using the middle step of Stable Diffusion to provide generative feedback and reduce the computation costs?
2. How about integrating the generative feedback in the instruction tuning phase? It will avoid inference costs.
3. Why not conduct GPT4/GPT4-V analysis like VCD [r1]?
[r1] Mitigating object hallucinations in large vision-language models through visual contrastive decoding. CVPR2024.

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
4

### Summary
This paper proposes self-correcting decoding with generative feedback (DeGF), a novel training-free approach that leverages feedback from diffusion models and corrects decoding procedure, either by contrastive or complementary manner. This paper has well grounded their approach on thorough analysis and ablations, surpassing previous approaches on five hallucination benchmarks.

### Strengths
Clear writing. Presentation and writing are clear and easy to follow.

Well-motivated. A clear negative correlation between hallucination rates and CLIP similarities can be observed (Figure 3), which gives a strong empirical foundation of proposed decoding approach.

Sufficient experiments. Authors do sufficient ablations, discussions to support their claims. Performance of proposed DeGF is quite good.

### Weaknesses
A concern originated from numerical hallucinations. Figure 2 presents an overview of proposed approach DeGF, with addressing numeric hallucinations as an example. A key premise for this method is that diffusion models can accurately perceive numbers. However, it seems a common observation that diffusion models fail to accurately interpret numbers [A]. Have authors considered the case when diffusion models fail to generate numerically accurate images? It is good to include analysis on tolerance of proposed DeGF to diffusion model failures.

Increased test-time computation cost. Diffusion models take dozens of inference steps to generate images, which is computationally less efficient than other decoding approaches.

Authors are suggested to include test-time computation comparison to complete this work.

[A] Mass-Producing Failures of Multimodal Systems with Language Models. NeurIPS 2023.

### Questions
1. May I ask how many samples authors use for plotting Figure 3?

2. For Table 2, may I ask if authors have tested long sequence, by setting max new tokens to larger numbers, such as 128 and 256?

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
The study proposes a new decoding method called Decoding with Generative Feedback (DeGF), which utilizes self-correcting feedback from text-to-image generative models to improve accuracy. By comparing original visual content with generated visuals based on responses, DeGF refines outputs through contrastive predictions. Extensive evaluations show that DeGF enhances performance across benchmarks, effectively reducing various types of hallucinations. However, DeGF faces limitations due to its time-consuming image generation process, limited benchmark evaluations, and inconsistencies in experimental results—particularly on the POPE benchmark compared to LLaVA-1.5—raising concerns about its suitability for real-time use and overall reliability.

### Strengths
- DeGF Leverages generative models to provide self-feedback by comparing the original visual input with a newly generated image, which helps in correcting hallucinations at both response and token levels.

- DeGF  demonstrates the capability of DeGF to handle diverse hallucination types, including object existence, visual appearance, and counting, showing generalizability beyond just language biases.

- DeGF  offers an efficient, cost-effective alternative to existing methods as it avoids the need for additional data or training, focusing instead on refining the decoding process.

- The study finds that text-to-image generative models effectively identify hallucinations. Higher discrepancies in token predictions, measured by JS divergence, indicate hallucinations, showing that generative feedback can highlight inaccuracies both broadly and specifically.

### Weaknesses
- The process of generating images adds time, potentially slowing down LVLM response generation and making it less suitable for real-time applications.
- The authors did not perform more extensive evaluations on comprehensive benchmark such as MMbench, which is crucial for assessing the method's overall performance.
- I am confused by the experimental results about POPE, as they do not seem to fully align with the result from LLAVA 1.5.

### Questions
-  Could the authors clarify the specific settings followed in the experiments on POPE benchmark?  How do these settings differ from those used in LLaVA?
- Could authors follow LLaVA’s setting and conduct more extensive evaluations on comprehensive benchmarks like MMbench and MMVet, given their importance for assessing the model's overall performance?
- Is this decoding method useful in more advanced VLLMs, such as Qwen-VL, Intern-VL, etc.?

### Soundness
3

### Presentation
3

### Contribution
3
