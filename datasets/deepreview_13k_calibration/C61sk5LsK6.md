# InfoBatch: Lossless Training Speed Up by Unbiased Dynamic Data Pruning

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Data pruning aims to obtain lossless performances with less overall cost. A common approach is to filter out samples that make less contribution to the training. This could lead to gradient expectation bias compared to the original data. 
To solve this problem, we propose \textbf{InfoBatch}, a novel framework aiming to achieve lossless training acceleration by unbiased dynamic data pruning. Specifically, InfoBatch randomly prunes a portion of less informative samples based on the loss distribution and rescales the gradients of the remaining samples to approximate the original gradient.
As a plug-and-play and architecture-agnostic framework, InfoBatch consistently obtains lossless training results on classification, semantic segmentation, vision pertaining, and instruction fine-tuning tasks. On CIFAR10/100, ImageNet-1K, and ADE20K, InfoBatch losslessly saves 40\% overall cost. For pertaining MAE and diffusion model, InfoBatch can respectively save 24.8\% and 27\% cost. For LLaMA instruction fine-tuning, InfoBatch is also able to save 20\% cost and is compatible with coreset selection methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a dynamic data pruning approach that can obtain lossless performances with less training cost.
It achieved the unbiased gradient update by randomly pruning a portion of less informative samples and rescaling the gradient of the remaining samples. The proposed approach consistently obtains lossless training results on various ML tasks.

### Strengths
- Clear presentation and easy-to-follow writing.
- The proposed method is theoretically-supported and, more importantly, very efficient and easy to implement.
- The evaluation, together with the analysis, is extensive and convincing.

### Weaknesses
The paper conducts a complete study on dynamic data pruning, and the following weakness is relatively minor.
- Missing recent works: 1) static data pruning [1,2,3], 2) dynamic data pruning [4]

[1] Active learning is a strong baseline for data subset selection. NeurIPS workshop, 2022

[2] Moderate: Moderate coreset: A universal method of data selection for real-world data-efficient deep learning. ICLR, 2023

[3] CCS: Coverage-centric Coreset Selection for High Pruning Rates. ICLR, 2023

[4] Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt. ICML, 2022

### Questions
- How to illustrate the gradient trajectory with landscape in Fig 1? Is it an illustration or a real plot on some dataset?
- Which dataset is used for Table 4? maybe ImageNet?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents InfoBatch, a novel data pruning approach which dynamically determines pruning probability over the course of training. InfoBatch soft prunes data with small loss value leading to negligible training cost overhead, and rescales remaining data so as to achieve unbiased gradient expectation. By conducting experiments across a wide range of tasks, the paper demonstrates the effectiveness and robustness of InfoBatch as a state-of-the-art data pruning technique in terms of tradeoff between performance and computational cost.

### Strengths
- The paper tackles a practically-relevant problem supported by a fair amount of experiments conducted across various tasks in the image domain. 
- InfoBatch is simple yet has a distinctive benefit over existing dynamic data pruning approaches: (i) replacing sorting operation with mean-thresholding significantly reduces the overhead cost, and (ii) gradient expectation bias is well addressed supported by theoretical analysis. 
- The proposed method demonstrates superior performance compared to the baselines, and the paper provides a comprehensive review of relevant previous works.
- Overall, the paper is well-written and easy to follow.

### Weaknesses
 - InfoBatch improves over UCB via throwing away the dataset sorting operation. However, in Table 2, the practical overhead cost saving seems negligible compared to the wall clock time and the total node hour. Also, how was the overall saved cost calculated in Tables 6 and 7?   
- To my understanding, annealing utilizes the whole dataset without pruning for the last 0.125% of total training epochs. This raises several concerns: (i) As the wall clock time of UCB and InfoBatch in Table 2 are both 10.5h, is this value taking the annealing process into account? (ii) Regarding Table 1, all the baselines and InfoBatch are compared under the same dataset pruning ratio. I wonder whether this is a fair comparison when annealing is involved in InfoBatch. (iii) Why did the authors utilize annealing only as a means of stabilizing the optimization, rather than leveraging the full dataset at the very beginning of optimization when we know that the early epochs of training can heavily influence the convergence of the loss landscape [1]?  
- The authors may need to provide further clarification regarding how annealing contributes to the stabilization of the rescaling process, especially if it does not seem to significantly impact the variance of the results in Table 4.
- The authors claim that the use of loss values in pruning conditions serves two purposes: (i) it reflects the learning status of samples, and (ii) it theoretically ensures unbiased gradient expectations. However, in Table 5, it is observed that even a random pruning criterion achieves nearly the same performance as the original pruning condition. This result raises questions about the necessity and effectiveness of using loss values as a pruning criterion and may require further discussion or clarification in the paper.

