### Summary

The paper proposes a novel framework for image compression that is able to control the compression rate by varying the granularity of the latent representations. The framework is based on VQGAN, and the authors introduce a granularity-informed encoder that maps image patches into hierarchical features of three granularities. The authors also introduce a probabilistic conditional decoder that aggregates the multi-granularity representations to reconstruct the image. The authors conduct experiments on the Kodak dataset and show that their framework achieves better rate-distortion performance compared to the baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The idea of controlling the compression rate by varying the granularity of the latent representations is interesting and novel.
- The authors conduct experiments on the Kodak dataset and show that their framework achieves better rate-distortion performance compared to the baselines.
- The authors provide a detailed description of the proposed method, including the encoder, decoder, and loss function.

### Weaknesses

#### Some Related Works


#### comment

 - The authors only conduct experiments on the Kodak dataset. It would be beneficial to evaluate the proposed framework on other datasets, such as the DIV2K dataset, to demonstrate its generalizability.
- The authors claim that their framework is able to control the compression rate by varying the granularity of the latent representations. However, it is not clear how the granularity is controlled in practice. Specifically, it is not clear how the ratio of medium-grained to fine-grained features is determined and how this affects the compression rate. A more detailed explanation of the granularity control mechanism is needed.
- The authors do not provide a detailed analysis of the computational cost of the proposed framework. It would be beneficial to compare the computational cost of the proposed framework with other state-of-the-art image compression methods. This analysis should include the encoding and decoding times, as well as the memory requirements.
- The authors do not provide a detailed analysis of the impact of the number of latent vectors on the performance of the proposed framework. It would be beneficial to investigate how the performance of the framework changes with different numbers of latent vectors and to provide a justification for the choice of the number of latent vectors used in the experiments.

### Suggestions

The authors should provide a more detailed explanation of how the granularity of the latent representations is controlled. Specifically, they should clarify how the ratio of medium-grained to fine-grained features is determined and how this ratio affects the compression rate. It would be beneficial to include a mathematical formulation of the granularity control mechanism and to provide a step-by-step explanation of how the granularity is varied during the compression process. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed framework. This analysis should include the encoding and decoding times, as well as the memory requirements. It would be beneficial to compare the computational cost of the proposed framework with other state-of-the-art image compression methods, such as BPG and VVC. This comparison should be done under similar conditions, including the same hardware and software configurations. The authors should also provide a detailed analysis of the impact of the number of latent vectors on the performance of the proposed framework. It would be beneficial to investigate how the performance of the framework changes with different numbers of latent vectors and to provide a justification for the choice of the number of latent vectors used in the experiments. This analysis should include a discussion of the trade-offs between compression rate and reconstruction quality.

To further strengthen the paper, the authors should consider evaluating their framework on a wider range of datasets, including the DIV2K dataset. This would help to demonstrate the generalizability of the proposed framework and to show that it is not limited to the Kodak dataset. The authors should also consider comparing their framework with other state-of-the-art image compression methods, such as BPG and VVC, under different compression rates. This would help to demonstrate the advantages of the proposed framework over existing methods. The authors should also consider providing a more detailed analysis of the impact of the proposed method on the perceptual quality of the reconstructed images. This analysis should include a discussion of the trade-offs between compression rate and perceptual quality and should provide a justification for the choice of the compression rate used in the experiments.

Finally, the authors should provide a more detailed explanation of the probabilistic conditional decoder. Specifically, they should clarify how the multi-granularity representations are aggregated to reconstruct the image. It would be beneficial to include a mathematical formulation of the decoder and to provide a step-by-step explanation of how the decoder works. The authors should also provide a more detailed analysis of the impact of the decoder on the reconstruction quality. This analysis should include a discussion of the trade-offs between compression rate and reconstruction quality and should provide a justification for the choice of the decoder used in the experiments.

### Questions

- How does the proposed framework compare to other state-of-the-art image compression methods, such as BPG and VVC, in terms of rate-distortion performance and computational cost?
- How does the proposed framework perform on other datasets, such as the DIV2K dataset?
- How does the proposed framework handle images with complex textures or structures?

### Rating

6

### Confidence

3

**********
