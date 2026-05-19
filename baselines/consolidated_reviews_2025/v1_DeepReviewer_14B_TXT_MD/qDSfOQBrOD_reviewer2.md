### Summary

The paper proposes a neural speech codec with built-in voice change capability for real-time communication scenarios. The system is based on a fully causal convolutional encoder-decoder network with scalar quantization. A lightweight causal projection network is proposed to perform timbre adaptation on tokens. The system is evaluated on both speech coding and voice conversion tasks, and compared with several state-of-the-art methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper proposes a novel system that integrates voice change into speech codec, which has potential applications in real-time communication.
- The system design is reasonable and well-motivated, using causal convolutions and a lightweight projection network to enable real-time inference and minimize latency.
- The system achieves competitive results on both speech coding and voice conversion tasks, demonstrating its effectiveness and versatility.

### Weaknesses

#### Some Related Works


#### comment

 - The system is only evaluated on a sampling rate of 16kHz, which is not the case for most of the state-of-the-art (SOTA) models.
- The model is not compared to any SOTA models in the voice changer mode. The only comparison is with the original voice mode, which is not a fair comparison since the baseline models are not designed for voice conversion.
- The model is not evaluated on the quality of voice conversion, but only on the quality of the output speech. The naturalness and similarity of the converted speech are not assessed.

### Suggestions

The paper would benefit significantly from a more thorough evaluation of the voice conversion capabilities, particularly in comparison to existing state-of-the-art voice conversion models. The current evaluation focuses primarily on speech quality metrics, which do not fully capture the performance of a voice conversion system. It is crucial to include metrics that specifically assess the naturalness and speaker similarity of the converted speech. For example, metrics like Mel Cepstral Distortion (MCD) for spectral distortion, and speaker recognition scores to measure the similarity between the converted and target speaker's voice, should be included. Furthermore, subjective evaluations such as Mean Opinion Score (MOS) tests for naturalness and similarity would provide valuable insights into the perceived quality of the voice conversion. The lack of these evaluations makes it difficult to ascertain the true effectiveness of the proposed method in the voice conversion domain.

To strengthen the paper, the authors should also consider comparing their model against other state-of-the-art voice conversion models, especially those that are designed for real-time applications. This would provide a more comprehensive understanding of the proposed model's performance relative to existing techniques. The comparison should not only focus on objective metrics but also include subjective evaluations to assess the perceived quality of the converted speech. It is important to ensure that the baseline models are evaluated under similar conditions, including the same datasets and evaluation protocols. This would allow for a fair and meaningful comparison of the proposed model's performance. Additionally, the authors should explore the impact of different quantization levels on the quality of the converted speech, as this is a key aspect of the proposed method. A detailed analysis of how the quantization process affects both speech quality and voice conversion quality would be beneficial.

Finally, the paper should address the limitations of using a 16kHz sampling rate. While this may be suitable for some applications, many state-of-the-art models operate at higher sampling rates, such as 48kHz, which can capture a wider range of frequencies and potentially lead to better speech quality. The authors should either provide a justification for using a 16kHz sampling rate or conduct experiments at higher sampling rates to demonstrate the model's performance in those conditions. This would make the paper more relevant to a broader range of applications and allow for a more direct comparison with other state-of-the-art models. Furthermore, the authors should clarify the specific datasets used for training and evaluation, and ensure that the evaluation datasets are representative of real-world scenarios. This would improve the reproducibility and generalizability of the results.

### Questions

- How does the model perform on a higher sampling rate, such as 48kHz?
- How does the model compare to other state-of-the-art voice conversion models in terms of voice conversion quality?
- How does the model perform on the voice conversion quality metrics, such as naturalness and similarity?

### Rating

6

### Confidence

4

**********
