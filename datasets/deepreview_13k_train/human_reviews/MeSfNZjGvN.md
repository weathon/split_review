# FedPeWS: Personalized Warmup via Subnetworks for Enhanced Heterogeneous Federated Learning

- Decision: Reject
- Scores: 3, 3, 1, 3

## Abstract
Statistical data heterogeneity is a significant barrier to convergence in federated learning (FL). While prior work has advanced heterogeneous FL through better optimization objectives, these methods fall short when there is \textit{extreme} data heterogeneity among collaborating participants. We hypothesize that convergence under extreme data heterogeneity is primarily hindered due to the aggregation of conflicting updates from the participants in the initial collaboration rounds. To overcome this problem, we propose a warmup phase where each participant learns a personalized mask and updates only a subnetwork of the full model. This \textit{personalized warmup} allows the participants to focus initially on learning specific \textit{subnetworks} tailored to the heterogeneity of their data. After the warmup phase, the participants revert to standard federated optimization, where all parameters are communicated. We empirically demonstrate that the proposed personalized warmup via subnetworks (\texttt{FedPeWS}) approach improves accuracy and convergence speed over standard federated optimization methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a personalized federated learning algorithm called FedPeWS. The paper proposes to split the learning rounds into two parts. The first $W$ rounds is called warmup phase where each client learns a personalized subnetwork of the model. The key parts of the proposed algorithm is to identify the subnetwork for each client and determining the warmup length.

### Strengths
The paper studies the problem of personalized federated learning from learning subnetworks point of view. The presentation of the paper is good.

### Weaknesses
 - The proposed algorithm is too intuitive. And reading the paper I am not clear why the proposed algorithm can help personalized federated learning. Also reading the introduction, the motivation is not convincing to me.
- Since this work is based on intuitions, I believe the paper should improve the experimental study significantly. Specifically, I believe the paper should add more baselines to the paper with more analytical explanations about the result.

### Questions
Based on my understating, in the first phase each client learns its own subnetwork. Then in the second phase the proposed algorithm employs federated averaging. Can you explain why does the algorithm split the learning rounds into two parts? I am not clear about the intuition behind this and its helpfulness in personalized federated learning.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To address the problem of extreme data heterogeneity in federated learning, this paper starts from the perspective of initialization. It argues that an appropriate personalized initial method can enable the clients to quickly learn their local data well before engaging in broader collaboration, and thus achieve faster convergence and a higher final accuracy. In this paper, the authors propose FedPeWS, a personalized warm-up method for the initial phase of federated learning training, which simultaneously optimize the personalized masks of the clients and update the corresponding sub-networks during the initial warm-up phase to enables the global network to adapt faster and better to extreme data heterogeneity scenarios. Experimental results under various scenarios and parameter settings validate the effectiveness of this method.

### Strengths
1. This paper addresses the problem of data heterogeneity from a novel perspective. 
2. The authors have conducted extensive experiments under a variety of datasets and made a detailed analysis of the ablation experiments around the relevant parameters.

### Weaknesses
1. As mentioned by the authors, this paper lacks proofs related to convergence, and therefore at the same time, it fails to give an analysis of the relationship between hyperparameters such as $\lambda$, $\tau$ and convergence to determine a better range of theoretical values. Therefore for different experimental scenarios, perhaps multiple experiments (e.g. grid search) are required to determine the most suitable parameter values, which has limitations in terms of generalizability and cost. Furthermore, the paper does not provide sufficient guidance on how to choose these parameters in new scenarios, making the method less practical for real-world applications where extensive hyperparameter tuning is not feasible. The lack of theoretical analysis also makes it difficult to understand the sensitivity of the method to these parameters, which could lead to unpredictable performance in different settings.
2. The experimental results show that the effectiveness of FedPeWS and FedPeWS-Fixed methods are comparable, and in some stages FedPeWS-Fixed even outperforms FedPeWS, which I think is an issue that should not be ignored. In conjunction with Appendix B.2, I think FedPeWS-Fixed is a rigid approach to divide the network evenly and fixedly, while the FedPeWS method dynamically optimizes the personalized masks to select the appropriate sub-networks. Intuitively this dynamic optimization method should be more effective than the simple fixed division method, but the experimental results are the opposite, does it mean that the dynamic optimization method of FedPeWS does not achieve much extra gain? I think this is a question worth analyzing. The comparable performance, and sometimes worse performance, of FedPeWS compared to FedPeWS-Fixed raises concerns about the actual benefit of the dynamic mask optimization. If a static, simpler approach performs as well or better, the added complexity of FedPeWS may not be justified, and this needs to be addressed with further analysis and experiments.

