# ACUS: Audio Captioning with Unbiased Sliced Wasserstein Kernel

- Decision: Reject
- Scores: 8, 3, 6, 5, 3

## Abstract
Teacher-forcing training for audio captioning usually leads to exposure bias due to training and inference mismatch. Prior works propose the contrastive method to deal with caption degeneration. However, the contrastive method ignores the temporal information when measuring similarity across acoustic and linguistic modalities, leading to inferior performance. In this work, we develop the temporal-similarity score by introducing the unbiased sliced Wasserstein RBF (USW-RBF) kernel equipped with rotary positional embedding to account for temporal information across modalities. In contrast to the conventional sliced Wasserstein RBF kernel, we can form an unbiased estimation of USW-RBF kernel via Monte Carlo estimation. Therefore, it is well-suited to stochastic gradient optimization algorithms, and its approximation error decreases at a parametric rate of $\mathcal{O}(L^{-1/2})$ with $L$ Monte Carlo samples. Additionally, we introduce an audio captioning framework based on the unbiased sliced Wasserstein kernel, incorporating stochastic decoding methods to mitigate caption degeneration during the generation process. We conduct extensive quantitative and qualitative experiments on two datasets, AudioCaps and Clotho, to illustrate the capability of generating high-quality audio captions. Experimental results show that our framework is able to increase caption length, lexical diversity, and text-to-audio self-retrieval accuracy. We also carry out an experiment on two popular encoder-decoder audio captioning backbones to illustrate that our framework can be compatible with a diversity of encoder-decoder architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ACUS (Audio Captioning with Unbiased Sliced Wasserstein kernel), a novel framework that addresses exposure bias and temporal misalignment issues in audio captioning systems. The key technical contribution is the development of an unbiased sliced Wasserstein RBF (USW-RBF) kernel equipped with rotary positional embeddings, which effectively measures similarity between acoustic and linguistic features while preserving temporal information. Experimental results on AudioCaps and Clotho datasets demonstrate significant improvements over state-of-the-art methods across multiple metrics.

### Strengths
The paper introduces an unbiased sliced Wasserstein RBF (USW-RBF) kernel that effectively handles temporal information across modalities while avoiding dimensionality curse issues that affect traditional Wasserstein distances.

Strong Theoretical Foundation: Provides formal proofs for the kernel's properties (positive definiteness, unbiasedness).
Demonstrates convergence rate for Monte Carlo estimation.

Comprehensive Evaluation: Tests on multiple datasets (AudioCaps and Clotho). Uses both automatic metrics and human evaluation
Includes detailed ablation studies for various components.

Achieves state-of-the-art performance on multiple metrics

### Weaknesses
No analysis of computational overhead from the USW-RBF kernel

Unclear how the method performs on longer audio sequences

While ablation studies are included, there's limited discussion of how sensitive the method is to various hyperparameters
Could benefit from more guidance on hyperparameter selection for new datasets.

Lacks detailed analysis of failure cases

### Questions
How does the computational complexity scale with audio length and batch size compared to baseline methods?
How robust is the method to different audio qualities or noise levels? Was this tested?
What is the impact of different positional embedding choices on the final performance? While rotary embeddings performed best, is there a theoretical justification for this?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel approach for audio captioning to address issues related to exposure bias and temporal misalignment. Here’s a summary of the key contributions:
1. Unbiased Sliced Wasserstein RBF Kernel (USW-RBF): The authors propose a novel kernel method to accurately measure cross-modal similarity between audio and textual data. This kernel, equipped with rotary positional embedding, captures temporal information more effectively than traditional methods, addressing limitations like dimensionality and temporal distortion.
2. Mitigating Exposure Bias: ACUS employs stochastic decoding techniques, such as nucleus and top-k sampling, to reduce exposure bias during the inference stage, enhancing caption diversity and quality. This is achieved by leveraging the USW-RBF kernel to improve alignment between generated captions and audio inputs.
3. Extensive Evaluation and Compatibility: The framework’s efficacy is validated through experiments on two datasets, AudioCaps and Clotho. Results demonstrate improved caption length, lexical diversity, and self-retrieval accuracy, and compatibility with diverse encoder-decoder architectures.

