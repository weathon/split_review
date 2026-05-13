# LASER: Linear Compression in Wireless Distributed Optimization

- Decision: Reject
- Scores: 3, 8, 6, 6, 6, 6

## Abstract
Data-parallel SGD is the de facto algorithm for distributed optimization, especially for large scale machine learning. Despite its merits, communication bottleneck is one of its persistent issues. Most compression schemes to alleviate this either assume noiseless communication links, or fail to achieve good performance on practical tasks. In this paper, we close this gap and introduce \textsc{LASER}: {\bf L}ine{\bf A}r Compre{\bf S}sion in Wir{\bf E}less Dist{\bf R}ibuted Optimization. \textsc{LASER} capitalizes on the inherent low-rank structure of gradients and transmits them efficiently over the noisy channels. Whilst enjoying theoretical guarantees similar to those of the classical SGD, \textsc{LASER} shows consistent gains over baselines on a variety of practical benchmarks. In particular, it outperforms the state-of-the-art compression schemes on challenging computer vision and GPT language modeling tasks. On the latter, we obtain $50$-$64 \%$ improvement in perplexity over our baselines for noisy channels.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a scheme for efficient and reliable uplink communication over a noisy channel in a federated environment. In particular, clients submit rank factors of the gradients, where owing to the inherent low-rank structure of gradients, reconstruction can be performed reliably server-side, leveraging error-feedback if necessary. The authors demonstrate the effectiveness of this communication strategy, dubbed LASER, by performing experiments such as an image-classification, a GPT language-modeling task, and a 1-layer NN MNIST task.

### Strengths
1. The narrative and motivation are very well-written. Indeed, uplink communication is often assumed to be noiseless in many FL setups. 
2. To the best of my knowledge, the theory is sound, and all assumptions are fair, with well-cited support regarding the low-rank nature of gradients. 
3. The large-scale GPT-2 experiment was quite impressive. Challenging large-scale language tasks are seldom seen in FL literature.

### Weaknesses
1. In my opinion, this work does not introduce anything truly novel or interesting to the subdomain of communication efficiency. Gradient compression via sketching (Rabbani et al., 2023, Rothchild et al., 2020; Haddadpour et al., 2020), quantization (Zakerinia et al., 2023), and even the blanket consideration of general contraction/compression operators (Dorfman et al., 2023) along with many other works indicate that the research area of uplink efficiency is saturated. Introducing a low-rank decomposition of the gradient as a form of compression is not a particularly novel technique, especially since it is handled under the general error-feedback recovery. The use of error-feedback mechanisms to handle the inexactness of low-rank approximations is well-established, and the paper does not offer a new perspective on this. Furthermore, the paper does not explore the trade-offs between the rank of the approximation and the resulting communication savings, nor does it compare against other compression techniques under similar settings. Bi-directional compression is a much more challenging and relevant problem in the modern landscape of FL communication efficiency.

2. The following lines concern me: "Rank compression methods (Yu et al., 2018; Cho et al., 2019; Wang et al., 2018) spectrally decompose gradient matrix (often via SVD) and transmit these factors. Since SVD is computationally prohibitive, we rely on the state-of-the-art
light-weight compressor PowerSGD (Vogels et al., 2019)." Since gradient rank decomposition has been performed in distributed settings, using a SoTA method for decomposition is simply a plug-and-play extension which further restricts the novelty of LASER. The choice of PowerSGD, while practical, does not introduce any theoretical or methodological novelty. The paper essentially applies an existing low-rank approximation technique within an error-feedback framework, which has been explored in prior work. The lack of a novel decomposition method or a unique way of leveraging low-rank structure further diminishes the contribution.

### Questions
1. In what scenario would the uplink communication be noisy but the downlink communication would be noiseless? "For the downlink
communication from the server to the clients (broadcast channel), we assume that it is noiseless and thus the clients exactly receive what the server transmits..."

2.  (Chang & Tandon, 2020; Guo et al., 2020) imply that clients must first transmit information regarding the norms of their gradients before constructing a power budget policy -- does this imply 2 rounds of communication would be necessary assuming a dynamic power schedule is employed?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a novel technique for distributed optimization: LASER, which is mostly composed of a low-rank compression step, and an over-the-air aggregation step. The authors present the theoretical advantage of such method over vanilla over-the-air SGD, and the convergence of the method is ensured. Finally, extensive experiments show the advantage of the proposed method, including on large scale tasks such as GPT language modeling tasks.

### Strengths
## Originality: 

The work is original, as it is the first one to study over-the-air gradient aggregation using a low-rank compression of the gradients. The results proven regarding the channel influence factor are novel and seem not trivial to show. The experiments show an improved performance over state of the art algorithms.

## Quality: 

The quality is good, with Theorems and their assumption clearly stated. Detailed proofs are provided for the results exposed. Additionally, the code is provided in the Supplementary material.

## Clarity: 

