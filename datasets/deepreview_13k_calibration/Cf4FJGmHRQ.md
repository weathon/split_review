# PAC-FNO: Parallel-Structured All-Component Fourier Neural Operators for Recognizing Low-Quality Images

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
A standard practice in developing image recognition models is to train a model on a specific image resolution and then deploy it. 
    However, in real-world inference, models often encounter images different from the training sets in resolution and/or subject to natural variations such as weather changes, noise types and compression artifacts. While traditional solutions involve training multiple models for different resolutions or input variations, these methods are computationally expensive and thus do not scale in practice. To this end, we propose a novel neural network model, parallel-structured and all-component Fourier neural operator (PAC-FNO), that addresses the problem. Unlike conventional feed-forward neural networks, PAC-FNO operates in the frequency domain, allowing it to handle images of varying resolutions within a single model. We also propose a two-stage algorithm for training PAC-FNO with a minimal modification to the original, downstream model. 
    Moreover, the proposed PAC-FNO is ready to work with existing image recognition models.
    Extensively evaluating methods with seven image recognition benchmarks, we show that the proposed PAC-FNO improves the performance of existing baseline models on images with various resolutions by up to 77.1\% and various types of natural variations in the images at inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work has developed a neural network architecture for image recognition that is designed to address the influence of complex degradation factors. It aims to capture both low-frequency and high-frequency components to balance accuracy and generalization. The authors first propose to discard the low-pass filters in the existing FNO structure to retain all frequency components. Subsequently, a parallel structure is introduced to further enhance the utilization of frequency domain information. Finally, the authors design a two-stage training strategy to ensure performance stability.

### Strengths
1. The overall paper has a clear logical structure, and the explanation of the methodology and the presentation of the constructed mechanisms are intuitive and easy to understand.
2. The author provides a sufficiently detailed explanation for the motivation behind each component in PAC-FNO.
3. The problem that this work aims to address holds a certain degree of practical application value.

### Weaknesses
1. The abandonment of the low-pass filter is one of the main innovations in this work. Although the author provides an explanation for the motivation behind this operation, it is still recommended that the author conduct ablative experiments to analyze the impact of low-frequency/high-frequency information on accuracy/generalization. Specifically, the paper should include quantitative results showing how performance changes when only low-frequency or high-frequency components are used, and how these changes affect both in-distribution and out-of-distribution performance.
2. As for parallel architecture, the relevant experimental results have indeed proven its effectiveness. However, the explanation of parallel architecture in the method section appears somewhat lacking. It is hoped that the author can provide further analysis of the mechanism that enables it to be effective. The explanation should delve deeper into why a parallel structure is superior to a serial one, perhaps by analyzing the information flow and the specific frequency components each path is capturing. A more detailed discussion of how the parallel paths interact and contribute to the final representation would also be beneficial.
3. In terms of comparative experiments, the methods used by the author for comparison appear to be lacking in both quantity and novelty. The comprehensiveness of the complex scenarios considered by the author is commendable, but it is hoped that the author can still increase the comparison results with more advanced works to more effectively validate the superiority of the proposed method. The current comparisons do not adequately demonstrate the advantage of the proposed method over state-of-the-art techniques. It would be beneficial to include comparisons against more recent and higher-performing models, particularly those designed for robustness against complex degradations.
4. The author mentions the advantages of this work in terms of efficiency, but it seems that no experimental analysis related to efficiency has been provided (such as FLOPs and runtime on data at different resolutions). The paper should include a detailed analysis of the computational cost of the proposed method, including FLOPs, parameter counts, and runtime measurements on various hardware configurations. This analysis should also compare the efficiency of the proposed method with other methods, especially at different input resolutions.

### Questions
Please refer to the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel neural network model, parallel-structured and all-component Fourier neural operator (PAC-FNO) to address visual recognition under low-quality images. By operating in the frequency domain, PAC-FNO is able to learn the semantics of images in various resolutions and/or natural variations for challenging image recognition with a single model. The proposed PAC-FNO is capable of handling both low-resolution and input variations typically observed in low-quality images with a single model. It can also be attached to a downstream visual recognition model, which is beneficial for handling multiple input variations at once and minimizing the changes in the downstream model during fine-tuning. In the evaluation with four visual recognition models and seven datasets, the proposed PAC-FNO achieves excellent performance.

### Strengths
1. The paper is organized well.
2. Extensive experimental results are provided to illustrate the effectiveness of the proposed method.

### Weaknesses
1. Is there a more advanced choice for the SR baseline model used for comparison in your experimental setup? This will affect the fairness of the performance of your experiment?
2. It can be found that in ViT-B16, PAC-FNO shows not very good results at all low resolutions compared to other methods. What caused this phenomenon to occur? Is your method also unfriendly to other Transformer methods?
3. The ideal low-pass filter in the FNO block removes detailed image signals that play an important role in classification in the fine-grained dataset. Is this conclusion applicable to Transformer based image classification methods? More quantitative results should be provided to confirm the universality of the proposed method.
4. The ablation experiments about the results of the zero-padding operation and the exclusion of the low pass filter need to be completed to explain the design of the AC-FNO block.

