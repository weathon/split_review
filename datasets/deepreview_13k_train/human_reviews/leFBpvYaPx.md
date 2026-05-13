# Adversarial Robustness of Graph Transformers

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Existing studies have shown that Message-Passing Graph Neural Networks (MPNNs) are highly susceptible to adversarial attacks. In contrast, despite the increasing importance of Graph Transformers (GTs), their robustness properties are unexplored. Thus, for the purpose of robustness evaluation, we design the first adaptive attacks for GTs. We provide general design principles for strong gradient-based attacks on GTs w.r.t. structure perturbations and instantiate our attack framework for five representative and popular GT architectures. Specifically, we study GTs with specialized attention mechanisms and Positional Encodings (PEs) based on random walks, pair-wise shortest paths, and the Laplacian spectrum. We evaluate our attacks on multiple tasks and threat models, including structure perturbations on node and graph classification and node injection for graph classification. Our results reveal that GTs can be catastrophically fragile in many cases. 
Consequently, we show how to leverage our adaptive attacks for adversarial training, substantially improving robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the robustness of Graph Transformers (GTs) against adversarial attacks, a relatively unexplored area compared to the vulnerabilities of Message-Passing Graph Neural Networks (MPNNs). The authors propose adaptive, gradient-based structure attacks targeting GT architectures and evaluate these attacks across different attention mechanisms and positional encoding methods. Their findings reveal that GTs can be highly vulnerable to adversarial attacks, similar to MPNNs. They further demonstrate that adversarial training effectively enhances the robustness of GTs, providing a defense mechanism against these vulnerabilities.

### Strengths
1.	The paper is the first to propose adaptive gradient-based attack strategies specifically for Graph Transformers (GTs), establishing a foundation for studying the adversarial robustness of GTs.
2.	The authors conduct multiple experiments across multiple tasks and threat models, demonstrating GTs’ performance under different attack budgets and highlighting their vulnerabilities to adversarial attacks.
3.	The authors propose an adversarial training strategy that reduces the hypersensitivity of some GT architectures, effectively enhancing their adversarial robustness and showing the potential of adversarial training in GTs.
4.	The paper is organized well, and the logic is smooth and convincing.

### Weaknesses
1.	The attack approach lacks generalizability and is overly empirical, requiring specific design adjustments for each model rather than presenting a systematic method or architecture, making it more of an empirical study than a universal solution.
2.	The effectiveness of the "adaptive attack" is questionable, as it does not significantly outperform grey-box attacks. Non-adaptive attacks without relaxation should have been included for comparison, and the baseline comparisons are limited to weak black-box attacks (random and transfer), which diminishes the impact of the results.
3.	The selection of baselines for both attacks and defenses is insufficient. The study lacks comparisons with established attack methods like Metattack and Nettack, as well as with more diverse defense strategies, such as other robust training techniques, graph cleaning methods, detection techniques, etc.

### Questions
1.	Could the authors include more attack and defense baselines?
2.	What is the performance of gradient-based attacks without relaxation?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work explores the adversarial robustness of five graph transformer (GT) models. The author designs adaptive gradient-based attacks on five GT models to poison the model’s node and graph classification performance. This work is the first to show that GTs are commonly vulnerable to adversarial attacks and proposes leveraging adversarial training to improve GTs’ adversarial robustness.

### Strengths
1. This paper establishes a good baseline for gradient-based adversarial attacks on graph transformers.

2. The work solves the problem of gradient-based structure attacks on GTs by introducing relaxation to attention scores.

3. The author has done explicit experiments on five graph transformers and types of attacks to validate the attack's effectiveness.

### Weaknesses
1. There are some typos and explanations which are not clear. For example, the last adjacency matrix symbol in Equation (6) should be \tilde{A} not A. The author may explain what ‘H’ means in equation (3) as it was not shown or explained before. Also, the author may clarify that the adjacency matrix ‘A’ in equation (2) is already self-looped. 

2. The author explains different types of GTs in detail in the background section. However, the author may also need to clarify whether the attack is aimed at degrading performance on training data, test data, or both, and to provide a formal definition of the attack loss function used in their experiments.

### Questions
1. Can the author provide concrete examples of potential real-world scenarios where these attacks might be relevant or impactful for each type of graph transformer discussed in the paper?

2. The author mentioned that the model output is discontinuous because positional encoding and attention mechanisms in GTs are designed for a discrete graph structure at the beginning of Section 3. Does this mean PEs and ATs are discontinuous because the adjacency matrix is discrete? Normally, the adjacency matrix becomes continuous values when you do the attack. Does this naturally solve the problem that PEs and ATs are discontinuous, so you do not need the relaxation on attention scores?

