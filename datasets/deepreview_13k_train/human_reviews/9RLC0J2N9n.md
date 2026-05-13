# SynBench: Evaluating Pretrained Representations for Image Classification using Synthetic Data

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Fine-tuning large models pretrained at scale on broad data for solving downstream tasks has made considerable success in recent years. There seems to be indeed an ongoing paradigm shift in deep learning from task-centric model design to task-agnostic representation learning and task-specific fine-tuning. Specifically, the representations of pretrained models are used as a foundation for different downstream tasks. This paper proposes a new task-agnostic framework, \textit{SynBench}, to measure the quality of pretrained representations for image classification using synthetic data. To address the challenge of task-agnostic data-free evaluation, we design synthetic binary classification proxy tasks with class-conditional Gaussian mixtures. This way we probe and compare the robustness-accuracy performance on pretrained representations and input synthetic data. SynBench offers a holistic quantitative evaluation, informs the model designers of the intrinsic performance, and spares efforts on task-specific finetuning with real-life data. Evaluated with various pretrained vision models for different downstream image classification tasks, the experimental results show that our SynBench score matches well the actual linear probing performance of the pretrained model when fine-tuned on downstream tasks using real-life data. Finally, SynBench can also be used in robust linear probing to mitigate the robustness-accuracy tradeoff in downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces SynBench, a task-agnostic framework designed for the evaluation of pre-trained representations using synthesized data derived from data prior. Notably, SynBench is independent of downstream image classification datasets or tasks. The experimental results demonstrate a strong correlation between SynBench scores and the model's performance as assessed through measures of adversarial robustness and standard accuracy. Additionally, SynBench proves to be helpful for guiding the design and selection of hyperparameters in robust linear probing.

### Strengths
- It is interesting to design a proxy task for the quality evaluation of pre-trained representations. This approach offers a fresh perspective on assessing the quality of representations without relying on downstream datasets. 

- Experiments show the effectiveness of SynBench-Scores in indicating real-life task accuracy.

- The paper demonstrates a high level of quality in its methodology and experimental design.

### Weaknesses
 - Robustness to Deviating Distributions 

  It would be valuable to assess SynBench's robustness when facing uncommon real-world data distributions. For instance, applying SynBench to datasets like DomainNet, which contains diverse and domain-shifted data, can provide insights into its adaptability to varying data sources and distributions. Demonstrating SynBench's effectiveness under such conditions would strengthen its applicability and reliability.


- Scalability to Tasks with More Classes

   The paper primarily uses datasets with limited categories for experiments. It's important to explore how SynBench performs on tasks with a more extensive range of classes, such as ImageNet.  It would help understand the framework's scalability and whether it maintains its effectiveness when applied to larger and more complex datasets. This expansion of experiments can provide a clearer picture of SynBench's utility across diverse tasks.

### Questions
see Weaknesses

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes SynBench, a method to evaluate the representations of pretrained models using synthetic data. The synthetic dataset is a class-conditional Gaussian in a binary classification setting. The proposed metric measures the accuracy and robustness on this constructed synthetic dataset (proxy task). SynBench-score is then defined as the ratio of area-under-curve between the representations obtained from pretrained models and the reference. The results on various image classification tasks demonstrate that SynBench-Score vastly outperforms baseline methods across wide range of supervised and self-supervised pretrained models. The paper also delves into the potential applications of this metric, discussing scenarios where it could be beneficial.

### Strengths
1. The paper provides a very comprehensive set of results with various backbones where SynBench-Score outperforms the baseline methods. The correlation of SynBench-Score is quite high even with limited number of samples.
2. Practically, this can potentially be a very useful metric given that it does not require any real data. The motivation of the paper is well explained and the authors give various scenarios where this metric would be useful.
3. Overall, this is mostly a complete paper with the authors discussing runtime analysis, limitations and the algorithm of SynBench.

### Weaknesses
The authors only consider the linear probing paradigm in evaluation of pretrained models. In practice, finetuning is also a common way to use these pretrained models. It is not clear how this metric would perform in the finetuning setup.

### Questions
1. What is the number of test samples in the synthetic dataset? I am not sure if I saw this in the paper.
2. In the Algorithm (A.6), what are $z_1$ and $z_2$ in Line 12?
3. It would be interesting to analyse the correlation on a subset of tasks instead of average of 27 tasks. For instance, it may be the case that metric performs better on OOD tasks compared to transfer learning on some datasets.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a task-agnostic evaluation framework based on synthetic data to estimate how well pretrained representations transfer to downstream tasks, and how robust they are. Concretely, the paper proposes to generate data from a mixture of Gaussians, and to measure how well separable according to mixture correspondence this data is when embedded with a pretrained representation network, compared to how separable the data is in the input space. The paper derives a corresponding theory, proposes a benchmark score and numerically investigates how well this score correlates with the robustness and transferability of different representations to a variety of tasks.

### Strengths
Better quality and more efficient evaluation methods are an important area of active research. Model robustness, while having been improved with increased model and data size, is still unsolved. The paper aims to address both these aspects. Further, further since the proposed method relies on synthetic data, it can avoid issues related to privacy and mitigate undesired biases.

### Weaknesses
I generally found the paper rather hard to follow. It is often unclear if the authors are targeting adversarial robustness, or how well a representation transfers or both.

