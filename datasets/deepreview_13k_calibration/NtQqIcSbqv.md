# Learning to Jointly Understand Visual and Tactile Signals

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Modeling and analyzing object and shape has been well studied in the past. However, manipulation of these complex tools and articulated objects remains difficult for autonomous agents. Our human hands, however, are dexterous and adaptive. We can easily adapt a manipulation skill on one object to all objects in the class and to other similar classes. Our intuition comes from that there is a close connection between manipulations and topology and articulation of objects. The possible articulation of objects indicates the types of manipulation necessary to operate the object. In this work, we aim to take a manipulation perspective to understand everyday objects and tools. We collect a multi-modal visual-tactile dataset that contains paired full-hand force pressure maps and manipulation videos. We also propose a novel method to learn a cross-modal latent manifold that allow for cross-modal prediction and discovery of latent structure in different data modalities. We conduct extensive experiments to demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors have curated a unique visual-tactile dataset and introduced a manifold algorithm to explore the cross-modal relationship between objects and their manipulation. By visualizing the cross-modal latent structures, they showcase that their approach outperforms current methods and effectively generalizes manipulations to unfamiliar objects.

### Strengths
1. The paper is articulately written, offering clarity and ease of comprehension, making it accessible even to readers unfamiliar with the subject matter.
2. A significant contribution of this research is the introduction of a novel visual-tactile dataset, especially noteworthy given the limited datasets available in this domain.
3. The innovative manifold learning approach presented has the potential to pave the way for subsequent research.
4. Through experiments, the paper effectively showcases the promise of the cross-modal retrieval, prediction, and the latent structure. Compared to existing methodologies, the proposed approach holds considerable promise.

### Weaknesses
1. The dataset would benefit from enhanced visualization and in-depth details, possibly within the appendix. Specifically, it would be useful to see a more detailed breakdown of the types of objects used, the range of manipulations performed, and the specific sensor data captured. For instance, providing histograms of the force magnitudes, or visual examples of the tactile sensor readings across different manipulation phases, would greatly aid in understanding the dataset's characteristics and potential biases.

2. There's a typographical error on page 5 after equation 2; "Additioanlly" should be corrected to "Additionally."

3. Based on observations from figures 3 and 4, the sequences appear to have minimal variation across different frames. Displaying greater variation would add value. It is unclear if this is a limitation of the dataset or the visualization. Additionally, considering a baseline that utilizes only the initial frame, as opposed to the entire sequence data, could provide intriguing insights. This comparison could highlight the importance of temporal information captured in the sequence data, and how much the manifold learning approach is actually benefiting from the sequence as opposed to a single snapshot.

### Questions
Please see the weakness above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper purposed a force maps and RGB paird visual-tactile dataset. And further purpose to first represent each signal in a shared latent space, and then project the global manifold to local submanifold for each signal for reconstruction. The results demonstrate the effectiveness of purposed method.

### Strengths
1. This paper tactles a more challenging visual-tactile prediction task which is harder compare to previous works.
2. The design of preoject global manifold to local submanifold force the model to capture different signals, and to futher incorporate with the test time optimization method to improve the prediction results.
3. The experiments are comprehensive.The TSNE results also show the model learned with some semantic meaningful infomation.

### Weaknesses
1. My major concern is since the training set : testing set is aroud 12:1, and only include 4 categoreis, can this method really generalize to unseen objects? How is the diversity of the training and testing set?
2. Presentation with Figure1: It would be better to also draw the process of getting shared latent space in the Figure1 for better understanding, it's quiet hard to undertand how to get a shared latent space from signals that are different dimension, could the author illustrate more about this ? Also projection layer of x seems missing in Figure 1.

3. If as the author statement, force maps and RGB id many-to-many mapping, what is the advantage of using force maps as tactile signal?  Why different object will not have similar surface texture property? And the challenge of disparity in spatial scale of different signals seems also exist even if it is one-one mapping?
4. How is the robustness of the tactile glove, will it need to calibrate a lot to make sure the tactile data is accurate?
5. How long will it take for test time optimization? Since this might be important for robotic application?

### Questions
1. If as the author statement, force maps and RGB id many-to-many mapping, what is the advantage of using force maps as tactile signal?  Why different object will not have similar surface texture property? And the challenge of disparity in spatial scale of different signals seems also exist even if it is one-one mapping?
2. How is the robustness of the tactile glove, will it need to calibrate a lot to make sure the tactile data is accurate?
3. How long will it take for test time optimization? Since this might be important for robotic application?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on understanding everyday objects and tools from a manipulation standpoint. The authors have constructed a multi-modal visual-tactile dataset, consisting of paired full-hand force pressure maps and manipulation videos. Additionally, they introduce a unique method to learn a cross-modal latent manifold. This manifold facilitates cross-modal prediction and uncovers latent structures in various data modalities. The extensive experiments establish the efficacy of the proposed approach approach.

