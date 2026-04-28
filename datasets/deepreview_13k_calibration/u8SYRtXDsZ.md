# AVESFormer: Efficient Transformer Design for Real-Time Audio-Visual Segmentation

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Recently, transformer-based models have demonstrated remarkable performance on audio-visual segmentation (AVS) tasks.
  However, their expensive computational cost makes real-time inference impractical.
  By characterizing attention maps of the network, we identify two key obstacles in AVS models: 1) attention dissipation, corresponding to the over-concentrated attention weights by Softmax within restricted frames, and 2) inefficient, burdensome transformer decoder, caused by narrow focus patterns in early stages.
  In this paper, we introduce \textbf{AVESFormer}, the first real-time \textbf{A}udio-\textbf{V}isual \textbf{E}fficient \textbf{S}egmentation transformer that achieves fast, efficient and light-weight simultaneously.
  Our model leverages an efficient prompt query generator to correct the behaviour of cross-attention. 
  Additionally, we propose ELF decoder to bring greater efficiency by facilitating convolutions suitable for local features to reduce computational burdens.
  Extensive experiments demonstrate that our AVESFormer significantly enhances model performance, achieving 79.9\% on S4, 57.9\% on MS3 and 31.2\% on AVSS, outperforming previous state-of-the-art and achieving an excellent trade-off between performance and speed.git}{here}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper finds two primary challenges in existing audio-visual segmentation models, namely attention dissipation caused by anomalous attention weights after Softmax over limited frames, and narrow attention patterns in shallow decoder stages leading to inefficient utilization of attention resources. An AVESFormer is then presented as the first real-time audio-visual efficient segmentation transformer. Particularly, the proposed method leverages a prompt query generator to rectify cross-attention behavior, and an early focus decoder to enhance efficiency. Extensive experiments demonstrate superiority of AVESFormer in mitigating cross-attention issues and achieving a trade-off between model effectiveness and efficiency.

### Strengths
1. Solving AVS via attention analysis is reasonable given the multimodal nature of AVS.
2. The attention dissipation issue seems interesting given the current QKV setting.
3. The experiments are comprehensive.

### Weaknesses
1. The two observations which motivate the proposed method are not clear explained (see details in the Questions section).
2. The setting of the paper for real time AVS should also be verified, especially it should be compared to naive settings, e.g. defining the rest of the frames as an empty token. Most importantly, as temporal information is totally discarded, more analysis is needed on how the proposed method achieve smooth real time AVS.
3. Comparison with other attention based techniques is needed (Ref 1 in the Questions section.)

### Questions
1. Line 53-76 tries to explain the issues of exiting AVS method. Although it's reasonable that effective multimodal fusion should be critical for AVS, it's not clear why this claim hold: "attention variants generally do not exhibit the same expressive capacity as the default mechanism" (line 75). Further explanation is needed.
2. In Fig. 2, the paper illustrates of attention dissipation. How the audio token is generated? Is this only a one case issue or does it happen all the time in all types of cross attention based AVS? More details are needed to verify the existence of the attention dissipation issue, especially when audio is defined as both key and value in the current cross attention setting. Moreover, where does the cross attention AVS model in equation 1 come from? Citation(s) are needed if it comes from existing literatures, or explanations are needed to explain why QKV is defied in the current way (compared to Ref1, Ref2, Ref3).
3. "Attention maps at early decoder stages tends to capture short-term local correlation features, leading to undesired low utilization of attention" (line 89-91) is used to explain the "narrow attention" issue, which is also not very clear. Why call it "narrow"?
4. In line 123, it's not clear why the existing AVS methods fail to work on the "single frame image + audio" setting.
5. what is the audio backbone in line 184?
6. F_audio=k=v, not clear (line 194). Also, audio feature dimension is D in line 185 and c in line191. It's better to use consistent symbols.
7. The prompt query generator (sec. 4.1) augments the audio feature. How does it bring extra useful information given the augmentation is based on the raw audio feature?
8. The early focus decoder is used to solve the "narrow attention" issue. However, it's not clear how eq. 6 and eq. 7 combined can solve the narrow attention issue.
9. In Table 1, why Ref1 is not compared?
10. In Table 4 and Table 5, it seems the proposed two strategies work better for MS3 dataset, explanations are needed.

Ref1: Unraveling Instance Associations: A Closer Look for Audio-Visual Segmentation. CVPR 2024

Ref2: AVSegFormer: Audio-Visual Segmentation with Transformer. AAAI 2024

Ref3: Audio–visual segmentation. ECCV 2022

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces AVESFormer, a transformer model designed for real-time audio-visual segmentation (AVS). It addresses attention dissipation and narrow attention patterns in AVS by implementing a Prompt Query Generator (PQG) and Early Focus (ELF) Decoder. These components aim to improve cross-attention efficiency and reduce computational costs. AVESFormer shows competitive performance on AVSBench with noted speed improvements.

### Strengths
1. The paper identifies critical issues in existing audio-visual segmentation (AVS) models, such as attention dissipation and narrow attention patterns, which are valid challenges in the field.

