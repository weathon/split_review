### Summary

This paper proposes a real-time video enhancement network called Recurrent Bottleneck Mixer Network (ReBotNet). The main contributions are as follows:
1. A new network architecture that combines tubelet and image tokens for spatio-temporal feature extraction.
2. A recurrent training setup that leverages the previous prediction as an additional input to improve temporal consistency.
3. Two new datasets, PortraitVideo and FullVideo, for video enhancement evaluation.
4. Experimental results show that ReBotNet outperforms previous methods with lower computational cost and faster inference time.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The experiments are comprehensive, including both quantitative and qualitative results.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation for the proposed method is not clearly explained. The authors claim that most existing methods focus on single degradation types, while real-world videos often suffer from multiple degradations. However, the paper does not provide specific examples or evidence to support this claim. It is unclear how the proposed method addresses the issue of multiple degradations, and whether it is designed to handle such cases. The paper should provide a more detailed analysis of the types of degradations encountered in real-world videos and how the proposed method is specifically designed to handle them.
2. The datasets used in the experiments are not well-explained. The authors mention that the datasets contain videos with multiple degradations, but they do not provide details about the types of degradations, their distribution, and the difficulty level of the datasets. The paper should include a more detailed description of the datasets, including the number of videos, the average length of the videos, and the specific types of degradations present. It is also important to clarify how the datasets were collected and whether they are representative of real-world scenarios.
3. The paper lacks a thorough analysis of the proposed method's performance under different conditions. For example, the authors should investigate how the method performs with varying levels of noise, different types of blur, and different types of compression artifacts. The paper should also analyze the method's performance on videos with different content, such as videos with fast motion, slow motion, and videos with complex scenes. It is important to understand the limitations of the proposed method and the conditions under which it performs well or poorly.

### Suggestions

The paper needs to provide a more detailed explanation of the motivation behind the proposed method. The authors should provide specific examples of real-world videos that contain multiple degradations and explain why existing methods are not suitable for handling these cases. For example, they could show examples of videos with simultaneous blur and noise, or videos with motion blur and compression artifacts. The paper should also discuss the limitations of existing methods in handling these types of degradations and how the proposed method addresses these limitations. The authors should also clarify whether the proposed method is designed to handle specific types of degradations or if it is designed to be robust to a wide range of degradations. A more detailed analysis of the types of degradations encountered in real-world videos is needed to justify the design choices of the proposed method.

The paper should provide a more detailed description of the datasets used in the experiments. The authors should include a table that summarizes the key characteristics of the datasets, such as the number of videos, the average length of the videos, the types of degradations present, and the difficulty level of the datasets. The paper should also clarify how the datasets were collected and whether they are representative of real-world scenarios. For example, the authors could describe the source of the videos, the methods used to introduce degradations, and the criteria used to select the videos. The paper should also discuss the potential biases in the datasets and how these biases might affect the results. A more detailed description of the datasets is essential for the reproducibility and validity of the experimental results.

The paper needs to include a more thorough analysis of the proposed method's performance under different conditions. The authors should investigate how the method performs with varying levels of noise, different types of blur, and different types of compression artifacts. The paper should also analyze the method's performance on videos with different content, such as videos with fast motion, slow motion, and videos with complex scenes. The authors should also discuss the limitations of the proposed method and the conditions under which it performs well or poorly. For example, they could analyze the performance of the method on videos with extreme motion or videos with very high levels of noise. The paper should also discuss the computational cost of the proposed method and how it compares to existing methods. A more thorough analysis of the method's performance under different conditions is essential for understanding its strengths and weaknesses and for identifying areas for future improvement.

### Questions

1. How does the proposed method handle videos with multiple types of degradations?
2. What are the specific characteristics of the PortraitVideo and FullVideo datasets, and how do they differ from existing datasets?
3. How does the proposed method perform under different conditions, such as varying levels of noise, blur, and compression artifacts?

### Rating

5

### Confidence

4

**********