In essence, ACUS represents an advancement in audio captioning by integrating the unbiased USW-RBF kernel with stochastic decoding, leading to more descriptive and temporally coherent audio captions.

### Strengths
1. The introduction of the unbiased sliced Wasserstein RBF (USW-RBF) kernel, which captures temporal information across audio and text modalities, is an advancement. By accounting for temporal alignment, it addresses limitations in prior contrastive methods that often ignore the temporal structure of audio data.
	
2. ACUS effectively addresses exposure bias—a common issue in captioning tasks—by combining the USW-RBF kernel with stochastic decoding methods. This approach ensures that generated captions maintain diversity and relevance across varying contexts.
	
3. The ACUS framework enhances not only the length and diversity of captions but also their semantic alignment with audio events. By capturing temporal details, it generates more descriptive and meaningful captions, which are validated by both quantitative metrics and qualitative assessments.

4. The paper thoroughly derives and proves the properties of the USW-RBF kernel, reinforcing its validity for multimodal tasks. Additionally, by introducing a practical approach to reducing exposure bias, it offers a methodological contribution that may extend beyond audio captioning to other sequence generation tasks.

### Weaknesses
1. While the paper introduces a promising method, the improvements observed in the current experiments are relatively modest. To more rigorously validate the effectiveness of your approach, I recommend evaluating your model on additional, more challenging benchmarks, which may make this work more convincing if your method reach higher score in these benchmarks, such as:

a. SUPERB: This benchmark includes a broad range of speech processing tasks, covering content, speaker, semantics, and paralinguistics. It would provide a comprehensive baseline, helping clarify how well your model generalizes across core speech tasks.

b. Dynamic-SUPERB: This benchmark extends SUPERB with instruction-tuning and zero-shot tasks, pushing models to handle more complex and varied speech processing scenarios. Testing on Dynamic-SUPERB could demonstrate your method’s robustness and adaptability in handling multi-task and instruction-following requirements, offering deeper insights into its generalization capabilities.

c. SpeechCaps: Given the emphasis in your work on speaker-specific and temporal information, SpeechCaps offers a relevant test for multi-talker and speaking style captioning. Its focus on speaker and prosodic information could highlight the strengths of your model in more intricate, real-world audio scenarios, such as multi-speaker dialogues and expressive speech.

2. Authors provide a detailed explanation of the USW-RBF kernel. However, it lacks sufficient details on how this kernel is integrated within the overall model architecture. You can try these to make it better, such as:

a. Integration Details: Please provide a clearer, step-by-step description of how the USW-RBF kernel is incorporated into the model pipeline. 

b. Diagram or Flowchart: Consider adding a diagram or flowchart that visualizes the integration process, illustrating where and how the USW-RBF kernel interacts with audio and textual embeddings within the architecture.

### Questions
1. There are some minor errors, like in line 187, it should be \( \nu = \frac{1}{N} \sum_{j=0}^N \delta_{z_y^j} \), not \( \nu = \frac{1}{M} \sum_{j=0}^N \delta_{z_y^j} \), to make two empirical distributions have the same number of supports. I did not thoroughly inspect every math part in this paper, but I think authors could check the whole paper again thoroughly.  Also, in conclusion, it should be "unbiased kernel", not "unbias kernel". (No worries, they are just minor error, but it is better to correct for clarity.)

2. As I mentioned in weakness part, the reported improvements over baselines appear modest. Could you provide more analysis on how the proposed method performs in more challenging scenarios (e.g., multi-speaker or noisy environments) to better highlight its strengths? If not, do you believe that temporal information is important in audio captioning task? 

3. The application area of this work seems limited. Do you have any plans to extend this work for multilingual audio captioning or automatic speech recognition? If so, how might the kernel method adapt to language diversity in audio processing? how you modify the text embedding under multilingual scenario? 

4. Since you use stochastic decoding strategies in inference stage, which may lead to high computational costs, and the reported score in your results is not very decent, we might not need such a high-cost method to get a minor improvement. Thus, could you provide more details on the differences in diversity and quality of captions generated by your approach?

