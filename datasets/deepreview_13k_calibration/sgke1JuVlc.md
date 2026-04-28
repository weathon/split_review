# Temporal Misinformation and Conversion through  Probabilistic Spiking Neurons

- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 6, 3, 3

## Abstract
In the age of large neural network models and their high energy demand, Spiking Neural Networks (SNNs) offer a compelling alternative to Artificial Neural Networks (ANNs) due to their energy efficiency and resemblance to biological brains. However, directly training SNNs with spatio-temporal backpropagation remains challenging due to their discrete signal processing and temporal dynamics. Alternative methods, notably ANN-SNN conversion, have enabled SNNs to achieve performance in various machine learning tasks, comparable to ANNs, but often to the expense of long latency needed to achieve such performance, especially on large scale complex datasets. The present work deals with ANN-SNN setting and identifies a new phenomenon we term ``temporal misinformation'', where random spike rearrangement through time in the converted SNN model improves its performance. To account for this, we propose bio-plausible, two-phase probabilistic (TPP) spiking neurons to be used in ANN-SNN conversion. We showcase the benefits of our proposed methods both theoretically and empirically through extensive experiments on CIFAR-10/100 and a large-scale dataset ImageNet over a variety of architectures, reaching SOTA performance. Code is available on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper primarily conducts further research on the ANN-SNN conversion methods. In particular, the authors have discovered a new phenomenon termed "temporal error information" and proposed biologically plausible two-phase probabilistic (TPP) spiking neurons for ANN-SNN conversion. The experimental results demonstrate the advantages of this method.

I believe that the method proposed by the authors is effective; however, I have some questions that need clarification, mainly regarding the explanation and interpretation of the phenomenon. At this stage, my rating is "6: Marginally above acceptance threshold." If the authors could address and clarify these questions, I would be very willing to raise my score.

### Strengths
1. The method is simple and effective, supported by comprehensive experimental validation. The proposed approach achieves state-of-the-art (SOTA) accuracy on the CIFAR-10/100 and ImageNet datasets, advancing the further development of ANN-SNN conversion.

2. Unlike SNN research that tends to focus on computational efficiency, the two-phase mechanism and probabilistic spike discharge proposed in this work are both biologically plausible and have similar implementations in certain neuromorphic hardware.

### Weaknesses
1. The description in lines 94-107 is difficult to understand. Table 1 indeed shows that the "permuted" model performs better, but how does this relate to the previously acknowledged yet erroneous assumption that "the precise timing of the spikes should not affect the performance of the SNN"? There is no explanation of what the "permuted" operation is or how it relates to "the precise timing of the spikes." Additionally, why is the phenomenon named "temporal error information"? Where does the error manifest? Section 3.1 addresses these questions, but lines 94-107 should also provide some insight for readers encountering this for the first time.

2. I find the experimental work convincing; however, the description of the phenomenon of "temporal error information" needs further clarification. The current description leaves me unclear about what constitutes "temporal error information" in the original spike sequence. Which time steps contain erroneous spikes? What portion of the temporal errors is addressed by the "permuted" operation, and how does this improve the accuracy of the conversion?

### Questions
1. I am unclear about the details of the "permuted" operation. Figure 2(a) mentions that "the second Spiking phase outputs the same spike trains, but permuted." Since the output spike sequences are the same, where does the permutation manifest? Is it the firing times that have been rearranged?

2. In ANN-SNN conversion, even if the spike firing rates match the ANN activation values, the conversion is not lossless. Some works have discussed this, noting that in early time steps, there can be spikes that should not have been fired, resulting in erroneous spikes [1]. Is this related to the "temporal misinformation" mentioned in the paper? Furthermore, uneven errors also point to this issue [2]. What is the relationship between "temporal misinformation" and uneven errors? Could the authors provide some discussion on this aspect?

[1] X. He, Y. Li, D. Zhao, Q. Kong, and Y. Zeng, “Msat: biologically inspired multistage adaptive threshold for conversion of spiking neural networks,” Neural Computing and Applications, pp. 1–17, 2024.

[2] Tong Bu, Wei Fang, Jianhao Ding, PengLin Dai, Zhaofei Y u, and Tiejun Huang. Optimal ANN-SNN
conversion for high-accuracy and ultra-low-latency spiking neural networks. In International
Conference on Learning Representations, 2022c.

### Soundness
3