### Questions
- How many random seeds are used throughout the experiments? 
 

[1] Fort et al., “Deep learning versus kernel learning: an empirical study of loss landscape geometry and the time evolution of the Neural Tangent Kernel.” 2020.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a dynamic data pruning scheme to reduce the cost of stochastic gradient training. It does so by stochastically removing lower loss data points and correspondingly rescaling their gradients to maintain an unbiased overall estimates. In conjunction with training on all data towards the end of training, the scheme is able to reduce training cost by about 20-40% on a range of datasets and architectures, including some large scale ones such as ImageNet and a LLaMA model.

Overall, this is a simple but highly pragmatic and practical approach. The scheme solely relies on quantities that are computed during training anyway, so incurs minimal overhead. Unfortunately, I believe that the comparison with the baselines is not entirely applies-to-apples and there are some minor issues with the write-up, so that all things considered I would lean towards rejecting the paper. Nevertheless, I hope these will be addressed over the course of the rebuttal and am open to increasing my score.

EDIT: the extensive additional results for the rebuttal have addressed my concerns and I would now recommend acceptance.

### Strengths
* The approach is simple but pragmatic, I appreciate the care that is taken to not incur substantial overheads for additional computation such as thresholding by the mean score. This could be a broadly applicable technique for speeding up training, both for researchers and practitioners.
* The method is described well, I think it would be straight-forward to implement this even without code being provided.
* There is a broad range of experiments, including some larger scale setting involving ImageNet and language models, emphasizing the potential relevance of the approach.

### Weaknesses
 * The comparison with the baselines does not seem entirely apples-to-apples to me due to the "annealing" period on the whole dataset. I suspect (intuitively and based on the ablations in Table 4 plus the pruning rule seemingly being irrelevant in Table 5) that ensuring the total length of the optimization trajectory remains comparable to that on the full dataset (by rescaling the gradients) in conjunction with the fine-tuning on all data towards the end of training is the "secret sauce" to making a dynamic pruning method perform without a degradation in test accuracy. I'm not familiar with the (Raju et al., 2021) paper, but would expect that at least the annealing period could be incorporated into this method without further issue. At the moment the paper presents its selection rule leading to performance matching that of full-data training as a core contribution, however if this can be achieved relatively easily with other selection techniques as well, I think it becomes more about the re-scaling/tuning as general purpose techniques and the cost comparison between different selection approaches being featured more prominently. I don't think this would worsen the paper at all, although it would change the key takeaways a fair bit and I think it is important that the latter accurately reflect the empirical results.
* On a related note, I am a little bit concerned that the hyperparameters on e.g. ResNets for CIFAR10 are not tuned for achieving the final test performance as quickly as possible. I think it would be worth adding a baseline that trains on all data with a reduced number of epochs/learning rate decay milestones but increased learning rate corresponding to the computation saved by pruning (so hypothetically for 20% saved computation, train for 80 instead of 100 epochs but with learning rate 1.25 instead of 1 and halve it after 40 instead of 80 epochs). This is to ensure that pruning approaches meaningfully speed up training rather than benefitting from slack in the canonical hyperparameter choices for benchmark problems.   
* I don't entirely follow what the theoretical analysis is trying to achieve in 2.3. Isn't this just showing that the soft-pruned and rescaled gradient is unbiased? Isn't this completely obvious from having independent Bernoullis multiplied onto the terms of a sum (the total gradient over the dataset) and the expectation of a Bernoulli being its probability (so that if we divide by the probability, we get an expectation of 1 and the sum remains unchanged)?
* I found the paper to be fairly different to what the title made me expect. "Info" and "lossless" imply a connection with information theory and lossless compression to me, which is of course not present in the method. I appreciate that this is entirely subjective, but would suggest reconsidering the title of the paper. In particular, I would argue that the "lossless" part is a bit misleading since this is not theoretically guaranteed by the method, but merely and empirical observation in the experiments. Of course matching performance to the full dataset can always be achieved by letting $r \rightarrow 0, \delta \rightarrow 1$, but this would remove any cost savings.
* Similarly, I think the paper overstates its relationship with coreset/data selection methods a little bit. These are generally not for speeding up an initial training run, but subsequent ones e.g. for continual learning or hyperparameter tuning and typically incur an upfront cost. On the contrary, the proposed method speeds up a given training run without producing any artefacts (a coreset) that are useful downstream. So to me this seems more like a curriculum learning paper (although I am not particularly familiar with this branch of the literature, so this is a somewhat speculative statement).