### Soundness
2

### Presentation
2

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
The paper proposes a new framework for audio captioning designed to mitigate exposure bias and improve temporal cross-modal similarity measurement. The authors claim that traditional audio captioning models trained via maximum likelihood estimation face exposure bias, leading to "degeneration" in generated captions. This paper introduces the unbiased sliced Wasserstein (USW-RBF) kernel equipped with rotary positional embedding to capture temporal information across acoustic and linguistic modalities, thereby reducing exposure bias. The authors show improvements on benchmark datasets (AudioCaps and Clotho)

### Strengths
- The paper is decently written and easy to follow for an expert. However, I would like to mention it might be difficult for a traditional audio captioning community to read. A bit more background on the 1, the unbiased sliced Wasserstein RBF kernel would have been appreciated.  The equations could have been improved by defining the notations better. Fro examples, if I want to read Eqtn 9., I need to find what the notations mean somewhere else in the paper.
- The problem handled in the paper is new. The approach is also novel. ACUS combines the USW-RBF kernel with stochastic decoding methods like nucleus and top-k sampling to alleviate exposure bias during inference. A lot of work in audio captioning ideally propose new architectures. This paper brings a fresh perspective in the problem space.
- The evaluation is sound. The 2 usual benchmark datasets are used and it is also combined with human evaluation. The metrics of descriptiveness, correctness, and fluency are good metrics for comparison as ideal benchmark metrics seem to have saturated and require style memorization.

### Weaknesses
 - The abstract says" "Prior works propose the contrastive method to deal with caption degeneration. However, the contrastive method ignores the temporal information when measuring similarity across acoustic and linguistic modalities, leading to inferior performance." -- which contrastive method and how does it ignore the "the temporal information when measuring similarity across acoustic and linguistic modalities"? This first line of the paper is very difficult to understand.
- The Monte Carlo sampling and stochastic gradient optimization may increase computational costs, potentially impacting efficiency in real-world large-scale applications.
- While I understand that the authors focus on Enc-Dec framework, a good number of baselines were missed for evaluation. ACUS can act as complimentary to most other methods proposed in literature as all methods require an audio encoder and a language decoder (including prefix based architectures). Thus, some baselines were missed. See [1,2] as examples and papers compared in [1,2].
- The analysis section is just ablations. A deeper analysis section (see questions below) would have strengthened the paper.

### Questions
- How does the performance of USW-RBF compare with other non-Wasserstein-based kernels for audio captioning tasks?
- What are the potential trade-offs between the accuracy improvements and the computational costs introduced by Monte Carlo sampling and stochastic gradient optimization in ACUS?
- Why was the rotary positional embedding favored over other encoding techniques, and could alternative embeddings further enhance the results?
- Why audio captioning? Can the method be useful to other tasks? Audio understanding? Speech Recognition?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel framework tackling the training-inference mismatch in automated audio captioning (AAC) by introducing a temporal-similarity score based on the unbiased sliced Wasserstein RBF (USW-RBF) kernel with rotary positional embeddings. By integrating this score with a stochastic decoding strategy, the approach effectively addresses caption degeneration issues encountered during inference. Experimental results on established AAC benchmark datasets demonstrate notable improvements in model performance, validated through both quantitative and qualitative metrics.

### Strengths
1. This paper introduces a novel temporal-similarity score, utilizing the unbiased sliced Wasserstein RBF (USW-RBF) kernel with rotary positional embeddings, to mitigate exposure bias in audio captioning models. Unlike prior research, which has not employed the USW-RBF kernel for cross-modal similarity calculation, this study leverages it to capture temporal dynamics more effectively.
2. The proposed framework is adaptable to a wide range of existing AAC models, with experimental results underscoring its effectiveness in improving model performance.
3. Comprehensive qualitative and quantitative experiments support the method's efficacy. Ablation studies comparing various similarity metrics further highlight the advantages of the USW-RBF kernel over alternative approaches.

