# Federated Instruction Tuning of LLMs with Domain Coverage Augmentation

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Federated Domain-specific Instruction Tuning (FedDIT) utilizes limited cross-client private data together with server-side public data for instruction augmentation, ultimately boosting model performance within specific domains. To date, the factors affecting FedDIT remain unclear, and existing instruction augmentation methods primarily focus on the centralized setting without considering distributed environments. Our experiments reveal that the cross-client domain coverage, rather than data heterogeneity, drives model performance in FedDIT. In response, we propose FedDCA, which optimizes domain coverage through greedy client center selection and retrieval-based augmentation. For client-side computational efficiency and system scalability, FedDCA$^*$, the variant of FedDCA, utilizes heterogeneous encoders with server-side feature alignment. Extensive experiments across four distinct domains (code, medical, financial, and mathematical) substantiate the effectiveness of both methods. Additionally, we investigate privacy preservation against memory extraction attacks utilizing various amounts of public data. Results show that there is no significant correlation between the volume of public data and the privacy-preserving capability. However, as the fine-tuning rounds increase, the risk of privacy leakage reduces or converges.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FedDCA, a novel approach to federated learning for domain-specific LLM instruction tuning that focusses on coverage, as opposed to heterogeneity (non-iid ness). Instead of worrying about how different each client's data is from others (data heterogeneity), the authors show that what really matters is how well the combined data from all clients covers the target domain. This insight leads to their proposed method which uses client selection and data augmentation strategies to maximize domain coverage.

The authors demonstrate their approach across four domains (code, medical, financial, and mathematical), showing significant improvements over existing methods. They also introduce a more computationally efficient variant called FedDCA* that uses different-sized encoders for clients and servers. While the paper lacks some theoretical guarantees and has limited privacy analysis, it presents a promising new direction for federated learning with LLMs by focusing on domain coverage rather than trying to manage data heterogeneity.

The authors do not provide any additional methods to guarantee privacy (no DP), though it is common in FL papers, also they mount extraction attacks to measure memorization.

### Strengths
1. novel idea and surprising insight, regarding coverage vs. heterogeneity.

2. Extensive and thorough experimentation

### Weaknesses
1. There is one main concern I have, maybe because I have not been following FL literature recently, but it seems like the baselines are all from 2020! I wonder why, is the setup not realistic? The paper cites Ye et al. 2024 (openfedllm) which is recent, but they only compare against in table 3, why not table 2? is it because the FedIT method there is the backbone to this method?


2. Minor: seems like clients are limited to 10, which is a bit low. Also I wonder how DP would come into play, but this is not necessary to study.

### Questions
Please respond to the weaknesses above. 

Also

How do you isolate whether the improvements come from your domain coverage method versus simply having more training data? Did you control for total training data size when comparing methods?

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
The paper proposes a new method for federate instruction fine tuning for LLMs.
The main idea involves around using cluster center info coming from clients to select publicly available data stored on the server to augment the local data to achieve better coverage.

### Strengths
+ The paper is motivated well.

+ The paper is easy to read.

+ Provides a basic clustering method that could improve the federated fine tuning process.

### Weaknesses
 - To me, the main question I have is that whether FedAvg and variants developed for dealing with Non-IID data combined with simple random sampling of the public data could achieve similar results.   The main reason is that Federated learning by itself is not sending data to the clients and just aggregates the client updates. Therefore, it is not surprising to me that sending more data to clients help even if this is done carefully using clustering as suggested in the paper. Therefore, how about sending some random data to clients and then use standard FL techniques especially the ones developed for non-iid settings.    Hence, I highly recommend the authors to explore this setting. One initial experiment could be to send the random data (e.g., the same amount sent using the clustering approach) to each client and then use FedAvg to see the performance. 

- The privacy experiments are good but not itself it is not adequate ( I understand that this is not the focus of this paper and I did not use this comment in any negative way in my ranking), I think a setting where noise is added during aggregation (e.g., something of differential privacy sense) can be evaluated. As a starting point, Gaussian noise could be added to achieve \epsilon-\delta differential privacy. Again this could be considered in the future work.

### Questions
Please see my first comment in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a federated domain-specific instruction tuning method to enable federated clients to utilize data from the server to augment their local data. The objective of this work is meaningful, as FL does indeed face the issue of insufficient data on the client-side. However, the assumption that there exists a large dataset on the server encompassing all domains seems unrealistic. If such a dataset is available on the server, why would there still be a need for FL to tune LLMs? Additionally, compared to traditional FL, this approach poses a risk of exposing additional information from the client-side data (such as domain information) to the server. In summary, I believe this work requires further refinement.

### Strengths
1. This manuscript is well-written and well-organized, making this work easy to understand.
2. Extensive experiment evaluations are provided.

### Weaknesses
 1. The main distinction between the proposed method and previous approaches is its ability to leverage server-side data, with the effectiveness of the method relying on the server holding a dataset that encompasses multiple domains. In fact, many LLM tuning methods based on FL aim to explore the possibility of tuning LLMs with client-side data when centrally collected data has been exhausted. If there is already a dataset on the server that encompasses multiple domains, why would we still need FL to tune the model? Wouldn't it be better to fine-tune the LLM directly on the central server?