2. The proposed AVESFormer model aims to address efficiency in real-time AVS tasks, which could be valuable for applications needing low-latency responses.

3. The model demonstrates competitive performance on standard benchmarks with a noted improvement in latency, supporting claims of efficiency gains.

### Weaknesses
While the issues identified in attention mechanisms are relevant, the approach—specifically the Prompt Query Generator and Early Focus Decoder—largely leverages incremental modifications rather than substantial innovations. Many elements, such as convolutional layers for early-stage feature extraction, are already established techniques in efficient transformers. The core of the method, the Prompt Query Generator (PQG), seems to be a relatively straightforward adaptation of existing query generation techniques, lacking a novel approach to how audio and visual information are integrated to form the prompts. Similarly, the Early Focus (ELF) Decoder, while aiming to reduce computational cost, appears to be a somewhat standard application of early-stage feature processing, without demonstrating a significant departure from existing decoder architectures. The paper does not adequately explore the limitations of these design choices, particularly how the PQG handles complex audio-visual relationships beyond simple co-occurrence, and how the ELF decoder might impact the model's ability to capture fine-grained segmentation details.

### Questions
See weaknesses

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
The paper presents AVESFormer, a transformer-based model for real-time audio-visual segmentation AVSAVS. It tackles two main issues in existing AVS models: attention dissipation and limited attention patterns in early decoders. AVESFormer uses a Prompt Query Generator PQGPQG to improve cross-attention and an Early Focus ELFELF decoder that integrates convolutional operations for efficient local feature extraction, reducing computational costs. Experiments show that AVESFormer addresses cross-attention problems, enhances attention utilization, and outperforms previous state-of-the-art models in both performance and speed. Additionally, the paper analyzes attention dissipation and the shortcomings of standard transformer decoders in real-time AVS.

### Strengths
A key innovation is the Prompt Query Generator PQGPQG, which corrects cross-attention behavior and mitigates attention dissipation, enhancing segmentation accuracy and efficiency. Additionally, the Early Focus ELFELF decoder incorporates convolutional operations for local feature extraction, reducing computational demands by replacing attention operations in early transformer stages. The model achieves state-of-the-art performance, surpassing previous models on metrics like the Jaccard index and F-score across datasets such as S4, MS3, and AVSS.

### Weaknesses
One concern is the significant parameter count of the audio backbone, Vggish, which limits deployment on mobile devices, suggesting future work could optimize this component. Specifically, the Vggish network, with its deep architecture and numerous convolutional layers, contributes a substantial portion of the model's overall parameters, making it computationally expensive and memory-intensive. Additionally, the model currently ignores temporal information from multiple frames, and incorporating this data could enhance its ability to track moving objects. The lack of temporal modeling means the model processes each frame independently, potentially missing crucial motion cues that could improve segmentation accuracy, especially for dynamic scenes. There is also a need to test the model's generalization to unseen datasets beyond AVSBench to evaluate its robustness in diverse scenarios. The current evaluation, limited to AVSBench, might not fully capture the model's performance across varied audio-visual conditions and object types. While qualitative analyses of attention maps are presented, a quantitative investigation could offer deeper insights into the model's attention mechanisms. A more rigorous analysis, using metrics such as attention entropy or variance, could provide a more objective assessment of the model's focus and attention distribution. Furthermore, comparing AVESFormer with non-transformer models would provide a broader context for its performance. The paper could also benefit from a more detailed discussion on the impacts of model complexity on real-time performance and ethical considerations regarding its application. The current discussion lacks a thorough analysis of how the model's parameter count and computational demands affect its real-time capabilities, and it does not address potential biases or misuse scenarios.

### Questions
The authors should consider optimizing the audio backbone, Vggish, which currently comprises about 60% of the model parameters, to enable better deployment on mobile devices. Next, the authors are encouraged to explore how incorporating temporal information might influence model performance and inference speed. Additionally, evaluating AVESFormer on a broader range of datasets beyond AVSBench would provide insights into its generalization capabilities. The paper currently lacks a detailed quantitative analysis of attention maps, so including metrics to evaluate the focus and spread of attention could enhance understanding of the model's behavior.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors proposed AVESFormer, an efficient framework for audio-visual segmentation tasks. By solving two issues of using cross-attention as attention dissipation and narrow attention patterns, they can effectively improve the utilization of cross-attention between audio and visual. AVESFormer improves attention utilization, improves the performance as well as reduces the running time.

### Strengths
- The paper is well-written and easy to follow.

- The authors offer comprehensive ablation studies, which aid in comprehending the various design decisions involved in solving cross-attention issues.

- The proposed method shows a strong performance improvement as well as a reduction in the inference time.

- Sufficient comparison with SOTA methods

### Weaknesses
 - Some typo: Table 3: lartency -> latency

- Regarding the PQG, what is the result if we set the number of queries to the number of objects in the category?

- How much of the flops and memory that AVESFormer save from replacing the early attention with convolution?

- Does the number of stages in the decoder affect the performance?

- Missing references [1], [2], and [3] in Table 1

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