### Weaknesses
1.	Combining the USW-RBF kernel with stochastic decoding strategies may lead to high computational costs. For example, at inference time, generating $\mathcal{B}$ candidate captions through stochastic decoding results in increased computational time. While the paper demonstrates effectiveness, it lacks a detailed discussion of computational overhead in training and inference, specifically regarding the time complexity of calculating the USW-RBF kernel and the impact of the number of Monte Carlo samples ($L$) on both training and inference times. Furthermore, the paper does not provide a clear analysis of how the computational cost scales with the size of the input audio and text sequences.
2.	The performance increase with the proposed approach is relatively minor. According to the original paper, EnCLAP-large achieved SPIDEr scores of 49.5 and 27.8 on AudioCaps and Clotho, while the proposed method reached only 50.0 and 27.5, making the claimed improvement less convincing. According to this comparison, the exposure bias is not that important in AAC tasks. The reported improvements, while present, are marginal and may not justify the added complexity of the proposed method. A more thorough analysis is needed to demonstrate the practical significance of these gains, especially considering the computational overhead.
3.	The application scope of this work appears limited, focusing primarily on AAC tasks. The authors have not explored the framework’s performance on other audio-text multimodal tasks, such as audio-text retrieval, and automatic speech recognition. For instance, can the proposed temporal-similarity score enhance the temporal reasoning capability of the CLAP model? It is unclear if the proposed method can be generalized to other tasks that involve cross-modal alignment between audio and text. The paper lacks a discussion on the potential limitations of the approach when applied to tasks with different characteristics.
4.	The study does not deeply explore the sensitivity of the framework to key hyper-parameters, such as the coefficient $\alpha$ in the objective function or the number of Monte Carlo samples $L$ used for the USW-RBF kernel. A comprehensive sensitivity analysis is needed to understand the robustness of the method and to provide guidelines for selecting optimal hyper-parameter values. The paper should include a detailed discussion on how these parameters affect the performance and computational cost of the model.
5.	The paper dedicates considerable space to explaining the USW-RBF kernel but provides a limited description of how it integrates with the model itself. For example, it’s unclear whether the text embedding is derived from the penultimate layer of the text decoder or from another layer. The lack of clarity regarding the integration of the USW-RBF kernel with the model makes it difficult to understand the practical implementation details of the proposed method. A more detailed explanation of the model architecture and the specific layers involved in the similarity calculation is needed.
6.	Although the paper separates AAC models into encoder-decoder and prefix-tuning architectures, with experiments performed only on the encoder-decoder type. The difference between these two types of architecture is not substantial. Both approaches essentially share the same structure of an audio encoder and a text decoder.
(Minor problems - Line 44: the former architecture → the latter architecture)

### Questions
1. Could the authors provide a more detailed explanation of the differences between the two types of AAC architectures? Additionally, could the proposed method be adapted for application within prefix-tuning structures?
2. What is the increase in computational cost introduced by the framework? For example, how much additional inference time is required when using stochastic decoding to generate $\mathcal{B}$ candidate captions?
3. Considering the advanced reasoning and generative capabilities of large language models, frequently used in AAC tasks, could the proposed approach be adapted to work alongside LLMs to achieve higher-quality captions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper is written to solve the exposure bias problem in audio captioning.
They propose the unbiased sliced Wasserstein RBF kernel, which is a better cross-modality similarity measure.
Together with the contrastive learning method, gains are observed in the audio captioning tasks.

### Strengths
This paper propose the unbiased sliced Wasserstein kernel framework to improve the audio captioning performance.

### Weaknesses
The motivation of the paper does not sound convincing.
Exposure bias is a general problem to auto-regressive networks. 
It is not a critical problem for audio captioning.
In general, exposure bias can be mitigated by a better training of model. 
I believe using a larger decoder will ease the problem a lot.
Specifically, I do not see in the paper how much the exposure bias problem is harming the audio captioning performance.
Even if we regard this as a serious problem, reinforcement learning (RL) should be a popular way to solve it as RL trains the model according to its inference output. The paper doesn't discuss about RL and address the audio captioning problem in a very narrow perspective.

### Questions
As proposing the unbiased kernel is the core technical contribution in the paper, how much gain is there from a biased kernel to a unbiased kernel ?

### Soundness
2

### Presentation
2

### Contribution
2
