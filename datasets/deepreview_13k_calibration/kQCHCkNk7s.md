# AstroCompress: A benchmark dataset for multi-purpose compression of astronomical data

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
The site conditions that make astronomical observatories in space and on the ground so desirable---cold and dark---demand a physical remoteness that leads to limited data transmission capabilities. Such transmission limitations directly bottleneck the amount of data acquired and in an era of costly modern observatories, any improvements in lossless data compression has the potential scale to billions of dollars worth of additional science that can be accomplished on the same instrument. Traditional lossless methods for compressing astrophysical data are manually designed. Neural data compression, on the other hand, holds the promise of learning compression algorithms end-to-end from data and outperforming classical techniques by leveraging the unique spatial, temporal, and wavelength structures of astronomical images. This paper introduces [AstroCompress](https://huggingface.co/AnonAstroData): a neural compression challenge for astrophysics data, featuring four new datasets (and one legacy dataset) with 16-bit unsigned integer imaging data in various modes: space-based, ground-based, multi-wavelength, and time-series imaging. We provide code to easily access the data and benchmark seven lossless compression methods  (three neural and four non-neural, including all practical state-of-the-art algorithms).
Our results on lossless compression indicate that lossless neural compression techniques can enhance data collection at observatories, and provide guidance on the adoption of neural compression in scientific applications. Though the scope of this paper is restricted to lossless compression, we also comment on the potential exploration of lossy compression methods in future studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces AstroCompress, a benchmark dataset designed for multi-purpose compression of astronomical images, providing a foundation for advancing astronomy-specific and science-oriented lossless neural compression. Through comprehensive experiments, various image compression codecs are tested and evaluated.

### Strengths
1. The released dataset is made open-accessible and well-organized for researchers to follow.
2. Several lossless compression codecs have been tested including both learned/traditional methods. Evaluations of the impact on datasets and methods are presented.

### Weaknesses
1. Since many of the datasets are from publicly accessible resources, therefore i suggest that the authors should contribute more over the analysis and deeper evaluation of the re-organized AstroCompress dataset.
2. The cross-dataset evaluation can be improved. In this paper, only brief conclusions about the generalization of different codecs are provided. A deeper evaluation of the similarity between different datasets and the reason for performing differently for different codecs is suggested.

### Questions
If there also exists some codecs specially designed for astro data, the authors should also provide some evaluation.

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
2

### Summary
This paper provide a dataset and benchmark for astronomical data compression. The dataset is relatively large (320 GB). Besides, the dataset composes 5 distinct subsets, which covers images of different dimension, resoluton and content types. The authors evaluate the datasets on different lossless compression methods, including IDF, L3C, PixelCNN++, JPEG series and RICE.

### Strengths
The dataset composes of diverse images, from 2D to 4D, which is impressive. The selective of neural lossless codec baseline is smart. In fact. IDF, L3C and PixelCNN++ represent three major paradigms of lossless compression: normalizing flow, latent variable model and auto-regressive model. In fact, I can not think of a better choice if I need to choose three most representative lossless image codec.

### Weaknesses
One most evident weakness is that the authors evaluate 7 general lossless codec and only 1 astronomical codec (published in 2009). I have two explainations for this evaluation:
* The authors's evaluation is not thorough, many astronomical codecs are omitted.
* The astronomical data compression is not an active research area, and the only reasonable baseline is published 15 years ago.
Either of the explaination makes me hesitate about accepting this paper.

Besides, I am not really sure about how important astronomical data compression is to ICLR community. From the BACKGROUND AND RELATED WORK section in this paper, I find that most papers of astronomical data compression are published in remote sensing and compression related venues, not machine learning related venues (NIPS, ICLR, ICML, CVPR, ICCV, ECCV, etc.). I am not really sure about:
* How many people in ICLR community is interested in astronomical data compression?
* How many people in astronomical data compression community will read ICLR?

### Questions
It is the first time that I ever review a benchmark paper. I am not definitely sure about my evaluation. And I am glad to change my mind if other reviewers are positive toward this paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper describes a new dataset for benchmarking neural compression on astronomical data. The paper lays out how the efficacy of astronomical experiments is highly dependent storage and transmission, and that the fidelity of the data must be preserved, motivating the use of neural lossless compression. The dataset itself is apparently unprecedented in scope for astronomical data with five sub-datasets including a mix of 2D still images as well as spatio-temporal and multispectral hypercubes of high resolution. The paper concludes by testing a series of well know neural and non-neural lossless compression algorithms on the dataset.

### Strengths
The paper makes a strong contribution to astrological and neural compression research. The paper lays out clearly how astrological experiments depend on good compression and why a dataset specific to astrological data is necessary. The scope of the dataset is also impressive. It is likely that a researcher working on neural compression, lossless or otherwise, would be interested in findings from testing their method on this dataset. Likewise I can imagine astrological researchers using results on this dataset to decide what methods to deploy. Finally the assembly procedure and details in Appendix A shows that great care was put into the curation of the data.

### Weaknesses
The only thing which I would have liked to see more discussion on was the point about runtime/compression ratio. Is there any actionable recommendation here? Also given that JPEG-XL is mostly a reference implementation right now and hasn't been optimized while the neural methods require a GPU, is it  fair comparison to say that it is slower? The paper presents runtime results without a clear discussion of the trade-offs between compression performance and computational cost. The lack of a detailed analysis of the computational resources required by the neural methods, particularly in comparison to the non-neural methods, makes it difficult to assess their practical applicability. For instance, the memory footprint of the neural networks and the impact of batch size on encoding/decoding speed are not discussed. Furthermore, the comparison of JPEG-XL, which is noted as a reference implementation, against neural methods that inherently require specialized hardware (GPUs) for efficient execution is not fully justified without a more thorough analysis of the hardware constraints and optimization potential for each method.

### Questions
* Any actionable recommendation around neural/classical compression based on results?
* Are resource requirements (GPU, memory) factored into speed results?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a benchmark dataset designed for multi-purpose compression of astronomical imagery. A range of image compression codecs is tested and evaluated through comprehensive experiments. The benchmark dataset can serve for researches in astronomy-specific and science-specific lossless neural compression by providing a carefully curated, accessible dataset, along with easily referenceable benchmarks.

### Strengths
1. The released dataset is well organized and large in scale and diversity to cover a wide range of astrophysics data.
2. The tested anchors are representative, including both popular learned and conventional codecs.

### Weaknesses
1.	Two different methods for handling 16-bit images are discussed and tested. It is recommended that the performance differences between these methods be highlighted. Specifically, the impact of converting 16-bit data to two 8-bit channels versus maintaining a single 16-bit channel should be analyzed in terms of compression efficiency and potential information loss. The paper should include a more detailed study on how these different representations affect the performance of various compression algorithms.
2.	The proposed dataset’s effectiveness, especially in comparison to existing datasets such as Maireles-González et al. (2023), could be explored more thoroughly. A more rigorous comparison, including quantitative metrics and specific use cases, is needed to demonstrate the unique advantages of the new dataset. The paper should provide a detailed analysis of the dataset's characteristics and how they address the limitations of existing datasets.
3.	The performance of RGB-pretrained models on the AstroCompress dataset are suggested to be examined and reported. It is important to understand how well models trained on natural images generalize to astronomical data, and whether the specific characteristics of astronomical images require specialized training. This analysis should include a discussion of the potential challenges and limitations of using RGB-pretrained models for astronomical data compression.
4.	The implementation details regarding correlated-frame compression could be clarified further. Specifically, it should be explained whether different frames are compressed independently for each tested anchor, or if a different approach is used. The paper should provide a clear description of the compression strategies used for multi-frame data, including the handling of temporal or spectral correlations.

### Questions
As an important aspect in image compression, some preliminary experiments and evaluation on lossy compression are expected.

### Soundness
3

### Presentation
3

### Contribution
3
