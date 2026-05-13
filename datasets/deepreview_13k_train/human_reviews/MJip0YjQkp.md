# SPACT18: Spiking Human Action Recognition Benchmark Dataset with Complementary RGB and Thermal Modalities

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
Spike cameras, bio-inspired vision sensors, asynchronously fire spikes by accumulating light intensities at each pixel, offering ultra-high energy efficiency and exceptional temporal resolution. Unlike event cameras, which record changes in light intensity to capture motion, spike cameras provide even finer spatiotemporal resolution and a more precise representation of continuous changes. In this paper, we introduce the first video action recognition (VAR) dataset using spike camera, alongside synchronized RGB and thermal modalities, to enable comprehensive benchmarking for Spiking Neural Networks (SNNs). By preserving the inherent sparsity and temporal precision of spiking data, our three datasets offer a unique platform for exploring multimodal video understanding and serve as a valuable resource for directly comparing spiking, thermal, and RGB modalities. This work contributes a novel dataset that will drive research in energy-efficient, ultra-low-power video understanding, specifically for action recognition tasks using spike-based data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes the first video action recognition using spike camera, alongside synchronized RGB and thermal modalities.

### Strengths
1. This paper is simple and easy to understand.

### Weaknesses
1.  The authors emphasize that the temporal resolution of spike cameras is superior to that of event cameras.  But I think that's wrong. The proof is not a hardware paper but an algorithm paper, which I don't think is a good starting point. The paper [1]  would have been able to do 3.6$\mu $s  temporal resolution compared to the spike camera even in 2011.

2. In line 60,  the thermal modality is used very suddenly, just to provide a comprehensive multimodal representation, and why this modality is important, I think, needs to be elaborated.

3. The references are out of date and need a more comprehensive review.

4. Different models should be utilized in the experiment to give more comparable results.

5. There is a lack of comparison of model experiments for SNNs that direct train.

6. Please reference these paper to set up and complete the experiment part [2],[3].

### Questions
None

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
SPACT18 has developed a novel VAR dataset for fully incorporating SNNs into VAR tasks. It is commendable that the author considered multiple variables in the process of constructing the dataset. In addition, the author's introduction is complete and logically fluent, with good narrative quality. In the methodology section, the author provides a complete introduction to the data construction process, its basic data architecture, and the most important event data alignment steps. However, in the experimental section, the author only tested the effectiveness of two typical algorithms and used the ANN-SNN conversion to test the performance of the SNN algorithm, which is incomplete. In future work, a larger number of ANN algorithms should be supplemented for testing to verify the stability of the distribution of the SPACT18 dataset. In addition, algorithm testing based entirely on SNN is also necessary. In summary, this article provides a large-scale VAR dataset based on events and innovatively proposes an event alignment strategy, which is in line with the logic and innovation required for conference papers.

### Strengths
This article proposes SPACT18- a novel event based large-scale VAR task dataset. The dynamic response characteristics of events and the low power consumption of SNNs provide new possibilities for the development of VAR. Meanwhile, the method section innovatively proposes an alignment method for event pulses, which is a unique compression method suitable for VAR tasks. This article has made certain progress and contributions to VAR tasks.

### Weaknesses
The experimental part appears slightly thin. Using only two typical VAR algorithms for verification is insufficient for verifying the distribution of RGB and thermal modal data. At the same time, the validation of the SNN algorithm is still based on the ANN-SNN conversion method, which cannot fully utilize the parsing ability that SNN should have. The choice of only X3D and UniFormer models is limiting, as these models may not fully capture the nuances of the proposed dataset. The lack of experiments with other established architectures for video understanding, such as C2D, I3D, and SlowFast, makes it difficult to assess the generalizability of the dataset. Furthermore, the SNN validation relies on ANN-SNN conversion, which is known to have limitations in fully exploiting the temporal processing capabilities of SNNs. Direct training of SNNs should be explored to better evaluate the dataset's suitability for spiking neural networks.

### Questions
(1) Has a detailed analysis been conducted on the impact of external factors such as age, gender, and race on the distribution of the dataset and the effectiveness of VAR;
(2) Does the architecture of the SPACT18 dataset include commonly used data collection methods (RGB/thermal mode) and analyze the differences between SPACT18 and other existing datasets;
(3) Due to the fact that video understanding typically adopts frame by frame input, i.e. still in the form of a single frame image sequence. Is there an analysis of the contribution of each frame to the video action recognition task? I believe that different cumulative states of the event stream can be equivalent to one frame of video image, and the contribution of each frame will be particularly prominent in the event camera;

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an action recognition dataset incorporating spike, RGB, and thermal modalities. Additionally, it presents a spiking data compression algorithm designed for preprocessing and compressing the dataset. The dataset is evaluated using state-of-the-art lightweight ANN and SNN models.