I might well have missed a central point of the paper, but I fundamentally doubt that it is possible
1. solely based on Gaussian mixtures with two components,
2. without any knowledge about the target downstream tasks,

to accurately predict classification performance of feature extractors across a broad range of downstream tasks. The baselines such as (Whitney et al., 2020) all rely on measures that are derived from the feature extractor and the downstream task/data, whereas the current method performs the predictions solely based on the feature extractor and synthetic data, while claiming to outperform the baselines. 

Another aspect that I found surprising is that the theory does not depend on the properties of the pretrained feature extractor, for example its Lipschitz constant, which is usually the case in similar contexts.

Overall, I cannot recommend acceptance at this point without further clarifications from the authors.

### Questions
I could not find any individual results of the proposed method on the 27 tasks from (Radford et al.) (the correlation is plotted in Figure 4). I would be interested to see the SynthBench score per task and model, and how well it correlates with downstream performance per data set.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the problem of evaluating the quality of a pretrained model (for classification) without any data from or knowledge of the downstream tasks for which it will be used. The idea is to generate binary classification data from a Gaussian mixture model and evaluate how well the representation separates the two classes relative to a theoretically optimal classifier. Models are evaluated in terms of standard accuracy and $\epsilon$-robust accuracy (in a certain adversarial sense). Depending on the experiment, evaluation metrics are based on CIFAR10, SVHN, TinyImageNet, or the average performance over the 27 benchmark tasks from the CLIP paper.

Generally, this paper was interesting to read and clear, but there are some issues that need to be addressed before it is ready for publication.

### Strengths
* The goal of the paper is ambitious. If the paper solved the problem they pose, it would be very impactful. 
* The paper considers its data and results from a number of interesting perspectives, speaking to a general concern for thorough evaluation. 
* The idea put forth in the paper is interesting and worthy of further exploration.
* The paper is well-edited and clearly written.

### Weaknesses
* The paper assumes that the raw input data for each class has a Gaussian distribution. In computer vision, this means assuming that, in pixel space, two visual categories have Gaussian distributions. This is akin to assuming we start with quite a good representation! What's the point of representation learning if that's where we start? Why would you transform your data?

* One of the key claims of the paper is that the "Pearson correlation between SynBench-Scores and the average real-life task accuracy is larger than 0.9". Flipping to Table 7 in the appendix, we learn that these Pearson correlations are based on $n=5$ data points! It is statistically unacceptable to make this claim without reporting confidence intervals. Running through the standard calculations, it seems to me that the confidence interval for the Pearson correlation of 0.92 would be $[-0.81, 1.0]$. That is, this correlation value is not very meaningful. This seems to be a highly misleading error, but I'm eager to be corrected if I'm off base on this point. In the absence of this claim, there is little evidence that "real world" task performance is related to the scores computed in this paper. The sample size of $n=5$ is likely too small to draw strong conclusions about Pearson's $r$, especially given the wide confidence intervals.

* There are many hyperparameters in this paper and no mention of hyperparameter tuning, e.g "$a_t$ ranging from 0.7 to 0.9" or "$\epsilon$ from 0 to 0.8" or "attack strength 0.2" etc. Can details be provided? If not, the reader should probably assume that the hyperparameters are charitable to the proposed method. The lack of details regarding hyperparameter selection makes it difficult to assess the robustness and generalizability of the proposed method.

* SimCLRv2 has the highest SynBench-Score in Table 1, but is generally understood to perform more poorly than the other techniques in the table in common evaluation protocols (see e.g the papers for DINO, BYOL, MAE, or other more recent methods). No mention is made of this in the discussion. This seems like a fairly large problem for the proposed method. Specifically, the apparent discrepancy between the high SynBench-Score of SimCLRv2 and its relatively lower performance in other evaluations raises questions about the effectiveness of SynBench in capturing practically relevant aspects of representation quality.

* The paper considers CIFAR10 and TinyImageNet as "real-life downstream data" (see Sec. 4.3) - I think many in computer vision would disagree with this characterization.

* The paper cites Zoran and Weiss 2012 to support the claim that natural image statistics can be well-represented by GMMs. However, that work focuses only on small image patches and (as far as I know) makes no claim that entire natural images can be well-represented by GMMs. Isn't this a misleading use of that reference? (Appendix A.1). The application of GMMs to entire images, as opposed to patches, requires further justification, especially given the differences in statistical properties between image patches and full images.

### Questions
See "Weaknesses" for supporting details on these questions.
1. A few big picture conceptual questions: Why should we even think it's possible to evaluate the quality of a representation for arbitrary classification tasks without any knowledge or data related to downstream tasks for which it will be used? Moreover, why should we think it's possible to boil that down to a single scalar? What does "quality" even mean without reference to downstream tasks?
2. Are the Pearson correlations appropriately reported (see weaknesses)? Absent that, is there strong evidence that the method in the paper produces scores that are predictive of performance on downstream tasks? 
3. Why is it not a problem for the proposed method that SimCLR has the highest score in Table 1, despite being generally understood to underperform DINO and supervised pretraining? 
4. The Gaussian assumption is basically an assumption that we start with a very good representation - this seems pretty unrealistic. Why would we bother transforming our data with a pretrained model at that point? 
5. Is the reference Zoran and Weiss used appropriately in Appendix A.1? 
6. How were the hyperparameters in this paper tuned?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
