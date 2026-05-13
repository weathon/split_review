# Specialized Foundation Models struggle to beat Supervised Baselines

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Following its success for vision and text, the ``foundation model'' (FM) paradigm---pretraining large models on massive data, then fine-tuning on target tasks---has rapidly expanded to domains in the sciences, engineering, healthcare, and beyond. 
Has this achieved what the original FMs accomplished, i.e. the supplanting of traditional supervised learning in their domains?
To answer we look at three modalities---genomics, satellite imaging, and time series---with multiple recent FMs and compare them to a standard supervised learning workflow: model development, hyperparameter tuning, and training, all using only data from the target task.
Across these three specialized domains, we find that it is consistently possible to train simple supervised models---no more complicated than a lightly modified wide ResNet or UNet---that match or even outperform the latest foundation models.
Our work demonstrates that the benefits of large-scale pretraining have yet to be realized in many specialized areas, reinforces the need to compare new FMs to strong, well-tuned baselines, and introduces two new, easy-to-use, open-source, and automated workflows for doing so.\looseness-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper aims to challenge the assumption that foundation models (FMs) consistently outperform traditional supervised learning methods. To support this, the authors design an automated machine learning framework, utilizing neural architecture search for genomics and satellite imaging tasks, and an Auto-ARIMA approach for time series analysis. These automated workflows produce competitive supervised models, providing strong baselines against which FMs are compared.

The study highlights that, unlike in general-purpose AI tasks (e.g., NLP or computer vision), the advantages of FMs in specialized fields remain unproven (FMs frequently fail to surpass traditional supervised learning models that are optimized for each task), emphasizing the need for diverse, well-tuned baselines in FM evaluation.

### Strengths
1. This paper is well-organized and well-written. The research questions are both interesting and practical, particularly in highlighting that some foundation models (FMs) are not fully comparable to in-domain, supervised baseline models. The experimental setup and results are comprehensive, effectively supporting the study’s objectives and providing valuable insights into the performance of FMs relative to tailored supervised models.

2. The two proposed automated supervised pipelines, DASHA and Auto-AR, are designed with detailed insights into model architecture, resulting in lightweight, simple yet powerful baselines. In particular, the development of Auto-AR highlights previously overlooked limitations and gaps in earlier works, encouraging the research community to rethink classical methods.

3. The paper demonstrates high quality through its methodological rigor and detailed experiments. (1) Thorough Benchmarking: The authors evaluate multiple foundation models (FMs) across three distinct scientific fields, using datasets and tasks that reflect real-world applications. This comprehensive experimental setup ensures that the results are robust and meaningful. (2) Well-Constructed Baselines: The paper establishes carefully optimized baselines using existing supervised models. This level of detail ensures fair and well-founded comparisons, providing a reliable foundation for drawing conclusions.

### Weaknesses
1. The strong performance of supervised methods through the automated pipeline may be largely attributed to the large-scale training data. As noted in the data statistics in the appendix, nearly all datasets contain over 10,000 samples for training, which is sufficient for effective supervised training from scratch, even without pretrained checkpoints. For a comprehensive evaluation and to support the claim that pure supervised learning can outperform pretraining, additional experiments varying data scale (e.g., using different ratios of training data) are needed. This would likely highlight the advantages of large-scale pretraining.

2. In addition to performance metrics like accuracy and model parameters, other essential factors are not addressed in the paper. Specifically, the authors do not mention the time and computing resources required to obtain the optimal architecture and hyperparameters. Compared to directly fine-tuning foundation models (FMs), it is unclear whether the automated pipeline is more time- and compute-intensive. Including these comparisons would provide a fuller understanding of the trade-offs involved in using the automated pipeline.

3. The assumption that “their creators make a best-effort attempt to present their own method in the best light” may not be fully reasonable. Due to the high computational costs and complexity of foundation models, obtaining optimal or even sub-optimal hyperparameters is generally challenging.

