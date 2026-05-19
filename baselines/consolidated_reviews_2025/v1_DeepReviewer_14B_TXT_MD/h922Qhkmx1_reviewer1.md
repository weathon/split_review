### Summary

The paper proposes a method of jointly training a music generation and source separation model. The model is based on a denoising diffusion probabilistic model, and is trained to model the distribution of individual sources. During inference, the model can be used to generate new music (by sampling from the learned distribution), or to separate sources in a given mixture (by conditioning the generation on the mixture).

The proposed method is evaluated in a number of experiments, which appear to show that it performs comparably to existing methods.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. To my knowledge, the idea of jointly training a source separation and source generation model has not been explored before, and could be useful for obtaining better conditional source generation capabilities.

### Weaknesses

#### Some Related Works

[1] Donahue, C., McAuley, J., Raffel, C. A., & Moseley, B. (2023). Singsong: A conditional diffusion model for music generation. arXiv preprint arXiv:2308.06721.
[2] Agostinelli, F., Dedieu, A., Vincent, D., Lachaux, M. A., & Badeau, R. (2023). MusicLM: A Text-to-Music Generation Model. arXiv preprint arXiv:2310.06287.
[3] Liu, X., Chen, J., Pons, J., Peddinti, V., Wang, Y., & Chen, Z. (2023). Audioldm: Latent diffusion model for real-time high-fidelity text-to-audio generation. arXiv preprint arXiv:2310.02074.

#### comment

My main concern is that the paper does not appear to make significant contributions to the field of music generation. While the proposed method can be used for unconditional music generation, the experiments in the paper focus on using it for conditional generation (given a mixture to be separated). In contrast, Singsong [1] is specifically designed for conditional generation, and can be used for both accompaniment generation and vocal removal. Although Singsong targets a different data representation (spectrogram vs. waveform), and has a different network architecture (modified Stable Diffusion vs. U-Net), these differences do not seem substantial, and could potentially be adapted to the problem of source separation. Moreover, the field of music generation is rapidly evolving, with new models such as MusicLM [2] and AudioLDM [3] being released on a monthly basis. As such, it seems that the paper would benefit from a stronger evaluation of the proposed method as a music generation model, for example, by comparing it to existing models.

I also note that the paper does not seem to significantly outperform existing source separation models. While the proposed method appears to perform comparably to Demucs, it is outperformed by Demucs + Gibbs. As such, I find that the claim in the abstract that the proposed method is a "step towards general audio models" to be an overstatement.

### Suggestions

The paper would be significantly strengthened by a more thorough evaluation of its music generation capabilities, particularly in comparison to existing state-of-the-art models. The current evaluation focuses primarily on conditional generation (source separation), which does not fully explore the potential of the proposed model as a general music generation tool. A more comprehensive evaluation should include both quantitative and qualitative assessments of the generated music, using metrics such as FAD (for audio quality) and coherence, as well as human listening tests to evaluate the quality and creativity of the generated samples. It would be beneficial to compare the proposed method against models like Singsong [1], MusicLM [2], and AudioLDM [3], even if the data representations and network architectures differ. This would provide a clearer understanding of the strengths and weaknesses of the proposed method in the context of the rapidly evolving field of music generation. Furthermore, the evaluation should include both unconditional and conditional generation tasks to fully demonstrate the versatility of the model.

To address the concern regarding source separation performance, the paper should include a more detailed analysis of the proposed method's performance compared to existing state-of-the-art models. While the paper shows that the proposed method is competitive with Demucs, it is outperformed by Demucs + Gibbs. A more in-depth analysis should explore the reasons for this performance gap and investigate potential improvements. For example, the authors could explore different sampling strategies or architectural modifications to improve the separation performance. Additionally, the paper should provide a more detailed comparison of the computational cost and efficiency of the proposed method compared to other models. This would provide a more complete picture of the trade-offs between performance and computational resources. The claim of being a "step towards general audio models" should be supported by more substantial empirical evidence.

Finally, the paper could benefit from a more detailed discussion of the limitations of the proposed method and potential avenues for future research. For example, the authors could discuss the challenges of extending the proposed method to more complex audio scenarios, such as multi-channel audio or audio with a large number of sources. They could also discuss the limitations of the current evaluation metrics and the need for more comprehensive and perceptually relevant metrics. Furthermore, the paper could explore the potential of the proposed method for other audio tasks, such as audio editing or sound design. By addressing these limitations and exploring future research directions, the paper could make a more significant contribution to the field.

### Questions

N/A

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
