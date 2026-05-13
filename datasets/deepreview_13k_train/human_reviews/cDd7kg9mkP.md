# SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
In this work, we bridge the gap between wearable sensor technology and personalized AI assistants by enabling Large Language Models (LLMs) to understand time-series tasks like human activity recognition (HAR). Despite the strong reasoning and generalization capabilities of LLMs, leveraging them for sensor data tasks remains largely unexplored. This gap stems from challenges like the lack of semantic context in time-series data, computational limitations, and LLMs' difficulty processing numerical inputs. To address these issues, we introduce SensorLLM, a two-stage framework to unlock LLMs’ potential for sensor data tasks. In the Sensor-Language Alignment Stage, we introduce special tokens for each sensor channel and automatically generate trend-descriptive text to align sensor data with textual inputs, enabling SensorLLM to capture numerical changes, channel-specific information, and sensor data of varying lengths—capabilities that existing LLMs typically struggle with, all without the need for human annotations. Next, in Task-Aware Tuning Stage, we refine the model for HAR classification using the frozen LLM and alignment module, achieving performance on par with or surpassing state-of-the-art models. We further demonstrate that SensorLLM evolves into an effective sensor learner, reasoner, and classifier through Sensor-Language Alignment, enabling it to generalize across diverse datasets for HAR tasks. We strongly believe our work lays the stepstone for future time-series and text alignment research, offering a path toward foundation models for sensor data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
SensorLLM paper presents a novel time-series (TS) data to language alignment focusing on training an alignment module that bridges a pre-trained LLM and a pre-trained TS embedding. 
The proposed foundational model intends to provide a methodology for analyzing TS data into user-understandable explanations. Developed in 2 components, first a sensor-to-language alignment through the introduction of an MLP alignment module. A second module for task-aware tunning that provides human activity recognition classification capabilities.

### Strengths
1. Open-source code already available
2. Comprehensive evaluation in 4 datasets evaluating meaningful language representations from test sets.
3. The appendix was well developed, explaining the SOTA, details of datasets and many examples of results provided in their model.
4. Very well-implemented set of metrics for evaluation of sensor data understanding.

### Weaknesses
1. The architecture description of their task-aware model was not comprehensive. A diagram of each architecture would help. Specifically, the interaction between the alignment module, the time-series embedder, and the classification head is unclear. It's not evident how the outputs of the alignment module are fed into the classification head, and what type of classification head is being used (e.g., linear layer, multi-layer perceptron). The description lacks detail on the specific operations performed, such as whether the alignment module output is directly used or if there are additional transformations before classification.
2. Innovative points on the architecture could be better explained. Although explained sometimes it is not clear what is the contribution of their own architecture. For instance, the role of the special tokens for each sensor channel is not well-defined. It's unclear how these tokens are incorporated into the model and what specific advantage they provide. The novelty of the alignment module itself is not fully justified; it is unclear why a simple MLP was chosen, and whether other alignment strategies were considered or evaluated. The authors should explain why their specific architectural choices are better suited for the task than other possible alternatives.
3. A slight lack of explanation of the process followed by the 5 human experts - it would be nice to have a short description of how the data was presented and evaluated, as well as, who these experts are (level of knowledge and in what domain?)
4. Comparison with SOTA methods in A.6 was not clear, the short description of the results on page 9 (lines 447-455) does not provide clear baseline results. The reported results for the baselines are not detailed enough, and it is not clear if all baselines were trained on the same data splits and pre-processing steps as the proposed model. This lack of clarity makes it difficult to assess the true performance gains of the proposed approach.
5. Baseline methods were not placed properly in the SOTA, especially for the task-aware Human Activity Recognition (see Q.5). The baselines used for comparison are not clearly justified, and it's not evident if they represent the state-of-the-art for the specific datasets and tasks considered. For example, the authors should justify why specific models were chosen and how they compare to other relevant methods in the field of time-series classification and human activity recognition.

### Questions
1. How many classes were used on each dataset?
2. Why are the baseline methods evaluated with current best-trained models for the datasets used: e.g, F1-scores on PAMAP2 0.86 (Essa & Abdelmaksoud, 2023), MHealth: 0.94(Suh et al., 2023), 0.83 USC-HAD (Essa & Abdelmaksoud, 2023), and so.
3. In sensor understanding, the comparison is done only with GPT-4o, is not there any other method yet existing to reference in sensor data description?
4. what is the architecture of the task-aware tuning module? how many parameters? 


References:
Ehab Essa and Islam R. Abdelmaksoud. Temporal-channel convolution with self-attention network for human activity recognition using wearable sensors. Knowledge-Based Systems, 278:110867, 2023. ISSN 0950-7051. doi: https://doi.org/10.1016/j.knosys.2023.110867.
Sungho Suh, Vitor Fortes Rey, and Paul Lukowicz. Tasked: Transformer-based adversarial learning for human activity recognition using wearable sensors via self-knowledge distillation. Knowledge- Based Systems, 260:110143, 2023. ISSN 0950-7051. doi: https://doi.org/10.1016/j.knosys. 2022.110143.

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
4

