# Exploring Adversarial Robustness of Graph Neural Networks in Directed Graphs

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Existing research on robust Graph Neural Networks (GNNs) focuses predominantly on undirected graphs, neglecting the trustworthiness inherent in directed graphs. This work analyzes the limitations of existing approaches from both attack and defense perspectives, and we present an exploration of the adversarial robustness of GNNs in directed graphs. Specifically, we first introduce a new and more realistic directed graph attack setting to overcome the limitations of existing attacks. Then we propose a simple and effective message-passing framework as a plug-in layer to enhance the robustness of GNNs while avoiding a false sense of security. Our findings demonstrate that the profound trust implications offered by directed graphs can be harnessed to bolster the robustness and resilience of GNNs significantly. When coupled with existing defense strategies, this framework achieves outstanding clean accuracy and state-of-the-art robust performance against both transfer and adaptive attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors study adversarial robustness w.r.t. perturbations of the graph structure for directed graphs. They identify a gap in the litreature, namely that most previous robustness studies forcus on undirected graphs. They argue that there is an asymmetry between out-links and in-links and that in some applications it is much easier for an adversary to perturb the in-links compared to the out-links of a target node. They propose RDGA -- a modification of existing attacks with additional restrictions on the out-links of the target node. They also propose a new heuristic defense where we a tunable parameter can place different weights on the in-links and out-links. This change is ortogonal to other defense measures and can be composed with both vanilla GNNs and existing defenses.

### Strengths
The simplicity of the proposed defense is in my opinion its biggest strengths. The experiments suggest that there is a range of $\beta$ values for which the clean accuracy is well mantained while showing a boost in adversarial accuracy -- sugestting that we can improve robustness without a significant trade-off.

The experimental analysis is comprehensive. The addition of adaptive attacks is especially appreciated since they are crucial for properly evaluating heuristic defenses.

The theorethical analysis is interesting even though it relies on many simplifying assumptions.

### Weaknesses
A big weakness of the paper is that the evaluation is focused on citation networks only -- where for the classification task the out-links are already quite informative. It's not clear how much benefit there could be for other types of networks, where e.g. the patterns of in vs. out-links are different. 

The proposed attack can be seen as a relaxation of the even more stringent indirect attack (aslo called the influencer attack by Zugner et al. (2018)) where neither the in-links nor the out-links of the target node can be modified. Therefore, it is not surprusing that the performance is somewhere between the unrestricted and the fully restricted attack. I think elaborating on this connection in the related work is warranted.

Studying the directed setting is imporant, however, whether the attacker is more likely to be able to change the in-links or the out-links depends highly on the application. For example, in social networks it might be true that changing out-links is more difficult but this is not necessarily always the case. Moreover, often there is no "attacker" and we are conducting adversarial robustness studies to quantify e.g. the robustness to worst-case noise -- i.e. treating nature as an adversary. That is to say, I don't think that all future studies should adopt a restricted attack such as the one proposed, but rather include this as another viewpoint.

I think the paper can benefit from further studying the impact of the proposed defense on other aspects of robustness:
- Is the robustness to attribute/feature perturbation positively/negatively affected?
- Does the proposed defense also improved certified robustness (which can be easily tested with one of the black-box randomized smoothing certificates)?
- How is the robustness to global (untargeted) attacks affected?

Essentially the question is what are the trade-offs from adopting the $\beta$ weighted adjacency matrix.

### Questions
1. In the ablation study currently the authors break down the links in terms of 1-hop, 2-hop and others. It would be intresting to see the breakdown in terms of in vs. out-links as well, i.e. show: 1-hop (always in-links), 2-hop in-link, 2-hop out-link, etc.
2. How does this approach compare to the more stringent indirect (adaptive) attack?
3. In Table 4 the masking rate starts at 50\%, it would be insightful to also show lower masking rates, and in particular 0\% which would correspond to unrestricted attacks. This will help in understanding whether the proposed defenses is "universally" helpful for different threat models.
4. It should be straightforward to set different $\beta$ values for each node, rather than a single global value. Tuning can be avoided by setting these values based on the theory.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the adversarial attack and robustness on directed graphs. The authors first propose a simple and more practical setting for attacks on directed graphs which restricted the perturbations on out-links. They conduct experiments with undirected graph neural networks to show there might be a false sense of robustness on directed graphs. To overcome this issue and to enhance the robustness of directed graph, the authors propose a biased bidirectional random walk, which balance the trustworthiness of out-links and in-links with a hyper-parameter $\beta$. They also provide a comprehensive theoretical analysis on the optimal selection of this hyper-parameter. When coupled with the proposed plug-in defense strategy, this framework achieves outstanding clean accuracy and state-of-the-art robust performance against both transfer and adaptive attacks.

