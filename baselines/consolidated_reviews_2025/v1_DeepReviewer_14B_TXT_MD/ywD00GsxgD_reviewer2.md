### Summary

The authors present a method for generating synthetic liver tumours which can be used for training and validation. The authors show that using the synthetic data for validation results in better models than using real data for validation.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well written and the results are interesting. The authors present an interesting method for generating synthetic liver tumours which appears to produce realistic results. The authors make good use of available data, and the experiments are well designed. The results are important, and show that using synthetic data for validation can result in better models than using real data for validation.

### Weaknesses

#### Some Related Works


#### comment

The paper is a little light on technical details. For example, the authors mention that they use a post-processing step to replicate mass effects. However, they do not explain how this is done. Specifically, the description lacks details on the mathematical formulation or algorithmic implementation of this post-processing. It is unclear what specific image transformations are applied, how the parameters of these transformations are determined, and how the 'realism' of the mass effect is quantified or evaluated. This lack of detail makes it difficult to reproduce the results and assess the validity of the approach. Furthermore, while the paper mentions using healthy liver CT scans from the BTCV dataset for synthetic tumor generation, it does not specify how many scans were used or how they were selected. This lack of clarity makes it difficult to assess the diversity and representativeness of the synthetic data.

### Suggestions

To improve the paper, the authors should provide a more detailed explanation of the post-processing step used to simulate mass effects. This should include a clear description of the mathematical operations performed on the images, the parameters used, and the rationale behind their selection. For example, if local scaling warping is used, the authors should specify the scaling factors, the spatial distribution of these factors, and how they are related to the size and location of the synthetic tumor. If edge detection algorithms are used, the specific algorithms and their parameters should be described. Furthermore, the authors should explain how the realism of the mass effect is evaluated, whether through visual inspection by medical experts or using quantitative metrics. Including a visual example of the post-processing step, showing the tumor before and after the mass effect simulation, would also be beneficial. This level of detail is crucial for reproducibility and for the community to understand the strengths and limitations of the proposed method. 

Additionally, the authors should provide more details on the healthy liver CT scans used for synthetic tumor generation. This should include the exact number of scans used, the selection criteria, and any preprocessing steps applied to these scans before tumor generation. If the scans were selected from the BTCV dataset, the authors should specify which subsets were used and why. It would also be helpful to describe the diversity of the healthy liver scans in terms of anatomical variability, image quality, and other relevant factors. This information is important to assess the generalizability of the synthetic data and the robustness of the models trained using this data. The authors should also clarify if any data augmentation techniques were applied to the healthy liver scans before generating synthetic tumors. 

Finally, the authors should consider including a more detailed analysis of the impact of different synthetic tumor characteristics on model performance. For example, how does the size, shape, and location of the synthetic tumors affect the model's ability to detect real tumors? This analysis would provide valuable insights into the effectiveness of the synthetic data generation method and help to identify potential areas for improvement. The authors could also explore the use of more sophisticated tumor generation techniques, such as generative adversarial networks (GANs), to create more realistic and diverse synthetic tumors. This would further enhance the value of the proposed method and its potential impact on the field.

### Questions

Please see weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
