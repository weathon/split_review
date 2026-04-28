# DINAR: Fine-Grained Privacy Preserving Federated Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Federated Learning (FL) enables collaborative model training among several participants, while keeping local data private at the participants' premises.However, despite its merits, FL remains vulnerable to privacy attacks, and in particular, to membership inference attacks that allow adversaries to deduce confidential information about participants' training data.
In this paper, we propose DINAR, a novel privacy-preserving FL method. DINAR follows a fine-grained approach that specifically tackles FL neural network layers that leak more private information than other layers, thus, efficiently protecting the FL model against membership inference attacks in a non-intrusive way. And in order to compensate for any potential loss in the accuracy of the protected model, DINAR combines the proposed fine-grained approach with adaptive gradient descent.The paper presents our extensive empirical evaluation of DINAR, conducted with six widely used datasets, four neural networks, and comparing against three state-of-the-art FL privacy protection mechanisms.The evaluation results show that DINAR reduces the membership inference attack success rate to reach its optimal value, without hurting model accuracy, and without inducing computational overhead. In contrast, existing FL defense mechanisms incur an overhead of up to +36% and +3,000% on respectively FL client-side and FL server-side computation times, and up to +168% on memory usage.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes DINAR, a privacy-preserving FL method to defend against Membership inference attacks in FL by specifically hiding FL neural network layers that leak more private information than other layers from the FL server in the aggregation step of FL. In order to compensate for any potential loss in the accuracy of the protected model, DINAR combines the proposed approach with adaptive gradient descent.

### Strengths
- The proposed approach is simple and easy to apply in real-world scenarios of FL settings.
- The proposed method can reduce the attack success rate of membership inference attacks while maintaining high model performance.
- Extensive empirical experiments are conducted for analytical insights and evaluations.

### Weaknesses
 - The privacy risk of Membership Inference Attacks is on the data-point level. Therefore, different data points will correlate to different neurons in different layers. As a result, the proposed method obfuscates a few layers and can not provide privacy protection for all data points in the clients' datasets.
- No guarantee is given for privacy protections.
- The considered attacks do not have high ASR in no defense models (e.g., 58% AUC in CelebA). Therefore, the defensive ability of the proposed method is degraded since it might be able to defend against weak attacks but not for stronger ones.

### Questions
1/ What is the attack success rate of the MIA on the vulnerable data points, i.e., the data points whose memberships are easy to infer?
2/ How does the proposed method deal with non-i.i.d problems in FL? Specifically, when the data is non-i.i.d, obfuscating multiple layers will incur a distribution shift between the client's local data and the data from other clients. 
3/ In Figure 6, why the model with no protection can have lower model performance compared to the model trained by the proposed method?
4. The size of the images is very small and hard to read. I suggest the authors make it more straightforward for the audiences.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a privacy-preserving method for FL, called  DINAR. Specifically, the paper presents an empirical analysis of how much each layer of a neural network leaks membership privacy information and identifies the most privacy-sensitive layer. Then, it proposes a fine-grained approach that obfuscates the most privacy-sensitive layer of the model, before sending it to the server for aggregation, and restores it at the client-side for personalization. It also adopts adaptive gradient descent for local training to improve the utility of the protected model. Finally, it evaluates DINAR with six datasets and four neural networks, and compares it with three FL privacy protection mechanisms. It shows that DINAR achieves effective privacy protection, without hurting model accuracy or inducing computational overhead.

### Strengths
- Originality: The proposed DINAR is new in its approach to obfuscating the most privacy-sensitive layer of the model before sending it to the server for aggregation, and restoring it at the client-side for personalization. 
- Quality: The quality of the paper is good in its thorough empirical analysis of layer-wise privacy characterization and obfuscation.  
- Clarity: The paper is well-written and clear in its presentation. The methodology is explained in detail, making it easy for readers to understand.
- Significance: By identifying and protecting the most privacy-sensitive layer of a model, DINAR can potentially help to advance FL techniques that balance privacy protection with model accuracy.