### Questions
* I would like to see results for Random*, $\epsilon$-greedy and UCB with annealing and gradient re-scaling (for Random*; for the other two as applicable). As much as possible for Table 1 and ideally Table 2 (ResNet-18 instead of 50 is perfectly fine if that makes it more realistic). My hypothesis here would be that all baselines will match InfoBatch in discriminative performance, which would necessitate the main claims in the paper being updated (again, I don't think this affects the value of the contribution). If all the baselines are already using annealing and rescaling, this point is of course void.
* Add a full data baseline with reduced epochs as proposed in the weaknesses.
* Is there anything more to section 2.3 than showing unbiasedness?
* I would be curious what fraction of the data are soft-pruned throughout training? With the losses being bound below by 0, I would expect the distribution to become quite asymmetric as training proceeds. Could e.g. the median or some percentile be preferable? The median (not sure about arbitrary percentiles) can be computed in linear time, although I don't know if it is possible to update it online as for the mean.
* Do you have any thoughts on how to set $r$ and $\delta$ on a new dataset/architecture? The benchmarks in the paper are of course well-studied, but I think it would be a nice addition to the paper to discuss some heuristics for finding close-to-optimal values without needing a full training run (although suboptimal values already present a cost saving of course).

Typos:
- p1, §3: "constrainT computation resources" -> "constrainED computation resources"
- p1, §4: "cubersome" -> "cumbersome"
- Section 3.3, §1: "see appendix" -> missing specific reference
- B4. last §: "bond" -> "bound"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel dynamic data pruning, aiming to remove (with a predefined probability) the samples with lower loss score. The algorithm does not require to sort the losses, but it does require to train the model with all samples in the final epochs. The experimental results show a significant speedup in the training procedure, with minimal (or zero) performance drop.

### Strengths
**originality**: Although the idea of dynamic pruning is not novel (as clearly stated by the authors), but the solution provided is original enough.

**quality**: The experimental results show the algorithm is able to obtain a clear speedup training, and also remarkable performance results, with almost no accuracy drop.

**clarity**: The idea is simple and easy to implement. The ablation study also provides a solid explanation about how each novel idea affects the overall result.

**significance**: Speeding up training procedures is of huge interest, as it can save a lot of time and energy.

### Weaknesses
 **originality**: The idea is somehow similar to other dynamic pruning approaches. It does not provide a different point of view in the matter.

**quality**: In the ablation study, I would like to see if different threshold selections (apart from the mean value) can affect the algorithm. I find it a little bit odd that there is no discussion regarding to this point.

**clarity**: The text is too dense. The figures are too small to be read in a paper. I suggest the authors to increase the figures, while removing the text surrounding them. Some sections, like 2.3, can be summarized to make room for the adjustment.

**significance**: the authors claim their threshold value can be established in constant time, whereas the state-of-the-art methods require a sorting part (the complexity should be $\mathcal{O}(N \log N)$. However, I think this improvement is no significant, as the speedup produced is residual compared to the time needed to train the network.

### Questions
- Why there is no discussion regarding to the threshold selection procedure? Different solutions like taking the mean plus a factor of the standard deviation can led to interesting results.

- Did the authors experiment with a pruning probability that depends on the sample score?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