### Presentation
1

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
This paper introduces the concept of "temporal misinformation" in the ANN-to-SNN conversion process. It employs two-phase probabilistic (TPP) spiking neurons as the neurons in the SNN. The converted SNN model improves performance by using probabilistic neurons that fires spikes randomly.

### Strengths
1. The method is relatively easy to understand.
2. The problem is relevant to the scope of ICLR.
3. The paper identifies an interesting phenomenon in the ANN-SNN conversion process, which could serve as a complementary insight.

### Weaknesses
1. This work primarily proposes a spiking neuron model rather than a novel conversion paradigm, which limits its originality, as similar work on probabilistic neurons has been done previously. While the authors introduce a two-phase probabilistic (TPP) spiking neuron, the core contribution remains at the neuron level rather than offering a fundamentally new approach to ANN-to-SNN conversion. The novelty is further diminished by the fact that the use of probabilistic neurons in SNNs is not entirely new, and the paper does not sufficiently differentiate its approach from existing methods in terms of the underlying mechanism or the specific application to the conversion process.
2. The authors’ definition of "temporal misinformation" is unclear. While the paper introduces the "temporal misinformation" phenomenon and experimentally demonstrates its impact on SNN performance, it lacks a sufficient theoretical basis to explain this phenomenon and does not provide quantifiable error analysis. The concept of temporal misinformation, as presented, is not rigorously defined, making it difficult to assess its validity and scope. The paper lacks a formal model or a mathematical framework to quantify this error, which makes it hard to understand how the proposed method mitigates it. The experimental results demonstrate the impact of this phenomenon, but without a theoretical underpinning, the analysis remains descriptive rather than explanatory.
3. The authors use "permutation" to introduce two-phase probabilistic spiking neurons (TPP). Theorem 1 suggests that the spikes emitted by probabilistic spiking neurons achieve an optimal spike firing order; however, this proof lacks persuasiveness. The use of permutations to reorder spikes is presented as a key aspect of the TPP neuron, but the justification for why this leads to an optimal firing order is not convincing. The theorem's proof does not provide a clear and rigorous argument for why a specific permutation would be optimal, and it does not consider the potential for other permutation strategies to yield similar or better results. The connection between the permutation and the claimed optimality remains unclear.

### Questions
1.  For T time steps, there are T! possible permutations. Does every permutation yield better results than the original, non-permuted approach?
2. Please clarify what the additional c steps in Tables 1 and 2 represent. 
3. In Tables 4 and 5, when comparing with SNNC, data suggests that at short time steps such as T=4 and T=8, "Permute" seems more effective than TPP. I would like to see if a similar phenomenon occurs with QCFS. Please provide additional comparative experiments between "Permute" and TPP on QCFS across CIFAR-10 and CIFAR-100 datasets. 
4.  Does the probabilistic neuron model introduce extra overhead for hardware implementation?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper analyzes the assumption in ANN-SNN conversion that information transfer relies solely on spike firing frequency. By permuting spike sequences, the paper observes the issue of “temporal misinformation” within the temporal domain. Further, it proposes an accumulation -> firing approach to avoid temporal misinformation, establishing an efficient ANN-SNN training method. The method is validated on datasets such as CIFAR and ImageNet, demonstrating advantages in model performance and other aspects.

### Strengths
The paper presents a compelling perspective: there exists a phenomenon of “temporal misinformation” in the ANN-SNN conversion method.

### Weaknesses
The novelty. The Ideas in this paper are quite similar to those in at least two other papers.

### Questions
1.Prior to this paper, many works have discussed the equivalence between spiking neurons with temporal information and neurons with quantized activation values. This includes papers in the ANN-SNN domain [A], as well as works in the direct training domain [B]. Could you highlight the key innovations in your paper?

2.I noticed that you cited paper [A], pointing out precision issues in its conversion process. In fact, your methods appear quite similar to theirs; could you provide a comparison between your approach and theirs?

3.Could your method be applied to direct training, as in [B]? Would you be able to discuss the similarities, differences, and advantages or disadvantages of your method when used in direct training compared to ANN-SNN conversion?

[A]Hu, Y., Zheng, Q., Jiang, X., & Pan, G. (2023). Fast-SNN: fast spiking neural network by converting quantized ANN. IEEE Transactions on Pattern Analysis and Machine Intelligence.
[B]Luo, Xinhao, et al. "Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection." arXiv preprint arXiv:2407.20708 (2024).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper identified a new phenomenon in SNNs, termed “temporal misinformation”, and proposed a solution. Results are validated on CIFAR-10, and CIFAR-100, and ImageNet

