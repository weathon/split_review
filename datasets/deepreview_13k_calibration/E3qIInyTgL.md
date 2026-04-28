# CC-VFed: Client Contribution Detects Byzantine Attacks in Vertical Federated Learning

- Decision: Reject
- Avg Score: 3.33
- Scores: 1, 6, 3

## Abstract
Vertical federated learning (VFL) is a type of federated learning where the collection of different features is shared among multiple clients, and it is attracting attention as a training method that takes into account the privacy and security of training data. On the other hand, in federated learning, there is a threat of Byzantine attacks, where some malicious clients disrupt the training of the model and output an trained model that does not exhibit the behavior that should be obtained. Thus far, numerous defense methods against Byzantine attacks on horizontal federated learning have been proposed, most of which focus on the similarity of the models generated across clients having the similar features and mitigate the attacks by excluding outliers. However, in VFL, the feature sets assigned by each client are inherently different, making similar methods inapplicable, and there is little existing research in this area. In light of the above, this paper organizes and classifies feasible Byzantine attacks and proposes a new defense method CC-VFed against these attack methods. Firstly, this paper organizes and classifies attack methods that contaminate training data, demonstrating that sign-flipping attacks pose a threat to VFL. Subsequently, in order to capture the differences in client features, this paper proposes a method for detecting and neutralizing malicious clients based on their contribution to output labels, demonstrating that it is indeed possible to defend Byzantine attacks in VFL.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper compares three Byzantine attack methods in Vertical Federated Learning, demonstrating that the sign-flipping attack exhibits the highest effectiveness.  Based on the attack, they propose a new defense method CC-VFed to identify the malicious client. The proposed method's efficacy is evaluated through experiments on the BCW and CIFAR-10 datasets.

### Strengths
Developing Byzantine attacks in the VFL context is an important topic, and has received limited attention so far.

### Weaknesses
1. Limited novelty. The investigated Byzantine attack methods, particularly sign-flipping [1], have been extensively studied in previous research. The authors could have enhanced the scope by incorporating other relevant adversarial attacks in VFL [2,3]. Additionally, the gradient contribution-based defense mechanism bears significant similarities to existing approaches [4].

2. The proposed defense methodology raises concerns regarding VFL protocol compliance and privacy preservation. Specifically, Step 1 of the defense mechanism requires clients to share training data $x_i$ with the central server, which compromises data privacy. Furthermore, the aggregation process of Grad-cam values needs clarification, particularly regarding the distinction between multiple nodes versus single node scenarios. The defense computation would benefit from more rigorous mathematical formulation.

3. The experimental evaluation could be more comprehensive. The current validation relies on two relatively simple datasets (BCW and CIFAR-10), which may not fully demonstrate the method's robustness across diverse scenarios. The absence of ablation studies limits our understanding of each component's contribution to the overall system performance.

### Questions
See Weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article organizes and classifies Byzantine attacks, and proposes a new defense method CCVFed for these attack methods. Firstly, it has been proven that flipping symbol attacks pose a threat to VFL. Subsequently, in order to capture the differences in client features, this paper proposes a method for detecting and neutralizing malicious clients based on their contribution to output labels, proving that it is indeed possible to defend against Byzantine attacks in VFL.

### Strengths
1. The article proposes a new defense method CC-VFed, which utilizes the contribution of each client to the output label to counter Byzantine attacks.
2.   The article has verified through extensive experiments that flipping symbol attacks are threatening.
3.    In the background section, the author delves into the research question layer by layer. The outlier detection methods used in HFL scenarios are not sufficient for VFL, and there are deficiencies in the existing methods in VFL. Thus presenting the challenge of this article.
4.   This study used real-world datasets such as BCW and CIFAR10 to evaluate the effectiveness of defense methods. And the article studied the differences in using this method on different datasets.