### Questions
1. Since the research purpose of this paper is to solve the problem of extreme data heterogeneity, more comparisons can be made with some of the current state-of-the-art methods for solving data heterogeneity. I think that besides the FedProx method mentioned in this paper, the MOON [1] method is also a worthy comparison. And I think FedPeWS is essentially an initialization method, so it can also be combined with methods such as PFL [2] in the subsequent standard federated optimization to investigate whether this method, FedPeWS, can bring further enhancement to the existing state-of-the-art methods.
2. In the related experimental descriptions of Table 1 and Table 2, there is no mention of the number setting of clients N. If I understand correctly, the settings on synthetic datasets for both experiments are N=2. This implies that when comparing with FedProx, the comparison has been made only in the scenario of synthetic datasets (N=2). If possible, I'd like to see experimental comparisons with the FedProx method under more datasets (and at the same time larger N value).
3. In this paper, collaboration rounds are used in the experimental part of the main text to compare the convergence speeds of FedAvg and FedPeWS, but since FedPeWS contains a greater computational overhead for one collaboration round during the warm-up phase (but only need to transmit sub-network, which is theoretically less expensive in terms of communication overheads), simply comparing the number of rounds is not convincing enough. Although the experimental analysis for wall-clock time is also presented in the Appendix, it can also be seen that FedPeWS does take more time in the warm-up phase, and thus the balance between the parameter $\tau$ and the actual convergence speed is very important in practical applications. To summarize, I think how to determine the size of the warm-up rounds $W$, or the size of $\tau$, in the experiments is an issue worth discussing, which also involves the analysis of the overall computational and communication overheads. (By the way, if I understand correctly, $\tau =25$ in Appendix C.4 should be changed to $W=25$)

[1] Li, Qinbin, Bingsheng He, and Dawn Song. "Model-contrastive federated learning." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.
[2] Arivazhagan, Manoj Ghuhan, et al. "Federated learning with personalization layers." arXiv preprint arXiv:1912.00818 (2019).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes "FedPeWS," a personalized warmup method for federated learning (FL) using subnetwork masking to improve model convergence under extreme data heterogeneity. It introduces a warmup phase where each participant trains a personalized subnetwork before switching to standard federated optimization, claiming enhanced accuracy and efficiency over baseline methods.

### Strengths
The paper studies an important problem which is convergence and performance issues of FL under extreme data heterogeneity.

### Weaknesses
Overall, while this paper attempts to address challenges in federated learning under extreme data heterogeneity, there are several critical issues regarding its hypotheses, methodology, and experimental validation. I hope these comments provide constructive insights for improvement:

