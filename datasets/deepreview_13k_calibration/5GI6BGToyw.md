# AtmosArena: Benchmarking Foundation Models for Atmospheric Sciences

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Deep learning has emerged as a powerful tool for atmospheric sciences, showing significant utility across various tasks in weather and climate modeling. In line with recent progress in language and vision foundation models, there are growing efforts to scale and finetune such models for multi-task spatiotemporal reasoning. Despite promising results, existing works often evaluate their model on a small set of non-uniform tasks, which makes it hard to quantify broad generalization across diverse tasks and domains. To address this challenge, we introduce AtmosArena, the first multi-task benchmark dedicated to foundation models in atmospheric sciences. AtmosArena comprises a suite of tasks that cover a broad spectrum of applications in atmospheric physics and atmospheric chemistry. To showcase the capabilities and key features of our benchmark, we conducted extensive experiments to evaluate two state-of-the-art deep learning models, ClimaX and Stormer on AtmosArena, and compare their performance with other deep learning and traditional baselines. By providing a standardized, open-source benchmark, we aim to facilitate further advancements in the field, much like open-source benchmarks have driven the development of foundation models for language and vision.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces AtmosArena, a benchmark designed for evaluating foundation models in atmospheric sciences, focusing on multi-task spatiotemporal learning. The paper mainly evaluates two prominent models, ClimaX and Stormer, comparing their performance with traditional baselines across various tasks. Stormer performs well in short-term forecasting, while ClimaX excels in tasks with longer temporal horizons, highlighting the benefits of multi-source pretraining. Overall, the authors demonstrate that pre-trained models generally outperform task-specific baselines, and AtmosArena serves as a comprehensive tool for advancing atmospheric modeling.

### Strengths
1. **New Perspective:** The article evaluates atmosphere modeling from a multitasking perspective and verifies the effectiveness of two pre-trained models: ClimaX (multi-source pre-trained models) and Stormer (single-source pre-trained models).
2. **Open Source:** By providing a standardized and open-source framework, AtmosArena sets a new standard for reproducibility and transparency in multi task atmospheric learning.
3. **Include Finetuneing:** The paper explores the finetuning protocols for foundation models, comparing frozen versus fully finetuned backbones.
4. **Diverse Tasks:** AtmosArena benchmark includes both atmospheric physics and atmospheric chemistry tasks, and the benchmarks utilize well-regarded datasets like ERA5, ClimateBench, and ClimateNet.

### Weaknesses
1. Regarding the completeness of the benchmark, I believe the authors should add relevant metrics, such as **inference FLOPs and model parameters**.

2. The authors need to provide more **evidence (e.g., frameworks and code)** to demonstrate the benchmark’s ease of use and reproducibility.

3. Although the authors conducted extensive experiments to show that no single model excels across all tasks, I believe they should **further analyze** the experimental results rather than simply testing performance across different tasks.

### Questions
See the weaknesses.

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
4

### Summary
The authors present a comprehensive collection of benchmarks, with appropriate baseline models, for tasks related to atmospheric science and prediction.

### Strengths
While each component of the dataset is not novel, the combination and the testing of multi-model foundational models make this a useful contribution. The baselines are well chosen and the data appears to be well structured (though I have not tested this). The paper is well structured and well written. In particular, each of the sub-tasks defined in the 'arena' are appropriate and complementary, and the baselines are appropriate and test interesting aspects of their generalizability.

### Weaknesses
It isn't entirely clear that any of the presented models are foundation models; it feels like the 'atmosphere' is a bit too specific of a system to qualify as foundational. To some extent this is something the cited models need to demonstrate, but nonetheless, to demonstrate its utility, this paper should describe what they mean by a foundation model for the atmosphere, and why the tasks they present (within a fairly narrow range of spatial and temporal scales) would test such foundational knowledge.  Relatedly, the paper feels a bit like a collection of benchmarks and could do a better job of explaining why the various tasks are complementary, e.g. because they all rely on some underlying understanding of the covariance of the atmosphere over different spatial and temporal scales (be explicit).

### Questions
Please explicitly describe how the presented tasks complement each other and aim to test the necessary variables, and spatial and temporal scales to qualify a model as 'foundational'.

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
The authors propose a benchmark suite in which they collect several benchmark datasets into one framework which therefore offers a broader set of tasks to evaluate foundation models in weather and climate. Using their AtmosArena setup, the authors evaluate two prominent foundation models, ClimaX and Stormer on the set of atmospheric phsysical tasks and highlight performance
differences that underline the usefulness of the benchmark.

### Strengths
The set of tasks under this new benchmark suite is larger than any of the individual existing frameworks and therefore offers the chance for a more in depth comparison of foundation models across tasks. The paper is clearly written and structured such that it is easy to follow.