### Weaknesses
Novelty 
-  It would be helpful if the authors could provide a clear and explicit comparison between the proposed DINAR method and the layer-wise privacy characterization studied in FL by Mo et al. (2021). Discussing the differences, similarities, and potential advantages of DINAR over Mo et al. will enhance the reader's understanding of the novel contributions of the present study. Specifically, it's unclear if DINAR leverages the specific metrics proposed by Mo et al. or if it uses a different method to identify the most sensitive layer.

Related Work
- The literature review on DP & FL seems outdated, with references primarily from 2019 and 2020. Recent advancements have significantly improved the utility of DPFL algorithms. Therefore, it is recommended that the authors conduct a comprehensive review of the latest DP & FL algorithms,  such as [1,2,3,4]. It would be beneficial to include more recent techniques like those that focus on personalized DP or adaptive privacy budgets.

Clarifications: 
- Generalization Gap of the layers: “The generalization gap of the penultimate layer is notably higher than the generalization gap of the other layer” This conclusion about the “penultimate layer” could be specific to certain model architectures used in Figure 1.  Can the authors clarify the extent to which this claim holds true across diverse model architectures? It would be helpful to see an analysis across different types of neural networks (e.g., CNNs, RNNs, Transformers) and different depths.

- Adaptive Gradient Descent vs. Adam: Could the authors shed more light on why adaptive gradient descent exhibits superior convergence behavior compared to Adam?   “Given the high-dimensional nature of optimization problems in neural networks, this technique dynamically adjusts the learning rate for each dimension in an iterative manner.”  this statement holds not only for adaptive gradient descent but also for Adam. The authors should clarify the specific differences in the adaptation mechanisms that lead to the observed performance gains.


Baselines:
- Comparison to DP-based Techniques:  My concern is that the comparison to DP-based techniques in Section 4.4 Figure 4 might be unfair, as the specific $\epsilon$ used for DP methods is either undisclosed or excessively large. According to Section 5.1,  $\epsilon$ might be set to 2.2 for all DP-related experiments throughout the paper.  Note that DP, by definition, safeguards data privacy against membership inference attacks. The suboptimal empirical privacy performance of DP methods in Figure 4 could potentially be attributed to the utilization of a large privacy budget. It would be more convincing if the authors could evaluate MIA against DP methods under a small privacy budget. Furthermore, it would be useful to show the utility of DP methods under the same small privacy budget.
- Comparing the proposed method with recent DP & FL techniques, which have state-of-the-art  DP utility,  would strengthen the submission, which helps to highlight the advantages and unique contributions of the proposed method. This should include a comparison against methods that achieve a better utility-privacy trade-off than the basic DP baselines.

Experiments:
  - It is claimed that “leveraging adaptive gradient descent and, thus, further maximizing model utility”. However, there are no ablation studies or analyses verifying the effectiveness of adaptive gradient descent, compared to other optimization methods such as Adam and SGD. It is not clear if the observed performance is due to the specific adaptive method or simply better hyperparameter tuning.

  - The experimental setup appears to be overly simplistic, with only 5 clients considered for all datasets. This is contrary to the typical cross-silo and cross-device settings, which usually involve a significantly larger number of clients.  The authors should provide a rationale for choosing this specific number of clients and discuss the potential impact on the results if the number of clients were varied.
  - Additionally, partitioning the entire dataset among just 5 clients might result in each client possessing a sufficient quantity of data, thereby ensuring the local model is well-trained and potentially leads to memorization or overfitting phenomena for specific layers. It might be helpful to explore how the effectiveness of the proposed method under MIA attacks might be influenced by varying the number of clients, the size of local data, or the number of local training epochs. The authors should also analyze the impact of data heterogeneity across clients.
  - Some experiment details are not provided.  What is the number of local epochs for each FL client? How many FL rounds are trained for all methods? It is necessary to provide these details for reproducibility.
  - Model Architecture: “we consider the CelebA dataset with a model containing eight convolutional layers.” Does this mean that the authors trained a classification model exclusively using convolutional layers? There should be at least one fully connected layer to predict the class. The exact architecture details need to be provided for reproducibility.

