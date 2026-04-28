# Mitigating Mode Collapse in Sequential Disentanglement via an Architecture Bias

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 6, 5, 1

## Abstract
One of the fundamental representation learning tasks is unsupervised sequential disentanglement, where latent representations of the inputs are decomposed to a single static factor and a sequence of dynamic factors. To extract this latent information, existing variational methods condition the static and dynamic codes on the entire input sequence. Unfortunately, these models often suffer from mode collapse, i.e., the dynamic vectors encode static and dynamic information, leading to a non-meaningful static component.  Attempts to alleviate this problem via reducing the dynamic dimension and mutual information loss terms gain only partial success.  Often, promoting a certain functionality of the model is better achieved via specific architectural biases instead of incorporating additional loss terms. For instance, convolutional nets gain translation-invariance with shared kernels and attention models realize the underlying correspondence between source and target sentences. Inspired by these successes, we propose in this work a novel model that mitigates mode collapse by conditioning the static component on a single sample from the sequence, and subtracting the resulting code from the dynamic factors.  Remarkably, our variational model has less hyper-parameters in comparison to existing work, and it facilitates the analysis and visualization of disentangled latent data. 
We evaluate our work on multiple data-modality benchmarks including general time series, video, and audio, and we show beyond state-of-the-art results on generation and prediction tasks in comparison to several strong baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an approach to learning disentangled representations while mitigating mode collapse in sequential datasets. They propose an approach by which models extract static and dynamical properties independently by anchoring the former in the initial input in the sequence processing the latter inputs as an offset of the former in representation space. The introduce latent penalties to accommodate for this modification and encourage sequential disentanglement. They then proceed to extensively test their proposal on a number of datasets while comparing it with previous work.

### Strengths
1. The model is well motivated based on limitations of previous work.
2. The description of the model and the derivation of novel penalties is clear and easy to follow.
3. Potential issues are described and the authors even address why their method fails to surpass a performance threshold on one specific dataset.
4. To the best of my knowledge they compare against relevant approaches.
5. The model is tested on a substantial amount of datasets.

### Weaknesses
1. Some figures are not very clear. For example in Figure 4 what is swapped? Is it the face or the expression? The caption should contain this information.
2. Some of the results for example in Table 1 make the model seem way less impressive. While indeed the model surpasses all the others, the increase in performance is somewhat small. Thus I don't think being SotA is the most compelling argument for this approach.
3. Similarly, there doesn't seem to be much disentanglement of the different properties in the Air Quality dataset.
4. The lack of empirical evidence regarding mode collapse is a significant weakness. The authors claim this is a key advantage, but do not provide any quantitative comparison to alternative models. This makes it difficult to assess the practical impact of their proposed method in this regard.

### Questions
1. Given that the authors stress the importance of mitigating mode collapse as an advantage of their model, why is there no comparison on how prevalent this issue is between their model and the alternatives? Given that as I have previously said the improvement in performance is not that great, then this would be an alternative way to support the idea that this is indeed a substantial improvement over previous approaches.
2. Similarly, I would like to see latent plots of alternative models as a way to compare the disentanglement properties of this approach.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors try to learn disentangled representations for time series data with time-invariant factors and time-dependent factors, by proposing to define a specific form of approximate variational posterior. Specifically, they encode the first data point in a time series into the time-invariant factors, such that they can "subtract" it from the subsequent data points. The authors claim that this can improve the disentanglement between these two types of factors of variation.
Empirically they evaluate their method on multiple time series datasets and compare with different baselines, and they show that their approach outperform the baselines.

### Strengths
Their work is well motivated in the sense that it is challenging to disentangle time-invariant factors and time-dependent factors on time series data, particularly on high-dimensional data (e.g., videos). The paper is well-structured and clearly written. The math in the methodology section is detailed and sound, to the best knowledge. Finally, they provide sufficient experimental results in the evaluation.

