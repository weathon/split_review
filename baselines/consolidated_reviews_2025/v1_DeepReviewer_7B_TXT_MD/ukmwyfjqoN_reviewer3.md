### Summary

This paper proposes a recurrent video enhancement network, ReBotNet, which can be used for real-time video enhancement. The proposed method is evaluated on two new datasets, PortraitVideo and FullVideo, which contain videos with various degradations. The experimental results show that the proposed method achieves better performance than existing methods in terms of both quantitative and qualitative metrics.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to understand.
2. The experiments are comprehensive, including both quantitative and qualitative results.
3. The proposed method achieves better performance than existing methods in terms of both quantitative and qualitative metrics.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation for the proposed method is not clearly explained. The authors claim that most existing methods focus on single degradation types, while real-world videos often suffer from multiple degradations. However, the paper does not provide specific examples or evidence to support this claim. It is unclear how the proposed method addresses the issue of multiple degradations, and whether it is designed to handle such cases. The paper should clarify whether the method is intended to handle specific types of multiple degradations or if it aims for a more general solution. Furthermore, the paper lacks a discussion on how the proposed architecture is specifically tailored to handle multiple degradations, as opposed to single ones.
2. The datasets used in the experiments are not well-explained. The authors mention that the datasets contain videos with multiple degradations, but they do not provide details about the types of degradations, their distribution, and the difficulty level of the datasets. The paper should include a more detailed description of the datasets, including the number of videos, the average length of the videos, and the specific types of degradations present. It is also important to clarify how the datasets were collected and whether they are representative of real-world scenarios. The paper should also discuss the potential biases in the datasets and how these biases might affect the results.
3. The paper lacks a thorough analysis of the proposed method's performance under different conditions. For example, the authors should investigate how the method performs with varying levels of noise, different types of blur, and different types of compression artifacts. The paper should also analyze the method's performance on videos with different content, such as videos with fast motion, slow motion, and videos with complex scenes. It is important to understand the limitations of the proposed method and the conditions under which it performs well or poorly. The paper should also discuss the computational cost of the proposed method and how it compares to existing methods. A more detailed analysis of the method's performance under different conditions is essential for understanding its strengths and weaknesses and for identifying areas for future improvement.

### Suggestions

The paper would benefit from a more detailed explanation of the motivation behind the proposed method. Specifically, the authors should provide concrete examples of real-world scenarios where videos suffer from multiple degradations simultaneously. For instance, they could describe a situation where a video captured in low light also experiences motion blur due to camera shake, or a video taken with a phone camera is affected by both compression artifacts and noise. This would help to justify the need for a method that can handle multiple degradations simultaneously. Furthermore, the authors should clarify whether the proposed method is designed to handle specific types of multiple degradations or if it aims for a more general solution. If the method is intended to handle specific types of degradations, the authors should clearly define these types and explain how the proposed architecture is tailored to address them. If the method is intended for a more general solution, the authors should discuss the limitations of the method and the types of degradations it might not be able to handle effectively. This would provide a more comprehensive understanding of the method's capabilities and limitations.

To address the lack of clarity regarding the datasets, the authors should provide a more detailed description of the datasets used in the experiments. This should include the number of videos, the average length of the videos, the types of degradations present, and the difficulty level of the datasets. The authors should also clarify how the datasets were collected and whether they are representative of real-world scenarios. For example, they could describe the source of the videos, the methods used to introduce degradations, and the criteria used to select the videos. The paper should also discuss the potential biases in the datasets and how these biases might affect the results. This would help to ensure that the results are generalizable to real-world scenarios. Furthermore, the authors should consider providing a more detailed analysis of the datasets, including the distribution of different types of degradations and the difficulty level of the videos. This would help to better understand the characteristics of the datasets and the challenges they pose.

Finally, the paper should include a more thorough analysis of the proposed method's performance under different conditions. This should include an investigation of how the method performs with varying levels of noise, different types of blur, and different types of compression artifacts. The authors should also analyze the method's performance on videos with different content, such as videos with fast motion, slow motion, and videos with complex scenes. This would help to understand the limitations of the proposed method and the conditions under which it performs well or poorly. The paper should also discuss the computational cost of the proposed method and how it compares to existing methods. A more detailed analysis of the method's performance under different conditions is essential for understanding its strengths and weaknesses and for identifying areas for future improvement. The authors should also consider including a discussion of the limitations of the proposed method and potential avenues for future research.

### Questions

Please refer to the weakness part.

### Rating

5

### Confidence

3

**********