I believe the contributions are clear, and well organized.

## Significance: 

I believe the work is significant, in particular given the extensive experimental comparison with state of the art algorithms, including a very encouraging experimental results on large scale tasks such as GPT language modeling, which have become prominent in machine learning. Additionally, the results proven regarding the channel influence factor seem non-trivial and therefore should be very useful for the research community to build upon.

### Weaknesses
I just have a few questions below:

1. In algorithm 1, the local error $e_i$ is only $\boldsymbol{M}_i - \text{DECOMPRESS}(\mathcal{C}_r(\boldsymbol{M}_i))$, without ever being multiplied by $\gamma$: is this correct ? It seems that if so, the error may not be compensated correctly ? (I may be mistaken)
2. If I understand correctly, Assumption 5 is a new assumption introduced in the paper: unless I missed it in the paper, I think it would be good to elaborate a bit further on why such assumption should be verified in the settings considered, theoretically and/or experimentally (or even just with a discussion, just to provide some intuition on why such assumption should be verified): it seems that to verify it, either the compression should be very accurate (i.e. $\delta_r$ large), or $\lambda_{\text{LASER}}$ should be small, but however, while taking a larger $r$ would make $\delta_r$ larger (more accurate compression), it would also make the bound on $\lambda_{\text{LASER}}$ larger, according to eq. (5), therefore it seems a bit unclear whether Assumption 5 can be verified (or how to make it verified in practice).
3. For the experiments, I believe it would be useful to just recall how one can deal with parameters of DNNs, which are not, per say, 1 matrix: looking into Vogels 2019, it seems that, to do that, the low-rank decompositions are done layer-wise (since each layer can be seen as a matrix, even in the convolutional case), but just a quick recall about this would be useful.
4. Minor remarks/typos:
- in 5. “decompose gradient matrix” -> “decompose the gradient matrix”
- In the supplemental, just before D.2: “experssion” —> “epxression”

### Questions
I just have a few questions below:

1. In algorithm 1, the local error $e_i$ is only $\boldsymbol{M}_i - \text{DECOMPRESS}(\mathcal{C}_r(\boldsymbol{M}_i))$, without ever being multiplied by $\gamma$: is this correct ? It seems that if so, the error may not be compensated correctly ? (I may be mistaken)
2. If I understand correctly, Assumption 5 is a new assumption introduced in the paper: unless I missed it in the paper, I think it would be good to elaborate a bit further on why such assumption should be verified in the settings considered, theoretically and/or experimentally (or even just with a discussion, just to provide some intuition on why such assumption should be verified): it seems that to verify it, either the compression should be very accurate (i.e. $\delta_r$ large), or $\lambda_{\text{LASER}}$ should be small, but however, while taking a larger $r$ would make $\delta_r$ larger (more accurate compression), it would also make the bound on $\lambda_{\text{LASER}}$ larger, according to eq. (5), therefore it seems a bit unclear whether Assumption 5 can be verified (or how to make it verified in practice).
3. For the experiments, I believe it would be useful to just recall how one can deal with parameters of DNNs, which are not, per say, 1 matrix: looking into Vogels 2019, it seems that, to do that, the low-rank decompositions are done layer-wise (since each layer can be seen as a matrix, even in the convolutional case), but just a quick recall about this would be useful.
4. Minor remarks/typos:
- in 5. “decompose gradient matrix” -> “decompose the gradient matrix”
- In the supplemental, just before D.2: “experssion” —> “epxression”

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a low-rank compression method for distributed optimization. The emphasis is on wireless communication systems where the averaging is done "over the air" in a noisy channel. The performance is evaluated in experiments with both language modeling and image classification tasks.

### Strengths
- The incorporation of a power budget and power allocation in the compression algorithm is somewhat new and interesting. 
- The consideration of a GPT model in the experiments is good.

### Weaknesses
 - The considered wireless communication system with "over the air" averaging is essentially doing the averaging in the analog domain. This is impractical as all modern wireless systems are digital and data transmission involves channel coding, which is likely incompatible with "over the air" averaging. I am aware that this concept has been presented in many papers published in wireless communications journals and conferences, but it is still impractical. It is unlikely that wireless communication standards will incorporate a specific physical layer technique only for the sake of computing averages, which in any foreseeable future represents only a very small fraction of data transmitted in common wireless systems. Moreover, this mechanism restricts the averaging to clients communicating with a single basestation, while in practice, the coverage of a single basestation is quite small and having all the clients connecting to the same basestation is very unlikely.
- The paper focuses on low-rank compression, which by itself is a known technique. Yet, the result in Theorem 1 and its assumptions seem to be a standard error-feedback result. In particular, Assumption 4 is standard and does not capture anything specific to the fact of using low-rank compression instead of other compression methods such as top-k and random-k. It seems the only difference from standard error-feedback compression analysis is the noise term, which, however, is a straightforward extension. 
- It is not quite clear how power reduction is achieved as shown in the experiments. The power budget is fixed according to Algorithm 1. If there is a fixed power budget, the same budget should apply to both the proposed algorithm and the baselines. The results in Table 1 and Table 3 either do not enforce a fixed power budget, which contradicts with the description in Algorithm 1, or there is something else wrong.