### Weaknesses
In my opinion a shortcoming of the proposed framework is that it is more a collection of existing benchmark frameworks like Weatherbench, ClimateBench, and ClimateNet and misses some opportunities for improvement. This statement to me is not about "novelty", but rather remaining shortcomings or inconsistencies under this new framework.

- While you state that in the future you would like to have a public
  leaderboard, I think this is already something to be expected from such a
  framework. Something like the google [Weatherbench leaderboard](https://sites.research.google/weatherbench/) is a decent
  refrenece to get a first idea of perfomrance across models
- For the task of climate down scaling you employ the RMSE, Bias and Pearson
  correlation as available metrics, however, especially here, metrics like Power
  Spectral Density (PSD), and PSD plots are important and offer more insights than a single error metric value
-  in fact, for all climate related prediction tasks (Forecasting, Super-resolution, inpainting mentioned in your paper) spectral metrics are
  commonly employed in the atmospheric science literature and should be a part of an atmospheric benchmark
- as another point, I think not including any probabilistic metrics across the
  collected tasks is unfortunate because simple point estimates just come short
  of the complexities given these tasks. A notion of prediction uncertainty and
  an assessment of the predictive uncertainty with metrics like proper scoring
  rules seems essential when aiming to do an holistic analysis. Probabilistic metrics were for example included in Weatherbench2 but seem to be missing from your framework.

Given that from my understanding you have collected existing frameworks under a new benchmark suite, I would have expected some additional improvements about the shortcomings of those, especially surrounding additional evaluation metrics as this is such an important part of benchmarking. While the employed metrics are very common in machine learning, I think additional metrics like PSD that exist in the atmospheric science literature are essential for a good benchmark framework.

Paper Questions:
- in section 4.5, Table 4, the numbers reported for ClimaX, ClimaX frozen and
  ClimateBench-NN are exactly the same as the values reported in the ClimaX
  publication Table 2, which I do find a bit surprising that there is no
  statistical difference given the non-deterministic nature of Deep Learning
  model training and a rather small data size
- is there a reference for the Spectral Divergence metric you use, or is this a metric you propose in this work?
- Line 18, you say the "first multi-task benchmark", but in table 1 you list
  existing works that consider "multiple atmospheric tasks" so I don't think
  your claim of "first" holds, but maybe you can clarify?

General Comment:
- I believe a work like this is highly dependent on the quality of the code,
  this is difficult to assess in this review process which is very unfortunate

### Questions
Paper Questions:
- in section 4.5, Table 4, the numbers reported for ClimaX, ClimaX frozen and
  ClimateBench-NN are exactly the same as the values reported in the ClimaX
  publication Table 2, which I do find a bit surprising that there is no
  statistical difference given the non-deterministic nature of Deep Learning
  model training and a rather small data size
- is there a reference for the Spectral Divergence metric you use, or is this a metric you propose in this work?
- Line 18, you say the "first multi-task benchmark", but in table 1 you list
  existing works that consider "multiple atmospheric tasks" so I don't think
  your claim of "first" holds, but maybe you can clarify?

General Comment:
- I believe a work like this is highly dependent on the quality of the code,
  this is difficult to assess in this review process which is very unfortunate

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article proposes a new benchmark for evaluating atmospheric and weather foundation models. It comprises the following tasks: 
weather forecasting, S2S forecasting, climate data infilling, climate model emulation, climate downscaling, and extreme weather events detection with several metrics for each task. datasets, fine-tuning protocols, evaluation code, standardized metrics, and traditional and machine learning baselines.

### Strengths
This paper presents a standardized benchmark for climate and weather evaluation with data, metrics, code, and baselines. It evaluates all consistently, transparently, in a way that it is easy to reproduce and that will facilitate and boost the research in this area.

### Weaknesses
AtmosArena, does not offer a pertaining dataset, only evaluation.

It is not clear to me why we need a new benchmark. In the related work section of benchmark three should be a clear comparison with the other benchmarks and why this one is better and needed.

AtmosArena has a great overlap with ClimateLearn, ClimaX, and Aurora. Almost all the tasks and datasets except for ClimateNet and Berkeley Earth are already in the other datasets. Is it that you created new annotations, or is it easier to use? Why do we need AtmosArena and not to test on the other ones directly?

### Questions
AtmosArena has a great overlap with ClimateLearn, ClimaX, and Aurora. Almost all the tasks and datasets except for ClimateNet and Berkeley Earth are already in the other datasets. Is it that you created new annotations, or is it easier to use? Why do we need AtmosArena and not to test on the other ones directly?

### Soundness
3

### Presentation
3

### Contribution
3
