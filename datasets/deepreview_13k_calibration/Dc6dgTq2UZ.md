# Towards Distributed Backdoor Attacks with Network Detection in Decentralized Federated Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Distributed backdoor attacks (DBA) have shown a higher attack success rate than centralized attacks in centralized federated learning (FL). However, it has not been investigated in the decentralized FL. In this paper, we experimentally demonstrate that, while directly applying DBA to decentralized FL, the attack success rate depends on the distribution of attackers in the network architecture. Considering that the attackers can not decide their location, this paper aims to achieve a high attack success rate regardless of the attackers' location distribution. Specifically, we first design a method to detect the network by predicting the distance between any two attackers on the network. Then, based on the distance, we organize the attackers in different clusters. Lastly, we propose an algorithm to \textit{dynamically} embed local patterns decomposed from a global pattern into the different attackers in each cluster. We conduct a thorough empirical investigation and find that our method can, in benchmark datasets,
outperform both centralized attacks and naive DBA in different decentralized frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose a distributed backdoor attack method. The core of the work is based on the insight that the attack success rate depends on the distribution of attackers in the network architecture. The authors design a topology detection method to detect the network by the distance of the attackers, and then organize the subsequent attacks based on the distance to improve the attack success rate. Experimental results show that the proposed method outperforms traditional centralized attacks and the naive distributed backdoor attack.

### Strengths
- The proposed work is the first to investigate the distributed backdoor attack method on decentralized federated learning tasks.
- Experimental results show that the proposed method achieves a higher attack success rate than traditional methods.

### Weaknesses
 - The work lacks discussion on the key parameters of the proposed method in the experiment, such as the number of clusters.
- The authors should add more ablation studies to evaluate the contribution of each module to the attack success rate.

### Questions
Please refer to the weaknesses for rebuttal. I will check the related content carefully.

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
3

### Summary
The authors examine distributed backdoor attacks in decentralized FL, introducing a method to detect attackers by estimating distances between them, clustering attackers accordingly, and proposing an algorithm to dynamically embed local patterns from a global pattern into each cluster.

### Strengths
1. It is interesting to consider the topology of decentralized FL and LSTM seems like a reasonable way to predict the distance. 
2. The authors consider dynamically embed the backdoor trigger instead of using fixed patterns.

### Weaknesses
1. DBA takes into account factors like location and size, resulting in potentially infinite combinations of triggers. Even with a dynamic selection method, there's no guarantee that the chosen combination will be optimal or near optimal. A more fundamental approach might involve using a generative model to implant invisible/stealthy triggers (as pixels), such as [1], to optimize the trigger more effectively. The current approach lacks a clear strategy for exploring the vast trigger space, and it's unclear how the dynamic selection method avoids getting stuck in local optima. The paper does not address the computational cost of exploring this space, which could be prohibitive.
2.  Considering the clustering method as a major contribution to this paper, ablation studies are needed to assess the improvement gained from introducing clustering (and the number of clusters, threshold distance to dividing clusters) compared to not using clustering in a fair comparison. The paper needs to show how the choice of clustering algorithm impacts the results. Moreover, the paper does not discuss the sensitivity of the method to the distance threshold used for clustering, which could significantly affect the performance.
3. To showcase the effectiveness of proposed attack, performance under defense mechanisms is needed. The paper should demonstrate how the proposed attack fares against common defense mechanisms used in federated learning, such as gradient clipping or robust aggregation methods. Without such evaluation, it is difficult to assess the practical relevance of the proposed attack.

### Questions
1. Have the authors considered other methods to enhance backdoor attacks durability like [1]
2. Since MNIST and CIFAR-10 each have only 10 classes, does the number of classes matter?
3. Can the current method effectively handle more complex real-world topologies in terms of scalability and performance guarantees?

[1] Zhang, Zhengming, et al. "Neurotoxin: Durable backdoors in federated learning." International Conference on Machine Learning. PMLR, 2022.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates distributed backdoor attacks (DBA) in the context of decentralized federated learning (DFL), where there is no central server. Traditional DBA methods, which work effectively in centralized settings, often experience reduced success rates in decentralized systems due to the varying influence of adversarial clients based on their network location. To address this, the authors propose a two-step approach: first, a method to estimate distances between adversarial clients in the network, and second, a clustering-based algorithm to maximize attack success by dynamically organizing the distributed backdoor attacks based on network topology. Through experiments on various DFL frameworks, the authors demonstrate that their method achieves higher attack success rates than standard DBA and centralized backdoor approaches.

### Strengths
The paper presents an innovative approach by introducing distributed backdoor attacks (DBA) specifically tailored for decentralized federated learning (DFL), an area that has seen limited exploration.

### Weaknesses
Although the proposed attack method is shown to be effective, the paper does not sufficiently explore potential defensive strategies against this enhanced DBA approach.

The success of the proposed approach heavily relies on the accuracy of topology detection and clustering. However, there is limited discussion on the potential impact of inaccuracies in clustering or topology estimation on the overall attack success rate.

The clustering and trigger decomposition steps involve hyperparameters, such as cluster size and trigger distribution patterns. However, the paper does not provide sufficient insight into how sensitive the method’s performance is to these parameters.

The method relies heavily on accurate distance estimation between adversarial clients. The paper does not discuss how inaccuracies in these estimates might affect the attack's effectiveness, especially in dynamic or less predictable network environments where client distances may vary.

### Questions
See the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates Distributed Backdoor Attacks (DBA) within a decentralized Federated Learning (FL) framework. The authors demonstrate that the attack success rate of DBA in decentralized settings is impacted by the distribution of attackers across the network. To address this, the paper introduces a two-step strategy: (1) a method to detect network topology by predicting distances between attackers, allowing them to cluster, and (2) an enhanced DBA method where attack patterns are distributed dynamically within clusters to optimize the attack’s impact across various network topologies. Experimental results show that the proposed approach improves attack success rates over traditional DBA and centralized attacks on standard datasets (CIFAR-10 and MNIST).

### Strengths
- Overall, the structure of this paper is easy to follow. 
- The problem studied is sound and important.
- The dynamic cluster-based trigger distribution is interesting.

### Weaknesses
 - This paper’s contribution is somehow limited as it only focuses on DBA. While DBA in decentralized FL is a novel attack, the study does not discuss possible defense mechanisms, which could provide a more balanced perspective.
- The clustering and dynamic distribution of triggers may become computationally expensive with a larger number of attackers and clients. 
- The approach assumes attackers can communicate to coordinate poisoned images and agree on target labels, which may not be practical in a real-world adversarial setting.

### Questions
- How would the clustering algorithm handle larger networks with significantly more clients and attackers? 
- How practical is it for attackers to synchronize their attacks across clusters in real-world decentralized FL applications with limited communication? 
- Have any potential defense mechanisms been considered that could mitigate the effectiveness of the proposed DBA in decentralized FL? 
- How sensitive is the method’s effectiveness to inaccuracies in distance prediction? Is there a tolerance threshold?
- Could this method be extended to other types of adversarial attacks in decentralized FL, such as data poisoning or model inversion attacks?

### Soundness
2

### Presentation
3

### Contribution
2
