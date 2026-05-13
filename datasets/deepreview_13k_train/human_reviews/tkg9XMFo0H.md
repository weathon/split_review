# Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Despite their impressive capabilities, Multimodal Large Language Models (MLLMs) are susceptible to hallucinations, especially assertively fabricating content not present in the visual inputs. To address the aforementioned challenge, we follow a common cognitive process - \textit{when one's initial memory of critical on-sight details fades, it is intuitive to look at them a second time to seek a factual and accurate answer.} Therefore, we introduce \textbf{Mem}ory-space \textbf{V}isual \textbf{R}etracing (\textbf{\modelname}), a novel hallucination mitigation paradigm that without the need for external knowledge retrieval or additional fine-tuning. In particular, we treat visual prompts as supplementary evidence to be reinjected into MLLMs via Feed Forward Network (FFN) as “key-value memory”, when the model is uncertain or even amnesic about question-relevant visual memories. Comprehensive experimental evaluations demonstrate that \modelname significantly mitigates hallucination issues across various MLLMs and excels in general benchmarks without incurring added time overhead, thus emphasizing its potential for widespread applicability.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes MEMVR, a training-free hallucination mitigation paradigm for MLLMs. MEMVR mimics human patterns of image understanding by revisiting image features to enhance comprehension of image content, utilizing layer-specific uncertainty for dynamic premature layer injection. The authors validate their approach against hallucination benchmarks as well as general-purpose benchmarks, demonstrating its high efficiency.

### Strengths
1. The writing quality is high. The paper provides a clear introduction to the hallucination problem in MLLMs, analyzes its causes, presents solutions, and offers a theoretical understanding of the methods used, with clear language and logical coherence.
2. High reusability. Due to the training-free nature of MEMVR, it can be applied in a plug-and-play manner across different MLLMs. The method's simplicity allows for easy adaptation with minimal costs.
3. Sufficient experimentation. The authors validate their approach on both hallucination benchmarks and general-purpose benchmarks, proving its adaptability across various scenarios.

### Weaknesses
1. The explanation of the specific process of MEMVR is not sufficiently clear; the discussion of the dynamic injection strategy is brief and potentially confusing. Specifically, the paper lacks a detailed explanation of how the uncertainty is calculated for each layer to determine the injection point. The description of the 're-look' mechanism, particularly how the visual features are re-injected and integrated with the existing hidden states, is also vague. The cross-attention operation and its relation to the FFN are not clearly articulated, making it difficult to understand the precise mechanics of the method.
2. Concerns about usability: The method requires manual tuning of hyperparameters, which may necessitate multiple rounds of adjustments to achieve optimal performance in different scenarios. The paper does not provide clear guidance on how to select the validation set for hyperparameter tuning, nor does it discuss the potential impact of different validation sets on the final performance. The lack of a systematic approach for hyperparameter selection makes the method less practical for real-world applications.

### Questions
1. In formula (2), the feedforward neural network comprises two fully connected layers. As MEMVR is a training-free method, how are the weight matrices W1 and W2 obtained? If they utilize weights from a pre-trained projector within the MLLM, how can their effectiveness be ensured?
2. In formula (3), K and V are regarded as visual projectors. What is their relationship with the keys and values in the attention mechanism? This seems to differ from the kv cache approach, leading to some ambiguity in the expression.
3. The injection ratio α is a manually tuned hyperparameter. How should the validation set be selected during the tuning process? Does the parameter range differ across scenarios such as healthcare and transportation?
4. In line 279, it is mentioned that details about the dynamic injection strategy will be presented in Appendix C.1; however, C.1 only discusses benchmarks. Due to the unclear introduction of the dynamic injection strategy, I still have some questions. If the authors could provide a detailed explanation of this method, I might consider increasing my score.

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
This paper proposes a hallucination mitigation technique called MEMVR, Memory-space Visual Retracing for MLLMs. The approach reinjects visual tokens as “key-value memory” into intermediate layers when high uncertainty is detected, to reinforce alignment between visual and textual information without additional fine-tuning or external data. The author used experimental results to show that MEMVR improves hallucination mitigation across various benchmarks, and the method operates efficiently by only triggering visual reinjection when needed.

