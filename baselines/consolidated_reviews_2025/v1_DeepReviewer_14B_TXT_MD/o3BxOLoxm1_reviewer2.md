### Summary

This paper proposes a training-free conditional generation framework that leverages pretrained diffusion models and off-the-shelf neural networks with minimal additional inference cost for a broad range of tasks. Specifically, they leverage the manifold hypothesis to refine the guided diffusion steps and introduce a shortcut algorithm in the process. The experiments show that MPGD is efficient and effective for solving a variety of conditional generation applications in low-compute settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to follow.
2. The proposed method is well-motivated and sound.
3. The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The qualitative results in Figure 6 seem to indicate that MPGD-LDM does not effectively learn the style features. In rows 1, 3, and 5 of Figure 6, the generated images appear to be in color, yet the reference style images are in black and white. Additionally, the generated images do not exhibit distinct style features that align with the reference style images.
2. The authors should include a discussion of the limitations of the proposed method in the main paper.
3. The authors should provide a more detailed explanation of the evaluation metrics used in the experiments. For example, what does the FaceID metric measure, and what are its strengths and limitations? Additionally, the authors should provide a more detailed analysis of the experimental results, including a discussion of the statistical significance of the results and a comparison to the performance of other state-of-the-art methods.

### Suggestions

The paper would benefit from a more thorough investigation into the style transfer capabilities of MPGD-LDM. While the quantitative results may show improvement over baselines, the qualitative results in Figure 6 raise concerns about the fidelity of style transfer. Specifically, the generated images often fail to capture the nuances of the reference style, such as texture, brush strokes, and color palettes. To address this, the authors could consider incorporating a more robust style loss function that explicitly penalizes deviations from the reference style. For example, they could explore using a perceptual loss based on deep feature differences, which has been shown to be effective in style transfer tasks. Furthermore, the authors should provide a more detailed analysis of the generated images, including a discussion of the types of styles that MPGD-LDM struggles with and the potential reasons for these failures. This would provide a more nuanced understanding of the method's strengths and weaknesses.

In addition to a more detailed discussion of the evaluation metrics, the authors should also provide a more rigorous analysis of the experimental results. For example, they should report confidence intervals or standard deviations for the quantitative metrics, which would allow for a more robust assessment of the statistical significance of the results. Furthermore, the authors should compare the performance of MPGD-LDM to other state-of-the-art methods on a wider range of datasets and tasks. This would provide a more comprehensive evaluation of the method's generalizability and its potential for real-world applications. The authors should also consider including a user study to assess the perceptual quality of the generated images, as quantitative metrics may not always correlate with human perception. This would provide a more holistic evaluation of the method's performance.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method. For example, they should discuss the computational cost of MPGD-LDM, its sensitivity to hyperparameter settings, and its potential for generating artifacts or unrealistic images. They should also discuss the potential for bias in the training data and its impact on the generated images. This would provide a more balanced and nuanced perspective on the method's capabilities and limitations. Furthermore, the authors should discuss the potential for future work, such as exploring the use of different diffusion models or incorporating additional constraints into the generation process. This would provide a roadmap for future research in this area.

### Questions

Please refer to the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
