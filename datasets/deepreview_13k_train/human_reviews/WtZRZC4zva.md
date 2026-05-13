# Privately Learning from Graphs with Applications in Fine-tuning Large Pretrained Models

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Graphs offer unique insights into relationships and interactions between entities, complementing data modalities like text, images, and videos. By incorporating relational information from graph data, AI models can extend their capabilities beyond traditional tasks. However, relational data in sensitive domains such as finance and healthcare often contain private information, making privacy preservation crucial. Existing privacy-preserving methods, such as DP-SGD, which rely on gradient decoupling assumptions, are not well-suited for relational learning due to the inherent dependencies between coupled training samples. To address this challenge, we propose a privacy-preserving relational learning pipeline that decouples dependencies in sampled relations during training, ensuring differential privacy through a tailored application of DP-SGD. We apply this method to fine-tune large language models (LLMs) on sensitive graph data, and tackle the associated computational complexities. Our approach is evaluated on LLMs of varying sizes (e.g., BERT, Llama2) using real-world relational data from four text-attributed graphs. The results demonstrate significant improvements in relational learning tasks, all while maintaining robust privacy guarantees during training. Additionally, we explore the trade-offs between privacy, utility, and computational efficiency, offering insights into the practical deployment of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on relational learning for graphs, tackling the challenge in existing privacy-preserving methods, where approaches (like DP-SGD) rely on a gradient decoupling assumption that doesn’t hold in graphs. To address it, this paper proposes a relational learning pipeline that can decouple dependencies in sampled relations, making it possible to adapt these privacy-preserving methods. Specifically, it introduces a decoupled sampling strategy for relations, ensuring that perturbation on a relation affects at most one loss term at a time. This approach is applied to fine-tuning LLMs on sensitive graph data.

### Strengths
S1. This work claims to be the first to explore privacy-preserving methods for relational learning, filling a gap where previous works focus only on entity-level privacy in graphs. 

S2. Besides proposing a decoupled sampling strategy to preserve the privacy of relations, it also tackles the efficiency challenge in fine-tuning LLMs in the private relational learning setting, by leveraging low-rank characterization of per-sample gradients. 

S3. The authors discuss trade-offs among utility, privacy, and computational efficiency in private relational learning.

S4. This paper is well-organized and easy to follow.

### Weaknesses
W1. While the paper addresses a general challenge—decoupling positive and negative relation sampling to enable privacy-preserving methods (i.e., DP-SGD)—the setting seems to be specific and trivial, involving aspects like LLMs, domain transfer, and cold-start (missing relations). It doesn’t clearly justify how the proposed sampling method would apply to the basic setting without more assumptions. For instance, it’s important to study whether the decoupled sampling method effectively supports privacy-preserving relational learning on the perspective of graph itself.

W2. The authors state in the introduction that current GNN methods fail to mitigate privacy risks in relational learning, yet it’s unclear how this extends to relational learning with LLMs. The reason "since many relational datasets involve entities with rich textual attributes" is not convincing. For example, with rich text, we could also encode it with LLMs and train graph ML models. Why is it necessary or what is the benefits to use LLMs to learn relations and to study privacy preserving specifically in this context?

W3. Regarding the random negative sampling mentioned in the last paragraph of Section 3.1, besides edge-based random sampling, another approach is to sample end nodes, which aligns with the approach discussed in the first paragraph of Section 3.2. This idea is thus not novel.

W4. (1) In negative sampling, it’s crucial to exclude positive edges. The authors state, “Note that this pairing strategy may generate negative relations (u, v) that are actually positive relations (u, v) ∈ E but with a low probability. Fortunately, our experiments show this does not obviously hurt the model performance.” However, this observation is based on empirical experiments limited to the specific setting. Also, whether the probability is low depends on the number of relations. Therefore, it is less rigorous to make this claim. Additionally, the impact of sampling positive edges as negatives can vary across cases.
(2) If positive relations are sampled as negatives, although “removing or adding a positive relation will change at most one tuple  $E_i$  in a mini-batch,” it could affect multiple message-passing steps or lead to conflict training signals, meaning that the sensitivity might not be bounded.
(3) On the other hand, if positive edges are excluded from the negative sampling, it cannot ensure that the perturbation of that positive relation impact at most one tuple, which still presents the challenge mentioned in Section 3.1. This point needs discussion in the paper.