### Strengths
- Originality: MEMVR’s approach to hallucination mitigation is innovative, leveraging visual token reinjection without additional training or external databases. This is a straightforward solution that addresses a critical issue in multimodal models.

- Efficiency: The proposed method minimizes computational overhead by using a single inference pass and only invoking reinjection when needed, making MEMVR potentially applicable to real-world scenarios.

- Empirical Performance: MEMVR demonstrates strong results across multiple benchmarks, including improvements over Visual Contrastive Decoding (VCD) and OPERA, showing its effectiveness in reducing hallucinations and enhancing model alignment with visual content.

### Weaknesses
 - Dependence on Threshold-based Mechanism: MEMVR's use of an uncertainty threshold for reinjection may lead to sensitivity to specific datasets or model architectures, potentially affecting its generalizability. The adaptability of this mechanism across different models without manual tuning remains uncertain. It's unclear how the threshold is determined, and whether a single threshold can be universally applied across diverse models and datasets without significant performance degradation. The paper lacks a detailed analysis of how the threshold impacts performance, particularly in edge cases or when dealing with noisy visual inputs. 

- Section C.3 Analysis: Section C.3 highlights only the successes of MEMVR. Including instances of failure would provide a more balanced analysis. Without external data as used by other methods, MEMVR might risk reinforcing biases in the original model by reinjecting similar visual features. Addressing these issues and examining cases where MEMVR underperforms would offer a more comprehensive understanding of its limitations and inform future improvements. The analysis should include specific examples where the reinjection of visual tokens does not lead to improved performance or even degrades it, and explore the reasons behind these failures, such as the complexity of the visual scene or the nature of the hallucination.

- Presentation Style: The Q&A format in Section 4.2 on quantitative results lacks logical structure and clarity. It would be more effective to present this section in a structured format that clearly outlines the key findings, for example: “Q2: How well does MEMVR perform on general-purpose benchmarks?” Can be simply phrase as “MEMVR performance on general-purpose benchmarks.” The current format makes it difficult to quickly grasp the main results and compare the performance across different benchmarks. 

- The paper provides valuable insights but needs more attention to detail in presenting results. Specific issues include:
In Table 2, Qwen-VL-10B + OPERA's best F1 score on MSCOCO is not bolded.
Table 7 shows LLaVA1.5-7B + OPERA and LLaVA1.5-7B + VCD have top scores on gnkwrec and ocrgnsp, respectively, but these are not bolded. Additionally, a value for LLaVA1.5-7B + OPERA is listed as +1.4 instead of +20.
Table 6 reports MemVR’s improvement on Convs as +0.5 instead of +5.0.

### Questions
- Could the authors clarify how the uncertainty threshold was selected, and how sensitive MEMVR is to this parameter across different datasets?

- Are there specific scenarios where MEMVR fails to reduce hallucinations, could you provide a few concrete examples of failure cases and limitation analysis on them?

- Would MEMVR function effectively if extended to other modalities (e.g., audio, 3D data)? Or would it require significant adjustments?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Despite their impressive capabilities, Multimodal Large Language Models (MLLMs) are susceptible to hallucinations, especially assertively fabricating content not present in the visual inputs. To address this issue the authors introduce a hallucination mitigation paradigm named Memory-space Visual Retracing (MEMVR). They design a dynamic premature layer injection strategy with visual retracing in MLLMs, mimicking human intuitive thinking to revisit image features for self-consistency and credible answers when pivotal memories are scrambled. Comprehensive experimental results demonstrate the effectiveness of MEMVR.

### Strengths
1. The paper uses concise and intuitive charts to illustrate the limitations of current methods based on Contrastive Decoding, while also clearly presenting the key design features of the proposed MEMVR framework.

2. Two statistical findings are presented that visually demonstrate the uncertainty present in large language models (LLMs) during multi-layer decoding. The authors provide initial insights into the causes of this uncertainty, adding depth to the analysis.

3. The proposed MEMVR is introduced as a training-free paradigm aimed at mitigating hallucinations in multimodal large language models (MLLMs).

### Weaknesses
The paper’s explanation for the occurrence of hallucinations in MLLMs is not sufficiently persuasive. While the authors identify uncertainty in the decoding process, they fail to provide adequate evidence that this uncertainty stems from the forgetting of visual features, subsequently leading to hallucinations. To strengthen this claim, I recommend that the authors conduct additional experiments, such as directly masking input image tokens to simulate the effect of forgetting. They could then test whether MEMVR is able to recover visual features through the "look twice" mechanism while utilizing the normal image tokens during the recovery process.