* The paper is built upon unproven hypotheses, especially as stated in the abstract (lines 15-17): "we hypothesize that ... rounds." Presenting such assumptions without experimental or theoretical proof weakens the foundation of the study. For any claim regarding the benefits of a personalized warmup phase, empirical or theoretical evidence is essential to establish credibility. The core hypothesis that a personalized warmup phase leads to better convergence by aligning subnetworks with individual client data distributions is not sufficiently justified. The paper lacks a clear explanation of why this alignment should occur, and how it specifically addresses the challenges of data heterogeneity. The authors need to provide a more rigorous justification for this core assumption, possibly through theoretical analysis or more targeted experiments.
* In lines 44-45, the authors suggest that the primary cause of federated learning failure under extreme data heterogeneity lies in high conflict between local updates during initial rounds. This premise is misleading, as conflicts due to objective misalignment and heterogeneity persist throughout the entire FL process, not just in early rounds. A more nuanced discussion around ongoing client conflicts across rounds would provide a clearer picture of challenges in FL. The paper's focus on early-round conflicts seems to ignore the persistent challenges of data heterogeneity throughout the federated learning process. The authors should acknowledge that conflicts and objective misalignment are not limited to the initial rounds and that their method should address these ongoing issues.
* Lines 51-53 mention that each participant uses a personalized binary mask to learn local data distributions and optimize local (sparse) models. However, there is no clear explanation of how the nonlinear parameter space of a model can be mapped directly to each client’s data distribution. To the best of my knowledge, there is no work which has been able to drive a specific subnetwork structure representing the data distribution in NN with non-linear activation. The paper does not provide a theoretical basis for why a subnetwork structure would directly correspond to a specific data distribution. The claim that a binary mask can effectively capture the nuances of a client's data distribution is not well-supported. The authors need to provide a more detailed explanation of how the mask is related to the data distribution, and why this approach is effective. The connection between the mask and the data distribution needs to be more rigorously established.
* The paper’s methodology seems to extend existing techniques without substantial innovation. Additionally, recent work in FL initialization with pre-trained models has shown that warmup rounds may not be necessary, as initialization with pre-trained or meta-learned models can often yield better results. A thorough discussion of and comparison with these approaches would better position the contributions within the current literature. I also urge the authors to enhance their literature review. The paper does not adequately address the existing literature on initialization techniques in federated learning, particularly those using pre-trained models. The authors need to discuss how their method compares to these approaches and justify why a personalized warmup is necessary when other initialization strategies may be more effective. The novelty of the proposed method is not clearly established in the context of existing work.
* The experimental setup lacks robust benchmarks, as it does not evaluate the method on deeper architectures or complex datasets like CIFAR-100. Additionally, comparisons with state-of-the-art FL methods (such as those involving advanced initialization or optimization techniques) would strengthen the empirical evaluation and actual benefits of the method. Right now, the actual benefits of method are questionable.

### Questions
See comments above.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper develops a warmup algorithm to tackle data heterogeneity in federated learning. The idea is to first allow clients to personalize their models in initial rounds, and then adopt conventional federated approach. Some experiments are provided to showcase the effectiveness of the algorithm. The paper is well written and easy to read.

### Strengths
- The idea of using independent subnet training in federated learning looks quite novel and reasonable to the reviewer.
- The paper is well written and easy to follow.

### Weaknesses
While the reviewer appreciates the novelty of the approach, they are a set of concerns/comments/questions:

- While the paper emphasizes that the primary benefit of the algorithm is improved convergence, there is a lack of theoretical analysis. 
- How does the proposed method differ from FedPM (Isik et al., 2023) which also uses mask training? 
- The biggest concern from the reviewer is that the numerical results are on a relatively simple setting:
   -- The datasets are too simple. The authors are suggested to try harder ones, e.g., CIFAR100, (Tiny) Imagenet
   -- The model used are too simple. The authors are suggested to try ResNet and ViT
   -- The comparison to SOTA is missing. Current comparison only involves FedAvg and FedProx and is far from enough. The authors are suggested to MOON, FedOpt, FedUV, etc.
   -- The number of clients is too small. While the authors tried N=200 in the appendix, the improvement is much less obvious than the simple setting in the main text. 
   -- Important ablation study is missing. For example, the authors might try replacing the current warmup strategy by random neuron sampling and other IST approaches. 
   -- Data heterogeneity with \alpha being 0.1 is not extreme. The authors are suggested to try smaller values, e.g., 0.01.

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