### Strengths
1. The proposed message-passing framework is a simple and effective approach by leveraging the directional information to enhancing the robustness of GNNs in directed graphs.

2. The paper introduces a new and more realistic directed graph attack setting to overcome the limitations of existing attacks.

3. The paper provides a comprehensive evaluation of the proposed framework and compares it with existing defense strategies on undirected graphs. The experiment results and findings demonstrate that the proposed framework achieves outstanding clean accuracy and state-of-the-art robust performance against both transfer and adaptive attacks.

4. This work presents an innovative approach to GNN attacks, focusing on improving the robustness and trustworthiness of directed graphs.

### Weaknesses
1. The description of the attack setting in this paper requires further clarification and precision. If I am understanding correctly, in terms of commonly used terms for adversarial attacks on graphs, this paper focuses on a target attack, while the transfer attack indicates the gray-box attack and adaptive attack is the white box setting. A more explicit definition and distinction between these terms would enhance the reader’s comprehension and align the terminology with established norms in the field.

2. The section discussing catastrophic failures due to indirect attacks seems somewhat disjointed from the existing body of work on directed graphs. The majority of experiments in Table 1 are centered around undirected graph neural networks, leading to a claim of a severe false sense of robustness against transfer attacks in these networks. Given the paper’s earlier assertion that out-links and in-links should be treated distinctly in directed graphs, this leap in logic is perplexing and necessitates a more thorough explanation. A more robust motivation could potentially be achieved by exploring existing attacks on directed graph neural networks, such as DiGNN and MagNet.

3. The proposed attack budget settings, encompassing 25%, 50%, and 100%, appear impractical and neglect the crucial aspect of attack unnoticeability. A more realistic and subtle approach to defining attack budgets would likely yield more applicable and insightful results.

4. The paper seems to lack a discussion on related works specifically addressing attacks or defenses in directed graphs. Clarification is needed as to whether this work stands alone in its focus on directed graph robustness or if there are other relevant studies in this domain.

5. The paper’s approach to conducting adaptive attacks solely on undirected graph neural networks raises questions of fairness and relevance, given the unique characteristics of directed graphs. If the issue stems from challenges related to gradient backpropagation, it would be beneficial to consider relevant baselines, such as Rossi, Emanuele, et al. "Edge Directionality Improves Learning on Heterophilic Graphs." arXiv preprint arXiv:2305.10498 (2023).

Minor Issues:
1. The paper would benefit from the inclusion of explanations for specific notations used, such as $\mathcal{N}$ in section 2.2 on adversarial capacity, and $A_{sym}$ in section 3.1, to aid reader comprehension and provide a more seamless reading experience.

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
2 fair

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
This paper focuses on the adversarial attack robustness on directed graphs. This paper introduces a directed attack setting, differentiating between out-link and in-link attacks. The authors propose a message-passing layer, Biased Bidirectional Random Walk (BBRW). The experiments demonstrate the robustness of BBRW.

### Strengths
1. This paper focuses on an important problem, the adversarial robustness of GNN.
2. This paper proposes Biased Bidirectional Random Walk (BBRW) with theoretical analysis.
3. Experiments show the robustness of BBRW.

