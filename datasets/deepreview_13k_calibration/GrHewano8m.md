# XXLTraffic: Expanding and Extremely Long Traffic forecasting beyond test adaptation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Traffic forecasting is crucial for smart cities and intelligent transportation initiatives, where deep learning has made significant progress in modeling complex spatio-temporal patterns in recent years. However, current public datasets have limitations in reflecting the distribution shift nature of real-world scenarios, characterized by continuously evolving infrastructures, varying temporal distributions, and long temporal gaps due to sensor downtimes or changes in traffic patterns. These limitations inevitably restrict the practical applicability of existing traffic forecasting datasets. To bridge this gap, we present XXLTraffic, the longest available public traffic dataset with the longest timespan collected from Los Angeles, USA, and New South Wales, Australia, curated to support research in extremely long forecasting beyond test adaptation. Our benchmark includes both typical time-series forecasting settings with hourly and daily aggregated data and novel configurations that introduce gaps and down-sample the training size to better simulate practical constraints. We anticipate the new XXLTraffic will provide a fresh perspective for the time-series and traffic forecasting communities. It would also offer a robust platform for developing and evaluating models designed to tackle the extremely long forecasting problems beyond test adaptation. Our dataset supplements existing spatio-temporal data resources and leads to new research directions in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present XXLTraffic, the longest available public traffic dataset with the longest timespan collected from Los Angeles, USA, and New South Wales, Australia, curated to support research in extremely long forecasting beyond test adaptation. The benchmark includes both typical time-series forecasting settings with hourly and daily aggregated data and novel configurations that introduce gaps and down-sample the training size to better simulate practical constraints.

### Strengths
1. A brand-new dataset is proposed, which is the largest available public traffic dataset in extremely long traffic forecasting.

2. Numerous comparative experiments validate the differences in performance of different models on this dataset, providing a good guide for peers to understand the latest technological developments.

### Weaknesses
1. The maximum number of nodes in the proposed dataset is less than the Large-ST, which seems to need improvement, after all, the real road network is very large.

2. I think it is necessary for the authors to explain in more depth the motivation for constructing such a long-term dataset, because as transportation infrastructure advances and human travel modes change, traffic data that is too ancient is not always helpful enough to understand future transportation patterns.

3.  Due to the sheer size of the proposed dataset, it requires more computational resources. Therefore, whether this dataset can be popularized and whether peers can easily adopt it in their own research is also a concern.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a traffic dataset containing extensive data records from multiple regions over a long-term period, aimed at supporting research in ultra-long-term traffic prediction.

### Strengths
(1) A new traffic dataset is proposed, comprising data from numerous regions across California and New South Wales over an extended time period.

(2) The temporal distribution evolution of selected data was visualized, revealing the evolutionary characteristics of the data.

(3) Tests were conducted on relevant prediction tasks, including scenarios with time gaps and varying input lengths.

### Weaknesses
(1) Compared to existing works like LargeST, this work's contribution is insufficient as it merely expands the temporal and spatial scope of data collection. These data can be obtained through the open-source PEMS system in the same way.

(2) Although the number of regions and time span are substantial, the vast majority of data is limited to California. Including data from more cities and countries might have been a better approach.

(3) Most baselines in the experiments are specifically designed for time series prediction, lacking models specifically designed for traffic prediction/spatiotemporal prediction, such as PDFormer[1], ASTGCN[2], STGCN[3], AGCRN[4], GWN[5], etc. It is important to explore the performance of these types of baselines on traffic datasets.

### Questions
Please refer to the Weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed large-scale datasets, named XXLTrafic, to address limitations in existing traffic forecasting datasets. It provides extensive, real-world datasets with long timespans to support research in extremely long forecasting and adaptive model development for evolving traffic patterns.

### Strengths
1.	The proposed XXLTraffic is the largest publicly available traffic dataset so far. The PEMS part spans up to 23 years and the NSW part also has around 11 years’ data.

2.	The authors evaluated the performance of existing baselines on the proposed datasets with various settings. The overall results verify the importance of introducing large-scale datasets with extremely long time spans.

### Weaknesses
1.	The most significant weakness is that this paper has no novelty. Although this conference has a dataset and benchmarks area, I do not think, for a top-tier conference, it is enough to propose a large-scale dataset without any model contribution. Given the fact that there are existing large-scale datasets available with just the number of nodes or time spans fewer than XXTraffic, my concern becomes more intense.

2.	Some motivations remain unclear. In the introduction section, the authors mentioned ‘beyond test adaptation’. However, it is not easy to understand how this relates to the proposed datasets. Is the concept of ‘beyond test adaptation’ better or more realistic than test time adaptation?

3.	The setting of Extremely Long Prediction with Gaps is a bit strange to me. Here, the authors used an example of highway route planning prediction to justify the necessity of the gap. It is possible that we need to stimulate the traffic flows of uninstalled sensors to facilitate road planning. Thus, the optimal setting should be using existing sensors to predict traffic flows of uninstalled sensors, plus the gap. However, it seems the authors still used historical signals of uninstalled sensors in this setting. If we already know their historical readings, we do not have to plan anything.

### Questions
The authors can address the above concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper present an XXLTraffic traffic dataset spanning up to 23 years in different countries, which can be useful for the other researchers. They have also implemented the datasets with many advanced approaches to confirm the range and different experiments directions.

### Strengths
1. This paper introduces an XXLTraffic dataset that spans up to 23 years from different regions, which means the dataset include sufficient information for the traffic feature.
2. This paper presents many potential conditions that the dataset could be applied to such as short-term traffic prediction, long-term multivariate traffic prediction and extremely long term prediction with gaps. All of these domains are worthwhile problem to focus.

### Weaknesses
1. The dataset is valuable, but performing extremely long-term predictions is challenging, as traffic patterns can change significantly over the years, and even the road infrastructure itself may be reshaped over a 23-year span. Such factors could potentially reduce the impact of the dataset's contribution, because many open datasets are enough for normal short and long term prediction. Moreover, the paper does not sufficiently address the potential for non-stationarity in the traffic data over such extended periods. The impact of temporal shifts in traffic patterns due to urban development, changes in commuting habits, or even economic fluctuations, is not discussed, which could limit the applicability of the dataset for robust long-term forecasting.
2. Some typos, e.g., ‘beyongd’  should be ‘beyond’ around line 130;

### Questions
How is the gap dataset collected, given that "gap" typically refers to missing data? Can this dataset be directly used to address traditional missing data scenarios?

### Soundness
4

### Presentation
3

### Contribution
4