3. The author claimed in Principle II that the relaxed model function f shoule be continuous w.r.t continuous version of A. Can the gradient-based attack be conducted if it is continuous but not differentiated?

4. Can the author explain why introducing relaxation by adding the log of continuous edge probability to the attention score in equation (6) can solve the gradient problem? What’s the reason for this specific relaxation?

5. Is the method only adapted to PGD and PRBCD attacks? Has the author considered adapting it to other attacks like meta-attacks [1]? Can the author show some results?

[1] https://openreview.net/pdf?id=Bylnx209YX

### Soundness
3

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
This paper presents the first analysis of the adversarial robustness of Graph Transformers (GTs). The authors design adaptive gradient-based attacks for five representative GT architectures, including those with specialized attention mechanisms and Positional Encodings (PEs) based on random walks, pair-wise shortest paths, and the Laplacian spectrum. The results reveal that GTs can be catastrophically fragile to adversarial attacks, with even slight perturbations to the graph structure leading to significant performance degradation. Consequently, the authors show how to leverage their adaptive attacks for adversarial training, substantially improving the robustness of GT models.

### Strengths
- This is the first study on the adversarial robustness of Graph Transformers (GTs), which have become popular alternatives to Message-Passing Graph Neural Networks (MPNNs).
- The authors design adaptive gradient-based attacks for five representative GT architectures, including those with specialized attention mechanisms and Positional Encodings (PEs).
- The results show that GTs can be vulnerable to adversarial attacks, with even small perturbations to the graph structure leading to significant performance drops.
- The authors use their adaptive attacks to develop an effective adversarial training strategy that substantially improves the robustness of GT models.

### Weaknesses
 - The mathematical formulas in the paper seem to appear out of nowhere, lacking sufficient explanation and intuition. For instance, in Eq. (6) ($\hat{w} = w + \log{A}$), the paper does not explain why the log function is necessary. Does the log function have special properties here? Providing a theoretical analysis to explain why such a design could help adversarial attacks would be very beneficial. The same issue arises in Eq. (7) (8) (9) (10).
- In Figure (1b), the attack effect for Graph Transformer （Graphormer, GRIT, SAN）seems not to be very well. Under small budget (for example, 5%), the accuracy drops are not very much compared with Figure (1a) and (1d). Could the author provide a further explanation?
- The writing is so confusing and needs to be improved. For example, the author directly use $deg(v_i)$ in Eq. (7) without any definition.
- The experiment setting has some problems. First, this paper lacks adversarial attack baselines. They should include both typical adversarial attacks and adversarial attacks for graphs. There should be many existing works, like [1, 2].
- If the authors want to validate the effectiveness of adversarial training, they should also compare it with typical graph adversarial defense methods, like [3]. In total, the experiments of this paper are obviously insufficient.
- The clarification of the experiment setting is also confusing. The authors list three different attack methods, but I cannot tell which one is proposed by this paper.

### Questions
The same as the weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This abstract discusses the vulnerability of Graph Transformers (GTs) to adversarial attacks, contrasting them with Message-Passing Graph Neural Networks (MPNNs), which are known to be susceptible. Despite GTs' growing importance, their robustness is underexplored. The authors design adaptive attacks specifically targeting GTs by creating gradient-based attacks focused on structural perturbations. They evaluate these attacks across five popular GT architectures, examining how GTs handle attention mechanisms and positional encodings (PEs). Results indicate that GTs are extremely fragile in many scenarios. To address this, the study also explores how adaptive attacks can inform adversarial training to enhance robustness.

### Strengths
1. This work provides an adaptive gradient-based structure attacks for GTs.
2. This work is the first to study the adversarial robustness of graph transformers
3. The presentation and writing are very clear and convincing

### Weaknesses
1. The main weakness of this paper is the limited contribution. The adaptive attack is specifically designed for a particular defense, which limits its generalizability. It would be a significant improvement if the adaptive attacks could share a generalizable principle across all GTs.

2. As shown in the experiments, the relaxation technique is ineffective, and the adaptive attack is not strong enough. In Figures 3, 4, 5, and 6, there are many cases where the adaptive attack is weaker than the transfer attacks. In the ablation study (Tables 1,2 and 3), relaxing the non-differentiable operator does not achieve a better attack in some cases and only provides minimal improvement in others. Additionally, the experiments do not compare results with non-adaptive gradient-based attacks. As noted in the paper, "A good approach might be to
try all individually as an ensemble and choose the strongest. " This work, however, appears highly incremental and lacks universality. All of these findings raise concerns regarding the effectiveness of the proposed method.

3. The attack baselines are limited; the experiments only compare transfer attacks and random attacks, which is insufficient. Furthermore, the adaptive attacks do not seem stronger than the transfer attacks. Additional baselines, including metattack and nettack, should be incorporated.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1