### Weaknesses
 1. Although the method is easy to understand, the author can better discuss the novelty of the proposed mechanism.
  2. The author should conduct a more detailed analysis of the method, identify its limitations, and make improvements.
  3. What are the unique advantages of our method compared to existing methods in other VFLs?
  4. The method lacks some key descriptions, making it difficult for people to understand

### Questions
1. Novelty: The novelty of the proposed method is unclear from the paper. For example, the core of the CC-VFed method mentioned in the contribution lies in the calculation of contribution degree. The author's description of two targeted improvements (Selvaraju et al., 2017) did not clearly state the effectiveness and necessity of the author's improvements. I think this needs to be strengthened. The method proposed by the author does have some practicality, but the method itself is too simple and cannot solve some key problems. For example, who will determine whether the output label matches the label of the training data? Did the author not explain this crucial issue in the methodology? If the client is to perform this critical operation, how can we prevent the client from doing evil and disrupting the correctness of the match? On the contrary, if the server executes it, then the privacy information of the data label is known by the server. How to ensure the user privacy of federated learning? These are the issues that the author needs to focus on. But I greatly appreciate the author's research on the challenges presented in this article, such as determining the most severe challenge through detailed experiments - the sign-ﬂipping attacks.
  2. Related work: What are the unique advantages of this method compared to existing methods in other VFLs? The author lacks a description and comparison of the shortcomings in other VFL methods, and does not highlight the unique advantages of the method proposed in this article, which can solve problems that cannot be solved by other methods. I think the author should add some state-of-the-art comparative literature for detailed comparison.
  3. Method: In addition to the security issues of the proposed method, some steps in the method are also confusing. For example, who will determine if the output label matches the label of the training data? The calculation formula for contribution degree lacks more description. The four defense methods proposed are actually four different situations within one defense method, which are not the four defense methods claimed by the author.
  4. Evaluation: Although the author conducted extensive experiments from various perspectives, their method did not compare with the most advanced existing methods. In addition, the author did not provide clear explanations in the experimental setup. For example, what is the experimental environment? How many experiments did the author conduct? Is the difference in results statistically significant?
  5. Organization and Writing: It is recommended that the author add some graphics to describe the proposed method, so that readers can clearly understand: which entities are there? What operations did each entity perform? What are the unique meanings behind each operation? In addition, the key standard of "Top-1 accuracy" has not been explained.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the author proposed CC-VFed to detect and neutralize malicious clients in the setting of vertical federated learning. In general the malicious clients are recognized based on how much it contributes to mislead the VFL model into making wrong predictions. Experiments are done on 2 datasets with a limited setting in which one and only one party is malicious. The effectiveness of the proposed method is verified for defending against sing-flipping byzantine attacks for VFL.

### Strengths
To verify the effectiveness of the proposed defense method, a strong byzantine attack for VFL, sign-flipping attack, is first proposed and demonstrated to be quite effective in harming the performance of a VFL system. Also, studies on what kind of model architectures is more robust to attacks and helps in boosting the defense capability is also conducted which is quite interesting.

### Weaknesses
1. Why should $c$ be close to one? Since this argument lacks analysis or supporting work reference, it sounds really weird.
2. Experiments are not adequate, only 2 datasets are used. Besides, the setting that only one party is malicious makes the experiment and the detection of malicious party relatively easy, which could not demonstrate the effectiveness of the proposed malicious party recognition method. To what extent can this defense safeguard VFL from Byzantine attack when the number of malicious parties is unknown is not demonstrated which is a very important setting that close to real world setting.
3. I doubt the effectiveness and design of the proposed method, since when the defense is applied to defend against random/permutation attacks, the Top-1 accuracy often drop compared to without defense setting. So, the defense acks like a “stronger attack” which is not acceptable.

### Questions
If the authors could explain clearly why the problem I mentioned in Weakness 3 occurs and why the proposed defense is not "a stronger attack" itself, I will consider raising my score.

### Soundness
2

### Presentation
3

### Contribution
2
