# SNAP-TTA: Sparse Test-Time Adaptation for Latency-Sensitive Applications

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Test-Time Adaptation (TTA) methods use unlabeled test data to dynamically adjust models in response to distribution changes. However, existing TTA methods are not tailored for practical use on edge devices with limited computational capacity, resulting in a latency-accuracy trade-off. To address this problem, we propose SNAP-TTA, a sparse TTA framework that significantly reduces adaptation frequency and data usage, delivering latency reductions proportional to adaptation rate. It achieves competitive accuracy even with an adaptation rate as low as 0.01, demonstrating its ability to adapt infrequently while utilizing only a small portion of the data relative to full adaptation. Our approach involves (i) Class and Domain Representative Memory (CnDRM), which identifies key samples that are both class-representative and domain-representative to facilitate adaptation with minimal data, and (ii) Inference-only Batch-aware Memory Normalization (IoBMN), which leverages representative samples to adjust normalization layers on-the-fly during inference, aligning the model effectively to changing domains. When combined with five state-of-the-art TTA algorithms, SNAP-TTA maintains the performances of these methods even with much-reduced adaptation rates from 0.01 to 0.5, making it suitable for edge devices serving latency-sensitive applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces SNAP-TTA, a sparse Test-Time Adaptation (STTA) framework designed for latency-sensitive applications on resource-constrained edge devices. Traditional TTA methods dynamically adjust models using unlabeled test data to handle distribution shifts, but they often incur high computational costs and latency, making them impractical for real-time edge environments. SNAP-TTA addresses these challenges by introducing two key components: (i) Class and Domain Representative Memory (CnDRM), which selects class-representative and domain-representative samples to enable effective adaptation with minimal data, and (ii) Inference-only Batch-aware Memory Normalization (IoBMN), which corrects feature distribution shifts during inference without additional training. By combining SNAP-TTA with five state-of-the-art TTA algorithms, the paper demonstrates that SNAP-TTA achieves significant latency reductions (up to 87.5%) while maintaining competitive accuracy. Experimental results on benchmarks like CIFAR10-C and ImageNet-C show SNAP-TTA’s superior performance in edge settings, making it suitable for real-world, latency-sensitive applications.

### Strengths
1. This paper addresses the challenge of achieving high adaptation accuracy while maintaining computational efficiency in Sparse Test-Time Adaptation (STTA), where updates rely on only a small subset of data.
2. SNAP-TTA demonstrates improved classification accuracy across adaptation rates (0.01 to 0.5) compared to baseline TTA methods on CIFAR10-C, CIFAR100-C, and ImageNet-C. At an adaptation rate of 0.1, SNAP-TTA reduces latency by up to 87.5% while mitigating accuracy loss, validating its effectiveness in STTA
3. IoBMN combines memory statistics from domain-representative samples with current inference batch statistics, using a soft shrinkage function to balance them. This dynamic normalization adjustment during inference effectively addresses domain shift, ensuring model adaptability and performance stability.

### Weaknesses
1. The reliance on a fixed confidence threshold of CnDRM may limit adaptability across varying data distributions and could lead to suboptimal sampling. Specifically, the threshold's static nature doesn't account for varying noise levels across different datasets or even within a single dataset under different corruptions. This could lead to either over-filtering potentially useful samples in cleaner distributions or under-filtering noisy samples in more corrupted ones, hindering the adaptation process.
2. In table 5, accuracy differences between methods are small, without statistical analysis, making it unclear if these differences are significant (In Detailed comments 4)

### Questions
I have some comments as following:

1. Some results for latency and performance metrics on mobile or embedded systems would be helpful, to further validate the method’s effectiveness and robustness


2. Some in-depth analysis of specific limitations would be helpful, such as how memory overhead might impact performance on resource-constrained devices and how SNAP-TTA handles highly dynamic data distributions in real-world applications. Additionally, there is no discussion on potential trade-offs between latency reduction and accuracy under different conditions