### Summary
This paper focuses on the problem of enabling state-of-the-art text-only LLM to ingest and understand time-series sensor data. The authors use a pre-trained time-series embedding model (Chronos) to generate sensor data embeddings and train a sensor-language alignment module to map them into Llama-3's input space. Then, on given text prompt + mapped sensor data embeddings as an input to Llama-3, author train a small MLP classifier for human activity recognition (HAR) on the final token embedding of the last layer of Llama-3. 

Authors compare their method with state-of-the-art HAR models on four datasets and they also GPT-4o performance as an additional baseline.

### Strengths
The paper's strengths are following: 

- The paper is well-written and the approach is described in detail. It was relatively easy to follow what authors are proposing and how they implemented it. 

- Authors do a good job in comparing their approach with a variety of state-of-the-art HAR models in the literature. The comparison plots are clear. 

- I think, the problem that authors are trying solve (enabling text-only LLMs to understand time-series sensor data) is an important and relevant problem.

### Weaknesses
There are some major weaknesses in author's approach as listed below: 

* It is not at all clear what value LLM (Llama-3 8b) is adding in the author's approach: 

Author's essentially use frozen TS-embedding model (Chronos) + fine-tuned MLP + frozen LLM (Llama-3) as a feature extractor, followed by fine-tuned MLP as an HAR classifier. I think, it is a significant overkill to use a versatile model like Llama-3-8b within a fixed multi-class HAR classifier. There is no exploration of zero-shot classification or any generating any reasoning or explanation behind a given inference using Llama-3. In fact, since the authors' sensorLLM is just a fixed multi-class classification model, it is almost a misnomer to call it an "LLM". 

* The empirical accuracy gains in HAR are small or non-existent compared to state-of-the-art (and *simpler*) HAR model: 

In figure 4, authors compare their approach with a set of state-of-the-art HAR works. On three out of four datasets, the F1 score bar for proposed sensorLLM overlaps with F1 score bar for Attend work (Abedin et al., 2021). Note that the sensorLLM has two huge models in sequence, Chronos (~100 M parameters) and Llama-3 (8 Billion parameters), whereas the Attend method just has a plain convolutional backbone followed by GRU and attention layers. So, most likely, the SensorLLM model is about *two orders of magnitude bigger* that Attend model. Despite this gigantic difference in the size, on UCI-HAR dataset, *fine-tuned* SensorLLM achieves lower F1 score than Attend. This further supports the first point above that the use & value of LLM in sensorLLM is really unclear. 

In fact, Chronos + MLP HAR classifier is an important baseline that authors should include. 

* TS-language alignment methodology is questionable: 

For sensor-language alignment training, authors generate the alignment training data as follows: given a sensor data time-series, authors run some signal processing algorithms to identify trends in the time-series (e.g. increasing, almost-stable (slope $\approx$ 0), decreasing). Then authors generate some prompt & QA templates using GPT-4 where the trend descriptions are edited automatically by filling in the results of the above signal processing algorithm. My question is: why ask LLM to generate an output that can easily be generated by some *simple* signal processing and template coding? 

* No evaluation/ablation using other LLMs (maybe the gains are only coming because of Llama-3?) 

The authors keep Llama-3-8b weights frozen throughout and explain their method as if it can work with any off-the-shelf frozen LLM. However, there are no results using any other LLM. Authors really need to show that their approach (of sensor-language alignment) works for different state-of-the-art LLMs. It would be a significant weakness if authors find out that the method gives worse results for other LLMs.

