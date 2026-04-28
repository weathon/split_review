# CarbonSense: A Multimodal Dataset and Baseline for Carbon Flux Modelling

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Terrestrial carbon fluxes provide vital information about our biosphere's health and its capacity to absorb anthropogenic CO$_2$ emissions. The importance of predicting carbon fluxes has led to the emerging field of data-driven carbon flux modelling (DDCFM), which uses statistical techniques to predict carbon fluxes from biophysical data. However, the field lacks a standardized dataset to promote comparisons between models. To address this gap, we present CarbonSense, the first machine learning-ready dataset for DDCFM. CarbonSense integrates measured carbon fluxes, meteorological predictors, and satellite imagery from 385 locations across the globe, offering comprehensive coverage and facilitating robust model training. Additionally, we provide a baseline model using a current state-of-the-art DDCFM approach and a novel transformer based model. Our experiments illustrate the potential gains that multimodal deep learning techniques can bring to this domain. By providing these resources, we aim to lower the barrier to entry for other deep learning researchers to develop new models and drive new advances in carbon flux modelling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a standardized dataset called CarbonSense, which is a dataset compiled from various sources. The compilation steps include fusing the data together on the same hourly scale, extracting relevant features, and doing min max normalization. Along with the dataset, the paper also proposes a data driven model based on Perceiver called EcoPerceiver. This proposed model uses transformer architecture to cross attend all input features. The paper also implemented a SOTA approach baseline and compared its performance on the proposed dataset with EcoPerceiver.

### Strengths
CarbonSense integrates diverse data modalities—measured carbon fluxes, meteorological predictors, and satellite imagery—across a wide array of ecosystems. Researchers can use this dataset as a standardized benchmark.

### Weaknesses
1.The dataset was compiled from multiple sources with various modalities, which may introduce inconsistency or OOD samples when doing model training. Careful data analysis can be helpful
2. The experiment shows the proposed EcoPerceiver outperformed the current SOTA approach for most IGBP types especially WET, WAT, and ENF. However, the paper did not include an ablation study to showcase why the proposed model achieved this performance.
3.There is only one baseline compared and there is no model with single modalities.

### Questions
How does the Perceiver model compare to other advanced machine learning models in terms of performance? In addition, which component of EcoPerceiver affects performance the most? I think adding more machine learning model baselines and conducting ablation study would help determine the model's relative strengths and weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors present CarbonSense as a machine learding ready multimodal dataset for carbon flux modeling. The dataset includes meteorological variables, MODIS 81 pixels satellite observations, and eddy covariance of carbon fluxes from hundreds of locations globally, Authors, in addition to the proposed dataset, presented a baseline machine learning model to predict carbon fluxes. The model shows the power of the multimodality of the dataset to improve canbon flux modeling performance.

### Strengths
* Paper is well written and cohesive. It is easy to follow and understand even for non-experts in the field
* Adds a clear contribution to existing dataset in terms of scale and modalities added. This will definitely help progress in the field.
* Dataset will be open for anyone to use. This is important for it to make any impact.

### Weaknesses
 * The satellite imagery added is very low resolution wich limits it's potential usefulness. Specifically, the 500m to 1km resolution of MODIS data is a significant limitation when trying to capture fine-scale variations in vegetation cover and land surface properties that strongly influence carbon fluxes. This makes it difficult to accurately model heterogeneous landscapes, where flux variability can be high even within small areas. 
* The dataset does not include many observations outside developed countries. Nothing the authors can do sinse they leverage existing EC stations available.

### Questions
* Consider adding satellite date from Sentinel 2 and 2 or Landsat which are higher resilution for days available. These datasets are open for anyone to use.
* Is it possible to keep expanding the dataset in a systematic way by ingesting EC and MODIS data periodically?

### Soundness
3

### Presentation
4

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
This paper presents a new benchmark dataset, Carbon Sense, for predicting carbon flux from geospatial and meteorological data. Two models are evaluated on the new benchmark: 1) an XGBoost model which emulates the SOTA method from prior work, and 2) the EcoPerceiver model proposed in this paper. Domain-relevant evaluation metrics of RMSE and NSE (Nash-Sutcliffe Modelling Efficiency) are reported for each model and broken down by ecosystem type, with statistical tests of significance of the differences in performance. EcoPerceiver significantly outperforms the XGBoost model, indicating there is room for improvement on the benchmark relative to the previous SOTA with more sophisticated/tailored ML approaches.

### Strengths
- The benchmark has multimodal inputs, which helps fill a notable gap in multimodal benchmarks for remote sensing/geospatial ML. 
- The paper presents useful and approachable background about the carbon flux modeling problem.
- The benchmark code is designed to allow flexibility in reproducing and extending or modifying the dataset based on user needs.
- The benchmark has a permissive CC-BY license.
- The EcoPerceiver method is well motivated based on the domain-specific carbon flux modeling problem.
- Domain relevant metrics are used for evaluation.

### Weaknesses
 - The train/test splits are divided by station location, which avoids spatial autocorrelation issues. It seems there could be significant temporal autocorrelation within each split since there are many measurements from the same location. Is temporal autocorrelation a concern?
- The experiments only compared two models, XGBoost and EcoPerceiver. It would be useful to see additional models benchmarked (especially deep learning models) to get a sense of the variation in performance existing solutions on this benchmark.
- What does the purple vector in Figure 4 represent?

### Questions
- The train/test splits are divided by station location, which avoids spatial autocorrelation issues. It seems there could be significant temporal autocorrelation within each split since there are many measurements from the same location. Is temporal autocorrelation a concern?

- What does the purple vector in Figure 4 represent?

- How do other deep learning models (existing models besides the new EcoPerceiver) perform on CarbonSense?

### Soundness
3

### Presentation
3

### Contribution
3