3. The combined CnDRM+IoBMN method performs best, but the contribution of each component is not discussed. A brief explanation of how they work together would improve clarity. The table 5 only shows results at an adaptation rate of 0.1, the authors can mention that the complete data is in appendix.

### Soundness
3

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
5

### Summary
This paper addresses the problem of test-time adaptation for out-of-distribution generalization. To reduce the adaptation rate and improve the overall latency of TTA, the authors propose a SNAP framework that selects partial samples for adaptation. Experimental results highlight the potential of the proposed method. However, I still have several concerns as outlined below.

### Strengths
The design of the SNAP method is well-motivated and reasonable from the technical perspective. 

The proposed approach is a plug-and-play module that can be integrated with existing TTA methods to reduce adaptation steps and enhance efficiency. 

Experimental results underscore the effectiveness of the proposed method.

### Weaknesses
On edge devices, the most critical factor in determining whether a TTA method is feasible is actually peak memory usage, as highlighted by MECTA [A]. While this work does reduce the number of adaptation steps, it does not decrease peak memory usage. In this sense, the primary motivation for applying the proposed method to edge devices may be misplaced.

I am somewhat confused about the latency differences between, Tent, EATA, SAR and SNAP, all of which are sample selection-based methods. Compared to Tent, EATA does not reduce latency because, this is because in the EATA’s code, even filtered samples are still used in back-propagation (due to limitations in PyTorch), despite halving the number of samples involved in adaptation. However, in SNAP, latency is reduced. If this reduction is due to engineering optimizations, the same should ideally apply to EATA and SAR for a fair comparison. If not, the comparison could be seen as unfair.

Another area of confusion is that, based on my experience, EATA generally outperforms Tent and SAR under standard settings. However, the authors’ results show SAR and Tent performing better than EATA, which contradicts my observations. Could the authors provide further clarification on this?

In the efficiency comparison, the authors compare SNAP-TTA (under the sparse setting, i.e., every $k$-th batch) with prior methods like TENT and EATA (under the fully update setting, i.e., every batch). However, for performance comparisons across all tables, the authors compare SNAP-TTA with baselines including TENT and EATA (under the sparse setting ($k$-batch updates)). This comparison is unfair. While I understand the motivation to adopt the sparse setting to improve average efficiency, this paper risks misleading both the reviewers and readers into believing that SNAP-TTA achieves both higher efficiency and higher performance than baselines. Actually, when baselines are evaluated under the same sparse setting, SNAP-TTA does not demonstrate superior efficiency over them. The efficiency are the same when CnDRM size equals to the batch size.

Moreover, how does the memory size of CnDRM affect the performance of SNAP-TTA? Given that saving samples may raise privacy concerns, this aspect should be carefully addressed.

In sparse settings, the number of learning iterations for the baselines is limited, indicating that the updates are very insufficient. In this case, have you considered increasing the learning rate for the baselines? Would this lead to improved performance?

### Questions
I am somewhat confused about the latency differences between, Tent, EATA, SAR and SNAP, all of which are sample selection-based methods. Compared to Tent, EATA does not reduce latency because, this is because in the EATA’s code, even filtered samples are still used in back-propagation (due to limitations in PyTorch), despite halving the number of samples involved in adaptation. However, in SNAP, latency is reduced. If this reduction is due to engineering optimizations, the same should ideally apply to EATA and SAR for a fair comparison. If not, the comparison could be seen as unfair.

Another area of confusion is that, based on my experience, EATA generally outperforms Tent and SAR under standard settings. However, the authors’ results show SAR and Tent performing better than EATA, which contradicts my observations. Could the authors provide further clarification on this?

Does the proposed method reduce latency for a single batch or does it show an average improvement over multiple batches?

Lastly, would the proposed method be effective for transformer-based models, such as ViT-base?

I strongly encourage the authors to move Table 1 to the Appendix and provide additional results on ImageNet-C with various adaptation rates in the main paper, as the CIFAR-10 results are less critical and not sufficiently convincing. Currently, Table 1 occupies nearly an entire page, which I feel could be better utilized for more impactful content.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on Test-Time Adaptation (TTA) for edge devices with limited computational capacity. The authors propose SNAP-TTA, a sparse TTA framework with two key components, Class and Domain Representative Memory (CnDRM) and Inference-only Batch-aware Memory Normalization (IoBMN), aiming to reduce model adaptation frequency and data usage while maintaining accuracy.