### Questions
Authors really need to justify their problem formulation of using state-of-the-art, versatile LLM within a restrictive supervised multi-class classification problem. The general direction of enabling to understand sensor data is interesting and that capability has much potential (e.g. LLM being able answer questions on a given stream of sensor data). I don't using LLM and then doing discrete activity classification problem makes sense. In fact, authors should look at [Listen, Think, and Understand, ICLR'24](https://openreview.net/forum?id=nBZBPXdJlC) paper as an example about the promise of LLM's potential QA abilities on input sensor data. 

I have listed all my remaining questions in "Weaknesses" section. If authors point out anything that I may have misunderstood there, I am willing to change my score during rebuttal.

### Soundness
2

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
The authors propose an approach to leverage LLM based trend analysis of sensor data for contextual understanding. A direct approach to this would require large scales of sensor data at least, and labels that are suitably rich. The authors focus on human activity recognition as the application, which has been well studied. They propose a two stage approach including an alignment step from pre trained time series encoding to intermediate descriptive task in language domain and final task specific adaption step for the human activity recognition. They have compared performance with time series methods and comparable LLM based approaches.

### Strengths
The work demonstrates limited originality in terms of attempting to fuse time series data with language model inference. It readily draws upon existing time series encoding paradigm and LLMs with limited training novelty via the MLPs. It address a practical problem by focusing on human activity recognition which has a broad spectrum of potential applications. The treatment is somewhat rigorous in terms of ablations and comparisons to prior art. There do remain considerable areas of concern and gaps.

### Weaknesses
The article purports computational complexity as a reason for pursuing this approach over classic time series. However it seems to not acknowledge the fact that the LLM as well as the TS encoder have required significant computational resources already. Further, the the ability of LLMs to comprehend TS embedding derived trends in a quantifiable sense remains a key open. The training data representation and is quality determines success at this task and there is no guarantee established thus far to this effect in prior work. The baseline methods chosen while interesting, have been trained on very limited data in comparison to the LLMs or even the TS encoder. Thus, comparisons drawn without controlling for the model complexity in themes of the effective number of parameters and data size, don’t seem fair. There are pre trained models on larger public domain data sets that have shown efficacy to HAR such as LIMU BERT or the work leveraging UK bio bank data seem relevant for fair comparison at least. Lastly, the expressive utility of the embedding alignment of time series will be limited by how expressive the trend descriptions can be and to that effect, it is unclear what the capacity is to do so for complex signal representations. This attempts to auto learn features based on language description or perhaps assume some low rank space in which the features exist. In many real world problems, while the low rank assumption is true, it requires a lot of scale and nuance to discover this expressivity.

### Questions
A true computational complexity comparison should include that of the TS encoder and the LLM itself. Could we compute a baseline including these and compare?

How might we be able to validate the assumptions on the LLM on being able to auto generate the trend results? What benchmarks exist here? Thus far, direct mathematical inference on even basic questions have been seeing questionable performance by LLMs unless a lot of care is given to avoid hallucinations.

Could we consider and evaluate pre train+fine tuned HAR models as part of the perf comparison baseline?

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
4

### Summary
Human activity recognition (HAR) is an important application for wearable sensor data.
However, a major limitation of HAR is the lack of large-scale labeled datasets due to the cost of time series annotation.
This paper proposes a SensorLLM that enables LLMs to understand sensor time series. The goal is
utilize well-performing LLMs to understand sensor data for which the pre-trained model is rather limited.

The SensorLLM proposed has two main components, one that alignment the sensor with language and another one that does fine-tuning 
for the downstream HAR tasks. The sensor language alignment was done to summarise the trend and other descriptive analyses of the sensor time series to train an alignment module. This alignment module takes in the raw sensor signals and generates sensor data embedding, which is then concatenated with other textual prompts. 

The SensorLLM has shown superior performance on four benchmark datasets in HAR. Furthermore, the prompts engineered and alignment modules appear to be essential for good performance, which are key contributions of this manuscript.

### Strengths
1. This paper addresses an important problem to enable LLMs to understand sensor time series for which we don't have a good solution yet.
2. The proposed SensorLLM provides a general formulation for sensor data that can handle different data modalities, which is well appreciated.
3. In order to train the sensor-language alignment module, the authors used a variety of different question-answer pairs to prompt the LLMs to understand trends and simple statistical estimates from the sensor data. It is a nice way to adapt the time series embedding as inputs for language models. The data generation process is an interesting way to obtain sensor embeddings without labelled data.
4. The schematic diagram Fig 2 is clear

### Weaknesses
While this manuscript proposes an interesting SensorLLM framework, the motivation of this work can be better clarified. Various parts of this manuscript need more rigour.

1. As the authors stated, existing HAR models are task-specific and struggle to scale across sensor configurations. However, the authors replied in saying that they would like to address this issue by improving the interpretation of the sensor data. I don't believe this is what SensorLLM is about. If so, please provide evidence in how the work enhance the interpretation of sensor data via LLMs.

2. The evaluations used are limited. HAR benchmarks are oftentimes small in nature. In the three out of four benchmarks used, only <= 3 subjects are used as test set. For the evaluations for LLMs, it is extremely easy to overfit because of the model capacity. I would highly suggest the author to include larger benchmark datasets such as Capture24 or also report the performance using held-one-subject-out.

3. In the design of the time series and language alignment, the text used as LLM output are trends, and simple statistics without considering the amplitude of the signal at all, which is an important aspect of motion time series. It is easy to conceive a situation of very little movement but small upwards/downwards trends. But the activity classes can be totally different.

### Questions
1. How are the data preprocessed for each dataset? sampling rate, data augmentation, window length? 
2. A small set of trainable weights don't imply the training will be efficient. Training efficiency is evaluated w.r.t. the number weights.
3. How the synonymous versions of your QA generation help with the training? Do they actually provide performance boost? 
4. HAR in free-living environment is quite messy. What's the intuition behind that knowing the trends of the sensor data is sufficient for HAR? 
5. How is GPT40 used as a baseline? More details are needed.
6. How is the cross-dataset experiment in T3 implemented? They share the same channels but they don't share the same activity classes?

### Soundness
3

### Presentation
2

### Contribution
2