### Weaknesses
I don't fully understand why we would want to have the time-invariant factors encoded merely from one single data point in a time series. Intuitively, the time-invariant and time-dependent factors are entangled at each time step, and there are time steps where those factors are more difficult to disentangle. For example, one video frame where 2 moving objects are highly cluttered while we want to disentangle their appearances (time-invariant) from their locations (time-dependent). Thus I would imagine that it is actually more reasonable to get some form of "average" across all time steps because that "average" is the part that does not change across time and, hence is the time-invariant factor. I understand that prior work sometimes has challenges in learning such disentangled representations for high-dimensional data, but I personally don't think merely picking up one single data point and encoding it into time-invariant can resolve this problem in general. Consider that case where the first data point is the more entangled data point across the whole time series, then you wouldn't get good representations at the beginning, thus the conditioning in the posterior of time-dependent factors would introduce bias. This is my main concern of the method in this paper.

### Questions
I don't have technical questions so far. My main question was in the previous section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a sequential disentanglement model designed to separately learn the static component and dynamic factors. The model subtracts the static content from the series of learned dynamic factors. The authors then evaluate its performance on various data-modality benchmarks.

### Strengths
- The manuscript is written clearly and is easy to follow. 
- The motivation of static posterior is conditioned on a single series element is reasonable. The implementation of learning the static factor independently of the sequence is reasonable.
- The authors conduct extensive experiments to evaluate the effectiveness.

### Weaknesses
 - I am worried about how to ensure that s contains only static features. The authors claim that static factors can be extracted from a single frame in the sequence, which is not a necessary and sufficient condition. Otherwise, any frame from the video can be used. Why the first frame?
- In addition, in Equation 8, if s contains dynamic factors, subtracting s from the dynamic information may result in the loss of some dynamic information, making it difficult for the LSTM module to capture the complete dynamic changes.
- The method of removing static information from dynamic information is by subtraction between features, which is quite naive.

### Questions
- How to ensure that small time-varying vectors are captured?
- Does the length of the time series affect the performance of the model?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of sequential disentanglement in which the goal is to learn representations for two factors that give rise to the observations: i) the time-invariant (static) features that are shared across all images within a sequence; ii) time-varying (dynamic) features that change along the sequence. The authors describe a common failure mode of existing models in which the static features ‘leak’ into the dynamic features representations, and propose a method to encode the static features only from the first observation in a sequence. The approach relies on a model with architecture inductive bias to learn the dynamic features from all the remaining observations. The method is benchmarked on several sequential datasets with different modalities.

### Strengths
1. The study of sequential disentanglement is well-motivated as videos are a major modality in real-world data.
2. The paper is well-written and easy to follow.

### Weaknesses
1. Technical claims put forth in this paper appear somewhat misleading in my evaluation.
The authors claim that subtracting the static representation from the dynamic representation induces an architectural bias and “removes” static features from leaking into the dynamic features. It is not clear to me why this subtraction may encourage removing static information since the static and dynamic representations are not embedded into the same latent space. In fact, they are not interchangeable when input into the decoder i.e. are not separate full-dimensional latent vectors within a same latent space; rather, these representations are concatenated to form the entire image encoding. Consequently, I fail to discern any relationship between this architectural approach and a potential inductive bias.

2. Following my previous point, I do not understand why the embeddings of static and dynamic features are being plotted along each other in Fig. 2. According to my understanding, static and dynamic are components / dimensions that form concatenated latent vectors, so what is the meaning of plotting different dimensions within the same embedding space? Why should they align or be distinct? For example, each dimension can follow same gaussian distribution, but still represent different features, as the decoder can apply any function to the latent vector (which is the concatenation of static || dynamic).

3. The quantitative evaluation includes only image-level metrics (derived from pre-trained classifiers). I believe it would be very valuable to conduct evaluation at the representation-level to measure the disentanglement quality, as the metrics proposed in [1].

4. I think the concept of ‘Mode collapse’ is often attributed to unconditional generative models and might mislead the reader. It may be better to use a different terminology to describe the degeneration problem in the context of disentanglement.

### Questions
1. The quantitative evaluation includes only image-level metrics (derived from pre-trained classifiers). I believe it would be very valuable to conduct evaluation at the representation-level to measure the disentanglement quality, as the metrics proposed in [1].

2. Could the author compare their method to class-content disentanglement methods as [1]? Class could be treated as the static features and content could be referred to as the dynamic features.  

3. I think the concept of ‘Mode collapse’ is often attributed to unconditional generative models and might mislead the reader. It may be better to use a different terminology to describe the degeneration problem in the context of disentanglement.

[1] Gabbay and Hoshen. “Demystifying Inter-Class Disentanglement”. In ICLR, 2020.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