2. In the experiments, it is mentioned that "each client has 100 local instructions and obtains 5000 augmented public instructions from the server." (line 885). In this case, the majority of the data is contributed by the server, and the significance of introducing FL seems unclear. Furthermore, the performance gains observed appear to correlate strongly with the volume of server-side data used for augmentation, suggesting that the method's effectiveness is primarily driven by the quantity of server data rather than the federated learning approach itself.
3. This work builds upon the original FL paradigm by providing additional client-side information, specifically client-side cluster centers. Although the original data remains on the client side, it is inappropriate to directly claim that "it does not violate the client’s privacy." Such a kind of information may reveal the distribution of client-side data, thereby exposing client data to privacy leakage threats such as membership inference attacks, which do not require direct access to the original data. As FedDCA describes as a distinguishing feature from other existing methods, it sends data from the server's public dataset that are related to a specific client to that client as augmentation. Doesn’t this imply that the server can determine the data domains of that client to some extent?
4. One of the claimed contribution, "no linear correlation between the degree of heterogeneity and model performance" has already been revealed by one of the cited works [1], which weakens the contribution of this work to a certain extent.
5. To the best of my knowledge, the appropriate citation of FedIT should be [2], which has been proposed in 2023, rather than (Ye et al., 2024b;a) in Line 764.
6. The codes are not available, making the reproducibility of this work difficult to assess.

### Questions
1. How are the four baselines based on FedIT implemented? Do they involve directly tuning and transmitting all parameters, or only PEFT adapters?
2. How is the weight of the projector in FedDIT* obtained? It seems that many details have not been provided in Appendix A.4.
3. Please refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a federated instruction tuning approach. The authors assume the existence of a large public dataset that covers all domain data, while each domain only has a small subset of data. The paper introduces multiple techniques, including greedy client center selection and domain data retrieval, to achieve data selection from the public dataset and improve the performance of federated instruction tuning. Furthermore, a heterogeneous encoder approach is introduced to further enhance efficiency. The experiments demonstrate that this data selection approach improves performance compared to client-data-only fine-tuning baselines.

### Strengths
1. This approach highlights domain coverage as the main bottleneck for federated instruction tuning.

### Weaknesses
1. The finding that motivates this research—"there is no linear correlation between the degree of non-independent and identically distributed (IID) and LLM performance in the context of FedDIT"—requires further evidence and rephrasing to avoid being misleading. First, "linear correlation" is a very strong term and may be inappropriate here; the authors likely mean "monotonicity" instead of "linearity." Second, the current experiments are insufficient to draw definitive conclusions. The results are not conducted over multiple rounds, nor do they report the mean and standard deviation of performance, which makes them highly dependent on the seed, especially in the Dirichlet instance split. Third, the number of clients (10, with 2 clients involved in each round) is relatively small and may not be significantly affected by $α$. Fourth, averaging performance across multiple datasets or tasks is problematic. For instance, in Table 1, Method 2 is clearly better than Method 1 on multiple datasets, but the average shows the opposite.

**Table 1. Performance of Method 1 and Method 2 on Binary Classification Tasks**

| Method  | Method 1  | Method 2 |
| ------- | --------- | -------- |
| Data 1  | 98%       | **99%**  |
| Data 2  | 98%       | **99%**  |
| Data 3  | 98%       | **99%**  |
| Data 4  | 98%       | **99%**  |
| Data 5  | **52%**   | 47%      |
| Average | **88.8%** | 88.6%    |

2. The assumption that there exists a public dataset requires further clarification regarding its prevalence in practice. Clarification is needed on whether there are real-world applications that align with this assumption. It is also necessary to determine how much of the improvement is due to the additional data versus the algorithmic design. Furthermore, it should be clarified whether the public multi-domain dataset needs to be within the domain of the clients, or if it can be out-of-domain data.

3. The method of retrieving similar public instructions to domain instructions requires the public dataset to already cover all domains (i.e., contain full domain knowledge). However, it is unclear which baseline uses this large, powerful public dataset for fine-tuning. It would be interesting to see the results of:

- Fine-tuning with the same public dataset.
- Fine-tuning with the public dataset followed by further federated fine-tuning with private clients' local dataset.

Including these baselines would significantly enhance the convincing nature of the experiments.

4. The experimental setting is unrealistic. In line 996, the authors randomly select 1,000 samples from the in-domain instruction set and split them into 10 shards as each client's local dataset, leaving the remaining 20x to 200x samples for the public dataset. The necessity of federated learning is questionable if such a large, independent and identically distributed (IID), noise-free public dataset exists.

**Minor Comments**

1. The format of Table 1 is difficult to read. It is unclear which entries represent methods and which represent metrics, as well as how to interpret the different metrics.

### Questions
1. Does random sampling baseline make a sample of each client's domain data? In Table 1, random sampling generally outperforms full-data fine-tuning. However, the introduction claims that FedIT requires a sufficient amount of instruction data. If this is true, why does down-sampling lead to an increase in average performance? More evidence is needed to support the motivation.

2. In "Results demonstrate that domain coverage significantly influences model performance in the corresponding domain," is this conclusion drawn from the experiments in this manuscript or from Wang et al. (2023)?

### Soundness
1

### Presentation
1

### Contribution
2