Lack of theoretical guarantee:
- While the proposed method is insightful, it is primarily based on heuristics and lacks privacy guarantees. Consequently, It is possible that advanced membership inference attacks could compromise the proposed method, whereas DP, with a small $\epsilon$, is guaranteed to provide privacy preservation. The authors should acknowledge the limitations of a heuristic approach and discuss potential future directions to address this.

Typos:
-  There is a missing period in the  caption of Figure 1.

### Questions
Please see the questions in "Weaknesses".

### Soundness
3 good

### Presentation
3 good

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
The paper proposes DINAR, a method designed to enhance the privacy of Federated Learning (FL) systems, specifically guarding against membership inference attacks. DINAR employs a straightforward yet efficient fine-grained approach, focusing on protecting the most vulnerable model layer in terms of privacy. This approach ensures effective and non-intrusive privacy protection in FL. Additionally, DINAR addresses potential accuracy losses in the protected model by leveraging adaptive gradient descent, thus optimizing model utility.

### Strengths
1. This paper proposes a fine-grained defense against MIAs. The authors investigate the impact of MIAs on different layers and provide empirical insights about perturbing some specific layers rather than the whole model.

2. The authors conduct extensive experiments on multiple datasets.

### Weaknesses
1. The authors do not provide a theoretical privacy guarantee against MIAs. Without the theoretical guarantee, people cannot analyze the effectiveness and generalization of the proposed privacy defense method.

2. It is unclear how the server or the clients derive the sensitive layer, e.g., layer p. Do all the clients share the same sensitive layer even under non-IID settings? If the clients have different sensitive layers, how does Dinar solve the divergence problem of local model updates since the clients perturb different layers?

3. It is unclear which MIA methods Dinar is evaluated against in the paper. The author should claim the attack methods more explicitly.

4. It might be a good idea to shrink the scope of the title to "privacy against MIA" rather than general privacy-preserving FL.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an approach for protecting FL neural network layers that leak more private information. This approach is motivated by an observation (Mo et al.; 2021) that is there is a layer in neural networks that leaks more private information than other layers.

In order to compensating accuracy, adaptive gradient descent is used. The evaluation results show that the proposed idea reduces the membership inference attack success rate with good model accuracy.

### Strengths
+ The idea seems to be interesting.
+ The authors conducted extensive experiments for comprehensive analysis.

### Weaknesses
 - I have privacy concerns for other layers.
- The motivation seems interesting, but it is from an unpublished paper.
- There is no discussion of similar related works.
- The authors criticize differential privacy (DP) and cryptography in the related works. The authors said they are different and novel. However, given my understanding, the proposed idea is less secure than DP and cryptography-based works. I do not think the comparison is fair.
- The authors missed the discussion of similar related works in the same research direction.
- The author claims better model accuracy. I suspect it is from using adaptive gradient descent. If so, the improved utility is not from the newly-designed protection, i.e., not novel. Where is the high utility from?

### Questions
1. The authors aim to protect a specific layer in FL models. What are the privacy risks contained in other layers? I think this protection is insecure.
2. The motivation is from an unpublished paper. Are there any similar papers from reputable conferences/journals? I have great concerns about the reliable analysis of the motivation. Although we should care about both published and unpublished papers, I think it would be better for authors to find more support for their conclusive motivation.
3. the authors criticize differential privacy (DP) and cryptography in the related works. The authors said they are different and novel. However, given my understanding, the proposed idea is less secure than DP and cryptography-based works. I do not think the comparison is fair.
4. The authors missed the discussion of similar related works in the same research direction.
5. The author claims better model accuracy. I suspect it is from using adaptive gradient descent. If so, the improved utility is not from the newly-designed protection, i.e., not novel. Where is the high utility from?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