### Strengths
- The dataset is original and diverse, featuring 44 participants and 18 activities, making it a sufficiently challenging resource for validating models.
- With three modalities—spike, RGB, and thermal—the dataset is highly informative and suitable for researchers in image processing, spiking neural networks, and multimodal analysis.
- The writing is clear, and the paper is well-structured.
- The authors validate the dataset using popular architectures, demonstrating its applicability.

### Weaknesses
1. The paper lacks a thorough comparison with existing action recognition datasets, particularly in terms of modality, participant diversity, types of activities, sample size, and duration. Given that the primary contribution of this work is the proposed dataset, a clear comparison would help emphasize its advantages over existing datasets. Specifically, a table summarizing key characteristics of other datasets, including sensor types (e.g., event-based, RGB, depth), resolution, number of classes, number of subjects, and recording duration would be beneficial. This would allow for a more direct assessment of the novelty and utility of the proposed dataset.
2. The paper cites only one spike-based action recognition dataset (Amir et al., 2021). However, there exist other spike-based action recognition datasets, such as (Wang et al., 2024, Liu et al., 2021, Miao et al., 2019). It would be beneficial for the authors to consider these datasets in their comparison and explore whether any other relevant action recognition datasets are available. A more comprehensive literature review would strengthen the paper's positioning within the field.
3. Could you provide the confusion matrix for one or several models in Table 3? Since some activities in the proposed dataset overlap with those in [Amir et al., 2021], a confusion matrix could help determine if the additional activities are sufficiently discriminative and enhance the dataset's value. This is crucial for understanding the model's performance on individual classes and identifying potential areas of confusion between similar actions.
4. The authors clearly specify the recording devices and versions for the thermal and RGB data. However, the spike camera is not similarly described. Could you include details about this device for completeness? Information such as the sensor model, pixel size, and dynamic range would be valuable for researchers seeking to replicate the data collection process.
5. I have a question regarding the proposed compression method. Specifically, what distinguishes the approach of calculating frequency first and then using IF neurons from directly employing leaky LIF neurons? Would using leaky LIF neurons potentially offer a simpler and more direct solution? It's unclear why the intermediate frequency calculation step is necessary, and a justification for this design choice is needed.

### Questions
Can you address the 1st, 3rd, 4th and 5th points I mentioned in the weakness section?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces SPACT18, a novel video action recognition (VAR) dataset captured using a spike camera, alongside synchronized RGB and thermal modalities.

### Strengths
Introducing a spike camera-based dataset for video action recognition is a novel contribution. The dataset could become a valuable resource for researchers exploring energy-efficient spiking models for real-time applications, particularly in edge devices or autonomous systems.

### Weaknesses
1. The experimental setup and analysis are not sufficiently thorough.  The dataset is aimed at benchmarking Spiking Neural Networks (SNNs) for action recognition tasks, but the paper does not include any direct evaluation using SNN-based methods. Since the core claim is that this dataset enables effective benchmarking for SNNs, its advantages in temporal processing remain unproven without such an evaluation. Including results from SNN-specific architectures or methodologies (eg. directly trained SNN models and ANN-SNN conversion methods) would strengthen the paper’s contribution to the field.

2. The dataset's scale and diversity are limited compared to established RGB video action recognition benchmarks such as HMDB-51, UCF-101, and Kinetics-400, which feature far more action classes (51, 101, and 400, respectively). SPACT18 includes only 18 action classes and a significantly lower number of training clips. This restricts its utility for developing models that generalize well across diverse action recognition tasks, limiting the dataset’s value for broader use in the community.

3. Overclaiming on Spike Camera superiority. The paper claims that spike cameras offer significant advantages over event cameras. However, this claim is not supported by sufficient evidence or direct comparisons. To substantiate such claims, the authors should provide side-by-side evaluations of spike and event camera performance, particularly in relevant tasks like video action recognition, or refer to studies that have explored these comparisons in depth.

4. The paper overstates the complexity of action recognition relative to tasks such as optical flow estimation, motion estimation, depth estimation, or image reconstruction [L133-138]. Action recognition, being a classification task, is often less complex than these tasks, which involve per-pixel regression and dense predictions. It would be more accurate to frame action recognition as an important but distinct problem, rather than more complex, to avoid misrepresentation.

### Questions
Could you clarify the advantages of using spike cameras over event cameras, RGB cameras, and thermal data? From Table 4, it appears that performance using spike data is consistently lower, and Figure 6 shows that spike data is quite blurry, which may make it harder for models to learn meaningful dynamic information. How do you address these limitations, and in what situations does spike data excel over other modalities?

### Soundness
1

### Presentation
2

### Contribution
1