### Questions
My primary concerns regarding the acceptance of this work are based on points 1 and 2 described in the “weakness” section. These concerns stem from my own experience, particularly regarding point 1, where foundation models (FMs) generally demonstrate greater robustness in small-scale data adaptation through fine-tuning in vision and language tasks. However, this behavior may differ in the other modalities used in this paper.

The claim that “FMs in these domains have not yet surpassed supervised workflows and are often outperformed by fairly simple methods, including lightly modified CNN backbones (in genomics and satellite imaging) and classical linear forecasters (for time series)” may be somewhat overstated. This is especially relevant when considering factors such as data bias, the challenges of hyperparameter optimization for FMs, and potential out-of-distribution issues that could lead to negative transfer due to pretraining data limitations.

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
The paper examines the effectiveness of foundation models (FMs) in specialized domains like genomics, satellite imaging, and time series data, relative to traditional supervised learning models. The authors aim to challenge the assumption that foundation models necessarily outperform supervised models in these domains. Using a rigorous experimental framework, they contrast FMs with supervised baselines, emphasizing cases where the benefits of large-scale pretraining do not translate into superior downstream performance. Through their novel automated pipelines—DASHA for genomics and satellite imaging, and Auto-AR for time series—the authors provide a streamlined, data-efficient, and computationally lighter alternative to FMs, that demonstrates competitive performance across several tasks. The study raises important considerations about the necessity and cost-efficiency of pretraining-heavy foundation models in specialized fields.

### Strengths
1. The benchmarks and datasets chosen for each domain appear to comprehensively cover relevant applications in genomics, satellite imaging, and time series.

2. The paper highlights computational efficiency as a priority by contrasting the costs associated with FMs versus the supervised baselines. Holds high relevance given the fast adoption of large, resource-intensive models in research and industry.

3. Contextualized the results within each domain, providing a nuanced understanding of the model performance across tasks.

### Weaknesses
1. The paper lacks an exploration of their applicability to other types of data or more complex, multi-modal tasks. A broader discussion of potential limitations could help future researchers understand the contexts in which DASHA and Auto-AR might or might not succeed. Specifically, the study does not address how these models would perform with data that has inherent structural differences, such as graph-based data or point clouds, which are increasingly relevant in biological and environmental applications. The current scope limits the generalizability of the findings.

2. The choice of baselines (e.g., Wide ResNet and UNet for genomics and satellite imaging) is reasonable but could be expanded. Although the selected baselines demonstrate competitive performance, further comparisons with more recent architectures, such as those employing attention mechanisms or more advanced convolutional designs, could reinforce the study’s claims regarding the relative inefficacy of FMs in these domains. For example, comparing against models that have shown state-of-the-art results on ImageNet or similar benchmarks would provide a stronger basis for comparison.

3. Although the paper effectively highlights the efficiency of supervised workflows, the focus on computational cost may not fully account for the trade-offs in scalability and generalization that FMs can offer. While computational cost is a crucial factor, the paper should also address the potential for FMs to adapt to new tasks with minimal retraining, a capability that supervised models often lack. The discussion should include a more nuanced analysis of the trade-offs between computational efficiency and model adaptability.

4. For time series, the paper does not sufficiently address the unique challenges of zero-shot forecasting. Including more details on why certain zero-shot FMs performed poorly could provide actionable insights for model improvement in zero-shot contexts. The paper should delve deeper into the specific characteristics of the time series data that might be causing the observed performance issues, such as seasonality, trend, or noise, and how these factors interact with the zero-shot capabilities of the FMs.

### Questions
Q1. Could the DASHA and Auto-AR workflows be extended or adapted for multi-modal datasets or tasks involving mixed data types? If so, what modifications might be necessary?
Q2. How do the authors envision the role of foundation models evolving in these domains if computational resources continue to scale? Would certain configurations of FMs potentially start to outperform supervised baselines, or do they anticipate the observed trends to persist?
Q3. Given the success of NAS in selecting optimal CNN architectures for genomics and satellite imaging, do the authors plan to explore whether reinforcement learning or meta-learning approaches might yield further performance gains?

