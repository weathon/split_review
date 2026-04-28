# Chinese Inertial GAN for Writing Signal Generation and Recognition

- Decision: Reject
- Avg Score: 5.20
- Scores: 6, 5, 6, 3, 6

## Abstract
Disabled people constitute a significant part of the global population, deserving of inclusive consideration and empathetic support. However, the current human-computer interaction based on keyboards may not meet the requirements of disabled people. The small size, ease of wearing, and low cost of inertial sensors make inertial sensor-based writing recognition a promising human-computer interaction option for disabled people. However, accurate recognition relies on massive inertial signal samples, which are hard to collect for the Chinese context due to the vast number of characters. Therefore, we design a Chinese inertial generative adversarial network (CI-GAN) containing Chinese glyph encoding (CGE), forced optimal transport (FOT), and semantic relevance alignment (SRA) to acquire unlimited high-quality training samples. Unlike existing vectorization focusing on the meaning of Chinese characters, CGE represents the shape and stroke features, providing glyph guidance for GAN to generate writing signals. FOT establishes a triple-consistency constraint between the input prompt, output signal features, and real signal features, ensuring the authenticity and semantic accuracy of the generated signals and preventing mode collapse and mixing. SRA constrains the consistency between the semantic relationships among multiple outputs and the corresponding input prompts, ensuring that similar inputs correspond to similar outputs (and vice versa), significantly alleviating the hallucination problem of generative models. The three modules guide the generator while also interacting with each other, forming a coupled system. By utilizing the massive training samples provided by CI-GAN, the performance of six widely used classifiers is improved from 6.7% to 98.4%, indicating that CI-GAN constructs a flexible and efficient data platform for Chinese inertial writing recognition. Furthermore, we release the first Chinese writing recognition dataset based on inertial sensors in GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the challenge of data scarcity in Chinese writing recognition using inertial sensors by proposing the Chinese Inertial Generative Adversarial Network (CI-GAN). CI-GAN includes three innovative modules, Chinese Glyph Encoding (CGE), Forced Optimal Transport (FOT), and Semantic Relevance Alignment (SRA), to generate high-quality inertial signal samples. CGE captures the shape and stroke of Chinese characters, FOT ensures feature consistency to prevent mode collapse, and SRA aligns the semantic relevance of generated signals to their glyph structures. With CI-GAN, the authors establish a flexible data platform for Chinese writing recognition and claiming to release  the first inertial-sensor-based dataset on GitHub.

### Strengths
1. The introduction of CI-GAN is a novel approach for enhancing data availability in Chinese inertial writing recognition, with modules designed specifically to tackle challenges unique to Chinese characters.
2. The improvement from 6.7% to 98.4% in classifier performance highlights the potential of CI-GAN-generated data to enhance recognition accuracy, indicating practical benefits for downstream applications.

### Weaknesses
1. In Figure 1, CI-GAN is presented as a framework overview, yet it lacks consistency in terminology, with CGE mislabeled as "GER" and FOT written in full without abbreviation. Additionally, SRA is not visually represented in the figure. This detracts from the clarity of the diagram and makes it harder for readers to grasp the full framework.
2. The paper’s theoretical foundation could be strengthened. The current theoretical analysis is minimal, with only a few formulas provided. More detailed mathematical explanations, particularly for FOT’s role in preventing mode collapse, would lend greater credibility to the approach. Specifically, the mechanism by which FOT enforces feature consistency and avoids the generator producing limited variations of the same output needs further elaboration. The paper should detail how the optimal transport cost is calculated and how this cost is integrated into the GAN training process to achieve the desired effect.
3. The ablation studies are somewhat limited, and additional experiments testing more comprehensive combinations of CGE, FOT, and SRA would provide a clearer understanding of each module's contribution. More exhaustive ablation tests would validate the effectiveness of the modules individually and collectively. The current ablation study does not explore all possible combinations, leaving open the question of whether the modules have synergistic effects or if some modules are redundant. For example, the impact of removing FOT while keeping CGE and SRA should be explicitly evaluated.
4. The example in Figure 1, intended to illustrate the framework's application for disabled individuals, doesn’t effectively convey this purpose. Including a more relatable example that directly addresses accessibility for disabled users would better align with the stated motivation of the study. The current example is too abstract and does not clearly show how the system would be used by a disabled individual, making it difficult to understand the practical implications of the work.

