# No Location Left Behind: Measuring and Improving the Fairness of Implicit Representations for Earth Data

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Implicit neural representations (INRs) exhibit growing promise in addressing Earth representation challenges, ranging from emissions monitoring to climate modeling. However, existing methods disproportionately prioritize global average performance, whereas practitioners require fine-grained insights to understand biases and variations in these models. To bridge this gap, we introduce FAIR-Earth: a first-of-its-kind dataset explicitly crafted to challenge and examine inequities in Earth representations. FAIR-Earth comprises various high-resolution Earth signals, and uniquely aggregates extensive metadata along stratifications like landmass size and population density to assess the fairness of models. Evaluating state-of-the-art INRs across the various modalities of FAIR-Earth, we uncover striking performance disparities. Certain subgroups, especially those associated with high-frequency signals (e.g., islands, coastlines), are consistently poorly modeled by existing methods. In response, we propose spherical wavelet encodings, building on previous spatial encoding research for INRs. Leveraging the multi-resolution analysis capabilities of wavelets, our encodings yield more consistent performance over various scales and locations, offering more accurate and robust representations of the biased subgroups. These open-source contributions represent a crucial step towards facilitating the equitable assessment and deployment of implicit Earth representations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new set of datasets called FAIR-EARTH, aimed at addressing and assessing fairness in Earth science. FAIR-EARTH encompasses various types of data, including environmental factors and emissions, while also taking geographical features and population density into account. Experimental results demonstrate that existing spherical harmonics methods fail to maintain accurate local performance, particularly regarding land and sea masses. To address this issue, the authors propose using spherical Morlet wavelets to correct localized biases. Results indicate that this approach outperforms existing methods in most situations.

### Strengths
S1. The bias issues in earth science are interesting and important.  
S2. The paper is well-written and easy to understand, even for those who are not familiar with earth or geographical concepts.  
S3. The experiments provide detailed insights into model behavior and validate the effectiveness of spherical wavelets in improving representation fairness.

### Weaknesses
W1. The performance trade-offs of spherical wavelets are insufficiently addressed.
W2. The computation efficiency of spherical wavelets is not discussed.
W3. More discussion regarding the flexibility and weakness of the proposed datasets.

### Questions
1. While spherical wavelets show good performance on most cases to correct localized biases, their robustness remains uncertain. It is known that correctly parameterizing elements like wave number and scaling factors for specific resolutions are necessary to reach the best performance. The authors should conduct experiments to illustrate the trade-offs associated with using spherical wavelets.

2. Since spherical wavelet is well-defined at poles, what should we do for poles? Would there exist bias in poles?

3. Implementing spherical wavelet encodings requires a more complex parameter selection and may need more computation. Efficiency evaluation should be considered for using spherical wavelets

4. While FAIR-EARTH can address some bias for the ill-represented areas like landmasses, authors should detail the weakness/flexibility of this combination approach. What kind of dataset can be integrated if there is temporal bias or learning representation for poles?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
1. This paper constructs a new dataset to unify different existing geospatial datasets under a consistent framework.

2. This paper proposes that fairness is reflected in the concurrent performance improvement of the model across different subgroups, and it conducts specific measurement and analysis based on correlation.

3. This paper proposes using SPHERICAL WAVELET for encoding to mitigate fairness issues while maintaining performance.

### Strengths
1. This paper products constructs a new dataset, which aggregates extensive metadata along stratifications like landmass size and population density and unifies disparate existing geospatial datasets under a consistent framework.

2. This paper proposes that fairness is reflected in the concurrent performance improvement of the model across different subgroups. Experiments and analysis show significant disparities in the performance of the spherical harmonic method across different subgroups uncovering a strong negative correlation between landmass size and representation loss, with areas corresponding to localized signals and high-frequency features exhibiting consistently poor performance.

3. This paper proposes that encoding using SPHERICAL WAVELET solves many obvious deviations in SPHERICAL HARMONIC on many benchmarks of FAIR-EARTH while maintaining competitive performance.

### Weaknesses
1. In this paper, only one of the existing methods is tested on the new dataset, which leads to the lack of convincing for the generality and accuracy of the new dataset. 

2. This paper proposes a method for measuring fairness, but in the experiments, it only conducts specific analyses on two different subgroups and one existing method.

3. This paper proposes using SPHERICAL WAVELET for encoding, but experiments are only carried out on the self-constructed dataset. Experiments should also be carried out on other datasets to verify the effectiveness of the method.

### Questions
1. Different methods are needed to illustrate the validity of the new dataset.

2. More groups of examples and different methods are needed to illustrate fairness.

3. Different datasets are needed to verify the validity of methods.

### Soundness
3

### Presentation
3

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
This paper addresses fairness issues in Implicit Neural Representations for Earth data. First, it introduces FAIR-EARTH, a comprehensive dataset designed to evaluate biases in Earth representations across various spatial resolutions and features. Second, to address the identified fairness issues, particularly in representing local features, the authors propose using wavelets instead of traditional harmonics, demonstrating improved representation of fine-grained geographical features while maintaining global performance.

### Strengths
1. Addresses a critical and underexplored issue of fairness in Earth data representation

2. The proposed dataset provides a comprehensive framework for evaluating and comparing different approaches to Earth representation, which will be valuable for future research

3. The use of wavelets for modeling local features is theoretically well-motivated in representing fine-grained geographical features

### Weaknesses
1. While the paper successfully identifies the problem and proposes a promising direction with Spherical Wavelets, it primarily remains at a conceptual level, lacking detailed implementation specifications and comprehensive empirical analysis across different wavelet types.

2. The computational complexity and scalability analysis should be presented, especially given that wavelet-based approaches typically incur higher computational costs than Spherical Harmonics due to their multi-scale nature and the need for both rotation and dilation operations.

### Questions
Have you evaluated other wavelet types besides the Morlet wavelet? What were their relative performances, particularly in representing different types of geographical features? Could you provide some intuitive guidelines for selecting wavelet parameters based on the type of geographical features being represented?

### Soundness
4

### Presentation
4

### Contribution
4
