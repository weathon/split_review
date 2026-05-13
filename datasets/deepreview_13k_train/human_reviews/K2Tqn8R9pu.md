# Gaussian Differentially Private Human Faces Under a Face Radial Curve Representation

- Decision: Accept
- Scores: 6, 3, 6

## Abstract
In this paper we consider the problem of releasing a Gaussian Differentially Private (GDP) 3D human face. The human face is a complex structure with many features and inherently tied to one's identity.  Protecting this data, in a formally private way, is important yet challenging given the dimensionality of the problem. We extend approximate DP techniques for functional data to the GDP framework. We further propose a novel representation, face radial curves, of a 3D face as a set of functions and then utilize our proposed GDP functional data mechanism. 
    To preserve the shape of the face while injecting noise we rely on tools from shape analysis for our novel representation of the face.
    We show that our method preserves the shape of the average face and injects less noise than traditional methods for the same privacy budget. Our mechanism consists of two primary components, the first is generally applicable to function value summaries (as are commonly found in nonparametric statistics or functional data analysis) while the second is general to disk-like surfaces and hence more applicable than just to human faces.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a method for creating Gaussian Differentially Private (GDP) representations of 3D human faces using a novel face radial curve representation. The proposed approach aims to address privacy concerns associated with sharing 3D facial data by employing differential privacy (DP) mechanisms. This method leverages statistical shape analysis to represent faces in a disk-parameterized structure, ensuring minimal noise addition while preserving the facial structure. The approach is specifically designed for applications that involve facial data but could extend to other disk-like surface data. The paper also presents experimental results demonstrating that the method injects less noise compared to point-wise differential privacy approaches while effectively preserving facial features.

### Strengths
1. The paper presents a novel approach to 3D face representation for privacy preservation using face radial curves, which is innovative and highly relevant to privacy concerns in biometric data.

2. The GDP mechanism integrated into this method ensures that facial features are preserved with minimal noise injection, enhancing privacy while maintaining utility.

3. The manuscript includes thorough experiments comparing the proposed method with traditional point-wise differential privacy techniques, demonstrating superior noise reduction and structure preservation.

### Weaknesses
1. **Manuscript Organization**: The paper would benefit from a more structured organization aligned with the standard conference paper layout in AI. The current structure is challenging to follow, and the clarity could be enhanced by including diagrams that illustrate the overall pipeline of the proposed method. Guiding sentences that introduce and connect sections and paragraphs would also help readers navigate the content more effectively.

2. **Assumptions on Data Structure**: The proposed approach assumes a genus-0 surface with no missing data points, which may not be realistic in practical settings. This limitation necessitates additional pre-processing for noisy or incomplete data. Expanding the discussion on how the method could handle such cases would improve its practical applicability. Specifically, the method does not address how the radial curves are handled when there are occlusions or self-intersections in the 3D face data, which are common in real-world scans.

3. **Limited Dataset and Generalizability**: The evaluation is conducted on a limited dataset without a detailed description of its statistics, raising concerns about the method’s generalizability. While the authors suggest that this approach could extend to applications such as terrain models, no experiments support this claim. More comprehensive testing, including diverse or noisy datasets, is recommended to validate the method’s broader applicability. The lack of information about the dataset's size, variability in pose, expression, and lighting conditions further limits the ability to assess the robustness of the proposed method.

4. **Computational Efficiency and Benchmarking**: Although the algorithm's methodology is well-described, the computational cost is not evaluated, which limits the ability to assess its practical performance. Additionally, the benchmark methods used for comparison are not clearly described, which could be clarified to provide a more comprehensive context for evaluating the proposed approach. It is unclear if the benchmark method is a naive application of differential privacy or if it is optimized for the specific task, which makes it difficult to assess the true advantage of the proposed method.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes to extend  existing approximate Differentially Private (DP) Functional Data analysis (FDA) tools into the Gaussian DP framework. These idea have been applied to the protection of 3D face data, where each face is represented by a collection of a set of curves.

### Strengths
The idea of using Functional Data Analysis  Gaussian  mechanism  Differentially Private to protect 3D face is interesting.

### Weaknesses
 - The writing of this paper should be improved,  it does not facilitate the understanding of the contributions in this paper.
- The approximation of 3D face by a set of radial curves has been published ins several papers related to 3D face recognition.  Hassen (1) Drira, Boulbaba Ben Amor, Mohamed Daoudi, and Anuj Srivastava. Pose and expression invariant
3d face recognition using elastic radial curves. In British machine vision conference, pp.
1–11, 2010. (2) Chafik Samir, Anuj Srivastava, and Mohamed Daoudi. Three-dimensional face recognition using
shapes of facial curves. IEEE Transactions on Pattern Analysis and Machine Intelligence, 28(11):
1858–1863, 2006.
- The contributions of this paper are not clear. Does the contributions of this paper concern the extension of GDP to functional data analysis, or the application to 3D face protection?
- The authors talk about functional data analysis which is a very general term, they should be more precise and discuss the representation of 3D faces by functions?
- In Appendix B.3 refers to the SRNF  representation of surfaces but how this representation is used in this paper ?

### Questions
Does the contributions of this paper concern the extension of GDP to functional data analysis, or the application to 3D face protection?
In Appendix B.3 refers to the SRNF  representation of surfaces but how this representation is used in this paper ?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new representation termed "face radical curves" for a set of 3D faces. It then utilizes the Gaussian Differential Privacy (DP) framework on this representation to create a private average face. The empirical and quantitative results from the experiments show that this method not only maintains the shape of the average face but also introduces less noise compared to traditional methods for the same privacy budget.

### Strengths
(1) This paper proposes a novel privacy-preserving representation method for 3D faces. According to the authors, this approach is also applicable to other disk-like surfaces.
(2) The paper presents the mean squared error between private estimates and the point-wise mean, showing that this method outperforms the conventional point-wise method.

### Weaknesses
（1) While the article effectively demonstrates the privacy capabilities of the representation through mean squared error metrics for 3D faces, it does not address the usability of the representation for practical applications, such as age estimation and expression analysis of faces. This aspect of usability verification is missing from the paper. Specifically, the paper lacks any discussion or experiments on how the face radical curves, after the application of differential privacy, retain the necessary information for these downstream tasks. It is unclear if the introduced noise primarily affects high-frequency details or if it also distorts the low-frequency components crucial for tasks like age estimation. The paper should include experiments or at least a discussion on the impact of the privacy mechanism on the feature space relevant to these applications.

（2）The authors suggest that the method described in the paper could be applicable to domains beyond 3D facial data. It would strengthen the paper if the authors could include experimental results demonstrating this method's effectiveness in other applications as well. The claim of general applicability is not sufficiently supported by the current experiments. The paper should provide evidence that the proposed method can handle different types of disk-like surfaces with varying topological and geometric characteristics. Without such evidence, the claim of broad applicability remains speculative.

### Questions
The paper needs to provide additional evidence to substantiate the usability of the proposed representation.

### Soundness
3

### Presentation
2

### Contribution
3