### Strengths
1. This paper tackles a common issue, manifold learning, through a pragmatic lens within robotics applications. The study aims to address multi-modal learning problems in the visual-tactile sensory observation context, a highly practical setup for manipulation tasks. The proposed representation learning method can be beneficial for a multitude of downstream applications within visuotactile learning in robotics.

2. The method proposed in the paper is straightforward, suggesting that it does not place a heavy computational load on the system.

3. The authors have gathered a substantial paired dataset for visual and tactile signals. If made publicly accessible, this dataset could prove to be a valuable resource for further research.

### Weaknesses
1. The method operates under the assumption that the sum of shape and tactile information equates to visual information. This assumption is manifested in the authors' approach of creating video latents by combining the latents of manipulation and the latents of canonical shapes. However, the tactile sequence may also encapsulate the object's geometric information. As suggested in the referenced paper 'Learning human–environment interactions using conformal tactile textiles,' tactile information can be employed to classify object geometry. Consequently, it's worth questioning the efficacy of combining shape and tactile embeddings to produce the video embedding. Specifically, the method seems to assume that the visual appearance of an object is a simple linear combination of its shape and tactile properties, which is a strong assumption. The tactile data, while not directly encoding color, can provide rich information about surface curvature and texture, which are crucial for visual perception. The method does not explicitly account for the complex, non-linear relationships between these modalities.

2. The cross-modality query necessitates an optimization process. Therefore, it's crucial to provide information regarding the time cost of these experiments. For instance, how much time would be required to employ the neural field in this inverse manner? The paper lacks a discussion on the computational overhead of the optimization process, which is essential for practical applications. The time required for this optimization could be a significant bottleneck, especially if the method is to be used in real-time robotic manipulation scenarios. Without this information, it is difficult to assess the practicality of the proposed approach.

3. The absence of videos in the paper is a notable limitation. Including video content could significantly enhance the understanding of the tasks and experiments conducted in the study. The lack of visual examples makes it difficult to fully grasp the nuances of the manipulation tasks and the quality of the generated video sequences. The reader is left to imagine the results, which could lead to misinterpretations of the method's capabilities and limitations.

### Questions
1. Do you want to claim the dataset as one of the contribution? In another word, would you open source the dataset once the paper is accepted?

2. Could you clarify the symbol $\gamma$ used in Equation 2? I was unable to locate a definition for it within the text.

3. Your elaboration on $I_i$ and $I_j$ would be appreciated, specifically in relation to the following sentence. How is the distance within the space of $I$ quantified, and how is the subtraction operation defined in Eq3 for $I_i$ and $I_j$, given that $I$ is a three-modality tuple? While I recognize that the manifold isometry loss is a standard loss in the manifold learning field, I would like to confirm if the subtraction operation is a simple reduction operation in the raw data format.
> any two samples sampled from the signal agnostic manifold $\{z_i, z_j \} ⊆ M$ respects the distance between the samples $I_i, I_j$ 

Minor issues:
1. There appears to be a typographical error in the first line of the 'Dataset: Data Collection Setup' section – the citation parentheses are empty.
2. It would enhance clarity if Figure 1 was referenced in Section 4.2 and if further details about the components in the figure were provided. This issue is also applicable to Figure 2.
3. Please use last names when citing authors. For instance, it should be 'Chen et al.' instead of 'Peter et al.'.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of learning representations for modeling visual and tactile sensor data. A large multi-modal visual-tactile dataset is presented, and a straightforward pipeline is proposed for learning the data. Experiments are performed on cross-modal prediction tasks to validate the idea.

### Strengths
The paper introduces a substantial dataset comprising paired visual and tactile sensor data, which holds the potential for significant advancements in cross-modal research; 

The paper's organization is clear and easy to follow.

### Weaknesses
The proposed approach has been exclusively assessed in the context of cross-modal prediction tasks, with no concrete verification of its applicability in downstream manipulation tasks; 

Moreover, it is worth noting that a single video observation could potentially correspond to a wide range of tactile signals, such as variations in the force applied when touching dough. Regrettably, the study does not appear to account for the inherent multimodality in the distribution of data in this respect; 

The paper lacks technical details, e.g., the learning rate, batch size, etc. 

The video prediction results for new instances and new categories seem not promising.

### Questions
Providing additional technical details would enhance the reproducibility of the work, e.g., model architecture, training details, etc. 

It would be interesting to see how the learned representations can be applied to downstream manipulation tasks, adding such results would further strengthen the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