W5. In Section 3.3, the authors mention limitations of two prior works, but there are more recent studies on efficiency with DP-SGD that should be reviewed and discussed to see if they apply to this relational learning context.

W6. Since entity features are usually also sensitive, this work is limited by considering only the privacy of relations, raising concerns about the privacy of features.

W7. The datasets (MAG and AMAZ) are small- and medium-scale. It would be better to include experiments on large-scale graphs.

W8. From the result tables, there are obvious performance drops comparing to the non-private preserving baselines.

W9. It would be better to also include empirical efficiency analysis.

### Questions
Q1. How would the decoupling sampling strategy apply to traditional graph ML methods?

Q2. This work aims to simulate common scenarios in relational learning, so why does it focus on domain transfer and missing relations in the new domain? How will it work when there exists domain shifts, and how well can relational learning transfer across domains? It would also be interesting to see performance evaluated on the same domain.

Q3. In real scenarios, the data is usually represented by heterogeneous graphs with multiple entity and relation types. How would the proposed pipeline work for such scenarios?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper works on improving the privacy on relational learning. Experiments on applying LLM for relational learning with lora and differential privacy show the performance.

### Strengths
1. Relational learning is an important topic.
2. DP-SGD can improve the privacy preservation during training.
3. Experiments show LLM can have good performance in relational learning.

### Weaknesses
1. Beside using DP-SGD+Lora for relational learning, the technical contribution is unclear.
2. Experiments did not compare with former GNN based methods.
3. The writing can be improved.

### Questions
As in weaknesses, the main concern is the technical contribution. What is the improvement of the proposed method over DP-SGD?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the potential privacy leakage issue in relational learning, where DP-SGD is not applicable since it violates the per-sample decoupling assumption. Rather than random or in-batch negative sampling, the authors propose to use a simple negative sampling strategy: pairing one end of the positive relation with entities uniformly sampled from the whole entity set, which is compatible with DP-SGD. The authors apply this method to privately fine-tune LLMs using real-world relational data as proof of concept.

### Strengths
1. The privacy issue in relational learning is an important research topic with a very broad impact.
2. This paper is generally well written and clearly organized.

### Weaknesses
1. The novelty of this paper is quite limited. The simple negative sampling solution proposed by the authors has already been widely used by many relational learning methods. This paper only contributes by highlighting its advantage in preserving privacy.
2. The technical quality of this paper is not good enough. The important privacy attack experiments are missing.

### Questions
1. Many relational learning methods already use the simple negative sampling strategy described in this paper. Most of them choose it because of its simplicity and efficiency. This paper merely highlights its advantage in preserving privacy when combined with DP-SGD. This seems to be the only innovation of this paper, which is inadequate.
2. The paper is missing some very important privacy attack experiments. The authors are advised to conduct membership inference attacks on different baselines (random/in-batch/proposed negative sampling with/without DP-SGD) and report the attack results. This can help validate whether the proposed negative sampling method indeed help DP-SGD in protecting relation privacy.
3. It is quite difficult to understand the difficulty of computing per-sample gradients for relational learning. Why must we first compute the gradients for individual entities (or even individual tokens) and then calculate the per-tuple gradients based on them? Why can't we just directly calculate the per-tuple gradients (which seems very simple in terms of programming)? It would be better if the authors could elaborate on this with more detailed explanations or figure illustrations.
4. In Table 4, why can the privately fine-tuned version sometimes outperform the non-privately fine-tuned baseline?
5. There are a few typos, such as
    1. Line 167: $e^{-}i_j$ should be corrected as $e^{-}_{i_j}$
    2. Line175-176: the Hinge loss formulation seems incorrect, it should be $[\gamma+\mathbf{z}_{e^{-}_{i_j}}-\mathbf{z}_{e_i^+}]_+$
    3. Line 292: "where $d$, $q$ are" should be corrected as "where $d$, $p$ are"

### Soundness
2

### Presentation
3

### Contribution
2