### Questions
Please see the weaknesses above.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a novel solution named PAC-FNO for image recognition, demonstrating the ability to simultaneously handle images of varying resolutions and resist the impact of various types of input-induced natural variations within a singular model in recognition tasks. The proposed parallel-structured and all-component Fourier neural operator (PAC-FNO), building on the resolution invariance of FNOs in the frequency domain, notably eliminates the ideal low-pass filter found in vanilla FNOs. Additionally, it transforms the traditional serial architectures into a parallel structure, thereby considering a broader range of frequency components, retaining high-frequency details, and notably enhancing performance, especially in fine-grained datasets. The proposed approach introduces a two-stage training method that fine-tunes pre-trained image recognition models in conjunction with PAC-FNO, allowing the acquisition of commonalities among various input resolutions with minimal modifications to the backbone classification network. Through conducted experiments, the authors effectively showcase the performance of PAC-FNO, significantly improving accuracy in comparison to existing baseline models. The manuscript is well-written, and the experiments conducted are comprehensive and convincingly articulated.

### Strengths
1. The paper exhibits a high level of innovation. Although neural network operators based on the Fourier domain transformation for learning, due to their excellent characteristics in resolution invariance, have been recognized and applied in various areas, especially for enhancing pre-processing operators in variable-resolution input networks. However, the authors, motivated by the rational desire to retain high-frequency image details, proposed for the first time to eliminate the inherent low-pass filters in the model. Additionally, they introduced a popular parallel structure similar to Multi-head Self-Attention, further enhancing the network's performance while expanding the design philosophy of relevant operators.

2. The presentation of this paper is professional and fluent. It has almost no expression errors and clearly elucidates the authors' contributions.

3. The paper conducted extensive and meticulous experiments, utilizing seven image recognition benchmark datasets and applying the operators to four different backbone networks. The authors closely follow the cutting-edge developments in the field, employing more advanced VIT and ConvNeXt for experimentation, which makes the results highly persuasive.

### Weaknesses
1. Although the author compared super-resolution (SR) models for variable resolution inputs, the compared SR models are outdated and lack representation across various upscaling factors for super-resolution reconstruction. The field of super-resolution has seen significant advancements recently; thus, it is recommended to select more appropriate comparative algorithms. Specifically, the comparison should include recent state-of-the-art methods that handle a wider range of upscaling factors, such as those based on transformer architectures or diffusion models, which have shown superior performance in preserving high-frequency details during upscaling. The current selection of SR baselines does not adequately challenge the proposed method's ability to handle variable resolution inputs compared to the current state-of-the-art.

2. The primary advantage of Fourier Neural Operators (FNOs) lies in their use of frequency domain processing for resolution invariance. As a learnable enhancement operator, it's expected to exhibit some resilience to input natural variations. However, the author hasn't provided a detailed and explanatory analysis of the mechanisms where the operator shows robustness against natural variations. Moreover, the chosen input variations in the experiments, like fog, brightness, spatter, and saturate, represent basic degradation scenarios that can be addressed without deep learning methods. Therefore, regarding resilience to input natural variations, this might not be sufficiently emphasized as a highlight of the paper. The paper suggests exploring degradation in real-world scenarios in future work, indicating that the authors are aware of the limitations in terms of experimental performance or the algorithm proposed. However, such scenarios represent fundamental problems studied in the field of Image Recognition (IR) and hold significant practical application implications. Actually, certain degradation processes might affect high or low frequency details in the image's frequency domain. For instance, blur involves the loss of high-frequency details, prompting the author to conduct a mechanistic analysis combining frequency domain and degradation processes to enhance this aspect's interpretability.

3. The original intent behind the existence of ideal low-pass filters was to reduce the number of parameters and computational complexity. While the author's innovative design to remove the inherent low-pass filter is intuitively comprehensible, the associated trade-offs are not discussed in the manuscript. It would be beneficial to provide supplementary explanations to demonstrate the worthiness of such a modification. The manuscript should include a detailed analysis of the computational cost, memory footprint, and inference time associated with removing the low-pass filter, and compare these metrics against the baseline FNO models. This would help to justify the design choice and demonstrate that the performance gains are not achieved at an unreasonable cost.

4. The experiments thoroughly prove the advantages of parallel architectures and claim that this approach encapsulates more frequency components. However, they lack further detailed explanations and justifications. The paper should include a more in-depth analysis of how the parallel architecture captures a broader range of frequency components compared to serial architectures. This could involve visualizing the frequency responses of different branches in the parallel structure and demonstrating how they complement each other to cover a wider spectrum. Additionally, a theoretical justification for why a parallel structure is better suited for capturing diverse frequency information would strengthen the argument.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