Poor Presentation. The presentation of the proposed method is convoluted and lacks clarity. The authors unnecessarily complicate straightforward concepts by introducing numerous "unusual" symbols and formulas. While this may create an impression of sophistication, it significantly increases the reading difficulty for the audience. For instance, in Equation (2), the symbol 
 typically denotes proportionality; however, the intended meaning remains unclear. Furthermore, the relationship between the content of Equation (2) and its explanation in Equation (3) is separated by a substantial amount of text, making it laborious for readers to follow. Additionally, the terms 
 and 
 mentioned in line 256 lack proper definitions, leading to confusion—if they represent trainable parameters of the FFN, it is unclear why they are treated as keys and values. There are multiple instances of such issues throughout the manuscript, indicating that it is not a well-presented piece of work. Here are some suggested modifications:
1. Provide a clear definition and explanation for each symbol when it is first introduced, especially for non-standard usage like $\propto$ in Equation (2).
2. Reorganizing the text to keep related equations and their explanations closer together, particularly for Equations (2) and (3).
3. Clearly define the terms $k$ and $v$ and explain the rationale behind treating them as keys and values if they are indeed FFN parameters.
4. Recommending the inclusion of a notation table or glossary to help readers keep track of symbols and their meanings throughout the paper.
5. Try to review the entire manuscript to identify and simplify overly complex formulations without losing essential information.

### Questions
See weakness.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a novel approach named Memory-Space Visual Retracing (MEMVR) to address the challenge of hallucinations in Multimodal Large Language Models (MLLMs). Hallucinations in this context refer to the models' tendency to generate content that is inconsistent with the provided visual inputs, which can compromise their reliability in various applications. MEMVR is designed to mimic a human cognitive process where one would revisit visual details to seek accurate answers when initial memories fade. It operates by reinjecting visual features as "key-value memory" into the model's Feed Forward Network (FFN) layers when the model exhibits uncertainty or memory lapses regarding visual details. This method does not require external knowledge retrieval or additional fine-tuning. The paper presents comprehensive experimental evaluations demonstrating that MEMVR significantly reduces hallucination issues across various MLLMs and performs well in general benchmarks without incurring additional time overhead.

### Strengths
1.  MEMVR is a training-free approach that enhances the model's ability to retrieve question-relevant visual information within the FFN layers, incurring minimal additional inference overhead.
2. The method demonstrates effectiveness in various benchmarks.
3. The authors provide a thorough analysis of the relationship between model uncertainty and the tendency to hallucination.

### Weaknesses
1. The paper presents a method for hallucination mitigation in MLLMs by re-focusing on visual details relevant to the textual prompt. While the concept of improving model performance through prompt-related visual cues is not entirely new, with prior works like API[1], AGLA[2] exploring similar ideas. Despite some innovation in the design, the contributions do not seem to offer substantial new value or advancements in the field.
2. The paper's writing style can be overly embellished, making it less intuitive in certain parts, which may not clearly convey the intended message.
3. The phrase "signifies the other side of the coin" at line 114 is unclear and requires further explanation to understand its intended meaning.
4. While the authors claim at line 499 that MEMVR is flexible and compatible with various architectures, they also mention at line 514 that adapting the method to other structures is challenging. It raises the question of whether MEMVR can be generalized to models like LLaVA-next and InstructBlip.
5. The analysis of uncertainty in section 3.2 is based on the entropy of the decoder's output distribution, but the impact of uncertainty on the method, as shown in Figure 7, is analyzed by adding noise to the images. The claim that the method is unrelated to the biases of language priors may be questionable, as the entropy-based uncertainty measure could be connected to these biases. Additionally, it is unclear how the analysis of uncertainty in section 3.2 is directly related to the proposed method, beyond its application in the Dynamic Injection Strategy.
6. There is a typo error in line 390 where "Preception" should likely be "Perception."
7. I recommend that the authors restructure the paper, including both figures and text, to express their ideas more clearly and logically, rather than attempting to embellish the research to make it appear more sophisticated.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
