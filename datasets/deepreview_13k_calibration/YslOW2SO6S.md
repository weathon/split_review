# CirT: Global Subseasonal-to-Seasonal Forecasting with Geometry-inspired Transformer

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Accurate Subseasonal-to-Seasonal (S2S) climate forecasting is pivotal for decision-making including agriculture planning and disaster preparedness but is known to be challenging due to its chaotic nature. Although recent data-driven models have shown promising results, their performance is limited by inadequate consideration of geometric inductive biases. Usually, they treat the spherical weather data as planar images, resulting in an inaccurate representation of locations and spatial relations. In this work, we propose the geometric-inspired Circular Transformer (CirT) to model the cyclic characteristic of the graticule, consisting of two key designs: (1) Decomposing the weather data by latitude into circular patches that serve as input tokens to the Transformer; (2) Leveraging Fourier transform in self-attention to capture the global information and model the spatial periodicity. Extensive experiments on the Earth Reanalysis 5 (ERA5) reanalysis dataset demonstrate our model yields a significant improvement over the advanced data-driven models, including PanguWeather and GraphCast, as well as skillful ECMWF systems. Additionally, we empirically show the effectiveness of our model designs and high-quality prediction over spatial and temporal dimensions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper propose an improved approach to the Subseasonal-to-Seasonal (S2S) climate forecasting problem. The method mainly has two novel parts: 1. A better input patching method which utilize the circular nature of the graticule. 2.  Propose to intervene Discrete Fourier Transform throughout the transformer layers. 

The propose methods demonstrate improvement over all the existing methods, both numeric methods and data-driven method. And the propose method is especially effective in the long time horizon prediction compared to other autoregressive data-driven methods which suffer from error aggregation. The method also show better performance in the hard-to-predict areas like polar areas.

### Strengths
1. The experiments are extensive, solid, and the results are good. The paper compares the proposed method with both numerical method and ml method, and the metrics on latitude-weighted RMSE and Anomaly are strong and solid. The visualization graphs are very useful to understand the impact of the proposed method in different dimensions.

2. The proposed method well utilize the characteristics of the input data modality. The circular patching strategy introduce a effective inductive bias, and the DFT well utilize the latitudinal spatial periodicity.

### Weaknesses
1. The comparison to existing method does not include computation complexity/model size. This weakens the comparison to other methods because the reader don't know whether the improvement is brought by the network architecture design or simply due to the increase in model size. It's crucial to understand if the performance gains are a result of more efficient architecture or just a larger model, especially when comparing against numerical methods which may have different computational profiles. Without this information, it's difficult to assess the practical applicability of the proposed method.

2. It would be a plus if the paper could also include a ablation study of autogressive prediction vs directly predicting all the future values, to ablate the effectiveness of the autoregressive formulation. The current autoregressive approach might be masking potential benefits of direct prediction, especially given the known issues of error accumulation in autoregressive models. An ablation study would help isolate the impact of the autoregressive formulation on the overall performance.

### Questions
I am wondering why the proposed method patch all the different longitudinal areas into the same patch. What prevents the model from taking a 2d input HxWxD and do e.g. axial transformer (intervene between attention along H axis and then W axis) with Fourier Transform.

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
1

### Summary
CIRT propose a novel network for accurate S2S climate forecasting. The key idea is to model the cyclic characteristic of the graticule, consisting of two designs: (1) decomposing the weather data by latitude into circular patches; (2) Use fourier transform in self-attention. Extensive experiments on ERA5 demonstrate the effectiveness of the proposed CIRT network.

### Strengths
1. The paper is well-written, and the idea and motivation are intuitive. Figure 1 clearly highlights the limitations in previous methods, providing a strong rationale for the proposed approach.

2. CIRT introduces significant innovations to address the lack of geometric inductive biases in prior work. Specifically, it partitions the graticule uniformly by latitude and leverages the Fourier transform to capture global features, which are then processed with self-attention.

3. The experimental results effectively demonstrate the superiority of CIRT, comparing favorably with both numerical and data-driven models.

### Weaknesses
GraphCast employs a graph neural network for weather forecasting, sharing a similar initial motivation with CIRT in aiming to reduce inappropriate geometric inductive biases. The authors should consider providing a more in-depth discussion on the distinctions between GraphCast’s model design and system architecture compared to their own, highlighting the unique aspects and advantages of their final approach.

### Questions
Add discussion with GraphCast.

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
5

### Summary
The article designs a circular transformer (CirT) to model medium—and long-term numerical forecasts. It takes into account the spherical structure of the ground, designs corresponding circular patches as input tokens of the Transformer, and uses the Fourier transform in self-attention to capture global information to model the spatial periodicity, achieving high accuracy.

### Strengths
The article has clear logic and ideas. The proposed method is very consistent with the research problem. It considers the problems faced by Patch Embedding in global meteorological modeling. Compared with most methods, it has achieved excellent results in high-latitude regions.

### Weaknesses
1、The data in the experiment of the article is 1.5° instead of 0.25° as used in the Pangu model. Obviously, the author should give a detailed explanation of the experiment. The lack of clarity on how the 1.5° results for the Pangu model were obtained is a significant concern. It is crucial to understand if the Pangu model was downsampled or if a separate 1.5° model was used. This difference in resolution directly impacts the comparability of results and the validity of the conclusions.
2、The article lacks experimental conditions for key variables such as wind u and wind v. The absence of results for wind components (u and v) is a notable omission, as these are critical variables in weather forecasting. The model's performance on these variables is essential for a comprehensive evaluation, especially considering their complex spatial and temporal dynamics.
3、The article states that the usage of the Transformer network with Fourier transform is an important component, but both AFNO and Fourcast use related structures, which is not innovative enough. While the use of Fourier transforms in self-attention is a valid approach, its novelty is questionable given its prior use in models like AFNO and Fourcast. The article needs to clearly articulate the unique aspects of its implementation and demonstrate how it differs from existing methods.

### Questions
1、The author should explain in detail how the results of the 1.5° experiment of the Pangu model were obtained. In global forecasts, there is currently a 0.25° prediction model. Is the 1.5° model necessary?
2、The experimental conditions of variables such as wind u and wind v.
3、Most weather models are tuned after training is complete, the article does not perform this work and fine-tuning can be used to further improve model performance.

### Soundness
2

### Presentation
3

### Contribution
2