### Soundness
3

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
This work evaluates the effectiveness of foundation models (FMs) in genomics, satellite data, and time series, finding that well-tuned supervised models can match or outperform FMs in these specialized domains. The results suggest that large-scale pretraining benefits are not yet fully realized in these areas, highlighting the need for solid baseline comparisons.

### Strengths
1) The paper addresses a highly relevant topic that warrants investigation, given the growing popularity of FMs and the ongoing efforts within the community to adapt these models to specialized domains beyond natural images and text.

2) The results are surprising and critical to keep a fair benchmarking of future FMs against other pipelines. The actual gains in data efficiency scored by the proposed baselines (nice summary in Figure 1) range from three to five orders of magnitude in the three tested domains (satellite imaging, genomics, and time series). The authors also plan to release the code for their baselines, providing the community with a valuable benchmark resource.

3) The experimental setup is comprehensive, with models evaluated on up to 50 tasks. I found the design of the supervised baseline to be rigorous and fair, especially the decision to approximate standard practitioner model development through architecture search. 

4) The paper is clear, well-written, and easy to follow, making its main message easy for the reader to understand.

### Weaknesses
1) The paper presents two "solutions" from an architectural standpoint, i.e., CNNs for genomics/satellite data and auto-AR for time series. This leads to two questions:
- What model should a practitioner use when facing a task in a different specialized domain?
- How come 1D CNNs (or, e.g., RNNs) fail to match the performance of FMs in time series forecasting?

Is it just a matter of domain knowledge and data type? In practice, the paper would benefit from some more convincing justification and evidence for the statement, "While DASHA can be applied to forecasting tasks, it is not competitive with state-of-the-art time series FMs." (Line 240). Specifically, the claim that DASHA is not competitive needs more rigorous support, perhaps with a more detailed analysis of its performance on time series data, including a breakdown of where it struggles compared to Auto-AR and FMs. Also, why in Table 3 the evaluation of DASHA for the "Full setting" panel is reported as "unknown" ("-")?

2) The authors should add a brief discussion either in the Introduction or Related Work with references regarding "simple tuned baselines", which were shown to outperform/match more complex approaches, as this fact has been seen multiple times in the machine/deep learning literature and is clearly relevant to this work. Some related literature:

- Evaluating Weakly Supervised Object Localization Methods Right, CVPR 2020
- In Search of Lost Domain Generalization, ICLR 2021
- Image Classification with Small Datasets: Overview and Benchmark, IEEE Access 2022
- OoD-Bench: Quantifying and Understanding Two Dimensions of Out-of-Distribution Generalization, CVPR 2022
- When Do Neural Nets Outperform Boosted Trees on Tabular Data?, NeurIPS 2023 Datasets & Benchmarks
- Systematic Comparison of Semi-supervised and Self-supervised Learning for Medical Image Classification, CVPR 2024

### Questions
See the weakness section for possible improvements. I am willing to listen to the author's feedback and raise my score during the rebuttal period if the weaknesses are addressed.

### Soundness
4

### Presentation
3

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
The paper conducts a comparitive study of foundation models across three domains of time-series data, genomics and satellite data, whereby a selection of foundation models in each domain are compared to a supervised baseline. More specifically, the authors propose an Auto-ML pipeline based on DASH (Shen et al. 2022)and ASHA (Li et al. 2020). The results show that foundation models are not
able to consistently beat supervised tuned baselines across these domains.

### Strengths
Foundation models are a hot topic in various machine learning research domains, and it is important to have appropriate evaluation regimes that can demonstrate the efficacy or show weaknesses in developed models and test whether they are able to deliver on their promises. Therefore, the research question posed by the authors is highly relevant and of importance to the community. Similarly, it is good that the authors focus on a rather straightforward simple baseline tuning technique that can be employed across domains.

### Weaknesses
I do understand the authors' idea and motivation to show subpar performance of foundation models against a well tuned supervised baseline across different domains. However, by attempting to do this across quiet different domains, I believe that the paper and methodology is falling short of the specific nuances of each of the included subdomains of genomics, time-series and satellite data.