### Strengths
The proposed SNAP-TTA framework addresses the latency-accuracy trade-off issue in existing TTA methods for edge devices in some cases. It reduces latency while achieving competitive accuracy, as demonstrated by extensive experiments on multiple benchmarks and with integration of several existing TTA algorithms.

### Weaknesses
 - In the background section, the mention of applications like real-time health monitoring for IoT edge devices may not be entirely appropriate as these devices often have extremely limited memory. With limited memory, these devices are difficult and even impossible for backward-propagation and gradient decent. In this sense, memory should perhaps be prioritized over latency as the primary concern.
- It is unclear whether the proposed method reduces the delay per batch or the average delay (adaptation occurs once every several batches as shown in Figure 1). If it is the latter, its effectiveness for latency-sensitive applications may be limited as the inference delay could increase significantly every several batches.
- The method reduces the cost of backpropagation by filtering samples to decrease the inference latency. However, EATA also uses a similar strategy, but in Figure 2, the delay of EATA is the same as that of Tent, and the delay of SAR is inconsistent with the results reported in its original paper.
- The paper could compare the inference latency in Tables 1, 2, and 3.
- In Table 6 for ImageNet-C, only the Tent method is compared, ignoring other methods, which could provide more comprehensive and convincing results.
- In the experiments, it is not clear how the number of participating samples is controlled to meet the adaptation rate. Is it through adjusting the $tau_conf$ hyperparameter? Also, it is not described how other compared methods meet the adaptation rate.
- The description of lines 10-15 of the algorithm in the paper is relatively brief, considering its importance for the proposed method. More detailed explanation in the paper would assist readers in understanding.

### Questions
NA

### Soundness
2

### Presentation
2

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
The authors propose a sparse test-time adaptation (TTA) framework, which they call SNAP, that improves the latency-accuracy trade-off of existing TTA algorithms to enable practical use of TTA on ede devices.
To this end, the authors propose "CnDRM", a method for identifying "important" samples for training based on class- and domain-representative sampling, and "IoBMN", a method for mitigating the effects of domain shifts on the model's internal feature distributions.

### Strengths
- The method is promising in that, at least on a Raspberry Pi 4 and when used together with STTA, SNAP provides a significant reduction in latency, as shown in Table 4, while being able to maintain accuracy comparable to using STTA alone.
- The authors show empirically that SNAP works well with a number of different TTA algorithms (TENT, CoTTA, EATA, SAR, RoTTA) and with different adaptation rates for different datasets (CIFAR10-C, CIFAR100-C, ImageNet-C).

### Weaknesses
 - The claimed contribution of the paper is that SNAP can make existing TTA algorithms more latency efficient and suitable for edge devices. However, this is only demonstrated in Table 4 for one algorithm (STTA) and one target device (Raspberry Pi 4). All other experiments focus only on accuracy. And while it is an important and valuable contribution to properly demonstrate that SNAP does not reduce the effectiveness of the TTA algorithms it is applied to, I think the evaluation overall fails to adequately demonstrate the claimed contribution of latency reduction across various edge devices.



### Questions
- What are the lower limits of the proposed approach? For example, would SNAP enable TTA on microcontroller units (MCUs) such as Cortex-M MCUs?
- How memory intensive is the approach? There seem to be some mechanisms in place to keep memory requirements fixed (line 264 ff), but could memory, i.e. RAM, availability still become a bottleneck of the approach on edge systems?
- I am a bit confused about the hyperparameter "adaptation rate": Is this parameter specifically implemented by SNAP or is it implemented by the underlying TTA algorithms? I was wondering because, for example, in Table 1 the accuracy for the TTA algorithms without SNAP-TTA also decreases at lower adaptation rates.

### Soundness
3

### Presentation
3

### Contribution
2