### Questions
1. Can you clarify how Figure 1 relates to accessibility for disabled individuals, as the example seems disconnected?
2. Could you provide more theoretical details on the FOT component to reinforce its foundation?
3. Are more exhaustive ablation studies possible to validate the contributions of CGE, FOT, and SRA individually?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper propose CI-GAN, which enhances Chinese writing recognition for disabled users, generating high-quality samples and improving classifier performance significantly.

### Strengths
1. The article is clearly written and easy to understand. 

2. The motivation is clear: translating subtle movements of user’s hand into written text can help disabled people of writing. 

3. Experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The dataset is relatively small and lacks comprehensive coverage of the Chinese character set, which may not support the generation of more complex Chinese characters.

2. The proposed method should be tested on other public available benchmarks with other SOTA methods, such as IAHCC-UCAS2016 and CASIA-OLHWDB.

### Questions
See weaknesses

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
This paper introduces CI-GAN, a generative adversarial network for Chinese writing recognition using inertial sensors, designed to aid disabled individuals. CI-GAN incorporates Chinese glyph encoding, forced optimal transport, and semantic relevance alignment to generate accurate signals. With these synthetic signals, classifier accuracy improved from 6.7% to 98.4%. The study also releases the first Chinese inertial sensor dataset for writing recognition, advancing accessible human-computer interaction.

### Strengths
1.	The application of research has significant potential and creativity about addressing accessibility needs for disabled individuals.
2.	The proposed dataset contributes valuable inertial sensor data for Chinese writing. And the research introduces a novel method using GAN for data augmentation, effectively addressing data scarcity and enhancing handwriting recognition research.
3.	The experimental results show promising improvements in classifier accuracy.

### Weaknesses
1.	The concept of inertial data is introduced only in Section 4.2, making it somewhat difficult to understand when mentioned in the earlier parts of the paper. It is recommended to provide a brief introduction to this concept earlier on, specifically detailing what type of inertial data is being used (e.g., accelerometer, gyroscope, magnetometer), how it is collected, and its inherent characteristics that make it suitable for handwriting recognition. Without this context, the reader struggles to grasp the significance of the proposed method.
2.	The first point in the summary of contributions mentions that it "provides new tools for the study of the evolution and development of pictograms," which may not be suitable for the contributions summary, as it seems the research does not cover this aspect. This statement is misleading and should be removed or rephrased to accurately reflect the actual contributions of the work.
3.	The description of CGE mentioned in Section 3.1 seems to be just an embedding? In my opinion, the current version of the introduction may be somewhat complex. The explanation lacks clarity on how the glyph features are extracted and encoded, and how this encoding differs from standard embedding techniques. It is unclear what specific properties of the glyph are captured by CGE and how the Rényi entropy regularization contributes to the encoding process beyond simply creating a dense representation.

### Questions
1.	According to my understanding, CGE can be divided into two parts: 1. converting one-hot encoding into dense features, and 2. using α-order Rényi entropy regularization in GER. Therefore, in the ablation study in Section 4.4, what specific configuration is being ablated when CGE is removed? Which part of these two components is being eliminated? Additionally, can this ablation experiment validate the effects of the glyph encoding regularization (GER) proposed in Section 3.1?
2.	What is the difference between the pre-trained VAE mentioned in Section 3.2 and CGE in Section 3.1? It seems that both can extract glyph features. Can VAE replace CGE?
3.	What are h_G, h_T, and e in Section 3.2? It seems that e comes from the GAN input, h_G comes from the GAN output, but where does h_T come from during training?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the author proposes a method of sensor-style Chinese character data generation based on GAN. It mainly consists of three modules CGE, FOT and SRA. CGE encodes Chinese characters according to glyphs. FOT uses a ternary consistency constraint to monitor the consistency of the predicted sample, the real sample, and the glyph encoding vector. The SRA module aligns glyph and semantic encoding. The author collected 4500 samples of 500 Chinese characters, including 1500 samples in the training set and 3000 samples in the test set. The author uses the proposed CI-GAN to generate additional training sets to augment the original data set. The validity of the generated data is proved by comparing the recognition effect of training with different data quantities. The effectiveness of the proposed module is verified by ablation experiments.