### Weaknesses
1. This paper lacks empirical evaluations on larger datasets, such as ogb datasets[1] or reddit[2], which makes us concerned about usefulness on large networks. 
2. This work lacks some necessary baselines, making the experiments unreliable. It is recommended to add the adversarial training method FLAG[3], as well as graph purification methods GARNET[4], ProGNN[5], and STABLE[6]. 
3. The experimental settings are unclear.
    a) Section 4.1 states, "We randomly select 20 target nodes per split for robustness evaluation." If my understanding is correct, does this mean 20 nodes are selected per split for training, validation, and testing, totaling 60 nodes? If so, there are 20 nodes from the training set, and is it reasonable to evaluate accuracy on the training set?
    b) Regarding "multiple link budgets ∆ ∈ { 0%, 25%, 50%, 100% } of the target node’s total degree," when ∆=100%, are the attack still imperceptible? Is it necessary to preserve the original label prediction?
    c) It would be useful to report the model's accuracy when the attack perturbation is at 5%, 10%, 15%, and 20%, as done in other studies[5,6].
4. The high accuracy of the GCN under 25% adaptive attack does not align with the findings of the original paper[7]. Please provide performance under the same adaptive attack settings as in the original paper[7].

### Questions
1. The performance of BBRW is incredible, as mentioned in Section 4.3. What contributes to its effectiveness?
2. How does BBRW handle node injection attacks[1,2]? In these attacks, only nodes or edges are injected, with the injected edges being directed. This scenario is practical and worth exploring.

[1] Xu Zou, Qinkai Zheng, Yuxiao Dong, Xinyu Guan, Evgeny Kharlamov, Jialiang Lu, and Jie Tang. Tdgia: Effective injection attacks on graph neural networks. KDD ’21.
[2] Shuchang Tao, Qi Cao, Huawei Shen, Junjie Huang, Yunfan Wu, and Xueqi Cheng. Single node injection attack against graph neural networks. CIKM ’21.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper delves into the domain of adversarial machine learning, focusing on the vulnerabilities of deep neural networks when faced with adversarial attacks. The authors present a broad study of various adversarial attack methods and their defences, evaluating their effectiveness on multiple datasets. By introducing a novel evaluation metric, the paper seeks to shed light on the nuances of designing robust models and offers a foundation for further research in the critical area of AI security.

### Strengths
This paper explores an interesting topic of trustworthy GNNs, i.e., the robustness of the GNNs for directed graphs. The authors conduct preliminary evaluations on the vulnerability of current GNN models, followed by discussing the observations. Next, they proposed a new operation to promote the robustness of GNNs.

### Weaknesses
1. The thread model should be presented in the section 2.2.

2. It is worth noting that the current attacking algorithm focuses on the gradient-based method. Other attack method (e.g., RL-based methods) should also be reviewed.

3. Current attacks range in budgets from 25% to 100%. However, adversarial samples should be generated by considering a limited budget (e.g., k edges, k<=5). Authors are suggested to report the evaluation results on a limited budget, as the proposed 100% perturbations are extremely noticeable.

4. Unclear statement. Authors are suggested to explain the details of the so-called adapative attacks.

4. Limited practicality. As mentioned by the authors, out-links are generated by proactive behaviours from the source nodes, and their awareness of these out-links makes the hardness of manipulate malicious perturbations (i.e., adding out links for target nodes). This consideration makes the 1-hop perturbations practical and 2-hop perturbations unpractical. 

5. Logical flaws. When considering the graph structure in GNNs, the authors proposed that the A is generated from out-links. In this case, authors are suggested to explain why the 1-hop perturbations are effective for the target nodes, as these perturbations should not be involved in the message aggregation of GNNs. On the other hand, the out-link should be avoided because of their noticeability. Given these considerations, the authors are suggested to explain how to use in-links to attack target nodes in this paper. Otherwise, section 3 should conduct evaluations on GNNs devised for directed graphs.

6. Confusing contributions. If this paper is designed to propose a new method to defend GNNs on directed graphs, the proposed method should be integrated into the above GNNs. If this paper aims to devise a new GNN architecture for directed graphs, comparisons should not focus only on robustness. Performance evaluations on other datasets should be presented in this paper.

7. Missed evaluations. As discussed above, the proposed method only be evaluated on two datasets. The evaluations on other datasets (e.g., large-scale datasets) should be included to verify the effectiveness of the proposed method.

### Questions
Refer to the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