### Questions
Please refer to the weaknesses. 

In addition, the ICLR template suggests that the appendix should be included at the end of the same PDF as the main paper.

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
Considering the randomness in the communication environment, to reduce the power needs of sending information from the local client, the author proposed a new distributed algorithm called LASER. Different from the previous algorithm, the proposed algorithm uses low-rank compression to reduce the vector dimension that will be sent to the server. Combined with error feedback, the algorithm's convergence is established in quasi-convex, convex, and nonconvex cases. The experiments show the proposed algorithm can achieve a similar performance with lower power.

### Strengths
1. Consider the power that is needed to transmit vectors from the client to the server.

2. To use the power efficiently, the authors introduce a low-rank compressor to make the SNR larger than transmitting the full matrix.

3. To eliminate the error from the compressors, the authors introduce the error feedback into the proposed algorithm.

4. The authors show the convergence of the proposed algorithm under quasi-convex, convex, and non-convex cases.

5  The experimental results show that the proposed algorithm can achieve a similar performance but requires less power.

### Weaknesses
1. In the distributed setting, how can each client know $max ||g||$?

2. The low-rank compressor seems to be time-consuming. Why not use top-k or other compressors?

3. It seems to be unfair to compare the energy budget in each iteration, because adding a compressor even with the error feedback, the algorithm needs more iterations to converge. Thus, it would be fair to compare total energy costs. Otherwise, the most energy-saving algorithm in this framework will be the top-1 compressor (sending only one value each time).

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address the communication bottleneck issue in data-parallel SGD, which is widely used for distributed optimization in large-scale machine learning. The authors highlight that existing compression schemes either assume noiseless communication links or fail to perform well in practical tasks. To bridge this gap, the authors propose LASER, a gradient compression scheme that transmits gradients over noisy channels by leveraging the inherent low-rank structure.

### Strengths
The authors demonstrate that LASER consistently outperforms baseline methods across various benchmarks, outperforming state-of-the-art compression schemes in computer vision and GPT language modeling tasks.

### Weaknesses
The novelty of the paper is not well stated. It is unclear whether low-rank matrix decomposition techniques already exist and if the contribution of the paper lies solely in the utilization of low-rank decomposition to reduce gradient transmission traffic.

The practicality of the compression method is questionable. Adopting low-rank decomposition on gradients requires massive computations. It is unclear whether this operation introduces additional overhead to the distributed training procedure.

### Questions
Please see the weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper  introduces the LASER scheme, a novel communication-efficient distributed optimization approach utilizing plain SGD. In contrast to most existing literature, LASER incorporates considerations for communication noise. The compression method implemented within LASER involves both low-rank representation and gradient scaling, with a detailed algorithmic description provided. Theoretical analyses are included to demonstrate the convergence assurance of the proposed scheme, while experimental evaluations validate the complexity improvements.

### Strengths
1. The algorithm design considers the noise in communication, which is more realistic than most works in literature. The design enables the level of noise to decrease when the norm gradient is smaller. This is important to guarantee good performance of SGD.
2. The convergence analysis of the proposed scheme is comprehensive and the result is reasonable. The convergence rate in quansi-convex and non-convex setting is comparable to literature and standard distributed optimization methods.
2. The experiments setup is closely related to the theoretical analysis and the result is convincing.

### Weaknesses
1. The major concern is the novelty of this work. The low-rank approximation of gradient or weight matrix is a common method in literature. And this method has been applied in distributed learning, especially Federated learning setting, e.g, Zhou, Huachi, et al. "Low rank communication for federated learning." , 2020,Konečný, Jakub, et al. "Federated learning: Strategies for improving communication efficiency." arXiv preprint arXiv:1610.05492 (2016). Thus, I do not think the proposed framework if of great contribution.
2. The power allocation step is also not novel. The method introduced in equation (2) is a standard noise variance minimization method in 'Guo, Huayan, An Liu, and Vincent KN Lau. "Analog gradient aggregation for federated learning over wireless networks: Customized design and convergence analysis." IEEE Internet of Things Journal 8.1 (2020): 197-210.' 
3. The theoretical analysis is based on standard distributed optimization with error feedback. The only difference is the low-rank compression and noise are considered.

### Questions
1. Looks like LASER is a combination of well-known methods(low-rank approximation and noise variance minimization), so is there any major difference or difficulty in theoretical analysis besides the ones are already sound in literature?
2. Could you provide intuitive understanding about why low-rank approximation can induce lower noise variance? Specifically, explain the intuition on the comparison of noise variance in equation (5).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