I will mainly attempt to make this point for the satellite data domain as this is the most closely related one to my background among the three:
- Earth Observation (EO) data encompasses a wide array of sensors and modalities. Additionally, there are a diverse set of tasks, classification, segmentation and pixel-wise regression just to name a few for optical data. Foundation models aim to perform well across these tasks based on a common encoder that yields relevant representations that can then be "decoded" for the task at hand. However, while you do select several classification datasets, the evaluation is limited to classification and does not include segmentation which is arguably more relevant in EO. Therefore, I would argue it is difficult to make your overall claim, if you do not compare across EO tasks, for example including segmentation, as this would align more with the premise of FMs. The authors should acknowledge that their conclusions are limited by this task selection.
- In line 352 you say "we only consider a restricted subset of top-performing, open-source, and compatibly-formatted models". However, I would believe that there are other relevant and easily accessible recent models available like Clay, Scale-MAE, the Satlas-model, or DOFA that include evaluations against your chosen models of CROMA and Sat-MAE. The lack of a comprehensive comparison to these models limits the generalizability of the findings.
- Regarding the experimental findings, I would argue that this is not necessarily new, because there are works that already show strong performances of supervised baselines. For example in the Prithvi by Jakubik et al. Table 4 you observe the competitive UNet performanceand that for subclasses it is often better than the FM. Similarly, in DOFA by Xiong et al., Table 1 and 2 show that fully trained supervised baselines can sometimes beat the finetuning schemes. More general a work by Corley et al. conducted a focused study around pretrained weights and demonstrated that carefully finetuned baselines are very competitive. The authors need to more clearly differentiate their contributions from these existing findings.
- From Table 6 it seems that you have conducted the experiments on quiet large datasets in the domain. However, the more interesting application of FMs is for fine tuning on datasets with scarce/few labels where training a model from scratch would likely just lead to over fitting. This domain relevant scenario is not considered here. The authors should include experiments that evaluate the performance of FMs in low-data regimes.

Given that for the satellite subdomain only a subset of existing FMs were used for classification (which is understandable since this requires significant experimental effort), I think some of the author's general statements do not follow the methodology. For example, the authors lead their discussion by stating in line 470 that "At a high level, our results show that the foundation models in these three domains have not yet surpassed supervised learning" but the selected methods are not representative of "the foundation models in the domain as illustrated for satellite data. As I said in the beginning, I believe that there are too many nuances within the separate domains that can be all included in one paper and allow for the conclusions that the authors draw.

### Questions
General Questions:
- I don't really understand the importance of including a ResNet and a UNet, as models for classifcation. From my understanding a UNet is an architecture choice where you need the model output to also be a HxW similar to the input. For classification this would imply that you have to include additional layers to get from that output to a vector-valued classification prediction. Additionally, I think a UNet can have all sorts of different convolutional or transformer encoders, including a ResNet, for example see [here](https://github.com/qubvel-org/segmentation_models.pytorch). Having access to the code would probably answer this question.
- In line 255, you state that beyond a subset of the GeoBench classification tasks you also include BigEarthNet, and EuroSAT, as well as two additional ones. However, BigEarthNet and EuroSAT are already included in GeoBench
- CROMA takes as input an optical and/or sar image as the code suggests [here](https://github.com/antofuller/CROMA/blob/59505a6bcadbf36ba20767270154bf9f3067c5e7/use_croma.py#L90). I wonder how that is handled across the selected different classification datasets, as it was not entirely clear to me from the appendix around line 953
- Is it possible to look at the code already which could help answer some of these questions?

Other Comments:
- in line 261 you state that "satellite imaging closely resembles RGB imaging" but that is only true for some optical satellites. Radar Satellites as well as other images are very different than RGB

Minor Comments:
- line 525 there is a typo in the word "work"
- I don't find the acronym "NAS" to be introduced. Also in line 191 you say "neural architecture search" where you use NAS beforehand already

### Soundness
2

### Presentation
3

### Contribution
2
