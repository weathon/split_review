# Efficient Multi Subject Visual Reconstruction from fMRI Using Aligned Representations

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Reconstructing visual images from fMRI data presents a challenging task, particularly when dealing with limited data and compute availability. This work introduces a novel approach to fMRI-based visual image reconstruction using a subject-agnostic common representation space. We show that subjects' brain signals naturally align in this common space during training, without the need for explicit alignment. This is leveraged to demonstrate that aligning subject-specific adapters to a reference subject is significantly more efficient than traditional end-to-end training methods. Our approach excels in low-data scenarios, where training the adapter with limited data achieves faster and better performance. We also introduce a novel method to select the most representative subset of images for a new subject, allowing for fine-tuning with 40\% less data while maintaining performance. These advancements make fMRI data collection more efficient and practical, reducing the burden on subjects and improving the generalization of fMRI reconstruction models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper achieves cross-subject brain visual decoding by training subject-specific adapters on subject-shared visual stimuli. To reduce the reliance on data, the authors propose a greedy selection algorithm to pick the more important data for cross-subject transfer. Experimental results show that the proposed method achieves results slightly, compared to normal fine-tuning.

### Strengths
+ In this paper, the rationalization of the shared visual representation space proposed by MindEye2 is slightly explained from a neuroscience perspective.
+ This paper explores the interpretability of the proposed method.

### Weaknesses
 + This proposed alignment strategy relies on visual stimuli shared by multiple subjects, however this assumption is often difficult to realize in real scenarios, i.e., the images in the fMRI-image pairs used to train the model are hardly shared across subjects. This severely limits the usability of the method. In almost all papers that use NSD for visual decoding [1-4], the visual stimuli of different subjects do not overlap in the training set, which is a more accepted setting. The method's reliance on shared stimuli for alignment severely restricts its practical application in scenarios where such overlap is not readily available, limiting its generalizability to standard datasets.
+ The innovations in this paper are limited. Compared to MindEye2 [2], the only difference is simply the addition of a training phase for MindEye2's ridge regression supervised with MSE loss, and the results achieved are less than impressive. The core contribution appears to be a relatively minor modification to an existing method, and the performance gains are not substantial enough to justify the added complexity. The method does not present a significant advancement over existing techniques, and the marginal improvements do not warrant the additional computational overhead.

### Questions
+ According to MindEye2's settings, the shared images are used for testing rather than training. If the authors used these shared images to train the alignment, how was the test set constituted?
+ Figure 5(b) states that good results can already be reconstructed at 0 epochs (i.e., no cross-subject training); is this a typo.?
+ Table 3 has shown that using more training data leads to better model performance, while Figure 7(a) shows that the proposed data selection algorithm is able to obtain better results using less data. This brings up the trade-off question, is it better to train with more data? Or is it better to use the proposed selection algorithm? The authors do not clarify this question in this paper.
+ Insufficient validation on the effectiveness of data selection algorithms. The authors only considered fewer evaluation metrics, used only 1 session of data for the experiment, and did not report the error of the experiment with different random number seeds. The authors should take richer experiments to prove the effectiveness of the method.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper tackles the problem of reconstructing visual images from fMRI signals. Based on prior work that has shown that fMRI signals can be embedded in a common space, where similar behavior and image semantics are represented along separate dimensions after a singular value decomposition. 

In this paper, the authors claim that instead of training on a large number of subjects, one can train on just a single subject to construct a representation space, where other subjects are automatically aligned. While the introduction motivates the problem and the background literature is adequately represented, there are no technical details about the method.

### Strengths
The experimental results are superior compared to other methods. However, see weaknesses.

### Weaknesses
Details of the method are completely missing from the paper. Thus it was difficult to determine what was the contribution of the paper.

Several concepts are mentioned and introduced, but no technical details are provided.

It seems the adapter network is an encoder-decoder architecture. However, details are missing.

The greedy image selection algorithm is not described anywhere.

The authors mention, "Recent works have achieved impressive results by mapping fMRI data to latent diffusion model (LDM) spaces (Takagi & Nishimoto, 2023; Scotti et al., 2023; Lu et al., 2023; Xia et al., 2024), while simultaneously integrating multiple modalities. Despite this progress, these methods have not been thoroughly tested for their generalization performance across a larger population of subjects." However, in this paper, it doesn't seem that they have overcome this challenge.

The method is tested on a limited set of subjects. In such runs, the authors show a superior performance. However, it is not clear if it will generalize to new data.

### Questions
What is an adapter? It is not defined anywhere.


The non-linear adapter is not described. What does it mean? 

How is the network trained? Does it minimize the reconstruction loss? 


Will the method first require an extended fMRI scan (> few hours) to train the initial subject?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the author addresses the challenge of reconstructing visual images from fMRI data, particularly with limited data and computer resources. In the paper, they introduce a shared representation space to align brain patterns from different people, allowing a single model to work across multiple individuals. The key innovations of this paper include Adapter Alignment (AA) for aligning fMRI data across subjects and a greedy algorithm for selecting optimal images, reducing training time and data by 40% while maintaining quality.

