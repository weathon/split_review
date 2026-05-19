### Summary

This paper proposes a large reconstruction model that predicts a triplane representation of a scene from a single image. The model is trained on a large amount of data, including synthetic data from Objaverse and real-world data from MVImgNet. The model is capable of reconstructing 3D objects from single images in real-time.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is capable of reconstructing 3D objects from single images in real-time. 
2. The proposed method is trained on a large amount of data, including synthetic data from Objaverse and real-world data from MVImgNet.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is trained on a large amount of data, including synthetic data from Objaverse and real-world data from MVImgNet. However, the paper does not provide a detailed analysis of the impact of the size and diversity of the training data on the performance of the model. Specifically, it is unclear how the model would perform with less diverse or smaller datasets. The paper lacks ablation studies that systematically vary the size and diversity of the training data to quantify their influence on reconstruction quality and generalization capabilities. This makes it difficult to assess the robustness of the method and its potential for deployment in resource-constrained environments.
2. The paper does not provide a detailed analysis of the computational resources required to train and deploy the model. This includes the amount of memory and processing power needed, as well as the training time. The paper should include a breakdown of the computational cost associated with each stage of the pipeline, such as the image encoder, the triplane decoder, and the NeRF rendering. This information is crucial for understanding the practical feasibility of the method and for comparing it with other approaches.

### Suggestions

The paper would benefit significantly from a more thorough investigation into the impact of training data size and diversity on the model's performance. The authors should conduct ablation studies where they systematically vary the size and diversity of the training data, for example, by using subsets of Objaverse or by introducing synthetic noise to the MVImgNet data. This would allow them to quantify the relationship between training data characteristics and reconstruction quality. Furthermore, it would be valuable to analyze the model's performance on objects not present in the training data to assess its generalization capabilities. Such analysis would provide a more comprehensive understanding of the model's strengths and limitations and would help to identify potential areas for improvement. The authors should also consider exploring techniques such as data augmentation to increase the diversity of the training data and improve the model's robustness.

In addition to the data analysis, the paper needs a more detailed discussion of the computational resources required for training and deployment. The authors should provide a breakdown of the computational cost associated with each stage of the pipeline, including the image encoder, the triplane decoder, and the NeRF rendering. This should include the number of parameters, the memory footprint, and the training time for different model sizes and datasets. It would also be beneficial to compare the computational cost of the proposed method with other state-of-the-art approaches. This information is crucial for assessing the practical feasibility of the method and for understanding its scalability. The authors should also discuss the hardware requirements for training and deployment, such as the type of GPU and the amount of RAM needed. This would help potential users to determine if the method is suitable for their specific use cases.

Finally, the paper should include a more detailed analysis of the limitations of the proposed method. This should include a discussion of the types of objects that the model struggles to reconstruct, as well as the limitations of the triplane representation for complex scenes. The authors should also discuss the potential for bias in the training data and how this might affect the model's performance. A thorough discussion of the limitations would provide a more balanced view of the method and would help to guide future research in this area. It would also be beneficial to explore the use of alternative representations, such as signed distance functions or occupancy fields, to see if they offer any advantages over the triplane representation.

### Questions

1. How does the size and diversity of the training data affect the performance of the model? 
2. What are the computational resources required to train and deploy the model?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