### Strengths
This paper makes a strong contribution to research in accessible human-computer interaction, focusing on Chinese handwriting recognition for disabled individuals. It addresses an important issue by introducing CI-GAN, a generative model with unique modules—Chinese Glyph Encoding, Forced Optimal Transport, and Semantic Relevance Alignment—that effectively tackle the challenges of data scarcity and segmentation. According to the visualization results of Chinese glyph encodings, the module proposed in this paper is effective in encoding Chinese character shapes. The experimental results in Table 3 and Table 4 prove that the generated data has useful value.

### Weaknesses
The proposed method section does not provide sufficient comparisons and analysis. The collected real data and generated data are insufficient, and the quality of the constructed dataset is not high. The experimental section lacks important comparative experiments and analysis, making it difficult to demonstrate the effectiveness of the proposed method. The specific issues are as follows:

1.  **Methodology**: The authors propose a GAN-based generation method but do not compare its generation quality with other generative approaches, such as diffusion models or other GAN-based methods. The lack of comparison with other generative models, particularly those known for high-quality data synthesis, makes it difficult to assess the relative performance of the proposed CI-GAN. It is unclear if the proposed approach offers any advantages over existing methods in terms of data quality or diversity.

2.  **Dataset**: The dataset collected is small in scale, with data from only nine individuals and without full coverage of the complete Chinese character set.

    (1) The complexity of different Chinese characters is very different, and the author only shows the generation and classification results of relatively simple Chinese characters in this paper, it is impossible to evaluate the model's generation effect on complex Chinese characters. The lack of evaluation on complex characters raises concerns about the generalizability of the proposed method. The authors should demonstrate the model's ability to handle characters with varying stroke counts and structural complexities.

    (2) Writing habits vary greatly among individuals, leading to significant differences in handwriting styles. With data from only nine participants, how can the authors ensure that the generated data quality aligns with real-world scenarios? The limited number of participants may not capture the full range of handwriting variations, potentially leading to a biased model that does not generalize well to unseen handwriting styles.

3.  **Experiments**:

      (1) Comparative methods lack citations. The absence of citations for the comparative methods makes it difficult to verify the implementation details and assess the validity of the comparisons. It is unclear which specific algorithms were used and how they were configured.

      (2) The algorithm’s performance has not been tested on other public datasets. Whether the CIGAN generation effect can be verified on other open source datasets of Chinese character data, such as IAHCC-UCAS2016, CASIA-OLHWDB (ICDAR 2013 Chinese Handwriting Recognition Competition). The lack of evaluation on standard public datasets makes it difficult to compare the proposed method with existing state-of-the-art approaches and limits the generalizability of the findings.

      (3) The authors did not compare their method with other high-performing algorithms for Chinese character recognition, such as the one mentioned in [1].  As far as I know, [1] achieved a recognition accuracy of 96.78% on the dataset of all Chinese characters in the Level 1 Character Set (IAHCC-UCAS2016) and 97.86% on ICDAR-2013. I suggest the authors compare their method with more state-of-the-art (SOTA) approaches. The absence of comparison with state-of-the-art recognition methods makes it difficult to assess the practical value of the generated data. It is unclear if the generated data can improve the performance of existing high-performing recognition systems.

     (4) The experiments lack further analysis, such as individual-level performance testing and performance evaluation across characters with different stroke complexities. The lack of detailed analysis makes it difficult to understand the strengths and weaknesses of the proposed method. It is unclear how the model performs on individual writers and how its performance varies across characters with different stroke complexities.