### Strengths
First, the authors introduce a novel approach for aligning subject-specific fMRI signals to a common visual representation space through Adapter Alignment (AA). This method efficiently manages multi-subject fMRI reconstruction by pre-training on a reference subject and using lightweight adapters to align new subjects, eliminating the need for end-to-end training for each individual.

Second, the authors provide compelling evidence for the existence of a shared visual representation space. They show that brain signals naturally align within this common space during training, even without explicit alignment mechanisms. This discovery is significant as it sheds light on how visual information is consistently represented across different human brains.

Moreover, the authors present a novel data selection strategy using a greedy algorithm to identify representative images. If effective, this strategy could substantially reduce data collection demands, which is particularly valuable in neuroscience research where fMRI acquisition is costly and resource-intensive. Impressively, this approach achieves a 40% reduction in required training data while maintaining performance.

### Weaknesses
The reviewers have several concerns regarding this work:

1). Limited Subjects and Datasets: The authors aim to reconstruct visual images from fMRI using the proposed method; however, they only utilized data from a few subjects (e.g., a total of 4) within the NSD dataset. Additionally, only a single dataset is involved in this work. This limitation in subjects and datasets can impair the generalizability of the proposed framework and restrict its broader applicability. The reviewers suggest incorporating additional task-based fMRI data, such as from the HCP dataset, to reconstruct diverse cognitive activities like language and emotional responses. The lack of diversity in both the number of subjects and the type of fMRI data (e.g., only natural image viewing) makes it difficult to assess the robustness of the method across different populations and cognitive tasks. The exclusive use of the NSD dataset, while large, limits the assessment of the method's ability to generalize to other datasets with different acquisition parameters and experimental designs.

2). Potential Overfitting: The Adapter Alignment (AA) method may be prone to overfitting due to the limited training subjects and images. The limited shared images may not provide a comprehensive representation across diverse datasets, and the authors do not discuss strategies to mitigate overfitting in training. The reliance on a small set of shared images for adapter alignment could lead to the model memorizing these specific images rather than learning generalizable features. Furthermore, the absence of explicit regularization techniques or validation strategies to monitor overfitting during training raises concerns about the reliability of the results, especially when applied to unseen data or new subjects.

3). Details on AA. In this work, several critical aspects of AA, such as the selection of a reference subject, bin size for image selection, and potential configurations for non-linear adapters, are not clearly addressed. A more in-depth discussion on these points could help enhance and demonstrate the advancement of AA. The lack of clarity on how the reference subject is chosen introduces a potential source of bias, as the choice of reference could significantly impact the alignment process. The adaptive binning strategy, while mentioned, lacks sufficient detail on how the bin sizes are dynamically adjusted based on the singular values, making it difficult to reproduce or evaluate the method. Additionally, the choice of a single linear layer with a GELU non-linearity for the adapter, without exploring other non-linear configurations, limits the potential of the method to capture more complex relationships between subjects' fMRI data.

4). Details on Greedy Heuristic Search: The authors employ a greedy heuristic algorithm for selecting image subsets; however, the methodology lacks sufficient detail. For instance, the authors state, “a greedy heuristic such as given below achieves an (1 − 1/e) approximation ratio.” Reviewers would like clarification on whether this approximation ratio was proven by the authors or referenced from existing literature. The description of the greedy heuristic algorithm lacks sufficient detail to understand its implementation and computational complexity. The absence of a formal proof or citation for the claimed approximation ratio raises concerns about the theoretical validity of the algorithm. Furthermore, the computational cost of the greedy search, which is often time-intensive, is not discussed, making it difficult to assess the practical feasibility of the approach.

### Questions
The primary concern remains the limited number of subjects and datasets used in this work, despite the originality of the proposed idea. The reviewers have several questions related to specific weaknesses:

1). Training Times and Computational Requirements: The proposed method reportedly achieves similar performance at epoch 1 compared to traditional methods at epoch 160. Could the authors provide specific training time consumption and computational requirements for both approaches, particularly for the first epoch, which seems critical for comparison?

2). Greedy Heuristic Algorithm for Image Selection: The authors mention that the greedy algorithm for image selection achieves a $(1 - 1/e)$ approximation ratio; however, this is neither proven nor cited in the paper. Reviewers request a formal proof of this approximation ratio or a reference citation. Additionally, the authors should report the time consumption for the greedy heuristic search, as heuristic search algorithms are often time-intensive.

3). Scalability of Adapter Alignment (AA): How would the AA method handle scaling in high-data or high-subject scenarios, where alignment and computational demands would likely increase? Reviewers recommend that the authors provide more details on the scalability of AA.

4). 40-Dimension Threshold in Table 5: In Table 5, the method demonstrates notable performance when using 40 singular values, particularly in high-level metrics. Could the authors clarify whether this 40-dimensional threshold aligns with existing findings on the dimensionality of visual representations in the brain? Additionally, how does this threshold vary across different subjects?

### Soundness
3

### Presentation
3

### Contribution
3