### Strengths
The overall problem identification in the introduction section sounds interesting. However, the writing of the paper is very poor and it is very hard to follow the paper to understand the motivation, method, and detailed strengths of the method. Also, I cannot find detailed descriptions of Figure 1, which prevents me from understanding the main motivation of this work. 

Basically, I lost at the very beginning phase when I read this paper, so have not been able to identify the strengths.

I encourage the author to make major changes to the clearness of the paper and writing before any potential resubmission, so readers can understand the paper better.

### Weaknesses
1. Line 11. "age of large neural network models", what "age of large neural network models" means? Is this a scientific term that deep learning researchers usually use? When did this age start? Which paper used the term "large neural network models" before?

2. I searched for the "Fig" but did not find any results that refer to Figure 1 explains Figure 1. Could you make it clearer to readers where the explanation in Figure 1 is located in your paper? It is NOT friendly for reviewers as you want to use Figure 1 to attract attention but then when a reviewer tries to enjoy the detailed explanation of this figure, you just hide explanations. 

3. Line 158 "\textbf{ANN-SNN} conversion" and Line 188 "\textbf{Direct training} This method a". Why "conversion "is not capitalized in Line 158, but "This" is capitalized in Line 188? What does "ANN-SNN" mean? Is this a term you created? If not, please cite papers that used "ANN-SNN" before, or explain this new term clearly.

4. Line 25. "Code is available on GitHub.". What do you mean by "Code is available on GitHub."? There is not any Github link in the paper. Please do not mention something that does not exist in the abstract.


--------------------------------------------------------
Updates After Rebuttal

After multiple rounds of discussion with the authors, only Point 2 has been addressed. Point 3 remains unresolved and has not been corrected in the latest paper version (19 Nov 2024). The other two points have not been responded to by the authors.

I have provided my final comments to the authors, requesting a revision of the paper to solve Point 3. I will not respond to any further comments from the authors, as the authors ignored my previous comments and it has been the second time I EXPLICITLY asked the author to correct it in the paper. I strongly suggest author read my comments sincerely and revise the paper, instead of continuing to give pointless discussions. 

Since the authors have addressed only one out of the four issues I raised, I have kept the score unchanged but increased the confidence level from 4 to 5.

------------------------
Second Update After Rebuttal:

This update focuses on the author's unprofessional behavior. I am extremely frustrated with how the author treats the reviewer and disregards the reviewer's comments.

I pointed out that Figure 1 in the paper is never referred to even once in the text. This is the first figure of the paper and should be clearly explained in detail. In the latest version of the paper (submitted on November 19, 2024), the author addressed one issue by correcting "Table 1" to "Figure 1" and responded that Figure 1 is described in the Introduction section and in Section 3.1. However, neither of these sections explains Figure 1 in detail, and Figure 1 is still not referred to in Section 3.1.

Additionally, I noted an issue in Line 158 regarding the term "ANN-SNN" I explained that "ANN-SNN" is not a term commonly used by researchers and that the first word of the sentence should be capitalized. The authors questioned the reviewer's expertise and professionalism, claiming that "ANN-SNN" is a widely used scientific term and suggested I look it up on Google Scholar. This response was unprofessional. I checked 30+ SNN papers on Google Scholar and confirmed that "ANN-SNN" is not used; instead, the technique is commonly referred to as "ANN-SNN Conversion." I informed the authors of this and requested that they revise the term explicitly in the paper and not let the efforts of the reviewer be wasted. Despite this, the authors refused to make the revision, arguing that the correct term is used 32 times elsewhere in the paper and dismissing my comments as "pointless discussions."

Even after providing evidence and explicitly asking for the revision, the authors have not made the changes. As of November 20, 2024, the term "\textbf{ANN-SNN}" has still not been revised to "\textbf{ANN-SNN Conversion}," and the first word of the sentence ("conversion") remains uncapitalized. The authors' repeated dismissal of my comments as "pointless" and their refusal to revise the paper is baffling and disrespectful to the review process. Their behavior is very unprofessional.

### Questions
See Weakness for detailed questions.

### Soundness
2

### Presentation
1

### Contribution
2