These improvements would better support the effectiveness and applicability of the proposed approach.

### Questions
Repeat:
1. **Methodology**: The authors propose a GAN-based generation method but do not compare its generation quality with other generative approaches, such as diffusion models or other GAN-based methods.

2. **Dataset**: The dataset collected is small in scale, with data from only nine individuals and without full coverage of the complete Chinese character set. 

    (1) The complexity of different Chinese characters is very different, and the author only shows the generation and classification results of relatively simple Chinese characters in this paper, it is impossible to evaluate the model's generation effect on complex Chinese characters. 

    (2) Writing habits vary greatly among individuals, leading to significant differences in handwriting styles. With data from only nine participants, how can the authors ensure that the generated data quality aligns with real-world scenarios?

3. **Experiments**: 

      (1) Comparative methods lack citations.

      (2) The algorithm’s performance has not been tested on other public datasets. Whether the CIGAN generation effect can be verified on other open source datasets of Chinese character data, such as IAHCC-UCAS2016, CASIA-OLHWDB (ICDAR 2013 Chinese Handwriting Recognition Competition).

      (3) The authors did not compare their method with other high-performing algorithms for Chinese character recognition, such as the one mentioned in [1].  As far as I know, [1] achieved a recognition accuracy of 96.78% on the dataset of all Chinese characters in the Level 1 Character Set (IAHCC-UCAS2016) and 97.86% on ICDAR-2013. I suggest the authors compare their method with more state-of-the-art (SOTA) approaches.

     (4) The experiments lack further analysis, such as individual-level performance testing and performance evaluation across characters with different stroke complexities. 

These improvements would better support the effectiveness and applicability of the proposed approach.

[1] Gan J, Wang W, Lu K. A new perspective: Recognizing online handwritten Chinese characters via 1-dimensional CNN[J]. Information Sciences, 2019, 478: 375-390.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an innovative approach to addressing the limitations in performance of inertial sensor-based systems for Chinese character recognition, which traditionally rely on extensive manual data collection. By introducing a Chinese Inertial Generative Adversarial Network (CI-GAN), the study offers a solution that generates unlimited, high-quality training samples, thereby providing a flexible and efficient data support platform for classification models. This method significantly reduces the dependency on labor-intensive data gathering and enhances the overall performance and feasibility of using inertial sensors for HCI in the context of disability.

### Strengths
* **Clear Motivation and Feasible Approach**: The paper is driven by a well-defined goal—to improve HCI for disabled individuals using inertial sensors. The proposed solution, a generative adversarial network (GAN) for data generation, is not only innovative but also practically feasible, as evidenced by the experimental results.

* **Innovation and High Performance**: By introducing advanced techniques of CGE,  FOT and SRA, the study significantly enhances the recognition accuracy of Chinese characters, with performance improvements reported from 6.7% to 98.4%.

* **Social Impact and Community Contribution**: The research addresses significant accessibility issues for disabled individuals and adds substantial value to the community by releasing the first Chinese writing recognition dataset based on inertial sensors, enabling further advancements in the field.

### Weaknesses
 * **Visualization and Clarity of Diagrams**: The diagrams in the paper could be improved for better systematic representation and intuitiveness. Visualizing abstract constraints and regularization techniques more clearly would aid in understanding the complex interactions within the model. The task and symbols need a more detailed defination to improve the understanding.
* **Detailed Justification of Model Constraints**: The paper could be improved by including more detailed exploration of the motivations and effectiveness of using specific constraints such as the Forced Optimal Transport (FOT). A deeper discussion on why aligning input stroke encoding features with generated signal features and real signal features; and why utilizing Wasserstein distance as regularization can mitigate mode mixing and mode collapse is necessary to validate the approach.
* **Analysis of Robustness Under External Disturbances**: The paper lacks a thorough analysis of the system's robustness in the presence of external disturbances. Detailed insights into how these factors affect the system and recommendations for enhancing robustness would strengthen the paper.

### Questions
As shown in Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
